#!/bin/bash
R=/home/claude/render_par.sh
par(){ $R $1 &  if [ -n "$2" ]; then $R $2 & fi; wait; echo "LISTO $3"; }
par "/home/claude/c17c/C2026112101_04.json /home/claude/c17c/vz_C2026112101_04.wav /home/claude/c17c/vz_C2026112101_04_palabras.json /home/claude/c17c/f5.mp4 deep" "" "C17"
par "/home/claude/r18c/R2026112101_05.json /home/claude/r18c/vz_R2026112101_05.wav /home/claude/r18c/vz_R2026112101_05_palabras.json /home/claude/r18c/f5.mp4 dark" "/home/claude/g19c/G2026112101_05.json /home/claude/g19c/vz_G2026112101_05.wav /home/claude/g19c/vz_G2026112101_05_palabras.json /home/claude/g19c/f5.mp4 deep" "R18 G19"
par "/home/claude/en20b/G2026112102en_04.json /home/claude/en20b/vz_G2026112102en_04.wav /home/claude/en20b/vz_G2026112102en_04_palabras.json /home/claude/en20b/f5.mp4 deep" "/home/claude/m20c/M2026112101_04.json /home/claude/m20c/vz_M2026112101_04.wav /home/claude/m20c/vz_M2026112101_04_palabras.json /home/claude/m20c/f5.mp4 deep" "E20 M20"
par "/home/claude/c21b/C2026112102_03.json /home/claude/c21b/vz_C2026112102_03.wav /home/claude/c21b/vz_C2026112102_03_palabras.json /home/claude/c21b/f5.mp4 deep" "/home/claude/r22c/R2026112102_04.json /home/claude/r22c/vz_R2026112102_04.wav /home/claude/r22c/vz_R2026112102_04_palabras.json /home/claude/r22c/f5.mp4 dark" "C21 R22"
par "/home/claude/g22c/G2026112102_04.json /home/claude/g22c/vz_G2026112102_04.wav /home/claude/g22c/vz_G2026112102_04_palabras.json /home/claude/g22c/f5.mp4 deep" "/home/claude/en13d/G2026112101en_08.json /home/claude/en13d/vz8.wav /home/claude/en13d/vz8_palabras.json /home/claude/en13d/f5.mp4 deep" "G22 E13"
par "/home/claude/perro1/D2026112101_01.json /home/claude/perro1/vz.wav /home/claude/perro1/vz_palabras.json /home/claude/perro1/v3.mp4 deep" "/home/claude/gato1/K2026112101_01.json /home/claude/gato1/vz.wav /home/claude/gato1/vz_palabras.json /home/claude/gato1/v3.mp4 deep" "PERRO GATO"
echo TODO_LISTO
