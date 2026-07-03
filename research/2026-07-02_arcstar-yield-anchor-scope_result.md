# RESULT — `arc* < ℓ_node` is an AVE-INTERNAL refinement, NOT a new benchtop falsifier

**Date:** 2026-07-02
**Lane:** research / scoping (bounded). HOLD canonization. Do NOT merge — push + report.
**Branch:** `analysis/arcstar-yield-anchor-scope` (off `origin/main` @ `a00ec11a`, PR #460)
**Prereg:** [`2026-07-02_arcstar-yield-anchor-scope_prereg.md`](2026-07-02_arcstar-yield-anchor-scope_prereg.md) (frozen @ `260f94b0`)
**Source:** [`2026-07-02_axiom4-moduli-hierarchy_result.md`](2026-07-02_axiom4-moduli-hierarchy_result.md) §4 (PR #460)
**Discipline:** `ave-prereg` + `substrate-native-check` + `ave-discrimination-check` + `pre-test-physics-check` + `ave-canonical-source`.

---

## 0. VERDICT (one line)

**INTERNAL REFINEMENT, not a bench falsifier — all three tasks land as pre-registered.** (1) The elastica curvature integral CONFIRMS the O(1/ρ) structure (`eps_c·ρ → const` at large ρ), shifting the prefactor by an O(1) factor ~0.79× (band 4.5–11.1% tent → ~4.0–13.1% elastica; same order, structurally model-robust); the tent's *exact A-independence* is revealed as a tent artifact — the elastica "fixed arc*" is a near-yield operating-point statement. (2) The measurable yield is **α-anchored** (`V_yield = √α·V_snap` EXACTLY, `resonant-lc-solitons.md:127`; corpus-unanimous) — **Case (b)**: `arc*<ℓ_node` surfaces as a discrepancy between the *geometric* yield strain (arc*-set, K=2G-imported) and the *α-defined* measurable V_yield, an AVE-internal consistency statement, NOT a knee-shift the bench reads. (3) Discrimination-check: the whole saturation curve is already AVE-distinct-vs-SM (SM has no knee); `arc*<ℓ_node` renormalizes AVE's *own* amplitude axis (A → u=A/arc*) but adds **no new AVE-vs-SM discriminator** — a ~5% shift of an AVE-internal feature against an SM flat-ε null. **Bank as an internal refinement; do NOT graduate to a cRIO C_eff(V) bench spec.**

---

## 1. Task 1 — the pinned prefactor (elastica vs tent)

### Method
Replaced the tent 2-segment kinematic (`arc = 2√((A/2)²+S²)`, bend energy `½k_s S²`, minimized over the midpoint sag S) with the **continuum planar mode-1 Euler elastica**: bend energy = the curvature integral `½·B·∫κ²ds` (matching the Cosserat `γ|κ|²` term, `cosserat_field_3d.py:693-708`), stretch energy the same axial-Hooke `½k_a(arc−ℓ)²`. The elastica bend was solved **exactly** (no small-bow assumption — the near-yield large-bow regime is where Axiom 4 lives) via the Jacobi-elliptic elastica quadrature: for shape parameter `p=sin(θ₀/2)`, the axial-span/arc ratio `A/s = (2E(p)−K(p))/K(p)` and the curvature integral `∫κ²ds` are pure functions of `p`. The bend modulus B was calibrated against `k_s` in the small-bow limit so **ρ = k_a/k_s stays the single dimensionless knob** — the elastica just distributes the curvature smoothly instead of concentrating it at the tent's midpoint kink.

**Numerical validation of the solver:** the small-bow curvature-integral constant came out `∫κ²ds/dL → 39.4799`, matching `4π² = 39.4784` to 1 part in 2·10⁴ — the analytic mode-1 elastica value, confirming the quadrature is sound (script: `elastica_arcstar.py` + `elastica_probe.py`, scratchpad; canonical `α`, `L_NODE` imported via `ave-canonical-source`, not hard-coded).

### Result — `arc*(ρ)` elastica vs tent

At the physically-relevant **near-yield self-consistent operating point** (knee at `A = √3/2·arc*`, i.e. R_II = √3/2 = `constants.py:485`, the non-linear→saturated boundary):

| ρ | arc*_tent = 4ρ/(4ρ+1) | eps_c_tent = 1/(4ρ+1) | arc*_elastica | eps_c_elastica | eps_el/eps_tent |
|---|---|---|---|---|---|
| **2.0** | 0.8889 | **11.11%** | 0.8693 | **13.07%** | 1.176 |
| 3.0 | 0.9231 | 7.69% | 0.9227 | 7.73% | 1.005 |
| 4.0 | 0.9412 | 5.88% | 0.9447 | 5.53% | 0.941 |
| **5.3** | 0.9550 | **4.50%** | 0.9595 | **4.05%** | 0.899 |
| 20.0 | 0.9877 | 1.23% | 0.9899 | 1.01% | 0.816 |
| 100.0 | 0.9975 | 0.25% | 0.9980 | 0.20% | 0.795 |

### The three findings

1. **O(1/ρ) structure SURVIVES (the source result's structural claim holds).** At large ρ, `eps_c_elastica·ρ → 0.198` (constant), so `eps_c ∝ 1/ρ` — the same power as the tent (`eps_c_tent = 1/(4ρ+1) → 1/(4ρ)`). The source result's "`arc*<ℓ_node` by O(1/ρ), model-robust" line (`axiom4-moduli-hierarchy_result.md:37,43`) is **CONFIRMED** by an independent (smooth-bow) kinematic. Outcome-C falsifier (band NOT ∝ 1/ρ) did NOT fire.

2. **The prefactor shifts by an O(1) factor ~0.79×** (asymptotic `eps_el/eps_tent → 0.791`, close to `(π²−2)/π² = 0.7974` — exact closed form not load-bearing for the verdict). Physically: a **smooth bow stores bend energy more efficiently than a tent kink** (the tent concentrates all curvature at one point, over-penalizing bend → over-bowing → over-shrinking the arc), so the elastica settles at a **slightly smaller deficit** at fixed ρ. Direction as pre-registered.

3. **The % band shifts modestly, stays the same order.** Tent: **4.5–11.1%** across ρ∈[2,5.3]. Elastica: **~4.0–13.1%**. Overlapping, same OOM. The band is **structurally model-robust** (both kinematics agree to within an O(1) prefactor); the **exact %** remains model-dependent at the ~15–20% level (at ρ=2 the two differ by 1.18×). The source result's "exact % not yet model-robust" caveat STANDS — but the two independent models now bracket it at ~4–13%.

### Honest flag: A-independence is a TENT ARTIFACT (not in the pre-reg — surface, don't smooth over)

The tent gives arc* **exactly independent of the axial span A** (a special algebraic property of the piecewise-linear kinematic). The **elastica arc* DRIFTS with A** (e.g. ρ=2: arc*_el ranges 1.08 at A=0.2 → 0.82 at A=0.8). The "self-consistent *fixed* arc-length" phrasing in the source result (`:33,:37`) is therefore **tent-specific**: for the smooth bow, arc* is fixed only *at the near-yield operating point* (the knee), where the two models reconverge (table above). This does NOT break the O(1/ρ) deficit or the √-in-u shape at the operating point — but the "fixed arc-length independent of A" claim is a tent property, not a general elastica theorem. **FLAG to the auditor lane** for whether the source result's §3 wording needs a one-line "A-independence is tent-specific; elastica fixes arc* only at the operating point" caveat (Rule-12 additive, not a walk-back — the operating-point conclusion is unchanged). Surfaced per flag-don't-fix; Grant/auditor adjudicates whether the merged doc gets the caveat.

---

## 2. Task 2 — the yield-anchoring verdict: **Case (b), α-anchored**

### The load-bearing corpus grep (verify-before-cite; all verified this session)

- `src/ave/core/constants.py:455` — `V_SNAP = (M_E*C_0**2)/e_charge` (≈511 kV). **Definitional** (rest energy / e).
- `src/ave/core/constants.py:464` — `V_YIELD = np.sqrt(ALPHA)*V_SNAP` (≈43.65 kV). **α-anchored, exact.**
- `manuscript/.../resonant-lc-solitons.md:127` (def-vyvsn1=T2, Grant 2026-06-30), verbatim: *"$V_{\text{yield}}=\sqrt{\alpha}\cdot V_{\text{snap}}$ EXACTLY, so the two are NOT independent per-sector thresholds (the $\sqrt{\alpha}$ is an $\alpha$-echo; $A=\sqrt\alpha$ is a Class-C echo operating point)."*
- `manuscript/.../regimes-of-operation.md:11` — *"the yield voltage … $V_{yield}=\sqrt{\alpha}\,V_{snap}\approx43.65$ kV. This yield applies per lattice node, i.e., across a single node spacing $\ell_{node}$"* — confirms ℓ_node enters only as the per-node length to convert the α-set *voltage* into the *field* `E_yield = V_yield/ℓ_node`; the yield **value** is √α·V_snap.
- `manuscript/.../cvr-dc-operating-point.md:22` — the kernel amplitude axis is `A_0 = Δφ/α` per-node — an **α-normalized amplitude**, NOT a geometric arc-length.
- **Negative grep (completeness, 2nd method):** `grep -rn "arc\*" manuscript/ave-kb/` returns ZERO leaves anchoring the *measurable* knee to a geometric arc-length. The measurable is α throughout.

### Verdict

**Case (b): the measurable yield is α-anchored.** `V_yield = √α·V_snap` is corpus-unanimous and exact; V_snap is definitional. The bench knee sits at √α·V_snap (per node), and the R_II = √3/2 "≈85% of E_yield" knee (`dielectric-plateau-prediction.md:36`) is a fixed fraction of *that* α-anchored E_yield.

Therefore `arc*<ℓ_node` does **NOT** move the measurable knee. It surfaces as a **DISCREPANCY** between two independent dimensionless numbers of **different provenance**:
- the **geometric** yield strain the kernel would set from the operating arc-length: `arc*/ℓ_node = 4ρ/(4ρ+1) = {0.889, 0.955}` — **K=2G-imported** (ρ is K=2G-set), and refined to ~0.79× that deficit by the elastica.
- the **α-defined measurable**: `V_yield/V_snap = √α = 0.0854` — an **α-echo**.

These do not multiply into the observable knee position; the knee stays pinned at √α·V_snap. **arc*<ℓ_node is an AVE-internal consistency statement (geometric-vs-α yield), not a directly-measured knee shift.** Outcome-B falsifier (a leaf anchoring the measurable to ℓ_node-geometry) did NOT fire — no such leaf exists.

**Substrate-native framing (substrate-native-check):** the amplitude the kernel saturates on is the α-normalized per-node phase `A_0 = Δφ/α`, a phase-space quantity (the varactor bias), NOT the real-space bond arc-length. arc* is a real-space geometric refinement of where the *bow* collapses; the *measurable* knee is a phase-space α-threshold. These live in different coordinates (A46 discipline) — which is exactly why arc* refines the geometry but leaves the phase-space knee where α puts it.

---

## 3. Task 3 — discrimination-check: **bench falsifier vs internal refinement**

### (a) Does arc*<ℓ_node produce a bench-measurable knee-position deviation?

**No.** Per Task 2, the measurable knee is α-anchored (√α·V_snap). arc*<ℓ_node is a K=2G-imported geometric refinement of the *bow-collapse* strain; it renormalizes AVE's own amplitude axis (A → u = A/arc*) but the bench-read knee voltage stays at the α value. The only place arc* would move a measurable is Case (a) (ℓ_node-geometric anchoring) — which the corpus does not use.

### (b) SM-counterfactual (discrimination-check Steps 2 + 2.5)

| Claim | SM predicts same? | AVE-distinct? |
|---|---|---|
| A knee/spike in C(E) exists near √3/2·E_yield | **NO** — SM has flat ε₀, no knee at any field below Schwinger | ✅ YES (the whole curve is the discriminator) |
| The knee sits at √α·V_snap per node | NO (no SM mechanism ties α to a dielectric knee) | ✅ YES — but this is the **existing** curve, not new |
| The knee position shifts ~4–13% due to arc*<ℓ_node | **N/A** — SM has no knee to shift; the shift is invisible against the SM flat-ε null | ❌ NO — refines an AVE-internal feature only |
| arc*/ℓ_node = 4ρ/(4ρ+1) (K=2G-imported deficit) | NO | ❌ NO — sharpens AVE's own kernel normalization |

**Step 2.5 axis (magnitude vs ratio/slope):** the AVE-vs-SM discriminator is the **EXISTENCE + shape of the whole saturation curve** (SM shares neither form nor scale — SM is flat). arc*<ℓ_node touches only the **position/normalization** of the knee, a ~5–13% correction *internal* to a curve SM already fails to predict at all. A shift of an AVE-internal feature against an SM null does not separate AVE from SM more than the bare curve already does. The arc* shift is a **refinement of the existing AVE curve, not a new AVE-vs-SM discriminator.**

### (c) Verdict: **INTERNAL REFINEMENT**

arc*<ℓ_node **sharpens AVE's own structure** (the kernel's effective yield strain, the amplitude renormalization u=A/arc*, the geometric-vs-α consistency ledger) — it does **not** add a new benchtop AVE-vs-SM falsifier. The pre-registered prediction lands. No overclaim: this is the valid, valuable outcome — the arc closes on a clean internal-consistency refinement, consistent with the corpus meta-finding (AVE forces FORMS, imports VALUES; here the √-FORM is refined, the α-VALUE anchor is untouched).

---

## 4. Recommendation — bank as internal refinement; do NOT graduate to a cRIO bench spec

**Bank `arc*<ℓ_node` as an AVE-internal refinement of the Axiom-4 kernel's effective yield strain — do not graduate it to a benchtop test spec.** The reasoning chain: (i) the measurable knee is α-anchored (√α·V_snap, corpus-unanimous), so arc* does not move a bench-read observable; (ii) the whole saturation curve is *already* the AVE-vs-SM bench discriminator (the cRIO C_eff(V) rig probes "is there a knee at all near √3/2·E_yield" — an existing target), and arc* only refines the position/normalization of a knee SM already can't predict; (iii) the elastica confirms the O(1/ρ) structure but leaves the exact % model-dependent (~4–13%), so even the *internal* deficit isn't a sharp single-number target. The cRIO C_eff(V) saturation rig's discriminating power lives in the EXISTENCE and gross shape of the knee (and, per `claim-quality.md:78`, the still-open longitudinal-A1-spike-÷S vs transverse-dielectric-rolloff-×S *sector* question — a genuine bench discriminator), NOT in a ~5% arc*-set position shift that the α-anchoring absorbs. arc*<ℓ_node's value is internal: it sharpens the geometric-vs-α yield ledger and the amplitude renormalization, and it is the fourth+ instance of FORM-refined / VALUE-imported. Recommend the auditor lane consider (a) a Rule-12 additive caveat on the source result's §3 "fixed arc-length independent of A" wording (tent-specific; see §1 flag), and (b) banking the elastica prefactor (~0.79× tent, band ~4–13%) alongside the tent value in the axiom-register residual note — Grant/auditor rules; this doc HOLDS canonization.

## 5. Outputs

This result + the frozen prereg, via the branch (research docs, **NOT a canon change**; HOLD canonization; do NOT merge — push + report). Scratchpad solvers (`elastica_arcstar.py`, `elastica_probe.py`, `elastica_analytic.py`) are working files, not committed.
