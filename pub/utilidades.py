import json
def extraer_json(texto):
    dec = json.JSONDecoder(); i = texto.find("[")
    while i != -1:
        try:
            obj, _ = dec.raw_decode(texto, i)
            if isinstance(obj, list): return obj
        except json.JSONDecodeError: pass
        i = texto.find("[", i + 1)
    raise ValueError("x")
