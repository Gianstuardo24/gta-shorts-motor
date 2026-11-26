#!/bin/bash
# uso: q2.sh SLOT ID VOZ VEL LANG [joven]  -> encola un render CON planificador de planos (nunca dos a la vez)
cd /home/claude/d24; (flock /tmp/render.lock ./uno2.sh "$@" > /tmp/uno_$1.log 2>&1 &) ; echo "encolado (con planos) $1"
