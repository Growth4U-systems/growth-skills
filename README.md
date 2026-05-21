# growth-skills

> Open-source Claude Code skills by **[Growth4U](https://github.com/Growth4U-systems)** — a growth consultancy based in Madrid.

A curated collection of production-tested skills we use day-to-day. Drop them into your `.claude/skills/` directory and Claude Code picks them up automatically.

## What's a Claude Code skill?

A skill is a `SKILL.md` file (with optional `references/`, `scripts/`, and `assets/` folders) that you place in `.claude/skills/<skill-name>/`. Claude Code reads its frontmatter (name + description) and decides when to invoke it. When triggered, the skill's body and bundled resources become available to guide the work.

Skills make Claude Code reproducible across sessions and clients. Instead of re-explaining "how do we do X here" every time, you encode it once and let the model follow it.

## Skills included

See [INDEX.md](./INDEX.md) for the full table with descriptions, triggers, dependencies, and MCP requirements.

| Skill | What it does | When it triggers |
|-------|--------------|------------------|
| [g4u-seo](./skills/g4u-seo/) | End-to-end SEO orchestrator — auditorías, landings comerciales, blog editorial, programmatic clusters. Includes accessibility + performance handoff briefs. | "auditar SEO", "crear landing SEO", "rankear en ChatGPT/Perplexity", "GEO", "blog SEO", "cluster SEO" |
| [deep-research](./skills/deep-research/) | Multi-source deep research with structured analysis and mandatory QA verification. Produces sourced, entity-by-entity reports. | "deep research", "investiga", "research for", "competitive analysis", "benchmark" |
| [qa-bot](./skills/qa-bot/) | Critical review using Chain of Verification (CoVe). Finds errors, logic gaps, and unverifiable claims in any document. | "QA this", "review critically", "find the problems", "devil's advocate" |
| [token-hygiene](./skills/token-hygiene/) | Audit and reduce hidden token overhead in Claude Code conversations. Monthly skill + automation. | "audit my token usage", "token hygiene", "reduce context overhead" |

## Install

For any skill: copy the folder into `.claude/skills/` in your project (or `~/.claude/skills/` for global use). Start a new Claude Code session and the skill auto-loads.

```bash
# Install one specific skill globally
mkdir -p ~/.claude/skills
git clone https://github.com/Growth4U-systems/growth-skills.git /tmp/growth-skills
cp -R /tmp/growth-skills/skills/g4u-seo ~/.claude/skills/

# Or install all skills at once
cp -R /tmp/growth-skills/skills/* ~/.claude/skills/
```

To verify a skill loaded: `claude --help` or check `claude config list-skills` (commands depend on Claude Code version).

## Philosophy

These skills follow a few principles we've found work in real client engagements:

1. **Orchestrators over reinventors** — when 30+ specialized skills already exist in the ecosystem, write skills that compose them (g4u-seo) instead of duplicating logic.
2. **Empirical before prescriptive** — detect actual stack/state before generating recommendations (see `g4u-seo` stack detection).
3. **Handoff briefs over auto-fixes** — diagnose deeply, but let the human (or another skill) execute. Each finding includes severity, location, fix steps, recommended skill, files to touch, effort estimate, verification method.
4. **Doctrine over defaults** — every output respects the same conventions (5-section + FAQ schema for SEO pages, HTML output for client deliverables, etc.).
5. **Context-aware without hardcoding** — skills read your client/project context if you point them to it, but never assume structure or create context themselves.

## Contributing

Open an issue or PR. Skills should be:
- Self-contained (work in any `.claude/skills/` directory)
- Documented (SKILL.md frontmatter + clear body)
- Tested (real-world use case backing the skill)
- Honest about dependencies (MCPs, API keys, external tools)

## Related work

- [Anthropic's official skills](https://github.com/anthropics/skills) — canonical examples and references
- [AY Skills by Walid Boulanouar](https://github.com/walidboulanouar/Ay-Skills) — well-curated collection by AY Automate
- [AgriciDaniel claude-seo](https://github.com/AgriciDaniel/claude-seo) — full SEO suite (used by `g4u-seo` as one of its underlying engines)
- [Corey Haines marketing skills](https://github.com/coreyhaines/) — comprehensive marketing skill set

## License

MIT — see [LICENSE](./LICENSE).

## About Growth4U

Growth consultancy based in Madrid. We help startups and scale-ups in B2B SaaS, fintech, and regulated industries.

- Website: [growth4u.io](https://growth4u.io)
- Founder: [Alfonso Sainz de Baranda](https://linkedin.com/in/alfonsosainzdebaranda)
- More tools: [Growth4U-systems on GitHub](https://github.com/Growth4U-systems)
