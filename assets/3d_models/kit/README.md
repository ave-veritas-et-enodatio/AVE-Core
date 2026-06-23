# Vacuum lattice DIY kit — print exports

Bed-ready, print-validated STLs for the Axiom-1 **diamond production K4** friction-fit
kit (Vol. 9 Ch. 18). Every part reloads **watertight + `is_volume=True`**, and the
bond↔socket joint carries a real **0.10 mm diametral** press-fit interference.

> **Epistemic class — unchanged.** This is an **identity-class consistency** model of
> the K4 graph topology plus a `[RENDERING]` absolute scale (`consistency-vs-emergence`
> v1.3). **A printed model asserts no new physics.** It renders the adjudicated
> *diamond-primary / achiral-cold* reading and nothing beyond it.

> **Status — REBUILT (validated 2026-06-21).** The legacy work-in-progress limitations
> are **RESOLVED**: the node STLs are no longer non-manifold (the boolean-CSG export
> now writes the welded trimesh directly instead of round-tripping through numpy-stl),
> and the press-fit is no longer 0 mm. Treat these files as print-ready.

---

## 1. The representation principle (read this first)

A 3D print is a **real-space object**, so the kit is scrupulous about *which*
coordinate system each feature stands for:

| Quantity | Coordinate system | How the print shows it |
|---|---|---|
| Nodes, bonds, 4 tetrahedral ports, √3·ℓ_node pitch | **real space** | **isomorphic** — the printed skeleton (degree-4 diamond net) |
| The 7-mode DOF basis (E / B / V stores) | real-space *directions* at each node | **snap-on color accents** (triad / rings / breathing) |
| LC-tank saturation state, (V_inc, V_ref) phasor, impedance plane | **phase space** | **labeled proxy only** — disc + dial, never a printed length |

**A/B is the bipartite SUBLATTICE label — not a storage split.** The legacy
cube-vs-sphere bodies encoded a denied "A stores E / B stores B" asymmetry. That is
fixed: **the A and B node bodies are an identical solid node** (same degree-4 coordination
shell, 4 tetrahedral round bond sockets — round so a rigid bond seats clean at any rotation, both ends). A vs B is shown only by **two node colors + an
embossed A/B key**, which is all the sublattice legitimately marks.

**The 7-mode store split.** Every node is the same full LC oscillator carrying all
stores, shown by snap-on accents:

- `accent_triad_E` — 3 translational DOF → **E** (dielectric displacement) → **ε² store**
- `accent_rings_B` — 3 micro-rotational DOF → **B** (inductive flywheel / spin) → **κ² store**
- `accent_breathing_V` — the A1 volumetric breathing → **V² store = MASS**

That is the Pythagorean store split **A² = ε² + κ² + V²** (6 spatial DOF + 1 A1
breathing). **A1 ⊥ T2**: the breathing axis is kept independent of the rotation rings
— mass and charge/spin never share one (V_inc, V_ref) phasor.

**Phase space is never a printed length.** The impedance disc + phasor dial are stamped
**`[STATE-SPACE — NOT A COORDINATE]`**. The saturation amplitude **A is the LC-tank
STATE**, not a spatial DOF — it lives only on the disc/dial, never as a node-body feature.

---

## 2. Start here — the hero unit cell

Print the **tetrahedral unit cell** first (the degree-4 coordination shell, ~9 parts):

> **1× `vacuum_node_A` + 4× `vacuum_node_B` + 4× `vacuum_bond` + accents + `jig_unit_cell`**

It shows z = 4 coordination, A/B bipartiteness, and the tetrahedral port geometry in a
single small build. Once it seats cleanly, step up to the full **L = 4** chunk
(`vacuum_assembly_L4.json`: 8× node_A + 8× node_B + 14× bonds, 16 nodes). For the full
crystal regenerate with `ASSEMBLY_L=16`.

---

## 3. BOM tiers (print one color per part; assign colors per tier)

The kit is **single-color prints + snap/glue-on color accents** — one filament per part,
no multi-material, no mid-print swaps (ideal for the single-extruder MK3+). Visual
differentiation comes from small accent parts that snap or glue onto a monochrome base.

| Tier | Parts | Color strategy |
|---|---|---|
| **Structural base** (monochrome) | `vacuum_node_A.stl`, `vacuum_node_B.stl`, `vacuum_bond.stl` | one neutral filament; **A vs B = two node colors** |
| **DOF accents** (color per store) | `accent_triad_E.stl` (E/ε²), `accent_rings_B.stl` (B/κ²), `accent_breathing_V.stl` (V²/mass), `key_A.stl`, `key_B.stl` | one distinct color **per store**; A/B key matches the node colors |
| **Phase space** (state-space proxy) | `phase_impedance_disc.stl`, `phase_dial_body.stl` + `phase_dial_pointer.stl`, `phase_dial2_body.stl` + `phase_dial2_pointer.stl` | a contrasting "instrument" color; pointers stand out (two dials = A1 ⊥ T2) |
| **Chiral srs instrument** | `srs_node_right.stl`, `srs_node_left.stl`, `srs_bond.stl`, `srs_handedness_right.stl`, `srs_handedness_left.stl` | a clearly *different* color family — kept visually distinct from the production diamond |
| **Assembly jig** | `jig_unit_cell.stl`, `jig_tile_<row>_<col>.stl` (2×2 tiling) | one base color |
| **Reference only** | `reference_tetra_unit_cell.stl`, `scale_plate.stl` | any; the scale plate embosses the magnification label |

---

## 4. The chiral srs companion

A small **degree-3 acceptance INSTRUMENT** ships alongside the production diamond net,
in **both enantiomorphs** — `srs_node_right` (I4₁32) and `srs_node_left` (I4₃32) — each
with a handedness glyph. It is **explicitly distinct** from the production diamond and
carries the optical-activity / charge / chirality story. Keep the two pieces separate:
the diamond net is the production substrate; the srs piece is the diagnostic instrument.

**On the "K4" overload:** the substrate the kit prints is honestly labeled the
**diamond production K4 (`build_diamond_net`)** — the degree-4 achiral Fd-3m net on which
all production drivers run. The srs piece is labeled the **degree-3 instrument**. The
name "K4" is a documented overload (engine degree-4 diamond vs Sunada degree-3 srs); the
kit does not blur them.

---

## 5. The jig + how it assembles (press-fit to locate, glue to secure)

**Joinery is round and clocking-free.** Bond tips and node bond-sockets are round
cylinders, so a rigid bond seats at *any* rotation in *both* end sockets (a hex tip can't
face-flush two independently-clocked sockets at once). The press-fit only **locates**;
grip is light by design — **glue secures** the joint.

**Base plate (bottom layer).** A keyed baseplate tiles the placement to the **250 × 210 mm
bed** (`jig_tile_<row>_<col>`, plus `jig_unit_cell` for the hero print). Each pocket embosses
the **node id + A/B label**; per-port **pips** show which port mates which neighbor (the
`nodes[].ports` map in the manifest). No guessing which of the four identical ports goes where.

**Standoff posts (upper layers — the stepped tier).** The lattice has nodes at several Z
levels; the base plate only holds the bottom one. Print the graded-height
`standoff_post_z<n>_h<H>mm` posts: each holds an upper node at its true Z while you glue its
bonds and the glue cures. Build **bottom-up** — locate bottom layer, prop the next node on
its standoff, press+glue its bonds, cure, move up.

**Closing a ring.** A loop-completing bond goes between two already-placed nodes, so you
can't press a rigid bond into it (no axial room). Use that bond as a **slip fit and glue
it** — the loop closes without forcing. (The L4 starter is two trees, so it has no rings;
this matters for larger, ring-bearing chunks.)

**Tall builds.** At the 100 mm default the top standoff exceeds the bed Z (~300 mm); rebuild
at `KIT_PRINT_MM_PER_L_NODE=60` for a jig-assisted full assembly (Z span ~180 mm, all posts
print).

---

## 6. Scale

| | |
|---|---|
| Default print scale | **100 mm / ℓ_node** |
| Magnification vs physical | **× 2.59 × 10¹¹** |
| ℓ_node | **386 fm — DEFINITIONAL** (electron reduced-Compton length, ℏ/m_e c) |
| Corpus mnemonic 38.6 mm | **reference only** — not the print scale |

`scale_plate.stl` embosses a 1-ℓ_node scale bar, the print-medium equivalent of the
`[RENDERING]` tag. Override the scale with `KIT_PRINT_MM_PER_L_NODE` (e.g. `=60` for a
smaller build).

---

## 7. Prusa i3 MK3+ slicer hints

| Setting | Value |
|---|---|
| Nozzle | 0.4 mm |
| Layer height | 0.20 mm |
| Perimeters | 3 |
| Infill | 20 % |
| Supports | **none** — every part is posed flat / solid (the bond prints horizontal) |
| Elephant-foot compensation | 0.15 mm (protects the mating-collar fit) |
| Filament | one color per part; assign accent colors per BOM tier |

Bed 250 × 210 × 210 mm; PLA/PETG; single extruder (no soluble support). Tune the joint
with `KIT_FRICTION_INTERFERENCE_MM` (per-side mm; default 0.05 → 0.10 mm diametral; try
0.03–0.08) if the fit is loose or tight.

---

## 8. Assembly steps

1. Print the jig tiles; assemble the baseplate (snap/glue tile edges). For the hero
   build use `jig_unit_cell` instead.
2. Print `node_A` × `counts.node_A` and `node_B` × `counts.node_B` in **two colors**.
3. Drop each node into its keyed jig pocket (the pocket emboss = node id + A/B).
4. Press bonds into the sockets; the pocket **port pips** show which port → which
   neighbor (manifest `nodes[].ports`).
5. *(Optional)* Snap on the DOF accents (`triad_E` / `rings_B` / `breathing_V`) + the
   A/B key, colored per store.
6. *(Optional)* Set the phasor dial / read the impedance disc as the **LC-tank STATE**
   (not a position).
7. Tune the press-fit via `KIT_FRICTION_INTERFERENCE_MM` if loose or tight.

---

## 9. Regenerate

The STL artifacts are **generated and gitignored** — the generator is the source of
truth. Regenerate the full kit + manifest with:

```bash
PYTHONPATH=src python src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py
```

Useful environment knobs:

```bash
# full crystal instead of the L=4 starter chunk
ASSEMBLY_L=16 PYTHONPATH=src python src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py

# smaller print scale (mm per ℓ_node)
KIT_PRINT_MM_PER_L_NODE=60 ASSEMBLY_L=4 PYTHONPATH=src python src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py

# tune the friction fit (per-side mm)
KIT_FRICTION_INTERFERENCE_MM=0.06 PYTHONPATH=src python src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py
```

Requires `trimesh` + `manifold3d`. The build re-emits `vacuum_assembly_L{L}.json` (the
node positions, port→neighbor map, BOM tiers, joinery, slicer hints, and per-part QC).

---

## 10. Open seams the print does NOT touch (Grant-gated physics)

The kit follows the adjudicated reading and asserts nothing beyond it:

- **Chirality realization** — achiral diamond + excited k_χ vs natively chiral. The
  production net is printed achiral; chirality is the srs instrument's story.
- **Crystalline vs amorphous** — the print is the degree-4 crystalline graph; it does
  not imply z_eff / z₀.
- **Proton multi-node vs nucleus-in-single-node** — untouched.

The print shows the production diamond's connectivity, the 7-mode store basis, and a
labeled phase-space proxy — and stops there.
