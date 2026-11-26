import sys, json; sys.path.insert(0,'/home/claude/largos'); from largo import *
R=[(r"\b1979\b","nineteen seventy-nine"),(r"135,000","one hundred thirty-five thousand")]
L=Largo(R)
LUCAS=dict(look="ejecutivo",var=301,camisa="#6d4c41",pelo="#3e2723",barba="#3e2723",s=1.0)
CAT=dict(look="inventor",var=302,camisa="#455a64",pelo="#4e342e",barba="#4e342e",s=0.95)
SMITH=dict(look="inventor",var=307,camisa="#8d6e63",pelo="#212121",s=0.95)
t=L.tramo("lab80",capitulo="The secret lab")
t.dice("In 1979, George Lucas hired a small team of computer scientists.",
       "Their job was to bring computers into moviemaking.",
       "Back then, computers were slow, huge, and very expensive.")
kj=t.m("job",1,"^job"); ks=t.m("slow",2,"^slow")
L.titulo(t.key,"THE SECRET LAB","cian",fin=kj)
t.actor(LUCAS,[{"x":420,"pose":"apunta","cara":"feliz"},{"k":ks,"x":420,"pose":"cruzado","cara":"neutral"}])
t.actor(CAT,[{"x":980,"pose":"juega","cara":"feliz","dir":-1},{"k":ks,"x":980,"pose":"piensa","cara":"neutral","dir":-1}])
t.actor(SMITH,[{"x":1520,"pose":"saluda","cara":"feliz","dir":-1}])
t=L.tramo("vitrina",capitulo="The $135,000 computer")
t.dice("Here is the machine they built.",
       "A graphics computer that cost 135,000 dollars.",
       "It made beautiful images. But almost nobody could afford it.")
kp=t.m("cost",1,"^cost"); kn=t.m("nob",2,"^nobody")
L.titulo(t.key,"THE $135,000 COMPUTER","amar",fin=kp)
t.prop("compu85",1010,1720,1.05,precio="$135,000")
L.chip(kn,"ALMOST NOBODY BOUGHT IT","rojo")
meta={"titulo":"muestra","texto_pantalla":"","lote":"M1","marca":"MILLION DOLLAR MISTAKE","tema":"","nota_datos":"","fuentes":[]}
g=L.armar(meta,cola=0.5)
json.dump(g,open("M1_src.json","w"),ensure_ascii=False)
print("ok")
