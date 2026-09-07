#!/usr/bin/env python3
"""Regime map for the X44-unblock FROZEN prereg (2026-08-27).

PURPOSE — this driver computes the ACCESSIBLE-REGIME BOUNDS that the prereg's
reachability demonstration (§5) cites. It is a characterisation of the engine's
configuration space, NOT the pre-registered test. It touches no weight, computes
no `eta_mixed`, and installs nothing.

WHAT IT ANSWERS: over an amplitude scan at fixed shape, what values of
`max A`, `U_bind/M`, and the Nordtvedt fraction `f = U_bind/(M + U_bind)` can the
N=24 gaussian-blob family actually REACH — and does it converge there?

WHY IT MATTERS: the superseded prereg
(`research/2026-07-12_x44-komar-source_prereg_FROZEN.md`) froze a PASS bin that
required `f ~ 0.6`. This driver measures the reachable supremum of `f`.

Run from the repo root:  python3 research/drivers/x44_unblock_regime_map.py
"""

import sys

sys.path.insert(0, "src")
sys.path.insert(0, "src/tests")

from engine_acceptance import _nordtvedt as NV  # noqa: E402

N = 24
S_MIN = 1e-3
G_SELF = 1.0
SIGMA = 1.8          # the mid member of the frozen #651 family
M_TARGET = 4.0       # frozen family rest energy; lambda scales it
LAMBDAS = (0.25, 0.5, 1.0, 2.0, 4.0, 6.0, 8.0, 12.0, 16.0, 24.0)


def main() -> None:
    Grad, _Div = NV.build_grad_div(N)
    print(f"# X44-unblock regime map  (N={N}, sigma={SIGMA}, g_self={G_SELF}, S_min={S_MIN})")
    print(f"{'lambda':>7} {'M':>9} {'max_A':>9} {'U_bind':>11} {'U/M':>9} {'f':>9} {'converged':>10}")
    f_sup_conv = 0.0
    for lam in LAMBDAS:
        T00 = NV.normalized_blob(N, SIGMA, M_TARGET * lam)
        res = NV.solve_config(N, T00, g_self=G_SELF, s_min=S_MIN)
        led = NV.energy_ledger(T00, res["eps11"], Grad, g_self=G_SELF)
        M, U = led["M_matter"], led["U_bind"]
        f = U / (M + U)
        conv = bool(res["converged"])
        if conv:
            f_sup_conv = max(f_sup_conv, f)
        print(
            f"{lam:7.2f} {M:9.3f} {float(res['max_A']):9.4f} {U:11.4f} "
            f"{U / M:9.4f} {f:9.4f} {str(conv):>10}"
        )
    print()
    print(f"# reachable supremum of f over CONVERGED members: {f_sup_conv:.4f}")
    print(f"# superseded prereg's PASS bin required f ~ 0.60  ->  {0.60 / f_sup_conv:.2f}x the reachable supremum")


if __name__ == "__main__":
    main()
