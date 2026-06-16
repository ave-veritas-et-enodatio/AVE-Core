# Passive winding-protected electron eigenmode — the hybrid (V,ω) high-Q standing mode — PREREG (Rule-11)

> **STATUS: DRAFT — auditor-gate PENDING; freeze (→ `_FROZEN`) after the read-only
> `ave-auditor` clears.** Grant-gated 2026-06-15 (B1 green-lit; high-Q refinement). Lane:
> `_orchestration/2026-06-15_passive-eigenmode-solve.md`. **Rule 11 — this is the commitment
> written BEFORE the driver; what I expect, why, and what discriminates, locked in advance.**
> **No knobs may be tuned to force a result.**

---

## §1 — The question (Rule-11 what-I-expect-and-why)

Does the **fully-coupled hybrid (V≠0 ∧ ω≠0) wave-eigenmode** of the substrate's **self-induced
$\Gamma=-1$ saturation cavity** exist as a **stable (real-eigenvalue), dissipationless standing
mode** — with the conserved $(2,3)$ winding imposed as a **topological boundary condition on
the independent Cosserat-ω carrier** — and what is its **radiative Q** (its leak to the photon
continuum)?

**What I expect (honest):** genuinely uncertain. Two adjacent passive routes returned negatives
(§3 prior-state), but **neither tested the imposed-BC hybrid-coupled mode** — every prior run
let the winding be *self-selected* (gradient flow on an objective; or a pure-V seed hitting the
ω=0 trap). Imposing the winding as a BC is the untried framing. **Prediction (conditional):** IF
a stable hybrid mode exists, its **radiative Q ≈ 1/α ≈ 137** — because the **same Op14
cross-coupling that BINDS the mode also LEAKS it** to the continuum: bind-strength and leak-rate
are **one coupling**, and that coupling is α.

---

## §2 — The high-Q reframe (Grant 2026-06-15) — the false-negative guard

The electron is **NOT lossless.** It is **high-Q: Q = 1/α = 137**, and the residual leak **is
α** (its radiative coupling to the photon continuum). A strictly-lossless **Q=∞** mode is the
**α=0 *decoupled* limit** — the wrong object, which finds **nothing** (zero leak ⇒ zero bind,
since they are one coupling).

**Therefore the solve targets the dissipationless, stable (real-eigenvalue) COUPLED mode AND
measures its radiative Q. A finite Q ≈ 137 is the POSITIVE.** Solving for Q=∞ and finding
nothing is a **false negative** and is **excluded**, not banked.

---

## §3 — Prior corpus state (verify-before-cite; from sweep `wte7dhv5v`)

| Route | Status | Anchor |
|:---|:---|:---|
| Energy/S11 gradient-flow stationary-point | **FALSIFIED** (GT not a stationary point; selected by topological ansatz; SM-leakage) | `…abcd-handoff…retrofit.md:24,50`; `VACUUM_ENGINE_MANUAL.md:1692` |
| Decoupled wave-eigensolve (V=output) | **Mode III, no bound state at ω_C** | `72_vacuum_impedance_design_space.md:21,158` |
| ABCD direct eigensolver | proposed-then-retired, no code | `2026-05-18_abcd-eigensolver-workstream-handoff.md:1-14` |
| **Hybrid-coupled (V≠0 ∧ ω≠0), Op14 binder** | **UNTRIED — this prereg** | `72_…:158`; `nyquist-binding-route_CLOSED.md:54-58` |

**Constraints any solve must clear (and how the imposed-BC framing clears them):**
- **ω≡0 trap** (`W_refl` even in ω → pure-V can't spin up charge; `simulation-assumptions-audit.md:13`)
  → the imposed (2,3) winding-BC supplies the odd ω.
- **Binder-must-be-nucleated** (impose (2,3) → 91% retention; withhold → disperse;
  `option-B-discrete-emergence-result.md:348,358`) → the charter imposes the winding.

---

## §4 — Discriminator + bins

**Classification (`consistency-vs-emergence`):** EXISTENCE + STABILITY = **emergence test**
(genuine). The **Q VALUE** is classified separately (§6 echo/chord).

| Bin | Condition | Reading |
|:---|:---|:---|
| **POSITIVE** | stable real-eigenvalue hybrid (V,ω) mode at ω_C; (2,3) conserved on ω-carrier; **finite radiative Q ≈ 1/α ≈ 137** | **eigencavity STRUCTURE is real** |
| **NEGATIVE-A** | self-consistency does not converge / disperses | no standing mode → structure fails |
| **NEGATIVE-B** | converges but largest stability eigenvalue real-part > 0 (requires gain) | not a passive eigenstructure |
| **EXCLUDED (false-neg guard)** | Q=∞ / α=0 / decoupled-limit "finds nothing" | **WRONG object — excluded, NOT a negative** |

---

## §5 — Falsifier ledger (locked)

| # | Falsifier | PASS condition |
|:---|:---|:---|
| **F0** | baseline: decoupled (V=0 or ω=0) returns no bound state at ω_C | reproduces prior Mode-III (sanity) |
| **F1** | existence: hybrid coupled solve converges to a bound mode | residual → 0 |
| **F2** | stability: dissipationless / no gain | max Jacobian-eigenvalue real-part ≤ 0 |
| **F3** | **radiative Q finite & ≈ 137** | open-cavity $Q=\omega_C\cdot$stored/radiated, finite, ≈ 1/α; **Q=∞ = decoupled artifact = EXCLUDED** |
| **F4** | winding conserved on the **ω-carrier** | (2,3): toroidal-2 + poloidal-3 via `extract_2_3_omega_fast` — **NOT** the `(V_inc,V_ref)` phasor (double-count guard) |
| **F5** | detector validated | sech eigen-profile **converges** (pos. control); generic Gaussian **disperses** (neg. control) |
| **F6** | conserved-not-pumped | mode stands with **NO drive**; drive-sustained = NEGATIVE |

---

## §6 — Q-value classification (echo vs chord) — `ave-discrimination-check` + `project_alpha_keystone_echo_resolved`

`Q_TANK = 1/α` is a **calibration identity, NOT a derivation.** If α enters the solve as an
input (coupling `κ_chiral = 1.2·α`, `cosserat_field_3d.py:98`), then a measured Q≈137 is a
**consistency identity (ECHO)** — the lane must **NOT** overclaim Lane 2 alone "derives α."

**The CHORD** (per the cross-lane headline) is the **agreement of two independent geometric
routes to Q**: Lane 2's measured eigenmode-leak Q vs Lane 1's constraint-count geometric Q
(z₀=52 + 2α gap), at the measured α. **The result MUST tag its Q with the echo/chord
classification** (is Q produced with α as an input → echo; or α-free from geometry → chord
candidate). This lane's deliverable Q becomes a **cross-check input to Lane 1**.

---

## §7 — Method (the driver brief)

1. **Impose** the (2,3) winding as a topological BC on the **independent Cosserat-ω carrier**
   (`fast_winding_extractor.py:165` for read-out; charge = Beltrami helicity
   `cosserat_field_3d.py:450`). **Never** wire into `(V_inc,V_ref)` (`master-equation.md:20`;
   `k4_tlm.py:346` — `V_ref` is a read-only projection of `V`).
2. **Closed-cavity hybrid eigensolve:** Op14 saturation $z(x)=S[\psi]$ renders the $\Gamma=-1$
   wall as a **boundary condition** (`substrate-native-check` CP10 — NOT a bulk energy/force
   term, which is singular at the wall and detonates); solve the coupled (V,ω) wave-eigenproblem
   (both sectors nonzero; Op14 cross-coupling load-bearing) → eigenmode φ + **real** ω_C.
3. **Self-consistency** $\psi\leftarrow\phi$ (winding-preserving projection) → fixed point;
   residual→0. **Reuse** `find_eigenstate` (`eigenvalue_root_finder.py:60`) / relax_*
   (`cosserat_field_3d.py:1453/1317`). **Do NOT** re-run gradient descent on an energy/S11
   objective (falsified + SM-leakage, §3).
4. **Stability layer (BUILD):** finite-difference Jacobian of the fixed-point map → eigenvalues
   (the primitives — exact gradient + Verlet step — exist; the eig step does not).
5. **Radiative-Q layer (BUILD):** the Γ=−1 wall's **residual transmission = the radiative
   coupling = α**; measure $Q=\omega_C\cdot$stored/radiated.
6. ω_C on the **shear** clock `c_shear = c₀(1−A²)^{1/4}` (INVARIANT-S2), **not** the stale ½
   (`op14-local-clock-modulation.md:17`) nor `c_EM`.
7. **Controls:** sech-converges / Gaussian-disperses (detector validation) **+** decoupled-(α=0)
   finds-nothing (confirms the coupling is load-bearing — the false-negative guard is physical).

**Platform** (`ave-loop-gap-harness-discipline`): hybrid spans the A1/bulk Γ=−1 cavity
(`crystal_engine.py`/`master_equation_fdtd.py`) ⊗ the Cosserat-ω carrier (`CosseratField3D` +
coupled `VacuumEngine3D`/`CoupledK4Cosserat`). **No new `chiral_lattice_v{N}` / `genesis_v{N}`.**

---

## §8 — Hazards / DO-NOT (locked)

1. **Do NOT** re-run the falsified gradient-flow stationary-point (energy/S11 descent).
2. **Do NOT** wire the winding into `(V_inc,V_ref)` (genesis-24/crystal `w_pol=0` double-count).
3. **Do NOT** seed pure-V and let it relax (ω=0 trap) — impose the winding BC.
4. **Do NOT** solve for Q=∞ / lossless / decoupled — that is the false-negative (excluded).
5. **Do NOT** render Γ=−1 as a bulk term (CP10 — detonates; cf. the genesis PUMP DETONATE arm).
6. **Do NOT** claim the lane *resolves* the A1-vs-T2 sector — it **bears on** it (note, not
   derivation; $m_ec²$ magnitude hypothesis-class).

---

## §9 — Scope (`consistency-vs-emergence` honest scope)

A negative here is **"no stable passive hybrid eigenmode on this platform / regime"**, NOT "no
electron." A positive is **"the eigencavity structure is a real passive eigenstructure with
radiative Q ≈ 1/α"** — bearing on (not resolving) the mass sector, and feeding the cross-lane
Q triangulation (the chord test). Any re-test on a different engine/regime gets its own
prereg + version + verification chain.

---

## §10 — Reproduce / deliverables (for the driver)

- Driver in `src/scripts/vol_1_foundations/` (own worktree); reuse-not-rebuild the §7 infra;
  build only the stability + radiative-Q layers. Canonical constants via
  `from ave.core.constants import …` (`ave-canonical-source`); `verify_constants` before any
  output. `--smoke` for CI; `--production` for the binned result.
- Result doc reports: the bin (§4), the measured **Q** with its **echo/chord tag** (§6), the
  winding read on the ω-carrier (§5 F4), the detector-control pair (§5 F5), and the
  decoupled false-negative-guard control (§7.7). Tag `ave-driver-script-honesty` +
  `consistency-vs-emergence` + `ave-discrimination-check`.
