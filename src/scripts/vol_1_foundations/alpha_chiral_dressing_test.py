"""
alpha_chiral_dressing_test.py -- alpha Class-2 lift, CHIRAL Meissner dressing (Test 4).

Tests whether the CHIRAL Meissner coupling -- the canonical R != r symmetry-
breaker that Tests 1-3 all MISSED -- selects the aspect ratio R/r -> phi^2 in the
K4 V-tank phase space. If yes, R/r = phi^2 AND R - r = 1/2 ==> R*r = 1/4 as a
CONSEQUENCE (derived, not posited) -> the alpha Class-2 lift LANDS.

WHY THIS IS THE TEST TESTS 1-3 MISSED
-------------------------------------
Tests 1-3 used SYMMETRIC / achiral perturbations. Test 3's dressing
(_frozen_z_local_from_seed in alpha_dressed_eigenmode_test.py) reads the |V|
MAGNITUDE strain on the plain K4-TLM lattice via K4Lattice3D._update_z_local_field
-- magnitude-symmetric (Z_eff/Z_0 = 1/sqrt(S), S = sqrt(1 - (|V|/V_SNAP)^2)). A
magnitude-symmetric perturbation CANNOT select an aspect ratio: it is invariant
under the chirality flip that distinguishes R from r. Test 3 MEASURED the PRODUCT
R*r (chirality-INVARIANT) and found it flat -- exactly as a symmetric perturbation
must.

The CHIRAL Meissner asymmetry lives in src/ave/topological/cosserat_field_3d.py
(_reflection_density_asymmetric, _update_saturation_kernels) and the coupled
engine src/ave/topological/k4_cosserat_coupling.py (CoupledK4Cosserat,
use_asymmetric_saturation=True, kappa_chiral=KAPPA_CHIRAL_ELECTRON). It was NEVER
invoked by Tests 1-3. The split is:
    A2_mu  = (1 + kappa_chiral * h_local) * kappa^2 / omega_yield^2      (magnetic)
    A2_eps = (1 - kappa_chiral * h_local) * (eps_sym^2/eps_yield^2 + V^2/V_SNAP^2) (electric)
    S_mu = sqrt(1 - A2_mu),  S_eps = sqrt(1 - A2_eps)
    Z_eff/Z_0 = sqrt(S_mu / S_eps)                                  (Vol 1 Ch 7:252)
where h_local = omega . (curl omega) / (|omega| |curl omega|) is the normalized
Beltrami HELICITY of the COSSERAT omega field (doc 54_ §6:167,220). h_local FLIPS
SIGN under handedness reversal -- the chirality the symmetric |V| dressing lacks.

ENGINE WIRING (settled by corpus -- doc 54_ §6, NOT an open question)
--------------------------------------------------------------------
doc 54_:167 "when the local Cosserat omega field has a preferred chirality,
saturation proceeds asymmetrically." doc 54_:220 h_local = omega.(curl omega)/
(|omega||curl omega|). doc 54_:358 kappa_chiral = 1.2*alpha = alpha*pq/(p+q) for
(2,3). So the chiral dressing is driven by the COSSERAT omega helicity, biases the
K4 BOND impedance via Z_eff = Z_0*sqrt(S_mu/S_eps), and the K4 V-tank eigenmode
then reads the chiral-dressed aspect. This is EXACTLY the CoupledK4Cosserat
._update_z_local_total path (k4_cosserat_coupling.py:379-393). THIS driver freezes
that chiral z_local into the same frozen-linear K4 step operator Test 3 used, then
measures R/r (the ASPECT) of the dressed V-sector eigenmode.

THE MEASUREMENT (CHANGED FROM TEST 3 -- load-bearing)
-----------------------------------------------------
Test 3 measured R*r (the PRODUCT -- chirality-INVARIANT, flat as expected).
TEST 4 MEASURES R/r (the ASPECT -- chirality-DEPENDENT). Sweep the (R, r) family;
for each, read the chiral-dressed eigenmode's selected R/r in the V-tank phasor
plane. Does the chiral dressing develop an R/r-selecting extremum vs the flat
symmetric Test-3 control? What R/r does it land on?

THE alpha-FREE / MAGNITUDE DISCRIMINATOR (THE crux)
---------------------------------------------------
chi_chiral = alpha*pq/(p+q) = 1.2*alpha ~= 0.0088 -- SMALL. A small coupling
NAIVELY gives a SMALL asymmetry (R/r ~ 1 + O(alpha)), NOT phi^2 ~= 2.618. So we
SWEEP the chiral coupling strength chi and resolve which regime holds:
  (A) R/r -> phi^2 set by the (2,3) TOPOLOGY (pq/(p+q)=6/5 handedness factor;
      phi^2 emerges ACROSS coupling strengths, alpha only the overall scale)
      -> alpha-FREE, LIFT LANDS.
  (B) R/r = phi^2 ONLY at the specific alpha-injected chi=1.2*alpha -> circular, close.
  (FLAT/SMALL) physical chi=1.2*alpha gives only a small O(alpha) saliency
      (R/r ~ 1, the g-2-scale delta = -3*alpha/2), never reaching phi^2
      -> phi^2 rests on R*r=1/4, close.
We report R/r vs chi (SWEPT) and whether phi^2 is topology-set (alpha-free) or
coupling-magnitude-set.

OUTCOMES
--------
  A (LIFT LANDS):  chiral dressing selects R/r = phi^2 from a generic seed,
                   phi^2 set by (2,3) topology (alpha-free; emerges across
                   coupling strengths) -> R*r = 1/4 derived.
  B (CIRCULAR):    R/r = phi^2 only at the alpha-injected chi = 1.2*alpha -> close.
  C (OTHER):       dressing lifts the aspect but selects a different R/r.
  FLAT/SMALL (CLOSE): chiral coupling gives only a small O(alpha) asymmetry
                   (R/r ~ 1), never reaches phi^2 -> close.

GUARDS (reuse Test-3 machinery -- one subtlety)
-----------------------------------------------
  GENERIC SEED: R/r != phi^2, no PHI / R_GOLDEN_TORUS imported (generic torus).
  SUBTLETY (kappa_chiral carries alpha BY DEFINITION, chi=1.2*alpha): kappa_chiral
    is an ALLOWED INPUT here (it IS the physics under test -- the chiral coupling),
    so it is whitelisted in the dressing builder ONLY. But the AST alpha-guard
    still FORBIDS {ALPHA_COLD*, V_SNAP, XI_TOPO, PHI, R_GOLDEN_TORUS*} in the
    GEOMETRY MEASURES (the R/r aspect read-out must be alpha-free), and we FLAG
    every place alpha enters and resolve whether R/r=phi^2 depends on the
    alpha-VALUE or only on the topology (the chi-sweep IS that resolution).
  FORWARD-NOT-FIT: raw R/r vs chi; no tuning to phi^2.
  PML-EXCLUDED: interior-only top-K sampling (Rule 10 corollary).
  THRESHOLD-FREE: participation-ratio / weighted-RMS, no magic cut.
  V-TANK COORDINATE: R/r measured in the K4 (V_inc, V_ref) phasor plane (doc
    28_:72,85-87 "phase-space R_phase/r_phase = phi^2 ... they needn't match"
    with real space), NOT real-space lattice and NOT the Cosserat (u, omega) plane.

Branch: analysis/alpha-chiral-dressing (off main; do NOT merge).
Skills: substrate-native-check (chiral asymmetric saturation; S_mu/S_eps split;
V-sector eigenmode dressed by Cosserat-omega-helicity-biased bond impedance),
phase-space-coordinate-check (K4 V-tank (V_inc, V_ref); measure R/r the ASPECT),
ave-canonical-source (KAPPA_CHIRAL_ELECTRON, KAPPA_TILDE_ELECTRON imported
canonically; omega_yield/eps_yield read from the engine), ave-driver-script-honesty
(forward chi-sweep, no fit; chiral z_local is computed by the engine kernel, not
a literal).
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))


# ======================================================================
# SECTION 1 -- configuration  (GENERIC seed; NO Golden-Torus / phi as VALUE)
# ======================================================================
N_LATTICE = 24  # K4 interior cells per axis (Test-3 validated floor where the
#   generic (2,3) seed reads back as (2,3) through the V-tank
#   phasor measure; r >= ~2 cells needed to resolve q=3).
PML = 4  # PML collar thickness (cells); excluded from all measures and
#   used as the leak channel for the binding signature.

# Generic (R, r) hedgehog sweep -- round-neutral grid, NOT centered on the Golden
# Torus. R/r straddles phi^2 = 2.618 (2.0 < ratios < 4.0) but NEVER samples it,
# and no grid point is the canonical Golden Torus. Whether the chiral dressing
# PULLS the dressed-eigenmode R/r toward phi^2 from these generic seeds is the test.
R_MAJOR_SWEEP = (5.0, 6.0, 7.0, 8.0)  # major radius (cells), generic
R_OVER_r_SWEEP = (2.0, 2.4, 2.8, 3.4, 4.0)  # generic R/r seeds (phi^2 straddled, absent)

SEED_AMPLITUDE_FRAC = 0.30  # peak |V| / |omega| seed amplitude (natural units,
#   V_SNAP=1 so strain == |V|). The doc-34 X4a/X4b bound-
#   state set-point, NOT a geometric posit. Fine for the
#   frozen eigensolve (z is FROZEN; no time-integration).

# Chiral coupling-strength sweep -- THE crux. chi=0 is the chiral-coupling-OFF
# reference (a residual base mu/eps asymmetry persists there from the seed -- see
# chiral_z_local_from_seed ENGINE-REALITY FLAG; the clean achiral control is the
# BARE op3=False arm). chi = KAPPA_CHIRAL_ELECTRON = 1.2*alpha ~= 0.00876 is
# the PHYSICAL alpha-injected point. The larger chi values probe whether the
# R/r-selection is set by the (2,3) topology (alpha-FREE -> phi^2 across chi) or
# only appears at the alpha-injected chi (circular). chi enters ONLY the dressing
# builder (the physics under test); the R/r geometry measure stays alpha-free.
# (Sweep spans O(alpha) -> O(1): the small values 0.001..0.05 bracket the physical
# 1.2*alpha to resolve any near-physical structure; 0.10, 0.30, 0.60, 0.90 reach
# O(1) coupling so a topology-set phi^2 PLATEAU, if it exists, is visible across a
# >100x range. h_local in [-1,+1], so chi*h_local stays < 1 -> A2_mu, A2_eps stay
# sub-rupture; chi up to ~0.9 keeps the saturation kernels real on the seed shell.
# Forward, not fit.)
CHI_SWEEP = (0.0, 0.001, 0.005, 0.00875682308316, 0.02, 0.05, 0.10, 0.30, 0.60, 0.90)
CHI_PHYSICAL_INDEX = 3  # index of KAPPA_CHIRAL_ELECTRON (=1.2*alpha) in CHI_SWEEP;
#   asserted == the canonical import at runtime (no drift).

# Target eigenphase for the V-sector transmission eigenmode. ALPHA-FREE:
#   theta_C = omega_C * dt = (c/ell_node)*(dx/(c*sqrt2)) = 1/sqrt(2) rad/step.
# Pure 4-port K4 lattice dispersion -- no alpha, no e, no phi.
THETA_C = 1.0 / np.sqrt(2.0)

HANDEDNESS = "RH"  # seed handedness for the chiral omega field. RH -> h_local > 0
#   on the shell -> A2_mu boosted, A2_eps suppressed (Meissner
#   mu-collapse first, doc 54_:199). The aspect-selection sign
#   is read off the dressed eigenmode; LH is run as a control to
#   confirm the asymmetry FLIPS with handedness (the chirality
#   signature the symmetric |V| dressing structurally lacks).

RNG_SEED = 20260602  # random-direction baseline seed.

N_EIGS = 40  # eigenpairs to request near theta_C per arm.


# ======================================================================
# SECTION 2 -- AST-token alpha-guard (Test-3 machinery + the chi subtlety)
# ======================================================================
# Every GEOMETRY / WINDING / aspect MEASURE must NOT consume alpha, charge, the
# topological self-impedance xi, the rupture voltage V_SNAP, PHI, or the Golden-
# Torus constants AS VALUES -- the R/r aspect read-out must be alpha-free so that
# whatever R/r the dressing selects cannot have been smuggled in. This scans the
# guarded functions' source (AST identifiers actually used as Name/Attribute,
# ignoring docstrings + comments) so a future edit that smuggles a forbidden
# token into a measure trips at RUNTIME. (Mirrors Test 3's _self_audit; the
# alpha-FREE part is identical.)
#
# THE SUBTLETY (per the brief): kappa_chiral carries alpha BY DEFINITION
# (chi=1.2*alpha) and is the PHYSICS UNDER TEST -- the chiral coupling we sweep.
# Three tiers, by how each function relates to the chiral coupling:
#
#   1. THE DRESSING BUILDER (chiral_z_local_from_seed): the ONE function that
#      CONSUMES the chiral coupling as a VALUE (feeds chi into the engine's
#      S_mu/S_eps kernel). It IS the dressing. Excluded from both guard tiers;
#      the audit asserts the chiral token APPEARS here (so a refactor can't
#      silently revert it to Test-3's symmetric form).
#
#   2. THE GEOMETRY/WINDING/ASPECT MEASURES (_MEASURE_FUNCS): read R/r and (p,q)
#      off the eigenvector. These must be FULLY alpha-free AND must NOT even name
#      a chiral-coupling token -- the aspect read-out cannot be contaminated by
#      the alpha-injected coupling. Strictest tier.
#
#   3. ORCHESTRATION / PLUMBING (_ORCHESTRATION_FUNCS): operator-builders + sweep
#      drivers + adjudication that THREAD chi as a routed PARAMETER to the
#      dressing builder (e.g. build_step_operator(..., chi) -> chiral_z_local_
#      from_seed(..., chi)). They never consume chi to MEASURE geometry -- they
#      pass it through. They remain under the FULL alpha-free forbidden-token
#      guard (no ALPHA/PHI/V_SNAP/GT as values), but naming `chi` as a plumbed
#      argument is legitimate (and unavoidable: something must route the swept
#      coupling to the dressing). Adjudicate names KAPPA_CHIRAL_ELECTRON only to
#      TAG which sweep point is physical, never to measure an aspect.
#
# This keeps the discriminator clean: alpha enters ONLY the coupling, the
# coupling is CONSUMED only in the dressing, and the aspect MEASURES are provably
# alpha-free and chiral-token-free.
_FORBIDDEN_TOKENS = (
    "ALPHA",
    "ALPHA_COLD",
    "ALPHA_COLD_INV",
    "ALPHA_S",
    "ALPHA_TARGET",
    "V_SNAP",
    "XI_TOPO",
    "e_charge",
    "E_CHARGE",
    "PHI",
    "PHI_SQ",
    "R_GOLDEN_TORUS",
    "R_GOLDEN_TORUS_MINOR",
    "RR_GOLDEN_TORUS",
    "GOLDEN_TORUS",
)
# Tokens the DRESSING builder may legitimately consume (the chiral coupling IS the
# physics under test). These are NOT a license to inject alpha into a measure --
# they are scoped to the dressing builder only, which is excluded from the guarded
# set. KAPPA_CHIRAL_ELECTRON / kappa_chiral carry alpha by the doc-20 definition
# chi = alpha*pq/(p+q); KAPPA_TILDE_ELECTRON is the pure topology factor (6/5).
_CHIRAL_COUPLING_TOKENS = (
    "KAPPA_CHIRAL_ELECTRON",
    "KAPPA_TILDE_ELECTRON",
    "kappa_chiral",
    "chi",
    "CHI_SWEEP",
)
# Tier 2 -- the GEOMETRY / WINDING / ASPECT MEASURES + seeders. STRICTEST: forbidden
# from BOTH the alpha-free token set AND the chiral-coupling token set. The aspect
# read-out (R/r) and the (p,q) winding must contain NO alpha and NO chiral coupling.
# seed_chiral_cosserat_omega is here too: it builds the omega field from pure
# geometry + a handedness SIGN, NOT from the chiral coupling strength (chi enters
# only later, in the dressing builder), so it must be chiral-token-free as well.
_MEASURE_FUNCS = (
    "seed_generic_2_3_vtank",
    "seed_random_baseline_vtank",
    "seed_chiral_cosserat_omega",
    "eig_near_thetaC",
    "measure_eigvec_localization",
    "measure_vtank_winding_pq",
    "measure_vtank_aspect_phase_space",
    "_eigvec_to_fields",
    "_phasor_contour_winding",
    "_port_chirality_weights",
    "_pack_live_as_eigvec",
)
# Tier 3 -- ORCHESTRATION / PLUMBING. Forbidden from the alpha-free token set
# (no ALPHA/PHI/V_SNAP/GT as values), but PERMITTED to NAME a chiral-coupling token
# as a routed parameter (build_step_operator threads `chi` to the dressing builder;
# the sweep drivers iterate CHI_SWEEP and pass chi through; adjudicate names
# KAPPA_CHIRAL_ELECTRON only to TAG the physical sweep point). None of these consume
# a chiral token to MEASURE an aspect -- they route or tag it.
_ORCHESTRATION_FUNCS = (
    "build_step_operator",
    "_mode_record",
    "_select_modes",
    "prong1_chiral_landscape",
    "chi_sweep_aspect",
    "_aspect_landscape_stats",
    "adjudicate",
)


def _ast_identifiers_used(fn) -> set[str]:
    """All identifiers a function uses as Name or Attribute (NOT in docstrings or
    comments). Pure-source scan via the AST -- the alpha-free verification core."""
    import ast
    import inspect
    import textwrap

    tree = ast.parse(textwrap.dedent(inspect.getsource(fn)))
    used: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            used.add(node.id)
        elif isinstance(node, ast.Attribute):
            used.add(node.attr)
    return used


def _self_audit_no_forbidden_tokens() -> None:
    """Hard-fail on token violations across the three tiers (see SECTION 2 header).

    Checks:
      (1) NO function in EITHER tier (_MEASURE_FUNCS, _ORCHESTRATION_FUNCS) consumes
          {ALPHA*, V_SNAP, XI_TOPO, charge, PHI, R_GOLDEN_TORUS*} -- alpha-free.
      (2) NO _MEASURE_FUNCS function even NAMES a chiral-coupling token -- the aspect
          / winding read-out must be alpha-free AND chiral-coupling-free.
      (3) The dressing builder chiral_z_local_from_seed DOES consume a chiral token
          (asserted present, so a refactor can't silently revert it to symmetric).

    _ORCHESTRATION_FUNCS are PERMITTED to name a chiral token: they route `chi` to
    the dressing builder or TAG the physical sweep point -- they never consume it to
    measure an aspect. (Verified by construction: build_step_operator passes chi to
    chiral_z_local_from_seed; the sweeps iterate CHI_SWEEP; adjudicate compares an
    ALREADY-measured R/r to a numeric target and tags chi==KAPPA_CHIRAL_ELECTRON.)
    """
    this_mod = sys.modules.get(_self_audit_no_forbidden_tokens.__module__)
    if this_mod is None:
        this_mod = sys.modules.get(__name__)
    if this_mod is None:
        _g = _self_audit_no_forbidden_tokens.__globals__

        class _GlobalsModule:
            def __getattr__(self, k):
                return _g.get(k)

        this_mod = _GlobalsModule()

    forbidden = set(_FORBIDDEN_TOKENS)
    chiral = set(_CHIRAL_COUPLING_TOKENS)
    violations: list[str] = []

    # (1) alpha-free across BOTH tiers.
    for fname in _MEASURE_FUNCS + _ORCHESTRATION_FUNCS:
        fn = getattr(this_mod, fname, None)
        if fn is None:
            continue
        used = _ast_identifiers_used(fn)
        for tok in sorted(used & forbidden):
            violations.append(f"{fname}: forbidden token '{tok}' (alpha/charge/PHI/V_SNAP/GT) -- not alpha-free")

    # (2) chiral-coupling-free in the MEASURES only.
    for fname in _MEASURE_FUNCS:
        fn = getattr(this_mod, fname, None)
        if fn is None:
            continue
        used = _ast_identifiers_used(fn)
        for tok in sorted(used & chiral):
            violations.append(
                f"{fname}: chiral-coupling token '{tok}' in a GEOMETRY/WINDING MEASURE "
                f"(the alpha-injected coupling must not enter the aspect read-out)"
            )

    if violations:
        raise RuntimeError(
            "GUARD TRIPPED -- token violation in an eigenvalue/geometry/winding measure:\n  "
            + "\n  ".join(violations)
        )
    # Positive confirmation: the dressing builder DOES consume the chiral coupling
    # (it is the physics under test) -- assert it is present so a refactor that
    # accidentally drops the chiral bias is caught (the dressing would silently
    # become Test-3's symmetric form again).
    dressing = getattr(this_mod, "chiral_z_local_from_seed", None)
    if dressing is not None:
        dused = _ast_identifiers_used(dressing)
        if not (dused & chiral):
            raise RuntimeError(
                "GUARD TRIPPED -- chiral_z_local_from_seed consumes NO chiral-coupling token: "
                "the dressing has silently reverted to a symmetric (Test-3) form; the CHIRAL "
                "asymmetry under test is absent."
            )
    print(
        "  [guard] AST token self-audit PASS: no alpha/charge/PHI/V_SNAP/Golden-Torus in any "
        "measure; chiral coupling confined to the dressing builder (and present there)"
    )


# ======================================================================
# SECTION 3 -- frozen-linear K4 step operator (achiral control + CHIRAL dressed)
# ======================================================================
import jax.numpy as jnp  # noqa: E402

from ave.core.k4_tlm import K4Lattice3D  # noqa: E402

# Canonical chiral-coupling imports (ave-canonical-source): the physical chiral
# coupling KAPPA_CHIRAL_ELECTRON = alpha*pq/(p+q) and its pure-topology factor
# KAPPA_TILDE_ELECTRON = 6/5. Imported, never hard-coded. _update_saturation_kernels
# is the engine's canonical (S_mu, S_eps) chiral split (single source of truth,
# shared with CoupledK4Cosserat._update_z_local_total).
from ave.topological.cosserat_field_3d import (  # noqa: E402
    KAPPA_CHIRAL_ELECTRON,
    KAPPA_TILDE_ELECTRON,
    _update_saturation_kernels,
)

# Cache for the (R, r, chi)-INDEPENDENT achiral BARE step matrix.
_BARE_MATRIX_CACHE: dict = {}


def _build_lattice(op3: bool) -> K4Lattice3D:
    """K4 lattice in ENGINE NATURAL UNITS (V_SNAP=1.0 -> strain == |V|, so no
    rupture-voltage token leaks into any seeder/measure). op3 toggles the Op14
    bond-reflection dressing path: op3=False is the BARE pure-unitary lattice
    (Gamma=0 everywhere); op3=True applies the strain-coupled bond reflection
    (into which we freeze the CHIRAL z_local)."""
    n = N_LATTICE + 2 * PML
    return K4Lattice3D(
        n,
        n,
        n,
        dx=1.0,
        pml_thickness=PML,
        op3_bond_reflection=op3,
        V_SNAP=1.0,
    )


def _toroidal_coords(lat: K4Lattice3D, R: float, r: float):
    """(phi, psi, rho_tube) toroidal coords about the lattice center, plus the
    (2,3) knot-tangent unit vector. Pure geometry -- no alpha/charge/phi."""
    cx = (lat.nx - 1) / 2.0
    cy = (lat.ny - 1) / 2.0
    cz = (lat.nz - 1) / 2.0
    idx = np.indices((lat.nx, lat.ny, lat.nz))
    x = idx[0] - cx
    y = idx[1] - cy
    z = idx[2] - cz
    rho_xy = np.sqrt(x**2 + y**2 + 1e-12)
    rho_tube = np.sqrt((rho_xy - R) ** 2 + z**2 + 1e-12)
    phi = np.arctan2(y, x)
    psi = np.arctan2(z, rho_xy - R)
    dphi_x = -(R + r * np.cos(psi)) * np.sin(phi)
    dphi_y = (R + r * np.cos(psi)) * np.cos(phi)
    dpsi_x = -r * np.sin(psi) * np.cos(phi)
    dpsi_y = -r * np.sin(psi) * np.sin(phi)
    dpsi_z = r * np.cos(psi)
    tx = 2.0 * dphi_x + 3.0 * dpsi_x
    ty = 2.0 * dphi_y + 3.0 * dpsi_y
    tz = 3.0 * dpsi_z
    tmag = np.sqrt(tx**2 + ty**2 + tz**2 + 1e-12)
    return phi, psi, rho_tube, (tx / tmag, ty / tmag, tz / tmag)


def seed_generic_2_3_vtank(lat: K4Lattice3D, R: float, r: float, peak_amp: float) -> None:
    """Write a GENERIC (2,3) chiral phasor into the K4 V-tank (V_inc, V_ref) at
    90-deg quadrature -- the corpus-canonical phase-space coordinate (doc 28_:64-67):
        V_inc[..,p] = env * chir_p * cos(2 phi + 3 psi)
        V_ref[..,p] = env * chir_p * sin(2 phi + 3 psi)
    The per-port phasor angle arctan2(V_ref, V_inc) = 2 phi + 3 psi winds the
    (2,3) pattern in PHASE-SPACE. (R, r) are GENERIC sweep values, never the
    Golden Torus. No alpha/charge/phi: amplitude is a plain float in natural
    units (V_SNAP=1). (Identical to Test 3's seeder -- the K4 V-tank C-state.)"""
    phi, psi, rho_tube, (thx, thy, thz) = _toroidal_coords(lat, R, r)
    r_opt = max(r, 1.0)
    env = peak_amp * np.pi / (1.0 + (rho_tube / r_opt) ** 2)
    ports = [(+1.0, +1.0, +1.0), (+1.0, -1.0, -1.0), (-1.0, +1.0, -1.0), (-1.0, -1.0, +1.0)]
    inv_sqrt3 = 1.0 / np.sqrt(3.0)
    theta = 2.0 * phi + 3.0 * psi
    cth, sth = np.cos(theta), np.sin(theta)
    for p, (px, py, pz) in enumerate(ports):
        chir = inv_sqrt3 * (px * thx + py * thy + pz * thz)
        lat.V_inc[..., p] = env * chir * cth
        lat.V_ref[..., p] = env * chir * sth
    lat.V_inc[~lat.mask_active] = 0.0
    lat.V_ref[~lat.mask_active] = 0.0


def seed_random_baseline_vtank(lat: K4Lattice3D, R: float, r: float, peak_amp: float) -> None:
    """Random-phase baseline at the SAME per-site |V| envelope as the generic
    (2,3) seed but with the toroidal winding scrambled -- the dispersal control.
    A non-topological blob should NOT develop a chirality-selected aspect."""
    seed_generic_2_3_vtank(lat, R, r, peak_amp)
    rng = np.random.default_rng(RNG_SEED)
    mag_inc = np.abs(lat.V_inc)
    mag_ref = np.abs(lat.V_ref)
    sgn = rng.integers(0, 2, size=lat.V_inc.shape) * 2 - 1
    lat.V_inc = mag_inc * sgn
    sgn2 = rng.integers(0, 2, size=lat.V_ref.shape) * 2 - 1
    lat.V_ref = mag_ref * sgn2
    lat.V_inc[~lat.mask_active] = 0.0
    lat.V_ref[~lat.mask_active] = 0.0


def seed_chiral_cosserat_omega(R: float, r: float, peak_amp: float, handedness: str = HANDEDNESS) -> np.ndarray:
    """Build a CHIRAL (2,3) Cosserat omega field whose Beltrami helicity h_local is
    nonzero -- this is what DRIVES the asymmetric (S_mu, S_eps) split (doc 54_:167,
    220). The symmetric Test-3 dressing had NO omega field; the chiral dressing
    NEEDS one with handedness so omega.(curl omega) != 0.

    Construction: a helical (2,3) hedgehog. The in-plane (omega_x, omega_y) carry
    the toroidal/poloidal winding theta = 2 phi + 3 psi; the out-of-plane omega_z
    is given a handedness-signed component proportional to the SAME envelope so the
    field has a net helicity along the tube (RH: omega_z follows +theta gradient;
    LH: -). Pure geometry + handedness sign -- no alpha/charge/phi (omega is a plain
    micro-rotation field in natural units; the chiral COUPLING strength enters later
    as chi in the dressing builder, not here).

    Returns omega array (nx, ny, nz, 3). The handedness sign FLIPS h_local; running
    both RH and LH and seeing the aspect asymmetry FLIP is the chirality signature
    the magnitude-symmetric |V| dressing structurally cannot produce.
    """
    lat = _build_lattice(op3=True)
    phi, psi, rho_tube, _t = _toroidal_coords(lat, R, r)
    r_opt = max(r, 1.0)
    env = peak_amp * np.pi / (1.0 + (rho_tube / r_opt) ** 2)
    theta = 2.0 * phi + 3.0 * psi
    sign = +1.0 if handedness.upper() == "RH" else -1.0
    omega = np.zeros((lat.nx, lat.ny, lat.nz, 3), dtype=np.float64)
    omega[..., 0] = env * np.cos(theta)
    omega[..., 1] = env * np.sin(theta)
    # Handedness-signed longitudinal component: a Beltrami-like omega_z that makes
    # the field helical (curl omega parallel/antiparallel to omega) so h_local != 0.
    # Tied to the SAME envelope and winding so it is a property of the (2,3) seed,
    # not an independent knob. sign flips RH<->LH (and thus h_local sign).
    omega[..., 2] = sign * env
    omega *= lat.mask_active[..., None]
    return omega


def chiral_z_local_from_seed(
    R: float, r: float, peak_amp: float, chi: float, handedness: str = HANDEDNESS
) -> np.ndarray:
    """THE CHIRAL DRESSING (the swap from Test 3). Build the chiral Cosserat omega
    field + the K4 V-tank (2,3) seed, then compute the ASYMMETRIC (S_mu, S_eps)
    saturation kernels via the engine's canonical _update_saturation_kernels and
    form the frozen impedance landscape

        z_local = sqrt(S_mu / S_eps)          (Z_eff/Z_0, Vol 1 Ch 7:252, doc 54_:194)

    where (per doc 54_:167,218-220)
        A2_mu  = (1 + chi*h_local) * kappa^2/omega_yield^2
        A2_eps = (1 - chi*h_local) * (eps_sym^2/eps_yield^2 + V^2/V_SNAP^2)
        h_local = omega.(curl omega)/(|omega||curl omega|)   (Cosserat-omega helicity)

    This is the EXACT CoupledK4Cosserat._update_z_local_total computation
    (k4_cosserat_coupling.py:379-393), evaluated on the (chiral omega, V) seed and
    FROZEN to linearize the K4 step about it. Contrast Test 3, which read the plain
    K4 |V| magnitude via K4Lattice3D._update_z_local_field -- magnitude-symmetric,
    chirality-blind, aspect-invariant.

    chi IS the chiral coupling strength under test (chi=1.2*alpha physically; SWEPT
    here). This is the ONE function permitted to CONSUME the chiral coupling as a
    value -- it is the physics under test, NOT a measure. (Excluded from both
    _MEASURE_FUNCS and _ORCHESTRATION_FUNCS; the self-audit asserts the chiral token
    appears HERE and in no geometry/winding measure.)

    Returns the frozen z_local_field (nx, ny, nz).

    ENGINE-REALITY FLAG (surfaced at scaffold-time, flag-don't-fix): chi=0 does NOT
    give z_local==1. The two base saturations A2_mu_base = kappa^2/omega_yield^2
    (magnetic, from Cosserat omega curvature) and A2_eps_base = eps_sym^2/eps_yield^2
    + V^2/V_SNAP^2 (electric, from strain + K4 voltage) are DIFFERENT MAGNITUDES on
    the seed (measured: A2_eps_base ~ 8x A2_mu_base because the K4 V^2 drive loads the
    electric sector harder than the rotational seed loads the magnetic one), so
    S_mu != S_eps and Z_eff = sqrt(S_mu/S_eps) != 1 even with NO chiral bias. The
    chiral coupling chi*h_local TILTS an ALREADY-asymmetric base; it does not create
    the asymmetry from a symmetric baseline. Consequence: the chi=0 dressed arm is
    NOT a clean achiral control -- it carries a baseline aspect-tilt from the seed
    structure. THE clean achiral control is the BARE arm (op3=False, Gamma=0
    everywhere), which Test 3 confirmed is flat. The chi-sweep therefore measures the
    chiral coupling's INCREMENT on top of the chi=0 (base-asymmetry) reference, and
    the adjudication baselines against the BARE arm. (doc 54_:197 "symmetric case"
    means A2_mu==A2_eps, which requires the magnetic and electric DRIVES to match --
    not automatic for a (2,3) hedgehog + V seed.)
    """
    lat = _build_lattice(op3=True)
    seed_generic_2_3_vtank(lat, R, r, peak_amp)
    omega = seed_chiral_cosserat_omega(R, r, peak_amp, handedness=handedness)
    u = np.zeros_like(omega)  # no translational strain seed; magnetic/electric from omega + V
    V_sq = np.sum(lat.V_inc**2, axis=-1)

    # Engine-canonical chiral (S_mu, S_eps) split. omega_yield = pi, eps_yield = 1
    # are the engine's alpha-free confinement scales (CosseratField3D defaults);
    # read them from a fresh field instance so no scale is hard-coded here.
    from ave.topological.cosserat_field_3d import CosseratField3D

    _cf = CosseratField3D(nx=2, ny=2, nz=2, dx=1.0)
    omega_yield = float(_cf.omega_yield)
    epsilon_yield = float(_cf.epsilon_yield)
    v_snap = float(lat.V_SNAP)  # = 1.0 (natural units); the engine kernel needs it

    S_mu, S_eps = _update_saturation_kernels(
        jnp.asarray(u),
        jnp.asarray(omega),
        jnp.asarray(V_sq),
        float(lat.dx),
        v_snap,
        omega_yield,
        epsilon_yield,
        float(chi),
    )
    S_mu_np = np.asarray(S_mu)
    S_eps_np = np.asarray(S_eps)
    z_local = np.sqrt(np.maximum(S_mu_np, 1e-12) / np.maximum(S_eps_np, 1e-12))
    z_local = np.where(lat.mask_active, z_local, 1.0)
    return z_local.astype(np.float64)


def build_step_operator(R: float, r: float, peak_amp: float, dressed: bool, chi: float, handedness: str = HANDEDNESS):
    """Return (sparse_matrix, lattice_template) for the one-tick K4 step map
    V_inc(t) -> V_inc(t+1), assembled EXPLICITLY as a sparse matrix on the
    active-site V_inc state (Test-3 strided-batch assembly, validated there).

    The step is a LOCAL linear map (connect couples only nearest K4 neighbors),
    so the matrix is sparse. An explicit matrix lets scipy do a sparse-LU complex
    shift-invert at exp(i*theta_C) -- the AC band, NOT the theta=0 DC trap.

    BARE   (dressed=False): op3 off -> pure unitary scatter+connect, Gamma=0.
                            The achiral control; flat by construction.
    DRESSED(dressed=True):  op3 on, z_local FROZEN at the CHIRAL sqrt(S_mu/S_eps)
                            landscape (chiral_z_local_from_seed) -> chirality-biased
                            bond reflection Gamma. The R != r symmetry-breaker.

    NO forbidden token enters: built from lattice geometry + the engine's chiral
    saturation kernel only. The chiral coupling chi enters ONLY via the dressing
    builder (chiral_z_local_from_seed)."""
    from scipy.sparse import csc_matrix

    template = _build_lattice(op3=dressed)
    active = template.mask_active
    n_active = int(active.sum())
    dim = n_active * 4

    # BARE operator is (R, r, chi)-INDEPENDENT -- assemble once and cache.
    if not dressed:
        cache_key = (N_LATTICE, PML)
        cached = _BARE_MATRIX_CACHE.get(cache_key)
        if cached is not None:
            return cached, template

    z_frozen = chiral_z_local_from_seed(R, r, peak_amp, chi, handedness=handedness) if dressed else None

    lat = _build_lattice(op3=dressed)
    if dressed:
        lat._update_z_local_field = (  # type: ignore[method-assign]
            lambda zf=z_frozen: setattr(lat, "z_local_field", zf.copy())
        )

    flat_idx = np.argwhere(active)
    col_of = -np.ones((template.nx, template.ny, template.nz, 4), dtype=np.int64)
    for s, (ii, jj, kk) in enumerate(flat_idx):
        for port in range(4):
            col_of[ii, jj, kk, port] = 4 * s + port

    # STRIDED-BATCH assembly (Test-3 validated): impulses >= STRIDE cells apart on
    # every axis have DISJOINT output supports -> one step() harvests them as
    # separate columns. STRIDE=4 (connect rolls by 1).
    STRIDE = 4
    cols = np.zeros((dim, dim), dtype=float)
    for port in range(4):
        for ox in range(STRIDE):
            for oy in range(STRIDE):
                for oz in range(STRIDE):
                    lat.V_inc[:] = 0.0
                    lat.V_ref[:] = 0.0
                    sub = np.zeros((template.nx, template.ny, template.nz), dtype=bool)
                    sub[ox::STRIDE, oy::STRIDE, oz::STRIDE] = True
                    src = active & sub
                    lat.V_inc[src, port] = 1.0
                    if dressed:
                        lat.z_local_field = z_frozen.copy()
                    lat.step()
                    out = lat.V_inc
                    src_sites = np.argwhere(src)
                    for ii, jj, kk in src_sites:
                        c = col_of[ii, jj, kk, port]
                        if c < 0:
                            continue
                        col_field = np.zeros_like(out)
                        i0, i1 = max(ii - 1, 0), min(ii + 2, template.nx)
                        j0, j1 = max(jj - 1, 0), min(jj + 2, template.ny)
                        k0, k1 = max(kk - 1, 0), min(kk + 2, template.nz)
                        col_field[i0:i1, j0:j1, k0:k1] = out[i0:i1, j0:j1, k0:k1]
                        cols[:, c] = col_field[active].reshape(-1)
    M = csc_matrix(cols)
    if not dressed:
        _BARE_MATRIX_CACHE[(N_LATTICE, PML)] = M
    return M, template


def eig_near_thetaC(M, n_eigs: int = N_EIGS):
    """Eigenpairs of the one-tick step matrix nearest eigenphase theta_C on the
    unit circle (theta ~ 1/sqrt(2), the AC ringing band, NOT the theta=0 DC trap).
    Complex shift sigma = exp(i*theta_C) via sparse LU. Returns (eigvals, eigvecs).

    DETERMINISM (surfaced at scaffold-time): ARPACK seeds its Arnoldi iteration with
    a RANDOM start vector v0 by default. Because the V-sector band near theta_C is
    ~40-fold near-degenerate (|lambda| all ~0.926 at theta~theta_C), a random v0
    returns a DIFFERENT basis WITHIN the degenerate cluster each call -- so the
    most-bound representative's V-tank R/r wobbles by ~0.05 between identical
    eigensolves. That noise would contaminate the chi-sweep's chiral-INCREMENT
    (R/r at physical chi MINUS R/r at chi=0) if the two used different v0. We PIN a
    deterministic v0 (all-ones, RNG_SEED-perturbed) so every eigensolve on a given
    matrix is reproducible and the increment isolates the chiral effect, not ARPACK
    noise. (The pinned v0 is a numerical-solver seed, NOT a physics input -- no
    alpha / phi; it only fixes which representative of a degenerate cluster is
    returned, identically for every arm.)"""
    from scipy.sparse.linalg import eigs

    sigma = np.exp(1j * THETA_C)
    k = min(n_eigs, M.shape[0] - 2)
    rng = np.random.default_rng(RNG_SEED)
    v0 = np.ones(M.shape[0], dtype=complex) + 1e-3 * rng.standard_normal(M.shape[0])
    vals, vecs = eigs(M, k=k, sigma=sigma, which="LM", maxiter=4000, tol=1e-9, v0=v0)
    return vals, vecs


# ======================================================================
# SECTION 4 -- V-tank phase-space measures ((p,q), R/r ASPECT) on an eigenvector
# ======================================================================
def _interior_mask(lat: K4Lattice3D) -> np.ndarray:
    """Active sites strictly inside the PML collar (Rule 10 corollary). PML cells
    carry frozen-absorbing artifact, not interior physics -- excluded."""
    i, j, k = lat._i, lat._j, lat._k
    p = lat.pml_thickness
    d = np.minimum.reduce(
        [
            np.minimum(i, lat.nx - 1 - i),
            np.minimum(j, lat.ny - 1 - j),
            np.minimum(k, lat.nz - 1 - k),
        ]
    )
    return lat.mask_active & (d >= p)


def _eigvec_to_fields(eigvec: np.ndarray, template: K4Lattice3D):
    """Map a COMPLEX step-operator eigenvector to the corpus (V_inc, V_ref) phase-
    space quadrature pair (doc 28_:64-67; doc 68_:189-194). For a standing
    eigenmode V(t) = Re(psi e^{i omega t}), the (V_inc, V_ref) quadrature pair over
    one cycle is exactly (Re psi, Im psi). Returns (V_inc_field, V_ref_field) as
    REAL arrays. (Identical to Test 3's doc-68 coordinate fix.)"""
    active = template.mask_active
    n_active = int(active.sum())
    psi = np.zeros((template.nx, template.ny, template.nz, 4), dtype=complex)
    psi[active] = eigvec.reshape(n_active, 4)
    V_inc = np.real(psi)
    V_ref = np.imag(psi)
    V_inc[~active] = 0.0
    V_ref[~active] = 0.0
    return V_inc, V_ref


def measure_eigvec_localization(eigvec: np.ndarray, template: K4Lattice3D) -> dict:
    """Threshold-free localization of an eigenvector's |psi|^2 density, interior-
    only (PML excluded). Reports the inverse participation ratio N_eff and the
    interior energy fraction (1 - leaked-to-PML). No alpha / charge."""
    interior = _interior_mask(template)
    V_inc, V_ref = _eigvec_to_fields(eigvec, template)
    rho_full = np.sum(V_inc**2 + V_ref**2, axis=-1)
    rho = rho_full[interior].astype(np.float64)
    s1 = float(rho.sum())
    s2 = float((rho**2).sum())
    total_all = float(rho_full[template.mask_active].sum())
    interior_frac = (s1 / total_all) if total_all > 0 else 0.0
    n_eff = (s1 * s1 / s2) if s2 > 0 else 0.0
    n_interior = int(interior.sum())
    return {
        "n_eff": float(n_eff),
        "n_interior_cells": n_interior,
        "localization": float(1.0 - n_eff / max(n_interior, 1)),
        "interior_energy_frac": float(interior_frac),
    }


def _port_chirality_weights(template, xs, ys, zs, R, r):
    """Geometric port-chirality projection chir_p = p_hat . t_hat(2,3) at the
    contour points -- pure geometry (same projection the seeder uses), no alpha /
    charge / phi. Weights the per-port phasor so the cross-port sum does NOT cancel
    (Sum_p chir_p = 0 but Sum_p chir_p^2 > 0)."""
    cx, cy, cz = (template.nx - 1) / 2.0, (template.ny - 1) / 2.0, (template.nz - 1) / 2.0
    x, y, z = xs - cx, ys - cy, zs - cz
    rho_xy = np.sqrt(x**2 + y**2 + 1e-12)
    phi = np.arctan2(y, x)
    psi = np.arctan2(z, rho_xy - R)
    dphi_x = -(R + r * np.cos(psi)) * np.sin(phi)
    dphi_y = (R + r * np.cos(psi)) * np.cos(phi)
    dpsi_x = -r * np.sin(psi) * np.cos(phi)
    dpsi_y = -r * np.sin(psi) * np.sin(phi)
    dpsi_z = r * np.cos(psi)
    tx = 2.0 * dphi_x + 3.0 * dpsi_x
    ty = 2.0 * dphi_y + 3.0 * dpsi_y
    tz = 3.0 * dpsi_z
    tmag = np.sqrt(tx**2 + ty**2 + tz**2 + 1e-12)
    thx, thy, thz = tx / tmag, ty / tmag, tz / tmag
    ports = [(+1.0, +1.0, +1.0), (+1.0, -1.0, -1.0), (-1.0, +1.0, -1.0), (-1.0, -1.0, +1.0)]
    inv_sqrt3 = 1.0 / np.sqrt(3.0)
    return [inv_sqrt3 * (px * thx + py * thy + pz * thz) for (px, py, pz) in ports]


def _phasor_contour_winding(V_inc, V_ref, template, R_major, r_minor, direction, n=128, R=None, r=None):
    """Signed winding of the K4 V-tank (V_inc, V_ref) PHASE-SPACE phasor along a
    toroidal ('p') or poloidal ('q') contour (corpus coordinate, doc 28_:64-67).
    Chirality-weighted cross-port sum + trilinear interp onto the bipartite lattice
    (Test-3 measure-bug fixes). Returns (signed_winding, reliability). Pure geometry
    -- no alpha / phi."""
    nx, ny, nz = template.nx, template.ny, template.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0
    s = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    if direction == "toroidal":
        rho = R_major + r_minor
        xs, ys, zs = cx + rho * np.cos(s), cy + rho * np.sin(s), cz + np.zeros_like(s)
    else:
        xs = cx + (R_major + r_minor * np.cos(s))
        ys = cy + np.zeros_like(s)
        zs = cz + r_minor * np.sin(s)
    ix = np.clip(xs.astype(int), 0, nx - 2)
    iy = np.clip(ys.astype(int), 0, ny - 2)
    iz = np.clip(zs.astype(int), 0, nz - 2)
    fx, fy, fz = xs - ix, ys - iy, zs - iz

    def _tri(field):
        return (
            (1 - fx) * (1 - fy) * (1 - fz) * field[ix, iy, iz]
            + fx * (1 - fy) * (1 - fz) * field[ix + 1, iy, iz]
            + (1 - fx) * fy * (1 - fz) * field[ix, iy + 1, iz]
            + (1 - fx) * (1 - fy) * fz * field[ix, iy, iz + 1]
            + fx * fy * (1 - fz) * field[ix + 1, iy + 1, iz]
            + fx * (1 - fy) * fz * field[ix + 1, iy, iz + 1]
            + (1 - fx) * fy * fz * field[ix, iy + 1, iz + 1]
            + fx * fy * fz * field[ix + 1, iy + 1, iz + 1]
        )

    R_g = R if R is not None else R_major
    r_g = r if r is not None else max(r_minor, 1.0)
    chir = _port_chirality_weights(template, xs, ys, zs, R_g, r_g)
    Z = np.zeros(n, dtype=complex)
    for p in range(4):
        Zp = _tri(V_inc[..., p]) + 1j * _tri(V_ref[..., p])
        Z = Z + chir[p] * Zp
    amp = np.abs(Z)
    amax = float(amp.max())
    if amax <= 0:
        return 0.0, 0.0
    reliability = float(amp.min() / amax)
    if reliability < 0.02:
        return 0.0, reliability
    phase = np.unwrap(np.angle(Z))
    total = (phase[-1] - phase[0]) / (2.0 * np.pi)
    return float(total), reliability


def measure_vtank_winding_pq(eigvec: np.ndarray, template: K4Lattice3D, R_major: float) -> dict:
    """Read the (p, q) winding of the eigenmode in the K4 V-tank (V_inc, V_ref)
    PHASE-SPACE (A46 coordinate). p = toroidal (major), q = poloidal (minor). No
    alpha / charge / phi. (Identical to Test 3.)"""
    V_inc, V_ref = _eigvec_to_fields(eigvec, template)
    best_p = (0.0, 0.0)
    best_q = (0.0, 0.0)
    for r_minor in np.linspace(1.0, max(2.0, R_major * 0.6), 6):
        pw, pa = _phasor_contour_winding(V_inc, V_ref, template, R_major, r_minor, "toroidal", R=R_major, r=r_minor)
        qw, qa = _phasor_contour_winding(V_inc, V_ref, template, R_major, r_minor, "poloidal", R=R_major, r=r_minor)
        if pa > best_p[1]:
            best_p = (pw, pa)
        if qa > best_q[1]:
            best_q = (qw, qa)
    p = int(round(abs(best_p[0])))
    q = int(round(abs(best_q[0])))
    return {
        "p_major_winding": p,
        "q_minor_winding": q,
        "p_reliability": float(best_p[1]),
        "q_reliability": float(best_q[1]),
        "is_2_3": bool(p == 2 and q == 3),
    }


def measure_vtank_aspect_phase_space(eigvec: np.ndarray, template: K4Lattice3D) -> dict:
    """PRIMARY MEASURE (Test 4, CHANGED from Test 3): the ASPECT RATIO R/r in the
    K4 V-tank (V_inc, V_ref) phasor plane -- NOT real-space, NOT Cosserat (u,omega).
    The corpus claim (doc 28_:72,85) is phase-space R_phase/r_phase = phi^2.

    Test 3 measured R*r (the PRODUCT -- chirality-INVARIANT under the R<->r flip
    that the chiral coupling breaks, so it was flat). Test 4 measures R/r (the
    ASPECT -- chirality-DEPENDENT) because ONLY a chirality-breaking perturbation
    can select it, and the CHIRAL dressing is exactly that.

    At each interior site the eigenmode parks on a (V_inc, V_ref) phasor; over the
    shell these trace a torus in the 2D phase-space. Geometry:
      R_phase = energy-weighted radius of the phasor locus from the origin
      r_phase = energy-weighted RMS swing about that radius
      R/r_phase = R_phase / r_phase   <-- the ASPECT (corpus phi^2 target)
    Each axis is normalized to its weighted RMS so the plane is dimensionless
    reactance (matching the dimensionless corpus R/r claim). No alpha / phi enters:
    the read-out is purely the eigenvector's (Re, Im) phasor geometry; 'phi' below
    is only a comment/variable name, never the constant. The AST guard scans
    identifiers used as values; V_inc/V_ref are engine arrays, not forbidden tokens.

    Reported FORWARD: whatever R/r comes out, per (R, r) and per chi. The
    discriminator is whether the DRESSED R/r develops a phi^2-selecting extremum vs
    the achiral (chi=0) flatness, and whether that phi^2 is set across chi (topology,
    alpha-free) or only at the physical chi=1.2*alpha (circular).
    """
    interior = _interior_mask(template)
    V_inc, V_ref = _eigvec_to_fields(eigvec, template)
    a = np.sqrt(np.sum(V_inc**2, axis=-1))[interior]  # incident-axis content
    b = np.sqrt(np.sum(V_ref**2, axis=-1))[interior]  # reflected-axis content
    weight = a**2 + b**2
    wsum = float(weight.sum())
    if wsum < 1e-30:
        return {"R_phase": 0.0, "r_phase": 0.0, "R_over_r_phase": 0.0, "R_times_r_phase": 0.0, "n_active_sites": 0}
    a_rms = np.sqrt(float(np.sum(weight * a**2) / wsum)) or 1.0
    b_rms = np.sqrt(float(np.sum(weight * b**2) / wsum)) or 1.0
    an, bn = a / a_rms, b / b_rms
    radius = np.sqrt(an**2 + bn**2)
    R_phase = float(np.sum(weight * radius) / wsum)
    var = float(np.sum(weight * (radius - R_phase) ** 2) / wsum)
    r_phase = float(np.sqrt(max(var, 0.0)))
    return {
        "R_phase": R_phase,
        "r_phase": r_phase,
        "R_over_r_phase": R_phase / max(r_phase, 1e-12),  # THE ASPECT (Test 4 primary)
        "R_times_r_phase": R_phase * r_phase,  # the product (Test-3 quantity; carried for cross-check)
        "n_active_sites": int((weight > 1e-12 * weight.max()).sum()),
    }


def _pack_live_as_eigvec(V_inc_live: np.ndarray, V_ref_live: np.ndarray, template_like) -> np.ndarray:
    """Pack a live (V_inc, V_ref) field pair into a COMPLEX 'eigvec' (V_inc +
    i*V_ref) so the eigenvector measures apply to a directly-seeded field (used by
    the seed-validity control). No alpha / charge / phi."""
    active = template_like.mask_active
    psi = V_inc_live[active].reshape(-1) + 1j * V_ref_live[active].reshape(-1)
    return psi.astype(complex)


# ======================================================================
# SECTION 5 -- PRONG 1: bare-vs-chiral-dressed (R, r) landscape + chi-sweep
# ======================================================================
THETA_WINDOW = 0.05  # |theta - theta_C| band defining the AC ringing modes.


def _mode_record(idx, vecs, template, R_major, mods, phases) -> dict:
    """Full per-mode record: binding signature + V-tank (p,q) + R/r ASPECT + R*r."""
    loc = measure_eigvec_localization(vecs[:, idx], template)
    pq = measure_vtank_winding_pq(vecs[:, idx], template, R_major=R_major)
    asp = measure_vtank_aspect_phase_space(vecs[:, idx], template)
    return {
        "idx": int(idx),
        "lambda_mod": float(mods[idx]),
        "theta": float(phases[idx]),
        "binding_score": float(loc["localization"] * mods[idx]),
        "localization": float(loc["localization"]),
        "n_eff": float(loc["n_eff"]),
        "interior_energy_frac": float(loc["interior_energy_frac"]),
        "p_major": int(pq["p_major_winding"]),
        "q_minor": int(pq["q_minor_winding"]),
        "p_reliability": float(pq["p_reliability"]),
        "q_reliability": float(pq["q_reliability"]),
        "is_2_3": bool(pq["is_2_3"]),
        "R_over_r_phase": float(asp["R_over_r_phase"]),  # THE ASPECT (Test 4 primary)
        "Rr_phase": float(asp["R_times_r_phase"]),  # product (cross-check vs Test 3)
    }


def _select_modes(vals, vecs, template, R_major):
    """Among eigenpairs within THETA_WINDOW of theta_C (AC band, NOT theta=0 DC),
    return TWO mode records (non-question-begging):
      'most_bound' -- maximizes localization*|lambda|.
      'best_2_3'   -- closest V-tank (p,q) to (2,3) (the topological selector).
    Reporting both avoids selecting-for-the-answer."""
    phases = np.abs(np.angle(vals))
    mods = np.abs(vals)
    in_band = np.where(np.abs(phases - THETA_C) <= THETA_WINDOW)[0]
    if in_band.size == 0:
        return {"most_bound": None, "best_2_3": None, "n_in_band": 0}
    recs = [_mode_record(idx, vecs, template, R_major, mods, phases) for idx in in_band]
    most_bound = max(recs, key=lambda rr: rr["binding_score"])
    best_2_3 = min(
        recs,
        key=lambda rr: (abs(rr["p_major"] - 2) + abs(rr["q_minor"] - 3), -(rr["p_reliability"] + rr["q_reliability"])),
    )
    return {"most_bound": most_bound, "best_2_3": best_2_3, "n_in_band": int(in_band.size)}


def prong1_chiral_landscape(
    peak_amp: float, chi: float, handedness: str = HANDEDNESS, verbose: bool = True, ratios=None
) -> dict:
    """Sweep the generic (R, r) hedgehog family; for each, eigensolve the BARE
    (achiral) and CHIRAL-DRESSED K4 V-sector step operators near theta_C, select the
    bound mode, and record its V-tank (p,q) + R/r ASPECT.

    The LIFT question (Test 4): does the chiral-dressed eigenmode's R/r develop an
    extremum -> phi^2 in V-tank coordinates that the BARE (achiral, Gamma=0) flat
    landscape lacks? Run at a given chi. No forbidden token enters; chi is confined
    to the dressing builder.

    ratios: optional subset of R/r ratios (default = full R_OVER_r_SWEEP). The
    handedness-flip control passes a SUBSET to keep its runtime bounded -- it only
    needs to confirm whether the aspect deviation flips sign with handedness, which
    a representative subset establishes (the full grid is run at the primary
    handedness)."""
    use_ratios = R_OVER_r_SWEEP if ratios is None else tuple(ratios)
    grid = []
    for R in R_MAJOR_SWEEP:
        for ratio in use_ratios:
            r = R / ratio
            row: dict = {"R": float(R), "r": float(r), "R_over_r_real": float(ratio), "chi": float(chi)}
            for arm, dressed in (("bare", False), ("dressed", True)):
                M, template = build_step_operator(R, r, peak_amp, dressed, chi, handedness=handedness)
                vals, vecs = eig_near_thetaC(M, n_eigs=N_EIGS)
                sel = _select_modes(vals, vecs, template, R_major=R)
                row[arm] = {
                    "in_band": sel["n_in_band"] > 0,
                    "n_in_band": sel["n_in_band"],
                    "most_bound": sel["most_bound"],
                    "best_2_3": sel["best_2_3"],
                }
            grid.append(row)
            if verbose:
                b = row["bare"]["most_bound"]
                d = row["dressed"]["most_bound"]
                d23 = row["dressed"]["best_2_3"]
                bb = f"R/r_ph={b['R_over_r_phase']:.3f}" if b else "OUT-OF-BAND"
                dd = f"loc={d['localization']:.4f} R/r_ph={d['R_over_r_phase']:.3f}" if d else "OUT-OF-BAND"
                t23 = f"(p,q)=({d23['p_major']},{d23['q_minor']}) R/r_ph={d23['R_over_r_phase']:.3f}" if d23 else "-"
                print(
                    f"  R={R:.1f} r={r:.2f} (R/r_seed={ratio:.1f}): BARE[{bb}]  "
                    f"DRESSED-bound[{dd}]  DRESSED-(2,3)[{t23}]",
                    flush=True,
                )
    return {"grid": grid, "theta_C": THETA_C, "theta_window": THETA_WINDOW, "chi": float(chi)}


def _aspect_landscape_stats(grid: list, arm: str, mode_key: str = "most_bound") -> dict:
    """Aspect-ratio (R/r) landscape statistics across (R, r) for one arm. Reports
    the MEAN selected R/r, its spread, and how close the mean sits to phi^2 = 2.618
    -- WITHOUT importing phi (the comparison constant 2.618 is the read-side target;
    the measure itself imported no phi). Flat-at-1 = no aspect selection; a tight
    cluster at ~2.618 = the phi^2 selection. mode_key: 'most_bound' or 'best_2_3'."""
    aspects, locs = [], []
    for row in grid:
        rec = row.get(arm, {}).get(mode_key)
        if rec is None:
            continue
        aspects.append(rec["R_over_r_phase"])
        locs.append(rec["localization"])
    if not aspects:
        return {"n_points": 0}
    aspects = np.asarray(aspects)
    locs = np.asarray(locs)
    return {
        "n_points": int(aspects.size),
        "aspect_mean": float(aspects.mean()),
        "aspect_median": float(np.median(aspects)),
        "aspect_std": float(aspects.std()),
        "aspect_min": float(aspects.min()),
        "aspect_max": float(aspects.max()),
        "loc_mean": float(locs.mean()),
        "loc_rel_spread": float((locs.max() - locs.min()) / max(abs(locs.mean()), 1e-12)),
    }


def chi_sweep_aspect(peak_amp: float, R: float, r: float, handedness: str = HANDEDNESS, verbose: bool = True) -> dict:
    """THE crux measurement: sweep the chiral coupling strength chi at a fixed
    generic (R, r) seed and record the chiral-dressed eigenmode's selected R/r
    ASPECT for each chi. Resolves the alpha-FREE / magnitude discriminator:

      (A) R/r -> phi^2 set by the (2,3) TOPOLOGY: phi^2 appears as a PLATEAU across
          a range of chi (alpha only the overall scale) -> alpha-FREE, lift lands.
      (B) R/r = phi^2 ONLY at the physical chi=1.2*alpha: a single crossing, no
          plateau -> circular.
      (FLAT/SMALL) R/r stays ~1 (or grows only ~ 1 + O(chi)) and never reaches
          phi^2 at the physical chi: the asymmetry is O(alpha)-small -> close.

    chi=0 is the chiral-coupling-OFF reference (but NOT a symmetric-impedance
    control -- see chiral_z_local_from_seed's ENGINE-REALITY FLAG: a base mu/eps
    asymmetry persists at chi=0 because the magnetic and electric drives differ on
    the seed). The clean achiral control is the BARE arm (bare_aspect, computed
    here once). The physical chi = KAPPA_CHIRAL_ELECTRON is asserted present in the
    sweep. Forward, not fit."""
    sweep = []
    bare_aspect = None
    # Achiral baseline once (chi-independent): the BARE R/r at this (R, r).
    Mb, tb = build_step_operator(R, r, peak_amp, dressed=False, chi=0.0, handedness=handedness)
    vb, ev_b = eig_near_thetaC(Mb, n_eigs=N_EIGS)
    selb = _select_modes(vb, ev_b, tb, R_major=R)
    if selb["most_bound"] is not None:
        bare_aspect = float(selb["most_bound"]["R_over_r_phase"])
    for chi in CHI_SWEEP:
        M, template = build_step_operator(R, r, peak_amp, dressed=True, chi=chi, handedness=handedness)
        vals, vecs = eig_near_thetaC(M, n_eigs=N_EIGS)
        sel = _select_modes(vals, vecs, template, R_major=R)
        d = sel["most_bound"]
        d23 = sel["best_2_3"]
        rec = {
            "chi": float(chi),
            "is_physical_chi": bool(abs(chi - KAPPA_CHIRAL_ELECTRON) < 1e-9),
            "R_over_r_phase_bound": float(d["R_over_r_phase"]) if d else None,
            "R_over_r_phase_2_3": float(d23["R_over_r_phase"]) if d23 else None,
            "localization_bound": float(d["localization"]) if d else None,
            "pq_2_3": (int(d23["p_major"]), int(d23["q_minor"])) if d23 else None,
            "n_in_band": int(sel["n_in_band"]),
        }
        sweep.append(rec)
        if verbose:
            ar = f"{rec['R_over_r_phase_bound']:.4f}" if rec["R_over_r_phase_bound"] is not None else "OOB"
            ar23 = f"{rec['R_over_r_phase_2_3']:.4f}" if rec["R_over_r_phase_2_3"] is not None else "OOB"
            tag = "  <-- PHYSICAL chi=1.2*alpha" if rec["is_physical_chi"] else ""
            print(f"    chi={chi:.6f}: R/r_bound={ar}  R/r_(2,3)={ar23}{tag}", flush=True)
    return {"R": float(R), "r": float(r), "bare_aspect": bare_aspect, "sweep": sweep}


# ======================================================================
# SECTION 6 -- adjudication (A / B / C / FLAT) + main
# ======================================================================
# phi^2 = 2.618... is the corpus aspect target (doc 28_:72). We compare the
# MEASURED R/r against it on the READ side. We do NOT import PHI: the literal 2.618
# below is the read-side comparison target, never fed into any seed or measure.
# (The AST guard forbids PHI/R_GOLDEN_TORUS only in the guarded MEASURES; this
# adjudicate function compares the already-measured R/r to a numeric target, which
# is the honest forward comparison, not a smuggled input.)
PHI_SQ_TARGET = 2.6180339887  # = ((1+sqrt5)/2)^2; read-side comparison constant ONLY.
ASPECT_BAND = 0.20  # +/- fractional band around phi^2 counted as "selects phi^2".


def adjudicate(land_phys: dict, chi_sweeps: list, hand_flip: dict | None) -> dict:
    """Map the chiral-dressed aspect landscape + chi-sweep to A / B / C / FLAT.

    Reads (forward-not-fit):
      - At the PHYSICAL chi (=1.2*alpha): does the dressed R/r cluster near phi^2,
        vs the achiral (BARE) baseline that does not select an aspect?
      - Across the chi-SWEEP: is R/r -> phi^2 a PLATEAU spanning multiple chi
        (topology-set, alpha-FREE) or only a single crossing at chi=1.2*alpha
        (circular)? Or does R/r stay ~1 / grow only O(chi), never reaching phi^2
        at the physical chi (FLAT/SMALL)?

    A:    DRESSED selects R/r ~ phi^2 from generic seeds AND the chi-sweep shows a
          phi^2 PLATEAU across coupling strengths (alpha-free, topology-set).
    B:    R/r ~ phi^2 appears ONLY at chi=1.2*alpha (no plateau; single crossing).
    C:    DRESSED lifts the aspect (R/r != bare, develops structure) but selects a
          DIFFERENT ratio, not phi^2.
    FLAT/SMALL: physical chi gives R/r ~ achiral baseline (~1) or only O(chi)-small
          asymmetry, never reaching phi^2 -> the chiral coupling does not select
          phi^2 at its physical strength -> the lift closes (honest negative).
    """
    grid = land_phys["grid"]
    bare = _aspect_landscape_stats(grid, "bare", "most_bound")
    dressed = _aspect_landscape_stats(grid, "dressed", "most_bound")
    dressed_23 = _aspect_landscape_stats(grid, "dressed", "best_2_3")

    if bare.get("n_points", 0) == 0 or dressed.get("n_points", 0) == 0:
        return {
            "outcome": "INCONCLUSIVE",
            "reason": "No eigenmode fell in the AC band for one or both arms -- the V-sector "
            "has no ringing mode near omega_C at this lattice/seed. Cannot adjudicate.",
            "bare": bare,
            "dressed": dressed,
            "dressed_2_3": dressed_23,
        }

    # The full op3 DRESSING effect (BARE vs DRESSED at physical chi). NOTE this
    # conflates TWO effects: (a) the base mu/eps asymmetry present even at chi=0
    # (op3 on, no chiral bias) and (b) the chiral coupling's increment. For the
    # CHIRAL claim specifically, the load-bearing number is the chiral INCREMENT
    # (b) alone -- computed below from the chi-sweep (R/r at physical chi MINUS R/r
    # at chi=0). The BARE-vs-DRESSED shift is reported for context but is NOT the
    # chiral discriminator.
    bare_aspect_mean = bare["aspect_mean"]
    dressed_aspect_mean = dressed["aspect_mean"]
    aspect_shift = abs(dressed_aspect_mean - bare_aspect_mean)

    # CHIRAL INCREMENT (the clean discriminator): how far does the chiral coupling
    # MOVE R/r as chi goes 0 -> physical, isolating effect (b) from the base
    # asymmetry (a)? Averaged across chi-sweep seeds, on the (2,3) topological mode
    # (falling back to the bound mode). This is what the brief's chi=1.2*alpha
    # question actually asks: does the CHIRAL coupling, at its physical strength,
    # move the aspect appreciably (toward phi^2) -- or is it O(alpha)-small?
    chiral_increments = []
    for cs in chi_sweeps:
        val0 = None
        valp = None
        for rec in cs["sweep"]:
            v = rec.get("R_over_r_phase_2_3") or rec.get("R_over_r_phase_bound")
            if v is None:
                continue
            if abs(rec["chi"]) < 1e-15:
                val0 = v
            if rec["is_physical_chi"]:
                valp = v
        if val0 is not None and valp is not None:
            chiral_increments.append(valp - val0)
    chiral_increment_mean = float(np.mean(chiral_increments)) if chiral_increments else float("nan")

    # selects_aspect (chiral): does the chiral coupling at physical strength move the
    # aspect by a non-negligible fraction toward phi^2? Threshold 5% of phi^2 (~0.13)
    # -- an aspect-selection worth the name should move R/r by at least that to
    # approach phi^2=2.618 from a generic ~2 seed. (O(alpha)~0.009 increments are far
    # below this -> FLAT/SMALL.)
    selects_aspect = bool(
        np.isfinite(chiral_increment_mean) and abs(chiral_increment_mean) > 0.05 * PHI_SQ_TARGET
    )

    # Does the dressed aspect (most-bound + (2,3)-selected) land near phi^2?
    near_phi2_bound = abs(dressed_aspect_mean - PHI_SQ_TARGET) <= ASPECT_BAND * PHI_SQ_TARGET
    near_phi2_23 = (
        dressed_23.get("n_points", 0) > 0
        and abs(dressed_23["aspect_mean"] - PHI_SQ_TARGET) <= ASPECT_BAND * PHI_SQ_TARGET
    )
    near_phi2 = near_phi2_bound or near_phi2_23

    # --- chi-sweep topology-vs-alpha-injected resolution (THE crux) ---
    # For each chi-sweep seed, find where R/r crosses into the phi^2 band and whether
    # a PLATEAU exists (multiple consecutive chi values within the band, spanning a
    # decade of coupling). Aggregate across seeds.
    plateau_seeds = 0
    physical_in_band_seeds = 0
    physical_aspect_vals = []
    for cs in chi_sweeps:
        in_band_chi = []
        phys_val = None
        for rec in cs["sweep"]:
            val = rec.get("R_over_r_phase_2_3") or rec.get("R_over_r_phase_bound")
            if val is None:
                continue
            if abs(val - PHI_SQ_TARGET) <= ASPECT_BAND * PHI_SQ_TARGET:
                in_band_chi.append(rec["chi"])
            if rec["is_physical_chi"]:
                phys_val = val
        if phys_val is not None:
            physical_aspect_vals.append(phys_val)
            if abs(phys_val - PHI_SQ_TARGET) <= ASPECT_BAND * PHI_SQ_TARGET:
                physical_in_band_seeds += 1
        # PLATEAU: >= 3 distinct chi in-band AND spanning >= 1 order of magnitude.
        if len(in_band_chi) >= 3:
            nz = [c for c in in_band_chi if c > 0]
            if nz and (max(nz) / min(nz) >= 10.0):
                plateau_seeds += 1
    n_seeds = max(len(chi_sweeps), 1)
    physical_mean_aspect = float(np.mean(physical_aspect_vals)) if physical_aspect_vals else float("nan")
    has_plateau = plateau_seeds >= max(1, n_seeds // 2)
    physical_selects_phi2 = physical_in_band_seeds >= max(1, n_seeds // 2)

    # Handedness flip control: does the asymmetry FLIP sign with handedness? (The
    # chirality signature the symmetric |V| dressing structurally lacks.) Compared
    # at the physical chi over the MATCHED (R, r) subset the LH control covered (the
    # LH grid is a ratio-subset; comparing its mean to the full RH/BARE mean would
    # mix different geometries -- so we restrict RH + BARE to the LH cells).
    hand_flip_confirmed = None
    hand_flip_detail = ""
    if hand_flip is not None:
        flip_keys = {(round(row["R"], 6), round(row["R_over_r_real"], 6)) for row in hand_flip["grid"]}

        def _matched_mean(g, arm):
            vals = [
                row[arm]["most_bound"]["R_over_r_phase"]
                for row in g
                if (round(row["R"], 6), round(row["R_over_r_real"], 6)) in flip_keys
                and row.get(arm, {}).get("most_bound") is not None
            ]
            return float(np.mean(vals)) if vals else None

        rh_matched = _matched_mean(grid, "dressed")
        bare_matched = _matched_mean(grid, "bare")
        lh_dressed = _matched_mean(hand_flip["grid"], "dressed")
        if rh_matched is not None and bare_matched is not None and lh_dressed is not None:
            # The "flip" shows up as the DEVIATION from the BARE (achiral) baseline
            # reversing sign (RH pushes R/r one way, LH the other), on matched cells.
            dev_rh = rh_matched - bare_matched
            dev_lh = lh_dressed - bare_matched
            hand_flip_confirmed = bool(dev_rh * dev_lh < 0)
            flip_msg = (
                "FLIPS sign (chirality signature confirmed)"
                if hand_flip_confirmed
                else "same sign (no clean flip at physical chi)"
            )
            hand_flip_detail = (
                f"matched-subset RH deviation from BARE baseline = {dev_rh:+.5f}, "
                f"LH deviation = {dev_lh:+.5f} -> {flip_msg}"
            )

    # --- Outcome logic ---
    if not selects_aspect:
        outcome = "FLAT/SMALL"
        reason = (
            f"CLOSE (FLAT/SMALL): the CHIRAL coupling's INCREMENT on the aspect, as chi goes "
            f"0 -> physical (1.2*alpha), is {chiral_increment_mean:+.5f} in R/r (mean over "
            f"chi-sweep seeds, (2,3) mode) -- O(alpha)-small and FAR below the ~{0.05 * PHI_SQ_TARGET:.3f} "
            f"needed to move a generic ~2 seed toward phi^2={PHI_SQ_TARGET:.4f}. At its physical "
            f"strength the chiral Meissner coupling does NOT select the aspect (it is the "
            f"g-2-scale delta ~ -3*alpha/2 regime, R/r stays put). phi^2 therefore does NOT "
            f"come from the chiral aspect-selection; it would have to rest on R*r=1/4. "
            f"(Context: the FULL op3 dressing -- base mu/eps asymmetry + chiral -- shifts "
            f"BARE->DRESSED R/r by {aspect_shift:.4f}, but that is dominated by the chi=0 base "
            f"asymmetry, NOT the chiral coupling.) The Class-2 lift closes."
        )
    elif near_phi2 and has_plateau:
        outcome = "A"
        reason = (
            f"LIFT LANDS (A): the CHIRAL dressing selects R/r ~ phi^2 from generic seeds "
            f"(dressed mean {dressed_aspect_mean:.4f}, (2,3)-mode mean "
            f"{dressed_23.get('aspect_mean', float('nan')):.4f} vs phi^2={PHI_SQ_TARGET:.4f}), "
            f"and the chi-SWEEP shows a phi^2 PLATEAU across {plateau_seeds}/{n_seeds} seeds "
            f"spanning >= 1 decade of coupling -- so phi^2 is set by the (2,3) TOPOLOGY "
            f"(pq/(p+q)=6/5 handedness factor), ALPHA-FREE (alpha only the overall scale). "
            f"With R/r=phi^2 AND R-r=1/2, R*r=1/4 follows as a CONSEQUENCE (derived, not "
            f"posited). The lift lands."
        )
    elif near_phi2 and physical_selects_phi2:
        outcome = "B"
        reason = (
            f"CIRCULAR (B): R/r ~ phi^2 appears at the physical chi=1.2*alpha (mean "
            f"{physical_mean_aspect:.4f} vs phi^2={PHI_SQ_TARGET:.4f}) but there is NO phi^2 "
            f"PLATEAU across the chi-sweep (only {plateau_seeds}/{n_seeds} seeds plateau) -- "
            f"the phi^2 selection is tied to the SPECIFIC alpha-injected coupling value, not "
            f"the (2,3) topology. phi^2 = phi^2(alpha) here, so deriving alpha from phi^2 is "
            f"circular. The lift closes as circular."
        )
    else:
        outcome = "C"
        reason = (
            f"OTHER (C): the CHIRAL coupling moves the aspect by a non-negligible increment "
            f"({chiral_increment_mean:+.5f} in R/r as chi:0->physical) -- so it IS an aspect-"
            f"selector -- but it selects a ratio NOT near phi^2={PHI_SQ_TARGET:.4f} (physical-chi "
            f"mean {physical_mean_aspect:.4f}). Whether the selected aspect maps to a different "
            f"corpus geometry is open; phi^2 is not what the chiral dressing picks here."
        )

    return {
        "outcome": outcome,
        "reason": reason,
        "selects_aspect": bool(selects_aspect),
        "chiral_increment_mean": chiral_increment_mean,
        "aspect_shift_full_op3": float(aspect_shift),
        "near_phi2": bool(near_phi2),
        "has_plateau": bool(has_plateau),
        "plateau_seeds": int(plateau_seeds),
        "physical_selects_phi2": bool(physical_selects_phi2),
        "physical_mean_aspect": physical_mean_aspect,
        "bare": bare,
        "dressed": dressed,
        "dressed_2_3": dressed_23,
        "hand_flip_confirmed": hand_flip_confirmed,
        "hand_flip_detail": hand_flip_detail,
    }


def _verify_canonical_source() -> None:
    """ave-canonical-source cross-check: the chiral coupling must be the canonical
    KAPPA_CHIRAL_ELECTRON = alpha*pq/(p+q), NOT a hard-coded literal, and the
    CHI_SWEEP physical point must equal it (no drift). Also assert the engine's
    saturation-kernel module is the AVE-Core canonical source."""
    import ave.topological.cosserat_field_3d as _cf_mod

    assert _cf_mod.__file__.endswith("ave/topological/cosserat_field_3d.py"), (
        "ave.topological.cosserat_field_3d is not the AVE-Core canonical source"
    )
    # KAPPA_CHIRAL_ELECTRON = ALPHA * KAPPA_TILDE_ELECTRON (= 1.2*alpha). Cross-check
    # the structure holds (topology factor separable from alpha scale).
    from ave.core.constants import ALPHA as _ALPHA

    assert abs(KAPPA_CHIRAL_ELECTRON - _ALPHA * KAPPA_TILDE_ELECTRON) < 1e-15, (
        "KAPPA_CHIRAL_ELECTRON != ALPHA * KAPPA_TILDE_ELECTRON -- canonical structure broken"
    )
    assert abs(KAPPA_TILDE_ELECTRON - 6.0 / 5.0) < 1e-12, "KAPPA_TILDE_ELECTRON != 6/5 (the (2,3) topology factor)"
    assert abs(CHI_SWEEP[CHI_PHYSICAL_INDEX] - KAPPA_CHIRAL_ELECTRON) < 1e-9, (
        f"CHI_SWEEP[{CHI_PHYSICAL_INDEX}] ({CHIRAL_PHYS_PRINT}) != canonical KAPPA_CHIRAL_ELECTRON "
        f"({KAPPA_CHIRAL_ELECTRON}); the physical-chi sweep point has drifted from canonical."
    )
    print(
        f"  [canonical] chiral coupling KAPPA_CHIRAL_ELECTRON = ALPHA*KAPPA_TILDE_ELECTRON "
        f"= {ALPHA_VAL:.10e}*{KAPPA_TILDE_ELECTRON} = {KAPPA_CHIRAL_ELECTRON:.10e} (= 1.2*alpha); "
        f"topology factor {KAPPA_TILDE_ELECTRON} = 6/5 is alpha-FREE"
    )


# Module-level read-side prints (NOT consumed by any guarded measure -- display only).
from ave.core.constants import ALPHA as ALPHA_VAL  # noqa: E402

CHIRAL_PHYS_PRINT = KAPPA_CHIRAL_ELECTRON


def main() -> dict:
    print("=" * 78, flush=True)
    print("  alpha Class-2 lift -- CHIRAL Meissner dressing (Test 4, R/r ASPECT selector)")
    print("  Engine: K4 V-sector eigenmode dressed by Cosserat-omega-helicity S_mu/S_eps split")
    print(f"  N_interior={N_LATTICE}  PML={PML}  theta_C=1/sqrt(2)={THETA_C:.4f} (ALPHA-FREE)")
    print("  Measuring R/r (the ASPECT, chirality-DEPENDENT) -- NOT Test 3's R*r (the product)")
    print("=" * 78, flush=True)

    _self_audit_no_forbidden_tokens()
    _verify_canonical_source()
    print()

    # --- Measurement-validity control: does the GENERIC (2,3) seed read as (2,3)
    #     through the V-tank phasor measure? ---
    ctrl_lat = _build_lattice(op3=True)
    seed_generic_2_3_vtank(ctrl_lat, R=R_MAJOR_SWEEP[-1], r=R_MAJOR_SWEEP[-1] / 3.0, peak_amp=SEED_AMPLITUDE_FRAC)
    ctrl_vec = _pack_live_as_eigvec(ctrl_lat.V_inc, ctrl_lat.V_ref, ctrl_lat)
    ctrl_pq = measure_vtank_winding_pq(ctrl_vec, ctrl_lat, R_major=R_MAJOR_SWEEP[-1])
    print(
        f"  [control] generic seed reads V-tank (p,q)=({ctrl_pq['p_major_winding']},"
        f"{ctrl_pq['q_minor_winding']})  is_2_3={ctrl_pq['is_2_3']}  "
        f"(reliab p={ctrl_pq['p_reliability']:.3f} q={ctrl_pq['q_reliability']:.3f})"
    )
    print(f"    -> measure {'VALID (reads the (2,3) it seeded)' if ctrl_pq['is_2_3'] else 'WARNING: seed not (2,3)'}")
    # --- Chiral-dressing sanity: confirm the chiral z_local is NON-trivial at the
    #     physical chi (S_mu != S_eps -> z_local != 1) and TRIVIAL at chi=0. ---
    _Rd, _rd = R_MAJOR_SWEEP[1], R_MAJOR_SWEEP[1] / 2.8
    z0 = chiral_z_local_from_seed(_Rd, _rd, SEED_AMPLITUDE_FRAC, chi=0.0)
    zp = chiral_z_local_from_seed(_Rd, _rd, SEED_AMPLITUDE_FRAC, chi=KAPPA_CHIRAL_ELECTRON)
    zrh = chiral_z_local_from_seed(_Rd, _rd, SEED_AMPLITUDE_FRAC, chi=0.9, handedness="RH")
    zlh = chiral_z_local_from_seed(_Rd, _rd, SEED_AMPLITUDE_FRAC, chi=0.9, handedness="LH")
    print(
        f"  [dressing] chi=0 -> z_local span [{z0.min():.4f},{z0.max():.4f}] (NOT ~1: residual base "
        f"mu/eps asymmetry from the seed -- see ENGINE-REALITY FLAG); chi=1.2*alpha -> "
        f"[{zp.min():.4f},{zp.max():.4f}]"
    )
    print(
        f"  [chirality] RH vs LH max|z_local diff| at chi=0.9 = {np.abs(zrh - zlh).max():.4e}  "
        f"(>0 confirms the dressing IS chirality-dependent -- the R!=r breaker Tests 1-3 lacked)"
    )
    print()

    print("  Generic (R, r) hedgehog sweep (NOT Golden Torus; R/r band brackets but")
    print(f"    never equals phi^2=2.618): R in {R_MAJOR_SWEEP}, R/r in {R_OVER_r_SWEEP}")
    print(f"    seed peak |V|=|omega|={SEED_AMPLITUDE_FRAC} (natural units, strain==|V|)")
    print()

    # PRONG 1 at the PHYSICAL chi (RH), the achiral baseline is inside (bare arm).
    print("=" * 78, flush=True)
    print("  PRONG 1 -- bare(achiral) vs CHIRAL-dressed V-sector aspect landscape @ chi=1.2*alpha (RH)")
    print("=" * 78, flush=True)
    land_phys = prong1_chiral_landscape(
        peak_amp=SEED_AMPLITUDE_FRAC, chi=KAPPA_CHIRAL_ELECTRON, handedness="RH", verbose=True
    )

    # Handedness-flip control (LH) at the physical chi -- does the asymmetry flip?
    # SUBSET of ratios (the single mid R/r across all R) -- enough to read the flip
    # sign without re-running the full grid at the secondary handedness.
    print()
    print("  --- handedness-flip control (LH, mid-ratio subset) @ chi=1.2*alpha: aspect flip sign? ---")
    land_flip = prong1_chiral_landscape(
        peak_amp=SEED_AMPLITUDE_FRAC,
        chi=KAPPA_CHIRAL_ELECTRON,
        handedness="LH",
        verbose=False,
        ratios=(R_OVER_r_SWEEP[len(R_OVER_r_SWEEP) // 2],),
    )

    # THE crux: chi-SWEEP at a few representative generic seeds.
    print()
    print("=" * 78, flush=True)
    print("  CHI-SWEEP (THE crux) -- R/r vs chiral coupling strength at generic seeds")
    print("    Resolves: phi^2 topology-set (plateau across chi, alpha-FREE) vs alpha-injected")
    print("=" * 78, flush=True)
    chi_sweep_seeds = [
        (R_MAJOR_SWEEP[1], R_MAJOR_SWEEP[1] / 2.0),  # R/r_seed = 2.0
        (R_MAJOR_SWEEP[2], R_MAJOR_SWEEP[2] / 2.8),  # R/r_seed = 2.8 (straddles phi^2)
        (R_MAJOR_SWEEP[2], R_MAJOR_SWEEP[2] / 4.0),  # R/r_seed = 4.0
    ]
    chi_sweeps = []
    for (Rc, rc) in chi_sweep_seeds:
        print(f"  -- seed R={Rc:.1f} r={rc:.2f} (R/r_seed={Rc / rc:.2f}) --", flush=True)
        cs = chi_sweep_aspect(SEED_AMPLITUDE_FRAC, Rc, rc, handedness="RH", verbose=True)
        if cs["bare_aspect"] is not None:
            print(f"       (achiral baseline R/r at this seed = {cs['bare_aspect']:.4f})", flush=True)
        chi_sweeps.append(cs)

    verdict = adjudicate(land_phys, chi_sweeps, land_flip)

    print()
    print("=" * 78, flush=True)
    print("  ADJUDICATION")
    print("=" * 78, flush=True)
    print(f"  OUTCOME: {verdict['outcome']}")
    print(f"  {verdict['reason']}")
    print()
    b, d = verdict["bare"], verdict["dressed"]
    d23 = verdict["dressed_2_3"]
    print("  --- bare(achiral)-vs-chiral-dressed R/r ASPECT landscape (most-bound mode) ---")
    print(
        f"  BARE(achiral): R/r mean={b['aspect_mean']:.4f} median={b['aspect_median']:.4f} "
        f"std={b['aspect_std']:.4f}  range[{b['aspect_min']:.4f},{b['aspect_max']:.4f}]"
    )
    print(
        f"  CHIRAL-DRESSED: R/r mean={d['aspect_mean']:.4f} median={d['aspect_median']:.4f} "
        f"std={d['aspect_std']:.4f}  range[{d['aspect_min']:.4f},{d['aspect_max']:.4f}]  [phi^2=2.618]"
    )
    if d23.get("n_points", 0):
        print(f"  CHIRAL-DRESSED (2,3)-selected: R/r mean={d23['aspect_mean']:.4f} std={d23['aspect_std']:.4f}")
    print()
    print(
        f"  >>> CHIRAL INCREMENT (the load-bearing number): R/r moves {verdict['chiral_increment_mean']:+.5f} "
        f"as chi:0->physical(1.2*alpha)"
    )
    print(
        f"      (vs {0.05 * PHI_SQ_TARGET:.3f} needed to approach phi^2 from a ~2 seed; the full op3 "
        f"BARE->DRESSED shift {verdict['aspect_shift_full_op3']:.4f} is dominated by the chi=0 base asymmetry)"
    )
    print()
    print(f"  chi-sweep phi^2 plateau: {verdict['plateau_seeds']}/{len(chi_sweeps)} seeds show a phi^2 plateau")
    print(f"    -> phi^2 is {'TOPOLOGY-SET (alpha-FREE)' if verdict['has_plateau'] else 'NOT a robust plateau'}")
    print(f"  physical-chi (=1.2*alpha) mean R/r = {verdict['physical_mean_aspect']:.4f}  [phi^2=2.618]")
    print(f"    -> physical chi {'DOES' if verdict['physical_selects_phi2'] else 'does NOT'} select phi^2")
    if verdict["hand_flip_confirmed"] is not None:
        print(f"  handedness flip: {verdict['hand_flip_detail']}")
    print()
    print("  *** Coordinate: R/r measured in the K4 V-tank (V_inc, V_ref) phasor plane")
    print("      (doc 28_:72,85-87), NOT real-space and NOT Cosserat (u,omega).")
    print("  *** Dressing: CHIRAL S_mu/S_eps split (doc 54_ §6) driven by Cosserat-omega")
    print("      Beltrami helicity h_local -- the R!=r symmetry-breaker Tests 1-3 missed.")
    results = {
        "landscape_physical": land_phys,
        "landscape_handflip": land_flip,
        "chi_sweeps": chi_sweeps,
        "verdict": verdict,
        "seed_control": ctrl_pq,
        "config": {
            "N_LATTICE": N_LATTICE,
            "PML": PML,
            "R_MAJOR_SWEEP": list(R_MAJOR_SWEEP),
            "R_OVER_r_SWEEP": list(R_OVER_r_SWEEP),
            "CHI_SWEEP": list(CHI_SWEEP),
            "KAPPA_CHIRAL_ELECTRON": float(KAPPA_CHIRAL_ELECTRON),
            "KAPPA_TILDE_ELECTRON": float(KAPPA_TILDE_ELECTRON),
            "SEED_AMPLITUDE_FRAC": SEED_AMPLITUDE_FRAC,
            "THETA_C": THETA_C,
            "PHI_SQ_TARGET": PHI_SQ_TARGET,
        },
    }
    # Persist raw results next to the driver so a 40-min sweep is never lost and the
    # auditor can re-adjudicate from the raw grid + chi-sweeps.
    import json

    out_path = Path(__file__).resolve().parent / "alpha_chiral_dressing_test_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=lambda o: float(o) if isinstance(o, np.floating) else str(o))
    print(f"\n  [results] raw landscape + chi-sweeps + verdict written to {out_path.name}")
    return results


if __name__ == "__main__":
    main()
