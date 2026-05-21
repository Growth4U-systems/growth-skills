#!/usr/bin/env python3
"""
Page brief generator — convierte SERP data + keyword en brief estructurado.

Usage:
    python3 page-brief-generator.py --keyword "<kw>" --serp-data <path-to-serp.json> --output <path.md>

Recibe un JSON con SERP data (top 10 + content gaps) y produce un brief markdown
con estructura de 5 secciones + FAQ schema según doctrina G4U.

Este script genera la PLANTILLA. El contenido real se rellena en Claude session
después usando el contexto cliente y la skill ai-seo/direct-response-copy.
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import date


BRIEF_TEMPLATE = """# Brief SEO — {keyword}

**Cliente**: {cliente}
**Keyword head**: {keyword}
**Intent**: {intent}
**Volume**: {volume} | **KD**: {kd} | **CPC**: ${cpc}
**Fecha**: {fecha}

---

## SERP analysis (top 10)

{serp_table}

### Content gaps detectados

{gaps}

---

## Estructura recomendada — 5 secciones + FAQ

> Doctrina G4U: 5 secciones es el sweet spot empírico (mejor que 3 o 7). FAQ schema obligatorio.

### H1 sugerido
**{h1_suggestion}**

### Hook (50-80 palabras)
_[Problem statement + promesa de solución. Rellenar usando contexto ICP del cliente.]_

### H2 Sección 1 — [Pain point / contexto] (200-300 palabras)
_[Identificar el pain point específico para el ICP. Incluir un dato externo (citar fuente real).]_

- Bullet concreto 1
- Bullet concreto 2
- Bullet concreto 3

### H2 Sección 2 — [Definition / framework] (200-300 palabras)
_[Definir el concepto/framework. Esquema visual recomendado aquí.]_

### H2 Sección 3 — [Cómo / proceso / pasos] (300-500 palabras)
_[Lista numerada 5-7 pasos con sub-bullets de detalle.]_

1. Paso 1
   - Sub-bullet
2. Paso 2
   - Sub-bullet

### H2 Sección 4 — [Examples / case studies] (200-400 palabras)
_[2-3 ejemplos concretos. Ideal: del propio cliente.]_

### H2 Sección 5 — [Action / next step] (150-250 palabras)
_[CTA claro + link al producto / siguiente paso del funnel.]_

---

## H2 Frequently asked questions

_[5-8 Q/A pairs. Cada respuesta 50-100 palabras. Empieza con conclusión, después justifica.]_

**Q1: ¿Pregunta exacta como la formularía el usuario?**
R: ...

**Q2: ¿Pregunta 2?**
R: ...

(continuar hasta 5-8 pares)

---

## FAQ Schema JSON-LD (copy-paste al `<head>`)

```json
{faq_schema}
```

---

## On-page checklist

- [ ] Title tag 55-60 chars con keyword head
- [ ] Meta description 150-160 chars con CTA
- [ ] H1 contiene keyword head
- [ ] 5 H2 según estructura
- [ ] Internal links: 3-5 contextuales
- [ ] External links: 2-3 a fuentes autoritativas (no inventadas)
- [ ] Imágenes con alt text descriptivo + nombre kebab-case
- [ ] Schema JSON-LD validado en https://search.google.com/test/rich-results
- [ ] No keyword stuffing (densidad < 2%)

## GEO checklist post-publicación

- [ ] Cada H2 empieza con summary statement de 1-2 frases
- [ ] Cada sección incluye al menos 1 dato numérico concreto
- [ ] Lenguaje declarativo (no marketing fluff)
- [ ] FAQ schema deployado y validado
- [ ] Tracking citation setup en DataForSEO (`ai_opt_llm_ment_search`)
- [ ] Re-check citation count a 30/60/90 días
"""

DEFAULT_FAQ_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "Pregunta 1",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Respuesta 1 — 50-100 palabras."
            }
        }
    ]
}


def format_serp_table(serp_top10):
    if not serp_top10:
        return "_(no SERP data provided)_"
    rows = ["| # | Title | URL | Words | Schema |", "|---|-------|-----|-------|--------|"]
    for i, item in enumerate(serp_top10[:10], 1):
        title = item.get("title", "?")[:60]
        url = item.get("url", "?")
        words = item.get("word_count", "?")
        schema = item.get("schema_detected", "?")
        rows.append(f"| {i} | {title} | {url} | {words} | {schema} |")
    return "\n".join(rows)


def format_gaps(gaps_list):
    if not gaps_list:
        return "_(no gaps provided)_"
    return "\n".join(f"- {g}" for g in gaps_list)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--keyword", required=True, help="Keyword head")
    parser.add_argument("--cliente", default="<cliente>", help="Cliente slug")
    parser.add_argument(
        "--serp-data",
        default=None,
        help="Path to JSON con SERP top10 + gaps. Opcional.",
    )
    parser.add_argument("--output", required=True, help="Output markdown path")
    args = parser.parse_args()

    serp_top10 = []
    gaps_list = []
    intent = "<por determinar>"
    volume = "?"
    kd = "?"
    cpc = "?"

    if args.serp_data and Path(args.serp_data).exists():
        with open(args.serp_data) as f:
            data = json.load(f)
        serp_top10 = data.get("top10", [])
        gaps_list = data.get("gaps", [])
        intent = data.get("intent", intent)
        volume = data.get("volume", volume)
        kd = data.get("kd", kd)
        cpc = data.get("cpc", cpc)

    brief = BRIEF_TEMPLATE.format(
        keyword=args.keyword,
        cliente=args.cliente,
        intent=intent,
        volume=volume,
        kd=kd,
        cpc=cpc,
        fecha=date.today().isoformat(),
        serp_table=format_serp_table(serp_top10),
        gaps=format_gaps(gaps_list),
        h1_suggestion=args.keyword.capitalize(),
        faq_schema=json.dumps(DEFAULT_FAQ_SCHEMA, indent=2, ensure_ascii=False),
    )

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(brief, encoding="utf-8")
    print(f"Wrote {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
