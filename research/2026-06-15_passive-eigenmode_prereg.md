# Passive winding-protected electron eigenmode — the hybrid (V,ω) high-Q standing mode — PREREG (Rule-11)

> **STATUS: DRAFT v2 — auditor-FLAG addressed (panel `wyxwc215e`, 4 dims, all FLAG/freeze-after-fix);
> THREE physics-framing forks open to Grant (§11) before freeze.** Freeze (→ `_FROZEN`) only after
> Grant's §11 voice + a re-gate confirms the must-fix items landed. Grant-gated 2026-06-15 (B1
> green-lit; high-Q refinement). Lane: `_orchestration/2026-06-15_passive-eigenmode-solve.md`.
> **Rule 11 — commitment written BEFORE the driver; no knobs tuned to force a result.**

---

## §1 — The question (Rule-11 what-I-expect-and-why)

Does the **fully-coupled hybrid (V≠0 ∧ ω≠0) wave-eigenmode** of a substrate **$\Gamma=-1$
saturation cavity** exist as a **stable (real-eigenvalue), dissipationless standing mode** — with
the conserved $(2,3)$ winding imposed as a **topological boundary condition on the independent
Cosserat-ω carrier** — and what is its **radiative Q** (its leak to the photon continuum)?

**What I expect (honest):** genuinely uncertain. Two adjacent passive routes returned negatives
(§3), but **neither tested the imposed-BC hybrid-coupled mode** — every prior run let the winding
be *self-selected* (gradient flow on an objective; or a pure-V seed hitting the ω=0 trap).
Imposing the winding as a BC is the untried framing.

**Conditional prediction + its HYPOTHESIS status (do not assert as fact):** IF a stable hybrid
mode exists, its **radiative Q is finite** and is plausibly set by the cross-coupling. The premise
that *"bind-strength and leak-rate are one coupling"* is the **HYPOTHESIS UNDER TEST, not a corpus
result** (no anchor found in sweep `wyxwc215e`). Two distinct candidate values are pre-registered
as **discriminating** (§5 F3): bare-α LC-tank reactive leak → **Q ≈ 1/α ≈ 137.0**
(`theorem-3-1-q-factor.md:83`); the engine's chiral binder κ_chiral = α·κ̃ = α·1.2 → **Q ≈
1/κ_chiral ≈ 114.2**. Which one fires is a physics read (§11 fork 2).

---

## §2 — The high-Q reframe (Grant 2026-06-15) — the false-negative guard, OPERATIONALIZED

The electron is **NOT lossless.** It is **high-Q** with a **finite radiative leak**. A strictly-
lossless **Q=∞** mode is the **α=0 *decoupled* limit** — the wrong object. **The solve targets the
dissipationless, stable (real-eigenvalue) COUPLED mode AND measures its radiative Q.**

**EXCLUDED is OPERATIONAL, not ontological (auditor fix):** the **EXCLUDED** bin applies **ONLY to
the explicit α=0 decoupled CONTROL arm** (§7.7 / F0). **A coupled-α production run can NEVER be
binned EXCLUDED** — it can only be POSITIVE / NEGATIVE-A / NEGATIVE-B. A coupled run that converges,
is stable, but returns **Q→∞ (no measurable leak)** is **NEGATIVE-B-adjacent (no radiative channel
found)**, NOT "wrong object." This closes the loophole where "decoupled artifact" could relabel a
real coupled-solve negative.

---

## §3 — Prior corpus state (verify-before-cite; from sweep `wte7dhv5v` + audit `wyxwc215e`)

| Route | Status | Anchor (auditor-corrected) |
|:---|:---|:---|
| Energy/S11 gradient-flow stationary-point | **FALSIFIED** (GT not a stationary point; selected by topological ansatz) | `…abcd-handoff…retrofit.md:24,50` |
| ↳ method dispreferred as SM/QM-style energy-stationarity (Rule 6, avoid) | corpus avoid-verdict | `72_vacuum_impedance_design_space.md:238` (NOT VEM:1692 — that is the *replacement* method) |
| Decoupled wave-eigensolve (V=output) | **Mode III, no bound state at ω_C** | `74_r7_k4tlm_lctank_run_result.md:57`; `126_…standing_wave_eigenmode…:17` |
| ABCD direct eigensolver | proposed-then-retired, no code | `2026-05-18_abcd-eigensolver-workstream-handoff.md:1-14` |
| **Hybrid-coupled (V≠0 ∧ ω≠0), Op14 binder — UNTRIED (this prereg)** | named residue (the L3 doc proposes **quadrature SEEDING**; this prereg's **imposed-BC** is its evolution) | `72_…:158`; `nyquist-binding-route_CLOSED.md:54-58` |

**Constraints any solve must clear (and how imposed-BC clears them):**
- **ω≡0 trap** (`W_refl` even in ω → pure-V can't spin up charge; `2026-06-06_simulation-assumptions-audit.md:13`)
  → the imposed (2,3) winding-BC supplies the odd ω.
- **Binder-must-be-nucleated** (impose → 91% retention; withhold → disperse;
  `2026-06-04_full-electron-option-B-discrete-emergence-result.md:348,358`) → the charter imposes it.

**Prior Q datapoint (scope honesty):** `2026-06-04_full-electron-transverse-selftrap-result.md:P7`
reports a **PARTIAL Q ≈ α⁻¹ = 137** from a leak-per-cycle estimate on `fdtd_3d.py` (no Cosserat) —
so this lane's Q is the **first HYBRID-on-Cosserat** measurement, not the first Q ever.

**Scope boundary (substitution-not-retraction):** this prereg is **NOT** the Layer-8 "smallest
stable soliton, $m_e$ NOWHERE in inputs" emergence target (`nyquist-binding-route_CLOSED.md:56-58`)
— that dissolves the $m_e/\ell_{node}$ DOF and is a strictly stronger object. This lane tests
existence + stability + radiative Q of an **imposed-BC** mode (§9).

---

## §4 — Discriminator + bins

**Classification (`consistency-vs-emergence`):** EXISTENCE + STABILITY = **emergence test**
(genuine). The **Q VALUE** is classified separately (§6 echo/chord).

| Bin | Condition | Reading |
|:---|:---|:---|
| **POSITIVE** | stable real-eigenvalue hybrid (V,ω) mode; (2,3) conserved on ω-carrier (F4 gate passed); **finite radiative Q**, binned 137 vs 114 (F3) | **eigencavity STRUCTURE is real** |
| **NEGATIVE-A** | coupled solve does not converge / disperses | no standing mode → structure fails |
| **NEGATIVE-B** | converges but unstable (max-eig real-part > 0 / requires gain) **OR** stable but **Q→∞** (no radiative channel) | not a passive radiating eigenstructure |
| **EXCLUDED** | **ONLY** the explicit α=0 decoupled control "finds nothing" | wrong object — EXCLUDED is unavailable to any coupled run |

---

## §5 — Falsifier ledger (locked) + instrument-validation gates

| # | Falsifier | PASS condition |
|:---|:---|:---|
| **F0** | baseline / decoupled control: α=0 (or V=0/ω=0) returns no bound state | reproduces Mode-III; **this is the only EXCLUDED-eligible arm** |
| **F1** | existence: hybrid coupled solve converges | residual → 0 |
| **F2** | stability: dissipationless / no gain | max Jacobian-eigenvalue real-part ≤ 0 |
| **F3** | **radiative Q finite, binned** | $Q=\omega_C\cdot E_\text{stored}/P_\text{radiated}$ (radiated **POWER**), finite; **±5% band** around **137.0 (bare-α)** OR **114.2 (κ_chiral=α·1.2)** — these are DISTINCT, discriminating reads; **Q→∞ on a coupled run = NEGATIVE-B**, not EXCLUDED |
| **F4** | winding conserved on the **ω-carrier** | (2,3): toroidal-2 + poloidal-3 via `extract_2_3_omega_fast` — **NOT** the `(V_inc,V_ref)` phasor (double-count guard); **gated on G4** |
| **F6** | conserved-not-pumped | mode stands with **NO drive**; drive-sustained = NEGATIVE |

**Instrument-validation gates — MUST pass BEFORE any production read is credible** (the corpus
plant-at-scale-before-de-novo discipline; the t2-genesis "detector-can't-certify-the-known-positive"
defect guard):

| Gate | Validates | PASS condition |
|:---|:---|:---|
| **G1** | residual / existence (F1) | sech eigen-profile **converges**; generic Gaussian **disperses** (`cage_stiffening_wall.py:109`; `cage-stiffening-wall_result.md:12,13`) |
| **G2** | stability-eig layer (F2) — NEW BUILD | returns max-real-part ≤ 0 on a **known-stable** mode AND > 0 on a **known-unstable/gain** seed |
| **G3** | radiative-Q layer (F3) — NEW BUILD | returns the **analytic Q of a known open resonator** (calibrate the stored/radiated accounting); state lattice N, dt, and a **Nyquist-resolvability** assertion for ω_C (corpus flags real-space ω_C sub-Nyquist, `75_…:176` — read Q in the phasor frame or prove resolvability) |
| **G4** | winding extractor (F4) | **PLANT-AT-SCALE**: seed a known (2,3) at **THIS run's (N,R,r)**; `extract_2_3_omega_fast` must read back (2,3) with **rel > 0.1**. The extractor is validated in general (`test_unified_quadrature_v7.py:142,153`) but is **SCALE-DEPENDENT** — collapses to (2,2)/garbage at minor radius r≈1.1 cells (`2026-06-09_extractor-poloidal-misread_note.md:37-39`). If the run's r is near 1.1, **G4 fails and F4 is uncertifiable on this lattice** — caught pre-freeze. |

---

## §6 — Q-value classification (echo vs chord) — `ave-discrimination-check` + `project_alpha_keystone_echo_resolved`

`Q_TANK = 1/α` is a **calibration identity, NOT a derivation** (`theorem-3-1-q-factor.md:19`;
clm-g0mkne conf 0.45 input-only; interlock ilk-rr14gt — "fitted-identification", the substrate does
NOT independently select R·r=¼). **If α enters the solve as an input** — the driver imports
`KAPPA_CHIRAL_ELECTRON = ALPHA × KAPPA_TILDE_ELECTRON` (`cosserat_field_3d.py:131`; α-injection at
`:124`; the bare factor κ̃=1.2 at `:98` is **α-FREE**) — then a measured Q is a **consistency
identity (ECHO)**; the lane must **NOT** overclaim Lane-2-alone "derives α."

**Driver-binding declaration (auditor fix — the echo/chord verdict hinges on this):** the driver
**MUST declare which coupling it imports**: `KAPPA_CHIRAL_ELECTRON` (`:131`, α-IN → ECHO-locked) vs
`kappa_tilde_torus` (`:98`, α-FREE → CHORD-eligible). The result tags its Q accordingly.

**The CHORD is CONTINGENT, not available today (auditor fix — corrects the headline):** the
cross-lane chord = agreement of **two INDEPENDENT α-free geometric routes** to Q. **Lane-1's leg is
the OPEN frontier (Path C), not an established route:** the α-free K4 path-count z₀=52 gives
α⁻¹≈**138.9**, **1.5% off** the calibrated 137.036, and *"z₀=52 is not physically forced"*
(`2026-06-08_ave-electron-definitive.md:40,45`; `2026-05-18_z0-first-principles-attempt-result.md:90`;
`theorem-3-1-q-factor.md:118` — "two paths agree" is a consistency check, NOT a first-principles
derivation). **The chord fires ONLY IF Lane-1 Path C closes (α-free z₀≈51.25).** A Lane-2 positive
banked against the present z₀=52 leg would **manufacture an apparent chord from two α-absorbing
routes** — forbidden. (Note: the chord needs ~1.5% Q precision; the §7.6 shear-clock evaluation
carries a ~3.2% ω_C systematic of the same order — another reason the chord is not yet reachable.)

---

## §7 — Method (the driver brief)

1. **Impose** the (2,3) winding as a topological BC on the **independent Cosserat-ω carrier**
   (`fast_winding_extractor.py:165` read-out; charge = Beltrami helicity `cosserat_field_3d.py:450`).
   **Never** wire into `(V_inc,V_ref)` (`master-equation.md:20`; `k4_tlm.py:346` — `V_ref` is a
   read-only projection of `V`).
2. **Closed-cavity hybrid eigensolve:** Op14 saturation $z(x)=S[\psi]$ renders $\Gamma=-1$ as a
   **boundary condition** (`substrate-native-check` CP10 — NOT a bulk energy/force term, which
   detonates); solve the coupled (V,ω) wave-eigenproblem (both sectors nonzero) → eigenmode φ +
   **real** ω_C.
3. **Self-consistency** $\psi\leftarrow\phi$ → fixed point; residual→0. **Reuse** `find_eigenstate`
   (`eigenvalue_root_finder.py:60`) / relax_* (`cosserat_field_3d.py:1453/1317`) **ONLY with
   `f_fn` = the wave-operator eigenvalue RESIDUAL** $\lVert L[\phi]-\omega^2\phi\rVert$ — **NOT** an
   energy or S11 functional (closes the hazard-1 loophole: a scalar root-finder can re-instantiate
   the falsified gradient-flow objective). **Do NOT** run `relax_to_ground_state`/`relax_s11`.
4. **Stability layer (BUILD):** finite-difference Jacobian of the fixed-point map → eigenvalues
   (primitives exist: exact gradient `cosserat_field_3d.py:1403` + Verlet step `:1808`; the eig
   step does not). **Validate via G2 before reading F2.**
5. **Radiative-Q layer (BUILD):** the Γ=−1 wall's residual transmission is the radiative coupling;
   measure $Q=\omega_C\cdot E_\text{stored}/P_\text{radiated}$. **Validate via G3 (analytic open
   resonator + Nyquist statement) before reading F3.**
6. ω_C on the **shear** clock $c_\text{shear}=c_0(1-A^2)^{1/4}$ (**Operator 16**,
   `universal_operators.py:969`; adjudicated `2026-06-09_substrate-temporal-values-definition.md:51`)
   — **NOT** the stale ½ (`op14-local-clock-modulation.md:17`) nor `c_EM`. State whether ω_C is
   evaluated at local $A^2(r)$ or a reference $A^2$ (the ~3.2% onset shift is the chord's order).
7. **Controls:** G1 sech-converges/Gaussian-disperses **+** the **decoupled (α=0)** control (the
   only EXCLUDED-eligible arm; confirms the coupling is load-bearing).

**PLATFORM — Grant framing-gate (§11 fork 1; the prereg CANNOT freeze with this unresolved):**
- **Default = option (a):** run the hybrid purely on **`CoupledK4Cosserat`** (branch 2), rendering
  the $\Gamma=-1$ wall as the engine's **own impedance-Γ clamp** (`k4_cosserat_coupling.py:674-686`)
  — **firewall-legal, NO `crystal_engine`.**
- **HONEST SCOPE CAVEAT:** the coupled engine's scalar is a `v_scalar_from_v_inc` projection (**no
  independent A1 `c_eff→∞` cage**; `engine-capability-map.md` §2, §3.1 irrotational↮winding firewall).
  So option (a) tests the **RESTRICTED hybrid** (projected-scalar ⊗ ω with a Γ-BC), **NOT** the full
  A1-cage⊗T2. A NEGATIVE on (a) **may reflect the projected-scalar limitation, not a true structural
  absence** — bounds what (a) can conclude.
- **Option (b)** = the full A1-cage⊗T2 cross-firewall **"substrate-complete engine that does not
  exist"** (`engine-capability-map.md` §4) — **needs Grant sign-off** per the
  `ave-loop-gap-harness-discipline` anti-loophole guard **+** building a new engine.
- **No new `chiral_lattice_v{N}` / `genesis_v{N}` either way.**

---

## §8 — Hazards / DO-NOT (locked)

1. **Do NOT** re-run the falsified gradient-flow stationary-point — incl. via `find_eigenstate` with
   an energy/S11 `f_fn` (pin it to the operator-residual, §7.3).
2. **Do NOT** wire the winding into `(V_inc,V_ref)` (genesis-24/crystal `w_pol=0` double-count).
3. **Do NOT** seed pure-V and let it relax (ω=0 trap) — impose the winding BC.
4. **Do NOT** bin a coupled run EXCLUDED — EXCLUDED is the α=0 control arm only (§2/§4).
5. **Do NOT** render Γ=−1 as a bulk term (CP10 — detonates).
6. **Do NOT** claim the lane *resolves* the A1-vs-T2 sector (bears-on; note, not derivation;
   $m_ec²$ magnitude hypothesis-class, `photon-identification.md:19`).
7. **Do NOT** bank a winding read (F4) or a stability/Q read (F2/F3) before its gate (G4/G2/G3) passes.
8. **Do NOT** present the cross-lane chord as available — it is contingent on Lane-1 Path C (§6).

---

## §9 — Scope (`consistency-vs-emergence` honest scope)

A negative here is **"no stable passive hybrid eigenmode on this platform/regime"** (and, under
option (a), bounded by the projected-scalar limitation), NOT "no electron." A positive is **"the
eigencavity structure is a real passive radiating eigenstructure with finite Q"** — **bearing on**
(not resolving) the mass sector, and a **candidate** input to the cross-lane Q triangulation
**contingent on Lane-1 Path C**. Any re-test on a different engine/regime gets its own prereg.

---

## §10 — Reproduce / deliverables (for the driver)

- Driver in `src/scripts/vol_1_foundations/` (own worktree); reuse-not-rebuild §7 infra; build only
  the stability + radiative-Q layers (with their G2/G3 validation). Canonical constants via
  `from ave.core.constants import …` (`ave-canonical-source`); `verify_constants` before output.
- Result reports: the bin (§4); the **measured Q** binned 137-vs-114 with its **echo/chord tag** and
  the **driver-binding declaration** (§6); the winding on the ω-carrier **after G4** (§5); the G1–G4
  gate outcomes; the decoupled control. Tag `ave-driver-script-honesty` + `consistency-vs-emergence`
  + `ave-discrimination-check` + `ave-apparatus-floor-attribution`.

---

## §11 — Open framing-gate to Grant (pre-freeze; flag-don't-fix)

The auditor surfaced three **physics-framing forks** the lane cannot resolve in-discipline:

1. **Platform (§7):** option (a) **restricted** hybrid on `CoupledK4Cosserat` (projected scalar +
   Γ-BC clamp, firewall-legal, no independent A1 cage — a NEGATIVE may be the projection's limit,
   not a true absence) **vs** option (b) **full** A1-cage⊗T2 cross-firewall engine (needs your
   sign-off + building the substrate-complete engine, which does not exist). Default (a); your call.
2. **F3 mechanism (§5):** does the radiative leak go as **bare α (Q≈137)** or the engine's
   **κ_chiral=α·1.2 (Q≈114)**? Pre-registered as discriminating; flagging because which one fires is
   load-bearing for the echo/chord read.
3. **Chord contingency (§6) — correction to the 2026-06-15 headline:** Lane-1's α-free Q leg is the
   **OPEN Path C** (z₀=52 → 138.9, 1.5% off; both lift-routes closed NEGATIVE), not an established
   route. The cross-lane chord is **contingent on Path C closing** — not a cross-check available the
   moment Lane-2 produces a Q.
