"""Configuración común del kit: config.json + canales/*.json (cada canal es un archivo)."""
import json
from pathlib import Path
from zoneinfo import ZoneInfo

RAIZ_KIT = Path(__file__).resolve().parent


def config():
    return json.loads((RAIZ_KIT / "config.json").read_text(encoding="utf-8"))


def salida():
    return Path(config().get("carpeta_salida", "~/Desktop/Shorts")).expanduser()


def zona():
    return ZoneInfo(config().get("zona_horaria", "America/Santiago"))


def canales():
    """{id: canal} con los canales de canales/*.json (se ignoran los que empiezan con _)."""
    out = {}
    for f in sorted((RAIZ_KIT / "canales").glob("*.json")):
        if f.name.startswith("_"):
            continue
        c = json.loads(f.read_text(encoding="utf-8"))
        c.setdefault("id", f.stem)
        c["handle"] = (c.get("handle") or "").lstrip("@").lower()
        out[c["id"]] = c
    return out


def canal(id_o_carpeta):
    for c in canales().values():
        if id_o_carpeta in (c["id"], c.get("carpeta"), c["handle"]):
            return c
    raise SystemExit(f"No encuentro el canal '{id_o_carpeta}' en canales/*.json")


def mapa():
    """carpeta → handle (lo usan métricas, fichas y la subida)."""
    return {c["carpeta"]: c["handle"] for c in canales().values() if c.get("carpeta") and c.get("handle")}
