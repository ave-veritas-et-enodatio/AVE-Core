# Apparatus-floor characterizations on the crystal/graft engine family

**Date:** 2026-06-10
**Branch:** `analysis/2026-06-10-apparatus-floors`
**Engine:** `src/ave/core/crystal_engine.py` (caps `:63-64` A_cap=0.99/S_min=0.05;
kernel clip `:157-161`), `crystal_graft_v2.py` (`helicity_bel` `:287-294`, `_curl`
`:147-159`), `crystal_graft_v3.py`.
**Drivers:** `src/scripts/vol_1_foundations/apparatus_floor_wall_run.py`,
`apparatus_floor_hbel_run.py`.

> **Scope discipline.** These are APPARATUS measurements — instrument floors and
> regularization attributions — not physics claims. They are the retroactive
> self-audit of `ave-apparatus-floor-attribution` (skill encoded 2026-06-10),
> which named both open questions directly: the unattributed Γ_min≈−0.85 and the
> uncalibrated H_bel ledger. Run verdicts (Outcome A/B/C, charge=helicity, α
> emergence) belong to the v2/v3/v4 prereg runs, not here.

---

## Characterization 1 — THE WALL vs THE KNOBS

**Setup.** Standard Mode-I trapped breather = the pure bulk c_eff trap
(`CrystalEngine`, converter/ω/buckle OFF; the wall is a bulk-V phenomenon,
`crystal_engine.py:163-166,388-406`). N=37 (odd → true center cell), σ=3, seed
frac = A_cap (the breather presses on the binding clip), evolved to a FIXED
physical time T=6.0 (dt ∝ √S_min, so equal-step runs would be unfair across the
sweep). Sweep S_min ∈ {0.0125, 0.025, 0.05, 0.1, 0.2} × A_cap ∈ {0.99, 0.999}
(10 cells, serial — trivially fast).

**The naive bound (the apparatus prediction).** The kernel is
`S(A)=sqrt(max(1−A², S_min²))` with A clamped to A_cap (`:157-161`). So the
deepest achievable S is `S_floor = max(sqrt(1−A_cap²), S_min)` and the deepest
wall the diagnostic can produce is `Γ_floor = (n−1)/(n+1)`, `n = S_floor^{1/4}`
(the engine's `refractive_index()` power).

**Result — Γ_min is APPARATUS, to machine precision.**

| A_cap | S_min | Γ_min (measured) | Γ_floor (naive clip) | binding clip | wall width |
|------:|------:|-----------------:|---------------------:|:-------------|-----------:|
| 0.99  | 0.0125 | −0.2400 | −0.2400 | A_cap | 3 cells |
| 0.99  | 0.025  | −0.2400 | −0.2400 | A_cap | 3 cells |
| 0.99  | 0.05   | −0.2400 | −0.2400 | A_cap | 3 cells |
| 0.99  | 0.1    | −0.2400 | −0.2400 | A_cap | 3 cells |
| 0.99  | 0.2    | −0.1985 | −0.1985 | S_min | 3 cells |
| 0.999 | 0.0125 | −0.3700 | −0.3700 | A_cap | 2 cells |
| 0.999 | 0.025  | −0.3700 | −0.3700 | A_cap | 2 cells |
| 0.999 | 0.05   | −0.3579 | −0.3579 | S_min | 2 cells |
| 0.999 | 0.1    | −0.2801 | −0.2801 | S_min | 2 cells |
| 0.999 | 0.2    | −0.1985 | −0.1985 | S_min | 3 cells |

`corr(Γ_min, Γ_floor) = 1.0000`, `max|residual| = 0.0000`. The measured wall sits
EXACTLY on the clip bound in every cell.

**Verdict: TRACKS-KNOB (apparatus), with a MIXED responsible-knob structure.**
Γ_min is set entirely by whichever clip binds: A_cap binds for small S_min (the
wall PLATEAUS *vs S_min* — but at the **A_cap** clip, still apparatus), S_min binds
for large S_min (the wall TRACKS S_min). There is NO S_min-independent, A_cap-
independent physical plateau — every Γ_min sits on a regularization clip.

**The −0.849 record is not f(S_min).** v2/v3's Γ_min≈−0.849 was the DEEPEST STATIC
SEED (A_core=0.999999999, S_min=1e-12, A_cap=0.9999999999 — NON-binding clips); it
is set by SEED DEPTH (A→1 approaching the kernel's √-singularity), not by
S_min=0.05. In any real run A is capped at A_cap and S floored at S_min, so the
wall **never approaches −1** — at the standard A_cap=0.999 it caps at −0.37.

**Wall width = 2-3 cells = the seed envelope / radial resolution**, not a physical
wall thickness. The √-singularity makes the continuum wall asymptotically sharp;
the clip + the grid render it as a 2-3 cell shoulder.

**FLAG (flag-don't-fix, for the auditor — NOT resolved here).**
`refractive_index()` (`crystal_engine.py:391`) returns `S**0.25`, but the
wave-speed identity `c_eff² = c0²/S` (`:164`) ⇒ physical `n = c0/c_eff = S**0.5`.
The Γ diagnostic and its own docstring (`:388` "n=c0/c_eff=S^{1/4}") disagree by a
power. We computed Γ with the engine's own diagnostic (to match the v2/v3/v4
record) and report both floors in the JSON. The tracks-vs-plateau verdict is
power-independent; only the absolute Γ values shift.

---

## Leak attribution (the α-from-leak question)

**Leak metric:** relative loss of the core energy fraction over the fixed physical
time T=6 (core radius = 2σ = 6, PML-excluded).

**Result — leak is FLAT across the entire sweep.** mean = 0.544, CV = 1.5%,
range/mean = 5.1% across the 16× S_min range AND both A_cap. The localization
retention is identical (0.185) in every cell. **The leak does NOT track the
wall-depth knobs.** It is set by the bulk breather's dispersion (shape-driven,
scale-invariant), independent of S_min and A_cap.

The reported correlation coefficients (leak-vs-Γ_floor = −0.63, leak-vs-S_min =
−0.35) are MISLEADING artifacts of ~1% phase-sampling noise (equal-physical-time
runs land at slightly different breather oscillation phases). With CV < 2% they
carry no signal.

**Implication for any α-from-leak claim:** a leak-derived α at this config would
be reading **breather dispersion dynamics, not a regularization-set wall
property** — and the leak does not even track the knob (S_min) that sets the wall
depth. Per the skill's special case, attributing a residual to α requires BOTH
knob-independence AND the physics-side signature; here the leak is knob-
independent in the *wrong way* (it is dynamics, not a wall transmission), so it
fails the wall-transmission premise the attribution would need.

---

## Characterization 2 — THE H_bel LEDGER FLOOR

**Instrument under test.** The graft family's headline helicity ledger
`H = ∫ξ·(∇×ξ)`, curl = `CrystalGraftV2._curl` (`:147-159`), exactly as used by
`helicity_bel` (ω carrier, `:287-294`), v4's `helicity_photon` (w photon,
`crystal_graft_v4.py:338-346`) and v4's headline `helicity_ledger`. We call the
engine's OWN `_curl` — byte-identical stencil. Grid: the v4-relevant **N=72**
(`crystal_graft_v4_run.py:43`) AND N=44 (v3) for cross-scale.

### (a) FREE DRIFT — the ledger noise floor
Free helical photon (the LOCKED photon config: σ=3, λ=6, helicity=+1), NO wall,
NO source, NO converter, NO ω-sector; 1000 steps.

- **Intensive** (H_bel/|w|², PML-robust): drifts **+3.0% end-to-end**, **4.9%
  swing**.
- **Extensive** (raw ∫w·∇×w): **swings ~22% during transit** (the packet
  breathes/disperses), end-drift +2.0%, |w|²-loss 1.0% (PML).
- **N-independent**: N=44 and N=72 identical to 6 sig figs — the localized packet
  never reaches the larger box's boundary in 1000 steps, so **small-N is a valid
  proxy for the N=72 floor.**

The ~22% extensive swing is the dominant floor: a ledger read at an arbitrary
timestep carries **±22% read-phase error** unless read at a consistent settled
phase.

### (b) KNOWN-NULL — the false-positive floor
Linearly polarized photon (helicity=0). `|H_bel|` = **0 to machine precision**,
and stays 0 through 1000 free steps. The false-positive floor is the one clean
number: **~0** — the stencil manufactures no helicity. (Note: a single-axis linear
field has identically-zero helicity density, so this confirms zero additive
bias.)

### (c) KNOWN-POSITIVE — read accuracy at resolvable scale
Planted ABC Beltrami ω with `∇×ω = λω` EXACTLY ⇒ analytic helicity = λ∫|ω|². The
read accuracy is exactly the central-difference curl truncation `sin(λdx)/(λdx)`:

| Beltrami wavelength | read accuracy | under-read |
|--------------------:|--------------:|-----------:|
| 4 cells  | 0.637 | −36% |
| 6 cells  | 0.827 | −17% |
| 8 cells  | 0.900 | −10% |
| **10 cells (v4 photon)** | **0.936** | **−6.5%** |
| 12 cells | 0.955 | −4.5% |

The instrument **under-reports** helicity magnitude by this truncation. The v4
photon (λ=10, `crystal_graft_v4_run.py:51`) is read 6.5% low; a few-cell winding
(the (2,3) extractor sits at r≈1.1 cells, per the extractor-floor note) would be
read ≥17-36% low.

### THE NUMBER v4's ledger-closure must beat
At **N=72, 1000 steps**: H_bel-ledger **closure claims tighter than ±6.5% are
below the instrument floor.** Decomposition:
- conservation: free helical photon conserves its OWN helicity to only 3.0%
  (intensive end) / 4.9% (intensive swing);
- read-phase: extensive ∫w·∇×w swings **±22%** during transit;
- magnitude: central-diff curl under-reads **6.5%** at the v4 photon scale,
  rising to **36%** at a 4-cell winding;
- false-positive: **~0** (clean).

**NET: trust the SIGN and ratios coarser than ~5%; distrust any closure magnitude
claimed tighter than ±6% (and ±22% if read at an arbitrary transit phase, up to
±36% if the winding sits below ~8 cells) at the v4 config.**

---

## Provenance / honesty
- `ave-apparatus-floor-attribution` — this run IS its retroactive self-audit
  (both flagged numbers characterized; check A instrument-floor + check B
  regularization-sweep both exercised).
- `ave-driver-script-honesty` — every number read from the evolved/seeded field;
  identical production stencil; naive bound and analytic known-positive computed
  from the clips/λ alone, never back-solved from the measurement.
- `ave-canonical-source` — engine = canonical crystal/graft family; no α-bearing
  input; κ̃=6/5 topology, V_yield≡1, λ from geometry.
- `verify-before-cite` — v4 N=72 / photon λ=10 verified against
  `crystal_graft_v4_run.py:43,51`; `helicity_bel`/`_curl`/clip line numbers
  grepped in `crystal_graft_v2.py` / `crystal_engine.py`.

## Artifacts
- `src/scripts/vol_1_foundations/apparatus_floor_wall_run.py` + `_results.json` +
  `apparatus_floor_wall_fig1.png`
- `src/scripts/vol_1_foundations/apparatus_floor_hbel_run.py` + `_results.json` +
  `apparatus_floor_hbel_fig1.png`
