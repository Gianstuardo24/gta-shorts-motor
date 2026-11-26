bash <<'FIN'
cd ~/gta-shorts || exit 1
{
echo; echo "===== PASO 1 · COMPROBACION PREVIA (Mac) · $(date) ====="
echo "== procesos que usan las bases =="
pgrep -fl "[Pp]ython[^ ]* (-u )?(estudio|movil|panel|diario|biblioteca|inteligencia|hooks|patrones|metricas|metricas_plus|fichas|lote)[.]py" || echo "ninguno"
echo "== ultima linea de la corrida diaria =="; tail -1 logs/diario.log
echo "== archivos temporales de las bases =="
find datos -maxdepth 1 \( -name "*-journal" -o -name "*-wal" -o -name "*-shm" \) | grep . || echo "ninguno"
echo "== tareas programadas =="; launchctl list | grep viceverso || echo "ninguna"
echo "== espacio =="
T=$(du -sk . | cut -f1); E=0
for d in venv venv_chatter models salida clips tomas tomas_mdm tomas_rabbit estudio_faceless/videos; do
  [ -d "$d" ] && E=$((E + $(du -sk "$d" | cut -f1)))
done
L=$(df -k "$HOME" | tail -1 | awk '{print $4}')
echo "respaldo estimado: $(( (T - E) / 1024 )) MB · libre en disco: $(( L / 1024 )) MB"
echo "== carpetas mas pesadas (MB) =="; du -sk */ | sort -n | tail -10 | awk '{printf "%6d  %s\n", $1/1024, $2}'
} >> estandar-produccion/verificacion_etapa0.txt 2>&1
tail -32 estandar-produccion/verificacion_etapa0.txt
FIN
