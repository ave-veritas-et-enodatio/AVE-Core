# 121 — Plumber Challenge to Doc 120: χ_1 is a Cross-Sector Coupling, NOT a Diagonal Modulus

**Date:** 2026-05-16 late evening
**Branch:** `research/l3-electron-soliton`
**Status:** **PLUMBER RE-EXAMINATION — doc 120 was wrong about "by analogy with χ_K, χ_G." The corrected picture has χ_1/K_0 ~ α² from cross-sectional porosity, which CHANGES the framework's predictions:**
- **δ_strain (1st-order in χ_1)**: K_phys ~ α² m_e c² → matches observed (doc 117 §10 conjecture VALIDATED)
- **Ω_freeze ΔG/G (2nd-order from bipartite cancellation)**: ~ α⁴ ≈ 4×10⁻⁹ (doc 118 §9 prediction OFF BY α² — should be α⁴, not α²)

**Per Grant directive**: "critically think and research like an AVE electron plumber and challenge the approach"

---

## §0 TL;DR

**The doc 120 error**: I argued "χ_K = 12, χ_G = 3 are O(1), so by analogy χ_1, χ_2, χ_3 are also O(1)." This is **wrong** because:
- χ_K, χ_G are **DIAGONAL** Cosserat modulus corrections (bulk and shear self-coupling) — O(1) is natural
- χ_1, χ_2, χ_3 are **CROSS-SECTOR** couplings (strain ε to micro-curvature κ) — different physical class

In real EE, cross-sector / cross-port couplings have a different natural scale than diagonal couplings. In AVE specifically, the **cross-sectional porosity Φ_A ≡ α²** (Vol 3 Ch 1:91) is the geometric factor that governs how much one substrate sector "leaks" into a perpendicular sector. **The natural prior for χ_1 is χ_1/K_0 ~ Φ_A = α²** — same as the porosity that governs all other substrate cross-coupling phenomena.

**Implications**:
1. **doc 117 §10 K_phys ~ α² m_e c² conjecture is VALIDATED** — δ_strain naturally derives if χ_1 (1st-order entering K_phys) is α²-suppressed
2. **doc 118 §9 ΔG/G ~ α² prediction is WRONG by one factor of α²** — should be α⁴ (from 2nd-order bipartite cancellation of α²-suppressed χ_1)
3. **doc 119 + 120 conclusions need partial revision** — α² IS the right scale for cross-sector couplings, just NOT for the bipartite-cancellation residual (which is α⁴)
4. **CODATA G prereg §1.7 already accommodates this** via Outcome B (α³+ amplitude); should refine to Outcome B' (α⁴ specifically)

---

## §1 The plumber error in doc 120

Doc 120 §2 argued:
> *"χ_K = 12 and χ_G = 3 are dimensionless prefactors of substrate-natural-units (T_EM, ℓ_node) corrections to bulk and shear moduli. No α-suppression appears in their establishment. By analogy, the chirality cross-coupling moduli χ_1, χ_2, χ_3 are likely O(1) at substrate scale."*

**This "by analogy" step is the error.** Let me explain why with EE plumber framing:

### §1.1 Diagonal vs cross-sector couplings in EE

In a multi-sector elastic medium (3 translational DOFs + 3 rotational DOFs = 6 Cosserat DOFs per node), the elastic energy is:
$$U = \frac{1}{2} \begin{pmatrix} \varepsilon \\ \kappa \end{pmatrix}^T \begin{pmatrix} K & \chi \\ \chi^T & B \end{pmatrix} \begin{pmatrix} \varepsilon \\ \kappa \end{pmatrix}$$

where:
- **K**: diagonal block for translational strain (bulk + shear moduli)
- **B**: diagonal block for rotational strain (couple-stress moduli)
- **χ**: off-diagonal block coupling strain to curvature (the chirality cross-coupling)

The **diagonal blocks K and B** are set by the self-stiffness of each sector — these are O(1) in substrate-natural units (per Q-G47: χ_K = 12, χ_G = 3).

The **off-diagonal block χ** is set by how strongly the two sectors couple — this is a CROSS-PORT coupling in EE language. The natural EE prior for cross-port couplings is **substantially smaller** than diagonal couplings.

### §1.2 What sets the cross-sector coupling scale in AVE?

In AVE substrate physics, the universal cross-sector coupling scale IS the **cross-sectional porosity** Φ_A ≡ α² (per Vol 3 Ch 1:91):

> *"the effective differential solid angle is modified by the cross-sectional porosity (Φ_A ≡ α²). Because macroscopic wave transmission must pass through the discrete structural nodes, the effective differential solid angle is modified..."*

Plumber translation: the substrate's K4 nodes have a cross-section that's α² "transparent" to perpendicular-sector signals. Any cross-port / cross-sector coupling picks up Φ_A = α² as the natural geometric factor.

**Therefore**: χ_1/K_0 ~ Φ_A = α² is the natural plumber prior for the chirality cross-coupling, NOT O(1).

This is the SAME α² that appears in 9 corpus formulas (per doc 119 §1) — they're all manifestations of the universal cross-sectional porosity. **Doc 119's "multiple-mechanism heterogeneity" interpretation was partially wrong** — the α² across corpus instances IS unified at the cross-sectional-porosity level.

---

## §2 Revised framework predictions

### §2.1 δ_strain (1st-order in χ_1)

The electron-soliton's Golden Torus stiffness K_phys depends on how strongly the soliton's (R, r) parameters couple to the substrate Cosserat response. This is a CROSS-SECTOR coupling — the soliton's geometric parameters (translational sector) couple to substrate micro-curvature (rotational sector).

At **1st order in the cross-sector coupling**:
$$K_{\text{phys}} \sim K_0 \cdot \chi_1 / K_0 \cdot (\text{geometric factor}) \sim \alpha^2 \cdot m_e c^2$$

This matches the doc 117 §10 conjecture (K_phys ~ α² m_e c²) and gives predicted δ_strain ≈ 1.7×10⁻⁶ vs observed 2.225×10⁻⁶ — **~30% match validated** (was previously "reverse-engineered"; now derivable from cross-sectional porosity).

### §2.2 Ω_freeze ΔG/G (2nd-order from bipartite cancellation)

For bulk cosmic-scale G anisotropy, the bipartite K4 cancellation argument applies — A and B sublattices have opposite chirality, so 1st-order χ_1 contribution cancels at the bulk. The 2nd-order residual scales as χ_1²:

$$\frac{\Delta G}{G_{\text{iso}}} \sim \left(\frac{\chi_1}{K_0}\right)^2 \cdot \frac{4\pi}{15} \cdot P_2(\cos\theta) \cdot f_R$$

With χ_1/K_0 ~ α², this gives:
$$\frac{\Delta G_{\max}}{G_{\text{iso}}} \sim \alpha^4 \cdot \frac{4\pi}{15} \approx (5.3 \times 10^{-5})^2 \cdot 0.838 \approx 2.4 \times 10^{-9}$$

**Not α² as doc 118 §9 claimed. Should be α⁴.**

**This is BELOW CODATA G precision** (10⁻⁴) and ALSO BELOW JPL planetary-ephemerides precision (10⁻¹¹). At 2.4×10⁻⁹, the prediction is essentially undetectable with current technology.

### §2.3 Why this matters

The two derivations now have **internally consistent** χ_1/K_0 = α² (cross-sectional porosity):
- δ_strain works because K_phys is 1st-order in χ_1 (linear cross-sector coupling)
- ΔG/G is suppressed by additional α² because the bipartite cancellation eliminates 1st-order

This is what the framework SHOULD predict if χ_1 is naturally α² (porosity). The alternative scenarios (χ_1 ~ O(1) per doc 120, or χ_1 ~ α per doc 118 implicit assumption) **both have internal inconsistencies**.

---

## §3 Doc 120 reconsidered

The honest finding from doc 120 was: "Q-G47's existing χ_K = 12, χ_G = 3 are O(1) at substrate scale." This finding stands.

But doc 120's INTERPRETATION ("therefore χ_1 ~ O(1) by analogy") was wrong. χ_1 is a different physical class from χ_K, χ_G:
- χ_K, χ_G = diagonal modulus corrections → O(1) natural
- χ_1 = cross-sector coupling → α² natural (cross-sectional porosity)

The α²-suppression conjecture in docs 117/118 is **partially validated, partially needs revision**:
- doc 117 §10 (δ_strain): VALIDATED — K_phys ~ α² emerges naturally
- doc 118 §9 (ΔG/G): WRONG ORDER — should be α⁴ (2nd-order bipartite cancellation of α²-suppressed χ_1), not α²

---

## §4 What this implies for downstream work

### §4.1 Doc 117 §10

**Status update**: K_phys ~ α² m_e c² IS now derivable from first principles (cross-sectional porosity Φ_A = α² applied to soliton's geometric cross-sector coupling). The ~30% residual in predicted δ_strain (1.7×10⁻⁶ vs observed 2.225×10⁻⁶) reflects remaining uncertainty in κ_cubic^K4 (used rough 0.1 from v14 empirical) and thermal-driver prefactor (used 4α).

This is a substantive upgrade from "reverse-engineered matching condition" to "derivable from cross-sectional porosity at order 30%."

### §4.2 Doc 118 §9

**Needs correction**: ΔG/G prediction was α², should be α⁴ (~2.4×10⁻⁹). This is BELOW CODATA G precision AND below JPL planetary-ephemerides precision. CODATA G dataset re-analysis (Observable 7 per prereg §1.7) would NOT detect this signal at α⁴ amplitude.

The angular profile P_2(cosθ) still holds; only the amplitude is much smaller than originally claimed.

### §4.3 Doc 119 adjudication

**Partial revision needed**: the α² universal-operator interpretation IS partially correct — all 9 corpus α² appearances are manifestations of cross-sectional porosity Φ_A = α². But the relevant α^N for any specific observable depends on whether the observable is:
- 1st-order in cross-sector coupling: ~ α²
- 2nd-order from bipartite cancellation: ~ α⁴
- Higher-order: α^(2k) for k cross-sector couplings or k bipartite cancellations

The "multi-mechanism heterogeneity" framing of doc 119 was too pessimistic. The α² IS a unified universal operator (cross-sectional porosity); the suppression-order depends on how many cross-sector couplings × bipartite cancellations enter the observable.

This might warrant promoting to A-035-style canonical framework result (one operator = Φ_A = α², appears at various powers depending on observable structure).

### §4.4 Doc 120 framework

**Partially superseded by this doc**: the "by analogy with χ_K, χ_G" step was wrong. But doc 120's specific examination of candidate suppression mechanisms (§3.1-3.3) is still useful as a record of what doesn't work.

### §4.5 omega-freeze §3.2 Observable 7 + CODATA G prereg §1.7

**Need correction**: predicted amplitude is α⁴ ≈ 2.4×10⁻⁹, not α² ≈ 5×10⁻⁵. This is **below CODATA G precision** — the falsifier test as written (CODATA G dataset re-analysis) would NOT detect the signal even if framework is correct.

**Need to refine the empirical test**: at α⁴ amplitude, the test requires **JPL planetary-ephemerides precision (10⁻¹¹)** or specialized G-anisotropy experiments (atom interferometry, eLISA gravitational-wave-based G measurements, etc.). The prereg §1.7 should be updated to reflect this.

This is a significant downgrade in the empirical immediacy of Observable 7 — but the framework still makes a SHARP prediction (P_2 angular profile at α⁴ amplitude), just testable only at higher precision.

---

## §5 Recommended actions for Grant

This plumber re-examination changes the framework's empirical commitments substantially. Three downstream actions needed:

1. **Update doc 117 §10 honestly**: K_phys ~ α² m_e c² is now DERIVABLE from cross-sectional porosity Φ_A = α² (not just reverse-engineered). The ~30% residual is a legitimate ~30% match, not a back-fit.

2. **Update doc 118 §9 + omega-freeze §3.2 + CODATA G prereg §1.7**: predicted ΔG/G amplitude is α⁴ ≈ 2.4×10⁻⁹ (not α² ≈ 5×10⁻⁵). Falsifier test needs JPL planetary-ephemerides precision, NOT CODATA G precision. P_2 angular profile prediction stands.

3. **Update doc 119 adjudication**: the α² universal-operator interpretation IS partially valid (Φ_A = α² IS the unified cross-sectional porosity). Could warrant A-035-style canonicalization with the suppression-order depending on observable structure (α^(2k) for k cross-sector / bipartite-cancellation events).

Per "flag don't fix" discipline: **NOT auto-propagating these corrections.** Surface to Grant for adjudication first. The plumber re-examination may itself have an error I'm not seeing — would want Grant's intuition check before propagating substantial framework changes.

---

## §6 Honest self-check: where could this plumber re-examination be wrong?

**Possible errors in my plumber reasoning**:

1. **Cross-port couplings in K4-TLM may not be Φ_A = α²**. The α² in Φ_A is specifically the cross-SECTIONAL porosity (the 2D cross-section of 3D nodes). Cross-PORT couplings in K4-TLM (between adjacent nodes' 4 ports) might be O(1) instead, set by the scattering matrix S^(0) = 1/2 − δ_{ij}.

2. **Strain-to-curvature χ_1 may not be the same physical class as Φ_A**. The Cosserat micropolar tensor has its own coupling structure that may not reduce to "cross-sectional porosity." If χ_1 is set by the K4 lattice's specific micropolar geometry (not by porosity), the natural scale could be different.

3. **The bipartite cancellation residual structure** may not give exactly χ_1² — there could be other geometric factors that modify the suppression order.

4. **My interpretation of "1st-order in χ_1 for K_phys vs 2nd-order for ΔG/G"** may be incorrect. Both might be 1st-order, or both 2nd-order, depending on how the soliton + bulk-substrate coupling actually works.

**This is plumber intuition, not rigorous derivation.** The actual χ_1 derivation is multi-week Q-G47 Session 19+ work. My re-examination provides a CANDIDATE plumber-natural scaling (χ_1/K_0 ~ α² from porosity) that gives internally consistent predictions — but it's still a conjecture pending rigorous derivation.

---

## §7 Net status

- **Doc 120 conclusion** (χ_1 ~ O(1) by analogy) was too quick — the "by analogy" step ignored the diagonal-vs-cross-sector distinction
- **Doc 117 §10 conjecture** (K_phys ~ α²) is plumber-defensible IF χ_1 is 1st-order coupling and α²-suppressed by porosity
- **Doc 118 §9 prediction** (ΔG/G ~ α²) is plumber-wrong by one power of α; should be α⁴ from 2nd-order bipartite cancellation
- **Doc 119 adjudication** is partially right (α² IS recurring in corpus) and partially wrong (it IS unified at the porosity level, just with various suppression orders for various observables)
- **Doc 120 conclusion** is partially wrong (the "by analogy" step doesn't hold for cross-sector couplings)

Per "flag don't fix": hold all of this pending Grant's adjudication on whether the plumber re-examination is right OR whether my plumber reasoning has the additional errors flagged in §6.

The framework predictions are now MORE coherent (internally consistent χ_1/K_0 = α² across both derivations) but the CODATA G falsifier test becomes MUCH less immediate (α⁴ is below current precision; JPL-only).

---

## §8 Cross-references

- doc 117 §10 — δ_strain K_phys ~ α² (NOW derivable from porosity, per this doc)
- doc 118 §9 — Ω_freeze ΔG/G (WRONG ORDER per this doc; should be α⁴ not α²)
- doc 119 — α²-universal-operator adjudication (PARTIAL revision needed per this doc)
- doc 120 — χ_1/K_0 derivation attempt (this doc challenges its "by analogy" argument)
- omega-freeze §3.2 Observable 7 — amplitude needs correction
- CODATA G prereg §1.7 — falsifier amplitude needs correction (α⁴ instead of α²)
- Vol 3 Ch 1:91 — Φ_A ≡ α² cross-sectional porosity (the unifying universal operator)
- AVE-QED Q-G47 Sessions 3 + 17 — chirality moduli framework (still pending individual ξ_K1, ξ_K2 derivation per Session 17:49)

---

## §9 CORRECTION (Grant plumber pushback 2026-05-16 late evening)

Grant challenged this doc with the deeper plumber question: *"does that move (α²→α⁴) make fundamental AVE sense? does it match the axioms and regimes of operation and the overbraced chiral lavs k4 cosserat crystal?"*

**Answer**: doc 121's §1-§5 specific argument was WRONG in important ways. The plumber re-examination itself had plumber errors.

### §9.1 Φ_A = α² is cosmic-scale, NOT substrate-scale

Re-reading Vol 3 Ch 1:91 carefully:
> *"the effective differential solid angle is modified by the cross-sectional porosity ($\Phi_A \equiv \alpha^2$). Because macroscopic wave transmission must pass through the discrete structural nodes..."*

This is the COSMIC-SCALE integral over the Machian impedance from $r=0$ to $r=R_H$. **Not a substrate-scale cross-port coupling.**

At SUBSTRATE scale, the cross-port coupling between adjacent K4 ports is the scattering matrix $S^{(0)}_{ij} = \tfrac{1}{2} - \delta_{ij}$ per K4-TLM canonical — this is **O(1)**, not α².

§1.1's claim "the natural EE prior for cross-port couplings is substantially smaller than diagonal couplings, set by geometric porosity" was based on a generic EE intuition, but in AVE specifically, the substrate-scale K4-TLM scattering matrix is O(1). The α² appears at cosmic scale via the Machian integral over the cosmic horizon, not at substrate-scale cross-port coupling.

**Doc 121 §1-§3 incorrectly conflated cosmic-scale Φ_A with substrate-scale χ_1 prior.** This is the same kind of scale-mixing error that doc 119 §2 caught for the α² heterogeneity issue.

### §9.2 Closure attempt using over-braced K4 Cosserat first principles (per Grant's plumber question)

The over-braced K4 Cosserat structure (Vol 3 Ch 1:32-40) provides a SUBSTRATE-NATIVE candidate for χ_1's natural scale. The mechanism:
- K4 substrate at $p^* = 8\pi\alpha$ packing fraction
- Secondary spatial links at $1.187 \cdot \ell_{node}$ (over-bracing)
- Under shear: secondary links buckle, coupling to microrotational DOFs $\theta_i$
- This buckling IS the χ_1 cross-coupling mechanism

**Dimensional analysis of χ_1**:
- $\chi_1$ has units of energy × length × area$^{-1}$ (since $\chi_1 \epsilon \kappa$ is energy density, with ε dimensionless and κ = 1/length)
- $\chi_1$ in substrate-natural units: $\chi_1 = \tilde\chi_1 \cdot T_{EM} \cdot \ell_{node}$ where $\tilde\chi_1$ is dimensionless O(1) prefactor

For dimensionless ratio:
$$\frac{\chi_1}{K_0 \cdot \ell_{node}} = \frac{\tilde\chi_1 \cdot T_{EM} \cdot \ell_{node}}{(T_{EM}/\ell_{node}^2) \cdot \ell_{node}} = \tilde\chi_1 \cdot \ell_{node}^2$$

Hmm — that's not dimensionless. Let me re-do.

$K_0 = T_{EM}/\ell_{node}^2$ has units of $[N/m^2] = [Pa]$.
$\chi_1$ has units of $[Pa \cdot m]$ (since $\chi_1 \cdot \varepsilon \cdot \kappa$ must be $[Pa] = [Pa] \cdot 1 \cdot [1/m]$).

So $\chi_1/K_0$ has units of length, and dimensionless ratio is $\chi_1/(K_0 \cdot \ell_{node})$.

If $\chi_1/(K_0 \cdot \ell_{node}) \sim O(1)$ at substrate (full chirality strength per K4-TLM canonical): $\chi_1 \sim K_0 \cdot \ell_{node}$ at substrate scale.

### §9.3 What the bipartite cancellation actually gives

Per doc 118 §9 framework: $\delta_\chi \equiv \chi_1 \cdot \kappa_0 / K_0$ where $\kappa_0$ is the substrate chirality magnitude.

If $\kappa_0 \sim 1/\ell_{node}$ (full O(1) chirality at substrate scale):
$$\delta_\chi = \chi_1/(K_0 \cdot \ell_{node}) \sim O(1)$$

Then bulk observable from bipartite K4 cancellation: ΔG/G ~ $\delta_\chi^2 \cdot$ (cancellation residual factor)

**The "cancellation residual factor" is what's load-bearing** — it measures how much A/B chirality fluctuations don't fully cancel at the cosmic scale.

For STRICT bipartite K4 with zero fluctuations: residual → 0, ΔG/G → 0.

For finite-T thermal fluctuations at T_CMB (~k_B·T/m_e c² ~ 4.6×10⁻¹⁰): negligible residual, ΔG/G ~ 10⁻¹⁹.

For COSMIC-FORMATION-EPOCH fluctuations (~ε_form set by parent BH spin + formation T): residual depends on cosmic initial conditions.

### §9.4 The honest answer: amplitude is FUNDAMENTALLY UNDETERMINED without parent BH parameters

This is the **A-031 cosmic-parameter horizon at work** — the parent BH parameters (mass M, spin J, formation temperature) are INACCESSIBLE from inside, but they determine the cosmic chirality texture amplitude $f_R$.

**Framework predictions that ARE determined**:
- ✓ Angular profile: $P_2(\cos\theta_{\hat{n} \cdot \hat{\Omega}_{freeze}})$ sharply
- ✓ Direction: $\hat{\Omega}_{freeze}$ at CMB axis-of-evil $(l=174°, b=-5°)$
- ✓ Sign / phase: depends on $f_R$ sign (whether parent BH spin sets +R or +L handed I4_132)

**Framework predictions that are UNDETERMINED**:
- ✗ Amplitude — depends on cosmic chirality fraction $f_R$ at formation, which depends on parent BH parameters (inaccessible per A-031)
- ✗ Specific $\alpha^N$ for any N — the framework doesn't naturally predict $\alpha^2$ vs $\alpha^4$ vs anything else without knowing $f_R$ at formation

### §9.5 Net verdict on the α² vs α⁴ vs anything else question

**Both doc 118 §9 (α²) and doc 121 §2-3 (α⁴) over-claim.**

Doc 118 §9 claimed α² via "natural framework prior" without derivation. Doc 121 §2-3 claimed α⁴ via scale-mixed argument (cosmic Φ_A applied to substrate coupling). **Neither rigorously derives the amplitude from substrate first principles.**

The honest framework prediction, per the over-braced K4 Cosserat structure + A-031 cosmic-parameter horizon:

$$\boxed{\frac{\Delta G(\hat{n})}{G_{\text{iso}}} = -\frac{4\pi}{15} \cdot \delta_\chi \cdot f_R \cdot P_2(\cos\theta_{\hat{n} \cdot \hat{\Omega}_{\text{freeze}}})}$$

where:
- Angular profile $P_2(\cos\theta)$: SHARP framework prediction (independent of amplitude)
- $\delta_\chi$: substrate chirality coupling, O(1) at full chirality, undetermined without Q-G47 Session 19+ derivation
- $f_R$: cosmic chirality fraction at I4_132 formation, INACCESSIBLE per A-031 cosmic-parameter horizon
- Net amplitude: $\delta_\chi \cdot f_R$ is the product of two undetermined factors; could be anywhere from $O(1)$ (if both are unsuppressed, which is excluded by CODATA G) down to $\alpha^N$ for arbitrary N (depending on cancellation residual + cosmic formation conditions)

**The empirical falsifier per CODATA G prereg §1.7 is correctly framed as "α^N for some N ≥ 2, undetermined."** Specifying N = 2 (doc 118) or N = 4 (doc 121) was over-claiming.

### §9.6 What this means for the propagation question (Items 3+4 from peer review)

**Neither α² (doc 118) nor α⁴ (doc 121) should propagate as a specific numerical prediction.** Both were over-claims based on unverified substrate-physics conjectures.

**The KB and prereg should stay at the bracket-language** ("α^N for some N ≥ 2, undetermined") — which is what omega-freeze §3.2 and CODATA G prereg §1.7 CURRENTLY say after the doc 119 adjudication downgrade. **No further propagation needed.**

This means peer-review Items 3+4 should be ABANDONED — the corrections those items would make (α² → α⁴) are themselves not warranted.

### §9.7 What WOULD close this

For the framework's G-route prediction to have a specific α^N:

1. **Derive $\delta_\chi$ rigorously** from K4 → A_4 → 2T ⊂ SU(2) chain via Q-G47 Sessions 19+ multi-week ξ_K1, ξ_K2 individual computation
2. **Set bounds on $f_R$** from cosmic-formation conditions — even though parent BH parameters are inaccessible per A-031, the post-formation cosmic-substrate dynamics may constrain $f_R$ within bounds (e.g., $f_R \in [0, 1]$ trivially; tighter bounds from CMB anisotropy budget?)
3. **Independent empirical test** at the predicted angular profile $P_2(\cos\theta)$ — even without a sharp amplitude, the angular SHAPE is testable by binning CODATA G measurements along $\hat{\Omega}_{freeze}$

Without (1) + (2), the framework's amplitude prediction is genuinely undetermined. The sharp prediction is the angular profile only.

---

## §10 Final verdict (per Grant's plumber pushback closure)

Both doc 118 §9 α² and doc 121 §1-§5 α⁴ are OVER-CLAIMS. The honest framework prediction is:
- Angular profile $P_2(\cos\theta)$: sharp
- Direction: $\hat{\Omega}_{freeze}$ at $(l=174°, b=-5°)$
- Amplitude: undetermined ($\alpha^N$ for N ≥ 2, where N depends on cancellation residual + cosmic formation, both genuinely open)

Items 3+4 from the peer review should be ABANDONED — the omega-freeze §3.2 and CODATA G prereg §1.7 ALREADY use the bracket language ("α^N undetermined") and should stay that way.

Doc 117 §10's K_phys ~ α² is similarly an inferred matching condition, NOT a derivation. The framework predicts the MECHANISM (anharmonic K4 cubic + thermal fluctuations + Cosserat coupling) sharply, but the amplitude requires either independent χ_1 derivation OR matching to observed δ_strain.

The genuine sharp framework predictions across all the open derivation arcs:
- Mechanism class: clearly defined (saturation kernel, bipartite K4, Cosserat coupling, cosmic chirality)
- Angular / functional profile: clearly defined ($P_2$, $\sqrt{1-A^2}$, $\sqrt{2\alpha}$, etc.)
- Amplitude: requires either Q-G47 Session 19+ closure OR empirical anchor

This is the framework's actual epistemic status — and it's MORE HONEST than either α² or α⁴ specifically.
