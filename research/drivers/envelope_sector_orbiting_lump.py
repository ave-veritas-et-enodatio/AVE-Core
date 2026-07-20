#!/usr/bin/env python3
"""LEG C — envelope-sector reduction: does an ORBITING saturated mass-envelope
radiate LONGITUDINAL (compression, P-branch) far-field content on the srs lattice,
and does SATURATION (the coefficient picture) change the compression/shear partition?

Prereg (FROZEN, criteria committed ALONE first):
    research/2026-07-20_envelope-sector-reduction_prereg-FROZEN.md   §3 Leg C
Analytic legs:
    research/2026-07-20_envelope-sector-reduction_derivation.md      (Legs 0/A/B)

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (fired before any standard-physics term)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : the TRANSLATIONAL (Cauchy-grade) VECTOR sector of the chiral srs-z3 net
           (ave.core.chiral_lattice._SRS_8A / _SRS_NN; I4₁32, Wyckoff-8a, z=3).
           Rank-2 bond tensor Φ_b = k_a·(d̂⊗d̂) + k_s·(I − d̂⊗d̂). NOT a Cartesian
           Laplacian. Rule-14 reuse of the #761 / srs_band_survey bond model.
  REGIME : SATURATED SOURCE (Op14 ON in the lump core, A₀ = 0.5·A_yield modulates
           the local bond stiffness via S(A) = √(1−A²)), COLD-LINEAR FAR FIELD.
           This is THE distinction from #761 (cold sub-yield breathing source):
           the envelope-lump is a moving OPERATING-POINT bias on the coefficients.
  COORDS : real-space displacement basis (A46-clean): OBSERVABLE = LONGITUDINAL
           (radial, ∇·u) vs TRANSVERSE (tangential, ∇×u) energy partition of the
           RADIATED field at a far shell. κ_env² ≡ F_∥/F_⊥, compared to the frozen
           κ_max² = δ_DP = 1.3e-4.
  CLASS  : lattice-derived EMPIRICAL leg. FALLBACK scope (declared in prereg §3):
           a self-bound saturated soliton is INFEASIBLE (electron-lock arc); this
           tests the COEFFICIENT-coupling question (a driven/pinned saturated
           texture translated in a dipole-free rotating BINARY), NOT envelope
           self-consistency. α-CLEAN (no α/Q_TANK). Every VALUE dimensionless.

ENGINE BYTE-UNTOUCHED: imports ave.core.chiral_lattice / ave.core.constants read-only;
the finite net, the rank-2 bond dynamics, the saturation modulation, and the driven
collective-coordinate stepper are built HERE.

Run: PYTHONPATH=src:src/scripts/vol_1_foundations python3 \
        research/drivers/envelope_sector_orbiting_lump.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy.spatial import cKDTree

# ── engine reads (read-only) ────────────────────────────────────────────────
from ave.core.chiral_lattice import _SRS_8A, _SRS_NN

# ── Rule-14 reuse of the VALIDATED survey pipeline (side-effect-free imports) ─
_VOL1 = Path(__file__).resolve().parents[2] / "src" / "scripts" / "vol_1_foundations"
sys.path.insert(0, str(_VOL1))
from srs_band_survey import srs_primitive_bcc  # noqa: E402
from srs_vector_band_survey import vector_bloch_D  # noqa: E402

TOL = 1e-9
A_YIELD = 1.0  # yield in normalized units; A is reported as A/A_yield


# ═════════════════════════════════════════════════════════════════════════════
# Finite real-space srs net (identical construction to #761 — Rule-14 reuse)
# ═════════════════════════════════════════════════════════════════════════════
def build_finite_srs(L: int):
    cells = np.array(
        [(cx, cy, cz) for cx in range(L) for cy in range(L) for cz in range(L)],
        dtype=float,
    )
    pos = (cells[:, None, :] + _SRS_8A[None, :, :]).reshape(-1, 3)
    tree = cKDTree(pos)
    pairs = tree.query_pairs(r=_SRS_NN + TOL, output_type="ndarray")
    d = pos[pairs[:, 1]] - pos[pairs[:, 0]]
    ln = np.linalg.norm(d, axis=1)
    keep = np.abs(ln - _SRS_NN) < TOL
    pairs, d, ln = pairs[keep], d[keep], ln[keep]
    dhat = d / ln[:, None]
    mid = 0.5 * (pos[pairs[:, 0]] + pos[pairs[:, 1]])  # bond midpoints (for S(A))
    return pos, pairs[:, 0].copy(), pairs[:, 1].copy(), dhat, mid


def bond_tensors(dhat, k_a, k_s, s_factor=None):
    """Per-bond rank-2 Φ_b = S·[k_a d̂⊗d̂ + k_s(I − d̂⊗d̂)]. s_factor (M,) is the
    per-bond saturation factor S(A_bond); None ⇒ cold (S≡1)."""
    P = np.einsum("bi,bj->bij", dhat, dhat)
    Phi = k_a * P + k_s * (np.eye(3)[None] - P)
    if s_factor is not None:
        Phi = Phi * s_factor[:, None, None]
    return Phi


def forces(u, Phi, bi, bj, N):
    du = u[bi] - u[bj]
    fb = np.einsum("bij,bj->bi", Phi, du)
    F = np.zeros((N, 3))
    np.add.at(F, bi, -fb)
    np.add.at(F, bj, +fb)
    return F


def omega_max_cold(Phi, bi, bj, N, iters=60):
    rng = np.random.default_rng(0)
    x = rng.standard_normal((N, 3))
    x /= np.linalg.norm(x)
    lam = 0.0
    for _ in range(iters):
        Dx = -forces(x, Phi, bi, bj, N)
        lam = float(np.linalg.norm(Dx))
        x = Dx / (lam + 1e-30)
    return np.sqrt(max(lam, 1e-12))


def sat_factor_static(mid, centers, A0, sigma):
    """Per-bond S(A_bond) for a STATIC saturated bias texture at fixed `centers`
    (list of (3,) positions). A(x) = A0·Σ exp(−|x−c|²/2σ²), clipped < A_yield.
    Bonds far from every lump have S≈1 (cold far field)."""
    A = np.zeros(mid.shape[0])
    for c in centers:
        r2 = np.sum((mid - c) ** 2, axis=1)
        A += A0 * np.exp(-r2 / (2.0 * sigma**2))
    A = np.clip(A, 0.0, 0.999 * A_YIELD)
    return np.sqrt(1.0 - (A / A_YIELD) ** 2), A


def texture_displacement(pos, center, amp, sigma):
    """Curl-free dilatation texture centered at `center`: u = ∇φ, φ=exp(−r²/2σ²).
    (Same pure-longitudinal seed shape #761 used; here it is the driven lump's
    imposed displacement field.)"""
    rel = pos - center
    r2 = np.sum(rel**2, axis=1)
    phi = np.exp(-r2 / (2.0 * sigma**2))
    u = -(rel / sigma**2) * phi[:, None]
    peak = np.abs(u).max() + 1e-30
    return u * (amp / peak)


def shell_partition(u_shell, rhat_shell):
    """Radial (longitudinal) vs tangential (transverse) energy of a shell field."""
    u_par = np.sum(u_shell * rhat_shell, axis=1)[:, None] * rhat_shell
    u_perp = u_shell - u_par
    E_par = float(np.sum(u_par**2))
    E_perp = float(np.sum(u_perp**2))
    return E_par, E_perp


# ═════════════════════════════════════════════════════════════════════════════
# Driven collective-coordinate stepper (velocity-Verlet with moving BC + moving S)
# ═════════════════════════════════════════════════════════════════════════════
def run_driven(L, centers_fn, amp_fn, sat_on, A0, sigma, r_core, r_meas,
               shell_w, Omega, n_periods, cfl, rho_star, k_s,
               cP_spec, cS_spec):
    """Drive a saturated (or cold) dilatation texture at moving centers and measure
    the far-field radial/tangential energy partition.

      centers_fn(t) -> list of (3,) lump centers at time t   (rotation / fixed)
      amp_fn(t)     -> scalar amplitude of the imposed texture (breathe / fixed)
      sat_on        -> if True, per-bond S(A) modulated by the moving texture
                       (the COEFFICIENT picture); if False, cold (S≡1).

    Core sites (within r_core of any center) are KINEMATICALLY DRIVEN to the imposed
    texture (a moving boundary); the free sites evolve under the rank-2 bond forces
    (with the moving stiffness bias when sat_on). Radiation is measured at the
    r_meas shell over the reflection-free spectral Poincaré window.
    """
    pos, bi, bj, dhat, mid = build_finite_srs(L)
    N = pos.shape[0]
    Phi_base = bond_tensors(dhat, rho_star, k_s, None)  # cold rank-2 bond tensors
    center0 = np.array([L / 2.0] * 3)

    omega_max = omega_max_cold(Phi_base, bi, bj, N)
    dt = cfl * 2.0 / omega_max

    rel0 = pos - center0
    r0 = np.linalg.norm(rel0, axis=1)
    rhat0 = rel0 / (r0[:, None] + 1e-30)
    shell = (r0 >= r_meas) & (r0 < r_meas + shell_w)

    # radiated wave at 2Ω (quadrupole) / Ω (breathe); integrate long enough that
    # the reflection-free window [t_P, t_reflect) is covered plus n_periods drive.
    d_face = L / 2.0
    t_reflect = (2.0 * d_face - r_meas) / (cP_spec + 1e-30)
    T_drive = 2.0 * np.pi / Omega
    t_end = max(1.15 * t_reflect, n_periods * T_drive)
    n_steps = int(np.ceil(t_end / dt)) + 5

    def imposed(t):
        u = np.zeros((N, 3))
        core = np.zeros(N, dtype=bool)
        cs = centers_fn(t)
        a = amp_fn(t)
        for c in cs:
            u += texture_displacement(pos, c, a, sigma)
            core |= (np.linalg.norm(pos - c, axis=1) < r_core)
        return u, core, cs

    def sat_of(cs):
        if not sat_on:
            return None
        s, _ = sat_factor_static(mid, cs, A0, sigma)
        return s

    u = np.zeros((N, 3))
    v = np.zeros((N, 3))
    u_imp, core, cs = imposed(0.0)
    u[core] = u_imp[core]
    free = ~core
    Phi = bond_tensors(dhat, rho_star, k_s, sat_of(cs))
    F = forces(u, Phi, bi, bj, N)

    times, fL, Esh = [], [], []
    for step in range(n_steps):
        t = step * dt
        # measure at the far shell (free-region radiation)
        u_sh = u[shell]
        rh = rhat0[shell]
        E_par, E_perp = shell_partition(u_sh, rh)
        E_tot = E_par + E_perp
        times.append(t)
        fL.append(E_par / (E_tot + 1e-30))
        Esh.append(E_tot)
        # advance free sites; drive the core boundary at t and t+dt
        u[free] = u[free] + v[free] * dt + 0.5 * F[free] * dt**2
        u_imp2, core2, cs2 = imposed(t + dt)
        u[core2] = u_imp2[core2]
        Phi = bond_tensors(dhat, rho_star, k_s, sat_of(cs2))
        F_new = forces(u, Phi, bi, bj, N)
        v[free] = v[free] + 0.5 * (F[free] + F_new[free]) * dt
        F = F_new
        core = core2
        free = ~core2

    times = np.array(times); fL = np.array(fL); Esh = np.array(Esh)
    t_P = r_meas / (cP_spec + 1e-30)
    t_S = r_meas / (cS_spec + 1e-30)
    win = (times >= t_P) & (times < t_reflect)
    if win.sum() < 3:
        win = (times >= t_P) & (times < 0.9 * times[-1])
    w = Esh[win]
    # energy-weighted longitudinal fraction and the bulk/shear partition κ_env²
    # over the reflection-free window
    E_par_win = float(np.sum((fL[win]) * w))
    E_tot_win = float(np.sum(w))
    f_long = E_par_win / (E_tot_win + 1e-30)
    kappa2 = f_long / (1.0 - f_long + 1e-30)          # F_∥/F_⊥ = f_long/(1−f_long)
    return {
        "grid": {"L": L, "N": N, "n_bonds": int(bi.shape[0]), "dt": float(dt),
                 "n_steps": n_steps, "r_core": r_core, "r_meas": r_meas,
                 "shell_w": shell_w, "Omega": Omega, "sat_on": sat_on,
                 "A0": A0, "sigma": sigma, "rho_star": rho_star},
        "omega_max": float(omega_max),
        "scale_sep_Omega_over_omega_max": float(Omega / omega_max),
        "window": {"t_P": float(t_P), "t_S": float(t_S), "t_reflect": float(t_reflect),
                   "captures_S": bool(t_S < t_reflect), "n_win": int(win.sum())},
        "f_long_window": float(f_long),
        "kappa2_F_par_over_F_perp": float(kappa2),
        "kappa_env": float(np.sqrt(max(kappa2, 0.0))),
        "E_par_win": E_par_win, "E_perp_win": float(E_tot_win - E_par_win),
    }


# ── source geometries ────────────────────────────────────────────────────────
def _rotating_binary(center, R, Omega):
    def f(t):
        c, s = np.cos(Omega * t), np.sin(Omega * t)
        off = R * np.array([c, s, 0.0])
        return [center + off, center - off]   # dipole-free binary, Q rotates at 2Ω
    return f


def _fixed_single(center):
    return lambda t: [np.array(center, float)]


# ═════════════════════════════════════════════════════════════════════════════
# C-2 spectral cross-check (cold Bloch structure; #761-parity self-consistency)
# ═════════════════════════════════════════════════════════════════════════════
def run_c2_speeds(rho_star, k_s, n_random=24, seed=1):
    basis, bonds = srs_primitive_bcc("right")
    rng = np.random.default_rng(seed)
    dirs = {"100": [1, 0, 0], "110": [1, 1, 0], "111": [1, 1, 1]}
    rand = rng.standard_normal((n_random, 3))
    rand /= np.linalg.norm(rand, axis=1, keepdims=True)
    for i in range(n_random):
        dirs[f"rand{i}"] = rand[i].tolist()
    kl = 1e-4
    cP_list, cS_list, per_dir = [], [], {}
    for name, dd in dirs.items():
        kh = np.array(dd, float); kh = kh / np.linalg.norm(kh)
        D = vector_bloch_D(kh * kl, basis, bonds, rho_star, k_s)
        w2, V = np.linalg.eigh(D)
        idx = np.argsort(w2)[:3]
        w2a, Va = w2[idx], V[:, idx]
        pol = Va.reshape(4, 3, 3).mean(axis=0)
        pol /= np.linalg.norm(pol, axis=0, keepdims=True) + 1e-30
        long_frac = np.abs(pol.T @ kh) ** 2
        c = np.sqrt(np.clip(w2a, 0, None)) / kl
        pL = int(np.argmax(long_frac))
        cP = float(c[pL]); cS = float(np.mean([c[j] for j in range(3) if j != pL]))
        if name in ("100", "110", "111"):
            per_dir[name] = cP / cS
        cP_list.append(cP); cS_list.append(cS)
    cP_iso = float(np.mean(cP_list)); cS_iso = float(np.mean(cS_list))
    return cP_iso, cS_iso, per_dir


def make_figure(out, path_png):
    """White-style figure: (L) f_long vs Ω for Model C cold vs saturated (the
    saturation-invariance + near→far trend); (R) far-field structural κ_env² vs
    the pulsar kill-lines. Okabe-Ito, honest axes+units, no on-figure title."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from ave.viz import style
    style.apply()
    C = style.COLORS

    oms = [0.15, 0.30]
    fl_cold = [out[f"model_C_orbiting_{t}_cold"]["f_long_window"]
               for t in ("Omega_lo", "Omega_hi")]
    fl_sat = [out[f"model_C_orbiting_{t}_sat"]["f_long_window"]
              for t in ("Omega_lo", "Omega_hi")]
    cc = out["spectral_cold"]["continuum_import_colorcheck_F_bulk_over_F_shear"]
    fl_ff = cc / (1.0 + cc)   # far-field longitudinal fraction from the color-check

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(10.2, 4.2))
    fig.subplots_adjust(left=0.11, right=0.98, bottom=0.15, top=0.90, wspace=0.32)

    axL.plot(oms, fl_cold, "o-", color=C["ave"], label="Model C — cold (S≡1)", ms=8)
    axL.plot(oms, fl_sat, "s--", color=C["comparison"],
             label="Model C — saturated S(A), A₀=0.5  (overlaps cold)", ms=6)
    axL.axhline(out["model_S_breathing_control"]["f_long_window"], color=C["muted"],
                ls=":", label="Model S breathing (control)")
    axL.axhline(fl_ff, color=C["accent"], ls="-.",
                label=f"far-field continuum (spectral) = {fl_ff:.3f}")
    axL.set_xlabel("orbital drive frequency  Ω  (lattice units)")
    axL.set_ylabel("longitudinal energy fraction  f_long = E∥ / (E∥+E⊥)")
    axL.set_ylim(0, 1.05)
    axL.legend(loc="upper right", fontsize=7, frameon=False)

    labels = ["far-field κ_env²\n(spectral)", "κ_max²\n(Hulse-Taylor)",
              "κ_max²\n(double pulsar)"]
    vals = [cc, 1.6e-3, 1.3e-4]
    cols = [C["ave"], C["muted"], C["comparison"]]
    axR.bar(range(3), vals, color=cols, width=0.6)
    axR.set_yscale("log")
    axR.set_xticks(range(3))
    axR.set_xticklabels(labels, fontsize=8)
    axR.set_ylabel("bulk/shear flux fraction  κ² = F_bulk / F_shear")
    axR.set_ylim(5e-5, 1e-1)
    axR.axhline(1.3e-4, color=C["comparison"], ls=":", lw=1)
    axR.annotate(f"port OPEN: {cc / 1.3e-4:.0f}×\nthe double-pulsar bound",
                 xy=(0, cc), xytext=(0.35, 3.2e-2), fontsize=8, color=C["data"])

    fig.savefig(path_png, dpi=150, bbox_inches="tight")
    fig.savefig(str(Path(path_png).with_suffix(".pdf")), bbox_inches="tight")
    plt.close(fig)


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--L", type=int, default=20)
    ap.add_argument("--out", default=str(Path(__file__).with_name(
        "envelope_sector_orbiting_lump_results.json")))
    args = ap.parse_args()

    RHO_STAR = 9.77337           # DERIVED from ν_Hill=2/7 (imported, not fit)
    K_S = 1.0
    SIGMA = 1.2                  # texture width (cells) — matches #761 seed
    R_CORE = 1.8                 # driven-core radius (cells)
    R_MEAS = 6.0                 # far shell (cells) — frozen
    SHELL_W = 1.0
    A0 = 0.5                     # saturated core operating point A₀ = 0.5·A_yield
    R_ORBIT = 2.5                # binary separation half (cells)
    CFL = 0.2
    NPER = 6

    # spectral speeds (cold Bloch) — window + #761-parity self-consistency gate
    cP_iso, cS_iso, cpcs_dir = run_c2_speeds(RHO_STAR, K_S)

    out = {
        "provenance": {
            "class": "LEG C — envelope-sector orbiting-lump; coefficient-coupling "
                     "FALLBACK (self-bound soliton infeasible per electron-lock arc); "
                     "mints no canon; engine byte-untouched",
            "kappa_max2_double_pulsar": 1.3e-4,
            "kappa_max_double_pulsar": 0.011401754250991,
            "note": "κ_env² = F_∥/F_⊥ measured at the far shell; compared to "
                    "κ_max² = δ_DP = 1.3e-4 (frozen prereg §1).",
        },
        "spectral_cold": {
            "cP_iso": cP_iso, "cS_iso": cS_iso, "cP_over_cS_iso": cP_iso / cS_iso,
            "cP_over_cS_dir": cpcs_dir,
            "continuum_import_colorcheck_F_bulk_over_F_shear":
                (2.0 / 3.0) * (cS_iso / cP_iso) ** 5,
        },
    }

    # ── Model S: BREATHING control (single fixed core, amplitude oscillating) ──
    OM_S = 0.20
    out["model_S_breathing_control"] = run_driven(
        L=args.L, centers_fn=_fixed_single([args.L / 2.0] * 3),
        amp_fn=lambda t, w=OM_S: A0 * np.sin(w * t), sat_on=False, A0=A0,
        sigma=SIGMA, r_core=R_CORE, r_meas=R_MEAS, shell_w=SHELL_W, Omega=OM_S,
        n_periods=NPER, cfl=CFL, rho_star=RHO_STAR, k_s=K_S,
        cP_spec=cP_iso, cS_spec=cS_iso)

    # ── Model C: ORBITING binary (quadrupole at 2Ω) — cold AND saturated ──
    center = [args.L / 2.0] * 3
    for tag, OM in (("Omega_lo", 0.15), ("Omega_hi", 0.30)):
        for sat in (False, True):
            key = f"model_C_orbiting_{tag}_{'sat' if sat else 'cold'}"
            out[key] = run_driven(
                L=args.L, centers_fn=_rotating_binary(np.array(center), R_ORBIT, OM),
                amp_fn=lambda t: A0, sat_on=sat, A0=A0, sigma=SIGMA,
                r_core=R_CORE, r_meas=R_MEAS, shell_w=SHELL_W, Omega=OM,
                n_periods=NPER, cfl=CFL, rho_star=RHO_STAR, k_s=K_S,
                cP_spec=cP_iso, cS_spec=cS_iso)

    # ── multipole-order check: F_par & F_perp scaling exponent in Ω (cold) ──
    lo = out["model_C_orbiting_Omega_lo_cold"]
    hi = out["model_C_orbiting_Omega_hi_cold"]
    r_om = 0.30 / 0.15
    with np.errstate(divide="ignore", invalid="ignore"):
        n_par = np.log(hi["E_par_win"] / (lo["E_par_win"] + 1e-300)) / np.log(r_om)
        n_perp = np.log(hi["E_perp_win"] / (lo["E_perp_win"] + 1e-300)) / np.log(r_om)
    out["multipole_check"] = {
        "n_exponent_F_par": float(n_par), "n_exponent_F_perp": float(n_perp),
        "same_order": bool(abs(n_par - n_perp) < 1.0),
        "note": "same Ω-scaling exponent ⇒ compression & shear at same multipole "
                "order ⇒ κ_env²=F_∥/F_⊥ is structural (Ω-independent), comparable "
                "to κ_max². Frozen prereg §3.",
    }

    # ── verdict summary (frozen-criterion outputs only) ──
    kc_cold = out["model_C_orbiting_Omega_lo_cold"]["kappa2_F_par_over_F_perp"]
    kc_sat = out["model_C_orbiting_Omega_lo_sat"]["kappa2_F_par_over_F_perp"]
    out["verdict_frozen_outputs"] = {
        "kappa2_env_C_cold": kc_cold,
        "kappa2_env_C_sat": kc_sat,
        "kappa_max2": 1.3e-4,
        "exceeds_kappa_max_cold": bool(kc_cold > 1.3e-4),
        "exceeds_kappa_max_sat": bool(kc_sat > 1.3e-4),
        "sat_over_cold_ratio": float(kc_sat / (kc_cold + 1e-300)),
        "model_S_f_long": out["model_S_breathing_control"]["f_long_window"],
    }

    Path(args.out).write_text(json.dumps(out, indent=2))
    make_figure(out, str(Path(args.out).with_name(
        "envelope_sector_orbiting_lump.png")))
    print(json.dumps(out["verdict_frozen_outputs"], indent=2))
    print("spectral cP/cS iso =", round(cP_iso / cS_iso, 4), "dir =",
          {k: round(v, 4) for k, v in cpcs_dir.items()})
    print("multipole:", out["multipole_check"])
    return out


if __name__ == "__main__":
    main()
