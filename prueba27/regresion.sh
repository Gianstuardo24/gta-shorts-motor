#!/bin/bash
# Prueba 27 · compara 9 cuadros de producción contra la línea base (semilla fija)
cd /home/claude/prueba27/base; rm -rf rx; mkdir rx
for s in COgH:6.5:27:48 CSa7:5:24:44 wCc0:7:31:56; do IFS=: read id a b c <<< "$s"; python3 ../cuadros.py /home/claude/escena/escena.html datos_$id.json rx/$id $a $b $c; done > rx/hash.txt
if diff -q hash_base.txt rx/hash.txt >/dev/null; then echo "REGRESION OK: 9/9 cuadros idénticos"; else echo "REGRESION FALLA"; diff hash_base.txt rx/hash.txt; fi
