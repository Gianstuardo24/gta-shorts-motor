#!/bin/bash
# uso: hacer.sh DIR ID voz vel lang pausa [joven]
# voz -> datos -> resolver offsets -> datos final. Deja DIR/ID.json, DIR/vz.wav, DIR/vz_palabras.json, DIR/datos.json
set -e
D=$1; ID=$2; VOZ=$3; VEL=$4; LANG=$5; PAU=$6; JOV=$7
cd /home/claude/escena
if [ -n "$JOV" ]; then
  python3 voz_local.py $D/${ID}_src.json $D/vz_base.wav $VOZ $VEL $LANG $PAU > /dev/null
  python3 joven.py $D/vz_base.wav $D/vz.wav > /dev/null
  cp $D/vz_base_palabras.json $D/vz_palabras.json
else
  python3 voz_local.py $D/${ID}_src.json $D/vz.wav $VOZ $VEL $LANG $PAU > /dev/null
fi
/home/claude/datos_de.sh $D/${ID}_src.json $D/vz.wav $D/vz_palabras.json $D/datos0.json
python3 /home/claude/resolver.py $D/${ID}_src.json $D/datos0.json $D/${ID}.json
/home/claude/datos_de.sh $D/${ID}.json $D/vz.wav $D/vz_palabras.json $D/datos.json
python3 -c "
import json;d=json.load(open('$D/datos.json'));T=d['T']
print('T:',' '.join(f'{k}={v:.2f}' for k,v in sorted(T.items(),key=lambda x:x[1])))
for f in d['frases']: print(' ',f if isinstance(f,str) else json.dumps(f,ensure_ascii=False)[:160])
"
