[↑ Biological Applications](./index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: 8zwyl3 -->

# Cancer as Impedance Decoupling

## Hypothesis

Normal tissue maintains cooperative standing-wave patterns through impedance-matched cell--cell coupling via gap junctions. Each cell presents a characteristic impedance $Z_{\mathrm{cell}}$ determined by its membrane composition, ion-channel distribution, and cytoskeletal stiffness. When these impedances are matched, the morphogenetic standing wave---the spatially-periodic field that encodes tissue identity and growth regulation---propagates freely through the multicellular network with minimal reflection ($\Gamma \approx 0$).

Cancer, in this framework, is *impedance decoupling*. A mutation that alters membrane lipid composition, channel density, or cytoskeletal tension shifts $Z_{\mathrm{cell}}$ away from the tissue-matched value. The reflection coefficient at the mutant/healthy boundary rises:

$$\Gamma_{\mathrm{tumour}} = \frac{Z_{\mathrm{mutant}} - Z_{\mathrm{healthy}}}{Z_{\mathrm{mutant}} + Z_{\mathrm{healthy}}}$$

When $|\Gamma|$ exceeds a critical threshold, the cell is effectively isolated from the tissue standing wave. The "stop dividing" signal---a morphogenetic cavity mode---can no longer reach it. Unregulated proliferation follows.

## Metastasis

Metastasis acquires a natural interpretation: a cell whose $Z_{\mathrm{cell}}$ has drifted far enough from its tissue of origin may, by chance, impedance-match a *different* tissue type. Migration to that tissue restores $\Gamma \approx 0$ for the new environment, enabling colonisation.

## Tumour Suppression

The p53 tumour suppressor protein functions, in this model, as an impedance calibration checkpoint. When a cell's impedance drifts beyond the tissue-matched tolerance band, p53 triggers apoptosis---a controlled network reset that removes the mismatched element before the standing wave can collapse.

## Testable Predictions

1. Tumour impedance spectra, measured via Electrical Impedance Spectroscopy (EIS), should show systematic loss of the standing-wave resonance peaks present in healthy tissue.
2. The tumour/healthy boundary should exhibit elevated $|\Gamma|$ at the morphogenetic standing-wave frequency.
3. Cell lines with p53 knockout should show larger impedance drift variance than wild-type, measurable via broadband EIS.

## Research Avenues for Treatment

Four treatment strategies follow directly from the impedance model:

- **Impedance-targeted RF ablation.** Design radiofrequency fields whose frequency and polarisation are impedance-matched to the tumour ($\Gamma_{\mathrm{tumour}} \to 0$, maximum energy absorption) while reflecting off healthy tissue ($\Gamma_{\mathrm{healthy}}$ large). This is frequency-selective ablation guided by pre-operative EIS mapping.

- **Morphogenetic recoupling.** Apply external fields at the healthy tissue's standing-wave frequency to re-establish the cooperative mode. Cells that can recouple differentiate; cells too far drifted to recouple are driven to apoptosis by the impedance mismatch stress.

- **EIS-guided diagnostics.** Tumour boundaries are impedance discontinuities. The reflection coefficient $\Gamma$ at the tumour/healthy interface is large and spatially mappable via multi-electrode EIS arrays, providing sub-millimetre margin delineation without ionising radiation.

- **Impedance-matched drug targeting.** Design drug molecules whose topological impedance $Z_{\mathrm{topo}}$ matches the tumour cell membrane, giving $\Gamma \approx 0$ for selective uptake. For healthy cells with a different $Z$, $\Gamma$ is large and the drug is reflected.

---
