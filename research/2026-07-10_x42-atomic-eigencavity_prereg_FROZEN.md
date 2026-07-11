# x42 — THE ATOMIC EIGENCAVITY: hydrogen as an Op6 phase-closure problem — PREREG (FROZEN)

**Date:** 2026-07-10 · **Lane:** implementer · **Branch:** `analysis/x42-atomic-eigencavity`
**Brief (binding):** `_orchestration/2026-07-10_x42-atomic-eigencavity-brief.md`
**FREEZE-BY-PUSH:** this file is committed as its OWN commit and PUSHED to `origin` BEFORE any
derivation/code commit. The git ordering (prereg push timestamp < first code commit) is the freeze
proof, audited later. Nothing below is tuned to data; the marks are computed from
`ave.core.constants` at prereg time and frozen verbatim.

---

## SECTOR HEADER (declared before any substrate claim)

- **MODE:** derivation-from-canon + numerical consistency driver. **NOT engine-fire** — the engine is
  not asked to adjudicate anything; it reproduces the modes of a GIVEN impedance profile. Op6 is
  eigenmode-finding for a given network, never geometry-selection (`src/ave/core/constants.py:212-228`
  α HONEST-SCOPE note: the S₁₁ landscape is FLAT in R·r, S₁₁-min does not select geometry;
  `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md:77`
  Rule-12 Op6-scope re-scope, 2026-07-10). Any sentence crediting Op6 with *selecting* a₀ or the 1/r
  geometry is a scope breach: a₀ falls out as the eigenmode SCALE of the given profile.
- **REGIME:**
  - Hydrogen: cold / linear, deep Regime I. Per-node Ax-4 kernel argument at a₀ is
    `V_Coulomb(a₀)/(m_e c²) = α·(ℓ_node/a₀) = α² ≈ 5.3×10⁻⁵` (deep-linear; the well acts as pure GIVEN
    geometry, saturation `S(A)≈1`). Cross-check `de-broglie-n.md`: `V/V_yield ~ Zα² ≈ 10⁻⁴`.
  - Muonic H: the reduced-mass scaling rides the SAME network as pure GIVEN geometry. The per-node
    Ax-4 argument `V_Coulomb(a_μ)/(m_e c²) = α·(ℓ_node/a_μ) ≈ 9.9×10⁻³` is STILL deep-linear (lattice
    rupture scale = `m_e c²`, a lattice property, not the muon's). BUT the brief §3 named check
    `A = E_Coulomb(a_μ)/E_yield` (dielectric-yield reference `E_yield = e·V_YIELD = 43.65 keV`) is
    `A ≈ 0.12` — O(0.1), decidedly NOT deep-linear like H's ~10⁻⁴. Whether the near-nucleus field
    ADDITIONALLY biases the lattice at the muonic scale is the X41 frozen tie (deliverable 5), NOT a
    spectral-correction claim here.
- **SECTOR:** the probe's de Broglie / matter-wave channel on the `Z₀` radial transmission line (the
  bulk-modulus / longitudinal soliton dispersion of `de-broglie-standing-wave.md`). The nuclear dress
  is longitudinal, source-slaved (bin 3 of walk (a): `|Γ|=1` at ω→0, radiates nothing). **A1 ⊥ T2**
  ownership respected; **charge = Cosserat (2,3) winding, untouched** by any mode-count integer here.

---

## FROZEN REPRODUCTION MARKS (consistency-class, NOT chords)

Canon already recovers `E_n` and `a₀` as consistency checks (`clm-oltvwy`,
`de-broglie-standing-wave.md`) — that is the CANONICAL CEILING. These marks are the analytic
expectations the phase-closure/ABCD driver must reproduce. All values from `ave.core.constants`
(`A_0`, `RY_EV`, `M_E`, `M_PROTON`) + `M_MUON` (added in commit #3, value frozen below).

### Reduced-mass convention (declared BEFORE running, per brief M1)

- **M1 / M2 adopt the INFINITE-nuclear-mass convention** (`E_1 = −RY_EV`, `a₀ = A_0`). This matches
  canon (`de-broglie-standing-wave.md` uses `E_n = −m_e c²α²/(2n²)`, infinite-mass Rydberg).
- **M3 adopts the REDUCED-mass convention** explicitly, because `m_μ` is NOT negligible against
  `m_p` (`m_r,μ/m_e = 185.84`, a ~0.54% correction on the electron side becomes a ~186× shift on the
  muon side). `m_r,μ = m_μ m_p/(m_μ + m_p)`; `m_r,H = m_e m_p/(m_e + m_p)`. Energy scaling is quoted
  as the ratio `m_r,μ/m_r,H` so the H-side reduced mass is not silently dropped.

### M1 — phase-closure spectrum reproduces `E_n ∝ 1/n²`, `E_1 = −RY_EV`

Infinite-mass convention:

| n | E_n [eV] | E_n·n² [eV] |
|---|---|---|
| 1 | −13.605693 | 13.605693 |
| 2 | −3.401423 | 13.605693 |
| 3 | −1.511744 | 13.605693 |
| 4 | −0.850356 | 13.605693 |

`E_n·n² = RY_EV = 13.605693122967754 eV` constant (the 1/n² FORM). `E_1 = −RY_EV` exactly.

### M2 — ground-state closure scale reproduces `a₀ = A_0`

`a₀ = A_0 = 5.291772105802553×10⁻¹¹ m`. Canon identity `a₀ = ℓ_node/α`:
`L_NODE/ALPHA = 5.291772105802553×10⁻¹¹ m == A_0` (verified exact to float precision this session).
a₀ is the EIGENMODE SCALE of the given Coulomb profile — not an Op6-selected geometry.

### M3 — muonic scaling (reduced mass), frozen numeric marks

`M_MUON := 1.883531627×10⁻²⁸ kg` (CODATA 2018 muon mass; to be added to `constants.py` commit #3;
this prereg freezes the value it will carry). Derived:

- `m_r,μ = 1.69289546986631×10⁻²⁸ kg`; `m_r,μ/m_e = 185.84083`; `m_r,μ/m_r,H = 185.94205`.
- `a_μ = a₀·(m_e/m_r,μ) = 2.847475×10⁻¹³ m = 284.748 fm` (≈ 285 fm).
- `E_n(μH) = E_n(H)·(m_r,μ/m_r,H)`, i.e. `E_n(μH) = −RY_EV·(m_r,μ/m_e)/n²`:

| n | E_n(μH) [keV] |
|---|---|
| 1 | −2.528493 |
| 2 | −0.632123 |
| 3 | −0.280944 |

Ground state `E_1(μH) ≈ −2.53 keV`, `a_μ ≈ 285 fm` (matches the brief's frozen estimates).

**⚑ SUBSTRATE FLAG (recorded at prereg, adjudicated in RESULT):** `a_μ = 284.7 fm < ℓ_node = 386.2 fm`.
The muonic ground-state orbit is SMALLER than one lattice cell (the electron reduced Compton
wavelength = the AVE lattice pitch, `de-broglie-standing-wave.md:155`). The reduced-mass SPECTRUM
scaling (M3) is an arithmetic consequence of the probe's dispersion scale and holds as consistency;
but the CONTINUUM "spherical radial transmission line" `Z(r)` picture (deliverable 1) is formally
sub-Nyquist below `ℓ_node`. This is flagged, not hidden — surfaced in RESULT §flags, not resolved
in-lane.

### M4 — inherited Z²-scaling consistency check (`de-broglie-n.md`, ξ₀ = Z²)

If the driver sweeps `Z`: `E_n(Z) = Z²·RY_EV/n²` and `a_n(Z) = n²a₀/Z`. Frozen mark for bare
hydrogenic ions: at `n=1`, `E_1(Z=2) = 4·RY_EV = 54.422772 eV` (He⁺); `E_1·1 / Z² = RY_EV`
independent of Z. Canon: `de-broglie-n.md` "ξ₀ = Z² emerges automatically (Z²-scaling verified
< 2%)".

---

## FROZEN TOLERANCES (set BEFORE code)

| Mark / gate | Tolerance | Basis |
|---|---|---|
| M1 `E_n` vs `RY_EV/n²`, n≤4 | rel err < 0.5% at converged resolution (N_sec ≥ 3000 geomspace) | ODE/ABCD is exact for the Coulomb radial equation (`radial-eigenvalue-solver.md` §E2f-6); residual scatter is pure discretization |
| M1 FORM: `E_n·n²` constant across n | spread < 0.5% | 1/n² is the closure form |
| M2 `a₀` identity `ℓ_node/α == A_0` | rel err < 1×10⁻¹² | algebraic identity |
| M2 closure scale from driver | rel err < 0.5% | eigenmode-scale extraction |
| M3 muonic marks (`a_μ`, `E_n(μH)`) | rel err < 0.5% of frozen values | reduced-mass scaling |
| Integer-closure gate: `n* = √(RY_EV/E_n)` | `|n* − round(n*)| < 0.02` | phase closure is `2πn`, integer |
| M4 Z²-scaling | rel err < 0.5% (bare ions) | inherited from `de-broglie-n.md` |

**No tolerance is a fitted knob.** The 0.5% bound is a discretization ceiling; the pilot run this
session already lands at −0.000% for n=1..6 (recorded in RESULT), so 0.5% is a generous honest bound,
not a target the physics was steered to hit.

---

## ENTAILED-BRANCH ENUMERATION (P10) — pre-stated, no post-hoc criterion drop

**Turning-point / Maslov phase handling (pre-stated):** the driver's canonical route is the ODE /
ABCD cascade with `B_total(E) = 0` (equivalently the outer boundary condition `ψ′ + κψ = 0` on the
decaying solution, with the regular Coulomb solution `f_l` selected at `r → 0`). These exact boundary
conditions capture the turning-point (Maslov) phase EXACTLY — **no ½-integer constant is inserted by
hand.** Consequently branch (i) is the EXPECTED outcome. A naive WKB Sommerfeld integral
`∮k dr = nπ` WITHOUT the Maslov `+½` would instead land in branch (ii); if a WKB comparison is run
and shows that O(1) offset, it is RECORDED as the location of the Maslov phase, NOT tuned away.

- **(i) Closure reproduces the marks within stated tolerance.** The ABCD `B_total=0` eigenvalues match
  `RY_EV/n²`, `a₀`, and the muonic marks within the frozen tolerances. → consistency demonstration
  confirmed; classification = re-derivation / consistency (brief §5).
- **(ii) Closure reproduces the 1/n² FORM but with an O(1) closure-constant offset.** The eigenvalues
  track `∝ 1/n²` but sit at `RY_EV·c₀/n²` with `c₀ ≠ 1` an O(1) constant (the Maslov / turning-point
  phase). → RECORD the offset honestly and name where it lives (the closure-integer phase); **do NOT
  tune it to 1.** The FORM reproduction still counts; the offset is reported as an open turning-point
  bookkeeping item, not a rescue.
- **(iii) Fails** (no `1/n²`, or eigenvalues do not track the marks). → clean negative record, mechanism
  named, branch closed. **No in-lane rescue / no debug-toward-rescue** (Rule 11).

---

## SABOTAGE-TEST PLAN (P11) — every numerical gate must be able to FIRE

A gate that cannot fire on a planted defect is a checklist, not a test. Each gate below must PASS on
the real profile AND FIRE on its plant.

**Gates:**
- **G-MARK:** each eigenvalue matches `RY_EV/n²` (integer n) within tol (M1).
- **G-FORM:** `E_n·n²` constant across n within spread tol (the 1/n² form).
- **G-INT:** `n* = √(RY_EV/E_n)` rounds to an integer within `|n*−round(n*)| < 0.02` (closure = `2πn`).

**Plants (each must FIRE at least one gate; the real profile must PASS all):**
- **(a) wrong-exponent dress:** replace the Coulomb `1/r` dress with a `1/r²` dress in the section
  builder (`V ∝ −1/r²`). A pure attractive `1/r²` profile does not carry a Rydberg `1/n²` spectrum →
  G-MARK / G-FORM must FIRE (no eigenvalues at the marks, or `E_n·n²` non-constant). Pilot this
  session: the `1/r²` plant yields NO bound eigenvalues in the Coulomb energy window → G-MARK fires.
- **(b) detuned closure integer:** compare the real spectrum against a DETUNED mark set
  `RY_EV/(n+δ)²` with `δ = 0.4` (half-ish-integer detuning). G-MARK / G-INT must FIRE against the
  detuned targets (real `n*` are integers, not `n+0.4`), while PASSING against the integer targets.
  This proves the integer-closure gate discriminates `2πn` from `2π(n+δ)`.

**Freeze rule:** the sabotage assertions (real PASS, plant FIRE) are frozen here; the RESULT reports
each outcome verbatim. If a gate cannot be made to fire, it is downgraded to a checklist in the
RESULT and not counted as a test.

---

## CLASSIFICATION (consistency-vs-emergence — pre-committed, brief §5)

Expected class: **re-derivation / consistency demonstration.** Canon already recovers `E_n` and `a₀`
(`clm-oltvwy`) — the canonical ceiling. The x42 added content is the **port-language derivation path**
(off-line Coulomb dress → graded `Z(r)` → reflections → `2πn` phase closure → Op6 spectrum). An
explicit new-primitive scan is run; the pre-committed expectation is **NONE** (no new primitive; the
`Ry`, `a₀`, `1/n²` results are the canonical consistency ceiling, and the two-register guard is a
FORMALIZATION of walk (c), not a new claim). No emergence headline. No promotion past the ceiling.
The marks ride CODATA-derived `RY_EV`, `A_0`, `M_E`, `M_PROTON`, `M_MUON` — CONSISTENCY-class
magnitudes, not chords.

## K1/K2 caveat (stated conditionally, NOT resolved — brief §5)

The well's kernel-transparency (does the held longitudinal Coulomb bias the Ax-4 kernel?) is governed
by the X41 fork. Verdict class quoted verbatim from
`research/2026-07-10_x41-radiative-scoping-why_RESULT.md`:
**"[UNDERDETERMINED — K1 ∧ K2, with the transverse-reactive near-zone as the named discriminator]"**.
Both keys predict the held Coulomb transparent-to-T2, each on its own unpaid premise; the standing
canonical reading (`manuscript/ave-kb/CLAUDE.md:75`) has a held static E LOADING `S_ε`. **This lane
does NOT resolve the fork.** Adjudicators: Grant + the CVR held-DC-E bench + the unbuilt near-zone
probe.

---

## DISCIPLINE

- **Freeze-by-push:** this prereg is pushed to `origin` before the first derivation/code commit; git
  ordering is the freeze proof.
- **Canonical source:** every constant from `ave.core.constants`; zero hard-codes in the driver.
- **Verify-before-cite:** all cites re-grepped at branch tip.
- **Flag-don't-fix:** the `a_μ < ℓ_node` sub-Nyquist fact and the two yield-references (dielectric
  `V_YIELD` vs rupture `m_e c²`) are surfaced, not silently reconciled.
- **No KB/canon edits from this lane** — `research/` + `src/` only; the ONE exception is the `M_MUON`
  addition to `constants.py` (commit #3), flagged in the PR body.
