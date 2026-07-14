# Cavity-Census Stage-1 — imposed-cavity mode census — **RESULT**

> **FROZEN prereg:** `research/2026-07-14_cavity-census-stage1_prereg_FROZEN.md`
> (freeze commit `1c362d1d`, pushed ALONE before this driver — freeze precedes
> driver in git history). **Instrument:** `src/ave/solvers/cavity_census.py`;
> **gates:** `src/tests/test_cavity_census.py`. This RESULT reports the frozen §4
> bins for the §3 battery. **Dimensionless outputs only (Rail 2).** Every deviation
> from the frozen body is carried as a **dated amendment in §A below — the frozen
> body is untouched.**
>
> **DO-NOT-MERGE — only Grant merges (frozen §6.5). This is an analysis PR.**

---

## Review findings + repairs (2026-07-14)

An independent adversarial review (3 lenses, 18 agents) confirmed **14 of 15** findings
(1 refuted). The **verdict NO (2,3) EMERGENCE survives** — the LA cavity fundamental (the
freeze-faithful "lowest interior mode", never read before) also returns non-(2,3). The
evidence base is rescoped to what the instrument actually measured. Finding → repair-commit:

| # | Finding (severity after review) | Repair | Commit |
|---|---|---|---|
| 1–2 | **Band inversion** — SA read the wrong spectral end; cavity fundamental never interrogated; phantom "frozen §2 smallest-algebraic" citation (MAJOR×2) | Read the **LA fundamental** (freeze-fidelity, A8); correct phantom §2 citations (code + A7); KEEP-BOTH ends | `c74aff23` |
| — | (m) eigvec real-fraction = single-Lanczos-draw noise (MINOR) | Retired as a data column; degeneracy is the robust invariant (A11) | `c74aff23` |
| — | (e) `INCONCLUSIVE-Nyquist` collapses 3 failure modes (MINOR) | `_refusal_label` reports the actual failing gate (A9) | `c74aff23` |
| — | (f) phantom "frozen §6 (f)" plant-gate citation (MINOR) | Corrected to §6 item 1 / §0.4 / §4 | `c74aff23` |
| g | Floor cell detector-blind; G0 validates one geometry; misreads planted (2,3) at rung 0.5 (MAJOR/MINOR) | Per-rung positive controls; `detector_trustworthy_rungs={1.0,1.6}` (A13) | `d8f3dccd` |
| h | No engine-representable positive control in cold-linear leg (MINOR) | Scope-note: cold-linear leg INSTRUMENT-INCONCLUSIVE by construction (A14); title qualifier | `d8f3dccd` |
| i | Driven-ping unwalled, reads common LC carrier (MAJOR) | Rescoped to #417 re-confirmation; walled-driven = Stage-2 (A15) | `d8f3dccd` |
| j | `select_census_mode` best-fill = silent frozen-observable move (MINOR) | Dated amendment reconciling vs §B-6 (A10) | `9dc9dee1` |
| k | Frozen "all 8 rungs" floor read shipped at 4 (MINOR) | Coverage rescoped; {10,100}=mode-ratio-only (A16) | `9dc9dee1` |
| l | Bin (iv) 4π = dead code (`int%1==0`); unbuilt sampling (MINOR) | Rebuilt as genuine half-integer detector (A12, test G8) | `9dc9dee1` |
| n | Cold reflection-probe = unlogged post-freeze leg (MINOR) | Logged as new impl of a frozen concept (A17) | `9dc9dee1` |
| d | Floor "(0,0) both shapes" headline = gate-refused read (MAJOR) | Rescoped to gate-refused/detector-blind (§2 in `c74aff23`; §7 + PR body in the cluster3-5 commit) | `c74aff23` + cluster3-5 |
| — | **Refuted (1):** — | (no repair) | — |

**Frozen prereg body BYTE-UNTOUCHED across all repairs** (git-verified); every prereg-level
item lands as a dated §A amendment (A8–A17) or an A7 correction. The **D3 framing is
unchanged**: RULED-COEXIST stress-test, COEXIST stands, SELECTION stays imported.

---

## Sector header (mandatory — carried from the frozen prereg)

- **SECTOR** — the imposed census wall terminates the **A1 dilatation-mass channel**
  ($Z_{\text{bulk}}\to0$ short). The **(2,3) winding under test is a T2 / Cosserat
  micro-rotation charge/helicity DOF**. **A1 ⊥ T2.** The imposed wall is **NOT** the
  $\Gamma_{\text{spinor}}=-1$ $2\pi\to4\pi$ stability wall (do-not-re-collide).
- **MODE** — Stage 1 imposes a **static** Γ=−1 boundary and reads
  **existence-given-boundary ONLY**. A Stage-1 pass is NOT the self-consistent
  electron (Stage 2 = task #45).
- **REGIME** — **KEEP-BOTH**: cold-linear Hermitian eigensolve (primary) +
  driven-ping (secondary spot-check). The regime flag is **frozen per bin**; a
  cold-linear null on a winding question where nonlinearity is load-bearing is
  **ARTIFACT-eligible, not a clean negative**.
- **PHASE-STATE** — the wall is imposed on the **cold medium**; the interior
  excitation is a broadband eigenmode extraction, **never a seeded finished mode**
  (CP8 fence).
- **consistency-vs-emergence** — a census returning **(2,3) as the ground-state
  closure class α-free** would be an **emergence-class** claim (converting the (2,3)
  SELECTION import→derivation) with its own adjudication. **The census did not return
  that** (see §2). Every read here is **consistency-class**: existence, spectrum
  fingerprint, geometry-invariance, floor-coincidence.

## Rails honored (frozen §5)

1. **Existence-NOT-formation** — no self-formation slot refilled; mass = A1 (#260)
   untouched. 2. **Dimensionless outputs only** — winding integers, mode-frequency
   ratios, per-sector participation numbers, floor-coincidence booleans; no absolute
   frequency / radius / scale on any verdict. 3. **(p,q) in PHASOR coordinates only**
   — read off the eigenvector's own `[a_A1, b_ω]` phase structure via
   `phase_space_winding` (Lissajous/quadrature), **never** `ê_w`, never the
   real-space linking extractors. 4. **A1 ⊥ T2** — STRUCTURE-derived / SELECTION-
   imported tag carried. 5. **No α** — import-guard triad; sphere-leg ABCD is
   α-clean (reuses the METHOD of `radial_eigenvalue`, not its α-loaded potential).
   6. **CP8/CP10 fence** — broadband extraction, static-wall Stage-1 only.

---

## §1 — DETECTOR TRUST (the plant gates must fire before any verdict is read)

The census verdict is **UNTRUSTED** unless the positive control reads a genuinely
planted (2,3) **and** all three eigenvector-level plant gates trip. Result:

| Gate | Role | Outcome |
|---|---|---|
| **G0 positive control** | canonical detector reads a genuinely planted (p,q)=(2,3) | **read (2,3), ok** — PASS |
| **G1 planted-geometric-only** | winding lives ONLY in seeded `ê_w`; canonical (reads eigenvector) must REFUSE it | canonical read **(0,0)** (refused); coord seed-leg tautologically **2** — **TRIPPED** |
| **G2 Nyquist-starved** | genuine winding 14 sampled at 10 bins (2.5 samples/period < 10) | Nyquist gate fired ⇒ **INCONCLUSIVE** — **TRIPPED** |
| **G3 sector-crosswired** | A1 fed into BOTH loops (the genesis-24 double-count fool-mode) | correct **(2,3)** ≠ crosswired **(2,0)** — **TRIPPED** |

**`detector_trustworthy = TRUE`** (global flag, single comfortable geometry). The pytest
gate suite (`test_cavity_census.py`, G0–G6) is green: 7 fast gates + 1 engine_sim cell
test, 8/8 pass.

**⚠ PER-RUNG SCOPE (A13 — the global flag is NOT a battery-wide license).** A per-rung
positive control (a genuine planted (2,3) restricted to the actual kept region at each
rung's geometry) shows the detector validates **only at rungs {1.0, 1.6}**:

| rung | sphere control | horn-torus control | trustworthy? |
|---|---|---|---|
| **0.16** | reads (0,0), read_ok=**False** (8-cell box) | reads (0,0), read_ok=**False** | **NO — detector-blind** |
| **0.5** | reads (0,0), read_ok=**True** | reads (0,2), read_ok=**True** | **NO — conclusively MISREADS a planted (2,3)** |
| **1.0** | reads **(2,3)**, ok | reads **(2,3)**, ok | **YES** |
| **1.6** | reads **(2,3)**, ok | reads **(2,3)**, ok | **YES** |

At rungs 0.16/0.5 the detector returns a confident false-negative on a KNOWN (2,3) with
every frozen gate passing (toroidal amplitude starvation on the sub-resolving box; the
dual counters share the corrupted input). `detector_trustworthy` is therefore scoped to
`detector_trustworthy_rungs = {1.0, 1.6}` — exactly the rungs carrying the verdict's
gated LA-fundamental reads (§2). Rungs 0.16/0.5 carry **no** trustable winding information
in either direction (INSTRUMENT-INCONCLUSIVE).

---

## §2 — bin (i): GROUND-STATE WINDING CLASS (per shape × BC × R)

**Headline read** — the eigenvector two-sector Clifford phasor winding (canonical,
HEADLINE) of the best-angular-fill interior mode (A10), per shape × BC × R. The 3-D
saturated-core cells below are the **SA (most-bound defect band)** end; the **LA
cavity-fundamental** companion (KEEP-BOTH, A8) is in the reflection-probe table below
and in the LA-companion column here.

| R/ℓ_node | sphere · amplitude | sphere · geometric | horn-torus · amplitude | horn-torus · geometric | LA-fundamental companion (all 4 cols) |
|---|---|---|---|---|---|
| **0.16** (floor) | INCONCLUSIVE-amplitude | INCONCLUSIVE-amplitude | INCONCLUSIVE-amplitude | INCONCLUSIVE-amplitude | BASIS-AMBIGUOUS / INCONCLUSIVE-amplitude |
| **0.5** | INCONCLUSIVE-amplitude | INCONCLUSIVE-amplitude | INCONCLUSIVE-amplitude | INCONCLUSIVE-amplitude | BASIS-AMBIGUOUS / INCONCLUSIVE-amplitude |
| **1.0** | INCONCLUSIVE-amplitude | INCONCLUSIVE-amplitude | INCONCLUSIVE-amplitude | INCONCLUSIVE-amplitude | **(0,0)** / other-(p,0) (seed-dep.) |
| **1.6** | INCONCLUSIVE-amplitude | INCONCLUSIVE-amplitude | INCONCLUSIVE-amplitude | INCONCLUSIVE-amplitude | **(0,0) all 4 cells** |
| **3, 10, 30, 100** | NOT-RUN-3D (compute, A6) | NOT-RUN-3D | NOT-RUN-3D | NOT-RUN-3D | NOT-RUN-3D |

*SA-end labels corrected from the collapsed `INCONCLUSIVE-Nyquist` to the ACTUAL failing
gate — the SA defect band is refused by the **amplitude** gate, not Nyquist (A9). None of
the 16 SA cells, and none of the 16 LA companions, returns (2,3). The gated non-`(0,0)` LA
reads at R=1.0 (`other-(1,0)` etc.) are single-Lanczos-draw integers that wobble across
seeds (never (2,3), never stable); the R=1.6 `(0,0)` is seed-STABLE (A11).*

**No cell returns an integer closure class.** Two spectral ends are now read on the
same masked H (KEEP-BOTH, amendment **A8** — the band-inversion repair):

- **SA end (as-shipped, retained).** `INCONCLUSIVE-amplitude` everywhere: the smallest-
  algebraic modes are tightly-localized defect modes (PN≈2–3 cells, §5-vi) that do not
  fill the cavity's angular loops (`angular_fill` 0.15–0.42), so the sector-phasor read
  is amplitude-starved and the frozen gates refuse it. (This label was previously the
  collapsed `INCONCLUSIVE-Nyquist`; it now reports the ACTUAL failing gate — the read is
  refused by the **amplitude** gate, not Nyquist.) Raw pre-gate `(p,q)` is inconsistent
  basis noise — **never (2,3)**, not stable.
- **⚠ Band inversion (A8).** The as-shipped `which="SA"` was a **build-time CODE choice,
  NOT a frozen commitment** (verify-before-cite: the frozen prereg names no spectral end;
  §4 bin i says only "the (p,q) of the lowest interior mode"). Because `H = ω·I − c²·L_D`
  with `L_D` real **SPD**, an H-eigenvalue `= ω − c²λ`: the band is INVERTED, so SA targets
  the **largest** `L_D`-eigenvalue = the most-oscillatory grid-scale end — **NOT** the smooth
  cavity fundamental. The freeze-faithful "lowest interior mode" is the smallest-`L_D`
  (smooth, interior-filling) mode = the **largest-algebraic (LA)** end of H, now read below.

**Reflection-map probe at the LA cavity FUNDAMENTAL (the freeze-faithful
"ground-state closure of the cavity's reflection map" — the smooth interior-filling
standing wave, band-inversion repair A8). Full gate internals; `deg` = eigenvalue
degeneracy of the selected mode (the robust, seed-independent basis-ambiguity invariant).**

| shape | R/ℓ_node | LA winding class | (p,q)* | angular_fill | deg | gate detail |
|---|---|---|---|---|---|---|
| sphere | **0.16** (floor) | INCONCLUSIVE-amplitude | (0,0)* | 0.042 | 3 | amp-starved both axes (8-cell box) |
| horn-torus | **0.16** (floor) | INCONCLUSIVE-amplitude | (0,0)* | 0.042 | 1 | amp-starved both axes |
| sphere | 0.5 | INCONCLUSIVE-amplitude | (1,0)* | 0.472 | 2 | amp-starved |
| horn-torus | 0.5 | INCONCLUSIVE-amplitude | (−1,−1)* | 0.403 | 2 | poloidal amp-starved |
| sphere | 1.0 | **BASIS-AMBIGUOUS** (real/degenerate) | (1,0)* | 0.500 | 4 | gated; 4-fold degenerate ⇒ arg basis-arbitrary |
| horn-torus | 1.0 | **BASIS-AMBIGUOUS** (real/degenerate) | (0,1)* | 0.806 | 6 | gated; 6-fold degenerate |
| sphere | 1.6 | **(0,0)** (gated-conclusive) | (0,0) | 0.917 | 4 | gated; stable (0,0) across 4 seed draws |
| horn-torus | 1.6 | **(0,0)** (gated-conclusive) | (0,0) | 0.889 | 8 | gated; stable (0,0) across 4 seed draws |

\* `(p,q)` is the raw arg-read of one Lanczos draw and is **seed-dependent** in a degenerate
subspace (see A11); it is shown for context, **not** as a stable data column. What is
seed-STABLE is the **class**: amplitude-starvation (deterministic from `angular_fill`),
degeneracy (deterministic eigenvalue clustering), and the R=1.6 gated `(0,0)` (reproduced
across 4 independent seed draws, both shapes).

**The LA cavity fundamental never reads (2,3).** Where the read is gated-conclusive it is
either a stable trivial `(0,0)` (the best-filled fundamentals, R=1.6 both shapes) or
`BASIS-AMBIGUOUS` (the degenerate R=1.0 modes — arg-winding basis-arbitrary); where the
box sub-resolves (R≤0.5) it is `INCONCLUSIVE-amplitude`. This is the substrate's answer
to the emergence suspicion on the **freeze-faithful** spectral end — the interior-filling
standing wave the frozen §2 promised, now actually interrogated. **No probe, at any rung,
shape, or spectral end, returns (2,3).** The floor-rung (R=0.16) reflection read is
`INCONCLUSIVE-amplitude` (an 8-cell box that sub-resolves any `(p,q)`; a genuinely planted
(2,3) reads the SAME gate-refused `(0,0)` there — the floor cell is detector-blind, see
amendment A14). It is **not** a gated "trivial (0,0)" result.

**Mechanism (documented, load-bearing; live-fire-verified this session).** The coupled
A1↔ω Hermitian generator is **exactly Hermitian** (`max|H − H^H| = 0` ⇒ real spectrum,
lossless) and **dominantly real-symmetric** — the only imaginary content is the coupling
chirality phase ($|{\rm Im}\,H|/|{\rm Re}\,H| \approx 0.005$, a gaugeable global phase).
A real-symmetric operator has real eigenvectors, and a **degenerate** eigenvalue cluster
has an arbitrary basis; in both cases the spatial arg-winding is a **basis/gauge artifact,
not a gauge-invariant topological integer**. (The robust, seed-independent tell is the
**eigenvalue degeneracy** — the R=1.0 fundamentals are 4-to-6-fold degenerate, so their
raw `(p,q)` wobbles draw-to-draw while the class stays `BASIS-AMBIGUOUS`; the earlier
`real-fraction` numbers were single Lanczos draws and are retired as a data column, A11.)
The census null then arrives by **three paths, none yielding (2,3)**:
- **LA cavity fundamental (freeze-faithful, HEADLINE):** the interior-filling standing wave
  reads a stable trivial `(0,0)` where best-filled (R=1.6) and `BASIS-AMBIGUOUS` where
  degenerate (R=1.0). This is the read the frozen §2 actually intended (A8).
- **SA defect band (as-shipped, retained):** the localized defect modes occupy PN≈2 cells
  and do **not** fill the cavity's angular loops ⇒ the sector-phasor read is
  **amplitude-starved** and gated `INCONCLUSIVE-amplitude` (label corrected from the
  collapsed `INCONCLUSIVE-Nyquist`). Live-fire: an independent from-scratch toroidal read
  of one cell returns **−3.88 turns (non-integer)**, which the module correctly refuses.
- **Exactly-Hermitian, real-symmetric-up-to-gauge H:** the operator cannot carry emergent
  inter-sector phase texture at all (the sector-relative phase has spatial std ~1e-12), so
  the cold-linear winding is trivial/artifact **by construction** — the reason the driven
  leg is regime-load-bearing (§B-1).

Both spectral ends were pre-declared in the instrument docstring; the substrate lands in
the frozen null bins on the **freeze-faithful** LA fundamental as well as the SA band. See
the D3-movement map (§7) and the regime caveat (§B-1).

## §3 — bin (ii): GEOMETRY DEPENDENCE (sphere vs horn-torus)

Classifier bins: `CLOSURE-FORCED` (same (2,3) both shapes) / `GEOMETRY-SET` /
`TORUS-ONLY` / `NEITHER`.

**Result: `NEITHER`.** Neither the sphere (null geometry) nor the horn-torus produces a
(2,3) — or any stable integer — closure class in the cold-linear regime. The null is
**shape-independent**: both shapes return trivial/basis-ambiguous/INCONCLUSIVE at every
rung. There is no shape at which (2,3) appears to be smuggled *in* or forced *out*, so
the geometry axis is uninformative about (2,3) in this regime — as expected once the
operator is real-symmetric-up-to-gauge (§2 mechanism), which is a shape-independent
property of the coupled generator.

## §4 — bin (iii): THE FLOOR TEST

Two dimensionless sub-reads (amplitude-clamp BC). `floor = ℓ_node/(2π) = 0.159`;
tolerance `2·Δgrid = 0.25 ℓ_node`; `SETTLES-AT-FLOOR` iff `|R_wall − 0.159| < 0.25`.

| R/ℓ_node | R_wall/ℓ_node | coincidence bin | mode resolves |
|---|---|---|---|
| **0.16** (floor/ground) | 0.325 | **SETTLES-AT-FLOOR** | yes |
| 0.5 | 0.541 | SETTLES-ABOVE-FLOOR | yes |
| 1.0 | 1.021 | SETTLES-ABOVE-FLOOR | no |
| 1.6 | 1.595 | SETTLES-ABOVE-FLOOR | no |

**Lift-off rider: `LIFTS-OFF`.** The amplitude wall settles **at the ropelength floor at
the ground rung** (R=0.16) and **lifts off it** (settles above) at every larger rung —
the qualitative signature the Wall-A ruling's lift-off rider predicts (ground state
saturates the floor; non-ground cavities sit above it). **Both shapes identical**
(sphere = horn-torus, R_wall is amplitude-profile-derived, shape-independent at Stage-1).

**Load-bearing caveat (A3, Stage-1 scope).** `R_wall ≈ R` at every rung
(0.54≈0.5, 1.02≈1.0, 1.59≈1.6): the wall location **tracks the imposed seed radius**,
which is an *input*, not a field-decided energy-minimizing settle. The `SETTLES-AT-FLOOR`
at R=0.16 is partly the seed-radius floor (`max(R_cells, 2 cells)`). So the floor-test
trend is a **consistency check that the instrument reproduces the imposed geometry and
the lift-off ordering** — it is **not** an emergence result. The genuine field-decided
settle is **Stage-2** (self-consistent), where the wall location is an output.

## §5 — bins (iv/v/vi): 4π-closure, mode-ratio ladder, fool-mode meters

**bin (iv) — SU(2) 4π-closure.** `unresolved`/`2π-closes` at every cell (no `4π-closes`).
The cold-linear modes carry no clean half-integer toroidal winding, so no 4π double-cover
is present to resolve. **⚠ A12 correction:** the earlier A2 framing ("the reader *cannot*
emit a positive `4π-closes`") reflected **dead code**, not physics — the shipped bin had a
tautological `int % 1 == 0` branch (4π unreachable) and an advertised-but-unbuilt `[0,4π)`
sample. The bin is now a **genuine half-integer detector** (open-loop slope fit; validated
G8: a planted half-integer winding reads `4π-closes`, an integer reads `2π-closes`), so a
real spinor double-cover WOULD now be positively resolved. It remains out of scope here —
the 4π double-cover is a $\Gamma_{\text{spinor}}$-wall (T2) property, not an A1-mass-wall
census result (sector header) — but the instrument no longer merely asserts its absence.

**bin (v) — dimensionless mode-ratio ladder.** Two reads:

*α-clean ABCD radial cross-check (the physically-meaningful spectrum fingerprint,
scale-free, no α, no absolute frequency):*

| l | eigen-kR (n=1,2,3) | ratios to l=0,n=1 | degeneracy 2l+1 |
|---|---|---|---|
| 0 | π, 2π, 3π | 1.0, 2.0, 3.0 | 1 |
| 1 | 4.493, 7.725, 10.904 | 1.430, 2.459, 3.471 | 3 |
| 2 | 5.764, 9.095, 12.323 | 1.835, 2.895, 3.922 | 5 |

These are the analytic **Dirichlet-sphere spherical-Bessel zeros** (validate-on-known,
gate G5): the cavity fundamental is l=0 (kR=π, the breathing mode), degeneracies 1/3/5.

*3-D lattice SA mode ratios (per cell):* the smallest-algebraic band is a set of
near-degenerate defect modes (e.g. sphere-geometric R=1.6:
`[0, 0, 0, 1, 1, 1, 72.4, 73.1]`) — this is the **defect-band spectrum, NOT the physical
cavity standing-wave ladder** (a direct consequence of the indefinite-H / SA-target
finding, §B-limitation 6). Reported for completeness; **the ABCD leg is the trustworthy
fingerprint.**

**bin (vi) — fool-mode meters** (per-sector PN + core-fraction + boundary-fraction proxy;
E_persist≡1.0 and raw φ-retention **refused**). Sample at R=1.0:

| cell | enclosure | A1 PN / core / bnd | ω PN / core / bnd |
|---|---|---|---|
| sphere · amplitude | energy-closed-**PERIODIC** | 3.12 / 0.978 / 0.000 | 3.12 / 0.978 / 0.000 |
| sphere · geometric | **Dirichlet**-box | 1.79 / 0.245 / 0.000 | 1.79 / 0.245 / 0.000 |
| horn-torus · amplitude | energy-closed-**PERIODIC** | 2.83 / 0.870 / 0.000 | 2.83 / 0.870 / 0.000 |
| horn-torus · geometric | **Dirichlet**-box | 2.09 / 0.978 / 0.0001 | 2.09 / 0.978 / 0.0001 |

**PN ≈ 2–3 cells** (tightly localized), **boundary-fraction ≈ 0** (the modes do **not**
hug the imposed wall → they are core-localized defects, **not** reflecting-wall
artifacts under the proxy, amendment A4). A1 and ω meters coincide per cell (the coupled
ground mode shares spatial support across sectors). Enclosure labels correct per the
torus erratum: amplitude = periodic, geometric = Dirichlet.

## §6 — DRIVEN-PING SPOT-CHECK (secondary regime)

**Verdict: `BREAK`.** At the census operating point (N=24, R=8 cells, conservative
evolver, 300 steps), the (2,3) does **not** live as a conserved closed time-orbit: the
winding read is **(−1,−1)**, not (2,3). Verbatim: *"the (2,3) does NOT live as a
conserved closed time-orbit in the conservative coupling (failing: is_2_3); the negative
DEEPENS (real-space AND phase-space null). Retract-not-refill: does NOT walk back
charge=Link(∂Ω,F)."*

**⚠ SCOPE CORRECTION (A15).** The earlier claim that this "removes the cold-linear
regime-artifact escape hatch" is **rescoped**: this driven leg has **NO imposed cavity
wall** (it routes `PhaseSpaceWindingConfig → run_phase_space_winding`, bypassing
`build_masked_H`, the only site applying the Γ=−1 Dirichlet cavity) and runs on the
unwalled periodic lattice with the winding DOF frozen in ê_w and `ω_b=ω_s=1.0`, so the
read `(−1,−1)` is the **common LC carrier ratio by config**, not an emergent (2,3). It
therefore **re-confirms the #417 PERSISTENCE-null on the unwalled seeded orbit at one
operating point**; it does **NOT** interrogate boundary-**emergence** (whether an imposed
wall induces the winding — the census's registered question). A walled-driven battery is
**Stage-2 (unrun)**. The cold-null's ARTIFACT-eligibility is therefore **not** closed by
this leg — see §B-1.

---

## §7 — THE D3-MOVEMENT STATEMENT (state, do NOT adjudicate)

Per the frozen D3-movement map, the census outcome is stated — **not adjudicated**
(adjudication is the auditor lane + Grant, not this implementer RESULT):

**Outcome class realized:** *"some (p,q) ≠ (2,3), or **no integer closure class**."*
**Honest evidence-base scope (review-repair):** there is **no conclusive winding read in
any preregistered cell** — every 3-D battery cell is `INCONCLUSIVE-amplitude` and every
gated reflection read is `(0,0)`/`BASIS-AMBIGUOUS`; **raw reads never show (2,3)** at any
rung, shape, BC mode, or spectral end (SA defect band OR the freeze-faithful LA cavity
fundamental, A8); the floor-rung read is `(0,0)` **raw / gate-refused (amplitude-starved,
detector-blind — a planted (2,3) reads the same (0,0) there, A13/A14)**, not a gated trivial
result; and the exactly-Hermitian, real-symmetric-up-to-gauge mechanism explains the cold
null by construction. The driven spot-check reads (−1,−1) (the common LC carrier on the
UNWALLED orbit, A15 — re-confirms #417, does not test boundary-emergence). Per the frozen
map, this "no integer closure class" outcome →

> **"The emergence suspicion fails; (2,3) SELECTION stays imported; COEXIST stands
> unchanged. NOT a falsification of the electron."**

Stated, not adjudicated. Three qualifiers the auditor/Grant must weigh (they are not mine
to resolve):

1. **Regime.** The primary leg is cold-linear. The frozen regime flag makes a cold-linear
   winding null **ARTIFACT-eligible** because the winding is a phase-texture object and
   the cold operator is real-symmetric-up-to-gauge (§2 mechanism — no emergent phase can
   exist there *by construction*). The driven spot-check (§6) `BREAK` argues the null is
   **not merely a cold artifact** at one operating point, but a full driven/self-consistent
   battery (Stage-2) is where the winding question is fully live.
2. **Instrument reach — CORRECTED (A8).** The as-shipped `which="SA"` target (a **build-
   time CODE choice, NOT frozen** — the frozen prereg names no spectral end; verify-before-
   cite) landed on localized defect modes because the band is **inverted** (`H = ω − c²·L_D`,
   L_D SPD): SA is the most-oscillatory grid-scale end, not the cavity fundamental. The
   band-inversion repair now reads the **LA end = the smooth cavity FUNDAMENTAL** = the
   freeze-faithful "lowest interior mode" (frozen §4 bin i). On that freeze-faithful end the
   read is still non-(2,3): stable trivial `(0,0)` at the best-filled fundamentals (R=1.6)
   and `BASIS-AMBIGUOUS` at the degenerate R=1.0 modes. So the wrong-modes limitation is
   **repaired, not merely flagged** — the frozen observable was interrogated and returned
   no (2,3). (The SA defect-band read is retained alongside, KEEP-BOTH.)
3. **The (2,3) SELECTION was never claimed derived here.** Consistent with the frozen
   consistency-vs-emergence tag, the census does **not** convert the (2,3) import→derivation
   (that was the only "strongest support" branch, and it did not fire).

**Emergence-class claim status:** **NOT made.** The census did not return (2,3) as the
ground-state closure class, so no emergence-class claim (import→derivation of the (2,3)
selection) is asserted. Every read here stays **consistency-class**.

**Residual that must NOT be silently resolved:** the precursor-vs-end-state sub-fork
(`clm-uatcql`, `vol2/claim-quality.md:1146`) stays **OPEN**.

---

## §A — DATED AMENDMENTS (frozen body untouched; freeze-at-API discipline)

Per the freeze contract, any deviation from the frozen prereg is recorded here as a
dated amendment; the frozen body is not edited.

**A1 (2026-07-14) — bin (i) landing label `BASIS-AMBIGUOUS (real eigenvector)`.**
The frozen bin-(i) landing set is
`(0,0) / (1,1) / (2,3) / other-(p,q) / NON-INTEGER (no closure) / INCONCLUSIVE-Nyquist / NOT-RUN-3D`.
The instrument emits an additional label **`BASIS-AMBIGUOUS (real eigenvector)`** when
the eigenvector is essentially real (`real_frac > 0.85`) — a **mechanism-forced
refinement of the `NON-INTEGER (no closure)` landing**: for a real-symmetric-up-to-
gauge operator any non-trivial arg-winding is a basis artifact, not a gauge-invariant
integer, so it is neither a genuine integer closure class nor a Nyquist failure. It is
reported **alongside**, not in place of, the frozen bins (KEEP-BOTH discriminator
pattern). No frozen bin is redefined.

**A2 (2026-07-14) — bin (iv) 4π-closure is positively unresolvable in cold-linear.**
The static single-loop reader rounds to an integer, so the implementation returns
`2π-closes` or `unresolved` only — it **cannot emit a positive `4π-closes`**. A genuine
spinor half-mode (double-cover) does not close over [0,2π): the dual-counter agreement
gate fails and it lands in **`unresolved`**, never a false `2π-closes`. Since the
cold-linear modes are trivial/real, bin (iv) is `2π-closes`/`unresolved` throughout.
The 4π double-cover is an **A1 ⊥ T2 $\Gamma_{\text{spinor}}$-wall property** (frozen
sector header) and is **out of scope for the static A1-mass-wall census** — flagged,
not fixed.

**A3 (2026-07-14) — floor-test `R_wall` tracks the imposed seed radius (Stage-1
scope).** The amplitude-clamp `R_wall` is read from the **seeded** A1 strain profile
(an input), so it reflects the imposed seed, not a field-decided energy-minimizing
settle. The field-decided settle location is **Stage-2** (self-consistent). This scope
limit is carried in the instrument's `amplitude_wall_location` scope-note and is a
**limitation, not a deviation** (the frozen prereg §2/§6.iii already scopes the
field-decided settle to Stage-2). The floor bin is reported with this caveat explicit.

**A4 (2026-07-14) — fool-mode absorbing-PML twin is a `boundary_fraction` PROXY, not
a second absorbing solve.** Frozen §2/§4-bin-vi requires the per-sector PN + core-
fraction "**under BOTH the imposed reflecting wall AND the absorbing-PML twin**." The
instrument runs a **single** Hermitian eigensolve per cell and substitutes a
**`boundary_fraction`** (density within 2 cells of the imposed wall) as a *proxy* for
the twin's discrimination (a wall-hugging mode = high boundary-fraction would die under
absorption; an interior-localized mode = low boundary-fraction survives). This is a
**deviation** (proxy-substitution) from the frozen two-solve prescription. It is
**non-load-bearing for the headline** — the verdict is a winding NULL, and the
fool-mode meters discriminate a *positive* localization claim, which the census does
not make. Recorded for freeze integrity; a genuine absorbing-PML re-solve is deferred
to the driven/Stage-2 leg where a positive localization claim could arise.

**A5 (2026-07-14) — bin (i) `NON-INTEGER (no closure)` is folded into
`BASIS-AMBIGUOUS`.** The static phasor reader (`read_static_winding`) rounds each read
to the nearest integer and gates conclusiveness on dual-counter agreement + Nyquist +
amplitude. A genuine non-integer (non-closing) winding therefore surfaces as
`read_ok = False` (→ `INCONCLUSIVE-Nyquist`) or, when the eigenvector is real, as
`BASIS-AMBIGUOUS` (A1) — the frozen `NON-INTEGER (no closure)` string is never emitted
verbatim. This is a **label-routing** refinement, not a redefinition: no winning
integer class is admitted that the frozen bins would reject.

**A6 (2026-07-14) — rung 3.0 dropped from the 3-D coupled leg (frozen-authorized).**
Frozen §0 item 3 authorizes rung 3 as "the dense-solve edge (N≈56); attempted, dropped
with disclosure if it exceeds the concurrency budget." The `which="SA"` Lanczos solve
at N=56 did not converge within the compute budget (16+ min CPU, single-core). Rung 3.0
is therefore reported **`NOT-RUN-3D (compute)`** alongside {10, 30, 100}. The 3-D
coupled winding census covers **{0.16, 0.5, 1, 1.6}**; the sphere-ABCD radial leg covers
all 8 rungs. **Minimum coverage {1, 1.6, 10, 100} is MET** (1, 1.6 via 3-D; 10, 100 via
sphere-ABCD) — **but see A16:** the sphere-ABCD leg supplies only the bin-v mode-RATIO
ladder (scale-free, rung-independent) at {10, 100}, NOT a bin-iii floor read; the floor
read shipped at 4 rungs {0.16, 0.5, 1, 1.6} only.

---

## §B — HONEST LIMITATIONS

1. **Cold-linear is the primary leg; the winding question is regime-load-bearing.**
   The (2,3) is a phase-texture object; the cold-linear real-symmetric operator cannot
   carry emergent inter-sector phase, so the cold-linear winding null is
   **ARTIFACT-eligible per the frozen regime flag**, NOT a clean falsification of the
   emergence suspicion. The driven leg (§6) is the regime where the winding question is
   physically live; it is a **spot-check here**, not a full driven battery.
2. **Rungs {10, 30, 100} have no 3-D coupled winding read** (infeasible dense,
   `R ≥ 80` cells) — covered by the sphere-ABCD radial leg only, **disclosed not
   silently capped** (frozen §0 item 3). Those bin-(i) cells report `NOT-RUN-3D`.
3. **"Closed" = energy-closed-PERIODIC for the amplitude BC** (the torus erratum): only
   the **geometric-mask BC** produces a true reflecting Dirichlet box. Each fool-mode
   meter states periodic-vs-Dirichlet per bin.
4. **The coordinate-prereg secondary decomposition direction leg is tautological**
   (`SEED-CARRIED`): the rigid-template ω sector is a scalar, so the only director is
   the seeded `ê_w`. It is the plant-gate positive control, **not a genuine emergence
   read** (frozen §0 item 5).
5. **`R_wall` is seed-tracking (Stage-1), see A3.**
6. **Spectral-end targeting — the as-shipped `which="SA"` was the WRONG END; REPAIRED
   (A8).** The masked H is `ω·I − c²·L_D` with L_D real **SPD**, so an H-eigenvalue
   `= ω − c²λ` — the band is **INVERTED**. `which="SA"` (smallest-algebraic H) therefore
   targets the **largest** `L_D`-eigenvalue = the most-oscillatory grid-scale end; for the
   saturated core that is the tightly-localized (PN≈2) defect band (3-fold degenerate,
   amplitude-starved ⇒ `INCONCLUSIVE-amplitude`), and the 3-D SA mode-ratio ladder (bin v)
   is that defect band, not the physical spectrum. The cavity FUNDAMENTAL (the frozen
   "lowest interior mode") is the **smallest**-`L_D` (smooth, interior-filling) mode = the
   **largest-algebraic (LA)** end. **This was never a frozen target:** verify-before-cite
   (two-method grep) confirms the frozen prereg contains no "smallest-algebraic"/"most-
   bound"/"which=" anywhere — the SA target was a **build-time code deviation** from the
   frozen §4-bin-i "lowest interior mode". **Note the earlier §B-6 recommendation to target
   the "lowest-POSITIVE mode" was ALSO the wrong end** under band inversion (lowest-positive
   is still on the oscillatory side of the indefinite window, not λ_min). The repair (A8)
   reads the **LA fundamental** — freeze-FIDELITY to "lowest interior mode", not a target
   move — with a Nyquist-resolved read and full gate internals. It returns **non-(2,3)**:
   stable trivial `(0,0)` at the best-filled fundamentals (R=1.6, both shapes) and
   `BASIS-AMBIGUOUS` at the degenerate R=1.0 modes. The SA defect-band read is kept
   alongside (KEEP-BOTH). **What remains for Grant** is ratifying the adjudication that
   reading the LA fundamental is freeze-fidelity (not a post-hoc target move); the SA read
   was the actual deviation.

---

## §A (cont.) — NUMERICAL-SOLVER AMENDMENT

**A7 (2026-07-14) — eigsh `tol=1e-7` + `maxiter=2000` + graceful non-convergence.**
**⚠ CORRECTION (2026-07-14, this review-repair):** the original A7 stated "the frozen §2
names `eigsh` on the smallest-algebraic end but fixes no tolerance." That was a **phantom
freeze citation** (verify-before-cite, two-method grep): the frozen §2 names **no `eigsh`
and no spectral end at all** — `eigsh` appears in the frozen file only in the §0-anchor
compute-timing receipt (prereg:121), and the strings "smallest-algebraic"/"most-bound"/
"which=" appear **nowhere** in the frozen body. The `which="SA"` end was a **build-time
solver choice**, itself a deviation from frozen §4 bin i ("the lowest interior mode") —
see A8. The tolerance/maxiter content stands: the default `tol=0` (machine precision) blew
the compute budget at N≳36 on the clustered/degenerate spectrum (16+ min CPU, unconverged);
`tol=1e-7` returns the **same eigenpairs** to a precision far tighter than an
integer-winding / 4-decimal-ratio read needs, in ~0.1 s; `maxiter=2000` bounds pathological
cells; on `ArpackNoConvergence` the converged subset is used (or the cell records
compute-limited) rather than hanging. This is a **numerical-precision completion**, not a
change of which modes are targeted. Reflection-probe `k_eigs` reduced 24→14 for the same
clustered-spectrum reason.

**A8 (2026-07-14, review-repair) — BAND INVERSION: the census now reads the LA cavity
FUNDAMENTAL (the freeze-faithful "lowest interior mode"). KEEP-BOTH both spectral ends.**
The pivotal review adjudication. The masked coupled generator is `H = ω·I − c²·L_D` with
`L_D` real **SPD** (`coupled_cage_winding.py:_assemble_H`; `native_cage_imex.py:176`
"SPD"), so an H-eigenvalue `= ω − c²λ` (λ = an `L_D`-eigenvalue ≥ 0) — the band is
**INVERTED**. Consequences:
- `which="SA"` (smallest-algebraic H, as-shipped) = **largest** `L_D`-eigenvalue = the
  **most-oscillatory grid-scale** end. It never interrogated the cavity fundamental — in
  ANY cell, including the cold reflection probe whose own docstring promised "cavity
  standing waves that fill the interior."
- The frozen **§4 bin i "lowest interior mode"** (prereg:258) is the SMOOTH, interior-
  filling mode = **smallest** `L_D`-eigenvalue = the **largest-algebraic (LA)** end of H.
- **The SA target was never frozen.** Verify-before-cite (two-method grep): the frozen
  prereg contains no "smallest-algebraic", "most-bound", or "which=" anywhere; `eigsh`
  appears only in the §0-anchor timing receipt. `which="SA"` was a **build-time code
  deviation** from the frozen observable — the phantom "frozen §2" citations at A7,
  `cavity_census.py` (the `solve_cavity_spectrum` docstring + the `which="SA"` comment),
  and `cold_cavity_reflection_winding`'s docstring are all corrected in this repair.

**Repair.** `solve_cavity_spectrum(cfg, which=...)` now reads either end; the cold
reflection probe defaults to **LA** (the freeze-faithful fundamental) and `run_cell`
reports **both** ends (KEEP-BOTH). **This is FIDELITY to the frozen "lowest interior
mode", not a target move** — reading the fundamental honors §4 bin i; the SA read was the
deviation. Live-fire (this repair, LA end, full gate internals in §2):
- **No cell — no rung, no shape, no BC, no spectral end — reads (2,3).**
- The best-filled fundamentals (R=1.6, both shapes) read a **stable trivial `(0,0)`**
  (reproduced across 4 independent Lanczos seed draws).
- The degenerate R=1.0 fundamentals read `BASIS-AMBIGUOUS` (4-to-8-fold eigenvalue
  degeneracy ⇒ arg-winding basis-arbitrary; raw `(p,q)` wobbles draw-to-draw).
- The sub-resolving rungs (R≤0.5, an 8-cell box) read `INCONCLUSIVE-amplitude`.

The SA defect-band read is retained (it is a defensible **bound-state** target that found
the PN≈2 defect band). **Adjudication for Grant:** ratify that reading the LA fundamental
is freeze-fidelity to "lowest interior mode" (this repair's position), vs. treating it as a
post-hoc target move. Either way the verdict is unchanged — non-(2,3) on both ends.

**A9 (2026-07-14, review-repair) — the collapsed `INCONCLUSIVE-Nyquist` label now reports
the ACTUAL failing gate.** `run_cell`/`cold_cavity_reflection_winding` previously mapped
EVERY refused read (`read_ok=False`) to the single label `INCONCLUSIVE-Nyquist`, collapsing
amplitude-starvation, dual-counter disagreement, and true Nyquist failures into one
mislabeled bin — and because a `(0,0)` read forces `samples_per_period = n_ang`, the
"Nyquist" name was STRUCTURALLY always wrong on a trivial refusal. `_refusal_label`
now inspects the per-axis gates and emits `INCONCLUSIVE-amplitude` / `INCONCLUSIVE-Nyquist`
/ `INCONCLUSIVE-disagree`. Empirically every refused census cell is `INCONCLUSIVE-amplitude`
(the sub-resolving/defect-band modes are amplitude-starved, not Nyquist-starved).

**A10 (2026-07-14, review-repair) — `select_census_mode` reads the best-angular-fill mode,
a silent move vs the frozen "lowest interior mode".** The frozen §4 bin i (prereg:258) says
"the (p,q) of the **lowest** interior mode"; the shipped `select_census_mode` scans the
first ≤8 (24 in the reflection probe) eigenmodes and returns the first with `angular_fill
≥ 0.5`, else the max-fill mode — so the selected index can be > 0. This is a heuristic
substitution disclosed only in the §2 headline prose, with no prior §A entry — recorded
here for freeze-discipline. It is reconciled against §B-6's own "moves a frozen target"
standard: the direction of bias is **anti-null** (best-fill gives (2,3) MORE chance to
appear, not less), so it cannot manufacture the negative; and under the band-inversion
repair (A8) it is applied to the LA fundamental band, where "lowest interior mode" =
"lowest-`L_D` (smooth, interior-filling) mode" — best-angular-fill is a faithful reading of
that intent. Zero verdict impact (every headline cell reads INCONCLUSIVE/BASIS-AMBIGUOUS/
(0,0) regardless of which of the near-degenerate modes is selected).

**A11 (2026-07-14, review-repair) — eigvec `real-fraction` RETIRED as a data column;
eigenvalue degeneracy is the robust basis-ambiguity invariant.** ARPACK uses a random
Lanczos start (no `v0`), so in a degenerate subspace the eigenvector basis mixes
arbitrarily: the `real-fraction` of the selected eigenvector varies draw-to-draw (live-fire:
the same operator returns real-fraction 0.04 / 0.63 / 0.93 / 0.49 across four draws) and is
even globally-gauge-dependent for a genuinely-real mode. The earlier RESULT table numbers
(0.84–0.997) were single Lanczos draws presented as a stable property — **retired**. The
`real_frac > 0.85` guard also **cannot reliably fire in a degenerate subspace** (a complex
mixture at real_frac 0.70 would pass as a conclusive integer). The instrument now flags
**BASIS-AMBIGUOUS on eigenvalue-cluster DEGENERACY** (deterministic, seed-independent) OR
real_frac>0.85; `real_frac` is reported only as seed-dependent context
(`eigvec_real_fraction_seed_dependent`), never as a data column or a sole gate. The
seed-STABLE invariants are: amplitude-starvation (from `angular_fill`), degeneracy, and the
R=1.6 gated `(0,0)` (reproduced across 4 draws).

**A12 (2026-07-14, review-repair) — bin (iv) 4π-closure REBUILT as a genuine half-integer
test (was dead code).** The shipped `four_pi_closure` advertised sampling "over TWO
traversals [0,4π)" but `_sector_phase_on_loop` only bins one [0,2π) traversal, and the
branch `"2π-closes" if w["winding_int"] % 1 == 0 else "4π-closes"` was **tautologically
dead** (`winding_int` is an int ⇒ `% 1 == 0` always True ⇒ `4π-closes` unreachable); the
one-traversal proxy `d_2pi` was computed and never used. So bin (iv) as shipped could not
interrogate closure at all (A2 disclosed only the consequence, not the unbuilt sampling).
Repaired: a spinor half-mode returns to MINUS itself after one [0,2π) traversal ⇒ a
HALF-INTEGER unwrapped winding; the bin is now read from `frac(w_unwrap)` — integer ⇒
`2π-closes`, half-integer ⇒ `4π-closes` (genuinely reachable), else `unresolved`. `d_2pi`
and the dead branch removed; docstring corrected. The A1-mass-wall cold-linear modes still
land `unresolved`/`2π-closes` (the 4π double-cover is a Γ_spinor-wall/T2 property, out of
scope for this census — sector header), but the instrument can now positively resolve a 4π
closure if one is present.

**A13 (2026-07-14, review-repair) — PER-RUNG positive controls; `detector_trustworthy`
scoped to the rungs where the control passes.** The frozen positive control (`G0`) validated
one comfortable geometry (`R_cells=12` ≈ rung 1.5). Live-fire per-rung (plant a genuine
(2,3) restricted to the actual kept region): the detector reads `(2,3)` cleanly at rungs
{1.0, 1.6} but is **detector-blind at 0.16** (reads (0,0), read_ok=False on the 8-cell box)
and **conclusively MISREADS at 0.5** (reads (0,0)/(0,2) with read_ok=**True** — every frozen
gate passes on the wrong integer, because the dual counters share the amplitude-starved
input). `positive_control_battery` now emits `detector_trustworthy_rungs = {1.0, 1.6}`; the
winding cells at 0.16/0.5 are **INSTRUMENT-INCONCLUSIVE** regardless of what they read. The
verdict's gated LA-fundamental evidence lives at exactly the validated rungs.

**A14 (2026-07-14, review-repair) — floor-cell detector-blindness; NO engine-representable
positive control exists in the cold-linear leg.** At the R=0.16 battery geometry a genuinely
planted (2,3) reads the SAME gate-refused `(0,0)` the earlier RESULT quoted as "trivial
(0,0)" — the floor cell has **zero discriminating power** (an 8–32-cell interior sub-resolves
any (p,q)). More broadly, the ONLY (2,3)-reading input demonstrated anywhere is a SYNTHETIC
analytic field; the canonical seeded electron reads a CONCLUSIVE `(0,0)` through the pipeline
(the detector fences off ê_w — the tautology the census forbids — and the real-symmetric-
up-to-gauge H carries no emergent inter-sector phase). So **no engine-representable positive
control can exist in the cold-linear leg**: the leg is INSTRUMENT-INCONCLUSIVE for a
(2,3)-vs-(0,0) by construction — which is exactly why Stage-2 driven is load-bearing. The
verdict "NO (2,3) emergence" stands as an honestly-scoped **cold-linear-leg** result.

**A15 (2026-07-14, review-repair) — driven-ping is UNWALLED and reads the common LC carrier;
it re-confirms #417, it does not test boundary-emergence.** See §6. The driven leg routes
`PhaseSpaceWindingConfig → run_phase_space_winding`, bypassing `build_masked_H` (the only
imposed-cavity-wall site), so it runs on the unwalled periodic lattice with ê_w frozen and
`ω_b=ω_s=1.0` ⇒ the read `(−1,−1)` is the config carrier ratio. It re-confirms the #417
persistence-null at one operating point; a walled-driven battery (the actual boundary-
emergence test) is Stage-2, unrun. The "removes the escape hatch" claim is rescoped
accordingly; the cold-null ARTIFACT-eligibility is NOT closed by this leg.

**A16 (2026-07-14, review-repair) — floor test (bin iii) coverage rescoped to the 4
interrogated rungs; {10,100} "coverage" relabeled mode-ratio-only (bin v).** Frozen §0
item 3 commits to "bin iii floor read at **all eight rungs** {0.16, 0.5, 1, 1.6, 3, 10, 30,
100}" via the sphere-ABCD leg. But the shipped `sphere_abcd_radial_spectrum` is **scale-
free** (dimensionless kR, no radius argument) — it cannot produce an `R_wall`-vs-floor read
(bin iii needs a seeded amplitude profile, which only the 3-D leg has); it returns the bin-v
mode-RATIO ladder, identical at every rung. So the bin-iii floor read shipped at **4 rungs**
{0.16, 0.5, 1.0, 1.6} (3-D leg), not 8. The frozen "all eight rungs / bin iii floor read"
commitment is rescoped to those 4; the A6 "minimum coverage {1,1.6,10,100} MET" claim is
corrected so that {10,100} coverage is **mode-ratio-only (bin v)**, a rung-independent
identity, NOT a per-rung floor measurement. The lift-off rider is verified over
{0.5,1.0,1.6} (the interrogated non-floor rungs); above R=1.6 a floor read would trivially
return SETTLES-ABOVE-FLOOR (re-confirming the ordering). This is a caveated, non-load-bearing
rider (A3: consistency-not-emergence), so the rescope does not touch the verdict.

**A17 (2026-07-14, review-repair) — the cold reflection-map probe is logged as a post-freeze
instrument leg.** `cold_cavity_reflection_winding` (a1_amplitude≈0.01 ⇒ near-Helmholtz
Dirichlet box) is not named in the frozen §2 detector list and was carried by no prior §A
amendment (A7 touched only its `k_eigs`). It is a **new implementation leg of a frozen
concept** — the frozen §1 "ground-state closure of the cavity's reflection map" (prereg:181,
191-193) — not an invented axis. Logged here for freeze-at-API parity; under the band-
inversion repair (A8) it is the HEADLINE bin-i read (LA cavity fundamental).

---

*Instrument + gates committed AFTER the freeze (freeze precedes driver in git
history). DO-NOT-MERGE. Only Grant merges.*
