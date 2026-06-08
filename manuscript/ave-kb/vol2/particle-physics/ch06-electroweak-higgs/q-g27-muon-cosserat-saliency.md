[↑ Ch.6 Electroweak and Higgs](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-8niffj]
-->

# Q-G27: Muon Cosserat Torsion Saliency — AVE Forward Prediction +502×10⁻¹¹ (4.6σ tension with Fermilab on e+e- baseline)

The Fermilab Muon g−2 experiment measured a 4.2σ tension with the Standard Model prediction. AVE forward-predicts a **topological/Cosserat second-order effect** that the Standard Model does not capture, with **zero fit parameters**. The muon's Cosserat torsion-quantum excitation contributes an additional saliency $\delta_{\text{Cosserat}}^{\mu}$ to the g−2 anomalous-moment expansion beyond the universal Q-G19α Petermann closure.

This leaf is the dedicated muon-sector g−2 leaf, parallel to the electron-sector [Q-G19α Petermann closure](q-g19a-petermann-saliency-closure.md). The muon's MASS formula (Cosserat torsion at 1.24%) is in the separate [Higgs Mass / lepton spectrum leaf](higgs-mass.md); this leaf addresses the g−2 ANOMALOUS-MOMENT contribution, a structurally separate derivation.

> **Scope correction (2026-05-18 late-evening walk-back):** prior versions of this leaf reported $\Delta a_\mu^{(2)} = +247 \times 10^{-11}$ as "0.8% off central value" of Fermilab Run-3. Direct arithmetic verification ([C3 Fermilab driver](../../../../../src/scripts/verify/muon_g2_fermilab_anchor.py), [finding doc](../../../../../research/2026-05-18_q-g27-q-g19a-systemic-conversion-error-finding.md)) found the textbook QED conversion $\Delta a = \Delta C_2\,(\alpha/\pi)^2$ applied to the corpus's own $\Delta C_2 = +9.30 \times 10^{-4}$ gives $+502 \times 10^{-11}$, exactly twice the prior corpus value. The corrected forward prediction is in **4.6σ tension** with Fermilab Run-3 on the e+e- SM baseline (BMW lattice baseline would close the tension differently — see Status block below). The Cosserat-saliency mechanism is preserved: $\delta_{\text{Cosserat}}^{\mu} = -\alpha\sqrt{3/7}/(2\pi)$ uses the same $\sqrt{3/7}$ PAT torsion-shear projection that produces $m_\mu = m_e/(\alpha\sqrt{3/7})$ at 1.24% match to measured muon mass. Walking back the saliency mechanism would break the lepton-mass derivation.

## Result

| Quantity | AVE-derived | Reference | Status |
|---|---|---|---|
| Cosserat saliency $\delta_{\text{Cosserat}}^{\mu}$ | $-\alpha\sqrt{3/7}/(2\pi) = -7.60 \times 10^{-4}$ | Vol 2 Ch 6:164 (PAT torsion-shear projection) | substrate-derived |
| Cosserat $C_2^\mu$ shift | $-0.32755$ vs electron $-0.32848$ | Route B + saliency = $-3\alpha/2 + \delta_{\text{Cosserat}}$ | $\Delta C_2 = +9.30 \times 10^{-4}$ |
| $\Delta a_\mu^{(2)}$ AVE forward | $+502 \times 10^{-11}$ | $\Delta C_2 \cdot (\alpha/\pi)^2$ (textbook QED conversion) | forward prediction |
| Fermilab Run-3 tension vs SM (e+e-) | $+245(56) \times 10^{-11}$ | Run-3 + Theory Initiative 2020 e+e- baseline | measured |
| Deviation: AVE forward vs Fermilab | $+257 \times 10^{-11}$ | difference | **+4.585σ above** (on e+e- baseline) |

AVE predicts a Cosserat-torsion second-order contribution that the Standard Model has no equivalent term for. The forward prediction is BMW-vs-e+e- conditional: on the e+e- SM baseline, AVE is 4.6σ over Fermilab; on the BMW lattice SM baseline (which closes the Fermilab tension toward 0σ vs SM), AVE would be in deeper tension.

## Structural derivation

The muon is canonically identified (per Vol 2 Ch 6:174 + Vol 1 Ch 5:39) as the electron $0_1$ unknot **plus one quantum of Cosserat torsional excitation**. The phase-space (2,3) trefoil topology is preserved; what changes is the Cosserat-sector excitation state, which adds an $\alpha$-order contribution to the saliency framework that produces Q-G19α's Petermann coefficient.

### Canonical Cosserat constants (Vol 2 Ch 6:154–176)

> **🔴 OPEN FLAG (Rule 12 — `√(3/7)` "PAT torsion-shear" label; Grant's physics adjudication pending. Body preserved unchanged below; label NOT swapped per substitution-not-retraction.):** $\sqrt{3/7} = \sqrt{1 - 2\nu_{vac}}$ at $\nu_{vac} = 2/7$ is EXACTLY the dilatational/compressional (bulk) elastic signature: $(1-2\nu)$ = bulk/volumetric, $(1+\nu)$ = shear/deviatoric (the corpus uses $(1+\nu) = 9/7$ as the Z-factor $3/\sqrt{7} = \sqrt{9/7}$). Labeling the **bulk** combination $\sqrt{1-2\nu}$ as "torsion-shear" is an elastic-type contradiction. **OPEN — Grant's physics adjudication:** does an independent torsion route reach $\sqrt{3/7}$, or is this the dilatational (bulk) projection and the label wrong? The engine constant `_SIN_THETA_W_PAT` (`src/ave/topological/cosserat.py:65`) is NOT renamed — deferred to Grant. This flag does NOT disturb the $\delta_{\text{Cosserat}}^{\mu}$ saliency magnitude (which uses $\sqrt{3/7}$'s numeric value $0.6547$, label-independent).

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

This shifts $C_2^\mu$ from the universal Petermann $-0.32848$ to $-0.32755$ — a $+0.28\%$ relative shift, i.e. $\Delta C_2 = +9.30 \times 10^{-4}$. Applying the textbook QED conversion $\Delta a^{(2)} = \Delta C_2 \cdot (\alpha/\pi)^2$ with $(\alpha/\pi)^2 = 5.395 \times 10^{-6}$ gives the AVE forward prediction $\Delta a_\mu^{(2)} = +502 \times 10^{-11}$.

## Generation-distinguishing prediction

If $\delta_{\text{Cosserat}} \propto n_{\text{Cosserat}}$ (linear scaling with the Cosserat-sector quantum number), tau lepton (2 quanta) would have:

$$\delta_{\text{Cosserat}}^{\tau} \approx 2\, \delta_{\text{Cosserat}}^{\mu}$$

giving $a_\tau$ shifted by approximately $+1000 \times 10^{-11}$ from the SM (doubly scaled per the corrected muon value). Future tau g-2 measurements would discriminate AVE's Cosserat-saliency framework from the Standard Model + new-physics alternatives.

## Status

**Mechanism structurally closed; forward prediction in 4.6σ tension with Fermilab Run-3 on e+e- SM baseline.** The derivation uses only canonical corpus constants (Vol 2 Ch 6:154–176): no fit parameters. The forward AVE prediction $\Delta a_\mu^{(2)} = +502 \times 10^{-11}$ is computed via textbook QED conversion $\Delta C_2 \cdot (\alpha/\pi)^2$ applied to the substrate-derived Cosserat-saliency $\delta_\mu = -3\alpha/2 - \alpha\sqrt{3/7}/(2\pi)$.

**BMW-vs-e+e- baseline conditionality:** on the e+e- Theory Initiative 2020 SM baseline, Fermilab Run-3 reports a $+245(56) \times 10^{-11}$ tension over SM, and AVE's $+502 \times 10^{-11}$ sits +4.6σ above the observed tension central value. On the BMW lattice baseline (which closes the Fermilab measurement toward $\sim 0\sigma$ vs SM), AVE's prediction is in deeper tension. **Either baseline puts AVE in genuine forward-vs-measurement disagreement that Run-4/5 will tighten.**

**Falsification target:** Fermilab Run-4/5 will tighten the measurement to $\pm 10$ ppm precision. If the central value (with BMW-vs-e+e- adjudication) settles more than $\sim 100 \times 10^{-11}$ from AVE's $+502 \times 10^{-11}$ forward prediction, the Cosserat-saliency framework — or the n_q-additive Q-G19α framework it builds on — needs revision.

## Cross-references

- **Sibling leafs (same chapter):**
  - [Q-G19α Petermann + saliency closure (electron; $+4.0\%$ parameter-free, 50 ppm postulate-conditional)](q-g19a-petermann-saliency-closure.md) — the universal Petermann derivation that this leaf extends with Cosserat torsion (Stage 1 symmetric Route B forward is $+4.0\%$ off PDG; the 50 ppm figure is conditional on the $n_q$-additivity postulate)
  - [Higgs Mass / lepton spectrum](higgs-mass.md) — muon MASS formula (Cosserat torsion at 1.24%), separate from this leaf's g−2 anomalous-moment derivation
  - [Lepton Spectrum](lepton-spectrum.md) — three-generation Cosserat sector chain
- **Canonical manuscript anchors:**
  - Vol 2 Ch 6 (Electroweak and Higgs) lines 154–176 — Cosserat constants $\alpha\sqrt{3/7}$, $\sqrt{3/7}$, $\nu_{\text{vac}} = 2/7$, $\Phi_{\text{twist}}$
  - Common Foreword §"Three Falsifiable Predictions" — empirical-test queue including Fermilab Muon g−2 Run-4/5
- **Empirical test queue:**
  - Fermilab Muon g−2 Run-4/5 (2026–2027) — $\pm 10$ ppm precision; discriminates AVE Cosserat-saliency from SM + new-physics alternatives
  - Tau g−2 (long-term) — generation-distinguishing prediction $+1000 \times 10^{-11}$ for $n_{\text{Cosserat}} = 2$ scaling (corrected per 2026-05-18 walk-back; prior $+490$ was the same factor-2 conversion error that affected the muon)
