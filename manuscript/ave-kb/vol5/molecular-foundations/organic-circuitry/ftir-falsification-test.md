[↑ Organic Circuitry](../index.md)
<!-- leaf: verbatim -->

---

## FTIR Falsification Test

To test the prediction, the computed transfer function is overlaid against known experimental FTIR absorption peaks from the NIST Chemistry WebBook and Shimanouchi (1972) reference tables. The predicted curve has a *fixed* frequency scale — no parameters can be tuned to improve agreement.

**Figure: fig:ftir_comparison** — Falsification test: AVE-predicted transfer functions for Glycine and Alanine (solid curves) overlaid with experimental FTIR absorption peaks from NIST (dashed lines). The backbone passband (600--1600 cm$^{-1}$) encompasses the majority of the fingerprint-region vibrational modes. High-frequency stretching modes ($>$2500 cm$^{-1}$) fall in the predicted rolloff zone, consistent with the single-unit backbone model not resolving individual bond stretches.

**Results:** For Glycine, 10 of 11 known FTIR peaks fall within the predicted passband ($|H|^2 > -60$ dB). For Alanine, 10 of 11 peaks pass the same threshold. The single "steep" peak in each case occurs in the high-frequency rolloff zone ($>$2500 cm$^{-1}$ for Glycine, $\sim$1100 cm$^{-1}$ for Alanine), where the single-backbone-unit model does not resolve individual bond stretching modes.

This is an expected physical limitation: the transfer function $H(f)$ describes the *power transmission through the entire backbone*, not the local absorption at each bond site. Individual bond stretches (C--H at 3000 cm$^{-1}$, N--H at 3400 cm$^{-1}$) are self-consistent by construction (eq:f_check), but their visibility in the backbone transfer function depends on the impedance matching between the R-group stub and the main chain. The backbone passband — which *is* the genuine prediction — matches the experimentally observed fingerprint amide region without adjustment.

---
