"""Arma una COPIA del motor de la rama con el bloque dc_mdm_ insertado. No modifica escena/escena.html.
Uso: python3 instalar.py CARPETA_DESTINO   (copia también render.py y las fuentes)"""
import sys, pathlib, shutil, hashlib
AQUI = pathlib.Path(__file__).resolve().parent
RAMA = AQUI.parents[2]
dst = pathlib.Path(sys.argv[1]); dst.mkdir(parents=True, exist_ok=True)
src = RAMA / "escena" / "escena.html"
s = src.read_text(encoding="utf-8"); b = (AQUI / "dc_mdm_bloque.js").read_text(encoding="utf-8")
marca = "// ===== P27 · FIN =====\n</script>"
assert s.count(marca) == 1, "no encuentro el final del bloque P27"
assert "DC_MDM" not in s, "el motor de la rama no debe contener el bloque"
(dst / "escena.html").write_text(s.replace(marca, marca + "\n" + b), encoding="utf-8")
for f in list((RAMA / "escena").glob("*.ttf")) + [RAMA / "escena" / "render.py"]: shutil.copy(f, dst / f.name)
print("motor de la rama", hashlib.sha256(src.read_bytes()).hexdigest()[:8], "→ copia con dc_mdm en", dst)
