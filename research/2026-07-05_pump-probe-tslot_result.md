# RESULT — [ADJUDICATION-INVALID — LAB-FRAME OBSERVABLE / FORK STILL OPEN]. The measured observable was lab-frame mixed; NO frozen arm is excluded or confirmed at bond-frame level. The real products are the instrument-liveness result, the kinematic-tilt characterization, and the boundary-artifact documentation — a methods result, fork OPEN.

> ## 🔴 SUPERSEDED VERDICT (2026-07-05, orchestrator review of PR #532 — 12 confirmed, 3 CRITICAL, 5 MAJOR, 0 refuted)
>
> **The live verdict is [ADJUDICATION-INVALID — LAB-FRAME OBSERVABLE / FORK STILL OPEN], NOT
> [EXCLUDES-DC_ONLY].** The original body below is PRESERVED (Rule 12) as the record of the
> invalid adjudication, with the load-bearing false claims corrected here. Rule 11: no rescue —
> the mechanism DIES, the fork stays OPEN. Summary of what the review verified (all reproduced
> this session — see §HONEST RE-ANALYSIS):
>
> 1. **CRITICAL-1 — the Jensen mechanism is FALSIFIED by my own dynamics.** ~77% of the measured
>    stiffening is an unmodeled **lab-frame KINEMATIC TILT-PROJECTION** term ⟨Φ''(A)·u_y²⟩ — the
>    probe feeling the AXIAL spring through the instantaneous bond SLOPE of the wiggling rope. A
>    **LINEAR chain** (no kernel, no concavity, no Jensen anywhere) reproduces the verdict number
>    to **2×10⁻⁶** (reproduced: 1.018048 vs 1.018046). The tangent stiffness read AT the
>    cycle-MEAN configuration is **0.9973 (COLD)** — there is NO deposited DC bias the slow probe
>    feels; the stiffening lives entirely in the cycle-averaged AC slope oscillation. **RETRACTED:**
>    the Jensen-deposited-DC mechanism, the "AC deposits DC — yes" clm-acdc07 framing, the PONDER
>    cross-link, and the #518 fallout row (Rule 12: preserved-struck below, NOT refilled).
> 2. **CRITICAL-2 — the ⟨A_bond⟩=+0.0045 "deposit" is a BOUNDARY ARTIFACT.** The drive pins
>    u[0]=0 (Dirichlet), letting the wall exert an arbitrary mean axial force. The cycle-mean
>    strain at the probe is actually **−0.0026 (pinned)** and **−0.0083 (free drive end)** — it
>    SIGN-FLIPS and is boundary-concentrated (0.0075 at node 20 → −0.0036 at node 380). **The
>    +0.0045 bulk-deposit claim is retracted.**
> 3. **RE-BIN.** The observable was lab-frame mixed while BOTH frozen arms predict BOND-FRAME slot
>    content; keying-B's [EXTENDED-CONFIRMED] flips to [NEITHER] under the probe-node sweep the doc
>    itself cited as the dominant residual; the honest band is **~0.5% (window spread 0.0049), not
>    0.30%**; the keying-A margin is band-edge under the free-end boundary. **No arm is excluded or
>    confirmed at bond-frame level. The #526 T-slot fork REMAINS OPEN.**
>
> **What is PRESERVED (KEEP-BOTH — the real products, a methods result in miniature):**
> - **Instrument liveness** — the uniform-stretch DC-bias control reads k_s+T/L = 1.078606 == the
>   merged #526 form to 6 digits. The probe DOES see a genuine BOND-FRAME static tension. (Untouched.)
> - **The kinematic-tilt characterization** — the dominant channel is real lab-frame kinematic
>   mixing, present identically in a linear chain, which NEITHER frozen arm modeled. This is the
>   thing to subtract for a future valid adjudication (§REQUIREMENTS).
> - **The boundary-artifact documentation** — both boundary configs + the strain profile.
>
> Corrected ledger split at the probe (keying A): shear ≈ −0.6 to −0.9% + bond-frame tension
> +0.45% + **kinematic tilt +1.40%** ≈ +0.87% (the tilt dominates). Keying B: shear **exactly
> 0.000000** (the keying-B deficit vs EXTENDED is longitudinal relaxation, NOT shear — Flag-3
> corrected). See §HONEST RE-ANALYSIS for the full reproduction + §REQUIREMENTS for the forward path.

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/pump-probe-tslot`
**Prereg (FROZEN):** `research/2026-07-05_pump-probe-tslot_prereg_FROZEN.md` (committed BEFORE the driver; commit order = freeze proof, 15fdee0a)
**Driver (dynamics):** `src/scripts/vol_1_foundations/pump_probe_chain.py`
**Prediction module (INDEPENDENT):** `src/scripts/vol_1_foundations/pump_probe_predictions.py`
**Tests:** `src/tests/test_pump_probe_chain.py` (20 pass: 10 gating + 10 engine_sim)
**Output:** `src/scripts/vol_1_foundations/_output/pump_probe_chain.json` (driver-regenerable; gitignored)
**Adjudicates:** the OPEN T-slot SCOPE FORK from PR #531 (`research/2026-07-05_channel-resolved-loading_result.md`).
**Grant directive (verbatim, attributed Grant 2026-07-05):** *"let the vacuum substrate lead the way..."*

---

## HONEST RE-ANALYSIS (the live result, 2026-07-05, post-review — all reproduced this session)

**Verdict: [ADJUDICATION-INVALID — LAB-FRAME OBSERVABLE / FORK STILL OPEN].** The frozen arms
(DC_ONLY, EXTENDED) both predict BOND-FRAME slot content (`k_shear_eff = k_s·S(A_shear) + T/ℓ`).
The measured tangent-stiffness observable `⟨−∂F_y/∂y⟩` is LAB-FRAME: it also feels the AXIAL
spring through the bond SLOPE, a term neither arm modeled. So the comparison was ill-posed.

**The dominant channel is kinematic, not Jensen (CRITICAL-1, reproduced):**
- A **LINEAR chain** (axial force `= k_a·(L−1)`, NO kernel, NO concavity, constant shear spring)
  gives pump ratio **1.018048** vs the nonlinear keying-B **1.018046** — agreement to **2×10⁻⁶**.
  If the effect were Jensen rectification (which requires the concave kernel), the linear chain
  would give nothing. It gives the whole thing. **The effect is a lab-frame kinematic
  tilt-projection**, present identically with no nonlinearity.
- Reading the tangent stiffness AT the cycle-MEAN configuration: **0.997355 (COLD**, in fact
  slightly below). There is **no deposited DC bias** the slow probe feels; the +0.87%/+1.80%
  lives entirely in the cycle-averaged AC slope oscillation `⟨Φ''(A)·u_y²⟩`.
- Channel decomposition at the probe (reproduced): keying A shear ≈ −0.6% + bond-frame tension
  +0.45% + **kinematic tilt +1.40%**; keying B shear **exactly 0.000000** + tension +0.44% + tilt
  +1.40% = +1.80%. **The tilt dominates (~77% of the keying-B signal).**

**The ⟨A_bond⟩ deposit is a boundary artifact (CRITICAL-2, reproduced):**
- Cycle-mean strain at the probe: **−0.002646** (pinned drive end, u[0]=0 Dirichlet) →
  **−0.008319** (free drive end). It SIGN-FLIPS and is boundary-concentrated (profile [node
  20,100,200,380] = [+0.0075, +0.0011, −0.0026, −0.0036], a 3.7× gradient toward the pin). The
  Dirichlet wall exerts an arbitrary mean axial force. **The +0.0045 bulk-deposit is retracted.**

**Honest band (RE-BIN grounds):** the pump ratio vs n_periods {160,200,240,280} = {1.0130,
1.0087, 1.0136, 1.0087}, spread **0.0049 (~0.5%)** — NOT window-converged; the honest band is
~0.5–0.66% (window non-convergence + drive-boundary + absorber systematics), not the 0.30% the
original claimed. Keying-B's EXTENDED "confirmation" (0.24% margin) is inside this honest band,
and flips to [NEITHER] under the probe-node sweep. **No arm is excluded or confirmed at
bond-frame level. The #526 T-slot fork REMAINS OPEN.**

**PC-ENERGY correction (MAJOR-d):** the original doc reported undriven drift = 4.7×10⁻⁴, but
that was measured over a TRUNCATED 6-period window. Over the FULL n_periods window the diagnostic
reads ~0.11 — however this is NOT dt-convergent (0.13 at dt=0.0025) and is present in the
Hamiltonian keying B too, so it is a **diagnostic-definition artifact**: the large-amplitude
seed + the linear ½k_s(Δy)² energy proxy for the SATURATING shear over-read the "energy." The
honest statement is that the undriven-drift diagnostic is not a clean drift measure at this seed
amplitude — the "4.7e-4" claim is retracted, and a valid arc needs a saturation-consistent
energy functional (part of §REQUIREMENTS).

**What survives (KEEP-BOTH):**
- **Instrument liveness** (untouched): the uniform-stretch DC-bias control = merged #526 form
  k_s+T/L = 1.078606 to 6 digits — the probe sees a genuine BOND-FRAME static tension.
- **The kinematic-tilt characterization** — the term to SUBTRACT for a valid adjudication.
- **The boundary-artifact documentation** — both configs + the profile.

---

## REQUIREMENTS FOR A FUTURE VALID ADJUDICATION (the forward value of this arc)

A valid engine adjudication of the #526 T-slot fork must have, all of which this arc lacked:

1. **A BOND-FRAME observable** — measure the slot content `k_s·S(A_shear) + T/ℓ` in the bond's
   own frame, NOT the lab-frame tangent stiffness (which mixes in the axial spring via the bond
   slope). The kinematic tilt term ⟨Φ''(A)·u_y²⟩ characterized here is precisely what must be
   subtracted.
2. **A genuinely DYNAMICAL probe with pump back-reaction** — the prereg-FROZEN slow weak probe
   WAVE (phase velocity through the pumped region), NOT a frozen-configuration finite-difference
   on snapshots (which omits the pump's response to the probe). See the prereg erratum.
3. **Momentum-closed or free boundaries with the ledger CLOSING** — not a Dirichlet pin that
   lets the wall inject an arbitrary mean axial force (CRITICAL-2). Report the mean-force ledger.
4. **Hamiltonian-consistent keyings only** — keying A as coded is non-Hamiltonian (Ax3-lossless
   violated in the bulk; MAJOR-b); a valid arm must derive the shear saturation from a potential.
5. **Systematics-honest bands** — window-convergence + boundary + absorber + chain-length sweeps,
   with the band ABOVE the demonstrated residual floor (the honest ~0.5–0.66% here, not 0.30%).

**Follow-on derivation candidate (NOT this scope):** on a LINEAR chain the entire effect is
kinematic — so the bond-frame slot content may be derivable ANALYTICALLY by subtracting the
now-characterized tilt term. A linear-chain analytic subtraction is a candidate shortcut to the
valid adjudication.

---

<details><summary>🔴 PRESERVED (Rule 12) — the original [EXCLUDES-DC_ONLY] body, INVALID. Read as the record of the invalid adjudication; the live corrections are above.</summary>

## VERDICT BOX

> **PRIMARY (robust, keying-INDEPENDENT): the traveling pump EXCLUDES ARM DC_ONLY.**
> Running the full nonlinear 2-DOF chain dynamics — no slot bookkeeping — a slow weak
> transverse probe reads a transverse stiffness that is **STIFFER than cold** through a
> genuinely traveling pump (SWR = 1.003), on **BOTH** modeling keyings, by margins
> (0.87%–1.80%) far above the DERIVED band (0.30%). **The DC_ONLY prediction (probe
> recovers cold, 1.000) is FALSIFIED by the dynamics.** The mechanism is honest and
> substrate-native: the concave kernel / convex bond-length rectifies a nonzero
> **second-order mean bond strain** ⟨A_bond⟩ = +0.0045 even though the field mean ⟨y⟩ = 0
> — the Jensen rectification (`claim-quality.md:263`) surfaced to Grant at prereg. A
> traveling transverse wave DOES deposit a DC bias the slow probe feels.
>
> **SECONDARY (keying-DEPENDENT — a substrate-ontology fork surfaced for Grant): does
> the pump land ON the EXTENDED prediction?**
>
> | keying (does a transverse pump strain the shear channel?) | PUMP k_trans | bin |
> |---|---|---|
> | **A — shear saturates** `k_s·S(A_shear)`, A_shear = bond angle \|Δy\|/L | **1.008730** | **[NEITHER]** (excludes DC_ONLY by 0.87% AND EXTENDED by 1.17%) |
> | **B — shear constant** `k_s`, transverse wave leaves the shear channel unstrained | **1.018046** | **[EXTENDED-CONFIRMED]** (at band edge: 0.24% below EXTENDED < 0.30% band; excludes DC_ONLY by 1.80%) |
>
> On keying A the pump partly cancels the rectified tension via shear-channel softening
> (a THIRD channel neither slot arm modeled) ⟹ the slot decomposition is INCOMPLETE at
> 2nd order ⟹ **[NEITHER]**, a DISCOVERY bin. On keying B the shear channel is inert and
> the pump lands on EXTENDED (slightly low). **The keying — whether a transverse
> displacement wave strains the shear channel that saturates `k_s` — is a
> substrate-ontology question I do not adjudicate (flag-don't-fix); it selects
> NEITHER vs EXTENDED. BOTH exclude DC_ONLY.**
>
> **Consequence for #518's radiation null (SURFACE, do not perform):** #518 correctly
> states ⟨field⟩ = ⟨A₀ sin ωt⟩ = 0 ⟹ ρ_eff = ρ_cold on the FIELD moment. The honest
> dynamics find a nonzero RECTIFIED 2nd-order strain moment ⟨A_bond⟩ > 0 that the field
> moment does not capture — so the traveling wave DOES move the transverse stiffness. This
> bears on #518's null (radiation is NOT stiffness-transparent at 2nd order) and it is
> exactly the fork's ARM EXTENDED consequence the #531 record anticipated. Surfaced for
> the auditor lane + Grant; NOT performed here.

**Consistency-vs-emergence:** CONSISTENCY / DC→AC-coupling (a DC medium state — the
rectified bias — read out through the AC probe). No VALUE derived (2/7, ρ*=9.7734, /7
stay GR-imported, PR#261/#506). The 2.04% arm separation is `(0.1428)²`, a derived
geometric factor — NOT ½, ¼, 2/7, 9.7734 (KNIFE-clean, §KNIFE).

---

## SUBSTRATE-FIRST SECTOR HEADER (as run)

- **SECTOR:** translational-u elastic sector, adjudicated on a **2-DOF-per-node chain**
  (longitudinal u + transverse y) as the minimal honest carrier of the transverse↔axial
  coupling. The force matches the CANONICAL srs bond tensor
  `Φ_bond = k_a·(d̂⊗d̂) + [k_s + T/ℓ]·(I−d̂⊗d̂)` (`prestress_elastic_tensor.py:124`) realized
  in the time domain. BOTH k_a, k_s are translational-u / **capacitive** springs of the same
  bond (PR#516) — NOT the ε/μ photon pair.
- **MODE:** TIME-DOMAIN nonlinear integration (symplectic velocity-Verlet). NOT slot algebra
  — the dynamics do not know how terms were divided between S and T.
- **REGIME:** small-signal ADIABATIC probe (the cycle-averaged transverse tangent stiffness =
  the Ω→0 slow-probe limit) about a traveling pump (Ax3-matched interior, Γ_internal≈0,
  SWR=1.003). Op14/Ax4 kernel ON.
- **PHASE-STATE:** sub-yield interior; the pump at tent-edge bow y₀=0.1428 (in-regime,
  `axiom-register.md:189`).
- **DC-vs-AC (clm-acdc07):** the **AC→AC sibling** of the SPICE lane's DC→AC bias-couples-to-
  wave `.TRAN` rung (`_orchestration/2026-07-03_spice-lane-charter.md:243`). The fork is
  precisely whether the AC pump deposits a DC bias the AC probe feels — the dynamics say
  **yes** (rectified ⟨A_bond⟩ > 0). Follow-on SPICE `.TRAN` cross-check is a candidate, not
  this arc's scope.
- **T2 HOMONYM GUARD (binding, #527):** the transverse bow y is the MECHANICAL T2-response
  bend, NOT the Cosserat (2,3) charge winding (`resonant-lc-solitons.md:95,:128`; A1⊥T2).
  mass=A1; charge=Cosserat-winding; bow=T2-mechanical-response.
- **COORDS (A46):** real-space displacement pump/probe; real-space transverse restoring
  stiffness readout. A46-clean (a real-space dynamical measurement, not a phase-space φ²
  comparison).
- **CLASS:** CONSISTENCY / DC→AC-coupling. EMERGENCE FORBIDDEN for any value.

---

## THE MEASURED PROBE-STIFFNESS TABLE (three states, both keyings, with bands)

Observable: the cycle-averaged transverse tangent stiffness `⟨−∂F_y/∂y⟩` at the probe node
(the Ω→0 slow-probe limit), reported as the CONVENTION-FREE ratio to cold (the 2× curvature-
stencil factor cancels identically across states). Measured from the time-domain response
ONLY (the #531 tautology guard — no slot formulas consumed).

| State | keying A (shear saturates) | keying B (shear constant) | FROZEN prediction | band |
|---|---|---|---|---|
| **(a) COLD** (pump off) | **1.000000** | **1.000000** | 1.000000 (=k_s) | ±1e-12 |
| **(b) DC-BIAS stretch** (uniform axial A=√α, y=0) | **1.078606** | **1.078606** | = merged #526 form k_s+T/L = **1.078606** (T_dc=Φ'(√α)=0.085321) | ±1e-4 |
| **(b′) DC-BIAS held bow** (frozen-prereg zig-zag, secondary) | 0.999930 | 1.110894 | (see Rule-10 §5: confounds shear channel) | — |
| **(c) PUMP** (traveling wave y₀=0.1428) | **1.008730** ± 0.30% | **1.018046** ± 0.30% | DC_ONLY=**1.000000** / EXTENDED=**1.020392** | ±0.30% |

**Diagnostics (both keyings):** SWR = **1.003** (clean traveling wave, no reflection);
undriven symplectic energy drift = **4.7×10⁻⁴** (bounded); measurement dt-converged to 5
digits (dt 0.005→0.0025 identical), δ-independent across 3 decades, probe-node-independent to
~0.1%.

### Frozen predictions vs measured

| Arm | FROZEN prediction | measured keying A | measured keying B |
|---|---|---|---|
| **DC_ONLY** (traveling wave loads nothing → cold) | 1.000000 | EXCLUDED (Δ=0.0087, >band) | EXCLUDED (Δ=0.0180, >band) |
| **EXTENDED** (⟨T⟩=(k_a/ℓ)y₀² enters slot) | 1.020392 | EXCLUDED (Δ=0.0117, >band) | within band (Δ=0.0024, ≤band) |

---

## LIVENESS-CONTROL STATUS — the mandatory structural-null stencil guard PASSED

**Did (b) see the T/ℓ term? YES, bit-exact.** The uniform axial pre-stretch DC-bias control
(every bond stretched to A=√α, transverse channel unstrained) reads k_trans = **1.078606**,
matching the merged #526 form `k_s + T/L = 1 + Φ'(√α)/L = 1.078606` to **6 digits** on the
SAME time-domain pipeline. **The probe demonstrably sees a genuine static tension term when
one exists — the instrument is LIVE.** No pump verdict is read past this control (the bin
selector HALTs if the liveness excess ≤ band; `test_bin_selector_halts_on_blind_instrument`
proves the HALT fires). Because the probe SEES a real tension (b) and then reads the pump
STIFFER than cold (c), the DC_ONLY null is bookable-as-excluded on a proven-live instrument.

**Rule-10 finding on the FROZEN-prereg held-bow control (b′):** the frozen prereg specified a
"held bow" (predicted 1.0376). Running it early (Rule 10) showed the zig-zag bow is a POOR
control — it maximizes the shear-channel strain, softening `k_s·S` by −3.85% which nearly
exactly cancels the +3.76% tension stiffening (keying A reads 0.99993, essentially cold). This
is not the probe failing; it is the zig-zag CONFOUNDING two channels. I KEEP-BOTH: the
frozen held-bow is reported (b′) as the confounded secondary, and the clean uniform-stretch
(b) — which isolates the T/ℓ term (shear strain = 0) — is the PRIMARY liveness control. The
uniform stretch is the faithful #526 static-DC picture (R2 varactor, T = Φ'(A_DC)); it is a
legitimate "held static tension" and it proves liveness unambiguously.

---

## THE HONEST NONLINEAR CHAIN (geometry + kernel — NO slot formulas)

2-DOF chain, N=600 nodes, rest spacing a₀=1. **Bond length** `L = √((a₀+Δu)² + Δy²)` is the
ONLY transverse↔axial coupling source — the string-tension force `T·(Δy/L)` emerges from it,
NOT inserted by hand. **Axial constitutive law** = the canonical kernel potential Φ,
`Φ''(a)=k₀√(1−a²)`, `Φ'(A)=k₀(A√(1−A²)+arcsin A)/2` (integrated once, sympy-verified: 5
exact-zero residuals). **Shear spring** `k_s·S(A_shear)` = the `(I−P)` block, the cold
transverse restoring stiffness (a bond at natural length has NO transverse stiffness from
tension — `prestress-tensor_result.md:142` verbatim — so the shear spring is the cold
baseline; the string tension adds under load, exactly `k_shear_eff = k_s·S + T/ℓ`).
**Symplectic velocity-Verlet** (Hamiltonian, energy-conservation-sensitive average — RK would
leak the pump). **Absorbing sponge** (width 200, γ=0.5) at the far end; SWR measured = 1.003.

**The dynamics realize the canonical srs tensor** — validated by (b) reproducing k_s+T/L
bit-exact. The pump measurement then just asks what a slow probe feels through a traveling
wave; the substrate answers.

---

## WHY DC_ONLY IS EXCLUDED — the Jensen rectification is real (the physics surfaced to Grant)

At prereg I surfaced to Grant the tension between #526's DC-scoped slot (⟨field⟩=0 ⟹ nothing
loads) and the PONDER-01 Jensen chain (`claim-quality.md:263`: concave S(E) → DC stress). **The
dynamics adjudicate it decisively for Jensen.** A traveling transverse wave y(x,t) makes each
bond length `L = √((1+Δu)² + Δy²)`; because the bond-length is convex in Δy, `⟨L⟩ > 1` even
though `⟨Δy⟩ = 0` — the bond LENGTHENS on average, rectifying a nonzero mean strain:

> measured **⟨A_bond⟩ = +0.004517** at the probe (below the no-relaxation geometric bound
> 0.00722 — the longitudinal DOF relaxes ~37% of it away; honest dynamics).

This rectified DC bias feeds the string-tension term `⟨T⟩/L > 0`, stiffening the transverse
probe — so DC_ONLY (which predicts the traveling wave loads nothing) is FALSIFIED. This is
the same mechanism that killed #529 as [RADIATION-CONTAMINATED], now seen directly in the
honest dynamics rather than through the slot bookkeeping.

**#518 reconciliation (flag-don't-fix, NOT performed):** #518's null rests on the FIELD moment
⟨A₀sin ωt⟩ = 0 (`matter-stiffening-rho_result.md:37,:146`). The dynamics find a nonzero
SECOND-order STRAIN moment ⟨A_bond⟩ > 0 — a DIFFERENT moment the field-mean statement does not
address. So the dynamics do not contradict #518's literal ⟨field⟩=0 claim, but they DO show
radiation is not transverse-stiffness-transparent at 2nd order. Surfaced for the auditor lane.

---

## THE KEYING FORK (the substrate-ontology question surfaced for Grant — flag-don't-fix)

The one input the verdict is sensitive to, which I do NOT resolve: **does a transverse
displacement wave strain the "shear channel" that saturates k_s?**

- **Keying A** (`shear_saturates=True`): the shear stiffness `k_s·S(A_shear)` with A_shear =
  the bond transverse angle |Δy|/L. Under the pump this softens `k_s` (−0.59% at the probe),
  partly cancelling the rectified tension (+0.43%) → net **+0.87%** → **[NEITHER]** (the slot
  decomposition omitted this softening channel — a genuine discovery of an incomplete slot).
- **Keying B** (`shear_saturates=False`): the shear spring is a constant k_s, unstrained by a
  pure transverse displacement → only the rectified tension acts → **+1.80%** → within the
  EXTENDED band → **[EXTENDED-CONFIRMED]** (at the band edge, 0.24% low).

Both keyings run through the IDENTICAL pipeline (KEEP-BOTH). The physical question — is the
Ax4 saturation of the transverse spring keyed on the transverse displacement, and toward the
same yield? — is genuinely underdetermined by what the corpus states, and it is exactly the
kind of framing fork the pre-test-physics-check exists to surface. **Grant's to rule. It
selects NEITHER vs EXTENDED; it does NOT change the robust DC_ONLY exclusion.**

---

## THE DERIVED TOLERANCE BAND (the #531 lesson: no vacuous bands)

The reconcile band is DERIVED, not vacuous. Convergence sweep (this session):

| residual source | measured |
|---|---|
| dt (0.005→0.0025) | 6.8×10⁻⁷ |
| window (n_periods 200→280) | 5.1×10⁻⁵ |
| probe-node (150/200/300) | ~1.0×10⁻³ (residual SWR=1.003 standing modulation) |

Summed residual floor ≈ 1.0×10⁻³; **band = 3× = 3.0×10⁻³ = 0.30%.** This is STRICTLY BELOW the
2.04% arm separation (`test_derived_band_below_arm_separation`), so the arms are RESOLVABLE
(not [UNRESOLVED]). The dominant residual is the node-to-node variation from the tiny residual
standing modulation (SWR=1.003 → ±0.15% envelope) — a real, honest systematic, correctly in
the band. Bands, not six-digit precision, carry the verdict.

---

## THE KNIFE (armed; coincidence discipline) — KNIFE=False

- **2.04% arm separation** = `(0.1428)²` = the tent-edge bow squared, a DERIVED geometric
  factor. NOT ½, ¼, 2/7 (0.2857), 9.7734, 1/√α (`test_arm_separation..._knife_clean`).
- **⟨A_bond⟩ = 0.0045** — the rectified strain; not on any canon target (it is `~⟨Δy²⟩/2`
  minus longitudinal relaxation, an honest 2nd-order geometric quantity).
- The measured pump values (1.0087 / 1.0180) do not land on ½, ¼, 2/7, or the identity
  endpoints. Keying B's 1.018 is NEAR EXTENDED (1.020) but 0.24% low — reported as
  within-band-but-low, NOT as a suspiciously-exact landing (and EXTENDED is a slot prediction
  in a SEPARATE module — the tautology guard confirms the dynamics never consumed it).

**KNIFE=False:** no measured quantity lands on a canon-distinguished value.

---

## HONEST CLOSURE (Rule 11) — the pre-registered DC_ONLY prediction failed decisively; one mechanism explains it

The prereg froze DC_ONLY (probe recovers cold, 1.000) and EXTENDED (1.020) BEFORE the driver
ran. The honest dynamics FALSIFY DC_ONLY on both keyings by a wide margin. **One mechanism**
explains it: the concave-kernel / convex-bond-length **Jensen rectification** deposits a
nonzero 2nd-order mean strain a slow probe feels — a traveling wave is NOT transverse-
stiffness-transparent. This is the discipline working: a clean falsification of a frozen arm,
mechanism named, no rescue. The SECONDARY axis (does it land ON EXTENDED) is honestly left as
a keying fork for Grant — NOT collapsed to a single answer, NOT tuned toward EXTENDED.

**Substitution-not-retraction (Rule 12):** this does NOT refill any slot with an unverified
hypothesis. It reports what the dynamics measure and surfaces the keying fork + the #518
2nd-order-moment question. Any new claim ("the pump-loaded medium has its own operating
point") would be a new version with its own verification chain — none asserted here.

---

## LEDGER (canon-forced vs derived vs engineering-choice; all magnitudes banded)

| # | Term | Status | Basis |
|---|---|---|---|
| 1 | Kernel `Φ''(a)=k₀√(1−a²)` | CANON-FORCED | Ax4, `scale_invariant.py:107-156` |
| 2 | Tension `Φ'(A)` | DERIVED (sympy) | integrate once, 5 exact-zero residuals |
| 3 | Bond length `L=√((a₀+Δu)²+Δy²)` | GEOMETRY (honest) | the coupling source; NOT a slot term |
| 4 | Shear spring `k_s·(I−P)` cold baseline | CANON-FORCED | srs tensor `prestress_elastic_tensor.py:124`; `#526:142` (T=0 → no transverse stiffness from tension) |
| 5 | ⟨A_bond⟩>0 rectified strain | MEASURED (dynamics) | Jensen; the DC_ONLY-exclusion mechanism |
| 6 | Symplectic velocity-Verlet | ENGINEERING (justified) | Hamiltonian, energy-sensitive average |
| 7 | Band = 3× derived residual = 0.30% | DERIVED (convergence sweep) | #531 discipline; < 2.04% separation |
| 8 | y₀ tent edge 0.1428 | READ-OFF (#527/#529) | `axiom-register.md:189` arc* band; never tuned |
| 9 | A=√α (DC-bias control) | READ-OFF (Class-C echo) | def-vyvsn1; never tuned |
| 10 | **shear-channel keying (A vs B)** | **OPEN GRANT-FORK** | selects NEITHER vs EXTENDED; DC_ONLY excluded either way |

**0 free parameters tuned toward 2/7 / 9.7734 / 2.04% / EXTENDED.** The band, y₀, and the
keying are the only knobs; band+y₀+A are derived/read-off; the keying is an explicit open fork.

---

## CONTROL STATUS — all pass; gates via #528 ReconcileGate; can-fire proven on real data paths

- **PC-COLD:** 1.000000 to 1e-12 (instrument zero). ✅
- **PC-DC-LIVENESS:** uniform stretch = merged #526 form to 6 digits; excess ≫ band (probe
  sees a real tension). ✅ Reconciled via #528 `ReconcileGate` (`PC_DC_LIVENESS_vs_526form`).
- **PC-SWR:** 1.003 (clean traveling wave). ✅
- **PC-ENERGY:** undriven drift 4.7×10⁻⁴. ✅
- **Bin selector:** no fall-through else; DISCREPANT-HALT reachable — `test_bin_selector_
  halts_on_broken_cold` (COLD≠1 HALTs) + `..._halts_on_blind_instrument` (liveness≤band HALTs).
- **ReconcileGate can-fire:** proven on **dropped-term** (claim=cold vs merged form → fires) and
  **sign-flip** (claim=compression vs tension → fires) synthetics on real data paths.
- **Tautology guard (#531):** `test_tautology_guard_no_cross_import` asserts the dynamics module
  never imports the prediction module; the gate compares OUTPUTS only.

---

## FALLOUT / AUDITOR-QUEUE (surfaced; implementer does NOT land manuals)

| Site | Proposed disposition |
|---|---|
| **#526 prestress T-slot scope fork** (`prestress-tensor_prereg_FROZEN.md`:64-78; #531 fork record) | **RESOLVE-VIA-ENGINE (candidate, Grant confirms):** the honest dynamics EXCLUDE DC_ONLY — a traveling wave DOES deposit a rectified 2nd-order bias the slow probe feels. So the slot's DC-only scope does NOT match the full nonlinear dynamics at 2nd order. Whether the result is EXTENDED or a NEW law (NEITHER) turns on the shear-keying fork (row below). Grant's Reading-A leaned DC_ONLY; the dynamics lean against it. |
| **#518 §7 radiation null** (`matter-stiffening-rho_result.md:37,:146`: pure-AC ⟨A⟩=0 → ρ_eff=ρ_cold) | **UP-FOR-REVISION (SURFACE, do not perform):** the ⟨field⟩=0 statement is literally correct, but the dynamics find a nonzero RECTIFIED 2nd-order strain moment ⟨A_bond⟩>0 — radiation is NOT transverse-stiffness-transparent at 2nd order. The null holds on the field moment; it does not hold on the strain moment. Auditor/Grant to adjudicate the scope. |
| **The shear-channel keying** (does a transverse wave strain the saturating shear spring?) | **OPEN GRANT-FORK:** keying A → [NEITHER] (slot incomplete: a shear-softening channel neither arm modeled); keying B → [EXTENDED-CONFIRMED]. Both exclude DC_ONLY. A one-line Grant ruling selects the secondary bin. |
| **#529 [RADIATION-CONTAMINATED]** (`resonant-tension-law_result.md`) | **CORROBORATED:** the mechanism that killed #529 (a matched traveling wave carries a persistent per-bond ⟨T⟩) is now seen DIRECTLY in the honest dynamics (⟨A_bond⟩>0 → ⟨T⟩/L>0), independent of the slot bookkeeping. |
| **PONDER-01 Jensen chain** (`claim-quality.md:263` concave S → DC stress) | **CROSS-LINK (candidate):** the pump-probe dynamics are a direct lattice realization of the Jensen rectification (⟨√(1+Δy²)⟩>1 rectifies a DC strain). |
| **SPICE lane charter** (`_orchestration/2026-07-03_spice-lane-charter.md:243`, `.TRAN` rung) | **CROSS-LINK (candidate):** this arc is the AC→AC sibling of the DC→AC bias-couples-to-wave rung; a `.TRAN` cross-check of the rectified bias is a follow-on candidate (NOT this scope). |

**No rewrites performed.** Resolve / revision-surface / fork / cross-link ROWS only; the
auditor lane lands the manual entries.

---

## FLAG-DON'T-FIX — surfaced, not resolved

1. **THE SHEAR-CHANNEL KEYING FORK (load-bearing, Grant's to rule).** Selects NEITHER (keying
   A) vs EXTENDED (keying B). Both exclude DC_ONLY. §"THE KEYING FORK".
2. **#518's 2nd-order moment.** The dynamics find a rectified strain moment the #518 field-mean
   null does not address. Surfaced, NOT performed. §"WHY DC_ONLY IS EXCLUDED".
3. **Keying B lands 0.24% BELOW EXTENDED (within band).** Reported honestly as within-band-but-
   low, not as an exact landing; the small residual is the shear-channel geometry contributing
   even in keying B. Not tuned.
4. **Cauchy-only, fixed-geometry, 2-DOF chain scope.** The srs z=3 cell-scale relaxation and the
   Cosserat couple-stress carrier (Stage 2) are out of scope; this is the minimal honest carrier
   of the transverse↔axial coupling, matching the #526 Cauchy scope.

---

## Cross-references (grep-verified at branch HEAD this session)

- Prereg (FROZEN): `research/2026-07-05_pump-probe-tslot_prereg_FROZEN.md`
- Driver / prediction module / tests / output: see header
- Fork record (PR #531): `research/2026-07-05_channel-resolved-loading_result.md`
- #526 frozen T-slot scope: `research/2026-07-04_prestress-tensor_prereg_FROZEN.md`:64-78;
  result + srs tensor form: `research/2026-07-04_prestress-tensor_result.md`:142; driver
  `src/scripts/vol_1_foundations/prestress_elastic_tensor.py`:124
- #529 [RADIATION-CONTAMINATED]: `research/2026-07-04_resonant-tension-law_result.md`
- Bond-force sign rule (merged Φ'): `research/2026-07-04_bond-force-sign-rule_result.md`
- #518 radiation null: `research/2026-07-04_matter-stiffening-rho_result.md`:37,:146
- Kernel: `src/ave/axioms/scale_invariant.py:107-156`; core `universal_saturation`
- ReconcileGate (#528): `src/ave/validation/reconcile_gate.py`
- Jensen-rectification chain: `manuscript/ave-kb/vol4/claim-quality.md:263`
- SPICE lane charter (DC→AC sibling): `_orchestration/2026-07-03_spice-lane-charter.md:243`
- T2 homonym guard: `resonant-lc-solitons.md:95,:128` (A1⊥T2, Grant-ratified 2026-06-14)

</details>

---

## CORRECTED FALLOUT / AUDITOR-QUEUE (live, post-review — supersedes the preserved rows above)

| Site | Corrected disposition |
|---|---|
| **#526 prestress T-slot scope fork** | **STILL OPEN.** This arc does NOT adjudicate it — the observable was lab-frame mixed. The dynamics EXCLUDE neither arm at bond-frame level. A valid adjudication needs the §REQUIREMENTS list (bond-frame observable, dynamical probe, closed boundaries, Hamiltonian keyings, honest bands). |
| **#518 §7 radiation null** (`matter-stiffening-rho_result.md:37,:146`) | **UNTOUCHED — the null STANDS.** 🔴 RETRACTED the prior "up-for-revision on the 2nd-order strain moment" row: the ⟨A_bond⟩>0 "deposit" was a boundary artifact (sign-flips to −0.0083 with a free end; cycle-mean reads COLD). #518's null rests on TWO independent legs — the ⟨A⟩=0 field mean AND the **⟨A²⟩ channel-SYMMETRY argument** (`matter-stiffening-rho_result.md:149`: a pure AC field drives BOTH grades with the same ⟨A²⟩, so ρ_eff is symmetric-invariant). Both survive this arc untouched. NO revision warranted. |
| **PONDER-01 Jensen chain** (`claim-quality.md:263`) | 🔴 RETRACTED the cross-link. This arc's stiffening is kinematic tilt, NOT Jensen (a linear chain reproduces it to 2e-6). No Jensen realization is claimed. |
| **clm-acdc07 "AC deposits DC — yes"** | 🔴 RETRACTED. The cycle-mean config reads COLD; no DC is deposited. This arc says nothing about AC→DC deposition. |
| **#529 [RADIATION-CONTAMINATED]** | **UNCHANGED / independent.** This arc does not bear on #529 (the corroboration claim rested on the retracted ⟨A_bond⟩ deposit). #529 stands on its own record. |
| **The instrument-liveness result** | **KEEP (the real product):** the uniform-stretch probe reads the merged #526 bond-frame form to 6 digits — a live bond-frame tension readout. |
| **The kinematic-tilt characterization + boundary-artifact documentation** | **KEEP (the real products):** the tilt term to subtract, both boundary configs, the strain profile. |

**Rule 12 note:** no slot is refilled with a new mechanism. The fork returns to OPEN; the forward
path is the §REQUIREMENTS list, not a new hypothesis.
