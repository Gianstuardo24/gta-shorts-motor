#!/bin/bash
# E0 · comparaciones iniciales largas (se corre una vez con flock: nunca dos renders a la vez)
cd /home/claude/pruebas; set -o pipefail
echo "== 1 · nivel completo, motor actual (línea base)"; date
python3 regresion.py --nivel completo --salida lineas_base/completo_motor_725e0dba.json
echo "== 2 · nivel completo, motor de entrega del 25-nov (solo los 7 videos) contra la línea base"; date
python3 regresion.py --nivel completo --motor corpus/motor_entrega_25nov/escena.html --items wd2,wk2,wc1,wm2,wr1,wge2,wgs1 --base lineas_base/completo_motor_725e0dba.json --salida informes/completo_motor_entrega.json; echo "salida $?"
echo "== 3 · nivel completo, planos, segunda corrida"; date
python3 regresion.py --nivel completo --items plano04,plano05,plano06,plano10 --base lineas_base/completo_motor_725e0dba.json --salida informes/completo_planos_corrida2.json; echo "salida $?"
echo "== 4 · camino real (render.py sin modificar + semilla) de los planos contra los videos aprobados"; date
mkdir -p lineas_base/camino_real /tmp/cr
for pl in 04 05 06 10; do
  D=corpus/planos/$pl/datos.json; FIN=$(python3 -c "import json;print(json.load(open('$D'))['T']['fin'])")
  python3 render_semilla.py 0.15 $FIN 30 /tmp/cr/plano$pl.mp4 $D > /dev/null
  ffmpeg -v error -i /tmp/cr/plano$pl.mp4 -map 0:v -f framemd5 - | grep -v "^#" > lineas_base/camino_real/plano$pl.framemd5
  ffmpeg -v error -i referencias_video/plano${pl}_aprobado.mp4 -map 0:v -f framemd5 - | grep -v "^#" > /tmp/cr/plano${pl}_aprobado.framemd5
  a=$(awk -F, '{print $NF}' lineas_base/camino_real/plano$pl.framemd5 | md5sum | cut -c1-12); b=$(awk -F, '{print $NF}' /tmp/cr/plano${pl}_aprobado.framemd5 | md5sum | cut -c1-12)
  n=$(wc -l < lineas_base/camino_real/plano$pl.framemd5); m=$(wc -l < /tmp/cr/plano${pl}_aprobado.framemd5)
  echo "plano$pl: $n cuadros · aprobado $m cuadros · $( [ "$a" = "$b" ] && echo 'IDÉNTICO al video aprobado' || echo "DISTINTO ($a vs $b)")"
done
echo "== 5 · camino real de wd2, dos corridas"; date
for r in 1 2; do python3 render_semilla.py 0 $(python3 -c "print((1413+0.5)/30)") 30 /tmp/cr/wd2_r$r.mp4 corpus/produccion/wd2/datos_render.json > /dev/null
  ffmpeg -v error -i /tmp/cr/wd2_r$r.mp4 -map 0:v -f framemd5 - | grep -v "^#" > /tmp/cr/wd2_r$r.framemd5; done
cp /tmp/cr/wd2_r1.framemd5 lineas_base/camino_real/wd2.framemd5
echo "wd2: $(wc -l < /tmp/cr/wd2_r1.framemd5) cuadros · corridas $(cmp -s /tmp/cr/wd2_r1.framemd5 /tmp/cr/wd2_r2.framemd5 && echo IDÉNTICAS || echo DISTINTAS)"
echo "== 6 · cordura contra los videos entregados (con tolerancia)"; date
python3 comparar_entregados.py
echo "== fin"; date
