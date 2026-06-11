"""Figures for the BEMF-feedback smoke (data-derived captions). Reads
bemf_feedback_results.json (written by bemf_feedback_smoke_run.py)."""
from __future__ import annotations

import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, "bemf_feedback_results.json")))
cfg = R["config"]
TOL = cfg["sat_tol"]
COL = {"OFF": "C0", "BEMF_pos": "C2", "BEMF_neg": "C3"}
LAB = {"OFF": "OFF (κ_L=0)", "BEMF_pos": "BEMF +κ_L (Lenz?)", "BEMF_neg": "BEMF −κ_L (anti?)"}


def panel_Lom(ax, group, title):
    for name in ("OFF", "BEMF_pos", "BEMF_neg"):
        a = group[name]
        s = a["series"]
        ax.plot(s["t"], s["Lom"], color=COL[name], lw=1.4,
                label=f"{LAB[name]}  4L/L={a['ratio_4L']:.2f}")
    ax.axhline(0, color="k", lw=0.4)
    ax.set_xlabel("t"); ax.set_ylabel("|L_ω|(t)")
    ax.set_title(title); ax.legend(fontsize=7)


def main():
    # ── Fig 1: the headline |L_ω|(t) saturation, primary + secondary ──
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
    panel_Lom(ax[0], R["primary"],
              f"PRIMARY: v4 lock ON (η=0.05) + BEMF\nOFF ratio={R['primary']['OFF']['ratio_4L']:.2f} "
              f"(v4 baseline 5.03); STOP gate ≤{TOL}")
    if "secondary" in R:
        panel_Lom(ax[1], R["secondary"],
                  f"SECONDARY: lock OFF (no ad-hoc damper) + BEMF alone\n"
                  f"OFF ratio={R['secondary']['OFF']['ratio_4L']:.2f}; STOP gate ≤{TOL}")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "bemf_feedback_fig1_saturation.png"), dpi=120)
    plt.close(fig)

    # ── Fig 2: the PAYMENT ledger (primary) ──
    grp = R["primary"]
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))
    # (a) source reservoir E_V and circulation E_ω
    for name in ("OFF", "BEMF_pos", "BEMF_neg"):
        s = grp[name]["series"]
        ax[0, 0].plot(s["t"], s["EV"], color=COL[name], lw=1.3, label=f"E_V {LAB[name]}")
        ax[0, 1].plot(s["t"], s["Eom"], color=COL[name], lw=1.3, label=f"E_ω {LAB[name]}")
    ax[0, 0].set_title("source reservoir E_V(t) (stencil)"); ax[0, 0].set_xlabel("t"); ax[0, 0].legend(fontsize=7)
    ax[0, 1].set_title("circulation E_ω(t) (stencil)"); ax[0, 1].set_xlabel("t"); ax[0, 1].legend(fontsize=7)
    # (b) drive vs back-EMF (the steady-state drive≈BEMF check)
    for name in ("BEMF_pos", "BEMF_neg"):
        s = grp[name]["series"]
        ax[1, 0].plot(s["t"], s["drive"], color=COL[name], lw=1.2, ls="-", label=f"drive {LAB[name]}")
        ax[1, 0].plot(s["t"], s["bemf_emf"], color=COL[name], lw=1.2, ls="--", label=f"BEMF {LAB[name]}")
    ax[1, 0].set_title("drive vs back-EMF (steady-state drive≈BEMF = payment)")
    ax[1, 0].set_xlabel("t"); ax[1, 0].legend(fontsize=7)
    # (c) cumulative reactive transfer work_V (source pays) / work_omega (circ gains)
    for name in ("BEMF_pos", "BEMF_neg"):
        s = grp[name]["series"]
        ax[1, 1].plot(s["t"], s["workV"], color=COL[name], lw=1.3, ls="-", label=f"work_V {LAB[name]}")
        ax[1, 1].plot(s["t"], s["workOm"], color=COL[name], lw=1.3, ls=":", label=f"work_ω {LAB[name]}")
    ax[1, 1].axhline(0, color="k", lw=0.4)
    ax[1, 1].set_title("reactive BEMF transfer: work_V (source) = −work_ω (circ), ledger-closed")
    ax[1, 1].set_xlabel("t"); ax[1, 1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "bemf_feedback_fig2_payment.png"), dpi=120)
    plt.close(fig)

    # ── Fig 3: gain-robustness sweep ──
    if "sweep" in R:
        sw = R["sweep"]
        ks = sorted(sw.keys(), key=lambda x: float(x))
        kv = [float(k) for k in ks]
        rr = [sw[k]["ratio_4L"] for k in ks]
        mo = [sw[k]["maxom_end"] for k in ks]
        fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
        ax[0].plot(kv, rr, "o-", color="C2")
        ax[0].axhline(TOL, color="r", ls="--", lw=1, label=f"STOP gate {TOL}")
        ax[0].axhline(cfg["v4_baseline_ratio"], color="k", ls=":", lw=1, label=f"OFF/v4 {cfg['v4_baseline_ratio']}")
        ax[0].set_xlabel("κ_L (signed gain)"); ax[0].set_ylabel("|L_ω| ratio_4L")
        ax[0].set_title("gain-robustness: ratio_4L vs κ_L"); ax[0].legend(fontsize=7)
        ax[1].plot(kv, mo, "s-", color="C1")
        ax[1].set_xlabel("κ_L (signed gain)"); ax[1].set_ylabel("max|ω| end")
        ax[1].set_title("detonation gate: max|ω| vs κ_L")
        fig.tight_layout()
        fig.savefig(os.path.join(HERE, "bemf_feedback_fig3_gain_sweep.png"), dpi=120)
        plt.close(fig)
    print("figures written to", HERE)


if __name__ == "__main__":
    main()
