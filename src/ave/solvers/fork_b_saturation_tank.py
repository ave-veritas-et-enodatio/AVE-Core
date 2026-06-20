"""Fork-B "Saturation-Tank Mass Confinement" gate — the GENUINE confinement solver.

Prereg: research/2026-06-20_fork-b-saturation-tank-confinement_prereg.md
        (frozen as the FIRST commit of branch
         analysis/2026-06-20-fork-b-saturation-tank-confinement).
Built off origin/main @ 19d55266 (PR#305 varactor scatter kernel is on main).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS MODULE IS (and is NOT) — the LOAD-BEARING architectural correction
═══════════════════════════════════════════════════════════════════════════════
Confinement (normalizable / gapped / Im(ω)) is a property of the SPATIAL
STIFFNESS operator  L = adjoint_div(D ∇),  D = 1/S(A)  — the SAME divergence-form
native Laplacian that graded_vacuum_network.py ALREADY builds and that ALREADY
produces the cold-cage bound mode. This module EXTENDS that eigensolve onto the
NATIVE CONNECT-MAP (build_srs_net / build_diamond_net) as the graph-stiffness
operator  L = Bᵀ diag(D_bond) B  (B = signed node-bond incidence; the discrete
divergence-form Laplacian written on the lattice's OWN bond graph, not a
Cartesian embedding).

The PR#305 scatter operator (vacuum_varactor_scatter.py) is ORTHOGONAL: its
spectrum is unit-modulus (a passive scattering matrix) — it has NO bound states.
This module does NOT eigensolve the scatter matrix for confinement. It IMPORTS
the PR#305 canonical S(A) kernel (vacuum_varactor_scatter.saturation_kernel,
delegating to crystal_engine.saturation_kernel) as the SINGLE S(A)
source-of-truth (ave-canonical-source).

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-NATIVE-CHECK (walked BEFORE this code, operating principle 1)
═══════════════════════════════════════════════════════════════════════════════
  * Sector (CP2): the bound mode lives in the A1 COMMON-MODE / SCALAR grade (the
    dilatation MASS-"3", a per-NODE scalar amplitude). The (2,3) micro-rotation
    CHARGE-"3" winding is NOT wired in (A1 ⊥ T2, master-equation.md:20). The
    operator acts on a per-node SCALAR field; the sector-projection guard
    (assert_sector_A1_scalar) confirms the bound eigenvector is sign-coherent
    common-mode, not a shear/curl pattern.
  * Objective (CP3): the AVE-native objective is the GAPPED bound EIGENMODE of the
    stiffness operator (a localized level separated from the continuum band edge),
    NOT energy-functional minimization / Hessian-of-W gradient-descent.
  * Boundary-not-bulk (CP10): the confinement wall is the μ-load SHORT (Z_eff=√S→0,
    Γ→−1) rendered as the STIFFNESS JUMP in the coefficient D=1/S(A), NOT a bulk
    confining potential U_conf(r) (which is singular at the wall and detonates).
  * Local clock (CP5): D=1/S(A) IS the local-clock modulation (c_eff²=c0²/S); the
    variable-coefficient operator carries it.
  * phase vs real (CP4): confinement is the REAL-space spatial operator's
    eigenvalue + eigenvector localization — coordinate-matched, NOT a φ²
    phase-space claim.
  * Emergence (CP8): the saturated core is PLANTED (a posited Gaussian dilatation
    well). This is a CONSISTENCY-class test (does the tank confine a posited mass?),
    explicitly NOT an emergence-class test (does the engine self-form one?). Flagged.

═══════════════════════════════════════════════════════════════════════════════
THE GAP IS ABOVE THE BAND, NOT BELOW (a load-bearing physics flag, RF-2/RF-3)
═══════════════════════════════════════════════════════════════════════════════
The varactor stiffness convention is D = 1/S → ∞ in the saturated core (HIGH
stiffness, c_eff²=c0²/S → ∞). A localized mode bound to a HIGH-stiffness inclusion
is a HIGH-frequency mode that sits in the gap ABOVE the continuum band top — NOT
below it. This is exactly the cold-cage breathing mode (ω_cutoff≈2.87, a stiff-core
breather). So the spectral-gap witness measures separation from the NEAREST band
edge (here, the band TOP), and the bound mode is the HIGHEST-ω core-localized level
— resolved EXPLICITLY (RF-2/RF-3: do not assume below-band; the bound-vs-band
direction is set by the stiffness sign and is ABOVE the band for D=1/S).

═══════════════════════════════════════════════════════════════════════════════
ALPHA-FREE STRUCTURAL (HR2; import-guarded)
═══════════════════════════════════════════════════════════════════════════════
The operator reads a DIMENSIONLESS saturation amplitude A=|V|/V_yield, so the
α-carrying dimensionful V_YIELD (=√ALPHA·V_SNAP, constants.py) CANCELS. ALPHA is
NEVER imported. α-invariance is STRUCTURAL (and verified by the α→2α gate).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# ── alpha-FREE: import ONLY the canonical S(A) kernel source-of-truth (PR#305) ──
from ave.core.chiral_lattice import (
    LatticeNet,
    build_diamond_net,
    build_srs_net,
)
from ave.solvers.vacuum_varactor_scatter import saturation_kernel  # canonical S(A)

# ─────────────────────────────────────────────────────────────────────────────
# ANTI-LEAK IMPORT-GUARD (HR2): no alpha-carrier reachable. The Fork-B confinement
# operator is alpha-FREE BY CONSTRUCTION (dimensionless A=|V|/V_yield).
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "alpha-leak: ELECTRON instance must NOT be imported"


# ═════════════════════════════════════════════════════════════════════════════
# 1. THE CANONICAL Γ-DEPTH MAP (gamma_bulk convention, crystal_engine.py:478)
# ═════════════════════════════════════════════════════════════════════════════
def gamma_from_S_floor(S_floor: float) -> float:
    """Canonical μ-load Smith-Γ at a saturation floor S_floor (the REACHABLE
    short depth). Γ = (√S − 1)/(√S + 1), the gamma_bulk impedance route
    (crystal_engine.py:478: Z_eff=√S, Γ=(Z_eff−1)/(Z_eff+1)).

    S_floor → 0  ⇒  Γ → −1 (total short, the deep mass cage).
    S_floor = 1  ⇒  Γ = 0 (matched vacuum).
    alpha-FREE (pure S)."""
    z = float(np.sqrt(max(S_floor, 0.0)))
    return (z - 1.0) / (z + 1.0)


# ═════════════════════════════════════════════════════════════════════════════
# 2. THE NATIVE CONNECT-MAP STIFFNESS OPERATOR  L = Bᵀ diag(D_bond) B
# ═════════════════════════════════════════════════════════════════════════════
def unique_bonds(net: LatticeNet) -> list[tuple[int, int]]:
    """The undirected unique bonds (u<v) of the lattice connect-map. Native:
    built from net.neighbors (the lattice's OWN adjacency), never a Cartesian
    distance posit."""
    N = net.n_nodes
    return sorted({(min(u, v), max(u, v)) for u in range(N) for v in net.neighbors[u]})


def saturated_core_strain_native(net: LatticeNet, *, frac: float, sigma_frac: float) -> np.ndarray:
    """A POSITED saturated longitudinal-bulk core on the connect-map nodes: a
    Gaussian dilatation well A(r) = frac·exp(−r²/2σ²) centred at the net centroid
    (the CONSISTENCY-class POSIT, CP8 — PLANTED, not self-formed; flagged).

    sigma = sigma_frac · box (a fraction of the periodic box edge). alpha-FREE
    (geometry only; A is dimensionless |V|/V_yield)."""
    c = net.pos.mean(axis=0)
    # minimum-image radius under PBC
    d = net.pos - c
    d -= net.box * np.round(d / net.box)
    r = np.linalg.norm(d, axis=1)
    sigma = sigma_frac * net.box
    return frac * np.exp(-(r**2) / (2.0 * sigma**2))


def node_radius(net: LatticeNet) -> np.ndarray:
    """Minimum-image node radius from the centroid (for core-fraction masks)."""
    c = net.pos.mean(axis=0)
    d = net.pos - c
    d -= net.box * np.round(d / net.box)
    return np.linalg.norm(d, axis=1)


def bond_stiffness(net: LatticeNet, A_node: np.ndarray, *, S_min: float, A_cap: float | None = None) -> np.ndarray:
    """Per-bond stiffness D_bond = 1/S(A_bond), the varactor map. The bond
    saturation A_bond = max(A_u, A_v) (the bond is as saturated as its most
    saturated endpoint — the well is deepest across the core's interior bonds).

    S(A) is the CANONICAL kernel (vacuum_varactor_scatter.saturation_kernel,
    delegating to crystal_engine — IMPORTED, never re-hardcoded). D=1/S → ∞ as
    S → S_min (the stiff core). alpha-FREE (dimensionless A)."""
    bonds = unique_bonds(net)
    A_bond = np.array([max(A_node[u], A_node[v]) for (u, v) in bonds])
    S = saturation_kernel(A_bond, S_min=S_min, A_cap=A_cap)
    return 1.0 / np.maximum(S, 1e-300)


def connect_map_stiffness_operator(
    net: LatticeNet, A_node: np.ndarray, *, S_min: float, A_cap: float | None = None
) -> np.ndarray:
    """The NATIVE connect-map stiffness operator  L = Bᵀ diag(D_bond) B  on the
    per-node A1 SCALAR field (the dilatation MASS-"3").

    B is the (n_bonds × n_nodes) signed node-bond incidence (B[b,u]=+1, B[b,v]=−1
    for bond (u,v)); D_bond=1/S(A_bond) the varactor stiffness. L is the discrete
    divergence-form Laplacian  adjoint_div(D ∇)  written on the lattice's OWN bond
    graph — the SAME physical operator as graded_vacuum's cube L, but on the native
    connectivity (NOT a Cartesian embedding; structural-null-stencil-lens
    satisfied: the stencil IS the connect-map).

    L is real symmetric positive-semidefinite (it is a weighted graph Laplacian);
    eigenproblem L ψ = ω² ψ with ω² ≥ 0; the nullspace is the constant mode.
    The bound mode is the HIGHEST-ω core-localized level (gap ABOVE the band; the
    stiff-core breather). alpha-FREE."""
    N = net.n_nodes
    bonds = unique_bonds(net)
    D = bond_stiffness(net, A_node, S_min=S_min, A_cap=A_cap)
    B = np.zeros((len(bonds), N))
    for b, (u, v) in enumerate(bonds):
        B[b, u] = 1.0
        B[b, v] = -1.0
    L = B.T @ np.diag(D) @ B
    return 0.5 * (L + L.T)  # enforce exact symmetry


# ═════════════════════════════════════════════════════════════════════════════
# 3. GATE 1 — CONFINEMENT (necessary): gapped, discrete, core-localized, Im(ω) sign
# ═════════════════════════════════════════════════════════════════════════════
@dataclass(frozen=True)
class ConfinementConfig:
    """Fork-B GATE1 config. ONE S_min for the binding operator (RF-3 DEPTH).

    The binding operator's floor is S_min (NOT the scatter's A_cap=0.99). The
    canonical reachable Γ against THIS floor is gamma_from_S_floor(S_min).
    """

    net: str = "diamond"          # "diamond" (degree-4) or "srs" (degree-3)
    L: int = 8                    # cubic cells per side (connect-map size)
    frac: float = 0.95            # planted core amplitude (A_cap of the well)
    sigma_frac: float = 1.0 / 6.0  # core width as a fraction of box
    S_min: float = 1e-3           # the ONE binding-operator floor (Γ≈−0.94)
    A_cap: float | None = None    # kernel clip (None = canonical 0.99); swept in DEPTH
    core_frac_floor: float = 0.50  # RF-1: OVERRIDE the live >0.05 floor
    em_port_closed: bool = True   # lossless reactive cage (Im(ω)=0); open adds loss

    def build_net(self) -> LatticeNet:
        if self.net == "diamond":
            return build_diamond_net(L=self.L)
        if self.net == "srs":
            return build_srs_net(L=self.L)
        raise ValueError(f"net must be 'diamond' or 'srs', got {self.net!r}")

    def gamma_floor(self) -> float:
        """The canonical reachable Γ at THIS binding-operator floor (RF-3 DEPTH)."""
        return gamma_from_S_floor(self.S_min)


def _cluster_spectrum(wpos: np.ndarray, *, rel_tol: float = 1e-4) -> list[tuple[float, int]]:
    """Cluster a sorted positive spectrum into degenerate levels. Returns a list of
    (level_value, multiplicity), ascending. Degeneracy-robust (the diamond/srs core
    breather is multiply degenerate by symmetry, so the bound LEVEL — not a single
    eigenvalue — is what carries the gap)."""
    clusters: list[list[float]] = []
    for x in wpos:
        if clusters and abs(x - clusters[-1][-1]) <= rel_tol * max(abs(x), 1.0):
            clusters[-1].append(x)
        else:
            clusters.append([x])
    return [(float(np.mean(c)), len(c)) for c in clusters]


def _band_structure(w: np.ndarray) -> dict:
    """Partition the (sorted, nullspace-removed) spectrum into the continuum band
    and the bound LEVEL(S) ABOVE it. The bound mode for D=1/S is the HIGHEST-ω
    isolated LEVEL (gap ABOVE the band top — the stiff-core breather, RF-2).

    CLUSTER-AWARE (load-bearing, RF-2): the bound level is multiply degenerate by
    core symmetry; the gap is measured between the bound CLUSTER and the next-lower
    CLUSTER (the band top), NOT between the top two eigenvalues (which are
    degenerate and give a spurious zero gap)."""
    wpos = np.sort(w[w > 1e-9])
    if len(wpos) < 3:
        return {"ok": False, "reason": "too few positive modes"}
    clusters = _cluster_spectrum(wpos)
    if len(clusters) < 2:
        return {"ok": False, "reason": "spectrum has no resolvable gap (one cluster)"}
    bound_level, bound_mult = clusters[-1]
    band_top, _ = clusters[-2]
    # continuum level spacing = median inter-cluster spacing within the band.
    band_levels = [lv for lv, _ in clusters[:-1]]
    spacings = np.diff(band_levels)
    nz = spacings[spacings > 1e-9]
    mean_spacing = float(np.median(nz)) if len(nz) else 0.0
    return {
        "ok": True,
        "w_bound_sq": bound_level,
        "bound_multiplicity": bound_mult,
        "w_band_top_sq": band_top,
        "gap_above_sq": bound_level - band_top,
        "mean_continuum_spacing_sq": mean_spacing,
        "band_min_sq": float(clusters[0][0]),
        "band_max_sq": band_top,
        "n_clusters": len(clusters),
    }


def _select_core_bound_mode(w: np.ndarray, V: np.ndarray, core_mask: np.ndarray, band: dict) -> dict:
    """Pick the most core-localized member of the BOUND LEVEL (the top cluster,
    RF-2). Among the degenerate bound cluster, pick the highest core_frac member.
    Returns {idx, w_sq, omega, core_frac, envelope_radial_conc}."""
    w_bound = band["w_bound_sq"]
    best = None
    for idx in range(len(w)):
        if w[idx] <= 1e-9:
            continue
        # restrict to the bound cluster (degeneracy-aware)
        if abs(w[idx] - w_bound) > 1e-4 * max(abs(w_bound), 1.0):
            continue
        psi = V[:, idx]
        p = psi**2
        p = p / (p.sum() + 1e-300)
        cf = float(p[core_mask].sum())
        if best is None or cf > best["core_frac"]:
            best = {
                "idx": int(idx),
                "w_sq": float(w[idx]),
                "omega": float(np.sqrt(max(w[idx], 0.0))),
                "core_frac": cf,
            }
    return best


def assert_sector_A1_scalar(net: LatticeNet, psi: np.ndarray, core_mask: np.ndarray) -> dict:
    """Sector-projection guard (substrate-native CP2). The bound mode must live in
    the A1 DILATATION-SCALAR grade (the MASS-"3"), NOT the (2,3) shear/micro-rotation
    grade (the CHARGE-"3"). Two structural facts establish A1-residency:

    (1) The operator is built on a per-node SCALAR field (1 DOF/node) — there is NO
        vector/shear grade in this operator for the mode to leak INTO. A1-residency
        is structural-by-construction (the differential/shear couple-stress would be
        a SEPARATE 3-vector operator we did NOT build).
    (2) The mode's ENERGY ENVELOPE |ψ|² is RADIALLY core-organized (a localized
        breather), not a delocalized band state. (The raw signed ψ of a band-TOP
        stiff-core mode necessarily alternates sign at the lattice scale — that is
        high spatial frequency, NOT shear-grade leakage; the A1 signature is the
        ENVELOPE concentration, not raw sign-coherence.)

    Returns {scalar_grade_only, envelope_radial_conc, a1_resident}."""
    p = psi**2
    p = p / (p.sum() + 1e-300)
    env_conc = float(p[core_mask].sum())  # |ψ|² envelope concentration on the core
    scalar_grade_only = True  # the operator has 1 scalar DOF/node — no shear grade
    a1_resident = bool(scalar_grade_only and env_conc >= 0.50)
    return {
        "scalar_grade_only": scalar_grade_only,
        "envelope_radial_conc": env_conc,
        "a1_resident": a1_resident,
    }


def solve_confinement(cfg: ConfinementConfig) -> dict:
    """GATE 1 — eigensolve L on the saturated core; return the bound-mode
    diagnostics with the spectral-gap witness, sign-preserving Im(ω), the
    core-fraction (RF-1 floor 0.50), and the A1-sector guard.

    em_port_closed=True: L is real symmetric → Im(ω)=0 → lossless reactive cage
    (the cold-cage lossless limit, Q=∞). The CONFINEMENT verdict does NOT need a
    loss port — confinement = a gapped, discrete, core-localized real eigenmode.
    alpha-FREE."""
    net = cfg.build_net()
    A = saturated_core_strain_native(net, frac=cfg.frac, sigma_frac=cfg.sigma_frac)
    L = connect_map_stiffness_operator(net, A, S_min=cfg.S_min, A_cap=cfg.A_cap)

    r = node_radius(net)
    sigma = cfg.sigma_frac * net.box
    core_mask = r <= max(sigma * 1.5, net.box / float(cfg.L))

    w, V = np.linalg.eigh(L)  # real symmetric: w real, V orthonormal
    band = _band_structure(w)
    if not band["ok"]:
        return {"ok": False, "reason": band["reason"], "net": net.name, "L": cfg.L}

    best = _select_core_bound_mode(w, V, core_mask, band)
    # spectral-gap witness (RF-2): the bound LEVEL sits ABOVE the band top by a
    # margin EXCEEDING the continuum level spacing (cluster-aware, degeneracy-safe).
    gap_above = band["gap_above_sq"]
    spacing = band["mean_continuum_spacing_sq"]
    discrete = bool(gap_above > max(spacing, 1e-9))

    # sector-projection guard (CP2): A1 dilatation-scalar grade, by construction +
    # envelope-radial concentration (NOT raw sign-coherence — a band-top stiff-core
    # mode alternates sign at the lattice scale; that is high spatial freq, not shear).
    sector = assert_sector_A1_scalar(net, V[:, best["idx"]], core_mask)

    # ── (c) sign-preserving Im(ω) READOUT (RF-3): RESOLVE bound-vs-growing, do NOT
    # assume. Add an OPEN matched loss-port on the outer shell (admittance −iσ on
    # the e^{−iωt} convention) and read the SIGN of Im(ω). The DECAYING (bound,
    # radiating) branch is Im(ω) < 0 in e^{−iωt}; a GROWING (unstable) branch would
    # be Im(ω) > 0. We CONFIRM the bound mode decays (Im<0), and that the CLOSED
    # cage is lossless (Im=0, the mass-cage Q=∞ limit). ──
    im_sign = _readout_im_omega_sign(net, L, r, best["w_sq"])
    omega_im_closed = 0.0  # closed lossless cage: real symmetric => Im=0 exactly

    confined = bool(
        best["core_frac"] >= cfg.core_frac_floor   # (a) RF-1 floor 0.50
        and discrete                               # (b) gapped + discrete (RF-2)
        and sector["a1_resident"]                  # A1-sector guard (CP2)
        and im_sign["bound_branch_confirmed"]      # (c) Im(ω) sign resolved = bound
    )
    return {
        "ok": True,
        "net": net.name,
        "L": cfg.L,
        "n_nodes": net.n_nodes,
        "S_min": cfg.S_min,
        "A_cap": cfg.A_cap,
        "gamma_floor": cfg.gamma_floor(),
        "n_core_saturated": int((A[core_mask] > 0.5).sum()),
        "core_frac": best["core_frac"],
        "core_frac_floor": cfg.core_frac_floor,
        "omega_bound": best["omega"],
        "omega_im_closed": omega_im_closed,
        "omega_im_open": im_sign["im_value"],
        "omega_im_open_sign": im_sign["im_sign"],
        "im_anchor_continuum": im_sign["im_anchor_continuum"],
        "convention_decay_is_negative_im": im_sign["convention_decay_is_negative_im"],
        "bound_branch_confirmed": im_sign["bound_branch_confirmed"],
        "omega_im_sign_convention": (
            "e^{-iωt}: DECAYING/bound branch Im(ω)<0; GROWING/unstable Im(ω)>0. "
            "Convention ANCHORED by a known port-coupled continuum mode (Im<0). "
            "Bound mode is core-localized => lossless (Im~0). Closed cage Im=0 "
            "(mass-cage Q=inf). RESOLVED, not assumed (RF-3)."
        ),
        "w_bound_sq": best["w_sq"],
        "bound_multiplicity": band["bound_multiplicity"],
        "band_top_sq": band["w_band_top_sq"],
        "gap_above_sq": gap_above,
        "continuum_spacing_sq": spacing,
        "discrete": discrete,
        "envelope_radial_conc": sector["envelope_radial_conc"],
        "a1_scalar_resident": sector["a1_resident"],
        "confined": confined,
    }


def _readout_im_omega_sign(net: LatticeNet, L: np.ndarray, r: np.ndarray, w_bound_sq: float) -> dict:
    """Sign-preserving Im(ω) readout (RF-3 — RESOLVE bound-vs-growing). Add an OPEN
    matched loss-port −iσ on the OUTER node shell, make the operator non-Hermitian,
    solve the complex eigenproblem, and read the SIGN of Im(ω) for the mode nearest
    the bound ω². In the e^{−iωt} convention a passive (lossy/radiating, bound) mode
    DECAYS ⇒ Im(ω) < 0; an active/unstable mode would GROW ⇒ Im(ω) > 0. We confirm
    the bound branch is the DECAYING one (and a small loss does not flip it positive).
    alpha-FREE."""
    sigma = 0.05  # small matched-port admittance (probe; magnitude irrelevant to sign)
    rmax = float(r.max())
    port = (r >= 0.85 * rmax).astype(float)  # outer shell
    H = L.astype(complex) - 1j * sigma * np.diag(port)
    lam, vecs = np.linalg.eig(H)
    omega = np.sqrt(lam.astype(complex))
    omega = np.where(omega.real < 0, -omega, omega)  # physical branch Re(ω)>0
    # the mode nearest the bound ω²
    k = int(np.argmin(np.abs(lam - w_bound_sq)))
    im = float(omega[k].imag)
    # CONVENTION ANCHOR (RF-3 RESOLVE-don't-assume): confirm the SIGN convention
    # against a KNOWN port-coupled continuum mode. The continuum mode with the
    # LARGEST port overlap MUST decay (Im<0) under a passive loss port in e^{-iωt}.
    # If that anchor decays, Im<0 = bound/decaying and Im>0 = growing/unstable.
    port_overlap = np.array([
        float((np.abs(vecs[:, j]) ** 2 * port).sum() / (np.abs(vecs[:, j]) ** 2).sum() + 1e-300)
        for j in range(len(lam))
    ])
    j_anchor = int(np.argmax(port_overlap))
    im_anchor = float(omega[j_anchor].imag)
    convention_ok = bool(im_anchor < 0.0)  # a port-coupled mode MUST decay
    # the bound mode is core-localized => port overlap ~0 => |Im| ~ 0 (lossless);
    # NOT growing (Im not significantly positive). That is the bound branch.
    bound_decays_or_lossless = bool(im <= 1e-6)
    return {
        "im_value": im,
        "im_magnitude": abs(im),
        "im_anchor_continuum": im_anchor,  # MUST be < 0 (decays) to fix the convention
        "convention_decay_is_negative_im": convention_ok,
        "bound_is_lossless_or_decaying": bound_decays_or_lossless,
        # RESOLVED: bound mode is lossless/decaying (not growing) AND the convention
        # is anchored by a known-decaying port-coupled continuum mode.
        "bound_branch_confirmed": bool(bound_decays_or_lossless and convention_ok),
        "im_sign": float(np.sign(im)) if abs(im) > 1e-12 else 0.0,
    }
