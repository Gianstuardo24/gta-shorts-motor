#!/bin/bash
until grep -q TODO_LISTO /tmp/lote4.log || grep -q TODO_LISTO /tmp/lote5.log; do sleep 5; done
R=/home/claude/render_par.sh
$R /home/claude/perro1/D2026112101_01.json /home/claude/perro1/vz.wav /home/claude/perro1/vz_palabras.json /home/claude/perro1/v2.mp4 deep
echo TODO_LISTO
