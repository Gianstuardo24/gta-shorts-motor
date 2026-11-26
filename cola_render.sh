#!/bin/bash
# uso: cola_render.sh dir1:ID1 dir2:ID2 ...   (de a uno, en orden) -> v2.mp4 en cada carpeta
for x in "$@"; do d=${x%%:*}; id=${x##*:}; D=/home/claude/d23/$d
  /home/claude/render_par.sh $D/$id.json $D/vz.wav $D/vz_palabras.json $D/v2.mp4 deep >> /tmp/cola_render.log 2>&1
  echo "$(date +%H:%M) $d $(ls -la $D/v2.mp4 2>/dev/null | awk '{print $5}')" >> /tmp/cola_render.log
done
