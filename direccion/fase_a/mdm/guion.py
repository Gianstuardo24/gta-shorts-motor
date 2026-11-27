"""MDM 18h · Nike's DIRTIEST Deal? · guion aprobado por Tao el 25-nov (GUIONES_FINALES_25nov.md), sin cambios.
Escribe voz/mdm_src.json para la voz. F es el texto en pantalla; V es el mismo texto con las cifras en letras (convención del 25-nov)."""
import json, pathlib
F = ["Some call it Nike's dirtiest deal. The price was so low it sounds like a joke. But that's only half the story.",
     "In 1971, Phil Knight needed a logo for his new shoe brand.",
     "He asked a design student, Carolyn Davidson.",
     "She charged 2 dollars an hour. After about 17 hours of work, the bill was 35 dollars.",
     "Knight wasn't even sure about it. He said he didn't love it, but it would grow on him.",
     "That logo became the swoosh, one of the most famous logos on Earth.",
     "Now the other half of the story, the one that everyone misses.",
     "In 1983, Nike surprised her with a gold swoosh ring with a diamond.",
     "And 500 shares of Nike stock.",
     "So it wasn't a dirty deal. She set her price, and Nike paid her back years later.",
     "Price the work, not the hours. A small job can become the face of a giant.",
     "Tell me what you would have charged. Follow for the next million dollar mistake."]
REEMPLAZOS = [("In 1971,", "In nineteen seventy-one,"), ("2 dollars", "two dollars"), ("17 hours", "seventeen hours"),
              ("35 dollars", "thirty-five dollars"), ("In 1983,", "In nineteen eighty-three,"), ("500 shares", "five hundred shares")]
def voz(f):
    for a, b in REEMPLAZOS: f = f.replace(a, b)
    return f
V = [voz(f) for f in F]
G2 = 6                                   # "Now the other half of the story…" (línea 7)
if __name__ == "__main__":
    g = {"titulo": "Nike's DIRTIEST Deal? 👟😳", "lote": "MDM18_FASEA", "marca": "MILLION DOLLAR MISTAKE", "tema": "mdm", "cuerpo": "pro",
         "pausa_larga_antes": [1, G2, G2 + 1, len(F) - 1], "frases": F, "frases_voz": V}
    p = pathlib.Path(__file__).parent / "voz" / "mdm_src.json"
    p.write_text(json.dumps(g, ensure_ascii=False))
    print("ok", p, len(F), "frases")
