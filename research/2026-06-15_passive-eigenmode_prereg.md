# Passive winding-protected electron eigenmode — the hybrid (V,ω) high-Q standing mode — PREREG (Rule-11)

> **STATUS: DRAFT v3 — ALL GATES PASSED, FREEZE-READY (pending a final referential-integrity auditor
> pass).** Pre-flights done: (a) `CoupledK4Cosserat` DEAD (wrong sector); (b′) `crystal_engine` V-tank
> VIABLE as a genuine BREATHER ((c) OFF). **Grant 2026-06-15: breather/limit-cycle framing CONFIRMED;
> (b′) cross-firewall coupling GRANTED (eyes-open precedent) with the G0 double-count smoke-gate as
> build-step-zero.** Forks 2–3 ruled: Q SECONDARY (the echo); α an ECHO for the z₀ route. **The
> keystone deliverable = EXISTENCE + STABILITY of the winding-protected hybrid breather (the form /
> structural chord-candidate); Q is the echo — do NOT let the headline drift to "we measured Q."**
> Grant-gated 2026-06-15 (B1; high-Q; existence-primary; breather; b′). Lane:
> `_orchestration/2026-06-15_passive-eigenmode-solve.md`.
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

**THE KEYSTONE IS EXISTENCE + STABILITY (PRIMARY); Q IS A SECONDARY CHARACTERIZATION (Grant
2026-06-15).** The lane's verdict — *does a stable passive high-Q hybrid mode EXIST* — is decided by
**F1 + F2 + F4 ONLY**. The radiative **Q (F3) is measured and reported but does NOT decide the bin**:
the cross-lane chord almost certainly will not fire (**α is an echo for the z₀ route** — §6), so the
lane must NOT hang on Q-agreement.

**THE MODE IS A LIMIT CYCLE / BREATHER, NOT A STATIC FROZEN CORE (pre-flight #2; Grant-CONFIRMED
2026-06-15).** *(Grant checked the one risk — post-hoc bin-shift / ave-prereg referential-integrity:
this is NOT a rescue. The ratified discriminator was a "stable real-eigenvalue mode with finite Q" —
which IS a non-decaying oscillation, i.e. a breather; "static Z→0" was a sub-target of the PRE-FLIGHT
[does the engine reach the wall], answered "at the breath peak, recurrently" = what a high-Q resonator
does. The breather reading is the FAITHFUL one, corpus-canonical.)* The V-tank renders a genuine deep TIR wall that **breathes** (self-focuses to
Γ_TRUE≈−0.43, relaxes, re-focuses — bounded, recurrent, no runaway), exactly the cage's ratified
"persistent breathing cage" and the corpus electron = limit cycle (`selftrap` phasor limit-cycle;
`master-equation.md:20` "A1 breather"). So **"stable real-eigenvalue mode" = a NON-DECAYING
oscillation**, and **EXISTENCE/STABILITY (F1/F2) is read on the CYCLIC / time-averaged mode, not an
instantaneous static Γ**: F1 = a bounded recurrent breather exists (self-focuses each cycle);
**F2 = it does not DECAY (low-Q) or BLOW UP (runaway/gain) over many breaths** (the breather's
cycle-to-cycle envelope is flat/slowly-decaying = dissipationless/high-Q). The radiative Q (F3) is
the breather's **per-cycle leak** (TRUE n=√S, not the proxy S^{1/4}, §8.9).

**Classification (`consistency-vs-emergence`):** EXISTENCE + STABILITY = **emergence test** (genuine,
the keystone). The **Q VALUE** is a separate characterization (§6 echo).

| Bin (decided by F1+F2+F4) | Condition | Reading |
|:---|:---|:---|
| **POSITIVE** | stable real-eigenvalue hybrid (V,ω) mode EXISTS (F1+F2); (2,3) conserved on ω-carrier (F4, G4-gated) | **eigencavity STRUCTURE is real (the keystone)** |
| **NEGATIVE-A** | coupled solve does not converge / disperses | no standing mode → structure fails |
| **NEGATIVE-B** | converges but unstable (max-eig real-part > 0 / requires gain) | not a passive eigenstructure |
| **EXCLUDED** | **ONLY** the explicit α=0 decoupled control "finds nothing" | wrong object — unavailable to any coupled run |

**SECONDARY characterization (NOT bin-deciding):** the radiative Q (F3), binned 137 (bare-α) vs 114
(κ_chiral=α·1.2), tagged echo (§6). A stable mode that exists but reads **Q→∞ (no radiative leak
despite the coupling on)** is still a **POSITIVE on the keystone** — reported as "exists but
radiatively decoupled," which would itself **refute the bind=leak=α hypothesis** (§2), NOT a
NEGATIVE. (This supersedes prereg-v2's "Q→∞ = NEGATIVE-B": Grant's reframe makes existence+stability
primary; Q→∞ on a coupled stable mode is a finding, not a failure.)

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

**🔴 G0 — DOUBLE-COUNT ORTHOGONALITY SMOKE-GATE = BUILD-STEP-ZERO (HARD gate, Grant 2026-06-15).**
The #1 build risk of the (b′) cross-firewall coupling is **NOT** the wall — it is the **two-"3"s
double-count** (the exact genesis-24 failure: wiring the winding into the A1 `(V_inc,V_ref)` phasor;
`master-equation.md:20`; `k4_tlm.py:346`). **Before any production run**, smoke-test the Op14 coupling:
does it keep the (2,3) winding strictly on the **independent Cosserat-ω carrier ⊥ the A1 breather**,
or does it **leak into the `(V_inc,V_ref)` phasor**? **PASS** = winding stays on the ω-carrier,
`w_pol` nonzero, **zero leak into `V_ref`** (which is a read-only projection of `V`). **FAIL** =
abort the build — the coupling is self-inflicting the genesis-24/crystal `w_pol=0` double-count.
This is a **hard gate, not a post-hoc check** — it catches the double-count for a smoke-test instead
of a contaminated production driver.

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

**UPDATE (Grant + Lane-1 grounding, 2026-06-15) — α is an ECHO for the z₀ route; the chord will
very likely NOT fire.** z₀=52 = 4·13 is a **multiplicative path-PRODUCT** (4 ports × 13 paths), but a
Maxwell–Calladine constraint count is **additive** (≈ 4 primary + 12 secondary ≈ **16 → α⁻¹≈49**,
off by 3×). The "1.46%-to-137" was a path-count coincidence dressed with the 8πα identity, never a
constraint count. **Neither amorphous-137 (α-circular fit) nor crystalline-49 is an α-free map → α
is an echo for the z₀/coordination route**, and retiring amorphous makes α *worse*, not better.
Triangulation consequence: even Lane-2's 114 (κ_chiral) vs Lane-1's 49 disagree → **echo regardless**.
**∴ Lane-2's Q is a SECONDARY characterization, not a chord-input** (§4); the lane rests on
existence + stability.

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

**PLATFORM — RESOLVED by two pre-flights; option (b′) GRANTED (Grant 2026-06-15).**
- **(a) `CoupledK4Cosserat` — DEAD** (pre-flight #1): clip-floor pseudo-Γ→−1 + runaway, and it reads
  Γ off **Cosserat ω-curvature** = the **wrong sector** (the (2,3) ω-knot is canon-flagged
  PROTON-family; the canonical unknot electron gave no wall).
- **(b′) `crystal_engine` V-tank wall ⊗ Cosserat-ω winding — GRANTED.** Pre-flight #2 confirmed
  `crystal_engine`'s A1/V-tank renders a **genuine, bounded, recurrent BREATHING TIR wall** (the right
  sector). The build **couples** the existing Cosserat-ω winding carrier to the existing
  `crystal_engine` breathing V-tank wall (the Op14 cross-coupling); reads the hybrid breather's
  existence + cyclic stability + per-cycle Q. **REUSE both validated halves — no new `*_vN` file, no
  from-scratch engine.** Read the wall with the **TRUE n=√S** impedance (`crystal_engine.py:197-200`),
  not the proxy (§8.9).
- **🔴 PRECEDENT (Grant, eyes-open):** this authorizes the **first substrate-complete (cross-firewall)
  engine** — the exact thing the `ave-loop-gap-harness-discipline` anti-loophole guard was built to
  gate. Justified because the need is **empirically forced** (the two pre-flights proved the
  electron's two sectors live in two different engines), but it is a **PRECEDENT, not a one-off** —
  future lanes will reach for it and over-trust it; that is the real cost of the sign-off.
- **BUILD-STEP-ZERO:** the **G0 double-count smoke-gate** (§5) runs FIRST, a hard gate, before any
  production run.

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
9. **Do NOT** read the impedance Γ from the proxy `gamma_bulk` = S^{1/4} (`crystal_engine.py:421-432`,
   `master_equation_fdtd.py:165-168`) — use the **TRUE n=√S** (`Z=1/c_eff`, `c_eff²=c0²/S`,
   `crystal_engine.py:197-200`). **Exponent-defect FLAG (pre-flight #2):** proxy floor −0.240 vs true
   −0.454 (~2×); same exponent-defect family as the clock exponent (§7.6 / Flag-D). Engine/cross-lane
   item — flag, the production driver uses the TRUE form.
10. **Do NOT** read EXISTENCE/STABILITY off an instantaneous static Γ — the mode BREATHES; read the
    **cyclic / time-averaged** mode (§4): F1 = a bounded recurrent breather exists; F2 = it does not
    decay (low-Q) or blow up (gain) over many breaths.

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
- **HEADLINE framing (Grant 2026-06-15):** the result's headline is **EXISTENCE + STABILITY of the
  winding-protected hybrid breather** (the form — the structural chord-candidate, the keystone). The
  **Q is the echo** (α value-imported per Lane-1 + the K=2G result) — report it, but **do NOT let the
  headline drift to "we measured Q."** "The hybrid winding-protected breather exists (or doesn't)" is
  the result; Q is a secondary characterization.
- Result reports: **build-step-zero G0 double-count smoke-gate outcome (§5)**; the bin (§4); the
  **measured Q** binned 137-vs-114 with its **echo/chord tag** and the **driver-binding declaration**
  (§6); the winding on the ω-carrier **after G4** (§5); the G1–G4 gate outcomes; the decoupled
  control. Tag `ave-driver-script-honesty` + `consistency-vs-emergence` + `ave-discrimination-check`
  + `ave-apparatus-floor-attribution`.

---

## §11 — Open framing-gate to Grant (pre-freeze; flag-don't-fix)

The auditor surfaced three **physics-framing forks**; **Grant RULED (2026-06-15):**

1. **Platform — RESOLVED (Grant 2026-06-15): (a) DEAD; (b′) GRANTED; (c) OFF.** Pre-flight #1
   (`CoupledK4Cosserat`): (a) DEAD — clip-floor + runaway, wrong sector (ω-curvature = proton-family).
   Pre-flight #2 (`crystal_engine` V-tank): a **genuine, bounded, recurrent BREATHING TIR wall**, right
   sector. **(c) OFF** (third-engine watch-item did not trigger). **Breather framing CONFIRMED** (not a
   post-hoc bin-shift — a stable real-eigenvalue mode IS a non-decaying oscillation). **(b′) GRANTED**:
   couple the Cosserat-ω winding to the `crystal_engine` breathing V-tank wall (reuse both halves; no
   new engine), read time-averaged/cyclic with TRUE n=√S. **Build-step-zero = the G0 double-count
   smoke-gate (§5, hard).** Eyes-open precedent: first substrate-complete cross-firewall engine (§7).
2. **F3 mechanism (§5) — RULED: pre-registered, awareness only.** 137 (bare-α) vs 114 (κ_chiral=α·1.2
   = the (2,3) factor κ̃); a 114 result = the chiral coupling sets the leak (a real finding). **Not
   bin-deciding** (§4 — Q is secondary).
3. **Chord contingency (§6) — RULED: confirmed; α is an ECHO for the z₀ route.** Lane-1 grounding:
   z₀=52 is a path-PRODUCT coincidence (additive count ≈16 → α⁻¹≈49, off 3×); neither 137 nor 49 is
   an α-free map → echo. The chord very likely will NOT fire. **∴ Lane-2's deliverable is
   EXISTENCE + STABILITY (the keystone); Q is secondary** (§4).
