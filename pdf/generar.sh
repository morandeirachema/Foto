#!/usr/bin/env bash
# Regenera los PDF del repo desde su Markdown.
# Uso: ./pdf/generar.sh [nombre]   (sin argumento, todos)
#   chuleta · verificacion-in-situ · cuaderno-de-composicion  → hojas de campo
#   guia-conceptos · guia-manejo-a6700 · guia-retoques      → cada sección completa
# Requiere: pandoc y Google Chrome (o Chromium), en macOS o Linux.
set -euo pipefail
cd "$(dirname "$0")/.."

CHROME="$(command -v google-chrome || command -v chromium || true)"
if [ -z "$CHROME" ]; then
  for app in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
             "/Applications/Chromium.app/Contents/MacOS/Chromium"; do
    [ -x "$app" ] && { CHROME="$app"; break; }
  done
fi
[ -z "$CHROME" ] && { echo "Falta Google Chrome/Chromium"; exit 1; }
command -v pandoc >/dev/null || { echo "Falta pandoc"; exit 1; }
export CHROME

NOMBRES="chuleta verificacion-in-situ cuaderno-de-composicion guia-conceptos guia-manejo-a6700 guia-retoques"

# Sin arrays asociativos: el bash 3.2 de macOS no los tiene
fuente() {
  case "$1" in
    chuleta)                 echo "manejo-a6700/16-chuleta.md" ;;
    verificacion-in-situ)    echo "manejo-a6700/17-verificacion-in-situ.md" ;;
    cuaderno-de-composicion) echo "conceptos/08-cuaderno-de-composicion.md" ;;
    *) echo "Hoja desconocida: $1 (son: $NOMBRES)" >&2; exit 1 ;;
  esac
}

hacer() {
  local nombre="$1"
  case "$nombre" in guia-*) ./pdf/generar-guia.sh "${nombre#guia-}"; return ;; esac
  local fuente; fuente="$(fuente "$1")"
  local tmp; tmp="$(mktemp -d)"
  local css=(--css=pdf/estilo.css)
  case "$nombre" in
    chuleta) css+=(--css=pdf/compacto.css) ;;   # debe caber en una cara
  esac
  # the sheet is printed without the chapter navigation
  sed '/^<!-- nav -->$/,/^<!-- \/nav -->$/d' "$fuente" > "$tmp/$nombre.md"
  pandoc "$tmp/$nombre.md" --standalone --embed-resources \
         "${css[@]}" --metadata title="" \
         -o "$tmp/$nombre.html"
  "$CHROME" --headless --disable-gpu --no-sandbox \
            --no-pdf-header-footer --print-to-pdf-no-header \
            --print-to-pdf="$PWD/pdf/$nombre.pdf" \
            "file://$tmp/$nombre.html" >/dev/null 2>&1
  rm -rf "$tmp"
  echo "  pdf/$nombre.pdf  ($(du -h "pdf/$nombre.pdf" | cut -f1))"
}

if [ $# -gt 0 ]; then hacer "$1"; else for n in $NOMBRES; do hacer "$n"; done; fi
