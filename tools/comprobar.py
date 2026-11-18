#!/usr/bin/env python3
"""Comprueba la coherencia del repo. Uso: python3 tools/comprobar.py

- Enlaces relativos: el archivo existe y, si llevan #ancla, el encabezado también.
- Bloques de código: ninguna valla ``` sin cerrar (en GitHub ocultaría el resto).
- Capítulos: en conceptos/, manejo-a6700/ y retoques/, el H1 de NN-*.md empieza por "# N.".
- Navegación: cada capítulo tiene sus bloques <!-- nav --> (los genera pdf/generar-guia.sh).
- Hoja de campo: la chuleta cabe en una cara (si existe pdfinfo).

Sale con código 1 si encuentra algún problema.
"""
import glob
import os
import re
import shutil
import subprocess
import sys
import unicodedata

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SECCIONES = ("conceptos", "manejo-a6700", "retoques")
problemas = []


def slug(h):
    h = re.sub(r"<[^>]+>", "", h)
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h)
    h = h.strip().lower()
    h = re.sub(r"[^\w\- ]", "", h, flags=re.UNICODE)
    return h.replace(" ", "-")


md = [f for f in glob.glob("**/*.md", recursive=True) if not f.startswith("sources/")]
anclas = {}
for f in md:
    texto = open(f, encoding="utf-8").read()
    vistas, codigo, s = {}, False, set()
    vallas = 0
    for linea in texto.split("\n"):
        if linea.lstrip().startswith("```"):
            codigo = not codigo
            vallas += 1
            continue
        m = None if codigo else re.match(r"^#{1,6} (.*)", linea)
        if m:
            b = slug(m.group(1))
            n = vistas.get(b, 0)
            s.add(b if n == 0 else f"{b}-{n}")
            vistas[b] = n + 1
    s |= set(re.findall(r'<a id="([^"]+)"', texto))
    anclas[f] = s
    if vallas % 2:
        problemas.append(f"{f}: valla ``` sin cerrar")

for f in md:
    texto = open(f, encoding="utf-8").read()
    for m in re.finditer(r"\]\(([^)\s]+)\)", texto):
        destino = m.group(1)
        if re.match(r"(https?:|mailto:|\.\.\.)", destino):
            continue
        ruta, _, ancla = destino.partition("#")
        p = os.path.normpath(os.path.join(os.path.dirname(f), ruta)) if ruta else f
        if not os.path.exists(p):
            problemas.append(f"{f}: enlace roto -> {destino}")
        elif ancla and p.endswith(".md"):
            if unicodedata.normalize("NFC", ancla).lower() not in anclas.get(p, set()):
                problemas.append(f"{f}: ancla inexistente -> {destino}")

for d in SECCIONES:
    for f in sorted(glob.glob(f"{d}/[0-9][0-9]-*.md")):
        n = int(os.path.basename(f)[:2])
        texto = open(f, encoding="utf-8").read()
        if "<!-- nav -->" not in texto:
            problemas.append(f"{f}: sin navegación (ejecuta ./pdf/generar.sh)")
        if n == 0:
            continue
        h1 = next((l for l in texto.split("\n") if l.startswith("# ")), "")
        if not h1.startswith(f"# {n}. "):
            problemas.append(f"{f}: el H1 no empieza por '# {n}.' -> {h1[:60]}")

if shutil.which("pdfinfo") and os.path.exists("pdf/chuleta.pdf"):
    salida = subprocess.run(["pdfinfo", "pdf/chuleta.pdf"], capture_output=True, text=True).stdout
    paginas = re.search(r"Pages:\s+(\d+)", salida)
    if paginas and paginas.group(1) != "1":
        problemas.append(f"pdf/chuleta.pdf: {paginas.group(1)} páginas (debe caber en una)")

capitulos = {d: len(glob.glob(f"{d}/[0-9][0-9]-*.md")) - 1 for d in SECCIONES}
print("Capítulos (sin la introducción):", ", ".join(f"{d} {n}" for d, n in capitulos.items()),
      f"· total {sum(capitulos.values())}")
if problemas:
    print(f"\n{len(problemas)} problema(s):")
    print("\n".join("  - " + p for p in problemas))
    sys.exit(1)
print("Todo correcto.")
