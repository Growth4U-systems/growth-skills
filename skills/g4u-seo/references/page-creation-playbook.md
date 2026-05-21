# Workflow 2 — Página individual + Workflow 3 — Cluster programmatic

---

## Workflow 2 — Página individual

Producir UNA página optimizada para una keyword target. Output: brief estructurado + schema JSON-LD + checklist GEO.

### Fase 1 — Keyword expansion + intent

**Skills (combinadas, paralelo)**:
- Corey Haines `keyword-research` — método 6 Circles (problem, solution, brand, competitor, audience, jobs-to-be-done)
- `toprank:keyword-research` — DataForSEO volumes + GSC matchback

**Output**:
- Cluster de 20-50 keywords variantes del seed
- Intent classification (informational / commercial / transactional / navigational)
- Para cada keyword: volume, KD, CPC, search trend
- **Priorización G4U**: empezar por longtail (volume 10-200, KD < 25) si el cliente no tiene autoridad establecida ([`bibliography-tactics.md` §8](./bibliography-tactics.md))

**Decisión bloqueante**: el usuario confirma 1 keyword head + 2-3 supporting antes de seguir. **Pregunto si hay ambigüedad**.

### Fase 2 — SERP analysis + content gap

Dos opciones según tiempo disponible:

**Opción A — Formal (entregable cliente)**: `/seo competitor-pages` + DataForSEO MCP
- Pull top 10 SERP para la keyword
- Análisis estructura común (H2/H3, count words, schema usado, media)
- Identificar gaps de contenido (qué cubren todos / qué cubren solo algunos / qué nadie cubre)
- Backlinks profile del top 3 (DataForSEO `backlinks_summary`)

**Opción B — Rápida (research interno)**: NotebookLM workflow
- Recolectar top 10 URLs del SERP via DataForSEO
- Subir las URLs a NotebookLM
- 4 prompts: (1) keyword clusters mencionados (2) FAQ list extraída (3) schema markup detected (4) gaps comunes
- Tiempo: 10 min vs 1h del flujo formal

Ver [`bibliography-tactics.md` §2](./bibliography-tactics.md) para detalles NotebookLM.

**Output**: `.cache/<cliente>/<keyword-slug>/02-serp-analysis.md`

### Fase 3 — Brief estructurado

**Skills**:
- Corey Haines `seo-page` — estructura on-page
- `direct-response-copy` — hooks copy persuasivos
- `brand-voice` — tono según contexto cliente (si está disponible)

**Estructura del brief — 5 secciones obligatorias + FAQ** ([`bibliography-tactics.md` §1.1](./bibliography-tactics.md)):

```
H1: <keyword exact match o variación natural>
[Hook 50-80 palabras: problem statement + promesa de solución]

H2: Sección 1 — [Pain point / context]
   [200-300 palabras]
   - Bullets concretos
   - Una cita / dato externo

H2: Sección 2 — [Definition / framework]
   [200-300 palabras]
   - Esquema visual recomendado

H2: Sección 3 — [Cómo / proceso / pasos]
   [300-500 palabras]
   - Lista numerada con 5-7 pasos
   - Cada paso con sub-bullet de detalle

H2: Sección 4 — [Examples / case studies]
   [200-400 palabras]
   - 2-3 ejemplos concretos
   - Idealmente del propio cliente

H2: Sección 5 — [Action / next step]
   [150-250 palabras]
   - CTA claro
   - Link al producto / siguiente paso

H2: Frequently asked questions
   [5-8 Q/A pairs, cada respuesta 50-100 palabras]
   ⚠️ ESTO va con FAQ schema JSON-LD obligatorio
```

**Por qué 5 secciones**: testeado en ChatGPT/Perplexity/Claude — los artículos con 5 secciones se citan más que los de 3 o 7. Sweet spot empírico ([`bibliography-tactics.md` §1.1](./bibliography-tactics.md)).

**Output**: `.cache/<cliente>/<keyword-slug>/03-brief.md`

### Fase 4 — Schema markup

**Skills**:
- `toprank:schema-markup-generator` — genera JSON-LD desde el brief
- `/seo schema` — valida contra HTML rendered (si la página ya existe)

Schemas obligatorios según tipo de página:
- **Article/BlogPosting**: headline, image, author, datePublished, dateModified
- **FAQPage**: para la sección FAQ obligatoria
- **BreadcrumbList**: navegación contextual
- **Product** (si aplica): name, image, description, brand, offers, aggregateRating
- **Organization**: en sitewide header

**Output**: `.cache/<cliente>/<keyword-slug>/04-schema.json`

### Fase 5 — GEO optimization

**Skills**:
- `toprank:geo-optimizer` — rewrite por motor (ChatGPT/Perplexity/AIO)
- Corey Haines `ai-seo` — per-platform tuning

Pasada de optimización sobre el brief:
- Cada H2 con summary statement al inicio (1-2 frases que un LLM pueda citar)
- Datos numéricos concretos (años, %, $) mejoran citation likelihood
- Enlaces externos a fuentes autoritativas (papers, estudios, .gov)
- Lenguaje declarativo (no marketing fluff) — los LLMs prefieren texto factual

**Output**: `.cache/<cliente>/<keyword-slug>/05-brief-geo-optimized.md`

### Fase 6 — QA final

**Skills**:
- `qa-bot` — verificación de coherencia, claims, datos
- Lighthouse via `toprank:seo-analysis` (si la página ya está publicada)

Checklist QA:
- [ ] H1 contiene keyword head (exact o variation natural)
- [ ] Title tag 55-60 caracteres, incluye keyword
- [ ] Meta description 150-160 caracteres, con CTA
- [ ] 5 secciones presentes + FAQ
- [ ] FAQ schema válido (validado en schema.org validator)
- [ ] Internal links: 3-5 contextuales a otras páginas del cliente
- [ ] External links: 2-3 a fuentes autoritativas
- [ ] Imágenes con alt text descriptivo + file name kebab-case
- [ ] Sin keyword stuffing (densidad < 2%)
- [ ] Datos/citas verificables (no inventadas)

### Output final del Workflow 2

Bundle entregable al cliente:
1. **Brief** (markdown o google doc)
2. **Schema JSON-LD** (listo para inyectar en `<head>`)
3. **Checklist GEO** post-publicación
4. **HTML preview** (si lo piden) — `OUTPUTS/<cliente>/<YYYY-MM-DD>-page-<keyword-slug>.html`

---

## Workflow 3 — Cluster programmatic

Generar N páginas (10-10,000) basadas en un template + data layer. Output: árbol de páginas en el repo del cliente.

### Fase 1 — Topic clustering + architecture

**Skills**:
- `/seo cluster <topic>` — descubre clusters semánticos
- Corey Haines `programmatic-seo` + `site-architecture` — hub-and-spoke design

**Output**:
- Lista de N keywords/variants con intent + volume + KD
- Architecture decision: 1 hub + N spokes, o multi-hub multi-spoke
- URL pattern: `/[topic-base]/[variant-slug]/` (kebab-case obligatorio)
- Internal linking schema (cada spoke linkea al hub + a 3-5 spokes hermanos)

**Decisión bloqueante**: el usuario aprueba el árbol propuesto antes de generar.

### Fase 2 — Template design

**Skills**:
- `/seo programmatic plan` + Corey `programmatic-seo`
- `page-builder` (para Astro/Next.js)

Template debe tener:
- 200-300 palabras únicas por variante mínimo ([`bibliography-tactics.md` §3](./bibliography-tactics.md))
- Schema dinámico (placeholders rellenados por data layer)
- Internal linking dinámico (hub + 3 hermanos según similaridad)
- Meta dinámicos
- Sitemap auto-generation

**Output**: código del template (Astro/Next.js page con frontmatter dinámico)

### Fase 3 — Data layer

CSV o JSON con N filas. Columnas obligatorias:
- `slug` (unique, kebab-case)
- `h1` (variation natural de la keyword)
- `title_tag`
- `meta_description`
- `intro` (50-80 palabras única)
- `section_1_title` + `section_1_content` (200-300 palabras únicas)
- ... (resto secciones)
- `faq` (array de 5-8 Q/A únicas por variante)
- `schema_extra` (campos específicos según tipo: product, location, etc.)

**Generación del contenido único**: aquí está el riesgo de thin content. Estrategia:
1. **Prompt LLM con variante + contexto cliente** para cada celda — no copy-paste
2. **Validar uniqueness**: hash de cada celda, alert si <5% diferencia entre variantes
3. **Sample human review**: al menos 10% de las variantes leídas por Alfonso antes de publicar

### Fase 4 — Bulk generation + publish

Por cada fila del data layer:
1. Renderizar template → HTML
2. Validar schema JSON-LD generado
3. Añadir a sitemap.xml
4. Setup internal linking (post-render pass)

Output: árbol de N páginas en `clients/<cliente>/seo/<cluster>/` o repo del cliente.

### Fase 5 — Post-publish

- Submit sitemap a GSC + Bing
- Monitor indexation rate primeros 7 días
- Si <80% indexadas en 7 días → revisar quality flags (probable thin content)
- Cada 30 días: `toprank:toprank-portfolio-review` sobre el cluster

---

## Verificación pre-entrega (ambos workflows)

- [ ] Brief / template tiene 5 secciones + FAQ
- [ ] Schema JSON-LD valida en schema.org validator
- [ ] H1 + title + meta cumplen límites
- [ ] Internal links presentes
- [ ] (Workflow 3) data layer validado uniqueness
- [ ] HTML output existe si fue requerido
