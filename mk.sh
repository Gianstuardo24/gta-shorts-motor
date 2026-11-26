P=/home/claude/escena/portada.py; T=/home/claude/txt.py; F=/home/claude/ficha.py; O=/mnt/user-data/outputs/d23n
mk(){ d=$1; id=$2; seg=$3; ptit="$4"; hora=$5; tit="$6"; desc="$7"; firma="$8"; tags="$9"; voz="${10}"; mus="${11}"; carp="${12}"; hh=${13}
 cd /home/claude/d23/$d; python3 $P v1.mp4 $seg "$ptit" portada.jpg; python3 $T $d.txt "Lun 23/11 $hora" "$tit" "$desc" "$firma" "$tags"; python3 $F $id.json datos.json "$voz" $mus ficha.json
 N="${hh}h - $(echo "$tit" | sed 's/ [^ ]*$//')"; cp v1.mp4 "$O/$N.mp4"; cp $d.txt "$O/$N.txt"; cp portada.jpg "$O/$N.portada.jpg"; cp ficha.json "$O/${carp}_2026-11-23_${hh}h.json"; }
