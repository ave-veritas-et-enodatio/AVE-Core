# Simulation Assumptions Audit — 2026-06-06 session

**Date:** 2026-06-06 · **Branch:** `analysis/2026-06-06-simulation-assumptions-audit` (off `origin/main` `16b6b6b5`)
**Scope:** every load-bearing assumption baked into this session's simulations — the Γ open/short measurement, the (2,3)/V0 survival work, the biquaternion node-algebra, the Cosserat-integrator diagnostic (Phase 0 / 0.5), and the electron-genesis arc (Arm A two-photon collision, Arm B flywheel-seed) — plus the underlying engine they all rest on.
**Method:** each assumption pinned to `file:line` (`verify-before-cite`), tagged for status, and traced to what it affects. **Discipline:** `ave-audit` · `verify-before-cite` · `substrate-native-check` · `ave-canonical-source` · `ave-evidence-framing` · `flag-don't-fix` (surface, don't silently fix).

**Status legend:** ✓ validated/canonical · ⚠ load-bearing-but-cleared-or-caveated · 🔍 surfaced-this-session · ❓ open plumber-question for Grant.

---

## §0 The headline (read this first)

**A1.1 — the engine couples the V-sector and the Cosserat-ω sector ONLY through the *even-in-ω* saturation kernel.** A pure-V seed can modulate the saturation `S(A)` but can **never** provide an odd drive to break the `ω=0` symmetry → `ω≡0` is a fixed point. **The entire electron-genesis (III) verdict is a direct consequence of this one assumption** — the photon cannot birth the charge carrier (Cosserat-ω) in the current engine. This is the open plumber question of the session.

---

## §1 ENGINE assumptions (deepest, load-bearing)

### A1.1 — V↔ω couple ONLY via the even-in-ω saturation; ω=0 is a fixed point ❓ **(headline)**
- **What:** ω is forced by `a_w = -dE_dw / I_omega` where `dE_du, dE_dw = energy_gradient()` (`cosserat_field_3d.py:1550-1552`). The energy enters ω only through `kappa² = ω²` (the even-in-ω saturation `A² = eps²/eps_yield² + kappa²/omega_yield²`, `:332`; `S_kappa² = 1 − kappa²/omega_yield²`, `:655`). So `dE_dw ∝ ω` → **vanishes at ω=0**. The V-sector can *modulate* the ω-stiffness via `S(A)` but supplies **no odd drive**.
- **Affects:** Arm A genesis (III) — pure-V photon → `ω≡0` exact (`omega_max=0.0` all runs, verified). The charge carrier never lights up. Also the Q0 fixed point (sharpens the 2026-06-04 finding).
- **Status:** ❓ **OPEN PLUMBER QUESTION.** Real pair-production makes charge *from light*. Either (a) the engine is **missing an odd V→ω coupling** (the photon's B *should* torque the microrotation) — an engine gap to close; or (b) the decoupling is physical and charge is a **separate ω-seed** (Arm B is then the only route). Not resolvable numerically — needs Grant.

### A1.2 — sources inject V only (the photon is pure-V) 🔍
- **What:** `Source.apply()` injects V (`amp_volts`, `vacuum_engine.py:206-269`); `V_inc` stays 0 unless `thermalize_V=True` (`:57`). PulsedSource / the genesis photon are V-injection.
- **Affects:** with A1.1 → `ω≡0`. The "photon" carries no microrotation.
- **Status:** 🔍 surfaced — engine photon is pure-V; whether a physical photon should carry ω is the A1.1 question.

### A1.3 — Cosserat-ω integrated as flat-ℝ³ velocity-Verlet (not SO(3)/Lie-geometric) ⚠
- **What:** `step_velocity_verlet:1556,1571` — `omega_dot += 0.5·dt·a_w`, flat-vector. No exponential-map/geometric integrator.
- **Affects:** the ω-winding evolution. **Phase 0 (B) cleared this as NOT the V0-degradation cause** (over-saturation was); the geometric integrator was correctly **not built**.
- **Status:** ⚠ load-bearing but Phase-0-cleared. Standing assumption; revisit only if a *quasi-stable* ω-winding regime is found that still leaks.

### A1.4 — saturation kernel `S(A)=√(1−A²)`, `A² = eps²/eps_yield² + kappa²/omega_yield²` ✓
- **What:** `cosserat_field_3d.py:332-334`. Op2/Op14. `eps_yield`↔`V_yield`, `omega_yield`.
- **Affects:** the entire over-yield/pinch-off regime (A→1).
- **Status:** ✓ canonical (Axiom 4).

### A1.5 — the K4-TLM "3"/C↔L scatter is unitary (structure-preserving) ✓
- **What:** scatter+connect unitary; the "3"/V-sector "conserving is the LC's job."
- **Affects:** the (2,3) "3"-half. Phase 0 (B): under over-saturation BOTH sectors collapsed — the unitary "3" was over-driven, not numerically leaked.
- **Status:** ✓ (scatter unitary); (2,3) survival is regime-dependent (Phase 0.5).

---

## §2 SEED / INITIAL-CONDITION assumptions

### A2.1 — the imposed (2,3) plant is a non-eigenmode, all-C (`Φ_link=0` at seed) 🔍
- **What:** `initialize_2_3_voltage_ansatz` seeds `V_inc` only; `Φ_link=0`. Phase 0.5 (II): degrades genuinely, **amplitude-independent** (identical at `A²≈0.07` and `≈6`) — the CP8 plant-the-finished-composite anti-pattern, missing the inductive L-half.
- **Affects:** the V0 fork — the imposed plant **cannot** be the electron (static, all-C, lossy). Motivates the balanced-LC / flywheel seed (Arm B).
- **Status:** 🔍 surfaced (Phase 0.5).

### A2.2 — the two-photon collision is FORCED over-yield (sharp rupture knee) ⚠
- **What:** Arm A — `A²` jumps `0.4→3–4` across ~0.03 amplitude; the drops form at `V/V_yield ≈ 10` in a 16-period window.
- **Affects:** Arm A check-1 FAIL (over-yield). **Caveat:** a longer-window / `use_memristive_saturation` re-run could test whether an over-ruptured core *relaxes* sub-yield.
- **Status:** ⚠ caveat — over-yield is *forced*; the carrier result (ω≡0) is window-independent, but sub-yield-relaxation is **untested** (cheap follow-up).

### A2.3 — the flywheel ansatz (Arm B) seeds ω directly `{ω,R,chirality}` 🔍
- **What:** Arm B seeds a Beltrami ω-flywheel (the "2"/Cosserat-ω) — the seed the photon provably cannot make (A1.1).
- **Affects:** Arm B (running) — tests whether seeding ω relaxes into the (2,3).
- **Status:** 🔍 in-test.

### A2.4 — matched-distribution baseline (same amplitude stats, no topology) ✓
- **What:** CP8 step 2.
- **Affects:** Arm A — the genesis did **NOT** beat the baseline (8.3% vs 29.9% retention) → emergence not amplitude-confounded *and* not achieved.
- **Status:** ✓ discipline.

---

## §3 MEASUREMENT / EXTRACTOR assumptions

### A3.1 — the (2,3) extractor lives in (V_inc,V_ref) phase-space; the SIGN extractor reads NOISE 🔍
- **What:** `r10_2_3_winding_extractor_coordinate.py` — phase-space winding. **Arm A: the charge-sign read inverts** — the same-handed *baseline* read opposite signs while the opposite-handed *genesis* read same signs (+1,+1). It reads noise, not drive chirality.
- **Affects:** Arm A check-5 (charge) **UNRELIABLE in the pure-V pinch-off** — consistent with charge being a Cosserat-ω quantity (A1.1/A6.1), not a V-phasor one.
- **Status:** 🔍 surfaced — do NOT trust V-phasor charge-sign on a pure-V seed.

### A3.2 — V/V_yield per-phasor trace (`A_yield = V_yield/V_snap ≈ 0.085`, `A²_yield ≈ α`) ✓
- **Affects:** the sub-V_yield vs over-yield verdicts (all sims).
- **Status:** ✓ grounded.

### A3.3 — Γ rebuilt from persistent `z_local_field` ✓
- **Affects:** the open/short measurement (|Γ|=1; sign-is-convention).
- **Status:** ✓ (this session's Γ work).

### A3.4 — PML exclusion + density-peak (not centroid) sampling ✓
- **Status:** ✓ discipline (CP7).

---

## §4 NUMERICS assumptions

### A4.1 — finite evolution window (~16 Compton periods) ⚠
- **Affects:** the over-yield-relaxation caveat (A2.2). The carrier (ω≡0) is window-independent; sub-yield-relaxation is window-dependent.
- **Status:** ⚠ caveat.

### A4.2 — sources-off free evolution (Phase 0.5) ✓
- **Status:** ✓.

### A4.3 — `ℓ_node = 1 cell` (electron is one grid cell) 🔍
- **What:** `ELL_NODE_CELLS = 1.0` (genesis). The (2,3) is a *phase-space* (V_inc,V_ref) topology, so 1 real-space cell *can* carry it — but spatial sub-structure of the winding is at grid resolution.
- **Affects:** any real-space read of the (2,3); the size-check (PASS, FWHM=1 cell) is at-resolution.
- **Status:** 🔍 flag — phase-space topology OK at 1 cell; real-space winding sub-structure unresolved.

---

## §5 CANONICAL CONSTANTS ✓

`V_yield=43.65 kV`, `V_snap=511 kV`, `ℓ_node`, `ω_C = c/ℓ_node`, `α`, `K=2G` — all from `src/ave/core/constants.py` (`ave-canonical-source`; no hard-coding). ✓

---

## §6 PHYSICAL-FRAMING assumptions (the interpretation layer)

### A6.1 — charge = Cosserat-ω handedness (the "2") ❓
- **What:** session framing — charge = the (2,3) handedness = the microrotation (Cosserat-ω) handedness. Arm A: charge **not** in the V-phasor (reads noise); Cosserat-ω is the candidate carrier but `ω≡0`.
- **Status:** ❓ open — Arm B tests whether seeding ω carries the charge; A1.1 is the engine-side of the same question.

### A6.2 — B(microrotation) = inductive = rest mass; Beltrami collimation = force-free = lossless ✓
- **What:** `dual-reactance-storage-taxonomy:72,196` (microrot-B → inductive flywheel → rest mass); `electron-unknot.md:9` (Beltrami `∇×A=kA`, force-free → confinement).
- **Status:** ✓ corpus-grounded.

### A6.3 — (2,3) = "2"/Cosserat-ω + "3"/V-sector ✓
- **Affects:** Arm A hosts the "3" (geometry) not the "2" (carrier); Arm B seeds the "2".
- **Status:** ✓ session-consistent.

### A6.4 — what the genesis (III) does and does NOT show ✓
- **Hosted:** the *geometry* — `ℓ_node`-sized drops, the two-drop e⁺e⁻ spatial split (real, amplitude-driven pinch-off).
- **NOT hosted:** the *carrier* — Cosserat-ω, the (2,3), sub-V_yield, charge. All downstream of A1.1.
- **Status:** ✓ honest scope (geometry ≠ electron).

---

## §7 Open follow-ups (ranked)

1. **❓ A1.1 / A6.1 — the V→ω coupling (Grant).** Should the photon's B torque the microrotation (odd V→ω term, engine gap) or is charge a separate ω-seed? Gates whether "two photons → charged pair" is hostable at all. *The decision of the session.*
2. **🔍 A2.3 — Arm B verdict (running).** Does a *seeded* ω-flywheel relax into the (2,3)? Resolves the carrier half independent of A1.1.
3. **⚠ A2.2 / A4.1 — sub-yield relaxation (cheap).** Longer-window / memristive re-run of the over-yield drops — do they relax sub-yield? Carrier result unaffected either way.
4. **🔍 A3.1 — charge-extractor.** Build a Cosserat-ω-sector charge read (the V-phasor sign is unreliable on pure-V).

**Net (pre-§8):** the session's simulations are sound *within* their assumptions; the load-bearing one (A1.1, even-in-ω V↔ω coupling) is **not a bug, but a modeling choice** that decides whether light can birth charge — and it is the open physics question, not a numerical artifact.

---

## §8 — HEADLINE CORRECTION: the seeded photon (V) ≠ the canonical photon (ω≠0)

*(Added 2026-06-06 after BOTH genesis arms returned (III). Cross-referencing the canonical photon hub resolves why — and reframes A1.1.)*

**The canonical photon is the ω-WAVE, not a V-wave.** `photon-identification.md:11,24` verbatim: the photon is *"a knotted transverse Cosserat shear wave with u=0 and ω≠0"* — pure microrotation, sub-saturation, `Z=Z_0` matched. And `:11`: ***"the electron is a self-trapped photon,"*** formed by **Axiom-4 saturation TIR confinement** (`V→V_yield ⇒ C_eff→∞, Z→0, Γ=−1` cavity, `:25`), **NOT** by force-free relaxation.

**Both arms seeded the wrong object / mechanism:**
- **Arm A** seeded a **V-wave** (`vacuum_engine.py:269`) → `ω≡0` (A1.2). *Wrong sector* — the photon is ω. Hosted the geometry (ℓ_node pair), not the carrier.
- **Arm B** seeded the **ω** (right sector) but as a localized **flywheel** under **force-free relaxation** → (III), it de-collimates. *Wrong geometry (flywheel vs wave) + wrong mechanism (relaxation vs saturation-confinement).*

**A1.1 reframed.** The open question may not be "should there be a V→ω coupling" — it may be that **the photon already IS ω**: seed the transverse Cosserat-ω shear **wave**, drive across `V_yield`, and saturation self-traps it into the standing (2,3). The two (III)s rule out the two wrong paths; the canonical genesis (ω-shear wave + saturation) is **untested and indicated**.

**❓ Architecture question (Grant — supersedes §7 #1):** is the engine's `V_inc/V_ref` injection a *wrong-sector* photon (canonical = Cosserat-ω `T₂` shear), or is the TLM-V the correct representation of the transverse mode with the Cosserat-ω a separate field the V-side should drive? `photon-identification.md:24` says photon = ω; the engine seeds V and gets ω≡0 — a **direct contradiction** to resolve before/within the re-run.

**The CMB / cosmic-frame half (extends A6.1):** the charge **sign** is not a free local input — it is inherited from `Ω_freeze` (cosmic rotation at lattice freeze-in: `trampoline-framework:105`, *"Direction of Ω_freeze → right-handed chirality"*). The CMB thermal bath cannot seed the ω-**magnitude** (Cosserat-ω is mass-gapped ≫ T_CMB); the CMB-frame **motion** + the **dark-wake back-reaction** is the magnitude route — and that back-reaction is currently **observed-not-acted** (`DarkWakeObserver` is an `Observer`, `vacuum_engine.py:1457`; absent from the even-in-ω `energy_gradient`). So: **charge sign ← Ω_freeze; charge magnitude ← motion through the CMB frame.**

**A1.6 — gradient-descent ω-settling (CP1 flag):** `cosserat_field_3d.py:1384` `omega -= learning_rate·dE_dw` is energy-minimization — `substrate-native-check` CP1 flags this (the substrate runs wave-propagation, not descent). Even-in-ω, so it doesn't change the ω=0 conclusion, but it's a real assumption on the record.

**Re-aim:** the canonical genesis — seed the transverse Cosserat-ω shear **wave**, drive across `V_yield`, watch it self-trap. *The electron is a self-trapped photon, and we were one sector + one mechanism off.*

---

## §9 — saturation-as-ENERGY vs saturation-as-IMPEDANCE-BOUNDARY (the precise gap)

*(Added 2026-06-06 after the canonical ω-shear-wave genesis (Arm C) returned (III) and isolated the gap exactly.)*

**Arm C (III), single mechanism:** the right photon (ω-shear wave) + the right kernel still does NOT self-trap, because the engine's **saturated Cosserat-ω energy `W_κ·γ·S_κ² = γ(κ² − κ⁴/ω_yield²)` is NON-CONVEX** (`cosserat_field_3d.py:661`). Energy-conserving wave dynamics **disperse** below the inflection or **collapse** (finite-time blow-up) above it — never confine (2 disperse + 2 collapse; verified not-CFL — smaller dt → *worse* blow-up).

**The clean positive:** **charge = helicity IS carried** by the ω-photon (`chirality_flips_helicity=True`; RH→−0.98, LH→+0.98, beats matched baseline) — the carrier works; only the **confinement** is mis-implemented. *We made a charged photon, not a confined electron.*

**The gap (exact):** the engine renders the Axiom-4 kernel as an **energy multiplier** (a non-convex potential → Hamiltonian collapse), but the **corpus mechanism is an impedance boundary**: `photon-identification.md:25`, `V→V_yield ⇒ C_eff→∞ ⇒ Z→0 ⇒ Γ=−1` — a **reflective TIR wall**, not an energy well. **The electron is the ω-photon bouncing off its own saturation-induced `Γ=−1` walls into a standing wave — a self-made TIR cavity** (the same `Γ=−1` wall measured all session: the open/short, `|Γ|=1`). *Energy-that-collapses vs wall-that-reflects.*

**Architecture (the §8 question, answered):** coupled `VacuumEngine3D` modulates saturation **V-only** (Cosserat `use_saturation=False`, `k4_cosserat_coupling.py:297`; zero ω-coupling force `:427-428`) → a pure-ω seed leaves the V-sector dark, no self-trap. Standalone saturated is non-convex-in-ω → collapse. **Neither confines the ω-photon via wave dynamics.** Per A44: **engine-mechanism gap, NOT a missing axiom.**

**Resolution (scoped separately):** implement the saturation TIR as a **moving `Γ=−1` impedance boundary** (the wave reflects off its own `Z→0` wall), not an energy minimum → `research/2026-06-06_saturation-tir-moving-boundary-prereg.md`.

**Net (post-§9):** the four genesis attempts (A V-wave · B ω-flywheel · C ω-shear-wave · architecture probe) **precisely localize the genesis gap to one engine-mechanism choice — saturation-as-energy vs saturation-as-`Γ=−1`-boundary — and confirm the charge carrier (helicity = chirality) works.** This is not a falsification of the physics; it is a fixable, localized mechanism gap.
