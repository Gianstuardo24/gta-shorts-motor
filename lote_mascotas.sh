#!/bin/bash
while ! grep -q TODO_LISTO /tmp/lote_arriba.log; do sleep 10; done
R=/home/claude/render_par.sh
$R /home/claude/perro1/D2026112101_01.json /home/claude/perro1/vz.wav /home/claude/perro1/vz_palabras.json /home/claude/perro1/v1.mp4 deep &
$R /home/claude/gato1/K2026112101_01.json /home/claude/gato1/vz.wav /home/claude/gato1/vz_palabras.json /home/claude/gato1/v1.mp4 deep &
wait; echo MASCOTAS_LISTO
