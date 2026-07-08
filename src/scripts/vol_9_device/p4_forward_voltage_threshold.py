"""P4 — forward-voltage conduction threshold for charge-keyed static loading.

Contention P4 of the paper-hardening epic. Grant ruled P4 = YES cutoff-limited and
reframed the lattice cutoff as a *forward-voltage / minimum-bias-to-conduct
threshold* V_f. This driver FORMALIZES the DIAC-gated varactor circuit, tests
whether V_f is FORCED or FREE against the canonical scales, and computes the
X-ray-through-copper + muonic-with-threshold constraints.

Frozen prereg: research/2026-07-08_p4-forward-voltage-threshold_prereg_FROZEN.md.

SECTOR (mandatory): T2 transverse permittivity (the eps-grade varactor; the shunt-C
per node, eps_eff = eps0 S(A_V), A_V = V/V_yield = |E|/E_yield). NOT the A1 bond
compliance C0/S keyed V_snap; NOT the mu-grade circulation inductor; NOT the
real-carrier (pair-production) sector. The threshold gates the T2 varactor.

REGIME: cold lattice (A=0 => S=1) driven to a HELD STATIC bias, probed weak
small-signal, Ax3-lossless below V_snap. The proposed threshold V_f is a DEAD ZONE
in the reactive varactor: flat at C0/eps0 for |V|<V_f, loading for |V|>=V_f.
Polarity-symmetric (S depends on E^2) => the gate is a DIAC (back-to-back diodes).

CLASSIFICATION: CONSISTENCY / FALSIFICATION-class. E_c = E_yield = sqrt(alpha)*E_crit
is CODATA-derived through alpha, m_e; delta_Cu ~ 2.4e-5 is an EXTERNAL empirical
input (tagged by value only). No emergence headline. Every number is imported from
ave.core.constants (no hardcoding); verify_constants() COMPUTES the cross-checks.
"""

from __future__ import annotations

import math

import numpy as np

from ave.core.constants import (
    ALPHA,
    C_0,
    E_CRIT,
    E_SLEW,
    E_YIELD,
    EPSILON_0,
    HBAR,
    L_NODE,
    MU_0,
    OMEGA_C,
    PROTON_ELECTRON_RATIO,
    V_SNAP,
    V_YIELD,
    Z_0,
    e_charge,
)

# --------------------------------------------------------------------------- #
# EXTERNAL empirical input (tagged; pure-AVE-corpus: value only, no attribution).
# The measured X-ray refractive DECREMENT of copper near the Cu-Kalpha line
# (~8 keV): delta = 1 - n ~ 2.4e-5, known to ~1%. Used ONLY as a comparison
# target; the AVE contribution below is OUR OWN independent compute.
DELTA_CU_MEASURED = 2.4e-5
DELTA_CU_KNOWN_FRAC = 0.01  # ~1% accuracy => uncertainty band ~2.4e-7

# EXTERNAL CODATA input (tagged): the muon/electron mass ratio, used only to set
# the muonic-H reduced-mass Bohr scale a_mu. NOT an AVE constant; the proton/
# electron ratio in the same reduced-mass formula IS canonical (imported above).
MUON_ELECTRON_RATIO = 206.7682830  # CODATA 2018 m_mu/m_e (EXTERNAL, tagged)

# Copper crystal geometry (FCC): lattice constant and atoms/cell. Structural
# facts of the Cu lattice (not AVE constants), tagged as such.
CU_Z = 29
CU_A_LATTICE = 3.615e-10  # m, FCC conventional cell edge
CU_ATOMS_PER_CELL = 4


# =========================================================================== #
# section 0 — canonical-source cross-check (verify_constants; before any output)
# =========================================================================== #
def verify_constants() -> dict:
    """Cross-check the canonical scales this driver rides on, COMPUTED not asserted.

    Every relation is recomputed from ave.core.constants through an independent
    path; a break in any input flips the corresponding check False.
    """
    k_coulomb = e_charge / (4.0 * math.pi * EPSILON_0)  # V.m
    checks = {
        # V_yield = sqrt(alpha) * V_snap (the alpha-echo ratio)
        "V_yield_is_sqrt_alpha_V_snap": bool(np.isclose(V_YIELD, math.sqrt(ALPHA) * V_SNAP)),
        # E_yield = V_yield / ell_node (the field image of the yield voltage)
        "E_yield_is_V_yield_over_ell": bool(np.isclose(E_YIELD, V_YIELD / L_NODE)),
        # E_yield = sqrt(alpha) * E_crit (kernel field scale = sqrt(alpha) x Schwinger)
        "E_yield_is_sqrt_alpha_E_crit": bool(np.isclose(E_YIELD, math.sqrt(ALPHA) * E_CRIT, rtol=1e-9)),
        # hbar * omega_C = m_e c^2 = e * V_snap (the temporal cutoff = pair gap)
        "hbar_omegaC_is_e_Vsnap": bool(np.isclose(HBAR * OMEGA_C, e_charge * V_SNAP)),
        # Z0 = sqrt(L_cell/C_cell) with L_cell=mu0*ell, C_cell=eps0*ell
        "Z0_is_sqrt_mu0_over_eps0": bool(np.isclose(Z_0, math.sqrt(MU_0 / EPSILON_0))),
        # omega_C = c/ell_node
        "omegaC_is_c_over_ell": bool(np.isclose(OMEGA_C, C_0 / L_NODE)),
        # E_slew = alpha * m_e c^2 => E_slew/e = alpha * V_snap, and A_f=sqrt(alpha)
        "Eslew_over_e_is_alpha_Vsnap": bool(np.isclose(E_SLEW / e_charge, ALPHA * V_SNAP)),
    }
    return {
        "k_coulomb_Vm": k_coulomb,
        "V_SNAP": float(V_SNAP),
        "V_YIELD": float(V_YIELD),
        "E_YIELD": float(E_YIELD),
        "E_CRIT": float(E_CRIT),
        "L_NODE": float(L_NODE),
        "Z_0": float(Z_0),
        "OMEGA_C": float(OMEGA_C),
        "checks": checks,
        "all_pass": all(checks.values()),
    }


# =========================================================================== #
# section 1 — the lossless L-C link + DIAC-gated varactor (circuit mapping)
# =========================================================================== #
def cell_reactances() -> dict:
    """The per-cell lumped LC of the lossless link (series-L bond / shunt-C node).

    L_cell = mu0 * ell_node, C_cell = eps0 * ell_node; Z0 = sqrt(L/C),
    omega_C = 1/sqrt(LC) = c/ell_node. Round-trip identities are machine-exact.
    """
    L_cell = MU_0 * L_NODE
    C_cell = EPSILON_0 * L_NODE
    return {
        "L_cell_H": L_cell,
        "C_cell_F": C_cell,
        "Z0_ohm": math.sqrt(L_cell / C_cell),
        "omegaC_rad_s": 1.0 / math.sqrt(L_cell * C_cell),
    }


def kernel_S(A: np.ndarray | float) -> np.ndarray:
    """Ax-4 elliptic kernel S(A) = sqrt(1 - A^2); NaN where A^2 > 1 (interior)."""
    A = np.asarray(A, dtype=float)
    inside = A**2 <= 1.0
    out = np.full_like(A, np.nan)
    out[inside] = np.sqrt(1.0 - A[inside] ** 2)
    return out if out.ndim else float(out)


def eps_eff_over_eps0(E: np.ndarray | float, E_f: float) -> np.ndarray:
    """DIAC-gated T2 permittivity: eps_eff/eps0.

    Piecewise (the P4 constitutive law):
        eps_eff/eps0 = 1                    for |E| <  E_f   (dead zone, transparent)
        eps_eff/eps0 = sqrt(1-(E/E_c)^2)    for |E| >= E_f   (loads)
    E_f = A_f * E_YIELD sets the forward threshold. E_f = 0 recovers the round-3
    continuous law (no dead zone). E_c = E_YIELD.
    """
    E = np.asarray(E, dtype=float)
    A = np.abs(E) / E_YIELD
    loaded = kernel_S(A)
    below = np.abs(E) < E_f
    out = np.where(below, 1.0, loaded)
    return out if out.ndim else float(out)


# =========================================================================== #
# section 2 — DERIVE V_f: is it FORCED or FREE? (the make-or-break)
# =========================================================================== #
def dispersion_has_gap() -> dict:
    """C1 — is the K4/srs LC-ladder dispersion gapped?

    The canonical cold dispersion is the monatomic sine law
        omega(q) = (2 c0 / ell_node) |sin(q ell_node / 2)|
    (graded-network-response.md:56). ACOUSTIC: omega(q->0) -> 0. A gap would need
    omega(q=0) > 0. We sample near q=0 and check the limit.
    """
    q = np.array([1e-6, 1e-5, 1e-4]) / L_NODE
    omega = (2.0 * C_0 / L_NODE) * np.abs(np.sin(q * L_NODE / 2.0))
    omega_at_zero = float(omega[0])
    omega_max = 2.0 * C_0 / L_NODE  # band edge at q=pi/ell
    return {
        "omega_near_zero_rad_s": omega_at_zero,
        "omega_band_edge_rad_s": omega_max,
        "is_gapped": bool(omega_at_zero > 1e-6 * omega_max),  # acoustic => False
        "gap_voltage_V": 0.0,  # no gap => no phonon-seeded V_f
    }


def vf_candidates() -> dict:
    """Evaluate C2..C6 forward-threshold candidates and their A_f = V_f/V_yield.

    Returns each candidate's V_f, A_f, and whether it is a genuine DEAD-ZONE ONSET
    (kernel flat below it) vs a HIGH-field ceiling / rupture scale.
    """
    k = e_charge / (4.0 * math.pi * EPSILON_0)
    r_ns_Z1 = math.sqrt(k / E_YIELD)  # Z=1 no-solution radius
    r_cut_A0 = 9.0 * L_NODE  # the A0 ~9 ell_node protective cutoff radius
    E_at_rcut = k / r_cut_A0**2  # Coulomb field there (Z=1)
    Vf_A0 = E_at_rcut * L_NODE

    cands = {
        # C2 slew-energy image: V_f = alpha*V_snap = sqrt(alpha)*V_yield
        "C2_slew": {
            "Vf_V": ALPHA * V_SNAP,
            "A_f": (ALPHA * V_SNAP) / V_YIELD,
            "onset_type": "kinetic/slew scale (not a dead-zone onset of the kernel)",
        },
        # C3 D-turnover reference field E_c/2
        "C3_turnover_ref": {
            "Vf_V": V_YIELD / 2.0,
            "A_f": 0.5,
            "onset_type": "HIGH-field ceiling (real-branch max of E_C); NOT a low-V floor",
        },
        # C4 D-turnover actual field E_c/sqrt2
        "C4_turnover_actual": {
            "Vf_V": V_YIELD / math.sqrt(2.0),
            "A_f": 1.0 / math.sqrt(2.0),
            "onset_type": "HIGH-field ceiling (actual field at turnover); NOT a low-V floor",
        },
        # C5 pair-production gap V_snap (first REAL excitation)
        "C5_pair_gap": {
            "Vf_V": V_SNAP,
            "A_f": V_SNAP / V_YIELD,
            "onset_type": "real-carrier gap (contradicts round-3 continuous loading)",
        },
        # C6 A0 protective-cutoff image (imaged to a bond voltage)
        "C6_A0_cutoff_image": {
            "Vf_V": Vf_A0,
            "A_f": Vf_A0 / V_YIELD,
            "onset_type": "image of a HIGH-field CEILING (suppress r<r_cut); wrong sign for a floor",
        },
    }
    cands["_scales"] = {
        "r_ns_Z1_fm": r_ns_Z1 * 1e15,
        "r_cut_A0_pm": r_cut_A0 * 1e12,
        "A_f_slew_is_sqrt_alpha": bool(np.isclose(cands["C2_slew"]["A_f"], math.sqrt(ALPHA))),
    }
    return cands


# =========================================================================== #
# section 3a — X-ray-through-copper decrement (OUR compute)
# =========================================================================== #
def _wigner_seitz_radius() -> float:
    """WS-cell-equivalent sphere radius for one Cu atom (FCC)."""
    v_atom = CU_A_LATTICE**3 / CU_ATOMS_PER_CELL
    return (3.0 * v_atom / (4.0 * math.pi)) ** (1.0 / 3.0)


def _mean_A2_shell(r_min: float, r_max: float, Z: int) -> float:
    """Volume-average of A^2(r) = (Z k / (E_yield r^2))^2 over the WS cell,
    integrated only over the shell [r_min, r_max] (the region that loads).

    <A^2> = (1/V_cell) * integral_{r_min}^{r_max} A^2(r) 4 pi r^2 dr
          = (1/V_cell) * 4 pi (Z k / E_yield)^2 (1/r_min - 1/r_max).
    V_cell is the full WS cell (loading outside the shell contributes 0).
    """
    k = e_charge / (4.0 * math.pi * EPSILON_0)
    v_atom = CU_A_LATTICE**3 / CU_ATOMS_PER_CELL
    pref = (Z * k / E_YIELD) ** 2
    return (1.0 / v_atom) * 4.0 * math.pi * pref * (1.0 / r_min - 1.0 / r_max)


def copper_decrement(A_f: float = 0.0) -> dict:
    """AVE static-loading contribution to the Cu X-ray refractive decrement.

    Three variants of the inner boundary (like the muonic doc's C-iii / L-i):
      - continuum, interior-excluded at the turnover r_turn(Cu) (A_actual=1/sqrt2)
      - reduced-Compton (ell_node) inner cutoff
      - WITH the forward-voltage dead zone at A_f (loads only where A(r) >= A_f,
        i.e. r <= r_f = sqrt(Z k / (A_f E_yield)); combined with the turnover floor)

    delta_index = 1 - n_perp = 1 - (1-A^2)^{1/4} ~ (1/4)<A^2>;
    eps-deficit 1 - S ~ (1/2)<A^2>. Compare to DELTA_CU_MEASURED.
    Bare-Z is the direction-conservative UPPER bound (screening lowers it).
    """
    k = e_charge / (4.0 * math.pi * EPSILON_0)
    Z = CU_Z
    R_ws = _wigner_seitz_radius()
    # radius where actual field A_actual = 1/sqrt2 (the real-branch turnover):
    # reference E_C = E_c/2 -> r_turn = sqrt(2 Z k / E_c)
    r_turn = math.sqrt(2.0 * Z * k / E_YIELD)
    # radius where |E| = E_YIELD (A=1): r_yield
    r_yield = math.sqrt(Z * k / E_YIELD)

    def decr(mean_A2):
        d_index = 0.25 * mean_A2
        d_eps = 0.5 * mean_A2
        return d_index, d_eps

    # variant (i): continuum, interior-excluded at turnover
    A2_turn = _mean_A2_shell(r_turn, R_ws, Z)
    # variant (ii): reduced-Compton inner cutoff at ell_node (note: for Cu, ell_node
    # is INSIDE the interior r_yield, so this over-counts the saturated core; report
    # it capped at the turnover as the honest inner boundary, and flag the raw value)
    r_inner_ln = max(L_NODE, r_turn)  # honest: cannot integrate below the real branch
    A2_ln = _mean_A2_shell(r_inner_ln, R_ws, Z)
    # variant (iii): with dead zone A_f. loads where A(r) >= A_f AND on real branch.
    # r_f (outer edge of loading) = sqrt(Z k/(A_f E_yield)); inner edge = r_turn.
    if A_f > 0.0:
        r_f = math.sqrt(Z * k / (A_f * E_YIELD))
        if r_f <= r_turn:
            A2_thresh = 0.0  # dead zone swallows the whole real-branch loading region
        else:
            A2_thresh = _mean_A2_shell(r_turn, min(r_f, R_ws), Z)
    else:
        A2_thresh = A2_turn  # A_f=0 => round-3 (no dead zone), same as variant (i)

    di_turn, de_turn = decr(A2_turn)
    di_ln, de_ln = decr(A2_ln)
    di_th, de_th = decr(A2_thresh)
    return {
        "R_ws_pm": R_ws * 1e12,
        "r_turn_Cu_pm": r_turn * 1e12,
        "r_yield_Cu_pm": r_yield * 1e12,
        "ell_node_inside_interior": bool(L_NODE < r_yield),
        "mean_A2_interior_excl": A2_turn,
        "mean_A2_lnode_cut": A2_ln,
        "mean_A2_with_threshold": A2_thresh,
        "delta_index_interior_excl": di_turn,
        "delta_eps_interior_excl": de_turn,
        "delta_index_lnode_cut": di_ln,
        "delta_index_with_threshold": di_th,
        "delta_eps_with_threshold": de_th,
        "delta_Cu_measured": DELTA_CU_MEASURED,
        "delta_Cu_1pct_band": DELTA_CU_MEASURED * DELTA_CU_KNOWN_FRAC,
        # CONSISTENT iff AVE decrement hides under the ~1% known accuracy of delta_Cu
        "verdict_index": (
            "CONSISTENT" if di_turn < DELTA_CU_MEASURED * DELTA_CU_KNOWN_FRAC else "CONSTRAINT"
        ),
        "ratio_index_to_delta_Cu": di_turn / DELTA_CU_MEASURED,
    }


# =========================================================================== #
# section 3b — muonic-hydrogen loading WITH the threshold
# =========================================================================== #
def muonic_loading_with_threshold(A_f: float) -> dict:
    """Does the forward-voltage dead zone drop the muonic loading below the window?

    The muonic-H overshoot (A0 [C-EXCLUDED]) is dominated by the SUB-PITCH band
    [r_turn, ell_node] (103% of the C-iii shift; A0 round-3 band-split). A dead
    zone at A_f removes the region A(r) < A_f, i.e. r > r_f = r_ns/sqrt(A_f)
    (reference A = (r_ns/r)^2). The real branch exists only for r >= r_turn =
    r_ns*sqrt(2) (A_ref <= 1/2). So the dead zone acts on the FAR tail; it can only
    empty the real-branch loading if A_f >= 1/2 (r_f <= r_turn) -- the D-TURNOVER,
    a HIGH-field ceiling used upside-down. We compute the surviving loading measure
    integral ½ A_ref(r)^2 rho_2s(r) 4 pi r^2 dr over [r_turn, r_f] vs [r_turn, inf).
    """
    k = e_charge / (4.0 * math.pi * EPSILON_0)
    Z = 1
    r_ns = math.sqrt(Z * k / E_YIELD)
    r_turn = r_ns * math.sqrt(2.0)
    # muonic 2S radial scale a_mu (reduced-mass Bohr). Reduced mass (in m_e units)
    # uses the CANONICAL proton/electron ratio; only the muon/electron ratio is an
    # EXTERNAL CODATA input (tagged). a_mu = a_0/mu_red = L_NODE/(alpha*mu_red),
    # since a_0 = L_NODE/alpha and L_NODE = hbar/(M_E c) — no hardcoded M_E.
    m_mu_over_m_e = MUON_ELECTRON_RATIO  # EXTERNAL CODATA input (tagged module-level)
    mu_red = m_mu_over_m_e / (1.0 + m_mu_over_m_e / PROTON_ELECTRON_RATIO)  # in m_e units
    a_mu = L_NODE / (ALPHA * mu_red)  # reproduces the muonic doc: 185.84 m_e / 284.75 fm

    # dead-zone outer edge r_f where A_ref(r_f) = A_f
    if A_f <= 0.0:
        r_f = np.inf
    else:
        r_f = r_ns / math.sqrt(A_f)

    # loading measure integrand: ½ A_ref^2 * rho_2s * 4 pi r^2, A_ref = (r_ns/r)^2
    # rho_2s ~ (1 - r/(2 a))^2 exp(-r/a) (2S hydrogenic, unnormalized shape)
    def integrand(r):
        A2 = (r_ns / r) ** 4  # A_ref^2 = (r_ns/r)^4
        rho = (1.0 - r / (2.0 * a_mu)) ** 2 * np.exp(-r / a_mu)
        return 0.5 * A2 * rho * 4.0 * math.pi * r**2

    rr = np.linspace(r_turn, 60.0 * a_mu, 400000)
    dr = rr[1] - rr[0]
    total = float(np.trapezoid(integrand(rr), dx=dr))
    if np.isinf(r_f) or r_f >= rr[-1]:
        surviving = total
    elif r_f <= r_turn:
        surviving = 0.0
    else:
        mask = rr <= r_f
        surviving = float(np.trapezoid(integrand(rr[mask]), dx=dr))
    frac = surviving / total if total > 0 else 0.0

    # cross-check anchor: A0 L-i lattice-cutoff shift (external result import)
    A0_Li_ueV = 4.92e4  # research/2026-07-05_problem3-muonic-lamb_RESULT.md:80 (L-i)
    window_ueV = 2.3
    # the dead zone scales the L-i-class shift by the surviving fraction (proxy)
    proxy_shift_ueV = A0_Li_ueV * frac
    return {
        "r_ns_fm": r_ns * 1e15,
        "r_turn_fm": r_turn * 1e15,
        "a_mu_fm": a_mu * 1e15,
        "r_f_fm": (r_f * 1e15) if np.isfinite(r_f) else float("inf"),
        "surviving_loading_fraction": frac,
        "A_f_needed_to_empty_real_branch": 0.5,
        "proxy_shift_ueV": proxy_shift_ueV,
        "window_ueV": window_ueV,
        "A0_Li_anchor_ueV": A0_Li_ueV,
        "verdict": "RESCUED" if proxy_shift_ueV < window_ueV else "C-STANDS",
    }


# =========================================================================== #
# section 3c — Delbruck / gamma-attenuation dispersion fence
# =========================================================================== #
def delbruck_fence() -> dict:
    """Above hbar*omega_C = m_e c^2 = 511 keV the reactive line is fenced.

    The sine-law dispersion omega(q) = (2c/ell)|sin(q ell/2)| has a hard band edge
    omega_max = 2 omega_C at q = pi/ell. Modes above omega_max do not propagate on
    the reactive line. hbar*omega_C = 511 keV (= e V_snap = pair-production gap);
    hbar*omega_max = 1.022 MeV. Delbruck scattering and gamma pair-attenuation live
    ABOVE this (MeV, the real-carrier / pair sector), not on the reactive line.
    """
    E_omegaC_keV = HBAR * OMEGA_C / e_charge / 1e3
    E_bandedge_MeV = HBAR * (2.0 * OMEGA_C) / e_charge / 1e6
    return {
        "E_response_scale_keV": E_omegaC_keV,  # 511 keV
        "E_band_edge_MeV": E_bandedge_MeV,  # 1.022 MeV
        "fenced": True,
        "statement": (
            "YES — the reactive line has a hard band edge at hbar*omega_max = "
            "2 hbar*omega_C = 1.022 MeV; Delbruck/gamma-attenuation (>=~1 MeV) are "
            "above the response scale, in the real-carrier (pair-production, V_snap) "
            "sector, not on the reactive T2 line. Dispersion fences them out."
        ),
    }


# =========================================================================== #
# section 4 — house-WHITE equivalent-circuit + constitutive-law figure
# =========================================================================== #
def make_circuit_figure(out_path: str) -> list:
    """Two-panel house-WHITE datasheet figure.

    (left) equivalent-circuit schematic: one lossless LC cell (series-L bond,
    shunt-C node) with the shunt C a DIAC-gated varactor.
    (right) the piecewise constitutive law eps_eff(|E|)/eps0 for several A_f,
    with A_f=0 (round-3 continuous) overlaid as the no-dead-zone limit.
    """
    import matplotlib.patches as mpatches
    import matplotlib.pyplot as plt

    from ave.viz import style

    style.apply("print")
    fig, (axL, axR) = plt.subplots(1, 2, figsize=style.figsize("wide"))

    # ----- left: schematic -----
    axL.set_xlim(0, 10)
    axL.set_ylim(0, 6)
    axL.axis("off")
    ave = style.COLORS["ave"]
    comp = style.COLORS["comparison"]
    muted = style.COLORS["muted"]

    # top rail with a series inductor (bond L)
    axL.plot([0.5, 3.0], [5.0, 5.0], color=muted, lw=1.5)
    # inductor coil (series-L bond)
    xs = np.linspace(3.0, 5.0, 200)
    axL.plot(xs, 5.0 + 0.25 * np.abs(np.sin(6 * np.pi * (xs - 3.0) / 2.0)), color=ave, lw=1.8)
    axL.text(4.0, 5.5, r"$L_{\rm cell}=\mu_0\ell_{\rm node}$", color=ave, ha="center", fontsize=9)
    axL.plot([5.0, 9.5], [5.0, 5.0], color=muted, lw=1.5)
    # shunt branch down to ground at x=7
    axL.plot([7.0, 7.0], [5.0, 3.6], color=muted, lw=1.5)
    # DIAC symbol (two opposed triangles) — the polarity-symmetric gate
    axL.add_patch(mpatches.Polygon([[6.7, 3.6], [7.3, 3.6], [7.0, 3.15]], closed=True,
                                   facecolor="none", edgecolor=comp, lw=1.6))
    axL.add_patch(mpatches.Polygon([[6.7, 2.7], [7.3, 2.7], [7.0, 3.15]], closed=True,
                                   facecolor="none", edgecolor=comp, lw=1.6))
    axL.plot([6.6, 7.4], [3.6, 3.6], color=comp, lw=1.6)
    axL.plot([6.6, 7.4], [2.7, 2.7], color=comp, lw=1.6)
    axL.text(8.7, 3.15, r"DIAC $\pm V_f$", color=comp, ha="center", fontsize=9)
    axL.plot([7.0, 7.0], [2.7, 2.2], color=muted, lw=1.5)
    # varactor (capacitor with an arrow) — the T2 shunt varactor
    axL.plot([6.6, 7.4], [2.2, 2.2], color=ave, lw=1.8)
    axL.plot([6.6, 7.4], [1.9, 1.9], color=ave, lw=1.8)
    axL.annotate("", xy=(7.5, 2.35), xytext=(6.5, 1.75),
                 arrowprops=dict(arrowstyle="->", color=ave, lw=1.2))
    axL.text(8.9, 2.05, r"$C(V)=C_0 S(A_V)$", color=ave, ha="center", fontsize=9)
    axL.plot([7.0, 7.0], [1.9, 1.4], color=muted, lw=1.5)
    # ground
    for i, w in enumerate([0.5, 0.32, 0.14]):
        axL.plot([7.0 - w, 7.0 + w], [1.4 - 0.12 * i, 1.4 - 0.12 * i], color=muted, lw=1.5)
    axL.text(1.7, 5.35, r"$Z_0=376.7\,\Omega$", color=muted, ha="center", fontsize=9)
    axL.text(5.0, 0.5, "lossless LC link + DIAC-gated T2 varactor (one cell)",
             color="black", ha="center", fontsize=9)

    # ----- right: constitutive law -----
    E = np.linspace(0.0, 1.0, 600) * E_YIELD  # up to E_c = E_YIELD
    x = E / E_YIELD
    for A_f, ls, lab in [(0.0, "-", r"$A_f=0$ (round-3, no dead zone)"),
                         (0.2, "--", r"$A_f=0.2$"),
                         (0.5, ":", r"$A_f=0.5$ (turnover)")]:
        y = eps_eff_over_eps0(E, A_f * E_YIELD)
        col = ave if A_f == 0.0 else (comp if A_f == 0.5 else style.COLORS["accent"])
        axR.plot(x, y, color=col, ls=ls, lw=1.8, label=lab)
    axR.axvline(0.5, color=muted, ls=":", lw=1.0)
    axR.axvline(1.0 / math.sqrt(2.0), color=muted, ls=":", lw=1.0)
    axR.set_xlim(0, 1.0)
    axR.set_ylim(0, 1.05)
    axR.set_xlabel(r"$|E|/E_c$   ($E_c=E_{\rm yield}$)")
    axR.set_ylabel(r"$\varepsilon_{\rm eff}/\varepsilon_0 = S$")
    axR.legend(loc="lower left", frameon=False, fontsize=8)

    return style.save(fig, out_path, strict=True)


# =========================================================================== #
# section 5 — main
# =========================================================================== #
def run() -> dict:
    vc = verify_constants()
    cell = cell_reactances()
    disp = dispersion_has_gap()
    cands = vf_candidates()
    cu = copper_decrement(A_f=0.0)  # A_f=0 => round-3 limit (no dead zone)
    cu_thr = copper_decrement(A_f=0.2)  # with a modest dead zone
    # muonic: sweep A_f to find whether ANY value rescues while preserving loading
    mu_small = muonic_loading_with_threshold(A_f=0.05)
    mu_turn = muonic_loading_with_threshold(A_f=0.5)
    fence = delbruck_fence()
    return {
        "verify_constants": vc,
        "cell": cell,
        "dispersion": disp,
        "vf_candidates": cands,
        "copper_no_threshold": cu,
        "copper_with_threshold_Af0p2": cu_thr,
        "muonic_Af0p05": mu_small,
        "muonic_Af0p5_turnover": mu_turn,
        "delbruck_fence": fence,
    }


def main() -> None:  # pragma: no cover
    import json
    import os

    res = run()
    print("=" * 96)
    print("  P4 — FORWARD-VOLTAGE CONDUCTION THRESHOLD (DIAC-gated T2 varactor)")
    print("=" * 96)
    vc = res["verify_constants"]
    print(f"  constants cross-check all_pass={vc['all_pass']}  checks={vc['checks']}")
    print(f"  cell: L={res['cell']['L_cell_H']:.3e} H  C={res['cell']['C_cell_F']:.3e} F  "
          f"Z0={res['cell']['Z0_ohm']:.2f} ohm  omega_C={res['cell']['omegaC_rad_s']:.3e} rad/s")
    d = res["dispersion"]
    print(f"  C1 dispersion gapped? {d['is_gapped']}  (omega~0={d['omega_near_zero_rad_s']:.3e}, "
          f"band-edge={d['omega_band_edge_rad_s']:.3e})  => phonon-seeded V_f = {d['gap_voltage_V']} V")
    print("  V_f candidates (A_f = V_f/V_yield):")
    for key, cand in res["vf_candidates"].items():
        if key.startswith("_"):
            continue
        print(f"    {key:22s} V_f={cand['Vf_V']:.4e} V  A_f={cand['A_f']:.4f}  [{cand['onset_type']}]")
    print(f"    scales: {res['vf_candidates']['_scales']}")
    cu = res["copper_no_threshold"]
    print(f"  COPPER (no dead zone / round-3): <A^2>={cu['mean_A2_interior_excl']:.3e}  "
          f"delta_index={cu['delta_index_interior_excl']:.3e}  delta_eps={cu['delta_eps_interior_excl']:.3e}")
    print(f"    vs delta_Cu={cu['delta_Cu_measured']:.2e} (1% band={cu['delta_Cu_1pct_band']:.2e})  "
          f"ratio={cu['ratio_index_to_delta_Cu']:.3e}  VERDICT={cu['verdict_index']}")
    mu5 = res["muonic_Af0p05"]
    mu50 = res["muonic_Af0p5_turnover"]
    print(f"  MUONIC A_f=0.05: surviving frac={mu5['surviving_loading_fraction']:.4f}  "
          f"proxy={mu5['proxy_shift_ueV']:.3e} ueV  VERDICT={mu5['verdict']}")
    print(f"  MUONIC A_f=0.50 (turnover): surviving frac={mu50['surviving_loading_fraction']:.4f}  "
          f"proxy={mu50['proxy_shift_ueV']:.3e} ueV  VERDICT={mu50['verdict']}")
    print(f"  DELBRUCK FENCE: {res['delbruck_fence']['statement']}")

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "p4_forward_voltage_threshold.json"), "w") as fh:
        json.dump(res, fh, indent=2, default=str)

    fig_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..", "..", "..", "manuscript", "vol_9_vacuum_datasheet", "figures", "forward_voltage",
    )
    fig_dir = os.path.abspath(fig_dir)
    os.makedirs(fig_dir, exist_ok=True)
    written = make_circuit_figure(os.path.join(fig_dir, "p4_diac_varactor_circuit.pdf"))
    print(f"  figure written: {[str(p) for p in written]}")


if __name__ == "__main__":  # pragma: no cover
    main()
