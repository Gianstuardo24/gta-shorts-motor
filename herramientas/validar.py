#!/usr/bin/env python3
"""
validar.py · Validador de claves de tiempo · E1, MODO AVISO (informa; nunca detiene ni cambia nada).

  python3 validar.py datos.json [más.json …] [--salida informe.json] [--detalle] [--estricto]
  python3 validar.py --cobertura [--motor escena.html] [--registrar]

Qué revisa en cada escena (con el mapa de campos de claves.py):
  ERROR  clave de texto que no existe en T (el motor usaría el inicio de la escena, en silencio) · desplazamiento
         mal escrito ("s_3+0..5") · número escrito como texto ("1.5") · tipo inválido · inicio de escena que no
         se puede resolver · en tipos antiguos, un campo que el motor lee como T[...] directo y no existe
  AVISO  algo que empieza cuando la escena ya no se ve (nunca aparece) · un fin antes de su inicio ·
         inicios de escena desordenados
  INFO   tiempos antes del inicio de su escena (el recurso "ya estaba": queda completo desde el primer cuadro)
Modo aviso: sale siempre con 0. --estricto (para etapas futuras, no se usa en la E1): sale con 1 si hay ERROR.
--cobertura: compara los usos de claves del motor con la foto guardada en campos_motor.json (avisa si el motor
empieza a usar claves en un lugar nuevo que el mapa todavía no conoce).
Solo lee. Nunca modifica escenas, configuraciones, renders ni el motor.
"""
import argparse, collections, hashlib, json, pathlib, re, sys

AQUI = pathlib.Path(__file__).parent
sys.path.insert(0, str(AQUI))
import claves as C

MOTOR = pathlib.Path("/home/claude/escena/escena.html")
FOTO = AQUI / "campos_motor.json"
MARCAS = {"error": "✗ ERROR", "aviso": "⚠ AVISO", "info": "· info "}


def inicio_escena(e, T):
    d = e.get("desde")
    if d == "0":
        return 0.0, None
    if isinstance(d, str) and d in T:
        return float(T[d]), None
    return None, (f'escenas[].desde = {json.dumps(d, ensure_ascii=False)}: el motor solo acepta "0" o un marcador de T '
                  f'exacto (sin ±n ni números); con esto la escena no se dibuja bien')


def cuadros_mezclados(e, a, T, t0=0.0, fps=30.0):
    """Cortes de cámara (zoom con dur ≤ 0,02) y de zona (pan con corte) del motor, cuadro a cuadro.
    El paneo con corte cambia de golpe (t ≥ clave); el zoom de corte pasa de un encuadre al otro en dur segundos.
    Un cuadro donde el paneo ya cambió y el zoom todavía no (o el zoom está a mitad de camino) mira un lugar que
    no corresponde: es el cuadro intermedio que se ve como un fondo ajeno (plano 10 v2 y los 7 videos del 25-nov)."""
    pans = [C.tk(p.get("k"), a, T) for p in e.get("pan") or [] if p.get("corte")]
    out = []
    for z in e.get("zoom") or []:
        dz = z.get("dur") or 0.6
        if dz > 0.02:
            continue
        tz = C.tk(z.get("k"), a, T)
        if tz != tz:
            continue
        tp = min(pans, key=lambda x: abs(x - tz)) if pans else None
        if tp is not None and abs(tp - tz) > 0.2:
            tp = None
        ini, fin = (min(tp, tz), max(tp, tz + dz)) if tp is not None else (tz, tz + dz)
        n = max(0, int(-(-(ini - t0) * fps // 1)))
        malos = []
        while t0 + n / fps < fin - 1e-9:
            t = t0 + n / fps
            q = (1.0 if t >= tz else 0.0) if z.get("corte") else min(1.0, max(0.0, (t - tz) / dz))   # zoom con corte: de golpe
            paneo = tp is None or t >= tp
            if (0 < q < 1) or (paneo != (q >= 1)):
                malos.append(n)
            n += 1
        if malos:
            out.append({"zoom_k": z.get("k"), "zoom": round(tz, 3), "paneo": None if tp is None else round(tp, 3),
                        "cuadros": malos})
    return out


def validar_datos(d, nombre="", t0=0.0):
    T = d.get("T") or {}
    esc = d.get("escenas") or []
    dur = T.get("fin")
    hall, n = [], 0
    def h(nivel, ruta, valor, motivo, t=None):
        hall.append({"nivel": nivel, "ruta": ruta, "valor": valor, "motivo": motivo,
                     "tiempo": None if t is None or t != t else round(t, 3)})
    a_s = []
    for i, e in enumerate(esc):
        a, err = inicio_escena(e, T)
        if err:
            h("error", f"escenas[{i}].desde", e.get("desde"), err)
        a_s.append(a)
    # El tipo "cierre" escribe T.s_fin = su inicio (motor, línea ≈453). Con un inicio inválido, s_fin queda sin valor
    # para todo el video; con un inicio distinto de s_fin, s_fin cambia de valor para todos los que lo usan.
    for i, e in enumerate(esc):
        if e.get("tipo") != "cierre":
            continue
        usos = [(f"escenas[{j}].{r}", v) for j, ej in enumerate(esc) for r, v, _, _ in C.claves_de_escena(ej)
                if isinstance(v, str) and (v == "s_fin" or v.startswith(("s_fin+", "s_fin-")))]
        if a_s[i] is None:
            for r, v in usos:
                h("error", r, v, "el inicio del cierre no se resuelve y el motor escribe T.s_fin = ese inicio: esta clave "
                                 "queda sin resolver (efecto en cascada de escenas[].desde)")
        elif "s_fin" in T and abs(a_s[i] - T["s_fin"]) > 1e-6 and usos:
            h("aviso", f"escenas[{i}].desde", e.get("desde"), f"el cierre empieza en {a_s[i]:.2f} s y el motor reescribe "
              f"T.s_fin ({T['s_fin']:.2f} s) con ese valor: cambian {len(usos)} claves que usan s_fin")
    prev = None
    for i, a in enumerate(a_s):
        if a is not None and prev is not None and a <= prev:
            h("aviso", f"escenas[{i}].desde", esc[i].get("desde"), f"empieza en {a:.2f} s, no después de la escena anterior ({prev:.2f} s)")
        prev = a if a is not None else prev
    for i, e in enumerate(esc):
        a = a_s[i]
        if a is None:
            continue
        sig = next((x for x in a_s[i + 1:] if x is not None), None)
        b = sig if sig is not None else (dur + 5 if dur is not None else float("inf"))
        visible_hasta = min(b + 0.7, dur) if dur is not None else b + 0.7
        por_objeto = collections.defaultdict(dict)
        for ruta, v, rol, modo in C.claves_de_escena(e):
            n += 1; r = f"escenas[{i}].{ruta}"
            if modo == "directo":
                if isinstance(v, str) and v not in T:
                    h("error", r, v, f'este tipo de escena lee T["{v}"] directo y no existe: usa su tiempo por defecto')
                elif v is not None and not isinstance(v, str):
                    h("error", r, v, "este tipo de escena solo acepta marcadores exactos de T (no números ni ±n)")
                continue
            tipo, nivel, motivo = C.clasificar(v, T)
            t = C.tk(v, a, T)
            if nivel:
                h(nivel, r, v, motivo + ("" if nivel == "info" else f" (resuelve a {t:.2f} s)" if t == t else ""), t)
                if nivel == "error":
                    continue
            if v is None or t != t:
                continue
            if rol in ("inicio", "punto") and t > visible_hasta + 1e-6:
                h("aviso", r, v, f"ocurre a los {t:.2f} s, cuando la escena ya no se ve (hasta {visible_hasta:.2f} s): nunca aparece", t)
            elif t < a - 1e-6:
                h("info", r, v, f"cae a los {t:.2f} s, antes del inicio de su escena ({a:.2f} s): queda completo desde el primer cuadro", t)
            m = re.match(r"^(.*?)(\.(k|fin|desde|hasta|de|a)|\[(0|1)\])$", ruta)
            if m:
                por_objeto[m.group(1)][m.group(3) or m.group(4)] = (t, r, v)
        if e.get("tipo") == "pelicula":
            for c in cuadros_mezclados(e, a, T, t0):
                ts = ", ".join(f"{t0 + n / 30:.3f}" for n in c["cuadros"])
                h("aviso", f"escenas[{i}].zoom (corte {c['zoom']:.3f} s)", c["zoom_k"],
                  (f"corte de zona a los {c['paneo']:.3f} s y de cámara a los {c['zoom']:.3f} s: " if c["paneo"] is not None
                   else f"corte de cámara a los {c['zoom']:.3f} s: ")
                  + f"{len(c['cuadros'])} cuadro(s) con encuadre intermedio (cuadro {', '.join(map(str, c['cuadros']))} · {ts} s)", c["zoom"])
        for obj, cs in por_objeto.items():
            for ini, fin in (("k", "fin"), ("desde", "hasta"), ("de", "a"), ("0", "1")):
                if ini in cs and fin in cs and cs[fin][0] < cs[ini][0] - 1e-6:
                    h("aviso", cs[fin][1], cs[fin][2], f"termina ({cs[fin][0]:.2f} s) antes de empezar ({cs[ini][0]:.2f} s)", cs[fin][0])
    cuenta = collections.Counter(x["nivel"] for x in hall)
    return {"archivo": nombre, "claves_revisadas": n, "errores": cuenta["error"], "avisos": cuenta["aviso"],
            "info": cuenta["info"], "hallazgos": hall}


# ------------------------------------------------------------------ cobertura del mapa contra el código del motor
CTX = [(re.compile(r"^const (TIPOS|UTILERIA|NUEVOS|LOOKS|SETS)\s*=\s*\{"), "dict"),
       (re.compile(r"^\s{0,2}([A-Za-z_\$][\w\$]*)\s*\([^)]*\)\s*\{"), "entrada"),
       (re.compile(r"^function\s+([A-Za-z_\$][\w\$]*)\s*\("), "funcion"),
       (re.compile(r"^(UTILERIA|TIPOS|NUEVOS)\.([A-Za-z_\$][\w\$]*)\s*="), "asig")]


def usos_del_motor(src):
    dic, cur, usos = None, "(global)", set()
    for l in src.split("\n"):
        for rx, kind in CTX:
            m = rx.match(l)
            if m:
                if kind == "dict": dic = cur = m.group(1)
                elif kind == "funcion": dic, cur = None, m.group(1) + "()"
                elif kind == "asig": cur = f"{m.group(1)}.{m.group(2)}"
                elif dic: cur = f"{dic}.{m.group(1)}"
                break
        for m in re.finditer(r"\btk\(\s*([^,()]+(?:\([^()]*\))?[^,()]*)\s*,", l):
            usos.add(f"{cur} · tk({m.group(1).strip()})")
        for m in re.finditer(r"\bT\[([^\]]+)\]", l):
            usos.add(f"{cur} · T[{m.group(1).strip()}]")
    return sorted(usos)


def cobertura(motor, registrar):
    src = motor.read_text(encoding="utf-8"); usos = usos_del_motor(src)
    sha = hashlib.sha256(src.encode()).hexdigest()
    if registrar:
        if FOTO.exists():
            sys.exit(f"{FOTO.name} ya existe: es la referencia del mapa")
        FOTO.write_text(json.dumps({"motor_sha256": sha, "usos": usos}, ensure_ascii=False, indent=1))
        print(f"foto guardada: {len(usos)} usos de claves en el motor {sha[:12]}"); return 0
    foto = json.loads(FOTO.read_text()); antes = set(foto["usos"]); ahora = set(usos)
    nuevos, quitados = sorted(ahora - antes), sorted(antes - ahora)
    print(f"motor {sha[:12]} (foto: {foto['motor_sha256'][:12]}) · {len(ahora)} usos de claves · "
          f"{len(nuevos)} nuevos · {len(quitados)} que ya no están")
    for u in nuevos:
        print("  ⚠ AVISO  nuevo uso de claves en el motor (revisar el mapa de claves.py):", u)
    for u in quitados:
        print("  · info   ya no está en el motor:", u)
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("datos", nargs="*"); ap.add_argument("--salida"); ap.add_argument("--detalle", action="store_true")
    ap.add_argument("--estricto", action="store_true"); ap.add_argument("--cobertura", action="store_true")
    ap.add_argument("--registrar", action="store_true"); ap.add_argument("--motor", default=str(MOTOR))
    ap.add_argument("--t0", type=float, default=0.0, help="inicio del render (producción 0; planos de prueba 0.15)")
    a = ap.parse_args()
    if a.cobertura:
        sys.exit(cobertura(pathlib.Path(a.motor), a.registrar))
    informes, errores = [], 0
    for f in a.datos:
        r = validar_datos(json.loads(pathlib.Path(f).read_text()), f, a.t0); informes.append(r); errores += r["errores"]
        print(f"{f}: {r['claves_revisadas']} claves · {r['errores']} errores · {r['avisos']} avisos · {r['info']} info")
        for x in r["hallazgos"]:
            if x["nivel"] != "info" or a.detalle:
                print(f"  {MARCAS[x['nivel']]}  {x['ruta']} = {json.dumps(x['valor'], ensure_ascii=False)} · {x['motivo']}")
    if a.salida:
        pathlib.Path(a.salida).write_text(json.dumps(informes, ensure_ascii=False, indent=1))
    sys.exit(1 if (a.estricto and errores) else 0)


if __name__ == "__main__":
    main()
