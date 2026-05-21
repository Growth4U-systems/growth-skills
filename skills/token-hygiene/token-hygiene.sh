#!/bin/bash
# token-hygiene.sh — Scheduled token overhead audit for Claude Code
#
# This script pre-fetches system metrics and passes them to Claude
# for analysis using the token-hygiene skill.
#
# Usage:
#   ./token-hygiene.sh                    # Run audit, print report
#   ./token-hygiene.sh --email you@co.com # Run audit + send HTML email
#
# Requirements:
#   - claude CLI installed and authenticated
#   - gog CLI (optional, for email delivery): brew install steipete/tap/gogcli
#
# Setup:
#   1. Copy SKILL.md to your project: 00-system/skills/token-hygiene/SKILL.md
#   2. Copy this script to: .claude/scheduler-scripts/token-hygiene.sh
#   3. chmod +x .claude/scheduler-scripts/token-hygiene.sh
#   4. Set PROJECT_DIR below to your project root
#   5. (Optional) Set up launchd/cron — see README.md

set -euo pipefail

# === CONFIGURATION ===
# Change these to match your setup
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
EMAIL_TO="${TOKEN_HYGIENE_EMAIL:-}"
EMAIL_ACCOUNT="${TOKEN_HYGIENE_EMAIL_ACCOUNT:-work}"
SKILL_PATH="00-system/skills/token-hygiene/SKILL.md"

# Parse --email flag
for arg in "$@"; do
  case $arg in
    --email=*) EMAIL_TO="${arg#*=}" ;;
    --email) EMAIL_TO="${2:-}" ;;
  esac
done

# === PATH SETUP ===
export PATH="/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin:$HOME/.local/bin:$PATH"
export HOME="${HOME:-/Users/$(whoami)}"

cd "$PROJECT_DIR"

# === DETECT AUTO-MEMORY LOCATION ===
# Claude Code stores auto-memory in ~/.claude/projects/<encoded-path>/memory/
ENCODED_PATH=$(echo "$PROJECT_DIR" | sed 's|/|-|g')
MEMORY_DIR="$HOME/.claude/projects/$ENCODED_PATH/memory"
MEMORY_FILE="$MEMORY_DIR/MEMORY.md"

# === PRE-FETCH METRICS ===
echo "[token-hygiene] Collecting metrics..."

MEMORY_LINES=$(wc -l < "$MEMORY_FILE" 2>/dev/null | tr -d ' ' || echo "0")
MEMORY_BYTES=$(wc -c < "$MEMORY_FILE" 2>/dev/null | tr -d ' ' || echo "0")
CLAUDE_LINES=$(wc -l < "CLAUDE.md" 2>/dev/null | tr -d ' ' || echo "0")
CLAUDE_BYTES=$(wc -c < "CLAUDE.md" 2>/dev/null | tr -d ' ' || echo "0")
SKILLS_COUNT=$(ls -d "$HOME/.claude/skills"/*/ 2>/dev/null | wc -l | tr -d ' ')
MCP_SERVERS=$(grep -c '"command"' .mcp.json 2>/dev/null || echo "0")
STALE_LOGS=$(find memory/ -name "20*.md" -mtime +30 2>/dev/null | wc -l | tr -d ' ')
TOPIC_FILES=$(ls -lhS "$MEMORY_DIR/"*.md 2>/dev/null | grep -v MEMORY.md || echo "none")
TRACKER=$(cat memory/token-hygiene-tracker.json 2>/dev/null || echo '{"last_audit":"never"}')

echo "[token-hygiene] CLAUDE.md: ${CLAUDE_LINES} lines, ${CLAUDE_BYTES} bytes"
echo "[token-hygiene] MEMORY.md: ${MEMORY_LINES} lines, ${MEMORY_BYTES} bytes"
echo "[token-hygiene] Skills: ${SKILLS_COUNT}, MCP servers: ${MCP_SERVERS}"
echo "[token-hygiene] Stale logs: ${STALE_LOGS}"

# === BUILD EMAIL INSTRUCTION ===
EMAIL_INSTRUCTION=""
if [ -n "$EMAIL_TO" ]; then
  EMAIL_INSTRUCTION="After generating the report, send it as an HTML email:
gog gmail send --account $EMAIL_ACCOUNT --to $EMAIL_TO --subject 'Token Hygiene — $(date +%Y-%m-%d) — STATUS' --body-html '<HTML_REPORT>' --no-input --force
Replace STATUS with summary (e.g., 'All Green' or '2 issues found')."
fi

# === RUN CLAUDE ===
echo "[token-hygiene] Running audit..."

claude -p "You are running as a scheduled proactive task (not interactive). Execute the token-hygiene skill.

Read the full skill at: $SKILL_PATH

=== PRE-FETCHED METRICS ===
MEMORY.md: $MEMORY_LINES lines, $MEMORY_BYTES bytes
CLAUDE.md: $CLAUDE_LINES lines, $CLAUDE_BYTES bytes
Skills installed: $SKILLS_COUNT
MCP servers: $MCP_SERVERS
Stale daily logs (>30 days): $STALE_LOGS
Topic files:
$TOPIC_FILES

Previous audit data:
$TRACKER
=== END METRICS ===

INSTRUCTIONS:
1. Read the skill file for thresholds and report format
2. Use the pre-fetched metrics above — do NOT re-run the measurements
3. Calculate estimated token overhead per conversation
4. Compare with previous audit if available
5. Generate the report following the skill template
6. Save tracker JSON to memory/token-hygiene-tracker.json
$EMAIL_INSTRUCTION

Today is $(date +%Y-%m-%d)." \
  --dangerously-skip-permissions \
  --allowedTools 'Read,Grep,Glob,Bash,Write,Edit'

echo "[token-hygiene] Done."
