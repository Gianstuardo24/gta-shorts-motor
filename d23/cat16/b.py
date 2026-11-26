import sys; sys.path.insert(0,'/home/claude/d23'); from comun import *
frases=["Your cat's purr can hide a tiny cry for food.",
"In 2009, researchers in England recorded cats purring in two moments: when they wanted food, and when they didn't.",
"Then 50 people listened to both.",
"The hungry purrs sounded more urgent, even to people who had never owned a cat.",
"The reason: a high-pitched sound hidden inside the purr, close to the pitch of a crying baby.",
"Researchers call it the solicitation purr.",
"Tell me if your cat does this at breakfast.",
"Follow to decode your cat."]
voz=[f.replace("2009","two thousand nine").replace("50","fifty") for f in frases]
M=[["purr0",0,"^purr"],["cry",0,"^cry"],["food0",0,"^food"],["s_rec",1,None],["recorded",1,"^recorded"],["wanted",1,"^wanted"],["didnt",1,"^didn"],
["s_50",2,None],["p50",2,"^50"],["listened",2,"^listened"],["s_urg",3,None],["urgent",3,"^urgent"],["never",3,"^never"],
["s_hidden",4,None],["high",4,"^high"],["baby",4,"^baby"],["s_name",5,None],["solicitation",5,"^solicitation"],["s_fin",6,None],["s_cta",7,None]]
P=[{"tipo":"sofa","x":330,"y":1720,"s":1.3,"k":0,"fin":"s_rec"},
   gato(x=500,y=1655,z=1850,k=0,fin="s_rec",lento=False),
   {"tipo":"pc","x":1950,"y":1650,"s":1.1,"k":"s_rec","texto":"PURR LAB","fin":"s_50"},
   gato(x=1550,y=1740,s=0.85,k="s_rec",fin="s_50",dir=1),
   {"tipo":"grafico","x":1950,"y":1150,"s":1.0,"k":"recorded","cae":True,"fin":"s_50"},
   {"tipo":"tv","x":3250,"y":1120,"s":1.0,"k":"s_50","fin":"s_name"},
   {"tipo":"viento","x":3250,"y":1100,"s":0.8,"k":"high","fin":"s_name"},
   gato(x=4550,y=1740,s=0.85,k="s_name",dir=1)]
A=[{"look":"gamer","var":201,"camisa":"#26a69a","pelo":"#5d4037","peloT":"largo","s":1.0,"hasta":"s_rec","keys":[
    {"k":0,"x":260,"y":1714,"pose":"sentado","cara":"neutral","z":1800},
    {"k":"food0","x":260,"y":1714,"pose":"sentado","cara":"sorpresa","z":1800,"fx":"salto"}]},
   {"look":"inventor","var":203,"s":0.95,"desde":"s_rec","hasta":"s_50","lentes":True,"pelo":"#8d6e63","peloT":"corto","camisa":"#eceff1","keys":[
    {"k":"s_rec","x":1800,"y":1700,"pose":"parado","cara":"neutral","dir":-1},{"k":"wanted","x":1800,"y":1700,"pose":"apunta","cara":"feliz","dir":-1}]},
   {"look":"cliente","var":211,"s":0.9,"desde":"s_50","hasta":"s_name","keys":[{"k":"s_50","x":2800,"y":1700,"pose":"parado","cara":"neutral"},{"k":"urgent","x":2800,"y":1700,"pose":"parado","cara":"sorpresa","fx":"salto"}]},
   {"look":"jugadora","var":212,"s":0.9,"desde":"s_50","hasta":"s_name","keys":[{"k":"s_50","x":3020,"y":1710,"pose":"parado","cara":"neutral"},{"k":"urgent+0.2","x":3020,"y":1710,"pose":"piensa","cara":"sorpresa"}]},
   {"look":"vendedor","var":213,"s":0.9,"desde":"s_50","hasta":"s_name","keys":[{"k":"s_50","x":3250,"y":1700,"pose":"parado","cara":"neutral","dir":-1},{"k":"never","x":3250,"y":1700,"pose":"apunta","cara":"sorpresa","dir":-1}]},
   {"look":"gamer","var":214,"s":0.9,"desde":"s_50","hasta":"s_name","peloT":"rulos","pelo":"#1d1d1d","keys":[{"k":"s_50","x":3470,"y":1710,"pose":"parado","cara":"neutral","dir":-1},{"k":"urgent+0.4","x":3470,"y":1710,"pose":"celebra","cara":"risa","dir":-1}]},
   {"look":"gamer","var":201,"camisa":"#26a69a","pelo":"#5d4037","peloT":"largo","s":1.0,"desde":"s_name","keys":[
    {"k":"s_name","x":4850,"y":1700,"pose":"parado","cara":"neutral","dir":-1},{"k":"solicitation","x":4850,"y":1700,"pose":"ofrece","cara":"risa","dir":-1,"objeto":"taza"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.0,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala","luz":"tenue"},{"x0":1300,"x1":2600,"set":"estudio","k":"s_rec"},{"x0":2600,"x1":3900,"set":"estudio","k":"s_50","luz":"tenue"},{"x0":3900,"x1":5200,"set":"cafe","k":"s_name","luz":"tenue"}],
 "pan":[{"k":"s_rec","x":1300,"dur":1.0},{"k":"s_50","x":2600,"dur":0.9},{"k":"s_name","x":3900,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[{"k":"purr0","de":0,"texto":"PRRR...","fin":"food0","dx":180}],
 "numeros":[{"k":"p50","n":50,"suf":" PEOPLE","c":"cian","etq":"LISTENING","fin":"s_hidden"}],
 "zoom":[{"k":0.1,"s":1.3,"x":460,"y":1560,"dur":0.8},{"k":"food0","s":1.05,"dur":0.5},{"k":"s_rec","s":1.0,"dur":0.5},
         {"k":"s_50","s":1.0,"dur":0.5},{"k":"s_name","s":1.0,"dur":0.5},{"k":"solicitation","s":1.2,"x":4650,"y":1540,"dur":0.7}],
 "titulos":[{"k":0.2,"texto":"THE HUNGRY PURR","c":"amar","fin":"s_rec"},
            {"k":"s_rec","texto":"UNIVERSITY OF SUSSEX · 2009","c":"cian","fin":"s_50"},
            {"k":"s_hidden","texto":"A HIDDEN CRY","c":"rosa","grande":True,"fin":"s_name"},
            {"k":"solicitation","texto":"SOLICITATION PURR","c":"verde","grande":True,"fin":"s_fin"}],
 "chips":[{"k":"wanted","texto":"FOOD VS NO FOOD","c":"amar","fin":"s_50"},
          {"k":"urgent","texto":"MORE URGENT","c":"rojo","fin":"s_hidden"},
          {"k":"baby","texto":"LIKE A CRYING BABY","c":"rosa","fin":"s_name"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"DOES YOURS DO IT?","cierre2":"Yes or no? Comment","paises":["YES","NO"],"cta":"FOLLOW FOR MORE","like":"LIKE","sfx":[]}
g={"titulo":"Why Your Cat Purrs When It's Hungry 🐱","texto_pantalla":"THE HUNGRY PURR","lote":"K2026112301","marca":"THE CATS DECODER",
"nota_datos":"McComb et al. 2009, Current Biology (Univ. of Sussex): purrs grabados de 10 gatos pidiendo comida vs. otros contextos; 50 personas los escucharon; los de 'solicitación' sonaron más urgentes y menos agradables, incluso a quienes nunca tuvieron gato; elemento agudo (~380 Hz) parecido al llanto de un bebé. Fuentes: Sussex, EurekAlert (Cell Press), National Geographic (Ed Yong), Scientific American.",
"frases":frases,"frases_voz":voz,"fuentes":["https://www.sussex.ac.uk/broadcast/read/1208","https://www.eurekalert.org/news-releases/728618","https://www.scientificamerican.com/blog/news-blog/the-manipulative-meow-cats-learn-to-2009-07-13/"],"escena":E}
guardar("K2026112301_01_src.json",g)
