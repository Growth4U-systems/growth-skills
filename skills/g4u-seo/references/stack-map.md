# Stack Map — qué skill usar para qué

Mapa de decisión de las 30+ skills SEO instaladas. Si dos skills se solapan, esta sección dice cuál ganar y por qué.

## Inventario verificado (al 2026-05-21)

### AgriciDaniel `/seo` — `~/.claude/skills/seo*` (24 skills)
Orquestador principal con sub-comandos. Ya conoce paralelización de subagents.

| Comando | Hace | Cuándo es la mejor opción |
|---------|------|--------------------------|
| `/seo audit <url>` | Full audit paralelizado (9 categorías) | Audit on-page completo de un sitio cuando ya tienes GSC data crudo |
| `/seo page <url>` | Deep single-page analysis | Una página específica, no full site |
| `/seo schema <url>` | Detect + validate + generate JSON-LD | Cualquier necesidad schema |
| `/seo geo <url>` | AI Overviews / GEO audit | Audit citation readiness (complementa Corey Haines `ai-seo`) |
| `/seo plan <type>` | Strategic SEO planning | Briefing de cliente nuevo, planning anual |
| `/seo programmatic <url\|plan>` | Programmatic SEO analysis + planning | Cluster scale 50+ páginas |
| `/seo competitor-pages <url\|generate>` | Competitor comparison page generation | Páginas "X vs Y" / "alternatives to X" |
| `/seo cluster <topic>` | Topic clustering | Hub-and-spoke design |
| `/seo local <url>` | Local SEO (GBP, citations, reviews, map pack) | Cliente brick-and-mortar/SAB |
| `/seo maps <command>` | Maps intelligence (geo-grid, GBP audit) | Tracking Map Pack ranking |
| `/seo technical <url>` | Technical SEO audit (9 categorías) | Si quieres audit técnico aislado sin lo demás |
| `/seo content <url>` | E-E-A-T y content quality | Audit dedicado de contenido |
| `/seo sitemap <url\|generate>` | XML sitemap análisis o generación | Issues de indexación o nuevo sitemap |
| `/seo images <url\|optimize>` | Image SEO | Sitio con muchas imágenes |
| `/seo hreflang [url]` | Hreflang/i18n audit | Cliente multi-mercado |
| `/seo ecommerce <url>` | E-commerce SEO | Cliente Shopify/Woo/etc |

### Corey Haines v2.0 — `~/.agent/skills/skills/` (6 SEO-relevantes)

| Skill | Hace | Cuándo |
|-------|------|--------|
| `seo-audit` | Audit jerarquizado (crawlability → técnica → on-page → content → autoridad) | Cuando AgriciDaniel falla o el sitio es JS-heavy (Corey tiene warning crítico sobre detección de schema vía web_fetch — usa render JS) |
| `ai-seo` | GEO/AEO con tabla por motor (AI Overviews, ChatGPT, Perplexity, Gemini, Copilot, Claude) | Audit GEO en profundidad — preferir sobre `/seo geo` cuando se quiera análisis por plataforma específica |
| `programmatic-seo` | Generación de páginas a escala | Programmatic SEO cuando AgriciDaniel `/seo programmatic` queda corto |
| `schema-markup` | Estructura completa schema.org | Si TopRank o `/seo schema` no dan suficiente |
| `site-architecture` | Hub-and-spoke design | Cluster planning Fase 1 |
| `keyword-research` | 6 Circles method | Fase 1 keyword expansion (combinar con `toprank:keyword-research`) |

### TopRank — `~/.claude/plugins/cache/nowork-studio/toprank/0.17.0/seo/` (9 skills)

| Skill | Hace | Cuándo |
|-------|------|--------|
| `toprank:seo-analysis` | Full audit con **GSC + PSI + URL Inspection reales** | **Siempre Fase 1 audit** — único que tiene los datos vivos |
| `toprank:keyword-research` | KW research con DataForSEO + GSC | Fase 1 keyword expansion (combinar con Corey) |
| `toprank:geo-optimizer` | GEO con research Princeton KDD2024 + CMU AutoGEO ICLR2026 | Fase 3 audit + Fase 5 página |
| `toprank:seo-page` | Page optimization recomendaciones | Backup de Corey Haines `seo-page` |
| `toprank:broken-link-checker` | Check de broken links | Audit técnico Fase 2 |
| `toprank:meta-tags-optimizer` | Title/meta optimization | Fase 4 página |
| `toprank:schema-markup-generator` | Generación JSON-LD | Fase 4 página (preferido sobre `/seo schema` para generar; `/seo schema` para validar) |
| `toprank:content-writer` | Content writing | Backup, no preferido — preferir Corey + direct-response-copy |
| `toprank:setup-cms` | CMS setup | Solo si el cliente es nuevo y necesita stack desde cero |

Bonus — TopRank `openclaw` skills (5):
- `toprank:toprank-site-onboard`, `toprank-portfolio-review`, `toprank-investigate-drop`, `toprank-improve-page`, `toprank-weekly-review`

Útiles para mantenimiento continuo (no para audit one-shot).

### Auxiliares — `~/.claude/skills/`

| Skill | Cuándo |
|-------|--------|
| `html-output` | **Siempre** para output final — tema Sancho |
| `direct-response-copy` | Brief Fase 3 página — copy hooks |
| `brand-voice` | Brief Fase 3 página — tono según contexto cliente |
| `qa-bot` | QA Fase 6 página |
| `deep-research` | Audit profundo de un competidor específico |
| `content-strategy` | Calendarización + content mix (post-audit) |
| `content-atomizer` | Repurposing del contenido SEO a social |
| `notion-research-documentation` | Si pedido explícito de subir hallazgos a Notion |

## Conflictos resueltos

| Conflicto | Ganador | Por qué |
|-----------|---------|---------|
| `/seo audit` vs Corey `seo-audit` | AgriciDaniel default; Corey si JS-heavy o necesitas el warning crítico schema | AgriciDaniel paraleliza; Corey es más prudente con detección |
| `/seo geo` vs Corey `ai-seo` vs `toprank:geo-optimizer` | Los 3 secuencialmente: TopRank (research-backed) → Corey (per-platform table) → AgriciDaniel (cita check) | Aportan capas distintas, no duplican |
| Corey `keyword-research` vs `toprank:keyword-research` | Ambos. Corey aporta método (6 Circles); TopRank aporta volúmenes GSC reales | Combinar |
| `/seo schema` vs `toprank:schema-markup-generator` | TopRank para generar JSON-LD; AgriciDaniel para validar contra HTML rendered | Roles complementarios |
| `/seo competitor-pages` vs NotebookLM workflow | Para entregable formal: AgriciDaniel. Para análisis rápido: NotebookLM (ver bibliography-tactics §2) | NotebookLM no produce código, AgriciDaniel sí |
| `seo-page` (AgriciDaniel) vs Corey `seo-page` vs TopRank `seo-page` | Corey para Fase 3 brief (mejor con marketing context); AgriciDaniel para Fase 6 QA; TopRank backup | Cada uno fortaleza distinta |

## Decision tree completo

```
Usuario pide algo SEO
│
├── ¿Es ambiguo? → Pregunto: audit / página / cluster
│
├── AUDIT
│   ├── ¿Local business? → /seo local + /seo maps + (TopRank seo-analysis para datos)
│   ├── ¿E-commerce? → /seo ecommerce + (TopRank + AgriciDaniel base)
│   ├── ¿Multi-país? → /seo hreflang + base
│   ├── Default → audit-playbook.md (TopRank seo-analysis → /seo audit → ai-seo + geo-optimizer → sintesis)
│   └── ¿Drop sospechado? → toprank:toprank-investigate-drop antes de todo
│
├── PÁGINA INDIVIDUAL
│   └── page-creation-playbook.md
│       ├── F1 keyword expansion: Corey keyword-research + toprank:keyword-research
│       ├── F2 SERP: /seo competitor-pages + DataForSEO (o NotebookLM rápido)
│       ├── F3 brief: Corey seo-page + direct-response-copy + brand-voice → 5 secciones + FAQ schema
│       ├── F4 schema: toprank:schema-markup-generator
│       ├── F5 GEO: toprank:geo-optimizer + Corey ai-seo
│       └── F6 QA: qa-bot + /seo page lighthouse
│
└── CLUSTER / PROGRAMMATIC
    └── page-creation-playbook.md sección programmatic
        ├── F1 cluster: /seo cluster + Corey site-architecture (hub-and-spoke)
        ├── F2 template: /seo programmatic + Corey programmatic-seo + page-builder
        ├── F3 data layer: CSV/JSON con N variants (200-300 palabras únicas mínimo)
        └── F4 bulk gen: page-creation-playbook Fases 2-6 paralelizadas
```

## MCPs requeridos / opcionales

- **DataForSEO MCP** (requerido): SERP, keyword volume, backlinks, on-page, AI mentions
- **Notion MCP** (requerido): para sync entregables si lo piden
- **Google Search Console** (requerido para audit deep): API via service account `~/.gcp/sancho-analytics.json` para growth4u.io. Para clientes hay que añadir el SA como user al property.
- **PageSpeed Insights** (free, no MCP — via curl en `toprank:seo-analysis`)
- **Chrome DevTools MCP** (instalado, recomendado para Fase 2c performance + 2b accessibility): `lighthouse_audit`, `performance_start_trace`, `performance_analyze_insight`
- **Firecrawl MCP** (opcional): crawling avanzado, si el sitio es JS heavy y `web_fetch` no llega
- **Google Analytics MCP** (opcional, no instalado aún): ver bibliography-tactics §7. Considerar añadir.
- **Playwright MCP** (instalado): render JS para validar schema markup que se inyecta vía JS

## Handoff destinations — accessibility + performance code

Estos hallazgos del audit (Fase 2b accessibility, Fase 2c performance) NO se arreglan dentro de `g4u-seo`. Se generan handoff briefs que un dev procesa con otras skills.

| Tipo de fix | Skill receptora recomendada | Cuándo |
|-------------|----------------------------|--------|
| UI/diseño (contraste, focus styles, layout) | `frontend-design` (Anthropic skill) | Repo del cliente accesible localmente |
| Componente React/Astro/Vue | `frontend-design` + Claude Code directo | Cambios en `src/components/` |
| Tokens de diseño (colors, fonts, spacing) | `frontend-design` o edit directo en CSS variables | `tokens.css`, `theme.ts`, `tailwind.config.js` |
| Optimización de imágenes | Chrome DevTools MCP + `cwebp` / `squoosh.app` CLI manual | Pipeline de assets |
| Lazy loading + responsive images | `frontend-design` + framework-specific tools (`next/image`, `astro:assets`) | Páginas con LCP alto |
| Bundle size / unused JS | Chrome DevTools MCP `performance_analyze_insight` + edits en repo | Webpack/Vite/Next builds |
| Critical CSS extraction | `frontend-design` + tools como Critical, Penthouse | Sitios con FCP alto |
| Font loading strategy | `frontend-design` (preload, font-display) | Web fonts custom |
| Cambios en Webflow Designer | Manual en Webflow + verificar PSI post-cambio | Clientes en Webflow (<Client A>) |
| Cambios en WordPress/Wix/Shopify | Manual + plugin específico + verificar PSI | Otros CMS |

**Filosofía handoff**: el brief debe permitir al dev arrancar sin re-auditar. Incluye severity + WCAG/CWV target + file path probable + effort estimado + verification method. Ver `audit-playbook.md` §2b y §2c para formato exacto.

## Skills que NO debo invocar desde g4u-seo

- `/seo plan` — es estrategia anual, no operativa. Si el cliente lo pide aparte, OK
- `seo-firecrawl` — solo si Firecrawl MCP está activo y el sitio lo requiere
- `seo-drift` — solo si existe baseline previo del sitio (raramente al primer audit)
- `seo-sxo` — solapamiento total con Corey `ai-seo` + UX consideration que ya está en quick wins
