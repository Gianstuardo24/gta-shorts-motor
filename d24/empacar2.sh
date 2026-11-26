#!/bin/bash
# uso: empacar2.sh SLOT ID SEG "TXT PORTADA" "TITULO" "DESC" "FIRMA" "TAGS" "VOZ VEL" CARPETA   -> NUEVO - titulo.{mp4,txt,portada.jpg}
S=$1; ID=$2; D=/home/claude/d24/$S; O=/mnt/user-data/outputs/d24n; cd $D
python3 /home/claude/escena/portada.py v1.mp4 $3 "$4" portada.jpg >/dev/null
python3 /home/claude/txt.py $S.txt "Mar 24/11 · formato nuevo (uno por canal)" "$5" "$6" "$7" "$8" >/dev/null
python3 /home/claude/ficha.py $ID.json datos.json "$9" deep ficha.json >/dev/null
N="NUEVO - $(echo "$5" | sed 's/ [^ ]*$//')"
cp v1.mp4 "$O/$N.mp4"; cp $S.txt "$O/$N.txt"; cp portada.jpg "$O/$N.portada.jpg"; cp ficha.json "$O/${10}_2026-11-24_nuevo.json"; echo "$N"
