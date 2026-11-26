import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["This man lost 10 percent of Apple in 12 days.",
"Ronald Wayne founded Apple with Steve Jobs and Steve Wozniak. He even drew its first logo.",
"Then Jobs borrowed 15,000 dollars for their first big order, and Wayne got scared.",
"He was the only partner who owned things a bank could take.",
"So he walked away, and sold his share for 800 dollars.",
"Today Apple is worth trillions. Wayne says he does not regret it.",
"Lesson: fear has a price too. Tell me if you would have stayed.",
"Follow for the next million dollar mistake."]
voz=[f.replace("1976","nineteen seventy-six").replace("10 percent","ten percent").replace("800 dollars","eight hundred dollars").replace("15,000","fifteen thousand").replace("12 days","twelve days") for f in frases]
M=[["lost",0,"^lost"],["p10",0,"^10"],["days0",0,"^12"],
["s_found",1,None],["jobs1",1,"^jobs"],["woz",1,"^wozniak"],["logo",1,"^logo"],
["s_loan",2,None],["d15",2,"^15"],["scared",2,"^scared"],
["s_only",3,None],["owned",3,"^owned"],["take",3,"^take"],
["s_days",4,None],["walked",4,"^walked"],["sold",4,"^sold"],["d800b",4,"^800"],
["s_today",5,None],["trillions",5,"^trillions"],["regret",5,"^regret"],
["s_les",6,None],["price",6,"^price"],["s_fin",6,"^tell"],["s_cta",7,None]]
WA=dict(look="inventor",var=81,pelo="#b0b0b0",camisa="#5d4037",lentes=True,s=1.0)
JO=dict(look="gamer",var=82,pelo="#2b1d14",camisa="#111111",s=0.97)
WO=dict(look="jugador",var=83,pelo="#3e2723",camisa="#1565c0",s=0.97)
P=[{"tipo":"pc","x":760,"y":1650,"s":1.0,"k":0.0,"texto":"APPLE I","fin":"s_loan"},
   {"tipo":"documento","x":300,"y":1150,"s":0.85,"sello":"FIRST LOGO","selloc":"amar","k":"logo","cae":True,"z":1800,"fin":"s_loan"},
   {"tipo":"bolsa_dinero","x":1900,"y":1690,"s":1.3,"k":"d15","cae":True,"fin":"s_only"},
   {"tipo":"documento","x":1500,"y":1200,"s":0.85,"sello":"LOAN","selloc":"rojo","k":"d15+0.3","cae":True,"z":1800,"fin":"s_only"},
   {"tipo":"casa","x":3230,"y":1640,"s":0.5,"k":"owned","fin":"s_days"},
   {"tipo":"billetes","x":3060,"y":1720,"s":1.2,"k":"owned+0.3","cae":True,"fin":"s_days"},
   {"tipo":"documento","x":4620,"y":1180,"s":1.0,"sello":"I QUIT","selloc":"rojo","k":"walked","cae":True,"z":1800,"fin":"s_today"},
   {"tipo":"bolsa_dinero","x":5860,"y":1690,"s":1.2,"k":"trillions","cae":True},
   {"tipo":"bolsa_dinero","x":6010,"y":1690,"s":1.2,"k":"trillions+0.2","cae":True},
   {"tipo":"bolsa_dinero","x":5935,"y":1580,"s":1.2,"k":"trillions+0.4","cae":True}]
A=[{**WA,"hasta":"s_loan","keys":[{"k":0,"x":320,"y":1700,"pose":"parado","cara":"neutral"},{"k":"s_found","x":320,"y":1700,"pose":"saluda","cara":"feliz"},{"k":"logo","x":320,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {**JO,"desde":"jobs1","hasta":"s_loan","keys":[{"k":"jobs1","x":560,"y":1700,"pose":"cruzado","cara":"feliz"}]},
   {**WO,"desde":"woz","hasta":"s_loan","keys":[{"k":"woz","x":960,"y":1700,"pose":"saluda","cara":"risa","dir":-1}]},
   {**JO,"desde":"s_loan","hasta":"s_only","keys":[{"k":"s_loan","x":1360,"y":1700,"pose":"camina","cara":"feliz"},{"k":"s_loan+1.0","x":1650,"y":1700,"pose":"apunta","cara":"feliz"},{"k":"d15","x":1650,"y":1700,"pose":"celebra","cara":"risa"}]},
   {**WA,"desde":"s_loan","hasta":"s_only","keys":[{"k":"s_loan","x":2140,"y":1700,"pose":"parado","cara":"neutral","dir":-1},{"k":"scared","x":2140,"y":1700,"pose":"piensa","cara":"sorpresa","dir":-1,"fx":"tiembla"}]},
   {**WA,"desde":"s_only","hasta":"s_days","keys":[{"k":"s_only","x":2900,"y":1700,"pose":"piensa","cara":"triste"},{"k":"take","x":2900,"y":1700,"pose":"cruzado","cara":"triste","fx":"tiembla"}]},
   {"look":"ejecutivo","var":84,"s":0.97,"desde":"take","hasta":"s_days","keys":[{"k":"take","x":3470,"y":1700,"pose":"apunta","cara":"enojado","dir":-1}]},
   {**WA,"desde":"s_days","hasta":"s_today","keys":[{"k":"s_days","x":4250,"y":1700,"pose":"parado","cara":"neutral"},{"k":"walked","x":4250,"y":1700,"pose":"ofrece","cara":"neutral","objeto":"documento"},{"k":"sold","x":4250,"y":1700,"pose":"sostiene","cara":"neutral","objeto":"cheque"}]},
   {**JO,"desde":"s_days","hasta":"s_today","keys":[{"k":"s_days","x":4720,"y":1700,"pose":"parado","cara":"sorpresa","dir":-1}]},
   {**WA,"pelo":"#f0f0f0","desde":"s_today","keys":[{"k":"s_today","x":5520,"y":1700,"pose":"parado","cara":"neutral"},{"k":"regret","x":5520,"y":1700,"pose":"cruzado","cara":"feliz"},{"k":"s_les","x":5520,"y":1700,"pose":"piensa","cara":"neutral"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.1,
 "zonas":[{"x0":-300,"x1":1300,"set":"garage"},{"x0":1300,"x1":2600,"set":"banco","k":"s_loan"},{"x0":2600,"x1":3900,"set":"sala","k":"s_only","luz":"tenue"},
          {"x0":3900,"x1":5200,"set":"oficina","k":"s_days"},{"x0":5200,"x1":6600,"set":"banco","k":"s_today"}],
 "pan":[{"k":"s_loan","x":1300,"dur":1.0},{"k":"s_only","x":2600,"dur":0.9},{"k":"s_days","x":3900,"dur":0.9},{"k":"s_today","x":5200,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[{"k":"scared+0.2","de":4,"texto":"TOO RISKY.","fin":"s_only","dx":-80},{"k":"regret","de":9,"texto":"NO REGRETS.","fin":"s_les","dx":110}],
 "numeros":[
            {"k":"d15","n":15000,"pre":"$","c":"rojo","etq":"BORROWED","fin":"s_only"}],
  "zoom":[],
 "sacudidas":[{"k":"lost","f":14},{"k":"d800b","f":14},{"k":"trillions","f":20}],
 "titulos":[{"k":"days0","texto":"12 DAYS","c":"rojo","grande":True,"fin":"s_found"},
            {"k":"s_found","texto":"THE THIRD FOUNDER","c":"cian","fin":"s_loan"},
            {"k":"s_loan","texto":"THE LOAN","c":"rojo","fin":"s_only"},
            {"k":"s_only","texto":"EVERYTHING TO LOSE","c":"rosa","fin":"s_days"},
            {"k":"s_days","texto":"HE WALKED AWAY","c":"amar","fin":"sold"},
            {"k":"s_today","texto":"TODAY","c":"verde","fin":"s_les"},
            {"k":"s_les+0.4","texto":"THE LESSON","c":"rojo","fin":"s_fin"}],
 "chips":[{"k":"woz","texto":"JOBS · WOZNIAK · WAYNE","c":"cian","fin":"s_loan"},
          {"k":"price","texto":"FEAR HAS A PRICE","c":"amar","fin":"s_fin"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"STAY OR LEAVE?","cierre2":"Would you have stayed? Comment","paises":["STAY","LEAVE"],"sfx":[],"cta":"FOLLOW FOR MORE","like":"LIKE"}
poner_sets(E,[None,None,("salaV",{"hora":"noche","sinSofa":True,"var":1}),None,("corporativoV",{"ticker":"AAPL ▲","hora":"noche"})])
insertar(E,"logo","s_loan",1300,"vitrinaV",{"fondo":["#1a1206","#3b2a0c","#120c04"],"luz2":"255,214,120","pedestal":False},[{"tipo":"documento","x":540,"y":1280,"s":2.0,"sello":"FIRST LOGO","selloc":"amar"}])
insertar(E,"sold","s_today",5200,"vitrinaV",{"fondo":["#e8e2d2","#a89878","#2a2214"],"luz2":"255,245,220"},[{"tipo":"papel","x":540,"y":1760,"s":1.25,"titulo":"BILL OF SALE · 1976","dato":"10% OF APPLE: $800","sello":"SOLD","selloc":"rojo","filaDato":6}])
insertar(E,"p10","s_found",0,"vitrinaV",{"fondo":["#3a0d0d","#1c0606","#080202"],"luz2":"255,150,150","pedestal":True},[{"tipo":"pc","x":540,"y":1380,"s":2.0,"texto":"APPLE"}])
g={"titulo":"He Lost 10% of Apple in 12 Days 👎","texto_pantalla":"LOST IN 12 DAYS","lote":"M2026112403","marca":"MILLION DOLLAR MISTAKE",
"nota_datos":"Ronald Wayne cofundó Apple el 1-abr-1976 con Jobs y Wozniak (10% para él, 45% cada uno); dibujó el primer logo y redactó el acuerdo. Jobs obtuvo una línea de crédito de US$15.000 para el pedido de Byte Shop; Wayne era el único con bienes que los acreedores podían embargar. A los 12 días vendió su parte por US$800 (más US$1.500 después por renunciar a reclamos). Dice no arrepentirse. Su parte se habría diluido. Fuentes: Wikipedia (Ronald Wayne), Fortune, Yahoo Finance. Banco MDM caso 2.",
"frases":frases,"frases_voz":voz,"fuentes":["https://en.wikipedia.org/wiki/Ronald_Wayne","https://fortune.com/","https://finance.yahoo.com/"],"escena":E}
guardar("M2026112403_src.json",g)
