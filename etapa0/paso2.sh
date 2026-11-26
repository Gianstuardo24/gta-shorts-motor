bash <<'FIN'
cd ~/gta-shorts || exit 1
R=estandar-produccion/verificacion_etapa0.txt
B=~/respaldos/gta-shorts_2026-11-24
PROC="[Pp]ython[^ ]* (-u )?(estudio|movil|panel|diario|biblioteca|inteligencia|hooks|patrones|metricas|metricas_plus|fichas|lote)[.]py"
if pgrep -fl "$PROC" > /dev/null; then echo "DETENIDO: hay un proceso usando las bases. No se copio nada."; exit 1; fi
export PATH="$HOME/.local/bin:$HOME/.claude/local:/opt/homebrew/bin:/usr/local/bin:$PATH"
{
echo; echo "===== PASO 2 · RESPALDO Y VERIFICACIONES (Mac) · $(date) ====="
echo "== huella de las bases ANTES =="; shasum -a 256 datos/cerebro.db datos/inteligencia.db datos/metricas.db
echo "== respaldo =="
mkdir -p "$B"
rsync -a --exclude '/venv/' --exclude '/venv_chatter/' --exclude '/models/' \
  --exclude '/salida/' --exclude '/clips/' \
  --exclude '/tomas/' --exclude '/tomas_mdm/' --exclude '/tomas_rabbit/' \
  --exclude '/estudio_faceless/videos/' --exclude '__pycache__/' \
  ./ "$B/"
echo "rsync termino con codigo $?"
du -sh "$B"
echo "programas .py: origen $(ls *.py | wc -l) · respaldo $(ls "$B"/*.py | wc -l)"
echo "archivos en el respaldo: $(find "$B" -type f | wc -l)"
echo "== huella de las bases EN EL RESPALDO (debe ser igual a ANTES) =="
(cd "$B" && shasum -a 256 datos/cerebro.db datos/inteligencia.db datos/metricas.db)
echo "== huella de las bases DESPUES (debe ser igual a ANTES) =="
shasum -a 256 datos/cerebro.db datos/inteligencia.db datos/metricas.db
echo "== integridad (se revisa la copia del respaldo, no el original) =="
for d in cerebro inteligencia metricas; do
  echo "$d: $(sqlite3 -readonly "$B/datos/$d.db" 'PRAGMA integrity_check;' | head -3 | tr '\n' ' ')"
done
echo "== tablas y filas (copia del respaldo) =="
for d in cerebro inteligencia metricas; do
  echo "-- $d"
  for t in $(sqlite3 -readonly "$B/datos/$d.db" "SELECT name FROM sqlite_master WHERE type='table' ORDER BY 1;"); do
    echo "$t: $(sqlite3 -readonly "$B/datos/$d.db" "SELECT COUNT(*) FROM \"$t\";")"
  done
done
echo "== arsenal por estado, area y origen =="
sqlite3 -readonly "$B/datos/cerebro.db" "SELECT 'estado', estado, COUNT(*) FROM arsenal GROUP BY 2;"
sqlite3 -readonly "$B/datos/cerebro.db" "SELECT 'area', area, COUNT(*) FROM arsenal WHERE estado='activa' GROUP BY 2;"
sqlite3 -readonly "$B/datos/cerebro.db" "SELECT 'origen', origen, COUNT(*) FROM arsenal GROUP BY 2;"
sqlite3 -readonly "$B/datos/cerebro.db" "SELECT 'con uso propio', COUNT(*) FROM arsenal WHERE usos > 0;"
echo "== fichas de la biblioteca por tipo y categoria =="
sqlite3 -readonly "$B/datos/inteligencia.db" "SELECT tipo, categoria, COUNT(*) FROM analisis GROUP BY 1, 2;"
echo "== videos con curva de retencion =="
sqlite3 -readonly "$B/datos/metricas.db" "SELECT COUNT(DISTINCT id) FROM retencion;"
echo "== entorno =="
echo "macOS $(sw_vers -productVersion) · $(uname -m)"
./venv/bin/python3 -V
for c in claude ffmpeg sqlite3 rsync; do echo "$c: $(command -v $c || echo FALTA)"; done
ffmpeg -version 2>&1 | head -1
echo "Chrome: $(defaults read '/Applications/Google Chrome.app/Contents/Info' CFBundleShortVersionString 2>&1)"
echo "== paquetes del entorno (sin importarlos) =="
./venv/bin/python3 -B -c "
import importlib.util as u, importlib.metadata as m
for mod, dist in [('playwright','playwright'),('kokoro_onnx','kokoro-onnx'),('onnxruntime','onnxruntime'),('soundfile','soundfile'),('numpy','numpy'),('PIL','pillow')]:
    print(mod, m.version(dist) if u.find_spec(mod) else 'FALTA')
"
echo "== modelos de voz =="; ls -lh models
} >> "$R" 2>&1
echo "Listo. Resultado en ~/gta-shorts/$R"
FIN
