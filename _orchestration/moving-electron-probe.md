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

All arms run on `master_equation_fdtd.py` at the validated v14-breather operating point. The breather seed is `profile='sech'`, `A=0.85·V_yield`, `R=2.5` — the Mode-I-PASS config from `r10_master_equation_v14_v2.py` (note: `0.99`/`0.95` higher-amp configs in that sweep are alternative seeds; `0.85, R=2.5` is the canonical breather). Boost is imparted via the `V_prev` leapfrog lag (the proven momentum operator).

> **Amplitude/operating-point note (ave-infinity-discipline):** the engine clips at `A_cap=0.99`, `S_min=0.05` (⇒ `c_eff ≤ √20·c₀`). The brief's validated sweep `{0.3,0.5,0.7}·V_snap/dx` is the transverse-photon-seed sweep on the OTHER engine (`fdtd_3d.py`, `v_yield=V_SNAP`); on THIS engine (`master_equation_fdtd.py`) the v14 breather uses `A·V_yield` with `V_yield=1.0` natural units, and `A=0.85` is the documented stable breather (the `r10_master_equation_v14_v2.py` sweep ran `0.85` to completion — it is NOT the NaN cap here; the engine's `A_cap`/`S_min` clip prevents the divergence). Reuse `A=0.85`, do not re-derive.

| Arm | Seed | Boost | Role |
|---|---|---|---|
| **BOOST** | v14 breather (sech, A=0.85, R=2.5) | transverse `k_x` phase ramp via `V_prev` lag | the test: does the self-trapped lump translate? |
| **STATIONARY (control)** | same breather | `k_x=0` (`V_prev=V`) | the pinned baseline / centroid-migration-noise floor |
| **BASELINE (matched)** | phase-scrambled breather (FFT phase-permute, power spectrum PRESERVED) | same `k_x` as BOOST | controls for amplitude/saturation depth (phase3f Factor-2 fix); same per-component amplitude stats + same spatial envelope, scrambled phase |

The matched BASELINE isolates topology/coherence from amplitude: a translating BOOST must out-translate (and out-retain) the phase-scrambled seed at identical saturation depth — otherwise any "motion" is an amplitude/dispersion artifact, not coherent transport of the self-trap.

## §5 Observable + discriminator (saturated-core vs envelope centroid)

Tracked over the recording window (PML-excluded throughout):
- **(a) energy-density centroid** `x_c = Σ x·V² / Σ V²` → displacement `Δx` + velocity `v_obs = Δx/Δt`.
- **(b) retention** — energy still trapped in the interior post-window (vs radiated into PML).
- **(c) FWHM** — stays localized vs spreads to grid scale.

**The duality discriminator (the load-bearing distinction):** compute TWO centroids —
- **saturated-core centroid**: weighted only over cells where `A > A_sat` (cells at/near saturation, the frozen-clock shell+core).
- **envelope centroid**: weighted over all interior `V²`.

Reading:
- **core + envelope translate together** ⇒ the self-trap MOVES (the boost carries the whole structure; interior-advect wins).
- **core pins while envelope sloshes** (envelope centroid moves but saturated-core centroid stationary, or vice-versa) ⇒ PIN-with-internal-motion (the frozen boundary holds the core; the duality resolves to boundary-pin).

**Verdict bins:**
- **MOVES:** centroid translates coherently at finite `v`, FWHM bounded, displacement ≫ STATIONARY migration-noise, AND core+envelope translate together.
- **PINS:** self-traps (retention high, FWHM bounded) but centroid ≈ stationary despite `k_x≠0` (the frozen-clock prediction); core pinned.
- **DISPERSES:** retention collapses; radiates at `c₀`; no durable trap under boost.

## §6 Forward-predicted group velocity (driver-honesty, stated BEFORE the run)

Per `de-broglie-standing-wave.md:181`, the massive dispersion is `ω²=c²k²+ω_C²`, `ω_C≡m_e c²/ℏ` (Compton frequency); group velocity `v_g=dω/dk=c²k/ω`.

**Substrate-derived `ω_C` in lattice units (NOT an engineering choice):** `ℓ_node = ℏ/(m_e c)` = the reduced Compton wavelength (`constants.py:237,262` verbatim). So `ω_C = m_e c²/ℏ = c₀/ℓ_node`, and in the engine's natural units (`c₀=1`, `ℓ_node↦dx=1`) this is **`ω_C(lattice) = 1.0`** exactly.

Forward-predicted `v_g` (NO tuning — `k_x` chosen as well-resolved cells/wavelength, not to hit a target):

| wavelength (cells) | `k_x` | `ω` | **`v_g/c₀`** | `v_phase/c₀` |
|---|---|---|---|---|
| 6 | 1.047 | 1.448 | **0.723** | 1.383 |
| **8 (PRIMARY)** | **0.785** | **1.272** | **0.618** | **1.619** |
| 12 | 0.524 | 1.129 | **0.464** | 2.156 |
| 16 | 0.393 | 1.074 | **0.366** | 2.736 |

**Primary prediction (`k_x=2π/8`): `v_g = 0.618·c₀`.** `v_g < c₀` always (massive dispersion). Compare observed centroid velocity to this; report predicted-vs-observed; do NOT tune `k_x` to hit a target.

> **Honesty caveat (stated pre-run):** the de-Broglie `v_g` is the GROUP/ENVELOPE prediction for a massive lump moving through the *cold* lattice (`ω_C=1` is the cold-lattice Compton frequency). The breather's *core* sits at saturation (A≈0.85) where the local clock is modulated (`ω_local=ω_C·√S`); the boost carrier `k_x` is imposed on the cold-lattice phase. So `v_g=0.618` is the leading prediction for the envelope transport speed, but a measured `v_obs` somewhat below it (clock-drag from the saturated core) would still be consistent with MOVES — the discriminator is `v_obs` finite & coherent vs `v_obs≈0` (PIN), not a tight match to 0.618.

## §7 Expected outcomes (MOVES / PINS / DISPERSES)

Three structural-capability outcomes, each a clean finding:

- **MOVES** — the engine hosts a MOBILE self-trap: the interior-advect (`c_eff→∞`) channel carries the boost; the corpus electron's transverse translation is a hostable layer on this engine. `v_obs` finite, coherent, ≫ STATIONARY noise, FWHM bounded, core+envelope together.
- **PINS** (the frozen-clock prediction) — the Γ=−1 saturated boundary holds the envelope: self-traps but does not translate despite `k_x≠0`. This is the CLEAN structural finding the brief flags as expected: the frozen clock holds; the corpus's actual electron motion is then the SEPARATE longitudinal bulk-modulus displacement channel (`de-broglie-standing-wave.md:50`), a follow-up probe, not a failure.
- **DISPERSES** — boost destroys the trap: retention collapses, radiates at `c₀`. Would say the breather is fragile to transverse momentum on this engine (the mobility layer is unhostable via this seed/operator).

## §8 Auditor queue

1. **Adjudicate the verdict's corpus propagation** (auditor lands, implementer surfaces): MOVES/PINS/DISPERSES → does this warrant a KB leaf (a `breathing-soliton` mobility addendum) or a research-result-only finding? No manuscript/matrix entry drafted by implementer.
2. **Duality reading**: if PIN-with-internal-motion, the saturated-core-vs-envelope split is the load-bearing observable — confirm the discriminator cleanly separates boundary-pin from interior-advect, or flag if the two centroids co-move ambiguously.
3. **The `ω_C(lattice)=1` mapping** (`ℓ_node`=reduced Compton wavelength ↦ dx): confirm this substrate-derivation is the right cold-lattice dispersion anchor for the forward-prediction, vs a saturated-clock-corrected `ω_C·√S`.
4. **Longitudinal follow-up**: a PIN here makes the longitudinal bulk-modulus displacement channel (`de-broglie-standing-wave.md:50`) the natural next probe — flag as closure-roadmap candidate.
