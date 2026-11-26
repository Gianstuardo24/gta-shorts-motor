#!/bin/bash
# Arma UN solo video, con poca carga para que el Mac no se caliente:
#   prioridad baja (nice) + pausas para enfriar entre pasos.
# Cada lote trae un solo guion (ej: guiones/G2026111901_01.json).
# Uso:  bash armar_uno.sh gta G2026111901      (gta = GTA español)
#       bash armar_uno.sh en  G2026111901en    (GTA inglés)
#       bash armar_uno.sh rabbit R2026111901
#       bash armar_uno.sh mdm M2026111901
set -e
cd "$(dirname "$0")"
C=$1; L=$2
[ -z "$L" ] && { echo "Uso: bash armar_uno.sh <canal> <lote>"; exit 1; }
[ "$C" != gta ] && export CANAL=$C
mkdir -p portadas
f=~/Downloads/portada_${L}.png
[ -e "$f" ] && cp "$f" "portadas/${L}_narrado_01.png" && echo "🖼  portada copiada"
p(){ local t0=$(date +%s); nice -n 15 caffeinate -i python3 "$@"; local st=$?; mkdir -p datos
  echo "$(date +%Y-%m-%dT%H:%M),$L,$C,$1,$(( $(date +%s) - t0 )),$st" >> datos/produccion.csv; return $st; }   # tiempo por paso (costo)
MARCA=$(mktemp); touch "$MARCA"
enfriar(){ echo "❄️  pausa ${1:-40}s para enfriar…"; sleep ${1:-40}; }
echo "===== $C · $L ====="
if [ -z "$SIN_REVISION" ]; then
  p revisar.py "$L" --corregir || { echo "⛔ El guion no pasó la revisión (motivos arriba). Corrígelo y vuelve a correr. Saltarla bajo tu responsabilidad: SIN_REVISION=1 bash armar_uno.sh $C $L"; exit 1; }
  enfriar 10
fi
p voz.py "$L";            enfriar 20
p montar.py "$L";         enfriar 40
p subtitular.py "clips/${L}_narrado_momentos.json"; enfriar 20
p publicar.py "$L"
echo "🔍 Control final del video..."
find ~/Desktop/YouTube -name "*.mp4" -newer "$MARCA" -print0 | while IFS= read -r -d '' v; do
  python3 control_final.py "$v" || echo "⛔ Revisa los ❌ antes de subir: $v"
done
rm -f "$MARCA"
echo "✅ Listo $L. Avísale a Claude para ponerlo en el calendario."
