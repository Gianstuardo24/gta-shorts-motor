#!/usr/bin/env python3
"""
E1 · Pruebas negativas del validador de claves: se pone a propósito UN error en una copia en memoria de los datos
congelados y se comprueba que el validador lo encuentra (y que no aparece nada más). Nunca escribe en el corpus.
Uso: python3 mutaciones_claves.py [--salida informe.json]      → sale con 1 si alguna mutación no se detecta.
"""
import copy, json, pathlib, sys
sys.path.insert(0, "/home/claude/herramientas")
import validar as V

C = pathlib.Path(__file__).parent / "corpus"
base = {
    "wd2": json.loads((C / "produccion/wd2/datos_render.json").read_text()),
    "wm2": json.loads((C / "produccion/wm2/datos_render.json").read_text()),
    "p05": json.loads((C / "planos/05/datos.json").read_text()),
    "p06": json.loads((C / "planos/06/datos.json").read_text()),
    "p10": json.loads((C / "planos/10/datos.json").read_text()),
}


def esc(d):
    return d["escenas"][0]


def m_tipeo_prop(d): esc(d)["props"][0]["k"] = "s_l"                      # s_1 con una ele
def m_tipeo_actor(d): esc(d)["actores"][0]["keys"][0]["k"] = "s_11"
def m_desplazamiento(d): esc(d)["actores"][1]["keys"][1]["k"] = "s_2+0..5"
def m_numero_texto(d): esc(d)["zoom"][3]["k"] = "1.5"
def m_booleano(d): esc(d)["props"][0]["fin"] = True
def m_inicio_escena(d): d["escenas"][1]["desde"] = "s_fln"
def m_inicio_con_desplazamiento(d): d["escenas"][1]["desde"] = "s_fin+0.2"
def m_nunca_aparece(d): esc(d)["emojis"][0]["k"] = "fin+3"
def m_fin_antes(d): esc(d)["props"][0]["fin"] = "red0"                     # termina antes de su inicio (s_1)
def m_hud_nuevo(d): esc(d)["telefono"] = {"k": "s_1", "fin": "s_2", "items": [{"k": "nadie"}]}
def m_escenas_desordenadas(d): d["escenas"].append({"tipo": "cierre", "desde": "s_1"})   # empieza antes que la anterior
def m_tipo_antiguo(d): d["escenas"].append({"tipo": "contador", "desde": "s_cta", "k": "s_cta", "k2": "s_cta2"})
def m_p05_despl(d): [p for p in esc(d)["props"] if p["tipo"] == "p27_visor"][0]["curMov"][1][0] = "p27_unusd"
def m_p05_cursor(d): [p for p in esc(d)["props"] if p["tipo"] == "p27_grilla"][0]["cursor"][0] = "p27_at-x"
def m_p06_despK(d): [p for p in esc(d)["props"] if p["tipo"] == "p27_visor"][0]["despK"][5][0] = "Leonida"
def m_p10_zona(d): esc(d)["zonas"][0]["k"] = "noexiste"
def m_corte_temprano(d): d["escenas"][1]["desde"] = "red0"                  # la escena siguiente empieza a los 0,64 s

CASOS = [  # (nombre, datos, mutación, nivel esperado, ruta esperada (contiene))
    ("clave mal escrita en utilería", "wd2", m_tipeo_prop, "error", "props[0].k"),
    ("clave inexistente en una pose de actor", "wd2", m_tipeo_actor, "error", "actores[0].keys[0].k"),
    ("desplazamiento mal escrito", "wd2", m_desplazamiento, "error", "actores[1].keys[1].k"),
    ("número escrito como texto", "wd2", m_numero_texto, "error", "zoom[3].k"),
    ("valor booleano", "wd2", m_booleano, "error", "props[0].fin"),
    ("inicio de escena inexistente", "wd2", m_inicio_escena, "error", "escenas[1].desde"),
    ("inicio de escena con ±n (el motor no lo acepta)", "wd2", m_inicio_con_desplazamiento, "error", "escenas[1].desde"),
    ("algo que empieza después del final", "wd2", m_nunca_aparece, "aviso", "emojis[0].k"),
    ("fin antes del inicio", "wd2", m_fin_antes, "aviso", "props[0].fin"),
    ("campo de un objeto nuevo (teléfono)", "wm2", m_hud_nuevo, "error", "telefono.items[0].k"),
    ("escenas desordenadas", "wd2", m_escenas_desordenadas, "aviso", "escenas[2].desde"),
    ("tipo de escena antiguo (T directo)", "wd2", m_tipo_antiguo, "error", "escenas[2].k2"),
    ("p27: recorrido del cursor", "p05", m_p05_despl, "error", "curMov[1][0]"),
    ("p27: desplazamiento mal escrito en el cursor", "p05", m_p05_cursor, "error", "cursor[0]"),
    ("p27: claves densas del desplazamiento", "p06", m_p06_despK, "error", "despK[5][0]"),
    ("p27: zona del plano 10", "p10", m_p10_zona, "error", "zonas[0].k"),
    ("escena cortada por la siguiente (efecto en cascada)", "wd2", m_corte_temprano, "aviso", "escenas[0].emojis[3].k"),
]


def main():
    filas, fallas = [], 0
    for nombre, cual, mut, nivel, ruta in CASOS:
        d = copy.deepcopy(base[cual]); mut(d)
        r = V.validar_datos(d, cual)
        dados = [x for x in r["hallazgos"] if x["nivel"] == nivel and ruta in x["ruta"]]
        extra = [x for x in r["hallazgos"] if x["nivel"] in ("error", "aviso") and x not in dados]
        ok = bool(dados)
        fallas += not ok
        filas.append({"caso": nombre, "datos": cual, "esperado": f"{nivel} en {ruta}", "detectado": ok,
                      "otros_hallazgos": [f"{x['nivel']} {x['ruta']}" for x in extra]})
        print(f"{'✔' if ok else '✗'} {nombre:48} → {nivel:5} {ruta:24}" + (f" · además: {len(extra)}" if extra else ""))
        for x in extra:
            print(f"      además: {x['nivel']} {x['ruta']} · {x['motivo'][:90]}")
    print(f"{len(CASOS) - fallas}/{len(CASOS)} mutaciones detectadas")
    if "--salida" in sys.argv:
        pathlib.Path(sys.argv[sys.argv.index("--salida") + 1]).write_text(json.dumps(filas, ensure_ascii=False, indent=1))
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()
