# Vacuum-lattice DIY print kit — v1 (Prusa i3 MK3+)

Print-ready, watertight STLs for the rebuilt Axiom-1 vacuum-lattice kit (Vol 9 Ch 18).
Artifact: `vacuum-lattice-kit-v1-100mm-L4.zip` — 26 STLs + manifest + README (2.70 MB),
regenerated through the gating QC. STLs are generated, not committed; this is the
downloadable bundle. Generators (`src/scripts/vol_1_foundations/`) are the source of truth.

## Validated (live-fire, on merged main)

- All 25 gated parts reload `watertight = is_volume = True` (direct trimesh export; the
  legacy numpy-stl round-trip non-manifold bug is fixed).
- As-built press-fit: **round** bond tip Ø7.30 into a **round** node bore Ø7.20 = **0.10 mm
  diametral** interference, seated into a 7 mm bore. Round joinery is rotation-symmetric, so a
  rigid bond seats clean in both end sockets at any clocking (`verify_kit_assembly.py`: 8/8 PASS,
  incl. clocking-free rotation-invariance).
- DFM rebuild rows all PASS at the shipped 100 mm/ℓ_node scale (`kit_dfm_check.py`).

## What's in it

- Structural base (degree-4 diamond, identical A/B node body): `vacuum_node_A/B`,
  `vacuum_bond` (helix groove, prints horizontal).
- DOF accents (snap-on, one color per store): `accent_triad_E` (E / ε²),
  `accent_rings_B` (B / κ²), `accent_breathing_V` (A1 / mass / V²), `key_A/B`.
  The 7-mode store split A² = ε² + κ² + V²; A1 ⊥ T2.
- Phase space `[STATE-SPACE — NOT A COORDINATE]`: `phase_impedance_disc`, `phase_dial*`.
- Chiral srs acceptance instrument (degree-3, both enantiomorphs): `srs_node_right/left`,
  `srs_bond`, `srs_handedness_*` — kept distinct from the production diamond.
- Keyed base jig: `jig_unit_cell`, `jig_tile_<row>_<col>` (forces node placement +
  port→neighbor; map in the manifest `nodes[].ports`).
- `scale_plate` + `vacuum_assembly_L4.json` (BOM tiers, joinery, port map).

## Print (Prusa i3 MK3+)

0.4 mm nozzle · 0.20 mm layer · 3 perimeters · 20 % infill · **no supports** (every part
posed flat / solid; the bond prints horizontal) · 0.15 mm elephant-foot compensation ·
one color per part. **Start with the hero unit cell** (~9 parts: 1× node_A + 4× node_B +
4× bond + accents + `jig_unit_cell`). Tune the joint with `KIT_FRICTION_INTERFERENCE_MM`.

## Reproduce / re-scale

```
PYTHONPATH=src python src/scripts/vol_1_foundations/package_kit_release.py
KIT_PRINT_MM_PER_L_NODE=60 PYTHONPATH=src python src/scripts/vol_1_foundations/package_kit_release.py
```

## Scope

Identity-class topology model + `[RENDERING]` absolute scale (magnification ≈ 2.6×10¹¹;
ℓ_node = 386 fm is definitional). A printed model asserts no new physics; it renders the
adjudicated diamond-primary / achiral-cold reading and nothing beyond it.
