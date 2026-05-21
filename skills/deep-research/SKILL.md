---
name: deep-research
description: "Multi-source deep research with structured analysis and mandatory QA verification. Produces sourced, entity-by-entity style reports with executive summaries, taxonomies, and detailed breakdowns. Use when user says deep research, investiga [topic], research [topic] for [client], analisis de mercado, competitive analysis, benchmark [topic], or needs a comprehensive market/product/regulatory investigation. Do NOT use for quick factual lookups (use WebSearch directly) or for content creation (use seo-content or social-content instead)."
metadata:
  author: Alfonso Sainz de Baranda (Growth4U)
  version: "1.0"
  system: Growth Raistlin
---

# Deep Research

> Investigación multi-fuente estructurada en 7 fases. De pregunta vaga a informe verificado con fuentes.

## When to Use

- Market analysis for a client (banks, competitors, regulations)
- Product benchmarking (pricing, features, models)
- Regulatory / legal landscape research
- Technology landscape evaluation
- Any research that will be shared with a client or stakeholder

## Workflow Overview

```
SCOPE → SOURCES → EXTRACT → FRAMEWORK → DETAIL → QA → DELIVER
  1        2         3          4          5       6      7
```

Each phase produces an artifact. Never skip a phase. The output of each feeds the next.

---

## Phase 1: SCOPE

Define exactly what we're researching before touching any source.

### Inputs to Capture

| Field | Example (Overdrafts) |
|-------|---------------------|
| **Research question** | How do Spanish banks handle overdrafts? Opt-in vs tacit? |
| **For whom** | Mauricio (Monzo Spain GTM) |
| **Entities to cover** | All major retail banks in Spain (ING, BBVA, CaixaBank, N26...) |
| **Data points per entity** | Model type, activation, limits, costs, grace period, sources |
| **"Complete" means** | Every bank with >1M customers in Spain covered |
| **Output format** | Markdown report with executive summary + bank-by-bank breakdown |
| **Client folder** | `01-business/clients/[client]/research/` |

### Rules

- If user hasn't specified scope clearly, ask with `AskUserQuestion` before proceeding.
- Write scope as a 3-5 line brief at the top of the working document.
- Scope defines the stopping criteria — without it, research never ends.

---

## Phase 2: SOURCE DISCOVERY

Find ALL relevant sources before extracting any data.

### Search Strategy

Run **minimum 5 different search queries** varying:
- Language (Spanish + English for Spain topics)
- Angle (product name, regulatory term, comparison term, consumer forum)
- Source type (official sites, comparison platforms, regulators, news, forums)

### Source Categories

| Priority | Type | Example |
|----------|------|---------|
| 1 | **Official** | Bank websites, regulator (BdE, CNMV), company docs |
| 2 | **Comparison** | Rankia, Roams, HelpMyCash, Kelisto, BusconOmico |
| 3 | **News** | El Economista, CincoDías, Expansión, Bloomberg |
| 4 | **Legal/Regulatory** | BOE, Tribunal Supremo rulings, EU directives |
| 5 | **Community** | Reddit, Forocoches, Twitter/X, specialized forums |

### Output

Source inventory list: URL + what it likely contains + reliability rating (A/B/C).

**Minimum 10 sources** before proceeding. If <10, run more search queries.

### Phase 2b: SOCIAL PULSE (Conditional — `/last30days`)

**Activate when** the research topic has social/community dimension, recency matters, or user sentiment is relevant.

| Activate | Skip |
|----------|------|
| Community perception matters | Regulatory/legal research |
| Topic is trending or emergent | Historical analysis |
| Need market buzz beyond official data | Product feature comparison from official docs |
| User sentiment drives the insight | Topic too niche for social media |

**Process:**
1. Run `python3 ~/.claude/skills/last30days/scripts/last30days.py "[research topic]"` via Bash (foreground, 5-min timeout)
2. The script searches Reddit, X (Twitter), YouTube, and web for the last 30 days
3. Integrate findings as a "Social Pulse" source category (Priority 5b) in the source inventory
4. Feed social sentiment data into Phase 3 extraction alongside official sources

**If unsure**, ask the user: "This topic may benefit from a social pulse check (Reddit, X, YouTube last 30 days). Should I run it?"

---

## Phase 3: DATA EXTRACTION

Extract structured data from each source.

### Process

1. Open each source (`WebFetch` or `WebSearch` for key claims)
2. Extract data points matching the scope definition
3. Use **consistent field structure** across all entities
4. Note source URL for EVERY data point
5. Mark confidence: `verified` (official source) / `reported` (secondary) / `inferred` (deduced)

### Rules

- **One claim, one source minimum.** No unsourced claims.
- When sources conflict, note BOTH versions and flag for Phase 6 (QA).
- Extract raw data first — don't synthesize yet.
- For numerical data: always note the date/year of the data.

---

## Phase 4: FRAMEWORK & TAXONOMY

Create the organizing structure that makes the data intelligible.

### Process

1. Review all extracted data
2. Identify natural groupings, patterns, categories
3. Create a taxonomy or framework that explains the landscape
4. Build comparison tables

### Example (from Overdrafts research)

The data revealed **3 models**, not the assumed 2:
1. **Opt-In** (customer activates) — ING, N26, Openbank
2. **Opt-Out** (bank activates, customer can disable) — BBVA
3. **Pure Tacit** (no control) — Santander, Sabadell, etc.

### Output

- Taxonomy diagram or table
- Summary table (entities as rows, key dimensions as columns)
- Key insight: what's the non-obvious finding?

### Rule

The framework should **surprise the reader** with a non-obvious insight. If it just confirms what everyone already knows, dig deeper.

---

## Phase 5: DETAILED ANALYSIS

Entity-by-entity deep breakdown using the framework.

### Structure per Entity

Use a **consistent template** across all entities:

```markdown
### [Entity Name] — [Product Name]

**Type:** [Category from taxonomy]

**How it Works:**
- [Step-by-step user journey]

**Key Data:**
| Feature | Detail |
|---------|--------|
| [Dimension 1] | [Value] |
| [Dimension 2] | [Value] |

**Sources:**
- [Source 1](URL)
- [Source 2](URL)
```

### Document Structure

```markdown
# [Research Title]

**Date:** YYYY-MM-DD
**For:** [Stakeholder name and role]
**Research by:** Alfonso Sainz de Baranda (Growth4U)

---

## Executive Summary
[Key findings table + 2-3 paragraph narrative]

---

## [Taxonomy/Framework Section]
[Models, categories, comparison tables]

---

## Detailed Analysis

### Category A: [Name]
#### 1. [Entity] — [Product]
#### 2. [Entity] — [Product]

### Category B: [Name]
...

---

## Recommendations
[Actionable next steps for the stakeholder]

## Sources Index
[All sources cited, grouped by type]
```

### Rules

- Every entity gets the SAME template structure (no entity gets less coverage than another).
- Executive summary must be standalone — readable without the detail sections.
- Include a "Recommendations" section with actionable takeaways for the stakeholder.

---

## Phase 6: QA VERIFICATION (Mandatory)

**This phase is NOT optional. Every deep research MUST be QA'd.**

### Process

1. Save the analysis document to the client research folder
2. Invoke `/qa-bot` on the saved document
3. The QA bot will:
   - Extract all factual claims
   - Generate 10-15 verification questions (Deep QA mode)
   - Independently verify each claim via web search
   - Compare against the document
   - Produce a QA Report with confidence score

### After QA

| QA Verdict | Action |
|------------|--------|
| **PASS** (score >=9/10) | Proceed to Phase 7 |
| **NEEDS REVISION** (7-8.9/10) | Fix flagged issues, re-run QA on fixes only |
| **MAJOR ISSUES** (<7/10) | Rework affected sections, full QA re-run |

### Rules

- Fix ALL errors and discrepancies before delivering.
- For UNVERIFIABLE claims: either find a source, mark explicitly as "no public data available", or remove the claim.
- Save the QA report alongside the analysis: `QA-REPORT-[filename].md`

---

## Phase 7: DELIVER

### File Outputs

Save to `01-business/clients/[client]/research/`:

| File | Content |
|------|---------|
| `[topic]-analysis.md` | The full detailed analysis |
| `QA-REPORT-[topic]-analysis.md` | The QA verification report |

### Notion (if requested)

Create a Notion page under the client's workspace with the executive summary + link to full analysis.

### Handoff

Present to the user:
1. Executive summary (inline in chat)
2. Key non-obvious finding
3. QA confidence score
4. File paths where everything is saved
5. Notion link (if created)

---

## Quality Standards

| Standard | Minimum |
|----------|---------|
| Sources per entity | >= 2 (at least 1 official) |
| Total unique sources | >= 10 |
| QA confidence score | >= 8/10 before delivery |
| Claims without source | 0 (all must be sourced or flagged) |
| Conflicting data | Noted with both versions |
| Data freshness | Year noted for all metrics |
