# RESULT — Sonic-horizon closure: the `c²=0` surface forms a clean reflecting horizon, but the pocket is a REVERSIBLE SPRING (LOCK), and the rotating horizon is handedness-BLIND

**Date:** 2026-06-10
**Branch:** `analysis/2026-06-10-sonic-horizon-closure` (worktree off `analysis/2026-06-10-cavitation-core-probe`; not pushed/merged)
**Prereg (frozen, committed alone first):** [`2026-06-10_sonic-horizon-closure_prereg.md`](2026-06-10_sonic-horizon-closure_prereg.md) (commit `f8226ac0`, before any run artifact)
**Predecessor (Rule 12 — this is the NAMED closure that probe GATED, not a refill):** `analysis/2026-06-10-cavitation-core-probe`, result §0-bis(e) (verdict CLIP)
**Engine (new):** [`src/ave/core/sonic_horizon_flow.py`](../src/ave/core/sonic_horizon_flow.py) — `SonicHorizonFlow2D` (subclass of the predecessor's `CavitationFlow2D`; the floored engine is kept INTACT as the control)
**Driver:** [`src/scripts/vol_4_engineering/sonic_horizon_closure.py`](../src/scripts/vol_4_engineering/sonic_horizon_closure.py) · figures [`…_figures.py`](../src/scripts/vol_4_engineering/sonic_horizon_closure_figures.py)
**Data:** `src/scripts/vol_4_engineering/_output/sonic_horizon_closure_results.json`
**Governing discipline:** `ave-apparatus-floor-attribution`. Skills: substrate-native-check, ave-prereg (Step 3.5), ave-canonical-source, ave-driver-script-honesty, ave-regime-phase-state-check, ave-conserved-vs-pumped, verify-before-cite, ave-representation-capability-check.

---

## 🔴 VERDICT ADDENDUM — handedness arm `BLIND → UNRESOLVED` (2026-06-10 panel follow-up; Rule 12 substitution-not-retraction)

**Status:** the closure-arm **LOCK** verdict (§0, §2, §3, §5, §6) **STANDS UNCHANGED**. The **handedness arm** verdict is **RETRACTED from BLIND to UNRESOLVED** per Rule 12 — the original §0/§4/§7 BLIND text is **preserved below, unedited**; this header supersedes it. Panel: 2026-06-10 sonic-horizon-closure adversarial review (run `f1648a0c`, prereg `f8226ac0`).

**1. Why the handedness BLIND is not a valid null (the probe was degenerate in `m`).**
The OAM probe `SonicHorizonFlow2D.add_oam_pulse` set the density perturbation as

> `sonic_horizon_flow.py:184  →  dens = amp * ring * np.cos(m * phi)`

which is **EVEN in `m`** (`cos(mφ) = cos(−mφ)`), and the radial velocity `ur = sgn·c0·dens` inherited that symmetry. So the `m=+1` (co) and `m=−1` (counter) probes were **bit-identical fields** — confirmed verbatim in the recorded data: `R_co = R_counter = 0.005989094178529873` to 18 digits, with `e_inc_co = e_inc_ct` identically (M=0.9 χ=1.0; same bit-identity at M=1.0 and χ=0). **The reported `asym = 0.0000` and `R_co = R_counter` were the PROBE's `m`-symmetry, NOT the medium's.** The prereg **§2.2 froze a genuine `e^{imφ}` winding**; the implementation collapsed it to its real (cos) part only, which carries no chirality. A null produced by an instrument that **cannot represent the asymmetry by construction** is not a frame-dragging null. Per the **frozen prereg's `UNRESOLVED` bin** ("the reflectivity read does not clear its own instrument floor / cannot distinguish"), the honest bin is **UNRESOLVED**. (Repaired + re-run in R1 — see §4-bis.)

**2. Second representation gap (restated, load-bearing — holds EVEN AFTER the probe is repaired).**
A fixed-probe re-run with a correct `e^{imφ}` winding tests **rotating-horizon FRAME-DRAGGING acoustic selectivity ONLY**. The **I4₁32 cholesteric-Bragg lattice selection rule** (hypothesis 0(c)) is **NOT representable** in this continuum bulk-flow engine (prereg §2.2 representation-capability flag) — it requires the chiral-crystal engine. So **neither** a repaired-BLIND **nor** a repaired-SELECTIVE result here can confirm or refute the cholesteric mechanism.

**3. Label softenings (panel-mandated, verdict-neutral) — applied inline below + logged here:**
- **(a)** "EOS-anchored shock dissipation" → "**tuned one-way void-KE sink (`χ_shock`) applied at the EOS-defined horizon; the reflector locus and the latent ledger are EOS-anchored**". Rationale: engine `sonic_horizon_flow.py:136–139` sets `E_diss += χ_shock · (void KE)` — the sink MAGNITUDE is the tuned coefficient `χ_shock`, while the threshold/locus (`ρ̄_cav`) and the `ΔU` latent ledger are EOS-fixed. Applied in §0, §6, queue #1.
- **(b)** §3 "no step, spike, or kink" → "**no discontinuous latent step; the slope steepens smoothly at dissipation onset**".
- **(c)** §3 23%/77% ledger split **softened to an estimate**: `E_sponge`, `E_visc` (`nu_art`), and `dU_massclamp` were **NOT separately ledgered**. The 23% is `E_diss / (KE+PE decline)`; the 77% is **inference-by-subtraction**. Note `mass_clamp = 5.0e-4` at M=0.9 ≈ **3× `E_diss`** (`1.67e-4`), so the unledgered mass-clamp channel alone exceeds the one-way sink — the split is an estimate, not a measured partition.
- **(d)** **FLAGGED — NOT applied (flag-don't-fix + verify-before-cite).** The panel asked to change the firewall anchor `double-slit-ee-mapping.md:92 → :101`. A fresh grep (2026-06-10) shows **`:92` IS the correct verbatim firewall content** ("sonoluminescence cavitation = saturated Rayleigh-Plesset inertia, a DIFFERENT mechanism from the Γ=−1 cavity"), while **`:101` is the unrelated E↔B-row pending-note** (auditor-queue item #2 of that brief). Moreover this firewall anchor appears **only in the FROZEN prereg (§0.3, §8)** — not in this result doc — and a frozen prereg must not be post-hoc edited (Rule 11). The fuller firewall guard (with the `ρ_eff` formula + `sonoluminescence-derivation.md:25-27`) is at **`:40`**. Surfaced for Grant adjudication; not silently rewritten to a wrong target.
- **(e)** The Stage-B apparatus gate (§1) was swept **One-At-a-Time (OAT)** — one knob varied per row at fixed defaults — **NOT full-factorial**; cross-knob interactions were not gated.

**4. Propagation into the 6 queued corpus-state items (§8):**
- **#1** (NEW capability): label fix (a) only — "tuned void-KE sink at the EOS-defined horizon" replaces "EOS-anchored shock dissipation". Capability claim otherwise stands.
- **#2** (NEW result LOCK): the clause "**rules out the acoustic horizon as the chirality valve (BLIND)**" is **RETRACTED** → the handedness arm is **UNRESOLVED** (the ±m probe was degenerate); the acoustic horizon is **neither ruled out nor in** as the chirality valve pending the R1 re-run. The **LOCK** half of #2 stands.
- **#3** (FLAG mass-conservation LOCK mechanism): **unaffected** (used no OAM probe).
- **#4** (FLAG representation-capability): **STRONGER.** There is **no valid frame-dragging null at all** — the BLIND was a probe artifact. The **do-not-headline-vapor-lock-v5** flag is strengthened: this engine supplies **neither** support **nor** even a clean BLIND null for the v5 "chirality valve = selection rule" claim.
- **#5** (FLAG `ρ̄_cav` CANDIDATE-CLAIM): **unaffected.**
- **#6** (FLAG floored-predecessor fragility): **unaffected.**

**5. Repair + re-run (R1).** The probe is re-implemented with a true quadrature `e^{imφ}` winding (`±m` physically distinct, opposite azimuthal circulation), guarded by a keeper unit test (`R(+m) ≠ R(−m)` on a rotating reference — a defect class `make verify` could not otherwise catch). The Stage-A handedness floor is re-derived on genuinely distinct `±m` fields and Stage D re-run. **Re-run verdict + asym numbers: see the Addendum-to-the-Addendum (§4-bis), added in the R1 commit.**

---

## 0. VERDICT — closure arm **LOCK**; handedness arm **BLIND**

> **With the full sonic-horizon closure ACTIVE — `c_eff²` clamped at exactly 0 below the locus (impedance collapse `Z_bulk=ρ·c→0` ⇒ a pressure-release `Γ→−1` reflector AND a sonic horizon), a one-way mass-conservative void at the vapor floor, and a tuned one-way void-KE sink (`χ_shock` up to 1) applied at the EOS-defined horizon (the reflector locus and the latent ledger are EOS-anchored) — a genuine reflecting horizon FORMS cleanly (max pocket 1280 `c²≤0` cells at M=1.0), the crossing produces real irreversible dissipation (`E_diss` up to 6.6e-4, `L` drift up to 3.1%), but the pocket is a REVERSIBLE SPRING: it heals on full de-spin at EVERY drive `M∈[0.6,1.0]` (`final_pocket=0`, `ρ̄_core` recovers to ≈−0.06..−0.08) and at EVERY `χ_shock∈{0,0.25,0.5,1.0}` (`final_pocket=0` throughout). Persistence does NOT track the dissipation knob, so this is a genuine LOCK, not a CLIP. The rotating horizon is handedness-BLIND: `R_co(m=+1) = R_counter(m=−1)` to within 0.000 (the static-mirror handedness floor), at M=0.9, M=1.0, and χ=0.**

**Plumber-physical one-liner (the LOCK mechanism — a single cause explains every failure, Rule 11):** cavitation is **mass-conservative** — the density evacuated from the core piles up as a `ρ̄>0` rim over-pressure. The sonic-horizon shock dissipation removes **kinetic** energy at the crossing, but the rim over-pressure is a **potential**-energy reservoir that the horizon does NOT vent. So the rim always pushes mass back in and refills the void, regardless of how much KE was dissipated. **Removing KE cannot stop a PE-driven refill.** A true vapor-LOCK would need the rim mass to LEAVE the system (radiate away) or a topological wall that forbids refill — neither is supplied by the `c²=0` horizon.

**Implication (hypothesis-class, per the prereg STEP-5 map): LOCK = the cavitated pocket is a spring even WITH genuine horizon physics.** The vapor-lock picture's defining **irreversibility is NOT supplied by the sonic-horizon closure.** This is the honest negative. It does not refute the vapor-lock event; it **localizes** where the irreversibility must come from (rim-venting / a hardened `Γ=−1` wall), and rules out the sonic-horizon shock as its source. The chirality valve (hypothesis 0(c)) is **not** demonstrated by the acoustic horizon (BLIND); if it exists it must be the lattice cholesteric-Bragg mechanism (which this continuum engine cannot represent — prereg §2.2), not rotating-horizon frame-dragging.

This is the discipline at full strength: **the data were NOT debugged toward FLASH.** The prereg (§5) stated the prior — that a horizon's trapping is conditional on the flow and FLASH would require irreversibly-removed energy robust across `χ_shock`. We implemented exactly that irreversibility and found it insufficient. Branch closed on a clean negative with a named mechanism.

---

## 1. The apparatus gate FIRST (STEP 3) — what the verdict had to clear (ALL CLEAN)

Per `ave-apparatus-floor-attribution`, the NEW BC knobs (prereg §3) were swept 4× each at the **sub-crossing** drive `M=0.6` (deepest ≈ −0.41, NOTHING should cavitate) BEFORE any physics run. Any pocket/`E_diss` there is the knob's false-positive floor.

| knob swept (4 values) | max pocket cells | `E_diss` | reads |
|---|---|---|---|
| `iface_thresh` (−0.668 → −0.518) | 0, 0, 0, 0 | 0 | no false trigger even at the shallowest threshold |
| `heal_width` (0 → 0.05) | 0, 0, 0, 0 | 0 | the re-closing barrier creates no sub-crossing pocket |
| `chi_shock` (0 → 1.0) | 0, 0, 0, 0 | 0 | the dissipation model fires nothing below the floor |
| `nu_art` (1e-4 → 5e-3) | 0, 0, 0, 0 | 0 | shock-capturing viscosity creates no pocket |
| `N` (128 → 224) | 0, 0, 0, 0 | 0 | resolution-robust; no under-resolved false pocket |

**Gate conclusion: every new BC knob has a ZERO false-positive floor at the sub-crossing drive.** A pocket/`E_diss`/persistence signature in the physics runs cannot be a sub-crossing artifact of these knobs. **(Caveat, Addendum §3(e): this gate was swept One-At-a-Time — one knob varied per row at fixed defaults — NOT full-factorial; cross-knob interactions were not gated.)**

**Known-positive:** a hand-opened static pressure-release void (`set_static_mirror`, radius 0.18) is correctly **held** by the BC: pocket 2608 → 2624 cells after 800 steps (the reflector holds a void when one is imposed). The BC works; the physics runs test whether the *dynamics* sustain one.

**Energy-ledger calibration (A1):** the exact-EOS internal energy `U(ρ̄)` conserves with KE to **−0.021%** over 600 steps in a free inviscid acoustic run — the U-table (which closes the predecessor's `pressure()`-had-zero-call-sites ledger gap) is validated as the correct conserved PE.

---

## 2. The closure arm (STEP 4a) — reach, transience, persistence, the χ-sweep crux

**UP branch (fresh runs, solid-body column R_core=0.18, N=160, nu_art=5e-4):**

| M_edge | deepest ρ̄_core | max pocket cells | final pocket (no de-spin) | E_diss | L drift |
|---|---|---|---|---|---|
| 0.6 | −0.4062 | 0 | 0 | 0 | −0.47% |
| 0.7 | −0.5353 | 0 | 0 | 0 | −0.86% |
| **0.8** | **−0.6180** | **212** | 0 | 9.66e-6 | −1.35% |
| 0.9 | −0.6180 | 732 | 0 | 1.67e-4 | −2.05% |
| 1.0 | −0.6180 | 1280 | 0 | 6.59e-4 | −3.11% |

- **The horizon FORMS cleanly (not NO-HORIZON):** at `M≥0.8` a `c²≤0` void of up to 1280 interior cells forms; `ρ̄_core` reaches the void floor exactly (−0.6180 = `ρ̄_cav` = the `iface_thresh` clamp). The reflector + horizon are real.
- **It is TRANSIENT under sustained drive:** even with the drive held on, the pocket peaks then DECAYS to 0 (`final_pocket=0` at every M). The mass-conservative refill (rim over-pressure) heals it during the ring-down.

**PERSISTENCE after FULL de-spin (χ_shock=1, the physical value):**

| M_edge | max pocket | → final pocket after de-spin | final ρ̄_core |
|---|---|---|---|
| 0.8 | 212 | **0** | −0.069 |
| 0.9 | 732 | **0** | −0.077 |
| 1.0 | 1280 | **0** | −0.083 |

The pocket re-closes on de-spin at **every** drive; `ρ̄_core` recovers to near zero. **No persistent defect (FLASH signature i NEGATIVE).**

**The χ-sweep CRUX (M=1.0) — the decisive CLIP test (Fig 2):**

| χ_shock | max pocket | final pocket after de-spin | final ρ̄_core | E_diss |
|---|---|---|---|---|
| 0.00 | 1044 | **0** | −0.079 | 0 |
| 0.25 | 1268 | **0** | −0.083 | 3.78e-4 |
| 0.50 | 1284 | **0** | −0.083 | 4.43e-4 |
| 1.00 | 1280 | **0** | −0.083 | 6.59e-4 |

`E_diss` scales with `χ_shock` (0 → 6.6e-4) — the dissipation knob does what it says. **But `final_pocket = 0` for EVERY `χ_shock`, and `final ρ̄_core` is flat (−0.079..−0.083).** Persistence does **not** track the dissipation knob and does **not** appear even at the maximally-dissipative physical value `χ=1`. **This is the verdict-clearing test: the (absent) FLASH does not track a §3 knob → the verdict is genuine LOCK, not CLIP.**

**Hysteresis loop (Fig 3):** down-sweep (de-spin from M=1.0 through effective M=0.9…0.6) gives `ρ̄_core` = −0.412, −0.269, −0.271, −0.175, −0.195 — **shallower** than the UP branch (−0.406, −0.535, −0.618, −0.618, −0.618), with **pocket cells = 0 at every down-branch point.** The loop opens only in the **dissipative-relaxation** direction (the core has refilled and stays refilled); the **pocket-cells hysteresis is CLOSED (0 = 0)** — no persistent defect carried down from the high drive. This is LOCK (reversible spring + ordinary dissipative relaxation), not FLASH (persistent pocket).

---

## 3. Latent ledger — exact-EOS energy accounting AT the crossing (M=0.9, recorded series)

The exact-EOS internal energy `U(ρ̄)` (Stage A-validated) lets us read the crossing honestly. The pocket first appears at `t=0.258`; the window straddling it:

| t | pocket cells | ρ̄_core | KE | PE_exact | KE+PE | E_diss (cum) |
|---|---|---|---|---|---|---|
| 0.243 | 0 | −0.5962 | 0.048756 | 0.014349 | 0.063105 | 0 |
| 0.251 | 0 | −0.6102 | 0.048297 | 0.014728 | 0.063025 | 0 |
| **0.258** | **256** | −0.6180 | 0.047835 | 0.015071 | 0.062907 | 2.70e-5 |
| 0.266 | 544 | −0.6180 | 0.047330 | 0.015351 | 0.062680 | 1.09e-4 |
| 0.273 | 656 | −0.6180 | 0.046876 | 0.015613 | 0.062490 | 1.46e-4 |
| 0.280 | 728 | −0.6180 | 0.046445 | 0.015885 | 0.062330 | 1.65e-4 |

- **The crossing is CONTINUOUS — no latent-release step (FLASH signature ii NEGATIVE).** KE declines smoothly (0.04876 → 0.04645), PE_exact rises smoothly (0.01435 → 0.01589), KE+PE eases down (0.063105 → 0.062330) with **no discontinuous latent step; the slope steepens smoothly at dissipation onset** at the `ρ̄_cav` crossing. The reactance pair (CP6: KE = L-state ↔ PE_exact = C-state) exchanges smoothly.
- **The one-way `E_diss` is real but a minority sink (split is an ESTIMATE, not a measured partition):** it accrues **gradually** (2.7e-5 → 1.65e-4 across the crossing); `E_diss / (KE+PE decline)` ≈ **23%** of the ≈ 7.3e-4 window decline. The remaining ≈ 77% is **inference-by-subtraction** — `E_sponge` (acoustic radiation), `E_visc` (`nu_art` shock-capturing), and `dU_massclamp` (the void-floor clamp) were **NOT separately ledgered**. In particular `mass_clamp = 5.0e-4` at M=0.9 is ≈ **3× `E_diss`** (`1.67e-4`), so the unledgered mass-clamp channel alone exceeds the one-way sink; treat the 23/77 split as an order-of-magnitude estimate. **There is no discontinuous latent heat** — the EOS `c²=0` root is a smooth softening point, not a first-order phase boundary, even with the void clamp and shock dissipation active.
- **Mass-clamp honesty:** the void-floor clamp added mass is bounded (`mass_clamp` ~1e-3, same order as the PE) and biases conservatively (it suppresses, never manufactures, a deeper deficit). `L` drift −2.07% at M=0.9 is the real transient dissipation (consistent with the predecessor's ~2% at high drive; conservative since viscosity biases shallower).

---

## 4. Handedness arm (STEP 4b) — BLIND (Fig 5)

> 🔴 **SUPERSEDED → UNRESOLVED (Rule 12; see Verdict Addendum §1).** The BLIND below is invalid: the OAM probe (`sonic_horizon_flow.py:184`, `cos(m·φ)`, EVEN in `m`) made the ±m fields bit-identical, so `R_co = R_counter` was the probe's symmetry, not the medium's. Body preserved unedited. Repaired re-run: §4-bis.

Bulk azimuthal-`m` acoustic OAM pulses (compression pulses with `e^{imφ}` phase — bulk-channel, prereg §2.2 / ave-representation-capability-check) probe the formed rotating core via difference-field flux-through-circle reflectometry (incident + reflected measured on the SAME circle r=0.30, so cylindrical geometry cancels).

**Calibration (Stage A):** known static pressure-release mirror `R = 0.310` (the loss-limited reference over the round trip); transparent (no pocket) `R = 0.002` (focal-passage baseline); **handedness instrument floor `|R(+1)−R(−1)| = 0.0000` on the non-rotating mirror** (m-symmetry, as it must be — this is the floor the SELECTIVE test must beat).

| config | R_co (m=+1) | R_counter (m=−1) | asym (co−counter) |
|---|---|---|---|
| M=0.9, χ=1.0 | 0.006 | 0.006 | **+0.0000** |
| M=1.0, χ=1.0 | 0.007 | 0.007 | **+0.0000** |
| M=0.9, χ=0.0 | 0.006 | 0.006 | **+0.0000** |

**BLIND:** `R_co = R_counter` to 0.000 (= the static-mirror floor) in every config. The rotating-acoustic-horizon **frame-dragging** asymmetry is below the instrument floor. **Caveat (flag, load-bearing):** the absolute reflectance ≈ 0.006 is only ~2% of the static-mirror reference and barely above the focal floor — **because the LOCK result means the pocket is transient, there is no SUSTAINED reflector for the probe to be selective about.** So BLIND here is "no frame-dragging selectivity on a weak/transient rotating reflector." It does NOT test the I4₁32 **cholesteric-Bragg** lattice selection rule (hypothesis 0(c)), which this continuum bulk-flow engine **cannot represent** (prereg §2.2) — that requires the chiral-crystal engine. The handedness valve, if real, is not the acoustic horizon.

---

## 5. Control comparison (STEP 4c) — the closure's effects vanish when the closure is OFF

| run | deepest ρ̄_core | after de-spin | persistent pocket | E_diss |
|---|---|---|---|---|
| **floored predecessor** `CavitationFlow2D` (c2_floor=1e-3), M=0.8 | −0.7675 | −0.069 (heals) | 0 (`c²≤0` never, by construction) | n/a (not tracked) |
| floored predecessor, M=1.0 | −0.9500 | NaN (de-spin rebound blows up) | 0 | n/a |
| **closure with floor RAISED back** (c2_floor=1e-3, χ=0), M=1.0 | −0.6180 | heals | **0** | **0** |

- The **floored predecessor** reaches **deeper** (−0.77 / −0.95) than the closure's clamped −0.618 — confirming the closure's −0.618 is the `iface_thresh` void clamp (the closure declares cavitation and holds the void at the floor; the floored scheme keeps rarefying to `rho_floor`). It heals where stable; at M=1.0 the floored scheme's deep −0.95 core blows up on de-spin (NaN) — the floored engine is **numerically fragile at high drive on de-spin** (flag), which is itself part of why a positive floor cannot decide FLASH/LOCK cleanly. The closure (clamp at −0.618 + inert void) is **stable** through the same de-spin.
- **Turning the closure OFF** (`χ=0` removes the one-way dissipation): `E_diss=0`, `final_pocket=0`. The distinctive closure quantity (`E_diss`) vanishes exactly when the dissipation is disabled — confirming `E_diss` is the closure's effect, and that **even the closure's reflector + clamp without the dissipation sink is reversible.** The closure's effects are correctly ABSENT in the control.

---

## 6. Implication for the vapor-lock picture (one paragraph, hypothesis-class language)

**Hypothesis-class statement (NOT a canonical claim):** the cavitation-core probe (predecessor) GATED the FLASH/LOCK question on a *named below-floor closure with the dissipation derived from the EOS, swept inside the reversibility test* (predecessor result §0-bis(e)). This probe **opened and ran exactly that closure** — the `c²=0` locus treated as a sharp-interface sonic horizon: an impedance-collapse pressure-release reflector (`Z_bulk→0 ⇒ Γ→−1`, the YM `Z_knot→0` mechanism applied to the bulk channel) with a one-way, entropy-positive, tuned void-KE sink applied at the EOS-defined horizon (reflector locus + latent ledger EOS-anchored; sink magnitude = the tuned `χ_shock`). **The result is LOCK.** Even with the genuine horizon physics and the maximally-dissipative physical `χ_shock=1`, the cavitated pocket is a **reversible spring**: it heals on de-spin at all drives, with no persistent defect, no pocket-cells hysteresis, and a smooth (non-latent) crossing. **The vapor-lock picture's defining IRREVERSIBILITY is therefore NOT supplied by the sonic-horizon closure.** The single mechanism (Rule 11) is **mass-conservation of the cavitation deficit**: the evacuated mass becomes a rim over-pressure (a potential-energy reservoir) that refills the void; the horizon dissipates *kinetic* energy at the crossing but does not vent the *rim potential energy*, so the refill always completes. A genuine vapor-LOCK would require the rim mass to LEAVE the system (radiate away) or a hardened `Γ=−1`-type topological wall that forbids refill — a **separate, named mechanism with its own verification chain (Rule 12 — NOT a refill of this slot).** This probe therefore **sharpens** the predecessor's localization: the irreversibility is not in the `c_eff²(ρ̄)` EOS (predecessor finding), AND it is not in the sonic-horizon shock dissipation either (this probe) — it must be in **rim-venting / topological-wall** physics. The chirality valve (hypothesis 0(c)) is **not** the acoustic horizon (BLIND); if real it is the I4₁32 cholesteric-Bragg lattice mechanism, untestable in this continuum engine.

---

## 7. DERIVED / VERIFIED / BLOCKED (honest split)

**DERIVED / canonical-anchored:**
- The reflector mechanism `Z_bulk = ρ·c_bulk → 0 ⇒ Γ = (Z−Z₀)/(Z+Z₀) → −1` is the bulk-channel analog of the YM `Z_knot→0` color-confinement mirror (`yang-mills-steps3-5.md:43`). The EM-channel `Z_eff = Z₀/√(1−ρ̄²)` does NOT collapse (≈1.27 Z₀ at the floor) — the reflector is correctly the BULK impedance (prereg §1.2). Hypothesis-class analogy, not an identity.
- The EOS `c²=0` root `ρ̄_cav=−1/φ` and softening slope `d(c²)/dρ̄|_cav = 3.618 c₀²` (`04_superluminal_transit.tex:86`). `ρ̄_cav` kept CANDIDATE-CLAIM throughout (not promoted).

**NUMERICALLY VERIFIED (this probe — native c₀ units; signs/depths/reversibility unit-free):**
- The horizon FORMS (max pocket 1280 cells at M=1.0; `c²≤0` void; reflector holds an imposed void, Stage B known-positive).
- The crossing produces real one-way dissipation `E_diss` ∝ `χ_shock` (0 → 6.6e-4), with `L` drift up to 3.1%.
- The pocket is a REVERSIBLE SPRING: `final_pocket=0` after de-spin at all M and all χ_shock; pocket-cells hysteresis closed; crossing smooth (no latent step) → **LOCK**.
- The verdict is knob-independent: the (absent) FLASH does not track `χ_shock`, `iface_thresh`, `heal_width`, `nu_art`, or `N` (sub-crossing gate clean; χ-sweep flat) → **not CLIP**.
- Handedness: `R_co = R_counter` to the 0.000 static-mirror floor at M=0.9/1.0/χ=0 → ~~**BLIND**~~ 🔴 **RETRACTED → UNRESOLVED** (Addendum §1: the ±m probe was degenerate; `0.000` was the probe's `m`-symmetry). Repaired re-run: §4-bis.
- Exact-EOS energy ledger validated (free-run drift −0.021%); the predecessor's `pressure()`-zero-call-sites ledger gap is closed.

**BLOCKED / out of scope:**
- Absolute units (natural c₀; the verdict is dimensionless: depths, reversibility, ratios).
- The rim-venting / hardened-`Γ=−1`-wall irreversibility mechanism the LOCK localizes — a separate hypothesis (Rule 12), not run here.
- The I4₁32 cholesteric-Bragg handedness selection rule — NOT representable in this continuum bulk-flow engine (prereg §2.2); needs the chiral-crystal engine.
- 3D vortex-ring geometry (deferred; the 2D column is the right tool for a free-boundary closure + apparatus sweep).

---

## 8. Corpus-state deltas to QUEUE (auditor lands; implementer surfaces only)

1. **NEW capability:** `SonicHorizonFlow2D` — the sharp-interface free-boundary sonic-horizon closure on the bulk-flow branch (impedance-collapse reflector + a tuned one-way void-KE sink at the EOS-defined horizon + exact-EOS internal-energy ledger). First AVE engine that integrates `c²=0` as a moving free boundary rather than flooring it positive. Closes the predecessor's `pressure()`-zero-call-sites ledger gap.
2. **NEW result (manifestation-class):** the named sonic-horizon closure the cavitation-core probe GATED (predecessor §0-bis(e)) returns **LOCK** — the cavitated pocket is a reversible spring even with the genuine horizon + one-way shock dissipation; the vapor-lock irreversibility is NOT in the sonic-horizon closure. Forward-useful: localizes the irreversibility to rim-venting / topological-wall physics. ~~and rules out the acoustic horizon as the chirality valve (BLIND).~~ 🔴 **RETRACTED (Addendum §4): the handedness arm is UNRESOLVED — the acoustic horizon is neither ruled out nor in as the chirality valve (the ±m probe was degenerate; repaired re-run §4-bis).**
3. **FLAG (flag-don't-fix) — the LOCK mechanism is mass-conservation:** the rim over-pressure (a PE reservoir) refills the void; the horizon dissipates KE but does not vent the rim PE. Any future vapor-lock-FLASH hypothesis must specify how the rim mass leaves the system. Surfaced verbatim, not reframed.
4. **FLAG — representation-capability (🔴 STRENGTHENED, Addendum §4):** the handedness arm is **UNRESOLVED** — there is **no valid frame-dragging null at all** (the ±m probe was degenerate, Addendum §1). Even after repair (§4-bis), a frame-dragging re-run is **NOT** the I4₁32 **cholesteric-Bragg** lattice selection rule, which this continuum engine cannot represent (needs the chiral-crystal engine). The vapor-lock v5 "chirality valve = the mirror's selection rule" claim is **NOT** supported by this engine, and there is not even a clean BLIND null. Do not headline v5 on this engine. *(Original BLIND-based wording preserved: "the handedness BLIND is for rotating-horizon frame-dragging, NOT the I4₁32 cholesteric-Bragg lattice selection rule... Do not headline v5 on this BLIND.")*
5. **FLAG — `ρ̄_cav` remains CANDIDATE-CLAIM** (zero KB/constants hits); this probe does not promote it. It confirms the `c²=0` root is a clean reflecting horizon and the crossing is dissipative-but-reversible; the physical interpretation still needs the §6 rim-venting mechanism + Grant adjudication.
6. **FLAG — the floored predecessor is numerically fragile on de-spin at M=1.0 (NaN rebound);** the sharp-interface closure (clamp + inert void) is stable through the same de-spin. A note for any future use of the floored `CavitationFlow2D` at high drive.



