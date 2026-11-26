"""uso: ficha.py guion.json datos.json "voz vel" musica salida.ficha.json  -> ficha del video para el análisis"""
import sys, json
g=json.load(open(sys.argv[1])); d=json.load(open(sys.argv[2])); voz=sys.argv[3]; mus=sys.argv[4]
MICRO={"G":"Los números de GTA 6","Gen":"Hidden mechanics","R":"Casos OVNI cerrados","C":"El café prohibido","M":"Lo vendió por $X","D":"Why your dog does that","K":"Why your cat does that"}
lote=g.get("lote",""); k="Gen" if lote.endswith("en") else lote[:1]
f={"gancho":g["frases"][0],"texto_pantalla":g.get("texto_pantalla"),"tema":g.get("titulo"),"micronicho":MICRO.get(k),
   "formato":"pelicula","voz":voz,"musica":mus,"duracion_s":round(d["T"]["fin"],1),
   "pregunta_cierre":g["escena"].get("cierre"),"idioma":"es" if voz.startswith("em_") else "en","lote":lote}
json.dump(f,open(sys.argv[5],"w"),ensure_ascii=False,indent=1); print(sys.argv[5])
