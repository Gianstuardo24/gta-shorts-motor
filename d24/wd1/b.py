import sys; sys.path.insert(0,'/home/claude/d24'); from formato import *
F=["Your dog knows what you're hiding. Even when you act normal.",
"You can smile and say you're fine.",
"But in 2022, scientists in Belfast put four dogs to a test.",
"They took breath and sweat from 36 people: once calm, and once right after a hard math problem.",
"Now the part you can't fake.",
"The dogs picked the stressed sample almost 94 percent of the time.",
"What they smell is your stress. You can hide it from people, but not from your dog.",
"Tell me if your dog notices your bad days.",
"Follow to decode your dog."]
V=[f.replace("2022","twenty twenty-two").replace("36 people","thirty-six people").replace("94 percent","ninety-four percent") for f in F]
P=dict(look="cliente",var=74,pelo="#4e342e",camisa="#26a69a",s=1.0)
video("D2026112501_src.json","D2026112501","THE DOGS DECODER","Your Dog Knows What You're Hiding 👻","YOUR DOG KNOWS",F,V,
 marcas=[("hiding",0,"^hiding"),("smile",1,"^smile"),("test",2,"^test"),("calm",3,"^calm"),("math",3,"^math"),("fake",4,"^fake"),("stress",6,"^stress")],
 escenas=[
  {"z":"salaV","o":{"hora":"noche","var":3,"sinSofa":True,"pared":["#45506b","#2b3248"]},
   "actores":[{**P,"keys":[{"k":0,"x":360,"pose":"cruzado","cara":"feliz"}]}],
   "props":[perro(x=760,y=1760,s=1.05,dir=-1),{"tipo":"lamparaPie","x":120,"y":1640,"s":1.1},{"tipo":"mesaCentro","x":560,"y":1880,"s":.9,"z":1900}]},
  {"k":"s_1","z":"cocinaV","actores":[{**P,"keys":[{"k":"s_1","x":420,"pose":"bebe","cara":"feliz","objeto":"taza"}]}],
   "props":[perro(x=800,y=1760,s=1.0,dir=-1,pose="sentado")]},
  {"k":"s_2","z":"labV","o":{"pantalla":"SCENT TEST","pantalla2":"BELFAST"},"titulo":("BELFAST, 2022","cian"),
   "actores":[{"look":"inventor","var":75,"lentes":True,"pelo":"#5d4037","camisa":"#eceff1","s":.98,"keys":[{"k":"s_2","x":330,"pose":"explica","cara":"feliz"}]}],
   "props":[perro(x=760,y=1760,s=.95,dir=-1),{"tipo":"mesaLab","x":900,"y":1640,"s":.8,"z":1500}]},
  {"k":"s_3","i":["#dfe9f5","#8fa6c2","#18222f"],"luz2":"235,245,255","props":[{"tipo":"cajita","x":300,"y":1560,"s":2.3,"color":"#a5d6a7","texto":"CALM","cae":True},{"tipo":"cajita","x":780,"y":1560,"s":2.3,"color":"#ef9a9a","texto":"STRESS","k":"math","cae":True},{"tipo":"nariz","x":540,"y":1080,"s":.85,"flota":6}]},
  {"k":"s_4","z":"dormitorioV","o":{"persona":False,"pared":["#3a4766","#252d47"]},
   "actores":[{**P,"keys":[{"k":"s_4","x":380,"pose":"piensa","cara":"triste"}]}],"props":[perro(x=760,y=1760,s=1.0,dir=-1)]},
  {"k":"s_5","i":["#1e3d2a","#0d1f14","#020604"],"luz2":"190,255,200","props":[{"tipo":"mitad","x":540,"y":1520,"s":.95,"de":"s_5","a":"s_5+2.2","n0":0,"n1":.94,"half":"94%","sinReloj":1,"c1":"#66bb6a","c2":"#1b5e20","texto":"RIGHT PICKS"}]},
  {"k":"s_6","z":"parqueV","o":{"hora":"tarde"},"actores":[{**P,"keys":[{"k":"s_6","x":380,"pose":"explica","cara":"feliz"}]}],
   "props":[perro(x=760,y=1760,s=1.05,dir=-1),{"tipo":"neblina","x":540,"y":1800,"a":.12}]}],
 emojis=[{"k":"hiding","e":"👻"},{"k":"fake","e":"😶","dur":1.0},{"k":"stress","e":"🐶","dur":1.2}],
 hints=[{"k":0,"tipo":"general"}],gancho2=4,cierre="DOES YOURS NOTICE?",paises=["YES","NO","ALWAYS"],
 nota="Wilson et al. (2022), PLOS ONE, Queen's University Belfast: aliento y sudor de 36 personas antes (calma) y después de una tarea aritmética difícil. 4 perros entrenados eligieron la muestra de estrés en 675 de 720 pruebas = 93,75 % -> 'almost 94 percent'. Lo que huelen es el cambio de olor por estrés. Emoji fantasma = prueba pedida por Tao. Disparador: secreto. Gancho tipo 2.",
 fuentes=["https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0274143","https://www.qub.ac.uk/News/Allnews/2022/"])
