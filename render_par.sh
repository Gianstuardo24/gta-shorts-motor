#!/bin/bash
# uso: render_par.sh guion voz palabras salida estilo  (corre en carpeta propia para no pisar _tmp)
set -e
G=$1; V=$2; P=$3; O=$4; E=$5
W=$(mktemp -d /tmp/rw.XXXX)
cp /home/claude/escena/*.py /home/claude/escena/escena.html /home/claude/escena/*.ttf $W/ 2>/dev/null || true
cp -r /home/claude/escena/sonidos $W/ 2>/dev/null || true
cd $W && python3 armar_escena.py $G $V $P $O $E > $O.log 2>&1 && echo "OK $O" || echo "FAIL $O"
