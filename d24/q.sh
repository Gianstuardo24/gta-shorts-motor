#!/bin/bash
# uso: q.sh SLOT ID VOZ VEL LANG [joven]  -> encola un render (nunca dos a la vez)
cd /home/claude/d24; (flock /tmp/render.lock ./uno.sh "$@" > /tmp/uno_$1.log 2>&1 &) ; echo "encolado $1"
