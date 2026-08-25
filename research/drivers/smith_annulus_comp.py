"""smith-annulus computation lane — T1 numerics.

All quantities in the Gamma-plane (phase-space). Lattice-natural units:
Z0 = 1, ell_node = 1, c = 1, so theta = beta*ell = omega.

Receipts for load-bearing forms (see FROZEN-expectations.md):
  end reflection -1/3      : scatter_matrix S_ij = 2/n - delta_ij (chiral_lattice.py:81)
  far arms = Z0 resistive  : x38-s11 derivation:15,46 -- NOTE this is the
                             ISOLATED-JUNCTION reading (x38 derivation:23,
                             "Same junction, two terminations"); the in-lattice
                             embedding is computed in the `embedding` block
                             below (Bethe-tree closure of the same model class)
  kernel S(A)=sqrt(1-A^2)  : ave-kb/CLAUDE.md:73
  Z = Z0*sqrt(S)           : resonant-lc-solitons.md:41
  alpha (imported value)   : CODATA calibration import
  outer-edge leak |G|^2=1-alpha : cvr-reflection-smith.md:38 (Class-B echo tag :80)
  nu_vac = 2/7             : gravity/__init__.py:45 (Op19)
Mark profile: rho(t) = (R + r cos 3t)/(R + r), R=2, r=1
  (the-electron-plumber repo, animations/smith_sim.py:59-68).

Repair pass 2026-08-24 (post-adversarial-verify): band edges by bisection not
grid-sampling; unitarity checked across the full sweep; T3 symmetric-bias field
COMPUTED not declared (uniform grading -> -1/3 at all orders; symmetric END
bias under FORM J moves the floor at O(eps^2)); Bethe-tree embedding appendix;
outer-edge alpha-leak numbers.
"""
from __future__ import annotations

import json

import numpy as np

Z0 = 1.0
ALPHA = 7.2973525693e-3          # imported CODATA value (calibration, not derived)
NU_VAC = 2.0 / 7.0               # Op19 trace-reversed Poisson ratio
KB_T_CMB_EV = 8.617333262e-5 * 2.725   # k_B * T_CMB in eV
ME_C2_EV = 510998.95             # m_e c^2 in eV (imported)

OUT = {}

# ---------------------------------------------------------------- helpers

def scatter_matrix(n: int) -> np.ndarray:
    """Copy of AVE-Core chiral_lattice.py:81-102 shunt-junction scatter."""
    return (2.0 / n) * np.ones((n, n)) - np.eye(n)


def S_kernel(A):
    return np.sqrt(np.clip(1.0 - np.asarray(A) ** 2, 0.0, None))


def gamma_from_z(z, z0=Z0):
    return (z - z0) / (z + z0)


def z_in_line(zl, theta, z0=Z0):
    """Input impedance of lossless line length theta terminated in zl."""
    t = np.tan(theta)
    return z0 * (zl + 1j * z0 * t) / (z0 + 1j * zl * t)


# ------------------------------------------------- T1(a) composite Gamma(omega)

# check the -1/3 counting fact against the engine's scatter matrix
S3 = scatter_matrix(3)
assert abs(S3[0, 0] - (-1.0 / 3.0)) < 1e-15
gamma_end_cold = gamma_from_z(Z0 / 2.0)
assert abs(gamma_end_cold - (-1.0 / 3.0)) < 1e-15
OUT["end_reflection_check"] = {
    "scatter_matrix_S11": S3[0, 0],
    "impedance_route": float(np.real(gamma_end_cold)),
}

theta = np.linspace(1e-6, np.pi, 20001)
# seen from one exterior semi-infinite line at junction 1 (shunt node):
#   other ports = one semi-infinite Z0 line  ||  bond(theta) loaded by Z0/2
z_bond_in = z_in_line(Z0 / 2.0, theta)
z_par = 1.0 / (1.0 / Z0 + 1.0 / z_bond_in)
g_comp = gamma_from_z(z_par)
ag = np.abs(g_comp)
i_min = int(np.argmin(ag))
below = ag < (1.0 / 3.0 - 1e-12)


def abs_gamma_comp(th):
    zi = z_in_line(Z0 / 2.0, th)
    zp = 1.0 / (1.0 / Z0 + 1.0 / zi)
    return abs(gamma_from_z(zp))


def bisect(f, a, b, tol=1e-14, itmax=200):
    fa, fb = f(a), f(b)
    assert fa * fb < 0, "bracket does not straddle a root"
    for _ in range(itmax):
        m = 0.5 * (a + b)
        fm = f(m)
        if fm == 0.0 or (b - a) < tol:
            return m
        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b)


# band edges of the below-1/3 band by ROOT-FINDING on |Gamma(theta)| = 1/3
# (grid samples only bracket; the grid values carry no digits past ~1e-4)
f_edge = lambda th: abs_gamma_comp(th) - 1.0 / 3.0
band = (bisect(f_edge, 0.5, 1.2), bisect(f_edge, 2.0, 2.6))
band_frac = (band[1] - band[0]) / np.pi

# unitarity check at a few frequencies: build full 4-external-port S-matrix
# ports: 1,2 = free lines at J1; 3,4 = free lines at J2; bond internal.
def composite_S(th):
    """4x4 S-matrix of the two-junction + bond network (shunt nodes)."""
    # Use wave-cascade: junction shunt node => for excitation at port p,
    # solve via admittance at each node with the bond as a two-port line.
    # Line ABCD for lossless Z0 line: [[cos, jZ0 sin],[j sin/Z0, cos]]
    A = np.cos(th); B = 1j * Z0 * np.sin(th)
    C = 1j * np.sin(th) / Z0; D = np.cos(th)
    S = np.zeros((4, 4), dtype=complex)
    for p in range(4):
        # incident unit wave on port p, others matched. Node voltages V1,V2.
        # At J1: ports 1,2 (Y0 each) + bond. At J2: ports 3,4 + bond.
        # Incident wave a on a matched line at node: source current 2a*Y0.
        Y0 = 1.0 / Z0
        # bond two-port admittance matrix from ABCD:
        # [I1; I2] = Ybond [V1; V2],  Ybond = [[D/B, -(AD-BC)/B], [-1/B, A/B]]
        Yb = np.array([[D / B, -(A * D - B * C) / B], [-1.0 / B, A / B]])
        Y = np.array([[2 * Y0, 0], [0, 2 * Y0]], dtype=complex) + Yb
        Isrc = np.zeros(2, dtype=complex)
        node = 0 if p < 2 else 1
        Isrc[node] = 2.0 * Y0  # unit incident wave
        V = np.linalg.solve(Y, Isrc)
        for q in range(4):
            nq = 0 if q < 2 else 1
            b = V[nq] - (1.0 if q == p else 0.0)  # reflected = V - incident
            S[q, p] = b
    return S


# unitarity across the FULL sweep (not spot frequencies): every theta on the
# 20001-point grid used for the band claim
unit_err = []
for th in theta:
    Sm = composite_S(th)
    unit_err.append(float(np.max(np.abs(Sm.conj().T @ Sm - np.eye(4)))))
for th in (0.3, np.pi / 2, 2.5):
    # cross-check S11 against impedance route at spot frequencies
    Sm = composite_S(th)
    zi = z_in_line(Z0 / 2.0, th)
    zp = 1.0 / (1.0 / Z0 + 1.0 / zi)
    assert abs(Sm[0, 0] - gamma_from_z(zp)) < 1e-10

OUT["composite"] = {
    "gamma_dc_limit": float(ag[0]),
    "min_abs_gamma": float(ag[i_min]),
    "theta_at_min": float(theta[i_min]),
    "quarter_wave_value_check": float(np.abs(gamma_from_z(
        1.0 / (1.0 / Z0 + 1.0 / z_in_line(Z0 / 2.0, np.pi / 2))))),
    "below_one_third_band_theta_rootfound": [float(band[0]), float(band[1])],
    "band_edge_sum_minus_pi": float(band[0] + band[1] - np.pi),
    "below_one_third_fraction_of_band": float(band_frac),
    "below_one_third_fraction_gridcheck": float(below.mean()),
    "max_unitarity_error_full_sweep": max(unit_err),
    "unitarity_sweep_points": len(unit_err),
}

# ---------------------------------------- T1(a2) in-lattice embedding appendix
# The Z0/2 termination above is the ISOLATED-JUNCTION reading (x38: far arms
# = matched semi-infinite lines). The in-lattice closure of the SAME model
# class (identical Z0 bonds + z=3 shunt junctions, loop-free Bethe-tree
# approximation of the srs net) replaces the matched arms with the lattice
# itself: the branch impedance z satisfies  z = line(z/2, theta), i.e.
#   j*t*z^2 + z - 2*j*t = 0,  t = tan(theta)   (Z0 = 1 units)
# Physical root: Re(z) >= 0.  End load seen from inside a bond = z/2.

def bethe_gamma_end(th):
    t = np.tan(th)
    if abs(t) < 1e-12:                      # theta -> 0 or pi: line invisible
        # shell recursion halves z each shell -> z -> 0 (short)
        return -1.0
    disc = 1.0 - 8.0 * t * t
    sq = np.sqrt(complex(disc))
    roots = [(-1.0 + sq) / (2j * t), (-1.0 - sq) / (2j * t)]
    # physical root: nonnegative real part (passive network)
    z = max(roots, key=lambda r: r.real)
    if z.real < -1e-12:                     # both reactive (stopband)
        z = roots[0]
    return complex(gamma_from_z(z / 2.0))


th_grid = np.linspace(1e-4, np.pi - 1e-4, 20001)
gb = np.array([abs(bethe_gamma_end(t)) for t in th_grid])
stop_edge = float(np.arctan(1.0 / np.sqrt(8.0)))  # |t|<=1/sqrt(8): reactive
near_third = np.mean(np.abs(gb - 1.0 / 3.0) < 0.05 / 3.0)
# shell-depth recursion at the n=1 comb frequency theta=pi:
#   shell 1 = matched arms (the isolated reading); shell k+1 feeds shell k
shell_g = []
zk = complex(Z0)
for _ in range(6):
    shell_g.append(float(abs(gamma_from_z(zk / 2.0))))
    zk = complex(z_in_line(zk / 2.0, np.pi))
OUT["embedding"] = {
    "model": "Bethe-tree closure, j*t*z^2 + z - 2*j*t = 0, end load z/2",
    "abs_gamma_end_at_quarter_wave": float(abs(bethe_gamma_end(np.pi / 2))),
    "abs_gamma_end_quarter_wave_analytic_3_minus_2sqrt2": float(3 - 2 * np.sqrt(2)),
    "reactive_stopband_theta": [stop_edge, float(np.pi - stop_edge)],
    "fraction_of_band_within_5pct_of_one_third": float(near_third),
    "abs_gamma_end_at_comb_theta_pi_by_shell_depth_1_to_6": shell_g,
    "comb_limit": "shell depth -> inf: |Gamma_end| -> 1 (short) at theta = n*pi",
    "note": ("isolated-junction floor -1/3 is NOT the steady-state in-lattice "
             "end reflection; in-band tree value 0.1716 < 1/3, comb value -> 1"),
}

# ------------------------------------------------- T1(b) eigenmodes (cold)

# poles: 1 - G1*G2*exp(-2j*theta) = 0 with G1=G2=-1/3  => exp(-2j th)=9
# analytic: th_n = n*pi + j*ln(9)/2 ; confirm by Newton on complex theta
def pole_fn(th):
    return 1.0 - (1.0 / 9.0) * np.exp(-2j * th)


poles = []
for n in (1, 2, 3):
    th = complex(n * np.pi, np.log(9.0) / 2.0) + 0.3 + 0.2j  # perturbed seed
    for _ in range(60):
        f = pole_fn(th)
        df = (2j / 9.0) * np.exp(-2j * th)
        th = th - f / df
    poles.append(th)
Qs = [float(p.real / (2 * p.imag)) for p in poles]
OUT["modes_cold"] = {
    "poles_theta": [[float(p.real), float(p.imag)] for p in poles],
    "analytic_check_imag": float(np.log(9.0) / 2.0),
    "Q_n": Qs,
    "Q_over_n_analytic": float(np.pi / np.log(9.0)),
    "SWR_on_bond": (1 + 1 / 3) / (1 - 1 / 3),
}
# mode shape n=1: V(x) ~ e^{-jkx} + G e^{-2jkL} e^{+jkx} evaluated on real axis
x = np.linspace(0, np.pi, 201)  # k_r = 1 (n=1), L = pi
G = -1.0 / 3.0
V = np.exp(-1j * x) + G * np.exp(-2j * np.pi) * np.exp(1j * (x - 2 * np.pi))
OUT["modes_cold"]["mode1_absV_ends_over_mid"] = float(
    np.abs(V[0]) / np.abs(V).max())

# ------------------------------------------------- T1(c) graded Gamma(A)

def gamma_J(A):
    s = np.sqrt(S_kernel(A))
    return (s / 2.0 - 1.0) / (s / 2.0 + 1.0)


def gamma_B(A):
    s = np.sqrt(S_kernel(A))
    return (0.5 - s) / (0.5 + s)


A = np.linspace(0.0, 1.0, 200001)
gJ, gB = np.abs(gamma_J(A)), np.abs(gamma_B(A))
OUT["H1"] = {
    "form_J_endpoints": [float(gJ[0]), float(gJ[-1])],
    "form_B_endpoints": [float(gB[0]), float(gB[-1])],
    "form_J_wall_sign": float(np.sign(np.real(gamma_J(1.0)))),
    "form_B_wall_sign": float(np.sign(np.real(gamma_B(1.0)))),
}
OUT["H2"] = {
    "form_J_monotone": bool(np.all(np.diff(gJ) >= -1e-14)),
    "form_J_range": [float(gJ.min()), float(gJ.max())],
    "form_B_monotone": bool(np.all(np.diff(gB) >= -1e-14)),
    "form_B_min_abs_gamma": float(gB.min()),
    "form_B_zero_crossing_A": float(A[int(np.argmin(gB))]),
    "form_B_zero_crossing_A_analytic": float(np.sqrt(15.0) / 4.0),
}

# H3: shape test against the mark rho(t) = (2 + cos 3t)/3
t = np.linspace(0, 2 * np.pi, 4096, endpoint=False)
rho_mark = (2.0 + np.cos(3 * t)) / 3.0
Ay = 1.0
A_N1 = Ay * (1 + np.cos(3 * t)) / 2.0
A_N2 = Ay * np.sqrt((1 + np.cos(3 * t)) / 2.0)


def h3_metrics(rho_model, name):
    d = rho_model - rho_mark
    # harmonic content of the model profile
    F = np.fft.rfft(rho_model) / len(t)
    mags = np.abs(F)
    fund = mags[3]
    others = np.sqrt(np.sum(mags[1:] ** 2) - fund ** 2)
    return {
        "name": name,
        "endpoints": [float(rho_model.min()), float(rho_model.max())],
        "max_abs_dev_from_mark": float(np.max(np.abs(d))),
        "rms_dev_from_mark": float(np.sqrt(np.mean(d ** 2))),
        "harmonic_distortion_other_over_cos3t": float(others / fund),
        "mean_level": float(rho_model.mean()),
    }


# NOTE: N1/N2 put A=Ay at cos3t=+1 -> |Gamma|=1 there; mark also has rho=1 at
# cos3t=+1. Good alignment. At cos3t=-1, A=0 -> 1/3; mark 1/3. Aligned.
h3 = [h3_metrics(np.abs(gamma_J(A_N1)), "N1 A=(1+cos3t)/2"),
      h3_metrics(np.abs(gamma_J(A_N2)), "N2 A^2=(1+cos3t)/2")]

# inverse: A_req(t) that reproduces the mark exactly under form J
s_req = 2.0 * (1.0 - rho_mark) / (1.0 + rho_mark)   # s = sqrt(S)
A_req = np.sqrt(np.clip(1.0 - s_req ** 4, 0.0, 1.0))
# is A_req close to either natural law?
h3_inv = {
    "A_req_range": [float(A_req.min()), float(A_req.max())],
    "max_dev_A_req_vs_N1": float(np.max(np.abs(A_req - A_N1))),
    "max_dev_A_req_vs_N2": float(np.max(np.abs(A_req - A_N2))),
    "corr_A_req_N1": float(np.corrcoef(A_req, A_N1)[0, 1]),
    "corr_A_req_N2": float(np.corrcoef(A_req, A_N2)[0, 1]),
}
OUT["H3"] = {"models": h3, "inverse": h3_inv,
             "endpoint_pin": {"rho_min": 1 / 3, "implies_R_over_r": 2.0}}

# graded Q(A)
for Aop, tag in ((np.sqrt(ALPHA), "electron_A1_op_point_sqrt_alpha"),
                 (0.5, "A_half"), (0.99, "A_0p99")):
    g = float(np.abs(gamma_J(Aop)))
    OUT.setdefault("graded_Q", {})[tag] = {
        "abs_gamma": g, "Q_over_n": float(np.pi / (2 * np.log(1 / g)))}

# ------------------------------------------------- T2 width numbers

d_op = float(np.abs(gamma_J(np.sqrt(ALPHA)))) - 1.0 / 3.0
A_th = np.sqrt(KB_T_CMB_EV / ME_C2_EV)
d_th = float(np.abs(gamma_J(A_th))) - 1.0 / 3.0
eps_lab = 1.4e-9  # ~Earth-surface 2GM/(c^2 r) scale, order-of-magnitude tag
d_br = float(np.abs(gamma_J(eps_lab))) - 1.0 / 3.0
OUT["T2_widths"] = {
    "closed_form_small_A": "abs_gamma ~ 1/3 + A^2/9",
    "onset_swing_electron_op_point": {"A": float(np.sqrt(ALPHA)),
                                      "delta_abs_gamma": d_op,
                                      "alpha_over_9": ALPHA / 9.0},
    "radiative_cold": {"delta_omega_over_omega_n1": float(np.log(9.0) / np.pi)},
    "backreaction_second_order": {"eps11_assumed": eps_lab,
                                  "delta_abs_gamma": d_br,
                                  "eps_sq_over_9": eps_lab ** 2 / 9.0},
    "thermal_T_CMB": {"A_th": float(A_th), "delta_abs_gamma": d_th,
                      "A_th_sq_over_9": float(A_th ** 2 / 9.0)},
}

# ------------------------------------------------- T3 lock detuning first-pass

# first order: delay-only. delta_omega/omega = -nu_vac * eps11 (Op19 extension)

# (a) UNIFORM grading -- the corpus's "immune to symmetric transformation"
# case (translation-circuit.md:189): EVERY arm, reference bond included,
# grades to Z0*sqrt(S).  The scale factor cancels in Gamma = (2-z)/z, so the
# floor is invariant at ALL orders.  COMPUTED, not declared:
uniform_dev = []
for A_u in (0.1, 0.5, 0.9, 0.999):
    s = np.sqrt(S_kernel(A_u))          # sqrt(S): same Z/Z0 factor as gamma_J
    z_graded = s * Z0
    load = 0.5 * s * Z0                 # two graded arms in parallel
    g_u = (load - z_graded) / (load + z_graded)
    uniform_dev.append(abs(g_u - (-1.0 / 3.0)))
floor_invariant_uniform = bool(max(uniform_dev) < 1e-15)

# (b) SYMMETRIC END bias under the FORM-J side-assignment (bond held cold,
# both junction sides graded equally, eps1 = eps2 = eps).  This is an implicit
# bond-vs-junction DIFFERENTIAL, so the floor DOES move, at O(eps^2):
eps_s = 1e-3
g_s = float(np.abs(gamma_J(eps_s)))
sym_product = g_s * g_s
sym_pred = (1.0 / 9.0) * (1 + 2.0 * eps_s ** 2 / 3.0)
sym_moves_floor = bool(abs(sym_product - 1.0 / 9.0) > 1e-12)

# (c) differential end bias: ends at A1=eps1, A2=eps2 ->
#   G_i ~ -(1/3 + eps_i^2/9);  |G1 G2| = 1/9 (1 + (eps1^2+eps2^2)/3) + O(eps^4)
eps1, eps2 = 1e-3, 0.0  # illustrative strong differential bias
g1 = float(np.abs(gamma_J(eps1))); g2 = float(np.abs(gamma_J(eps2)))
OUT["T3_lock"] = {
    "first_order_delay_detuning_per_eps11": -NU_VAC,
    "impedance_detuning_order": "second (dZ/Z = -eps^2/4)",
    "floor_invariant_under_UNIFORM_grading_all_orders": floor_invariant_uniform,
    "uniform_grading_max_dev_from_minus_third": float(max(uniform_dev)),
    "uniform_grading_A_tested": [0.1, 0.5, 0.9, 0.999],
    "symmetric_END_bias_form_J": {
        "eps": eps_s, "product": sym_product,
        "predicted_(1/9)(1+2eps^2/3)": sym_pred,
        "moves_floor": sym_moves_floor,
        "note": ("symmetric end bias with a cold bond is an implicit "
                 "bond-vs-junction differential under FORM J -- the O(eps^2) "
                 "shift presupposes the STUCK-POINT-2 side-assignment"),
    },
    "differential_example": {
        "eps": [eps1, eps2], "g1_g2_product": g1 * g2,
        "cold_product": 1.0 / 9.0,
        "predicted_product": (1.0 / 9.0) * (1 + (eps1**2 + eps2**2) / 3.0),
        "Q_over_n_biased": float(np.pi / (-np.log(g1 * g2))),
        "Q_over_n_cold": float(np.pi / np.log(9.0)),
    },
}

# ------------------------------------------------- outer-edge alpha leak
# canonical wall reflectivity |Gamma|^2 = 1 - alpha (cvr-reflection-smith.md:38;
# Class-B value-level echo per :80).  Offset of the outer annulus edge and the
# finite ceiling it puts on the wall-closed Q:
outer_edge_gap = 1.0 - np.sqrt(1.0 - ALPHA)
OUT["outer_edge_alpha_leak"] = {
    "abs_gamma_wall": float(np.sqrt(1.0 - ALPHA)),
    "outer_edge_offset_1_minus_sqrt_1_minus_alpha": float(outer_edge_gap),
    "approx_alpha_over_2": ALPHA / 2.0,
    "ratio_to_inner_edge_offset_alpha_over_9": float(outer_edge_gap / (ALPHA / 9.0)),
    "Q_ceiling_per_n_pi_over_neg_ln_1_minus_alpha": float(
        np.pi / (-np.log(1.0 - ALPHA))),
}

with open(__file__.replace("smith_annulus_comp.py", "smith_annulus_results.json"), "w") as f:
    json.dump(OUT, f, indent=2)
print(json.dumps(OUT, indent=2))
