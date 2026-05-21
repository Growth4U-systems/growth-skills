#!/usr/bin/env bash
# audit-runner.sh — Encadena las 3 fases de datos del audit y deja outputs en .cache/
#
# Usage:
#   ./audit-runner.sh <url> <cliente-slug>
#
# Genera:
#   .cache/<cliente>/01-toprank.json    (vía toprank:seo-analysis)
#   .cache/<cliente>/02-agricidaniel.md (vía /seo audit)
#   .cache/<cliente>/03a-geo-score.json (vía toprank:geo-optimizer)
#   .cache/<cliente>/03b-ai-seo.md      (vía Corey ai-seo)
#   .cache/<cliente>/03c-llm-mentions.json (vía DataForSEO si disponible)
#
# Nota: este script es un ORQUESTADOR DE INVOCACIONES a Claude Code skills.
# No ejecuta lógica SEO por sí mismo — solo prepara el cache dir y registra outputs.
# Las skills se invocan desde la sesión de Claude.

set -euo pipefail

if [ $# -lt 2 ]; then
    echo "Usage: $0 <url> <cliente-slug>" >&2
    exit 1
fi

URL="$1"
CLIENTE="$2"
CACHE_DIR=".cache/${CLIENTE}"

mkdir -p "${CACHE_DIR}"

echo "▶ Audit pipeline para ${CLIENTE} (${URL})"
echo "▶ Cache dir: ${CACHE_DIR}"
echo ""
echo "Este script prepara el cache dir. Las skills se invocan desde la sesión Claude así:"
echo ""
echo "  Fase 1 (datos crudos):"
echo "    Invocar: toprank:seo-analysis ${URL}"
echo "    Guardar output JSON en: ${CACHE_DIR}/01-toprank.json"
echo ""
echo "  Fase 2 (audit técnico/on-page):"
echo "    Invocar: /seo audit ${URL}"
echo "    Guardar output md en: ${CACHE_DIR}/02-agricidaniel.md"
echo ""
echo "  Fase 3a (GEO score):"
echo "    Invocar: toprank:geo-optimizer ${URL}"
echo "    Guardar output JSON en: ${CACHE_DIR}/03a-geo-score.json"
echo ""
echo "  Fase 3b (AI/per-platform analysis):"
echo "    Invocar skill: ai-seo (Corey Haines)"
echo "    Pasar: URL + top queries de Fase 1"
echo "    Guardar output md en: ${CACHE_DIR}/03b-ai-seo.md"
echo ""
echo "  Fase 3c (LLM mentions tracking — opcional):"
echo "    Invocar DataForSEO MCP: mcp__dataforseo__ai_opt_llm_ment_search"
echo "    Query: brand + competitor keywords"
echo "    Guardar output JSON en: ${CACHE_DIR}/03c-llm-mentions.json"
echo ""
echo "  Fase 4 (sintesis G4U):"
echo "    Componer outputs anteriores según references/audit-playbook.md §4"
echo "    Generar HTML vía html-output (tema Sancho) en:"
echo "      OUTPUTS/${CLIENTE}/$(date +%Y-%m-%d)-seo-audit.html"
echo ""
echo "✓ Cache dir listo. Procede con las invocaciones de skill arriba."
