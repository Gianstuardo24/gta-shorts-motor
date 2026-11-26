#!/bin/bash
# reconstruir.sh SLOT [SALIDA] [B.PY] · 27i bloque 4 · camino nuevo para rehacer un Short con el perfil de fondos.
# No toca uno2.sh, hacer.sh, la voz, d24/<slot> ni el corpus: escribe solo en SALIDA (por defecto rehacer/<slot>/).
#  1 b.py v2 (con el d24 de la rama; tiene que pedir v2=True)
#  2 voz y tiempos CONGELADOS del corpus (mismo guion aprobado: la narración no cambia)
#  3 datos → resolver → datos → post.py → planificador → datos que recibe el motor
#  4 validador y inspección de fondos ANTES del render: un error técnico detiene todo (salida 2)
#  5 render con el motor de la rama (nunca dos renders a la vez) → detector de cuadros aislados
#  6 hoja de control y vista de teléfono (rev.py --movil --tiempos)
# Salidas: 0 listo · 1 falla del camino · 2 bloqueado por errores técnicos (no se entrega).
set -uo pipefail
RAMA=$(cd "$(dirname "$0")" && pwd)
S=${1:?uso: reconstruir.sh SLOT [SALIDA] [B.PY]}; OUT=$(realpath -m "${2:-$RAMA/rehacer/$S}"); B=$(realpath -m "${3:-$OUT/b.py}")
COR=$RAMA/pruebas/corpus/produccion/$S
log(){ echo "[$(date +%H:%M:%S)] $*"; }
falla(){ log "FALLA: $*"; exit 1; }
[ -d "$COR" ] || falla "sin voz congelada para $S en el corpus"
case "$OUT/" in */d24/*|*/pruebas/corpus/*|/home/claude/escena/*) falla "SALIDA no permitida: $OUT";; esac
[ -f "$B" ] || falla "no existe $B"
ID=$(basename "$(ls "$COR"/*_src.json | head -1)" _src.json)
mkdir -p "$OUT"; cd "$OUT" || falla "no se puede entrar a $OUT"
log "slot $S · ID $ID · salida $OUT"

# 1 · b.py v2 con el d24 de la rama
sed "s#'/home/claude/d24'#'$RAMA/d24'#" "$B" > b_rama.py
grep -q "v2=True" b_rama.py || falla "el b.py no pide v2=True"
python3 b_rama.py > b.log 2>&1 || falla "b.py (ver b.log)"
[ -s "${ID}_src.json" ] || falla "b.py no escribió ${ID}_src.json"

# 2 · voz congelada
cp "$COR/vz.wav" "$COR/vz_palabras.json" .

# 3 · datos (armar_escena de la rama, solo hasta datos.json; se corta antes de dibujar)
datos(){                                   # arranca armar_escena (que empieza a dibujar): con el candado de render
  exec 9>/tmp/render.lock; flock 9
  local W PID; W=$(mktemp -d /tmp/rr.XXXX)
  cp "$RAMA"/escena/*.py "$RAMA"/escena/escena.html "$RAMA"/escena/*.ttf "$W"/ 2>/dev/null; cp -r "$RAMA/escena/sonidos" "$W"/
  setsid bash -c "cd '$W' && exec python3 armar_escena.py '$OUT/$1' '$OUT/vz.wav' '$OUT/vz_palabras.json' '$W/_x.mp4' deep" > /dev/null 2>&1 &
  PID=$!
  for _ in $(seq 1 240); do [ -s "$W/_tmp/datos.json" ] && sleep 0.3 && break; sleep 0.5; done
  kill -- -"$PID" 2>/dev/null; wait "$PID" 2>/dev/null
  cp "$W/_tmp/datos.json" "$OUT/$2" 2>/dev/null; local ok=$?; rm -rf "$W"; flock -u 9; exec 9>&-
  [ $ok -eq 0 ] || falla "datos de $1"
}
datos "${ID}_src.json" datos0.json
python3 "$RAMA/resolver.py" "${ID}_src.json" datos0.json "${ID}.json" > resolver.log 2>&1 || falla "resolver (ver resolver.log)"
datos "${ID}.json" datos.json
python3 "$RAMA/d24/post.py" "$OUT" "$ID" > post.log 2>&1 || falla "post.py (ver post.log)"
python3 "$RAMA/planos_shorts.py" "$OUT" "$ID" > planos.txt 2>&1 || falla "planificador (ver planos.txt)"
datos "${ID}.json" datos_render.json
log "datos listos · $(head -1 planos.txt)"

# 4 · validador e inspección antes del render
python3 "$RAMA/herramientas/validar.py" datos_render.json --salida validador.json --estricto > validador.txt 2>&1
if [ $? -ne 0 ]; then log "BLOQUEADO: el validador encontró errores en los datos (validador.txt)"; exit 2; fi
flock /tmp/render.lock python3 "$RAMA/herramientas/inspeccion_fondos.py" datos_render.json --salida inspeccion.json --hoja hoja_inspeccion.png > inspeccion.txt 2>&1
if [ $? -ne 0 ]; then log "BLOQUEADO: errores técnicos en la inspección (inspeccion.txt)"; cat inspeccion.txt | grep -v "/"; exit 2; fi
log "inspección: $(grep -m1 "cuadros en" inspeccion.txt)"

# 5 · render con el motor de la rama
W=$(mktemp -d /tmp/rr.XXXX)
cp "$RAMA"/escena/*.py "$RAMA"/escena/escena.html "$RAMA"/escena/*.ttf "$W"/ 2>/dev/null; cp -r "$RAMA/escena/sonidos" "$W"/
log "render…"
( cd "$W" && flock /tmp/render.lock python3 armar_escena.py "$OUT/$ID.json" "$OUT/vz.wav" "$OUT/vz_palabras.json" "$OUT/v1.mp4" deep > "$OUT/v1.mp4.log" 2>&1 )
rm -rf "$W"
[ -s v1.mp4 ] || falla "render (ver v1.mp4.log)"
python3 "$RAMA/herramientas/saltos.py" v1.mp4 --datos datos_render.json --json saltos.json --salida tiras > saltos.txt 2>&1
if grep -q "REVISAR" saltos.txt; then log "BLOQUEADO: cuadros aislados en el video (saltos.txt)"; exit 2; fi

# 6 · hoja de control y vista de teléfono
python3 "$RAMA/d24/rev.py" "$S" --dir "$OUT" --movil --tiempos > rev.txt 2>&1 || falla "rev.py (ver rev.txt)"
log "listo: $OUT/v1.mp4 · $(cat rev.txt | tr '\n' ' ')"
exit 0
