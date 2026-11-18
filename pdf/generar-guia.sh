#!/usr/bin/env bash
# Builds one section of the repo (conceptos, manejo-a6700 or retoques) from its chapter files:
#   1. refreshes the prev/index/next navigation block in every chapter (<carpeta>/NN-*.md),
#   2. concatenates all chapters (without navigation) into <carpeta>/guia-completa.md,
#   3. renders that file to an A4 PDF, pdf/guia-<carpeta>.pdf, with pandoc + headless Chrome.
#      Mermaid diagrams are replaced by a short note in the PDF (GitHub draws them).
# Usage: ./pdf/generar-guia.sh <carpeta> [--no-pdf]
set -euo pipefail
cd "$(dirname "$0")/.."

dir="${1:?uso: ./pdf/generar-guia.sh <conceptos|manejo-a6700|retoques> [--no-pdf]}"
case "$dir" in
  conceptos)    title="Conceptos de fotografía" ;;
  manejo-a6700) title="Manejo de la Sony a6700" ;;
  retoques)     title="Mejorar JPEG de safari, paisaje y fotografía nocturna con Luminar" ;;
  *) echo "Carpeta desconocida: $dir" >&2; exit 1 ;;
esac
GUIDE_MD="$dir/guia-completa.md"
GUIDE_PDF="pdf/guia-$dir.pdf"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"

chapters=("$dir"/[0-9][0-9]-*.md)
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
  echo "<!-- Archivo generado por pdf/generar-guia.sh a partir de $dir/. No lo edites a mano. -->"
  echo
  for ((i = 0; i < n; i++)); do
    strip_nav "${chapters[$i]}"
    ((i < n - 1)) && printf '\n---\n\n'
  done
} > "$GUIDE_MD"
echo "OK  $GUIDE_MD"

# 3. PDF
[[ "${2:-}" == "--no-pdf" ]] && exit 0
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
awk '/^```mermaid/{skip=1; print "> 📊 *Diagrama: se ve en la versión de GitHub.*"; next}
     skip && /^```/{skip=0; next} !skip' "$GUIDE_MD" > "$tmp/guia.md"
# links to the repo's own files don't work inside a PDF: keep the text, drop the link
sed -E 's/\[([^]]+)\]\((\.\.\/)?[^):]*\.(md|pdf)(#[^)]*)?\)/\1/g; s/\[([^]]+)\]\(#[^)]*\)/\1/g' "$tmp/guia.md" > "$tmp/guia2.md"
pandoc "$tmp/guia2.md" --from gfm --standalone --embed-resources --css pdf/guia.css \
  --metadata pagetitle="$title" --metadata lang=es -o "$tmp/guia.html"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$PWD/$GUIDE_PDF" "file://$tmp/guia.html" 2>/dev/null
echo "OK  $GUIDE_PDF"
