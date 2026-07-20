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
> g_{eff} \;=\; g_N + \sqrt{g_N \cdot a_0}\; \sqrt{1 - \frac{g_N}{a_0}}
> $$

<!-- label: eq:saturation_mond -->

> **🔴 CONTRADICTION FLAG — dated 2026-07-19 (flag-don't-fix; neither kernel edited, no side picked — routed to Grant for adjudication).** The drag-kernel functional form in the Resultbox above **disagrees with the engine that produced the headline SPARC residual.** Exposed by unbanked work recovered in the 2026-07-19 branch scrub (archive tag `archive/analysis/stage4-a1-eos-scope` @ `205d6e6b`, the S4-5 drag kernel-conflict flag). Both sides VERBATIM, with provenance:
> - **KB leaf (this file, `effective-galactic-acceleration-mond.md:15`) — LINEAR in the ratio:** $g_{eff} = g_N + \sqrt{g_N \cdot a_0}\; \sqrt{1 - \frac{g_N}{a_0}}$ — kernel factor $\sqrt{1 - g_N/a_0}$.
> - **Engine (`src/ave/gravity/galactic_mond_drag.py:49`) — QUADRATIC in the ratio:** `return np.sqrt(1.0 - r**2)` with `r = g_n / a_0`, i.e. $\sqrt{1 - (g_N/a_0)^2}$.
> - **Load-bearing:** the headline-confirmed **11.5% Q=1 mean SPARC residual** (87 galaxies; `claim-quality-closure-roadmap.md`, `dm-mechanism-unification.md:18`) rode the **QUADRATIC engine kernel** — "a kernel the manuscript does not state" (scope doc `205d6e6b`, verbatim). So the confirmed number and the canonical leaf form are not the same function.
> **NOT resolved here.** Per the scope doc's S4-5 gate this needs a reconciliation (SHA-pin the manuscript form to match the engine, or re-run + document the residual under the corrected kernel) — a **Grant/auditor** call. Implementer surfaces the conflict; does not pick a side and does not edit either kernel statement (both preserved verbatim above / at the engine).

---
