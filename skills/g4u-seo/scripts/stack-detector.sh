#!/usr/bin/env bash
# stack-detector.sh — Detección empírica del stack tecnológico de un sitio.
#
# Usage:
#   ./stack-detector.sh <url> [--json]
#
# Output:
#   - Por defecto: markdown legible
#   - Con --json: JSON estructurado (para consumo programático)
#
# Detecta:
#   - CMS (WordPress, Webflow, Shopify, Wix, Squarespace, Drupal, Ghost)
#   - Framework JS (Next.js, Astro, Nuxt, Gatsby, SvelteKit, Remix, Hugo)
#   - CDN (Cloudflare, Vercel, Netlify, Fastly, Akamai, AWS CloudFront)
#   - Server software (nginx, Apache, LiteSpeed, Caddy)
#   - Lenguaje backend probable (PHP, Node, Python, Ruby, Go)
#   - Plugins/themes (Divi, Avada, Yoast, RankMath, AIOSEO, Elementor)
#   - Third-party scripts (GA, GTM, Facebook Pixel, Zendesk, Intercom, Hotjar)
#
# Esto alimenta los handoff briefs de Fase 2b accessibility y 2c performance:
# saber el stack permite ser preciso en `files probables` (ej. WordPress →
# wp-content/themes/..., Next.js → src/components/..., Webflow → cambios en
# Designer manual).
#
# DEPENDS ON: curl, grep, awk. dig es opcional.

set -uo pipefail

URL=""
OUTPUT_JSON=false

while [ $# -gt 0 ]; do
    case "$1" in
        --json) OUTPUT_JSON=true; shift ;;
        -h|--help)
            sed -n '2,28p' "$0" | sed 's/^# \?//'
            exit 0
            ;;
        *) URL="$1"; shift ;;
    esac
done

if [ -z "$URL" ]; then
    echo "Usage: $0 <url> [--json]" >&2
    exit 1
fi

# Normaliza URL — si no tiene esquema, añadir https://
if ! [[ "$URL" =~ ^https?:// ]]; then
    URL="https://${URL}"
fi

HOST=$(echo "$URL" | awk -F[/:] '{print $4}')
TMP_HEAD="/tmp/stack-detector-head-$$"
TMP_BODY="/tmp/stack-detector-body-$$"

cleanup() { rm -f "$TMP_HEAD" "$TMP_BODY"; }
trap cleanup EXIT

# Fetch headers + body
if ! curl -s -L -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
    --max-time 20 \
    -D "$TMP_HEAD" \
    -o "$TMP_BODY" \
    "$URL" 2>/dev/null; then
    echo "ERROR: no se pudo fetchear $URL" >&2
    exit 2
fi

# Helper: extract header value (case-insensitive)
header() {
    grep -i "^$1:" "$TMP_HEAD" 2>/dev/null | tail -1 | sed "s/^[^:]*: //" | tr -d '\r\n'
}

# Helper: count grep matches in body
body_count() {
    grep -ic "$1" "$TMP_BODY" 2>/dev/null || echo 0
}

# Helper: yes if body contains pattern
body_has() {
    grep -iq "$1" "$TMP_BODY" 2>/dev/null && echo "yes" || echo "no"
}

# ===== DETECCIÓN =====

SERVER=$(header "Server")
X_POWERED_BY=$(header "X-Powered-By")
CF_RAY=$(header "CF-Ray")
CF_CACHE=$(header "CF-Cache-Status")
VIA=$(header "Via")
X_VERCEL_ID=$(header "X-Vercel-Id")
X_NF_REQUEST_ID=$(header "X-Nf-Request-Id")
X_FASTLY=$(header "X-Served-By")
X_AMZ_CF_ID=$(header "X-Amz-Cf-Id")

# CMS detection
CMS="unknown"
CMS_CONFIDENCE="low"
if [ "$(body_has 'wp-content\|wp-includes\|wp-json')" = "yes" ]; then
    CMS="WordPress"
    CMS_CONFIDENCE="high"
elif [ "$(body_has 'webflow.com\|w-mod\|data-wf-page')" = "yes" ]; then
    CMS="Webflow"
    CMS_CONFIDENCE="high"
elif [ "$(body_has 'cdn.shopify.com\|shopify-payment-button')" = "yes" ]; then
    CMS="Shopify"
    CMS_CONFIDENCE="high"
elif [ "$(body_has 'wix.com\|wixstatic\|wixsite')" = "yes" ]; then
    CMS="Wix"
    CMS_CONFIDENCE="high"
elif [ "$(body_has 'squarespace\|static1.squarespace')" = "yes" ]; then
    CMS="Squarespace"
    CMS_CONFIDENCE="high"
elif [ "$(body_has 'drupal-settings-json\|sites/default/files')" = "yes" ]; then
    CMS="Drupal"
    CMS_CONFIDENCE="high"
elif [ "$(body_has 'ghost.io\|ghost-sdk')" = "yes" ]; then
    CMS="Ghost"
    CMS_CONFIDENCE="medium"
fi

# Framework JS detection
FRAMEWORK="unknown"
FRAMEWORK_CONFIDENCE="low"
if [ "$(body_has '_next/static\|__NEXT_DATA__')" = "yes" ]; then
    FRAMEWORK="Next.js"
    FRAMEWORK_CONFIDENCE="high"
elif [ "$(body_has '_astro/\|astro-island')" = "yes" ]; then
    FRAMEWORK="Astro"
    FRAMEWORK_CONFIDENCE="high"
elif [ "$(body_has '_nuxt/\|__NUXT__')" = "yes" ]; then
    FRAMEWORK="Nuxt"
    FRAMEWORK_CONFIDENCE="high"
elif [ "$(body_has '/_gatsby/\|window.___gatsby')" = "yes" ]; then
    FRAMEWORK="Gatsby"
    FRAMEWORK_CONFIDENCE="high"
elif [ "$(body_has 'sveltekit\|_app/immutable')" = "yes" ]; then
    FRAMEWORK="SvelteKit"
    FRAMEWORK_CONFIDENCE="high"
elif [ "$(body_has '__remixManifest\|/build/_assets')" = "yes" ]; then
    FRAMEWORK="Remix"
    FRAMEWORK_CONFIDENCE="medium"
elif [ "$(body_has 'data-hugo\|hugo-generator')" = "yes" ]; then
    FRAMEWORK="Hugo"
    FRAMEWORK_CONFIDENCE="medium"
fi

# CDN detection
CDN="unknown"
if [ -n "$CF_RAY" ] || [ -n "$CF_CACHE" ]; then
    CDN="Cloudflare"
elif [ -n "$X_VERCEL_ID" ]; then
    CDN="Vercel"
elif [ -n "$X_NF_REQUEST_ID" ]; then
    CDN="Netlify"
elif [[ "$X_FASTLY" == *"cache-"* ]] || [[ "$VIA" == *"varnish"* ]]; then
    CDN="Fastly"
elif [ -n "$X_AMZ_CF_ID" ]; then
    CDN="AWS CloudFront"
elif [[ "$VIA" == *"akamai"* ]] || [[ "$SERVER" == *"AkamaiGHost"* ]]; then
    CDN="Akamai"
fi

# Server / language
LANG="unknown"
if [[ "$X_POWERED_BY" == *"PHP"* ]] || [ "$CMS" = "WordPress" ] || [ "$CMS" = "Drupal" ]; then
    LANG="PHP"
elif [[ "$X_POWERED_BY" == *"Express"* ]] || [[ "$X_POWERED_BY" == *"Next.js"* ]] || [ "$FRAMEWORK" = "Next.js" ]; then
    LANG="Node.js"
elif [[ "$X_POWERED_BY" == *"ASP.NET"* ]]; then
    LANG=".NET"
fi

# WP plugins (only if WordPress detected)
WP_PLUGINS=""
if [ "$CMS" = "WordPress" ]; then
    [ "$(body_has 'wp-content/themes/divi\|et_dom\|et_pb_')" = "yes" ] && WP_PLUGINS="$WP_PLUGINS,Divi"
    [ "$(body_has 'wp-content/themes/Avada\|fusion-')" = "yes" ] && WP_PLUGINS="$WP_PLUGINS,Avada"
    [ "$(body_has 'wp-content/plugins/elementor\|elementor-')" = "yes" ] && WP_PLUGINS="$WP_PLUGINS,Elementor"
    [ "$(body_has 'wp-content/plugins/wordpress-seo\|yoast')" = "yes" ] && WP_PLUGINS="$WP_PLUGINS,Yoast SEO"
    [ "$(body_has 'wp-content/plugins/seo-by-rank-math\|rank-math')" = "yes" ] && WP_PLUGINS="$WP_PLUGINS,RankMath"
    [ "$(body_has 'wp-content/plugins/all-in-one-seo-pack\|aioseo')" = "yes" ] && WP_PLUGINS="$WP_PLUGINS,AIOSEO"
    [ "$(body_has 'wp-content/plugins/wpml\|sitepress')" = "yes" ] && WP_PLUGINS="$WP_PLUGINS,WPML"
    [ "$(body_has 'wp-content/plugins/woocommerce\|wc-blocks')" = "yes" ] && WP_PLUGINS="$WP_PLUGINS,WooCommerce"
    WP_PLUGINS="${WP_PLUGINS#,}"
fi

# Third-party scripts (analytics, chat, A/B, monitoring)
THIRD_PARTY=""
[ "$(body_has 'googletagmanager.com/gtm\|GTM-')" = "yes" ] && THIRD_PARTY="$THIRD_PARTY,GTM"
[ "$(body_has 'google-analytics.com/analytics\|gtag(.config')" = "yes" ] && THIRD_PARTY="$THIRD_PARTY,GA4"
[ "$(body_has 'connect.facebook.net.*fbevents')" = "yes" ] && THIRD_PARTY="$THIRD_PARTY,Meta Pixel"
[ "$(body_has 'snap.licdn.com\|linkedin-insight')" = "yes" ] && THIRD_PARTY="$THIRD_PARTY,LinkedIn Insight"
[ "$(body_has 'static.hotjar.com')" = "yes" ] && THIRD_PARTY="$THIRD_PARTY,Hotjar"
[ "$(body_has 'cdn.amplitude.com')" = "yes" ] && THIRD_PARTY="$THIRD_PARTY,Amplitude"
[ "$(body_has 'static.zdassets.com\|zendesk')" = "yes" ] && THIRD_PARTY="$THIRD_PARTY,Zendesk"
[ "$(body_has 'widget.intercom.io')" = "yes" ] && THIRD_PARTY="$THIRD_PARTY,Intercom"
[ "$(body_has 'cdn.optimizely.com')" = "yes" ] && THIRD_PARTY="$THIRD_PARTY,Optimizely"
[ "$(body_has 'cdn.cookielaw.org\|cookieyes\|complianz')" = "yes" ] && THIRD_PARTY="$THIRD_PARTY,Cookie consent"
[ "$(body_has 'cdn.trustpilot.com\|tp-widget')" = "yes" ] && THIRD_PARTY="$THIRD_PARTY,Trustpilot"
[ "$(body_has 'google.com/recaptcha\|recaptcha/api')" = "yes" ] && THIRD_PARTY="$THIRD_PARTY,reCAPTCHA"
THIRD_PARTY="${THIRD_PARTY#,}"

# Total script count
SCRIPT_COUNT=$(grep -c '<script' "$TMP_BODY" 2>/dev/null || echo 0)
EXTERNAL_SCRIPTS=$(grep -oE '<script[^>]+src="https?://[^"]+"' "$TMP_BODY" 2>/dev/null | wc -l | tr -d ' ')

# Implications for handoff briefs
IMPLICATIONS=""
case "$CMS" in
    WordPress)
        IMPLICATIONS="Handoff a Martín: edits en wp-content/themes/<theme>/. Si Divi/Elementor builder, también cambios en builder UI. Si plugins SEO (Yoast/RankMath), respetar su schema generation."
        ;;
    Webflow)
        IMPLICATIONS="Handoff a Martín: cambios en Webflow Designer manualmente (no skill). Para schema custom: Page Settings > Custom Code. Para tracking: Project Settings > Custom Code."
        ;;
    Shopify)
        IMPLICATIONS="Handoff a Martín: edits en theme files via Shopify CLI o admin Themes editor. Liquid templates."
        ;;
esac

case "$FRAMEWORK" in
    Next.js)
        IMPLICATIONS="$IMPLICATIONS Handoff: src/components/, src/pages/ o app/. Para imágenes usar next/image. Para schema, head con <Head> o metadata API."
        ;;
    Astro)
        IMPLICATIONS="$IMPLICATIONS Handoff: src/components/, src/pages/. astro:assets para imágenes optimizadas. Layouts en src/layouts/."
        ;;
esac

# ===== OUTPUT =====

if [ "$OUTPUT_JSON" = true ]; then
    cat <<EOF
{
  "url": "$URL",
  "host": "$HOST",
  "cms": {"name": "$CMS", "confidence": "$CMS_CONFIDENCE"},
  "framework": {"name": "$FRAMEWORK", "confidence": "$FRAMEWORK_CONFIDENCE"},
  "cdn": "$CDN",
  "server": "$SERVER",
  "language": "$LANG",
  "wordpress_plugins": "$WP_PLUGINS",
  "third_party_scripts": "$THIRD_PARTY",
  "total_scripts": $SCRIPT_COUNT,
  "external_scripts": $EXTERNAL_SCRIPTS,
  "implications": "$IMPLICATIONS"
}
EOF
else
    cat <<EOF
# Stack Manifest — $HOST

Detected $(date -u +"%Y-%m-%dT%H:%M:%SZ")

## CMS / Platform
- **CMS**: $CMS (confidence: $CMS_CONFIDENCE)
- **Framework JS**: $FRAMEWORK (confidence: $FRAMEWORK_CONFIDENCE)
- **Language**: $LANG

## Infrastructure
- **CDN**: $CDN
- **Server**: ${SERVER:-unknown}
- **X-Powered-By**: ${X_POWERED_BY:-not exposed}

## Plugins / Builders
- **WordPress plugins detected**: ${WP_PLUGINS:-none/not-WP}

## Third-party scripts
- **Detected**: ${THIRD_PARTY:-none detected}
- **Total \`<script>\` tags**: $SCRIPT_COUNT
- **External scripts**: $EXTERNAL_SCRIPTS

## Implications para handoff briefs (Fase 2b/2c)

$IMPLICATIONS

---

> Este manifest informa los \`files probables\` y la \`skill recomendada\` de cada handoff brief de accessibility y performance code en la auditoría.
EOF
fi
