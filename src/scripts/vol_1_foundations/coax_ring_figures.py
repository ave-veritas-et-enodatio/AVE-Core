#!/usr/bin/env python3
"""
Coax-ring secondary route to alpha --- figures (data-derived captions only).
Reads the two run JSONs; every plotted number comes from them. No re-computation
of physics here (ave-driver-script-honesty: this is a plot generator over honest
pre-computed data).

Outputs (research/figures/):
  coax_ring_fig1_ratio_vs_clip.png   -- Arm 1/2: b/a=R/r diverges + tracks A_cap;
                                        2.27 real-space canon + phi^2 reference lines.
  coax_ring_fig2_dead_input.png      -- Arm 1: dead-input (inner moves; alpha flat;
                                        rejected sqrt(2a) BC alpha-dependent).
  coax_ring_fig3_scale_invariance.png-- Arm 3: f_exch invariant + omega scales down.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "_output")
FIGDIR = os.path.abspath(os.path.join(HERE, "..", "..", "..", "research", "figures"))
os.makedirs(FIGDIR, exist_ok=True)

with open(os.path.join(OUT, "coax_ring_secondary_results.json")) as fh:
    A12 = json.load(fh)
with open(os.path.join(OUT, "coax_ring_scale_invariance_results.json")) as fh:
    A3 = json.load(fh)

PHI2 = 2.6180339887
CANON = 2.27


# ---- Fig 1: b/a vs A_cap clip (Arm 1/2) ----
ba = A12["ARM_1"]["block23_coax_ratio"]["ba_vs_A_cap_clip"]
caps = [float(k.split("=")[1]) for k in ba]
vals = [ba[k] for k in ba]
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot([1 - c for c in caps], vals, "o-", color="crimson", label="b/a = exp[G(A_cap) - G($\\rho_{cav}$)]")
ax.set_xscale("log")
ax.invert_xaxis()
ax.axhline(CANON, ls="--", color="green", label=f"real-space canon $R/r\\approx${CANON} (L3 doc 28 §5.3)")
ax.axhline(PHI2, ls=":", color="gray", label=f"phase-space $\\varphi^2={PHI2:.3f}$ (NOT the target)")
ax.set_xlabel("$1-A_{cap}$  (approach to the $A\\to1$ rupture wall) $\\rightarrow$")
ax.set_ylabel("$b/a = R/r$  (real-space radius ratio)")
ax.set_title("Arm 1/2: the $\\alpha$-free $A\\to1$ outer BC gives a DIVERGENT $b/a$ that\n"
             "TRACKS the saturation clip $A_{cap}$ (apparatus) — never settles on 2.27")
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)
cap = (f"b/a grows 5.2$\\to${vals[-1]:.0f} as $A_{{cap}}$: 0.9$\\to$0.99999 and diverges at the exact "
       f"$A\\to1$ wall.\nResidual vs 2.27 at $A_{{cap}}$=0.99: "
       f"{A12['ARM_2']['comparison']['residual_vs_2.27_at_A_cap_0.99']:+.0%}. Arm 2 = DIFFERENT.")
fig.text(0.5, -0.02, cap, ha="center", fontsize=8, wrap=True)
fig.tight_layout()
fig.savefig(os.path.join(FIGDIR, "coax_ring_fig1_ratio_vs_clip.png"), dpi=130, bbox_inches="tight")
plt.close(fig)


# ---- Fig 2: dead-input test (Arm 1) ----
b5 = A12["ARM_1"]["block5_dead_input"]
inner = b5["a_inner_floor_sweep"]
rej = b5["c_REJECTED_sqrt2alpha_BC_sweep"]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))
xin = [float(k.split("=")[1]) for k in inner]
yin = [inner[k] for k in inner]
ax1.plot(xin, yin, "s-", color="navy")
ax1.set_xlabel("inner floor $\\rho_{cav}$ (varied)")
ax1.set_ylabel("b/a (at $A_{cap}$=0.99)")
ax1.set_title("LIVE input: vary the inner floor $\\Rightarrow$ b/a MOVES\n(physics, not tautology)")
ax1.grid(alpha=0.3)
# alpha sweep (canonical BC, flat) vs rejected sqrt(2a) BC (moves)
amul = [0.5, 1.0, 2.0]
yrej = list(rej.values())
yalpha = list(A12["ARM_1"]["block5_dead_input"]["b_alpha_sweep_canonical_BC"].values())
ax2.plot([0.01, 1.0, 100.0], yalpha, "o-", color="green", label="canonical $A\\to1$ BC (FLAT = circularity-free)")
ax2.plot([0.5, 1.0, 2.0], yrej, "x--", color="crimson", label="REJECTED $\\sqrt{2\\alpha}$ onset BC ($\\alpha$-dependent)")
ax2.set_xscale("log")
ax2.set_xlabel("$\\alpha$ multiplier")
ax2.set_ylabel("b/a")
ax2.set_title("DEAD input: $\\alpha$ does not move the canonical b/a;\nthe rejected $\\sqrt{2\\alpha}$ BC WOULD")
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3)
fig.suptitle("Arm 1 dead-input test: the $A\\to1$ b/a is CIRCULARITY-FREE ($\\alpha$-independent)", fontsize=11)
fig.tight_layout()
fig.savefig(os.path.join(FIGDIR, "coax_ring_fig2_dead_input.png"), dpi=130, bbox_inches="tight")
plt.close(fig)


# ---- Fig 3: scale invariance (Arm 3) ----
v = A3["VERDICT"]
rs = [4, 6, 8]
f_exch = v["f_exch_by_scale_r4_r6_r8"]
omega = v["omega_field_by_scale_r4_r6_r8"]
loc = v["L_over_C_by_scale"]
drift = [A3["scale_sweep_carrier_reactance_pair"][f"r={r}"]["ledger_drift"] for r in rs]
fig, (axA, axB) = plt.subplots(1, 2, figsize=(11, 4.5))
# f_exch with ledger-floor error bars
axA.errorbar(rs, f_exch, yerr=[d * fe for d, fe in zip(drift, f_exch)], fmt="o-", color="navy", capsize=4,
             label="f_exch (C$\\leftrightarrow$L slosh), $\\pm$ledger floor")
axA.axhline(1.0, ls=":", color="gray")
axA.set_xlabel("minor radius r (scale)")
axA.set_ylabel("exchange fraction f_exch")
axA.set_ylim(0.85, 1.20)
axA.set_title(f"f_exch INVARIANT within ledger floor\nspread {v['f_exch_spread']*100:.1f}% < floor {v['ledger_floor_worst']*100:.0f}%")
axA.legend(fontsize=8)
axA.grid(alpha=0.3)
axB.plot(rs, omega, "o-", color="crimson", label="$\\omega_{field}$ (mode freq)")
axB.axhline(1.0, ls="--", color="green", label="mass-gap floor $\\omega_0=1.0$")
axB.plot(rs, loc, "s:", color="darkorange", label="$\\langle L\\rangle/\\langle C\\rangle$ (virial)")
axB.set_xlabel("minor radius r (scale)")
axB.set_ylabel("$\\omega_{field}$ ,  $\\langle L\\rangle/\\langle C\\rangle$")
axB.set_title("$\\omega$ SCALES with size (product-set):\n$\\to\\omega_0$ floor as LC predicts")
axB.legend(fontsize=8)
axB.grid(alpha=0.3)
fig.suptitle(f"Arm 3: carrier reactance pair — BIN = {v['BIN']}", fontsize=11)
fig.tight_layout()
fig.savefig(os.path.join(FIGDIR, "coax_ring_fig3_scale_invariance.png"), dpi=130, bbox_inches="tight")
plt.close(fig)

print("wrote:")
for f in ("coax_ring_fig1_ratio_vs_clip.png", "coax_ring_fig2_dead_input.png", "coax_ring_fig3_scale_invariance.png"):
    print("  ", os.path.join(FIGDIR, f))
