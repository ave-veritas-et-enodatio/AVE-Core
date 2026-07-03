[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-3i66gp]
-->

# Q-G20a Lamb Shift: Structural Closure via Today's Inputs

🔴 **2026-07-02 (α-factor cutoff correction + honesty re-tag, Rule 12):** the geometric UV cutoff was written as $1/\ell_{\text{node}} = m_e c/\alpha$ at :29,:39 below — **WRONG by a factor $1/\alpha$**. Canonical $\ell_{\text{node}} = \hbar/(m_e c)$ (electron-unknot.md:28, $C_{\text{loop}} = \hbar/(m_e c)$), so the momentum cutoff is $1/\ell_{\text{node}} = m_e c$ (the Compton momentum), **not** $m_e c/\alpha$. The corrected Bethe-log-equivalent runs $\alpha m_e c \to m_e c$, giving $\ln(1/\alpha) \approx 4.92$ — **not** $\ln(1/\alpha^2) = 2\ln(1/\alpha) \approx 9.84$. Corrected AVE log $4.92$ vs QED's $2.81$ is a **$1.75\times$ ratio** (was mis-stated as a $3.5\times$ gap). **Consequence for the headline:** this is a **likely structural match on the FORM** — AVE produces a Bethe-log-type self-energy of the right shape and order — with a **coefficient $\sim 1.75\times$ tension/echo**, NOT a clean numerical AVE prediction. The $+1010$ MHz self-energy magnitude was always **QED-imported** (consistency-class; there is no independent AVE numerical generator of $+1010$ MHz anywhere in the KB — the AVE log was a structural comparison, never the magnitude generator; see claim-quality.md rationale). Correcting the log therefore does **not** move the $\approx +1051$ MHz total (it was never generated from the AVE log), but the total "lands right" only because the dominant term is imported — so the honest headline is **structural/consistency-class, not a $0.65\%$ AVE precision result.** Body preserved below for audit; read the header for current status.

The 2S–2P hydrogen Lamb shift ($+1057.85$ MHz measured) is the QED canonical demonstration of vacuum-fluctuation effects. AVE reproduces the **form** of it (a Bethe-log-type self-energy of the right shape and order) at leading order by composing three substrate-native inputs, with the dominant self-energy magnitude QED-imported (consistency-class, see header):

| Contribution | QED value | AVE input | AVE-derived | Notes |
|---|---|---|---|---|
| Self-energy | $+1010$ MHz | Finite-size electron $T_{EM}\,\ell_{\text{node}} = m_e c^2$ (Vol 2 Ch 1) | $\approx +1010$ MHz (QED-imported magnitude) | Finite-size geometric integral gives the Bethe-log FORM; corrected AVE log $\approx 4.92$ vs QED $2.81$ ($1.75\times$). Magnitude is QED-imported (consistency), not an AVE numerical output — see header |
| Vacuum polarization | $-27$ MHz | Q-G20f $\Pi(q^2)$ closed | $\approx -27$ MHz | Matches QED at observable scales |
| Anomalous moment | $+68$ MHz | Q-G19α $a_e$ matched at 50 ppm (postulate-conditional; see note) | $\approx +68$ MHz | AVE inherits QED $a_e$ structurally |
| **Total (leading order)** | **$+1057.85$ MHz** | (sum) | $\approx +1051$ MHz | **$0.65\%$ off, but the total lands right only because the dominant self-energy term is QED-imported — consistency/structural-class, NOT a clean AVE precision prediction (see header)** |

The remaining $\sim 7$ MHz to measurement comes from higher-order QED corrections (Bethe logarithm at $\alpha^5$, recoil, nuclear size) — explicitly outside the leading-order scope.

> **Honesty note (Q-G19α two-stage framing):** the "$a_e$ matched at 50 ppm" input above is the Q-G19α **Stage 2** result, which is **conditional on the $n_q$-additivity postulate** (the corpus's "single remaining intuitive step," not derived). The Q-G19α **parameter-free** result (symmetric Route B forward, no postulate, no fit) is $C_2 = -0.3416$, **+4.0% off PDG**. The anomalous-moment contribution to the Lamb shift inherits this postulate-conditionality; only the leading-order Schwinger $a_e = \alpha/(2\pi)$ piece is unconditional. See [Q-G19α Petermann saliency closure](../../particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md).

## The three contributions in AVE language

### Self-energy contribution ($+1010$ MHz)

**QED mechanism:** electron radiates and reabsorbs photons; the Bethe logarithm integrates over all virtual-photon momenta from $\sim \alpha m_e c$ (orbital scale) to UV cutoff. Renormalization removes the UV divergence.

**AVE mechanism:** the electron is a closed flux tube of finite size $\ell_{\text{node}}$, with self-energy $T_{EM} \cdot \ell_{\text{node}} = m_e c^2$ (canonical at [Vol 2 Ch 1 Electron Unknot](../../particle-physics/ch01-topological-matter/electron-unknot.md)). The Bethe-logarithm-equivalent integral runs from $\alpha m_e c$ (orbital scale) to $1/\ell_{\text{node}} = m_e c$ (Compton / lattice cutoff, since $\ell_{\text{node}} = \hbar/(m_e c)$). **The UV divergence is naturally absent** — the cutoff is geometric, finite, and derivable from Axiom 1.

For the Lamb shift, only the **2S vs 2P differential** matters:
- $2S$ amplitude at $r = 0$: $|\psi_{2s}(0)|^2 = 1/(8\pi a_0^3)$
- $2P$ amplitude at $r = 0$: $0$

The electron's finite-size self-interaction at $r \sim \ell_{\text{node}}$ couples to $|\psi(0)|^2$:

$$\Delta E_{\text{SE,AVE}} = \frac{\alpha^4\, m_e c^2\, \langle\ln(...)\rangle}{6\pi\, n^3} \cdot \delta_{\ell,0}$$

where the logarithm runs from $\alpha m_e c$ to $1/\ell_{\text{node}} = m_e c$, giving $\ln(1/\alpha) \approx 4.92$. QED's Bethe logarithm for $2S_{1/2}$ is $\ln(K_{2S}/Z\alpha m_e c) \approx 2.81$ — a **$1.75\times$ ratio** (not the previously mis-stated $3.5\times$): the same functional FORM (Bethe-log self-energy) with a coefficient $\sim 1.75\times$ tension/echo. This is a **likely structural match on the form, NOT a numerical match**; the $+1010$ MHz magnitude used below is QED-imported (consistency-class), not generated from this AVE log — see the 🔴 header.

### Vacuum polarization contribution ($-27$ MHz)

**QED mechanism:** virtual $e^+e^-$ pairs near the nucleus screen the Coulomb potential at small $r$. Uehling potential modifies the energy of $2S$ (which has amplitude at $r = 0$) more than $2P$.

**AVE mechanism:** $\Pi(q^2)$ from [Q-G20f vacuum polarization closure](../../particle-physics/ch06-electroweak-higgs/q-g20f-vacuum-polarization.md). Q-G20f closure explicitly establishes "matches QED at observable scales; no Landau pole; UV saturation at $q \to \pi/\ell_{\text{node}}$." Net contribution to Lamb shift at relevant momentum scale $q \sim \alpha m_e c$ matches QED's Uehling result.

### Anomalous moment contribution ($+68$ MHz)

**QED mechanism:** the electron's $g$-factor deviation from $g = 2$ enters the Dirac–Coulomb spin-orbit Hamiltonian. For $2S_{1/2}$ (which has the Darwin term contribution at $r = 0$), the anomalous moment shifts the energy.

**AVE mechanism:** $a_e$ from [Q-G19α Petermann coefficient closure](../../particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md) — leading order matched via Schwinger $\alpha/(2\pi)$ (unconditional); second-order matched at 50 ppm via Route B + saliency, but the 50 ppm figure is **postulate-conditional on $n_q$-additivity** (the parameter-free symmetric Route B forward is $+4.0\%$ off PDG). AVE inherits QED's $a_e$ structurally.

## Status

**Structural match on the FORM** (Bethe-log self-energy of the right shape and order), coefficient $\sim 1.75\times$ tension/echo after the α-factor cutoff correction (corrected AVE log $4.92$ vs QED $2.81$). The $\approx +1051$ MHz total is a **consistency composition**: none of the three inputs is calibrated to the Lamb measurement, but the dominant self-energy magnitude ($+1010$ MHz) is QED-imported, not an AVE numerical output — so the total "landing" at $0.65\%$ is **not** a clean AVE precision prediction. This is a likely structural match, not a numerical match (Grant 2026-07-02).

**Full quantitative closure to $10^{-6}$ precision** requires explicit bound-state integration (Bethe-equivalent logarithm, recoil corrections, nuclear-size effects) — multi-session work, deferred. The structural match at leading order is the load-bearing claim.

## Cross-references

- **Composing closures:**
  - [Q-G19α Petermann (50 ppm, postulate-conditional; +4.0% parameter-free)](../../particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md) — anomalous moment input
  - [Q-G20f Vacuum Polarization](../../particle-physics/ch06-electroweak-higgs/q-g20f-vacuum-polarization.md) — vacuum-polarization input
  - [Electron Unknot (Vol 2 Ch 1)](../../particle-physics/ch01-topological-matter/electron-unknot.md) — finite-size self-energy input
- **Canonical manuscript anchors:**
  - Vol 2 Ch 7 (Quantum Mechanics and Orbitals) — hydrogen / 2S / 2P canonical framework
- **Related precision tests in same chapter:**
  - [Helium Symmetric Cavity](./helium-symmetric-cavity.md) — He IE at $-1.6\%$ from CODATA via mutual cavity loading
  - [Ionization Energy Validation Z=1 to 14](./ionization-energy-validation.md) — broader Z-sweep precision
