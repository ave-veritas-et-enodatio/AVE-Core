"""P1a — the CHIRAL srs z=3 RE-HOMING of the A1 cage + the ω Cosserat winding.

Branch: engine/p1a-carrier-unification (off engine/p0-unified-dynamic).
Design driver: the carrier-unification make-or-break — collapse the TWO
K4-family carriers P0 left (the srs z=3 free-photon carrier + the diamond z=4
A1/ω carrier) onto ONE literal chiral z=3 srs node list.

═══════════════════════════════════════════════════════════════════════════════
WHY chiral srs (Decision-1 ratified)
═══════════════════════════════════════════════════════════════════════════════
The soliton's charge IS a handed (2,3) winding. The achiral diamond (z=4,
inversion-symmetric Fd-3m) CANNOT carry handedness — its writhe pseudoscalar
vanishes identically (net_ring_writhe == 0 on the centrosymmetric net). Only the
chiral srs (z=3, I4₁32/I4₃32, NO inversion centre) carries the winding handedness
= charge / spin / parity / optical-activity. So the A1/ω MUST live on chiral srs,
NOT on the diamond z=4 TETRA_OFFSETS stencil the P0 carriers used.

═══════════════════════════════════════════════════════════════════════════════
THE RE-HOMING (Rule-14: ADAPT the certified cores, do NOT rebuild from scratch)
═══════════════════════════════════════════════════════════════════════════════
The diamond carriers (ave.solvers.native_cage_imex / coupled_cage_winding) build
the cage Grad/Div from TETRA_OFFSETS — the 4 body-diagonal struts (z=4) — via
global roll-permutations on a regular N³ cube. The srs net is z=3 (3 struts/node)
with NODES at irregular Wyckoff-8a positions. So the cage / winding Grad/Div must
be ADAPTED z=4 → z=3:

  * the srs-native L_native (this module) reuses the SAME native-graph divergence-
    form Laplacian L = Bᵀ·diag(D_bond)·B that ave.solvers.fork_b_saturation_tank
    already builds on build_srs_net's connectivity (the per-bond varactor
    stiffness D_bond = 1/S(A_bond), the SAME α-clean kernel). This is the srs
    z=3 generalisation of the diamond assemble_L_D — same physical operator
    (adjoint_div(D·grad)), on the lattice's OWN bond graph (z=3), NOT a Cartesian
    embedding and NOT the TETRA z=4 stencil.
  * the CN/Cayley unitary stepper STRUCTURE is reused verbatim from
    coupled_cage_winding (the energy-conserving (I+i·dt/2·H) solve); only the
    L_native blocks are swapped from the z=4 TETRA assemble_L_D to the z=3 srs
    graph Laplacian assembled here.
  * the winding seed + the integer reader are RE-HOMED onto the srs NODE CLOUD:
    the (2,3) phase field θ = pφ + qψ is evaluated at the srs node real-space
    positions (the SAME formula seed_pq_winding uses on the cube), and the integer
    is read by a srs-native IDW toroidal sampler (the z=3 analog of
    compute_Q_link's grid trilinear sampler).

═══════════════════════════════════════════════════════════════════════════════
WHAT CHANGED (z=4 → z=3) — the honest strut-count + operator delta
═══════════════════════════════════════════════════════════════════════════════
  diamond carrier (P0)                  srs carrier (P1a, this module)
  ──────────────────────────────       ────────────────────────────────────────
  TETRA_OFFSETS (4 body-diagonals)  →  build_srs_net neighbours (3 struts/node)
  z = 4                             →  z = 3
  global roll-permutation on N³     →  per-node bond graph (LatticeNet.neighbors)
  assemble_L_D (Div·diag(D)·Grad)   →  Bᵀ·diag(D_bond)·B (graph Laplacian)
  achiral (inversion-symmetric)     →  CHIRAL (writhe ≠ 0, sign-flips L/R)
  winding read on N³ trilinear grid →  winding read by srs-node IDW sampler

═══════════════════════════════════════════════════════════════════════════════
GENESIS-24 GUARD (unchanged) — ω is its OWN DOF, NEVER grad(V)
═══════════════════════════════════════════════════════════════════════════════
A1 (= MASS, the longitudinal dilatation "3") and ω (= CHARGE/helicity (2,3)
winding) are SEPARATELY seeded, SEPARATELY conserved. ω is seeded at the srs node
positions by the (p,q) phase field, NEVER read off a_A1. The energy gate certifies
BOTH the A1-norm AND the ω grade — a "pin" cannot be bought by bleeding the
winding into the scalar.

α-CLEAN: κ̃=6/5 and θ_χ=2π·ν_vac (ν_vac=2/7) carried verbatim from
coupled_cage_winding (NO ALPHA / Q_TANK / V_SNAP / KAPPA_CHIRAL_ELECTRON on the
chord path). Same import-guard triad re-asserted below.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# α-FREE: the SAME validated kernel the diamond carriers use (G1-G8 unchanged).
from ave.solvers.graded_vacuum_network import saturation_kernel, stiffness_profile

# the chiral srs net + its native connectivity (the free-mode carrier's net).
from ave.core.chiral_lattice import LatticeNet, build_srs_net

# the real-space (2,3) winding seed formula (the SAME coordinate compute_Q_link
# reads) — used here to evaluate the phase field at srs node positions.
# (seed_pq_winding itself rasters onto a cube; we re-home the FORMULA onto nodes.)

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard triad (import-time; extends the coupled-carrier guards onto srs).
# An α-carrier leaking here fails the import. The leak is the signal.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "α-leak: ELECTRON instance must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the chord path"
assert "KAPPA_CHIRAL_ELECTRON" not in globals(), "α-leak: KAPPA_CHIRAL_ELECTRON (=α·κ̃) forbidden"
assert "RHO_BULK" not in globals(), "second-leak: bare RHO_BULK magnitude must NOT be imported"

# ── the α-FREE coupling inputs (named once; routed via the winding host) ──
from tests.engine_acceptance._winding_host import winding_kappa_tilde  # noqa: E402

KAPPA_TILDE: float = winding_kappa_tilde(2, 3)  # = 6/5, α-free
NU_VAC: float = 2.0 / 7.0                        # α-free lattice chirality fraction
THETA_CHI: float = 2.0 * np.pi * NU_VAC


# ═════════════════════════════════════════════════════════════════════════════
# srs-NATIVE Grad / Div / L_native (the z=3 ADAPTATION of the z=4 TETRA operator)
# ═════════════════════════════════════════════════════════════════════════════
def unique_bonds(net: LatticeNet) -> list[tuple[int, int]]:
    """The undirected unique bonds (u<v) of the srs connect-map. Built from
    net.neighbors (the lattice's OWN z=3 adjacency), NEVER a Cartesian distance
    posit. (Reuses the fork_b_saturation_tank pattern — native connect-map.)"""
    N = net.n_nodes
    return sorted({(min(u, v), max(u, v)) for u in range(N) for v in net.neighbors[u]})


def build_incidence(net: LatticeNet):
    """Signed node-bond incidence B (n_bonds × n_nodes), sparse: B[b,u]=+1,
    B[b,v]=−1 for bond (u,v). The srs-native discrete gradient operator (∇ on the
    z=3 bond graph). Its adjoint Bᵀ is the divergence. This is the z=3 analog of
    native_cage_imex.build_grad_div_periodic (which built Grad/Div from the z=4
    TETRA_OFFSETS roll-permutations); here the struts ARE the srs bonds (3/node)."""
    from scipy import sparse

    bonds = unique_bonds(net)
    nb = len(bonds)
    rows = np.empty(2 * nb, dtype=np.int64)
    cols = np.empty(2 * nb, dtype=np.int64)
    vals = np.empty(2 * nb, dtype=np.float64)
    for b, (u, v) in enumerate(bonds):
        rows[2 * b] = b
        cols[2 * b] = u
        vals[2 * b] = +1.0
        rows[2 * b + 1] = b
        cols[2 * b + 1] = v
        vals[2 * b + 1] = -1.0
    B = sparse.csr_matrix((vals, (rows, cols)), shape=(nb, net.n_nodes))
    return B, bonds


def assemble_L_srs(B, bonds, D_node: np.ndarray):
    """L_srs = Bᵀ·diag(D_bond)·B — the srs-native divergence-form stiffness
    Laplacian (the z=3 analog of native_cage_imex.assemble_L_D). The per-node
    stiffness D=1/S(A) is folded to per-bond by D_bond = max(D_u, D_v) (the bond
    is as stiff as its stiffest endpoint — the SAME convention fork_b uses for
    the saturated core). Real symmetric PSD; the constant mode is the nullspace
    (∇ of a constant = 0). NOT a Cartesian embedding, NOT the TETRA z=4 stencil —
    the stencil IS the chiral srs connect-map (structural-null-stencil-lens
    satisfied)."""
    from scipy import sparse

    D_node = np.asarray(D_node, dtype=float).reshape(-1)
    D_bond = np.array([max(D_node[u], D_node[v]) for (u, v) in bonds], dtype=float)
    Dexp = sparse.diags(D_bond)
    L = (B.T @ Dexp @ B).tocsr()
    return (0.5 * (L + L.T)).tocsr()  # enforce exact symmetry


# ═════════════════════════════════════════════════════════════════════════════
# srs-NODE (2,3) winding seed + the srs-native integer reader (RE-HOMED off N³)
# ═════════════════════════════════════════════════════════════════════════════
def seed_pq_winding_on_srs(
    net: LatticeNet, p: int, q: int, R: float, r: float, *,
    frame_N: int, amplitude_scale: float = 1.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Evaluate the (p,q) winding phase field θ = pφ + qψ AT the srs node real-
    space positions (the SAME hedgehog-envelope formula seed_pq_winding uses on
    the cube, charge_quantization.py:486-511 — re-homed onto the node cloud,
    NOT rasterised). Returns (omega_nodes (n_nodes,3), env (n_nodes,)).

    The torus (R,r) is specified in the SAME frame_N cube-frame the diamond
    carrier uses; srs node positions are mapped into that frame so the (2,3)
    geometry is identical. This is the genesis-24-clean ω seed (its OWN DOF)."""
    box = net.box
    g = net.pos / box * frame_N        # srs positions in the cube frame [0,frame_N)
    c = (frame_N - 1) / 2.0
    x, y, z = g[:, 0] - c, g[:, 1] - c, g[:, 2] - c
    rho = np.sqrt(x ** 2 + y ** 2)
    rtube = np.sqrt((rho - R) ** 2 + z ** 2)
    phi = np.arctan2(y, x)
    psi = np.arctan2(z, rho - R)
    r_opt = r if r > 0 else 1.0
    env = amplitude_scale * (np.sqrt(3.0) / 2.0) * np.pi / (1.0 + (rtube / r_opt) ** 2)
    theta = p * phi + q * psi
    omega = np.zeros((net.n_nodes, 3), dtype=np.float64)
    omega[:, 0] = env * np.cos(theta)
    omega[:, 1] = env * np.sin(theta)
    return omega, env


def compute_Q_link_srs(
    net: LatticeNet, omega_nodes: np.ndarray, R: float, r: float, *,
    frame_N: int, n_loops: int = 8, n_ang: int = 720, k_idw: int = 4,
) -> dict:
    """Read the (p,q) winding integer off the ω field carried on srs NODES — the
    z=3 srs-native analog of charge_quantization.compute_Q_link (which sampled an
    N³ grid by alive-weighted trilinear). Here the torus loops are sampled by
    inverse-distance-weighted (IDW) interpolation over the k nearest srs nodes
    (a KD-tree on the periodic node cloud), then arg(ω_⊥) is unwrapped.

    Returns {Q_link (poloidal=q), w_tor (toroidal=p), Q_link_raw, w_tor_raw,
    sign, w_pol_rel, w_tor_rel} — the SAME keys compute_Q_link returns, so the
    winding-reader role is a drop-in on the srs carrier. REAL-SPACE ω-grade only
    (GUARD 2/4 preserved)."""
    from scipy.spatial import cKDTree

    box = net.box
    tree = cKDTree(net.pos, boxsize=box)
    c = (frame_N - 1) / 2.0
    bases = np.linspace(0.0, 2.0 * np.pi, n_loops, endpoint=False)
    angs = np.linspace(0.0, 2.0 * np.pi, n_ang, endpoint=False)

    def _torus_pt(base, ang, kind):
        if kind == "poloidal":
            phi, psi = base, ang
        else:
            phi, psi = ang, base
        rad = R + r * np.cos(psi)
        gx = c + rad * np.cos(phi)
        gy = c + rad * np.sin(phi)
        gz = c + r * np.sin(psi)
        return np.array([gx, gy, gz]) / frame_N * box  # cube-frame → srs real space

    def _winding(kind):
        ws, rels = [], []
        for base in bases:
            phases = np.full(n_ang, np.nan)
            amps = np.zeros(n_ang)
            for a, ang in enumerate(angs):
                pt = _torus_pt(base, ang, kind)
                d, idx = tree.query(pt, k=k_idw)
                wt = 1.0 / (d + 1e-9)
                wt /= wt.sum()
                v = (wt[:, None] * omega_nodes[idx]).sum(axis=0)
                phases[a] = np.arctan2(v[1], v[0])
                amps[a] = float(np.hypot(v[0], v[1]))
            ok = np.isfinite(phases) & (amps > 1e-9)
            if ok.sum() < 16:
                continue
            ph = np.unwrap(phases[ok])
            ws.append((ph[-1] - ph[0]) / (2.0 * np.pi))
            rels.append(float(amps[ok].mean() / (amps[ok].max() + 1e-30)))
        return ws, rels

    pol_w, pol_rel = _winding("poloidal")
    tor_w, tor_rel = _winding("toroidal")
    Q_raw = float(np.median(pol_w)) if pol_w else 0.0
    w_tor_raw = float(np.median(tor_w)) if tor_w else 0.0
    Q_int = int(np.round(Q_raw)) if pol_w else 0
    w_tor_int = int(np.round(w_tor_raw)) if tor_w else 0
    return {
        "Q_link": Q_int,
        "Q_link_raw": Q_raw,
        "w_tor": w_tor_int,
        "w_tor_raw": w_tor_raw,
        "sign": int(np.sign(Q_int)) if Q_int != 0 else 0,
        "w_pol_rel": float(np.median(pol_rel)) if pol_rel else 0.0,
        "w_tor_rel": float(np.median(tor_rel)) if tor_rel else 0.0,
    }


def front_gate(A: np.ndarray, *, center: float = 4.0 / 7.0, width: float = 0.18) -> np.ndarray:
    """g_front(A): a thin shell at the Non-Linear→Saturated boundary — the
    saturation-FRONT window where the A1↔ω coupling ENGAGES (zero in cold vacuum
    A→0 AND in the deep frozen core A→1). center = R_II = 4/7 (α-free, the SAME
    shell coupled_cage_winding.front_gate uses; verbatim per Rule-14)."""
    return np.exp(-((A - center) ** 2) / (2.0 * width ** 2))


def _strain(absV: np.ndarray, V_yield: float, A_cap: float) -> np.ndarray:
    """A = |V|/V_yield, clipped to A_cap (avoids the S=0 singularity)."""
    return np.minimum(absV / V_yield, A_cap)


# ═════════════════════════════════════════════════════════════════════════════
# THE COUPLED A1↔ω CARRIER, RE-HOMED ONTO THE CHIRAL srs z=3 NODE LIST.
# The CN/Cayley unitary stepper STRUCTURE is adapted verbatim from
# ave.solvers.coupled_cage_winding (Rule-14); the ONLY change is the L_native
# block: the z=4 TETRA assemble_L_D is swapped for the z=3 srs assemble_L_srs.
# ═════════════════════════════════════════════════════════════════════════════
@dataclass(frozen=True)
class SrsCageWindingConfig:
    """Frozen P1a srs coupled-cage config (α-free). Mirrors
    CoupledCageWindingConfig but on the chiral srs net (L = srs supercell edge,
    NOT the diamond N³ cube). frame_N is the cube-frame the (R,r) torus is
    specified in (so the (2,3) geometry matches the diamond carrier exactly)."""

    L: int = 12                     # srs supercell edge (z=3, chiral)
    enantiomorph: str = "right"     # I4₁32 (matter) — sign-flips charge for "left"
    frame_N: int = 32               # cube-frame for the (R,r) torus + readout
    V_yield: float = 1.0
    exponent: float = 0.5           # Op14 saturation (√S primary)
    S_min: float = 1e-3
    A_cap: float = 0.999
    c_A1: float = 1.0               # A1 cold dispersion speed
    c_omega_b: float = 1.0          # ω LC-amplitude dispersion speed
    omega_b: float = 1.0            # A1 breather frequency
    omega_s: float = 1.0            # ω-tank LC frequency (resonant)
    rate: float = 0.3               # the coupling rate scale (× g_front × S)
    chi: int = +1                   # lattice handedness (matter)
    gate: str = "front"             # saturation-front-gated coupling PORT
    R: float = 7.0                  # (2,3) torus major radius (cube-frame)
    r: float = 2.3                  # (2,3) torus minor radius (cube-frame)
    dt: float = 0.066               # accuracy-set (production dt)
    gmres_tol: float = 1e-10
    gmres_maxiter: int = 2000
    winding_on: bool = True         # winding OFF ⇒ Ω≡0 ⇒ A1-alone control


class SrsCageWinding:
    """The COUPLED real-space A1↔ω PDE re-homed onto the CHIRAL srs z=3 net.

    State (complex analytic signals, on the srs node list):
      self.a_A1 : (n_nodes,) complex  — the A1 bulk-dilatation breather (MASS).
      self.b_w  : (n_nodes,) complex  — the ω LC-quadrature AMPLITUDE on the fixed
                                        winding template ê_w (CHARGE/helicity);
                                        the (2,3) winding integer is carried by the
                                        FROZEN ê_w ⇒ conserved by construction (the
                                        rigid_template representation, faithful to
                                        coupled_cage_winding's production mode).
      self.e_w  : (n_nodes,3) real    — the FIXED seeded winding template ê_w.

    Integration: Crank–Nicolson / Cayley (I + i·dt/2·H) a^{n+1} = (I − i·dt/2·H)
    a^n with H Hermitian ⇒ exactly UNITARY ⇒ joint energy ‖a_A1‖² + ‖b_w‖²
    conserved to solver tolerance (the rigor guard — no damping fakes a pin).
    D=1/S(A^n) and Ω(x) frozen each step (nonlinearity lagged). H_native is the
    srs z=3 graph Laplacian (NOT the diamond z=4 TETRA operator).
    """

    def __init__(self, cfg: SrsCageWindingConfig):
        self.cfg = cfg
        self.net = build_srs_net(L=cfg.L, enantiomorph=cfg.enantiomorph)
        self.n = self.net.n_nodes
        self.dt = cfg.dt
        self.winding_on = cfg.winding_on

        # the srs-native incidence (assembled ONCE; D re-weights per step).
        self.B, self.bonds = build_incidence(self.net)

        # complex analytic-signal fields on the srs nodes.
        self.a_A1 = np.zeros(self.n, dtype=np.complex128)
        self.b_w = np.zeros(self.n, dtype=np.complex128)
        self.e_w = np.zeros((self.n, 3), dtype=np.float64)
        self.w_amp0 = np.zeros(self.n, dtype=np.float64)

        self.time = 0.0
        self.step_count = 0
        self.last_gmres_info = 0

    # ── kernel readouts (α-free; A from the A1 breather magnitude) ──
    def strain(self) -> np.ndarray:
        return _strain(np.abs(self.a_A1), self.cfg.V_yield, self.cfg.A_cap)

    def saturation_S(self) -> np.ndarray:
        return saturation_kernel(self.strain(), exponent=self.cfg.exponent, S_min=self.cfg.S_min)

    def stiffness_D(self) -> np.ndarray:
        """D = c_eff²/c0² = 1/S(A). The native saturated stiffness."""
        return stiffness_profile(self.strain(), exponent=self.cfg.exponent, S_min=self.cfg.S_min)

    def coupling_Omega(self) -> np.ndarray:
        """Ω(x) = rate · g_front(A) · S(A) — the saturation-front-gated A1↔ω rate.
        winding_on=False ⇒ Ω≡0 (the A1-alone control)."""
        if not self.winding_on:
            return np.zeros(self.n, dtype=np.float64)
        A = self.strain()
        S = self.saturation_S()
        if self.cfg.gate == "front":
            g = front_gate(A)
        elif self.cfg.gate == "saturation":
            g = S
        elif self.cfg.gate == "front_times_S":
            g = front_gate(A) * S
        elif self.cfg.gate == "off":
            g = np.zeros_like(A)
        else:
            raise ValueError(f"unknown gate '{self.cfg.gate}'")
        return self.cfg.rate * g * S

    # ── seeding (A1 + ω separately initialised — genesis-24 guard) ──
    def seed_A1_sech(self, *, amplitude: float, radius: float):
        """A sech A1 breather centred at the srs net centroid (the already-
        localized A1 eigen-precursor; analytic signal at-rest ⇒ a_A1 real)."""
        c = self.net.pos.mean(axis=0)
        d = self.net.pos - c
        d -= self.net.box * np.round(d / self.net.box)
        rr = np.linalg.norm(d, axis=1)
        # scale radius into the srs node-pitch frame
        scale = self.net.box / self.cfg.frame_N
        seed = amplitude * (1.0 / np.cosh(rr / (radius * scale)))
        self.a_A1[:] = seed.astype(np.complex128)

    def seed_A1_field(self, V_seed: np.ndarray):
        """Plant an arbitrary at-rest A1 seed (∂_t a=0 ⇒ a_A1 = V_seed real)."""
        self.a_A1[:] = np.asarray(V_seed, dtype=np.complex128)

    def seed_winding(self, *, amplitude: float = 1.0):
        """Seed the ω winding DOF with the real-space (2,3) phase field evaluated
        at the srs node positions (the SAME coordinate compute_Q_link_srs reads).
        SEPARATELY-initialized charge winding; NEVER grad(V) (genesis-24 guard).

        rigid_template (production): the FIXED winding template ê_w = normalized
        seeded ω carries the (2,3) winding integer (conserved by construction);
        the dynamical amplitude b_ω starts at the seeded |ω| (at-rest LC C-state,
        Im=0). The reconstructed ω = b_ω·ê_w."""
        om, env = seed_pq_winding_on_srs(
            self.net, 2, 3, self.cfg.R, self.cfg.r, frame_N=self.cfg.frame_N,
            amplitude_scale=amplitude,
        )
        nrm = np.sqrt(np.sum(om ** 2, axis=-1))
        self.w_amp0[:] = nrm
        self.e_w[:] = np.where(nrm[:, None] > 1e-12, om / np.maximum(nrm[:, None], 1e-30), 0.0)
        self.b_w[:] = nrm.astype(np.complex128)

    # ── the Hermitian generator H (srs-Laplacian blocks + on-site coupling) ──
    def _assemble_H(self):
        """Assemble the sparse Hermitian generator H on the srs z=3 net. D=1/S(A^n)
        and Ω(x) frozen at the current strain (nonlinearity lagged). H_native is
        the srs graph Laplacian L_srs (NOT the diamond z=4 TETRA operator; the z=3
        ADAPTATION). H Hermitian ⇒ e^{-iHdt} unitary ⇒ joint energy conserved.

        State x = [a_A1 (n), b_ω (n)]:
          A1 block  : ω_b·I − c_A1²·L_srs
          b_ω block : ω_s·I − c_ωb²·L_srs   (b_ω LC amplitude on fixed ê_w)
          coupling  : a_A1 ← Ω·e^{+iχθ_χ}·b_ω ,  b_ω ← Ω·e^{−iχθ_χ}·a_A1
                      (on-site scalar conjugate pair ⇒ Hermitian; the winding
                      integer is carried by the frozen ê_w ⇒ separately conserved)."""
        from scipy import sparse

        n = self.n
        D = self.stiffness_D()
        L_srs = assemble_L_srs(self.B, self.bonds, D).astype(complex)
        I = sparse.identity(n, format="csr", dtype=complex)
        H_A1 = self.cfg.omega_b * I - (self.cfg.c_A1 ** 2) * L_srs
        H_b = self.cfg.omega_s * I - (self.cfg.c_omega_b ** 2) * L_srs
        Omega = self.coupling_Omega()
        phase = self.cfg.chi * THETA_CHI
        cpl = Omega * np.exp(1j * phase)
        blocks = [
            [H_A1, sparse.diags(cpl, format="csr")],
            [sparse.diags(np.conj(cpl), format="csr"), H_b],
        ]
        return sparse.bmat(blocks, format="csr")

    def _stack(self) -> np.ndarray:
        x = np.empty(2 * self.n, dtype=np.complex128)
        x[: self.n] = self.a_A1
        x[self.n:] = self.b_w
        return x

    def _unstack(self, x: np.ndarray):
        self.a_A1 = x[: self.n]
        self.b_w = x[self.n:]

    def step(self):
        """One Crank–Nicolson / Cayley step (the energy-conserving unitary scheme):
            (I + i·dt/2·H) x^{n+1} = (I − i·dt/2·H) x^n
        with H Hermitian (D, Ω frozen this step). Solved by GMRES. Exactly
        norm-preserving to solver tolerance — NO spurious damping fakes a pin."""
        from scipy.sparse import identity
        from scipy.sparse.linalg import gmres

        H = self._assemble_H()
        nd = 2 * self.n
        I = identity(nd, format="csr", dtype=complex)
        half = 0.5j * self.dt
        A_sys = (I + half * H).tocsr()
        x = self._stack()
        rhs = (I - half * H) @ x
        x_new, info = gmres(A_sys, rhs, rtol=self.cfg.gmres_tol,
                            maxiter=self.cfg.gmres_maxiter, x0=x)
        self.last_gmres_info = info
        self._unstack(x_new)
        self.time += self.dt
        self.step_count += 1

    # ── reconstructed ω + winding integer (RE-HOMED reader on srs nodes) ──
    def omega_field(self) -> np.ndarray:
        """The reconstructed real-space ω vector field on srs nodes: ω = |b_ω|·ê_w
        (the quadrature-invariant magnitude on the fixed winding template; the
        winding integer lives in ê_w, |b_ω| only modulates it — the SAME read
        coupled_cage_winding.omega_field uses, re-homed onto the node cloud)."""
        return np.abs(self.b_w)[:, None] * self.e_w

    def winding_integer(self) -> dict:
        """Read the (2,3) winding integer off the reconstructed ω field via the
        srs-native sampler (compute_Q_link_srs — the z=3 analog of compute_Q_link)."""
        q = compute_Q_link_srs(
            self.net, self.omega_field(), self.cfg.R, self.cfg.r, frame_N=self.cfg.frame_N
        )
        return {"Q_link": int(q["Q_link"]), "w_tor": int(q["w_tor"]),
                "Q_link_raw": float(q["Q_link_raw"]), "w_pol_rel": float(q["w_pol_rel"])}

    # ── energy observables (the rigor guard: BOTH A1-norm AND ω grade) ──
    def total_energy(self) -> float:
        """Joint energy H = ‖a_A1‖² + ‖b_ω‖² (the conserved norm of the unitary
        map). Certifies BOTH grades together — a pin bought by bleeding ω into A1
        would still have to keep THIS conserved, and the per-grade split certifies
        neither grade is silently drained into the other."""
        return self.a1_energy() + self.omega_energy()

    def a1_energy(self) -> float:
        """‖a_A1‖² (the A1-norm — genesis-24 separate-cert)."""
        return float(np.sum(np.abs(self.a_A1) ** 2))

    def omega_energy(self) -> float:
        """‖b_ω‖² (the ω-charge-sector grade norm — genesis-24 separate-cert)."""
        return float(np.sum(np.abs(self.b_w) ** 2))
