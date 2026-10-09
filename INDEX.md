# Skills Index

Detailed catalog of all skills in this repo. For installation see [README.md](./README.md).

---

## Categories

- [SEO + content](#seo--content)
- [Research + verification](#research--verification)
- [Productivity + hygiene](#productivity--hygiene)
- [Marketing documental: 25 skills](#marketing-documental-25-skills)

Catálogo actual: 29 skills. Las cuatro fichas históricas se conservan; las 25 documentales se verifican separadamente.

---

## SEO + content

### [g4u-seo](./skills/g4u-seo/)

End-to-end SEO orchestrator. Composes the 30+ specialized SEO skills already available in the Claude Code ecosystem (AgriciDaniel `/seo`, Corey Haines marketing skills, TopRank suite) into 4 reusable workflows with G4U doctrine layered on top.

**4 workflows**:

1. **Auditoría completa** — 4 fases con sub-fases para stack detection empírico (2a), accessibility (2b), performance code (2c). Genera handoff briefs ejecutables para que un dev arregle accessibility/performance con `frontend-design` skill o Chrome DevTools MCP. No arregla — solo diagnostica con briefs específicos al stack detectado.
2. **Landing comercial** — 6 fases: keyword expansion → SERP analysis → brief 5 secciones + FAQ → schema JSON-LD → GEO optimization → QA. Intent transactional, schema Product/Service, CTA fuerte.
3. **Cluster programmatic** — hub-and-spoke arquitectura, 200-300 palabras únicas mínimo por variante, schema dinámico.
4. **Blog editorial** — 7 fases: editorial context → keyword informacional → SERP+audience → brief 5 secciones tono narrativo → schema BlogPosting + Person.sameAs → GEO → QA → atomization plan (D/D+2/D+5/D+7/D+10/D+14 a LinkedIn + Twitter + newsletter + lead magnet).

**Triggers**: "auditar SEO", "audit SEO", "crear landing SEO", "página SEO", "artículo de blog SEO", "rankear en ChatGPT/Perplexity/AI Overviews", "GEO", "AEO", "cluster SEO", "programmatic SEO", "improve organic traffic", "por qué no rankeo".

**Doctrina G4U incluida**:
- 5 secciones + FAQ schema obligatorio (sweet spot empírico testeado en ChatGPT/Perplexity/Claude)
- Output HTML cliente vía `html-output` skill por defecto
- GEO no opcional (AI traffic convierte 4.4x-23x más que organic)
- Quick wins primero (3-5 priorizadas por impacto × esfuerzo)
- Handoff briefs estructurados — severity, WCAG/CWV, location, root cause, fix, skill recomendada, files, effort, verification

**Dependencias**:
- Recomendado: DataForSEO MCP (SERP, keyword volume, backlinks, LLM mentions tracking)
- Recomendado: Chrome DevTools MCP (accessibility + performance audits)
- Opcional: Google Search Console API (via service account)
- Opcional: PageSpeed Insights API
- Opcional: Notion MCP (sync entregables)

**Composes (no requiere instalar, recomienda)**:
- [AgriciDaniel `/seo` suite](https://github.com/AgriciDaniel/claude-seo) — 24 sub-skills
- Corey Haines marketing skills — 6 SEO-relevantes
- TopRank suite — 9 skills SEO con GSC + PSI reales

**Scripts incluidos**:
- `stack-detector.sh` — detecta CMS / framework / CDN / plugins / third-party scripts vía `curl + grep`. Validado contra WordPress + Divi + WPML, Webflow, Astro + Netlify, Next.js + Vercel, Shopify.
- `audit-runner.sh` — orchestration helper para el pipeline de audit
- `page-brief-generator.py` — template generator para brief de página
- `bibliography-extractor.py` — re-genera la bibliografía desde una Notion DB (opcional)

**Tamaño**: 1 SKILL.md (119 líneas) + 8 references (en total ~2700 líneas) + 4 scripts. La SKILL.md es liviana — las references se cargan on-demand cuando la skill se activa.

---

## Research + verification

### [deep-research](./skills/deep-research/)

Multi-source deep research with structured analysis and mandatory QA verification. Produces sourced, entity-by-entity style reports with executive summaries, taxonomies, and detailed breakdowns.

**Triggers**: "deep research", "investiga [topic]", "research [topic] for [client]", "analisis de mercado", "competitive analysis", "benchmark [topic]".

**Use it for**: comprehensive market investigations, regulatory analysis, competitive landscapes, product deep-dives.

**Do NOT use it for**: quick factual lookups (use WebSearch directly) or content creation (use seo-content or social-content instead).

**Dependencies**: WebSearch + WebFetch tools. Optional: domain-specific MCPs (Crunchbase, Apollo, etc).

**Pairs well with**:
- `qa-bot` — for verifying findings before publishing
- `g4u-seo` — feed research into Fase 2 (SERP analysis) of page creation

---

### [qa-bot](./skills/qa-bot/)

Critical review using **Chain of Verification (CoVe)** in 4 phases: extract topics → generate verification questions → research independently → compare against the document. Finds errors, logic gaps, missing elements, and unverifiable claims.

**Triggers**: "QA this", "review critically", "find the problems", "devil's advocate", "QA bot", "QA [file]".

**Modes**:
- **Quick QA**: 5-7 verification questions
- **Deep QA**: 10-15 verification questions (default for substantive documents)

**Use it for**: validating reports before sending to clients, peer-reviewing your own analysis, fact-checking research.

**Dependencies**: WebSearch + WebFetch for independent verification.

**Pairs well with**:
- `deep-research` — verify the report before publishing
- `g4u-seo` — QA briefs and audits before client delivery

---

## Productivity + hygiene

### [token-hygiene](./skills/token-hygiene/)

Audit and reduce the hidden token overhead in every Claude Code conversation. Monthly skill + launchd automation for macOS.

**What it does**: scans `~/.claude/` (settings, projects, history) for token-bloating patterns — bloated MEMORY.md, redundant CLAUDE.md duplications, oversized PreToolUse hooks, etc. Generates a report with concrete reductions.

**Triggers**: "audit my token usage", "token hygiene", "reduce context overhead", "why are my conversations so expensive".

**Cadence**: monthly via launchd plist (included). Manual invocation anytime.

**Dependencies**: macOS launchd (for automation). Manual run works on any OS.

**Pairs well with**: ANY skill — keeping token usage lean makes everything faster and cheaper.

---

## Skill connection diagram

```
                  ┌─────────────────────┐
                  │   deep-research     │
                  │  (gather context)   │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │     g4u-seo         │
                  │ (use research +     │
                  │  produce output)    │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │      qa-bot         │
                  │  (verify output     │
                  │  before client)     │
                  └─────────────────────┘

  token-hygiene runs orthogonally — keeps the whole stack lean
```

Suggested workflow for a new SEO engagement:
1. `deep-research` → competitive landscape + audience research
2. `g4u-seo Workflow 1` → full audit + handoff briefs
3. `g4u-seo Workflow 2 or 4` → produce landings / blog posts based on audit findings
4. `qa-bot` → verify deliverables before sending to client
5. `token-hygiene` → monthly, keeps your Claude Code sessions efficient

---

## Versions

| Skill | Version | Last updated |
|-------|---------|--------------|
| g4u-seo | 1.0.0 (iteración 3) | 2026-05-21 |
| deep-research | as published in [ai-research-skills](https://github.com/AlfonsoSBLA/ai-research-skills) | 2026 |
| qa-bot | as published in [ai-research-skills](https://github.com/AlfonsoSBLA/ai-research-skills) | 2026 |
| token-hygiene | as published in [claude-token-hygiene](https://github.com/AlfonsoSBLA/claude-token-hygiene) | 2026 |

## Marketing documental: 25 skills

Versión 2.0.0. Datos suministrados; sin claves, llamadas externas ni acciones ejecutadas.

| ID | Skill | Uso |
|---|---|---|
| 01 | [g4u-plan-cortes-video](skills/g4u-plan-cortes-video/SKILL.md) | Plan de cortes de vídeo |
| 02 | [g4u-brief-seo](skills/g4u-brief-seo/SKILL.md) | Brief SEO con datos aportados |
| 03 | [g4u-contenido-con-fuentes](skills/g4u-contenido-con-fuentes/SKILL.md) | Brief y redacción con fuentes |
| 04 | [g4u-email-revision-humana](skills/g4u-email-revision-humana/SKILL.md) | Borrador genérico de email |
| 05 | [g4u-ficha-experimento](skills/g4u-ficha-experimento/SKILL.md) | Ficha de experimento |
| 06 | [g4u-plan-investigacion](skills/g4u-plan-investigacion/SKILL.md) | Plan de investigación de audiencia |
| 07 | [g4u-guion-entrevista](skills/g4u-guion-entrevista/SKILL.md) | Guion de entrevista no inductiva |
| 08 | [g4u-sintesis-entrevistas](skills/g4u-sintesis-entrevistas/SKILL.md) | Síntesis de notas y contradicciones |
| 09 | [g4u-encuesta-diagnostico](skills/g4u-encuesta-diagnostico/SKILL.md) | Encuesta breve de diagnóstico |
| 10 | [g4u-comparativa-alternativas](skills/g4u-comparativa-alternativas/SKILL.md) | Comparativa de alternativas con evidencia |
| 11 | [g4u-posicionamiento](skills/g4u-posicionamiento/SKILL.md) | Documento de posicionamiento provisional |
| 12 | [g4u-matriz-mensajes](skills/g4u-matriz-mensajes/SKILL.md) | Matriz de beneficios, pruebas y objeciones |
| 13 | [g4u-mapa-contenidos](skills/g4u-mapa-contenidos/SKILL.md) | Mapa de contenidos por preguntas e intención |
| 14 | [g4u-calendario-editorial](skills/g4u-calendario-editorial/SKILL.md) | Calendario editorial por dependencias |
| 15 | [g4u-reutilizacion-activo](skills/g4u-reutilizacion-activo/SKILL.md) | Plan de reutilización de un activo fuente |
| 16 | [g4u-brief-campana](skills/g4u-brief-campana/SKILL.md) | Brief de campaña con dependencias y límites |
| 17 | [g4u-estructura-landing](skills/g4u-estructura-landing/SKILL.md) | Estructura y textos de una landing |
| 18 | [g4u-revision-conversion](skills/g4u-revision-conversion/SKILL.md) | Revisión de fricciones de una página |
| 19 | [g4u-edicion-texto](skills/g4u-edicion-texto/SKILL.md) | Edición de texto con registro de cambios |
| 20 | [g4u-brief-recurso-descargable](skills/g4u-brief-recurso-descargable/SKILL.md) | Brief de recurso descargable desde necesidades |
| 21 | [g4u-secuencia-bienvenida](skills/g4u-secuencia-bienvenida/SKILL.md) | Secuencia de bienvenida con reglas de salida |
| 22 | [g4u-secuencia-educativa](skills/g4u-secuencia-educativa/SKILL.md) | Secuencia educativa según dudas |
| 23 | [g4u-onboarding-primer-valor](skills/g4u-onboarding-primer-valor/SKILL.md) | Plan de onboarding hacia una primera tarea |
| 24 | [g4u-plan-medicion](skills/g4u-plan-medicion/SKILL.md) | Plan de medición con diccionario de métricas |
| 25 | [g4u-informe-resultados](skills/g4u-informe-resultados/SKILL.md) | Informe de resultados y decisiones limitadas |

Cada carpeta incluye contrato, ejemplo completo, casos límite y licencia. No sustituyen al orquestador g4u-seo ni a investigación real.

## Roadmap

Future skills we may release (currently private):

- `html-output` — universal HTML output skill with theme system (Sancho, G4U, Minimal, Dark)
- `kickoff-project` — initialize a new client project with templated structure
- `sync-notion-tasks` — sync Claude Code sessions ↔ Notion Tasks DB
- `mental-models-os` — 80 mental models with chaining commands (`/think`, `/chain`, `/compare`)

Want any of these prioritized? [Open an issue](https://github.com/Growth4U-systems/growth-skills/issues).
