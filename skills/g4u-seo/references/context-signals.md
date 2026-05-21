# Context Signals — qué buscar en el contexto cliente

Cuando el usuario me da una ruta/archivos/IDs de Notion al arrancar, leo todo y extraigo estas señales orientativas.

**No es un schema impuesto** — el usuario tiene su propia forma de capturar contexto. Esto es solo guía de qué información me sirve si está disponible. Si no está, sigo y pregunto cuando bloquee.

## Señales mínimas (sin estas, pregunto)

| Señal | Por qué la necesito | Si falta |
|-------|---------------------|----------|
| **Dominio del sitio** | Sin esto no puedo auditar nada | Pregunto explícitamente |
| **Cliente slug** | Path del output `OUTPUTS/<cliente>/...` | Infiero del host del dominio |

## Señales útiles para audit

| Señal | Para qué | Si falta |
|-------|----------|----------|
| **Sector / vertical** | Decide branch del decision tree (SaaS / ecom / local / publisher) | AgriciDaniel `/seo audit` auto-detecta — uso eso |
| **Mercados objetivo** | Decide si activar `/seo hreflang` | Default: assume mercado único = idioma principal de la web |
| **Idioma principal** | Selección de tools (DataForSEO location, GSC region) | Detecto del `<html lang="">` |
| **GSC property URL** | Acceso a datos reales | Sin GSC, TopRank skill degrada con aviso |
| **DataForSEO location code** | Volume + KD precisos por geo | Default: usar location_code = 2840 (US) si no especifica |

## Señales útiles para creación de páginas

| Señal | Para qué | Si falta |
|-------|----------|----------|
| **ICP / buyer persona** | Brand-voice + copy hooks | Pregunto si genera brief; salto si solo audit |
| **JTBD del usuario** | Estructura del contenido (sección "Cómo / pasos") | Genero genérico, aviso al usuario |
| **Producto: features + diferenciador + precio** | Comparison pages y sección "next step" | Genero placeholders, aviso |
| **Competidores** | SERP analysis tiene contexto | Detecto del SERP top 10 |
| **Brand voice / tono** | Si existe en el contexto, uso `brand-voice` skill | Default neutro profesional |
| **Keywords core ya identificadas** | Acelera Fase 1 keyword expansion | Hago expansion completo desde seed |

## Señales útiles para GEO/AI

| Señal | Para qué | Si falta |
|-------|----------|----------|
| **Brand mentions actuales** (si existe tracking) | Baseline para mejora | No bloquea, lo creo |
| **Plataformas off-page activas** (Reddit, YouTube, Medium del cliente) | Plan GEO off-page | Asumo greenfield |
| **Author bios establecidas** | E-E-A-T quick wins | Recomiendo crearlas si faltan |

## Señales operativas G4U

| Señal | Para qué | Si falta |
|-------|----------|----------|
| **Owner del proyecto en Notion** | Si pide sync, sé quién va en la task | Default: Alfonso |
| **Convención de output específica del cliente** | Algunos clientes prefieren ruta distinta | Default `OUTPUTS/<cliente>/...` |
| **Notion task parent** | Si el cliente tiene su own sub-DB en Notion | Default DB Tasks & Projects |

## Heurística de extracción

Cuando leo los archivos/páginas:

1. **Busco encabezados** que sugieran las señales arriba (sin importar el formato exacto: markdown, YAML, prosa)
2. **Cito la fuente** cuando uso una señal: "según `clients/sancho/foundation/icp.md` el ICP es X"
3. **Si dos fuentes contradicen**: pregunto al usuario cuál vale
4. **Si una señal está incompleta**: la marco como `<incompleta>` y sigo, pregunto cuando bloquee
5. **NO escribo nada de vuelta** al contexto del cliente. Es read-only desde la skill

## Ejemplo de uso

Usuario: `/g4u-seo-audit https://client-site.example.com`

Contexto previamente apuntado: `clients/<your-client-slug>/`

Yo leo:
- `client-example/foundation/positioning.md` → sector, ICP, JTBD, competidores
- `client-example/foundation/voice.md` → tono brand
- `client-example/seo/2026-04-22-full-audit.md` → audit previo, baseline
- `client-example/foundation/markets.md` → ES + LATAM, idiomas

Extraigo:
- Cliente slug: `client-example` ✓
- Dominio: `client-site.example.com` ✓
- Sector: fintech / pasarela pagos ✓
- ICP: PYMEs en sectores regulados ✓
- Mercados: ES + LATAM → activar `/seo hreflang` ✓
- Idioma: español
- DataForSEO location: usar 2724 (Spain) + 2484 (Mexico) + 2076 (Brazil)
- Audit previo existe → comparar resultados vs. baseline

Si falta `markets.md` → asumo mercado único España, lo digo en el output.
