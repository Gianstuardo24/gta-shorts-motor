#!/usr/bin/env python3
"""
E1 · Evaluación del detector de cuadros aislados (herramientas/saltos.py) sobre las referencias congeladas.
Corre el detector con y sin los datos de render, lo compara con los cuadros intermedios que predice el validador
(validar.cuadros_mezclados) y guarda tiras de imagen de cada isla. Solo lee videos y datos.
Uso: python3 evaluar_saltos.py [--salida informe.json] [--tiras carpeta]
"""
import json, pathlib, sys
sys.path.insert(0, "/home/claude/herramientas")
import saltos as S, validar as V

C = pathlib.Path(__file__).parent / "corpus"; R = pathlib.Path(__file__).parent / "referencias_video"
arg = lambda k: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else None


def main():
    tiras = arg("--tiras"); filas = {}
    casos = [(s, R / f"{s}_entregado.mp4", C / f"produccion/{s}/datos_render.json", 0.0) for s in ("wc1", "wd2", "wge2", "wgs1", "wk2", "wm2", "wr1")]
    casos += [(f"plano{n}", R / f"plano{n}_aprobado.mp4", C / f"planos/{n}/datos.json", 0.15) for n in ("04", "05", "06", "10")]
    casos += [("plano10_v2 (caso real)", pathlib.Path("/home/claude/prueba27/p10/plano10_v2.mp4"), None, 0.15)]
    for nombre, video, datos_p, t0 in casos:
        datos = json.loads(datos_p.read_text()) if datos_p else None
        con = S.analizar(video, datos, t0, tiras) if datos else None
        sin = S.analizar(video, None, t0, None)
        pred = sorted({n for e in (datos or {}).get("escenas", []) if e.get("tipo") == "pelicula"
                       for c in V.cuadros_mezclados(e, 0.0, datos["T"], t0) for n in c["cuadros"]}) if datos else []
        marc_con = sorted({k for x in (con or {"islas": []})["islas"] for k in range(x["desde"], x["hasta"] + 1)})
        marc_sin = sorted({k for x in sin["islas"] for k in range(x["desde"], x["hasta"] + 1)})
        fila = {"video": str(video), "cuadros": sin["cuadros"],
                "islas_con_datos": None if con is None else con["islas"], "islas_sin_datos": sin["islas"],
                "destellos_sin_datos": sin["destellos_sin_confirmar"],
                "previstos_por_el_validador": pred,
                "previstos_no_marcados": [n for n in pred if n not in marc_con] if datos else None,
                "marcados_no_previstos": [n for n in marc_con if n not in pred] if datos else None}
        filas[nombre] = fila
        print(f"{nombre:24} {sin['cuadros']:5} cuadros · islas con datos {('-' if con is None else len(con['islas'])):>3} · "
              f"sin datos {len(sin['islas']):3} (+{len(sin['destellos_sin_confirmar'])} destellos) · "
              f"previstos {len(pred):3} · previstos no visibles {('-' if not datos else len(con['previstos_no_visibles'])):>3} · "
              f"marcados no previstos {('-' if not datos else fila['marcados_no_previstos'])}")
    if arg("--salida"):
        pathlib.Path(arg("--salida")).write_text(json.dumps(filas, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
