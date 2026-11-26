#!/bin/bash
# uso: empacar.sh SLOT ID SEG "TXT PORTADA" HH "TITULO" "DESC" "FIRMA" "TAGS" "VOZ VEL" CARPETA
S=$1; ID=$2; D=/home/claude/d24/$S; O=/mnt/user-data/outputs/d24n; cd $D
python3 /home/claude/escena/portada.py v1.mp4 $3 "$4" portada.jpg >/dev/null 2>&1
python3 /home/claude/txt.py $S.txt "Mar 24/11 $5:00" "$6" "$7" "$8" "$9" >/dev/null
python3 /home/claude/ficha.py $ID.json datos.json "${10}" deep ficha.json >/dev/null
N="${5}h - $(echo "$6" | sed 's/ [^ ]*$//')"; cp v1.mp4 "$O/$N.mp4"; cp $S.txt "$O/$N.txt"; cp portada.jpg "$O/$N.portada.jpg"; cp ficha.json "$O/${11}_2026-11-24_${5}h.json"; echo "$N"
