#!/bin/bash
# Junta 00-16 en MAESTRO.md (una sola fuente: los archivos numerados)
cd "$(dirname "$0")"
{ echo "# MAESTRO · Estándar de producción de videos animados"; echo; echo "> Archivo generado: $(date '+%d-%m-%Y %H:%M'). No se edita a mano: se editan los archivos numerados y se corre armar_maestro.sh."; echo;
  for f in $(ls [0-9][0-9]-*.md | sort); do echo; echo "---"; echo; sed 's/^# /## /; t; s/^## /### /; t; s/^### /#### /' "$f"; done; } > MAESTRO.md
wc -l MAESTRO.md
