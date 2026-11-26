#!/bin/bash
R=/home/claude/render_par.sh
until grep -q "✅\|Error\|Traceback" /home/claude/g19c/f3.mp4.log 2>/dev/null && grep -q "✅\|Error\|Traceback" /home/claude/en20b/f3.mp4.log 2>/dev/null; do sleep 5; done
echo "LISTO G19 E20"
par(){ $R $1 &  if [ -n "$2" ]; then $R $2 & fi; wait; echo "LISTO $3"; }
par "/home/claude/r18c/R2026112101_05.json /home/claude/r18c/vz_R2026112101_05.wav /home/claude/r18c/vz_R2026112101_05_palabras.json /home/claude/r18c/f4.mp4 dark" "/home/claude/m20c/M2026112101_04.json /home/claude/m20c/vz_M2026112101_04.wav /home/claude/m20c/vz_M2026112101_04_palabras.json /home/claude/m20c/f3.mp4 deep" "R18 M20"
par "/home/claude/c21b/C2026112102_03.json /home/claude/c21b/vz_C2026112102_03.wav /home/claude/c21b/vz_C2026112102_03_palabras.json /home/claude/c21b/f3.mp4 deep" "/home/claude/r22c/R2026112102_04.json /home/claude/r22c/vz_R2026112102_04.wav /home/claude/r22c/vz_R2026112102_04_palabras.json /home/claude/r22c/f3.mp4 dark" "C21 R22"
par "/home/claude/g22c/G2026112102_04.json /home/claude/g22c/vz_G2026112102_04.wav /home/claude/g22c/vz_G2026112102_04_palabras.json /home/claude/g22c/f3.mp4 deep" "/home/claude/en13d/G2026112101en_08.json /home/claude/en13d/vz8.wav /home/claude/en13d/vz8_palabras.json /home/claude/en13d/f3.mp4 deep" "G22 E13"
par "/home/claude/m15c/M2026112102_04.json /home/claude/m15c/vz4.wav /home/claude/m15c/vz4_palabras.json /home/claude/m15c/f3.mp4 deep" "/home/claude/perro1/D2026112101_01.json /home/claude/perro1/vz.wav /home/claude/perro1/vz_palabras.json /home/claude/perro1/v1.mp4 deep" "M15 PERRO"
par "/home/claude/gato1/K2026112101_01.json /home/claude/gato1/vz.wav /home/claude/gato1/vz_palabras.json /home/claude/gato1/v1.mp4 deep" "" "GATO"
echo TODO_LISTO
