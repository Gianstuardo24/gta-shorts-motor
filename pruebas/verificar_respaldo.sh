#!/bin/bash
# E0 · prueba de recuperación en el contenedor: corre la comprobación portátil del respaldo y, además,
# restaura en una carpeta nueva, compara cada archivo con el entorno vivo y renderiza con el motor RESTAURADO.
# Uso: verificar_respaldo.sh CARPETA_DEL_RESPALDO NOMBRE_PRUEBA
set -o pipefail; R=$(cd "${1:?carpeta}" && pwd); NOM=${2:-prueba}; X=/tmp/recuperacion_$NOM; rm -rf $X; mkdir -p $X
cd $R || exit 1; N=$(ls motor_*.bundle.part-00 | sed 's/^motor_//;s/\.bundle\.part-00$//')
echo "######## A · comprobación portátil (la misma que se corre en el Mac)"
bash $R/comprobar_respaldo.sh $R || { echo "FALLA la comprobación portátil"; exit 1; }
echo "######## B · restaurar y comparar con el entorno vivo"
cat $R/motor_$N.bundle.part-* > $X/motor.bundle; cat $R/referencias_video_$N.tar.part-* > $X/ref.tar
git clone -q $X/motor.bundle $X/fabrica && tar -xf $X/ref.tar -C $X/fabrica/pruebas/ && rm $X/motor.bundle $X/ref.tar
echo "HEAD restaurado: $(git -C $X/fabrica rev-parse HEAD) · vivo: $(git -C /home/claude rev-parse HEAD)"
cd $X/fabrica; git ls-files -z | xargs -0 sha256sum > $X/rest.sha; cd /home/claude; git ls-files -z | xargs -0 sha256sum > $X/vivo.sha
cmp -s $X/rest.sha $X/vivo.sha && echo "OK: $(wc -l < $X/vivo.sha) archivos versionados idénticos al entorno vivo" || { echo "DIFERENCIAS:"; diff $X/rest.sha $X/vivo.sha | head; }
( cd $X/fabrica/pruebas && find referencias_video -type f -exec sha256sum {} + | sort -k2 ) > $X/rv_rest.sha
( cd /home/claude/pruebas && find referencias_video -type f -exec sha256sum {} + | sort -k2 ) > $X/rv_vivo.sha
cmp -s $X/rv_rest.sha $X/rv_vivo.sha && echo "OK: $(wc -l < $X/rv_vivo.sha) videos de referencia idénticos a los vivos" || echo "DIFERENCIAS en referencias_video"
echo "######## C · el motor RESTAURADO renderiza igual que la línea base (nivel rápido, corpus restaurado)"
cd $X/fabrica/pruebas && flock /tmp/render.lock python3 regresion.py --nivel rapido --motor $X/fabrica/escena/escena.html \
  --base lineas_base/rapido_motor_725e0dba.json --salida $X/rapido_restaurado.json | tail -12
