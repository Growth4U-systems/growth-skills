# Bibliography Tactics — SEO + GEO

Síntesis de 87 entradas SEO en `bibliography-1395dacf-4f14-81de-801f-dee0678dc51e` (Notion). Dump completo en [`_bibliography-raw.md`](./_bibliography-raw.md).

Aquí solo las tácticas accionables que **no están** o están **mal cubiertas** por las skills instaladas (AgriciDaniel `/seo`, Corey Haines, TopRank).

---

## 1. AI Search / GEO — tácticas verificadas

### 1.1 Estructura de 5 secciones + FAQ schema
**Fuente**: ["15 hacks to rank #1 in AI answers"](https://telepathic.notion.site/15-hacks-to-rank-1-in-AI-answers-tested-across-ChatGPT-Perplexity-Claude-2eacfb4e815c804296c5f7b2a5ccb442) (2026-01-17). Testado en ChatGPT, Perplexity, Claude.

- **Artículos con 5 secciones principales** se citan más que los de 3 o 7 (sweet spot)
- **FAQ schema markup** sube tasa de citación de forma significativa
- **Summaries estructurados** al inicio del artículo (TL;DR de 3-5 bullets) facilitan extracción por LLM
- **Publishing cadence consistente** mejora indexación AI

Aplicar en: `page-creation-playbook.md` (Fase 3 brief: imponer 5 secciones + FAQ schema obligatorio).

### 1.2 AI traffic convierte 4.4x-23x más que organic
**Fuente**: ["AI Search Disrupts Google's Traffic"](https://x.com/milliemarconnni/status/2034571397901815829) (2026-03-19), ["Boost Your SEO with AI: 100 days"](https://x.com/denohawari/status/2051631168567885892) (2026-05-06).

- Conversión AI vs SEO orgánico: **4.4x-23x más alta** (rango según vertical)
- Aunque tráfico bruto sea menor, **valor por sesión es mucho mayor**
- Justificación para invertir en GEO incluso si volumen AI es 10% del orgánico

Aplicar en: Sintesis de auditoría (priorizar quick wins GEO sobre tácticas SEO clásicas si volumen GSC es bajo).

### 1.3 Plataformas con peso en LLM citations
**Fuente**: ["Optimizing LLM Mentions with GEO Strategy"](https://www.linkedin.com/posts/andrewwarner_my-friends-company-is-recommended-by-chatgpt-activity-7437544982380429312) (Andrew Warner, 2026-03-12), ["Achieving Top 5 AI Visibility in 90 Days"](https://www.youtube.com/watch?v=QTorh2RXX28) (Julian Goldie).

- **Reddit (posts antiguos > 6 meses)** muy valorados por LLMs
- **YouTube B2B** influye en respuestas LLM más de lo esperado
- **Medium** sigue siendo plataforma alta señal para visibility
- **LinkedIn URLs**: análisis de 89K URLs citadas en AI Search (SemRush, 2026-03-15) confirma peso

Aplicar en: `geo-citations-playbook.md` (sección "off-page" recomendar Reddit + YouTube + Medium como parte del playbook).

### 1.4 Herramientas tracking de AI citations
**Fuente**: Andrew Warner LinkedIn post (2026-03-12).

- **Profound** — tracking de menciones LLM
- **Amplitude** — citation metrics
- **DataForSEO `llm_mentions` endpoints** (ya disponible en MCP instalado)

Aplicar en: `stack-map.md` (cuando usuario pide tracking AI, mencionar las 3 opciones).

---

## 2. NotebookLM como herramienta SEO (no auditada por skills instaladas)

**Fuente**: ["Boost Your SEO with NotebookLM"](https://x.com/juliangoldieseo/status/2007507268259164389) + ["Transform NotebookLM into a Powerful SEO Content Tool"](https://x.com/juliangoldieseo/status/2008530329234272651) (Julian Goldie, ene-2026). Más entradas: ["Revolutionizing SEO with NotebookLM and Gemini 3"](https://www.notion.so/Revolutionizing-SEO-with-NotebookLM-and-Gemini-3) (Walid Boulanouar).

Workflow:
1. Subir **top 10 páginas Google** del SERP target a NotebookLM
2. Pedir: keyword clusters + FAQ list + schema markup recommendations
3. Generar brief estructurado en minutos
4. Opcional: convertir a video script (NotebookLM v2 con Gemini 3)

NotebookLM maneja hasta **1M tokens** — caben fácil 20-30 páginas competidoras.

Aplicar en: `page-creation-playbook.md` (Fase 2 SERP analysis: NotebookLM como alternativa rápida a la combinación `/seo competitor-pages` + DataForSEO MCP).

---

## 3. Programmatic SEO arquitectura a escala

**Fuente**: ["Scalable Programmatic SEO Architecture for 100k+ Pages"](https://x.com/kalashbuilds/status/2012409234990973284) (Kalash, 2026-02-15), ["Creating 10,000 SEO Pages with Claude Code in 48 Hours"](https://x.com/roundtablespace/status/2041240776726700535) (2026-04-07), ["I built 3,200 pages"](https://mail.google.com/mail/u/0/#inbox/19de09f65bc55de6) (James/Boring Marketer, 2026-05-01).

Principios críticos:
- **Separar concerns en sistemas distintos**: template engine, data layer, schema generator, internal linking generator, sitemap publisher
- **Hub-and-spoke model** obligatorio para internal linking
- **Dynamic metadata** + **structured data** por variante (no copy-paste)
- **Content uniqueness mínimo 200-300 palabras** únicas por variante (más allá del template)
- **Evitar thin content** y **keyword cannibalization** — risk #1

Aplicar en: `cluster` workflow + nuevo apartado en `page-creation-playbook.md` para programmatic.

---

## 4. Quick wins de auditoría con AI + GSC (los que más rinden)

**Fuente**: ["Boost SEO Rankings with AI in Under 30 Minutes"](https://www.linkedin.com/posts/akash-sehgal-25241b221_huge-seo-win-using-ai-that-costs-0-and-activity-7428003511625293824) (Akash Sehgal, 2026-02-13).

Top 3 quick wins (en orden de impacto/esfuerzo):

1. **GSC → pages with impressions but low CTR**: usar AI para sugerir title/meta variants
2. **GSC → missing queries on ranked pages**: páginas que rankean para queries que no aparecen en el contenido → añadir secciones
3. **Internal linking subóptimo**: pasada con AI sobre todas las páginas para sugerir 2-5 links contextuales a cada una

"Costs $0, no new content, no backlinks." — convertir en checklist al final de cada `/g4u-seo-audit`.

Aplicar en: `audit-playbook.md` (Fase 4 sintesis: incluir estas 3 como quick wins por defecto si GSC data está disponible).

---

## 5. Reddit workflow para AI search

**Fuente**: ["6-step Reddit workflow for AI search"](https://sunset-plum-4e9.notion.site/6-step-Reddit-workflow-for-AI-search-224a6c1473298028b305d43150630e76) (2025-10-20), ["Boost Your SEO with Reddit and AI: Rank in Hours"](https://x.com/) (varias).

Workflow:
1. Identificar subreddits relevantes del nicho (mínimo 5-10)
2. Construir karma + contexto durante 2-3 semanas (no publicar promo desde día 1)
3. Responder con valor en threads existentes alineados con queries target
4. Usar mismas palabras clave que las queries que se quiere rankear en LLMs
5. Crear posts propios con estructura de respuesta (no marketing)
6. Repurposar respuestas top en otros canales (LinkedIn, blog)

Riesgo: si lo automatizamos demasiado se detecta y banean — debe haber humano en el loop.

Aplicar en: `geo-citations-playbook.md` sección off-page. NO auto-ejecutar; solo recomendar al cliente.

---

## 6. Local SEO + Map Pack — tácticas G4U-aplicables

**Fuente**: ["Strategies for Dominating Local SEO and AI Search in 2026"](https://x.com/noahiglerseo/status/2052006854515995000) (Noah Igler, 2026-05-06), ["Master Local SEO with AI: Rank #1 in 30 Days"](https://x.com/), ["Outrank Local Businesses with Claude Cowork in 60 Days"](https://x.com/).

Relevante solo para clientes con presencia física (<Local Business Client>, posibles futuros). NO <Client A>/Monzo/<Client C> (todos puro online).

Stack:
- GBP optimization: completar 100% perfil, categoría primaria + 10 secundarias, **posts semanales**
- NAP consistency en 50+ citation sites
- Local schema: LocalBusiness + AggregateRating + ContactPoint
- **Press releases + listicles** para alimentar AI search local (innovación 2026: AI cita listicles para queries locales)
- Reviews respondidas en <24h: peso muy alto en Map Pack 2026

Aplicar en: `stack-map.md` decision tree — si cliente es brick-and-mortar/SAB, derivar a `/seo local` + `/seo maps` con extensión press release.

---

## 7. Google Analytics MCP — capacidad ya disponible

**Fuente**: ["Oh man, the Google Analytics MCP is INCREDIBLY powerful for SEOs"](https://x.com/chris_nectiv/status/2011472454816804871) (Chris Long, 2026-01-14).

Existe MCP de Google Analytics que permite a Claude:
- Identificar top-performing content vía sesiones/conversiones
- Cross-reference con GSC (queries que traen tráfico que convierte)
- Detectar content decay (páginas que pierden ranking pero aún convierten)
- Generar reports automatizados

**Acción**: evaluar si el MCP de Google Analytics está instalado. Si no, considerar añadirlo a `.mcp.json` (es trabajo separado, fuera de esta skill).

Aplicar en: `stack-map.md` mencionar como dependencia opcional para audit deep.

---

## 8. Longtail focus (Teal case study: 1M clicks/mes)

**Fuente**: ["How Teal Gets 1 Million Google Clicks a Month with AI-Powered SEO"](https://www.youtube.com/watch?v=8wImHWoQ7C4) (Edward Sturm, 2026-01-12).

- Teal rankea para **893,000 keywords** — mayoría longtail
- **Estrategia**: una página = una intención exacta. Ej. "[Job title] resume template" generado por cada job title
- Automation con Claude + MCPs para análisis SERP por variante
- **No competir por head terms** en early stages — entrar por la cola

Aplicar en: `page-creation-playbook.md` Fase 1 keyword expansion — priorizar longtail (volumen 10-200/mes, KD < 25).

---

## 9. Parasite SEO (cuidado, riesgo reputacional)

**Fuente**: ["SEO Strategies for 2026"](https://x.com/indexsy/status/2048890962316062927) (Jacky Chou), ["Effective Parasite SEO Strategies Without a Budget"](https://x.com/).

- Publicar en plataformas con DA alto (Medium, Forbes, LinkedIn Articles, Reddit)
- Big sites dominan SERP cada vez más — apropiarse de su autoridad
- AI Overviews favorecen también estas plataformas
- **Riesgo**: contenido "fuera" del dominio propio → no construye activo, solo tracción puntual
- Recomendación G4U: usar SOLO como táctica complementaria, no como estrategia principal

Aplicar en: marcado como "advanced/situational" en `geo-citations-playbook.md`.

---

## 10. Lo que NO aporta valor (entradas filtradas)

- 4 duplicados de "Outrank Local Businesses with Claude Cowork in 60 Days" (entradas 26-28 + similares)
- Entradas con summary vacío (status Error: 2, 14, 15) — no accionable
- Promo de herramientas sin metodología detrás (ej. SEOWritingAI)
- "Backlink generator muller" — link parece de baja calidad, no validado
- Posts de Julian Goldie genéricos sobre AI SEO sin diferenciador concreto (~5 entradas equivalentes a su 90-day case study)

---

## Recap: integraciones decididas

| Táctica | Dónde se aplica | Sección |
|---------|-----------------|---------|
| Estructura 5 secciones + FAQ schema | `page-creation-playbook.md` | Fase 3 brief |
| AI traffic 4.4-23x conversion | Audit synthesis priorities | Quick wins ordering |
| Reddit/YouTube/Medium como off-page GEO | `geo-citations-playbook.md` | Sección off-page |
| NotebookLM para SERP analysis | `page-creation-playbook.md` | Fase 2 (alternativa) |
| Hub-and-spoke + 200-300 palabras únicas | Cluster workflow | Fase 1 architecture |
| Top 3 GSC quick wins (CTR, missing queries, internal links) | `audit-playbook.md` | Fase 4 sintesis |
| Reddit workflow para AI search | `geo-citations-playbook.md` | Off-page playbook |
| GBP + reviews 24h + press releases para Local AI | `stack-map.md` | Brick-and-mortar branch |
| Google Analytics MCP | `stack-map.md` | Optional deep audit |
| Longtail focus | `page-creation-playbook.md` | Fase 1 keyword expansion |
| Parasite SEO advanced | `geo-citations-playbook.md` | Situational, no default |
