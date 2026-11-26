"""Prueba de voz Chatterbox (Resemble AI, open source) — ES y EN, sin tocar el venv principal.
Corre con:  venv_chatter/bin/python probar_chatter.py
Opcional: pon una grabacion TUYA (o de alguien que te dio permiso) de ~10 s en _prueba_voz/referencia.wav
y la prueba tambien clona esa voz.
"""
from pathlib import Path
import torch, torchaudio as ta

dev = "mps" if torch.backends.mps.is_available() else "cpu"
_load = torch.load
torch.load = lambda *a, **k: _load(*a, **{**k, "map_location": k.get("map_location", torch.device(dev))})
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

OUT = Path("_prueba_voz"); OUT.mkdir(exist_ok=True)
REF = OUT / "referencia.wav"
TEXTOS = {
    "es": "Ya están jugando GTA 6 en Nueva Zelanda. ¿Y tú? ¿A qué hora te toca? Te lo muestro país por país.",
    "en": "In 1974, humans sent our address into space. On purpose. And a reply would take fifty thousand years.",
}
ESTILOS = {"natural": dict(exaggeration=0.5, cfg_weight=0.5), "expresiva": dict(exaggeration=0.75, cfg_weight=0.35)}

print(f"Cargando Chatterbox Multilingual en {dev} (la primera vez descarga ~3 GB)...")
m = ChatterboxMultilingualTTS.from_pretrained(device=dev)
for idi, txt in TEXTOS.items():
    for nombre, kw in ESTILOS.items():
        extra = {"audio_prompt_path": str(REF)} if REF.exists() else {}
        wav = m.generate(txt, language_id=idi, **kw, **extra)
        f = OUT / f"chatter_{idi}_{nombre}{'_clon' if extra else ''}.wav"
        ta.save(str(f), wav, m.sr)
        print("✅", f)
print("Listo. Escúchalas en la carpeta _prueba_voz/")
