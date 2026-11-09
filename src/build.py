#!/usr/bin/env python3
"""Assemble the single-file atlas: inline Leaflet, marker cluster and the species list."""
import pathlib, re, sys

SRC = pathlib.Path(__file__).resolve().parent
LIBS = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else SRC
OUT = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else SRC.parent / "qld-native-seed-atlas.html"

def read(p):
    return pathlib.Path(p).read_text(encoding="utf-8")

def js(p):
    s = read(p)
    s = re.sub(r"^//# sourceMappingURL=.*$", "", s, flags=re.M)
    if "</script" in s.lower():
        s = re.sub(r"</script", "<\\/script", s, flags=re.I)
    return s.strip()

tpl = read(SRC / "template.html")
parts = {
    "/*__LEAFLET_CSS__*/": read(LIBS / "leaflet-1.9.4/package/dist/leaflet.css"),
    "/*__CLUSTER_CSS__*/": read(LIBS / "leaflet.markercluster-1.5.3/package/dist/MarkerCluster.css")
                           + "\n" + read(LIBS / "leaflet.markercluster-1.5.3/package/dist/MarkerCluster.Default.css"),
    "/*__LEAFLET_JS__*/": js(LIBS / "leaflet-1.9.4/package/dist/leaflet.js"),
    "/*__CLUSTER_JS__*/": js(LIBS / "leaflet.markercluster-1.5.3/package/dist/leaflet.markercluster.js"),
    "/*__SPECIES_JS__*/": js(SRC / "species.js"),
}
for k, v in parts.items():
    assert k in tpl, k
    tpl = tpl.replace(k, v)
OUT.write_text(tpl, encoding="utf-8")
print(OUT, f"{OUT.stat().st_size/1024:.0f} KB")
