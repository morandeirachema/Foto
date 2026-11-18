#!/usr/bin/env bash
# Builds the Luminar guide from the chapter files in retoques/:
#   1. refreshes the prev/index/next navigation block in every chapter,
#   2. concatenates all chapters (without navigation) into the single-file guide,
#   3. renders that file to an A4 PDF with pandoc + headless Google Chrome.
# Usage: ./pdf/generar-guia-luminar.sh            (everything)
#        ./pdf/generar-guia-luminar.sh --no-pdf   (skip step 3)
set -euo pipefail
cd "$(dirname "$0")/.."

GUIDE_MD="retoques/guia-completa.md"
GUIDE_PDF="pdf/guia-luminar.pdf"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"

chapters=(retoques/[0-9][0-9]-*.md)
n=${#chapters[@]}

strip_nav() { sed '/^<!-- nav -->$/,/^<!-- \/nav -->$/d' "$1" | sed -e :a -e '/^\n*$/{$d;N;ba' -e '}' | sed '/./,$!d'; }

# 1. Navigation
for ((i = 0; i < n; i++)); do
  f=${chapters[$i]}
  prev=""; next=""
  ((i > 0)) && prev="[← Anterior]($(basename "${chapters[$((i - 1))]}"))"
  ((i < n - 1)) && next="[Siguiente →]($(basename "${chapters[$((i + 1))]}"))"
  nav="<!-- nav -->"$'\n'"${prev:+$prev · }[Índice](README.md)${next:+ · $next}"$'\n'"<!-- /nav -->"
  body=$(strip_nav "$f")
  printf '%s\n\n%s\n\n%s\n' "$nav" "$body" "$nav" > "$f"
done

# 2. Single-file guide
{
  echo "<!-- Archivo generado por pdf/generar-guia-luminar.sh a partir de retoques/. No lo edites a mano. -->"
  echo
  for ((i = 0; i < n; i++)); do
    strip_nav "${chapters[$i]}"
    ((i < n - 1)) && printf '\n---\n\n'
  done
} > "$GUIDE_MD"
echo "OK  $GUIDE_MD"

# 3. PDF
[[ "${1:-}" == "--no-pdf" ]] && exit 0
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
pandoc "$GUIDE_MD" --from gfm --standalone --embed-resources --css pdf/guia-luminar.css \
  --metadata pagetitle="Mejorar JPEG de safari, paisaje y fotografía nocturna con Luminar" \
  --metadata lang=es -o "$tmp/guia.html"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$PWD/$GUIDE_PDF" "file://$tmp/guia.html" 2>/dev/null
echo "OK  $GUIDE_PDF"
