[↑ Ch.9 Gamma Scaling](../index.md)
<!-- leaf: verbatim -->
<!-- status: pending-autotune -->

# Autotune Results: Llama 3.2 3B

The binary search proceeded over 8 steps on Llama 3.2 3B Instruct (Q4_K_M):

| **Step** | **$\gamma$** | **FFN pruned** | **tok/s** | **Result** |
|---|---|---|---|---|
| 1 | 0.050 | 40--53% | 42.1 | **PASS** |
| 2 | 0.075 | 48--60% | --- | FAIL |
| 3 | 0.063 | 44--56% | --- | FAIL |
| 4 | 0.056 | 42--54% | --- | FAIL |
| 5 | 0.053 | 41--53% | --- | FAIL |
| 6 | 0.051 | 40--53% | --- | FAIL |
| 7 | 0.050 | 40--52% | 41.8 | **PASS** |
| 8 | 0.031 | 34--40% | 40.0 | FAIL |

The quality boundary lies near $\gamma = 0.030$: output contains "4" at $\gamma \leq 0.030$, but degrades to "2+2 is the same as 2+..." at higher values. The final converged value is $\gamma_{\max} = 0.030$.
