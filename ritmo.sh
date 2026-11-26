#!/bin/bash
# ritmo.sh video.mp4 [umbral]  -> cortes duros, cortes/min, primer corte (mismo método que el laboratorio)
f="$1"; u="${2:-0.25}"
dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
t=$(ffmpeg -hide_banner -i "$f" -vf "select='gt(scene,$u)',showinfo" -an -f null - 2>&1 | grep -o 'pts_time:[0-9.]*' | cut -d: -f2 | awk '$1>0.3' | tr '\n' ' ')
python3 - "$dur" "$t" <<'EOF'
import sys
d=float(sys.argv[1]); t=[float(x) for x in sys.argv[2].split()]
pm=len(t)/d*60
huecos=[b-a for a,b in zip([0]+t,t+[d])]
print(f"dur={d:.1f}s cortes={len(t)} por_min={pm:.1f} primero={t[0] if t else '-'} hueco_max={max(huecos):.1f}s",
      "OK" if pm>=15 and max(huecos)<=5 else "LENTO (meta ≥15/min, hueco ≤5 s)")
EOF
