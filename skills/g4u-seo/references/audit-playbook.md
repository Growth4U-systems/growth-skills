# Workflow 1 — Auditoría SEO completa

Encadenamiento de 4 fases. Output final: HTML entregable cliente en `OUTPUTS/<cliente>/<YYYY-MM-DD>-seo-audit.html`.

## Inputs requeridos

| Input | De dónde | Bloqueante |
|-------|----------|------------|
| URL del sitio | Usuario o contexto cliente | SÍ |
| Cliente slug (para output path) | Inferido o preguntado | NO (default = host del dominio) |
| Acceso GSC | Service account `~/.gcp/sancho-analytics.json` añadido al property | NO bloqueante — degrada con aviso |
| DataForSEO MCP autenticado | `.mcp.json` ya validado | SÍ para audit completo |

Si no hay GSC: el audit sigue, pero sintesis quick-wins basados en GSC NO se generan (aviso explícito en output).

---

## Fase 1 — Datos crudos (TopRank seo-analysis)

**Skill**: `toprank:seo-analysis <url>`

**Recoge**:
- GSC: queries, clicks, impressions, CTR, position (últimos 90 días)
- URL Inspection API: indexability, canonical, last crawl, robots, status
- PageSpeed Insights: LCP, INP, CLS, FCP, TTFB, Speed Index — mobile + desktop
- Top pages por tráfico orgánico
- Pages with impressions but low CTR (<2%)
- Queries en posiciones 4-15 (oportunidades de mejora rápida)

**Output**: JSON estructurado guardado en `.cache/<cliente>/01-toprank.json`.

**Tiempo esperado**: 2-5 min según volumen del sitio.

**Si falla**:
- Auth GSC → mostrar instrucciones para añadir service account al property
- PSI rate limit → reintentar tras 60s, max 3 veces
- Sitio muy grande (>10K pages) → muestrear top 100 + random 100

---

## Fase 2 — Audit técnico/on-page (AgriciDaniel `/seo audit`)

**Skill**: `/seo audit <url>` — orquestador paralelo 9 categorías

**Cubre**:
- Crawlability (robots.txt, sitemap, hreflang)
- Indexability (canonicals, noindex, status codes)
- Technical (CWV from PSI, security HTTPS, mobile friendliness)
- On-page (titles, metas, headings, internal linking)
- Schema (detected + validated — usa Playwright para render JS, no web_fetch)
- Content (E-E-A-T preliminary)
- Images (alt text, file names, size)
- Links (broken via `toprank:broken-link-checker`)
- Industry-specific (auto-detecta SaaS/ecom/local/publisher)

**Critical caveat — schema detection**: NO confiar en `web_fetch`. Si el sitio inyecta JSON-LD vía JS (común con AIOSEO, Yoast, RankMath), web_fetch lo pierde. AgriciDaniel ya sabe esto pero **verificar manualmente** con Playwright MCP si el sitio reporta "no schema":

```javascript
// vía Playwright
document.querySelectorAll('script[type="application/ld+json"]').forEach(s => console.log(s.innerText))
```

**Output**: Markdown estructurado por categorías en `.cache/<cliente>/02-agricidaniel.md`.

**Tiempo esperado**: 5-15 min.

### Fase 2a — Stack detection empírico (precondición para 2b/2c)

**Por qué existe esta fase**: las Fases 2b accessibility y 2c performance generan handoff briefs con `files probables` y `skill recomendada` específicos al stack. Si no detecto antes el stack real, los briefs son genéricos y obligan al dev (Martín) a re-investigar. Filosofía G4U: el brief debe ser ejecutable sin que el dev tenga que volver a auditar.

**Script**: [`scripts/stack-detector.sh`](../scripts/stack-detector.sh)

**Ejecución**:

```bash
./scripts/stack-detector.sh <url>             # Markdown legible
./scripts/stack-detector.sh <url> --json      # JSON para consumo programático
```

**Qué detecta** (vía `curl + grep` sobre HTML + headers, ~3 segundos):

| Categoría | Cómo lo detecta | Ejemplos |
|-----------|-----------------|----------|
| CMS | grep patterns en HTML | WordPress (`wp-content`), Webflow (`data-wf-page`), Shopify, Wix, Squarespace, Drupal, Ghost |
| Framework JS | grep build artifacts | Next.js (`_next/static`), Astro (`_astro/`), Nuxt, Gatsby, SvelteKit, Remix, Hugo |
| CDN | response headers | Cloudflare (`CF-Ray`), Vercel (`X-Vercel-Id`), Netlify, Fastly, Akamai, CloudFront |
| Server | header `Server` | nginx, Apache, LiteSpeed, Caddy, cloudflare |
| Language backend | combinación de signals | PHP, Node.js, .NET |
| WP plugins (si WP) | grep paths en HTML | Divi, Avada, Elementor, Yoast, RankMath, AIOSEO, WPML, WooCommerce |
| Third-party scripts | grep src patterns | GTM, GA4, Meta Pixel, LinkedIn Insight, Hotjar, Amplitude, Zendesk, Intercom, Optimizely, cookie consent, Trustpilot, reCAPTCHA |
| Script count | grep `<script>` tags | Total + externos |

**Output**: stack manifest guardado en `.cache/<cliente>/02a-stack-manifest.md` (también JSON `.cache/<cliente>/02a-stack-manifest.json`).

**Cómo lo usan 2b y 2c**: el manifest informa los `files probables` y `skill recomendada` de cada handoff brief. Ejemplos:

| Stack detectado | `files probables` típico en handoff brief | `skill recomendada` |
|-----------------|------------------------------------------|---------------------|
| WordPress + Divi | `wp-content/themes/Divi-child/functions.php`, `style.css`, `wp-content/uploads/...` | Edit directo en repo + Divi builder UI para visual changes |
| WordPress + Elementor | `wp-content/themes/<theme>/`, `wp-content/plugins/elementor/` settings | Elementor editor + theme child edits |
| Webflow | Webflow Designer manual + Page Settings > Custom Code | NO skill (manual) + verify post-cambio con Chrome DevTools MCP |
| Next.js | `src/components/<Component>.tsx`, `src/styles/tokens.css`, `next.config.js`, `public/` | `frontend-design` skill + `next/image`, `next/font` patterns |
| Astro | `src/components/<Component>.astro`, `src/layouts/`, `astro.config.mjs`, `public/` | `frontend-design` skill + `astro:assets`, `<Image>` component |
| Shopify | Liquid templates en theme files (via Shopify CLI o admin Themes editor) | Shopify-specific edits |

**Confidence levels**:
- `high`: pattern explícito en HTML (ej. `_next/static` → Next.js definitivo)
- `medium`: indicador parcial (ej. solo header Server o un meta tag)
- `low`: nada concluyente — pedir confirmación al usuario

**Si confidence es low en CMS Y Framework**: no asumir. Pedir al usuario que confirme el stack antes de generar handoff briefs con `files probables` específicos. Mejor decir "files probables: depende del stack — confirmar con dev" que inventar paths.

**Verificación**:
- Manifest tiene `cms.name` o `framework.name` con confidence ≥ medium
- `implications` no está vacío
- Si todo es `unknown/low`, escalar al usuario antes de Fase 2b

---

### Fase 2b — Accessibility audit (handoff brief)

**Skills/herramientas**:
- Lighthouse via `toprank:seo-analysis` (ya tira en Fase 1) — sección Accessibility
- Chrome DevTools MCP (`mcp__chrome-devtools__lighthouse_audit`) — si quieres pasada deep
- AgriciDaniel `/seo audit` no cubre accessibility profundo — toca complementar

**Qué auditar**:
- Color contrast (WCAG AA: 4.5:1 texto normal, 3:1 texto grande)
- Alt text en imágenes (todas requieren alt, decorativas con alt="")
- Heading hierarchy (no saltar de H1 a H3, exactamente un H1 por página)
- Form labels asociados a inputs (label[for] o aria-labelledby)
- Keyboard navigation (todos los elementos interactivos accesibles por Tab + Enter/Space)
- Focus visible (no `outline: none` sin alternativa)
- ARIA labels donde el texto visible no es suficiente
- Skip-to-content link al inicio de cada página
- Idioma declarado en `<html lang="...">`
- Document title único y descriptivo por página

**IMPORTANTE — yo solo diagnostico, NO arreglo**. Por cada finding genero un **handoff brief** que un dev puede ejecutar con otras skills (`frontend-design`, Claude Code en repo cliente).

**Formato de cada finding (accessibility)** — `files probables` y `skill recomendada` derivados del stack manifest de Fase 2a:

```markdown
### A11Y-01 · [Título corto del issue]

- **Severity**: critical | high | medium | low
- **WCAG criterion**: 1.4.3 Contrast (Minimum) [Level AA]
- **Lighthouse score impact**: -X puntos en accessibility
- **Stack context** (de Fase 2a): WordPress + Divi + Yoast SEO
- **Location**: 
  - URL: https://...
  - Elemento: `button.cta-primary` (selector CSS)
  - Componente probable: `wp-content/themes/Divi-child/style.css` línea aproximada de la variable de color
- **User impact**: usuarios con baja visión no pueden leer el CTA con confianza
- **Fix description**: cambiar color de fondo del botón de `#FFB627` a `#E89A05` para conseguir ratio 4.6:1 con texto blanco
- **Handoff brief**:
  - **Skill recomendada**: edit directo en repo cliente (WordPress, no aplica `frontend-design`) o Divi builder UI si el cambio es a nivel global
  - **Files a modificar**: `wp-content/themes/Divi-child/style.css` (override) o WP Admin > Divi > Theme Options > Colors
  - **Effort estimado**: 10 min + visual review
  - **Verification**: re-run Lighthouse / Chrome DevTools `lighthouse_audit`; target accessibility >95; verificar también en versión móvil
- **References**: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum
```

**Nota crítica sobre `files probables`**: dependen del stack detectado en Fase 2a. NO inventes paths sin haber confirmado stack. Si Fase 2a devolvió confidence `low`, escribe `files probables: depende del stack — confirmar con dev` en lugar de inventar. Es mejor un brief honesto que pida verificación que uno preciso pero falso.

**Severidad guía**:
- **Critical**: bloquea uso para personas con discapacidad (sin alt text en imágenes informativas, sin keyboard nav, contrast < 3:1)
- **High**: degrada experiencia significativamente (heading skipping, form sin labels)
- **Medium**: mejor experiencia pero hay workarounds (ARIA labels faltantes en iconos)
- **Low**: cosmético / preferencia (focus styles refinables)

**Output**: `.cache/<cliente>/02b-accessibility.md` con N findings + tabla resumen + handoff briefs.

### Fase 2c — Performance code audit (handoff brief)

**Skills/herramientas**:
- PageSpeed Insights ya en Fase 1 — extraer las "Opportunities" + "Diagnostics"
- Chrome DevTools MCP (`mcp__chrome-devtools__performance_start_trace` + `performance_analyze_insight`) — pasada deep si está disponible
- Lighthouse via toprank

**Qué auditar (más allá de las métricas CWV genéricas)**:
- **JavaScript blocking**: `<script>` síncronos en `<head>` que bloquean LCP
- **Render-blocking CSS**: CSS no-crítico cargado en `<head>` sin `media` ni preload
- **Unused JavaScript**: scripts cargados pero <30% usado
- **Unused CSS**: stylesheets sobredimensionados
- **Image optimization**: imágenes >100KB, formato no-WebP/AVIF, sin `width`/`height` (causa CLS)
- **LCP element**: identificar el elemento concreto que causa LCP — probablemente imagen hero o web font
- **Font loading strategy**: `font-display`, preload, swap
- **Bundle size**: total JS shipped > 200KB compressed
- **Third-party scripts**: analytics, chats, A/B tools que bloquean main thread
- **Lazy loading**: imágenes below-the-fold sin `loading="lazy"`
- **Critical CSS**: si no se extrae critical CSS, FCP/LCP sufren

**Formato de cada finding (performance)** — `files probables` y `skill recomendada` derivados del stack manifest:

```markdown
### PERF-01 · [Título corto del issue]

- **Severity**: critical | high | medium | low
- **CWV metric impacted**: LCP / INP / CLS / FCP / TTFB
- **Current value**: LCP 4.2s mobile (target <2.5s)
- **Lighthouse score impact**: -X puntos en performance
- **Stack context** (de Fase 2a): Next.js + Vercel + Tailwind
- **Location**:
  - URL: https://...
  - Recurso: `https://example.com/_next/static/media/hero.png` (3.2MB)
  - Componente probable: `<Hero />` en `src/components/Hero.tsx`
- **Root cause**: imagen hero PNG sin comprimir, sirviendo 3.2MB vs ~250KB con WebP optimizado
- **Fix description**:
  1. Migrar `<img src="">` a `next/image` con `<Image fill priority />`
  2. Convertir source a WebP/AVIF (Next.js lo hace auto si usa next/image)
  3. Definir `width` + `height` para evitar CLS
  4. Añadir `priority` para preload del LCP image
- **Handoff brief**:
  - **Skill recomendada**: `frontend-design` (Anthropic) + Chrome DevTools MCP para verificar
  - **Files a modificar**:
    - `src/components/Hero.tsx` — cambiar `<img>` a `<Image>` de next/image
    - `next.config.js` — verificar `images.remotePatterns` si la imagen es externa
    - `public/hero.png` — opcional: pre-convertir a WebP si quieres bypassear el optimizer
  - **Effort estimado**: 45-60 min (incluye visual review en mobile + desktop)
  - **Verification**:
    - PSI re-audit; LCP target <2.5s mobile, CLS <0.1
    - Chrome DevTools MCP `performance_start_trace` antes/después para comparar
  - **Tooling útil**: `next/image` (built-in optimizer), `squoosh.app` para conversión manual de fallbacks
- **Impact estimado**: LCP -2.1s → -2.5s mejora (paso de "poor" a "good")
```

**Variantes del handoff brief según stack detectado**:

| Stack | `files probables` | `skill recomendada` |
|-------|-------------------|---------------------|
| Next.js | `src/components/*.tsx`, `next.config.js`, `public/` | `frontend-design` + `next/image`, `next/font` |
| Astro | `src/components/*.astro`, `astro.config.mjs`, `public/` | `frontend-design` + `astro:assets`, `<Image>` |
| WordPress + Divi | `wp-content/themes/Divi-child/`, WP Media Library | edit directo en repo + Divi builder visual |
| WordPress + Elementor | `wp-content/themes/<theme>/`, Elementor settings | edit en repo + Elementor editor |
| Webflow | NO archivos — cambios en Webflow Designer | Manual en Designer + verify post-cambio |
| Shopify | `themes/<theme>/sections/`, `assets/` via Shopify CLI | Theme editor + Liquid templates |
| Stack desconocido (Fase 2a confidence low) | "depende del stack — confirmar con dev" | `frontend-design` genérico, pedir clarificación |

**Importante**: si Fase 2a no detectó el stack con confidence ≥ medium, NO inventar paths. Mejor un brief honesto que pida verificación que uno detallado pero falso.

**Severidad guía**:
- **Critical**: CWV en "poor" (LCP >4s, INP >500ms, CLS >0.25). Probable impacto en ranking
- **High**: CWV "needs improvement" + opportunity de >500ms de mejora
- **Medium**: opportunity <500ms o solo afecta a ciertos casos (mobile slow 3G)
- **Low**: best practice no aplicable a la prioridad actual

**Output**: `.cache/<cliente>/02c-performance.md` con N findings + tabla CWV actual vs target + handoff briefs.

---

## Fase 3 — AI/GEO audit (3 capas)

**Skills**, en este orden secuencial:

### 3a. `toprank:geo-optimizer <url>` — GEO score research-backed

Genera:
- Citation likelihood score por motor (ChatGPT, Perplexity, Claude, Gemini, AI Overviews)
- Signal stack analysis (autoridad, freshness, citation density, structure)
- Comparación con top SERP results en el nicho

**Output**: `.cache/<cliente>/03a-geo-score.json`.

### 3b. Corey Haines `ai-seo` — per-platform gap analysis

Skill: pasarle el sitio + queries top de GSC. Devuelve:

| Plataforma | Cómo selecciona fuentes | Recomendación para este sitio |
|------------|------------------------|-------------------------------|
| AI Overviews | Correlación fuerte con ranking tradicional | ... |
| ChatGPT (search) | Wide range, no top-rank only | ... |
| Perplexity | Authoritative + recent + structured | ... |
| Gemini | Google index + Knowledge Graph | ... |
| Copilot | Bing + authoritative | ... |
| Claude | Brave Search results | ... |

**Output**: `.cache/<cliente>/03b-ai-seo.md`.

### 3c. AI citation tracking (si hay DataForSEO LLM endpoints)

Si DataForSEO `ai_opt_llm_ment_*` está disponible:
- Buscar menciones de la marca/dominio en respuestas ChatGPT/Perplexity
- Cross-aggregate metrics por LLM
- Top competidores citados para queries equivalentes

**Output**: `.cache/<cliente>/03c-llm-mentions.json`.

---

## Fase 4 — Sintesis G4U (composición del entregable)

Aquí es donde aporto valor. Combinar los outputs anteriores en:

### 4.1 Quick wins (3-5 acciones, default si hay GSC data)

Según [`bibliography-tactics.md` §4](./bibliography-tactics.md):

1. **CTR low-hangers**: páginas con impressions > 100 pero CTR < 2% en pos 4-10. Sugerir new title/meta variants.
2. **Missing query coverage**: queries que rankean (pos 4-15) pero no aparecen en el copy de la página. Sugerir sección añadida.
3. **Internal linking gaps**: páginas top con poca cantidad de internal links entrantes. Sugerir 2-5 contextuales.
4. **(si GEO score bajo)** Páginas con buen ranking pero baja citation likelihood: sugerir restructure a 5 secciones + FAQ schema (§1.1).
5. **(si schema gaps)** Schema crítico ausente (Article, Product, Organization según tipo): generar JSON-LD listo para inyectar.

Cada quick win = título + impacto estimado + esfuerzo + acción concreta.

### 4.2 Roadmap 30 días

Tres bloques temporales:

- **Semana 1-2**: quick wins arriba + technical urgent (broken links, 404s, redirects mal formados, indexation issues)
- **Semana 3-4**: content optimization (top 5 páginas con potencial sin explotar) + schema deployment
- **Semana 5+ (overview)**: estrategia GEO + content gaps + link building

### 4.3 GEO playbook específico

De [`geo-citations-playbook.md`](./geo-citations-playbook.md):
- Off-page recommendations (Reddit + YouTube + Medium si aplica al nicho)
- 5-section structure + FAQ schema deployment
- Citation tracking setup (Profound/Amplitude/DataForSEO)

### 4.4 Métricas baseline (para tracking futuro)

Snapshot del estado actual:
- Total páginas indexadas
- Top 10 queries con clicks
- Top 10 páginas con tráfico
- CWV scores (LCP/INP/CLS)
- Accessibility score (Lighthouse)
- GEO score por motor
- Backlinks count (DataForSEO `backlinks_summary`)

Esto sirve como baseline para comparar en re-audit a los 30/60/90 días.

### 4.5 Handoff briefs consolidados (NUEVO)

Toda finding accessibility (Fase 2b) + performance code (Fase 2c) se compila en una sección de **handoff** del entregable final. Esta sección está pensada para que **otra persona pueda arreglar el problema sin más context** — yo solo diagnostico.

Estructura del handoff consolidado:

```markdown
## Handoff: arreglos técnicos no-SEO (accessibility + performance)

> Estos hallazgos NO los arreglo yo (g4u-seo). Salen del audit pero
> requieren intervención de dev / otra skill. Cada item es self-contained
> para que un dev pueda ejecutarlo con `frontend-design` skill,
> Chrome DevTools MCP, o directo en el repo.

### Resumen

| ID | Tipo | Severity | Impacto | Effort estimado |
|----|------|----------|---------|-----------------|
| A11Y-01 | Accessibility | critical | WCAG 1.4.3 (contraste) | 5 min |
| A11Y-02 | Accessibility | high | Alt text en imágenes informativas | 20 min |
| PERF-01 | Performance | critical | LCP 4.2s → <2.5s objetivo | 60 min |
| PERF-02 | Performance | high | Unused JS (-400ms TBT) | 90 min |

### Cómo procesar

1. **Para arreglos de UI/diseño** (contraste, focus, layout): usar `frontend-design` skill
2. **Para optimización de assets** (imágenes, fonts, bundles): usar Chrome DevTools MCP + ediciones en repo
3. **Si es Webflow / CMS**: cambios en Designer + verificar con PSI
4. **Verificación post-fix**: re-correr Lighthouse / PSI / `mcp__chrome-devtools__lighthouse_audit`

### Findings detallados

[Aquí van los findings individuales con el formato handoff brief
 documentado en audit-playbook §2b y §2c]
```

**Cada handoff brief incluye obligatoriamente**:
- Severity + impact concretos
- Location (URL + selector + componente probable si detectable)
- Root cause explicado
- Fix description paso a paso
- Skill recomendada para hacerlo
- Files probables a modificar
- Effort estimado
- Verification (cómo confirmar que está arreglado)
- References (WCAG / docs oficiales)

**Filosofía G4U**: no propongo "mejora el contraste" abstracto. Propongo "cambia `--color-cta-bg` de `#FFB627` a `#E89A05` en `src/styles/tokens.css`, verifica con Lighthouse, target accessibility >95". El handoff debe ser ejecutable sin que el dev tenga que volver a auditar.

---

## Output final

**Skill**: `html-output` con tema Sancho.

**Path**: `OUTPUTS/<cliente>/<YYYY-MM-DD>-seo-audit.html`

**Estructura del HTML**:

1. Hero / Executive summary (5-7 bullets)
2. Quick wins (3-5 con priorización visual)
3. Roadmap 30 días (timeline visual)
4. Detalle Fase 2 técnico (categorías collapsibles)
5. Detalle Fase 3 GEO (tabla por motor)
6. GEO playbook (próximas acciones)
7. Métricas baseline (cards)
8. Apéndice: outputs raw de cada fase (collapsed)

Si Alfonso lo pide: subir a Notion como sub-página de un task nuevo.

---

## Verificación pre-entrega

- [ ] HTML abre en browser sin errores de render
- [ ] Las 4 fases tienen contenido (no secciones vacías)
- [ ] Quick wins son accionables — cada uno con "qué cambiar", "dónde", "por qué"
- [ ] Métricas concretas citadas (no "tu CTR es bajo" sino "página X tiene CTR 0.8% en pos 6 para 'query Y'")
- [ ] Si una fase falló parcialmente, está documentado en el output (no oculto)
- [ ] Roadmap está priorizado y realista (no 50 acciones en 30 días)
