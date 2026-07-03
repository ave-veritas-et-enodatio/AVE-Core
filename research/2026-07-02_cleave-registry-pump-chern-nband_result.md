# RESULT — N-band Cleave registry-pump Chern: the LAST roll → NULL-CONFIRMED-FINAL

**Date:** 2026-07-02
**Lane:** implementer (N-band upgrade — run complete)
**Branch:** `analysis/cleave-nband-chern` (off main, post-#454)
**FROZEN prereg:** `research/2026-07-02_cleave-registry-pump-chern-nband_prereg.md`
**Upstream:** `research/2026-07-02_cleave-registry-pump-chern_result.md` (2-band NULL-DERIVED, §5)
**Driver:** `src/scripts/vol_4_engineering/cleave_registry_pump_chern_nband.py`
**Tests:** `src/tests/test_cleave_registry_pump_chern_nband.py`
**Class:** adjudication / consistency-class. Solidity: **NULL-CONFIRMED-FINAL** — the coupling
question closes (Grant's frozen last-roll pre-commitment).

> **Headline.** The genuine 8-band srs-cell occupied-manifold Chern over the `(k_z, θ)` registry
> torus is **C_N = 0 in BOTH readings AND BOTH enantiomorphs** (gapped, grid-converged n=24/36/48).
> The validate-on-known gate passes both ways (recovers the 2-band 0; detects a known |C|=2).
> **VERDICT BIN: NULL-CONFIRMED-FINAL.** The registry-pump mechanism — the sole surviving coupling
> candidate — is dead at the faithful N-band level. Per the frozen pre-commitment the coupling
> question **closes permanently**: `Q = ξ_topo·x` is a unit-bridge, and Cleave-01 retires as a
> *discriminator* (AVE itself predicts the bench null — a corroborative-null-class bench).

---

## 1. Validation gates (all pass — the verdict counts)

| gate | result | pass |
|---|---|---|
| **GATE-VOK Check A** (recover 2-band C=0 in a restricted subspace) | sliding → 0, locked → 0 | **PASS** |
| **GATE-VOK Check B** (detect a KNOWN multi-band pump, \|C\|=2) | pump +1 → **−2**, pump −1 → **+2** (flips sign, converged n=24/36/48) | **PASS** |
| **G-HERMITIAN** (srs Bloch H Hermitian + half-manifold gapped) | `max|H−H†| = 0`, min occ/unocc gap > 1e-3 both readings | **PASS** |
| **G-SLIDING-FLAT** (sliding H θ-independent → C_slide=0 by construction) | `H(θ=0) = H(θ)` for all θ | **PASS** |
| **G-ANCHOR** (OA bulk g₀ = 2.21589 rad/z-unit) | srs-R bare pitch 2.22144 (0.2505% off, match) | **PASS (srs-R)** |
| **convergence** (integer stable across n=24/36/48, gapped, slices agree) | all four configs converged | **PASS** |

GATE-VOK is the load-bearing pair: an integrator that both **recovers the validated 2-band 0** AND
**detects a real |C|=2 that flips sign** cannot be dismissed as returning 0 trivially. It reports 0
on the srs manifold because the srs manifold *is* topologically trivial in both readings.

---

## 2. The srs N-band `(k_z, θ)` occupied-manifold Chern (n_occ = 4 of 8)

| reading | enantiomorph | C_N (int) | by grid (24/36/48) | min occ/unocc gap | converged |
|---|---|---|---|---|---|
| **sliding**/Eulerian | srs-R | **0** | 0 / 0 / 0 | 0.0409 | ✔ |
| sliding/Eulerian | srs-L | **0** | 0 / 0 / 0 | 0.0409 | ✔ |
| **locked**/Lagrangian | srs-R | **0** | 0 / 0 / 0 | 0.0409 | ✔ |
| locked/Lagrangian | srs-L | **0** | 0 / 0 / 0 | 0.0409 | ✔ |

- **Method:** the non-Abelian (multi-band) Chern via the Fukui-Hatsugai overlap-**determinant** on
  the occupied manifold (`det⟨frame(a)|frame(b)⟩`, gauge-invariant over the whole occupied
  manifold, handles band entanglement; reduces to single-band FH at n_occ=1). Occupied = the lower 4
  of 8 srs bands (frozen half-filling), gapped by a fixed staggered on-site potential (frozen, not
  tuned).
- **Sliding:** θ is an unobservable global wavefunction phase (matter drags no texture) → the srs H
  is θ-independent → the `(k_z, θ)` Berry curvature is identically zero → **C_slide = 0 by
  construction.** (Corrected from a first draft that multiplied hoppings by `e^{iθ}` — that is a
  spectrum-changing operation and the *wrong* reading; the corpus sliding engine drags no texture,
  so θ cannot enter H. The G-SLIDING-FLAT test guards this.)
- **Locked:** θ co-rotates the transverse frame through the actual `find_screw_operator` block
  (t_z-signed, enantiomorph-odd). The genuine 8-band occupied manifold is gapped (0.0409) but the
  co-moving winding does **not** enclose a Berry-curvature source → **C_lock = 0**, grid-stable,
  well-resolved.

**Enantiomorph-odd guard:** all configs 0 → trivially consistent (no same-sign-nonzero red flag).

**Slope (moot — null):** had C_N been nonzero, the derived slope would be `C_N × {146.7 (full-cell
a_cell) | 586.8 (quarter-pitch p)} fC/µm` — never the bench's 414.9 (needs non-integer C=2√2). With
C_N=0 there is no integer-C pump.

---

## 3. FINDING — the high-symmetry-point branch artifact (reported, not brute-forced)

At **exactly** the transverse high-symmetry points (Γ = kx=ky=0, and the M-corner (π,π)) the srs
occupied manifold has an **isolated accidental degeneracy** where the Fukui-Hatsugai plaquette lands
on the ±π branch cut (`max_plaquette = π` exactly) and the Chern integer **flickers across grids**
(Γ: 0/+2/−4/−1/+2 over n=24/36/48/72/96). This is an **ill-defined invariant AT that measure-zero
point**, NOT a bulk pump. The diagnosis is unambiguous:

- Perturbing off the HS point by even `1e-3` gives a **clean, grid-stable C=0 with `max_plaquette =
  0.0`** (perfectly smooth) — the bulk invariant is unambiguously 0.
- The flicker is confined to the exact symmetry point; the whole smooth interior of the transverse
  BZ is C=0.

**Handling (standard practice):** the bulk Chern is defined on the smooth interior; exact
high-symmetry points where accidental degeneracies sit are sampled with an infinitesimal offset
(`_HS_EPS = 1e-3`). This is documented in the driver and is not a result-tuning choice — it removes a
gauge/numerical artifact at a measure-zero point, verified by the off-point smoothness. **This is
exactly the class of finding the slice-independence guard (`all_slices_agree`) exists to surface;
it is reported here, not papered over.**

---

## 4. Engineering-choice amendment to the frozen prereg (no bin/gate change)

The prereg (§5) left the transverse-BZ density an implementation detail ("transverse BZ sampled at ≥
2 densities"). This run makes it concrete: **a capped 12-slice transverse set** — the four
high-symmetry points (offset by `_HS_EPS`, §3) plus a 3×3 interior grid. Rationale: the pump Chern is
transverse-slice-**independent** for a gapped manifold (it is the flux through the `(k_z, θ)` torus,
not the transverse BZ), so FH-density transverse sweeping is unnecessary; the `all_slices_agree`
guard verifies the independence and would surface any genuine slice-dependent gap-closing. **This
changes only the transverse sampling density — no frozen bin, gate, convergence criterion, or
enantiomorph guard is touched.** (Recorded here as the amendment note the mission instructed, rather
than silently deviating.) It also delivered the ~700× speedup (80s → 1.6s) together with the batched
eigh.

---

## 5. The frozen bin

**VERDICT BIN: NULL-CONFIRMED-FINAL** (`C_N = 0` in BOTH readings AND BOTH enantiomorphs, gapped +
converged, GATE-VOK PASS, enantiomorph-odd consistent). Per the frozen bins (prereg §4):

> The registry-pump mechanism is DEAD at the faithful N-band srs level. Per Grant's pre-commitment
> the coupling question CLOSES permanently — no further rolls. `Q = ξ_topo·x` is a unit-bridge;
> Cleave retires as a discriminator (AVE itself predicts the bench null — corroborative-null class).

**What this now licenses (bounded honestly).** The 2-band result's §5 scope caveat named the N-band
`Link(∂Ω, F)` srs manifold as the honest upgrade that could still differ. It does not differ: the
genuine multi-band srs manifold is also topologically trivial in both readings. The "maybe a richer
construction differs" escape is spent. Per Grant's frozen last-roll pre-commitment, **this is the
terminal answer for the registry-pump mechanism** — not one more effective model to escape past.
(As always: this is the faithful srs tight-binding manifold at half-filling; it is not a proof over
every conceivable coupling functional, but it IS the substrate-native object, and the pre-commitment
closes the question on that basis.)

---

## 6. Corpus impact (landed with this final verdict — see §7 and the propagation)

- **Cleave-01 coupling status → FINAL:** the registry-pump candidate is dead; `Q = ξ_topo·x` is a
  unit-bridge. The bench retires as a *discriminator* — a corroborative-null-class bench (AVE predicts
  the null; a nonzero gap-independent floor would still falsify AVE, so it retains value as a
  one-sided falsifier, but it is NOT a chord-confirming forward prediction).
- **def-tk1xfm ceiling REAFFIRMED by a computed null** — no derived-mechanism instance emerged at
  either the 2-band or N-band level; the "identity-by-translation, NOT a derivation" ceiling holds.
- Landed in this branch: the claim-quality row, the forward-prediction register Cleave/Ax2 row, the
  def-tk1xfm note, the `project-cleave-01.md` full coupling-status rewrite + Outcome-C rescope, the
  requirements-leaf corner disposition, and the fallout-doc update (Femto items stay SEPARATE).

---

## 7. Reproduce

```
PYTHONPATH=<worktree>/src <main>/.venv/bin/python \
  src/scripts/vol_4_engineering/cleave_registry_pump_chern_nband.py
# incremental JSON (detached-run resilient): run_all_nband(incremental_dir=...)
# tests (gating): pytest src/tests/test_cleave_registry_pump_chern_nband.py -m "not engine_sim"
# tests (engine): make test-engine
```

All numbers are the driver's in-run output (grids 24/36/48, 12 transverse slices). Full run 1.6s.
`make verify` PASSED.
