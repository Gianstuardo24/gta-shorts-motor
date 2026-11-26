#!/bin/bash
# Instala la Fábrica de Shorts en tu Mac. Uso:  bash instalar.sh
# Tarda ~5–10 min la primera vez (baja Python, ffmpeg, el navegador del motor y la voz). Se puede repetir sin problema.
set -e
cd "$(dirname "$0")"
KIT="$(pwd)"
echo "🏭 Instalando en: $KIT"

# 1) Homebrew (si falta, lo instalas tú: pide tu contraseña del Mac)
if ! command -v brew >/dev/null 2>&1; then
  for b in /opt/homebrew/bin/brew /usr/local/bin/brew; do [ -x "$b" ] && eval "$("$b" shellenv)"; done
fi
if ! command -v brew >/dev/null 2>&1; then
  echo ""
  echo "⚠️  Falta Homebrew. Pega esto en la Terminal, sigue lo que pida y vuelve a correr  bash instalar.sh :"
  echo '   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
  exit 1
fi

# 2) Python 3.12 y ffmpeg
brew list python@3.12 >/dev/null 2>&1 || brew install python@3.12
brew list ffmpeg >/dev/null 2>&1 || brew install ffmpeg
PY="$(brew --prefix python@3.12)/bin/python3.12"

# 3) Entorno de Python del kit
[ -d venv ] || "$PY" -m venv venv
./venv/bin/pip install -q --upgrade pip
./venv/bin/pip install -q -r requirements.txt
./venv/bin/pip install -q pyworld || echo "   (pyworld no se instaló: la voz 'joven' y el tono de preguntas quedan desactivados; todo lo demás funciona)"

# 4) Navegador que dibuja los cuadros del video
./venv/bin/python -m playwright install chromium

# 5) Voz Kokoro (modelo abierto, licencia Apache 2.0)
mkdir -p modelos
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  if [ ! -s "modelos/$f" ]; then
    echo "⬇️  $f…"
    curl -fL --retry 3 -o "modelos/$f" "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/$f" \
      || curl -fL --retry 3 -o "modelos/$f" "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f"
  fi
done

# 6) Sonidos propios (sintetizados, sin licencias de terceros) y carpetas
./venv/bin/python motor/crear_sonidos.py
mkdir -p datos guiones planes analisis logs secretos
SALIDA="$(./venv/bin/python -c 'import kit; print(kit.salida())')"
mkdir -p "$SALIDA"

# 7) Prueba rápida: cuadros del guion de ejemplo (no renderiza el video entero)
echo "🧪 Prueba del motor…"
./venv/bin/python motor/producir.py plantillas/guion-ejemplo.json --canal ejemplo --dia "$(date +%F)" --hora 18 --muestras 2 8 14 >/dev/null \
  && echo "   ✅ el motor funciona (cuadros en datos/trabajo/)" || echo "   ⚠️ la prueba falló: abre Claude en esta carpeta y pídele que lo revise"

echo ""
echo "✅ Listo. Siguiente paso: abre Claude Code en esta carpeta y dile:  «Quiero crear mi canal»"
echo "   Estudio:   ./venv/bin/python3 estudio/estudio.py   →  http://localhost:8765"
echo "   Videos en: $SALIDA"
