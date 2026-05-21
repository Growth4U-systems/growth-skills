# Reporting Templates

Plantillas para los HTML outputs de cada workflow. Todos generados vía skill `html-output` con tema Sancho default.

## Workflow 1 — Audit Report

**Path**: `OUTPUTS/<cliente>/<YYYY-MM-DD>-seo-audit.html`

**Estructura HTML**:

```
<header>
  <client logo + name>
  <title>Auditoría SEO — <cliente></title>
  <date + dominio auditado>
</header>

<section #executive-summary>
  <h2>Executive summary</h2>
  <ul> 5-7 bullets clave </ul>
  <metrics-cards>
    <card>Pages indexed: X</card>
    <card>Top query clicks: Y</card>
    <card>GEO score: Z/100</card>
    <card>Quick wins identified: 3-5</card>
  </metrics-cards>
</section>

<section #quick-wins>
  <h2>Quick wins prioritized</h2>
  <quick-win-card priority="critical|high|medium">
    <h3>Título acción</h3>
    <impact>+X% CTR esperado</impact>
    <effort>~30 min</effort>
    <action>
      <what>Qué cambiar</what>
      <where>Dónde (URL + selector)</where>
      <why>Por qué (data point concreto)</why>
    </action>
  </quick-win-card>
</section>

<section #roadmap-30-days>
  <h2>Roadmap 30 días</h2>
  <timeline>
    <phase weeks="1-2">Foundations + quick wins</phase>
    <phase weeks="3-4">Content optimization + schema</phase>
    <phase weeks="5+">Strategic GEO + link building</phase>
  </timeline>
</section>

<section #technical-audit collapsible>
  <h2>Audit técnico (Fase 2)</h2>
  <category-card name="Crawlability">...</category-card>
  <category-card name="Indexability">...</category-card>
  <category-card name="Technical/CWV">...</category-card>
  <category-card name="On-page">...</category-card>
  <category-card name="Schema">...</category-card>
  <category-card name="Content quality">...</category-card>
  <category-card name="Images">...</category-card>
  <category-card name="Links">...</category-card>
  <category-card name="Industry-specific">...</category-card>
</section>

<section #stack-manifest>
  <h2>Stack detection (Fase 2a) — precondición de handoff</h2>
  <stack-card>
    <cms>WordPress (confidence: high)</cms>
    <framework>unknown</framework>
    <cdn>Cloudflare</cdn>
    <server>cloudflare / PHP 8.5.2</server>
    <plugins>Divi, Yoast SEO, WPML</plugins>
    <third-party-scripts>GA4, Zendesk, Cookie consent, reCAPTCHA (46 scripts total, 23 external)</third-party-scripts>
  </stack-card>
  <implications>
    Para handoff a Martín: edits en `wp-content/themes/<theme>/`. Si Divi builder UI involucrada,
    cambios visuales en builder. Si plugins SEO Yoast presentes, respetar su schema generation.
  </implications>
  <raw-output>
    Generado vía `./scripts/stack-detector.sh <url>` — output completo en `.cache/<cliente>/02a-stack-manifest.md`.
  </raw-output>
</section>

<section #accessibility-audit>
  <h2>Accessibility (Fase 2b) — handoff a frontend</h2>
  <summary-card>
    <lighthouse-score>X/100</lighthouse-score>
    <wcag-target>WCAG 2.2 Level AA</wcag-target>
    <total-findings>N findings (X critical, Y high, Z medium, W low)</total-findings>
  </summary-card>
  <findings-table>
    <!-- ID | Issue | Severity | WCAG | Effort -->
  </findings-table>
  <findings-detail collapsible>
    <finding id="A11Y-01">
      <severity>critical</severity>
      <wcag>1.4.3 Contrast Minimum</wcag>
      <location>URL + selector + componente probable</location>
      <user-impact>...</user-impact>
      <fix-description>...</fix-description>
      <handoff-brief>
        <skill>frontend-design</skill>
        <files>...</files>
        <effort>5 min</effort>
        <verification>...</verification>
      </handoff-brief>
      <references>links WCAG</references>
    </finding>
  </findings-detail>
</section>

<section #performance-audit>
  <h2>Performance code (Fase 2c) — handoff a frontend</h2>
  <summary-card>
    <lighthouse-score>X/100</lighthouse-score>
    <cwv-snapshot>
      <lcp>4.2s mobile / 2.1s desktop</lcp>
      <inp>320ms mobile</inp>
      <cls>0.18 mobile</cls>
    </cwv-snapshot>
    <total-findings>N findings (X critical, Y high, Z medium)</total-findings>
  </summary-card>
  <findings-table>
    <!-- ID | Issue | CWV impacted | Current vs target | Effort -->
  </findings-table>
  <findings-detail collapsible>
    <finding id="PERF-01">
      <severity>critical</severity>
      <cwv>LCP</cwv>
      <current-value>4.2s mobile (target <2.5s)</current-value>
      <root-cause>...</root-cause>
      <fix-description>1. ... 2. ... 3. ...</fix-description>
      <handoff-brief>
        <skill>frontend-design + Chrome DevTools MCP</skill>
        <files>...</files>
        <effort>30-60 min</effort>
        <verification>...</verification>
        <tooling>cwebp, next/image, astro:assets</tooling>
      </handoff-brief>
      <impact-estimated>LCP -2.1s → -2.5s mejora</impact-estimated>
    </finding>
  </findings-detail>
</section>

<section #handoff-consolidated>
  <h2>Handoff técnico consolidado (accessibility + performance)</h2>
  <intro>
    Estos hallazgos NO los arregla g4u-seo. Requieren intervención de dev
    o de otra skill (typically `frontend-design` o Chrome DevTools MCP).
    Cada item es self-contained — un dev puede ejecutar sin re-auditar.
  </intro>
  <combined-table>
    <!-- ID | Type | Severity | Impact | Effort -->
  </combined-table>
  <processing-guide>
    <step>Para UI/diseño (contraste, focus): frontend-design skill</step>
    <step>Para assets (imágenes, fonts, bundles): Chrome DevTools MCP + repo edits</step>
    <step>Para Webflow / CMS: cambios en Designer + verificar PSI</step>
    <step>Verification post-fix: re-correr Lighthouse / PSI</step>
  </processing-guide>
</section>

<section #geo-audit>
  <h2>AI/GEO audit (Fase 3)</h2>
  <geo-score-card>
    <overall-score>Z/100</overall-score>
    <per-platform>
      <platform name="AI Overviews" score="...">...</platform>
      <platform name="ChatGPT" score="...">...</platform>
      <platform name="Perplexity" score="...">...</platform>
      <platform name="Gemini" score="...">...</platform>
      <platform name="Claude" score="...">...</platform>
    </per-platform>
  </geo-score-card>
  <gap-analysis>... gaps por plataforma ...</gap-analysis>
</section>

<section #geo-playbook>
  <h2>GEO playbook</h2>
  <on-page>5-section + FAQ schema deployment</on-page>
  <off-page>Reddit/YouTube/Medium strategy</off-page>
  <tracking>DataForSEO LLM mentions setup</tracking>
</section>

<section #baseline-metrics>
  <h2>Métricas baseline</h2>
  <metrics-grid> ... snapshots para re-audit 30/60/90 ... </metrics-grid>
</section>

<section #appendix collapsible>
  <h2>Apéndice — outputs raw</h2>
  <details><summary>Fase 1 TopRank</summary>...</details>
  <details><summary>Fase 2 AgriciDaniel</summary>...</details>
  <details><summary>Fase 3a TopRank GEO</summary>...</details>
  <details><summary>Fase 3b Corey AI-SEO</summary>...</details>
  <details><summary>Fase 3c DataForSEO LLM mentions</summary>...</details>
</section>

<footer>
  <attribution>Growth4U · SanchoCMO · g4u-seo skill</attribution>
  <generated-at>2026-MM-DD HH:MM CET</generated-at>
  <verification-checklist>
    [x] HTML válido
    [x] Las 4 fases con contenido
    [x] Quick wins accionables
    [x] Métricas concretas
  </verification-checklist>
</footer>
```

**Estilo**:
- Tema Sancho default — palette azul/dorado del design system
- Tipografía: Bangers (H1/H2 grandes), DM Sans (body), Source Sans 3 (meta)
- Cards con border + shadow Sancho
- Quick-win cards con color por prioridad (rojo crítico, naranja alto, amarillo medio)

## Workflow 2 — Page Brief

**Path**: `OUTPUTS/<cliente>/<YYYY-MM-DD>-page-<keyword-slug>.html`

**Estructura**:

```
<header>
  <client name>
  <title>Brief SEO — <keyword></title>
  <intent classification + volume + KD>
</header>

<section #serp-analysis>
  <h2>SERP analysis</h2>
  <top-10-table>...</top-10-table>
  <gaps-identified>...</gaps-identified>
</section>

<section #brief-structure>
  <h2>Estructura recomendada</h2>
  <h1-preview>Sugerencia H1</h1-preview>
  <section-1>...</section-1>
  <section-2>...</section-2>
  <section-3>...</section-3>
  <section-4>...</section-4>
  <section-5>...</section-5>
  <faq-list>5-8 Q/A pairs</faq-list>
</section>

<section #schema-jsonld>
  <h2>Schema JSON-LD</h2>
  <code-block lang="json">... listo para copy-paste al <head> ...</code-block>
</section>

<section #geo-checklist>
  <h2>GEO checklist post-publicación</h2>
  <ul> tareas con checkboxes ... </ul>
</section>

<section #qa-checklist>
  <h2>QA checklist</h2>
  <ul> 10 items pre-publish ... </ul>
</section>
```

## Workflow 4 — Blog Editorial Brief

**Path**: `OUTPUTS/<cliente>/<YYYY-MM-DD>-blog-<keyword-slug>.html`

**Estructura**:

```
<header>
  <client name>
  <title>Brief Blog Editorial — <keyword></title>
  <editorial-context>
    <piece-type>pillar | spoke | timely</piece-type>
    <target-length>2000-3000 words</target-length>
    <author>Person + sameAs</author>
    <calendar-slot>Week X of YYYY-MM</calendar-slot>
  </editorial-context>
</header>

<section #audience-research>
  <h2>Audience + SERP research</h2>
  <persona-derived>...</persona-derived>
  <serp-gaps>...</serp-gaps>
  <wedge-angle>El ángulo no cubierto por los top 10</wedge-angle>
</section>

<section #brief-structure>
  <h2>Estructura editorial</h2>
  <h1-preview>...</h1-preview>
  <hook>80-120 words narrative</hook>
  <section-1>Context + problem (300-400)</section-1>
  <section-2>Framework (300-500)</section-2>
  <section-3>How (500-800) ← MÁS LARGA</section-3>
  <section-4>Examples + counterpoints (300-500)</section-4>
  <section-5>Takeaways + soft CTA (200-300)</section-5>
  <faq-list>5-8 Q/A editorial tone</faq-list>
</section>

<section #tone-checklist>
  <h2>Tono editorial — checklist</h2>
  <ul> primera persona, frases <25 words, verbos activos, sin fluff, citas verificables </ul>
</section>

<section #schema-jsonld>
  <h2>Schema JSON-LD</h2>
  <required>BlogPosting + FAQPage + Person.sameAs + BreadcrumbList</required>
  <optional>HowTo si aplica</optional>
  <code-block lang="json">...</code-block>
</section>

<section #atomization-plan>
  <h2>Plan de atomización post-publicación</h2>
  <schedule>
    <day d="0">Artículo + LinkedIn post #1 + Twitter thread #1</day>
    <day d="2">LinkedIn post #2 (framework carousel)</day>
    <day d="5">Newsletter issue (si toca)</day>
    <day d="7">LinkedIn post #3</day>
    <day d="10">Twitter thread #2</day>
    <day d="14">Re-share LinkedIn #1 nuevo ángulo</day>
  </schedule>
  <pieces-detail>
    <piece type="linkedin">post copy ya redactado</piece>
    <piece type="twitter">thread con 8-10 tweets</piece>
    ...
  </pieces-detail>
</section>

<section #qa-checklist>
  <h2>QA pre-publicación</h2>
  <ul> tono editorial + schema válido + author E-E-A-T + citas reales </ul>
</section>
```

## Workflow 3 — Cluster Plan

**Path**: `OUTPUTS/<cliente>/<YYYY-MM-DD>-cluster-<topic-slug>.html`

**Estructura**:

```
<header>
  <client name>
  <title>Cluster SEO — <topic></title>
  <total pages + URL pattern>
</header>

<section #architecture>
  <h2>Arquitectura propuesta</h2>
  <tree-diagram>hub + spokes visualization</tree-diagram>
  <url-pattern>/[topic-base]/[variant]/</url-pattern>
  <internal-linking-rules>...</internal-linking-rules>
</section>

<section #data-layer>
  <h2>Data layer schema</h2>
  <columns-table>...</columns-table>
  <variant-count>N páginas a generar</variant-count>
  <uniqueness-strategy>...</uniqueness-strategy>
</section>

<section #template-preview>
  <h2>Template preview</h2>
  <code-block>Astro/Next.js page con frontmatter dinámico</code-block>
</section>

<section #qa-rules>
  <h2>QA rules pre-publish</h2>
  <ul>...</ul>
</section>

<section #monitoring>
  <h2>Post-publish monitoring</h2>
  <indexation-targets>...</indexation-targets>
  <review-cadence>...</review-cadence>
</section>
```

## Notas comunes

- **Idioma del output**: si el contexto cliente indica idioma (ES/EN/etc), generar el HTML en ese idioma. Default: español.
- **Branding cliente vs G4U**: el header usa logo + nombre del cliente. El footer atribuye a Growth4U.
- **Links absolutos**: todos los enlaces a recursos externos (papers, herramientas) con `target="_blank" rel="noopener"`.
- **Embeds**: si hay gráficos/charts, generar con Chart.js inline (no external CDN dependencies para que el HTML sea standalone).
- **Print-friendly**: media query @print que oculta collapsibles y expande todo — para que el cliente pueda imprimir si quiere.
