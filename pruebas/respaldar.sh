#!/bin/bash
# E0 · arma el respaldo fechado del entorno: bundle git (código, datos, documentos, con toda la historia y etiquetas)
# + videos de referencia. Los dos van en partes de 20 MB para poder copiarlos al Mac. Sumas sha256 + instrucciones.
# Uso: respaldar.sh ETIQUETA   →   /home/claude/.respaldos/<fecha>_ETIQUETA/
set -e
ET=${1:?etiqueta}; F=$(date +%Y-%m-%d); N="${F}_${ET}"; O=/home/claude/.respaldos/$N; A=/home/claude/.respaldos/_armado_$N
rm -rf $O $A; mkdir -p $O $A; cd /home/claude
git bundle create $A/motor_$N.bundle --all 2>/dev/null
git bundle verify $A/motor_$N.bundle > /dev/null 2>&1 && echo "bundle verificado"
tar -C /home/claude/pruebas -cf $A/referencias_video_$N.tar referencias_video
tar -C /mnt/user-data/outputs -cf $O/estandar-produccion_$N.tar estandar-produccion   # copia de los documentos del estándar
( cd $A && sha256sum motor_$N.bundle referencias_video_$N.tar ) > $O/SHA256_completos.txt
split -b 20m -d -a 2 $A/motor_$N.bundle $O/motor_$N.bundle.part-
split -b 20m -d -a 2 $A/referencias_video_$N.tar $O/referencias_video_$N.tar.part-
rm -rf $A
cp pruebas/entorno.txt pruebas/comprobar_respaldo.sh $O/
HEAD=$(git rev-parse HEAD); TAGS=$(git tag --points-at HEAD | tr '\n' ' ')
MOTOR=$(sha256sum escena/escena.html | cut -d' ' -f1)
echo "$HEAD" > $O/COMMIT.txt; echo "$MOTOR  escena/escena.html" > $O/MOTOR_SHA256.txt
cat > $O/LEEME_recuperacion.md <<EOT
# Respaldo del motor · $N
- **Fecha:** $(date '+%Y-%m-%d %H:%M %Z')
- **Commit:** \`$HEAD\` · etiquetas: \`$TAGS\`
- **Motor de referencia** (\`escena/escena.html\`): sha256 \`$MOTOR\`
- **Contenido:** el bundle git (código, datos, corpus, líneas base e informes, con su historia) y los videos de referencia, los dos en partes de 20 MB, más una copia de los documentos del estándar tal como estaban al respaldar (\`estandar-produccion_$N.tar\`).

## Comprobar (en cualquier Linux o Mac con git)
\`\`\`bash
bash comprobar_respaldo.sh        # partes, armado, clon, commit, motor y los 11 videos contra el manifiesto
\`\`\`

## Recuperar a mano
\`\`\`bash
sha256sum -c SHA256SUMS                                        # 1 · las partes están íntegras
cat motor_$N.bundle.part-* > motor_$N.bundle                   # 2 · rearmar el bundle y el tar
cat referencias_video_$N.tar.part-* > referencias_video_$N.tar
sha256sum -c SHA256_completos.txt
git clone motor_$N.bundle fabrica                              # 3 · código, datos y documentos, con su historia
git -C fabrica checkout $HEAD
tar -xf referencias_video_$N.tar -C fabrica/pruebas/           # 4 · videos de referencia
\`\`\`
- En un Mac sin \`sha256sum\`: \`shasum -a 256 -c SHA256SUMS\`.
- Las versiones de las herramientas están en \`entorno.txt\`. El modelo de voz (Kokoro) está en \`~/gta-shorts/models\` del Mac.
- Comprobar que el motor recuperado renderiza igual (en el contenedor, con Chrome):
  \`cd fabrica/pruebas && python3 regresion.py --nivel rapido --motor ../escena/escena.html --base lineas_base/rapido_motor_725e0dba.json\`
EOT
cd $O; sha256sum motor_$N.bundle.part-* referencias_video_$N.tar.part-* estandar-produccion_$N.tar entorno.txt comprobar_respaldo.sh \
  LEEME_recuperacion.md COMMIT.txt MOTOR_SHA256.txt SHA256_completos.txt > SHA256SUMS
ls -la $O; du -sh $O
