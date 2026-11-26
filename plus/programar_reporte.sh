#!/bin/bash
# Programa en tu Mac (launchd, igual que programar_metricas.sh):
#   · todos los días 08:20 → metricas_plus.py + fichas.py   (enganche, retención, tráfico y fichas)
#   · cada domingo 09:30   → reporte_semanal.py             (analisis/reporte_AAAA-MM-DD.md)
# Si el Mac está dormido a esa hora, corre apenas despierte.
# Uso:   bash programar_reporte.sh          (programa)
#        bash programar_reporte.sh quitar   (desprograma)
# Registro: ~/gta-shorts/logs/plus.log y ~/gta-shorts/logs/reporte.log
DIR="$HOME/gta-shorts"
LA="$HOME/Library/LaunchAgents"
P1="$LA/com.viceverso.plus.plist"
P2="$LA/com.viceverso.reporte.plist"
if [ "$1" = "quitar" ]; then
  launchctl unload "$P1" 2>/dev/null; launchctl unload "$P2" 2>/dev/null; rm -f "$P1" "$P2"
  echo "Desprogramado."; exit 0
fi
mkdir -p "$LA" "$DIR/logs" "$DIR/analisis"
plist () {   # $1 archivo  $2 label  $3 comando  $4 bloque de horario
cat > "$1" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$2</string>
  <key>ProgramArguments</key><array>
    <string>/bin/bash</string><string>-lc</string>
    <string>$3</string>
  </array>
  <key>StartCalendarInterval</key>$4
</dict></plist>
PLIST
}
PY="$DIR/venv/bin/python"
plist "$P1" com.viceverso.plus \
  "cd \"$DIR\" &amp;&amp; \"$PY\" -u metricas_plus.py &gt;&gt; \"$DIR/logs/plus.log\" 2&gt;&amp;1; \"$PY\" -u fichas.py &gt;&gt; \"$DIR/logs/plus.log\" 2&gt;&amp;1" \
  "<dict><key>Hour</key><integer>8</integer><key>Minute</key><integer>20</integer></dict>"
plist "$P2" com.viceverso.reporte \
  "cd \"$DIR\" &amp;&amp; \"$PY\" -u reporte_semanal.py &gt;&gt; \"$DIR/logs/reporte.log\" 2&gt;&amp;1" \
  "<dict><key>Weekday</key><integer>0</integer><key>Hour</key><integer>9</integer><key>Minute</key><integer>30</integer></dict>"
for P in "$P1" "$P2"; do launchctl unload "$P" 2>/dev/null; launchctl load "$P"; done
echo "✅ Diario 08:20 (métricas extra + fichas) y domingos 09:30 (reporte en analisis/)."
