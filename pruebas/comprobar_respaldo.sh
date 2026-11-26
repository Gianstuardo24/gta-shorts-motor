#!/bin/bash
# Comprueba un respaldo del motor SIN depender del contenedor: viaja dentro de cada respaldo.
# Rearma las partes en una carpeta temporal, clona el bundle y verifica commit, motor, corpus y videos.
# Uso (dentro de la carpeta del respaldo):  bash comprobar_respaldo.sh      · sale con 0 si todo está bien
R=$(cd "${1:-$(dirname "$0")}" && pwd); T=$(mktemp -d); trap 'rm -rf "$T"' EXIT; F=0
if command -v sha256sum >/dev/null 2>&1; then SHA="sha256sum"; else SHA="shasum -a 256"; fi
mal() { echo "FALLA: $*"; F=1; }
cd "$R" || exit 1; N=$(ls motor_*.bundle.part-00 | sed 's/^motor_//;s/\.bundle\.part-00$//')
echo "== respaldo $N"
echo "== 1 · sumas de cada parte";  $SHA -c --quiet SHA256SUMS && echo "OK: $(wc -l < SHA256SUMS | tr -d ' ') archivos íntegros" || mal "sumas de las partes"
echo "== 2 · rearmar el bundle y los videos"
cat motor_$N.bundle.part-* > "$T/motor_$N.bundle"; cat referencias_video_$N.tar.part-* > "$T/referencias_video_$N.tar"
( cd "$T" && $SHA -c --quiet "$R/SHA256_completos.txt" ) && echo "OK: bundle y tar completos íntegros" || mal "bundle o tar rearmado"
echo "== 3 · clonar el bundle"
RF=$(git bundle list-heads "$T/motor_$N.bundle" 2>/dev/null | wc -l | tr -d ' '); [ "$RF" -gt 0 ] && echo "OK: bundle legible ($RF referencias)" || mal "bundle ilegible"
git clone -q "$T/motor_$N.bundle" "$T/fabrica" 2>/dev/null || mal "no se pudo clonar"
git -C "$T/fabrica" fsck --no-progress >/dev/null 2>&1 && echo "OK: repositorio sin errores (fsck)" || mal "fsck"
H=$(git -C "$T/fabrica" rev-parse HEAD); [ "$H" = "$(cat COMMIT.txt)" ] && echo "OK: commit $H" || mal "commit $H ≠ $(cat COMMIT.txt)"
echo "   etiquetas: $(git -C "$T/fabrica" tag | tr '\n' ' ')· archivos versionados: $(git -C "$T/fabrica" ls-files | wc -l | tr -d ' ')"
echo "== 4 · motor de referencia"
( cd "$T/fabrica" && $SHA -c --quiet "$R/MOTOR_SHA256.txt" ) && echo "OK: escena/escena.html $(cut -c1-16 MOTOR_SHA256.txt)…" || mal "el motor no coincide"
echo "== 5 · corpus y videos de referencia contra el manifiesto"
tar -xf "$T/referencias_video_$N.tar" -C "$T/fabrica/pruebas/" || mal "no se pudo abrir el tar"
python3 - "$T/fabrica/pruebas" <<'PY' || F=1
import hashlib, json, pathlib, sys
P = pathlib.Path(sys.argv[1]); m = json.loads((P / "corpus/manifiesto.json").read_text())
h = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
vid = sum(h(P / it["video"]["archivo"]) == it["video"]["sha256"] for it in m["items"])
arch = tot = 0
for it in m["items"]:
    base = P / "corpus" / ("produccion" if it["tipo"] == "produccion" else "planos") / it["id"].replace("plano", "")
    for nom, d in it["archivos"].items():
        tot += 1; arch += (base / nom).exists() and h(base / nom) == d["sha256"]
me = h(P / "corpus/motor_entrega_25nov/escena.html") == m["motor_entrega_25nov"]["escena.html"]
ok = vid == len(m["items"]) and arch == tot and me
print(f"{'OK' if ok else 'FALLA'}: {vid}/{len(m['items'])} videos, {arch}/{tot} archivos del corpus y "
      f"motor de entrega {'íntegro' if me else 'DISTINTO'} (sha256 del manifiesto)")
sys.exit(0 if ok else 1)
PY
echo "== 6 · documentos del estándar"
D=$(tar -tf estandar-produccion_$N.tar 2>/dev/null | grep -c '\.md$'); [ "$D" -gt 0 ] && echo "OK: la copia de los documentos se abre ($D archivos .md)" || mal "copia de documentos"
[ $F = 0 ] && echo "== TODO OK: el respaldo se abre y se recupera completo" || echo "== HAY FALLAS"
exit $F
