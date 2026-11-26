import sys; sys.path.insert(0,'/home/claude/d24'); from formato import *
F=["Nike paid peanuts for its logo. And that's only half the story.",
"In 1971, Phil Knight needed a logo for his new shoes.",
"He asked a design student, Carolyn Davidson.",
"She charged 2 dollars an hour and worked about 17 hours: 35 dollars in total.",
"Now the part most people never hear.",
"Twelve years later, Nike surprised her with a gold ring and 500 shares of stock.",
"Lesson: price the work, not the hours. A small job can become the face of a giant.",
"Tell me what you would have charged.",
"Follow for the next million dollar mistake."]
V=[f.replace("1971","nineteen seventy-one").replace("2 dollars","two dollars").replace("17 hours","seventeen hours").replace("35 dollars","thirty-five dollars").replace("500 shares","five hundred shares") for f in F]
K=dict(look="ejecutivo",var=87,pelo="#5d4037",camisa="#455a64",corbata="#c62828",s=1.0)
D=dict(look="jugadora",var=88,pelo="#6d4c41",camisa="#ffb300",s=1.0)
video("M2026112501_src.json","M2026112501","MILLION DOLLAR MISTAKE","Nike Paid Peanuts for Its Logo 👟🥜","PAID PEANUTS",F,V,
 marcas=[("peanuts",0,"^peanuts"),("half",0,"^half"),("student",2,"^student"),("m35",3,"^35"),("never",4,"^never"),("ring",5,"^ring"),("m500",5,"^500"),("price",6,"^price")],
 escenas=[
  {"i":["#2b2b2b","#141414","#030303"],"luz2":"255,235,200","pedestal":True,"props":[{"tipo":"zapatilla","x":540,"y":1290,"s":1.25,"color":"#eceff1","color2":"#ff7043"},{"tipo":"rotulo","x":540,"y":1010,"s":1.2,"texto":"LOGO PRICE: ???","color":"#ffd54f"},{"tipo":"neblina","y":1700,"a":.12}]},
  {"k":"s_1","z":"tallerV","titulo":("OREGON, 1971","amar"),"actores":[{**K,"keys":[{"k":"s_1","x":360,"pose":"piensa","cara":"neutral"}]}],
   "props":[{"tipo":"zapatilla","x":800,"y":1640,"s":.6,"z":1500},{"tipo":"cajita","x":800,"y":1760,"s":1.2,"color":"#ff7043","texto":"SHOES"}]},
  {"k":"s_2","z":"cuartoV","actores":[{**D,"keys":[{"k":"s_2","x":420,"pose":"lee","cara":"feliz","objeto":"documento"}]}],"props":[{"tipo":"lamparaPie","x":900,"y":1640,"s":1.0,"z":1500}]},
  {"k":"s_3","i":["#e8e2d2","#a89878","#2a2214"],"luz2":"255,245,220","props":[{"tipo":"papel","x":540,"y":1760,"s":1.25,"titulo":"INVOICE · 1971","dato":"17 HOURS x $2 = $35","sello":"PAID","selloc":"verde","filaDato":5}]},
  {"k":"s_4","z":"nocheV","o":{"ciudad":True,"sem":21},"actores":[{**D,"keys":[{"k":"s_4","x":420,"pose":"piensa","cara":"sorpresa"}]}]},
  {"k":"s_5","i":["#2a1d55","#120b2c","#030108"],"luz2":"255,215,140","pedestal":True,"props":[{"tipo":"anillo","x":540,"y":1300,"s":1.6}]},
  {"k":"s_6","z":"corporativoV","o":{"ticker":"SHARES ▲"},"actores":[{**K,"keys":[{"k":"s_6","x":360,"pose":"explica","cara":"feliz"}]},{**D,"keys":[{"k":"s_6","x":760,"pose":"aplaude","cara":"risa"}]}]}],
 numeros=[{"k":"m35","n":35,"pre":"$","c":"verde","etq":"FOR THE LOGO","fin":"s_4"},{"k":"m500","n":500,"c":"amar","etq":"SHARES OF STOCK","fin":"s_6"}],
 emojis=[{"k":"peanuts","e":"🥜","y":640},{"k":"never","e":"🤫"},{"k":"price","e":"💡","dur":1.2}],
 gancho2=4,cierre="FAIR OR NOT?",cierre2="Tell me. Comment",paises=["FAIR","NOT FAIR"],
 nota="1971: Carolyn Davidson, estudiante de diseño en Portland State University (Oregon), diseñó el logo para Phil Knight; cobró US$2 por hora, ~17,5 horas = US$35. 1983 (12 años después): Nike le regaló un anillo de oro con el logo y un diamante, y 500 acciones. No se dibuja el logo real (marca registrada). Disparador: pérdida/injusticia. Gancho tipo 7.",
 fuentes=["https://en.wikipedia.org/wiki/Swoosh","https://about.nike.com/","https://www.cnbc.com/"])
