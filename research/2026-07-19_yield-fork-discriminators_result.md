# RESULT — Yield-fork discriminators: thixotropy-τ (Leg A) + memristor loop-area (Leg B)

> **SECTOR HEADER (read first).**
> - **MODE:** driven, time-domain LC-relaxation of the longitudinal-A1 bulk saturation state `S(t)`. NOT a minimization, NOT continuum-Helmholtz.
> - **REGIME / PHASE-STATE:** near-yield crossing, **Regime II→III** (V_SNAP-referenced three-regime convention, `k4_tlm.py:308–311`). The registered drive `r∈[0.4,1.0]` spans Regime II into III/rupture — the band the thixotropy prereg §2.6/§40 mandates (bulk, near-yield; NOT the transverse achromatic sector, which is rate-asymmetry-free by construction).
> - **DISCIPLINE:** frozen-then-run (protocols pushed before driver code); engine/meter byte-UNTOUCHED (kernel byte-locked to `k4_tlm.py:283,291` and proven bit-identical by test); Rule-11 (frozen adjudication governs the verdict; findings do not retro-edit it); flag-don't-fix; verify-before-cite.

**Date:** 2026-07-19 · **Lane:** implementer, yield-fork discriminators (Grant dispatch 2026-07-19) · **Branch:** `feat/yield-fork-discriminators` · **Sidecar:** `research/2026-07-19_yield-fork-discriminators_result.json`

**The fork this lane serves (unchanged, OPEN, ruling stays Grant's):** *finite-area memristive loop (`∮S dr≠0`, dissipative) vs zero-area saturating reactance (lossless refusal) at the near-yield crossing* (`research/2026-07-17_regime-iv-dissipation-audit.md` §5). Grant's reversible-reactive lean is RECORDED; the fork stays OPEN; this lane RUNS the two registered discriminators. **It does not close the fork.**

---

## 1. Headline

| Leg | Frozen protocol | Verdict (frozen bin) | One line |
|---|---|---|---|
| **A — thixotropy τ** | `2026-06-09_thixotropy-amplitude-dependent-tau_prereg.md` (+ PROTOCOL-COMPLETION 2026-07-19) | **B** (rectification door closed by derivation) | canonical kernel has **no genuine `sign(dr/dt)` memory** and is dissipative → excluded from bin A |
| **B — loop area** | `2026-07-19_yield-fork-loop-area_PROTOCOL-COMPLETION.md` (`P_phase5`, `tau-relax-derivation.md:109`) | **NEITHER** (frozen bin, fail-closed) — but its *evidential* weight is re-banked below | the frozen **(r,S)-plane** window test is **information-free** (a priori unreachable for a first-order kernel); ★the **testable (V,I) plane** measured its peak at **`ωτ=0.911`, INSIDE `[0.85,0.95]`** (F-B2 caveat: no origin-pinch) |

> **★ HEADLINE DATUM (2026-07-19 repair, R-1 — was omitted).** The one datum that leans *toward* the memristive window is the **(V,I)-plane peak at `ωτ=0.911`, INSIDE `[0.85,0.95]`** (sub-rupture `Δr=0.25`: `0.9577`, just above the upper edge). The frozen NEITHER verdict was produced by the **(r,S) plane**, whose loop-area peak is the Debye dissipation shape — **pinned at `ωτ≈1.00` across the entire drive family** (`r_0∈[0.3,0.9], Δr∈[0.05,0.5]`; verified) — so the `[0.85,0.95]` window is **a-priori unreachable in that plane**. The NEITHER verdict therefore carries **no evidence against the memristive branch**; it is a theorem of the observable that plane fails. Details: F-B1 (re-banked), §4.

**Neither leg adjudicates the fork against Grant's lean.** Both relocate the crux to the same upstream object: **`#59` Flag F** — whether the near-yield `S`-dynamics are *first-order overdamped* (dissipative, the frozen model) or *second-order reactive* (`I_S≠0`, lossless, Grant's branch). That is a **derivation** question, upstream of and unreachable by either driver. Routed to Grant (§6).

---

## 2. What was run (both legs share one byte-locked kernel; engine untouched)

Canonical Level-2 kernel, **byte-locked to the engine**:
- `S_eq(r) = √(max(0, 1 − min(|r|,1)²))` — verbatim `k4_tlm.py:283`.
- Level-2 ODE `dS/dt = (S_eq − S)/τ_relax`, backward Euler `S_{n+1} = (S_n·τ + dt·S_eq)/(τ + dt)` — verbatim `k4_tlm.py:291`.
- Engine-native units: `τ_relax = TAU_RELAX_NATIVE = 1.0` (constants.py:453, asserted in-driver), `V_SNAP=1`, `ℓ_node=1`, `m_e c²=1`, so `r ≡ V/V_SNAP`, `ωτ=ω`.
- Symmetric drive `r(t)=0.7+0.3·sin(ωt)` (registered `#59` §6.4/§11 near-yield point). `dt=min(2π/ω/512, τ/50)`; settle `max(8 periods,20τ)`; measure the last full steady-state period.

**Byte-match is proven, not assumed:** `test_yield_fork_discriminators.py::test_backward_euler_bit_identical_to_engine` drives a live `K4Lattice3D(use_memristive_saturation=True)` at one site and asserts its `S_field` equals the driver's `be_step` iteration to `rel=1e-12` using the engine's own `dt, tau_relax`. Engine byte-UNTOUCHED.

---

## 3. Leg A — thixotropy amplitude-dependent-τ

**Question (prereg §1):** does `τ_relax(A)` carry a `sign(dA/dt)` memory (true two-τ thixotropy → rectifies → a genuine directional loop) or is it an instantaneous even `τ(A)` (time-symmetric → no rectification)? **A ⇔** non-zero net area *with H conserved* (reactive rectifier); **B ⇔** no sign-memory OR the area is dissipative (loss, not H-conserving thrust).

**Three arms, one symmetric near-yield drive** (all reach Regime III: `max_r=1.000`; all finite):

| Arm | raw `R` | raw `Δτ_rel` | `W_cycle` (∮S dr) | reading |
|---|---|---|---|---|
| 1 · canonical single-τ | −0.200 | 0.540 | 0.174 | dissipative; raw asymmetry present |
| 2 · two-τ control (`τ_down=3τ_up`) | −0.539 | 1.011 | (dissipative) | **instrument LIVE** |
| 3 · even `τ(A)=τ(1+A²)` | −0.031 | 0.618 | (dissipative) | amplitude-dep alone: small `R` |

**Finding F-A1 (discovered at integrator time — Rule-10 empirical-driver discipline).** The frozen A.4 raw observables `R` and `Δτ_rel` are **contaminated by nonlinear loop-shape asymmetry** at the strongly-nonlinear registered point (`r→1`). Proof: the single-τ raw `R` **scales with drive amplitude and vanishes as Δr→0** — `R(Δr=0.30)=−0.200 → R(Δr=0.02)=−0.009 → R(Δr=0.01)=−0.005`. A single-τ model has **zero** sign-memory by construction, so this residual `R` is a memoryless nonlinear-loop artifact, not memory. The frozen classifier therefore sub-labels arm 1 "B-anelastic" — an artifact of the contaminated raw observable (disclosed; the verdict-CLASS is robust, below).

**The CLEAN referenced discriminator (τ-swap sign-flip) — the airtight isolation of genuine memory:**
- `R_mem ≡ R(model) − R(single-τ baseline)`. Single-τ baseline `R=−0.200` is the memoryless midpoint.
- two-τ **down-slow** (`τ_down=3τ_up`): `R_mem = −0.339`.
- two-τ **up-slow** (`τ_up=3τ_down`): `R_mem = +0.379`.
- **They FLIP SIGN under the swap** → genuine `sign(dr/dt)` memory. Single-τ: `R_mem = 0` → **no genuine sign-memory**.

**Verdict A = B (robust, via the H-gate — NOT contaminated):** bin A requires `W_cycle ≤ tol` (H-conserved). The canonical loop is **dissipative**, `W_cycle = 0.174 ≫ tol = 0.0035` → **excluded from A regardless of any memory estimate**. Combined with the clean result (`R_mem = 0`, no swap-flip → no genuine memory), the canonical kernel **does not rectify a symmetric drive** → the rectification-thrust door is **closed by derivation** (upgrades the prereg's dead-by-default to dead-by-proof on the sign-memory axis). The two-τ positive control fires, so the null is real, not a dead instrument — **but the *gate* that certifies "instrument live" is vacuous as coded; see F-A2.**

**Finding F-A2 — the frozen Leg-A liveness gate is VACUOUS as coded (disclosed 2026-07-19, R-4). The B verdict stands on the clean τ-swap discriminator, NOT on this gate.**
- **The liveness gate cannot fail.** As coded, `instrument_live ≡ (Δτ_rel > 1e-3) AND (|R| > 1e-3)` (`leg_a_thixotropy.py:151`). But the **memoryless** single-τ arm already gives `Δτ_rel = 0.54` and `|R| = 0.20` — both ~500× the `1e-3` threshold, and (F-A1) both are nonlinear-loop *artifacts* with **zero** sign-memory. So a genuinely **dead** (memoryless) instrument would still pass "live." The thresholds sit ~500× *below* the proven F-A1 artifact background → the gate certifies nothing.
- **The frozen `Δτ_rel ≈ 2` outcome was neither met nor its fail-path reachable.** A.6 froze the two-τ control's required outcome as `Δτ_rel ≈ 2` (`τ_up=τ`, `τ_down=3τ` ⇒ `Δτ = 2`). But the code renormalizes to the **geometric mean** — `τ_up = τ/√3`, `τ_down = τ√3` (`yield_fork_kernel.py:43`, "to keep the loop in the same `ωτ` band") — so the reachable ideal is `√3 − 1/√3 = 1.155`, **not 2**; measured `1.011`. The geometric-mean choice **made the frozen `≈2` criterion structurally unreachable**, and there is no fail-path (the gate is satisfied by the artifact background anyway).
- **Why the verdict still stands.** The honest liveness evidence is the **clean τ-swap discriminator** (§3 above): `R_mem` **flips sign** under the swap (`−0.339` down-slow vs `+0.379` up-slow) for the two-τ model and is `0` for single-τ. *That* is the fireable discriminator — it distinguishes genuine sign-memory (flips) from memoryless artifact (does not), and it is what actually carries the B verdict. The vacuous liveness gate is redundant to it.
- **Gate-hardening is SPEC'd, NOT retro-applied (Rule-11).** A re-run should replace the liveness gate with a **fireable** one: certify "live" only if the two-τ `R_mem` **flips sign** and exceeds a threshold set *above* the single-τ artifact background (e.g. `|R_mem| > 5×|R_single-τ,Δr→0|`), i.e. a gate that a memoryless input **fails**. This is not applied to the frozen verdict here (which is not retro-edited).

**Structural corollary (ties Leg A to the fork):** every first-order relaxation (single- **or** two-τ) is dissipative (`W>0`), so **bin A is structurally unreachable within the first-order framework**. A *reactive* (H-conserving) rectifier requires the **second-order reactive `S`-structure = `#59` Flag F = the lossless branch of the fork.** Leg A thus kills the *two-τ thixotropic* version of the dissipative branch and points the only surviving route to A at Flag F.

---

## 4. Leg B — memristor loop-area (`P_phase5_memristor_loop_area`)

**Prediction (`tau-relax-derivation.md:109`, `#59` §6/§11):** loop area `= ℓ_node²·m_e c²·f(ωτ)`, `f` a K4-nonlinear-corrected Debye shape **peaking at `ωτ≈0.9`**, falsification window **`[0.85,0.95]`**.

**Integrator floor (frozen §6):** both analytic-zero limits give `ε_qs = ε_fr = 3.53×10⁻⁴`; `tol = 10·max = 3.53×10⁻³`.

**Measured (60-pt `ωτ`-sweep + fine-grid peak refit):**

| Quantity | (r,S) plane [frozen-primary — but *information-free*, see F-B1] | (V,I) Lissajous [the *testable* plane] |
|---|---|---|
| peak `ωτ` (Δr=0.30) | **1.001** (pinned at linear Debye) | **0.911 — INSIDE `[0.85,0.95]`** |
| peak `ωτ` (Δr=0.25, sub-rupture) | 1.001 | **0.9577** (banked `peak_subrupture_VI`; the earlier `0.955` table value did not reproduce — corrected 2026-07-19, R-5 finding 10) |
| area at peak | 0.175 (`≫ tol`) | 0.086 |

**Adjudication (frozen bins):** the (r,S)-plane area is **FINITE** (`0.175 ≫ tol`) → **not** the zero-area lossless bin; but the peak `ωτ=1.001` is **OUTSIDE `[0.85,0.95]`** → does **not** match P_phase5 → **NEITHER / fail-closed**. This is the frozen-bin output and it stands (Rule-11). What it *means* evidentially is re-banked in F-B1.

**Finding F-B1 — RE-BANKED 2026-07-19 (R-1 zero-information reframe + R-2 mis-registration provenance).**

> *Superseded framing (letter-true but evidentially empty), kept for the record:* "the P_phase5 nonlinear peak-shift is falsified in its stated (r,S) plane; the (r,S) loop peaks at the linear Debye `ωτ=1.00`, outside `[0.85,0.95]`." That statement is true but carries **no evidence**, for the two reasons below.

**(R-1) The (r,S)-plane window test is INFORMATION-FREE — a priori unreachable.** The loop area `∮ S dr` of *any* first-order relaxation kernel is the **Debye dissipation shape**, whose peak is pinned at `ωτ≈1` *independent of the nonlinear `S_eq` shape*. Verified: the (r,S) peak sits at **`1.0014` across the whole drive family** (`r_0∈[0.3,0.9], Δr∈[0.05,0.5]`) — it **never** enters `[0.85,0.95]`. So the frozen (r,S)-plane window test **could not pass for any first-order-kernel parameters**: its "peak outside `[0.85,0.95]`" failure is a **theorem of the observable**, not a measurement outcome. Reading it as "P_phase5 falsified" over-reads a guaranteed-fail test.

**★The testable plane is (V,I), and it landed INSIDE the window.** The (V,I) loop-area peak *does* move with drive amplitude (`I=r√S` is a genuine nonlinear transform) and measured **`ωτ=0.911`, INSIDE `[0.85,0.95]`** at the registered `Δr=0.3` (sub-rupture `Δr=0.25`: `0.9577`, just above the upper edge). This is the datum that leans *toward* the memristive window — with the **F-B2 caveat** below (no origin-pinch at the near-yield point, so the (V,I) registration is itself imperfect here).

**(R-2) The `[0.85,0.95]` window was itself MIS-REGISTERED (BOTH-AND, not either/or).** Two independent problems, both true:
- **(a)** the registered `ωτ≈0.9` peak-shift **fails to reproduce** — the engine's (r,S) loop peaks at the linear Debye `1.001` (above).
- **(b)** the window's **`0.9` center does not follow from `#59`'s own derivation.** It was imported from **doc-48's `A²_cos` response-amplitude observable** (`#59` §6.3: "*48 §6: max A²_cos = 0.962 at ωτ=0.90*") — a **different observable** from the loop area. `#59` §6.4's own arithmetic assumes `A_2/A_1 ≈ 1/10`, but at the **registered** drive (`r_0=0.7, Δr=0.3`) `A_2/A_1 = Δr²/(4r_0²) = 0.046`, and Eq 6.3 then peaks at **`0.978`** (`0.954` even at the assumed `1/10`) — **not `0.9`**. So the registered `[0.88,0.92]`/`[0.85,0.95]` window is not what `#59`'s stated Eq 6.3 yields at the registered operating point. (Verified in-code; banked `window_test_reframe_2026_07_19_repair`.)

`#59` §6.5 Flag C already warned the two-channel form is not the full nonlinear solution. Net: neither (a) nor (b) is evidence against the memristive branch — one is a guaranteed-fail plane, the other a mis-registered target. The one *live* comparison (the (V,I) plane) leans *toward* the window.

**Finding F-B2 — the (V,I) "pinched hysteresis" registration does not apply at the near-yield point.** `nonlinear-vacuum-capacitance.md:66` registers a Lissajous that "passes through the origin." At `r_0=0.7, Δr=0.3` the drive `r∈[0.4,1.0]` **never crosses `r=0`**, so `min|I|=0.354 ≠ 0` → the loop is **offset, not origin-pinched**. The origin-pinch is a property of a full-swing drive, not the small-amplitude near-yield drive `#59` registered; the (r,S) plane is the appropriate one here (and it is the plane the prediction is stated in, `tau-relax:24`).

**Finding F-B3 (the H-ledger throughline) — CORRECTED 2026-07-19 (R-3).** The loop area is a **rate-dependent Debye lag**: it → 0 in **both** the quasi-static (`ωτ→0`) and frozen (`ωτ→∞`) limits (`3.53×10⁻⁴` each vs `0.175` at peak). A rate-dependent lag is produced by a reactive element too; **the finite `∮` alone does not require a resistor.** Its *dissipative* reading is inherited from the **first-order overdamped** model structure (Eq 2.1), which `#59` §12 **Flag F** flags as *asserted, not derived*.

> **RETRACTED (Rule-12):** an earlier version of this finding stated "*a second-order kinetic-`S` form (`I_S≠0`) gives the **same** `τ`-lag but conserves H (lossless)*." **That is FALSE** and is withdrawn. A lossless (undamped) second-order kinetic-`S` system is **resonant** — it has a resonance peak and a 180° phase inversion through resonance, **not** the monotonic Debye lag. It does *not* reproduce the same loop. The Flag-F relocation does **not** rest on any lag-equivalence.

**What the relocation actually rests on (the model-tautology leg — the surviving leg).** This driver **integrates the first-order Eq 2.1 on itself** (PROTOCOL-COMPLETION §8: "*this leg RUNS Eq 2.1 as frozen*"). It can therefore **only ever report first-order-overdamped behavior** — it structurally *cannot* tell whether the substrate's true near-yield `S`-dynamics are first-order (dissipative) or second-order kinetic-`S` (`I_S≠0`, potentially lossless), because it *assumes* the first-order form as input. So the frozen bin's identity "finite `∮` = dissipative" is exactly the assumption the fork questions, and this measurement **cannot** independently establish dissipation. Which dynamics hold is `#59` Flag F — a **derivation** question upstream of any run of this driver.

> **Disclosure (undisclosed deviation, R-3).** PROTOCOL-COMPLETION §8 promised the RESULT would report "*a clearly-labeled reactive second-order contrast*." **That contrast never ran** — the driver contains no second-order kinetic-`S` integration. It is **SPEC'd** as part of the Flag-F derivation branch (§6): integrate `d²S/dt² + γ dS/dt + ω_S²(S − S_eq) = 0` in the undamped (`γ=0`) lossless limit on the identical drive, compare its loop shape and H-ledger against the first-order Eq 2.1. This is what would make the first-vs-second-order distinction empirically crisp; a driver that only runs Eq 2.1 cannot.

---

## 5. Capability finding (experiments-fully-lattice-derived rule)

`#59` §10 and `tau-relax-derivation.md:117` state the dynamic Level-2 `S(t)` relaxation-ODE was **UNBUILT** ("flagged for future engine work"). **This is now stale:** the engine implements it via `use_memristive_saturation=True` (`k4_tlm.py:266–296`, backward Euler at `:291`), added since `#59` was written. So Leg B did **not** require an engine change — the drivers reproduce the engine's own memristive update (byte-match test) with the engine byte-untouched. **No CANNOT-RUN-AS-FROZEN was needed; no silent approximation was made.** (Routed as a doc-staleness flag for the auditor lane: `tau-relax-derivation.md:117` and `#59` §10/§28 should note the capability now exists; I surface it, the auditor lands it.)

---

## 6. FORK ADJUDICATION — routed to Grant (NOT closed here)

Per the KEEP-BOTH fork record (`2026-07-17` §5): the substrate decides via the registered discriminators; the ruling stays Grant's. Both discriminators ran (with the gate- and plane-level caveats disclosed in §3–§4: F-A2 vacuous liveness gate, F-B1 information-free adjudication plane). What each outcome means for the fork:

- **Leg A (B):** the canonical kernel has **no genuine `sign(dr/dt)` memory** and is dissipative → the **two-τ thixotropic (fast-liquefy/slow-refreeze)** version of the dissipative branch is **closed by derivation.** This does *not* settle dissipative-vs-reversible for the *symmetric* single-τ loop (a symmetric loop can be either); it kills only the directional/thixotropic sub-branch and shows the only route to a *reactive* rectifier (bin A) is the **second-order reactive structure = Flag F = your lossless branch.**
- **Leg B (NEITHER — frozen bin; evidential weight re-banked, F-B1):** the loop is **finite** (argues against a *strict* zero-area reading at the (r,S)-area level). The frozen NEITHER comes from the **(r,S) plane**, but that window test is **information-free** — the (r,S) loop-area peak is pinned at the linear Debye `≈1.00` for *any* first-order kernel, so `[0.85,0.95]` is a-priori unreachable there and the "falsified" reading is a **theorem of the observable**, not evidence (R-1). The **testable (V,I) plane** peaks at **`0.911`, INSIDE `[0.85,0.95]`** — the one datum leaning *toward* the memristive window (F-B2 caveat: no origin-pinch). The registered `0.9` target was itself **mis-registered** (imported from doc-48's `A²_cos`, and not what `#59`'s own Eq 6.3 yields at the registered drive: `~0.954–0.978`) (R-2). So the memristive prediction is **neither cleanly confirmed nor cleanly falsified** by these drivers. And (F-B3, corrected) the finite area's *dissipative* character is **assumed by the model this driver runs**, not measured — so a finite `∮` does not by itself falsify your reversible lean.

**Net for the fork.** Neither discriminator adjudicates against your reversible-reactive lean. They **converge on relocating the crux to `#59` Flag F**: *is the near-yield `S`-dynamics first-order overdamped (dissipative) or second-order reactive (`I_S≠0`, lossless)?* That is a **derivation** question — deriving the overdamped limit rigorously from a K4 Lagrangian with a kinetic term in `S` (Flag F / Flag A), showing whether `I_S→0` is forced. Until that is done, the memristive-loop object stays **LOSS-REQUIRED by its own prose but NOT axiom-forced** (exactly the `2026-07-17` §5 status). **Fork stays OPEN.** Recommended next step (yours to call): a Flag-F derivation branch, not another driver — the drivers have said what they can.

**Adjudication criteria were NOT dropped to convert a verdict (Rule-11):** Leg A's literal frozen classifier output (arm-1 "B-anelastic") is preserved in the sidecar; the robust verdict-class (B, not-A) is reached via the un-contaminated H-gate, with the contamination disclosed as F-A1. Leg B's NEITHER is the literal frozen bin.

---

## 7. Gates, deviations, status

**Gates:** regime gate (drive reaches Regime III, `max_r=1.00`) — *fires*; finite gate (all swept points finite; no blow-up) — *fires*; byte-match gate (driver kernel bit-identical to engine, `rel<1e-12`) — *fires, the load-bearing gate*; symmetric-drive gate — **evaluated by construction, not asserted**: the drive `r(t)=r_0+Δr·sin(ωt)` is a pure symmetric sine by definition, so this "gate" cannot fail (the measured half-cycle mirror residual `≈3.7×10⁻³` is a settle-phase discretization artifact, *reported* but not itself a fail-threshold); positive-control gate — **VACUOUS as coded, see F-A2** (cannot fail; the real liveness evidence is the τ-swap sign-flip).

**Deviations disclosed:**
1. Leg B protocol is a **standalone frozen doc**, not a bottom-append (the `P_phase5` prediction lives in a claim-hosting KB leaf, not an editable prereg — auditor-lane/Rule-12). Disclosed in that doc §0.
2. **F-A1** frozen raw observables contaminated by nonlinear loop-shape → clean referenced τ-swap discriminator supplied; verdict-class robust via H-gate. Frozen output preserved.
3. **F-A2 (R-4)** the Leg-A positive-control liveness gate is **vacuous as coded** (thresholds ~500× below the F-A1 artifact background → cannot fail); the frozen `Δτ_rel≈2` outcome was neither met (`1.011`) nor its fail-path reachable (geometric-mean τ renormalization capped the reachable ideal at `1.155`). Verdict stands on the clean τ-swap sign-flip; a fireable gate is SPEC'd (not retro-applied).
4. **F-B1 (R-1/R-2)** the (r,S)-plane window test is **information-free** (peak pinned at linear Debye `≈1.00` for any first-order kernel → `[0.85,0.95]` a-priori unreachable in that plane); the testable **(V,I) plane peaks at `0.911`, INSIDE the window**; and the `0.9` window target was **mis-registered** (imported from doc-48's `A²_cos`; not `#59` Eq 6.3's own `~0.954–0.978` at the registered drive). NEITHER stands as the frozen bin, but with no evidential weight against memristive.
5. **F-B2** origin-pinch absent at the near-yield operating point (drive `r∈[0.4,1.0]` never crosses 0; `min|I|=0.354≠0`).
6. **F-B3 (R-3, CORRECTED)** finite `∮` is a rate-dependent Debye lag; its dissipative reading is **assumed by the first-order model this driver integrates on itself** (PROTOCOL §8), not measured. The earlier "a second-order form gives the *same* τ-lag" claim is **RETRACTED as FALSE** (Rule-12). The PROTOCOL §8-promised **second-order reactive contrast never ran** — SPEC'd for the Flag-F branch.
7. **Peak-fit method deviation (R-5 finding 3):** the peak `ωτ*` is located by coarse argmax + a **fine-grid linear sub-grid re-fit** (`leg_b_loop_area.py:58`); an earlier **parabolic-in-log** refit overshot on the very flat top and was replaced (discovered at run time). Verdict-invariant.
8. **`peak_subrupture_VI` table cell (R-5 finding 10):** the result table originally quoted `0.955` for the (V,I) sub-rupture peak; it did **not reproduce** — the banked value is `0.9577` (now computed and stored, `leg_b_loop_area.py`). Corrected.
9. Leg A driver is **0D** (temporal kernel); spatial self-steepening is out-of-scope **by the prereg's own §4/§7 reversibility guard** (it is not the rectifier). Disclosed in amendment §A.8.
10. Capability staleness: `tau-relax-derivation.md:117` / `#59` §10 "unbuilt" is stale (§5).

**Status tags:**
- **DERIVED:** Leg A no-sign-memory → B (H-gate + τ-swap flip); bin-A-requires-Flag-F corollary.
- **VERIFIED:** engine byte-match (`rel<1e-12`) — **the genuine independent check** (the engine computes `S` via its own code path, byte-identical to the driver); zero-limits below `0.01×`peak; amplitude-scaling of the artifact. **NOTE (R-5 finding 9):** the "shoelace re-derivation of `∮`" (`test_loop_area_independent_shoelace_matches_driver`) uses the **same trapezoid formula** as `loop_area_rS` — it is a **consistency re-computation, not an independent method**; the independent check is the byte-match, not the shoelace. `make verify` PASS; `ruff` clean; 13/13 tests pass (routed to `make test-engine`).
- **BLOCKED / OPEN (routed to Grant):** the fork itself — resolvable only by a **Flag-F derivation** (first-order overdamped vs second-order reactive `S`-dynamics), not by a driver.

*Run 2026-07-19 by Opus 4.8 (implementer lane) per Grant's yield-fork discriminator dispatch. Frozen protocols governed; deviations recorded as findings; the fork ruling stays Grant's.*

*Repaired 2026-07-19 (implementer lane) per review `wf_f0870d0d` (11 confirmed / 1 refuted; CRITICAL→MAJOR): the fork-open disposition and the Flag-F relocation SURVIVE (via the model-tautology leg only). Evidential framing re-banked — R-1 (the (r,S)-plane window test is information-free; the (V,I) plane's `0.911` surfaced), R-2 (both-and mis-registration provenance), R-3 (the "same τ-lag" leg retracted via Rule-12; second-order contrast disclosed-as-unrun + SPEC'd), R-4 (Leg-A liveness gate vacuity disclosed; verdict stands on the τ-swap), R-5 (peak-fit deviation, symmetric-drive relabel, "independent" softened, `0.955→0.9577`, "(verbatim)" corrected in the PROTOCOL-COMPLETION). Frozen verdicts (Leg A = B, Leg B = NEITHER) not retro-edited (Rule-11).*
