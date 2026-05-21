# Skills Index

Detailed catalog of all skills in this repo. For installation see [README.md](./README.md).

---

## Categories

- [SEO + content](#seo--content)
- [Research + verification](#research--verification)
- [Productivity + hygiene](#productivity--hygiene)

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

## Roadmap

Future skills we may release (currently private):

- `html-output` — universal HTML output skill with theme system (Sancho, G4U, Minimal, Dark)
- `kickoff-project` — initialize a new client project with templated structure
- `sync-notion-tasks` — sync Claude Code sessions ↔ Notion Tasks DB
- `mental-models-os` — 80 mental models with chaining commands (`/think`, `/chain`, `/compare`)

Want any of these prioritized? [Open an issue](https://github.com/Growth4U-systems/growth-skills/issues).
