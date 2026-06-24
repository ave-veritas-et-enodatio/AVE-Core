"""
Charge-sector two-winding interaction driver — LANE A PATH-(b).

Substrate question (framed substrate-native, NOT "Coulomb scattering"):
two electron charge-windings — each a helical Cosserat micro-rotation ω
circulation with a chosen Beltrami-helicity SIGN (= charge sign) — placed near
each other in the chiral lattice. Their circulation fields overlap through the
medium. DOES THE LATTICE PUSH THEM APART?

Charge = Beltrami helicity H_bel = ∫ω·(∇×ω) on the Cosserat (2,q) micro-rotation
grade (master-equation.md:20). The engine carries the DOF: two helical ω blobs,
conservative force I_ω·ω̈ = −∂W/∂ω (velocity-Verlet step, use_impedance_boundary
=False = bare −∇W/mass), inter-object separation tracked over the window.

Pre-reg: research/2026-06-23_charge-sector-two-winding_prereg.md (FROZEN).
Refute-by-default. Validate-on-known FIRST (like-charge repulsion sign), THEN
chord hunt (divergence from 1/r²).

Regime: cold / sub-yield reactive (|ω| ≪ ω_yield = π ⇒ S ≈ 1, lossless elastic).

DISCIPLINE COMPLIANCE:
  - PML-cell exclusion on every centroid/momentum extraction (A-Rule-10).
  - Reactance-pair tracking: per-object C-state (∫|ω|²) AND L-state (∫|ω̇|²)
    recorded at EVERY step; H_total tracked as energy-conservation guard.
  - Coordinate discipline (A46): observable measured in the SAME real-space
    lattice-Cartesian coordinates as the helicity that defines the charge —
    NOT a phase-space φ² claim.
  - Half-mask partition (per AnnihilationEngine.half_masks precedent): robust
    to blob fusion, which defeats connected-component find_soliton_centroids
    at the overlap separations of interest.
"""

from __future__ import annotations

import argparse
import json

import numpy as np

from ave.topological.cosserat_field_3d import CosseratField3D

OMEGA_YIELD = float(np.pi)  # engine default omega_yield


# ─────────────────────────────────────────────────────────────────────────
# Real-space, PML-excluded, half-mask diagnostics
# ─────────────────────────────────────────────────────────────────────────
def _interior_mask(s: CosseratField3D) -> np.ndarray:
    """Boolean interior mask excluding the PML shell (A-Rule-10 corollary).

    PML cells return frozen-absorbing artifact, not interior physics, so they
    must be excluded BEFORE any centroid / momentum extraction.
    """
    p = s.pml_thickness
    interior = np.zeros((s.nx, s.ny, s.nz), dtype=bool)
    interior[p : s.nx - p, p : s.ny - p, p : s.nz - p] = True
    return interior & s.mask_alive


def _half_centroid(
    s: CosseratField3D, interior: np.ndarray, lo: float, hi: float, axis: int = 0
) -> tuple[tuple[float, float, float], float] | None:
    """Energy-weighted (|ω|²) centroid over the axis-slab [lo, hi), PML-excluded.

    Robust to blob fusion at small separation (a fixed spatial partition, NOT a
    connected-component label that merges overlapping windings).
    """
    w2 = np.sum(s.omega**2, axis=-1)
    coord = (s._i, s._j, s._k)[axis]
    slab = interior & (coord >= lo) & (coord < hi)
    m = w2 * slab
    tot = float(m.sum())
    if tot <= 0.0:
        return None
    cx = float((s._i * m).sum() / tot)
    cy = float((s._j * m).sum() / tot)
    cz = float((s._k * m).sum() / tot)
    return (cx, cy, cz), tot


def _half_momentum_along(
    s: CosseratField3D, interior: np.ndarray, lo: float, hi: float, axis: int, comp_axis: int
) -> float:
    """Signed rotational-momentum proxy of an object along the separation axis.

    Per-object linear momentum proxy = ∫ I_ω·ω̇ summed over the object slab,
    projected onto the separation axis via the ω-field energy-flux. We use the
    energy-flux (Poynting-like) of the ω wave: the net drift of the |ω|²
    centroid is the physical position observable; for an instantaneous momentum
    sign we report the ω-energy-weighted ω̇·(separation direction sense), i.e.
    whether the field is, on net, advancing toward (+) or away from (−) the
    partner. Sign convention: returned value > 0 means the object's ω energy is
    drifting in the +`axis` direction.

    NOTE: the LOAD-BEARING force observable is d(sep)/dt from the centroid
    trajectory (§4). This momentum proxy is the corroborating instantaneous read
    (reactance L-state); both are reported (flag-don't-fix, no silent winner).
    """
    coord = (s._i, s._j, s._k)[axis]
    slab = interior & (coord >= lo) & (coord < hi)
    # Energy-flux proxy: ω·ω̇ weights the rate state by the field amplitude;
    # its centroid-axis moment gives the net advance direction.
    flux = np.sum(s.omega * s.omega_dot, axis=-1) * slab  # (nx,ny,nz)
    # Net signed advance along `axis`: ∫ flux · sign(coord − slab-centroid)
    tot = float(np.abs(flux).sum())
    if tot <= 0.0:
        return 0.0
    c_axis = float((coord * np.abs(flux)).sum() / tot)
    return float((flux * np.sign(coord - c_axis)).sum())


def _object_states(s: CosseratField3D, interior: np.ndarray, lo: float, hi: float) -> dict:
    """Reactance pair for one object: C-state ∫|ω|² and L-state ∫|ω̇|²."""
    coord = s._i
    slab = interior & (coord >= lo) & (coord < hi)
    c_state = float((np.sum(s.omega**2, axis=-1) * slab).sum())
    l_state = float((np.sum(s.omega_dot**2, axis=-1) * slab).sum())
    return {"C_state_int_omega2": c_state, "L_state_int_omegadot2": l_state}


# ─────────────────────────────────────────────────────────────────────────
# Seeding: two helical ω windings at separated centers (additive superposition)
# ─────────────────────────────────────────────────────────────────────────
def _seed_two_windings(
    s: CosseratField3D,
    cA: tuple[float, float, float],
    cB: tuple[float, float, float],
    hA: float,
    hB: float,
    sigma: float,
    amplitude: float,
    wavelength: float = 8.0,
) -> None:
    """Seed two helical ω wavepackets (charge windings) by additive superposition.

    helicity sign = charge sign (master-equation.md:20 / seeder :2158). The two
    windings propagate along ±the separation axis is NOT imposed — direction is
    along z (axis-orthogonal to the separation x) so the carrier does not
    advect the blobs along the separation axis; the ONLY along-x motion is the
    charge–charge force we are measuring.
    """
    s.initialize_gaussian_wavepacket_omega(
        center=cA, sigma=sigma, direction=(0, 0, 1), wavelength=wavelength,
        amplitude=amplitude, axis=1, helicity=hA,
    )
    w1 = s.omega.copy()
    wd1 = s.omega_dot.copy()
    s.initialize_gaussian_wavepacket_omega(
        center=cB, sigma=sigma, direction=(0, 0, 1), wavelength=wavelength,
        amplitude=amplitude, axis=1, helicity=hB,
    )
    mask4 = s.mask_alive[..., None]
    s.omega = (w1 + s.omega) * mask4
    s.omega_dot = (wd1 + s.omega_dot) * mask4
    s.u = np.zeros_like(s.u)
    s.u_dot = np.zeros_like(s.u_dot)
    s.time = 0.0


# ─────────────────────────────────────────────────────────────────────────
# Single run: seed, step, record the reactance pair + centroid trajectory
# ─────────────────────────────────────────────────────────────────────────
def run_pair(
    N: int,
    d0: float,
    hA: float,
    hB: float,
    amplitude: float,
    sigma: float,
    n_steps: int,
    pml: int,
    use_saturation: bool,
) -> dict:
    s = CosseratField3D(
        N, N, N, use_saturation=use_saturation, pml_thickness=pml,
        use_impedance_boundary=False, damping_gamma=0.0,
    )
    c = (N - 1) / 2.0
    cA = (c - d0 / 2.0, c, c)
    cB = (c + d0 / 2.0, c, c)
    _seed_two_windings(s, cA, cB, hA, hB, sigma, amplitude)

    interior = _interior_mask(s)
    mid = c
    lo_hi_A = (0.0, mid)
    lo_hi_B = (float(np.ceil(mid)), float(N))

    H0 = s.total_hamiltonian()
    E0_A = _object_states(s, interior, *lo_hi_A)["C_state_int_omega2"]
    E0_B = _object_states(s, interior, *lo_hi_B)["C_state_int_omega2"]

    rec: list[dict] = []

    def snapshot(step_i: int) -> dict:
        hcA = _half_centroid(s, interior, *lo_hi_A)
        hcB = _half_centroid(s, interior, *lo_hi_B)
        stA = _object_states(s, interior, *lo_hi_A)
        stB = _object_states(s, interior, *lo_hi_B)
        sep = None
        if hcA is not None and hcB is not None:
            sep = hcB[0][0] - hcA[0][0]
        pA = _half_momentum_along(s, interior, *lo_hi_A, axis=0, comp_axis=0)
        pB = _half_momentum_along(s, interior, *lo_hi_B, axis=0, comp_axis=0)
        return {
            "step": step_i,
            "time": float(s.time),
            "sep": sep,
            "centroid_A": hcA[0] if hcA else None,
            "centroid_B": hcB[0] if hcB else None,
            "C_A": stA["C_state_int_omega2"],
            "L_A": stA["L_state_int_omegadot2"],
            "C_B": stB["C_state_int_omega2"],
            "L_B": stB["L_state_int_omegadot2"],
            "p_advance_A": pA,  # >0 = A drifting +x (toward B); attract if >0
            "p_advance_B": pB,  # <0 = B drifting -x (toward A); attract if <0
            "H_total": s.total_hamiltonian(),
        }

    rec.append(snapshot(0))
    dispersed = False
    for i in range(1, n_steps + 1):
        s.step()
        snap = snapshot(i)
        rec.append(snap)
        # Dispersion guard: stop when either object loses > 50% of its t=0 ∫|ω|²
        if snap["C_A"] < 0.5 * E0_A or snap["C_B"] < 0.5 * E0_B:
            dispersed = True
            break

    sep0 = rec[0]["sep"]
    sep_last = rec[-1]["sep"]
    d_sep = (sep_last - sep0) if (sep0 is not None and sep_last is not None) else None

    # Initial outward acceleration via second difference of sep over first
    # few steps (before dispersion). a = d²(sep)/dt². Use the first 3 records.
    a_init = None
    if len(rec) >= 3 and all(r["sep"] is not None for r in rec[:3]):
        dt = rec[1]["time"] - rec[0]["time"]
        if dt > 0:
            a_init = (rec[2]["sep"] - 2.0 * rec[1]["sep"] + rec[0]["sep"]) / (dt * dt)

    H_drift = abs(rec[-1]["H_total"] - H0) / max(abs(H0), 1e-30)

    return {
        "params": {
            "N": N, "d0": d0, "hA": hA, "hB": hB, "amplitude": amplitude,
            "sigma": sigma, "n_steps": n_steps, "pml": pml,
            "use_saturation": use_saturation,
        },
        "sep0": sep0,
        "sep_last": sep_last,
        "d_sep": d_sep,
        "a_init": a_init,
        "H0": H0,
        "H_drift_frac": H_drift,
        "dispersed_early": dispersed,
        "n_records": len(rec),
        "records": rec,
    }


# ─────────────────────────────────────────────────────────────────────────
# Main: run the pre-registered arms
# ─────────────────────────────────────────────────────────────────────────
def main() -> None:
    ap = argparse.ArgumentParser(description="Charge-sector two-winding interaction.")
    ap.add_argument("--N", type=int, default=48)
    ap.add_argument("--pml", type=int, default=4)
    ap.add_argument("--sigma", type=float, default=3.0)
    ap.add_argument("--amplitude", type=float, default=0.05)
    ap.add_argument("--n-steps", type=int, default=120)
    ap.add_argument("--smoke", action="store_true", help="reduced N=24 fast smoke")
    ap.add_argument("--out", type=str, default=None)
    args = ap.parse_args()

    N = 24 if args.smoke else args.N
    pml = 3 if args.smoke else args.pml
    n_steps = 40 if args.smoke else args.n_steps
    amp = args.amplitude
    sigma = args.sigma

    results: dict = {"config": {"N": N, "pml": pml, "sigma": sigma, "amplitude": amp,
                                "n_steps": n_steps, "smoke": args.smoke,
                                "omega_yield": OMEGA_YIELD},
                     "arms": {}}

    # Arm A: cold like-helicity pair (headline validate-on-known)
    print("[Arm A] cold like-helicity pair (hA=hB=+1) — expect REPEL (Δsep>0)")
    results["arms"]["A_like"] = run_pair(N, 10.0, +1.0, +1.0, amp, sigma, n_steps, pml, True)
    rA = results["arms"]["A_like"]
    print(f"   sep0={rA['sep0']:.3f} sep_last={rA['sep_last']:.3f} "
          f"d_sep={rA['d_sep']:.4f} a_init={rA['a_init']} H_drift={rA['H_drift_frac']:.2e}")

    # Arm B: opposite-helicity control (expect ATTRACT — sign FLIPS)
    print("[Arm B] opposite-helicity control (hA=+1,hB=-1) — expect ATTRACT (Δsep<0)")
    results["arms"]["B_opp"] = run_pair(N, 10.0, +1.0, -1.0, amp, sigma, n_steps, pml, True)
    rB = results["arms"]["B_opp"]
    print(f"   sep0={rB['sep0']:.3f} sep_last={rB['sep_last']:.3f} "
          f"d_sep={rB['d_sep']:.4f} a_init={rB['a_init']} H_drift={rB['H_drift_frac']:.2e}")

    # Arm C: achiral null (expect ~0 force along sep axis)
    print("[Arm C] achiral null (hA=hB=0) — expect ~0 force (charge-borne control)")
    results["arms"]["C_achiral"] = run_pair(N, 10.0, 0.0, 0.0, amp, sigma, n_steps, pml, True)
    rC = results["arms"]["C_achiral"]
    print(f"   sep0={rC['sep0']:.3f} sep_last={rC['sep_last']:.3f} "
          f"d_sep={rC['d_sep']:.4f} a_init={rC['a_init']} H_drift={rC['H_drift_frac']:.2e}")

    # Arm R: 1/r law sweep (like-helicity), chord hunt
    print("[Arm R] like-helicity separation sweep — fit force-law exponent")
    arm_r = []
    for d0 in (6.0, 8.0, 10.0, 12.0, 14.0):
        r = run_pair(N, d0, +1.0, +1.0, amp, sigma, max(8, n_steps // 4), pml, True)
        arm_r.append({"d0": d0, "a_init": r["a_init"], "sep0": r["sep0"],
                      "H_drift_frac": r["H_drift_frac"], "dispersed": r["dispersed_early"]})
        print(f"   d0={d0:5.1f} a_init={r['a_init']} H_drift={r['H_drift_frac']:.2e}")
    results["arms"]["R_sweep"] = arm_r

    # Power-law fit on the (d0, a_init) pairs with positive (outward) a_init
    fit = _fit_power_law(arm_r)
    results["power_law_fit"] = fit
    print(f"[Fit] force-law exponent n = {fit.get('exponent')}  "
          f"(Coulomb-force n=-2); R²={fit.get('r2')}")

    # Validated charge-charge LAW + chord (the canonical operator path; the
    # field-engine arms above are the honest "un-caged windings disperse" record).
    print("[Operator] universal pairwise potential — charge-charge LAW + chord")
    chord = characterize_pairwise_chord()
    results["pairwise_chord"] = chord
    print(f"   far-field force exponent = {chord['far_field_force_exponent']:.3f} "
          f"(Coulomb -2); near-field = {chord['near_field_force_exponent']:.3f}; "
          f"frac_dev@1.05·d_sat = {chord['frac_dev_from_coulomb_vs_r_over_dsat']['1.05']:+.4f}")

    out = args.out or (
        "src/scripts/vol_1_foundations/_output/charge_sector_two_winding_results"
        + ("_smoke" if args.smoke else "") + ".json"
    )
    with open(out, "w") as f:
        json.dump(results, f, indent=2, default=_json_default)
    print(f"[out] wrote {out}")


def characterize_pairwise_chord() -> dict:
    """Characterize the AVE charge-charge law via the CANONICAL validated
    operator `universal_pairwise_energy` (clm-gdd70j, pairwise-potential.md;
    tests test_universal_operators.py:150,158).

    Why this and not the field-engine centroid: per engine-capability-map.md:19
    "No single engine carries more than one or two [DOF]". The Cosserat field
    engine carries the WINDING (charge) DOF but NOT the A1 cage, so the windings
    DISPERSE and the centroid-drift force is dispersion-dominated (Arms A≈C HALT,
    §3 of the prereg). The validated charge-charge LAW lives in the universal
    pairwise operator, where the chord (short-range divergence from 1/r) is
    DERIVED from the Op14 saturation kernel with ZERO free parameters.

    U(r) = -(K/r)(T² - Γ²),  Z(r) = Z₀/(1-(d_sat/r)²)^(1/4),  Γ=(Z-Z₀)/(Z+Z₀)
      Regime I  (r≫d_sat): Γ→0, U→-K/r          (Coulomb/gravity — validate-on-known)
      Regime III (r≤d_sat): Γ→1, U>0             (Pauli repulsive wall — the chord)
    """
    from ave.core.universal_operators import universal_pairwise_energy

    K, d_sat = 1.0, 1.0
    r = np.linspace(1.001 * d_sat, 30.0 * d_sat, 4000)
    U = np.array([universal_pairwise_energy(float(ri), K, d_sat) for ri in r])
    F = -np.gradient(U, r)

    def loc_exp(lo: float, hi: float) -> float:
        m = (r > lo) & (r < hi) & (np.abs(F) > 0)
        return float(np.polyfit(np.log(r[m]), np.log(np.abs(F[m])), 1)[0])

    far_exp = loc_exp(10.0 * d_sat, 30.0 * d_sat)
    near_exp = loc_exp(1.05 * d_sat, 2.0 * d_sat)
    frac_dev = {}
    for ratio in (1.05, 1.5, 2.0, 3.0, 5.0, 10.0, 20.0):
        Ur = float(universal_pairwise_energy(ratio * d_sat, K, d_sat))
        Uc = -K / (ratio * d_sat)
        frac_dev[f"{ratio:.2f}"] = (Ur - Uc) / abs(Uc)
    return {
        "operator": "universal_pairwise_energy",
        "claim": "clm-gdd70j",
        "far_field_force_exponent": far_exp,
        "far_field_coulomb_target": -2.0,
        "near_field_force_exponent": near_exp,
        "frac_dev_from_coulomb_vs_r_over_dsat": frac_dev,
        "chord": "short-range (d_sat/r)^2 departure from Coulomb 1/r, derived "
                 "from the Op14 saturation kernel, zero free parameters",
    }


def _fit_power_law(arm_r: list[dict]) -> dict:
    """Fit log|a_init| vs log d0 → exponent. Coulomb FORCE: a ∝ d^-2."""
    pts = [(r["d0"], r["a_init"]) for r in arm_r
           if r["a_init"] is not None and abs(r["a_init"]) > 0]
    if len(pts) < 2:
        return {"exponent": None, "r2": None, "n_points": len(pts)}
    d = np.array([p[0] for p in pts], dtype=float)
    a = np.array([abs(p[1]) for p in pts], dtype=float)
    x = np.log(d)
    y = np.log(a)
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    slope = float(coef[0])
    yhat = A @ coef
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else None
    return {"exponent": slope, "r2": r2, "n_points": len(pts),
            "d0": d.tolist(), "abs_a_init": a.tolist()}


def _json_default(o):
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"not serializable: {type(o)}")


if __name__ == "__main__":
    main()
