#!/bin/bash
# Cadena completa de un video del lote, en serie con las demás (candado propio): render → revisar → montar → empacar → lámina.
# Uso: bash cadena.sh <id> <carpeta de salida>      Registro: /tmp/fv2/lote/cadena_<id>.log
cd "$(dirname "$0")"; id=$1; car=$2
flock /tmp/cadena.lock bash -c "python3 kit.py $id datos >/dev/null 2>&1; python3 kit.py $id instalar && (python3 kit.py $id render > /tmp/fv2/lote/r_$id.log 2>&1 && python3 kit.py $id revisar && python3 kit.py $id montar && python3 kit.py $id empacar | tail -1 && python3 hoja.py $id '$car/${id}_previa.jpg' || tail -5 /tmp/fv2/lote/r_$id.log); echo FIN \$(date +%H:%M:%S)" > /tmp/fv2/lote/cadena_$id.log 2>&1
