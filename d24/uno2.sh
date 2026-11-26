#!/bin/bash
# uso: uno.sh SLOT ID VOZ VEL LANG [joven]  -> b.py, voz, tiempos, render, hoja de control
S=$1; ID=$2; D=/home/claude/d24/$S; cd $D || exit 1
python3 b.py || { echo "FALLO b.py"; exit 1; }
/home/claude/hacer.sh $D $ID $3 $4 $5 0.12 $6 > $D/hacer.log 2>&1 || { echo "FALLO hacer"; tail -5 $D/hacer.log; exit 1; }
python3 /home/claude/d24/post.py $D $ID || { echo "FALLO post"; exit 1; }
python3 /home/claude/planos_shorts.py $D $ID > $D/planos.txt 2>&1 || { echo "FALLO planos"; tail -3 $D/planos.txt; exit 1; }; head -2 $D/planos.txt
grep -c . $D/hacer.log >/dev/null; python3 -c "
import json;d=json.load(open('$D/datos.json'));print('duracion',round(d['T']['fin'],1),'s · marcadores',len(d['T']))"
grep -iE "sin resolver|no encontr|error|warn" $D/hacer.log | head -5
/home/claude/render_par.sh $D/$ID.json $D/vz.wav $D/vz_palabras.json $D/v1.mp4 deep
[ -s $D/v1.mp4 ] || { tail -8 $D/v1.mp4.log; exit 1; }
dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $D/v1.mp4); paso=$(python3 -c "print(round($dur/8,2))")
ffmpeg -hide_banner -loglevel error -y -i $D/v1.mp4 -vf "fps=1/$paso,scale=216:-2,tile=8x1:padding=2" -frames:v 1 -q:v 5 /tmp/qc_$S.jpg; echo "video $dur s · hoja /tmp/qc_$S.jpg"
