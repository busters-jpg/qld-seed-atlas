#!/usr/bin/env bash
# Rebuild index.html from src/ (edit src/species.js to change the species list).
set -euo pipefail
cd "$(dirname "$0")"
LIBS=.libs
if [ ! -d "$LIBS/leaflet-1.9.4" ]; then
  mkdir -p "$LIBS" && cd "$LIBS"
  npm pack leaflet@1.9.4 leaflet.markercluster@1.5.3 --silent
  for f in *.tgz; do mkdir -p "${f%.tgz}" && tar -xzf "$f" -C "${f%.tgz}"; done
  cd ..
fi
python3 src/build.py "$LIBS" index.html
