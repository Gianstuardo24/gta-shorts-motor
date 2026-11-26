#!/bin/bash
# uso: hoja_video.sh video.mp4 salida.png  -> 8 cuadros repartidos
V=$1; O=$2; D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V"); T=$(mktemp -d)
for i in 0 1 2 3 4 5 6 7; do t=$(python3 -c "print(round($D*(0.03+$i*0.135),2))"); ffmpeg -y -loglevel error -ss $t -i "$V" -frames:v 1 -vf scale=270:-1 $T/$i.png; done
python3 -c "
from PIL import Image;import glob
ims=[Image.open(f'$T/{i}.png') for i in range(8)];c=Image.new('RGB',(270*8,ims[0].height))
[c.paste(im,(i*270,0)) for i,im in enumerate(ims)];c.save('$O')"; rm -rf $T; echo "dur $D"
