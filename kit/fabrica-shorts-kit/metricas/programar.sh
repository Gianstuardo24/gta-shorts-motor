#!/bin/bash
# Deja las métricas corriendo solas en tu Mac (launchd):
#   · cada hora          → metricas.py        (vistas a las 2 h, 6 h, 24 h, 48 h)
#   · todos los días 08:20 → metricas_plus.py + fichas.py (enganche, retención, tráfico, fichas)
#   · domingos 09:30     → reporte_semanal.py  (analisis/reporte_AAAA-MM-DD.md)
# Si el Mac está dormido a esa hora, corre apenas despierta.
# Uso:   bash metricas/programar.sh          (programa)
#        bash metricas/programar.sh quitar   (desprograma)
KIT="$(cd "$(dirname "$0")/.." && pwd)"
LA="$HOME/Library/LaunchAgents"
PY="$KIT/venv/bin/python"
P0="$LA/com.fabricashorts.metricas.plist"; P1="$LA/com.fabricashorts.plus.plist"; P2="$LA/com.fabricashorts.reporte.plist"
if [ "$1" = "quitar" ]; then
  for P in "$P0" "$P1" "$P2"; do launchctl unload "$P" 2>/dev/null; rm -f "$P"; done
  echo "Desprogramado."; exit 0
fi
mkdir -p "$LA" "$KIT/logs" "$KIT/analisis"
plist () {   # $1 archivo  $2 label  $3 comando  $4 clave de horario  $5 valor
cat > "$1" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$2</string>
  <key>ProgramArguments</key><array><string>/bin/bash</string><string>-lc</string><string>$3</string></array>
  <key>$4</key>$5
</dict></plist>
PLIST
}
plist "$P0" com.fabricashorts.metricas \
  "cd \"$KIT\" &amp;&amp; \"$PY\" -u metricas/metricas.py &gt;&gt; logs/metricas.log 2&gt;&amp;1" \
  StartInterval "<integer>3600</integer>"
plist "$P1" com.fabricashorts.plus \
  "cd \"$KIT\" &amp;&amp; \"$PY\" -u metricas/metricas_plus.py &gt;&gt; logs/plus.log 2&gt;&amp;1; \"$PY\" -u metricas/fichas.py &gt;&gt; logs/plus.log 2&gt;&amp;1" \
  StartCalendarInterval "<dict><key>Hour</key><integer>8</integer><key>Minute</key><integer>20</integer></dict>"
plist "$P2" com.fabricashorts.reporte \
  "cd \"$KIT\" &amp;&amp; \"$PY\" -u metricas/reporte_semanal.py &gt;&gt; logs/reporte.log 2&gt;&amp;1" \
  StartCalendarInterval "<dict><key>Weekday</key><integer>0</integer><key>Hour</key><integer>9</integer><key>Minute</key><integer>30</integer></dict>"
for P in "$P0" "$P1" "$P2"; do launchctl unload "$P" 2>/dev/null; launchctl load "$P"; done
echo "✅ Métricas cada hora, extras a las 08:20 y reporte los domingos 09:30 (carpeta analisis/)."
