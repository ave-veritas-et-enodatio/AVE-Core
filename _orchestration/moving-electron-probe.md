# Moving-electron probe (CP8) — does the Master-Equation FDTD engine host a MOVING self-trapped core?

**Date**: 2026-06-04
**Branch**: `analysis/moving-electron-probe` (off main `ea917144`)
**Engine**: [`src/ave/core/master_equation_fdtd.py`](../src/ave/core/master_equation_fdtd.py) — the ONLY engine with `c_eff(V)=c₀/√S` AND the only one that autonomously hosted a self-trap (v14 breather, Mode-I PASS)
**Driver**: [`src/scripts/vol_1_foundations/moving_electron_boost_probe.py`](../src/scripts/vol_1_foundations/moving_electron_boost_probe.py)
**Result**: [`research/2026-06-04_moving-electron-boost-probe-result.md`](../research/2026-06-04_moving-electron-boost-probe-result.md)

**Status**: PREREG FROZEN. (Filled incrementally; result lands in the result doc.)

**Classification**: Class-D emergence/hosting test — the NEXT LAYER (mobility) on the proven self-trap host. A non-hostable layer is a STRUCTURAL-CAPABILITY FINDING, not a failure (substrate-native-check Checkpoint 8).

---

## §0 HEADLINE (the deliverable)

One question, sharpest form: **does the proven self-trap (the v14 breathing soliton) TRANSLATE when given net transverse momentum, or does the Γ=−1 frozen clock PIN it (or does it DISPERSE under boost)?**

- The v14 breather is the PROVEN host: a transverse photon self-traps into a localized breathing soliton on this engine (Mode-I PASS, [`breathing-soliton-v14-mode-i`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md)). That is mass/localization.
- **Mobility is the NEXT LAYER** — never tested. All prior self-traps were stationary seeds. This probe isolates exactly that layer: seed the proven precursor, add the simplest momentum operator (a transverse `k_x` phase ramp), and watch the centroid.
- **The verdict is the deliverable** (MOVES / PINS / DISPERSES), and either way it is a structural-capability finding: a PIN result is the clean structural statement that the frozen clock holds the envelope in place (and the corpus's actual electron motion is then the separate longitudinal bulk-modulus channel, `de-broglie-standing-wave.md:50`).

## §1 Corpus state (green-field, grep-confirmed)

- **The moving/translating self-trapped core has NEVER been tested.** Grep of `src/scripts/` for `centroid|translat|boost|moving.*soliton|moving.*breather` returns only (a) the FDTD3D moving-*photon* wake test (`test_fdtd3d_moving_pulse_wake.py` — a linear Maxwell pulse, not a self-trap), and (b) the q_g47 / r10 self-trap drivers, all of which seed STATIONARY (`V_prev = V`, zero initial velocity).
- **Engine = Master-Equation FDTD** (`master_equation_fdtd.py`) — confirmed (STEP-0) to implement `c_eff²=c₀²/S`, `S(A)=√(1−A²)` (lines 141-151), the self-trapping feedback. It is the ONLY engine with `c_eff(V)`, and the only one that autonomously hosted a self-trap (the v14 breather). K4-TLM structurally cannot (no `c_eff`; Mode-III'd every v14 seed; `research/_archive/L3_electron_soliton/111_master_equation_audit_and_engine_gap.md:18,89`).
- **Sibling precedent (today, on main):** the transverse-photon self-trap result ([`research/2026-06-04_full-electron-transverse-selftrap-result.md`](../research/2026-06-04_full-electron-transverse-selftrap-result.md)) established that a transverse photon self-traps into a localized bound photon (mass emerges) but the (2,3) winding does NOT emerge on the continuum engine (Mode II). That result is about *internal structure*; THIS probe is about *mobility of the proven localization* — an orthogonal next layer.

## §2 The load-bearing duality the test adjudicates

The Γ=−1 saturated boundary is BOTH `c_local→0` (hyper-rigid → PIN) AND `c_eff→∞` (interior advects). The two are NOT contradictory — they describe different locations of a saturated core:

- **Boundary shell (A→1):** `resonant-lc-solitons.md:50` (verbatim): *"the nodes at the saturation boundary are geometrically jammed at the absolute hard-sphere exclusion limit. The local phase velocity (c_local=1/√(LC)) strictly collapses to zero, creating a hyper-rigid, localized envelope."* → the PIN candidate. The saturated shell IS a frozen-clock mirror (Γ=−1).
- **Interior (Master Equation):** `111_master_equation_audit_and_engine_gap.md:41` (verbatim): the effective wave speed `c_eff(V)=c₀·(1−A²)^(−1/4)=c₀/√S → ∞` as A→1. → the ADVECT candidate. A boost imparted to the interior could carry the envelope.

**The question the centroid adjudicates:** does the rigid boundary pin the whole envelope (the saturated shell holds position despite `k_x≠0`), or does the interior carry the boost (core + envelope translate together)?

**Grant adjudication (2026-06-04, recorded in brief):** test the transverse `k_x` boost FIRST — the literal *"does the self-trapped lump translate."* A PIN result is the clean structural finding (frozen clock holds; the corpus's actual electron motion is then longitudinal bulk-modulus displacement, `de-broglie-standing-wave.md:50` — a separate follow-up, NOT this probe).

## §3 substrate-native-check CP8 — the generative-precursor walk

Fired `substrate-native-check` (Checkpoint 8) + `pre-test-physics-check` before locking the design.

| Checkpoint | Finding |
|---|---|
| **Substrate dynamics** | Wave propagation (FDTD leapfrog on the scalar Master Equation `∂²V/∂t²=(c₀²/S)∇²V`). NOT minimization, NOT gradient-descent, NOT Helmholtz-eigensolve. |
| **Sector** | Scalar `V`-field continuum realization of the Master Equation (the engine doc 111 calls the full `c_eff(V)` realization). Single-field, real-space. |
| **Objective (AVE-native)** | Watch autonomous self-trap + translation under the saturation kernel. No energy functional. |
| **Coordinate system (Checkpoint 4 — THE one)** | The observable is the energy-density **centroid in REAL space**, and that IS the correct coordinate here — the corpus claim under test ("does the lump translate") is literally a real-space displacement (`de-broglie-standing-wave.md:50` "its motion displaces the lattice"). This is NOT the phase-space-(2,3) trap; translation is a real-space observable. `phase-space-coordinate-check`: centroid is real-space, appropriate (brief states this explicitly). |
| **Saturation-modulated local clock (Checkpoint 5)** | This IS the physics under test. Saturated core A→1 ⇒ `ω_local→0` (clock freezes) ⇒ the PIN prediction. Interior `c_eff→∞` ⇒ the ADVECT prediction. Accounted for via the saturated-core-vs-envelope discriminator. |
| **Sampling discipline (Checkpoint 7)** | PML cells (`pml_thickness=4`) EXCLUDED from centroid/FWHM. The breather is a FILLED core (sech), so centroid-of-core is valid (NOT the empty-middle shell trap). |
| **Checkpoint 8 (generative precursor)** | Seed = the PROVEN v14 breather (Mode-I PASS) — the generative precursor for "a self-trapped core." Mobility is the layer ADDED on top. NOT planting a "finished moving electron"; taking the proven host + the single simplest momentum operator (`k_x` phase ramp via the `V_prev` leapfrog lag). Matched baseline = phase-scrambled (preserves power spectrum). A non-hostable mobility layer = structural-capability finding. |

**Boost-mechanism verification (numerical, NOT a framing probe — Step-2 corpus-search territory):** the `V_prev`-lag is the correct momentum operator for the 2nd-order leapfrog. `V = env·cos(k_x x)`, `∂_tV = ω·env·sin(k_x x)` at t=0 ⇒ `V_prev = V(−dt) = V − dt·∂_tV`. Sanity-probed in the LINEAR regime (tiny-amplitude Gaussian + `k_x` ramp): centroid translated **+12.6 cells at v_obs=+0.81·c₀** in +x, while the `k_x=0` control stayed put (−0.22 cells = migration-noise floor). Mechanism sound; applied to the breather below.

**pre-test-physics-check outcome:** the framing was ALREADY adjudicated by Grant in the brief (boost `k_x` first; PIN = clean structural finding) and the duality is settled by the corpus (the two `c` statements describe boundary-shell vs interior, verify-before-cite confirmed). No open framing question remains for Grant; proceed.

## §4 The CP8 test design (3 arms)

<!-- skeleton -->

## §5 Observable + discriminator (saturated-core vs envelope centroid)

<!-- skeleton -->

## §6 Forward-predicted group velocity (driver-honesty, stated BEFORE the run)

<!-- skeleton -->

## §7 Expected outcomes (MOVES / PINS / DISPERSES)

<!-- skeleton -->

## §8 Auditor queue

<!-- skeleton -->
