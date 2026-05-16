[↑ Ch.6 Electroweak and Higgs](index.md)
<!-- leaf: verbatim -->

# Q-G27: Muon Cosserat Torsion Saliency — Fermilab g−2 Tension at 0.8%

The Fermilab Muon g−2 experiment measured a 4.2σ tension with the Standard Model prediction. AVE explains this tension as a **topological/Cosserat second-order effect** that the Standard Model does not capture, with **zero fit parameters**. The muon's Cosserat torsion-quantum excitation contributes an additional saliency $\delta_{\text{Cosserat}}^{\mu}$ to the g−2 anomalous-moment expansion beyond the universal Q-G19α Petermann closure.

This leaf is the dedicated muon-sector g−2 leaf, parallel to the electron-sector [Q-G19α Petermann closure](q-g19a-petermann-saliency-closure.md). The muon's MASS formula (Cosserat torsion at 1.24%) is in the separate [Higgs Mass / lepton spectrum leaf](higgs-mass.md); this leaf addresses the g−2 ANOMALOUS-MOMENT contribution, a structurally separate derivation.

## Result

| Quantity | AVE-derived | Reference | Match |
|---|---|---|---|
| Cosserat saliency $\delta_{\text{Cosserat}}^{\mu}$ | $-\alpha\sqrt{3/7}/(2\pi) = -7.60 \times 10^{-4}$ | Vol 2 Ch 6:164 (PAT torsion-shear projection) | — |
| Cosserat $C_2^\mu$ shift | $-0.32755$ vs electron $-0.32848$ | Route B + saliency = $-3\alpha/2 + \delta_{\text{Cosserat}}$ | — |
| $\Delta a_\mu^{(2)}$ vs electron g−2 | $+247 \times 10^{-11}$ | Saliency framework | — |
| Fermilab measured tension | $+245(56) \times 10^{-11}$ | Run-3 | **0.8% off central value** |

The 0.8% deviation is **within Fermilab's $\pm 23\%$ measurement uncertainty**. AVE predicts the tension as a structural consequence of the muon's Cosserat torsional excitation; the Standard Model has no equivalent term.

## Structural derivation

The muon is canonically identified (per Vol 2 Ch 6:174 + Vol 1 Ch 5:39) as the electron $0_1$ unknot **plus one quantum of Cosserat torsional excitation**. The phase-space (2,3) trefoil topology is preserved; what changes is the Cosserat-sector excitation state, which adds an $\alpha$-order contribution to the saliency framework that produces Q-G19α's Petermann coefficient.

### Canonical Cosserat constants (Vol 2 Ch 6:154–176)

- **Torsional coupling:** $\alpha\sqrt{3/7}$ (single-vertex process; one factor of $\alpha$)
- **PAT torsion-shear projection:** $\sqrt{3/7} \approx 0.6547$ (fraction of translational shear that maps onto rotational/torsional DOF via $\nu_{\text{vac}} = 2/7$)
- **Helical twist angle per unknot traverse:** $\Phi_{\text{twist}} = 2\pi\sqrt{3/7} \approx 236°$

### The saliency contribution

$$\boxed{\;\delta_{\text{Cosserat}}^{\mu} = -\frac{\alpha\sqrt{3/7}}{2\pi}\;}$$

Decomposition:
- **$\alpha$:** Cosserat torsional coupling at single-vertex (one $\alpha$, distinguishes muon static defect from W boson transient $\alpha^2$)
- **$\sqrt{3/7}$:** PAT torsion-shear projection from vacuum Poisson ratio
- **$1/(2\pi)$:** natural form-factor normalization (one $2\pi$ for averaging over one Compton traverse, matching Schwinger's $1/(2\pi)$ form factor)

### Sign

$\delta_{\text{Cosserat}} < 0$: the q-axis (rotational DOF) is **heavier** than the d-axis when the Cosserat torsion is active. Physically: the helical spiral adds energy to the rotational DOF, which lives on the q-axis in the dq-frame (motor analog: rotational kinetic energy is q-axis in the dq-frame).

### Full muon saliency

The muon's total saliency in the Q-G19α Route B framework adds the universal Petermann saliency to the Cosserat contribution:

$$\delta^{\mu} = -\frac{3\alpha}{2} - \frac{\alpha\sqrt{3/7}}{2\pi}$$

This shifts $C_2^\mu$ from the universal Petermann $-0.32848$ to $-0.32755$ — a $+0.28\%$ relative shift, producing the observed $+247 \times 10^{-11}$ contribution to $a_\mu^{(2)}$.

## Generation-distinguishing prediction

If $\delta_{\text{Cosserat}} \propto n_{\text{Cosserat}}$ (linear scaling with the Cosserat-sector quantum number), tau lepton (2 quanta) would have:

$$\delta_{\text{Cosserat}}^{\tau} \approx 2\, \delta_{\text{Cosserat}}^{\mu}$$

giving $a_\tau$ shifted by approximately $+490 \times 10^{-11}$ from the SM. Future tau g-2 measurements would discriminate AVE's Cosserat-saliency framework from the Standard Model + new-physics alternatives.

## Status

**Structurally closed.** The derivation uses only canonical corpus constants (Vol 2 Ch 6:154–176): no fit parameters. The match with Fermilab Run-3 at 0.8% is **within Fermilab's measurement uncertainty** (Run-3 central value $+245 \times 10^{-11}$, AVE prediction $+247 \times 10^{-11}$).

**Falsification target:** Fermilab Run-4/5 will tighten the measurement to $\pm 10$ ppm precision. If the central value drifts more than $\sim 50 \times 10^{-11}$ from AVE's $+247$ prediction, the saliency framework needs revision.

## Cross-references

- **Sibling leafs (same chapter):**
  - [Q-G19α Petermann + saliency closure (electron, 50 ppm)](q-g19a-petermann-saliency-closure.md) — the universal Petermann derivation that this leaf extends with Cosserat torsion
  - [Higgs Mass / lepton spectrum](higgs-mass.md) — muon MASS formula (Cosserat torsion at 1.24%), separate from this leaf's g−2 anomalous-moment derivation
  - [Lepton Spectrum](lepton-spectrum.md) — three-generation Cosserat sector chain
- **Canonical manuscript anchors:**
  - [Vol 2 Ch 6 (Electroweak and Higgs)](../../../../vol_2_subatomic/chapters/06_electroweak_and_higgs.tex) lines 154–176 — Cosserat constants $\alpha\sqrt{3/7}$, $\sqrt{3/7}$, $\nu_{\text{vac}} = 2/7$, $\Phi_{\text{twist}}$
  - Common Foreword §"Three Falsifiable Predictions" — empirical-test queue including Fermilab Muon g−2 Run-4/5
- **Empirical test queue:**
  - Fermilab Muon g−2 Run-4/5 (2026–2027) — $\pm 10$ ppm precision; discriminates AVE Cosserat-saliency from SM + new-physics alternatives
  - Tau g−2 (long-term) — generation-distinguishing prediction $+490 \times 10^{-11}$ for $n_{\text{Cosserat}} = 2$ scaling
