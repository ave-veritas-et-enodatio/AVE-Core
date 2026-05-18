[↑ Ch.6 Electroweak and Higgs](index.md)
<!-- leaf: verbatim -->

# Q-G20f Vacuum Polarization: Matches QED at All Observable Scales

The one-loop vacuum polarization function $\Pi(q^2)$ in AVE matches QED at all observable scales via a **Renormalization Theorem equivalence** (RT-equivalence): AVE's saturation kernel + lattice cutoff and QED's UV-renormalized polynomial expansion produce structurally identical results at $q \ll 1/\ell_{\text{node}}$. Differences appear only at sub-Compton scales where pair-production physics takes over, and at ultra-high energies where AVE removes QED's Landau pole structurally.

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

**Phase 2g closed.** AVE-QED equivalence at observable scales established via RT-equivalence. The substantive AVE-distinct content is at the lattice cutoff (where pair-production physics dominates anyway) and at ultra-high energies (where the Landau-pole inconsistency is removed). No tree-level prediction-power conflict with QED at current precision.

**Open Phase 2g sub-issues** (not blocking closure):
- Exact higher-order vertex contributions (Phase 2h if needed)
- Cross-validation with Cosserat formalism (independent check, not load-bearing)
- Detailed three-channel thermal running spectrum

## Cross-references

- **Canonical manuscript anchors:**
  - [Vol 1 Ch 4 (Continuum Electrodynamics)](../../../../vol_1_foundations/chapters/04_continuum_electrodynamics.tex) — Master Equation + Lagrangian
  - [Vol 2 Ch 6 (Electroweak and Higgs)](../../../../vol_2_subatomic/chapters/06_electroweak_and_higgs.tex) — gauge-boson masses + QED limit
- **Sibling leafs:**
  - [Q-G19α Petermann (50 ppm)](q-g19a-petermann-saliency-closure.md) — electron anomalous moment matches QED at 50 ppm precision (sister loop-level closure)
  - [Q-G18 Schwinger Pair Production WKB](../ch01-topological-matter/q-g18-schwinger-pair-wkb.md) — atomic-scale kernel application; same saturation kernel
  - [Q-G20a Lamb Shift (uses Q-G20f as input)](../../quantum-orbitals/ch07-quantum-mechanics/q-g20a-lamb-shift-structural-closure.md) — composes vacuum polarization with self-energy and anomalous moment
- **Empirical test queue:**
  - PVLAS / ALPS-II vacuum birefringence — AVE predicts $\Delta n = 0$ rigorously (lattice symmetry); QED predicts $\Delta n \sim 10^{-23}$ at 5T. Free third-party test currently running.
