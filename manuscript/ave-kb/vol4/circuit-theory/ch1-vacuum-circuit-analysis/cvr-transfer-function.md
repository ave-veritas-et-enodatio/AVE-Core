[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Consolidation / translation leaf (consistency-vs-emergence: CONSISTENCY, not emergence). Re-expresses already-derived canon — the electron LC tank (clm-kezk9z/p5cf3t), alpha=1/Q (clm-rtdmsn), the magnetic-branch Gamma=-1 (clm-lv3uw1), the EE-circuit identity (clm-fy05jc/eemap1) — as the explicit substrate-native transfer function H(s). Fills the translation-circuit.md:189 H(s) gap (was: 'general H(s) pole-zero synthesis not mapped'). Originates no new derivation. PURE-SCALAR mass-dilatation H(s) (all-DERIVED); the (2,3) winding's chiral scattering is the orthogonal charge-'3', documented separately in common/window-blind-bounding-plane.md and never wired into this H(s) (the no-phasor-wire rule, master-equation.md:20)."
-->

# CVR Transfer Function $H(s)$ — the Electron Mass-Dilatation Resonator

This leaf consolidates the electron's mass-cage as an explicit **substrate-native transfer function** $H(s)$ — the AC small-signal response of the self-made nonlinear resonant LC cavity. It fills the one gap the [circuit translation table](../../../common/translation-tables/translation-circuit.md):189 flagged for the *Filter theory / transfer fn* row (⚠ "matched-$Z$ ($\Gamma=0$) case only; general $H(s)$ pole-zero synthesis not mapped"). The object is a **scalar $H(s)$** — the **mass-dilatation "3"** ([master-equation.md](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20) — whose pole pair sits at $s = -\alpha\omega_0/2 \pm j\omega_d$: the pole's distance from the $j\omega$ axis IS the per-cycle radiative leak $\alpha = 1/Q$. The $(2,3)$ winding's chiral scattering is the **orthogonal charge-"3"** ([window-blind-bounding-plane.md](../../../common/window-blind-bounding-plane.md)), never wired into this $H(s)$.

## §1 — Scope and classification

> **[Resultbox]** *Classification — consolidation / consistency (NOT emergence)*
>
> Per `consistency-vs-emergence`: every element here is an **EE re-expression of already-derived canon**.
> The 2nd-order pole structure is forced by the canonical LC tank (clm-kezk9z) + $\alpha=1/Q$ (clm-rtdmsn);
> the $\Gamma=-1$ short branch is the magnetic-branch saturation (clm-lv3uw1). This leaf carries `no-claim:`
> frontmatter and references its owning claims by cross-link. **This leaf is all-DERIVED scalar** (the
> mass-dilatation $H_{co}$); the chiral/winding content — the one STATED, engine-pending frontier — lives entirely
> in the orthogonal charge-"3" leaf ([window-blind-bounding-plane.md](../../../common/window-blind-bounding-plane.md)), never merged here.

The substrate is an LC network at minimal DOF (Axiom 1; [translation-circuit.md](../../../common/translation-tables/translation-circuit.md) §2). The electron is a topological defect locked into that network as a high-$Q$ resonant LC tank ([resonant-lc-solitons.md](resonant-lc-solitons.md):10). Its small-signal AC response around a DC operating point $A_0$ is a transfer function $H(s)$ — the object this leaf makes explicit.

## §2 — The co-polarized $H(s)$ (DERIVED from the LC tank + $Q=1/\alpha$)

A series-fed lossy LC resonator has the canonical 2nd-order transfer function

$$
H(s) \;=\; \frac{\omega_0^2}{s^2 + \dfrac{\omega_0}{Q}\,s + \omega_0^2}, \qquad
\omega_0 = \omega_{\text{local}}(A_0) = \omega_C\,S(A_0), \qquad Q = \frac{1}{\alpha}
$$

with $\omega_C = c_0/\ell_{node} \approx 7.76\times10^{20}$ rad/s the bond LC natural frequency (AC datasheet, $\omega_C$ derivation) and $S(A_0) = \sqrt{1-A_0^2}$ the Axiom-4 operating-point kernel (the varactor bias detunes the tank down — [op14-local-clock-modulation.md](op14-local-clock-modulation.md)). The pole pair:

$$
\boxed{\; s_{\pm} \;=\; -\frac{\omega_0}{2Q} \pm j\,\omega_0\sqrt{1-\frac{1}{4Q^2}}
\;=\; -\frac{\alpha\,\omega_0}{2} \pm j\,\omega_d \;}
$$

**The real part $-\alpha\omega_0/2$ is the radiative linewidth** — the pole sits a distance $\alpha/2$ (in units of $\omega_0$) to the left of the $j\omega$ axis, and that distance is exactly the per-cycle energy leak $1/Q = \alpha$ through the TIR boundary ([theorem-3-1-q-factor.md](theorem-3-1-q-factor.md):81, "only a fraction $1/Q=\alpha$ of the stored energy leaks per cycle"). The computed value matches to machine precision: `pole_real/ω₀ = −0.00364868 = −α/2` (`cvr_ee_sweep_metrics.json`).

| Quantity | Substrate-native form | Value | Provenance |
|---|---|---|---|
| Tank $Q$ | $1/\alpha$ | $137.036$ | DERIVED-FORM / **VALUE = echo** ([theorem-3-1-q-factor.md](theorem-3-1-q-factor.md):38, clm-rtdmsn) — see scope-correction note below |
| Resonance $\omega_0$ | $\omega_C\,S(A_0)$ | $7.76\times10^{20}\,S(A_0)$ rad/s | DERIVED (Ax 1 primitives) |
| Pole real part | $-\alpha\omega_0/2$ | $-0.00365\,\omega_0$ | DERIVED (= the $1/Q$ leak) |
| $-3$ dB bandwidth | $\omega_0/Q = \alpha\omega_0$ | $5.67\times10^{18}$ rad/s | DERIVED |
| Peak $|H|$ | $20\log_{10}Q$ | $42.7$ dB | DERIVED |

> **🔴 Scope correction (2026-06-19, Rule 12 — table row above PRESERVED).** The bare "DERIVED" on the **Tank $Q$** row over-stated the value's provenance. What is DERIVED is the **FORM** ($Q=1/\alpha$ as the per-cycle radiative-leak structure of the LC tank); the **VALUE** $137.036$ is an **echo at the value level** — adjudicated at [theorem-3-1-q-factor.md](theorem-3-1-q-factor.md):19 (keystone $\alpha$-verdict, value-scoped) and baked at the instance (`cvr_model.py:72` $Q_{\mathrm{TANK}}=1/\alpha$), NOT a first-principles derivation of 137. The $\alpha$-free cold cage does NOT reproduce 137 (cold-cage $Q\approx30.8$, `test_l3_mass_cage.py`:702). The other rows ($\omega_0$, pole-real, bandwidth, peak) are FORM-DERIVED but inherit the $\alpha$-echo through $Q$. This corrects the bare tag to match the canonical value-scope without altering the table.
>
> **Reconciliation note (base-crack #37 Item 3, 2026-06-19 — clm-rtdmsn DERIVED-vs-echo CLOSED).** The base audit flagged an apparent contradiction between this leaf's DERIVED tag and [theorem-3-1-q-factor.md](theorem-3-1-q-factor.md)'s "echo at the value level." NO contradiction: the #297 loaded-$Q$ reframe ([theorem-3-1-q-factor.md](theorem-3-1-q-factor.md):145 Amendment) settles it — $\alpha=1/Q$ is the **LOADED/radiative $Q$**, a vacuum$\leftrightarrow$EM **coupling** coefficient; the $H(s)$ **FORM** (2nd-order pole structure, $s_\pm=-\alpha\omega_0/2\pm j\omega_d$) is DERIVED, while the $\alpha$ **VALUE** $137.036$ stays an echo (loaded-$Q$ value derivability remains OPEN per that amendment). DERIVED-form / echo-value are the two faces of one object, not a clash. Item CLOSED.

## §3 — The winding's chiral scattering is the charge-"3" (separate leaf)

The electron is the mass-dilatation "3" **carrying** the orthogonal Cosserat $(2,3)$ winding-charge "3" ([master-equation.md](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20). The winding's chiral scattering — the $(L,R)$-handedness 2×2 with $S_{LR}\ne S_{RL}^*$ (the parity-odd, AVE-distinct signature) — is **charge-"3" content** and is documented in its own leaf:

> → Primary: [Window-Blind / Bounding-Plane — the Charge-Winding "3"](../../../common/window-blind-bounding-plane.md) — the $(L,R)$ chiral 2×2 scattering matrix ($S_{LR}\ne S_{RL}^*$, the computed $0.53$ non-reciprocity, STATED / needs the chiral-crystal engine), the EE form of the winding handedness.

This $H(s)$ stays the **pure-scalar mass-dilatation "3"**. The two "3"s are orthogonal and are **never wired together** — never wire the winding into the breather's phasor $(V_{inc},V_{ref})$ (the genesis-24 / $w_{pol}=0$ double-count, master-equation.md:20).

## §4 — Computed figure

![CVR transfer function: Bode + pole-zero](../../../../../src/scripts/vol_9_device/cvr_ee_sweep/_output/fig2_transfer_function_bode.png)

Re-runnable: `PYTHONPATH=$PWD/src python src/scripts/vol_9_device/cvr_ee_sweep/cvr_ee_sweep.py` (View 2). The Bode magnitude peaks at $42.7$ dB $=20\log_{10}(1/\alpha)$ at $\omega/\omega_C=1$; the phase inverts $0°\to-180°$ (the short-circuit boundary); the pole pair sits at $\mathrm{Re}/\omega_0 = -\alpha/2$.

## §5 — Discrimination (ave-discrimination-check)

- **CONSISTENCY (not AVE-distinct):** the $Q=1/\alpha$ peak is $\alpha$ in its original Sommerfeld coupling-strength meaning ([theorem-3-1-q-factor.md](theorem-3-1-q-factor.md):81) re-expressed as a Bode peak — a re-expression, not a new prediction. The 2nd-order roll-off is generic resonator physics.
- **The AVE-distinct content lives in the orthogonal leaves:** $|\Gamma|^2=1-\alpha$ in [cvr-reflection-smith.md](cvr-reflection-smith.md) (the mass-wall's radiative leak), and the parity-odd $S_{LR}\ne S_{RL}^*$ in [window-blind-bounding-plane.md](../../../common/window-blind-bounding-plane.md) (the charge-"3" winding). This scalar $H(s)$ is all-DERIVED consistency.

## §6 — Honest-status flags (carry verbatim per `ave-evidence-framing-discipline`)

- **Magnetic branch (PRIMARY):** the $\Gamma=-1$ short that closes the resonator is the **magnetic-branch** saturation $\mu_{eff}\to0 \Rightarrow Z\to0$ ([master-equation.md](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):78-79, clm-lv3uw1) — NOT the electric branch ($\varepsilon_{eff}\to0$, $Z\to\infty$, $\Gamma=+1$, open = dielectric rupture, a different object).
- **Sector vs gauge (2026-06-13):** the $\mu_{eff}\to0$-vs-$C_{eff}\to\infty$ split is partly the two **gauge** sides of one wall ($Z\to0$ inside $\leftrightarrow Z\to\infty$ outside, Möbius $Z\leftrightarrow1/Z$, $|\Gamma|=1$; [trampoline-framework.md](../../../common/trampoline-framework.md):641) — not a physical branch. The physical axis is the **two-"3"s** (mass-dilatation $\perp$ charge-winding, [master-equation.md](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20); this leaf is the mass-"3".
- **Exponent defect** ($n=S^{0.5}$ physical vs $S^{0.25}$ as-coded, `master_equation_fdtd.py:165`) affects $\Gamma$-from-$n$ magnitudes downstream — carried on the DC-operating-point and reflection leaves. The chiral $\chi$-STATED frontier now lives in the window-blind leaf.

## Cross-references

- **Owning canonical claims:** [theorem-3-1-q-factor.md](theorem-3-1-q-factor.md) (clm-rtdmsn, $\alpha=1/Q$); [master-equation.md](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):78-79 (clm-lv3uw1, magnetic-branch $\Gamma=-1$); [resonant-lc-solitons.md](resonant-lc-solitons.md) (clm-kezk9z/p5cf3t, the LC tank).
- **Orthogonal charge-"3" companion (never wired):** [Window-Blind / Bounding-Plane](../../../common/window-blind-bounding-plane.md) — the winding's chiral scattering ($(L,R)$ 2×2, $S_{LR}\ne S_{RL}^*$).
- **Companion sweep views:** [DC Operating Point](cvr-dc-operating-point.md) · [Reflection / Smith](cvr-reflection-smith.md) · [Phasor / Reactance](cvr-phasor-reactance.md) · [Stability / Eigenmode](cvr-stability-eigenmode.md).
- **Tool-axis:** [translation-circuit.md](../../../common/translation-tables/translation-circuit.md):189 (§4.5(b) *Filter theory / transfer fn* row this leaf consolidates).
- **Canonical script:** `src/scripts/vol_9_device/cvr_ee_sweep/cvr_ee_sweep.py` (+ `cvr_model.py` spine).

---
