#!/usr/bin/env python3
"""
inspeccion_fondos.py · Inspección de fondos, cobertura y continuidad · 27i, bloque 2 · SOLO LEE.

  python3 inspeccion_fondos.py DATOS.json [--motor escena.html] [--fps 30] [--t0 0] [--cuadros N]
                               [--video V.mp4] [--salida informe.json] [--hoja hoja.png] [--desde N] [--hasta M]

Dibuja cada cuadro con el motor dos veces, con colores testigo distintos debajo de todo y en lugar del fondo base de
CTA. La diferencia entre las dos pasadas dice, píxel a píxel, si se ve un hueco (nada pintado) o el fondo base. Además
registra qué plano está en el centro del encuadre y su escala. Todo se mide dentro de la página, en una copia reducida
a 270×480 (promedio exacto de bloques de 4×4: una costura de 1 píxel se sigue viendo).

Dos categorías (Tao, 26-nov 16:23):
  ERROR TÉCNICO (bloquea la entrega; sale con 1)
    hueco ················· píxeles sin pintar (en el video quedan negros)
    base_fuera_de_lugar ··· el fondo base de CTA se ve fuera del cierre y fuera de un plano que lo pide
    base_no_permitida ····· un plano pide el fondo base y el perfil del canal no lo permite
    fuera_de_plano ········ el plano en el centro del encuadre no es el que toca según los datos (fuera de un paneo),
                            o el escenario dibujado no es el entorno que declara el plano
    desfase_de_corte ······ el corte de plano y el de cámara no caen en el mismo cuadro
    primer_cuadro ········· el cuadro 0 no muestra su primer plano completo
    validador ············· error de los datos según el validador: clave inexistente o mal escrita, campo de plano
                            inválido, fundido sin plano anterior, dos cortes de cámara en el mismo instante…
    cuadro_aislado ········ isla de 1 o 2 cuadros en el video (detector de la E1; solo con --video)
  OBSERVACIÓN CREATIVA (solo informa; nunca bloquea)
    oscuro, negro (declarado o no), quietud, paneo, fundido, base_pedida, aviso del validador
Sin perfil de fondos (videos anteriores al 27i), el fondo base se pinta en todos los cuadros: lo que mide es dónde se ve.
Nunca modifica escenas, configuraciones, renders, videos ni el motor.
"""
import argparse, base64, hashlib, json, pathlib, sys, time

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import claves as C  # noqa: E402
import validar as V  # noqa: E402

MOTOR = AQUI.parent / "escena" / "escena.html"
SEMILLA = ("window.__semilla=v=>{let s=v>>>0;Math.random=()=>{s=(Math.imul(s,1664525)+1013904223)>>>0;"
           "return s/4294967296}};true;")
UMBRAL_BASE = 0.05        # % de la pantalla con fondo base visible para contarlo (evita bordes suavizados)
MARGEN_CIERRE = 0.25      # el cierre empieza a verse 0,25 s antes de s_fin (la película se desliza)
OSCURO, NEGRO, QUIETO = 0.08, 97.0, 0.5   # luminancia media; % de píxeles casi negros; cambio medio entre cuadros (0–255)

MEDIR_JS = """(()=>{
const W=1080,H=1920,mk=(w,h)=>{const c=document.createElement('canvas');c.width=w;c.height=h;return [c,c.getContext('2d')]};
const [C2,X2]=mk(W,H),[C4,X4]=mk(540,960),[C5,X5]=mk(270,480),Cv=document.getElementById('c');
const cr=X.clearRect.bind(X);window.__S=null;
X.clearRect=function(x,y,w,h){cr(x,y,w,h);if(window.__S){const f=this.fillStyle;this.fillStyle=window.__S.c;this.fillRect(x,y,w,h);this.fillStyle=f}};
const pb=pintarBase;window.__nb=0;
pintarBase=function(){if(!window.__S)return pb.apply(this,arguments);window.__nb++;X.save();X.setTransform(1,0,0,1,0,0);X.fillStyle=window.__S.b;X.fillRect(0,0,W,H);X.restore()};
const zd=zonaDeco;window.__Zc=[];window.__esc=null;
zonaDeco=function(z,t,q){if(window.__S&&z&&q>0){const m=X.getTransform(),p=m.inverse().transformPoint(new DOMPoint(W/2,H/2));
  if(window.__esc===null)window.__esc=+Math.hypot(m.a,m.b).toFixed(4);if(z.x0<=p.x&&p.x<z.x1)window.__Zc.push(z.x0)}return zd.apply(this,arguments)};
const chico=()=>{X4.drawImage(C2,0,0,540,960);X5.drawImage(C4,0,0,270,480);return X5.getImageData(0,0,270,480).data};
let prev=null;
window.__inspeccionar=function(t,n,continuo){const o={n};
  window.__S={c:'#ff00ff',b:'#00ffff'};window.__nb=0;window.__Zc=[];window.__esc=null;window.__semilla(12345+n);render(t);
  o.bp=window.__nb;o.zc=[...new Set(window.__Zc)];o.esc=window.__esc;
  X2.globalCompositeOperation='copy';X2.drawImage(Cv,0,0);const img=chico();
  window.__S={c:'#00ff00',b:'#ffff00'};window.__semilla(12345+n);render(t);window.__S=null;
  X2.globalCompositeOperation='difference';X2.drawImage(Cv,0,0);const dif=chico();
  let hu=0,ba=0,b2=0,hy=[1e9,-1],by=[1e9,-1],lum=0,neg=0,mov=0;const N=dif.length/4;
  for(let i=0,p=0;i<dif.length;i+=4,p++){const g=dif[i+1],b=dif[i+2],y=(p/270)|0;
    if(g>3){hu++;if(y<hy[0])hy[0]=y;if(y>hy[1])hy[1]=y}else if(b>3){ba++;if(y<by[0])by[0]=y;if(y>by[1])by[1]=y}
    const L=0.2126*img[i]+0.7152*img[i+1]+0.0722*img[i+2];lum+=L;if(L<6)neg++;
    if(prev&&continuo)mov+=Math.abs(img[i]-prev[i])+Math.abs(img[i+1]-prev[i+1])+Math.abs(img[i+2]-prev[i+2])}
  o.hueco=+(100*hu/N).toFixed(3);o.base=+(100*ba/N).toFixed(3);o.yh=hu?[hy[0]*4,hy[1]*4+3]:null;o.yb=ba?[by[0]*4,by[1]*4+3]:null;
  o.lum=+(lum/N/255).toFixed(3);o.negro=+(100*neg/N).toFixed(1);o.mov=(prev&&continuo)?+(mov/N/3).toFixed(2):null;prev=new Uint8ClampedArray(img);
  const e=(DATOS.escenas||[]).find(s=>s.tipo==='pelicula');
  if(e&&typeof camXde==='function'){const a=e.desde==='0'?0:T[e.desde];const z=zonaEn(e,camXde(e,t,a));o.ze=z?z.x0:null}else o.ze=null;
  return o};
window.__foto=function(t,n){window.__S=null;window.__semilla(12345+n);render(t);return Cv.toDataURL('image/jpeg',0.85)};
return true})()"""


def tramos(ns):
    """Agrupa cuadros consecutivos: [(desde, hasta), …]."""
    out = []
    for n in sorted(ns):
        if out and n == out[-1][1] + 1:
            out[-1][1] = n
        else:
            out.append([n, n])
    return out


def ventanas_declaradas(d, fps, t0):
    """Ventanas (en cuadros) de las transiciones declaradas en los planos: paneo, fundido y negro."""
    T = d.get("T") or {}
    e = next((s for s in d.get("escenas") or [] if s.get("tipo") == "pelicula"), None)
    out = {"paneo": [], "fundido": [], "negro": []}
    if not e:
        return out
    a, _ = V.inicio_escena(e, T)
    a = a or 0.0
    a_cuadro = lambda t: int(round((t - t0) * fps))
    LEN = e.get("lento") or 1.6
    for p in e.get("pan") or []:
        if p.get("corte"):
            continue
        D = (p.get("dur") or 1.0) * LEN; k0 = C.tk(p.get("k"), a, T) - D * .3
        if k0 == k0:
            out["paneo"].append((a_cuadro(k0) - 1, a_cuadro(k0 + D) + 1, p.get("x")))
    for z in e.get("zonas") or []:
        if z.get("k") is None:
            continue
        k = C.tk(z.get("k"), a, T)
        if k != k:
            continue
        if z.get("transicion") == "fundido":
            out["fundido"].append((a_cuadro(k), a_cuadro(k + (z.get("dur_fundido") or .5)), z.get("x0")))
        if z.get("transicion") == "negro":
            o = z.get("negro") or {}; b, n, u = o.get("baja", .2), o.get("negro", .08), o.get("sube", .2)
            out["negro"].append((a_cuadro(k - n / 2 - b), a_cuadro(k + n / 2 + u), z.get("x0")))
    return out


def en(ventanas, n):
    return any(a <= n <= b for a, b, _ in ventanas)


def compatible(z):
    """¿El escenario que se dibuja es el entorno que declara el plano?"""
    ent, st = z.get("entorno"), z.get("set")
    return ent == st or (ent == "vitrina" and st == "vitrinaV") or (ent == "base" and st == "baseCanal")


def medir(motor, datos_txt, ns, t0, fps, avance=True):
    from playwright.sync_api import sync_playwright
    res = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.add_init_script(f"window.DATOS={datos_txt};")
        pg.goto(pathlib.Path(motor).resolve().as_uri()); pg.wait_for_function("window.LISTO===true", timeout=30000)
        pg.evaluate(SEMILLA); pg.evaluate(MEDIR_JS)
        t_ini = time.time(); ant = None
        for j, n in enumerate(ns):
            t = round(t0 + n / fps, 6)
            res.append(pg.evaluate(f"window.__inspeccionar({t},{n},{'true' if ant is not None and n == ant + 1 else 'false'})"))
            ant = n
            if avance and j and j % 300 == 0:
                print(f"    {j}/{len(ns)} cuadros · {time.time() - t_ini:.0f} s", flush=True)
        b.close()
    return res


def fotos(motor, datos_txt, ns, t0, fps):
    from playwright.sync_api import sync_playwright
    out = {}
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.add_init_script(f"window.DATOS={datos_txt};")
        pg.goto(pathlib.Path(motor).resolve().as_uri()); pg.wait_for_function("window.LISTO===true", timeout=30000)
        pg.evaluate(SEMILLA); pg.evaluate(MEDIR_JS)
        for n in ns:
            url = pg.evaluate(f"window.__foto({round(t0 + n / fps, 6)},{n})")
            out[n] = base64.b64decode(url.split(",", 1)[1])
        b.close()
    return out


def clasificar(d, cs, fps, t0, perfil):
    """Errores técnicos y observaciones creativas a partir de la medición cuadro a cuadro."""
    T = d.get("T") or {}
    e = next((s for s in d.get("escenas") or [] if s.get("tipo") == "pelicula"), None)
    zonas = {z.get("x0"): z for z in (e or {}).get("zonas") or []}
    s_fin = T.get("s_fin")
    n_cierre = int(-(-((s_fin - MARGEN_CIERRE - t0) * fps) // 1)) if s_fin is not None else 10 ** 9
    ven = ventanas_declaradas(d, fps, t0)
    permite_base = bool(perfil) and perfil.get("escenas", "solo_si_la_piden") == "solo_si_la_piden"
    err = {k: set() for k in ("hueco", "base_fuera_de_lugar", "base_no_permitida", "fuera_de_plano", "desfase_de_corte", "primer_cuadro")}
    obs = {k: set() for k in ("base_pedida", "oscuro", "negro_declarado", "negro_no_declarado", "quietud", "paneo", "fundido")}
    M = {c["n"]: c for c in cs}
    for c in cs:                 # si en el cuadro no se pintó el fondo base, lo que parece base es hueco (mezclas con filtros)
        if not c.get("bp") and c["base"] > 0:
            c["hueco"] = round(c["hueco"] + c["base"], 3); c["base"] = 0.0
    for c in cs:
        n = c["n"]
        if c["hueco"] > 0:
            err["hueco"].add(n)
        plano = zonas.get(c.get("ze"))
        pide = bool(plano) and (plano.get("entorno") == "base" or plano.get("set") == "baseCanal")
        if c["base"] > UMBRAL_BASE and n < n_cierre:
            if pide and plano.get("entorno") == "base":
                (obs["base_pedida"] if permite_base else err["base_no_permitida"]).add(n)
            else:
                err["base_fuera_de_lugar"].add(n)
        if n < n_cierre and plano and plano.get("entorno") and not compatible(plano):
            err["fuera_de_plano"].add(n)          # el escenario dibujado no es el entorno que declara el plano
        if n < n_cierre and c.get("ze") is not None:
            if c["ze"] not in c["zc"]:
                if en(ven["paneo"], n):
                    obs["paneo"].add(n)
                elif en(ven["fundido"], n) and c["zc"]:
                    obs["fundido"].add(n)
                else:
                    err["fuera_de_plano"].add(n)
            elif en(ven["fundido"], n):
                obs["fundido"].add(n)
        if c["negro"] >= NEGRO:
            (obs["negro_declarado"] if en(ven["negro"], n) else obs["negro_no_declarado"]).add(n)
        elif c["lum"] < OSCURO:
            obs["oscuro"].add(n)
        if c.get("mov") is not None and c["mov"] < QUIETO:
            obs["quietud"].add(n)
    # desfase: el plano en el centro cambia en un cuadro y la escala de la cámara salta 1–3 cuadros antes o después
    ns = sorted(M)
    def plano_de(c):
        return c["ze"] if c.get("ze") in c["zc"] else (c["zc"][0] if c["zc"] else None)
    saltos_plano = [n for a, n in zip(ns, ns[1:]) if n == a + 1 and n < n_cierre and plano_de(M[n]) != plano_de(M[a])]
    def rel(n):        # cambio relativo de escala entre n-1 y n (None si falta alguno)
        a, b = M.get(n - 1), M.get(n)
        return abs(b["esc"] - a["esc"]) / a["esc"] if a and b and a.get("esc") and b.get("esc") else None
    # un salto de escala es un escalón aislado (> 4 % en un cuadro, < 1,5 % en los vecinos): así no cuentan los zooms suaves
    saltos_escala = [n for n in ns if n < n_cierre and (rel(n) or 0) > 0.04
                     and (rel(n - 1) or 0) < 0.015 and (rel(n + 1) or 0) < 0.015]
    for n in saltos_plano:
        cerca = [m for m in saltos_escala if 0 < abs(m - n) <= 3]
        if cerca and n not in saltos_escala:
            m = min(cerca, key=lambda x: abs(x - n))
            err["desfase_de_corte"] |= set(range(min(n, m), max(n, m)))
    # junto a un corte previsto (cambia el plano que toca), mirar otro plano 1–3 cuadros es un desfase del corte
    cortes_prev = [n for a, n in zip(ns, ns[1:]) if n == a + 1 and M[n].get("ze") != M[a].get("ze")]
    for n in sorted(err["fuera_de_plano"]):
        if any(-3 <= n - c <= 3 for c in cortes_prev) and (M[n].get("ze") is not None and M[n]["ze"] not in M[n]["zc"]):
            err["fuera_de_plano"].discard(n); err["desfase_de_corte"].add(n)
    if 0 in M:
        c0 = M[0]
        if c0["hueco"] > 0 or (c0["base"] > UMBRAL_BASE and 0 < n_cierre) or (c0.get("ze") is not None and c0["ze"] not in c0["zc"]):
            err["primer_cuadro"].add(0)
    # observaciones de duración: oscuro ≥ 0,5 s, quietud ≥ 1 s (una pausa breve no se informa)
    obs["oscuro"] = {n for a, b in tramos(obs["oscuro"]) if b - a + 1 >= 0.5 * fps for n in range(a, b + 1)}
    obs["quietud"] = {n for a, b in tramos(obs["quietud"]) if b - a + 1 >= 1.0 * fps for n in range(a, b + 1)}
    return err, obs, n_cierre


def detalle(grupo, M, fps, t0, zonas):
    out = {}
    for k, ns in grupo.items():
        if not ns:
            continue
        tr = []
        for a, b in tramos(ns):
            cs = [M[n] for n in range(a, b + 1) if n in M]
            z = zonas.get(cs[0].get("ze")) if cs else None
            tr.append({"desde": a, "hasta": b, "cuadros": b - a + 1, "seg": round(t0 + a / fps, 3),
                       "plano": (z or {}).get("set"), "hueco_max": max((c["hueco"] for c in cs), default=0),
                       "base_max": max((c["base"] for c in cs), default=0)})
        out[k] = {"cuadros": len(ns), "tramos": tr}
    return out


def hoja(ruta, imgs, etiquetas):
    from PIL import Image, ImageDraw, ImageFont
    try:
        F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 17)
    except Exception:
        F = ImageFont.load_default()
    w, h = 216, 384; cols = min(6, max(1, len(imgs))); filas = -(-len(imgs) // cols)
    H = Image.new("RGB", (cols * (w + 10) + 10, filas * (h + 58) + 10), (18, 18, 22)); dr = ImageDraw.Draw(H)
    import io
    for i, (n, (txt, col)) in enumerate(etiquetas.items()):
        x = 10 + (i % cols) * (w + 10); y = 10 + (i // cols) * (h + 58)
        H.paste(Image.open(io.BytesIO(imgs[n])).convert("RGB").resize((w, h)), (x, y))
        dr.rectangle([x - 2, y - 2, x + w + 1, y + h + 1], outline=col, width=3)
        for j, linea in enumerate(txt.split("\n")[:2]):
            dr.text((x, y + h + 6 + j * 22), linea[:26], fill=(230, 230, 230), font=F)
    H.save(ruta)


def inspeccionar(datos, motor=MOTOR, fps=30.0, t0=0.0, cuadros=None, video=None, salida=None, ruta_hoja=None,
                 desde=0, hasta=None, avance=True):
    datos = pathlib.Path(datos); txt = datos.read_text(); d = json.loads(txt); T = d.get("T") or {}
    perfil = V.perfil_de_datos(d)              # arriba o dentro de la escena, como lo toma el motor
    N = cuadros if cuadros else int(T["fin"] * fps)
    ns = list(range(desde, min(N, hasta + 1) if hasta is not None else N))
    t_ini = time.time()
    cs = medir(motor, txt, ns, t0, fps, avance)
    M = {c["n"]: c for c in cs}
    err, obs, n_cierre = clasificar(d, cs, fps, t0, perfil)
    val = V.validar_datos(d, str(datos), t0)
    for h in val["hallazgos"]:
        if h["nivel"] == "error":
            err.setdefault("validador", set()).add(max(0, int(round(((h.get("tiempo") or 0) - t0) * fps))))
    sal = None
    if video:
        import saltos as S
        sal = S.analizar(video, d, t0)
        for x in sal["islas"]:
            err.setdefault("cuadro_aislado", set()).update(range(x["desde"], x["hasta"] + 1))
    zonas = {z.get("x0"): z for z in next((s for s in d.get("escenas") or [] if s.get("tipo") == "pelicula"), {}).get("zonas") or []}
    errores = detalle(err, M, fps, t0, zonas)
    if err.get("validador"):
        errores["validador"]["hallazgos"] = [h for h in val["hallazgos"] if h["nivel"] == "error"]
    if sal and sal["islas"]:
        errores["cuadro_aislado"]["islas"] = sal["islas"]
    observaciones = detalle(obs, M, fps, t0, zonas)
    avisos = [h for h in val["hallazgos"] if h["nivel"] == "aviso"]
    if avisos:
        observaciones["aviso_del_validador"] = {"cuadros": len(avisos), "hallazgos": avisos}
    motor = pathlib.Path(motor)
    inf = {"meta": {"datos": str(datos), "motor": str(motor), "motor_sha256": hashlib.sha256(motor.read_bytes()).hexdigest(),
                    "perfil_de_fondos": perfil, "cuadros": len(ns), "fps": fps, "t0": t0, "cierre_desde_cuadro": n_cierre,
                    "video": str(video) if video else None, "segundos": round(time.time() - t_ini, 1),
                    "fecha": time.strftime("%Y-%m-%d %H:%M:%S")},
           "bloquea": bool(errores), "errores_tecnicos": errores, "observaciones_creativas": observaciones,
           "base_sobre_2pct_antes_del_cierre": sum(1 for c in cs if c["base"] > 2 and c["n"] < n_cierre),
           "cuadros": [{k: c.get(k) for k in ("n", "hueco", "base", "bp", "zc", "ze", "esc", "lum", "negro", "mov")} for c in cs]}
    if salida:
        pathlib.Path(salida).write_text(json.dumps(inf, ensure_ascii=False))
    if ruta_hoja:
        et = {}
        for k, v in errores.items():
            for tr in v.get("tramos", [])[:3]:
                et.setdefault(tr["desde"], (f"✗ {k}\n{tr['seg']:.2f} s · {tr['cuadros']} cuadro(s)", (230, 60, 60)))
        for k, v in observaciones.items():
            for tr in v.get("tramos", [])[:2]:
                et.setdefault(tr["desde"], (f"· {k}\n{tr['seg']:.2f} s · {tr['cuadros']} cuadro(s)", (80, 150, 230)))
        et = dict(list(sorted(et.items()))[:18])
        if not et:
            et = {0: ("sin errores\ncuadro 0", (90, 200, 120))}
        hoja(ruta_hoja, fotos(motor, txt, list(et), t0, fps), et)
        inf["meta"]["hoja"] = str(ruta_hoja)
    return inf


def resumen_texto(inf):
    m = inf["meta"]; L = [f"{pathlib.Path(m['datos']).name}: {m['cuadros']} cuadros en {m['segundos']} s · perfil "
                          f"{'sí' if m['perfil_de_fondos'] else 'no'} · {'BLOQUEA' if inf['bloquea'] else 'OK'}"]
    for k, v in inf["errores_tecnicos"].items():
        L.append(f"   ✗ {k}: {v['cuadros']} cuadro(s) en {len(v.get('tramos', []))} tramo(s)"
                 + "".join(f" · {t['seg']:.2f} s ({t['cuadros']})" for t in v.get("tramos", [])[:4]))
    for k, v in inf["observaciones_creativas"].items():
        L.append(f"   · {k}: {v['cuadros']}" + "".join(f" · {t['seg']:.2f} s ({t['cuadros']})" for t in v.get("tramos", [])[:3]))
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("datos"); ap.add_argument("--motor", default=str(MOTOR)); ap.add_argument("--fps", type=float, default=30.0)
    ap.add_argument("--t0", type=float, default=0.0); ap.add_argument("--cuadros", type=int); ap.add_argument("--video")
    ap.add_argument("--salida"); ap.add_argument("--hoja"); ap.add_argument("--desde", type=int, default=0); ap.add_argument("--hasta", type=int)
    a = ap.parse_args()
    inf = inspeccionar(a.datos, a.motor, a.fps, a.t0, a.cuadros, a.video, a.salida, a.hoja, a.desde, a.hasta)
    print(resumen_texto(inf))
    sys.exit(1 if inf["bloquea"] else 0)


if __name__ == "__main__":
    main()
