# BEMF-feedback SMOKE — the inductive reaction-half COUPLES (correctly-signed) but is SUB-THRESHOLD (RESULT)

**Date:** 2026-06-10 · **Branch:** `analysis/2026-06-10-bemf-feedback-smoke` (off `analysis/2026-06-10-graft-v4-photon-helicity`) · **Lane:** implementer
**Prereg (FROZEN):** [`2026-06-10_bemf-feedback-smoke_prereg.md`](2026-06-10_bemf-feedback-smoke_prereg.md)
**Engine:** [`src/ave/core/crystal_graft_bemf.py`](../src/ave/core/crystal_graft_bemf.py) · **Driver:** [`src/scripts/vol_1_foundations/bemf_feedback_smoke_run.py`](../src/scripts/vol_1_foundations/bemf_feedback_smoke_run.py) · **Figures:** `bemf_feedback_fig{1,2,3}_*.png` · **Data:** `bemf_feedback_results.json`
**Config:** N=72, lock_eta=0.05 (v4) / 0 (secondary), κ_L=±{0.3,0.6,1.2,2.4}, n_steps=1200, |L_ω| checkpoints (300,600,1200), STOP gate ≤1.3.

## 🔴 VERDICT ADDENDUM — 2026-06-10 panel record-honesty pass (Rule 12: body PRESERVED, this header SUPERSEDES)

> **Rule 12 walk-back (substitution-not-retraction): the doc body below (from `## VERDICT — INERT` onward) is PRESERVED UNCHANGED; this dated header SUPERSEDES it wherever they conflict.** The verdict STANDS — **INERT, panel-confirmed (`survives_adversarial = true`)** — but the body over-claims at three points and must carry the six corrections below. Every number re-verified against `bemf_feedback_results.json` (the fig source series) and the prereg. The slot is NOT refilled (no new hypothesis); the named residual — the missing primitive is **SOURCE DEPLETION, NOT REACTION** (§8) — is the boundary.

**Headline (restated, panel-confirmed):** the derived Lenz reaction-half (`κ_L = κ̃ = 6/5 = pq/(p+q)`, p=2 q=3 — **DERIVED, not tuned**: `crystal_graft_bemf` config) couples with the **correct sign** but **never bounds** (the 1.3 gate is missed by **≈3.4× or more at every swept gain ±{0.3,0.6,1.2,2.4}**: worst case κ_L=−2.4 ratio 4.394 → **3.38×**; Lenz-side min +1.2 ratio 4.729 → 3.64×) and **never pays** (emf/drive plateaus **5.3–8.0%**; drive≈BEMF cannot form while the drive is photon-refilled — E_V grows **+19.6% OFF / +38.0% Lenz / +8.5% anti**, every arm). **The missing primitive is SOURCE DEPLETION, not reaction** — convergent with the v4 graft's named gap ("a non-depleting chiral director that never pays for its torque").

**(a) RETRACTION — §6's "the same in all arms ⇒ undepleting-photon pump, NOT a BEMF artifact (the BEMF adds/removes no net energy)" is SUPERSEDED by a measured SIGN-CORRELATED spread.** The full-system stencil drift `H_total = E_V + E_ω + H_couple + E_w` (series first→last) is **OFF +27.294% / Lenz +26.789% / anti +29.164%** — NOT arm-independent. `E_w` (the photon shear sector) is **bit-identical across all three arms** (`56.27311354070744 → 56.35113406521613`, exact float equality) — so the spread is **not** in the photon pump; it is pinned on the BEMF-steered **indefinite** `H_couple`, whose end values diverge **+5.79 (OFF) / −4.72 (Lenz) / +10.27 (anti)**. The Lenz arm drifts ~**0.5pp BELOW OFF** (27.294 → 26.789, gap **+0.505pp**) — the engine's own damper-in-disguise gate signature at small amplitude. **Attribution between small-net-work and pump-steering is UNRESOLVED** — carried forward, never cited as settled.

**(b) DEMOTION — the header word "CONSERVATIVE" → "reactive at proxy level".** The ledger closure `|work_V + work_ω|` is the **discrete-IBP stencil identity** (antisymmetric `_curl` stencil + matched pre-leapfrog velocities in `_bemf_forces`/`bemf_ledger`), **NOT evolved-energy neutrality**. Measured: primary Lenz `|imb|=2.70e-8` (rel 1.04e-8), primary anti `|imb|=1.38e-7` (rel 1.59e-7), secondary anti `|imb|=1.56e-7` (rel 1.81e-7) — i.e. the closure floor is **≤1.4e-7 (abs, primary worst case)**, normalized reaching ~1.6–1.8e-7 on the anti arms — **NOT 9e-8**. **Do NOT upgrade this 9e-8/1e-7-class closure to a conservation proof downstream.**
  - FLAG (`verify-before-cite`): the body **§4 "imbalance (rel)" column `9.3e-8` (Lenz) / `4.9e-8` (anti) does NOT reproduce** from the shipped JSON (which gives abs 2.70e-8 / 1.38e-7, rel 1.04e-8 / 1.59e-7). The §4 figures are stale/erroneous; **this addendum's numbers govern**. §4 body left intact per Rule 12.

**(c) PREDICTION FAILURE recorded — the §6 / prereg sign-probe payment-DIRECTION prediction is FALSIFIED.** Prereg (lines 64, 76) + §6 predicted **+κ_L ⇒ work_V < 0** (the source-depletes / payment direction). Measured: **`work_V` ends +2.598 (POSITIVE)**, wandering **−2.465 … +3.049** over the window — there is no net source→circulation payment direction. The "+κ_L = Lenz" label survives **only on the |L_ω|-attenuation axis** (primary Lenz **4.729** < OFF **5.035** < anti **5.950**; secondary **2.890** < **3.686** < **4.881**), **NOT on the payment-direction axis.**

**(d) LANGUAGE HYGIENE — the anti-Lenz control PASSED as RATIO AMPLIFICATION, NOT detonation.** Anti raises `ratio_4L` above OFF (**5.950 > 5.035**) — the falsifiable control firing on the |L_ω| axis. But `max|ω|` is **marginal**: anti **0.0532** vs OFF **0.0525** (and Lenz is actually the highest at **0.0581**). State this explicitly so "ANTI-LENZ PASSES" cannot be read as a **measured detonation** — there is no blow-up anywhere in the sweep below κ_L=2.4.

**(e) HEADLINE VERDICT LINE — INERT, panel-confirmed (`survives_adversarial = true`).** See "Headline (restated)" above: correctly-signed, derived, never bounds (gate missed ≥~3.4× at every swept gain), never pays (emf/drive 5–8%, E_V grows in all arms). **The missing primitive is source depletion, not reaction** (convergent with the v4 graft's named gap).

**(f) SURFACED TO GRANT — two OPEN adjudications (NOT resolved here):**
  1. **Energy-weighted-gate question:** `|L_ω|` (the saturation gate) carries only **~1e-8 of H_total** — the gate quantity is **energetically negligible**, so a reactive feedback steering it cannot bound the total energy. Is the load-bearing gate an *energy-weighted* one rather than the rigid-rotation `|L_ω|`? **OPEN** (order-of-magnitude observation, not a settled headline).
  2. **Named-loop question:** the literal `τ_zx` Fork-A observer arm vs the built cross-sector conjugate pair — `corr(bemf_emf, τ_zx) = +0.117` (Lenz) / +0.030 (anti), **weak**. Which is the load-bearing loop (the V-only meter or the cross-sector dynamical pair)? **OPEN.**

## VERDICT — **INERT** (on both targets) — qualified: the reaction-half is REAL, CONSERVATIVE, and CORRECTLY-SIGNED, but SUB-THRESHOLD

> The inductive back-EMF reaction-half (`f_V^BEMF=−κ_L g[w·(∇×π_ω)]`, `f_ω^BEMF=+κ_L∇×(g π_V w)`, derived from the single Lagrangian `L_BEMF=κ_L∫g[w·(∇×ω)]V̇` — the velocity-sector mirror of the v4 buckle) is wired into the EOM and **does couple, with the physically-correct Lenz sign** (the anti-Lenz control fires: §3). But it **does NOT saturate** the |L_ω| runaway at the derived gain OR across the ±κ_L sweep, and the **PAYMENT signature does NOT emerge**. On the two targets that define success (bound + pay) the feedback is inert; the strong sign-asymmetry confirms it is **sub-threshold, NOT decoupled**.

**Why this is reported as INERT and not one of the other bins (Rule 11 — applied to the data):** the frozen bins were built around "bounds + pays." The result bounds nothing (ratio wanders 4.39–5.95 across the whole sweep, never approaching the 1.3 gate) and pays nothing (no drive≈BEMF; the back-EMF stays ≈5–8% of the drive). It does **not** detonate under the Lenz sign (max|ω| bounded 0.05–0.09). The prereg's INERT definition ("sign-flip does nothing") is **partially violated** — sign-flip DOES change the ratio (4.73↔5.95) and the energy distribution — so this is recorded as **target-inert (sub-threshold)**, the honest 5th outcome the four bins do not cleanly capture; it is NOT force-fit, and the correctly-signed coupling is a real (if under-powered) positive for the mechanism.

## §1 — The headline saturation gate (no arm, no gain, saturates)

| panel | arm | κ_L | |L_ω|_max [300,600,1200] | ratio_4L | gate ≤1.3 | max|ω| |
|---|---|---|---|---|---|---|
| PRIMARY (lock η=0.05) | OFF | 0 | [0.432, 0.432, 2.177] | **5.035** | ❌ | 0.0525 |
| | BEMF +κ_L (Lenz) | +1.2 | [0.549, 0.549, 2.594] | **4.729** | ❌ | 0.0581 |
| | BEMF −κ_L (anti) | −1.2 | [0.416, 0.476, 2.474] | **5.950** | ❌ | 0.0532 |
| SECONDARY (lock OFF) | OFF | 0 | [2.688, 4.640, 9.909] | **3.686** | ❌ | 0.0525 |
| | BEMF +κ_L (Lenz) | +1.2 | [3.268, 6.173, 9.446] | **2.890** | ❌ | 0.0581 |
| | BEMF −κ_L (anti) | −1.2 | [2.541, 3.011, 12.404] | **4.881** | ❌ | 0.0532 |

- **OFF reproduces the v4 baseline EXACTLY:** lock-ON `5.035` (v4 RH_frozen_lockON `5.03`), lock-OFF `3.686` (v4 `3.69`). The unified single-trajectory method is bit-exact (deterministic FDTD, no RNG). Control (c) PASSES: feedback-OFF reproduces the v4-class runaway.
- The runaway is a **late-time EXCURSION** (Fig 1: |L_ω| flat-then-climbs at t≳5, the photon's wall-interaction timescale), not a steady rotation — the same character the v4 result named.

## §2 — Gain-robustness sweep (lock η=0.05): NO gain bounds; the verdict is gain-robust

| κ_L | −2.4 | −1.2 | −0.6 | −0.3 | **0** | +0.3 | +0.6 | +1.2 | +2.4 |
|---|---|---|---|---|---|---|---|---|---|
| ratio_4L | 4.394 | 5.950 | 5.463 | 5.238 | **5.035** | 4.858 | 4.749 | **4.729** | 4.942 |
| max|ω| | 0.050 | 0.053 | 0.054 | 0.053 | 0.053 | 0.051 | 0.049 | 0.058 | **0.091** |

- **Lenz side (+κ_L):** monotonic weak attenuation `5.035→4.749` (best ≈ κ_L 0.6–1.2, a mere **~6%** reduction), then turns **back UP** at +2.4 (`4.942`, max|ω| nearly doubles to 0.091 — heading toward instability). **There is no gain at which the ratio approaches 1.3.** The DERIVED gain κ_L=κ̃=6/5 sits near the optimal-attenuation point — yet it still fails by ~3.6×.
- **Anti-Lenz side (−κ_L):** monotonic **amplification** `5.035→5.950` (worse, the falsifiable control) through −1.2, then non-monotonic at −2.4.
- **GAIN STATUS:** the gain is **DERIVED** (κ_L=κ̃=6/5, the inductive half of the same coupling) AND the **non-bounding verdict is gain-robust** (true across ±{0.3..2.4}). No tuning could rescue it — there is no bounding gain to tune to.

## §3 — The controls (the falsifiable anti-Lenz control PASSES — the feedback couples, correctly-signed)

- **feedback-OFF reproduces the v4 runaway:** ✅ (5.035 lock-ON / 3.686 lock-OFF, bit-exact).
- **ANTI-LENZ detonates faster:** ✅ (the falsifiable control). `−κ_L` raises the ratio above OFF in BOTH panels: lock-ON `5.950 > 5.035`, lock-OFF `4.881 > 3.686`; and `+κ_L` lowers it (`4.729 < 5.035`, `2.890 < 3.686`). Sign-flip is **decisive** (lock-OFF spread 2.890 ↔ 4.881, a factor 1.69). So the BEMF is **NOT inert in the "sign does nothing" sense** — it is wired and correctly-signed (Lenz attenuates circulation buildup, anti-Lenz feeds it). It is **inert on the saturation/payment TARGETS** because it is far too weak to bound.
- Energy redistribution confirms the sign physics: `+κ_L` (Lenz) keeps energy in the source (E_V +38.0%) and OUT of the circulation (E_ω end 13.07); `−κ_L` (anti) drains the source (E_V +8.5%) into the circulation (E_ω end 18.35, higher L_ω ratio).

## §4 — The PAYMENT ledger (does NOT close as Grant's locked-motor unification requires)

| arm | work_V end | work_ω end | imbalance (rel) | bemf_emf/drive (end) | work_V wanders both signs? |
|---|---|---|---|---|---|
| +κ_L (Lenz) | +2.598 | −2.598 | **9.3e-8** | **0.054** | YES (−2.465 … +3.049) |
| −κ_L (anti) | +0.864 | −0.864 | **4.9e-8** | **0.080** | no (0 … +5.633) |

- **The BEMF is genuinely REACTIVE (no net work):** `work_V = −work_ω` to **rel 9e-8** (machine precision) — the conjugate pair (derived in the prereg §3) cancels EXACTLY. This is the strongest positive: the reaction-half is **conservative, not a damper** (a damper would drift the stencil ledger down). **Ledger-closure floor ≈ 9e-8 — WAY above the ±6.5%-class instrument floor.**
- **But there is NO drive≈BEMF balance:** the back-EMF stays at **5–8% of the drive** and never grows to cancel it (Fig 2). The reactive transfer **wanders both signs** (+κ_L: work_V swings −2.465→+3.049) — there is **no robust source→circulation payment direction**. Grant's payment signature (*source-delivered power falls as BEMF rises; steady-state drive≈BEMF; source-side reservoir depletes by what the circulation gains*) **does NOT emerge**.
- **The deep reason (the load-bearing mechanism, `ave-conserved-vs-pumped`):** the engine's ultimate source — the photon `w` — is **UNDEPLETING** (`photon_deplete=False`, the ONLY stable v4 setting; `photon_deplete=True` is the indefinite-Hamiltonian DETONATION). With an **infinite source there is no reservoir to deplete**: E_V *grows* +20–38% in every arm (the photon pump), so "source-side reservoir depletes" **cannot manifest by construction**. A purely *reactive* (no-net-work) back-EMF redistributes energy but cannot bound a photon-driven secular excursion, and cannot pay because there is nothing to spend. **This is exactly the v4 named gap, unmoved: "a non-depleting chiral director that never pays for its torque." The BEMF reaction-half does NOT close it — because the non-depletion is structural, not a missing back-reaction.**

## §5 — Observer vs dynamics reconciliation (τ_zx is the meter, the functional derivative is the dynamics)

`corr(bemf_emf, tau_zx_proxy)` = **+0.117** (+κ_L) / **+0.030** (−κ_L) — **weak** positive. The `DarkWakeObserver`-class τ_zx ∝ Z_local·∂|V|²/∂x (V-sector-only meter, here `tau_zx_proxy()`, end value ≈ 3.84) and the dynamical `bemf_emf = ‖f_V^BEMF‖ = κ_L‖g[w·(∇×π_ω)]‖` (cross-sector reaction, end ≈ 0.42) are **distinct objects**: they share some V-sector structure (hence the small positive correlation) but the dynamical reaction carries the **ω-circulation-rate** information the V-only observer cannot see. **Confirmed as prereg §3 stated: the functional-derivative form IS the dynamics; τ_zx IS the meter** — they are NOT interchangeable, and feeding the observer's τ_zx back (the literal "OBSERVED-NOT-FED-BACK" loop closure) would feed the wrong, V-only object.

## §6 — Apparatus floors (`ave-apparatus-floor-attribution`)

- **Ledger-closure floor:** `|work_V+work_ω|/|work_ω|` ≈ **9e-8** (machine; the conjugate pair cancels). The reactive ledger closes ~6 orders of magnitude above the ±6.5% instrument floor — the "no-net-work" claim is solid.
- **|L_ω| ratio floor:** OFF is bit-exact reproducible (deterministic); κ_L→0 continuity holds (the sweep is smooth through OFF). The 1.3 gate is saturation-across-doublings, NOT a secular-blind bound — and is missed by ≥3.4× in every arm.
- **Stencil H_total drift:** +27.3% (OFF) / +26.8% (+κ_L) / +29.2% (−κ_L) — **the same in all arms** ⇒ it is the **undepleting-photon pump, NOT a BEMF artifact** (the BEMF adds/removes no net energy, consistent with the 9e-8 reactive-ledger closure). Not a damper-in-disguise (no downward drift), not a BEMF detonation (no blow-up).
- **Detonation gate:** max|ω| bounded 0.049–0.091 across the whole sweep; only +2.4 shows a rise (0.091) — a warning that high reactive gain perturbs the dynamics, not a detonation.

## §7 — Honest closure (Rule 11 / substitution-not-retraction)

The BEMF reaction-half is the **physically-correct object** Grant's locked-motor unification calls for — a conservative, conjugate-pair, correctly-signed inductive back-EMF (the L-half of the buckle's C-half; reactive to machine precision). It is **NOT an ad-hoc damper** (unlike the v4 lock it replaces). But on the smoke's two targets it is **sub-threshold**: it neither saturates |L_ω| (at any swept gain, either sign — the verdict is gain-robust) nor pays (no drive≈BEMF). **The reason is structural and important: the engine's source (the photon) is undepleting, so a reactive back-EMF has no reservoir to deplete and cannot bound a photon-driven secular excursion.** The four frozen bins are recorded as: not PAYS-AND-BOUNDS, not BOUNDS-WITHOUT-PAYING, not DETONATES (under Lenz); closest **INERT (sub-threshold)**, with the explicit caveat that the anti-Lenz control PASSED (the term couples, correctly-signed). **No debug-toward-success:** the derived gain was set a priori (κ_L=6/5), the sweep was pre-specified, and no gain bounds — I did not move the 1.3 tolerance. **The slot is not refilled** (Rule 12): the named residual (§8) is the boundary, surfaced for Grant, not auto-pivoted.

## §8 — v5 payment-coupling spec (what v5 inherits VERBATIM)

> **v5 must make the SOURCE depletable, not just add a reactive back-EMF.** This smoke proves the inductive reaction-half (the L-half of the LC tank) is real, conservative, and correctly-signed — but it is **reactive (no net work)** and so cannot pay while the photon source is **undepleting** (`photon_deplete=False`). The payment ledger requires a **bounded, DEPLETING, helicity-transferring source coupling** (the v4 named gap, unmoved) — a coupling that lets the photon `w` lose helicity into the winding 1:1 **without** the indefinite-Hamiltonian pump that `photon_deplete=True` triggers (`H_bel −4107` detonation). The BEMF reaction-half should be **retained as the L-half** (it is correctly-signed and conservative), but **paired with a depleting drive half** so that: (i) the back-EMF can grow to drive≈BEMF (it cannot when the drive is photon-refilled at constant amplitude); (ii) the source-side reservoir (the photon helicity, NOT the bulk V) depletes by what the circulation gains. Concretely: v5 inherits `crystal_graft_bemf.py`'s `_bemf_forces()` (the derived conjugate pair, κ_L=6/5) UNCHANGED, and adds a **norm-preserving (bounded) photon→ω helicity-transfer** coupling — an orthogonal field-space rotation (à la the `crystal_engine` converter) rather than a trilinear potential — so the photon depletes WITHOUT the pump. Only then can drive≈BEMF form and |L_ω| bound. **The missing primitive is depletion, not reaction.**

**Skills fired:** `substrate-native-check` (CP9 the reaction is dynamical, the τ_zx-vs-functional-derivative is the heuristic-vs-dynamical checkpoint; CP10 frozen-wall boundary coupling); `ave-conserved-vs-pumped` (THE framing — the BEMF is reactive/no-net-work, so it neither pumps nor pays; the undepleting photon is why payment can't close); `ave-apparatus-floor-attribution` (§6 — the 9e-8 reactive-ledger floor, the photon-pump stencil drift attributed away from the BEMF); `ave-fundamental-ground-up-implementation` (the conjugate pair derived from ONE Lagrangian, verified reactive to 9e-8); `ave-driver-script-honesty` (every number from the evolved field; the work-sign-wander, the emf/drive≈5-8%, the +2.4 max|ω| rise all surfaced not buried); `ave-canonical-source` (the M_inertial≡L_drag / τ_zx canonical back-EMF chain); `verify-before-cite` (the convergence quote `fe896f12`, the v4 result numbers re-greped); `phase-space-coordinate-check` (|L_ω| and the (ω,π_ω) reactance pair are the native coordinates; the BEMF couples the velocity quadratures π_V, π_ω); `flag-don't-fix` (the undepleting-photon-blocks-payment mechanism + the target-inert-vs-frozen-bins mismatch surfaced for Grant, not reconciled away).

**Figures (data-derived captions):**
- `bemf_feedback_fig1_saturation.png` — |L_ω|(t), OFF/+κ_L/−κ_L, PRIMARY (lock-ON, ratios 5.03/4.73/5.95) + SECONDARY (lock-OFF, 3.69/2.89/4.88). All arms climb in a late-time excursion (t≳5); the BEMF arms barely separate from OFF; the anti-Lenz (red) excursion is largest. No arm flattens (the 1.3 gate is off-scale low).
- `bemf_feedback_fig2_payment.png` — E_V(t) (source, grows +20–38% in all arms = photon pump), E_ω(t), drive vs back-EMF (the BEMF curve sits at ~5–8% of drive — no drive≈BEMF crossover), and the reactive transfer work_V=−work_ω (closed to 9e-8, but wandering both signs = no robust payment).
- `bemf_feedback_fig3_gain_sweep.png` — ratio_4L vs κ_L (the 1.3 gate and the OFF=5.03 line; the curve never crosses below ~4.4) and max|ω| vs κ_L (the +2.4 rise to 0.091).
