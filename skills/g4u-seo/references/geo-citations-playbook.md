# GEO Citations Playbook

Doctrina G4U para hacer que el contenido del cliente sea **citado** por LLMs (no solo rankeado en Google). Es complemento, no sustituto, de SEO clásico.

## Por qué GEO no es opcional en 2026

- AI traffic convierte 4.4x-23x más que organic ([`bibliography-tactics.md` §1.2](./bibliography-tactics.md))
- Volumen AI crece mientras orgánico se erosiona por AI Overviews (zero-click)
- Aunque el cliente sea fuerte en SEO clásico, si no está optimizado para GEO pierde la conversión más rentable

## Diferencia clave SEO vs GEO

| Aspecto | SEO clásico | GEO |
|---------|-------------|-----|
| Goal | Rankear pos 1-3 | Ser citado en respuesta del LLM |
| Optimization unit | Página | Passage / sección |
| Signal stack | Backlinks, on-page, CWV | Authority + structure + freshness + entity velocity |
| Measurement | GSC clicks/impressions | Profound/Amplitude citation count |
| Latency | 3-6 meses | 30-90 días según plataforma |

## On-page: cómo hacer cada passage citable

### Estructura de 5 secciones obligatoria

Ver [`page-creation-playbook.md` Fase 3](./page-creation-playbook.md). Resumen de por qué:
- Testeado en ChatGPT, Perplexity, Claude — sweet spot de 5 (no 3, no 7)
- Cada H2 con un **summary statement** al inicio (1-2 frases) que el LLM pueda citar literalmente
- Cada H2 con un **dato numérico concreto** (año, %, $) mejora citation likelihood

### FAQ schema markup

Critical. Las FAQ schema son citadas con frecuencia 3-5x mayor que texto sin schema:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "¿Pregunta exacta como la formularía el usuario?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Respuesta directa, 50-100 palabras. Empieza con la conclusión, después justifica."
      }
    }
  ]
}
```

### Lenguaje declarativo, no marketing

LLMs prefieren texto factual a copy promocional:
- ✅ "El método X reduce CAC en 40% según un estudio de Y"
- ❌ "Nuestra solución revolucionaria transforma tu negocio"

### Citations externas

2-3 enlaces a fuentes autoritativas por sección:
- Papers (arxiv.org, Google Scholar)
- Sitios .gov / .edu
- Empresas reconocidas en el nicho (no competidores directos)
- NUNCA inventar fuentes — los LLMs verifican

## Off-page: dónde construir señal LLM

### Plataformas top según peso en LLM citations

| Plataforma | Por qué LLMs la valoran | Estrategia |
|------------|------------------------|------------|
| **Reddit** (posts >6 meses) | Authoritative according to crawl data | Workflow 6-step ([`bibliography-tactics.md` §5](./bibliography-tactics.md)) |
| **YouTube B2B** | Influye más en LLMs de lo esperado | Videos con transcripts, descripciones largas |
| **Medium** | Sigue siendo plataforma alta señal | Republish con canonical hacia tu sitio |
| **LinkedIn Articles** | 89K URLs analizadas — peso confirmado (SemRush) | Articles largos (1500+ palabras), no posts |
| **GitHub READMEs** | Alta autoridad técnica | Solo si producto open-source o developer |
| **HuggingFace** | Si AI/ML | Model cards + datasets |
| **Stack Overflow** | Si dev-related | Respuestas validadas |

### Reddit workflow (6-step) — del playbook bibliografía

Para clientes con tiempo/recursos para construir presencia:

1. **Identificar subreddits** relevantes — mínimo 5-10
2. **Construir karma** durante 2-3 semanas — comentarios de valor, no promo
3. **Responder con valor** en threads existentes alineados con queries target
4. **Usar mismas palabras clave** que las queries que quieres rankear en LLMs
5. **Crear posts propios** con estructura de respuesta (no marketing)
6. **Repurposar** respuestas top en otros canales (LinkedIn, blog del cliente)

**Riesgo**: si lo automatizamos demasiado se detecta y banean. Debe haber humano en loop. NO auto-ejecutar.

### Press releases + listicles (especialmente local)

Innovación 2026: AI search local cita listicles para queries tipo "best [service] in [city]".

Estrategia:
- Pitch a publicaciones locales del nicho del cliente
- Aparecer en listicles "top X [vertical] companies"
- Press release distribution (PRNewswire si presupuesto, alternativas free para casos low-budget)

## Citation tracking — cómo medir

Tres opciones, según presupuesto:

| Tool | Costo | Capability |
|------|-------|------------|
| **Profound** | Pago | Tracking dedicado de menciones LLM por query |
| **Amplitude** | Tiered | AI citation analytics integrado con producto |
| **DataForSEO `ai_opt_llm_ment_*`** | Pay-per-use | API: search mentions, top domains, agg metrics — endpoints disponibles via MCP ya instalado |

Para clientes G4U: empezar con **DataForSEO** (ya pagado). Solo escalar a Profound si el cliente justifica budget dedicado.

### Setup DataForSEO citation tracking

Endpoints relevantes:
- `ai_opt_llm_ment_search` — buscar menciones específicas
- `ai_opt_llm_ment_top_domains` — qué dominios son citados más
- `ai_opt_llm_ment_top_pages` — qué páginas concretas son citadas
- `ai_opt_llm_ment_agg_metrics` — métricas agregadas
- `ai_opt_llm_ment_cross_agg_metrics` — cross-LLM comparison

**Setup mensual**: cron que ejecuta queries para top 10-20 brand keywords + competitor keywords. Tracking de citation share over time.

## GEO playbook por tipo de cliente

### SaaS B2B

- Foco en **comparison pages** ("X vs Y") y **alternatives pages** — alta citation rate en queries comerciales
- Documentation pages con FAQ schema — citadas en queries informacionales
- Case studies con números concretos — alta citation likelihood
- LinkedIn Articles del CEO con thought leadership

### E-commerce

- Product schema riguroso (Product + AggregateRating + Offers)
- Reviews integradas con UGC schema
- Listicles ("Best X for Y") via partnerships con publishers
- Reddit subreddits del nicho del producto

### Local services

- GBP optimization 100% + posts semanales
- Press releases en publicaciones locales
- Listicles "best [service] in [city]"
- Reddit r/[city] threads donde aparezcan recomendaciones del nicho

### Publishers / Content sites

- Author bios robustas con E-E-A-T signals
- Multi-source citation (cite y sé citado por papers, otros publishers)
- Fresh content cadence — algoritmos LLM valoran freshness
- HTML estructurado limpio (no markdown rendered, no infinite scroll)

## Anti-patterns — qué NO hacer

- **Fabricar citas o datos**: el paper de Princeton GEO 2023 mostró que funcionaba contra GPT-3.5. Pero (a) los modelos 2026 detectan, (b) penaliza confianza brand, (c) éticamente inaceptable
- **Keyword stuffing**: contraproducente en GEO. LLMs prefieren densidad natural
- **Walls of text**: cada section >500 palabras se cita menos. Mejor secciones de 200-400
- **Marketing fluff**: "revolutionary", "game-changing", "best-in-class" — los LLMs descartan ese registro
- **Schema JS-injected si el sitio depende del crawl AI**: muchos LLM bots no ejecutan JS. Server-render schema crítico

## Verificación GEO post-implementación

A los 30/60/90 días:
- [ ] Track citation count en DataForSEO `ai_opt_llm_ment_search` para queries target
- [ ] Brand mentions en respuestas ChatGPT/Perplexity para queries informacionales del nicho
- [ ] FAQ schemas correctamente parseados (verificar en Search Console rich results report si Google AIO)
- [ ] Páginas con 5-section structure rankean mejor en AI Overviews vs no-structure
