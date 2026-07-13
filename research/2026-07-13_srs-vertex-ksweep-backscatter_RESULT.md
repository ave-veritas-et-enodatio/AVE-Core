# RESULT — srs vertex k-sweep backscatter (T4 ontology fork)

**Date:** 2026-07-13 · **Prereg (frozen, pushed before run):**
[`research/2026-07-13_srs-vertex-ksweep-backscatter_prereg_FROZEN.md`](2026-07-13_srs-vertex-ksweep-backscatter_prereg_FROZEN.md)
· **Driver:** [`src/scripts/vol_1_foundations/srs_vertex_ksweep_backscatter.py`](../src/scripts/vol_1_foundations/srs_vertex_ksweep_backscatter.py)
· **Output:** `assets/sim_outputs/srs_vertex_ksweep_backscatter.{json,png}`
· **Handoff:** [`_orchestration/2026-07-13_srs-vertex-ksweep-handoff.md`](../_orchestration/2026-07-13_srs-vertex-ksweep-handoff.md)

---

## TL;DR

**Verdict — bin (i) HOMOGENIZATION-SPLIT** (Grant's leaned frame), all four frozen
classifier conditions satisfied with wide margins. The srs per-vertex −1/3 tee is a
**real reactive event that is invisible to in-band collective carriers and resolves
near the band edge.** Bin (ii) REAL-AT-ALL-K and bin (iii) NULL-EVERYWHERE are both
**refuted**. All four gates pass; all three evolved-field sabotage plants are caught.

**Class (consistency-vs-emergence): CONSISTENCY / peer-with-SM.** This is the ordinary
"why a periodic medium is transparent to long-wavelength carriers and reflective at
band edges" physics, reproduced quantitatively for the specific chiral srs z=3 net —
**not an AVE-distinct chord.** The deliverable is the *quantitative* band-edge
characterization (below) that downstream muon-Q work load-bears on, plus a clean
adjudication of docket **T4**.

---

## Sector header (as-run)

MODE linear wavepacket propagation (carrier/homogenization property of the network);
REGIME cold, **KERNEL OFF** — the combinatorial scatter+connect step is orthogonal ⇒
**lossless to machine ε** (pristine energy drift `1.7×10⁻¹⁴`, gate G1); PHASE-STATE
freely-propagating sub-yield; SECTOR scalar/compression channel. Platform: srs
scalar-TLM only (no cage / VacuumEngine3D); reused the frozen v9 scaffold graph + Op5
scatter primitives — **no new `chiral_lattice_vN`** (per `ave-loop-gap-harness-discipline`).

---

## Headline numbers (primary L=16, N=32 768)

| metric | value | frozen threshold | pass |
|---|---|---|---|
| `R_LW` (long-λ, k·ℓ∈[0.15,0.5]) | **0.0616** | — | — |
| `R_BE` (band-edge, k·ℓ∈[2.0,3.0]) | **0.1933** | ≥ 0.0556 (½·⅑) | ✓ |
| `R_dis` (incoherent limit, all k) | **0.5001** | ≈ 0.5 expected | ✓ |
| `σ = R_LW/R_dis` (suppression) | **0.123** | ≤ 0.35 (i.a) | ✓ |
| `ρ = R_BE/R_LW` (band-edge rise) | **3.14** | ≥ 2.0 (i.b) | ✓ |
| `R_dis ≥ 2·R_LW` (meter-not-blind) | 0.500 ≥ 0.123 | (i.d) | ✓ |
| `s_rank` (monotone rise) | **0.994** | ≥ 0.7 (G3) | ✓ |

**R(k) pristine** rises **monotonically** from `0.062` (k·ℓ=0.15) through the per-vertex
scale `|Γ|²=1/9≈0.111` (crossed near k·ℓ≈1.85) to `0.262` at the zone boundary
(k·ℓ=3.0) — i.e. the band-edge backscatter reaches **1.7–2.4× the bare-tee 1/9 scale**.
The disorder control sits **flat at 0.500** across the whole sweep. See figure.

### Frozen three-way classifier evaluation

- **(i) HOMOGENIZATION-SPLIT — SELECTED.** i.a `σ=0.123≤0.35` ✓ · i.b `ρ=3.14≥2.0` ✓ ·
  i.c `R_BE=0.193≥0.0556` ✓ · i.d `R_dis=0.500≥2·R_LW=0.123` ✓.
- **(ii) REAL-AT-ALL-K — REFUTED** (`σ=0.123≯0.35`; `ρ=3.14≮2.0`).
- **(iii) NULL-EVERYWHERE — REFUTED** (`R_BE=0.193≮0.0556`; the tee plainly resolves at
  the band edge).

---

## The honest refinement of Grant's leaned frame ("plateau", not "→ 0")

Grant's bin (i) prose said backscatter *"falls toward zero with a power law at long
wavelength."* **What the frozen estimator actually shows is a strongly-suppressed
PLATEAU, not a strict power-law-to-zero:** `R(k)` is flat at `≈0.061–0.062` for
k·ℓ ≲ 0.5 (with a shallow minimum near k·ℓ≈0.32), then rises. The classifier did **not**
test "→0"; it tested **suppression vs the incoherent limit** (σ≤0.35) and **band-edge
rise** (ρ≥2) — both hold decisively — so the **bin (i) selection is robust** and this is
a *refinement, not a walk-back*.

Two facts bound the plateau's meaning honestly:
- **It is not a finite-size artifact.** Convergence L=12/16/20 gives `R_LW =
  0.0632 / 0.0616 / 0.0615` and `R_BE = 0.1960 / 0.1933 / 0.1924` — stable, mildly
  decreasing with box size.
- **The instantaneous coherent minimum is far below the plateau.** Meter-validation
  (prereg P-series) recorded the *instantaneous* `b(t)` dipping to `~0.004` at long
  wavelength; the `0.062` plateau is the time-averaged frozen estimator (it folds in the
  broadband launch content + residual multiple scattering). So the *coherent* long-λ
  backscatter is even more suppressed than `0.062` — the homogenization is if anything
  stronger than the headline number. **The plateau is reported as the frozen-estimator
  value, not upgraded to a coherent floor.**

Physical reading (unchanged from Grant's frame, now quantified): **in-band collective
Bloch modes barely see the tee** — the periodic srs lattice diagonalizes the per-vertex
−1/3 into its band structure, so a carrier that fits the band transmits with strongly
suppressed backscatter; only content approaching the zone boundary (band edge) resolves
the individual junction, where R climbs through and past the bare-tee `1/9`.

---

## Gate battery (all pass)

| gate | test | result |
|---|---|---|
| **G1 lossless** | pristine energy drift < 1×10⁻⁸ | drift `1.7×10⁻¹⁴` ✓ |
| **G2 meter-not-blind** | `R_dis ≥ 2·R_LW` | 0.500 ≥ 0.123 ✓ |
| **G3 monotone-rise** | `s_rank ≥ 0.7` | 0.994 ✓ |
| **G4 enantiomorph symmetry** | `|R_R−R_L|/R < 0.20` | max dev `2.2×10⁻¹⁶` ✓ |

**G4 is essentially exact** (right/left agree to machine ε): the backscatter magnitude is
chirality-blind, as the counting fact `Γ=(2−z)/z` demands — the two enantiomorphs have
mirror-identical band structure. This is a strong internal-consistency confirmation.

---

## Sabotage battery — every evolved-field corruption is caught

Each plant corrupts the **evolved field** (not a post-hoc reduction), per the rail. The
frozen gate that catches each fired:

| plant | evolved-field corruption | fakes | drift | caught by |
|---|---|---|---|---|
| **A kill-backward** | zero backward-port energy each step | (iii) | `1.0` | **G1** (lossy) ✓ |
| **B inject-source** | add fixed backward amplitude each step | (ii) floor | `481` | **G1** (adds energy) ✓ |
| **D lossless fwd↔bwd mix** | per-node orthogonal fwd↔bwd rotation (θ=0.15) | flat (ii) | `3.8×10⁻¹⁴` | **G3** ✓ |

Plant **D is the sharp one**: being orthogonal it is genuinely **lossless (passes G1)**,
so an energy-conservation check alone would not catch it. It is caught by **G3**: it
collapses the band-edge rise (`ρ` falls `3.67 → 1.20`) and elevates the long-λ floor
`~3×` (`R_LW 0.062 → 0.194`), i.e. it flattens R(k) toward a k-independent (ii)-like
floor — exactly the signature G3 tests. **The test cannot be fooled by an evolved-field
corruption without a gate firing.**

---

## Band-structure cross-check (scope-honest)

`measure_dispersion` (canonical) on L=16 confirms the **long-wavelength linear regime**:
phase velocity / c_link = `0.581, 0.575, 0.577, 0.577, 0.575, 0.575` across
k·ℓ ∈ [0.14, 0.83], vs the analytic network factor `1/√3 = 0.5774` (agreement < 1%). This
is the "homogenized effective medium" the carrier rides at long wavelength.

**Honest limitation (prereg-vs-run reconciliation).** The prereg's G3 description also
named an *"R-rise region overlaps the v_g→0 band-edge region"* sub-clause. **As run, G3 is
the monotone-rise / ρ-collapse test** (`s_rank`, plus the plant-D ρ-collapse detection) —
this is what actually gates and what catches plant D. The `v_g→0` sub-clause was **not
operationalized**: the dispersion probe (`m=1..6`) covers only k·ℓ ≤ 0.83 (the linear
acoustic window), and cleanly locating the band edge in the **8-band** srs spectrum is
beyond a single-peak FFT extraction. **The band-edge is therefore evidenced by R(k)'s own
monotone climb toward the zone boundary, not independently by a measured v_g→0.** This is
a documented scope limit, not a hidden gap; it does not affect the three-way selection
(which rests on σ, ρ, R_BE — all measured directly).

---

## The sharp edge — is the result consistent with the electron's terminal-pole Q→∞?

Stated as the prereg's **named consistency check** (NOT assumed as a result). The electron
is also node-scale (`R*≈1.6 ℓ_node`, dimensionally-forced / CANDIDATE-class;
`hollow-vortex-binding.md:133`) yet `Q→∞` (terminal pole, `Q_tank=4π³+π²+π=α⁻¹`). A bin-(i)
result is **consistent** with this: backscatter is priced **only near the band edge**
(where an onward channel opens), and **vanishingly at long wavelength** — so a mode that
sits cleanly inside the band (no onward channel to drain into) pays no backscatter price,
matching a terminal-pole Q→∞. A bin-(ii) result would have *tensioned* it (a per-vertex
price at all k would force a separate reason the electron escapes) — and bin (ii) is
refuted. **So the result does not contradict the electron sharp edge; it is the regime in
which "proximity prices the channel only where an onward mode exists" holds.** The
band-edge-straddling → finite-price picture for the muon remains a *downstream hypothesis*,
not established here.

---

## What this settles (and does not) for docket T4

**Settles (peer-with-SM consistency level):**
- The srs `z=3` per-vertex `Γ=−1/3` reflection is a **real reactive event** (meter
  reproduces `|Γ|²=1/9` exactly at the single vertex, prereg P3) but is **homogenized away
  for in-band collective carriers** (σ=0.12) and **resolves near the band edge** (R climbs
  to ≥1/9). It is **neither** a per-vertex price at all k (bin ii, refuted) **nor** a
  never-resolving bookkeeping idealization (bin iii, refuted).
- For A-class cascade drainage's "primitive unit" language: the srs `1/9` **is** a
  physically real unit, but it is **expressed for band-edge-straddling content, not for
  band-interior carriers** — the "primitive unit" is real yet **carrier-selective**.

**Does NOT settle (out of scope here):**
- Whether the muon's finite `Q_μ` is *caused* by band-edge backscatter — that requires the
  muon's actual radial/spectral content and a bound-mode calculation; this driver only
  characterizes R(k) on the bare srs network.
- The precise band-edge location / multi-band structure (see cross-check limitation).

---

## Honest cite-flags (unchanged from prereg)

- **"muon content ~0.74-cell radial"** = Grant's leaned estimate (2026-07-13), **no corpus
  receipt**; not used or tested by this driver.
- **`Q_μ ≈ 3.5×10¹⁷`** (`vol4/…/ch14-leaky-cavity-particle-decay/theory.md:14`) — the
  middle-of-ladder value is **flagged NOT-verified at this HEAD**
  (`research/2026-07-13_registers-walk_framing.md:129`, pending `ww0giq5he`); carried as a
  cited lean only.
- The band-edge ⇒ muon-Q link is a **downstream hypothesis, not adjudicated here.**

## References (grep-verified anchors — 2026-07-13)

- `manuscript/ave-kb/common/translation-tables/translation-circuit.md:180` — srs z=3 vertex
  = mismatched reciprocal 3-port; Γ=−1/3; |Γ|²=1/9 reactive back-scatter; |S₁₁|≥1/3 floor.
- `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-vertex-scattering.md`
  §1 (`clm-v3port`; X38/X37, PR #619/#616/#620) — the canonical bare-vertex result this
  driver's collective-mode measurement complements.
- `manuscript/ave-kb/common/program-arc-map.md:306` — the open T4 fork this adjudicates.
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/hollow-vortex-binding.md:133`
  — electron R*≈1.6 ℓ_node (dimensionally-forced / CANDIDATE-class consistency check).
- `research/2026-07-08_p4-forward-voltage-threshold_RESULT.md:115` +
  `research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md:374` — muon radial-extent
  nearest anchors (the "~0.74-cell" figure is Grant's unreceipted lean).
- `manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md:14` —
  `Q_μ≈3.5×10¹⁷` (flagged NOT-verified at HEAD).
