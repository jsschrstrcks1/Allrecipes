# milk-substitution.json — provenance and authority (UL-058 resolution)

**Soli Deo Gloria.** Recorded 2026-07-29 (household task `recipes-milk-substitution-dedupe`).

## The verdict

| Copy | Version | Milk types | Status |
|---|---|---|---|
| `Grandmasrecipes/data/milk-substitution.json` | **1.1.0** (2026-01-22) | 11 (cow…yak, donkey, reindeer) | **AUTHORITATIVE** |
| Atlas `recipe-tool-data/milk-substitution.json` | 1.1.0 | 11 | byte-identical mirror of the SSOT |
| `Allrecipes/data/milk-substitution.json` (this repo) | 1.0.0 (2026-01-17) | 3 (cow, goat, sheep) | reduced subset — see below |

Verified mechanically, not assumed: on every shared milk type the two files are
**content-identical** once v1.1.0's added `available` flag is set aside; the
rennet factor table is extended in v1.1.0 (8 exotic milks added), not changed
(cow 1.0, goat 0.625, sheep 0.65 agree everywhere); temperature and calcium
guidance are identical. **There is no data conflict** — this repo's copy is
older and smaller, not wrong.

## Why this repo is NOT being synced to v1.1.0 (yet)

This repo's `milk-substitution.js` (502 lines, vs the SSOT repo's 1,688) has
**no `available`-flag filtering** — it offers `Object.keys(milk_types)` as
substitution options directly. Dropping the v1.1.0 file in as-is would present
donkey, camel, and reindeer milk as everyday substitution choices in this
site's UI. Syncing the data therefore requires porting the availability logic
first; that pairing is registered on the household ledger as its own candidate
rather than done as a blind copy.

## The rules this record establishes

1. **Edit milk knowledge in Grandmasrecipes first.** Its `data/milk-substitution.json`
   is the SSOT; Atlas mirrors it byte-for-byte.
2. **Never edit this repo's copy independently.** Either sync from the SSOT
   (together with the `available` filtering port) or leave it as the frozen
   v1.0.0 subset it is.
3. A future sync must bump this file's table and delete the "not yet" section.
