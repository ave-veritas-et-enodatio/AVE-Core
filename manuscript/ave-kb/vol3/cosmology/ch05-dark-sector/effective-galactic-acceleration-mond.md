[↑ Ch.5 Dark Sector](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-u86caq]
-->

## Effective Galactic Acceleration (Axiom 4 MOND)

When local Newtonian acceleration $g_N$ serves as the saturation amplitude (with $a_0$ as the yield limit), the drag contribution becomes:

> **[Resultbox]** *Effective Galactic Acceleration (Axiom 4 MOND)*
>
> $$
> g_{eff} \;=\; g_N + \sqrt{g_N \cdot a_0}\; \sqrt{1 - \left(\frac{g_N}{a_0}\right)^{2}}
> $$

<!-- label: eq:saturation_mond -->

> **✅ RESOLVED 2026-07-20 (MOND kernel adjudication; supersedes the 2026-07-19 🔴 contradiction flag; git carries the original).** The kernel factor in the Resultbox is the **QUADRATIC** $\sqrt{1 - (g_N/a_0)^2}$, matching the shipped engine that produced the headline (`galactic_rotation.py` → `saturation_factor` → `universal_saturation`; Axiom-4 Born–Infeld $n{=}2$). This **corrects a prior transcription** that displayed the LINEAR $\sqrt{1 - g_N/a_0}$ — the object of the 2026-07-19 S4-5 / #738 D7 contradiction flag.
> - **Empirical (non-discriminating):** the two-kernel SPARC contrast ([`research/2026-07-20_mond-kernel-adjudication_result.md`](../../../../../research/2026-07-20_mond-kernel-adjudication_result.md); driver `src/scripts/vol_3_macroscopic/mond_kernel_contrast.py`) found **KERNEL-DEGENERATE-ON-SPARC** on the gating Q=1 mean\|residual\| — quadratic **11.476%** vs linear **10.834%**, $|\Delta| = 0.642\% <$ frozen $\tau = 1.020\%$ (jackknife SE). The linear was nominally lower but sub-threshold and confounded with the +7.7% over-prediction bias, so the data do not pick a form.
> - **Form-level (decisive):** the DEGENERATE verdict routes to which form Axiom 4 forces. This leaf's own prose ("$g_N$ serves as the saturation amplitude, $a_0$ the yield limit") + the canonical kernel $S(A)=\sqrt{1-(A/A_\text{yield})^2}$ (INVARIANT-S2) give $\sqrt{1-(g_N/a_0)^2}$ — the QUADRATIC. The Maxwell small-amplitude limit kills the linear route (`research/2026-07-02_axiom4-buckling-kernel_result.md:21`).
> - **Headline unchanged:** the banked **11.5% Q=1** result always rode the quadratic engine; adopting the quadratic form required **zero engine change** (no kernel edited). The 2026-07-19 flag's cite of `galactic_mond_drag.py:49` was correct-in-substance (that module is also quadratic) but the SPARC headline actually rode `galactic_rotation.py` — cite corrected here.

---
