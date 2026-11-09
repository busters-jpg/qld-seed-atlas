# QLD Native Seed Atlas

Interactive satellite map of photo-backed occurrence records for commercially useful Queensland native seed species. One static file (`index.html`), no backend.

## Data

- **GBIF** (default): research-grade iNaturalist observations plus imaged herbarium specimens (Queensland Herbarium and others), filtered to a Queensland polygon. Name matching via the GBIF backbone (synonyms resolved).
- **ALA** (optional, Filters → Data provider): adds unconfirmed iNaturalist sightings. Switch providers before loading a species.

Points are sightings, not confirmed stands. Verify by drone and on the ground before harvesting, and check Nature Conservation (Plants) Regulation licensing and landholder consent per tenure. Photos carry their own licences (mostly CC BY-NC); open the record before reusing one.

## Use

- Tick species in the Species tab (or "Load tier A grasses"). Add any species by scientific name.
- Filters: year, month photographed (phenology proxy), record type, coordinate uncertainty, radius from a tapped point or your location, load cap.
- Results: month histogram, top hotspot cells (10 km), per-species sparklines, CSV / GeoJSON export (opens in QGIS).
- iPhone: open in Safari → Share → Add to Home Screen.

## Edit the species list

`src/species.js` → run `./build.sh` → commit `index.html`.
