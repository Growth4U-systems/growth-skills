# Claude Code Token Hygiene

**Your Claude Code conversations are wasting 30-50% of tokens on system context you don't need.**

Every conversation loads CLAUDE.md, MEMORY.md, skill descriptions, MCP tool listings, and hooks — before you type a single word. On a typical power-user setup, that's **15,000-35,000 tokens of overhead per conversation**.

This skill audits that overhead and tells you exactly where to cut.

---

## The Problem

```
You type: "fix the bug in auth.ts"

What Claude actually processes:
  ├── CLAUDE.md instructions        ~8,000 tokens
  ├── MEMORY.md auto-memory         ~5,000 tokens
  ├── 89 skill descriptions         ~6,000 tokens
  ├── 7 MCP servers (220 tools)     ~3,300 tokens
  ├── Hooks & system reminders      ~2,000 tokens
  ├── Your message                      ~20 tokens
  └── Total                        ~24,320 tokens  ← before Claude even thinks
```

On Opus at $15/M output tokens, that overhead costs **real money** on every conversation.

## The Solution

A monthly audit that measures your system context, flags what's bloated, and recommends specific cuts:

```
Token Hygiene Report — 2026-03-05

┌──────────────┬───────────────┬────────┬─────────────┐
│ Metric       │ Value         │ Status │ Tokens Est. │
├──────────────┼───────────────┼────────┼─────────────┤
│ CLAUDE.md    │ 123 lines/6KB │   ✅   │ ~1,600      │
│ MEMORY.md    │ 90 lines/5KB  │   ✅   │ ~1,350      │
│ Skills       │ 82            │   🟡   │ ~5,330      │
│ MCP servers  │ 5             │   ✅   │ ~1,125      │
│ Stale logs   │ 0             │   ✅   │ —           │
│ Total        │               │        │ ~9,405      │
└──────────────┴───────────────┴────────┴─────────────┘

↓ Down from ~30,000 tokens (previous audit)
```

## Real Results

I ran this on my own setup and reduced overhead from **~30,000 to ~15,000 tokens per conversation** — a 50% reduction:

| What I did | Savings | Time |
|-----------|---------|------|
| Compressed CLAUDE.md (713→123 lines) | ~6,700 tokens | 15 min |
| Compressed MEMORY.md (296→90 lines) | ~4,300 tokens | 10 min |
| Removed 3 unused MCP servers | ~2,000 tokens | 5 min |
| Removed 4 duplicate skills | ~300 tokens | 2 min |
| Disabled cloud MCP integrations | ~600 tokens | 1 min |
| **Total** | **~14,000 tokens** | **~33 min** |

---

## Quick Start (2 minutes)

### Option 1: Just run it manually

Copy `SKILL.md` to your project and ask Claude:

```
You: "Run the token-hygiene skill"
```

Claude will measure your system context and report what to optimize.

### Option 2: Install as a project skill

```bash
# In your Claude Code project
mkdir -p 00-system/skills/token-hygiene
cp SKILL.md 00-system/skills/token-hygiene/SKILL.md
```

Now you can trigger it anytime with:
- "token hygiene"
- "audit my tokens"
- "context audit"

### Option 3: Automated monthly audit (recommended)

Set up a scheduled task that runs the audit monthly and emails you the report.

```bash
# 1. Copy files to your project
mkdir -p .claude/scheduler-scripts
cp token-hygiene.sh .claude/scheduler-scripts/
chmod +x .claude/scheduler-scripts/token-hygiene.sh

# 2. Edit the script — set your project directory
# Open .claude/scheduler-scripts/token-hygiene.sh
# The PROJECT_DIR defaults to $(pwd), or set CLAUDE_PROJECT_DIR env var

# 3. Set up monthly schedule (macOS)
cp com.claude.schedule.token-hygiene.plist ~/Library/LaunchAgents/
# Edit the plist — change the project path and email address
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude.schedule.token-hygiene.plist

# 4. Verify it's loaded
launchctl list | grep token-hygiene
```

For **Linux/cron**:
```bash
# Monthly on the 1st at 9:30 AM
echo "30 9 1 * * cd /path/to/project && .claude/scheduler-scripts/token-hygiene.sh" | crontab -
```

---

## What It Checks

| Check | What it measures | Why it matters |
|-------|-----------------|----------------|
| **CLAUDE.md** | Size in bytes | Loaded in full on every conversation. Reference sections, old command lists, and stale instructions waste tokens. |
| **MEMORY.md** | Line count | Auto-memory grows silently. After 200 lines, detailed entries should move to topic files. |
| **Skills** | Installed count | Each skill's description is listed in the system prompt (~65 tokens each). 90 skills = 5,850 tokens of listings. |
| **MCP servers** | Server + tool count | Every registered tool appears in the deferred tools list (~15 tokens each). One server with 85 tools = 1,275 tokens. |
| **Daily logs** | Files older than 30 days | Stale logs don't cost tokens directly but slow down file operations and clutter the workspace. |

## Common Optimization Patterns

### 1. Split CLAUDE.md into core + reference

**Before** (713 lines, 29KB):
```markdown
# My Project
## Instructions (essential)
## MCP Reference (rarely needed)
## Repository Structure (rarely needed)
## All Commands (rarely needed)
## Framework Docs (rarely needed)
```

**After** (123 lines, 6KB):
```markdown
# My Project
## Instructions (essential)
## Reference → see docs/reference.md
```

Move anything you don't need in **every** conversation to a separate file. Claude can read it on-demand when needed.

### 2. Compress MEMORY.md with topic files

**Before** (296 lines):
```markdown
## Client: Acme
- 15 lines of detailed history
## Client: Globex
- 12 lines of detailed history
## OAuth Troubleshooting
- 20 lines of debugging notes
```

**After** (90 lines):
```markdown
## Clients → memory/client-details.md
## OAuth → memory/oauth-notes.md
```

Keep operational rules in MEMORY.md. Move detailed reference to topic files.

### 3. Remove duplicate and unused skills

```bash
# Find duplicates (same skill from plugin + manual install)
ls ~/.claude/skills/ | sort | uniq -d

# Check for skills you never use
# If you have knowledge-capture AND notion-knowledge-capture, remove one
```

### 4. Disable heavy MCP servers

Some MCP servers register dozens of tools:

| Server | Typical tools | Impact |
|--------|--------------|--------|
| stealth-browser | ~85 tools | ~1,275 tokens |
| Supabase | ~30 tools | ~450 tokens |
| Qonto (2 accounts) | ~60 tools | ~900 tokens |

If you don't use them daily, remove from `.mcp.json` and re-add when needed.

### 5. Disable cloud MCP integrations

If you use Claude Code with a Claude.ai Pro/Max account, cloud integrations (Supabase, Kiwi.com, etc.) inject tools into every session:

```bash
# Disable all cloud MCP servers
export ENABLE_CLAUDEAI_MCP_SERVERS=false

# Add to ~/.zshrc for permanent effect
echo 'export ENABLE_CLAUDEAI_MCP_SERVERS=false' >> ~/.zshrc
```

---

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | The skill definition — copy to your project's skills directory |
| `token-hygiene.sh` | Shell script for automated execution via cron/launchd |
| `com.claude.schedule.token-hygiene.plist` | macOS launchd template for monthly scheduling |

## How the Automation Works

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────┐
│   launchd    │────▶│ token-hygiene.sh  │────▶│  claude -p   │
│  (monthly)   │     │  (pre-fetches     │     │  (analyzes   │
│              │     │   all metrics)    │     │   + reports)  │
└─────────────┘     └──────────────────┘     └──────┬──────┘
                                                      │
                                              ┌───────▼───────┐
                                              │  Email report  │
                                              │  (via gog CLI) │
                                              └───────────────┘
```

1. **launchd** (or cron) triggers `token-hygiene.sh` on the 1st of each month
2. The script **pre-fetches metrics** via shell (file sizes, counts) — fast and free
3. It passes the metrics to `claude -p` with the skill instructions
4. Claude analyzes against thresholds, compares with previous audit, generates report
5. (Optional) Sends HTML report via email using `gog` CLI

The pre-fetch step means Claude doesn't waste tokens running `wc` and `ls` commands — it gets the data ready-made.

---

## FAQ

**Q: Does this modify my files?**
No. The skill is read-only. It reports issues and recommends actions. You decide what to change.

**Q: How much does the monthly audit cost?**
About 5,000-10,000 tokens per run (~$0.03 on Sonnet). The savings from one cleanup easily pay for years of audits.

**Q: I don't use auto-memory. Is this still useful?**
Yes. CLAUDE.md bloat and MCP server overhead affect everyone. Memory is just one of the checks.

**Q: Can I change the thresholds?**
Yes. Edit the thresholds table in `SKILL.md` to match your setup.

**Q: Does this work with Claude Code on VS Code?**
Yes. Claude Code loads the same system context regardless of whether you use the CLI or VS Code extension.

---

## Contributing

Found a new optimization pattern? Open a PR. The goal is to build a community knowledge base of token-saving techniques for Claude Code power users.

## License

MIT — use it, share it, improve it.

---

Built by [@AlfonsoSBLA](https://github.com/AlfonsoSBLA) after watching his Claude Code conversations burn 30K tokens on system context.
