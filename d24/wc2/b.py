import sys; sys.path.insert(0,'/home/claude/d24'); from formato import *
F=["Your mug of coffee beats a shot of espresso on caffeine. Cup for cup.",
"Espresso tastes stronger, so it feels like it has more.",
"And sip for sip, it does: about 63 milligrams in one small ounce.",
"But a regular 8 ounce mug of brewed coffee has about 95.",
"Now here's how to use that.",
"A double shot gets you to about 126, more than the mug.",
"So for less caffeine, go single shot. For more, go double.",
"Tell me which one you drink.",
"Follow for one coffee curiosity a day."]
V=[f.replace("63 milligrams","sixty-three milligrams").replace("8 ounce","eight ounce").replace("about 95","about ninety-five").replace("about 126","about a hundred and twenty-six") for f in F]
CL=dict(look="cliente",var=97,pelo="#5d4037",camisa="#00897b",s=1.0)
BA=dict(look="vendedor",var=98,pelo="#212121",camisa="#5d4037",s=1.0)
video("C2026112502_src.json","C2026112502","COFFEE, BUT WHY?","Your Mug Beats Espresso on Caffeine ☕😳","YOUR MUG BEATS ESPRESSO",F,V,
 marcas=[("beats",0,"^beats"),("stronger",1,"^stronger"),("m63",2,"^63"),("m95",3,"^95"),("use",4,"^use"),("double",5,"^double"),("m126",5,"^126"),("single",6,"^single")],
 escenas=[
  {"i":["#3a2a20","#1c130d","#050302"],"luz2":"255,220,180","props":[{"tipo":"barras2","x":540,"y":1650,"s":1.6,"a":[63,"ESPRESSO","#8d6e63"],"b":[95,"MUG","#ff7043"],"suf":" MG"},{"tipo":"humo","x":540,"y":1700,"s":.6,"a":.12}]},
  {"k":"s_1","z":"fuenteSodaV","actores":[{**BA,"keys":[{"k":"s_1","x":330,"pose":"ofrece","cara":"feliz","objeto":"taza"}]},{**CL,"keys":[{"k":"s_1","x":760,"pose":"sostiene","cara":"sorpresa","objeto":"taza"}]}],
   "props":[{"tipo":"cafetera","x":120,"y":1520,"s":.8,"z":1500},{"tipo":"humo","x":130,"y":1300,"s":.4,"a":.2}]},
  {"k":"s_2","i":["#2b1d14","#140d08","#040201"],"luz2":"255,214,160","pedestal":True,"props":[{"tipo":"capas","x":540,"y":1300,"s":1.0,"h":140,"w":120,"k":"s_2","nombre":"1 OUNCE","capas":[[.9,"#3e1f0c","ESPRESSO"],[.1,"#c98a4a","CREMA"]]}]},
  {"k":"s_3","z":"cocinaV","actores":[{**CL,"keys":[{"k":"s_3","x":420,"pose":"bebe","cara":"feliz","objeto":"taza"}]}],"props":[{"tipo":"humo","x":760,"y":1500,"s":.4,"a":.16}]},
  {"k":"s_4","z":"cafetalV","actores":[{**BA,"keys":[{"k":"s_4","x":420,"pose":"explica","cara":"feliz"}]}],"props":[{"tipo":"neblina","x":540,"y":1800,"a":.14}]},
  {"k":"s_5","i":["#3a2a20","#1c130d","#050302"],"luz2":"255,220,180","props":[{"tipo":"barras2","x":540,"y":1650,"s":1.6,"a":[95,"MUG","#ff7043"],"b":[126,"DOUBLE SHOT","#6d4c41"],"suf":" MG"}]},
  {"k":"s_6","z":"parqueV","o":{"hora":"tarde"},"actores":[{**CL,"keys":[{"k":"s_6","x":330,"pose":"bebe","cara":"feliz","objeto":"taza"}]},{**BA,"keys":[{"k":"s_6","x":760,"pose":"explica","cara":"feliz"}]}]}],
 numeros=[{"k":"m63","n":63,"suf":" MG","c":"verde","etq":"ONE ESPRESSO SHOT","fin":"s_3"},{"k":"m95","n":95,"suf":" MG","c":"rojo","etq":"8 OZ BREWED MUG","fin":"s_4"}],
 emojis=[{"k":"beats","e":"😳"},{"k":"use","e":"💡"},{"k":"single","e":"☕","dur":1.2}],
 gancho2=4,cierre="SINGLE OR DOUBLE?",cierre2="Your pick. Comment",paises=["SINGLE","DOUBLE","MUG"],
 nota="USDA: espresso ~63 mg de cafeína por 1 oz (un shot); café filtrado ~95-96 mg por taza de 8 oz (12-16 mg/oz). Doble shot ~126 mg. Por onza el espresso tiene más; por taza, la taza de filtrado gana a un shot. Las cifras varían por grano, tueste y preparación ('about'). Fuentes: Consumer Reports (datos USDA), Bean Box, The Takeout. Disparador: contradicción. Gancho tipo 1.",
 fuentes=["https://www.consumerreports.org/health/coffee/is-there-more-caffeine-in-espresso-than-in-coffee-a4556213289","https://fdc.nal.usda.gov/"])
