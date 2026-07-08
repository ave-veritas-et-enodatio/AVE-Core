"""P5 — RADIATIVE FAR-FIELD KEYING: is one radiative-scoping postulate the key for BOTH EM sectors?

Contention P5 of the paper-hardening epic (Grant: "test it"). Prereg (frozen
BEFORE this driver, git-ordering = freeze proof):
  research/2026-07-08_p5-radiative-far-field-keying_prereg_FROZEN.md

THE HYPOTHESIS UNDER TEST (Grant-blessed ontology — TESTED, not assumed): the
single key for BOTH EM sectors is the field's RADIATIVE / far-field character.
A held static E (charge-sourced, near-zone) LOADS; a held static B (monopole-
free, near-zone) is TRANSPARENT; a RADIATION field (far-zone) is ACTIVE. If
true, ONE radiative-scoping statement replaces the two sector-keying postulates.

OPERATIONAL CONTENT: if radiative far-field character is the key, the loading of
a config must TRACK a FIELD-INTRINSIC far-field diagnostic F (net radiated power).
If a NEAR-ZONE config loads (F small) or a FAR-ZONE config is transparent, the
far-field diagnostic does NOT explain the loading -> two postulates remain.

METHOD (substrate-native): drive the two canonical Axiom-4 keying functionals
  eps-grade (capacitive):  S_eps = sqrt(1 - A_V^2),  A_V = |E|/E_yield         (potential coord)
  mu-grade  (inductive) :  S_mu  = sqrt(1 - A_I^2),  A_I = |curl H|*l_node^2 / I_max  (circulation coord)
directly (NOT the fdtd engine, which carries the live VCA-R01 |B|-keying defect,
pvlas-static-b-verdict.md:55) on four field configs. A_V, A_I are computed by the
SAME operators for every config; no channel is told which config it sees.

FIREWALL: the verdict-path functions (VERDICT_PATH_FNS below) reference NO
ALPHA/M_E/m_e token (AST self-scan asserts it). Field construction uses
E_YIELD/I_MAX/L_NODE as dimensional normalizations only. SCALE-INVARIANCE:
the {load,transparent} pattern is re-checked with E_yield,I_max rescaled +-10x.

Constants imported from ave.core.constants (no hardcoding).
"""

from __future__ import annotations

import ast
import json
import os

import numpy as np

import ave.core.constants as C

# --- canonical constants (imported) -----------------------------------------
C_0 = C.C_0
MU_0 = C.MU_0
EPS_0 = C.EPSILON_0
E_YIELD = C.E_YIELD                 # ~1.13e17 V/m ; V_YIELD/L_NODE
L_NODE = C.L_NODE                   # ~3.86e-13 m
I_MAX = C.XI_TOPO * C.C_0           # = e*c/l_node ~ 124.4 A  (relativistic-inductor.md:18)
EPS_CLIP = C.EPS_CLIP               # kernel sqrt-domain clip

# ===========================================================================
# SHARED OPERATORS (identical for every config; no config label enters)
# ===========================================================================


def kernel_deficit(A):
    """Axiom-4 loading deficit 1 - S(A), S = sqrt(1 - A^2). A may be array."""
    A2 = np.clip(np.asarray(A, dtype=float) ** 2, 0.0, 1.0 - EPS_CLIP)
    return 1.0 - np.sqrt(1.0 - A2)


def curl_H(Hx, Hy, Hz, h):
    """Finite-difference curl of a sampled 3D H field (interior, central diff).
    Returns the three interior curl components [A/m^2]. The null MUST emerge
    here for a source-free static field (curl H -> 0), not be hard-coded."""
    dHz_dy = (Hz[1:-1, 2:, 1:-1] - Hz[1:-1, :-2, 1:-1]) / (2 * h)
    dHy_dz = (Hy[1:-1, 1:-1, 2:] - Hy[1:-1, 1:-1, :-2]) / (2 * h)
    dHx_dz = (Hx[1:-1, 1:-1, 2:] - Hx[1:-1, 1:-1, :-2]) / (2 * h)
    dHz_dx = (Hz[2:, 1:-1, 1:-1] - Hz[:-2, 1:-1, 1:-1]) / (2 * h)
    dHy_dx = (Hy[2:, 1:-1, 1:-1] - Hy[:-2, 1:-1, 1:-1]) / (2 * h)
    dHx_dy = (Hx[1:-1, 2:, 1:-1] - Hx[1:-1, :-2, 1:-1]) / (2 * h)
    cx = dHz_dy - dHy_dz
    cy = dHx_dz - dHz_dx
    cz = dHy_dx - dHx_dy
    return cx, cy, cz


def curl_mag(Hx, Hy, Hz, h):
    cx, cy, cz = curl_H(Hx, Hy, Hz, h)
    return np.sqrt(cx * cx + cy * cy + cz * cz)


def A_I_from_curl(curl_magnitude, i_max):
    """Node-scale circulation coordinate: A_I = |curl H| * l_node^2 / I_max
    (the grid-invariant node-perimeter form; the per-cell factor is OPEN but
    OFF the verdict path — moot for the static null, scale-guarded for active)."""
    return curl_magnitude * (L_NODE ** 2) / i_max


def A_V_from_E(Emag, e_yield):
    return Emag / e_yield


def poynting_z_and_u(Ex, Hy):
    """For the z-propagating configs: S_z = Ex*Hy, u = 1/2 eps0 Ex^2 + 1/2 mu0 Hy^2."""
    S_z = Ex * Hy
    u = 0.5 * EPS_0 * Ex ** 2 + 0.5 * MU_0 * Hy ** 2
    return S_z, u


# ===========================================================================
# FIELD BUILDERS (analytic; sampled on a lattice; sources radius-masked)
# ===========================================================================

N3 = 25          # 3D grid for the static configs
NZ = 400         # z-samples for the wave configs
NT = 240         # temporal samples over one full cycle


def build_static_E(e_yield):
    """Config 1: point charge at center; Coulomb E ~ 1/r^2, H = 0. Sampled in a
    shell (source core masked). Amplitude set so A_V ~ 0.3 at the shell."""
    L = 12.0 * L_NODE
    ax = np.linspace(-L, L, N3)
    h = ax[1] - ax[0]
    X, Y, Z = np.meshgrid(ax, ax, ax, indexing="ij")
    r = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)
    core = 4.0 * L_NODE                      # exclude the singular core
    mask = r > core
    # choose q so |E| at r=core is ~0.3 E_yield
    Emag_at_core = 0.30 * e_yield
    kq = Emag_at_core * core ** 2            # k_e q  = |E| r^2
    rr = np.where(mask, r, np.nan)
    Emag = kq / rr ** 2
    Ex = np.where(mask, Emag * X / rr, 0.0)
    Ey = np.where(mask, Emag * Y / rr, 0.0)
    Ez = np.where(mask, Emag * Z / rr, 0.0)
    Hx = np.zeros_like(Ex)
    Hy = np.zeros_like(Ex)
    Hz = np.zeros_like(Ex)
    Emag_full = np.sqrt(Ex ** 2 + Ey ** 2 + Ez ** 2)
    return dict(Ex=Ex, Ey=Ey, Ez=Ez, Hx=Hx, Hy=Hy, Hz=Hz, Emag=Emag_full,
                Bmag=np.zeros_like(Ex), mask=mask, h=h, kind="static_E")


def build_static_B(e_yield):
    """Config 2: uniform static B (solenoid-interior / the PVLAS transverse-B
    geometry) = a real, monopole-free current source, near-zone, E = 0. |B| set
    STRONG (cB ~ 0.3 E_yield) to demonstrate the field-strength-INDEPENDENT null.
    curl H = 0 EMERGES (source-free static: no enclosed current/displacement in the
    vacuum interior). The dipole (non-uniform source-free static B) is checked
    separately (null_emergence_refinement) to show the null is NOT a uniform-field
    trivial-difference artifact but the general source-free-static-B property."""
    L = 12.0 * L_NODE
    ax = np.linspace(-L, L, N3)
    h = ax[1] - ax[0]
    X = ax  # only for shape
    shape = (N3, N3, N3)
    Bmag = 0.30 * e_yield / C_0              # a very strong static B (cB ~ 0.3 E_yield)
    Bz = np.full(shape, Bmag)               # uniform along zhat
    Bx = np.zeros(shape)
    By = np.zeros(shape)
    Hx, Hy, Hz = Bx / MU_0, By / MU_0, Bz / MU_0
    Ex = np.zeros(shape)
    mask = np.ones(shape, dtype=bool)       # whole interior is vacuum (no source inside)
    Bmag_full = np.sqrt(Bx ** 2 + By ** 2 + Bz ** 2)
    return dict(Ex=Ex, Ey=np.zeros(shape), Ez=np.zeros(shape),
                Hx=Hx, Hy=Hy, Hz=Hz, Emag=np.zeros(shape),
                Bmag=Bmag_full, mask=mask, h=h, kind="static_B")


def build_static_B_dipole(e_yield):
    """Non-uniform source-free static B (magnetic dipole m*zhat) — used ONLY by
    the refinement check to show curl H -> 0 with grid refinement (converging to
    the analytic zero), i.e. the null generalizes beyond the uniform field."""
    L = 12.0 * L_NODE
    ax = np.linspace(-L, L, N3)
    h = ax[1] - ax[0]
    X, Y, Z = np.meshgrid(ax, ax, ax, indexing="ij")
    r = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)
    core = 6.0 * L_NODE                      # sample farther out (smoother field)
    mask = r > core
    rr = np.where(mask, r, np.nan)
    Bmag_at_core = 0.30 * e_yield / C_0
    m = Bmag_at_core * core ** 3 / (MU_0 / (4 * np.pi))
    pref = MU_0 / (4 * np.pi) * m
    rhz = Z / rr
    Bx = np.where(mask, pref * (3 * rhz * (X / rr)) / rr ** 3, 0.0)
    By = np.where(mask, pref * (3 * rhz * (Y / rr)) / rr ** 3, 0.0)
    Bz = np.where(mask, pref * (3 * rhz * (Z / rr) - 1.0) / rr ** 3, 0.0)
    Hx, Hy, Hz = Bx / MU_0, By / MU_0, Bz / MU_0
    Bmag_full = np.sqrt(Bx ** 2 + By ** 2 + Bz ** 2)
    return dict(Ex=np.zeros_like(Bx), Ey=np.zeros_like(Bx), Ez=np.zeros_like(Bx),
                Hx=Hx, Hy=Hy, Hz=Hz, Emag=np.zeros_like(Bx),
                Bmag=Bmag_full, mask=mask, h=h, kind="static_B_dipole")


def _wave_axes(e_yield, ai_target=0.30):
    """Common wave geometry: choose k so the traveling-wave A_I lands ~ai_target
    (structural band; the VERDICT is invariant to this choice — any k>0 loads,
    k=0 is transparent — verified by the scale/loading gates)."""
    E0 = 0.30 * e_yield                       # A_V amplitude ~ 0.3
    # traveling wave: |curl H| = (E0/(mu0 c)) k ; A_I = |curl H| l_node^2 / I_max
    #   -> k = ai_target * I_max / (E0/(mu0 c) * l_node^2)
    k = ai_target * I_MAX / ((E0 / (MU_0 * C_0)) * L_NODE ** 2)
    lam = 2 * np.pi / k
    L = 1.0 * lam                             # one wavelength of interior
    z = np.linspace(0.0, L, NZ)
    hz = z[1] - z[0]
    t = np.linspace(0.0, 2 * np.pi / (k * C_0), NT, endpoint=False)  # one period
    return E0, k, z, hz, t


def build_traveling(e_yield):
    """Config 3: plane wave Ex=E0 cos(kz-wt), By=(E0/c)cos(kz-wt). Net Poynting>0."""
    E0, k, z, hz, t = _wave_axes(e_yield)
    w = k * C_0
    ZZ, TT = np.meshgrid(z, t, indexing="ij")     # (NZ, NT)
    phase = k * ZZ - w * TT
    Ex = E0 * np.cos(phase)
    By = (E0 / C_0) * np.cos(phase)
    Hy = By / MU_0
    return dict(Ex=Ex, Hy=Hy, By=By, z=z, hz=hz, k=k, kind="traveling")


def build_standing(e_yield):
    """Config 4 (CONTROL): standing wave Ex=2E0 cos(kz)cos(wt), By=(2E0/c) sin(kz)sin(wt).
    NET Poynting time-averaged = 0, but local |E|, curl H nonzero -> CAN load."""
    E0, k, z, hz, t = _wave_axes(e_yield)
    w = k * C_0
    ZZ, TT = np.meshgrid(z, t, indexing="ij")
    Ex = 2 * E0 * np.cos(k * ZZ) * np.cos(w * TT)
    By = (2 * E0 / C_0) * np.sin(k * ZZ) * np.sin(w * TT)
    Hy = By / MU_0
    return dict(Ex=Ex, Hy=Hy, By=By, z=z, hz=hz, k=k, kind="standing")


# ===========================================================================
# PER-CONFIG DIAGNOSTICS
# ===========================================================================


def analyze_static(fld, e_yield, i_max):
    m = fld["mask"][1:-1, 1:-1, 1:-1]
    Emag = fld["Emag"][1:-1, 1:-1, 1:-1][m]
    cmag = curl_mag(fld["Hx"], fld["Hy"], fld["Hz"], fld["h"])[m]
    A_V = A_V_from_E(Emag, e_yield)
    A_I = A_I_from_curl(cmag, i_max)
    rms_A_V = float(np.sqrt(np.mean(A_V ** 2)))
    rms_A_I = float(np.sqrt(np.mean(A_I ** 2)))
    defic_eps = float(np.mean(kernel_deficit(A_V)))
    defic_mu = float(np.mean(kernel_deficit(A_I)))
    # far-field: static -> net Poynting identically 0 (E or H is zero)
    F = 0.0
    Bmag = fld["Bmag"][1:-1, 1:-1, 1:-1][m]
    uE = 0.5 * EPS_0 * np.mean(Emag ** 2)
    uB = 0.5 * np.mean(Bmag ** 2) / MU_0
    beta = float((uE - uB) / (uE + uB + 1e-300))
    return dict(kind=fld["kind"], rms_A_V=rms_A_V, rms_A_I=rms_A_I,
                deficit_eps=defic_eps, deficit_mu=defic_mu,
                F_radiated=float(F), beta_EB=beta, kr="0 (static, deep near-zone)")


def analyze_wave(fld, e_yield, i_max):
    Ex, Hy, By, hz = fld["Ex"], fld["Hy"], fld["By"], fld["hz"]
    Emag = np.abs(Ex)
    # curl H for a z-propagating H_y(z,t): (curl H)_x = -dHy/dz
    dHy_dz = np.zeros_like(Hy)
    dHy_dz[1:-1, :] = (Hy[2:, :] - Hy[:-2, :]) / (2 * hz)
    cmag = np.abs(dHy_dz)[1:-1, :]
    Emag_i = Emag[1:-1, :]
    A_V = A_V_from_E(Emag_i, e_yield)
    A_I = A_I_from_curl(cmag, i_max)
    rms_A_V = float(np.sqrt(np.mean(A_V ** 2)))
    rms_A_I = float(np.sqrt(np.mean(A_I ** 2)))
    defic_eps = float(np.mean(kernel_deficit(A_V)))
    defic_mu = float(np.mean(kernel_deficit(A_I)))
    # far-field diagnostic F = |<S>_net| / (<u> c) ; <> over interior z and full cycle
    S_z, u = poynting_z_and_u(Ex[1:-1, :], Hy[1:-1, :])
    S_net = np.mean(S_z)                       # time+space average (net flux)
    u_mean = np.mean(u)
    F = float(abs(S_net) / (u_mean * C_0 + 1e-300))
    uE = 0.5 * EPS_0 * np.mean(Ex ** 2)
    uB = 0.5 * np.mean(By ** 2) / MU_0
    beta = float((uE - uB) / (uE + uB + 1e-300))
    return dict(kind=fld["kind"], rms_A_V=rms_A_V, rms_A_I=rms_A_I,
                deficit_eps=defic_eps, deficit_mu=defic_mu,
                F_radiated=F, beta_EB=beta, kr="plane wave (intrinsically radiative)")


# ===========================================================================
# VERDICT PATH (FIREWALLED — no ALPHA/M_E/m_e token below this line's fns)
# ===========================================================================

TAU_A = 1e-4          # committed loading threshold on the RMS keying coordinate
F_FAR = 0.5           # committed far-field threshold on net radiated power


def classify_loading(diag):
    """LOADS iff either sector's RMS keying coordinate exceeds TAU_A."""
    eps_loads = diag["rms_A_V"] > TAU_A
    mu_loads = diag["rms_A_I"] > TAU_A
    overall = "load" if (eps_loads or mu_loads) else "transparent"
    return dict(eps_loads=bool(eps_loads), mu_loads=bool(mu_loads), overall=overall)


def classify_farfield(diag):
    return "far" if diag["F_radiated"] > F_FAR else "near"


def verdict(diags, loads, fars):
    """Route CONFIRMED / REFUTED / MIXED per the frozen prereg (§5).

    tracking violation = loads-but-near, OR transparent-but-far.
    """
    violations = []
    for name in diags:
        L = loads[name]["overall"]
        R = fars[name]
        if L == "load" and R == "near":
            violations.append(f"{name}: LOADS but near-field (F<{F_FAR})")
        if L == "transparent" and R == "far":
            violations.append(f"{name}: transparent but far-field (F>{F_FAR})")
    # ontology per-config check (config-intrinsic labels, not fed to channels)
    ont_ok = (
        loads["static_E"]["overall"] == "load"
        and loads["static_B"]["overall"] == "transparent"
        and loads["traveling"]["overall"] == "load"
    )
    if not violations and ont_ok:
        route = "RADIATIVE-KEY-CONFIRMED"
    elif violations:
        # distinguish full refute vs mixed: if the three ontology configs still
        # behave as predicted but violations exist, it is the "near-zone loader"
        # partial (still a refutation of the SINGLE far-field key).
        route = "RADIATIVE-KEY-REFUTED"
    else:
        route = "RADIATIVE-KEY-MIXED"
    return dict(route=route, tracking_violations=violations, ontology_configs_ok=bool(ont_ok))


VERDICT_PATH_FNS = ["classify_loading", "classify_farfield", "verdict"]


# ===========================================================================
# GUARDS: firewall AST scan, scale-invariance, anti-tautology
# ===========================================================================


def firewall_ast_scan(this_file, fn_names):
    """Assert NO ALPHA/M_E/m_e Name token appears in the verdict-path functions."""
    with open(this_file) as f:
        tree = ast.parse(f.read())
    forbidden = {"ALPHA", "M_E", "m_e"}
    hits = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in fn_names:
            names = {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}
            bad = names & forbidden
            attrs = {a.attr for a in ast.walk(node) if isinstance(a, ast.Attribute)}
            bad |= attrs & forbidden
            if bad:
                hits[node.name] = sorted(bad)
    return dict(clean=(len(hits) == 0), hits=hits, scanned=fn_names)


def run_all(e_yield, i_max):
    diags = {
        "static_E": analyze_static(build_static_E(e_yield), e_yield, i_max),
        "static_B": analyze_static(build_static_B(e_yield), e_yield, i_max),
        "traveling": analyze_wave(build_traveling(e_yield), e_yield, i_max),
        "standing": analyze_wave(build_standing(e_yield), e_yield, i_max),
    }
    loads = {k: classify_loading(v) for k, v in diags.items()}
    fars = {k: classify_farfield(v) for k, v in diags.items()}
    return diags, loads, fars


def scale_invariance_check():
    """Rescale E_yield and I_max by 0.1x and 10x; the {load,transparent} pattern
    and the routed verdict must be UNCHANGED (alpha-echo magnitude off the verdict)."""
    base_diags, base_loads, base_fars = run_all(E_YIELD, I_MAX)
    base_pattern = {k: base_loads[k]["overall"] for k in base_loads}
    base_route = verdict(base_diags, base_loads, base_fars)["route"]
    results = {}
    stable = True
    for factor in (0.1, 10.0):
        d, ld, fr = run_all(E_YIELD * factor, I_MAX * factor)
        pat = {k: ld[k]["overall"] for k in ld}
        route = verdict(d, ld, fr)["route"]
        same = (pat == base_pattern) and (route == base_route)
        stable = stable and same
        results[f"factor_{factor}"] = dict(pattern=pat, route=route, matches_base=bool(same))
    return dict(scale_invariant=bool(stable), base_pattern=base_pattern,
                base_route=base_route, rescaled=results)


def anti_tautology_check(diags, loads):
    """(a) static-B mu-null EMERGES (rms_A_I << active); (b) control CAN load."""
    active_A_I = max(diags["traveling"]["rms_A_I"], diags["standing"]["rms_A_I"])
    null_A_I = diags["static_B"]["rms_A_I"]
    gap_decades = float(np.log10((active_A_I + 1e-300) / (null_A_I + 1e-300)))
    control_can_load = loads["standing"]["overall"] == "load"
    return dict(
        static_B_mu_null_emerges=bool(null_A_I < TAU_A),
        static_B_rms_A_I=float(null_A_I),
        active_rms_A_I=float(active_A_I),
        null_vs_active_gap_decades=gap_decades,
        control_standing_can_load=bool(control_can_load),
        informative_null=bool(control_can_load and null_A_I < TAU_A),
    )


def _dipole_H(px, py, pz, e_yield):
    """Analytic magnetic-dipole H (m*zhat) at a point (vectorized over arrays)."""
    r = np.sqrt(px ** 2 + py ** 2 + pz ** 2)
    Bmag_ref = 0.30 * e_yield / C_0
    core = 6.0 * L_NODE
    m = Bmag_ref * core ** 3 / (MU_0 / (4 * np.pi))
    pref = MU_0 / (4 * np.pi) * m
    rhz = pz / r
    Bx = pref * (3 * rhz * (px / r)) / r ** 3
    By = pref * (3 * rhz * (py / r)) / r ** 3
    Bz = pref * (3 * rhz * (pz / r) - 1.0) / r ** 3
    return Bx / MU_0, By / MU_0, Bz / MU_0


def null_emergence_refinement(e_yield, i_max):
    """Non-uniform source-free static B (dipole): FD curl-H residual -> 0 as the
    STENCIL h shrinks (O(h^2) central-difference truncation), at FIXED smooth
    sample points. Confirms the mu-null is the GENERAL source-free-static-B
    property (converges to the analytic zero), emergent from the curl operator,
    not a uniform-field trivial-difference artifact and not imposed."""
    # fixed smooth sample points (a shell at r ~ 9 l_node, away from core + edge)
    rng = np.random.default_rng(0)
    n_pts = 200
    theta = rng.uniform(0.2, np.pi - 0.2, n_pts)
    phi = rng.uniform(0, 2 * np.pi, n_pts)
    r0 = 9.0 * L_NODE
    px = r0 * np.sin(theta) * np.cos(phi)
    py = r0 * np.sin(theta) * np.sin(phi)
    pz = r0 * np.cos(theta)
    out = {}
    for h in (r0 / 4, r0 / 8, r0 / 16, r0 / 32, r0 / 64):
        # central-difference curl at each point with stencil h
        def H(dx, dy, dz):
            return _dipole_H(px + dx, py + dy, pz + dz, e_yield)
        Hxyp = H(0, h, 0); Hxym = H(0, -h, 0)
        Hxzp = H(0, 0, h); Hxzm = H(0, 0, -h)
        Hxxp = H(h, 0, 0); Hxxm = H(-h, 0, 0)
        cx = (Hxyp[2] - Hxym[2]) / (2 * h) - (Hxzp[1] - Hxzm[1]) / (2 * h)
        cy = (Hxzp[0] - Hxzm[0]) / (2 * h) - (Hxxp[2] - Hxxm[2]) / (2 * h)
        cz = (Hxxp[1] - Hxxm[1]) / (2 * h) - (Hxyp[0] - Hxym[0]) / (2 * h)
        cmag = np.sqrt(cx ** 2 + cy ** 2 + cz ** 2)
        A_I = A_I_from_curl(cmag, i_max)
        out[f"h_over_{int(round(r0 / h))}_rms_A_I"] = float(np.sqrt(np.mean(A_I ** 2)))
    vals = list(out.values())
    out["monotone_decreasing"] = bool(all(vals[i] > vals[i + 1] for i in range(len(vals) - 1)))
    out["converges_toward_zero"] = bool(vals[-1] < vals[0] and vals[-1] < TAU_A)
    out["order_ratio_first_pair"] = float(vals[0] / (vals[1] + 1e-300))  # ~4 for O(h^2)
    return out


def s_b_near_zone_limit(e_yield, i_max):
    """S_B deliverable (b): near-zone suppression of A_I for an OSCILLATING magnetic
    dipole, computed via the Faraday chain (NOT an imposed power law):

        A_dipole ~ (mu0/4pi) m sin(theta)/r^2            (vector potential)
        E_phi = -dA/dt = omega (mu0/4pi) m sin(theta)/r^2   (induced near-zone E)
        |curl H| = eps0 dE/dt = omega^2 eps0 (mu0/4pi) m sin/r^2 = k^2 (m sin/4pi)/r^2
        A_I = |curl H| l_node^2 / I_max                  (circulation coordinate)

    So A_I(kr) ~ k^2 = (kr)^2/r^2 at fixed r -> the (kr)^2 near-zone law EMERGES
    from two time-derivatives (Faraday + displacement current). |m| is anchored so
    A_I = 0.30 at the near-zone edge kr=0.1 (a tagged readable anchor; the absolute
    magnitude rides I_max/alpha-echo, the SCALING is the physics). PVLAS/BMV sit at
    kr -> 0 (Hz/ms modulation, optical timescale) -> A_I -> 0 -> S_mu -> 1 ->
    delta_n_mu -> 0 : static/near-zone-B transparency COMPUTED, not asserted."""
    r = 50.0 * L_NODE
    theta = np.pi / 2                                    # equatorial (max)
    sin_t = np.sin(theta)
    kr_vals = np.array([1e-3, 3e-3, 1e-2, 3e-2, 1e-1])
    k_vals = kr_vals / r
    # anchor dipole moment m so A_I(kr=0.1)=0.30 (readable band; magnitude rides
    # I_max/alpha-echo, the (kr)^2 SCALING is the physics). Solve the full chain
    # at k_edge for m, then re-run the chain per kr with TWO explicit d/dt (omega)
    # factors so the k^2 EMERGES from Faraday(dA/dt) + displacement(eps0 dE/dt).
    def chain_A_I(k, m):
        """The explicit Faraday + displacement-current chain (two d/dt = two omega)."""
        omega = k * C_0
        A_vec = (MU_0 / (4 * np.pi)) * m * sin_t / r ** 2   # vector potential ~ A_phi
        E_phi = omega * A_vec                                # 1st d/dt: E = -dA/dt (amplitude)
        curl_H = omega * EPS_0 * E_phi                       # 2nd d/dt: curl H = eps0 dE/dt
        return curl_H * (L_NODE ** 2) / i_max
    # anchor dipole moment m so A_I(kr=0.1)=0.30 (exact, via the chain itself)
    k_edge = 0.1 / r
    m = 0.30 / chain_A_I(k_edge, 1.0)
    A_I = np.array([float(chain_A_I(k, m)) for k in k_vals])  # ~ omega^2 = k^2 (two d/dt)
    S_mu = np.sqrt(1.0 - np.clip(A_I ** 2, 0, 1 - EPS_CLIP))
    dn_mu = np.sqrt(S_mu) - 1.0
    slope = float(np.polyfit(np.log(kr_vals), np.log(A_I + 1e-300), 1)[0])
    return dict(kr=kr_vals.tolist(), A_I=A_I.tolist(), S_mu=S_mu.tolist(),
                delta_n_mu=dn_mu.tolist(), loglog_slope_A_I_vs_kr=slope,
                emergent_scaling="A_I ~ (kr)^2 from Faraday(dA/dt) + displacement(eps0 dE/dt) = two d/dt",
                interpretation="kr->0 (PVLAS Hz / BMV ms): A_I->0, S_mu->1, delta_n_mu->0 (transparent)")


# ===========================================================================
# MAIN
# ===========================================================================


def main():
    this_file = os.path.abspath(__file__)
    diags, loads, fars = run_all(E_YIELD, I_MAX)
    v = verdict(diags, loads, fars)
    fw = firewall_ast_scan(this_file, VERDICT_PATH_FNS)
    scale = scale_invariance_check()
    anti = anti_tautology_check(diags, loads)
    refine = null_emergence_refinement(E_YIELD, I_MAX)
    sb = s_b_near_zone_limit(E_YIELD, I_MAX)

    out = dict(
        title="P5 radiative-far-field keying test + S_B",
        prereg="research/2026-07-08_p5-radiative-far-field-keying_prereg_FROZEN.md",
        constants=dict(E_YIELD=E_YIELD, I_MAX=I_MAX, L_NODE=L_NODE, C_0=C_0),
        thresholds=dict(TAU_A=TAU_A, F_FAR=F_FAR),
        per_config=diags,
        loading=loads,
        farfield=fars,
        VERDICT=v,
        firewall=fw,
        scale_invariance=scale,
        anti_tautology=anti,
        null_emergence_refinement=refine,
        S_B_near_zone_limit=sb,
        S_B_equation="S_B = S_mu = sqrt(1 - A_I^2); mu_eff = mu0/sqrt(1-A_I^2); "
                     "A_I = |curl H|*l_node^2 / I_max; I_max = e c / l_node ~ 124.4 A",
    )

    # hard self-gates (fail loud)
    assert fw["clean"], f"FIREWALL BREACH on verdict path: {fw['hits']}"
    assert scale["scale_invariant"], f"SCALE-INVARIANCE FAIL: {scale}"
    assert anti["informative_null"], f"ANTI-TAUTOLOGY FAIL: {anti}"

    outdir = os.path.join(os.path.dirname(this_file), "_output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "p5_radiative_far_field_keying.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))
    return out


if __name__ == "__main__":
    main()
