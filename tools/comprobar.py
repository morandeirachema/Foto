#!/usr/bin/env python3
"""Comprueba la coherencia del repo. Uso: python3 tools/comprobar.py

- Enlaces relativos: el archivo existe y, si llevan #ancla, el encabezado también.
- Bloques de código: ninguna valla ``` sin cerrar (en GitHub ocultaría el resto).
- Capítulos: en conceptos/, manejo-a6700/, manejo-pixel-10-pro/ y retoques/, el H1 de NN-*.md empieza por "# N.".
- Navegación: cada capítulo tiene sus bloques <!-- nav --> (los genera pdf/generar-guia.sh).
- Hojas de campo: cada chuleta cabe en una cara (si existe pdfinfo).
- Nivel: cada capítulo abre con su línea de nivel (> 🟢/🔵/🔴/✅/📋), salvo las chuletas.
- Números: el texto de un enlace a un capítulo ("capítulo 9", "Manejo 9", "9 ·") coincide con el número del archivo.
- Recuentos: las insignias y tablas de capítulos de los README coinciden con los archivos.
- Sin marcas 🆕 (lo nuevo va fechado en NOVEDADES.md).
- Índices: cada informe y cada nota de investigación está enlazado desde algún sitio.
- Resumen: PENDIENTES abiertas por sección y preguntas de la autoevaluación por etapa.

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
SECCIONES = ("conceptos", "manejo-a6700", "manejo-pixel-10-pro", "retoques")
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

for hoja in ("pdf/chuleta.pdf", "pdf/chuleta-pixel.pdf"):
    if shutil.which("pdfinfo") and os.path.exists(hoja):
        salida = subprocess.run(["pdfinfo", hoja], capture_output=True, text=True).stdout
        paginas = re.search(r"Pages:\s+(\d+)", salida)
        if paginas and paginas.group(1) != "1":
            problemas.append(f"{hoja}: {paginas.group(1)} páginas (debe caber en una)")

# --- nivel, números, recuentos, marcas e índices (auditoría del 28 de noviembre de 2026) ---
CHULETAS = {"manejo-a6700/22-chuleta.md", "manejo-pixel-10-pro/13-chuleta.md"}
for d in SECCIONES:
    for f in sorted(glob.glob(f"{d}/[0-9][0-9]-*.md")):
        if f.endswith("00-introduccion.md") or f in CHULETAS:
            continue
        texto = open(f, encoding="utf-8").read()
        if not re.search(r"^> (🟢|🔵|🔴|✅|📋)", texto, re.M):
            problemas.append(f"{f}: sin línea de nivel (> 🟢/🔵/🔴 …)")

pat_num = re.compile(r"(?:capítulo|Capítulo|Manejo|Conceptos|Retoques)\s+(\d+)\b(?![.,]\d)|^\*{0,2}(\d+)(?= ·)")
for f in md:
    if f.startswith(("informes/", "notas-de-investigacion/")) or f.endswith("guia-completa.md"):
        continue
    texto = open(f, encoding="utf-8").read()
    for m in re.finditer(r"\[([^\]]*)\]\(([^)\s#]+\.md)(#[^)]*)?\)", texto):
        txt, ruta = m.group(1), m.group(2)
        p = os.path.normpath(os.path.join(os.path.dirname(f), ruta))
        sec, base = os.path.dirname(p), os.path.basename(p)
        if sec not in SECCIONES or not re.match(r"\d\d-", base):
            continue
        mm = pat_num.search(txt)
        if mm and int(mm.group(1) or mm.group(2)) != int(base[:2]):
            problemas.append(f"{f}: el texto [{txt}] no coincide con {base}")

def cuenta(d):
    return len(glob.glob(f"{d}/[0-9][0-9]-*.md")) - 1
total = sum(cuenta(d) for d in SECCIONES)
for d in SECCIONES:
    r = open(f"{d}/README.md", encoding="utf-8").read()
    m = re.search(r"capítulos-(\d+)", r)
    if m and int(m.group(1)) != cuenta(d):
        problemas.append(f"{d}/README.md: la insignia dice {m.group(1)} capítulos y hay {cuenta(d)}")
raiz = open("README.md", encoding="utf-8").read()
m = re.search(r"capítulos-(\d+)", raiz)
if m and int(m.group(1)) != total:
    problemas.append(f"README.md: la insignia dice {m.group(1)} capítulos y hay {total}")
for d in SECCIONES:
    m = re.search(r"\| \[`" + re.escape(d) + r"/`\]\(" + re.escape(d) + r"/\) \|[^|]*\| (\d+) \|", raiz)
    if m and int(m.group(1)) != cuenta(d):
        problemas.append(f"README.md: la tabla dice {m.group(1)} capítulos en {d} y hay {cuenta(d)}")

for f in md:
    if f in ("NOVEDADES.md", "CLAUDE.md") or f.startswith(("informes/", "notas-de-investigacion/")):
        continue
    if "🆕" in open(f, encoding="utf-8").read():
        problemas.append(f"{f}: marca 🆕 (lo nuevo se apunta con fecha en NOVEDADES.md)")

enlazados = set()
for f in md:
    for m in re.finditer(r"\]\(([^)\s#]+)", open(f, encoding="utf-8").read()):
        if not m.group(1).startswith("http"):
            enlazados.add(os.path.normpath(os.path.join(os.path.dirname(f), m.group(1))))
for f in md:
    if f.startswith(("informes/", "notas-de-investigacion/")) and f not in enlazados:
        problemas.append(f"{f}: ningún archivo enlaza a este informe o nota (añádelo a su README)")

pend, seccion = {}, None
for linea in open("PENDIENTES.md", encoding="utf-8"):
    if linea.startswith("## "):
        seccion = linea[3:].split(" · ")[0].strip()
    elif linea.startswith("- [ ]") and seccion:
        pend[seccion] = pend.get(seccion, 0) + 1
preg, etapa = {}, None
for linea in open("AUTOEVALUACION.md", encoding="utf-8"):
    if linea.startswith("## Etapa"):
        etapa = linea[3:].split(" · ")[0].strip()
    elif re.match(r"^\*\*[A-Z]*\d+[a-z]?\. ", linea) and etapa:
        preg[etapa] = preg.get(etapa, 0) + 1

capitulos = {d: len(glob.glob(f"{d}/[0-9][0-9]-*.md")) - 1 for d in SECCIONES}
print("Capítulos (sin la introducción):", ", ".join(f"{d} {n}" for d, n in capitulos.items()),
      f"· total {sum(capitulos.values())}")
print("PENDIENTES abiertas:", sum(pend.values()), "(" + ", ".join(f"§{k}: {v}" for k, v in pend.items()) + ")")
print("Autoevaluación:", sum(preg.values()), "preguntas (" + ", ".join(f"{k}: {v}" for k, v in preg.items()) + ")")
if problemas:
    print(f"\n{len(problemas)} problema(s):")
    print("\n".join("  - " + p for p in problemas))
    sys.exit(1)
print("Todo correcto.")
