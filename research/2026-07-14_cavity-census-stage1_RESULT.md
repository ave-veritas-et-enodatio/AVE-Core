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

**`detector_trustworthy = TRUE`.** The pytest gate suite (`test_cavity_census.py`,
G0–G6) is green: 7 fast gates + 1 engine_sim cell test, 8/8 pass.

---

## §2 — bin (i): GROUND-STATE WINDING CLASS (per shape × BC × R)

**Headline read** — the eigenvector two-sector Clifford phasor winding (canonical,
HEADLINE) of the ground / best-angular-fill interior mode, per shape × BC × R.

| R/ℓ_node | sphere · amplitude | sphere · geometric | horn-torus · amplitude | horn-torus · geometric |
|---|---|---|---|---|
| **0.16** (floor) | INCONCLUSIVE-Nyquist | INCONCLUSIVE-Nyquist | INCONCLUSIVE-Nyquist | INCONCLUSIVE-Nyquist |
| **0.5** | INCONCLUSIVE-Nyquist | INCONCLUSIVE-Nyquist | INCONCLUSIVE-Nyquist | INCONCLUSIVE-Nyquist |
| **1.0** | INCONCLUSIVE-Nyquist | INCONCLUSIVE-Nyquist | INCONCLUSIVE-Nyquist | INCONCLUSIVE-Nyquist |
| **1.6** | INCONCLUSIVE-Nyquist | INCONCLUSIVE-Nyquist | INCONCLUSIVE-Nyquist | INCONCLUSIVE-Nyquist |
| **3, 10, 30, 100** | NOT-RUN-3D (compute, A6) | NOT-RUN-3D | NOT-RUN-3D | NOT-RUN-3D |

**No cell returns an integer closure class.** The canonical read on the frozen
smallest-algebraic (most-bound) modes is `INCONCLUSIVE-Nyquist` everywhere: those modes
are tightly-localized defect modes (PN≈2–3 cells, §5-vi) that do not fill the cavity's
angular loops (`angular_fill` 0.15–0.42), so the sector-phasor read is amplitude-starved
and the dual-counter/Nyquist gates refuse it. The raw pre-gate `(p,q)` reads are
inconsistent basis noise (e.g. sphere-amplitude across the ladder: `(6,-3)`, `(8,2)`,
`(1,-4)`, `(-5,12)`) — **never (2,3)**, and not stable.

**Reflection-map probe (the direct "ground-state closure of the cavity's reflection
map" read — a *cold* near-Helmholtz Dirichlet box whose low modes are cavity standing
waves, not saturation-front defects).**

| shape | R/ℓ_node | winding class | raw pre-gate (p,q) | eigvec real-fraction |
|---|---|---|---|---|
| sphere | **0.16** (floor) | INCONCLUSIVE-Nyquist | (0,0) | 0.843 |
| horn-torus | **0.16** (floor) | INCONCLUSIVE-Nyquist | (0,0) | 0.900 |
| sphere | 0.5 | INCONCLUSIVE-Nyquist | (1,−1) | 0.937 |
| horn-torus | 0.5 | INCONCLUSIVE-Nyquist | (3,5) | 0.836 |
| sphere | 1.0 | BASIS-AMBIGUOUS (real eigenvector) | (−2,2) | **0.997** |
| horn-torus | 1.0 | INCONCLUSIVE-Nyquist | — (SA non-conv.) | — |
| sphere | 1.6 | BASIS-AMBIGUOUS (real eigenvector) | (3,−3) | 0.923 |
| horn-torus | 1.6 | INCONCLUSIVE-Nyquist | — (SA non-conv.) | — |

**The reflection-map standing waves are essentially REAL** (real-fraction 0.84–0.997):
their arg-winding is a basis/gauge artifact, not a gauge-invariant integer. **Confirming
tell:** the raw `(p,q)` of the sphere/torus R=1.0 probe *changed* — from `(−1,1)`/`(1,6)`
to `(−2,2)`/basis-ambiguous — when the ONLY thing altered was the Lanczos `k_eigs`
(24→14). A genuine topological integer is invariant to the solver's mode count; a basis
artifact is not. **No probe, at any rung or shape, returns (2,3).** At the **floor rung
(R=0.16) the ground-state closure is trivial `(0,0)` in both shapes.**

**Mechanism (documented, load-bearing; live-fire-verified this session).** The coupled
A1↔ω Hermitian generator is **exactly Hermitian** (`max|H − H^H| = 0` ⇒ real spectrum,
lossless) and **dominantly real-symmetric** — the only imaginary content is the coupling
chirality phase ($|{\rm Im}\,H|/|{\rm Re}\,H| \approx 0.005$, a gaugeable global phase).
A real-symmetric operator has real eigenvectors whose spatial arg-winding is a
**basis/gauge artifact, not a gauge-invariant topological integer**. The census null then
arrives by **two paths, neither yielding (2,3)**:
- **Reflection-map standing waves (cold, near-Helmholtz):** eigenvectors essentially real
  (real-fraction 0.84–0.997) ⇒ winding is **basis-ambiguous** noise (the `k_eigs`-
  dependence of the raw (p,q) is the tell).
- **Saturated-core cells (SA defect band):** the localized defect modes are only ~40%
  real, but they occupy PN≈2 cells and do **not** fill the cavity's angular loops ⇒ the
  sector-phasor read is **amplitude-starved** and gated `INCONCLUSIVE-Nyquist`.
  Live-fire: an independent from-scratch toroidal read of one cell returns **−3.88 turns
  (non-integer)**, which the module correctly refuses.

Both paths were pre-declared in the instrument docstring; the substrate lands in the
frozen null bins. See the D3-movement map (§7) and the regime caveat (§B-1).

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

**bin (iv) — SU(2) 4π-closure.** `unresolved` at every cell. The cold-linear modes carry
no clean toroidal winding (trivial/basis-noise), so neither a 2π nor a 4π closure is
positively resolvable. Per **amendment A2**, the static single-loop reader cannot emit a
positive `4π-closes`; a genuine spinor double-cover would land in `unresolved` (not a
false `2π-closes`). The 4π double-cover is a $\Gamma_{\text{spinor}}$-wall (T2) property,
**out of scope** for this static A1-mass-wall census (sector header).

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
charge=Link(∂Ω,F)."* This **removes the cold-linear regime-artifact escape hatch** for
the winding question at this operating point: the (2,3) fails to emerge in the driven
leg too. **Scope-honest:** this is a **single-operating-point spot-check** (the historical
#417 negative re-confirmed at census scale), not a full driven battery — a complete
driven/self-consistent sweep is Stage-2.

---

## §7 — THE D3-MOVEMENT STATEMENT (state, do NOT adjudicate)

Per the frozen D3-movement map, the census outcome is stated — **not adjudicated**
(adjudication is the auditor lane + Grant, not this implementer RESULT):

**Outcome class realized:** *"some (p,q) ≠ (2,3), or **no integer closure class**."* The
census returns **no integer closure class** in any cell, shape, BC mode, or rung probed;
the driven spot-check reads (−1,−1). Per the frozen map, this outcome →

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
2. **Instrument reach.** The frozen "smallest-algebraic (most-bound)" target lands on
   localized defect modes of an **indefinite** masked H, not cavity standing waves
   (§B-limitation 6). The reflection-map probe (cold near-Helmholtz standing waves) is the
   physically-appropriate read and it too returns non-(2,3) basis noise — but this is a
   **flagged instrument-reach limitation**, not a clean full-strength census.
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
sphere-ABCD).

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
6. **The masked coupled H is INDEFINITE; the frozen "smallest-algebraic (most-bound)"
   target lands on defect modes, not cavity standing waves (load-bearing — flagged, not
   silently fixed).** Empirically the reduced operator's smallest-algebraic band is a set
   of **negative-eigenvalue, tightly-localized (PN≈2) defect modes** at the D=1/S(A)
   saturation front, 3-fold degenerate — **not** the positive-frequency cavity standing
   waves the census intends. Shift-invert σ=0 finds a *different* near-zero cluster, so it
   is not a valid substitute for the frozen SA target. Consequence: the canonical bin-(i)
   read is `INCONCLUSIVE-Nyquist` everywhere (the defect modes are amplitude-starved), and
   the 3-D SA mode-ratio ladder (bin v) is the defect-band, not the physical spectrum. The
   **cold reflection-map probe** (a1_amplitude≈0 ⇒ near-Helmholtz) is the physically-
   appropriate standing-wave read and is reported alongside; it returns non-(2,3) basis
   noise, consistent with the §2 real-eigenvector mechanism. **Recommendation (surfaced,
   NOT self-adopted):** a physically-faithful census should target the **lowest-positive
   (cavity-fundamental) mode**, not the smallest-algebraic end of the indefinite H. This
   would be a **dated amendment / Stage-2 refinement** requiring Grant adjudication (it
   moves a frozen target — I do not adopt it post-hoc to rescue a read).

---

## §A (cont.) — NUMERICAL-SOLVER AMENDMENT

**A7 (2026-07-14) — eigsh `tol=1e-7` + `maxiter=2000` + graceful non-convergence.** The
frozen §2 names `eigsh` on the smallest-algebraic end but fixes no tolerance. The default
`tol=0` (machine precision) blew the compute budget at N≳36 on the clustered/degenerate
spectrum (16+ min CPU, unconverged). `tol=1e-7` returns the **same SA eigenpairs** to a
precision far tighter than an integer-winding / 4-decimal-ratio read needs, in ~0.1 s.
`maxiter=2000` bounds pathological cells; on `ArpackNoConvergence` the converged subset is
used (or the cell records compute-limited) rather than hanging — this is why two
horn-torus reflection probes read `— (SA non-conv.)`. This is a **numerical-precision
completion**, not a change of which modes are targeted (SA preserved). Reflection-probe
`k_eigs` reduced 24→14 for the same clustered-spectrum reason.

---

*Instrument + gates committed AFTER the freeze (freeze precedes driver in git
history). DO-NOT-MERGE. Only Grant merges.*
