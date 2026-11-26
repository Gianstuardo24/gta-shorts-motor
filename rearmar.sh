#!/bin/bash
# uso: rearmar.sh DIR ID   (mismo guion y voz; recalcula datos con la escena nueva)
set -e
D=/home/claude/d23/$1; ID=$2
cd $D && python3 b.py > /dev/null
/home/claude/datos_de.sh $D/${ID}_src.json $D/vz.wav $D/vz_palabras.json $D/datos0.json
python3 /home/claude/resolver.py $D/${ID}_src.json $D/datos0.json $D/${ID}.json | tail -1
/home/claude/datos_de.sh $D/${ID}.json $D/vz.wav $D/vz_palabras.json $D/datos.json
ls -la $D/datos.json | awk '{print $6,$7,$8}'
