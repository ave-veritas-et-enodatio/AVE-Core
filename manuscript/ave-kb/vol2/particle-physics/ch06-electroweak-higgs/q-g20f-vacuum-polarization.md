[↑ Ch.6 Electroweak and Higgs](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-bqtasn]
-->

# Q-G20f Vacuum Polarization: Matches QED at All Observable Scales

> 🔴 **QED-NORMALIZATION CORRECTION (2026-07-03; Rule-12 — body preserved below, git is the trail).**
> The E-route birefringence ratio "$7.5/\alpha^3\approx1.93\times10^7$" referenced below carries an understated
> QED denominator. **Corrected (v3 headline, single instantaneous footing — OPTION-B re-freeze 2026-07-07):
> $3.75\pi/\alpha^2\approx2.2\times10^5$** (the 2026-07-03 QED-normalization step gave the propagating/mixed-footing
> $7.5\pi/\alpha^2\approx4.42\times10^5$, exactly double via the $\langle\cos^2\rangle=\tfrac12$ carrier average; no
> order of magnitude or falsifier verdict changes). The static-B
> null verdict and the vacuum-polarization matching are UNAFFECTED. Canonical:
> [`../../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`](../../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md);
> reconciliation `research/2026-07-03_birefringence-qed-normalization-correction.md`.

The one-loop vacuum polarization function $\Pi(q^2)$ in AVE matches QED at all observable scales via a **Renormalization Theorem equivalence** (RT-equivalence): AVE's saturation kernel + lattice cutoff and QED's UV-renormalized polynomial expansion produce structurally identical results at $q \ll 1/\ell_{\text{node}}$. Differences appear only at sub-Compton scales where pair-production physics takes over, and at ultra-high energies where AVE removes QED's Landau pole structurally.

> 🔴 **SCOPED-IMPORT RE-TAG (2026-07-14; #685 QED-TRACE beta-gate verdict — body below preserved per KEEP-BOTH, git is the trail).**
> The "**Identical** (RT-equivalence)" Status cells in the table below (the $\Pi(q^2)$, running-$\alpha$, and Uehling
> rows) and the prose assertions "*no way to distinguish AVE from QED … structural inevitability*" and "*AVE's loop
> predictions must agree with QED's … by the RT theorem*" are **re-tagged from argued-match to SCOPED IMPORT**. The
> QED-TRACE beta-function gate ([`research/2026-07-14_qed-trace-beta-gate_RESULT.md`](../../../../../research/2026-07-14_qed-trace-beta-gate_RESULT.md) §7 scope boundary; PR #685) computed the two-body
> saturation-dressed force and found it **WRONG-FORM** for QED running (a clean power law, not a `ln(q)`; wrong sign on
> the transfer register). **Mandatory boundary (per the §7 scope note — paraphrased; the "UNPROBED, NOT CLOSED" clause is verbatim):** *the beta gate (PR #685) proved
> WRONG-FORM for the two-body pointwise route; **the many-body scale-integrated medium-response route is UNPROBED, NOT
> CLOSED** (not pre-judged here).*
> Logarithms routinely emerge from analytic kernels via scale-integration (QED's own vacuum-polarization `ln(q)`
> integrates algebraic integrands), so the analyticity kill is proven **only** for the pointwise/pairwise objects — it
> does **not** close the log route in general. The rows survive as a **consistency-scaffold appeal** (solidity 0.60,
> "use as input only, don't build deeper"), not as a computed match. Register-class: CONSISTENCY / ECHO (the saturation
> dress is charge-agnostic). Companion re-tag: [`../../claim-quality.md`](../../claim-quality.md) (clm-bqtasn) rationale block.

## The structural match

At currently-accessible scales ($q \ll 1/\ell_{\text{node}} = m_e c/\hbar$):

| Quantity | AVE | QED | Status |
|---|---|---|---|
| Polarization $\Pi(q^2)$ | $-(\alpha/3\pi)\, q^2 \ln(q^2/m_e^2)$ at low $q$ | $-(\alpha/3\pi)\, q^2 \ln(q^2/m_e^2)$ at low $q$ | **Identical** (RT-equivalence) |
| Running coupling $\alpha(q^2)$ | $\alpha(0)/[1 - \Pi(q^2)/q^2]$ | $\alpha(0)/[1 - \Pi(q^2)/q^2]$ | **Identical functional form** |
| Uehling potential | matches QED | $V_{\text{Uehling}} \propto -\alpha(\alpha/r) \exp(-2m_e r/\hbar)$ | **Identical at observable scales** |

**No way to distinguish AVE from QED via vacuum polarization at currently-accessible scales.** The match is by structural inevitability (Renormalization Theorem equivalence), not coincidence.

## The mechanism

AVE Master Equation derived Lagrangian:
$$\mathcal{L}_{\text{AVE}} = \frac{1}{2c^2}\, K(V)\, (\partial_t V)^2 - \frac{1}{2}(\nabla V)^2$$

where $K(V) = 1/\sqrt{1-(V/V_{\text{yield}})^2}$ is the saturation-kernel-derived coefficient (Axiom 4 inverse-kernel for capacitance). The kernel expansion to cubic order gives a $V^3$ vertex:

$$\mathcal{L}_{\text{cubic}} = \frac{1}{4 c^2 V_{\text{yield}}^2}\, V^2 (\partial_t V)^2 + \text{(total-derivative terms via IBP)}$$

This vertex computes the one-loop polarization integral with the **Brillouin Zone (BZ) geometric cutoff** at $|\vec{k}| = \pi/\ell_{\text{node}}$ — the substrate's natural UV boundary. The integral converges automatically without UV-renormalization counterterms.

## Why this works: RT-equivalence

The Renormalization Theorem states that any local relativistic field theory with the same low-energy gauge content gives the same observable predictions after renormalization, up to finite counterterms. AVE is a local relativistic field theory (Axiom 3 Minimum Reflection Principle) with the same low-energy U(1) gauge content as QED (Maxwell Lagrangian in the linear regime). Therefore, AVE's loop predictions must agree with QED's at observable scales by the RT theorem.

The substantive AVE-distinct claim is **where the agreement breaks**:

### AVE-distinct beyond observable scales

| Regime | AVE | QED | Discriminator |
|---|---|---|---|
| **Sub-Compton** ($q \sim 1/\ell_{\text{node}}$) | $\Pi/q^2$ saturates; $\alpha$ stops running | $\Pi/q^2$ continues logarithmic growth | Structural at $q \hbar c \sim 0.5$ MeV; coincides with pair-production threshold (different physics) |
| **Ultra-high energy** ($q \gg m_e c$, hypothetical) | Bounded by geometric cutoff $\pi/\ell_{\text{node}}$ | Landau pole at $q \sim m_e \exp(3\pi/(2\alpha))$ | AVE removes Landau-pole inconsistency structurally |
| **Cosmological running of $\alpha$** | Three-channel thermal running via CMB strain | Standard running | $\delta_{\text{strain}}$ at $T_{\text{CMB}}$; potential precision-experiment discriminator |

### Novel chiral piece

AVE's chiral Laves K4 Cosserat substrate (Axiom 1) introduces an additional **chiral piece** in the polarization tensor for circular polarization, $\alpha$-suppressed. Potential precision-experiment discriminator at high-precision polarimetry (PVLAS / ALPS-II vacuum-birefringence class experiments).

## Status

**Phase 2g closed — as a SCOPED IMPORT (re-tagged 2026-07-14, #685; see the header note).** AVE-QED equivalence at observable scales is a scoped consistency-import via RT-equivalence, **not** a computed match: the beta-gate proved the two-body pointwise route WRONG-FORM, and the many-body scale-integrated screening-sum route is UNPROBED, NOT CLOSED. The substantive AVE-distinct content is at the lattice cutoff (where pair-production physics dominates anyway) and at ultra-high energies (where the Landau-pole inconsistency is removed). No tree-level prediction-power conflict with QED at current precision.

**Open Phase 2g sub-issues** (not blocking closure):
- Exact higher-order vertex contributions (Phase 2h if needed)
- Cross-validation with Cosserat formalism (independent check, not load-bearing)
- Detailed three-channel thermal running spectrum

## Cross-references

- **Canonical manuscript anchors:**
  - Vol 1 Ch 4 (Continuum Electrodynamics) — Master Equation + Lagrangian
  - Vol 2 Ch 6 (Electroweak and Higgs) — gauge-boson masses + QED limit
- **Sibling leafs:**
  - [Q-G19α Petermann (50 ppm, postulate-conditional)](q-g19a-petermann-saliency-closure.md) — electron anomalous moment matches QED at 50 ppm precision **only conditional on the $n_q$-additivity postulate**; the parameter-free symmetric Route B forward is $+4.0\%$ off PDG (sister loop-level closure)
  - [Q-G18 Schwinger Pair Production WKB](../ch01-topological-matter/q-g18-schwinger-pair-wkb.md) — atomic-scale kernel application; same saturation kernel
  - [Q-G20a Lamb Shift (uses Q-G20f as input)](../../quantum-orbitals/ch07-quantum-mechanics/q-g20a-lamb-shift-structural-closure.md) — composes vacuum polarization with self-energy and anomalous moment
- **Empirical test queue:**
  - PVLAS / ALPS-II vacuum birefringence — AVE predicts $\Delta n = 0$ rigorously **under static $\mathbf B$** because the $\mu$-grade is an ideal relativistic inductor keyed on circulating current $I$ (not on $|\mathbf B|$): a static $\mathbf B$ has no $\partial\mathbf B/\partial t$ to load it, so $S_\mu=1$, $\delta n_\mu=0$ (NOT a "lattice symmetry" argument — see [`pvlas-static-b-verdict.md`](../../../vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md)). QED predicts $\Delta n \sim 10^{-23}$ at 5T. The PVLAS null is therefore **consistent with AVE**, not a falsifier; the discriminating measurement is the **E-route** ([`vacuum-birefringence-e4.md`](../../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md), $7.5/\alpha^3\approx1.93\times10^7$).
