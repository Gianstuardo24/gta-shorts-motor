"""Reemplaza en escena.html el bloque entre los marcadores P27 por el contenido de p27_bloque.js"""
import re
p='/home/claude/escena/escena.html';s=open(p,newline='').read();b=open('/home/claude/prueba27/p27_bloque.js',newline='').read()
i=s.index('// ===== P27 · INICIO');j=s.index('// ===== P27 · FIN =====')+len('// ===== P27 · FIN =====\n')
s=s[:i]+b+s[j:];open(p,'w',newline='').write(s);print('bloque instalado',len(b))
