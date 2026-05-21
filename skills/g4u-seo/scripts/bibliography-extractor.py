#!/usr/bin/env python3
"""
Bibliography extractor — re-genera references/_bibliography-raw.md desde Notion.

Usage:
    python3 bibliography-extractor.py [--theme SEO] [--limit 100]

Requires NOTION_TOKEN env var. Lee de la DB Bibliografía (1395dacf-4f14-81de-801f-dee0678dc51e).

El output se escribe a references/_bibliography-raw.md (sobreescribe).
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
from pathlib import Path

NOTION_API = "https://api.notion.com/v1"
BIBLIO_DB = "1395dacf-4f14-81de-801f-dee0678dc51e"
NOTION_VERSION = "2025-09-03"


def get_token():
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        # Try .mcp.json
        mcp_path = Path(__file__).resolve().parents[4] / ".mcp.json"
        if mcp_path.exists():
            with open(mcp_path) as f:
                cfg = json.load(f)
                token = cfg.get("mcpServers", {}).get("notion", {}).get("env", {}).get("NOTION_TOKEN")
    if not token:
        print("ERROR: NOTION_TOKEN no encontrado en env ni en .mcp.json", file=sys.stderr)
        sys.exit(1)
    return token


def notion_request(path, method="GET", body=None, token=None):
    url = f"{NOTION_API}{path}"
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Notion-Version", NOTION_VERSION)
    req.add_header("Content-Type", "application/json")
    if body is not None:
        req.data = json.dumps(body).encode("utf-8")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode()}", file=sys.stderr)
        raise


def get_data_source_id(token):
    db = notion_request(f"/databases/{BIBLIO_DB}", token=token)
    sources = db.get("data_sources", [])
    if not sources:
        print("ERROR: DB sin data sources", file=sys.stderr)
        sys.exit(1)
    return sources[0]["id"]


def query_entries(data_source_id, theme, limit, token):
    """Pagina hasta `limit` entradas con el theme dado."""
    results = []
    cursor = None
    while True:
        body = {
            "filter": {"property": "Theme", "select": {"equals": theme}},
            "page_size": min(100, limit - len(results)),
        }
        if cursor:
            body["start_cursor"] = cursor
        resp = notion_request(
            f"/data_sources/{data_source_id}/query",
            method="POST",
            body=body,
            token=token,
        )
        results.extend(resp.get("results", []))
        if not resp.get("has_more") or len(results) >= limit:
            break
        cursor = resp.get("next_cursor")
    return results[:limit]


def get_prop(entry, prop_name):
    return entry.get("properties", {}).get(prop_name, {})


def render_entry(entry):
    p = entry.get("properties", {})
    title = "".join(t.get("plain_text", "") for t in p.get("Title", {}).get("title", []))
    url = p.get("URL", {}).get("url") or ""
    estado = (p.get("Estado", {}).get("select") or {}).get("name", "")
    tipo = (p.get("Tipo", {}).get("select") or {}).get("name", "")
    idioma = (p.get("Idioma", {}).get("select") or {}).get("name", "")
    plataforma = (p.get("Plataforma", {}).get("select") or {}).get("name", "")
    autores = ", ".join(a["name"] for a in p.get("Autor", {}).get("multi_select", []))
    summary = " ".join(
        t.get("plain_text", "")
        for t in p.get("Summary", {}).get("rich_text", [])
    )
    created = p.get("Fecha de creación", {}).get("created_time", "")[:10]

    return f"""## {title}

- **Autor**: {autores}
- **Tipo**: {tipo} / {plataforma} / {idioma}
- **Estado**: {estado}
- **Fecha**: {created}
- **URL**: {url}
- **Notion**: {entry.get("url", "")}

{summary}

---
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--theme", default="SEO", help="Theme filter (default: SEO)")
    parser.add_argument("--limit", type=int, default=200, help="Max entries (default: 200)")
    parser.add_argument(
        "--output",
        default=None,
        help="Output path (default: ../references/_bibliography-raw.md)",
    )
    args = parser.parse_args()

    out_path = (
        Path(args.output)
        if args.output
        else Path(__file__).resolve().parent.parent / "references" / "_bibliography-raw.md"
    )

    token = get_token()
    print(f"Querying theme={args.theme}, limit={args.limit}...", file=sys.stderr)
    ds_id = get_data_source_id(token)
    entries = query_entries(ds_id, args.theme, args.limit, token)
    print(f"Got {len(entries)} entries.", file=sys.stderr)

    rendered = [render_entry(e) for e in entries]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(rendered), encoding="utf-8")
    print(f"Wrote {out_path} ({sum(len(r) for r in rendered)} chars)", file=sys.stderr)


if __name__ == "__main__":
    main()
