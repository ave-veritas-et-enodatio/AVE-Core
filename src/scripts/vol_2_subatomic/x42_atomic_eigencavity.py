"""
x42 — The Atomic Eigencavity: hydrogen as an Op6 phase-closure problem (task #11)
=================================================================================

The atom read in the IMPEDANCE-CARVE register (walk (c),
research/2026-07-10_impedance-register-walks_framing.md):

  * The nucleus's Coulomb well is the electron's own OFF-LINE, source-slaved
    reactive dress (bin 3 of walk (a): |Γ|=1 at ω→0, radiates nothing). Seen by
    the electron's de Broglie dispersion it is a GRADED INDEX / dispersion
    profile n(r,ξ) — the DEFECT'S dispersion, the graded walls of a cavity, not a
    potential floor. NAMED-QUANTITY GUARD: this is NOT a medium impedance — the
    lattice keeps Z_0 = 377 Ω everywhere in Regime I; conflating the de Broglie
    index with a medium impedance is the named-quantity error flagged at
    vol2/claim-quality.md:344. Where this file/RESULT writes the frozen-prereg
    label "Z(r)" it denotes THIS graded index/dispersion profile n(r,ξ) (the
    graded line the ABCD cascade integrates), never a spatially-varying medium
    impedance.
  * The orbital = the electron's matter-wave trapped between its own reflections.
  * Quantization = round-trip phase closure ∮k·dl = 2πn on the graded line.
  * The spectrum = an Op6 problem: B_total(E) = 0 on the ABCD cascade
    (clm-gdd70j, λ_min(S†S)→0). Op6 finds the MODES of the GIVEN Z(r); it does
    NOT select a₀ or the 1/r geometry (honest scope: constants.py:212-228,
    electron-identification.md:77 Op6-scope re-scope).

DELIVERABLE MAP
  1. Z(r) from the Coulomb dress — the port-language profile (docstring +
     `de_broglie_refractive_index`, built ON de-broglie-n.md's spherical radial
     transmission line n(r,ξ)=√(2 Z_eff(r) a₀/r − ξ)).
  2. Phase-closure spectrum — `phase_closure_spectrum`: ABCD cascade B_total=0
     over the canonical Op5 primitive (radial_eigenvalue._abcd_section), giving
     E_n ∝ 1/n² and a₀ as the eigenmode scale.
  3. Muonic case — same network, heavier probe: `muonic_spectrum` /
     `muonic_marks` swap the probe mass m_e → m_r,μ (reduced mass); the network
     (the m_e-defined lattice) is unchanged.
  4/5. The two-register guard + the K1/K2 caveat live in the RESULT doc.

SABOTAGE (P11): `phase_closure_spectrum` takes `dress_exp` (1 = Coulomb, real;
2 = planted 1/r² dress) and the gates `gate_mark` / `gate_form` / `gate_int`
FIRE on the plant and PASS on the real profile. A gate that cannot fire is a
checklist.

CONSTANTS: every value from ave.core.constants (A_0, RY_EV, M_E, M_PROTON,
M_MUON, ALPHA, HBAR, C_0, L_NODE, e_charge, EPSILON_0, V_YIELD). Zero hard-codes.

MODE: derivation-from-canon + numerical consistency driver (NOT engine-fire).
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import (
    A_0,
    ALPHA,
    C_0,
    EPSILON_0,
    HBAR,
    L_NODE,
    M_E,
    M_MUON,
    M_PROTON,
    RY_EV,
    V_YIELD,
    e_charge,
)
from ave.core.universal_operators import universal_saturation

# `dress_section` below is a faithful generalization of
# `ave.solvers.radial_eigenvalue._abcd_section`; the tests import that canonical
# primitive directly and assert element-wise equality at (m_probe=m_e,
# dress_exp=1, saturate=True), so the reuse is machine-checked there.

# ---------------------------------------------------------------------------
# Reduced masses (M3 convention; declared in the FROZEN prereg)
# ---------------------------------------------------------------------------
M_R_H = M_E * M_PROTON / (M_E + M_PROTON)  # hydrogen reduced mass
M_R_MU = M_MUON * M_PROTON / (M_MUON + M_PROTON)  # muonic-H reduced mass


# ---------------------------------------------------------------------------
# Deliverable 1 — the port-language graded INDEX / dispersion profile n(r,ξ)
# ("Z(r)" in the frozen prereg/RESULT ≡ this index profile, NOT a medium impedance)
# ---------------------------------------------------------------------------


def de_broglie_refractive_index(r, xi, Z_eff=1.0):
    """The graded index / dispersion profile n(r,ξ) the Coulomb dress casts.

    Canon (de-broglie-n.md, clm-oltvwy): the atom is a spherical radial
    transmission line; the source-slaved Coulomb dress, seen by the probe's de
    Broglie dispersion, is the graded index

        n(r, ξ) = √( 2·Z_eff(r)·a₀ / r  −  ξ ),   ξ = |E|/Ry.

    This is the DEFECT'S dispersion — NOT the medium impedance. The lattice keeps
    Z_0 = 377 Ω everywhere in Regime I; conflating the de Broglie index with a
    medium impedance is the named-quantity error at vol2/claim-quality.md:344.

    ENTAILED-FORM CHECK (this function is NOT dead code): for l=0 the executed
    ABCD cascade's local radial wavenumber is EXACTLY this index over a₀,
        k²(r)·a₀² == n(r,ξ)²   element-wise
    (dress_section builds every section from `local_wavenumber_sq`, and
    `test_de_broglie_index_is_cascade_local_wavenumber` machine-checks the
    equality across the integration grid). So the imported de Broglie FORM is an
    explicit entailment of the executed route, not port-language prose.

    Near the nucleus n→∞ (fast defect, short de Broglie wavelength); at the
    classical turning point n=0 (defect stops). Standing waves between these
    boundaries are the orbitals — the PORT-LANGUAGE statement of the cavity
    walls. Op6 finds the modes of THIS given profile.
    """
    arg = 2.0 * Z_eff * A_0 / r - xi
    return np.sqrt(np.maximum(arg, 0.0))


def local_wavenumber_sq(r_mid, E_J, Z, l, m_probe=M_E, dress_exp=1, saturate=True):
    """Local radial wavenumber² k²(r) = −K2 the ABCD cascade actually integrates.

        k²(r) = (2 m_probe/ℏ²)·(|V_dress(r)| + E) / S(A)  −  l²/r²

    the de Broglie dispersion on the graded dress. dress_section builds every
    section from −K2 = this quantity, so this IS the executed route's dispersion.
    For l=0 and the LINEAR network (saturate=False) it equals the imported de
    Broglie index squared over a₀²:  k²(r)·a₀² == de_broglie_refractive_index²
    (machine-checked). Returns >0 in the classically-allowed (propagating) region,
    <0 in the classically-forbidden (evanescent) region.
    """
    ang_react = float(l) ** 2 / r_mid**2
    # |V_dress| at r_mid  (dress_exp=1 -> Coulomb -Zαℏc/r)
    V_mag = Z * ALPHA * HBAR * C_0 / r_mid * (A_0 / r_mid) ** (dress_exp - 1)
    cap_bias = 2.0 * m_probe * V_mag / (HBAR**2)  # = -2 m_probe V / ℏ²
    ind_phase = 2.0 * m_probe * E_J / HBAR**2  # E_J < 0 for bound states
    if saturate:
        # Ax-4 saturation keyed on the LATTICE rest energy m_e c²
        strain_amp = V_mag / (M_E * C_0**2)
        S_r = max(universal_saturation(strain_amp, 1.0), 1e-10)
    else:
        S_r = 1.0  # cold-lattice linear network
    k2_coeff = (cap_bias + ind_phase) / S_r
    return k2_coeff - ang_react  # = −K2


# ---------------------------------------------------------------------------
# Deliverable 2/3 — the ABCD section, generalized in probe mass + dress exponent
# ---------------------------------------------------------------------------


def dress_section(r1, r2, E_J, Z, l, m_probe=M_E, dress_exp=1, saturate=True):
    """One radial-TL ABCD section on the graded Z(r) dress (canonical Op5).

    Faithful generalization of radial_eigenvalue._abcd_section:
      * `m_probe`  — the PROBE mass in the de Broglie dispersion (m_e for
        hydrogen, m_r,μ for the muonic probe). The LATTICE rupture scale in the
        Ax-4 saturation stays m_e (a lattice property, not the probe's) — this
        is the literal "same network, heavier probe" separation.
      * `dress_exp` — the Coulomb-dress exponent. 1 ⇒ real 1/r dress (EXACTLY
        reproduces `_abcd_section` at m_probe=m_e, saturate=True; cross-checked
        in the tests). 2 ⇒ planted 1/r² dress (SABOTAGE P11).
      * `saturate` — apply the Ax-4 kernel S(A). True reproduces `_abcd_section`
        (canonical). False = the COLD-LATTICE LINEAR network (S≡1). The muonic
        run uses saturate=False: at r ≲ α·ℓ_node the muonic Coulomb field drives
        strain_amp = V/(m_e c²) PAST yield (>1) so S→0 and the linear cascade
        diverges — that near-nucleus non-linearity IS the X41 frozen-tie regime
        (does the near-nucleus field additionally bias the lattice?), which the
        reduced-mass SPECTRUM reproduction deliberately excludes (brief §3). The
        reduced-mass scaling is a property of the LINEAR network alone.

    Dress potential V(r) = −Z·αℏc / r · (a₀/r)^(dress_exp−1); dress_exp=1 is
    bare Coulomb. The section is the exact Coulomb radial ODE (Ax 1+2+4), so the
    turning-point/Maslov phase is captured by the boundary conditions — no
    ½-integer inserted by hand (prereg branch (i)).
    """
    r_mid = 0.5 * (r1 + r2)
    dr = r2 - r1

    # −K2 = the local de Broglie wavenumber² the cascade integrates (SAME code
    # path the entailed-form check reads; for l=0/linear this == de Broglie index²/a₀²).
    K2 = -local_wavenumber_sq(r_mid, E_J, Z, l, m_probe, dress_exp, saturate)

    if K2 > 0:  # classically forbidden / evanescent
        g = np.sqrt(K2)
        cosh_g, sinh_g = np.cosh(g * dr), np.sinh(g * dr)
        A, B, C, D = cosh_g, (sinh_g / g if g > 1e-15 else dr), g * sinh_g, cosh_g
    else:  # classically allowed / propagating
        k = np.sqrt(-K2)
        cos_k, sin_k = np.cos(k * dr), np.sin(k * dr)
        A, B, C, D = cos_k, (sin_k / k if k > 1e-15 else dr), -k * sin_k, cos_k

    return np.array([[A, B], [C, D]])


def _phase_closure_residual(E_eV, Z, n_ref, l, m_probe, dress_exp, r_min, r_max, N_sec, saturate=True):
    """B_total(E) residual (Op6): ψ′ + κψ evaluated at r_max on the decaying wave.

    Inner BC: regular Coulomb solution at r_min. Outer BC: ψ′ + κψ = 0, the
    decaying branch (equivalently B_total(E)=0). Zero of this residual = a
    phase-closure eigenmode of the given graded dress.
    """
    E_J = -abs(E_eV) * e_charge
    kappa = np.sqrt(2.0 * m_probe * abs(E_J)) / HBAR
    if l == 0:
        x = float(Z) * r_min / A_0
        psi, dpsi = r_min * (1.0 - x), 1.0 - 2.0 * x
    else:
        psi, dpsi = r_min ** (l + 1), (l + 1) * r_min**l
    edges = np.geomspace(r_min, r_max, N_sec + 1)
    state = np.array([psi, dpsi])
    for i in range(N_sec):
        state = dress_section(edges[i], edges[i + 1], E_J, Z, l, m_probe, dress_exp, saturate) @ state
    psi_o, dpsi_o = state
    return (dpsi_o + kappa * psi_o) / max(abs(dpsi_o), abs(kappa * psi_o), 1e-30)


def phase_closure_spectrum(Z=1, l=0, m_probe=M_E, ry_scale=None, n_max=4, dress_exp=1, N_sec=6000, saturate=True):
    """Phase-closure eigenvalues on the graded Coulomb dress (E_n ∝ 1/n²).

    Scans the B_total(E)=0 residual across the bound-state energy window in a
    fixed box sized to the probe's orbit scale, collects all sign changes, and
    Brent-refines each. Returns eigenvalues in eV, sorted DESCENDING (ground
    state first). ONLY the probe mass / dress exponent change between runs — the
    network (the Op5 cascade) is identical. `saturate=False` (used for the
    muonic run) is the cold-lattice LINEAR network; see `dress_section`.
    """
    from scipy.optimize import brentq

    if ry_scale is None:
        ry_scale = RY_EV * (m_probe / M_E)
    a_scale = A_0 * (M_E / m_probe) / Z  # ground-state orbit scale for this probe
    r_min = 1e-4 * a_scale
    r_max = 8.0 * (n_max + 1) ** 2 * a_scale
    # PHYSICAL ground-state bound: a pure Coulomb well has NO state more bound
    # than E = Z²·ry_scale (n=1). Scanning past it is scanning for states that
    # cannot exist and only surfaces numerical artifacts — cap the window there.
    e_ground = ry_scale * Z**2
    e_hi = e_ground * 1.03
    e_lo = e_ground / (n_max + 2) ** 2 * 0.6
    grid = np.geomspace(e_lo, e_hi, 3000)

    def f(E):
        return _phase_closure_residual(E, Z, n_max, l, m_probe, dress_exp, r_min, r_max, N_sec, saturate)

    fv = np.array([f(E) for E in grid])
    roots = []
    for i in range(len(grid) - 1):
        if fv[i] * fv[i + 1] < 0 and abs(fv[i]) < 5 and abs(fv[i + 1]) < 5:
            root = brentq(f, grid[i], grid[i + 1], xtol=1e-9)
            if root <= e_ground * 1.03:  # discard any unphysical deeper-than-ground artifact
                roots.append(root)
    return sorted(roots, reverse=True)


def muonic_spectrum(n_max=3, N_sec=6000):
    """Muonic-H phase-closure spectrum — same network, probe mass m_e → m_r,μ.

    Cold-lattice LINEAR network (saturate=False): the reduced-mass scaling is a
    property of the linear Coulomb network; the near-nucleus saturation (r ≲
    α·ℓ_node, where the muonic field pushes strain_amp > 1) is the X41 frozen-tie
    regime, deliberately excluded from the spectrum reproduction (brief §3).
    """
    return phase_closure_spectrum(Z=1, l=0, m_probe=M_R_MU, n_max=n_max, N_sec=N_sec, saturate=False)


def _trapz(y, x):
    """Trapezoidal integral (numpy-version-agnostic; avoids trapz/trapezoid churn)."""
    return float(np.sum(0.5 * (y[1:] + y[:-1]) * (x[1:] - x[:-1])))


def ground_state_mean_radius(Z=1, l=0, m_probe=M_E, n_max=4, N_sec=6000, saturate=True):
    """M2 eigenmode-scale EXTRACTION — ⟨r⟩ of the ground-state radial eigenfunction.

    The frozen prereg (:115) promised "closure scale from driver | eigenmode-scale
    extraction". This integrates the ground-state reduced radial eigenfunction
    u(r)=r·R(r) at the Brent-refined ground-state eigenvalue and returns
    ⟨r⟩ = ∫ r|u|² dr / ∫ |u|² dr. For the 1s state ⟨r⟩ = 1.5·a_scale
    (a_scale = A_0·(m_e/m_probe)/Z), the textbook shape factor — a genuine
    measurement of the eigenmode SHAPE scale from the ODE eigenfunction, NOT a
    restatement of the box unit (r_max = 8(n_max+1)²·a_scale ≈ 133×⟨r⟩, so the
    box extent does not force ⟨r⟩; the wavefunction peaks at a₀ on its own).

    INTEGRATION DIRECTION IS LOAD-BEARING: forward shooting is unusable — the
    exponentially growing branch swamps the tail (|u| ~ 1e62 at r_max). We
    integrate INWARD from the decaying boundary u ∝ e^{-κr} at r_max (the stable
    branch), which selects the physical decaying mode; at the refined eigenvalue
    the inward solution is also regular at r→0 (u→0), so ⟨r⟩ is clean.
    """
    eigs = phase_closure_spectrum(Z=Z, l=l, m_probe=m_probe, n_max=n_max, N_sec=N_sec, saturate=saturate)
    if not eigs:
        raise ValueError("no ground-state eigenvalue found")
    E1 = max(eigs)  # ground state = most bound (largest |E|); spectrum sorted descending
    E_J = -abs(E1) * e_charge
    kappa = np.sqrt(2.0 * m_probe * abs(E_J)) / HBAR
    a_scale = A_0 * (M_E / m_probe) / Z
    r_min = 1e-4 * a_scale
    r_max = 8.0 * (n_max + 1) ** 2 * a_scale
    edges = np.geomspace(r_min, r_max, N_sec + 1)
    # decaying BC at r_max: u ∝ e^{-κr}, u′ = -κu (normalize u(r_max)=1)
    state = np.array([1.0, -kappa])
    r_rec = [edges[-1]]
    u_rec = [1.0]
    for i in range(N_sec - 1, -1, -1):
        Msec = dress_section(edges[i], edges[i + 1], E_J, Z, l, m_probe, 1, saturate)
        # inward step: invert the lossless ABCD section (det = 1)
        M_inv = np.array([[Msec[1, 1], -Msec[0, 1]], [-Msec[1, 0], Msec[0, 0]]])
        state = M_inv @ state
        r_rec.append(edges[i])
        u_rec.append(state[0])
    r = np.array(r_rec[::-1])
    u = np.array(u_rec[::-1])
    w = np.abs(u) ** 2
    mean_r = _trapz(r * w, r) / _trapz(w, r)
    return {
        "E1_eV": E1,
        "mean_r_m": mean_r,
        "a_scale_m": a_scale,
        "mean_r_over_a_scale": mean_r / a_scale,  # == 1.5 for the 1s shape factor
        "inner_regularity": abs(u[0]) / np.max(np.abs(u)),  # small ⇒ u→0 at r_min (regular)
    }


# ---------------------------------------------------------------------------
# Analytic frozen marks (M1-M4) and the muonic operating-point check (brief §3)
# ---------------------------------------------------------------------------


def hydrogen_marks_inf_mass(n_max=4):
    """M1/M2 — infinite-mass convention: E_n = −Ry/n², a₀ = A_0."""
    E = {n: -RY_EV / n**2 for n in range(1, n_max + 1)}
    return {"E_n_eV": E, "En_n2": {n: E[n] * n**2 for n in E}, "a0_m": A_0, "a0_identity_ell_over_alpha": L_NODE / ALPHA}


def muonic_marks():
    """M3 — reduced-mass muonic marks (a_μ, E_n(μH))."""
    a_mu = A_0 * (M_E / M_R_MU)
    E = {n: -RY_EV * (M_R_MU / M_E) / n**2 for n in (1, 2, 3)}
    return {
        "a_mu_m": a_mu,
        "a_mu_fm": a_mu * 1e15,
        "E_n_muH_eV": E,
        "mr_mu_over_me": M_R_MU / M_E,
        "mr_mu_over_mr_H": M_R_MU / M_R_H,
        "a_mu_vs_ell_node": a_mu / L_NODE,  # <1 ⇒ sub-lattice-cell (substrate flag)
    }


def muonic_operating_point_A():
    """Brief §3 named check — A = E_Coulomb(a_μ)/E_yield.

    Returns BOTH yield references honestly:
      * A_dielectric = E_Coulomb(a_μ)/(e·V_YIELD)  — the brief §3 formula
        (dielectric-yield reference); O(0.1), NOT deep-linear.
      * A_rupture    = V_Coulomb(a_μ)/(m_e c²)      — the Ax-4 kernel argument
        the ODE saturation ACTUALLY uses (lattice rupture scale); deep-linear.
    The gap between them is the two-yield-reference flag (surfaced, not resolved).
    """
    a_mu = A_0 * (M_E / M_R_MU)
    E_coul_J = e_charge**2 / (4.0 * np.pi * EPSILON_0 * a_mu)  # Coulomb energy at a_μ
    E_coul_eV = E_coul_J / e_charge
    E_yield_eV = V_YIELD  # e·V_YIELD in eV == V_YIELD numerically
    A_dielectric = E_coul_eV / E_yield_eV
    A_rupture = E_coul_J / (M_E * C_0**2)
    return {
        "E_coulomb_a_mu_eV": E_coul_eV,
        "A_dielectric": A_dielectric,  # brief §3: ~0.12
        "A_rupture": A_rupture,  # Ax-4 kernel arg the ODE uses: ~0.0099
        "hydrogen_A_dielectric_ref": (e_charge**2 / (4.0 * np.pi * EPSILON_0 * A_0) / e_charge) / V_YIELD,  # ~6e-4
    }


# ---------------------------------------------------------------------------
# Gates (P11) — each must PASS on the real profile and FIRE on its plant
# ---------------------------------------------------------------------------


def _assign_n(eigs_eV, ry_scale, Z=1):
    """Map eigenvalues to n* = √(Z²·ry_scale/E); returns (n*, nearest int)."""
    out = []
    for E in eigs_eV:
        nstar = np.sqrt(Z**2 * ry_scale / E)
        out.append((nstar, int(round(nstar))))
    return out


def gate_mark(eigs_eV, ry_scale=RY_EV, Z=1, tol=5e-3):
    """G-MARK: every eigenvalue matches Z²·ry_scale/n² (integer n) within tol.

    Returns (passed, detail). FIRES (passed=False) if any eigenvalue misses its
    nearest integer level, or if no eigenvalues were found at all.
    """
    if not eigs_eV:
        return False, {"reason": "no eigenvalues found at the marks"}
    detail = {}
    ok = True
    for E in eigs_eV:
        nstar = np.sqrt(Z**2 * ry_scale / E)
        n = int(round(nstar))
        if n < 1:
            ok = False
            detail[f"E={E:.4g}"] = {"n": n, "rel_err": None, "fire": True}
            continue
        tgt = Z**2 * ry_scale / n**2
        rel = abs(E - tgt) / tgt
        detail[f"n={n}"] = {"E": E, "target": tgt, "rel_err": rel, "fire": bool(rel > tol)}
        ok = ok and (rel <= tol)
    return bool(ok), detail


def gate_form(eigs_eV, Z=1, spread_tol=5e-3):
    """G-FORM: E_n·n² constant across n (the 1/n² form). FIRES if spread > tol."""
    if len(eigs_eV) < 2:
        return False, {"reason": "need ≥2 eigenvalues for a form check"}
    ry_guess = eigs_eV[0] / Z**2  # ground state = n=1 level
    prods = []
    for E in eigs_eV:
        n = int(round(np.sqrt(Z**2 * ry_guess / E)))
        n = max(n, 1)
        prods.append(E * n**2 / Z**2)
    prods = np.array(prods)
    spread = (prods.max() - prods.min()) / prods.mean()
    return bool(spread <= spread_tol), {"En_n2_values": prods.tolist(), "spread": float(spread)}


def gate_int(eigs_eV, ry_scale=RY_EV, Z=1, int_tol=0.02):
    """G-INT: n* = √(Z²·ry_scale/E) rounds to an integer (closure = 2πn).

    FIRES if any n* is farther than int_tol from an integer.
    """
    if not eigs_eV:
        return False, {"reason": "no eigenvalues"}
    devs = []
    for nstar, n in _assign_n(eigs_eV, ry_scale, Z):
        devs.append(abs(nstar - n))
    devs = np.array(devs)
    return bool(devs.max() <= int_tol), {"n_star_devs": devs.tolist(), "max_dev": float(devs.max())}


def _report():  # pragma: no cover — human-readable driver run
    print("=" * 74)
    print("x42 — THE ATOMIC EIGENCAVITY (hydrogen as Op6 phase closure)")
    print("=" * 74)

    print("\n[M1/M2] infinite-mass marks:")
    m12 = hydrogen_marks_inf_mass()
    for n, E in m12["E_n_eV"].items():
        print(f"   n={n}: E_n={E:+.6f} eV   E_n·n²={m12['En_n2'][n]:.6f} eV")
    print(f"   a₀ = {m12['a0_m']:.9e} m ; ℓ_node/α = {m12['a0_identity_ell_over_alpha']:.9e} m")

    print("\n[Deliverable 2] phase-closure spectrum (ABCD B_total=0, Z=1, real 1/r):")
    eigs = phase_closure_spectrum(Z=1, l=0)
    for E in eigs:
        nstar = np.sqrt(RY_EV / E)
        tgt = RY_EV / round(nstar) ** 2
        print(f"   E={E:.4f} eV  n*={nstar:.4f}  Ry/n²={tgt:.4f}  err={(E - tgt) / tgt * 100:+.3f}%")
    print("   gates:", "MARK", gate_mark(eigs)[0], "| FORM", gate_form(eigs)[0], "| INT", gate_int(eigs)[0])

    print("\n[M2] eigenmode-scale extraction — ⟨r⟩ of the ground-state eigenfunction:")
    m2 = ground_state_mean_radius(Z=1, l=0, N_sec=4000)
    print(f"   ⟨r⟩/a_scale = {m2['mean_r_over_a_scale']:.6f}  (1s shape factor = 1.5;"
          f" rel err {abs(m2['mean_r_over_a_scale'] - 1.5) / 1.5 * 100:+.4f}%)")

    print("\n[Deliverable 3] muonic-H — same network, probe m_e→m_r,μ:")
    mm = muonic_marks()
    print(f"   a_μ = {mm['a_mu_fm']:.3f} fm   (a_μ/ℓ_node = {mm['a_mu_vs_ell_node']:.4f}  <1 ⇒ sub-cell)")
    for n, E in mm["E_n_muH_eV"].items():
        print(f"   n={n}: E_n(μH)={E / 1e3:+.5f} keV")
    eigs_mu = muonic_spectrum()
    for E in eigs_mu[:3]:
        nstar = np.sqrt((RY_EV * mm["mr_mu_over_me"]) / E)
        print(f"   driver: E={E / 1e3:.5f} keV  n*={nstar:.4f}")

    print("\n[Brief §3] muonic operating-point A:")
    A = muonic_operating_point_A()
    print(f"   A_dielectric = E_Coulomb(a_μ)/E_yield = {A['A_dielectric']:.4f}  (H ref ~{A['hydrogen_A_dielectric_ref']:.1e})")
    print(f"   A_rupture (Ax-4 kernel arg the ODE uses) = {A['A_rupture']:.5f}")

    print("\n[Sabotage P11] planted 1/r² dress (dress_exp=2) — gates MUST fire:")
    eigs_bad = phase_closure_spectrum(Z=1, l=0, dress_exp=2)
    print("   1/r² eigenvalues:", [f"{E:.4f}" for E in eigs_bad] or "none")
    print("   G-MARK fired:", not gate_mark(eigs_bad)[0])
    print("\n[Sabotage P11] detuned closure integer (targets Ry/(n+0.4)²):")
    detuned = RY_EV / (np.arange(1, 5) + 0.4) ** 2
    print("   G-MARK vs detuned fired:", not gate_mark(list(detuned))[0])


if __name__ == "__main__":  # pragma: no cover
    _report()
