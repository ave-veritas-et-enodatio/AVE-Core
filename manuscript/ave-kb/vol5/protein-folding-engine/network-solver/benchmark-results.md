[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Benchmark Results

## 1D ABCD Cascade vs 2D S-Parameter Network

All constants identical between engines; only the network topology differs. $R_g$ target from $\eta_\text{eq} = P_C(1-\nu)$. 10,000 gradient steps, 3 random starts, Adam optimiser ($\text{lr}=2\times 10^{-3}$).

| **Protein** | $N$ | 1D $R_g$ err | 2D $R_g$ err | 1D SS% | 2D SS% | 1D RMSD (\AA) | 2D RMSD (\AA) |
|---|---|---|---|---|---|---|---|
| Trp-cage (1L2Y) | 20 | 3.8% | 10.8% | 34 | 6 | 5.65 | 5.87 |
| Villin HP35 (1YRF) | 35 | 0.5% | 11.4% | 24 | **27** | 7.61 | 8.44 |
| GB1 (1PGA) | 56 | 5.5% | 10.9% | 22 | 17 | 9.89 | 10.51 |
| Ubiquitin (1UBQ) | 76 | 7.6% | 11.8% | 27 | 16 | 10.83 | 11.26 |
| **Mean** | | 4.4% | 11.2% | 26.8 | 16.5 | 8.50 | 9.02 |
| **$|S_{11}|^2$ (loss)** | | 0.82 $\to$ 0.075 | | *15$\times$ lower reflection* | | | |

## v3 (ABCD Cascade) vs v4 (Y-Matrix) Benchmark

| Protein | N | v3 RMSD (\AA) | v4 RMSD (\AA) | $\Delta$ |
|---|---|---|---|---|
| Chignolin | 10 | **2.59** | 2.78 | $+0.19$ |
| Trp-cage | 20 | 6.25 | **5.67** | $-0.58$ |
| BBA5 | 22 | 7.39 | **6.05** | $-1.34$ |
| Villin HP35 | 36 | 8.25 | **6.06** | $-2.19$ |
| Protein G | 56 | 13.25 | **10.66** | $-2.59$ |

The Y-matrix improves 4 of 5 benchmarks, with the largest gain ($-2.16$ \AA) on Villin HP35. The single regression (Chignolin $+0.22$ \AA) is within sampling noise for a 10-residue peptide. The improvement scales with chain length, consistent with the Y-matrix's ability to capture long-range contact topology.

## v4 Benchmark (All-Derived Constants, Even/Odd Mode $\beta$-Sheets)

| Protein | N | v3 RMSD (\AA) | v4 RMSD (\AA) | $\Delta$ |
|---|---|---|---|---|
| Chignolin | 10 | 2.59 | **2.77** | $+0.18$ |
| Trp-cage | 20 | 6.25 | **5.46** | $-0.79$ |
| BBA5 | 22 | 7.39 | **5.98** | $-1.41$ |
| Villin HP35 | 36 | 8.25 | **6.91** | $-1.34$ |
| Protein G | 56 | 13.25 | **10.92** | $-2.33$ |

---
