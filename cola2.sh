#!/bin/bash
# procesa /home/claude/d22/cola.txt linea por linea (G V P O E), una a la vez; espera nuevas lineas
Q=${1:-/home/claude/d22/cola.txt}; touch $Q; n=0
while true; do
  L=$(sed -n "$((n+1))p" $Q)
  if [ -z "$L" ]; then sleep 5; continue; fi
  if [ "$L" = "FIN" ]; then echo COLA_FIN; exit 0; fi
  echo "$(date +%H:%M:%S) INICIO $L"; /home/claude/render_par.sh $L; echo "$(date +%H:%M:%S) LISTO $L"; n=$((n+1))
done
