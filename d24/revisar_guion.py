#!/usr/bin/env python3
"""Revisa guiones de Shorts contra el doc 25 (motor de guiones).
Uso: python3 revisar_guion.py GUIONES.md
Formato: bloques '## Canal HH · TÍTULO' + líneas numeradas; 'G2:' marca el segundo gancho y 'CTA:' el cierre.
"""
import re, sys

EMOJI = re.compile(r'[\U0001F300-\U0001FAFF☀-➿⭐⭕]')

def revisar(head, L):
    avisos = []
    titulo = head.split('·', 1)[1].strip() if '·' in head else head
    if len(titulo) > 46: avisos.append(f'título largo ({len(titulo)} > 46)')
    if not any(w.isupper() and len(w) > 1 and w.isalpha() for w in re.findall(r"[\wÁÉÍÓÚÑ']+", titulo)):
        avisos.append('título sin palabra en MAYÚSCULAS')
    ne = len(EMOJI.findall(titulo))
    if not 1 <= ne <= 3: avisos.append(f'título con {ne} emojis (1–3)')
    gs = [i for i, l in enumerate(L) if l.startswith('G2')]
    if not gs: return avisos + ['falta segundo gancho (G2:)']
    g = gs[0]; pos = g / (len(L) - 1)
    if not 0.40 <= pos <= 0.70: avisos.append(f'segundo gancho en {pos:.0%} (40–70 %)')
    tras = len(L) - g - 2
    if tras < 2: avisos.append(f'solo {tras} línea(s) después del segundo gancho (mín. 2)')
    frases = len(re.findall(r'[.!…]+(?=\s|$)', L[0]))
    if frases < 2: avisos.append(f'gancho con {frases} frase(s) (mín. 2; ideal 3: eco + fricción + anticipación)')
    for i, l in enumerate(L):
        if '?' in l: avisos.append(f'línea {i+1}: pregunta con "?" en la voz')
        for f in re.split(r'(?<=[.!…:])\s+', re.sub(r'^(G2|CTA):\s*', '', l)):
            n = len(f.split())
            if n > 24: avisos.append(f'línea {i+1}: frase de {n} palabras (subtítulos de 2 líneas, máx. ~24)')
    if not re.match(r'CTA:\s*(Tell me|Comenta)', L[-1]): avisos.append('CTA no empieza con "Tell me…"/"Comenta…"')
    if not re.search(r'Follow|Sigue', L[-1]): avisos.append('CTA sin "Follow/Sigue"')
    if not re.search(r'\b(1[89]|20)\d{2}\b', ' '.join(L[1:4])): avisos.append('sugerencia: sin ancla de año/fecha en las líneas 2–4')
    if not re.match(r'(So |Lesson|O sea|Así|Por eso|Pero a|Esto)', L[-2]): avisos.append('sugerencia: la penúltima línea no es conclusión (So…/Lesson:)')
    total = sum(len(re.sub(r'^(G2|CTA):\s*', '', l).split()) for l in L)
    if not 120 <= total <= 215: avisos.append(f'{total} palabras (120–215)')
    return avisos

def main(p):
    t = open(p, encoding='utf-8').read()
    ok = 0; n = 0
    for b in re.split(r'\n## ', '\n' + t)[1:]:
        head, *lines = b.strip().split('\n')
        L = [re.sub(r'^\d+\.\s*', '', l).strip() for l in lines if re.match(r'^\d+\.', l)]
        if not L: continue
        n += 1; a = revisar(head, L)
        print(('✅ ' if not a else '⚠️ ') + head)
        for x in a: print('   -', x)
        ok += not a
    print(f'\n{ok}/{n} sin avisos')

if __name__ == '__main__':
    main(sys.argv[1])
