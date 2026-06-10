# PREREG — Sonic-horizon closure: is the `c²=0` locus a one-way shock-class reflector (FLASH), a reversible spring (LOCK), an apparatus artifact (CLIP), or does the surface never form (NO-HORIZON)? And is the reflector handedness-selective (SELECTIVE / BLIND)?

**Date (frozen):** 2026-06-10
**Branch:** `analysis/2026-06-10-sonic-horizon-closure` (worktree off `analysis/2026-06-10-cavitation-core-probe`; do not push/merge)
**Governing discipline:** `ave-apparatus-floor-attribution` (the new boundary condition introduces knobs — a FLASH that tracks a knob is apparatus, not physics)
**Skills fired at design time:** `ave-apparatus-floor-attribution` (governing), `substrate-native-check` (CP1/2/4/5/6/7/9/10 walked below), `ave-prereg` (Step 3.5 expected-values + corpus-grep below), `ave-canonical-source`, `ave-driver-script-honesty`, `ave-regime-phase-state-check`, `ave-conserved-vs-pumped`, `verify-before-cite`, `ave-representation-capability-check` (the reflector acts on BULK waves — the probe waves must be bulk-channel, §2.2).

---

## 0. The named hypothesis (Grant 2026-06-10, recorded verbatim)

> "this feels like orbital escape velocity or bow shock related, its saturation and incidence angle? its a perfect reflector in a certain chiral direction?"

**Formalized (this prereg's named hypothesis — NEW, with its own verification chain):** the `c²(ρ̄)=0` locus is a **SONIC HORIZON** with three claimed properties:

- **(a) Perfect reflector at all angles, automatically.** As the local bulk sound speed `c_in → 0` at the locus, the bulk acoustic impedance `Z_bulk = ρ·c_bulk → 0`; the universal reflection coefficient `Γ = (Z_in − Z_0)/(Z_in + Z_0) → −1` (a pressure-release / "short" boundary). Equivalently the total-internal-reflection critical angle for an internal ray trying to escape, `sinθ_c = c_in/c_out → 0`, so all internal rays are trapped at any incidence — both follow from `c_in→0`, not from a hand-painted Γ.
- **(b) Crossing physics is SHOCK-CLASS — one-way / entropy-producing.** Converging flow that crosses the `c=0` surface cannot carry its kinetic energy back out (a horizon traps outgoing characteristics, `c_eff − |u| < 0`); the irreversible mechanism the predecessor's floored scheme excluded by construction.
- **(c) The reflector is HANDEDNESS-SELECTIVE — partial-asymmetry version.** Co-handed reflected with a different efficiency (Q) than counter-handed; both signs trappable (the **partial** version). The **strict** version (one handedness perfectly transmitted) is **NOT built in** — it would contradict positron stability (a counter-handed electron-analog must still be trappable). Flag-don't-fix: see §2.2 for the representation-capability caveat on WHICH chirality mechanism this engine can actually test.

## 0.1 Predecessor — Rule 12 (substitution-not-retraction): this is a NEW hypothesis, NOT a refill

The predecessor is the **cavitation-core probe** (branch `analysis/2026-06-10-cavitation-core-probe`, result `research/2026-06-10_cavitation-core-probe_result.md`). Its panel-reviewed standing verdict is **CLIP** (the §0 LOCK was demoted; result §0-bis). The demotion driver (result §0-bis(a)): **the dynamics never integrated `c²<0`** — the momentum RHS ran on the *floored* wave speed `c_eff² = max(c²_raw, +1e-3·c₀²)` (`src/ave/core/cavitation_flow.py:159–163`, default `c2_floor=1e-3`), so FLASH was **excluded by construction, not by evidence**. The result §0-bis(e) explicitly **gates** the FLASH/LOCK question on a **NAMED below-floor closure** with `c2_floor` swept inside the reversibility test, and **forbids refilling the slot** with an unverified hypothesis.

This prereg **opens that named closure** as a NEW hypothesis (Rule 12 / A47 v11b): the **sonic-horizon sharp-interface closure**. It inherits the predecessor's engine + its clip-invariant *reach* result (a circulating core reaches/crosses `ρ̄_cav=−1/φ` at `M*≈0.8`; result §0-bis(b)) and tests the *kind* of event the predecessor could not.

## 0.2 CANDIDATE-CLAIM status of ρ̄_cav (HARD CONSTRAINT — unchanged)

`ρ̄_cav = −1/φ` is a **CANDIDATE-CLAIM**, Propulsion-derived: the `c_eff²→0` root of `c_eff² = c₀²(1 + ρ̄/(1−ρ̄²))` (`AVE-Propulsion/.../04_superluminal_transit.tex:86`, "not a free parameter", Ax4; verified 2026-06-10). The root:
```
1 + ρ̄/(1−ρ̄²) = 0  →  ρ̄² − ρ̄ − 1 = 0  →  ρ̄ = (1−√5)/2 = −1/φ ≈ −0.6180339887
```
(`PHI = (1+√5)/2` canonical, `constants.py:199`; `−1/PHI` reproduces the root.) Zero KB/`constants.py` hits for the *floor* → **NOT Core-canonical**. `ρ̄_cav = −1/φ` remains CANDIDATE-CLAIM throughout this probe; this closure does **not** promote it.

## 0.3 FIREWALL (HARD CONSTRAINT — the pocket is a FOURTH object)

Per the cavitation-distinctness firewall (`_orchestration/double-slit-ee-mapping.md:92`, verified 2026-06-10: "sonoluminescence cavitation = saturated Rayleigh-Plesset inertia, a DIFFERENT mechanism from the Γ=−1 cavity"), the cavitated pocket is a **substrate-bulk-density tensile-failure pocket** — NOT the Rayleigh-Plesset gas bubble, NOT the photon bubble, NOT the shear-sector `Γ=−1` EE cavity. It is the `c_bulk²≤0` tensile-failure region of the volumetric **K** modulus. The reflector mechanism we *borrow* (impedance collapse `Z→0 ⇒ Γ→−1`) is the same algebra as the YM color-confinement mirror (`yang-mills-steps3-5.md:43`, verified 2026-06-10: `Z_knot→0 ⇒ Γ→−1`), but applied to the **bulk acoustic channel** here, not the EM/shear channel there — hypothesis-class analogy, not an identity (§2.2).

---

## 1. Physical picture (substrate-native, before equations)

- **What forms the horizon:** the predecessor showed a self-circulating bulk-density core rarefies (centrifugal pressure deficit) and *crosses* `ρ̄_cav=−1/φ`, where `c_bulk²(ρ̄)→0`. At and below that locus the local bulk sound speed vanishes/goes imaginary. A surface where `c_eff→0` while a finite flow `|u|` persists is a **sonic horizon** (acoustic-black-hole analog): the local Mach number `|u|/c_eff → ∞`, outgoing acoustic characteristics have group velocity `c_eff − |u| < 0` (they cannot escape outward).
- **Why it reflects (a):** for an external bulk wave in the `Z_0`-medium hitting the `Z_in→0` void, `Γ = (Z_in − Z_0)/(Z_in + Z_0) → −1` — perfect reflection with phase inversion, at all angles (the normal-incidence limit is angle-robust because `Z_in→0` dominates). A `c=0` region is the acoustic **pressure-release ("short") boundary**. We implement this via the impedance collapse (the EOS drives `c_bulk²→0`), **not** by painting a Γ on a surface.
- **Why crossing is one-way (b):** a horizon is one-way by construction. Energy converging inward crosses the `c=0` surface but the trapped outgoing characteristics cannot return. The predecessor's `+1e-3·c₀²` floor kept `c²` strictly positive everywhere → only reversible compliance was representable → FLASH excluded by construction. Removing the floor (clamping `c²` at *exactly* 0 below the locus, with the void quiescent at vapor pressure) admits the irreversible branch.
- **Bow-shock / escape-velocity intuition (Grant's framing):** the bulk EOS *steepens* on the compression side (`04_superluminal_transit.tex:89`, the Alcubierre bow-shock) and *softens* to `c=0` on the rarefaction side. The rarefaction `c=0` surface is the rarefaction-side analog of the compression-side shock front: a characteristic-convergence surface. "Escape velocity" = the horizon: once flow is supersonic relative to the vanishing `c_eff`, acoustic information cannot climb back out.
- **The conserved invariant (ave-conserved-vs-pumped):** circulation Γ / vorticity ζ is the conserved topological invariant (barotropic Kelvin, `d|Γ|/dt=0`). It is **ENERGIZED + LOCKED** once by the drive `M_edge`; never pumped. KE↔PE are the pumpable stores that slosh at fixed Γ. The shock dissipation and the radiated acoustic are the only sinks.

## 1.1 substrate-native-check (walked at design time, recorded)

- **CP1 (dynamics):** dynamical time-integration of the compressible bulk-density flow; the horizon/pocket EMERGES from the integration — NOT a minimization, NOT an algebraic root-find.
- **CP2 (sector + carrier capability):** BULK volumetric **K** sector; vector velocity `u` + compressible density `ρ̄` (inherited `CavitationFlow2D`). The scalar `MasterEquationFDTD` is irrotational and *stiffening* (`c²=c₀²/√(1−A²)`); `lbm_3d` is incompressible. Neither can host "circulating + rarefying-to-a-horizon"; the inherited vector-flow branch is the required carrier.
- **CP4 / phase-space-coordinate-check:** `ρ̄_cav` and `c_bulk²(ρ̄)` are claims about the **real-space density variable ρ̄** and the **real-space sound speed**; the matching measurement coordinate is the real-space `ρ̄`/`c²` field. NOT the (2,3) phase-space case. PASS.
- **CP5 (local clock):** the bulk clock `τ_bulk(r) = τ₀/√(c²(ρ̄)/c₀²)` freezes (τ→∞) exactly at the horizon (`c²→0`) — a horizon co-signature; tracked at the core.
- **CP6 (reactance pair):** LC pair = compression PE (C-state, **exact EOS internal energy** `U(ρ̄)`, §2) ↔ kinetic energy (L-state, `½∫ρ|u|²`). BOTH tracked every recorded step, plus `E_diss` (shock, one-way), `E_latent` (cavitation release), Γ.
- **CP7 (sampling):** sponge cells excluded before any extremum/pocket extraction; `ρ̄_core` = interior density minimum; pocket cells counted only in the interior.
- **CP9 (heuristic-vs-dynamical):** LOAD-BEARING. `ρ̄_core`, the pocket, and the horizon are **dynamically integrated** (continuity + momentum); the reflector is the EOS impedance collapse, NOT an algebraic Γ painted on a prescribed circle.
- **CP10 (boundary-not-bulk):** cavitation/horizon rendered as a **stiffness collapse in the EOS wave-speed + a free-surface BC at the `c=0` locus**, NOT as an added confining bulk potential.

## 1.2 FLAG (verify-before-cite, the impedance distinction) — Z_eff (EM, stiffens) vs Z_bulk (collapses)

`04_superluminal_transit.tex:89` defines `Z_eff = Z_0/S(ρ̄)`, `S=√(1−ρ̄²)` — this is the **EM/transverse** impedance and it does **NOT** collapse at the floor: at `ρ̄_cav=−0.618`, `S=√0.618≈0.786`, so `Z_eff≈1.27·Z_0` (finite). The reflector hypothesis therefore is **NOT** about `Z_eff`. It is about the **BULK ACOUSTIC** impedance `Z_bulk = ρ·c_bulk = (1+ρ̄)·c_bulk` (natural units `ρ₀=1`), which **does** collapse: at the floor `c_bulk→0 ⇒ Z_bulk→0`. The YM `Z_knot→0` (`yang-mills-steps3-5.md:43`) is the EM-channel confinement mirror; we cite it as the **candidate-mechanism analogy** for the bulk-channel reflector, flagged as hypothesis-class, NOT an identity. This distinction is load-bearing for §2.2 (the probe waves must be bulk-channel).

## 2. The closure (governing equations + the sharp-interface BC)

Inherited 2-D barotropic inviscid bulk flow (state `ρ̄`, `u=(u,v)`; `ρ=1+ρ̄`):
```
Continuity:  ∂ρ̄/∂t = −∇·[(1+ρ̄) u]
Momentum:    ∂u/∂t  = −(u·∇)u − [c_eff²(ρ̄)/(1+ρ̄)] ∇ρ̄
EOS:         c_raw²(ρ̄) = c₀²(1 + ρ̄/(1−ρ̄²))   (Propulsion 04:86; Ax4; root ρ̄_cav=−1/φ)
```
**THE CLOSURE (replaces the predecessor's positive `c2_floor`):**
1. **`c²` clamped at EXACTLY zero below the locus:** `c_eff² = max(c_raw², 0)`. Below `ρ̄_cav` the medium is **inert** (no restoring force, no anti-restoring runaway). The `c=0` void is automatically a `Z=0` pressure-release reflector AND a sonic horizon.
2. **One-way pocket mask `C` (memory):** a cell enters `C` when `ρ̄ ≤ ρ̄_cav`; it leaves `C` only when `ρ̄ > ρ̄_cav + Δ_heal` (`Δ_heal≥0`; default 0). The mask gives the horizon a history (hysteresis comes from energy removed, not from `Δ_heal` — see (4)).
3. **Void = quiescent vapor at the floor:** inside `C`, `ρ̄` is clamped to `ρ̄_cav` (vapor density; the deficit mass has been pushed to the rim by continuity — **mass-conservative**, the clamped mass is ledgered) and the velocity is damped by the shock fraction (4). A quiescent void at constant vapor pressure presents a pressure-release boundary to the surrounding bulk ⇒ `Γ→−1` **emerges** (not painted).
4. **Shock-class dissipation (one-way, entropy-positive, EOS-anchored):** when a cell newly enters `C`, its kinetic energy cannot be stored by the quiescent void (a rarefied void carries no coherent flow — vacuum-engineer). A fraction `χ_shock` of the crossing KE is removed to `E_diss` (irreversible) and the velocity scaled by `(1−χ_shock)`. The reversible EOS internal-energy change `ΔU = U(ρ̄_cav) − U(ρ̄_before)` is ledgered as `E_latent`. **`χ_shock=1` is the physical value** (quiescent void); `χ_shock=0` is the degenerate **elastic/reversible** limit (the in-engine LOCK control). `χ_shock` is the one modeling coefficient and is **swept** (§3); the verdict must be coefficient-robust (a FLASH that exists only at one `χ_shock` and scales with it = CLIP).
5. **Exact EOS internal energy (closes the predecessor's ledger gap):** `pressure(ρ̄)=c₀²[ρ̄−½ln(1−ρ̄²)]` (`cavitation_flow.py:165–168`, **zero call sites** in the predecessor — the ledger gap). The internal-energy density `U(ρ̄)=ρ∫₁^ρ p(s)/s² ds` (`ρ=1+ρ̄`) is integrated numerically and **validated by free-run KE+U conservation** (calibration). Replaces the linear `½c₀²∫ρ̄²` proxy so latent release across the floor is representable.

### 2.1 Shock-dissipation magnitude — EOS-derived, not free

The dissipation *threshold* is the EOS root `ρ̄_cav` (fixed). The dissipation *magnitude per crossing* is the crossing KE (set by the flow, not dialed) times `χ_shock`. The EOS softening slope at the floor is fixed: `d(c²)/dρ̄|_cav = c₀²(1+ρ̄²)/(1−ρ̄²)² = c₀²(1.382)/(0.382) = 3.618·c₀²`, so `c²(ρ̄)≈3.618c₀²·(ρ̄−ρ̄_cav)` near the floor (a definite, EOS-fixed approach slope). The only free dial is `χ_shock∈[0,1]`; it is swept and the verdict reported across the sweep.

### 2.2 ave-representation-capability-check — WHICH chirality, and the bulk-channel requirement (FLAG)

- **The reflector acts on BULK (compression) waves.** The probe wave-packets MUST be bulk-channel: I implement them as **azimuthal-`m` acoustic OAM pulses** — a compression pulse `ρ̄(r,φ,t)` carrying an `e^{imφ}` phase winding. `m=+1` (co-handed with the pocket circulation Γ) vs `m=−1` (counter-handed), matched amplitude/energy. These are divergence-bearing bulk waves (NOT shear/vortical probes). Verified bulk-channel.
- **WHAT chirality this engine can test (the honest caveat):** the I4₁32 lattice **cholesteric-Bragg** selection rule (hypothesis 0(c)) is a property of the chiral *crystal lattice*. **This continuum bulk-flow engine carries NO lattice handedness** — it cannot represent cholesteric-Bragg selectivity. What it CAN represent is the **rotating-acoustic-horizon frame-dragging** asymmetry: the formed pocket carries circulation Γ (sign = drive sign), and a co-rotating vs counter-rotating bulk-OAM probe sees a different effective medium (rotational Doppler / acoustic-superradiance analog). So the handedness arm tests the **frame-dragging** selection rule, a DIFFERENT mechanism from cholesteric-Bragg. A SELECTIVE result here supports "the reflector has a handedness" but does NOT confirm the I4₁32 cholesteric mechanism specifically (that needs the chiral-crystal engine). Flagged, not built-in.

## 3. APPARATUS INVENTORY — the CLIP suspects (NEW BC knobs + inherited)

| # | knob | default | what it could secretly set | CLIP signature |
|---|---|---|---|---|
| N1 | `iface_thresh` | `ρ̄_cav` (=−1/φ) | the density at which a cell is declared "cavitated" | persistence/pocket-count tracks the threshold |
| N2 | `heal_width` Δ_heal | `0.0` | the over-pressure barrier a void needs to re-close | hysteresis tracks Δ_heal (built-in irreversibility) |
| N3 | `chi_shock` | `1.0` | fraction of crossing-KE dissipated (the shock model) | FLASH exists only at large χ and scales with it |
| N4 | `stencil`/interface width | sharp (1 cell) | how the BC is applied at the void boundary | reflectivity tracks stencil width |
| K1 | `c2_floor` | **0.0** (was 1e-3) | the predecessor's positive floor — now the CONTROL knob | LOCK reappears as c2_floor→+ (the control reproduces the predecessor) |
| K4 | `nu_art` | `5e-4` | artificial (shock-capturing) viscosity | persistence tracks nu_art rather than plateauing |
| K6 | `N` | 160 | grid resolution | pocket/reflectivity tracks resolution |

**Verdict-clearing rule:** a FLASH signature (pocket persistence, hysteresis, latent release, reflectivity asymmetry) that **tracks** N1–N4/K1/K4/K6 under the sweep is **APPARATUS ⇒ CLIP**. A signature **robust** across them (and present for all `χ_shock>0`, plateauing) is provisionally physics. STEP 3 sweeps these BEFORE any verdict.

### 3.5 Expected-value subsection (ave-prereg Step 3.5 — dimensional estimates, canonical primitives only)

- **Crossing KE density** (transonic core, `|u|~M·c₀`, `M~0.8`, void density `ρ=1+ρ̄_cav=0.382`): `½ρ|u|² ~ ½·0.382·(0.8)²·c₀² ≈ 0.12·c₀²` per unit area. Over a pocket of `~`a few % of the domain area `L²`, `E_diss ~ O(10⁻³)·c₀²L²` per cavitation episode — same order as the predecessor's total PE (`~`0.016, result §2.2). So **if** dissipation is real it should be a **resolvable** fraction of the ledger (not a rounding artifact).
- **Vapor pressure (EOS):** `p(ρ̄_cav)=c₀²[−0.618−½ln(0.618)]=c₀²[−0.618+0.240]=−0.378·c₀²` (tension — consistent with a tensile-failure void). The latent `E_latent` per crossing is `O(0.1·c₀²)`×area — resolvable.
- **Reflectivity:** a perfect pressure-release mirror gives `R=|Γ|²=1`. Instrument floor (numerical scatter off a transparent region) expected `O(1–3%)`. Frame-dragging asymmetry for a rotating horizon at edge Mach `M`: rotational-Doppler fractional split `~ 2mΩR/ω_probe`; at `M~0.8`, `m=±1`, `ω_probe~c₀/R`, the split is `O(M)~O(0.8)` in *frequency*, but the *reflectivity* asymmetry `|R_co−R_counter|` is expected smaller, `O(M²)~O(0.1–0.6)` IF frame-dragging is strong, or `≈0` (BLIND) if both handedness reflect equally. The SELECTIVE threshold is `|R_co−R_counter| >` the calibrated floor.

## 4. THE BINS (FROZEN — Rule 11, no post-hoc redefinition)

**Crossing/closure arm:**
- **FLASH** — with the closure active, the crossing is **one-way**: (i) a `c²≤0` pocket forms AND **persists after full de-spin** above a threshold drive (pocket cells > the apparatus floor at `t→∞`, `u=0`); AND (ii) a **latent/dissipation release** is recorded at the crossing (`E_diss` and/or `E_latent` step up at the floor crossing, resolvable per §3.5); AND (iii) the **M-sweep hysteresis loop opens** (up-sweep and down-sweep `ρ̄_core(M)` / pocket-cells(M) do not coincide). AND all three are **robust** to N1–N4/K1/K4/K6 and present for **all** `χ_shock>0` (not single-χ).
- **LOCK** — even with the genuine horizon physics active, the pocket **re-closes on de-spin at all M**, **no hysteresis** (up/down sweeps coincide), `E_diss→0` in the inviscid/`χ_shock→0` limit AND no residual persistence at `χ_shock=1`. The pocket is a reversible spring.
- **CLIP** — any FLASH signature **tracks a §3 knob** (name it): persistence∝χ_shock with no plateau (→ the dial), or hysteresis∝Δ_heal (→ built-in), or reflectivity∝stencil/N, or the whole effect vanishes as `c2_floor→0⁺` is *increased* back toward the predecessor (→ the effect was the clamp).
- **NO-HORIZON** — the `c=0` surface never forms cleanly (the flow never reaches genuinely supersonic-relative-to-`c_eff`, or the pocket is a single under-resolved cell that vanishes at higher `N`). Characterize the limiter.

**Handedness arm:**
- **SELECTIVE** — `R_co > R_counter` beyond the calibrated reflectivity floor (partial asymmetry; both still reflect). Report `R_co`, `R_counter`, the floor, and the known-mirror reference.
- **BLIND** — `R_co ≈ R_counter` within the floor (the horizon reflects both handedness equally; the valve, if any, must come from the lattice mechanism §2.2, not the acoustic horizon).
- **UNRESOLVED** — the reflectivity read does not clear its own instrument floor (cannot distinguish).

**A FLASH/SELECTIVE that sits at a clip value is apparatus (HARD CONSTRAINT). Do NOT debug toward FLASH (Rule 11).**

## 5. PREDICTIONS (discriminating, with the honest prior)

- **Prior expectation (stated to avoid debugging toward FLASH):** the `c²=0` clamp alone makes the void a reflector + horizon, but a horizon's trapping is **conditional on the flow** — de-spin removes the flow, `c_eff` recovers, the horizon dissolves, trapped energy escapes → would heal (LOCK) **unless energy was irreversibly removed**. So genuine FLASH (persistence after de-spin) requires `χ_shock>0`. The **decisive apparatus question** is whether persistence/hysteresis is **robust across `χ_shock∈(0,1]`** (→ FLASH, the horizon+shock are physics) or **scales with `χ_shock`** with no plateau (→ CLIP, the irreversibility is the dial).
- **Control (predecessor reproduction):** the floored-`c²` scheme (`c2_floor=1e-3`, the predecessor) at the SAME drives must show the closure's effects **ABSENT** (LOCK-like reversible compliance, no persistent pocket). If the control already shows persistence, the effect is not the closure.
- **Handedness:** if the rotating horizon frame-drags strongly, `R_co≠R_counter` (SELECTIVE); if the reflection is set purely by the `Z→0` impedance (handedness-blind), BLIND.

### 5.1 Falsifiers
- The closure-FLASH is falsified (→ CLIP) if persistence tracks `χ_shock` (no plateau), or hysteresis tracks `Δ_heal`, or any signature vanishes when `c2_floor` is raised back toward the predecessor's value, or Γ is not conserved across the "event" (→ the event is dissipation/numerics).
- SELECTIVE is falsified (→ BLIND) if `|R_co−R_counter|` ≤ the calibrated floor.

## 6. Regime / phase-state + conserved-vs-pumped (ave-regime-phase-state-check)

- **MODE:** BULK (volumetric K, density). NOT shear, NOT EM-transverse. The probe waves are bulk-channel (§2.2). Scalar/longitudinal-density effect — regime-relevant.
- **REGIME:** near-floor → through-floor rarefaction (the **ruptured** branch the predecessor could not reach). The effect (cavitation/horizon) CAN exist here by construction — NOT a wrong-regime artifact.
- **PHASE-STATE:** compliant (ρ̄>ρ̄_cav) → horizon/rupture (ρ̄≤ρ̄_cav) → (FLASH: persists / LOCK: heals).
- **ave-conserved-vs-pumped:** circulation Γ = conserved (energize+lock, drive sets it once); never pumped. KE↔PE slosh at fixed Γ; `E_diss`/radiation are the only sinks. A run whose Γ drifts beyond the predecessor's 0.044% free-floor in the *quiet* phase is dissipation-contaminated (flagged).

## 7. Free parameters

The ONLY physics input is the swept **drive `M_edge`** (energizes Γ once). `c₀`, the EOS, `ρ̄_cav` are canonical/candidate-derived. `χ_shock` is the one modeling coefficient (swept; `χ=1` physical, `χ=0` the elastic control). N1–N4/K1/K4/K6 are apparatus knobs (swept in STEP 3). No coefficient is tuned to produce the verdict.

## 8. Corpus-grep + anchor re-verification (verify-before-cite, all confirmed 2026-06-10)

- **Predecessor** (CLIP, gated the named closure): `analysis/2026-06-10-cavitation-core-probe`, result `§0-bis(a),(e)`; engine `cavitation_flow.py:159–163` (the positive floor), `:165–168` (`pressure()`, zero call sites).
- **EOS / floor:** `04_superluminal_transit.tex:86` (`c_eff²=c₀²(1+ρ̄/(1−ρ̄²))`, "not a free parameter"); `:89` (`Z_eff=Z_0/√(1−ρ̄²)` — the EM impedance that does NOT collapse, §1.2). Verified.
- **Reflector mechanism (candidate analogy):** `yang-mills-steps3-5.md:43` (`Z_knot→0 ⇒ Γ=(Z_knot−Z_0)/(Z_knot+Z_0)→−1`, EM color-confinement mirror). Verified — cited hypothesis-class for the bulk channel.
- **Cavitation number / no-bound-state limit:** `de-broglie-standing-wave.md:248` (`C=v/c_S=Zα/n`; at `Z=1/α≈137`, `C=1`, no bound state). Verified — the macroscopic-`C→1` analog of the core reaching its own sound-speed-vanishing surface.
- **FIREWALL:** `_orchestration/double-slit-ee-mapping.md:92` (cavitation = Rayleigh-Plesset, DIFFERENT from the Γ=−1 cavity). Verified.
- **No existing sonic-horizon / free-boundary cavitation closure** in `src/ave/` (predecessor's `CavitationFlow2D` floors `c²` positive). Green-field closure; cross-checked by the in-engine elastic-limit control (`χ_shock=0`) + the floored-scheme control + the known-mirror reflectivity calibration.

**Corpus state:** OPEN. The reach/crossing is established (predecessor, clip-invariant). The *kind* of event (FLASH/LOCK/CLIP/NO-HORIZON) and the handedness (SELECTIVE/BLIND) are unrun.

