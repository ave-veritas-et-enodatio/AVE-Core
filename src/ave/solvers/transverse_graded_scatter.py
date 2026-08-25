"""Transverse per-directed-bond graded scatter — the Stage-1 named extension.

Prereg (FROZEN, executed verbatim):
    research/2026-08-24_transverse-gamma-meanstest_prereg_FROZEN.md  (SS4.0-4.2)
Template generalized: vacuum_varactor_scatter's admittance-weighted shunt junction
    S_ij = 2 Y_j / (Sum_k Y_k) - delta_ij                                    (1)
(the Op5 shunt KCL with per-port admittance retained, vacuum_varactor_scatter.py:28-35)
applied IDENTICALLY to both transverse components of the ratified vector-TLM
container (S_u (x) I_2; "Scatter uses the same Op5 shunt matrix on both components",
chiral_lattice_vector.py:4-5). CONNECT = the lattice's own directed-edge permutation
applied per component, UNTOUCHED.

THE TWO LOADING MAPS (prereg SS2.2/SS4.2; both on the shared exact/unclipped kernel
S(A) = sqrt(1 - A^2), the ave_chart.saturation_kernel form — defined LOCALLY here so
the scatter path stays alpha-free (ave_chart imports ALPHA at module level); the
shared-form receipt is the pytest bit-equality gate, not an import):

    load="magnetic":  Y_b = Y0 / sqrt(S(A_b))   (z_b = sqrt(S)   -> Z->0, short rim)
    load="electric":  Y_b = Y0 * sqrt(S(A_b))   (z_b = 1/sqrt(S) -> Z->inf, open rim)

SCOPE-ASSERTION COMPLIANCE: the electric map is built FRESH here — it does NOT
reuse gamma_bulk's Z_eff form (the EPSILON-LOAD FORBID, crystal_engine.py:471-474:
"A future eps-load import MUST NOT reuse this method's Z_eff form"). Load-type
compliance is COMPUTED, not declared: gate_cs7_reconcile() checks the built Y
against universal_operators.universal_dynamic_impedance(1.0, S, load=<declared>),
putting the sign-lock w35sn2bq3 raise in the path (imported function-locally so the
scatter path does not drag jax).

PER-BOND, NOT PER-NODE (the cancellation trap, prereg SS4.0):
  * T1 (inherited): a per-node-uniform admittance CANCELS in (1) — a common factor
    Y in every Y_j cancels in 2Y_j/Sum Y_k, reducing to (2/n)J - I regardless of S
    (vacuum_varactor_scatter.py:52-57). With a constant-A slab every INTERIOR slab
    node has all three ports at equal Y and collapses to bedrock EXACTLY; the
    response is boundary-layer-only. Gates: gate_t1a_global_uniform (collapse,
    <=1e-13) and gate_t1b_boundary_set (deviation set == mixed-admittance node set,
    non-empty, max deviation >= 1e-3).
  * T2 (component-space, NEW): the bond has ONE impedance — the loading is
    COMPONENT-SCALAR (one Y_b, both polarization components). A per-component
    loading would smuggle un-owned birefringent structure. Gate:
    gate_so2_equivariance (the graded step commutes with a global polarization
    rotation, <=1e-12), run under BOTH loading maps.
  * T3 (observable blindness): because the graded scatter is S_u (x) I_2 and
    commutes with global SO(2), every polarization-angle observable is blind to
    the grading — extraction reads port amplitude sums on the launch component
    only (driver scope).
  * T-CONN: the Op3 bond-mismatch connect is blind to gradings equal at a bond's
    two ends — NOT APPLICABLE here by design (CONNECT stays the pure permutation).

SECTOR FENCES (A1 _|_ T2; prereg SS0/SS2.3): no winding, charge, or spin content;
the polarization pair is NOT the Cosserat micro-rotation (def-0pt1ac fences the
per-node TWIST, which this module does not implement — optical activity is OFF in
the Stage-1 measurement). No sector-ownership claim travels with either loading
map; the magnetic-first constitutive label is one horn of the routed-open
mu-at-core fork (saturation-rim-inversion.md:70) and functions here as the
declared reciprocal of the electric map.

R40-B2a STAMPS (cited, never load-borne silently): (i) the (V_inc, V_ref)
port-phasor reading of the scalar template carries the in-file demotion stamp
(vacuum_varactor_scatter.py:72, family longitudinal-TLM-port, BIAS-DEBT) — scoped
to the A1/longitudinal carrier reading; (ii) the -1/3 vertex counting fact's leaf
carries its own inline stamp (srs-vertex-scattering.md:24). gate_ct1_vertex() is
an IMPLEMENTATION IDENTITY of formula (1) at equal Y (it cannot carry channel
content and does not verify the transverse vertex; prereg SS2.6).
"""

from __future__ import annotations

import numpy as np

from ave.core.chiral_lattice import LatticeNet, scatter_matrix

# ---------------------------------------------------------------------------
# ANTI-LEAK IMPORT-GUARD: the graded scatter is alpha-FREE BY CONSTRUCTION.
# A is the dimensionless per-bond grading amplitude; no dimensionful V_yield
# (and hence no ALPHA) may be reachable from this module's namespace.
# ---------------------------------------------------------------------------
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported here"
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK must NOT be imported here"

LOADS = ("magnetic", "electric")


def saturation_kernel(A: np.ndarray) -> np.ndarray:
    """S(A) = sqrt(1 - A^2), exact/unclipped on [0, 1] (values outside clipped to
    the physical domain) — the ave_chart.saturation_kernel form, defined locally
    so the scatter path stays alpha-free. Bit-equality with ave_chart's kernel is
    a pytest gate (test_transverse_graded_scatter.py), which is the shared-form
    receipt the prereg SS4.2 requires."""
    A = np.asarray(A, dtype=np.float64)
    return np.sqrt(np.clip(1.0 - A * A, 0.0, 1.0))


def bond_admittance(A_bond: np.ndarray, load: str, *, Y0: float = 1.0) -> np.ndarray:
    """The per-bond admittance for the DECLARED loading (prereg SS4.2).

    load="magnetic": Y = Y0/sqrt(S)  (z = sqrt(S),  Z->0 short rim, Gamma -> -1)
    load="electric": Y = Y0*sqrt(S)  (z = 1/sqrt(S), Z->inf open rim, Gamma -> +1)

    The load string is asserted (the sign-lock discipline): a typo raises rather
    than silently building the wrong-sign wall."""
    if load not in LOADS:
        raise ValueError(
            f"bond_admittance: load must be 'magnetic' (Y0/sqrt(S), short) or "
            f"'electric' (Y0*sqrt(S), open); got {load!r}. Naming the load "
            f"prevents silently building the wrong-sign wall (sign-lock w35sn2bq3)."
        )
    S = saturation_kernel(np.asarray(A_bond, dtype=np.float64))
    root = np.sqrt(S)
    return Y0 / root if load == "magnetic" else Y0 * root


# ---------------------------------------------------------------------------
# Bond bookkeeping (per-undirected-bond ids; both end-ports share one Y_b)
# ---------------------------------------------------------------------------
class BondTables:
    """Canonical bond tables for a LatticeNet: undirected bond ids per directed
    port, plus unwrapped x-coordinates (cell units) for geometry membership.
    Mirrors the Class-C driver's Rig bond bookkeeping (engine_gamma_meanstest.py),
    lifted into the module so the both-end-ports-share-Y_b invariant is gated."""

    def __init__(self, net: LatticeNet):
        self.net = net
        self.a_cell = net.a_cell
        N, d = net.n_nodes, net.degree
        bond_id: dict[tuple[int, int], int] = {}
        b_x0, b_dx = [], []
        self.port_bond = np.zeros((N, d), dtype=np.int64)
        for u in range(N):
            for p, v in enumerate(net.neighbors[u]):
                key = (min(u, v), max(u, v))
                if key not in bond_id:
                    bond_id[key] = len(b_x0)
                    u0, u1 = key
                    dx = net.pos[u1, 0] - net.pos[u0, 0]
                    dx -= net.box * np.round(dx / net.box)  # minimum image
                    b_x0.append(net.pos[u0, 0] / self.a_cell)
                    b_dx.append(dx / self.a_cell)
                self.port_bond[u, p] = bond_id[key]
        self.bonds = np.array(sorted(bond_id, key=bond_id.get), dtype=np.int64)
        self.b_x0 = np.array(b_x0)
        self.b_dx = np.array(b_dx)
        self.b_mid = np.mod(self.b_x0 + 0.5 * self.b_dx, net.box / self.a_cell)
        self.n_bonds = len(self.bonds)

    def port_admittance(self, A_bond: np.ndarray, load: str, *, Y0: float = 1.0) -> np.ndarray:
        """(N, degree) per-directed-port admittance from the per-BOND grading.
        Both end-ports of a bond receive the SAME Y_b by construction (the
        port_bond gather), and both transverse components see the same Y (the
        component-scalar T2 fence — Y carries no component axis)."""
        A_bond = np.asarray(A_bond, dtype=np.float64)
        if A_bond.shape != (self.n_bonds,):
            raise ValueError(f"A_bond must be per-bond {(self.n_bonds,)}; got {A_bond.shape}")
        Yb = bond_admittance(A_bond, load, Y0=Y0)
        return Yb[self.port_bond]


# ---------------------------------------------------------------------------
# The graded scatter (per-node coefficients) + the vector step
# ---------------------------------------------------------------------------
def scatter_coeffs(Y_port: np.ndarray) -> np.ndarray:
    """Per-node admittance-weighted scatter coefficients a[u, j] = 2 Y_j / Sum_k Y_k,
    so that S_u = a[u] (row-broadcast) - I, i.e. V_ref = (a . V_inc) - V_inc per
    component (formula (1) per node). Passivity asserted: Sum Y finite, positive."""
    Y = np.asarray(Y_port, dtype=np.float64)
    Ysum = Y.sum(axis=1, keepdims=True)
    if not np.all(np.isfinite(Ysum)) or np.any(Ysum <= 0.0):
        raise ValueError("Sum of port admittances must be finite and positive at every node")
    return 2.0 * Y / Ysum


def vector_graded_step(V_inc: np.ndarray, a_nodes: np.ndarray, conn) -> np.ndarray:
    """One graded scatter + connect step on the (N, degree, 2) transverse field.

    SCATTER (per component c): V_ref[u, :, c] = (a[u] . V_inc[u, :, c]) - V_inc[u, :, c]
    — exactly S_u (x) I_2 (no cross-component term exists; gated by the SO(2)
    equivariance and decoupling tests). CONNECT: the lattice's directed-edge
    permutation applied per component, UNTOUCHED (no Op3 bond mixing; T-CONN
    fence)."""
    w = np.einsum("nd,ndc->nc", a_nodes, V_inc)
    V_ref = w[:, None, :] - V_inc
    src_flat, dst_flat = conn
    V_new = np.zeros_like(V_inc)
    V_new.reshape(-1, 2)[dst_flat] = V_ref.reshape(-1, 2)[src_flat]
    return V_new


def energy_Y(V_inc: np.ndarray, Y_port: np.ndarray) -> float:
    """The Y-weighted line-power norm E_Y = Sum_{u,p} Y_{b(u,p)} (V0^2 + V1^2)[u,p]
    (prereg SS4.1). Conservation under vector_graded_step is a run GATE (V2)."""
    return float((np.asarray(Y_port)[:, :, None] * V_inc * V_inc).sum())


# ---------------------------------------------------------------------------
# Gates (prereg SS4.0 / SS5; consumed by pytest + the driver)
# ---------------------------------------------------------------------------
def gate_t1a_global_uniform(net: LatticeNet, tables: BondTables, A: float, load: str) -> dict:
    """T1(a): a GLOBAL-UNIFORM grading (any A, either load) must collapse the
    graded coefficients to the bedrock (2/n)J - I, max abs deviation <= 1e-13."""
    A_bond = np.full(tables.n_bonds, float(A))
    a_nodes = scatter_coeffs(tables.port_admittance(A_bond, load))
    a_bedrock = np.full_like(a_nodes, 2.0 / net.degree)
    dev = float(np.max(np.abs(a_nodes - a_bedrock)))
    return {"max_abs_dev": dev, "pass": bool(dev <= 1e-13)}


def gate_t1b_boundary_set(tables: BondTables, A_bond: np.ndarray, load: str) -> dict:
    """T1(b): the set of nodes whose coefficients deviate from bedrock by > 1e-13
    must EQUAL the mixed-admittance node set (ports not all equal-Y), be
    NON-EMPTY, and carry max deviation >= 1e-3 (the positive half has a floor and
    can fail). Verifies the operator deviates exactly where — and only where —
    the admittance input is mixed."""
    Y_port = tables.port_admittance(np.asarray(A_bond, float), load)
    a_nodes = scatter_coeffs(Y_port)
    d = Y_port.shape[1]
    dev_per_node = np.max(np.abs(a_nodes - 2.0 / d), axis=1)
    deviating = dev_per_node > 1e-13
    mixed = (np.max(Y_port, axis=1) - np.min(Y_port, axis=1)) > 1e-15
    same_set = bool(np.array_equal(deviating, mixed))
    n_dev = int(deviating.sum())
    max_dev = float(dev_per_node.max()) if n_dev else 0.0
    return {
        "n_deviating": n_dev,
        "n_mixed": int(mixed.sum()),
        "sets_equal": same_set,
        "max_dev": max_dev,
        "pass": bool(same_set and n_dev > 0 and max_dev >= 1e-3),
    }


def gate_so2_equivariance(
    net: LatticeNet,
    tables: BondTables,
    A_bond: np.ndarray,
    load: str,
    *,
    angle: float = 0.7,
    steps: int = 100,
    seed: int = 7,
) -> dict:
    """CS-6b / T2: the graded step commutes with a GLOBAL polarization rotation.
    Rotating a random launch by `angle` and stepping must equal stepping then
    rotating, to <= 1e-12 max abs over `steps` steps. Run under BOTH loads by the
    caller (an anisotropy present in only one map would otherwise pass)."""
    a_nodes = scatter_coeffs(tables.port_admittance(np.asarray(A_bond, float), load))
    conn = net.connect_index()
    rng = np.random.default_rng(seed)
    V = rng.standard_normal((net.n_nodes, net.degree, 2))
    c, s = np.cos(angle), np.sin(angle)

    def rot(X):
        out = np.empty_like(X)
        out[..., 0] = c * X[..., 0] - s * X[..., 1]
        out[..., 1] = s * X[..., 0] + c * X[..., 1]
        return out

    Va, Vb = rot(V.copy()), V.copy()
    dev = 0.0
    for _ in range(steps):
        Va = vector_graded_step(Va, a_nodes, conn)
        Vb = vector_graded_step(Vb, a_nodes, conn)
        dev = max(dev, float(np.max(np.abs(Va - rot(Vb)))))
    return {"max_abs_dev": dev, "angle": angle, "steps": steps, "pass": bool(dev <= 1e-12)}


def gate_cs7_reconcile(A: float, load: str, *, tol: float = 1e-12) -> dict:
    """CS-7: reconcile the module's admittance map against the GUARDED in-tree
    reference universal_dynamic_impedance (sign-lock w35sn2bq3) — imported
    function-locally so the scatter path does not drag jax/EPS constants.

    Y_module(A, load) must equal 1 / Z_ref where Z_ref = UDI(1.0, S(A), load).
    A deliberately swapped label MUST fail this gate (demonstrated in pytest,
    both directions)."""
    from ave.core.universal_operators import universal_dynamic_impedance

    S = float(saturation_kernel(np.asarray(A)))
    Z_ref = float(universal_dynamic_impedance(1.0, S, load=load))
    Y_mod = float(bond_admittance(np.asarray(A), load))
    dev = abs(Y_mod - 1.0 / Z_ref)
    return {"A": float(A), "load": load, "Y_module": Y_mod, "Y_ref": 1.0 / Z_ref,
            "abs_dev": dev, "pass": bool(dev <= tol)}


def gate_ct1_vertex(*, tol: float = 1e-15) -> dict:
    """CT-1 (IMPLEMENTATION IDENTITY, prereg SS2.6 — not a transverse-vertex
    measurement): the equal-admittance 3-port coefficients give S_ii = -1/3 and
    S_ij = 2/3 per component to <= 1e-15 abs, and match the bedrock
    scatter_matrix(3). The -1/3 is the channel-free counting fact Gamma=(2-z)/z
    at z=3 (srs-vertex-scattering.md:13, leaf stamp at :24 carried in the module
    header); this gate can fail only on a coding error."""
    a = scatter_coeffs(np.ones((1, 3)))[0]
    S_u = np.broadcast_to(a, (3, 3)) - np.eye(3)
    bedrock = scatter_matrix(3)
    dev_diag = float(np.max(np.abs(np.diag(S_u) - (-1.0 / 3.0))))
    off = S_u[~np.eye(3, dtype=bool)]
    dev_off = float(np.max(np.abs(off - 2.0 / 3.0)))
    dev_bed = float(np.max(np.abs(S_u - bedrock)))
    return {"dev_diag": dev_diag, "dev_off": dev_off, "dev_vs_bedrock": dev_bed,
            "pass": bool(dev_diag <= tol and dev_off <= tol and dev_bed <= tol)}
