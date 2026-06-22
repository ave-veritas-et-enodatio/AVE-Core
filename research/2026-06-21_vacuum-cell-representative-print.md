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

1. **Per-node mode markers — triad + 3 rings + breathing core, identical on EVERY node.** *(Upgraded from 6→7 modes per audit: the node carries 6 spatial DOF PLUS the A1 volumetric breathing = the mass-"3"/V-store; Pythagorean A² = ε² + κ² + V².)*
   - 3-axis orthogonal triad (stubs/grooves) = 3 translational DOF → **E** / capacitor / dielectric displacement → **ε² store** (`09:207`).
   - 3 orthogonal rings/loops = 3 micro-rotational DOF → **B** / inductive flywheel / spin → **κ² store** (`09:208`, `09:22`).
   - 1 radial **breathing indicator** (concentric "bellows" ridge or radial-arrow set at the node core) = A1 volumetric dilation → **mass / V² store** (`03_pin_port_configuration.tex:45-66`, `trampoline-framework.md:200`). Kept on an axis independent of the rings per **A1 ⊥ T2** (`09:86`). Third accent color.
   - *(The dynamical saturation-amplitude A is the LC-tank STATE, an 8th item that is NOT a spatial DOF — represented only by the phase-space disc/dial, item 3-4, never as a node body feature.)*
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

## 4. Canonical facts the geometry must honor ✓ (audit-verified, workflow `w7qwv0e6g`; digest `.agents/handoffs/2026-06-21_audit-digest.md`)

- ✓ **Production = degree-4 diamond** (`build_diamond_net`, `K4Lattice3D`), achiral **Fd-3m**; ALL production drivers (α, Lorentz, photon) run on it. The kit already builds this correctly: verified kit port dirs == engine `_DIAMOND_PORTS`, all bonds bipartite A–B, port-pair angle 109.47° tetrahedral. **Instrument = degree-3 srs** (`build_srs_net`), chiral **I4₁32/I4₃32**, girth-10, 120° bonds — diagnostic only.
- ✓ **"K4" is a documented THREE-WAY overload** (`vocabulary-register.md:378-394`): axiom-name "chiral Laves K4"=degree-3 srs; engine "K4"=degree-4 diamond; rotation group K4→A₄. The Axiom-1 single-source statement (`eq_axiom_1.tex:26`) welds "I4₁32 chiral space group" onto "z=4 diamond connectivity" in one sentence — a **confirmed major NAMING defect** with a **queued, UNMERGED z4-walk-back** (`origin/analysis/2026-06-08-vacuum-z4-coordination-walkback`), Grant-gated. *Physics is reconciled*: Fd-3m ⊃ I4₁32 (supergroup); cold lattice achiral (k_χ=0→Fd-3m), chirality is an **excited k_χ Cosserat order-parameter** (k_χ>0→I4₁32). **The print must follow the adjudicated direction: production = achiral diamond; chirality is the srs instrument's story, not a cold-diamond property.**
- ✓ **Node mode content is 6 spatial DOF + 1 A1 breathing = 7 kinematic modes** (NOT just 6). `eq_axiom_1.tex:26`/`CLAUDE.md:70`: 6 DOF = 3 translational→**E** (ε² store) + 3 microrotational→**B** (κ² store). `03_pin_port_configuration.tex:45-66` + `trampoline-framework.md:200,247`: **plus the A1 volumetric breathing mode → V² store = the mass-"3"** (Pythagorean total A² = ε² + κ² + V²). The saturation-amplitude **A is an 8th *state*, NOT a spatial DOF** (`03:96`). **A1 ⊥ T2**: mass (A1/V) and charge-spin (microrotation/κ) never share one phasor (`09_mechanical:86`). **→ a faithful node shows triad (ε/E) + rings (κ/B) + a breathing indicator (V/A1/mass); the phasor disc/dial is the state A, kept separate.**
- ✓ **Every node is an identical full oscillator carrying ALL stores.** A/B is the **bipartite sublattice only**, NOT a DOF/storage split (`ch18.tex:70`, `index.md:45`). The current cube(A)/sphere+ring(B) shapes + `_capacitive`/`_inductive` SKUs **encode a denied split** (REP-01, confirmed major) → fix by identical body + color/key.
- ✓ **ℓ_node = ħ/(m_e c) ≈ 386 fm is DEFINITIONAL** (electron reduced-Compton length), not derived — despite sitting under a "DERIVED TOPOLOGICAL CONSTANTS" header (`constants.py:252,257`; minor mislabel). Print magnification at 100 mm/ℓ_node ≈ ×2.59e11.
- ✓ **Coordination numbers are distinct, do not conflate**: graph degree **4** (what a print shows); √6 in ℓ_c=√6·ℓ_node is the Cosserat elastic ratio ξ_K2/(2ξ_K1)=6 (`constants.py:261`), **not** a coordination; z_eff→6 = isostatic constraint ceiling; **z₀≈51.25 = effective coordination of the *amorphous* picture**. Crystalline-Fd-3m vs amorphous-z₀ is a **REAL OPEN SEAM the corpus admits** (`the-abandoned-interior.md:185`). Print = degree-4 crystalline graph; must not imply z₀/z_eff.
- ✓ **Open seams to NOT touch (flag-don't-fix, Grant-gated physics):** chirality realization (achiral+k_χ vs natively-chiral, unmerged walk-back); crystalline vs amorphous; proton multi-node vs nucleus-in-single-node (`ACCURATE_SCALING.md:179-185`). The print stays consistent with the adjudicated reading and asserts nothing beyond it.

## 5. Audit findings being remediated ✓ (verified; full list in digest)

**Mesh / watertight (blocker):** node A/B reload non-manifold because `_trimesh_to_mesh` (`vacuum_lc_geometry.py:427-430`) explodes the welded boolean trimesh into per-face numpy-stl (loses shared vertices), then binary-STL float32 over-merges slivers. **Fix: export the welded trimesh DIRECTLY (`tm.export(...)`) — verified to give watertight=True, is_volume=True; stop round-tripping through numpy-stl.** Bond reloads is_volume=False from inconsistently-wound `sweep_hex_prism_open` end caps → `fix_normals`/build as primitive. **Make `saved_qc()` GATING** once fixed (env escape hatch for WIP).

**Printability MK3+ (blocker/major):**
- Bond 143 mm × 6 mm printed VERTICAL, 20:1 aspect → topples (`kit_print_pose.py:70-73`). Fix: print horizontal OR short-insert (see §8 fork).
- Bond length == mouth-to-mouth → **ZERO axial insertion** (`vacuum_lc_geometry.py:101-109`); bond must be longer than the gap by the insertion depth each end.
- Node A flat pose: 2 of 4 ports point DOWNWARD (`kit_print_pose.py:52-57`) → with snap-on accent ports the node body has no protruding ports → **moot**; else body-diagonal-up pose.
- Node B hollow-sphere dome = internal overhang → **make B solid** (it's a mnemonic, no functional cavity) → dissolves with the single-body fix.
- 0 mm press-fit (`vacuum_lc_geometry.py:55` `KIT_BOND_RADIUS = KIT_SOCKET_RADIUS`). **Fix: `KIT_BOND_RADIUS = KIT_PEG_RADIUS` (single interference source via `KIT_FRICTION_INTERFERENCE_MM`).**
- FDM-floor guard checks collar circumradius (never trips) → guard wall/socket/peg minimums. `supports:'none'` untruthful; add elephant-foot chamfer on mating surfaces; build-volume guard; tolerance-stack over the 14-bond L4 closed loop; Z-seam off sphere mating zone.

**Assembly (major):** `bond_total_length`/`peg_length_mm` report pegs the kit mesh never builds (geometry-lie) → build pegs or stop reporting. **The 4 ports are geometrically identical — no keying tells a builder which port→which neighbor** → emboss port-index marks + per-node port→neighbor map in manifest, AND/OR ship a printed base jig with sockets at node positions (robust assemblability).

**Code quality:** delete dead `_cube_frame_mesh` (undefined `KIT_FRAME_BEAM_RADIUS`) + dead constants `KEY_FIN_THICK`/`SOCKET_POCKET_DEPTH`/`KIT_TL_RADIUS` (no physical "key fin" exists — strike from `ch18:114`/`kit_print_pose.py:62-63`); collapse redundant `_KIT_DEFAULT_MM` double env read; remove unused imports; set shared module default 25→100 mm; tag the joinery constant block `[RENDERING]`.

**Critic adds:** the 21 MB showpiece (`generate_axiom1_lattice_showpiece_stl.py`) was never audited, prints at 25 mm with sub-nozzle ribbon features, and its turbine cap shows degree-3 (srs) → FDM-guard + label, or pair with diamond. No scale-bar/magnification embossed on any part → emboss a `[RENDERING] ℓ_node≈386 fm, ×2.6e11` plate. Offer a **single diamond unit-cell hero print (2 nodes + 4 bonds, ~6 parts)** as the recommended first build instead of L4 (30 parts).

**Refuted — do NOT carry forward:** Op5-two-operators; `K4_BOND_DIRECTIONS` "non-existent" (it exists); per-DOF-tensor "missing caveat"; node-A stem "wrong side of cube" (geometry is correct); "137 mm bond is a bug" (full-length strut is by-construction — the real defects are zero-insertion + vertical-pose, not the length itself).

## 6. Prusa i3 MK3+ constraints (hard)

Bed 250×210×210 mm; 0.4 mm nozzle; PLA/PETG; single extruder ⇒ no soluble support; unsupported overhang ≤ ~55°; reliable bridge a few mm; min robust feature ~0.8–1.0 mm; watch elephant-foot on collars, warp on large flat faces, seam on sphere.

## 7. Implementation sequence

1. Design doc (this) — commit #1, open draft PR.
2. DOF markers module + A/B mnemonic fix (Task #6).
3. Bond helix + phase-space companions (Task #7).
4. Watertight + press-fit + printability pass (Task #8); live-fire regenerate, on-disk QC must be green.
5. Vol 9 docs lockstep (KB leaf → ch18.tex → kit README) + figures (Task #9).
6. Validate; push; PR ready-for-review.

## 8. Decisions

**RESOLVED — Grant 2026-06-21:**
- **Chiral srs piece: INCLUDE** (both enantiomorphs; acceptance instrument label).
- **Color: single-color prints + snap/glue-on color accent parts** (no multi-material).

**RESOLVED — Grant 2026-06-21 (round 2):**
- **7th mode (A1 breathing/mass): YES** — add the breathing indicator (§3 item 1).
- **Bond geometry: (a) full-length TRUE-PITCH strut (~143 mm), printed HORIZONTAL** with real insertion pegs. ("a for now" — true √3·ℓ_node pitch is the default; compact scale available via env override.)
- **Base jig: YES** — printed baseplate with sockets at node positions forces correct placement + solves the unkeyed-port problem; port-index emboss + port→neighbor map in manifest.
- **Hero first print: YES** — single diamond unit cell (~6 parts) recommended starter; L4 demoted to "next."
- **Showpiece:** add FDM-floor guard + "degree-3 srs INSTRUMENT, not production diamond" label.
- **Build method (Grant directive):** maximize parallel compute — implement via a parallel workflow (independent parts fan out; the node+accent+bond mating core stays one author for fit integrity).

**NOT touched (Grant-gated physics open seams):** chirality realization, crystalline-vs-amorphous, proton multi-node — the print follows the adjudicated diamond-primary/achiral-cold reading and asserts nothing beyond it.

---
*Skill plan: `.agents/handoffs/2026-06-21_vacuum-cell-print_skill-plan.md`. Prereg corpus-inventory = audit workflow `w7qwv0e6g`.*
