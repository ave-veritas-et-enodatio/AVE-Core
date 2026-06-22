# Representative + printable vacuum-lattice kit (Prusa i3 MK3+) — design + prereg

**Status:** DRAFT / skeleton (sections marked ⏳ are gated on the in-flight audit workflow `w7qwv0e6g`).
**Branch:** `analysis/2026-06-21-vacuum-cell-print`
**Owner:** orchestration→implementor session, 2026-06-21
**Epistemic class:** identity-class consistency on K4 graph topology + `[RENDERING]` absolute scale (Vol 9 Ch 18; `consistency-vs-emergence` v1.3). No new substrate-physics claim is asserted by a printed model.

---

## 1. Goal

Upgrade the Vol 9 Ch 18 DIY vacuum-lattice kit from a *topology preview* into a model that is simultaneously:
1. **Highly representative** of the canonical vacuum cell — its real-space K4 topology AND the Cosserat 6-DOF (translational vs micro-rotational) structure AND, by labeled proxy, the phase-space (LC tank) state;
2. **Printable** on a Prusa i3 MK3+ (FDM, 0.4 mm nozzle, 250×210×210 mm, single extruder → no soluble support);
3. **Assemblable** with a friction-fit that actually mates (current kit has 0 mm interference → does not mate).

## 2. The governing representation principle (Grant-approved 2026-06-21)

A 3D print is a **real-space object**. Therefore:

| Quantity | Coordinate system | Representation in the print |
|---|---|---|
| Node positions, bonds, 4 tetrahedral ports | **real space** | **isomorphic** — the printed skeleton |
| Translational vs micro-rotational DOF basis | real-space *directions* at each node | **oriented markers** — triad (E) + 3 rings (B) |
| LC tank state, (V_inc, V_ref) phasor / impedance plane | **phase space** | **labeled proxy only** — never a spatial length |

Hard fence (`09_mechanical_characteristics.tex:86`): **A1 ⊥ T2** — mass (A1 dilatation) and charge/spin (Cosserat micro-rotation) grades are orthogonal and **never share one (V_inc, V_ref) phasor**. Any phase-state indicator is therefore *two independent orthogonal* indicators, never one merged dial.

Design rule (from `phase-space-coordinate-check`): no real-space length in the print may stand for a phase-space quantity without an explicit `[STATE-SPACE — NOT A COORDINATE]` tag (the physical analog of the existing `[RENDERING]` scale tag).

## 3. What gets built (all of it, per Grant 2026-06-21)

1. **Per-node DOF markers — triad + 3 rings, identical on EVERY node.**
   - 3-axis orthogonal triad (stubs/grooves) = 3 translational DOF → E / capacitor / dielectric displacement (`09:207`).
   - 3 orthogonal rings/loops = 3 micro-rotational DOF → B / inductive flywheel / spin (`09:208`, `09:22`).
   - **Fixes the A/B-mnemonic bug**: today A=solid cube (reads capacitive-only), B=sphere+ring (reads inductive-only) — a misleading shape the docs already flag (`18_experimental_prints.tex:70`). New scheme: every node shows BOTH stores; A/B distinguished only by an orientation/topology key (port sign + color/label), not a fake storage asymmetry. Generalizes the existing `_inductive_ring` idiom (`vacuum_lc_geometry.py:596`).
2. **Bond couple-stress helix groove** — helical groove along the bond, twist ∝ phase advance along the TL / couple-stress γ_c gradient, handedness = chirality. Reuses `_micropolar_helix_curve` / `twist_turns` (`generate_axiom1_lattice_showpiece_stl.py:88,146`).
3. **Companion impedance-plane disc** — separate printed Smith/Lissajous puck, stamped `[STATE-SPACE — NOT A COORDINATE]`, sits beside the lattice. Keeps the two coordinate systems physically separate (Vol 4 circuit-theory ch1 phasor/Smith leaves).
4. **Per-node phasor dial (deluxe)** — optional movable pointer(s) per node; phase = literal angle; lets a user dial a propagating mode / standing wave. Two orthogonal dials per A1⊥T2.
5. **Chiral srs companion piece (Grant 2026-06-21).** A small `build_srs_net` chunk (degree-3, 120° bonds, both enantiomorphs `right`=I4₁32 / `left`=I4₃32) shipped ALONGSIDE the production diamond kit — the *instrument* substrate that carries the optical-activity / charge / chirality story (Vol 9 Ch 11 chirality sector). Must be clearly labeled "acceptance instrument, NOT the production engine net" (`18_experimental_prints.tex:34`) so the two are never conflated. Reuses the existing srs network generator (`generate_vacuum_lattice_stl.py` `build_srs_net`), kit-ified into a degree-3 node + 120° bond.

### 3.1 Color / material architecture (Grant 2026-06-21)

**Single-color prints + snap/glue-on color accent parts.** Every printed part is monochrome — one filament per part, no multi-material, no mid-print filament swaps (ideal for the single-extruder MK3+). Visual differentiation is delivered by **separate, small color-accent parts** that snap (friction peg) or glue onto the monochrome base:

| Tier | Parts | Color |
|---|---|---|
| **Structural base** (each monochrome) | diamond node body, srs node body, bonds, impedance disc, dial body | one filament each |
| **Color accents** (separate snap/glue parts) | translational triad (E-color), micro-rotation rings (B-color), A/B sublattice key cap, srs handedness marker, dial pointer | distinct filament per accent type |

Implication: the DOF markers and keys are **printed as separate parts with their own friction pegs / glue pads**, not fused to the node body. This keeps every base print simple + monochrome + watertight, and lets a builder color-code E vs B vs sublattice without a multi-material printer. Accent parts must clear the FDM min-feature floor (~0.8–1.0 mm) at the chosen scale; the 100 mm/ℓ_node default gives headroom.

## 4. Canonical facts the geometry must honor ⏳ (audit-grounded — fill from workflow `w7qwv0e6g`)

- [ ] Production substrate = `build_diamond_net` (degree-4 diamond, achiral Fd-3m); instrument = `build_srs_net` (degree-3 srs, chiral I4₁32/I4₃32). Confirm "K4" naming convention + flag any latent K4-complete-graph vs diamond-net conflation.
- [ ] 6-DOF-per-node, every node a full LC oscillator; A/B = bipartite sublattice not DOF split (verbatim cites).
- [ ] `_DIAMOND_PORTS` 4 tetrahedral directions; A=+ports, B=−ports; bond = TL between port mouths; pitch = √3·ℓ_node.
- [ ] ℓ_node = L_NODE = ħ/(m_e c) provenance; the THREE coordination numbers (degree-4 / z_eff≈6 / z₀≈51.25) disambiguated so the print doesn't imply the wrong one.
- [ ] Vol 9 datasheet self-consistency findings; KB-leaf source-of-truth + existing open items.

## 5. Audit findings being remediated ⏳ (fill from workflow)

- [ ] **Watertight/manifold**: node A & B reload non-manifold; bond reloads is_volume=False. Root cause + fix (export path).
- [ ] **Press-fit 0 mm**: `KIT_BOND_RADIUS = KIT_SOCKET_RADIUS` (`vacuum_lc_geometry.py:55`). Corrected sizing + single interference source.
- [ ] **Printability**: overhang angles in print poses, min feature vs 0.4 mm nozzle, stem-inboard geometry sanity, build-volume.
- [ ] **Code quality**: dead/legacy paths, env-var scale ordering, reported-vs-actual geometry mismatches.
- [ ] Completeness-critic items.

## 6. Prusa i3 MK3+ constraints (hard)

Bed 250×210×210 mm; 0.4 mm nozzle; PLA/PETG; single extruder ⇒ no soluble support; unsupported overhang ≤ ~55°; reliable bridge a few mm; min robust feature ~0.8–1.0 mm; watch elephant-foot on collars, warp on large flat faces, seam on sphere.

## 7. Implementation sequence

1. Design doc (this) — commit #1, open draft PR.
2. DOF markers module + A/B mnemonic fix (Task #6).
3. Bond helix + phase-space companions (Task #7).
4. Watertight + press-fit + printability pass (Task #8); live-fire regenerate, on-disk QC must be green.
5. Vol 9 docs lockstep (KB leaf → ch18.tex → kit README) + figures (Task #9).
6. Validate; push; PR ready-for-review.

## 8. Decisions (RESOLVED — Grant 2026-06-21)

- **Chiral srs piece: INCLUDE.** Ship a small chiral srs companion alongside the production diamond kit (§3 item 5). Both enantiomorphs; labeled as acceptance instrument.
- **Color/material: single-color prints + snap/glue-on color accent parts (§3.1).** No multi-material, no mid-print swaps. Every base part monochrome; color lives in separate accent parts.

---
*Skill plan: `.agents/handoffs/2026-06-21_vacuum-cell-print_skill-plan.md`. Prereg corpus-inventory = audit workflow `w7qwv0e6g`.*
