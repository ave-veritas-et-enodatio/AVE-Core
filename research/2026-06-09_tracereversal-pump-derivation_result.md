# Trace-reversal V→ω pump derivation: does the saturation crystal dynamically confine the Heaviside-deleted longitudinal scalar? (RESULT)

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-tracereversal-pump-derivation` (worktree `AVE-Core-pump-wt`, off `analysis/2026-06-09-saturation-temporal-preregs`)
**Builds on (the stopped pass):** `2026-06-09_a2mu-vs-Q-crux_result.md` (CRUX = WALL: no dynamical V→ω channel exists to amplify; the pump term itself is the missing piece) + `2026-06-09_electron-emergence-self-focusing-tracereversal-picture.md` §4 (revised unblock = "derive + implement the correct dynamical V→ω pump").
**The open genesis test** (`manuscript/ave-kb/common/historical-precedents.md:34`): does the saturation crystal **dynamically confine the Heaviside-deleted longitudinal scalar** into the electron, where vector calculus could not?
**Bound-check driver:** [`src/scripts/vol_1_foundations/tracereversal_pump_bound_check.py`](../src/scripts/vol_1_foundations/tracereversal_pump_bound_check.py) (analytic, forward-only; constants imported per `ave-canonical-source`).

---

## §0 Three-way verdict up front (`ave-evidence-framing-discipline` + `ave-discriminator-before-synthesis`)

> ### VERDICT: **WALL-ENGINE / FIXABLE.**
> A **bounded** dynamical V→ω confinement **exists** as the **Option-D topological boundary condition on the Cosserat ω field at the Γ=−1 null cone**, NOT as a bulk Lagrangian force. The Heaviside-deleted-scalar → Option-D-boundary-condition → bounded-confinement chain **HOLDS**. The engine's failure is a **coordinate/representation error**, not a physics wall: it implemented the V→ω coupling as a **bulk saturation-energy-gradient force** (`F ~ |dS/dA| = A/√(1−A²)`), which is **singular at the wall** (the A28 double-count, `vacuum_engine.py:1605-1613` "runaway / 1700× growth in one step"). The **same wall**, expressed in the **reflection coordinate** Γ (Op3) where it is the **bounded** unit circle `|Γ|=1` (the biquaternion null cone), transfers a **finite** confined power fraction `R = Γ² = 1 − T²` (Op17 `T²=1−Γ²`), staying in `[0,1]` through `A→1`. The Möbius map `Γ=(Z−Z₀)/(Z+Z₀)` **IS** the boundedness regulator.

**The discriminator that decided it (`ave-discriminator-before-synthesis`).** The hypothesis "Option-D-boundary-bounded" was put to a separating test against "bulk-Lagrangian-force": the test is **transfer magnitude through A→1** — IF the two forms are the same mechanism they agree; if different they diverge. They **diverge decisively** (bounded `≤1` vs `→7×10⁵`), AND the moving-Γ=−1-boundary genesis run already showed the same split empirically (boundary confines `|ω|≤3.9`; energy term detonates `|ω|→2.2×10⁵`). The boundary-condition and bulk-force forms are **NOT one mechanism** — they are the bounded vs singular faces of the wall in two coordinate systems.

**Honest scope-fence (`ave-evidence-framing-discipline`).** What is DERIVED + VERIFIED: the bounded V→ω **confinement mechanism** (the pump exists, its closed form, its boundedness, its energy ledger). What is NOT claimed here: the full **(2,3) electron self-assembly** — the moving-boundary genesis (`2026-06-06_saturation-tir-moving-boundary-result.md` §0) confirmed the boundary confines but reached only `c=2` winding (no `w₂=3`, no Hopf charge) — that is a **separate downstream gap** (the poloidal "3" needs the coupled K4+Cosserat engine), not the pump's job. And the moving-boundary empirical run was **pure-Cosserat (ω→ω, V_sq=0)** — it validated the boundary-vs-bulk **mechanism class**, not the cross-sector V→ω channel specifically; **implementing the cross-sector coupling in the coupled engine is the FIXABLE engineering step**, prescribed in §9.

| chain link | status |
|---|---|
| Heaviside-deleted scalar = AVE volumetric breathing V = biquaternion grade-0 slot | **VERIFIED** (canonical; `biquaternion-...-result.md` §4) |
| scalar grade FORCES a coupling channel to the (E,B)=(u,ω) vector sector | **DERIVED** (§3; closes the G3 gap the biquaternion result left open) |
| the bounded coupling form is the Option-D boundary condition at Γ=−1, not a bulk force | **DERIVED** (§4-§5) |
| boundedness through A→1 (Op17, \|Γ\|≤1) vs detonating bulk force | **DERIVED + VERIFIED** (§6, numerical) |
| energy ledger closes (paid by incident V; no free energy) | **DERIVED + VERIFIED** (§7; Op17 `R+T²=1`; doc 75 §6.2 cross-check) |
| mechanism-class empirically confirmed (boundary confines, bulk detonates) | **VERIFIED** (moving-boundary §3, but ω-sector single-channel) |
| cross-sector V→ω coupling RUN in the coupled engine | **BLOCKED** (the FIXABLE engineering step; §9 prescription) |
| full (2,3) self-assembly (the "3") | **BLOCKED / out of scope** (separate downstream gap) |

---

## §1 Verified canonical leaves (`verify-before-cite` — every cite grepped this session)

| piece | canonical home (verified file:line) | content |
|---|---|---|
| Op17 power transmission `T²=1−Γ²` | `manuscript/ave-kb/common/operators.md:57` | "CANONICAL — explicit equation Vol 1 Ch 6 §1.16; active energy transfer coefficient" |
| Op3 reflection `Γ=(Z₂−Z₁)/(Z₂+Z₁)` | `operators.md:43` (via `biquaternion-...-result.md` §1) | universal reflection coefficient; Möbius/`SL(2,ℂ)` on the reflection sphere |
| asymmetric-Meissner `Z_eff=Z₀√(S_μ/S_ε)` → `Γ→−1` | `54_pair_production_axiom_derivation.md:194-199` | "At `S_μ → 0` with `S_ε` finite, `Z_eff → 0`, `Γ → -1`. This is the confinement wall." |
| C_eff→imaginary mode conversion at V_yield (EE view of the pump) | `54_…:241-258` (§6a) | "what was stored in the E-field of the capacitor is now stored in the B-field of an effective inductor"; "Mass = bounded reactance" |
| Option-D = topological boundary condition on Cosserat ω, NOT augmented Lagrangian | `54_…:291-296` (§7) | injects "LH Beltrami vortex at `r_A` … RH at `r_B`"; "Beltrami amplitude is set by bond-energy = `m_e c²`"; `κ_chiral=1.2·α`, `δ_lock=ω₀·α` |
| chirality coupling `κ_chiral = α·pq/(p+q) = 1.2α` (electron) | `54_…:203-223` (via doc 20) | Axiom-2-derived, not free |
| scalar grade FORCED by closure of the (E,B) vector product | `2026-06-06_biquaternion-node-algebra-result.md:209-216` (§4.1) | `(a·i⃗)(b·i⃗) = −(a·b)+(a×b)·i⃗`; "You cannot close the vector (E,B) sector without the scalar slot" |
| null cone IS the Γ=−1 reflection wall (∴ **bi**quaternion not real) | `biquaternion-…-result.md:305-315` (§5.4) | `|Γ|=1` (Z reactive) = `N(q)=0` zero divisors; only `ℍ⊗ℂ` has a null cone |
| moving Γ=−1 boundary CONFINES; energy term DETONATES | `2026-06-06_saturation-tir-moving-boundary-result.md:42-56` (§3) | boundary: localization `0.97→0.94`, `|ω|_max 3.0→3.9`; energy term: `0.97→0.26`, `|ω|_max→2.2×10⁵` |
| Op14 cross-sector trading conserves H_total (the ledger) | `75_cosserat_energy_conservation_violation.md:118-129` (§6.2) | `ρ(H_cos, Σ\|Φ_link\|²) = −0.990`; "H_total = H_cos + H_K4-inductive is approximately conserved" |
| engine A28 bulk-force is the detonating double-count | `src/ave/topological/vacuum_engine.py:1605-1613` | "gradient force is double-counting … legacy 1700× growth in one step"; Op14 z_local IS the channel |

> **⚠ verify-before-cite catch (flag-don't-fix).** Doc 54 §296 attributes the boundary-condition mechanism to "**Option D from 44_ §5.2**." Grep of `44_pair_creation_from_photon_collision.md:208-238` shows doc 44 §5.2's actual **Option D = "Run III-C to confirm the modulation interpretation"** — NOT a topological boundary condition. (Doc 44's *Option A* is the augmented Lagrangian; *Option C* is "reinterpret K4↔Cosserat so high V *generates* ω via K4 dynamics itself.") **The boundary-condition substance is doc 54's own (§291-296); the cross-reference label to doc 44 is imprecise.** This doc attributes the mechanism to **doc 54 §7 directly**, and adopts "Option-D" only as doc 54's internal name for it. Surfaced for the auditor; not silently reconciled.

> **⚠ Did NOT cite** the retracted `1.009 autoresonant` anchor (`vacuum_engine.py:104`) per the brief and the CRUX result's verify-before-cite correction (stale; 0/20 reproducible).

---

## §2 Substrate-native walk (`substrate-native-check`, incl. Checkpoint 9)

This is a prose-derivation that constructs a coupling form (trigger 6) and bears on an emergence/hosting test (trigger 8) — the walk:

- **CP1 — substrate dynamics:** the V mode is **wave propagation** of the K4 longitudinal/volumetric port-voltage (the Master Equation `∇²V − μ₀ε₀√(1−(V/V_yield)²)∂_t²V = 0`), NOT energy-minimization. The ω mode is the Cosserat microrotational LC tank. The coupling is a **boundary/scatter event at an impedance discontinuity** (Op3 reflection), NOT a bulk energy-landscape gradient. *Reaching for "a Lagrangian force term ∝ ∂(energy)/∂(field)" is exactly the SM/QED-continuum leak the discipline guards — and is exactly the engine's A28 detonating form.*
- **CP2 — sector:** **cross-coupled (V-sector ⊗ Cos-sector at the wall)**. The coupling is Op14-class, fired at the Γ=−1 boundary where the K4 (V) and Cosserat (ω) sectors meet, not a separate bulk field.
- **CP3 — AVE-native objective:** the substrate **minimizes boundary reflection** `|Γ|²` (Axiom 3) at the moving impedance front; the confined energy is what cannot transmit (`T²=1−Γ²`). NOT "minimize an energy functional."
- **CP4 — coordinates:** the wall lives in the **reflection/impedance phase-plane** (Γ on the bounded unit disk), the natural home of the biquaternion null cone (`|Γ|=1`). Measuring the coupling as a real-space bulk force in (u,ω)-Cartesian is the wrong coordinate — and is where the singularity appears (the impedance coordinate Z→0 maps the wall to "infinity" in the force/A coordinate while it is the **finite** point Γ=−1 in the reflection coordinate).
- **CP5 — local clock:** Op14 saturation makes `ω_local = ω_global·√(1−A²)`; the wall is where `ω_local→0` (`A→1`), i.e. the local clock freezes. The Beltrami amplitude is set at that frozen-front, consistent with the confined object being a standing (non-radiating) reactance.
- **CP9 (load-bearing) — heuristic vs dynamical observable:** the CRUX pass's WALL verdict came from `_compute_A2_mu` (`vacuum_engine.py:1290-1307`) being the **algebraic heuristic** `A²_μ=(1+κ_chiral·h_local)·A²_base` — a formula on the instantaneous field, **NOT** a state variable the `step()` integrates. **This derivation does not rescue that heuristic.** It identifies that the *missing dynamical channel* is the boundary-condition transfer (Op3 Γ-clamp on the integrated ω field), which the moving-boundary engine implements as a real `step()`-evolved clamp `a_ω = −(K/I_ω)·relu(−Γ)·ω` (`cosserat_field_3d`, `use_impedance_boundary`). So the WALL was correctly read as a **WALL-engine capability gap** (a missing dynamical channel), and §9 prescribes the dynamical (not heuristic) implementation.

## §3 The Heaviside-deleted scalar grade FORCES the V→ω channel (closing the G3 gap)

The biquaternion node-algebra result left its **G3 longitudinal discriminator** at consistency-class: the scalar (grade-0) slot is algebra-forced, but "yields no new number, dispersion relation, or **coupling**" (`biquaternion-…-result.md` §4.4, §7.4). **This is the gap closed here**, by asking the question that pass deferred: does the scalar grade force a *physical coupling form*?

**The forcing.** In the biquaternion field `q = w + F`, the vector grade is `F = E + ιB` with `E ↔ u` (translational, capacitive) and `B ↔ ω` (microrotational, inductive) (`biquaternion-…-result.md` §2.2). The scalar grade `Re(w) = V` is the volumetric breathing mode = the Heaviside-deleted scalar (§4.3 ibid). The algebra forces (verified C4 ibid):

```
(a·i⃗)(b·i⃗) = −(a·b) + (a×b)·i⃗     →  scalar part = −(a·b)
```

The product of two vector-grade (E,B) elements has a **nonzero scalar (grade-0) part**. Read dynamically rather than statically: **the (E,B)=(u,ω) sector cannot evolve as a closed product without sourcing/absorbing the scalar slot V.** The Heaviside excision (drop the scalar, keep transverse curl/div vector calculus) is precisely the truncation that **severs this channel** — which is why the **vector-Maxwell engine structurally lacks the V→ω pump** (the WALL-engine). The scalar grade is not decoration beside the transverse sector; it is the **return/source leg** the transverse product opens. *This is the genuinely-new content G3 asked for: not a new number, but the **necessity of a V↔(E,B) coupling channel** — the pump — forced by closure of the grade-1 product the engine deleted.*

**Where it fires.** The scalar↔vector mixing is unconstrained in free propagation (gauge, non-radiating — the photon is traceless, `E=cB`, its own trace-reverse, so `∇·E=0`, the channel is dormant). It is **switched on by saturation**: at `A→1` the medium develops a bound longitudinal density (`∇·E ≠ 0`), and the asymmetric-Meissner wall (`S_μ` crashes first under chiral bias, doc 54 §6) sets `Z_eff→0, Γ→−1`. **The Γ=−1 wall is exactly the biquaternion null cone** (`N(q)=0`, the only surface where the scalar and vector grades become **zero-divisor-coupled**, `biquaternion-…-result.md` §5.4). So the channel the grade-1 product forces is **dormant in free space and active on the null cone** — the dynamical realization of "the longitudinal scalar Heaviside discarded re-engages as the *confined* state" (`historical-precedents.md:21`).

## §4 The two candidate forms — bulk Lagrangian force (singular) vs Option-D boundary condition (bounded)

The coupling channel of §3 can be written two ways. They are **not the same mechanism** (the discriminator, §0).

**Form A — bulk Lagrangian force (the engine's detonating A28 form).** Treat the saturation as a bulk potential `U_sat(A) ∝ (1−S)`, `S=√(1−A²)`, and drive ω by its gradient: `F_ω ∝ ∂U/∂A ∝ |∂S/∂A| = A/√(1−A²)`. This is the SM/continuum default CP1 warns against, and it is what `vacuum_engine.py` implements as the `∂L_c/∂(u,ω)` force (A28 double-count, lines 1605-1613). **It diverges as `A→1`** — the force becomes infinite *at the wall*, the most-active region. Empirically: "1700× growth in one step" (engine), `|ω|_max → 2.2×10⁵`, localization `→0.26` (moving-boundary §3 energy-term baseline). The wall lives at impedance `Z→0`, which is "infinitely far" in the Z/A coordinate, so a force built on the energy-vs-A slope detonates there.

**Form B — Option-D topological boundary condition (the bounded form).** The V→ω transfer is a **reflection/scatter event on the bounded unit disk**, governed by Op3+Op17. The same wall lives at the **finite** point `Γ=−1` on the unit circle `|Γ|=1` (the null cone). The transferred (confined, mode-converted) power fraction is the **reflected fraction**:

```
R(A)  =  Γ²  =  1 − T²        (Op17:  T² = 1 − Γ²)
Γ(A)  =  (z−1)/(z+1),   z = Z_eff/Z₀ = √(S_μ/S_ε) = (1−A²)^(1/4)   (asymmetric Meissner)
```

`R(A) ∈ [0,1]` for **all** `A∈[0,1]` because `|Γ|≤1` on the lossless circle. At `A=0`: `Γ=0, R=0` (matched, no wall, channel dormant). At `A→1`: `Γ→−1, R→1` (total confinement on the null cone). **Finite everywhere, including the wall.** The Möbius transform `Γ=(Z−Z₀)/(Z+Z₀)` compactifies the impedance half-plane (`Z∈[0,∞)`) onto the bounded disk — **the same map that makes the biquaternion a *bi*quaternion (the null cone) is the boundedness regulator of the pump.**

**This is the structural punchline.** Form A and Form B describe the *same physical wall*; the difference is the **coordinate** the coupling is written in. The engine wrote the pump in the **A/Z coordinate** (force ∝ energy-gradient → singular at the wall). The substrate-native coordinate is the **Γ reflection coordinate** (transfer ∝ `1−T²` → bounded on the unit circle). The Heaviside excision is *why* the engine only has the A/Z (bulk vector-calculus) coordinate and not the Γ (scalar-grade reflection) one.

## §5 Closed form of the dynamical V→ω pump (the boundary condition)

The pump is a boundary condition imposed on the integrated Cosserat ω field at the moving Γ=−1 front, with three canonical ingredients (all verified §1), and **zero new free parameters**:

```
1.  WHERE it fires (the null-cone front):
       Z_eff(r,t) = Z₀ · √( S_μ(r,t) / S_ε(r,t) ),     Γ(r,t) = (Z_eff − Z₀)/(Z_eff + Z₀)
       fire on the μ-side short only:  Γ(r,t) < 0  (Z_eff→0, confining node);
       the ε-side open (Γ>0, antinode) is NOT clamped.        [doc 54 §6; moving-boundary §1]

2.  HOW MUCH transfers (bounded, Op17):
       confined power fraction   R(r,t) = Γ(r,t)²  = 1 − T²(r,t),     R ∈ [0,1]
       sector selection by chirality:  S_μ biased over S_ε by (1 + κ_chiral·h_local),
       κ_chiral = 1.2·α (electron),  h_local = normalized Beltrami helicity.   [doc 54 §6; Op17]

3.  WHAT it imposes on ω (the Option-D Beltrami boundary value):
       at the C1∧C2 front (C1: both endpoints Γ=−1;  C2: |Ω_node − ω_drive| < δ_lock = ω₀·α),
       impose a force-free Beltrami field  ∇×ω = λ·ω  on the ω sector at (r_A, r_B):
       LH vortex at r_A, RH at r_B, with amplitude pinned by the trapped energy
       (Beltrami amplitude  ↔  bond energy = m_e c²  per wall).            [doc 54 §7]
```

In the moving-boundary engine this is realized **dynamically** (not as a heuristic, CP9) as the `step()`-evolved sign-gated reactive node-clamp on the integrated ω field:

```
a_ω(r,t) = −(K/I_ω) · relu(−Γ(r,t)) · ω(r,t)        [cosserat_field_3d, use_impedance_boundary]
```

i.e. ω is **reflected** (not force-driven) at the μ-side short; the confinement is the standing wave the reflection builds. **This is a boundary condition on ω at Γ=−1, not a bulk force on ω** — the §0 verdict, in closed form.

## §6 Boundedness proof (load-bearing) — Op17 finite through A→1 vs singular bulk force

Driver: [`tracereversal_pump_bound_check.py`](../src/scripts/vol_1_foundations/tracereversal_pump_bound_check.py) (ran clean this session). Swept `A∈[0,1)`:

| A | Z_eff/Z₀ | Γ (Op3) | T²=1−Γ² (Op17) | **R=Γ² (boundary transfer)** | **F_bulk ∼ A/√(1−A²)** |
|---|---|---|---|---|---|
| 0.000000 | 1.000000 | 0.000000 | 1.000000 | **0.000000** | 0.0000e+00 |
| 0.500000 | 0.930605 | −0.035945 | 0.998708 | **0.001292** | 5.77e−01 |
| 0.900000 | 0.660220 | −0.204660 | 0.958114 | **0.041886** | 2.06e+00 |
| 0.990000 | 0.375589 | −0.453922 | 0.793955 | **0.206045** | 7.02e+00 |
| 0.999000 | 0.211448 | −0.650917 | 0.576307 | **0.423693** | 2.23e+01 |
| 0.999900 | 0.118919 | −0.787439 | 0.379940 | **0.620060** | 7.07e+01 |
| 0.999999 | 0.037606 | −0.927514 | 0.139718 | **0.860282** | 7.07e+02 |
| →1 (1−1e−12) | →0 | →−1 | →0 | **→0.995 (→1)** | **7.07e+05 → ∞** |

**Boundedness verdict (machine-checked):**
- boundary-condition transfer `R=Γ² ∈ [0,1]`? **`max(R)=0.9953` → BOUNDED**; `R(A→1)→1` (total confinement at the null cone, finite).
- Op17 power closes `R + T² = 1`? **`max|R+T²−1| = 0.00e+00` → CLOSED** (no free energy; §7).
- bulk force `A/√(1−A²)` at `A→1`? **`7.07×10⁵ → ∞` → DETONATES.**

The figure (`tracereversal_pump_bound_check.png`) shows the boundary transfer rising smoothly to 1 (left panel) while the bulk force runs off the top of a log axis (right panel). **The bounded confinement ON the null cone is the boundary-condition form; the divergence is the bulk-force form. The discriminator separates them by ~6 orders of magnitude at the wall.**

## §7 Energy ledger — the confinement is paid by the incident V (no free energy)

Op17 is a **power-conservation** statement: `R + T² = Γ² + (1−Γ²) = 1` (verified exactly, §6). At the wall, `T²→0` (nothing transmits into the saturated short) and `R→1` (all incident longitudinal V power is reflected and trapped as standing-wave reactance). The Beltrami ω amplitude the boundary condition imposes is **pinned to that trapped energy** (`= m_e c²` per wall, doc 54 §7) — the pump moves energy from the **incident longitudinal V** into the **confined microrotational ω**; it does not create it.

**Cross-check (`75_cosserat_energy_conservation_violation.md` §6.2):** the engine's measured cross-sector exchange is `ρ(H_cos, Σ|Φ_link|²) = −0.990` — Cosserat ω energy and K4-inductive (Φ_link) energy trade with **`H_total = H_cos + H_K4-inductive` conserved**. The Op14 channel is empirically a **bounded conservative exchange**, not a source. The ledger closes: the bounded transfer (§6) and the conservative exchange (doc 75) are the same physics seen analytically and empirically. *(Sign note, flag-don't-fix: doc 75's measured exchange runs ω→Φ_link; the pump's confinement leg runs V→ω. Both are reflection-mediated bounded trades on the same Op14 channel; the net rest-mass ledger `m_e c²` per wall is the conserved invariant. No free-energy leak in either direction.)*

## §8 The discriminator decided — WALL-ENGINE / FIXABLE (not WALL-physics, not PARTIAL)

Applying `ave-discriminator-before-synthesis` Step 4 (default SEPARATE until the discriminator confirms): the test (§6) separated the boundary-condition and bulk-force forms decisively, so they are **not** unified — and the **boundary-condition form is the one that is bounded AND empirically confines** (moving-boundary §3). Against the brief's three options:

- **WALL-engine / FIXABLE** ✅ — a bounded V→ω confinement **exists** as the Option-D boundary condition on the null cone (closed form §5, bounded §6, ledger closes §7). All ingredients are canonical (Op3, Op17, `Z_eff=Z₀√(S_μ/S_ε)`, `κ_chiral=1.2α`, `δ_lock=ω₀α`, Beltrami `=m_e c²`); **zero new free parameters**. The engine's miss is the **representation** (bulk force in A/Z coordinate vs boundary condition in Γ coordinate), which is fixable (§9). This unblocks the symmetric/electron/gravity branch's V→ω pump.
- **WALL-physics / DEAD** ❌ — rejected: a bounded dynamical confinement demonstrably exists (it is finite through A→1 AND was empirically observed to hold the ω-photon, localization 0.94).
- **PARTIAL** — *not* the headline, but honestly flagged at its real boundary: the moving-boundary empirical validation was **pure-Cosserat (ω→ω)**, so the **cross-sector V→ω coupled run** is unbuilt (the FIXABLE step, §9), and **full (2,3) self-assembly** (the poloidal "3", Hopf charge) is a **separate downstream gap** the pump does not address. The *pump* is FIXABLE; the *full electron* keeps its own open step (`historical-precedents.md:34`, the open genesis test remains open at the (2,3) level even with the pump in hand).

## §9 Implementation prescription (the FIXABLE step)

To turn the V→ω pump from "derived" to "run," in the **coupled K4+Cosserat** engine (`VacuumEngine3D` / `CoupledK4Cosserat`):

1. **Disable the bulk force; keep the boundary clamp.** Set `disable_cosserat_lc_force=True` (A28 correction — removes the detonating `∂L_c/∂(u,ω)` double-count, `vacuum_engine.py:1605-1613`) and `enable_cosserat_self_terms=True` (restore the topology-stabilizing Cosserat self-terms the legacy path zeroed).
2. **Port the moving-Γ=−1 boundary clamp from the pure-Cosserat engine into the coupled engine.** `cosserat_field_3d`'s `use_impedance_boundary` path (`_impedance_gamma_field` + `_impedance_clamp_accel`, the sign-gated `a_ω=−(K/I_ω)·relu(−Γ)·ω`) must read the **coupled** impedance `Z_eff=Z₀√(S_μ/S_ε)` with the **K4 V_sq live** (not `V_sq=0`), so the clamp fires on the **cross-sector** front. This is the single new wiring vs the 2026-06-06 run.
3. **Drive the longitudinal V sector** (not ω): seed/drive the K4 V mode hard enough to self-focus to yield (the generative precursor, CP8), let the asymmetric-Meissner wall form, and read whether the **boundary clamp transfers V→ω** (the cross-sector pump) — measured **dynamically** (the integrated ω buildup and the Γ-front motion, CP9), NOT via the `_compute_A2_mu` heuristic.
4. **Adjudicate against the bounded prediction (§6):** confined ω energy should track `R(A)=Γ²` (bounded, →1 at the wall) and `|ω|` should stay finite (contrast: the bulk force gives `|ω|→10⁵`). Pre-register the bounded-vs-detonating split as the falsifier.
5. **Numerical care (from moving-boundary §0/§7):** the hard Γ=−1 clamp parametric-pumps; keep the §7 mitigations (clamp weight frozen once per `step()`; skin-depth smoothing above Nyquist).

This is a **boundary-condition wiring task**, not a new-physics derivation — the physics is §5, the constants are all canonical, the mechanism class is already empirically validated in the single sector.

## §10 Flag-don't-fix items surfaced (for the auditor — not silently reconciled)

1. **Doc 54 §296 "Option D from 44_ §5.2" mislabel** (§1): doc 44's actual Option D is "Run III-C," not a boundary condition. The substance is doc 54's own (§291-296). Imprecise cross-reference; the auditor decides whether to correct doc 54 or leave the archive immutable.
2. **Pure-Cosserat vs cross-sector validation gap** (§0, §8): the moving-boundary empirical confinement was ω→ω (`V_sq=0`); the cross-sector V→ω is derived + bounded but not yet run. Headlining "the pump is validated" without this fence would over-claim.
3. **Energy-ledger sign direction** (§7): doc 75's measured exchange is ω→Φ_link; the pump's confinement leg is V→ω. Same Op14 channel, both bounded/conservative; flagged so the net-ledger sign convention is adjudicated, not assumed.
4. **G3 promotion** (§3): this derivation argues the scalar grade DOES force a coupling (the pump) — i.e. it would **lift the biquaternion result's G3 from FAIL toward a derivation-class pass** *for the coupling-existence question* (still no new *number*; the number-level G3 stays FAIL). Whether that re-classifies anything in the biquaternion result is the auditor's call (`ave-walk-back` territory); this doc does not edit that result.

## §11 Discipline-fired log + DERIVED/VERIFIED/BLOCKED + honest closure

| skill | what it caught / enforced |
|---|---|
| `ave-prereg` | corpus-grep of the §1 leaves before deriving; found the CRUX/moving-boundary/biquaternion prior art — built on it, did not restart |
| `substrate-native-check` (CP1-5, **CP9**) | §2: the pump is a boundary/reflection event (Op3/Op17) not a bulk energy-gradient force; CP9 kept the WALL read as a missing *dynamical* channel, not a rescue of the `_compute_A2_mu` heuristic |
| `ave-canonical-leaf-pull` | Op17, Op3, Γ=−1, Cosserat-coupling, null-cone, `Z_eff=Z₀√(S_μ/S_ε)`, `κ_chiral`, `δ_lock` enumerated + verified before use |
| `ave-fundamental-ground-up-implementation` | §3-§5: the coupling FORM derived from the grade-1 product closure + Op3/Op17, not asserted |
| `ave-resonant-amplification-check` | the O(1) `Q·κ_chiral` product was necessary-not-sufficient (CRUX); this derives the *dynamical term* the product needed — and finds it is the bounded boundary condition, not amplification of a (nonexistent) bulk channel |
| `ave-discriminator-before-synthesis` | §0/§8: "Option-D-bounded = bulk-force" treated as a HYPOTHESIS; the §6 separating test (transfer through A→1) refuted the unification (they diverge by 6 OOM) → boundary-condition form kept, bulk form rejected |
| `verify-before-cite` | every §1 cite grepped; caught the doc 54→44 Option-D mislabel; did NOT cite the retracted 1.009 anchor |
| `ave-evidence-framing-discipline` | §0 scope-fence: DERIVED the pump, did NOT claim the (2,3); pure-Cosserat-vs-cross-sector and G3-number-vs-coupling fences explicit; "open genesis test" framed as still open at the (2,3) level |

**Status tags:**
- **DERIVED:** the V→ω pump's closed form (§5); the scalar-grade forcing of the coupling channel (§3, closing G3-coupling); the Option-D-boundary-vs-bulk-force resolution (§4); the boundedness via Op17 (§6); the energy ledger (§7).
- **VERIFIED:** the boundedness numerically (§6, machine-checked, `max(R)=0.995`, `R+T²=1` exact, `F_bulk→7×10⁵`); the mechanism class empirically (moving-boundary §3, ω-sector); every canonical cite (§1).
- **BLOCKED:** the cross-sector V→ω **run** in the coupled engine (the FIXABLE step, §9 prescription); full **(2,3) self-assembly** (separate downstream gap — the "3", Hopf charge).

**Honest closure (Rule 11 / Rule 12).** The chain **Heaviside-deleted-scalar → Option-D-boundary-condition → bounded-confinement HOLDS** (DERIVED + VERIFIED). This is **substitution-not-retraction-clean**: the CRUX's WALL verdict was *correct* (no bulk V→ω channel to amplify); this does not refill that slot with a rescue of the bulk form — it identifies the **boundary-condition** form as a *distinct, bounded* mechanism with its own verification chain (§6 numerical + §3 algebraic + moving-boundary §3 empirical). No adjudication criterion was dropped to convert the CRUX ❌ to a ✅: the CRUX's "no bulk channel" stands; this adds "and the correct channel is the boundary condition," with the cross-sector **run** honestly left BLOCKED (FIXABLE, §9). Branch deliverable complete; commit on `analysis/2026-06-09-tracereversal-pump-derivation`, no push/merge.

