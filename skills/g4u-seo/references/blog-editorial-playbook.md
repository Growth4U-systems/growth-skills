# Workflow 4 — Blog editorial

Para artículos de blog editoriales/educacionales que encajan en un calendario recurrente. Distinto de Workflow 2 (landing comercial) en tono, schema, y post-publish.

Output bundle: brief editorial + schema JSON-LD + atomization plan + (opcional) borrador del artículo.

---

## Cuándo usar este workflow vs Workflow 2

| Característica | Workflow 2 (Landing) | Workflow 4 (Blog) |
|---------------|---------------------|-------------------|
| Intent | Commercial / transactional | Informational / educational |
| Tono | Persuasivo, conversion-focused | Narrativo, educativo |
| CTA | Fuerte, top + bottom + sticky | Suave, contextual, no intrusivo |
| Schema | Product / Service / Offer | BlogPosting / Article / HowTo |
| Frecuencia | Una vez, raramente cambia | Recurrente (semanal / quincenal) |
| Encaje | Standalone | En calendario editorial + atomización |
| Long-term | Hits "evergreen" comercial | Construye autoridad + tráfico orgánico |

Si dudas: pregúntale al usuario. _"¿Es una landing comercial (intent transactional) o un blog editorial (intent informacional)?"_

---

## Inputs requeridos

| Input | De dónde | Bloqueante |
|-------|----------|------------|
| Keyword head + supporting | Usuario | SÍ |
| Tipo de blog (pillar / cluster / timely) | Usuario o calendario | NO (default pillar si no hay calendario) |
| Calendario editorial existente | Contexto cliente o `content-strategy` skill | NO (genero standalone si no hay) |
| Brand voice / autor | Contexto cliente | NO (uso default cliente o "Equipo de") |
| Cadencia esperada | Usuario | NO |

---

## Fase 0 — Editorial context (NUEVA — solo en Workflow 4)

Antes de empezar, pregunto al usuario:

1. **Tipo de pieza editorial**:
   - **Pillar / cornerstone**: artículo extenso (2000-3000 palabras) que cubre un tema completo. Pocos al año.
   - **Cluster spoke**: artículo medio (800-1500) que orbita alrededor de un pillar. Cadencia regular.
   - **Timely / news**: artículo corto (500-1000) sobre algo del momento. Tendencia o noticia.

2. **¿Existe calendario editorial?** Si sí, en qué ranura encaja este artículo.

3. **¿Quién firma?** Autor real con E-E-A-T (preferido) o "Equipo de X" (acepta pero peor para GEO).

4. **Atomización esperada**: ¿se va a repurposear a LinkedIn / Twitter / newsletter / video? Si sí, lo tengo en cuenta desde el brief.

Si el usuario no tiene respuestas, uso defaults razonables y aviso.

---

## Fase 1 — Keyword expansion (intent INFORMACIONAL)

**Skills**:
- Corey Haines `keyword-research` — 6 Circles, **filtrado a intent informational + commercial-investigation**
- `toprank:keyword-research` — DataForSEO volumes
- `dataforseo_labs_search_intent` — clasificación automática

**Filtros editoriales clave (distintos de Workflow 2)**:
- Excluir intent transactional puro (esos van a landing)
- Priorizar long-tail con **modificadores informacionales**: "qué es", "cómo", "por qué", "guía", "tutorial", "ejemplos", "diferencia entre"
- Priorizar volumen medio (200-2000) con KD < 30 si autoridad del cliente es media-baja

**Output**: `.cache/<cliente>/<keyword-slug>/01-keywords.md` con 1 head + 5-10 supporting clasificados por intent.

---

## Fase 2 — SERP + audience research

**Skills**:
- `/seo competitor-pages` o NotebookLM workflow (más rápido)
- DataForSEO `serp_organic_live_advanced` + `content_analysis_search`
- `deep-research` skill (opcional, para tema complejo)

**Foco editorial específico**:
- ¿Qué pregunta latente está detrás de la keyword? (no solo qué keyword se busca, sino qué problema viene a resolver el lector)
- ¿Qué ángulos cubren los top 10? ¿Cuál ángulo NO cubre nadie? → ahí está el wedge
- ¿Quién es el lector? (job title, sector, momento del problema)
- ¿Qué objeciones probables tendrá?

**Output**: `.cache/<cliente>/<keyword-slug>/02-serp-audience.md` con tabla top 10 + gaps + audience persona derivado.

---

## Fase 3 — Brief editorial (estructura 5 + FAQ con tono narrativo)

**Skills**:
- Corey Haines `seo-page` (estructura) + `copywriting` (narrativa)
- `direct-response-copy` (solo para hook y CTA suave, NO para todo el body)
- `brand-voice` — aplicar tono del cliente si existe

**Estructura — misma 5 + FAQ que Workflow 2, pero con tono editorial**:

```
H1: <keyword exact match o variación natural>

[Hook narrativo 80-120 palabras: anécdota o data point sorprendente + 
 promesa de lo que el lector aprende. NO usar copy de venta aquí.]

H2: Sección 1 — El contexto / el problema (300-400 palabras)
   [Establece el problema. Cuenta una historia o usa un dato sorpresivo.
    Conecta con el día a día del lector. Lenguaje narrativo, no listado.]

H2: Sección 2 — Concepto / framework (300-500 palabras)
   [Define el concepto. Aquí SÍ caben listas + diagramas + esquemas.]

H2: Sección 3 — Cómo aplicarlo / proceso (500-800 palabras)
   [La parte más práctica del artículo. Pasos numerados con detalle.
    Si aplica, mini casos o ejemplos en cada paso.]

H2: Sección 4 — Casos / ejemplos / counterpoints (300-500 palabras)
   [2-3 ejemplos reales, idealmente verificables. Cita fuentes.
    Si hay contrapuntos, mencionarlos — refuerza autoridad.]

H2: Sección 5 — Takeaways / siguientes pasos (200-300 palabras)
   [Síntesis de aprendizajes + qué hacer mañana.
    CTA SUAVE: "si quieres profundizar, lee X" o "suscríbete a newsletter".
    NO hard sell.]

H2: Frequently asked questions
   [5-8 Q/A. Tono editorial — respuesta corta y útil, no pitch.]
```

**Diferencia crítica con Workflow 2**: en blog la **Sección 3 es la más larga** (es donde el lector saca el valor). En landing la **Sección 5 es la más fuerte** (CTA).

**Tono — checklist editorial**:
- [ ] Primera persona ("nosotros" plural si es brand) o tercera neutra. Evitar "tú" agresivo
- [ ] Frases <25 palabras
- [ ] Verbos en presente activo
- [ ] Cero marketing fluff ("revolutionary", "game-changing", "best-in-class")
- [ ] Cero exageraciones sin dato detrás
- [ ] Citas con fuente verificable (no inventar)

**Output**: `.cache/<cliente>/<keyword-slug>/03-brief.md`

---

## Fase 4 — Schema editorial

**Skills**: `toprank:schema-markup-generator` + `/seo schema`

**Schema obligatorio**:
- `BlogPosting` o `Article` (NewsArticle si timely) — con `headline`, `image`, `author`, `datePublished`, `dateModified`, `publisher`
- `FAQPage` (sección FAQ)
- `BreadcrumbList`
- `Person` (autor) con `sameAs` a LinkedIn/Twitter/etc — crítico para E-E-A-T en GEO

**Schema opcional según contenido**:
- `HowTo` si la Sección 3 es realmente un proceso paso a paso (ojo: el HowTo schema requiere imágenes por paso)
- `Course` si es educacional formal
- `Review` si reseña algo

**Output**: `.cache/<cliente>/<keyword-slug>/04-schema.json`

---

## Fase 5 — GEO optimization

**Misma que Workflow 2** — ver [`geo-citations-playbook.md`](./geo-citations-playbook.md):
- Summary statement al inicio de cada H2 (citable por LLM)
- Datos numéricos concretos por sección
- Lenguaje declarativo
- External links autoritativos (.gov, .edu, papers verificables)

**Adicional para blog**: el `author Person` schema con `sameAs` es CRÍTICO para que el LLM atribuya autoridad. Si el cliente firma con "Equipo de X" sin Person identificable, GEO sufre.

---

## Fase 6 — QA editorial

**Skills**: `qa-bot` + `copy-editing` (Corey)

Checklist específico blog:
- [ ] Hook engancha en primeras 100 palabras
- [ ] Sección 3 tiene 500+ palabras (mayor peso editorial)
- [ ] Lenguaje narrativo, sin tono publicitario
- [ ] Citas con fuente real (no inventadas)
- [ ] Internal links 3-5: hub si es spoke, spokes si es hub
- [ ] External links 2-3 autoritativos
- [ ] Author bio firmando con E-E-A-T (no "Equipo de")
- [ ] Imagen hero + 2-3 imágenes inline con alt text descriptivo
- [ ] BlogPosting schema válido con Person.sameAs
- [ ] CTA al final es suave y contextual (newsletter, lead magnet, NO "compra ya")

---

## Fase 7 — Atomization plan (NUEVA — única de blog)

Tras publicar, el artículo se descompone a otros canales. Lo planifico desde el brief.

**Skills**:
- `content-atomizer` — orquesta el atomization
- `social` o `content-strategy` para schedule

**Jerarquía atomization estándar**:

```
1 pillar article (2000-3000 palabras)
  ↓
3-5 LinkedIn posts
  - Post 1: contrarian take del hook
  - Post 2: framework de Sección 2 (carousel)
  - Post 3: lista de los pasos de Sección 3 (text post)
  - Post 4: case study de Sección 4
  - Post 5: takeaways de Sección 5

2-3 Twitter threads
  - Thread 1: 5-7 tweets con el framework
  - Thread 2: 8-10 tweets con los pasos detallados

1 newsletter issue (si el cliente tiene newsletter)
  - TL;DR + link al artículo completo

1-2 video scripts cortos
  - Reels / Shorts con la sección más visual

1 lead magnet derivado (opcional)
  - Si el artículo es pillar, descomponer a PDF/checklist
```

**Schedule recomendado** (a partir de publicación día D):
- D: publicar artículo + first LinkedIn post + tweet primer thread
- D+2: LinkedIn post #2 + cross-post a otros canales
- D+5: newsletter issue (si toca)
- D+7: LinkedIn post #3
- D+10: Twitter thread #2
- D+14: re-share LinkedIn post #1 con nuevo ángulo

**Output**: `.cache/<cliente>/<keyword-slug>/07-atomization-plan.md`

---

## Output final del Workflow 4

Bundle entregable:

1. **Brief editorial completo** (markdown)
2. **Schema JSON-LD** listo para inyectar
3. **Atomization plan** con 5-7 piezas derivadas planificadas
4. **HTML preview** (si lo piden) — `OUTPUTS/<cliente>/<YYYY-MM-DD>-blog-<keyword-slug>.html`
5. **(Opcional)** Borrador del artículo redactado — pedir explícitamente, si no solo brief

Si el cliente tiene calendario editorial:
- Confirmo en qué slot encaja
- Actualizo el calendario (vía Notion si está ahí, o markdown si está en repo cliente)
- Marco depend-on con los atomization derivados (días D+2, D+5, etc.)

---

## Integración con calendario editorial (si existe)

Si el contexto cliente apunta a un calendario editorial (típicamente en Notion DB o markdown), invoco `content-strategy` skill al inicio para:

1. Confirmar que el artículo encaja en una ranura existente
2. Si no, proponer la ranura nueva y pedir confirmación
3. Tras producir el brief, actualizar el calendario con el slug del artículo

Si no hay calendario y el cliente quiere uno: ofrecer construir uno separadamente con `content-strategy` skill — NO mezclar con este workflow.

---

## Verificación pre-entrega

- [ ] Brief tiene 5 secciones + FAQ con longitudes editoriales (más largo en S3, menos en S5)
- [ ] Tono editorial verificado (no marketing fluff)
- [ ] Schema BlogPosting + FAQPage + Person válidos
- [ ] Author tiene E-E-A-T identifiable (Person.sameAs real, no inventado)
- [ ] Atomization plan con 5-7 piezas + schedule
- [ ] Internal/external links respetan jerarquía hub-spoke si aplica
- [ ] Citas verificables (no fabricated)
