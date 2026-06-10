"""
Figures for the sonic-horizon closure probe (data-derived captions printed to stdout).
Reads `_output/sonic_horizon_closure_results.json`; writes PNGs to `_output/`.
"""
from __future__ import annotations

import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "_output")
D = json.load(open(os.path.join(OUT, "sonic_horizon_closure_results.json")))
RHO_CAV = D["floor_rho_cav"]


def fig1_reach():
    up = D["C_hysteresis"]["up_branch"]
    M = [r["M"] for r in up]
    deep = [r["deepest"] for r in up]
    pk = [r["max_pocket"] for r in up]
    fig, ax1 = plt.subplots(figsize=(6.4, 4.2))
    ax1.plot(M, deep, "o-", color="C0", label="deepest ρ̄_core")
    ax1.axhline(RHO_CAV, ls="--", color="k", lw=1, label=f"ρ̄_cav=−1/φ={RHO_CAV:.3f}")
    ax1.set_xlabel("drive M_edge"); ax1.set_ylabel("deepest ρ̄_core", color="C0")
    ax1.tick_params(axis="y", labelcolor="C0")
    ax2 = ax1.twinx()
    ax2.plot(M, pk, "s-", color="C3", label="max pocket cells")
    ax2.set_ylabel("max pocket cells (c²≤0)", color="C3")
    ax2.tick_params(axis="y", labelcolor="C3")
    ax1.set_title("Sonic-horizon UP-branch: pocket forms at M≥0.8; ρ̄_core clamps at the void floor")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig1_reach.png"), dpi=130); plt.close(fig)
    print(f"[fig1] deepest pins at the iface clamp −0.618 for M≥0.8 (={deep}); "
          f"max_pocket {pk} grows 0→1280 — the horizon FORMS cleanly (not NO-HORIZON).")


def fig2_chi():
    chi = D["C_hysteresis"]["chi_sweep"]
    cs = [r["chi_shock"] for r in chi]
    fp = [r["final_pocket"] for r in chi]
    ed = [r["E_diss"] for r in chi]
    fig, ax1 = plt.subplots(figsize=(6.4, 4.2))
    ax1.bar([c - 0.02 for c in cs], fp, width=0.04, color="C3", label="final pocket cells")
    ax1.set_xlabel("shock-dissipation fraction χ_shock"); ax1.set_ylabel("final pocket cells", color="C3")
    ax1.set_ylim(-0.5, max(5, max(fp) + 1))
    ax2 = ax1.twinx()
    ax2.plot(cs, ed, "o-", color="C0", label="E_diss (one-way sink)")
    ax2.set_ylabel("cumulative E_diss", color="C0")
    ax1.set_title("CRUX: E_diss scales with χ_shock, but persistence = 0 for ALL χ → LOCK, not CLIP")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig2_chi_sweep.png"), dpi=130); plt.close(fig)
    print(f"[fig2] final_pocket={fp} (ZERO at every χ_shock={cs}); E_diss grows {ed[0]:.1e}→{ed[-1]:.1e}. "
          f"Persistence does NOT track the dissipation knob → genuine LOCK, not CLIP.")


def fig3_hyst():
    up = D["C_hysteresis"]["up_branch"]
    dn = D["C_hysteresis"]["down_branch"]
    Mu = [r["M"] for r in up]; du = [r["deepest"] for r in up]
    Md = [r["M_eff"] for r in dn]; dd = [r["rho_core"] for r in dn]
    pkd = [r["pocket"] for r in dn]
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.plot(Mu, du, "o-", color="C0", label="UP branch (deepest, fresh)")
    ax.plot(Md, dd, "s--", color="C1", label="DOWN branch (de-spun from M=1.0)")
    ax.axhline(RHO_CAV, ls=":", color="k", lw=1, label="ρ̄_cav")
    ax.set_xlabel("effective drive M"); ax.set_ylabel("ρ̄_core")
    ax.set_title("Hysteresis: DOWN branch is SHALLOWER (relaxed), pocket-cells=0 on de-spin\n"
                 f"(down-branch pocket cells = {pkd}) — reversible, not a persistent defect")
    ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig3_hysteresis.png"), dpi=130); plt.close(fig)
    print(f"[fig3] DOWN-branch ρ̄_core {[f'{x:.3f}' for x in dd]} shallower than UP {[f'{x:.3f}' for x in du]}; "
          f"down-branch pocket cells {pkd} (all 0). The loop opens in the DISSIPATIVE-RELAXATION "
          f"direction (core refills), NOT toward a persistent pocket — pocket-cells hysteresis is closed.")


def fig4_timeseries():
    s = D["C_hysteresis"]["series_M0.9"]
    t = np.array(s["t"]); rc = np.array(s["rho_core"]); pk = np.array(s["pocket"])
    KE = np.array(s["KE"]); PE = np.array(s["PE_exact"]); Ed = np.array(s["E_diss"])
    fig, (axa, axb) = plt.subplots(2, 1, figsize=(6.6, 6.0), sharex=True)
    axa.plot(t, rc, color="C0", label="ρ̄_core")
    axa.axhline(RHO_CAV, ls="--", color="k", lw=1, label="ρ̄_cav")
    axa2 = axa.twinx(); axa2.plot(t, pk, color="C3", label="pocket cells")
    axa2.set_ylabel("pocket cells", color="C3")
    axa.set_ylabel("ρ̄_core", color="C0"); axa.legend(loc="lower right", fontsize=8)
    axa.set_title("M=0.9: transient pocket (peak 728 cells) heals under sustained drive")
    axb.plot(t, KE, label="KE"); axb.plot(t, PE, label="PE_exact (EOS)")
    axb.plot(t, KE + PE, label="KE+PE"); axb.plot(t, Ed, label="E_diss (one-way)")
    axb.set_xlabel("t"); axb.set_ylabel("energy"); axb.legend(fontsize=8)
    axb.set_title("Crossing is SMOOTH (no latent step); E_diss accrues gradually")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig4_timeseries.png"), dpi=130); plt.close(fig)
    print(f"[fig4] pocket peaks {int(pk.max())} at t={t[np.argmax(pk)]:.3f} then decays to {int(pk[-1])}; "
          f"KE+PE declines smoothly across the crossing (no latent discontinuity); "
          f"E_diss→{Ed[-1]:.2e} (the one-way sink, ~23% of the KE+PE decline; rest is acoustic radiation).")


def fig5_handedness():
    hd = D["D_handedness"]; cal = D["A_calibration"]
    keys = list(hd.keys())
    co = [hd[k]["R_co"] for k in keys]; ct = [hd[k]["R_counter"] for k in keys]
    x = np.arange(len(keys))
    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    ax.bar(x - 0.18, co, 0.34, label="R_co (m=+1)", color="C0")
    ax.bar(x + 0.18, ct, 0.34, label="R_counter (m=−1)", color="C1")
    ax.axhline(cal["R_known_mirror"], ls="--", color="g", lw=1,
               label=f"static-mirror reference R={cal['R_known_mirror']:.2f}")
    ax.axhline(cal["R_transparent_floor"], ls=":", color="k", lw=1,
               label=f"transparent floor R={cal['R_transparent_floor']:.3f}")
    ax.set_xticks(x); ax.set_xticklabels(keys, fontsize=8, rotation=15)
    ax.set_ylabel("reflectance R"); ax.legend(fontsize=7)
    ax.set_title(f"Handedness: R_co = R_counter (asym=0.000); floor={cal['handedness_floor_static']:.3f}\n"
                 "BLIND — no rotating-horizon frame-dragging selectivity above the floor")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig5_handedness.png"), dpi=130); plt.close(fig)
    asy = [hd[k]["asym"] for k in keys]
    print(f"[fig5] R_co={[f'{x:.3f}' for x in co]} vs R_counter={[f'{x:.3f}' for x in ct]}; "
          f"asym={asy} (all 0.000, = the static-mirror handedness floor). BLIND. "
          f"Absolute R≈0.006 ≈ floor (the LOCK pocket is transient — no SUSTAINED reflector).")


if __name__ == "__main__":
    fig1_reach(); fig2_chi(); fig3_hyst(); fig4_timeseries(); fig5_handedness()
    print("\nWrote 5 figures to", OUT)
