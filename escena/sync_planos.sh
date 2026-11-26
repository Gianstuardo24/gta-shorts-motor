#!/bin/bash
# re-inserta planos.js en escena_h.html (entre marcadores)
cd /home/claude/escena && node -e "new Function(require('fs').readFileSync('planos.js','utf8'))" && python3 - <<'PY'
import re
h=open('escena_h.html').read(); p=open('planos.js').read()
i=h.index('/*PLANOS_INI*/'); j=h.index('/*PLANOS_FIN*/')
open('escena_h.html','w').write(h[:i]+'/*PLANOS_INI*/\n'+p+'\n'+h[j:]); print('sync ok')
PY
