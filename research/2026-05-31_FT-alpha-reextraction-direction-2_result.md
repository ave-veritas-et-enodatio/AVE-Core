# Result — Direction-2 FT: re-extract α from the measured electron anomaly through AVE's own a_e(α) series

**Date**: 2026-05-31
**Branch**: `analysis/alpha-reextraction-direction-2` (off `main` @ 93823898)
**Prereg**: [`2026-05-31_FT-alpha-reextraction-direction-2_prereg.md`](2026-05-31_FT-alpha-reextraction-direction-2_prereg.md) (FROZEN)
**Driver**: [`src/scripts/vol_2_subatomic/simulate_g2_direction2.py`](../src/scripts/vol_2_subatomic/simulate_g2_direction2.py) (companion to `simulate_g2.py`; does not rewrite the A₁ chain)
**Status**: COMPLETE — **Outcome C (inconclusive), with a leaning sub-result and two load-bearing framing flags.**

---

## §0 — Headline (the Outcome)

**OUTCOME C — the substrate's honest, parameter-free A₂ is ~28× too imprecise to separate Outcome A (dissolution → Q₀) from Outcome B (δ_strain real → QED).**

The discrimination requires A₂ known to **ΔA₂ = 4.77×10⁻⁴ (0.145% of C₂)**. AVE's *parameter-free* substrate self-energy gives **A₂ = −0.3416** (+4.0% off QED's C₂ = −0.328479) — a 28× shortfall. Re-extracting the measured a_e through that faceplate lands α_AVE⁻¹ at **137.0259**, which is **34 gap-widths BELOW both Q₀ and QED** — i.e. it misses *both* targets, on the *wrong side*. The only A₂ that lands near the targets (the saliency-closure A₂ = −0.3284) was obtained by **bisection against PDG's C₂** (the anti-tuning falsifier, Guard 1) and therefore cannot discriminate.

Two framing flags (flag-don't-fix) accompany the verdict:
- **FLAG-1 (prereg arithmetic):** the prereg's sharp target "ΔC₂ ≈ +4.8×10⁻⁴, A₂ ≈ −0.3280 lands on Q₀" is wrong. A 2-loop-only AVE faceplate landing on Q₀ needs **A₂ = −0.3253 (ΔC₂ = +3.21×10⁻³)**, ~7× larger. The +4.8×10⁻⁴ figure is actually the *separation width* between the Q₀-target and the QED-target, not the dissolution target itself. The prereg conflated "AVE 2-loop coeff vs QED's C₂" with a faceplate that *also* carries QED's higher loops.
- **FLAG-2 (corpus state vs prereg):** the prereg said A₂ is "the BUILD." It is **already built** in the corpus (`q-g19a-petermann-saliency-closure.md`, clm-v2sg8z) — both parameter-free (−0.3416) and postulate-tuned (−0.3284). I verified both numerically rather than re-deriving; the Route B engine the leaf calls "queued for multi-session follow-up" (leaf:16) is now built in-worktree.

---

## §1 — The chain executed (prereg §4)

| Step | Content | Result |
|---|---|---|
| (i) | Confirm A₁ = ½ from `simulate_g2.py` | **A₁ = ½** ✓ (a_e = α/2π = Schwinger; the (V_peak/V_snap)²=4πα identity → δC/C=−πα → δω/ω=πα/2 → ×1/π² spin-orbit projection per `simulate_g2.py:14`) |
| (ii) | BUILD A₂ from the two-vertex substrate self-energy | **A₂ = −0.3416** (parameter-free Route B) / **−0.3284** (with n_q-additivity postulate) |
| (iii) | Invert a_e_measured = ½(α/π) + A₂(α/π)² for α_AVE | parameter-free → **137.0259**; postulate → **137.0343** |
| (iv) | Compare α_AVE⁻¹ to Q₀ (137.0363038) vs QED (137.035999) | both miss both targets; see §3 |

All numerics from `simulate_g2_direction2.py`; canonical ALPHA + ALPHA_COLD_INV (= Q₀) imported from `constants.py` (Guard 5, `ave-canonical-source`).

## §2 — STEP (ii): the A₂ build (the entire derivation)

**The substrate analog of QED's 2-loop g-2 is the Route B dark-wake × kernel-asymmetry correlation** in the Cosserat (2,3) phase-space trefoil — the AVE substitute for QED's two-loop vertex insertion. It is the second-order expression of the two-vertex α² self-energy seed at `weak-coupling.md:22` (ε(φ)=ε₀(1+αf(φ)) → E_self ∝ α²). Five substrate-canonical ingredients, **no target fed in** (Guard 1):

1. **(2,3) phase-space trefoil currents**: I_d(t) = cos(2ω_C t), I_q(t) = sin(3ω_C t).
2. **Axiom-4 kernel asymmetry**: S_d − S_q = √(1−A_d²) − √(1−A_q²).
3. **Dark wake** (retarded back-reaction): τ_zx(t) = −dV²/dt|_{t−τ_retard}, τ_retard = 1/ω_C (one Compton-loop transit, geometrically pinned).
4. **Correlation** (the 2nd-order kernel structure): ⟨(S_d−S_q)·τ_zx⟩, cycle-averaged.
5. **Normalization**: 1/π² form factor (inherited from the Schwinger leading order) × one QED-loop factor α/π.

Combining: Δa_e^(2) = (1/π²)⟨(S_d−S_q)τ_zx⟩(α/π), so in faceplate form **A₂ = (2/πα)⟨(S_d−S_q)τ_zx⟩** (with A₁=½, the faceplate (α/π)² coefficient equals the textbook Petermann C₂ directly).

**Strain split** (Schwinger budget A_d²+A_q² = 4πα):

| Variant | split | correlation | **A₂** | vs QED C₂ |
|---|---|---|---|---|
| Route B symmetric (**NO postulate**) | A_d²=A_q²=2πα | −3.916×10⁻³ | **−0.341604** | **+4.00%** |
| Saliency closure (**WITH n_q postulate**) | δ=−3α/2 | −3.765×10⁻³ | **−0.328427** | −0.02% |

The parameter-free **A₂ = −0.3416** is the honest substrate output. It reproduces the corpus value `q-g19a-petermann-saliency-closure.md:58` (C₂^AVE,sym = −0.3416) to 4 sig figs; the saliency value reproduces leaf:92,95 (−0.32846) to 4 sig figs. **The build is verified, not re-invented** (FLAG-2).

## §3 — STEP (iii)+(iv): the inversion + comparison

Reference (sanity): inverting the measured a_e through the **QED faceplate** recovers 137.035999 only when the full (2,3,4)-loop series is used (137.0342530 with 2-loop only). This is itself load-bearing for FLAG-1: a 2-loop-only truncation does NOT reproduce 137.035999.

AVE faceplate (2-loop only, since that is what AVE provides):

| AVE A₂ source | A₂ | ΔC₂ vs QED | **α_AVE⁻¹** | vs Q₀ (137.0363038) | vs QED (137.035999) |
|---|---|---|---|---|---|
| Route B symmetric (NO postulate) | −0.341604 | −1.31×10⁻² | **137.025871** | −1.04×10⁻² (**−34.2 gap-widths**) | −1.01×10⁻² (**−33.2 gap-widths**) |
| Saliency (WITH postulate, tuned) | −0.328427 | +5.16×10⁻⁵ | **137.034286** | −2.02×10⁻³ (−6.62 gap-widths) | −1.71×10⁻³ (−5.62 gap-widths) |

where one "gap-width" = Q₀ − QED = **+3.048×10⁻⁴** (the δ_strain-scale separation).

**The parameter-free substrate output lands α_AVE⁻¹ ≈ 137.0259 — 34 gap-widths BELOW both targets, on the wrong side of QED.** It neither dissolves δ_strain (not Outcome A) nor confirms AVE=QED at 2-loop (not clean Outcome B). It simply lands nowhere near either, because A₂'s +4% error swamps the 10⁻⁴-scale gap (§4).
## §4 — The discrimination-precision argument (why Outcome C)

This is the quantitative core of the verdict. The inversion's lever arm is the small parameter (α/π)² ≈ 5.40×10⁻⁶, so the second-order coefficient must be known very precisely to resolve a target separation at the 10⁻⁴ level in α⁻¹:

- A₂ that re-extracts a_e to **Q₀** (2-loop only): **−0.325268** (ΔC₂ = +3.21×10⁻³ vs QED).
- A₂ that re-extracts a_e to **QED** (2-loop only): **−0.325745** (ΔC₂ = +2.73×10⁻³ vs QED).
- **Separation: ΔA₂ = 4.77×10⁻⁴ = 0.145% of |C₂|.**

To discriminate Outcome A from Outcome B, AVE's A₂ must be known to **better than 0.145%**. The parameter-free Route B A₂ is **+4.0%** off → **28× too imprecise**. This is the textbook definition of the prereg's **Outcome C**: *"A₂ not computable to sufficient precision to separate A from B → need higher order."*

> **FLAG-1 detail.** The prereg §2 quoted "δ_strain dissolves iff A₂ differs from C₂ by ΔC₂ ≈ +4.8×10⁻⁴ (A₂ ≈ −0.3280)." That +4.8×10⁻⁴ is numerically the *Q₀-to-QED separation width* (4.77×10⁻⁴ here), NOT the dissolution offset. The actual A₂ that lands on Q₀ is −0.3253, a ΔC₂ of +3.21×10⁻³ (≈7× larger). The prereg's −0.3280 figure appears to assume a faceplate that ALSO carries QED's 3+-loop tail (so only the 2-loop *piece* differs by the small amount), but the AVE faceplate as built is 2-loop-only — there is no AVE 3-loop term. Surfaced per flag-don't-fix; not silently reconciled.

## §5 — Anti-tuning audit (Guard 1) — the saliency A₂ is tuned to PDG

The saliency-closure A₂ = −0.3284 is the only AVE value that lands near the targets, so Guard 1 must be applied to it directly. **It fails the anti-tuning test:**

- The leaf locates the saliency via high-precision **bisection** at N_t = 2×10⁶: δ* = −0.01093 (`q-g19a-petermann-saliency-closure.md:76`). Bisection of *what against what?* — δ tuned so that C₂(δ) matches **PDG's −0.32848**. The PDG target IS the bisection objective.
- The closed form δ = −3α/2 is then back-fit to δ* (0.12% structural agreement, leaf:14), and the n_q-additivity postulate that yields it is admitted as "the single remaining intuitive step" (leaf:14, leaf:110) — alternatives (√n_q, n_q²) "give wrong magnitudes" *as judged against the same PDG target*.

So the saliency A₂'s 0.15% precision is **borrowed from PDG**, not earned from the substrate. Per Guard 1: *"if A₂ is TUNED to hit [the target] rather than computed from substrate → circular, REJECT and report C."* The saliency branch is rejected as a discriminator. **Only the parameter-free Route B A₂ = −0.3416 is admissible**, and it is Outcome C.

This is not a criticism of the saliency *mechanism* (the d/q split + Compton retardation are substrate-canonical); it is the observation that its *numerical precision at the C₂ level is set by the fit*, which is exactly the precision the discrimination needs. The honest substrate prediction is the symmetric +4% value.

## §6 — SM-counterfactual verdict (ave-discrimination-check, Guard 3)

The AVE-distinct content of this FT is precisely **whether AVE's A₂ ≠ QED's C₂ = −0.328478965**.

| Claim | SM (QED) predicts? | AVE-distinct? |
|---|---|---|
| A₁ = ½ (Schwinger) | YES (Schwinger 1948) | ❌ NO — consistency (both give ½) |
| A₂ (parameter-free) = −0.3416 | NO (QED gives −0.32848 from 2-loop diagrams) | ✅ YES — AVE's substrate self-energy gives a **distinct** value, +4.0% from QED |
| A₂ (saliency) = −0.3284 ≈ C₂ | YES (it was fit to C₂) | ❌ NO — tuned to QED, adds nothing (§5) |
| α_AVE⁻¹ (parameter-free) = 137.0259 | — | ✅ distinct, but lands on neither Q₀ nor QED |

**SM-counterfactual verdict:** the *parameter-free* AVE A₂ IS AVE-distinct (QED has no mechanism that produces −0.3416 at 2-loop; QED's 2-loop g-2 is −0.32848 by direct diagram computation). But the distinctness cuts the *wrong way for both outcomes*: AVE's honest A₂ disagrees with QED's C₂ by +4.0% — far more than the ~0.001% the dissolution hypothesis (Outcome A) would require, AND in a direction that overshoots past Q₀ rather than landing on it. So AVE is neither QED-identical (which would be Outcome B) nor Q₀-landing (Outcome A); the AVE-distinct A₂ is simply **too coarse to be a faceplate that resolves δ_strain at all**.
## §7 — Power-category lock (ave-power-category-check, Guard 2)

**Load-bearing quantity:** the second-order anomalous-moment shift Δa_e^(2) — the (α/π)² self-load the electron's LC tank imposes on the substrate measurement.

| Axis | Classification | Basis |
|---|---|---|
| A — Real vs Reactive | **REAL** (dissipative leg) | a_e is the per-cycle *dissipative* self-load (the g−2 anomaly is a measured energy-extraction observable), NOT the reactive Q = α⁻¹ chain. The dark wake τ_zx is a *retarded* (lossy) back-reaction — that is the dissipative signature. |
| B — Propagating vs Bound | bound (on-site tank mode) | second-order back-reaction localized to the unknot's LC tank |
| C — On-shell vs Off-shell | substrate real-rate | AVE treats the Schwinger/Petermann factors as real substrate-mode rates, not QED virtual-loop integrals (per `ave-power-category-check` Axis C canonical example) |
| D — Internal-tank vs External-matched | internal | a_e is intrinsic to the electron tank, not a detector-coupling efficiency |
| E — Substrate-mode vs Atomic | substrate-mode | Z-independent; set by ℓ_node-scale Cosserat trefoil dynamics + α |

**Guard 2 satisfied:** A₂ was built as the REAL-power dissipative self-load (dark-wake retarded correlation), explicitly NOT from the reactive Q-chain (Q = α⁻¹ = Q_vol+Q_surf+Q_line at `theorem-3-1-q-factor.md`). The reactive chain produces the geometric Q₀ = 4π³+π²+π; the dissipative chain produces a_e. These are the two distinct legs the prereg's faceplate framing rests on, and they were kept categorically separate.

## §8 — No cosmic-magnitude smuggling (Guard 4) — confirmed clean

The A₂ build uses only: the MEASURED a_e (for the inversion/comparison, never inside the build), the LOCAL Axiom-4 saturation kernel S(A)=√(1−A²), the (2,3) trefoil currents, the Compton retardation 1/ω_C, the 1/π² Schwinger form factor, and CODATA α (the coupling, via `constants.py`). **No f_R, no cosmic chirality fraction, no A-031-inaccessible parameter enters anywhere.** Direction-2 escapes the A-031 horizon as designed — the cosmic parameter never appears. (Confirmed by inspection of every input to `route_b_correlation`.)

## §9 — Consistency-vs-emergence classification

Per `consistency-vs-emergence`, the load-bearing comparison is "AVE A₂ vs QED C₂," and the inversion compares to CODATA-derived targets. **Dual-axis classification (Trigger 7, "AVE reproduces the 2-loop g−2"):**

- **Substrate-mechanism axis: Class B (axiom manifestation), NOT Class 2 emergence.** The Route B chain references canonical content (Axiom 4 kernel, (2,3) trefoil, Compton retardation, 1/π² Schwinger form factor) but contains a **requires-additional-postulate** step: the n_q-additivity assumption (leaf:110, "single remaining intuitive step") for the saliency, AND the τ_retard = 1/ω_C choice is geometrically *asserted*, not derived (the τ-scan in the driver shows the result is exactly zero at τ ∈ {π/2, π, 2π} and −0.876 at π/3 — only τ=1 gives −0.341). With a "requires-additional-postulate"/"asserted-without-tracing" step present, the substrate-mechanism axis is **Class B**, per Step 7. The canonical leaf does not self-classify above Class B either (Step 8a/8c: no promotion past canonical ceiling claimed here).
- **Observable axis: the parameter-free A₂ = −0.3416 is a Class E new prediction** (substrate-distinct: +4.0% from QED's 2-loop, experimentally distinguishable in principle). The saliency A₂ = −0.3284 is **Class 4 consistency** (replicates PDG by construction — it was fit). 

The α_AVE⁻¹ inversion itself is **Class C (consistency check)**: it routes through CODATA-derived inputs (measured a_e + CODATA α) via the faceplate-inversion identity; removing the CODATA inputs destroys it. The "0% match" question is moot because there is no match — α_AVE⁻¹ lands 34 gap-widths off. **Not headlined as emergence.**

## §10 — Honest closure + what would move this off Outcome C

**Rule 11 (honest closure):** the parameter-free substrate self-energy gives A₂ = −0.3416 at +4.0% precision — categorically (28×) too coarse to separate dissolution (Q₀) from internal-inconsistency (QED) at the 0.145%-of-C₂ level the discrimination demands. **This is a clean Outcome C.** The branch does not get debugged toward a rescue: the saliency A₂ that *would* land near the targets is tuned to PDG (§5) and is therefore inadmissible as a discriminator. The honest result is "inconclusive, pending a higher-precision parameter-free A₂."

**What this FT did establish (positive content):**
- The A₁ = ½ Schwinger leg is confirmed and AVE-consistent (not distinct).
- AVE's parameter-free 2-loop-analog A₂ exists and is computable (−0.3416, verified against corpus).
- The δ_strain question is **not resolvable from the second-order anomaly faceplate at current precision** — a sharp, useful negative: the (α/π)² lever arm is ~10⁻⁶, so a 10⁻⁴-scale extraction-frame offset would need a 0.1%-precision A₂ that the substrate does not yet deliver parameter-free.

**What would move it off Outcome C** (decisive either way):
1. A **parameter-free** A₂ to <0.145% — i.e. derive the τ_retard = 1/ω_C pinning and the d/q split from the K4-Cosserat Lagrangian (the Q-G47 Sessions-19+ work the leaf itself names, leaf:110), with NO bisection-against-PDG. If that lands A₂ on −0.3253 → **Outcome A**; if on −0.3257 → **Outcome B**; if it stays at −0.3416 → δ_strain is simply not a faceplate offset (a third, also-decisive reading: the residual is not in the 2-loop coefficient at all).
2. Note the sign: the parameter-free A₂ = −0.3416 currently lands BELOW both targets. If a refined parameter-free A₂ moved *toward* −0.3253 it would have to become *less* negative (toward QED's −0.32848 and beyond) — i.e. the +4% offset would have to reverse to a small positive offset. Worth flagging that the current substrate value overshoots in the more-negative direction.

## §11 — Cross-references

> → Driver: [`src/scripts/vol_2_subatomic/simulate_g2_direction2.py`](../src/scripts/vol_2_subatomic/simulate_g2_direction2.py) — A₂ build + inversion + τ-fragility scan
> → Primary: [`simulate_g2.py`](../src/scripts/vol_2_subatomic/simulate_g2.py) — A₁ = ½ Schwinger chain (unchanged)
> → Primary: [`q-g19a-petermann-saliency-closure.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md) (clm-v2sg8z) — the A₂ corpus source: Route B symmetric −0.3416 (line 58) + saliency −0.32846 (lines 92,95) + bisection δ* (line 76)
> → Primary: [`weak-coupling.md:22`](../manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/weak-coupling.md) — two-vertex α² self-energy seed
> → Primary: [`theorem-3-1-q-factor.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) (clm-rtdmsn) — α⁻¹ = Q₀ = 4π³+π²+π (the REACTIVE Q-chain; distinct from a_e's REAL leg per §7)
> → Reference engine (sibling repo, read-only): `AVE-QED/scripts/g2_research/q_g19_alpha_route_b_petermann.py` — original Route B implementation whose −0.3413 (τ=1) the worktree driver reproduces
> ↗ Method: this result is the prototype for `ave-external-provenance-check` — re-extract the raw observable through AVE's framework rather than deriving a correction to the SM-extracted number.
> ↗ Lineage: prereg §6 lineage — thermal FT-1 (falsified) → α²/24 (rejected) → dual-loading magnitude (A-031-blocked) → Direction-2 (this, Outcome C).
