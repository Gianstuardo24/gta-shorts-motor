import sys; sys.path.insert(0,'/home/claude/d24'); from formato import *
F=["Stop buying red toys for your dog. At least until you see this. Careful, you might be wasting your money on the wrong colors.",
"For years, people thought dogs saw the world in black and white.",
"In 1989, scientist Jay Neitz showed that dogs do see color, just fewer than us.",
"We have three types of color cells in our eyes. Dogs have only two.",
"Specifically, blues and yellows. Reds look dark and muddy instead, almost brownish gray.",
"Now the part almost nobody notices. And it's where your money goes to waste.",
"Green grass looks dull to them too. So a red ball on the lawn almost blends in.",
"That bright toy you paid for is hard for your dog to spot. That's why it may run right past it.",
"So for games outside, pick blue or yellow. Those are the colors dogs see best.",
"Tell me what color your dog's favorite toy is.",
"Follow to decode your dog."]
V=[f.replace("1989","nineteen eighty-nine") for f in F]
P=dict(look="cliente",var=95,pelo="#212121",camisa="#e53935",s=1.0)
video("D2026112502_src.json","D2026112502","THE DOGS DECODER","STOP Buying RED TOYS For Your Dog 🐶🔴🚫","STOP BUYING RED TOYS",F,V,
 marcas=[("red0",0,"^red"),("wasting",0,"^wasting"),("white",1,"^white"),("color",2,"^color"),("three",3,"^three"),("two",3,"^two"),("blues",4,"^blues"),("reds",4,"^reds"),("nobody",5,"^nobody"),("waste",5,"^waste"),("blends",6,"^blends"),("spot",7,"^spot"),("past",7,"^past"),("blue",8,"^blue")],
 escenas=[
  {"i":["#3a1414","#1c0808","#050101"],"luz2":"255,200,200","pedestal":True,"props":[{"tipo":"pelota","x":540,"y":1300,"s":2.2,"color":"#e53935"},{"tipo":"neblina","y":1700,"a":.12}]},
  {"k":"s_1","z":"salaV","o":{"hora":"tarde","var":4,"sinSofa":True},"actores":[{**P,"keys":[{"k":"s_1","x":360,"pose":"explica","cara":"feliz"}]}],
   "props":[perro(x=780,y=1760,s=1.05,dir=-1),{"tipo":"tv","x":980,"y":1500,"s":.7,"z":1500}]},
  {"k":"s_2","z":"labV","o":{"pantalla":"DOG VISION","pantalla2":"1989"},"titulo":("1989","amar"),
   "actores":[{"look":"inventor","var":96,"lentes":True,"pelo":"#8d6e63","camisa":"#eceff1","s":.98,"keys":[{"k":"s_2","x":330,"pose":"lee","cara":"neutral","objeto":"documento"},{"k":"color","x":330,"pose":"explica","cara":"feliz"}]}],
   "props":[perro(x=780,y=1760,s=.95,dir=-1)]},
  {"k":"s_3","i":["#16243f","#0b1222","#020408"],"luz2":"200,220,255","pedestal":True,"props":[
    {"tipo":"rotulo","x":310,"y":1150,"s":1.4,"texto":"YOU · 3","color":"#ffffff","k":"three"},
    {"tipo":"rotulo","x":770,"y":1150,"s":1.4,"texto":"DOG · 2","color":"#ffd54f","k":"two"},
    perro(x=770,y=1560,s=1.05,dir=-1),{"tipo":"neblina","y":1750,"a":.12}]},
  {"k":"s_4","i":["#1c2a44","#0d1424","#020408"],"luz2":"200,220,255","props":[{"tipo":"visionPerro","x":540,"y":1600,"s":1.0,"k":"s_4","a":"YOU","b":"YOUR DOG"}]},
  {"k":"s_5","z":"parqueV","o":{"hora":"tarde"},"actores":[{**P,"keys":[{"k":"s_5","x":330,"pose":"ofrece","cara":"feliz","objeto":"pelota"}]}],"props":[perro(x=780,y=1760,s=1.05,dir=-1)]},
  {"k":"s_6","i":["#203a1c","#0f1d0d","#030602"],"luz2":"220,255,200","props":[{"tipo":"visionPerro","x":540,"y":1600,"s":1.0,"k":"s_6","a":"RED BALL","b":"TO YOUR DOG"}]},
  {"k":"s_7","z":"parqueV","o":{"hora":"tarde"},"actores":[{**P,"keys":[{"k":"s_7","x":300,"pose":"piensa","cara":"sorpresa"}]}],
   "props":[{"tipo":"pelota","x":560,"y":1760,"s":.8,"color":"#8d4a3a"},perro(x=860,y=1760,s=1.0,dir=1)]},
  {"k":"s_8","z":"casaPalmasV","o":{"sinCasa":True},"actores":[{**P,"keys":[{"k":"s_8","x":330,"pose":"celebra","cara":"risa"}]}],
   "props":[perro(x=760,y=1760,s=1.05,dir=-1),{"tipo":"pelota","x":600,"y":1720,"s":.9,"color":"#1e88e5","k":"blue"},{"tipo":"pelota","x":900,"y":1740,"s":.8,"color":"#fdd835","k":"blue"}]}],
 prohibidos=[{"k":"red0","x":540,"y":1180,"r":220,"ins":1}],sacudidas=[{"k":"red0","f":12}],
 emojis=[{"k":"wasting","e":"💸"},{"k":"white","e":"🤔"},{"k":"nobody","e":"👀"},{"k":"blue","e":"💙","dur":1.2}],
 gancho2=5,cierre="WHAT COLOR IS IT?",cierre2="Tell me. Comment",paises=["RED","BLUE","YELLOW"],
 nota="Neitz, Geist y Jacobs (1989), Visual Neuroscience: los perros son dicromáticos (dos tipos de conos, humanos tres); ven azules y amarillos; rojo y verde se ven apagados (pardo grisáceo). Un juguete rojo sobre pasto verde se confunde con el pasto. AKC: juguetes azules y amarillos. Guion aprobado por Tao 25-nov (línea base).",
 fuentes=["https://www.scientificamerican.com/article/what-colors-do-dogs-see/","https://www.akc.org/expert-advice/health/are-dogs-color-blind/"])
