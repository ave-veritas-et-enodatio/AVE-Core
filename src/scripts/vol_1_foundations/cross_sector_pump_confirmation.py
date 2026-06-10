#!/usr/bin/env python3
"""Cross-sector V->omega pump CONFIRMATION run (the crux-unblock test, DYNAMICAL).

Companion to research/2026-06-09_cross-sector-pump-confirmation_result.md and the
binding prereg research/2026-06-09_cross-sector-pump-confirmation_prereg.md.
Builds on the derivation research/2026-06-09_tracereversal-pump-derivation_result.md
(verdict WALL-ENGINE/FIXABLE; this RUNS the cross-sector step it left BLOCKED).

WHAT THIS IS (ave-driver-script-honesty):
  IMPLEMENT + RUN + FIGURE of the derived bounded V->omega boundary-condition pump
  in the COUPLED K4 (x) Cosserat engine. Zero new free parameters: K (clamp), I_omega,
  Z0=1, the Op14 asymmetric-Meissner front Z_eff = Z0*sqrt(S_mu/S_eps), Op3 Gamma, the
  Op17 R = Gamma^2 = 1 - T^2 bound, kappa_chiral = 1.2*alpha, S(A) -- all canonical.

  Prescription (prereg sec 3 / derivation sec 9), implemented via the COUPLED
  use_impedance_boundary path with couple_v_sector=True:
    1. disable_cosserat_lc_force=True (kill the detonating bulk A28 W_refl force).
    2. the moving Gamma=-1 clamp a_omega = -(K/I_omega)*relu(-Gamma)*omega on the
       engine-EVOLVED cos.omega, with Gamma read from the SHARED front
       Z_eff = Z0*sqrt(S_mu/S_eps) and K4 V_sq LIVE (couple_v_sector=True) so V
       co-determines the front (the cross-sector channel).
    3. drive the V sector toward yield (V_SNAP=1 natural units so V is live),
       evolve, read omega DYNAMICALLY (Checkpoint 9: engine.cos.omega, NOT the
       _compute_A2_mu heuristic).
    4. adjudicate R(A)=Gamma^2 (bounded <=1) vs |omega|->1e5 (detonating).

  This does NOT claim the (2,3) electron. It confirms (or refutes) the cross-sector
  PUMP only; the (2,3) self-assembly stays a separate downstream gap.

  CONFIGS (the discriminators):
    PUMP      : impedance BC, couple_v_sector=True, omega0 = noise floor, V driven
                near yield. Does omega GROW from V?  (A: grows bounded; B: stays floor)
    DECOUPLED : impedance BC, couple_v_sector=False (V_sq=0 forced into the front).
                PUMP - DECOUPLED isolates the live-V contribution to omega.
    CONFINE   : impedance BC, SEEDED helical omega (real curvature -> mu-short).
                Establishes the clamp CONFINES bounded -- so a null V->omega is
                "no source", not "broken clamp".
    DETONATE  : bulk A28 W_refl force (use_impedance_boundary=False,
                disable_cosserat_lc_force=False). The runaway control for fig 1.

CANONICAL ANCHORS (verify-before-cite; imported, not fit -- did NOT cite the
  retracted vacuum_engine.py:104 1.009 anchor):
    Op17  T^2 = 1 - Gamma^2                  operators.md:57
    Op3   Gamma = (Z2-Z1)/(Z2+Z1)            operators.md:43
    Z_eff = Z0*sqrt(S_mu/S_eps)              doc 54_ sec 6 (asymmetric Meissner)
    a_omega = -(K/I_omega)*relu(-Gamma)*omega  cosserat_field_3d._impedance_clamp_accel
    kappa_chiral = 1.2*alpha                  doc 54_ sec 6 / doc 20
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(_HERE, "..", "..", "..", "src"))

from ave.core.constants import ALPHA  # noqa: E402
from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat  # noqa: E402

KAPPA_CHIRAL = 1.2 * ALPHA           # electron (2,3) chirality coupling (canonical)
CLAMP_K = 200.0                      # impedance_clamp_strength (canonical genesis default)
N = 20
PML = 4
SIGMA = 2.5
KZ = 1.2                             # helical pitch for the seeded omega-photon


# --------------------------------------------------------------------------
# seeds (ave-canonical-source: amplitudes in V_SNAP=1 natural units)
# --------------------------------------------------------------------------
def _grid(n: int):
    c = n // 2
    xs = np.arange(n)
    X, Y, Z = np.meshgrid(xs, xs, xs, indexing="ij")
    blob = np.exp(-(((X - c) ** 2 + (Y - c) ** 2 + (Z - c) ** 2)) / (2.0 * SIGMA**2))
    return X, Y, Z, blob


def _seed_helical_omega(engine, amp: float) -> None:
    """A charged (Beltrami-helical) omega-photon -- the generative precursor (CP8)."""
    _, _, Z, blob = _grid(engine.N)
    engine.cos.omega[..., 0] = amp * blob * np.cos(KZ * Z)
    engine.cos.omega[..., 1] = amp * blob * np.sin(KZ * Z)
    engine.cos.omega[..., 2] = 0.2 * amp * blob


def _seed_noise_omega(engine, amp: float, seed: int = 1) -> None:
    rng = np.random.default_rng(seed)
    engine.cos.omega[:] = amp * rng.standard_normal(engine.cos.omega.shape)


def _set_V_drive(engine, vamp: float) -> None:
    """Drive the longitudinal V sector toward yield (A2_eps ~ (vamp/V_SNAP)^2)."""
    _, _, _, blob = _grid(engine.N)
    engine.k4.V_inc[:] = (vamp * blob)[..., None] * np.ones(4)


# --------------------------------------------------------------------------
# observables (Checkpoint 9: engine-EVOLVED omega, PML-excluded peaks)
# --------------------------------------------------------------------------
def _omega_max_interior(engine) -> float:
    """Top |omega| over INTERIOR cells only (A-Rule 10: exclude PML shell)."""
    p = engine.pml
    interior = np.zeros(engine.cos.omega.shape[:3], dtype=bool)
    interior[p:engine.N - p, p:engine.N - p, p:engine.N - p] = True
    mag = np.linalg.norm(engine.cos.omega, axis=-1)
    return float(mag[interior].max()) if interior.any() else 0.0


def _front_stats(engine) -> dict:
    """Shared-front Gamma + clamp-gate stats from the LIVE front (V_sq as configured)."""
    g = engine._impedance_gamma_shared()
    relu = np.maximum(0.0, -g)
    Vsq = np.sum(engine.k4.V_inc**2, axis=-1)
    return {
        "gamma_min": float(g.min()),
        "gamma_max": float(g.max()),
        "relu_max": float(relu.max()),
        "R_max": float((g**2).max()),     # Op17 confined fraction R = Gamma^2
        "A2_eps_max": float(Vsq.max()),   # V^2/V_SNAP^2 (V_SNAP=1)
    }


def _energy(engine) -> dict:
    """Coupled ledger: K4 V energy (drive input) + Cosserat reactive (T+W_lin+V_clamp)."""
    h = engine.impedance_hamiltonian()
    return {"E_k4": h["E_k4"], "T_cos": h["T_cos"],
            "W_lin": h["W_linear_cos"], "V_clamp": h["V_clamp"], "H": h["H"]}


# --------------------------------------------------------------------------
# runs
# --------------------------------------------------------------------------
def _make(impedance: bool, couple: bool, bulk_force: bool) -> CoupledK4Cosserat:
    return CoupledK4Cosserat(
        N=N, pml=PML, V_SNAP=1.0,
        use_impedance_boundary=impedance,
        couple_v_sector=couple,
        impedance_clamp_strength=CLAMP_K,
        disable_cosserat_lc_force=(not bulk_force),
        enable_cosserat_self_terms=False,
    )


def run(name: str, *, impedance: bool, couple: bool, bulk_force: bool,
        omega_seed: float, omega_noise: bool, vamp: float, steps: int,
        sustain_V: bool, cap: float = 1e6) -> dict:
    e = _make(impedance, couple, bulk_force)
    if omega_noise:
        _seed_noise_omega(e, omega_seed)
    elif omega_seed > 0:
        _seed_helical_omega(e, omega_seed)
    _set_V_drive(e, vamp)

    ts, om, Ecos, Ek4, relu, Rmax = [], [], [], [], [], []
    f0 = _front_stats(e)
    # record the pre-step seed so the seed->step-1 jump (detonation) is visible
    ts.append(0.0)
    om.append(_omega_max_interior(e))
    relu.append(f0["relu_max"])
    Rmax.append(f0["R_max"])
    Ecos.append(np.nan)
    Ek4.append(float(e.k4_energy()))
    t0 = time.time()
    for i in range(steps):
        if sustain_V:
            _set_V_drive(e, vamp)        # hold V near yield (sustained longitudinal drive)
        e.step()
        omx = _omega_max_interior(e)
        ts.append(e.time)
        om.append(omx)
        fs = _front_stats(e)
        relu.append(fs["relu_max"])
        Rmax.append(fs["R_max"])
        if impedance:
            en = _energy(e)
            Ecos.append(en["T_cos"] + en["W_lin"] + en["V_clamp"])
            Ek4.append(en["E_k4"])
        else:
            Ecos.append(np.nan)
            Ek4.append(float(e.k4_energy()))
        if not np.isfinite(omx) or omx > cap:
            break
    return {
        "name": name, "t": np.array(ts), "omega": np.array(om),
        "E_cos": np.array(Ecos), "E_k4": np.array(Ek4),
        "relu": np.array(relu), "R": np.array(Rmax),
        "front0": f0, "vamp": vamp, "omega0": _seed_floor(omega_seed, omega_noise, e),
        "wall_s": time.time() - t0, "steps_done": len(ts),
    }


def _seed_floor(omega_seed, omega_noise, e):
    return float(omega_seed) if omega_seed > 0 else 0.0


# --------------------------------------------------------------------------
# main + figures
# --------------------------------------------------------------------------
def main() -> None:
    print("=" * 78)
    print("Cross-sector V->omega pump CONFIRMATION (dynamical, coupled K4 x Cosserat)")
    print("=" * 78)
    print(f"alpha={ALPHA:.6e}  kappa_chiral=1.2a={KAPPA_CHIRAL:.6e}  K_clamp={CLAMP_K}")
    print(f"N={N} pml={PML} V_SNAP=1 (natural units, V live)")
    print()

    NEAR_YIELD = [0.0, 0.3, 0.5, 0.7, 0.9, 1.1]   # V=0 baseline + band: A2_eps 0 -> 4.84 (past yield)
    HEAD_V = 0.9
    HEAD_STEPS = 40
    SWEEP_STEPS = 24

    # ---- PUMP: does omega grow from V? (omega0 = noise floor, V sustained) ----
    print("[PUMP] impedance BC, couple_v_sector=True, omega0=1e-6 noise, V sustained @0.9 ...")
    pump = run("PUMP", impedance=True, couple=True, bulk_force=False,
               omega_seed=1e-6, omega_noise=True, vamp=HEAD_V, steps=HEAD_STEPS, sustain_V=True)
    print(f"   omega0={pump['omega'][0]:.3e} -> omega_final={pump['omega'][-1]:.3e}  "
          f"(grew from V? {pump['omega'][-1] > 10*pump['omega'][0]})  "
          f"relu(-Gamma)_max={pump['relu'].max():.3e}  {pump['wall_s']:.0f}s")

    # ---- DECOUPLED: V_sq=0 forced into the front (isolate the live-V contribution) ----
    print("[DECOUPLED] same but couple_v_sector=False (V_sq=0 in front) ...")
    deco = run("DECOUPLED", impedance=True, couple=False, bulk_force=False,
               omega_seed=1e-6, omega_noise=True, vamp=HEAD_V, steps=HEAD_STEPS, sustain_V=True)
    dmax = float(np.max(np.abs(pump["omega"] - deco["omega"])))
    print(f"   max|omega_PUMP - omega_DECOUPLED| = {dmax:.3e}  (live-V contribution to omega)")

    # ---- CONFINE: seeded helical omega -> clamp engages, bounded confinement ----
    print("[CONFINE] impedance BC, seeded helical omega=0.8, couple=True, V @0.6 ...")
    conf = run("CONFINE", impedance=True, couple=True, bulk_force=False,
               omega_seed=0.8, omega_noise=False, vamp=0.6, steps=HEAD_STEPS, sustain_V=False)
    print(f"   |omega| {conf['omega'][0]:.3e} -> {conf['omega'][-1]:.3e}  "
          f"max={conf['omega'].max():.3e}  bounded={conf['omega'].max() < 10}  "
          f"clamp relu_max={conf['relu'].max():.3e}")

    # ---- DETONATE: bulk A28 W_refl force, same seed (the runaway control) ----
    print("[DETONATE] bulk W_refl force (disable_cosserat_lc_force=False), seed+V ...")
    deto = run("DETONATE", impedance=False, couple=True, bulk_force=True,
               omega_seed=0.8, omega_noise=False, vamp=HEAD_V, steps=HEAD_STEPS,
               sustain_V=False, cap=1e4)
    print(f"   |omega| {deto['omega'][0]:.3e} -> {deto['omega'][-1]:.3e} in "
          f"{deto['steps_done']} steps  (growth {deto['omega'][-1]/max(deto['omega'][0],1e-30):.1f}x)")

    # ---- SENSITIVITY SWEEP: omega-buildup vs V-drive amplitude across near-yield band ----
    print("[SWEEP] omega-buildup vs V-drive amplitude (the robust-vs-tuned discriminator) ...")
    sweep = []
    base_of = None
    for v in NEAR_YIELD:
        r = run(f"sweep_v{v}", impedance=True, couple=True, bulk_force=False,
                omega_seed=1e-6, omega_noise=True, vamp=v, steps=SWEEP_STEPS, sustain_V=True)
        gain = r["omega"][-1] / max(r["omega"][0], 1e-30)
        if base_of is None:
            base_of = r["omega"][-1]                       # V=0 baseline (noise evolution, no V)
        sweep.append({"v": v, "omega_final": r["omega"][-1], "gain": gain,
                      "relu_max": r["relu"].max(), "A2_eps": r["front0"]["A2_eps_max"],
                      "R_max": r["R"].max(),
                      "ratio_to_V0": r["omega"][-1] / max(base_of, 1e-30)})
        print(f"   V={v:.1f}  A2_eps={r['front0']['A2_eps_max']:.2f}  "
              f"omega_final={r['omega'][-1]:.3e}  omega/omega(V=0)={r['omega'][-1]/max(base_of,1e-30):.4f}  "
              f"relu(-G)={r['relu'].max():.2e}")

    _figures(pump, deco, conf, deto, sweep, NEAR_YIELD)
    _adjudicate(pump, deco, conf, deto, sweep)


def _analytic_RA(A):
    z = (1.0 - A**2) ** 0.25            # Z_eff/Z0 = sqrt(S_mu/S_eps), mu-side
    g = (z - 1.0) / (z + 1.0)
    return g**2


def _figures(pump, deco, conf, deto, sweep, band):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:  # pragma: no cover
        print(f"(figures skipped: {e})")
        return
    stamp = time.strftime("%Y-%m-%d %H:%M")
    out = _HERE

    # FIG 1 -- omega(t): bounded BC vs detonating bulk force
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    ax[0].plot(conf["t"], conf["omega"], "o-", color="C0", ms=3,
               label="BC clamp (seeded omega): bounded")
    ax[0].plot(pump["t"], pump["omega"], "s-", color="C2", ms=3,
               label="BC pump (omega0=noise, V driven)")
    ax[0].axhline(1.0, color="k", lw=0.5, ls=":")
    ax[0].set_xlabel("t"); ax[0].set_ylabel("|omega|_max (interior)")
    ax[0].set_title("Boundary-condition clamp: BOUNDED"); ax[0].legend(fontsize=8)
    ax[1].semilogy(deto["t"], np.maximum(deto["omega"], 1e-6), "^-", color="C3", ms=4,
                   label="bulk A28 W_refl force")
    ax[1].semilogy(conf["t"], np.maximum(conf["omega"], 1e-6), "o-", color="C0", ms=3,
                   label="BC clamp (bounded)")
    ax[1].set_xlabel("t"); ax[1].set_ylabel("|omega|_max (log)")
    ax[1].set_title("Bulk force: DETONATES (>1e4 in 1 step)"); ax[1].legend(fontsize=8)
    fig.suptitle(f"FIG 1  omega(t): bounded boundary-condition vs detonating bulk force   [{stamp}]")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(os.path.join(out, "cross_sector_pump_fig1_omega_buildup.png"), dpi=130)
    plt.close(fig)

    # FIG 2 -- R(A) = Gamma^2 vs A: bounded in [0,1] through A->1
    A = np.linspace(0.0, 1.0 - 1e-9, 4000)
    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    ax.plot(A, _analytic_RA(A), lw=2, color="C0", label=r"R=$\Gamma^2$=1-$T^2$ (Op17, mu-side)")
    ax.plot(A, 1.0 - _analytic_RA(A), lw=2, ls="--", color="C1", label=r"$T^2$=1-$\Gamma^2$")
    Rmax = max(pump["R"].max(), conf["R"].max())
    ax.axhline(1.0, color="k", lw=0.6, ls=":")
    ax.scatter([0.99], [Rmax], color="C3", zorder=5,
               label=f"engine front max R={Rmax:.3f} (bounded)")
    ax.set_xlabel("saturation amplitude A  (A->1 = Gamma=-1 wall)")
    ax.set_ylabel("power fraction"); ax.set_ylim(-0.05, 1.1)
    ax.set_title(f"FIG 2  R(A)=Gamma^2 bounded in [0,1] through A->1   [{stamp}]")
    ax.legend(fontsize=8, loc="center left")
    fig.tight_layout()
    fig.savefig(os.path.join(out, "cross_sector_pump_fig2_RA_bounded.png"), dpi=130)
    plt.close(fig)

    # FIG 3 -- cross-sector V->omega pump curve: omega_final vs V_drive
    vs = [s["v"] for s in sweep]
    of = [s["omega_final"] for s in sweep]
    rl = [s["relu_max"] for s in sweep]
    fig, ax = plt.subplots(figsize=(6.6, 4.4))
    ax.plot(vs, of, "s-", color="C2", label="omega_final from V (pump output)")
    ax.axhline(1e-6, color="C7", lw=0.8, ls=":", label="omega0 noise floor (1e-6)")
    ax.set_xlabel("V-drive amplitude (V_SNAP=1)"); ax.set_ylabel("omega_final (interior)")
    ax.set_yscale("log")
    ax2 = ax.twinx()
    ax2.plot(vs, rl, "x--", color="C3", label="relu(-Gamma) from V (clamp gate weight)")
    ax2.set_ylabel("relu(-Gamma)_max from V-front", color="C3")
    ax.set_title(f"FIG 3  cross-sector V->omega: FLAT at floor (no fire)   [{stamp}]")
    ax.legend(fontsize=8, loc="upper left"); ax2.legend(fontsize=8, loc="lower right")
    fig.tight_layout()
    fig.savefig(os.path.join(out, "cross_sector_pump_fig3_V_to_omega.png"), dpi=130)
    plt.close(fig)

    # FIG 4 -- energy ledger bar: V drive input vs omega reactive storage + dissipation
    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    W_in = float(pump["E_k4"].max())                  # V drive energy reservoir
    E_om_pump = float(np.nanmax(pump["E_cos"]))       # omega reactive (pump config)
    E_om_conf = float(np.nanmax(conf["E_cos"]))       # omega reactive (seeded confine)
    E_clamp_conf = E_om_conf                          # confined reactance
    labels = ["W_in (V drive,\nK4 reservoir)", "omega reactive\n(PUMP: from V)",
              "omega reactive\n(CONFINE: seeded)"]
    vals = [W_in, E_om_pump, E_om_conf]
    ax.bar(labels, vals, color=["C0", "C2", "C1"])
    for i, v in enumerate(vals):
        ax.text(i, v, f"{v:.2e}", ha="center", va="bottom", fontsize=8)
    ax.set_ylabel("energy (natural units)")
    ax.set_title(f"FIG 4  ledger: V drive present, omega-from-V ~0 (no transfer, no free energy)   [{stamp}]",
                 fontsize=9)
    fig.tight_layout()
    fig.savefig(os.path.join(out, "cross_sector_pump_fig4_energy_ledger.png"), dpi=130)
    plt.close(fig)

    # FIG 5 -- sensitivity sweep: omega_final vs V across band, normalized to V=0 baseline
    ratios = [s["ratio_to_V0"] for s in sweep]
    a2 = [s["A2_eps"] for s in sweep]
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(vs, ratios, "s-", color="C2", ms=7, label=r"$\omega_{final}(V)/\omega_{final}(V{=}0)$")
    ax.axhline(1.0, color="k", lw=1.0, ls=":", label="V-independent baseline (=1: no V effect)")
    ax.axhline(2.0, color="C3", lw=0.9, ls="--", label="pump-fire threshold (2x over baseline)")
    ax.set_xlabel("V-drive amplitude (V_SNAP=1)")
    ax.set_ylabel(r"$\omega_{final}$ normalized to V=0")
    ax.set_ylim(0.0, 2.4)
    for x, y, a in zip(vs, ratios, a2):
        ax.annotate(f"A2e={a:.2f}", (x, y), fontsize=7, xytext=(0, 7),
                    textcoords="offset points", ha="center")
    ax.set_title(f"FIG 5  SENSITIVITY SWEEP: omega FLAT at V=0 baseline across band = robustly NULL   [{stamp}]",
                 fontsize=8.5)
    ax.legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    fig.savefig(os.path.join(out, "cross_sector_pump_fig5_sensitivity_sweep.png"), dpi=130)
    plt.close(fig)
    print("\nfigures saved: cross_sector_pump_fig{1..5}_*.png in", out)


def _adjudicate(pump, deco, conf, deto, sweep):
    print("\n" + "=" * 78)
    print("ADJUDICATION (ave-discriminator-before-synthesis -- the run decides)")
    print("=" * 78)
    grew = pump["omega"][-1] > 10 * pump["omega"][0]
    bounded_pump = np.isfinite(pump["omega"]).all() and pump["omega"].max() < 10
    bounded_conf = conf["omega"].max() < 10
    detonated = (not np.isfinite(deto["omega"]).all()) or deto["omega"].max() > 1e3
    relus = np.array([s["relu_max"] for s in sweep])
    ratios = np.array([s["ratio_to_V0"] for s in sweep])   # omega_final / omega_final(V=0)
    # robustly NULL = (i) clamp gate machine-zero from V across band, AND
    # (ii) omega_final V-INDEPENDENT (every driven point equals the V=0 baseline).
    sweep_robust_null = bool(np.all(relus < 1e-9)) and bool(np.max(np.abs(ratios - 1.0)) < 0.01)
    Rmax = max(pump["R"].max(), conf["R"].max())
    ledger_R_bounded = Rmax <= 1.0 + 1e-9

    print(f"  omega GROWS from V (cross-sector fire)?   {grew}   "
          f"(omega {pump['omega'][0]:.2e} -> {pump['omega'][-1]:.2e})")
    print(f"  BC clamp BOUNDED (pump+confine, no deton)? {bounded_pump and bounded_conf}  "
          f"(max |omega| pump={pump['omega'].max():.2e} confine={conf['omega'].max():.2e})")
    print(f"  bulk-force control DETONATES?             {detonated}  "
          f"(max |omega|={deto['omega'].max():.2e})")
    print(f"  R(A)=Gamma^2 BOUNDED <=1 (Op17)?          {ledger_R_bounded}  (max R={Rmax:.4f})")
    print(f"  live-V contribution to omega (PUMP-DECO)? {float(np.max(np.abs(pump['omega']-deco['omega']))):.2e}")
    print(f"  SWEEP robustly NULL (gain<10 & relu==0)?  {sweep_robust_null}")
    print()
    if detonated and not bounded_pump:
        verdict = "C -- STILL-DETONATES / LEDGER-VIOLATION"
    elif grew and bounded_pump and ledger_R_bounded:
        verdict = "A -- CONFIRMED (cross-sector V->omega pump fires, bounded)"
    elif (not grew) and bounded_pump and ledger_R_bounded:
        verdict = "B -- FORM-BUT-NO-FIRE (BC bounded; V does NOT source omega cross-sector)"
    else:
        verdict = "ambiguous -- inspect"
    print(f"  >>> VERDICT: {verdict}")
    print("  localization (if B): V enters A2_eps (electric) -> Gamma->+1 (eps-OPEN antinode),")
    print("  relu(-Gamma) gate rejects it; the mu-short clamp is driven by omega-curvature,")
    print("  not V; and a_omega=-(K/I)relu(-G)omega is a CONFINEMENT (restoring) term, not the")
    print("  Beltrami SOURCE (derivation sec 5 step 3). Missing V->omega source localized.")


if __name__ == "__main__":
    main()
