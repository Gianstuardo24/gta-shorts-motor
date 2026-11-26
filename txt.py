"""uso: python3 txt.py salida.txt 'Dom 22/11 14:00' 'TÍTULO' 'desc' 'firma' '#tags' ['relacionado']"""
import sys
o,pub,tit,desc,firma,tags=sys.argv[1:7]; rel=sys.argv[7] if len(sys.argv)>7 else ''
s=f"PUBLICAR: {pub} (hora de Chile)\n\nTÍTULO:\n{tit}\n\nDESCRIPCIÓN:\n{desc}\n\n{firma}\n\n{tags}\n"
# sin VIDEO RELACIONADO: Tao copia la descripcion completa (22-nov)
open(o,'w').write(s); print(s)
