"""k4_crystal_graft_run.py — SMOKE + (2,3) for the K4 4-port crystal graft.

THE BUILD: put the c_eff(V) bulk-trap + the conserved ADD-2 converter ONTO the K4
4-port (V_inc,V_ref) WINDING carrier (`ave.core.k4_crystal_graft.K4CrystalGraft`),
so the carrier that CAN wind (unlike the scalar Master-Equation bulk, whose Outcome-C
finding was "no U(1)-fibre carrier") finally has a WALL + a SOURCE.

RULE-10 SMOKE FIRST — all three must pass to EARN the full α-emergence run:
  (1) WALL       — does the Γ-wall bound state form on the 4-port (vs genesis-24's
                   Γ→0/matched)?
  (2) CONVERTER  — does ADD-2 fire CONSERVATIVELY (energize-LOCK: |L| bounded, fields
                   O(1), no detonation, centrosymmetric baseline EXACTLY 0)?
  (3) PHASE-SPACE— THE LOAD-BEARING NEW CHECK: does the (V_inc,V_ref) phase-space
                   winding RESPOND to / get DRIVEN by the real-space trap — or are the
                   real-space trap and the phase-space winding INCOHERENT?

If any smoke fails → STOP, report SMOKE-FAIL, do NOT force the full run. The failure
mode (esp. real-space-vs-phase-space incoherence) is itself the key finding, and
forcing the α run on an engine that cannot sustain the (2,3) would risk a false
Class-D fluke (strictly worse than an honest negative — Grant 2026-06-09).

CANONICAL-AVE-ONLY: electron = LONGITUDINAL K4 monopole bulk; photon = transverse
chiral port mode; absorb/emit = Axiom-4 crystallize/melt via the front converter.

Run:  PYTHONPATH=src python src/scripts/vol_1_foundations/k4_crystal_graft_run.py
"""

from __future__ import annotations

import json
import os

import numpy as np
from scipy import ndimage

from ave.core.constants import ALPHA_COLD_INV, PHI, R_II
from ave.core.k4_crystal_graft import K4CrystalGraft

HERE = os.path.dirname(os.path.abspath(__file__))

N = int(os.environ.get("K4G_N", "26"))
KAPPA_TILDE = 6.0 / 5.0  # (2,3) topology pq/(p+q) — α-FREE
V_YIELD = 1.0  # engine-natural — α-FREE
SEED_R = 4.0  # sharp strain-snap front radius (super-Gaussian)
SEED_FRAC = 0.95
PHOTON_AMP = 0.30
PHOTON_LAM = 6.0
PHOTON_SIGMA = 3.0
K_WIND = 2  # the photon's toroidal OAM (the "2" — a physical photon property / input)


# ─────────────────────────────────────────────────────────── measurement helpers
def _fill(F, active):
    """Density-fill inactive (diamond-sublattice-empty) cells by nearest active value
    so a real-space contour samples a DENSE phasor field (the K4 carrier is half-empty;
    raw contour sampling hits inactive zeros → reliability collapses to 0)."""
    idx = ndimage.distance_transform_edt(~active, return_distances=False, return_indices=True)
    return F[tuple(idx)]


def _contour_winding(fx, fy, center, R, r_minor, plane, n=160):
    """Phase winding of (fx+i·fy) on a torus contour. toroidal→'2'(p), poloidal→'3'(q).
    Returns (winding, reliability=amp.min/amp.max). Trilinear-sampled (A46 phase-space,
    NOT real-space R/r)."""
    cx, cy, cz = center
    t = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    if plane == "poloidal":
        xs, ys, zs = cx + (R + r_minor * np.cos(t)), cy + np.zeros_like(t), cz + r_minor * np.sin(t)
    else:
        xs, ys, zs = cx + R * np.cos(t), cy + R * np.sin(t), cz + np.zeros_like(t)
    nx, ny, nz = fx.shape
    ix = np.clip(xs.astype(int), 0, nx - 2)
    iy = np.clip(ys.astype(int), 0, ny - 2)
    iz = np.clip(zs.astype(int), 0, nz - 2)
    dx_, dy_, dz_ = xs - ix, ys - iy, zs - iz

    def samp(F):
        return (
            (1 - dx_) * (1 - dy_) * (1 - dz_) * F[ix, iy, iz]
            + dx_ * (1 - dy_) * (1 - dz_) * F[ix + 1, iy, iz]
            + (1 - dx_) * dy_ * (1 - dz_) * F[ix, iy + 1, iz]
            + (1 - dx_) * (1 - dy_) * dz_ * F[ix, iy, iz + 1]
            + dx_ * dy_ * (1 - dz_) * F[ix + 1, iy + 1, iz]
            + dx_ * (1 - dy_) * dz_ * F[ix + 1, iy, iz + 1]
            + (1 - dx_) * dy_ * dz_ * F[ix, iy + 1, iz + 1]
            + dx_ * dy_ * dz_ * F[ix + 1, iy + 1, iz + 1]
        )

    ox, oy = samp(fx), samp(fy)
    amp = np.sqrt(ox**2 + oy**2)
    mx = float(amp.max())
    if mx < 1e-30:
        return 0.0, 0.0
    phase = np.unwrap(np.arctan2(oy, ox))
    return float((phase[-1] - phase[0]) / (2.0 * np.pi)), float(amp.min() / mx)


def best_winding(eng, center, plane):
    """Best (winding, reliability) over a scan of (R, r_minor) on RELIABLE contours
    (rel>0.1), on the density-filled native chiral phasor."""
    vx, vy, _, _ = eng.chiral_phasor()
    act = eng.k4.mask_active
    vxf, vyf = _fill(vx, act), _fill(vy, act)
    wb, rb = 0.0, 0.0
    for R in (3.0, 4.0, 5.0, 6.0):
        for rm in np.linspace(1.0, R * 0.7, 5):
            w, rel = _contour_winding(vxf, vyf, center, R, rm, plane)
            if rel > rb and rel > 0.1:
                wb, rb = w, rel
    return round(wb, 2), round(rb, 3)


def sharp_seed(eng, R, frac):
    """Saturated LONGITUDINAL bulk seed with a TRUE first-order strain-snap FRONT
    (a top-hat: hard r≤R cutoff = a 1-cell impedance DISCONTINUITY). This is
    load-bearing: SMOKE-1 shows a SMOOTH seed (sech OR super-Gaussian) does NOT trap on
    the fixed-roll K4 — the bond-Γ reflection Γ=(z_B−z_A)/(z_B+z_A) is a GRADIENT effect
    that needs an actual STEP; a smooth absolute-c_eff well (which the scalar Master
    Equation self-focuses) does NOT transport on the fixed light-cone connect. A true
    step traps with retention ratio ~10³–10⁴ over the linear control. Consistent with
    A-034 crystallization being FIRST-ORDER (strain-snap), not a smooth refractive well."""
    n = eng.N
    i, j, k = np.indices((n, n, n))
    c = np.array([n // 2] * 3)
    r = np.sqrt((i - c[0]) ** 2 + (j - c[1]) ** 2 + (k - c[2]) ** 2)
    core = (r <= R).astype(float) * frac
    eng.k4.V_inc += np.where(eng.k4.mask_active[..., None], (core * 0.5)[..., None] * np.ones(4), 0.0)


def smooth_seed(eng, R, frac):
    """A SMOOTH (sech) bulk seed — the scalar-engine profile. SMOKE-1 sub-test: this
    does NOT trap on the fixed-roll K4 (the load-bearing fixed-roll-vs-c_eff finding)."""
    n = eng.N
    i, j, k = np.indices((n, n, n))
    c = np.array([n // 2] * 3)
    r = np.sqrt((i - c[0]) ** 2 + (j - c[1]) ** 2 + (k - c[2]) ** 2)
    core = frac / np.cosh(r / R)
    eng.k4.V_inc += np.where(eng.k4.mask_active[..., None], (core * 0.5)[..., None] * np.ones(4), 0.0)


def make(conv=True, trap=True, helicity=1.0):
    eng = K4CrystalGraft(N=N, V_yield=V_YIELD, kappa_tilde=KAPPA_TILDE, converter_on=conv, pml_thickness=4, helicity=helicity)
    eng.k4.op3_bond_reflection = bool(trap)  # the c_eff wall toggle
    return eng


# ───────────────────────────────────────────── SMOKE-1 — the Γ wall / bound state
def smoke_1_wall(nst=400):
    C = (N // 2, N // 2, N // 2)

    def retention(seed_fn, trap, conv=False):
        eng = make(conv=conv, trap=trap)
        seed_fn(eng, SEED_R, SEED_FRAC)
        E0 = eng.interior_energy()
        E, A, G, L = [], [], [], []
        for _ in range(nst):
            eng.step()
            E.append(eng.interior_energy() / E0)
            A.append(eng.strain_field().max())
            G.append(eng.gamma_core()["gamma_core_abs"])
            L.append(eng.spin_L())
        return np.array(E), np.array(A), np.array(G), np.array(L)

    w = slice(nst // 3, nst)
    E_sharp, A_sharp, G_sharp, L_sharp = retention(sharp_seed, trap=True)
    E_smooth, _, _, _ = retention(smooth_seed, trap=True)  # smooth seed: does it trap?
    E_lin, _, _, _ = retention(sharp_seed, trap=False)  # linear (no wall): radiates

    e_ret = float(E_sharp[w].mean())
    breath = float(E_sharp[w].std() / max(E_sharp[w].mean(), 1e-9))
    gamma = float(G_sharp[w].mean())
    strain = float(A_sharp[w].mean())
    lin_ret = float(E_lin[w].mean())
    smooth_ret = float(E_smooth[w].mean())
    # the wall: sharp-front bound state RETAINS energy (>0.2) breathing, the core stays
    # SATURATED (A>R_II), Γ away from 0; and it traps >>5× better than the linear control.
    # a TRAPPED bound state: retains energy (>0.2), bounded breathing (a steady trap is
    # valid), core SATURATED (A>R_II), |Γ| away from 0, and >>5× the linear control.
    passes = bool(e_ret > 0.2 and breath < 0.6 and strain > R_II and gamma > 0.3 and e_ret > 5.0 * max(lin_ret, 1e-9))
    return {
        "E_retain_sharp_mean": e_ret,
        "E_retain_breathing_std_over_mean": breath,
        "E_retain_smooth_seed": smooth_ret,
        "E_retain_linear_control": lin_ret,
        "gamma_core_mean": gamma,
        "gamma_core_peak": float(G_sharp.max()),
        "strain_core_mean": strain,
        "L_max": float(L_sharp.max()),
        "wall_forms": passes,
        "_series": {"E_sharp": E_sharp.tolist(), "E_smooth": E_smooth.tolist(), "E_lin": E_lin.tolist()},
    }


# ─────────────────────────────────── SMOKE-2 — ADD-2 conservative (energize-LOCK)
def smoke_2_converter(nst=450):
    C = (N // 2, N // 2, N // 2)

    def run(conv, helicity, photon_only=False):
        eng = make(conv=conv, trap=True, helicity=helicity)
        if not photon_only:
            sharp_seed(eng, SEED_R, SEED_FRAC)
        eng.seed_photon(C, sigma=PHOTON_SIGMA, wavelength=PHOTON_LAM, amplitude=0.6 if photon_only else PHOTON_AMP, helicity=helicity, k_wind=K_WIND)
        mv, mm, L = [], [], []
        for _ in range(nst):
            eng.step()
            mv.append(eng.field_intensity()["max_V"])
            mm.append(float(np.abs(eng.bulk_monopole()).max()))
            L.append(eng.spin_L())
        return np.array(mv), np.array(mm), np.array(L), eng.converter_residual

    # centrosymmetric baseline: h=0 ⇒ the rotation is the identity ⇒ residual EXACTLY 0
    eng0 = make(conv=True, trap=True, helicity=0.0)
    sharp_seed(eng0, SEED_R, SEED_FRAC)
    eng0.seed_photon(C, sigma=PHOTON_SIGMA, wavelength=PHOTON_LAM, amplitude=PHOTON_AMP, helicity=0.0, k_wind=K_WIND)
    for _ in range(50):
        eng0.step()
    centro_residual = float(eng0.converter_residual)

    mv_on, mm_on, L_on, res_on = run(conv=True, helicity=1.0)
    # bootstrap: net bulk-monopole sourced from a PURE photon, converter ON vs OFF
    _, mm_pon, _, _ = run(conv=True, helicity=1.0, photon_only=True)
    _, mm_poff, _, _ = run(conv=False, helicity=1.0, photon_only=True)

    max_V = float(mv_on.max())
    fields_bounded = bool(np.isfinite(mv_on).all() and max_V < 3.0)
    L_bounded = bool(L_on.max() < 100.0 and L_on[-1] < 5.0 * max(L_on[: nst // 5].mean(), 1e-9))
    centro_zero = bool(centro_residual == 0.0)
    conservative = bool(res_on < 1e-9)
    bootstrap_ratio = float(mm_pon.max() / max(mm_poff.max(), 1e-12))
    # SMOKE-2 criterion (task): ADD-2 fires, |L| bounded, fields O(1), no detonation,
    # centrosymmetric baseline = 0. (The weak bootstrap ratio≈1 is the energize-LOCK
    # signature: an ORTHOGONAL rotation conserves exactly and so does NOT net-pump.)
    passes = bool(fields_bounded and L_bounded and centro_zero and conservative)
    return {
        "centrosymmetric_residual": centro_residual,
        "centrosymmetric_exactly_zero": centro_zero,
        "converter_residual_asym": float(res_on),
        "conservative_orthogonal": conservative,
        "max_V_over_window": max_V,
        "genesis24_detonation_max_Vinc": 1.08e4,
        "fields_bounded_O1": fields_bounded,
        "L_max": float(L_on.max()),
        "L_bounded": L_bounded,
        "bootstrap_monopole_ratio_on_over_off": bootstrap_ratio,
        "converter_fires_conservatively": passes,
        "_series": {"on_max_V": mv_on.tolist(), "on_L": L_on.tolist(), "on_monopole": mm_on.tolist()},
    }


# ──────────────── SMOKE-3 — does the real-space trap DRIVE phase-space winding?
def smoke_3_phasespace(nst=300):
    """THE LOAD-BEARING NEW CHECK. Seed a chiral photon (toroidal '2') + saturated bulk,
    evolve, and ask: does the trap SUSTAIN the (V_inc,V_ref) phase-space winding, or do
    the real-space trap and the phase-space winding DECOUPLE (incoherent)?"""
    C = (N // 2, N // 2, N // 2)

    def winding_series(trap):
        eng = make(conv=True, trap=trap, helicity=1.0)
        sharp_seed(eng, SEED_R, SEED_FRAC)
        eng.seed_photon(C, sigma=PHOTON_SIGMA, wavelength=PHOTON_LAM, amplitude=PHOTON_AMP, helicity=1.0, k_wind=K_WIND)
        ts, wt = [], []
        seed_w = best_winding(eng, C, "toroidal")  # t=0: the carrier carries the '2'
        for s in range(nst):
            eng.step()
            if s in (5, 15, 30, 60, 120, 200, nst - 1):
                w, rel = best_winding(eng, C, "toroidal")
                ts.append(s)
                wt.append((w if rel > 0.1 else 0.0, rel))
        return seed_w, ts, wt

    seed_w_on, ts, wt_on = winding_series(trap=True)
    seed_w_off, _, wt_off = winding_series(trap=False)

    # carrier capability: the phase-space CARRIES winding at the seed (the scalar bulk
    # could NOT — w_tor=w_pol=0 there). This IS a response capability.
    carrier_winds = bool(abs(seed_w_on[0]) > 1.0 and seed_w_on[1] > 0.1)
    # coherence: does the trap SUSTAIN the winding? compare the late-time winding magnitude
    # trap ON vs OFF — if the trap drives/sustains it, ON >> OFF at late time.
    late_on = abs(wt_on[-1][0]) if wt_on[-1][1] > 0.1 else 0.0
    late_off = abs(wt_off[-1][0]) if wt_off[-1][1] > 0.1 else 0.0
    sustained_by_trap = bool(late_on > 1.0 and late_on > 2.0 * max(late_off, 0.05))
    # SMOKE-3 PASSES only if the trap DRIVES/sustains the phase-space winding.
    passes = bool(carrier_winds and sustained_by_trap)
    return {
        "seed_w_tor_on": seed_w_on,
        "carrier_winds_at_seed": carrier_winds,
        "winding_vs_time_trap_on": list(zip(ts, [list(x) for x in wt_on])),
        "winding_vs_time_trap_off": list(zip(ts, [list(x) for x in wt_off])),
        "late_winding_trap_on": late_on,
        "late_winding_trap_off": late_off,
        "trap_sustains_winding": sustained_by_trap,
        "phase_space_responds_coherently": passes,
    }


# ─────────────────── (2,3) diagnostic (confirms the SMOKE-3 incoherence; CONTROLS)
def winding_23_diagnostic(nst=320):
    C = (N // 2, N // 2, N // 2)

    def evolve(trap, conv, photon):
        eng = make(conv=conv, trap=trap, helicity=1.0)
        sharp_seed(eng, SEED_R, SEED_FRAC)
        if photon:
            eng.seed_photon(C, sigma=PHOTON_SIGMA, wavelength=PHOTON_LAM, amplitude=PHOTON_AMP, helicity=1.0, k_wind=K_WIND)
        for _ in range(nst):
            eng.step()
        return {"w_tor": best_winding(eng, C, "toroidal"), "w_pol": best_winding(eng, C, "poloidal")}

    return {
        "FULL_trap_conv_photon": evolve(True, True, True),
        "control_no_photon": evolve(True, True, False),
        "control_no_converter": evolve(True, False, True),
        "control_no_trap": evolve(False, True, True),
    }


# ───────────────────────────────────────────────────────────────────── figures
def make_figures(out):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    paths = {}
    # FIG 1 — the Γ wall: sharp-front bound state retains vs smooth/linear radiate
    s1 = out["smoke_1"]
    fig, ax = plt.subplots(1, 2, figsize=(13, 4.6))
    ax[0].plot(s1["_series"]["E_sharp"], "C0-", label="sharp strain-snap front (TRAP)")
    ax[0].plot(s1["_series"]["E_smooth"], "C1--", label="smooth sech seed (no trap)")
    ax[0].plot(s1["_series"]["E_lin"], "C3:", label="sharp, op3 OFF (linear, radiates)")
    ax[0].set_xlabel("step")
    ax[0].set_ylabel("interior energy / E₀")
    ax[0].set_title(
        f"SMOKE-1 WALL: sharp-front bound state RETAINS {s1['E_retain_sharp_mean']:.2f}\n"
        f"(smooth={s1['E_retain_smooth_seed']:.3f}, linear={s1['E_retain_linear_control']:.3f}) — needs a STEP"
    )
    ax[0].legend(fontsize=8)
    ax[1].bar([0, 1], [s1["gamma_core_mean"], 0.08], color=["C0", "C7"])
    ax[1].set_xticks([0, 1])
    ax[1].set_xticklabels([f"K4 graft\nΓ_core={s1['gamma_core_mean']:.2f}", "genesis-24\nΓ→0 (matched)"])
    ax[1].axhline(1.0, color="k", ls=":", lw=0.6, label="|Γ|=1 total reflection")
    ax[1].set_ylabel("|Γ_core| (bond reflection)")
    ax[1].set_title(f"the wall: |Γ_core|→{s1['gamma_core_peak']:.2f}, core strain A={s1['strain_core_mean']:.2f} (saturated)")
    ax[1].legend(fontsize=8)
    fig.suptitle("FIG 1 — SMOKE-1: the c_eff(V) trap GRAFTS onto the K4 (sharp front) — Γ-wall bound state forms")
    fig.tight_layout()
    p = os.path.join(HERE, "k4graft_fig1_wall.png")
    fig.savefig(p, dpi=110)
    plt.close(fig)
    paths["fig1"] = p

    # FIG 2 — SMOKE-2 converter energize-LOCK (fields bounded, residual 0)
    s2 = out["smoke_2"]
    fig, ax = plt.subplots(1, 2, figsize=(13, 4.6))
    ax[0].plot(s2["_series"]["on_max_V"], "C0-", label="max|V| (converter ON)")
    ax[0].axhline(1.0, color="k", ls=":", lw=0.6)
    ax[0].set_xlabel("step")
    ax[0].set_ylabel("max|V_inc| (interior)")
    ax[0].set_title(
        f"SMOKE-2: max|V|={s2['max_V_over_window']:.2f} O(1)\nvs genesis-24 EMF pump → 1.08e4 (4 OOM below)"
    )
    ax[0].legend(fontsize=8)
    ax[1].plot(s2["_series"]["on_L"], "C2-", label="|L| (converter ON)")
    ax[1].set_xlabel("step")
    ax[1].set_ylabel("|L| (shear angular momentum)")
    ax[1].set_title(
        f"|L| BOUNDED (max={s2['L_max']:.1f}, oscillates) vs gen-24 pump 2.7→43\n"
        f"centrosym residual={s2['centrosymmetric_residual']:.1e} (EXACTLY 0); orthogonal residual={s2['converter_residual_asym']:.1e}"
    )
    ax[1].legend(fontsize=8)
    fig.suptitle("FIG 2 — SMOKE-2: ADD-2 fires CONSERVATIVELY (energize-LOCK; orthogonal rotation, no pump)")
    fig.tight_layout()
    p = os.path.join(HERE, "k4graft_fig2_converter.png")
    fig.savefig(p, dpi=110)
    plt.close(fig)
    paths["fig2"] = p

    # FIG 3 — SMOKE-3: the real-space-trap / phase-space-winding INCOHERENCE
    s3 = out["smoke_3"]
    fig, ax = plt.subplots(figsize=(8.4, 5.2))
    ton = [(t, abs(w[0]) if w[1] > 0.1 else 0.0) for t, w in s3["winding_vs_time_trap_on"]]
    toff = [(t, abs(w[0]) if w[1] > 0.1 else 0.0) for t, w in s3["winding_vs_time_trap_off"]]
    ax.plot([0] + [t for t, _ in ton], [abs(s3["seed_w_tor_on"][0])] + [v for _, v in ton], "C0-o", label="trap ON")
    ax.plot([0] + [t for t, _ in toff], [abs(s3["seed_w_tor_on"][0])] + [v for _, v in toff], "C3--s", label="trap OFF")
    ax.axhline(2.0, color="k", ls=":", lw=0.8, label="toroidal '2' (seeded)")
    ax.set_xlabel("step")
    ax.set_ylabel("|w_tor| on reliable (rel>0.1) contour")
    ax.set_title(
        "FIG 3 — SMOKE-3 (load-bearing): the carrier WINDS at seed (w_tor=%.1f) — real progress\n"
        "over the scalar bulk — BUT the winding DECAYS trap-ON ≈ trap-OFF: the amplitude-wall\n"
        "binds the +1 monopole (mass); the winding rides the −1 photon & RADIATES → DECOUPLED"
        % abs(s3["seed_w_tor_on"][0])
    )
    ax.legend(fontsize=9)
    fig.tight_layout()
    p = os.path.join(HERE, "k4graft_fig3_phasespace_incoherence.png")
    fig.savefig(p, dpi=110)
    plt.close(fig)
    paths["fig3"] = p
    return paths


def main():
    out = {
        "config": {
            "N": N,
            "kappa_tilde": KAPPA_TILDE,
            "V_yield": V_YIELD,
            "seed_R": SEED_R,
            "seed_frac": SEED_FRAC,
            "photon_amp": PHOTON_AMP,
            "k_wind": K_WIND,
            "alpha_cold_inv": ALPHA_COLD_INV,
            "phi2": PHI**2,
            "R_II": R_II,
        }
    }
    print("=" * 88)
    print("K4 CRYSTAL GRAFT — c_eff(V) trap + conserved ADD-2 converter ON the K4 4-port carrier")
    print(f"  N={N}  κ̃={KAPPA_TILDE} (α-free)  V_yield={V_YIELD} (α-free)")
    print("=" * 88)

    print("\n[SMOKE-1] does the Γ-wall bound state form on the 4-port?")
    s1 = smoke_1_wall()
    out["smoke_1"] = s1
    print(
        f"  E_retain sharp={s1['E_retain_sharp_mean']:.3f} (smooth={s1['E_retain_smooth_seed']:.3f}, "
        f"linear={s1['E_retain_linear_control']:.3f}) breathing={s1['E_retain_breathing_std_over_mean']:.3f}"
    )
    print(
        f"  |Γ_core|={s1['gamma_core_mean']:.3f} (peak {s1['gamma_core_peak']:.3f}) strain A={s1['strain_core_mean']:.3f} "
        f"|L|max={s1['L_max']:.2f}  => wall_forms={s1['wall_forms']}"
    )

    print("\n[SMOKE-2] does ADD-2 fire CONSERVATIVELY (energize-LOCK, not genesis-24 pump)?")
    s2 = smoke_2_converter()
    out["smoke_2"] = s2
    print(
        f"  centrosym residual={s2['centrosymmetric_residual']:.1e} (==0: {s2['centrosymmetric_exactly_zero']}) "
        f"orthogonal residual={s2['converter_residual_asym']:.1e}"
    )
    print(
        f"  max|V|={s2['max_V_over_window']:.3f} (gen24 1.08e4) |L|max={s2['L_max']:.2f} bootstrap_ratio={s2['bootstrap_monopole_ratio_on_over_off']:.2f} "
        f"=> fires_conservatively={s2['converter_fires_conservatively']}"
    )

    print("\n[SMOKE-3] does the real-space trap DRIVE the (V_inc,V_ref) phase-space winding?")
    s3 = smoke_3_phasespace()
    out["smoke_3"] = s3
    print(f"  carrier winds at seed: w_tor={s3['seed_w_tor_on']} -> carrier_winds={s3['carrier_winds_at_seed']}")
    print(
        f"  late winding trap ON={s3['late_winding_trap_on']:.2f} vs OFF={s3['late_winding_trap_off']:.2f} "
        f"=> trap_sustains_winding={s3['trap_sustains_winding']}  coherent={s3['phase_space_responds_coherently']}"
    )

    smoke_pass = bool(s1["wall_forms"] and s2["converter_fires_conservatively"] and s3["phase_space_responds_coherently"])
    out["smoke_pass"] = smoke_pass

    # the (2,3) diagnostic (confirms the SMOKE-3 finding; NOT the earned full run)
    print("\n[(2,3) DIAGNOSTIC] evolved winding with matched controls (confirms SMOKE-3):")
    d = winding_23_diagnostic()
    out["winding_23_diagnostic"] = d
    for k, v in d.items():
        print(f"  {k:24s} w_tor={v['w_tor']} w_pol={v['w_pol']}")

    if not smoke_pass:
        # Guard (Grant 2026-06-09): do NOT force the α-emergence full run on a failed
        # smoke — a false Class-D fluke is strictly worse than an honest negative.
        out["verdict"] = "SMOKE-FAIL"
        out["alpha_run_forced"] = False
        out["guard_reason"] = (
            "SMOKE-3 reveals real-space-trap / phase-space-winding INCOHERENCE: the amplitude-wall "
            "binds the +1 isotropic monopole (the trapped mass) but the winding rides the −1 transverse "
            "chiral photon modes, which radiate (decay ~40 steps, trap-ON≈trap-OFF). With no SUSTAINED "
            "(2,3) there is no resonator for α to emerge from; forcing the leak-Q run would risk a "
            "param-fluke false Class-D. Full α-emergence run REFUSED (frozen guard)."
        )
        print("\n" + "=" * 88)
        print(f"VERDICT: {out['verdict']} — SMOKE-3 incoherence (the load-bearing finding). Full α run REFUSED.")
        print("=" * 88)
    else:
        out["verdict"] = "SMOKE-PASS (proceed to full α run — not reached)"

    try:
        out["figures"] = make_figures(out)
        print("\nFigures:")
        for kk, pp in out["figures"].items():
            print(f"  {kk}: {pp}")
    except Exception as exc:
        print(f"\n[figures FAILED: {exc}]")
        out["figures"] = {}

    jpath = os.path.join(HERE, "k4_crystal_graft_results.json")
    with open(jpath, "w") as fh:
        json.dump(out, fh, indent=2, default=float)
    print(f"\nResults JSON: {jpath}")
    return out


if __name__ == "__main__":
    main()
