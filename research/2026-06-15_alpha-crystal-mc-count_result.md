# Result — Exact Maxwell–Calladine constraint count of α on the achiral diamond K4 crystal

**Date:** 2026-06-15 · **Lane:** α (Lane 1, crystalline pivot) · **Status: COMPLETE**
**Prereg (FROZEN, Rule-11):** `2026-06-15_alpha-crystal-mc-count_prereg_FROZEN.md` — **OFF-CORPUS (referential-integrity note, 2026-06-19):** this FROZEN prereg lives only on the now-deleted branch `analysis/2026-06-15-alpha-crn-flip-test` (no remote, not on `main`), so the link cannot resolve on-corpus. The load-bearing falsifier-bins this result was judged against are **stated inline below** (see "Bin classification" §, the parenthetical *"Bin D condition (frozen): z_eff ≈ additive 16 (→49 only via circular EMT), OR the only map to 137 is 8πα"* at the head of this doc) — referential integrity is preserved by the inline bin-set, no on-branch lookup required. Verdict assignment (Bin D — ECHO, both disjuncts satisfied) is self-contained in this doc.
**Driver:** [`src/scripts/vol_1_foundations/alpha_crystal_mc_count.py`](../src/scripts/vol_1_foundations/alpha_crystal_mc_count.py)
**Raw output:** `src/scripts/vol_1_foundations/alpha_crystal_mc_count_results.json`

---

## Bin classification: **D — ECHO** (both Bin-D disjuncts satisfied)

The exact constraint count **closes the z₀ → α route**. There is **no α-free map**
from the crystal's independent-constraint coordination to 1/α = 137.036. The
canonical z₀ = 52 → 137 was a **multiplicative path-count convention** dressed
with the 8πα identity; the prereg's "additive ~16" was a **bond multiplicity**;
the *true* independent-constraint coordination converges to the **central-force
isostatic ceiling z_eff → 6**. α stays **Class-B echo** — confirmed, banked clean.

Bin D condition (frozen): *"z_eff ≈ additive 16 (→49 only via circular EMT), OR
the only map to 137 is 8πα."* **Both disjuncts hold:** (i) the bond multiplicity
per node is exactly 16 (4 first + 12 second), and (ii) the only published
z → 1/α maps are the circular 8πα FTG-EMT or the forbidden dilution-p_c. The
exact rank **refines** the expected "16" to the isostatic 6 — see §4 (this is a
sharpening of the prereg mechanism, not a bin change; surfaced honestly per
Rule 11 / flag-don't-fix).

---

## 1. The numbers (L = 4, 6, 8 supercell sweep)

All counts are **exact** (sparse SVD rank with a hard floppy/rigid singular-value
gap of ~10¹⁴–10¹⁵ — no tractability wall; the N-bin never engaged). Topology
verified **byte-for-byte identical** to `ave.core.chiral_lattice.build_diamond_net`
at every L (parity=True; the standalone α-free rebuild reproduces the canonical
adjacency exactly).

DOF = degrees of freedom, #C = number of constraint rows, rank = rank(R),
**f = floppy = DOF − rank**, **s = self-stress = #C − rank**, **f−s = Maxwell–
Calladine index = DOF − #C**, **z_eff = 2·rank/N** (additive effective
independent-constraint coordination per node).

### Central-force 3N — PRIMARY, primary network (1st-neighbour only)

| L | N | DOF | #C | rank | f | s | f−s | **z_eff** |
|---|---|-----|----|------|---|---|-----|-----------|
| 4 | 16 | 48 | 32 | 30 | 18 | 2 | 16 | 3.7500 |
| 6 | 54 | 162 | 108 | 107 | 55 | 1 | 54 | 3.9630 |
| 8 | 128 | 384 | 256 | 254 | 130 | 2 | 128 | **3.9688** |

Bare diamond is **sub-isostatic** (#C/N = 2.0 ≪ 6; z_eff → 4 = the bare
coordination). f ≫ s: it is floppy, as Maxwell predicts for z=4 < z_iso=6.

### Central-force 3N — PRIMARY, **over-braced (1st + 2nd-neighbour |T|=12 shell)**

| L | N | DOF | #C | rank | f | s | f−s | **z_eff** |
|---|---|-----|----|------|---|---|-----|-----------|
| 4 | 16 | 48 | 56 | 40 | 8 | 16 | −8 | 5.0000 |
| 6 | 54 | 162 | 432 | 159 | 3 | 273 | −270 | 5.8889 |
| 8 | 128 | 384 | 1024 | 378 | 6 | 646 | −640 | **5.9062** |

Rank **saturates at 3N − 6** (L=8: 378 = 384 − 6, exact). Adding the 12
second-neighbour bonds/node does **not** raise the rank past the rigidity
ceiling — it only adds **redundant** constraints (s explodes: 646 self-stress
states at L=8, f drops to the 6 rigid-body/homogeneous-strain modes). **z_eff →
6** (the central-force isostatic value 2·(3N−6)/N → 6; L=10 confirms 5.976).

### Micropolar 6N (Cosserat, SENSITIVITY)

| variant | L | N | DOF | #C | rank | f | s | f−s | **z_eff** |
|---|---|---|-----|----|------|---|---|-----|-----------|
| primary | 8 | 128 | 768 | 768 | 672 | 96 | 96 | 0 | 10.5000 |
| over-braced | 8 | 128 | 768 | 3072 | 762 | 6 | 2310 | −2304 | **11.9062** |

Same structural story with doubled DOF: over-braced rank → 6N − 6 (z_eff → 12,
the micropolar isostatic value). Robust to the central-vs-micropolar axis: **no
variant approaches 137**; all converge to the isostatic ceiling of their DOF set.

### Keating angular over-bracing (the prereg's EITHER/OR alternative)

| L | N | DOF | #C | rank | f | s | f−s | z_eff |
|---|---|-----|----|------|---|---|-----|-------|
| 8 | 128 | 384 | 1024 | 378 | 6 | 646 | −640 | 5.9062 |

Bond-bending angular over-bracing gives the **identical** rank/z_eff as
2nd-neighbour central-force bonds (378, z_eff=5.906) — confirming they are the
same linear-rigidity object (fixing bond lengths + angles ≡ fixing the
2nd-neighbour separation). The over-bracing route does not matter; the ceiling
is the same.

---

## 2. Is there an α-free map z_eff → 1/α? — **NO** (the load-bearing Q1 verdict)

| reference | value | how it relates to α | z_eff vs it |
|---|---|---|---|
| **z_eff (over-braced, L=8)** | **5.906** | the exact independent-constraint coordination | — |
| multiplicative path-count z₀ = 4·(1+\|T\|) | **52** | α-free integer, but a PATH count not a constraint count | 88.6% off |
| additive bond multiplicity | **16** | α-free, but the count of BONDS/node not INDEPENDENT constraints | 63.1% off |
| α-fit FTG-EMT root | **51.25** | **CIRCULAR** — the root of p_c = 8πα; needs α as input | 88.5% off |
| CODATA 1/α | **137.036** | the chord target | 95.7% off |

**There is no α-free closed form taking an integer/float coordination to
137.036.** The only two z → 1/α maps in the corpus are:

1. **FTG-EMT quadratic** `p_c = (10z−12)/(z(z+2)) = 8πα`, then `1/α = 8π/p_c`
   (`constants.py:512-520`, `Z_COORDINATION ≈ 51.25`). This **requires α** as
   input (it sets p_c = 8πα *first*, then solves for z). It is **circular** — it
   manufactures a z that reproduces α, it does not derive α from z.
2. **Dilution percolation** `1/α = 8π/p_c` with p_c a stochastic packing
   fraction (`derive_alpha_m4_pro.py:130-137`, `boinc_alpha_derivation.cpp:216-217`).
   This **reintroduces the deprecated stochastic disorder** the prereg forbids.
   The tell named in the prereg holds exactly: `8π/p_c` is type-correct for 1/α
   **only** in the dilution form — that *is* the smuggle.

The driver reports `alpha_free_map_to_137_exists = False`. The crystal-pure
exact count lands z_eff = 6 (central) / 12 (micropolar); **neither maps to 137
α-free.**

---

## 3. What the canonical z₀ = 52 → 137 actually was

z₀ = 52 = 4·(1 + |T|) = **4 ports × 13 paths** is a **multiplicative path-count
convention**, not a constraint count:

- the "4" = the K4/diamond coordination N_K4 = 4;
- the "13" = 1 + |T| = 1 + 12, where |T| = 12 is the number of secondary
  **paths** (4 B-neighbours × 3 other-A sublattices = the 12 graph-2-hop A-nodes).

The exact MC count shows that those 12 second-neighbour bonds/node are
**topologically redundant** — they add self-stress, not independent constraints.
The independent-constraint coordination is bounded by the Maxwell isostatic value
(z=6 central-force, z=12 micropolar), and **z₀=52 = 4·13 is a product of two
multiplicities, dimensionally an edge/path tally, never a per-node constraint
count.** The 8πα identity was layered on top of the FTG-EMT to relabel this path
tally as a coordination that "predicts" α — but the prediction runs α → z, not
z → α.

This is exactly the readout `derive_alpha_m4_pro.py:146-151` named but
**declined** to compute: *"we would mathematically calculate the EXACT rank of
R_matrix to find the exact phase transition where Rank = 3N−6 … But computing
exact rank … will hang a laptop for hours. Instead, we print the … packing
fraction."* This driver computes that exact rank. It lands on **Rank = 3N−6**
(the isostatic ceiling that file named), giving **z_eff = 6**, not 137.

---

## 4. Refinement of the prereg's "~16" expectation (honest, Rule 11)

The prereg expected the echo to land **z_eff ≈ additive 16**. The exact count
**sharpens** this: the **bond multiplicity** per node is exactly 16.000 (4 first
+ 12 second-neighbour bonds/node), confirming the prereg's mechanism — *"the 12
= secondary paths, NOT independent constraints"* — even more precisely. But the
**independent-constraint** coordination (rank-based z_eff) is the **isostatic 6**,
because rank(R) ≤ 3N−6 regardless of bond count. So:

- **16 was a bond/path multiplicity** (exactly recovered: 2·(#1st+#2nd)/N = 16).
- **6 is the independent-constraint coordination** (z_eff → isostatic ceiling).
- **52 was the multiplicative path-count** (4 × 13).

All three are the same story at different stages of redundancy. None is 137. This
refines (does not overturn) the prereg: Bin D's condition is fully satisfied (the
only map to 137 is 8πα), and the exact value 6 is *more* echo-confirming than the
expected 16, since it shows even the "16" overcounted independent constraints by
~10/node. Surfaced per flag-don't-fix; no bin rewrite, no post-hoc criterion drop.

---

## 5. Coordinate-projection caveat (phase-space-coordinate-check)

This is a **REAL-SPACE BULK** constraint count on the diamond crystal. The
electron's α is a **PHASE-SPACE / BOUNDARY Q** (the electron-instance value, a
bound-resonator Q on the (V_inc, V_ref) Clifford torus, per the field-def lane /
`cvr_model.py`). The two live in **different projections**:

- the bulk count measures the lattice's real-space rigidity coordination;
- the electron's α is a boundary/phase-space impedance ratio.

**A bulk-z_eff → boundary-α link is itself an open projection question.** Even
had the bulk count landed near 137 (it did not), one could not conclude the
electron's α is the crystal's bulk coordination without resolving the
bulk→boundary projection. This null is therefore doubly clean: the bulk
coordination is not 137 *and* a bulk→boundary map is unestablished. The crystal's
real-space rigidity and the electron's phase-space Q are not the same observable.

---

## 6. α-free discipline audit (how the count stayed clean)

- **Import-graph guard** (`assert 'ave.core' not in sys.modules` at module
  import): verified to **trip** when `ave.core` is pre-imported and **pass** on
  fresh import (the count never pulls in the α-bearing `constants.py`). Stronger
  than `verify_universe.py`'s literal scan — it forbids the smuggle module from
  the import graph entirely.
- **Diamond net rebuilt standalone** (no `build_diamond_net` import, which pulls
  `ave.core.constants`). Topology proven identical by parity check in `__main__`.
- **No 1.187, no C_ratio, no p_c, no 8πα fed in.** Over-bracing specified
  **topologically** (the |T|=12 2nd-neighbour shell), never by an α-bearing
  length ratio. The deprecated amorphous/dilution path of
  `derive_alpha_m4_pro.py` / `boinc_alpha_derivation.cpp` is NOT used — only the
  directional-cosine row-assembly pattern, fed explicit crystal bonds.
- **CODATA α** appears only at `__main__` time as `1.0/ALPHA` (imported from the
  canonical constants module, ave-canonical-source; computed so no `137.036`
  literal token appears), labeled a one-way comparison reference, never fed into
  any count.
- **`verify_universe.py`**: PASS (889/889 MATHEMATICALLY PURE, including this
  file).
- **No `minimize`/`curve_fit`/target-fit anywhere** (ave-driver-script-honesty):
  the driver forward-computes exact rank; the honest deliverable is the echo.

---

## 7. Cross-references

- Walk-back precedent: `research/2026-05-18_z0-first-principles-attempt-result.md`
  (z₀=52 convention-dependent; physical z ≈ 16 → 1/α ≈ 49).
- α-circularity anchors: `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/topological-packing-fraction.md`;
  `constants.py:512-520` (Z_COORDINATION FTG-EMT quadratic root from p_c = 8πα).
- Declined-rank readout this driver supplies: `derive_alpha_m4_pro.py:146-151`.
- Pebble-game (3,6) redundancy readout (the N-bin fallback, not needed — exact
  rank was tractable): `boinc_alpha_derivation.cpp::add_bond` (independent/
  redundant counts it currently discards).
- Reuse: `derive_alpha_m4_pro.py::build_sparse_rigidity_matrix` (directional-
  cosine row pattern); `chiral_lattice.py::build_diamond_net` (parity reference);
  `q_g47_path_b_k4_eigenmode.py` (Keating `k_θ`, `k_s = k_θ/d²`).

---

## 8. Banked finding (one line)

**Exact Maxwell–Calladine count on the α-free over-braced achiral diamond K4
crystal: z_eff → 6 (central-force isostatic ceiling, rank = 3N−6) / 12
(micropolar), bond multiplicity = 16, path-count z₀ = 52; NONE maps to 1/α =
137.036 α-free (only 8πα [circular] or dilution-p_c [forbidden]). The z₀ → α
route is closed: 52 → 137 was a path-count convention + the 8πα identity, never a
constraint count. α stays Class-B echo. Bin D — ECHO, banked clean.**
