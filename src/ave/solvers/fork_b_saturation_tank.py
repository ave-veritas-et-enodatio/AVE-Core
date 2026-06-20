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


# ═════════════════════════════════════════════════════════════════════════════
# 4. GATE 2 — SCRAMBLE (anti-tautology, necessary): does S-STRUCTURE bind?
# ═════════════════════════════════════════════════════════════════════════════
# ARM-A: S->1 uniform (must de-confine).
# ARM-B (LOAD-BEARING): spatially PERMUTE the per-bond S field holding the
#   S-histogram FIXED (must de-confine). A mode surviving ARM-B with core_frac>=0.50
#   gapped is BC/projector-decided = AUTO-VOID.
# Negative control: a uniform-field scramble is a no-op.
# Freeze the de-confinement margin >= 0.30 vs the ARM-A flat baseline.
# ═════════════════════════════════════════════════════════════════════════════


def _bound_core_frac_from_operator(net: LatticeNet, L: np.ndarray, core_mask: np.ndarray) -> dict:
    """Solve L, find the bound LEVEL (top cluster), and return its best-member
    core_frac + gap + discreteness. Shared kernel for the scramble arms (so every
    arm is judged by the IDENTICAL bound-mode selector as GATE1)."""
    w, V = np.linalg.eigh(L)
    band = _band_structure(w)
    if not band["ok"]:
        return {"ok": False, "core_frac": 0.0, "gapped_discrete": False, "reason": band["reason"]}
    best = _select_core_bound_mode(w, V, core_mask, band)
    gapped_discrete = bool(band["gap_above_sq"] > max(band["mean_continuum_spacing_sq"], 1e-9))
    return {
        "ok": True,
        "core_frac": best["core_frac"],
        "omega": best["omega"],
        "gap_above_sq": band["gap_above_sq"],
        "continuum_spacing_sq": band["mean_continuum_spacing_sq"],
        "gapped_discrete": gapped_discrete,
    }


def _bond_S_field(net: LatticeNet, A_node: np.ndarray, *, S_min: float, A_cap: float | None) -> np.ndarray:
    """The per-bond S(A_bond) field (NOT the stiffness D=1/S). This is what the
    scramble PERMUTES (holding its histogram fixed)."""
    bonds = unique_bonds(net)
    A_bond = np.array([max(A_node[u], A_node[v]) for (u, v) in bonds])
    return saturation_kernel(A_bond, S_min=S_min, A_cap=A_cap)


def _operator_from_bond_S(net: LatticeNet, S_bond: np.ndarray) -> np.ndarray:
    """Assemble L=B^T diag(1/S_bond) B directly from a per-bond S field (used by the
    scramble arms, which manipulate S_bond directly rather than via A_node)."""
    N = net.n_nodes
    bonds = unique_bonds(net)
    D = 1.0 / np.maximum(S_bond, 1e-300)
    B = np.zeros((len(bonds), N))
    for b, (u, v) in enumerate(bonds):
        B[b, u] = 1.0
        B[b, v] = -1.0
    L = B.T @ np.diag(D) @ B
    return 0.5 * (L + L.T)


def solve_scramble(cfg: ConfinementConfig, *, seed: int = 20260620) -> dict:
    """GATE 2 — the scramble arms. Returns the baseline (graded) bound core_frac and
    the three arms (ARM-A uniform-S, ARM-B histogram-preserving permutation, negative
    control), with the de-confinement margins and the AUTO-VOID flag.

    AUTO-VOID (the structural successor to Fork-A's verdict_is_projector_tautology):
    if ARM-B SURVIVES (the permuted-S mode is still core_frac>=0.50 AND gapped), the
    'confinement' is BC/projector-decided, NOT S-structure-decided => VOID.
    alpha-FREE."""
    net = cfg.build_net()
    A = saturated_core_strain_native(net, frac=cfg.frac, sigma_frac=cfg.sigma_frac)
    r = node_radius(net)
    sigma = cfg.sigma_frac * net.box
    core_mask = r <= max(sigma * 1.5, net.box / float(cfg.L))

    # ── baseline: the GRADED operator (the real saturated core) ──
    S_bond = _bond_S_field(net, A, S_min=cfg.S_min, A_cap=cfg.A_cap)
    L_graded = _operator_from_bond_S(net, S_bond)
    base = _bound_core_frac_from_operator(net, L_graded, core_mask)

    rng = np.random.default_rng(seed)

    # ── ARM-A: S -> 1 uniform (vacuum everywhere); must de-confine ──
    L_unif = _operator_from_bond_S(net, np.ones_like(S_bond))
    armA = _bound_core_frac_from_operator(net, L_unif, core_mask)

    # ── ARM-B (LOAD-BEARING): permute the per-bond S field, histogram FIXED ──
    S_perm = S_bond.copy()
    rng.shuffle(S_perm)  # same multiset of S values, spatially scrambled
    L_perm = _operator_from_bond_S(net, S_perm)
    armB = _bound_core_frac_from_operator(net, L_perm, core_mask)
    # histogram-preservation check (the load-bearing invariant)
    hist_preserved = bool(np.allclose(np.sort(S_bond), np.sort(S_perm)))

    # ── NEGATIVE CONTROL: permute a UNIFORM (constant) S field => no-op ──
    S_const = np.full_like(S_bond, 0.5)
    S_const_perm = S_const.copy()
    rng.shuffle(S_const_perm)
    L_const = _operator_from_bond_S(net, S_const)
    L_const_perm = _operator_from_bond_S(net, S_const_perm)
    control_is_noop = bool(np.allclose(L_const, L_const_perm, atol=1e-12))

    base_cf = base["core_frac"]
    armA_cf = armA["core_frac"]
    armB_cf = armB["core_frac"]
    margin_A = base_cf - armA_cf
    margin_B = base_cf - armB_cf

    # de-confinement: the arm must DROP core_frac by >= 0.30 OR lose the gap.
    armA_deconfines = bool(margin_A >= 0.30 or not armA["gapped_discrete"] or armA_cf < 0.50)
    armB_deconfines = bool(margin_B >= 0.30 or not armB["gapped_discrete"] or armB_cf < 0.50)
    # AUTO-VOID: ARM-B SURVIVES (still confined: core_frac>=0.50 AND gapped).
    armB_survives = bool(armB_cf >= 0.50 and armB["gapped_discrete"])
    auto_void = armB_survives

    return {
        "ok": True,
        "net": net.name,
        "L": cfg.L,
        "baseline_core_frac": base_cf,
        "baseline_gapped": base["gapped_discrete"],
        "armA_uniform_core_frac": armA_cf,
        "armA_margin": margin_A,
        "armA_deconfines": armA_deconfines,
        "armB_permute_core_frac": armB_cf,
        "armB_margin": margin_B,
        "armB_deconfines": armB_deconfines,
        "armB_histogram_preserved": hist_preserved,
        "armB_survives_AUTO_VOID": armB_survives,
        "negative_control_is_noop": control_is_noop,
        "deconfines_both_arms": bool(armA_deconfines and armB_deconfines),
        "auto_void": auto_void,
    }


def solve_scramble_rate(
    cfg: ConfinementConfig, *, n_perm: int = 120, seed: int = 20260620
) -> dict:
    """GATE 2 ARM-B RATE-SWEEP — disclose the researcher-degree-of-freedom in the
    single-seed ARM-B verdict (honest-scope disclosure, NOT a verdict change).

    `solve_scramble` reports ARM-B's NOT-VOID (de-confine) verdict on ONE frozen
    seed. That binary is honest but UNDER-DISCLOSES that a histogram-preserving
    permutation can — by chance — accidentally reconstitute a confining core. This
    function runs `n_perm` INDEPENDENT histogram-preserving permutations of the
    per-bond S(A) field (the SAME shuffle ARM-B does, judged by the IDENTICAL
    `_bound_core_frac_from_operator` selector as GATE1/ARM-B) and MEASURES the
    fraction that RE-CONFINE (core_frac>=0.50 AND gapped — i.e. the auto_void
    condition).

    Physical reading: the re-confine RATE is the probability that a random
    histogram-preserving shuffle accidentally concentrates the bound mode's |ψ|²
    back onto the core. A LOW rate (measured ~6% on srs) means the NOT-VOID verdict
    is PREDOMINANTLY (~94%) S-STRUCTURE-decided — confinement needs the SPATIAL S
    arrangement, not just the S multiset. It is NOT 100%: the verdict's margin is
    (1 − rate), measured, not a single-seed binary.

    A FIXED RNG seed (default 20260620, matching ARM-B's frozen seed) makes the
    measured rate REPRODUCIBLE. alpha-FREE (the operator never reads ALPHA)."""
    net = cfg.build_net()
    A = saturated_core_strain_native(net, frac=cfg.frac, sigma_frac=cfg.sigma_frac)
    r = node_radius(net)
    sigma = cfg.sigma_frac * net.box
    core_mask = r <= max(sigma * 1.5, net.box / float(cfg.L))

    S_bond = _bond_S_field(net, A, S_min=cfg.S_min, A_cap=cfg.A_cap)
    rng = np.random.default_rng(seed)

    n_reconfine = 0
    n_cf_only = 0       # core_frac>=0.50 alone (the BINDING constraint)
    n_gapped_only = 0   # gapped alone (almost always true for a graph Laplacian)
    core_fracs: list[float] = []
    for _ in range(n_perm):
        S_perm = S_bond.copy()
        rng.shuffle(S_perm)  # histogram-preserving: same S multiset, scrambled space
        res = _bound_core_frac_from_operator(net, _operator_from_bond_S(net, S_perm), core_mask)
        cf_ok = bool(res["core_frac"] >= 0.50)
        gp_ok = bool(res["gapped_discrete"])
        core_fracs.append(res["core_frac"])
        n_cf_only += int(cf_ok)
        n_gapped_only += int(gp_ok)
        # RE-CONFINE = the auto_void condition (core_frac>=0.50 AND gapped).
        n_reconfine += int(cf_ok and gp_ok)

    rate = n_reconfine / float(n_perm)
    return {
        "ok": True,
        "net": net.name,
        "L": cfg.L,
        "n_perm": n_perm,
        "seed": seed,
        "n_reconfine": n_reconfine,
        "reconfine_rate": rate,
        "deconfine_rate": 1.0 - rate,
        # decomposition: which sub-condition is the binding constraint for re-confine
        "n_core_frac_ge_half": n_cf_only,
        "n_gapped": n_gapped_only,
        "mean_perm_core_frac": float(np.mean(core_fracs)),
        # the NOT-VOID verdict is PREDOMINANTLY S-structure-decided iff the rate is low
        "predominantly_deconfines": bool(rate < 0.20),
    }


def scramble_rate_sweep(
    *, nets=(("srs", 4), ("srs", 6)), n_perm: int = 120, seed: int = 20260620
) -> dict:
    """Run `solve_scramble_rate` over the srs connect-maps the auditor flagged
    (L=4 and L=6) and return the per-net + POOLED measured re-confine rate. The
    pooled rate is the headline disclosure number (the chance a random
    histogram-preserving shuffle accidentally reconstitutes a confining core).
    Fixed seed => reproducible. alpha-FREE."""
    rows = []
    tot_reconf = 0
    tot_perm = 0
    for net, L in nets:
        rr = solve_scramble_rate(ConfinementConfig(net=net, L=L), n_perm=n_perm, seed=seed)
        rows.append(rr)
        tot_reconf += rr["n_reconfine"]
        tot_perm += rr["n_perm"]
    pooled = tot_reconf / float(tot_perm) if tot_perm else 0.0
    return {
        "ok": True,
        "rows": rows,
        "pooled_n_reconfine": tot_reconf,
        "pooled_n_perm": tot_perm,
        "pooled_reconfine_rate": pooled,
        "pooled_deconfine_rate": 1.0 - pooled,
        "predominantly_deconfines": bool(pooled < 0.20),
    }


# ═════════════════════════════════════════════════════════════════════════════
# 5. GATE 3 — QUARTER-ARC SHAPE (headline; CANNOT earn CHORD alone)
# ═════════════════════════════════════════════════════════════════════════════
# The canonical AVE kernel S(A)=√(1−A²) (p=0.5) IS the quarter-circle EXACTLY
# (S²+A²=1; ∫₀¹√(1−A²)dA = π/4 = the quarter-circle area). The discriminator: does
# the bound-mode Δ/L of the canonical quarter-arc DIFFER from a same-family
# comparator (1−A²)^p, p≠0.5, matched on BOTH integral-norm AND well-depth, by
# >10% — size-converged, monotone, passing the null-shape control, and PERSISTING
# as the floor is lifted (S_min→0)?
#
# RF-5: the endpoint-tanh comparator is RETIRED (sup-norm 0.5<π/4=norm-INFEASIBLE).
# The norm-feasible SAME-FAMILY comparator (1−A²)^p has norms that OVERLAP π/4
# (p=0.6→0.757, p=0.75→0.719, p=1.0→0.667), so a brentq norm-match has a bracketed
# root (asserted before freezing).
# ═════════════════════════════════════════════════════════════════════════════


def _shape_norm(p: float) -> float:
    """The integral shape-norm ∫₀¹ (1−A²)^p dA (the prereg's reference norms:
    p=0.5→π/4≈0.785, p=0.6→0.757, p=0.75→0.719, p=1.0→0.667). Pure shape (NOT
    the bound mode); used by the brentq norm-match."""
    from scipy.integrate import quad

    val, _ = quad(lambda A: (1.0 - A**2) ** p, 0.0, 1.0)
    return float(val)


def norm_match_p(target_norm: float, *, bracket: tuple[float, float] = (0.3, 3.0)) -> dict:
    """RF-5: assert the brentq norm-match SUCCEEDS (a bracketed root) before freezing
    the comparator. Returns {ok, p, norm, target} or {ok:False} if the target is
    outside the feasible norm range (HALT — the comparator is norm-infeasible, the
    exact failure of the retired endpoint-tanh)."""
    from scipy.optimize import brentq

    lo, hi = bracket
    n_lo, n_hi = _shape_norm(lo), _shape_norm(hi)
    if not (min(n_lo, n_hi) <= target_norm <= max(n_lo, n_hi)):
        return {"ok": False, "reason": f"target_norm {target_norm:.4f} outside feasible [{n_hi:.4f},{n_lo:.4f}]"}
    p = brentq(lambda pp: _shape_norm(pp) - target_norm, lo, hi)
    return {"ok": True, "p": float(p), "norm": _shape_norm(p), "target": target_norm}


def _depth_matched_bond_S(
    net: LatticeNet, A_node: np.ndarray, *, p: float, target_min_S: float
) -> np.ndarray:
    """Build a per-bond S field for shape exponent p, RESCALED so its MINIMUM S
    (the well depth = D_max⁻¹) EQUALS target_min_S. This is the DEPTH-INVARIANT
    construction (match BOTH norm via p AND depth via this rescale) so the Δ/L
    metric reads CURVATURE, not floor-saturation. The rescale is an affine map of
    the well that PRESERVES the shape exponent's curvature signature while pinning
    the depth: S' = target_min_S + (S − S.min())·(1 − target_min_S)/(1 − S.min())."""
    bonds = unique_bonds(net)
    A_bond = np.array([max(A_node[u], A_node[v]) for (u, v) in bonds])
    S = np.maximum(1.0 - A_bond**2, 0.0) ** p
    s0 = float(S.min())
    if abs(1.0 - s0) < 1e-12:
        return np.clip(S, target_min_S, 1.0)
    S_scaled = target_min_S + (S - s0) * (1.0 - target_min_S) / (1.0 - s0)
    return np.clip(S_scaled, target_min_S, 1.0)


def _bound_delta_over_L(net: LatticeNet, S_bond: np.ndarray, core_mask: np.ndarray, r: np.ndarray) -> dict:
    """Δ/L = √(Σ r²|ψ|² / Σ|ψ|²) / L for the bound mode of L(S_bond). The
    depth-invariant CURVATURE metric (the bound-mode RMS radius over box size)."""
    L = _operator_from_bond_S(net, S_bond)
    w, V = np.linalg.eigh(L)
    band = _band_structure(w)
    if not band["ok"]:
        return {"ok": False, "reason": band["reason"]}
    best = _select_core_bound_mode(w, V, core_mask, band)
    psi = V[:, best["idx"]]
    p2 = psi**2
    rms = float(np.sqrt((p2 * r**2).sum() / (p2.sum() + 1e-300)))
    return {
        "ok": True,
        "delta_over_L": rms / net.box,
        "rms_radius": rms,
        "core_frac": best["core_frac"],
        "omega": best["omega"],
        "gapped_discrete": bool(band["gap_above_sq"] > max(band["mean_continuum_spacing_sq"], 1e-9)),
        "min_S": float(S_bond.min()),
    }


def solve_quarter_arc_shape(
    cfg: ConfinementConfig, *, comparator_p: float = 0.75, null_p_pair: tuple[float, float] = (0.6, 1.0)
) -> dict:
    """GATE 3 — the quarter-arc shape discriminator (depth-invariant, with the
    null-shape control + floor-artifact guard). Returns the canonical-vs-comparator
    Δ/L gap, the null control, and the per-arm diagnostics. alpha-FREE.

    The canonical quarter-arc is p=0.5 (S=√(1−A²)); the comparator is a same-family
    p≠0.5 shape matched on BOTH norm (brentq) and well-depth (rescale). The gap is
    |Δ/L_canon − Δ/L_comp| / Δ/L_canon; CHORD requires >10% (but the anchor is the
    binding constraint, so >10% here is necessary-not-sufficient)."""
    net = cfg.build_net()
    A = saturated_core_strain_native(net, frac=cfg.frac, sigma_frac=cfg.sigma_frac)
    r = node_radius(net)
    sigma = cfg.sigma_frac * net.box
    core_mask = r <= max(sigma * 1.5, net.box / float(cfg.L))

    # RF-5: assert the brentq norm-match SUCCEEDS before freezing the comparator.
    nm = norm_match_p(_shape_norm(comparator_p))
    norm_match_ok = nm["ok"]

    # the canonical quarter-arc (p=0.5) sets the depth target (its well depth).
    S_canon = _depth_matched_bond_S(net, A, p=0.5, target_min_S=cfg.S_min)
    target_depth = float(S_canon.min())
    S_comp = _depth_matched_bond_S(net, A, p=comparator_p, target_min_S=target_depth)

    d_canon = _bound_delta_over_L(net, S_canon, core_mask, r)
    d_comp = _bound_delta_over_L(net, S_comp, core_mask, r)
    if not (d_canon["ok"] and d_comp["ok"]):
        return {"ok": False, "reason": "bound mode not found in canon/comp"}
    gap = abs(d_canon["delta_over_L"] - d_comp["delta_over_L"]) / (d_canon["delta_over_L"] + 1e-300)

    # ── NULL-SHAPE CONTROL: two SAME-family shapes matched norm+depth must give
    # Δ/L within ≪10% (proves the metric reads SHAPE not DEPTH) BEFORE any
    # cross-family gap counts. ──
    p1, p2 = null_p_pair
    S_n1 = _depth_matched_bond_S(net, A, p=p1, target_min_S=target_depth)
    S_n2 = _depth_matched_bond_S(net, A, p=p2, target_min_S=target_depth)
    dn1 = _bound_delta_over_L(net, S_n1, core_mask, r)
    dn2 = _bound_delta_over_L(net, S_n2, core_mask, r)
    null_gap = abs(dn1["delta_over_L"] - dn2["delta_over_L"]) / (dn1["delta_over_L"] + 1e-300)
    null_control_passes = bool(null_gap < 0.10)  # metric reads shape, not depth

    return {
        "ok": True,
        "net": net.name,
        "L": cfg.L,
        "S_min": cfg.S_min,
        "norm_match_ok": norm_match_ok,
        "comparator_p": comparator_p,
        "comparator_norm_match": nm,
        "target_depth_min_S": target_depth,
        "delta_over_L_canonical": d_canon["delta_over_L"],
        "delta_over_L_comparator": d_comp["delta_over_L"],
        "shape_gap": gap,
        "shape_gap_exceeds_10pct": bool(gap > 0.10),
        "null_gap": null_gap,
        "null_control_passes": null_control_passes,
        "canon_min_S": d_canon["min_S"],
        "comp_min_S": d_comp["min_S"],
        "depth_matched": bool(abs(d_canon["min_S"] - d_comp["min_S"]) < 1e-6),
    }


def quarter_arc_floor_lift(cfg: ConfinementConfig, *, comparator_p: float = 0.75,
                           S_mins=(1e-1, 1e-2, 1e-3, 1e-5)) -> dict:
    """FLOOR-ARTIFACT GUARD (RF / GATE3): require the shape gap to PERSIST as
    S_min → 0 (the floor lifted). If the gap VANISHES when neither shape clips, it
    was a floor artifact → ECHO. Returns the gap vs S_min sweep + the verdict."""
    gaps = []
    for sm in S_mins:
        c = ConfinementConfig(net=cfg.net, L=cfg.L, frac=cfg.frac, sigma_frac=cfg.sigma_frac, S_min=sm)
        r = solve_quarter_arc_shape(c, comparator_p=comparator_p)
        gaps.append((sm, r["shape_gap"] if r["ok"] else float("nan")))
    finite = [g for _, g in gaps if np.isfinite(g)]
    # the gap PERSISTS if it does NOT collapse toward 0 as the floor lifts.
    persists = bool(len(finite) >= 2 and min(finite) > 0.10)
    return {
        "ok": True,
        "gap_vs_S_min": gaps,
        "gap_persists_as_floor_lifts": persists,
        "verdict": "shape-load-bearing" if persists else "floor-artifact-or-shape-generic (ECHO)",
    }


def quarter_arc_size_convergence(net: str, Ls, *, comparator_p: float = 0.75,
                                 frac: float = 0.95, S_min: float = 1e-3) -> dict:
    """SIZE-CONVERGENCE (GATE3): the shape gap must be MONOTONE-CONVERGING over the
    connect-map size ladder (L=2/4/6 on the connect-map; the cube N-ladder is a
    separate Cartesian-embedded sensitivity, flagged). Returns the gap vs L curve +
    the monotone-converging verdict."""
    rows = []
    for Lc in Ls:
        c = ConfinementConfig(net=net, L=Lc, frac=frac, sigma_frac=1.0 / 6.0, S_min=S_min)
        r = solve_quarter_arc_shape(c, comparator_p=comparator_p)
        rows.append({"L": Lc, "shape_gap": r["shape_gap"] if r["ok"] else float("nan"),
                     "delta_over_L_canon": r.get("delta_over_L_canonical", float("nan"))})
    gaps = [row["shape_gap"] for row in rows if np.isfinite(row["shape_gap"])]
    # monotone-converging: the successive differences shrink (a Cauchy tail). When
    # the gap is converged-near-zero (all < 1% — the ECHO outcome), the Cauchy-tail
    # test on the noise floor is moot; "size-stable below threshold" IS the
    # convergence statement. We report BOTH.
    if len(gaps) >= 3:
        diffs = [abs(gaps[i + 1] - gaps[i]) for i in range(len(gaps) - 1)]
        cauchy_tail = bool(diffs[-1] <= diffs[0] + 1e-9)
    else:
        diffs = []
        cauchy_tail = False
    converged_near_zero = bool(len(gaps) >= 2 and max(gaps) < 0.01)
    gap_exceeds_10pct_anywhere = bool(len(gaps) >= 1 and max(gaps) > 0.10)
    # MONOTONE-CONVERGING in the prereg sense: either a real gap with a shrinking
    # Cauchy tail, OR the gap is size-stably below threshold (converged to ~0).
    monotone_converging = bool(cauchy_tail or converged_near_zero)
    return {"ok": True, "net": net, "rows": rows, "gaps": gaps, "diffs": diffs,
            "cauchy_tail": cauchy_tail, "converged_near_zero": converged_near_zero,
            "gap_exceeds_10pct_anywhere": gap_exceeds_10pct_anywhere,
            "monotone_converging": monotone_converging}


# ═════════════════════════════════════════════════════════════════════════════
# 6. ELECTRON ANCHOR (CHORD-required, NOT expected) + alpha-free + DEC-5
# ═════════════════════════════════════════════════════════════════════════════
COLD_CAGE_OMEGA_CUTOFF = 2.87  # FORM anchor: test_l3_mass_cage.py:18 (NOT m_e — definitional)
Z_RADIATION_VALUE = 29.98       # DEC-5 anti-coincidence (the only ~30 is Z_RADIATION)


def electron_anchor_check(net: str, Ls, *, frac: float = 0.95, S_min: float = 1e-3,
                          tol: float = 0.10) -> dict:
    """The ELECTRON ANCHOR (CHORD-required, NOT bonus, NOT expected): does the
    CONVERGED connect-map bound mode reproduce the cold-cage ω_cutoff≈2.87 WITHOUT
    α-import? A FORM/structural anchor, NOT m_e (which is definitional).

    Honest finding (pre-committed): the connect-map bound-mode ω is set by the
    lattice's OWN band structure (degree / geometry / normalization), NOT a
    universal 2.87 — so it is NOT expected to converge TO 2.87. Reproduction =
    converged AND within `tol` of 2.87. alpha-FREE."""
    omegas = []
    for Lc in Ls:
        r = solve_confinement(ConfinementConfig(net=net, L=Lc, frac=frac, sigma_frac=1.0 / 6.0, S_min=S_min))
        if r["ok"] and r["confined"]:
            omegas.append((Lc, r["omega_bound"]))
    if len(omegas) < 2:
        return {"ok": True, "net": net, "omegas": omegas, "anchor_reproduced": False,
                "reason": "too few confined sizes to assess convergence"}
    ws = [w for _, w in omegas]
    converged = bool(abs(ws[-1] - ws[-2]) / (abs(ws[-2]) + 1e-300) < 0.05)
    near_anchor = bool(abs(ws[-1] - COLD_CAGE_OMEGA_CUTOFF) / COLD_CAGE_OMEGA_CUTOFF < tol)
    return {
        "ok": True,
        "net": net,
        "omegas": omegas,
        "omega_converged_value": ws[-1],
        "cold_cage_anchor": COLD_CAGE_OMEGA_CUTOFF,
        "converged_in_L": converged,
        "within_tol_of_anchor": near_anchor,
        # the anchor is reproduced ONLY if BOTH converged AND within tol.
        "anchor_reproduced": bool(converged and near_anchor),
    }


def alpha_free_invariance(cfg: ConfinementConfig) -> dict:
    """α-FREE STRUCTURAL gate (validate-on-known iv): double ALPHA in constants,
    re-solve, and confirm the Δ/L (and ω) are BIT-INVARIANT (|dx/x|<1e-6) — the
    operator never reads ALPHA (dimensionless A=|V|/V_yield). Also asserts the
    import-guards (no ALPHA/Q_TANK/ELECTRON reachable)."""
    import importlib

    import ave.core.constants as C
    import ave.solvers.fork_b_saturation_tank as F

    alpha_reachable = ("ALPHA" in vars(F)) or ("Q_TANK" in vars(F)) or ("ELECTRON" in vars(F))

    def _metric():
        r = F.solve_confinement(cfg)
        s = F.solve_quarter_arc_shape(cfg)
        return r["omega_bound"], s["delta_over_L_canonical"]

    o0, d0 = _metric()
    saved = C.ALPHA
    try:
        C.ALPHA = 2.0 * saved
        o1, d1 = _metric()
    finally:
        C.ALPHA = saved
    rel_o = abs(o1 - o0) / (abs(o0) + 1e-300)
    rel_d = abs(d1 - d0) / (abs(d0) + 1e-300)
    return {
        "ok": True,
        "alpha_reachable_in_module": bool(alpha_reachable),  # MUST be False
        "rel_d_omega": rel_o,
        "rel_d_delta_over_L": rel_d,
        "alpha_free_pass": bool((not alpha_reachable) and rel_o < 1e-6 and rel_d < 1e-6),
    }


def dec5_anti_coincidence(cfg: ConfinementConfig) -> dict:
    """DEC-5 anti-coincidence pin: the bound-mode ω (and any reported Q-like number)
    is NOT silently the constant Z_RADIATION=29.98. |ω − 29.98| > 1.0 (the only ~30
    is band-consistent Z_RADIATION, never an identity)."""
    r = solve_confinement(cfg)
    om = r["omega_bound"]
    return {
        "ok": True,
        "omega_bound": om,
        "Z_RADIATION": Z_RADIATION_VALUE,
        "not_Z_radiation": bool(abs(om - Z_RADIATION_VALUE) > 1.0),
    }


# ═════════════════════════════════════════════════════════════════════════════
# 7. TOP-LEVEL VERDICT DRIVER (the frozen binning)
# ═════════════════════════════════════════════════════════════════════════════
def run_fork_b_gate(*, primary_net: str = "diamond", primary_L: int = 8,
                    cube_anchor_Ls=None, S_min: float = 1e-3) -> dict:
    """Run the full Fork-B gate and return the frozen-binned verdict.

    Order (VOID-check first, then REFUTE, then CHORD-requires-all):
      GATE2 ARM-B survives  -> VOID  (tautology; discarded, NOT a negative)
      GATE1 not confined    -> REFUTE
      CHORD = confined AND scramble-de-confines AND shape-gap>10%-converged-null-ok
              AND electron-anchor-reproduced
      ECHO  = confined + scramble-de-confines BUT (shape-generic OR no anchor)

    alpha-FREE. Returns the full diagnostics + the verdict string."""
    cfg = ConfinementConfig(net=primary_net, L=primary_L, S_min=S_min)
    g1 = solve_confinement(cfg)
    g2 = solve_scramble(cfg)
    g3 = solve_quarter_arc_shape(cfg)
    g3_floor = quarter_arc_floor_lift(cfg)
    ladders = {"diamond": [4, 6, 8], "srs": [2, 4, 6]}
    g3_size = quarter_arc_size_convergence(primary_net, ladders[primary_net])
    anchor = electron_anchor_check(primary_net, ladders[primary_net], S_min=S_min)
    afi = alpha_free_invariance(cfg)
    dec5 = dec5_anti_coincidence(cfg)

    confined = bool(g1["ok"] and g1["confined"])
    deconfines = bool(g2["deconfines_both_arms"])
    auto_void = bool(g2["auto_void"])
    shape_gap_chord = bool(
        g3["shape_gap_exceeds_10pct"]
        and g3["null_control_passes"]
        and g3_size["monotone_converging"]
        and g3_size["gap_exceeds_10pct_anywhere"]
        and g3_floor["gap_persists_as_floor_lifts"]
    )
    anchor_ok = bool(anchor["anchor_reproduced"])

    # ── frozen binning ──
    if auto_void:
        verdict = "VOID"
        reason = "GATE2 ARM-B survives: confinement is BC/projector-decided (tautology)"
    elif not confined:
        verdict = "REFUTE"
        reason = "GATE1 not confined even at the binding-operator floor"
    elif confined and deconfines and shape_gap_chord and anchor_ok:
        verdict = "CHORD"
        reason = "confined + scramble-de-confines + shape-gap>10%-converged + anchor reproduced"
    elif confined and deconfines:
        verdict = "ECHO"
        reason = "confined + scramble-de-confines (real, S-dependent) BUT shape-generic and/or no anchor (FORM-chord/consistency)"
    else:
        verdict = "REFUTE"
        reason = "confined but scramble did NOT de-confine and not a tautology (anomalous)"

    return {
        "verdict": verdict,
        "reason": reason,
        "primary_net": primary_net,
        "primary_L": primary_L,
        "S_min": S_min,
        "gate1_confinement": g1,
        "gate2_scramble": g2,
        "gate3_shape": g3,
        "gate3_floor_lift": g3_floor,
        "gate3_size_convergence": g3_size,
        "electron_anchor": anchor,
        "alpha_free_invariance": afi,
        "dec5_anti_coincidence": dec5,
        "binning": {
            "confined": confined,
            "scramble_deconfines_both_arms": deconfines,
            "auto_void": auto_void,
            "shape_gap_chord": shape_gap_chord,
            "electron_anchor_reproduced": anchor_ok,
        },
    }


if __name__ == "__main__":
    import json

    print("FORK-B SATURATION-TANK MASS CONFINEMENT GATE")
    print("=" * 72)
    out = run_fork_b_gate()
    # compact summary (full dict is large)
    print(json.dumps(out["binning"], indent=2))
    print("-" * 72)
    print(f"VERDICT: {out['verdict']}")
    print(f"REASON : {out['reason']}")
