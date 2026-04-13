[↑ Ch.4 Experimental Audit](../index.md)
<!-- leaf: verbatim -->

# Current Limitations

1. **MoE models exceed hardware budget.** The Qwen3.5-35B-A3B (21 GB) and GLM-4.7B-Flash (17 GB) MoE models exceed the M4 Pro's 19 GB GPU working set. MoE expert-router impedance correlation (Chapter 11) remains a theoretical prediction.
2. **Attention heads require per-layer $n_{\text{heads}}$.** Uniform head pruning breaks quality; per-layer variable head counts require architectural changes.
3. **$\gamma_{\max}$ requires per-model calibration.** No universal threshold exists across architectures.
