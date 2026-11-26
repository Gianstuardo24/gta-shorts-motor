#!/bin/bash
# uso: datos_de.sh guion voz palabras salida_datos   (corta el armado apenas existe _tmp/datos.json)
W=$(mktemp -d /tmp/dd.XXXX); cp /home/claude/escena/*.py /home/claude/escena/escena.html /home/claude/escena/escena_h.html /home/claude/escena/*.ttf $W/ 2>/dev/null; cp -r /home/claude/escena/sonidos $W/ 2>/dev/null
cd $W && (python3 armar_largo.py "$1" "$2" "$3" /tmp/_x_$$.mp4 deep >/dev/null 2>&1 &) ; for i in $(seq 1 120); do [ -s _tmp/datos.json ] && sleep 0.3 && break; sleep 0.5; done
cp _tmp/datos.json "$4" 2>/dev/null || echo "FALLO datos_de (ver armar_escena)"; pkill -f "armar_largo.py $1" 2>/dev/null; pkill -f "_x_$$.mp4" 2>/dev/null; pkill -f "$W/render_h.py" 2>/dev/null; cd /; rm -rf $W
