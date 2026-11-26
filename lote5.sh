#!/bin/bash
until grep -q "LISTO M15 PERRO" /tmp/lote4.log; do sleep 5; done
R=/home/claude/render_par.sh
$R /home/claude/g19c/G2026112101_05.json /home/claude/g19c/vz_G2026112101_05.wav /home/claude/g19c/vz_G2026112101_05_palabras.json /home/claude/g19c/f4.mp4 deep &
$R /home/claude/c21b/C2026112102_03.json /home/claude/c21b/vz_C2026112102_03.wav /home/claude/c21b/vz_C2026112102_03_palabras.json /home/claude/c21b/f4.mp4 deep &
wait; echo "LISTO G19 C21"
echo TODO_LISTO
