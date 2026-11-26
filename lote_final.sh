#!/bin/bash
R=/home/claude/render_par.sh
$R /home/claude/c17c/C2026112101_04.json /home/claude/c17c/vz_C2026112101_04.wav /home/claude/c17c/vz_C2026112101_04_palabras.json /home/claude/c17c/fin.mp4 deep &
$R /home/claude/r18c/R2026112101_05.json /home/claude/r18c/vz_R2026112101_05.wav /home/claude/r18c/vz_R2026112101_05_palabras.json /home/claude/r18c/fin.mp4 dark &
wait
$R /home/claude/g19c/G2026112101_05.json /home/claude/g19c/vz_G2026112101_05.wav /home/claude/g19c/vz_G2026112101_05_palabras.json /home/claude/g19c/fin.mp4 deep &
$R /home/claude/en20b/G2026112102en_04.json /home/claude/en20b/vz_G2026112102en_04.wav /home/claude/en20b/vz_G2026112102en_04_palabras.json /home/claude/en20b/fin.mp4 deep &
wait
$R /home/claude/m20c/M2026112101_04.json /home/claude/m20c/vz_M2026112101_04.wav /home/claude/m20c/vz_M2026112101_04_palabras.json /home/claude/m20c/fin.mp4 deep &
$R /home/claude/c21b/C2026112102_03.json /home/claude/c21b/vz_C2026112102_03.wav /home/claude/c21b/vz_C2026112102_03_palabras.json /home/claude/c21b/fin.mp4 deep &
wait
$R /home/claude/r22c/R2026112102_04.json /home/claude/r22c/vz_R2026112102_04.wav /home/claude/r22c/vz_R2026112102_04_palabras.json /home/claude/r22c/fin.mp4 dark &
$R /home/claude/g22c/G2026112102_04.json /home/claude/g22c/vz_G2026112102_04.wav /home/claude/g22c/vz_G2026112102_04_palabras.json /home/claude/g22c/fin.mp4 deep &
wait
echo TODO_LISTO
