# FROZEN PREREG — the N-band Cleave registry-pump Chern: the LAST roll

**Date:** 2026-07-02
**Lane:** implementer (N-band upgrade — the gated last roll on the coupling)
**Branch:** `analysis/cleave-nband-chern` (off main, post-#454)
**Disciplines fired:** `ave-prereg`, `ave-canonical-source`, `substrate-native-check`,
`phase-space-coordinate-check`, `consistency-vs-emergence`, `verify-before-cite`
**Status at freeze:** predictions, gates, outcome bins, and convergence criterion locked BEFORE any
N-band Chern number is computed. Upstream: `research/2026-07-02_cleave-registry-pump-chern_result.md`
(the 2-band NULL-DERIVED result, §5 of which scoped THIS upgrade as the gated route).

> **SHA-PIN.** Frozen at commit time, committed BEFORE the driver code. Any change to a setup, a
> gate, an outcome bin, or the convergence criterion AFTER any C_N is known is a Rule-16 violation
> and must be a NEW prereg. **Pre-commitment (Grant, 2026-07-02): this is the LAST roll on the
> coupling. A confirmed null closes the mechanism question permanently — no further rolls, no rescue
> escapes.** That pre-commitment is frozen here so it cannot be walked back after the number is seen.

---

## 0. Why this roll, and what it can/cannot do

The 2-band result (`..._result.md`) returned **NULL-DERIVED** (`C_slide = C_lock = 0`) for an
*effective 2-band screw-block* model. Its §5 scope caveat named the honest bound: the locked C=0 was
construction-specific to the effective Bloch model; a **full N-band `Link(∂Ω, F)` srs eigensolve**
(the genuine 8-site srs-cell tight-binding manifold, not a 2-band reduction) was the gated upgrade
that could in principle differ. This roll runs it.

- **What it decides:** whether the genuine multi-band srs occupied manifold, swept over the
  `(k_z, θ)` registry torus, carries a nonzero Chern number in EITHER substrate reading. If the
  N-band manifold is also trivial, the "maybe a richer construction differs" escape is spent.
- **What it cannot claim:** absolute proof over *every* conceivable coupling functional. But per
  Grant's pre-commitment, the N-band srs manifold IS the faithful substrate object; a null here is
  the honest terminal answer, not one more effective model to escape past. **A null closes it.**

### substrate-native-check (fired BEFORE the numerical design)

- **Carrier / K4 checkpoint:** the genuine **srs 8a-orbit cell** (`chiral_lattice._SRS_8A`, 8 sites,
  degree-3 net, `build_srs_net`) — the free-mode carrier, I4₁32. This is the N-band object the
  2-band model only approximated. Do NOT flip z=3→4 (no diamond substitution).
- **Sector:** T2 Cosserat micro-rotation WINDING (charge = `Link(∂Ω, F) ∈ ℤ`), sector-orthogonal to
  A1 mass. The Chern number of the occupied manifold IS the pumped `Link` per registry period (the
  degree↔linking identity, `charge_quantization.py:257` docstring). No A1 cross-wiring.
- **Phase-space (A46):** the Chern number lives on the `(k_z, θ)` registry-torus phase space; the OA
  anchor is a holonomy (rad/z-unit). Both phase-space invariants — matched coordinates. The
  real-space slope (fC/µm) is the phase invariant × the substrate-native period, an explicit
  phase→real bridge.
- **No SM/QED default:** the Chern number is a Berry-curvature integral of the occupied **projector**
  over a closed torus (non-Abelian Wilson-loop / Fukui-Hatsugai on the occupied manifold) — the
  substrate-native adiabatic-pump invariant. No Lagrangian minimization, no energy basin.

### consistency-vs-emergence (frozen tag)

Same as the 2-band: the mechanism CLASS and the FORMS are consistency/adjudication-class; the value
414.9 fC/µm is a VALUE-import through the ξ_topo unit-bridge (CODATA through ℓ_node). A nonzero C_N
would be an **existence** result (the mechanism is real), not emergence-of-the-value. On any outcome
we tag consistency-class; we do NOT headline the slope value as emergence.

---

## 1. The N-band construction (concrete)

Build the srs tight-binding Bloch Hamiltonian `H(k; θ)` on the 8-site srs cell from the genuine net
(`build_srs_net` neighbor/bond structure), a degree-3 nearest-neighbor hopping model. The occupied
manifold = the lower half of the spectrum (a filled-band / Γ=−1-bounded reading; the exact filling
is stated below and frozen). Sweep the `(k_z, θ)` torus at fixed transverse `(k_x, k_y)` on a BZ
grid, and compute the **occupied-projector Chern number** (trace of the Berry curvature over the
occupied manifold), summed/averaged over the transverse BZ.

**The two readings (identical to the 2-band; θ enters ONE way each):**

- **SLIDING / Eulerian (canonical engine):** θ is a **global U(1) phase** applied uniformly to the
  readout boundary — matter drags no substrate texture. A global phase commutes with the occupied
  projector `P(k)` and factors out of every Berry link → the `(k_z, θ)` Berry curvature is
  identically zero → **C_slide = 0 by construction** (a structural null, as in the 2-band; this is
  the corpus sliding-engine reading, Angles B/C).
- **LOCKED / Lagrangian (finite-strain co-moving):** θ **co-rotates the transverse (x,y) on-site /
  bond frame THROUGH the screw operator** (`find_screw_operator` R block, the π/2 4-fold rotation),
  advected by the finite-strain displacement. θ then enters `H(k; θ)` as a real parameter that can
  wind the occupied manifold. The screw's t_z (srs-R 1/4 vs srs-L 3/4, signed) carries the
  enantiomorph sign, so C_lock is enantiomorph-odd IF nonzero.

**Frozen filling.** Occupied = the lower `n_occ = 4` of the 8 srs bands (half-filling, the natural
Γ=−1 filled-manifold reading). If half-filling is gapless over the torus (no clean occupied
manifold), that is a DOCUMENTED convergence outcome (→ INCONCLUSIVE unless a nearby frozen gap exists
— see §4), NOT a re-pick of filling to manufacture a gap. The filling is frozen at half here.

> **Honesty clause (frozen).** If the N-band locked construction is ill-defined at implementation
> (occupied manifold not gauge-closable over the torus, or persistently gapless at half-filling),
> that is a DOCUMENTED OUTCOME (INCONCLUSIVE with the named blocker), not a failure to hide and not a
> licence to re-pick filling/coupling until a number appears.

---

## 2. Validate-on-known gate (MUST pass before any verdict counts)

The N-band machinery must reproduce a known result in the SAME run. TWO checks (both if cheap; at
minimum check A):

- **Check A — recover the 2-band C=0 in a restricted subspace.** Project the N-band occupied-manifold
  Chern integrator onto a 2-band subspace reproducing the effective screw block; it must return the
  same **C = 0** (sliding and locked) the 2-band driver got. This proves the N-band integrator is
  consistent with the validated 2-band result — the machinery did not introduce a spurious nonzero.
- **Check B — a known multi-band pump with C ≠ 0.** Run the occupied-projector Chern integrator on a
  multi-band Thouless pump model with a KNOWN nonzero occupied-manifold Chern (e.g. a stacked /
  coupled Rice-Mele giving `|C| = 1` or a known `|C| = 2`); it must return that integer and flip
  sign with pump direction. This proves the integrator CAN detect a nonzero when one exists (it is
  not trivially returning 0).

**GATE-VOK-PASS:** Check A returns C=0 (matches 2-band) AND Check B returns the known nonzero integer
(flips sign). **If either fails, the run is INCONCLUSIVE** — the srs numbers are printed but marked
"machinery-unvalidated, not adjudicated." An integrator that cannot both recover the 2-band null AND
detect a real nonzero cannot be trusted to report the srs verdict.

---

## 3. Anchor cross-check (Grant's (b) canon-slot decider, carried forward)

Independently of C_N, the run recomputes the OA anchor from the same srs ground state:
bulk **g₀ = 2.21589 rad/lattice-z-unit** (`chiral-vector-tlm-phase1_result.md:23,65`), loop
holonomy **±0.256776 rad** (`:23`). srs-R must reproduce the bare-pitch magnitude to 0.25% (the
2-band run showed the ±enantiomorph SIGN-flip lives in the writhe/torsion channel, not the
bare-pitch formula — carried forward honestly, not re-litigated). ANCHOR-PASS confirms the pump ran
on the right texture. In a null outcome the decider is moot (no C≠0 to earn the slot); in a reopen it
selects the canon reading.

---

## 4. FROZEN outcome bins (no post-hoc edits)

Computed per reading × per enantiomorph; C_N = the occupied-manifold Chern number over `(k_z, θ)`.

| bin | condition | verdict |
|---|---|---|
| **NULL-CONFIRMED-FINAL** | `C_N = 0` in BOTH readings AND BOTH enantiomorphs (integer-round to 0), GATE-VOK PASS, occupied manifold gapped + converged | **The coupling question CLOSES permanently** (Grant pre-commitment). The registry-pump mechanism is dead at the faithful N-band level; `Q = ξ_topo·x` is a unit-bridge, no derived pump. Cleave retires as a *discriminator* — AVE itself predicts the bench null (corroborative-null class). No further rolls. |
| **REOPENS** | `C_N ≠ 0` in at least one reading, GATE-VOK PASS, enantiomorph-odd satisfied | The mechanism is REAL after all. Record WHICH reading; run the anchor cross-check (§3) for the canon slot; compute the implied slope `C_N × {146.7 (full-cell a_cell) | 586.8 (quarter-pitch p)} fC/µm` from the period the pump quantum matches. Cleave becomes a CONDITIONAL forward prediction with the computed slope. |
| **INCONCLUSIVE** | GATE-VOK FAIL, OR occupied manifold gapless at half-filling over the torus, OR C_N non-integer / grid-unstable | No verdict; NOT a close and NOT a reopen. Report the numbers with the named concrete blocker (this does NOT spend Grant's last-roll pre-commitment — a genuine non-result is not a null). |

**Enantiomorph-odd guard (frozen).** For any bin reporting `C_N ≠ 0`: C_N MUST flip sign srs-R ↔
srs-L. Same-sign nonzero = RED FLAG → downgrade to INCONCLUSIVE (numerical artifact suspected),
regardless of magnitude.

**Bench slope pre-frozen (carried from 2-band):** the exact 414.9 fC/µm is NOT integer-C-reachable
(needs C = 2√2 full-cell or 1/√2 quarter-pitch); whatever C_N comes out, the derived slope is
`C_N × {146.7 | 586.8}` fC/µm, never 414.9. Computed in-run from `ave.core.constants`.

---

## 5. Convergence criterion (frozen up front)

The C_N verdict counts only if it is grid-converged. Stated BEFORE any number:

- **≥ 3 grid densities** on the `(k_z, θ)` torus: `n ∈ {24, 36, 48}` (and the transverse BZ sampled
  at ≥ 2 densities to confirm the transverse average is stable). The reported C_N integer must be
  **identical across all three** `(k_z, θ)` densities.
- **Gapped occupied manifold:** min direct gap between the occupied and unoccupied manifolds over the
  sampled torus > `1e-3` (in the model's hopping units) — else the Chern is ill-defined → INCONCLUSIVE.
- **Integer-round tolerance:** `|C_N − round(C_N)| < 0.1` at the finest grid.
- A result failing any of these three is INCONCLUSIVE (not a null, not a reopen).

---

## 6. Coordinate + honesty discipline (frozen)

- **phase-space-coordinate-check:** Chern on `(k_z, θ)` (phase space); anchor g₀ a holonomy (phase).
  Matched. The bench slope (real-space fC/µm) is the phase invariant × substrate-native period — the
  bridge is explicit, not a coordinate-mismatched comparison.
- **ave-driver-script-honesty:** EVERY printed number computed in-run; ALL constants imported from
  `ave.core.constants` (never hard-coded); the srs net/bonds come from `chiral_lattice.build_srs_net`
  / `_SRS_8A`, not transcribed. The VOK checks, srs Chern, and anchor are all live computes.
- **Route heavy solves to the engine_sim CI lane** (the N-band torus Chern + transverse-BZ average +
  grid-convergence sweep) via the conftest partition; keep the fast VOK/slope/anchor structural
  checks gating. Follow the #411/#414 routing pattern (as in the 2-band test file).

---

## 7. What would make this WRONG (pre-committed failure modes)

- A bin edited after C_N is known → Rule-16 (§SHA-PIN); the last-roll pre-commitment forbids
  converting a confirmed null into "one more roll."
- Filling re-picked off half to manufacture a gap after seeing a gapless result → §1 frozen filling.
- GATE-VOK Check B skipped so a false 0 passes unchecked → §2 requires the detect-a-nonzero check.
- Convergence criterion loosened after seeing a grid-unstable C_N → §5 frozen.
- Same-sign C_N across enantiomorphs reported as a real pump → §4 enantiomorph-odd guard.
- 414.9 reverse-engineered as "the derived slope" → §4 pre-freezes it is NOT integer-C-reachable.
- A number hard-coded instead of imported / transcribed instead of built from the net → §6.

---

## 8. Deliverable

`research/2026-07-02_cleave-registry-pump-chern-nband_result.md`: GATE-VOK (Check A recover-2-band-0,
Check B detect-known-nonzero), the N-band srs `(k_z, θ)` occupied-manifold Chern per reading ×
enantiomorph, the grid-convergence table (n = 24/36/48), the anchor cross-check, the FROZEN bin that
fired, the derived slope `C_N × {146.7 | 586.8}` (moot if null), and the enantiomorph-odd check.
Then — WITH the final verdict in hand — the auditor-lane landings (claim-quality row,
forward-prediction register, def-tk1xfm note) and the un-gated AVE-Core fallout items per the final
verdict. Femto-repo items stay [SEPARATE SESSION]. Honest solidity, consistency-class.
