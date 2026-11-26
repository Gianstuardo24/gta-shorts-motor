#!/bin/bash
# uso: empacar25.sh SLOT ID SEG "TXT PORTADA" HH "TITULO" "DESC" "FIRMA" "TAGS" "VOZ VEL" CANAL  -> /mnt/user-data/outputs/d25/CANAL/HHh - titulo.{mp4,txt,portada.jpg}
S=$1; ID=$2; D=/home/claude/d24/$S; O=/mnt/user-data/outputs/d25/${11}; mkdir -p "$O"; cd $D
python3 /home/claude/escena/portada.py v1.mp4 $3 "$4" portada.jpg >/dev/null 2>&1
python3 /home/claude/txt.py $S.txt "Mié 25/11 $5:00" "$6" "$7" "$8" "$9" >/dev/null
python3 /home/claude/ficha.py $ID.json datos.json "${10}" deep ficha.json >/dev/null 2>&1
N="${5}h - $(echo "$6" | sed 's/ [^ ]*$//' | tr -d ':')"; cp v1.mp4 "$O/$N.mp4"; cp $S.txt "$O/$N.txt"; cp portada.jpg "$O/$N.portada.jpg"; cp ficha.json "/mnt/user-data/outputs/d25/${11}_${ID}_${5}h.json" 2>/dev/null; echo "$O/$N"
