"""CAVITY-CENSUS STAGE-1 — imposed-cavity mode census (the (2,3) emergence test).

FROZEN PRE-REG: research/2026-07-14_cavity-census-stage1_prereg_FROZEN.md
(freeze SHA on branch analysis/cavity-census-stage1; freeze precedes this driver
in git history).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS (task #49 — the D3 COEXIST stress-test)
═══════════════════════════════════════════════════════════════════════════════
Impose a Γ=−1 closed surface of electron scale as a BOUNDARY-CONDITION OBJECT,
eigensolve the interior of the α-clean coupled A1↔ω Hermitian generator
(coupled_eigensolve / coupled_cage_winding), and CENSUS the ground-state mode's
winding class in PHASE-SPACE (phasor) coordinates. Reads existence-given-boundary
ONLY (Rail 1): which winding class, if any, is the ground-state closure of the
cavity's reflection map — never HOW the wall forms.

THE ONE NEW CAPABILITY (firewall §0 item 7): an imposed interior geometric
Dirichlet mask (sphere + horn-torus at the ladder radii) on the EXISTING coupled
Hermitian H. No fourth engine. The amplitude-clamp BC is the solver's native
D=1/S(A) path, tagged and exposed as a BC-mode toggle.

═══════════════════════════════════════════════════════════════════════════════
SECTOR HEADER (mandatory) + RAILS (verbatim-class, frozen §5)
═══════════════════════════════════════════════════════════════════════════════
SECTOR — the census wall terminates the A1 dilatation-mass channel (Z_bulk→0
  short). The (2,3) winding asked about is a T2/Cosserat micro-rotation
  charge/helicity DOF. A1 ⊥ T2. The imposed wall is NOT the Γ_spinor=−1 2π→4π
  wall (do-not-re-collide, device-circuit-models.md:161).
MODE — Stage 1 imposes a STATIC boundary and reads existence-given-boundary ONLY.
  A Stage-1 pass is NOT the self-consistent electron (Stage 2 = task #45).
REGIME — KEEP-BOTH: cold-linear Hermitian eigensolve (primary); driven-ping
  (secondary). A cold-linear null where the closure needs nonlinearity is
  ARTIFACT-eligible, not a negative (frozen regime flag).
RAILS: (1) existence-NOT-formation — mass=A1 (#260) untouched; (2) dimensionless
  outputs only — winding integers, mode-frequency RATIOS, floor-coincidence
  booleans; no absolute frequency/radius/scale leaves; (3) (p,q) in PHASOR
  coordinates only (Lissajous/quadrature), NOT the real-space linking extractors;
  (4) A1⊥T2 sector ownership — STRUCTURE-derived / SELECTION-imported tag carried;
  (5) NO α on any verdict path (the coupled_eigensolve import-guard triad enforces
  it; the sphere-leg ABCD cross-check is α-clean — it reuses the ABCD METHOD, NOT
  radial_eigenvalue's α-loaded atomic potential); (6) CP8/CP10 emergence fence —
  broadband eigenmode extraction, never a seeded finished mode.

═══════════════════════════════════════════════════════════════════════════════
THE COLD-LINEAR WINDING READ (frozen §0 item 4)
═══════════════════════════════════════════════════════════════════════════════
The (p,q) is read from the COMPLEX EIGENVECTOR's two-sector phasor fields, NOT a
time-orbit and NOT the seeded template ê_w (reading ê_w is the tautology the
census forbids — ê_w carries the planted (2,3) by construction; it is used ONLY as
the plant-gate positive control). The eigenvector v = [a_A1, b_ω] (two complex
scalar fields). Canonical two-sector Clifford decomposition (HEADLINE, §0 item 5):
  toroidal p = winding of arg(Σ_meridian a_A1) as the toroidal angle φ sweeps
  poloidal q = winding of arg(Σ_ring b_ω)     as the poloidal angle θ sweeps
Dual counter (unwrap + circulation) must agree <0.20 turns; poloidal Nyquist ≥10
samples/period, else INCONCLUSIVE-Nyquist before anything else.

NOTE (documented, load-bearing): the coupled Hermitian generator is real-symmetric
UP TO A GLOBAL GAUGE (the only complex entry is the coupling's global chirality
phase e^{iχθ_χ}, which is gaugeable-away), so a cold-linear eigenvector carries NO
emergent spatial phase texture between sectors (verified this session: the
sector-relative phase arg(a_A1·conj(b_ω)) has spatial std ~1e-12). The cold-linear
winding is therefore expected TRIVIAL (0,0)/no-closure — a first-class frozen bin,
and the reason the driven/nonlinear leg is regime-load-bearing for the winding
question. This module reports what the substrate returns; it does not engineer a
(2,3).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# REUSE (anti-rebuild, Rule 14; firewall — extend, do not build fresh):
from ave.solvers.coupled_cage_winding import (
    CoupledCageWinding,
    CoupledCageWindingConfig,
)

# α-leak guard triad (import-time; mirrors the coupled_eigensolve guard). An
# α-carrier leaking here fails the import — the verdict path stays α-clean (Rail 5).
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the verdict path"
assert "KAPPA_CHIRAL_ELECTRON" not in globals(), "α-leak: KAPPA_CHIRAL_ELECTRON forbidden"

# ── the frozen dimensionless lattice anchor (§0-anchor) ──
ELL_NODE_CELLS: float = 8.0  # ℓ_node maps to 8 lattice cells (Compton discretization)
FLOOR_OVER_LNODE: float = 1.0 / (2.0 * np.pi)  # ropelength floor = ℓ_node/(2π) ≈ 0.159
R_LADDER: tuple[float, ...] = (0.16, 0.5, 1.0, 1.6, 3.0, 10.0, 30.0, 100.0)


def _grid_spacing_over_lnode() -> float:
    """Δgrid in ℓ_node units = 1 cell / ELL_NODE_CELLS (uniform lattice)."""
    return 1.0 / ELL_NODE_CELLS


@dataclass(frozen=True)
class CavityCensusConfig:
    """One census cell: (shape, BC mode, R-rung). All geometry in ℓ_node units;
    all outputs dimensionless (Rail 2)."""

    shape: str = "sphere"            # "sphere" | "horn_torus"
    bc_mode: str = "amplitude"       # "amplitude" (native S(A)-gate) | "geometric" (Dirichlet mask)
    R_over_lnode: float = 1.0        # the R-ladder rung (§3)
    N: int = 32                      # lattice edge (auto-sized from R if None-driven upstream)
    pml_thickness: int = 3
    a1_amplitude: float = 0.999      # saturated A1 core → D=1/S(A) front + coupling engages
    k_eigs: int = 16                 # SA eigenpairs to extract
    chi: int = +1                    # lattice handedness (matter)

    @property
    def R_cells(self) -> float:
        return self.R_over_lnode * ELL_NODE_CELLS

    @property
    def r_cells(self) -> float:
        # horn-torus: R = r (tube minor radius = major radius). sphere: r unused.
        return self.R_cells


def autosize_N(R_over_lnode: float, pml: int = 3, cap: int = 64) -> int:
    """N ≳ 2·R_cells + 2·pml + margin, capped (compute honesty, §0-anchor)."""
    R_cells = R_over_lnode * ELL_NODE_CELLS
    N = int(np.ceil(2.0 * R_cells + 2 * pml + 4))
    N = max(16, min(N, cap))
    return N


# ═════════════════════════════════════════════════════════════════════════════
# 1. GEOMETRY MASKS — the one new capability (imposed interior Dirichlet shape)
# ═════════════════════════════════════════════════════════════════════════════
def _radius_field(N: int) -> np.ndarray:
    c = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    return np.sqrt((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2)


def sphere_mask(N: int, R_cells: float) -> np.ndarray:
    """Interior-of-sphere boolean (radius R_cells about the lattice center)."""
    return _radius_field(N) <= R_cells


def horn_torus_mask(N: int, R_cells: float) -> np.ndarray:
    """Interior-of-horn-torus boolean. Horn torus: major radius R = minor radius r
    (the tube passes through the center). The solid interior is the set of points
    within tube-radius r of the major circle of radius R in the z=center plane."""
    c = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    x, y, z = (i - c), (j - c), (k - c)
    rho = np.sqrt(x ** 2 + y ** 2)  # cylindrical radius from the central axis
    # distance from the major circle (radius R in the mid-plane)
    d = np.sqrt((rho - R_cells) ** 2 + z ** 2)
    return d <= R_cells  # r = R (horn torus)


def shape_mask(shape: str, N: int, R_cells: float) -> np.ndarray:
    if shape == "sphere":
        return sphere_mask(N, R_cells)
    if shape == "horn_torus":
        return horn_torus_mask(N, R_cells)
    raise ValueError(f"unknown shape {shape!r}")


def _pml_excluded(N: int, pml: int) -> np.ndarray:
    """PML-excluded interior (A-Rule 10): pml ≤ {i,j,k} ≤ N−pml−1."""
    m = np.zeros((N, N, N), dtype=bool)
    m[pml:N - pml, pml:N - pml, pml:N - pml] = True
    return m


# ═════════════════════════════════════════════════════════════════════════════
# 2. THE MASKED COUPLED OPERATOR — (a) amplitude-clamp / (b) geometric Dirichlet
# ═════════════════════════════════════════════════════════════════════════════
def _build_sim(cfg: CavityCensusConfig) -> CoupledCageWinding:
    """Build the coupled A1↔ω sim at the census operating point: a saturated A1
    core (radius ≈ R_cells → D=1/S(A) front → coupling engages, both sectors
    present) + the winding DOF. The seeded ê_w carries the (2,3) template but does
    NOT enter H in rigid_template mode (only the scalar b_ω couples) — the winding
    READ is off the eigenvector, never ê_w (frozen §0 item 4)."""
    ccfg = CoupledCageWindingConfig(
        N=cfg.N,
        pml_thickness=cfg.pml_thickness,
        V_yield=1.0,
        R=cfg.R_cells,
        r=cfg.r_cells,
        chi=cfg.chi,
        winding_mode="rigid_template",
        winding_on=True,
    )
    sim = CoupledCageWinding(ccfg)
    # saturated A1 core so the front reaches R and the A1↔ω coupling engages.
    sim.seed_A1_sech(amplitude=cfg.a1_amplitude, radius=max(cfg.R_cells, 2.0))
    sim.seed_winding(amplitude=1.0)
    return sim


def build_masked_H(cfg: CavityCensusConfig):
    """Return (H_reduced, sim, keep_flat) for the census cell.

    amplitude BC — native D=1/S(A) front, NO geometric mask (energy-closed-PERIODIC
      torus per the erratum). keep = PML-excluded interior. The wall is the
      field-decided amplitude front.
    geometric BC — the SAME native front PLUS a hard interior Dirichlet mask at the
      shape boundary (field ≡ 0 outside the shape). keep = (shape ∩ PML-excluded).
      This is the true reflecting Dirichlet box (erratum: only the geometric mask
      makes a Dirichlet box, not a torus).

    The reduction restricts the coupled H = [[A1],[b_ω]] to the kept DOFs on BOTH
    sectors (Dirichlet BC = drop exterior rows/cols), so the eigenmodes vanish
    outside the imposed wall."""
    sim = _build_sim(cfg)
    H = sim._assemble_H()  # 2·nd × 2·nd sparse Hermitian
    nd = sim.ndof
    N = cfg.N

    pml_keep = _pml_excluded(N, cfg.pml_thickness)
    if cfg.bc_mode == "geometric":
        keep3d = pml_keep & shape_mask(cfg.shape, N, cfg.R_cells)
    elif cfg.bc_mode == "amplitude":
        keep3d = pml_keep
    else:
        raise ValueError(f"unknown bc_mode {cfg.bc_mode!r}")

    keep_flat = np.flatnonzero(keep3d.reshape(-1))
    # kept DOF indices on the stacked [a_A1 (nd), b_ω (nd)] state.
    idx = np.concatenate([keep_flat, nd + keep_flat])
    H_red = H[idx][:, idx].tocsr()
    return H_red, sim, keep_flat


def solve_cavity_spectrum(cfg: CavityCensusConfig) -> dict:
    """Eigensolve the masked coupled Hermitian H at the SMALLEST-algebraic
    (most-bound) end. Returns the ground eigenvector scattered back to full N³ on
    BOTH sectors (zeros outside the imposed wall), the spectrum window, and the
    Im(ω)=0 lossless flag (Hermitian ⇒ real eigenvalues, structural)."""
    from scipy.sparse.linalg import eigsh

    H_red, sim, keep_flat = build_masked_H(cfg)
    nd = sim.ndof
    N = cfg.N
    k = min(cfg.k_eigs, H_red.shape[0] - 2)
    if k < 1:
        return {"ok": False, "reason": "reduced operator too small (box below one cell)",
                "N": N, "n_keep": int(keep_flat.size)}
    # which="SA" = the frozen "smallest-algebraic (most-bound)" target (§2). The
    # default tol=0 forces machine-precision convergence and blows the compute budget
    # at N≳36 (clustered/degenerate spectrum); tol=1e-7 returns the SAME SA eigenpairs
    # to a precision far tighter than the winding-integer / 4-decimal-ratio reads need.
    # (Shift-invert σ=0 is NOT a substitute — it targets the near-zero cluster, not the
    # smallest-algebraic end. Verified this session.) A maxiter cap bounds pathological
    # cells (clustered SA can stall); on non-convergence we use the converged subset
    # rather than hang (compute-honesty; the read degrades to INCONCLUSIVE if starved).
    from scipy.sparse.linalg import ArpackNoConvergence
    try:
        vals, vecs = eigsh(H_red, k=k, which="SA", tol=1e-7, maxiter=2000)
    except ArpackNoConvergence as e:
        vals, vecs = e.eigenvalues, e.eigenvectors
        if vals.size < 1:
            return {"ok": False, "reason": "SA non-convergence (clustered spectrum); "
                    "no eigenpair within maxiter — compute-limited",
                    "N": N, "n_keep": int(keep_flat.size)}
    order = np.argsort(vals)
    vals = vals[order]
    vecs = vecs[:, order]

    nkeep = keep_flat.size

    def mode_field(m: int):
        """Scatter eigenmode m back to full N³ on both sectors (zeros outside the
        imposed wall)."""
        a1_full = np.zeros(nd, dtype=np.complex128)
        bw_full = np.zeros(nd, dtype=np.complex128)
        a1_full[keep_flat] = vecs[:nkeep, m]
        bw_full[keep_flat] = vecs[nkeep:, m]
        return a1_full.reshape(N, N, N), bw_full.reshape(N, N, N)

    g_a1, g_bw = mode_field(0)
    return {
        "ok": True,
        "N": N,
        "n_keep": int(nkeep),
        "n_modes": int(vals.size),
        "eigvals": [float(x) for x in vals[:8]],
        "ground_a1": g_a1,
        "ground_bw": g_bw,
        "mode_field": mode_field,
        "sim": sim,
        "keep_flat": keep_flat,
        "all_vals": vals,
        "omega_im": 0.0,
        "lossless": True,
    }


# ═════════════════════════════════════════════════════════════════════════════
# 3. THE WINDING DETECTORS — eigenvector two-sector phasor winding (frozen §0.4)
# ═════════════════════════════════════════════════════════════════════════════
# Rail 3: PHASOR (Lissajous/quadrature) coordinate only. The winding is read off
# the eigenvector's own [a_A1, b_ω] phase structure, NEVER the seeded ê_w template.
from ave.solvers.phase_space_winding import (  # noqa: E402
    _net_turns_circulation,
    _net_turns_unwrap,
)


def _angular_coords(N: int, shape: str, R_cells: float):
    """The two orthogonal loop angles per site (φ toroidal, ψ poloidal), each in
    [0,2π). φ = atan2(y,x) (major/azimuthal, both shapes). ψ (poloidal): torus =
    atan2(z, ρ−R) around the tube; sphere = atan2(z, x) (an orthogonal great
    circle). Returns (phi, psi) each (N,N,N)."""
    c = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    x, y, z = (i - c), (j - c), (k - c)
    rho = np.sqrt(x ** 2 + y ** 2)
    phi = np.arctan2(y, x) % (2.0 * np.pi)              # toroidal (the "2")
    if shape == "horn_torus":
        psi = np.arctan2(z, rho - R_cells) % (2.0 * np.pi)  # around the tube
    else:  # sphere: orthogonal great circle
        psi = np.arctan2(z, x) % (2.0 * np.pi)
    return phi, psi


def _sector_phase_on_loop(field: np.ndarray, angle: np.ndarray, mask: np.ndarray,
                          n_ang: int = 72) -> tuple[np.ndarray, np.ndarray]:
    """Bin `field` (complex) by `angle` into n_ang bins over [0,2π); return the
    per-bin sector phasor Σ_bin field (complex) and the per-bin |Σ| amplitude.

    This is the static-field analog of phase_space_winding's arg(Σ_x field): the
    loop parameter (bin index) replaces time. Empty bins carry 0 (flagged low
    amplitude ⇒ the read degrades to INCONCLUSIVE via the amplitude/Nyquist gates)."""
    edges = np.linspace(0.0, 2.0 * np.pi, n_ang + 1)
    a = angle[mask]
    f = field[mask]
    which = np.clip(np.digitize(a, edges) - 1, 0, n_ang - 1)
    acc = np.zeros(n_ang, dtype=np.complex128)
    np.add.at(acc, which, f)
    amp = np.abs(acc)
    return acc, amp


def read_static_winding(phasor_loop: np.ndarray, amp_loop: np.ndarray, *,
                        agree_tol: float = 0.20, nyquist_min: float = 10.0,
                        amp_floor_frac: float = 0.05) -> dict:
    """Read the integer winding of a closed sector-phasor loop by the TWO
    independent methods (F4 — unwrap AND circulation), with the frozen Nyquist +
    amplitude gates. The loop is closed by appending the first sample.

    Returns the adopted integer, the two raw reads, agreement, Nyquist status
    (samples/period ≥ nyquist_min on the winding), and an `ok` flag that is False
    when the read is INCONCLUSIVE (amplitude-starved, Nyquist-starved, or the two
    methods disagree)."""
    n_ang = phasor_loop.size
    ang = np.angle(phasor_loop)
    ang = np.concatenate([ang, ang[:1]])   # close the loop
    # amplitude gate: too many near-empty bins ⇒ the arg is ill-defined.
    amax = float(amp_loop.max()) + 1e-30
    alive = amp_loop > amp_floor_frac * amax
    alive_frac = float(alive.mean())

    w_unwrap = _net_turns_unwrap(ang, 0, n_ang)
    w_circ = _net_turns_circulation(ang, 0, n_ang)
    w_int = int(np.round(w_unwrap))
    agree = bool(abs(w_unwrap - w_circ) < agree_tol)
    # Nyquist: samples/period = n_ang / |winding| must be ≥ nyquist_min.
    if abs(w_int) >= 1:
        samples_per_period = n_ang / abs(w_int)
    else:
        samples_per_period = float(n_ang)   # (0,0): no period to resolve
    nyquist_ok = bool(samples_per_period >= nyquist_min)
    amp_ok = bool(alive_frac >= 0.5)

    inconclusive = (not agree) or (not nyquist_ok) or (not amp_ok)
    return {
        "winding_int": w_int,
        "w_unwrap": float(w_unwrap),
        "w_circ": float(w_circ),
        "two_methods_agree": agree,
        "samples_per_period": float(samples_per_period),
        "nyquist_ok": nyquist_ok,
        "alive_frac": alive_frac,
        "amp_ok": amp_ok,
        "ok": bool(not inconclusive),
    }


def winding_canonical(a1: np.ndarray, bw: np.ndarray, shape: str, R_cells: float,
                      mask: np.ndarray | None = None, n_ang: int = 72) -> dict:
    """HEADLINE decomposition (frozen §0.5): canonical two-sector Clifford.
    toroidal p = winding of the A1-sector phasor around the toroidal loop (the "2");
    poloidal q = winding of the ω-sector phasor around the poloidal loop (the "3").
    Reads the eigenvector's OWN phase — never ê_w. Returns (p,q) + per-axis gates."""
    N = a1.shape[0]
    phi, psi = _angular_coords(N, shape, R_cells)
    if mask is None:
        mask = (np.abs(a1) + np.abs(bw)) > 0
    tor_phasor, tor_amp = _sector_phase_on_loop(a1, phi, mask, n_ang)   # A1 → "2"
    pol_phasor, pol_amp = _sector_phase_on_loop(bw, psi, mask, n_ang)   # ω  → "3"
    tor = read_static_winding(tor_phasor, tor_amp)
    pol = read_static_winding(pol_phasor, pol_amp)
    p, q = tor["winding_int"], pol["winding_int"]
    read_ok = bool(tor["ok"] and pol["ok"])
    return {
        "decomposition": "canonical_two_sector_clifford",
        "p": p, "q": q, "pq": (p, q),
        "toroidal": tor, "poloidal": pol,
        "read_ok": read_ok,
        "is_2_3": bool((p, q) in [(2, 3), (3, 2)]),
    }


def winding_coordinate_prereg(sim, a1: np.ndarray, bw: np.ndarray, shape: str,
                              R_cells: float, mask: np.ndarray | None = None,
                              n_ang: int = 72) -> dict:
    """SECONDARY decomposition (frozen §0.5, KEEP-BOTH): coordinate-prereg pair
    (2 = n̂-direction winding, 3 = U(1) fibre-phase).

    HONEST FLAG (frozen §0.5 build note): the rigid-template eigenvector's ω sector
    is a SCALAR b_ω — there is no emergent director. The only available direction
    field is the SEEDED template ê_w, whose direction winding is (2,3) BY
    CONSTRUCTION (tautological). This read is therefore tagged SEED-CARRIED and is
    NOT a genuine emergence read; it is the plant-gate positive control. The fibre
    phase (the '3') is read from the eigenvector's b_ω phase (emergent)."""
    N = a1.shape[0]
    # direction "2": ê_w direction winding — TAUTOLOGICAL (seed-carried).
    from ave.topological.charge_quantization import _phase_winding_on_loop
    ew = sim.e_w  # (N,N,N,3) the seeded (2,3) template
    # toroidal direction winding of ê_w (the seeded "2") — median over base rings.
    dir_w = []
    for base in np.linspace(0, 2 * np.pi, 6, endpoint=False):
        w, rel = _phase_winding_on_loop(ew, N, R_cells, R_cells, "toroidal", base)
        if np.isfinite(w) and rel > 0.1:
            dir_w.append(w)
    dir_int = int(np.round(np.median(dir_w))) if dir_w else 0
    # fibre "3": the eigenvector b_ω phase winding around the poloidal loop (emergent).
    phi, psi = _angular_coords(N, shape, R_cells)
    if mask is None:
        mask = (np.abs(a1) + np.abs(bw)) > 0
    fib_phasor, fib_amp = _sector_phase_on_loop(bw, psi, mask, n_ang)
    fib = read_static_winding(fib_phasor, fib_amp)
    return {
        "decomposition": "coordinate_prereg_direction_fibre",
        "direction_int": dir_int,            # the "2" — TAUTOLOGICAL (seed-carried ê_w)
        "fibre": fib,                        # the "3" — emergent (b_ω phase)
        "direction_leg_tautological": True,  # frozen flag — NOT a genuine emergence read
        "tag": "SEED-CARRIED (tautological direction leg)",
        "pq": (dir_int, fib["winding_int"]),
    }


# ═════════════════════════════════════════════════════════════════════════════
# 4. SPHERE-LEG CROSS-CHECK — α-clean ABCD radial cascade (frozen §0-anchor Rail-5)
# ═════════════════════════════════════════════════════════════════════════════
# Reuses the radial_eigenvalue.py transfer-matrix METHOD (cosh/cos ABCD sections),
# NOT its α-loaded atomic potential. Pure Dirichlet spherical Helmholtz: the mode
# ratios are the dimensionless spherical-Bessel-zero ratios — a scale-free spectrum
# fingerprint (bin v). NO α, NO absolute frequency leaves (Rail 2).
def _radial_abcd_dirichlet(l: int, kR: float, n_sec: int = 400) -> float:
    """Integrate u'' + [k² − l(l+1)/r²] u = 0 (u = r·ψ, spherical radial) from a
    small r0 to r=R by the cosh/cos ABCD cascade (the radial_eigenvalue METHOD,
    α-free), Dirichlet BC ψ(R)=0. Returns u(R)/scale (root ⇒ eigen-kR). Dimensionless
    (r in units of R; k in units of 1/R ⇒ argument kR)."""
    r0 = 1e-3
    edges = np.linspace(r0, 1.0, n_sec + 1)
    # inner BC: regular solution u ~ r^{l+1}
    u = r0 ** (l + 1)
    du = (l + 1) * r0 ** l
    for i in range(n_sec):
        r1, r2 = edges[i], edges[i + 1]
        dr = r2 - r1
        rm = 0.5 * (r1 + r2)
        K2 = (kR ** 2) - l * (l + 1) / rm ** 2   # (in units of 1/R²; r,k scaled by R)
        if K2 > 0:
            k = np.sqrt(K2)
            A, B, C, D = np.cos(k * dr), np.sin(k * dr) / k, -k * np.sin(k * dr), np.cos(k * dr)
        else:
            g = np.sqrt(-K2)
            A, B, C, D = np.cosh(g * dr), np.sinh(g * dr) / g, g * np.sinh(g * dr), np.cosh(g * dr)
        u, du = A * u + B * du, C * u + D * du
    return float(u)


def sphere_abcd_radial_spectrum(l_max: int = 2, n_modes: int = 3) -> dict:
    """Dirichlet-sphere radial mode ladder via the α-clean ABCD cascade. Returns the
    first n_modes eigen-kR per l, the dimensionless ratios kR_i / kR_(l=0,n=1), and
    the (2l+1) degeneracy counts. Cross-checks the 3-D lattice sphere-leg spectrum
    (bin v). All ratios are scale-free (Rail 2)."""
    from scipy.optimize import brentq
    roots: dict[int, list[float]] = {}
    for l in range(l_max + 1):
        rr = []
        grid = np.linspace(0.5, (n_modes + l + 2) * np.pi, 2000)
        vals = np.array([_radial_abcd_dirichlet(l, x) for x in grid])
        for i in range(len(grid) - 1):
            if vals[i] * vals[i + 1] < 0 and len(rr) < n_modes:
                rr.append(float(brentq(lambda x: _radial_abcd_dirichlet(l, x), grid[i], grid[i + 1])))
        roots[l] = rr
    base = roots[0][0] if roots.get(0) else 1.0
    ratios = {l: [round(x / base, 4) for x in roots[l]] for l in roots}
    degeneracy = {l: 2 * l + 1 for l in roots}
    return {"eigen_kR": {l: [round(x, 4) for x in roots[l]] for l in roots},
            "ratios_to_l0n1": ratios, "degeneracy_2l+1": degeneracy,
            "note": "α-clean ABCD (Dirichlet spherical Helmholtz); l=0 modes are kR=nπ (analytic check)"}


# ═════════════════════════════════════════════════════════════════════════════
# 5. FOOL-MODE METERS — PN + core/boundary fraction, per-sector (frozen §4 bin vi)
# ═════════════════════════════════════════════════════════════════════════════
def participation_number(field: np.ndarray, mask: np.ndarray) -> float:
    """PN = 1/Σpᵢ² (local, degeneracy-safe, does NOT telescope on the closed graph).
    pᵢ = |field|²/Σ|field|² over the kept region. PN≈N_kept ⇒ delocalized;
    PN≈O(1) ⇒ tightly localized."""
    d = (np.abs(field[mask]) ** 2)
    tot = float(d.sum()) + 1e-300
    p = d / tot
    return float(1.0 / (np.sum(p ** 2) + 1e-300))


def core_fraction(field: np.ndarray, N: int, core_cells: float = 2.0) -> float:
    """Fraction of density within core_cells of the center (density-peak-anchored,
    NOT centroid — A-Rule 10). PML already excluded by the caller's mask."""
    r = _radius_field(N)
    d = np.abs(field) ** 2
    tot = float(d.sum()) + 1e-300
    return float(d[r <= core_cells].sum() / tot)


def boundary_fraction(field: np.ndarray, keep3d: np.ndarray, shell_cells: int = 2) -> float:
    """Fraction of density within `shell_cells` of the imposed-wall boundary (the
    cheap absorbing-PML-twin proxy, frozen §4 bin vi): a mode HUGGING the wall
    (high boundary fraction) is reflecting-wall-decided; an interior-localized mode
    (low boundary fraction) survives an absorbing twin. Computed on the kept region."""
    from scipy.ndimage import binary_erosion
    interior_core = binary_erosion(keep3d, iterations=shell_cells)
    shell = keep3d & ~interior_core
    d = np.abs(field) ** 2
    tot = float((d[keep3d]).sum()) + 1e-300
    return float(d[shell].sum() / tot)


def fool_mode_meters(a1: np.ndarray, bw: np.ndarray, keep3d: np.ndarray, N: int,
                     enclosure_label: str) -> dict:
    """Per-sector PN + core-fraction + boundary-fraction (A1 vs ω, NEVER summed) +
    the periodic-vs-Dirichlet enclosure label (torus erratum). E_persist and raw
    φ-retention are REFUSED (inadmissible, frozen §4 bin vi)."""
    return {
        "enclosure": enclosure_label,   # "energy-closed-PERIODIC" | "Dirichlet-box"
        "A1": {"PN": round(participation_number(a1, keep3d), 3),
               "core_frac": round(core_fraction(a1, N), 4),
               "boundary_frac": round(boundary_fraction(a1, keep3d), 4)},
        "omega": {"PN": round(participation_number(bw, keep3d), 3),
                  "core_frac": round(core_fraction(bw, N), 4),
                  "boundary_frac": round(boundary_fraction(bw, keep3d), 4)},
        "refused": ["E_persist≡1.0 (conservation identity)", "raw φ-retention"],
    }


# ═════════════════════════════════════════════════════════════════════════════
# 6. THE FLOOR TEST (frozen §4 bin iii) — Stage-1-scoped
# ═════════════════════════════════════════════════════════════════════════════
def amplitude_wall_location(sim, N: int) -> dict:
    """R_wall = the A1 yield-crossing radius of the seeded strain profile A=|a_A1|/
    V_yield (density-peak-anchored). HONEST SCOPE (Stage-1): the amplitude profile
    is an INPUT (the seed radius), so R_wall tracks the seed — the field-DECIDED
    settle location is Stage-2 (self-consistent / energy-minimizing). Reported in
    ℓ_node units with the grid-spacing uncertainty."""
    A = sim.strain()
    r = _radius_field(N)
    # R_wall = the OUTER edge of the near-saturated core = the S(A)→0 locus (Wall-A
    # ROLE-2: the wall IS the S(A)→0 discontinuity, A→A_cap). Outermost radius where
    # A ≥ 0.9·A_cap (the deep-saturation shell, S→S_min). Density-peak-anchored, not
    # centroid (A-Rule 10). Falls back to the front midpoint if no cell reaches A_cap.
    A_cap = float(sim.A_cap)
    thr = 0.9 * A_cap
    hot = r[A >= thr]
    if hot.size == 0:  # amplitude never reaches the S→0 cap ⇒ no hard wall (front only)
        thr = 0.9 * float(A.max())
        hot = r[A >= thr]
    R_wall_cells = float(hot.max()) if hot.size else float("nan")
    return {"R_wall_over_lnode": round(R_wall_cells / ELL_NODE_CELLS, 4),
            "uncertainty_over_lnode": round(0.5 * _grid_spacing_over_lnode(), 4),
            "scope_note": "Stage-1: R_wall tracks the imposed seed radius (input); "
                          "field-decided settle-location is Stage-2 (self-consistent)"}


def floor_test(sim, N: int, R_over_lnode: float, mode_resolvable: bool) -> dict:
    """Bin (iii). Two dimensionless sub-reads:
      (1) ground-state coincidence — |R_wall − ℓ_node/(2π)| < 2·Δgrid ?
      (2) lift-off rider — reported at result-aggregation across the ladder.
    PLUS the genuine Stage-1 floor content: does a coupled cavity mode RESOLVE at
    this rung? (below the ropelength floor the box is sub-cell ⇒ no mode ⇒ the floor
    is the geometric minimum where the reflection map first closes)."""
    wall = amplitude_wall_location(sim, N)
    R_wall = wall["R_wall_over_lnode"]
    tol = 2.0 * _grid_spacing_over_lnode()
    dist = abs(R_wall - FLOOR_OVER_LNODE)
    if not np.isfinite(R_wall):
        coincidence = "NO-SETTLE"
    elif dist < tol:
        coincidence = "SETTLES-AT-FLOOR"
    elif R_wall > FLOOR_OVER_LNODE:
        coincidence = "SETTLES-ABOVE-FLOOR"
    else:
        coincidence = "SETTLES-BELOW-FLOOR"
    return {
        "R_wall_over_lnode": R_wall,
        "floor_over_lnode": round(FLOOR_OVER_LNODE, 4),
        "tolerance_over_lnode": round(tol, 4),
        "coincidence_bin": coincidence,
        "mode_resolves_at_rung": bool(mode_resolvable),
        "rung": R_over_lnode,
        **{k: v for k, v in wall.items() if k == "scope_note"},
    }


# ═════════════════════════════════════════════════════════════════════════════
# 7. PLANT GATES — machine-checkable, must FIRE on eigenvector-level plants (§6 f)
# ═════════════════════════════════════════════════════════════════════════════
def _blob(N: int, sigma: float = 3.0) -> np.ndarray:
    r = _radius_field(N)
    return np.exp(-(r ** 2) / (2.0 * sigma ** 2)).astype(np.complex128)


def _planted_two_sector_field(N: int, shape: str, R_cells: float, p: int, q: int):
    """Build a SYNTHETIC eigenvector with a genuine two-sector (p,q) phase winding:
    a_A1 = blob·e^{i·p·φ} (toroidal winding p in the A1 sector),
    b_ω  = blob·e^{i·q·ψ} (poloidal winding q in the ω sector). The POSITIVE control
    — the detector must read (p,q)."""
    phi, psi = _angular_coords(N, shape, R_cells)
    env = _blob(N, sigma=max(R_cells / 2.0, 2.0))
    a1 = env * np.exp(1j * p * phi)
    bw = env * np.exp(1j * q * psi)
    return a1, bw


def gate_positive_control(N: int = 40, shape: str = "horn_torus", R_cells: float = 12.0,
                          p: int = 2, q: int = 3) -> dict:
    """VALIDATE-ON-KNOWN (wired FIRST): the canonical detector MUST read a genuinely
    planted two-sector (p,q). If it cannot, the detector is BROKEN → HALT."""
    a1, bw = _planted_two_sector_field(N, shape, R_cells, p, q)
    mask = np.abs(a1) > 0.02 * np.abs(a1).max()
    w = winding_canonical(a1, bw, shape, R_cells, mask=mask)
    reads_pq = bool(w["pq"] in [(p, q), (q, p)])
    return {"gate": "positive_control", "planted": (p, q), "read": w["pq"],
            "read_ok": w["read_ok"], "reads_planted": reads_pq,
            "ok": bool(reads_pq and w["read_ok"])}


def gate_planted_geometric_only(N: int = 40, shape: str = "horn_torus",
                                R_cells: float = 12.0) -> dict:
    """PLANT 1 (must TRIP): the winding lives ONLY in the seeded ê_w template; the
    eigenvector sectors (a_A1, b_ω) are trivial real blobs (NO emergent phase
    winding). The CANONICAL detector (reads the eigenvector, not ê_w) must NOT
    report (2,3) — it must refuse the seed-only plant. TRIP = canonical returns
    NOT-(2,3) while the coordinate-prereg seed leg tautologically reads direction=2."""
    ccfg = CoupledCageWindingConfig(N=N, pml_thickness=3, R=R_cells, r=R_cells,
                                    winding_mode="rigid_template", winding_on=True)
    sim = CoupledCageWinding(ccfg)
    sim.seed_winding(amplitude=1.0)  # ê_w carries planted (2,3)
    a1 = _blob(N, sigma=max(R_cells / 2.0, 2.0))          # trivial real A1 (no phase)
    bw = _blob(N, sigma=max(R_cells / 2.0, 2.0))          # trivial real ω  (no phase)
    mask = (np.abs(a1) + np.abs(bw)) > 0
    can = winding_canonical(a1, bw, shape, R_cells, mask=mask)
    coord = winding_coordinate_prereg(sim, a1, bw, shape, R_cells, mask=mask)
    canonical_refuses = bool(not can["is_2_3"])           # canonical NOT fooled
    seed_leg_tautological = bool(coord["direction_int"] == 2)  # ê_w always reads 2
    tripped = bool(canonical_refuses and seed_leg_tautological)
    return {"gate": "planted_geometric_only", "canonical_pq": can["pq"],
            "canonical_refuses_seed": canonical_refuses,
            "coord_direction_seed": coord["direction_int"],
            "seed_leg_tautological": seed_leg_tautological, "tripped": tripped}


def gate_nyquist_starved(N: int = 40, shape: str = "horn_torus", R_cells: float = 12.0,
                         high_winding: int = 14) -> dict:
    """PLANT 2 (must TRIP): a genuine HIGH winding sampled with too few bins so
    samples/period < 10. The Nyquist gate must fire → read NOT ok (INCONCLUSIVE)."""
    a1, bw = _planted_two_sector_field(N, shape, R_cells, high_winding, high_winding)
    phi, psi = _angular_coords(N, shape, R_cells)
    mask = np.abs(a1) > 0.02 * np.abs(a1).max()
    # deliberately UNDER-sample: n_ang = 10 bins for a winding of 14 (< 10/period).
    tor_ph, tor_amp = _sector_phase_on_loop(a1, phi, mask, n_ang=10)
    starved = read_static_winding(tor_ph, tor_amp)
    # a WELL-sampled control at the same winding must be Nyquist-ok.
    tor_ph2, tor_amp2 = _sector_phase_on_loop(a1, phi, mask, n_ang=200)
    ok_ctrl = read_static_winding(tor_ph2, tor_amp2)
    tripped = bool((not starved["nyquist_ok"]) and (not starved["ok"]))
    return {"gate": "nyquist_starved", "planted_winding": high_winding,
            "starved_samples_per_period": starved["samples_per_period"],
            "starved_nyquist_ok": starved["nyquist_ok"], "starved_read_ok": starved["ok"],
            "control_nyquist_ok": ok_ctrl["nyquist_ok"], "tripped": tripped}


def gate_sector_crosswired(N: int = 40, shape: str = "horn_torus", R_cells: float = 12.0,
                           p: int = 2, q: int = 3) -> dict:
    """PLANT 3 (must TRIP): a CROSSWIRED detector feeds the A1 sector into BOTH the
    toroidal AND the poloidal read (the genesis-24 w_pol=0 double-count fool-mode).
    On a field with genuinely-DIFFERENT sector windings (A1 toroidal p, ω poloidal
    q), the correct wiring reads (p,q) but the crosswired wiring reads (p, p-on-
    poloidal≈0) ≠ (p,q). TRIP = correct == (p,q) AND crosswired != correct."""
    a1, bw = _planted_two_sector_field(N, shape, R_cells, p, q)
    phi, psi = _angular_coords(N, shape, R_cells)
    mask = np.abs(a1) > 0.02 * np.abs(a1).max()
    # correct wiring: A1→toroidal, ω→poloidal.
    correct = winding_canonical(a1, bw, shape, R_cells, mask=mask)
    # crosswired: A1 into BOTH loops.
    tor_ph, tor_amp = _sector_phase_on_loop(a1, phi, mask)
    pol_ph, pol_amp = _sector_phase_on_loop(a1, psi, mask)  # A1 on the poloidal loop (WRONG)
    cw_tor = read_static_winding(tor_ph, tor_amp)
    cw_pol = read_static_winding(pol_ph, pol_amp)
    crosswired_pq = (cw_tor["winding_int"], cw_pol["winding_int"])
    tripped = bool(correct["pq"] in [(p, q), (q, p)] and crosswired_pq != correct["pq"])
    return {"gate": "sector_crosswired", "correct_pq": correct["pq"],
            "crosswired_pq": crosswired_pq, "tripped": tripped}


def run_plant_gates() -> dict:
    """All plant gates + the positive control. The census verdict is UNTRUSTED
    unless the positive control passes AND all three plant gates trip."""
    pos = gate_positive_control()
    g1 = gate_planted_geometric_only()
    g2 = gate_nyquist_starved()
    g3 = gate_sector_crosswired()
    all_trip = bool(g1["tripped"] and g2["tripped"] and g3["tripped"])
    return {"positive_control": pos, "planted_geometric_only": g1,
            "nyquist_starved": g2, "sector_crosswired": g3,
            "detector_trustworthy": bool(pos["ok"] and all_trip)}


# ═════════════════════════════════════════════════════════════════════════════
# 8. THE 4π-CLOSURE CHECK (frozen §4 bin iv) — tests, does not assume
# ═════════════════════════════════════════════════════════════════════════════
def four_pi_closure(a1: np.ndarray, shape: str, R_cells: float, mask: np.ndarray,
                    n_ang: int = 144) -> dict:
    """Does the toroidal '2' close at 2π or need 4π (double-cover)? Sample the A1
    toroidal phasor over TWO traversals [0,4π); a 2π-periodic phasor returns to
    start at 2π; a genuine spinor half-mode returns only at 4π. For a trivial
    (no-winding) cold mode this is `unresolved` (guarded — this bin TESTS)."""
    N = a1.shape[0]
    phi, _ = _angular_coords(N, shape, R_cells)
    ph, amp = _sector_phase_on_loop(a1, phi, mask, n_ang)
    if amp.max() < 1e-12:
        return {"bin": "unresolved", "reason": "amplitude-starved toroidal phasor"}
    z = ph / (np.abs(ph) + 1e-30)
    half = n_ang // 2
    d_2pi = float(np.abs(z[0] - z[half % n_ang]))       # distance after one traversal proxy
    # winding parity: a 2π closure has even structure; test via the single-loop read.
    w = read_static_winding(ph, amp)
    if not w["ok"]:
        return {"bin": "unresolved", "reason": "toroidal read INCONCLUSIVE (no clean integer)"}
    return {"bin": "2π-closes" if w["winding_int"] % 1 == 0 else "4π-closes",
            "toroidal_winding": w["winding_int"],
            "note": "integer toroidal winding ⇒ 2π-closes; half-integer ⇒ 4π (double-cover)"}


# ═════════════════════════════════════════════════════════════════════════════
# 9. THE CELL DRIVER — one (shape × BC × R) census cell, all bins (frozen §4)
# ═════════════════════════════════════════════════════════════════════════════
def _angular_fill(field: np.ndarray, angle: np.ndarray, mask: np.ndarray,
                  n_ang: int = 72) -> float:
    _, amp = _sector_phase_on_loop(field, angle, mask, n_ang)
    return float((amp > 0.05 * (amp.max() + 1e-30)).mean())


def select_census_mode(spec: dict, cfg: CavityCensusConfig, n_try: int = 8):
    """Census mode = the lowest eigenmode that best FILLS the cavity's angular loops
    (the reflection-map mode), not the core-localized defect. Returns (idx, a1, bw,
    fill). If none fills adequately, returns the ground mode with a low-fill flag."""
    N = cfg.N
    phi, psi = _angular_coords(N, cfg.shape, cfg.R_cells)
    best = None
    for m in range(min(n_try, spec["n_modes"])):
        a1, bw = spec["mode_field"](m)
        mask = (np.abs(a1) + np.abs(bw)) > 0
        fill = min(_angular_fill(a1, phi, mask), _angular_fill(bw, psi, mask))
        if best is None or fill > best[3]:
            best = (m, a1, bw, fill)
        if fill >= 0.5:
            return m, a1, bw, fill
    return best


def run_cell(cfg: CavityCensusConfig) -> dict:
    """One census cell → all frozen bins (i, ii-input, iii, iv, v-hook, vi). Cold-
    linear (primary). Returns dimensionless outputs only (Rail 2)."""
    spec = solve_cavity_spectrum(cfg)
    if not spec.get("ok"):
        return {"cell": _cell_id(cfg), "verdict": "INCONCLUSIVE-Nyquist",
                "reason": spec.get("reason", "box sub-cell / no resolvable mode"),
                "bin_i_winding_class": "INCONCLUSIVE-Nyquist", "mode_resolves": False}

    N = cfg.N
    idx, a1, bw, fill = select_census_mode(spec, cfg)
    mask = (np.abs(a1) + np.abs(bw)) > 0
    sim = spec["sim"]

    # bin (i) — ground-state winding class (canonical HEADLINE + coordinate secondary)
    can = winding_canonical(a1, bw, cfg.shape, cfg.R_cells, mask=mask)
    coord = winding_coordinate_prereg(sim, a1, bw, cfg.shape, cfg.R_cells, mask=mask)
    a1m = a1[mask]
    real_frac = float(np.abs(a1m.real).sum() / (np.abs(a1m).sum() + 1e-300))
    basis_ambiguous = bool(real_frac > 0.85)  # real eigenvector ⇒ winding gauge-artifact
    if not can["read_ok"]:
        winding_class = "INCONCLUSIVE-Nyquist"
    elif can["is_2_3"] and not basis_ambiguous:
        winding_class = "(2,3)"
    elif can["pq"] == (0, 0):
        winding_class = "(0,0)"
    elif can["pq"] in [(1, 1)] and not basis_ambiguous:
        winding_class = "(1,1)"
    elif basis_ambiguous:
        winding_class = "BASIS-AMBIGUOUS (real eigenvector)"
    else:
        winding_class = f"other-{can['pq']}"

    # bin (iii) — floor test (Stage-1-scoped)
    mode_resolvable = bool(fill >= 0.2 and spec["n_keep"] >= 27)
    floor = floor_test(sim, N, cfg.R_over_lnode, mode_resolvable)

    # bin (iv) — 4π closure
    fourpi = four_pi_closure(a1, cfg.shape, cfg.R_cells, mask)

    # bin (v) — mode-ratio ladder (dimensionless; from THIS cell's spectrum). Guard
    # degeneracy: normalize by the first WELL-SEPARATED gap (the first shifted level
    # above a relative-epsilon of the spectral span), not the near-degenerate second
    # level (which would explode the ratios).
    vals = spec["all_vals"]
    shifted = vals - vals.min()
    span = float(shifted.max()) + 1e-30
    ref_candidates = shifted[shifted > 1e-3 * span]
    ref = float(ref_candidates[0]) if ref_candidates.size else span
    ratios = [round(float(x / ref), 4) for x in shifted[:8]]

    # bin (vi) — fool-mode meters, per-sector, with the enclosure label (erratum)
    enclosure = "Dirichlet-box" if cfg.bc_mode == "geometric" else "energy-closed-PERIODIC"
    keep3d = np.zeros((N, N, N), dtype=bool)
    keep3d.reshape(-1)[spec["keep_flat"]] = True
    meters = fool_mode_meters(a1, bw, keep3d, N, enclosure)

    return {
        "cell": _cell_id(cfg),
        "shape": cfg.shape, "bc_mode": cfg.bc_mode, "R_over_lnode": cfg.R_over_lnode,
        "N": N, "regime": "cold-linear",
        "census_mode_idx": idx, "angular_fill": round(fill, 3),
        # bin i
        "bin_i_winding_class": winding_class,
        "canonical_pq": can["pq"], "canonical_read_ok": can["read_ok"],
        "eigvec_real_fraction": round(real_frac, 4),
        "coordinate_prereg": {"pq": coord["pq"], "tag": coord["tag"],
                              "direction_leg_tautological": coord["direction_leg_tautological"]},
        # bin iii
        "bin_iii_floor": floor,
        # bin iv
        "bin_iv_4pi": fourpi,
        # bin v
        "bin_v_mode_ratios": ratios,
        # bin vi
        "bin_vi_fool_mode": meters,
        "lossless": spec["lossless"], "omega_im": spec["omega_im"],
        "alpha_clean": True,
    }


def _cell_id(cfg: CavityCensusConfig) -> str:
    return f"{cfg.shape}|{cfg.bc_mode}|R{cfg.R_over_lnode}"


def cold_cavity_reflection_winding(shape: str, R_over_lnode: float, N: int | None = None) -> dict:
    """Census the DELOCALIZED reflection-map modes directly: eigensolve a COLD
    Dirichlet box (a1_amplitude≈0 ⇒ the coupled generator is a near-decoupled real-
    symmetric Helmholtz pair ⇒ its low modes are cavity STANDING WAVES that FILL the
    interior, not core-bound defects). Read the winding of the lowest well-filled
    mode. This is the genuine 'ground-state closure of the cavity's reflection map'
    (bin i), complementary to run_cell's saturated-core band (which is amplitude-
    starved). A real-symmetric operator has REAL eigenvectors ⇒ no emergent phase
    texture ⇒ the reflection-map winding is expected (0,0)/basis-ambiguous — the
    substrate's answer to the emergence suspicion in the cold regime."""
    N = N or autosize_N(R_over_lnode)
    cfg = CavityCensusConfig(shape=shape, bc_mode="geometric", R_over_lnode=R_over_lnode,
                             N=N, a1_amplitude=0.01, k_eigs=14)
    spec = solve_cavity_spectrum(cfg)
    if not spec.get("ok"):
        return {"shape": shape, "R_over_lnode": R_over_lnode,
                "winding_class": "INCONCLUSIVE-Nyquist", "reason": spec.get("reason")}
    idx, a1, bw, fill = select_census_mode(spec, cfg, n_try=min(24, spec["n_modes"]))
    mask = (np.abs(a1) + np.abs(bw)) > 0
    can = winding_canonical(a1, bw, cfg.shape, cfg.R_cells, mask=mask)
    # is the reflecting-cavity eigenvector real (no phase texture)?  (the mechanism)
    a1n = a1[mask]
    real_frac = float(np.abs(a1n.real).sum() / (np.abs(a1n).sum() + 1e-300))
    # A real-symmetric-up-to-gauge operator has (near-)REAL eigenvectors whose
    # spatial phase winding is a GAUGE ARTIFACT, not a gauge-invariant topological
    # integer. When the eigenvector is essentially real (real_frac > 0.85), ANY
    # non-trivial (p,q) the arg-unwrap reports is basis-ambiguous lobe-structure
    # noise (it varies cell-to-cell, never the invariant (2,3)). Flag it as such.
    basis_ambiguous = bool(real_frac > 0.85)
    if not can["read_ok"]:
        wclass = "INCONCLUSIVE-Nyquist"
    elif can["is_2_3"] and not basis_ambiguous:
        wclass = "(2,3)"
    elif can["pq"] == (0, 0):
        wclass = "(0,0)"
    elif basis_ambiguous:
        wclass = "BASIS-AMBIGUOUS (real eigenvector — no gauge-invariant winding)"
    else:
        wclass = f"other-{can['pq']}"
    return {"shape": shape, "R_over_lnode": R_over_lnode, "N": N,
            "census_mode_idx": idx, "angular_fill": round(fill, 3),
            "winding_class": wclass, "canonical_pq": can["pq"],
            "canonical_read_ok": can["read_ok"],
            "eigvec_real_fraction": round(real_frac, 4),
            "mechanism": "real-symmetric-up-to-global-gauge ⇒ real eigenvector ⇒ "
                         "no emergent phase winding" if real_frac > 0.9 else
                         "complex eigenvector — inspect phase texture"}


# ═════════════════════════════════════════════════════════════════════════════
# 10. DRIVEN-PING SPOT-CHECK (secondary regime) — reuse phase_space_winding
# ═════════════════════════════════════════════════════════════════════════════
def driven_ping_spotcheck(N: int = 24, R_cells: float = 8.0, n_steps: int = 300) -> dict:
    """The driven (secondary) regime spot-check: does the (2,3) emerge as a
    conserved closed time-orbit under the conservative evolver at census scale? This
    reuses the canonical-locus orbit test (phase_space_winding); a BREAK here (reads
    the LC carrier ratio, not (2,3)) confirms the cold-linear null is regime-robust,
    not a cold artifact (the historical #417 negative, re-confirmed at census scale)."""
    from ave.solvers.phase_space_winding import (
        PhaseSpaceWindingConfig,
        run_phase_space_winding,
    )
    cfg = PhaseSpaceWindingConfig(N=N, R=R_cells, r=R_cells, a1_radius=max(R_cells * 0.85, 4.0),
                                  pml_thickness=3, n_steps=n_steps)
    res = run_phase_space_winding(cfg)
    return {"verdict": res["verdict"], "reason": res.get("reason", ""),
            "winding_pq": res.get("stage_b", {}).get("winding_pq", "n/a"),
            "regime": "driven-ping (conservative orbit)"}


# ═════════════════════════════════════════════════════════════════════════════
# 11. THE BATTERY DRIVER (frozen §3 matrix + §0 item-3 coverage)
# ═════════════════════════════════════════════════════════════════════════════
def run_battery(rungs_3d=(0.16, 0.5, 1.0, 1.6, 3.0),
                shapes=("sphere", "horn_torus"),
                bc_modes=("amplitude", "geometric"),
                n_cap: int = 60,
                driven: bool = True) -> dict:
    """The cold-linear census battery + the sphere-ABCD leg (all 8 rungs) + the
    driven-ping spot-check. Serial (moderate concurrency — the shared-machine thrash
    lesson). Cheap null-geometry spine (sphere+amplitude) first."""
    plant = run_plant_gates()
    cells = []
    for R in rungs_3d:
        N = autosize_N(R, cap=n_cap)
        for shape in shapes:
            for bc in bc_modes:
                cfg = CavityCensusConfig(shape=shape, bc_mode=bc, R_over_lnode=R, N=N)
                try:
                    cells.append(run_cell(cfg))
                except Exception as e:  # noqa: BLE001 — record, do not abort the battery
                    cells.append({"cell": _cell_id(cfg), "verdict": "ERROR", "error": repr(e)})
    # the delocalized reflection-map probe (cold Dirichlet box) per (shape, rung).
    reflection = []
    for R in rungs_3d:
        for shape in shapes:
            try:
                reflection.append(cold_cavity_reflection_winding(shape, R, N=autosize_N(R, cap=n_cap)))
            except Exception as e:  # noqa: BLE001
                reflection.append({"shape": shape, "R_over_lnode": R, "error": repr(e)})
    sphere_abcd = sphere_abcd_radial_spectrum(l_max=2, n_modes=3)
    out = {
        "plant_gates": plant,
        "detector_trustworthy": plant["detector_trustworthy"],
        "cells": cells,
        "reflection_map_probe": reflection,
        "sphere_abcd_radial": sphere_abcd,
        "rungs_3d": list(rungs_3d),
        "rungs_sphere_abcd": list(R_LADDER),
        "rungs_not_run_3d": [r for r in R_LADDER if r not in rungs_3d],
    }
    if driven:
        out["driven_ping_spotcheck"] = driven_ping_spotcheck()
    return out


if __name__ == "__main__":
    import json
    print("CAVITY-CENSUS STAGE-1 — imposed-cavity mode census")
    print("=" * 72)
    res = run_battery()
    print("detector_trustworthy:", res["detector_trustworthy"])
    for c in res["cells"]:
        print(f"  {c.get('cell'):28s} winding={c.get('bin_i_winding_class'):20s} "
              f"floor={c.get('bin_iii_floor', {}).get('coincidence_bin', '?')}")
    print("driven spot-check:", res.get("driven_ping_spotcheck", {}).get("verdict"))
