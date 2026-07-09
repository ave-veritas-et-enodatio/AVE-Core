"""Production run of the CHIRAL-DRIVE SELF-ORBIT test (pre-reg 2026-07-08, Task #22).

ONE blocking run at the production scale (N=64, 6000 steps, 9-point flux sweep).
Writes the results JSON and the house-white figure. NO polling; unitary evolver
only (Cayley/Crank–Nicolson — no damping term is representable).

  python src/scripts/vol_2_particle_physics/chiral_drive_selforbit_run.py

Outputs:
  results/chiral_drive_selforbit_results.json
  research/figures/2026-07-08-chiral-drive-selforbit/chiral_drive_selforbit.{png,pdf}
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

# ── ave-canonical-source cross-check: constants import cleanly; they enter ONLY
# as OFF-PATH scale anchors. The verdict observables (chiral_drive_gate) are pure
# phases / current ratios and NEVER import α / m_e / NU_VAC on the verdict path. ──
import ave.core.constants as _c  # noqa: E402
from ave.solvers.chiral_drive_selforbit import ChiralDriveConfig, chiral_drive_gate


def _verify_constants() -> dict:
    """Cross-check the canonical anchors and the corpus chiral reference. No
    hardcoded physics value is on the verdict path (the gate is α-free)."""
    assert abs(_c.NU_VAC - 2.0 / 7.0) < 1e-15, "NU_VAC drifted from 2/7"
    assert abs(_c.OMEGA_C - _c.C_0 / _c.L_NODE) < 1e-6 * _c.OMEGA_C, "OMEGA_C != C_0/L_NODE"
    theta_chi = 2.0 * np.pi * _c.NU_VAC  # node-circulator §1 per-cell chiral phase
    return {
        "constants_module": _c.__file__,
        "NU_VAC": float(_c.NU_VAC),
        "OMEGA_C_rad_s": float(_c.OMEGA_C),
        "theta_chi_2pi_nu_vac": float(theta_chi),
        "loop_flux_3port_reference_3theta_chi": float(3.0 * theta_chi),
        "note": (
            "θ_χ=2π·ν_vac and the 3-port loop flux 3θ_χ are the corpus chiral "
            "references (research/2026-06-20_node-circulator-coupling.md:116). "
            "ν_vac=2/7 is GR-IMPORTED (constants.py:381) ⇒ the flux VALUE is an "
            "ECHO, not lattice-forced. Off-path anchors only; the verdict is α-free."
        ),
    }


def _forced_vs_free(res: dict, anchors: dict) -> dict:
    """Is the flux needed for an ω_C-rate circulation FORCED or a FREE knob?

    In engine-natural units the ring-current rate is I_ring(Φ)=2t·sin(Φ/N)/N — set
    by the free hopping scale t AND the flux Φ. The canonical chiral flux value is
    θ_χ=2π·ν_vac with ν_vac=2/7 GR-IMPORTED. Both the rate scale (via t) and the
    flux value (via ν_vac) are free/imported ⇒ the ω_C-rate is NOT forced.
    """
    N = res["config"]["N"]
    t = res["config"]["t_hop"]
    # the flux that would give ring-current == 1 (engine-natural target); a free
    # inversion (exists for any target ≤ 2t/N) — demonstrates the knob is free.
    target = 2.0 * t / N  # the max ring current (at Φ=Nπ/2); any target below is reachable
    return {
        "rate_scale_free_via_hopping_t": True,
        "flux_value_imported_via_nu_vac": True,
        "canonical_flux_theta_chi": anchors["theta_chi_2pi_nu_vac"],
        "canonical_loop_flux_3theta_chi": anchors["loop_flux_3port_reference_3theta_chi"],
        "max_ring_current_natural_units": float(target),
        "omega_C_rate_flux_is_forced": False,
        "verdict": (
            "FREE/IMPORTED KNOB — the circulation rate is set by the free hopping "
            "scale t and a flux whose canonical value (2π·ν_vac) is GR-imported. "
            "The mechanism is real; the VALUE is a calibration/echo. Matches the "
            "node-circulator IMPOSED-AT-MAGNITUDE verdict."
        ),
    }


def make_figure(res: dict, out_dir: Path) -> list[Path]:
    import ave.viz.style as style

    style.apply("print")
    plt = style.plt
    C = style.COLORS

    fig, axes = plt.subplots(1, 3, figsize=(13.0, 3.8), constrained_layout=True)

    # ── Panel A: the DISCRIMINATOR — curl drives, gradient is null ──
    axA = axes[0]
    sweep = res["arm1_curl_sweep"]
    fl = np.array([r["flux"] for r in sweep])
    Cu = np.array([r["C_dc_uniform"] for r in sweep])
    Cl = np.array([r["C_dc_localized"] for r in sweep])
    N = res["config"]["N"]
    anchor = 2.0 * res["config"]["t_hop"] * np.sin(fl / N)
    axA.plot(fl, anchor, "-", color=C["muted"], lw=2.2, label="anchor 2t·sin(Φ/N)", zorder=1)
    axA.plot(fl, Cu, "o", color=C["ave"], ms=6, label="CURL, uniform seed", zorder=3)
    axA.plot(fl, Cl, "s", color=C["accent"], ms=5, label="CURL, localized seed", zorder=2)
    grad_C = res["arm2_gradient_control"]["gradient_C_dc"]
    axA.axhline(grad_C, ls="--", color=C["comparison"], lw=1.6,
                label=f"GRADIENT (∮=0): {grad_C:.1e}")
    axA.set_xlabel("loop flux  Φ = ∮θ  [rad]")
    axA.set_ylabel("DC net circulation  ⟨C⟩")
    axA.set_title("Discriminator: curl drives, gauge does not")
    axA.legend(loc="upper left", fontsize=7, frameon=False, bbox_to_anchor=(0.0, 1.0))

    # ── Panel B: MASS OBSERVABLE — E_circ ∝ M² ──
    axB = axes[1]
    M = np.array([abs(r["M_dc_localized"]) for r in sweep])
    E = np.array([r["E_circ_localized"] for r in sweep])
    good = (M > 1e-9) & (E > 0)
    axB.loglog(M[good], E[good], "o", color=C["ave"], ms=6, label="measured", zorder=3)
    a4 = res["arm4_mass_observable"]
    if np.isfinite(a4["E_circ_vs_M_exponent"]) and good.sum() >= 2:
        coeffs = np.polyfit(np.log(M[good]), np.log(E[good]), 1)
        xg = np.linspace(np.log(M[good].min()), np.log(M[good].max()), 50)
        axB.loglog(np.exp(xg), np.exp(np.polyval(coeffs, xg)), "-", color=C["muted"], lw=2.0,
                   label=f"fit slope {a4['E_circ_vs_M_exponent']:.3f}  (R²={a4['E_circ_vs_M_r2']:.5f})")
    axB.set_xlabel("DC inter-node mismatch  |M|")
    axB.set_ylabel("circulation energy  E_circ")
    axB.set_title("Mass observable: E_circ ∝ M²")
    axB.legend(loc="upper left", fontsize=7, frameon=False)

    # ── Panel C: A1-sourcing (saturation ON) — DC density, curl vs bias-off ──
    axC = axes[2]
    a5 = res["arm5_a1_sourcing"]
    rho_curl = np.array(res["_arm5_rho_curl"])
    rho_off = np.array(res["_arm5_rho_off"])
    nn = np.arange(len(rho_curl))
    axC.plot(nn, rho_off, "-", color=C["muted"], lw=1.8,
             label=f"bias-off  PR={a5['off_participation_ratio']:.3f}")
    axC.plot(nn, rho_curl, "-", color=C["ave"], lw=1.8,
             label=f"curl  PR={a5['curl_participation_ratio']:.3f}")
    axC.set_xlabel("node index  n")
    axC.set_ylabel("DC density  ⟨|ψ_n|²⟩")
    axC.set_title("A1 sourcing (proxy): NULL — no extra trapping")
    axC.legend(loc="upper right", fontsize=7, frameon=False)

    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for ext in ("png", "pdf"):
        p = out_dir / f"chiral_drive_selforbit.{ext}"
        fig.savefig(p, dpi=180, bbox_inches="tight")
        paths.append(p)
    plt.close(fig)
    return paths


def main() -> None:
    root = Path(__file__).resolve().parents[3]
    anchors = _verify_constants()

    cfg = ChiralDriveConfig(N=64, n_steps=6000, dt=0.02, record_frac=0.5)
    res = chiral_drive_gate(cfg, flux_ref=np.pi, flux_sweep=tuple(np.linspace(0.0, 2.0 * np.pi, 9)))

    # capture the A1-arm DC density profiles for the figure (re-run the two sat
    # configs once more to grab rho_dc — cheap; keeps the gate output compact)
    from ave.solvers.chiral_drive_selforbit import evolve

    def _sat(**kw):
        d = dict(cfg.__dict__)
        d.update(dict(A_yield=1.0, seed_kind="localized"))
        d.update(kw)
        return evolve(ChiralDriveConfig(**d))

    res["_arm5_rho_curl"] = _sat(bias="curl", flux=np.pi)["rho_dc"]
    res["_arm5_rho_off"] = _sat(bias="off", flux=0.0)["rho_dc"]

    res["verify_constants"] = anchors
    res["forced_vs_free"] = _forced_vs_free(res, anchors)

    out_json = root / "results" / "chiral_drive_selforbit_results.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    # drop the bulky per-step rho arrays from the on-disk sweep? keep — small (N).
    with out_json.open("w") as f:
        json.dump(res, f, indent=2, default=str)

    fig_dir = root / "research" / "figures" / "2026-07-08-chiral-drive-selforbit"
    fig_paths = make_figure(res, fig_dir)

    print("=" * 64)
    print("CHIRAL-DRIVE SELF-ORBIT — PRODUCTION RUN (N=64, 6000 steps)")
    print("=" * 64)
    print(f"VERDICT: {res['verdict']}")
    print(f"  curl C_dc            = {res['arm2_gradient_control']['curl_C_dc']:.6e}")
    print(f"  gradient C_dc (null) = {res['arm2_gradient_control']['gradient_C_dc']:.3e}")
    print(f"  curl H-drift         = {res['arm3_conservative']['curl_h_drift']:.3e}")
    print(f"  rate-∝-flux anchor err = {res['arm1_rate_law']['anchor_max_abs_err']:.3e}")
    print(f"  E_circ∝M^ {res['arm4_mass_observable']['E_circ_vs_M_exponent']:.4f} "
          f"(R²={res['arm4_mass_observable']['E_circ_vs_M_r2']:.6f})")
    print(f"  A1-sourcing localizes-more-than-off = {res['arm5_a1_sourcing']['localizes_more_than_off']}")
    print(f"  ω_C-rate flux forced = {res['forced_vs_free']['omega_C_rate_flux_is_forced']}")
    print(f"  results: {out_json}")
    print(f"  figure : {fig_paths[0]}")


if __name__ == "__main__":
    main()
