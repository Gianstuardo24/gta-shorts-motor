#!/bin/bash
# Instala Chatterbox en un venv APARTE (venv_chatter) para no romper el venv de la fabrica, y genera 4 muestras.
set -e
cd "$(dirname "$0")"
[ -d venv_chatter ] || python3 -m venv venv_chatter
venv_chatter/bin/pip install -q --upgrade pip
venv_chatter/bin/pip install -q chatterbox-tts
caffeinate -i venv_chatter/bin/python probar_chatter.py
open _prueba_voz
