#!/bin/bash
# uso: entregar.sh DIR SEG "NOMBRE ARCHIVO SIN EXTENSION"  -> deja v2.mp4 + portada nueva en /mnt/user-data/outputs/v2_23n/DIR/
D=/home/claude/d23/$1; SEG=$2; N="$3"; O=/mnt/user-data/outputs/v2_23n/$1; mkdir -p "$O/viejo"
TIT=$(python3 -c "import json,glob;print(json.load(open(glob.glob('$D/*_src.json')[0]))['texto_pantalla'])")
cd $D && python3 /home/claude/escena/portada.py v2.mp4 $SEG "$TIT" portada2.jpg > /dev/null 2>&1
cp v2.mp4 "$O/$N.mp4"; cp portada2.jpg "$O/$N.portada.jpg"; cp v1.mp4 "$O/viejo/$N.mp4"; cp portada.jpg "$O/viejo/$N.portada.jpg"
ls -la "$O" | tail -3; echo "portada: $TIT"
