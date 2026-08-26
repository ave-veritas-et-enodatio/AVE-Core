#!/usr/bin/env python3
"""SCX Phase-1 comparison driver — engine vs ngspice on the substrate's own graph.

Prereg (FROZEN): ``research/2026-08-25_solver-crosscheck-phase1_prereg-FROZEN.md``
  frozen at commit 737ba888, pushed BEFORE this file existed (freeze-by-push).
GO gate: ``_orchestration/docket-entries/2026-08-24-ruling-r56-scx-trades.md`` (R56).
Epic: ``_orchestration/2026-08-23_external-solver-crosscheck-epic.md`` sec 4 Phase 1.

CLASS: IMPLEMENTATION-VERIFICATION (a sub-class of CONSISTENCY).
Two integrators agreeing on the SAME network validates that the engine solves its
own equations. It says NOTHING about whether the axioms describe the vacuum. No
output of this driver may be framed as emergence, as a chord, or as a
falsification of AVE.

SECTOR: MODE numerical-infrastructure / REGIME I cold sub-yield lossless-reactive
(A = 0, S(A) = 1, Op14 off) / PHASE-STATE cold crystalline quiescent / CHANNEL
scalar-translational ONLY / CARRIER srs-z3.

WHAT IT DOES (prereg sec 3.4, the frozen extraction method)
-----------------------------------------------------------
  0. REPRODUCTION GATE (epic sec 5.2) -- re-derive every engine-side reference on
     the CURRENT engine before exporting anything. Drift is a finding, banked,
     never silently overwritten.
  1. Export each rung's netlist from the ENGINE's own graph (T3) with canonical
     element values and the R2 delay (R56 item 2).
  2. Coarse `.AC` sweep per drive node; record the driving-point reactance.
  3. Bracket poles by sign changes of 1/X where |X| diverges (Foster's reactance
     theorem makes poles and zeros alternate, so the classification is exhaustive).
  4. Refine by SECANT iteration on 1/X, which vanishes linearly at a pole.
  5. Multiplicity from the rank of the residue matrix: near a pole the residue is
     a scalar times an ORTHOGONAL PROJECTOR (prereg sec 3.1), so its nonzero
     singular values are all equal and its rank IS the multiplicity.
  6. Compare on the dimensionless axis omega/omega_C, interior band 0 < theta < pi.

DRIVER HONESTY (`ave-driver-script-honesty`)
--------------------------------------------
  * L1/L2 are TWO-WAY (analytic vs solver), NOT the epic's three-way anchor.
    `scatter_matrix` raises for n < 2, so the engine cannot build a 1-port
    open termination and NO ENGINE TOUCH IS AUTHORIZED (prereg sec 6.3, FL-3).
    Any 1-port closed form used here is a FORMULA, not an engine code path.
  * L3/L4 ARE three-way: every node has degree 3, so the engine's own
    `scatter_matrix(3)` and `chiral_lattice.scalar_tlm_step` run unmodified.
  * L3's `LatticeNet` is ASSEMBLED BY THIS DRIVER from the engine's primitive-cell
    motif (`_SRS_8A`/`_SRS_NN` via the exporter), not returned by an engine
    builder; L4's comes straight from `build_srs_net(2)`. Disclosed because the
    two legs are not equally direct.
  * L0 is solver-vs-ARITHMETIC, not a two-integrator comparison, and carries zero
    srs topology (SCX-REQ-ANCHOR.2/.3).
  * AUX-B validates a PLOTTING INSTRUMENT, not the engine, and cannot move the bin.

Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/scx_phase1_crosscheck.py
"""

from __future__ import annotations

import json
import math
import shutil
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from ave.bench.spice_runner import ngspice_available, ngspice_version, read_wrdata, run_ngspice
from ave.core.chiral_lattice import LatticeNet, build_srs_net, scalar_tlm_step, scatter_matrix
from ave.core.chiral_lattice_dynamics import ANALYTIC_NETWORK_FACTOR
from ave.core.constants import C_CELL, L_CELL, OMEGA_C
from ave.solvers import scx_spice_export as X

_ROOT = Path(__file__).resolve().parents[3]
NETLIST_DIR = _ROOT / "research" / "netlists" / "2026-08-25-scx-phase1"
RESULT_JSON = _ROOT / "research" / "drivers" / "scx_phase1_crosscheck_results.json"

# ─── FROZEN prereg constants. Changing one of these is a Rule-12 amendment. ───
TOL_GRID = 1.0e-2       # coarse step / smallest reference mode spacing
TOL_REFINE = 1.0e-9     # achieved relative secant convergence
TOL_FREQ = 1.0e-7       # |w_solver/w_ref - 1| per matched mode
TOL_LOSSLESS = 1.0e-9   # max |Re Z / Im Z| over sampled points
TOL_GAMMA = 1.0e-12     # AUX-B locus agreement
EC1_COARSE_POINTS = 20001
EC2_BAND_LO = 1.0e-3
# ── RULE-12 AMENDMENT A1 (2026-08-25, BEFORE any comparison number was banked) ──
# The prereg froze EC-2's upper edge at 1.0 x f_top. That edge coincides EXACTLY
# with the theta = pi pole of every bipartite rung, which breaks the instrument
# two ways:
#   (a) the boundary root cannot be BRACKETED inside the band -- a sign change
#       needs samples on both sides -- so detecting it depends on the
#       floating-point sign of cot() at the final grid point, i.e. on an accident;
#   (b) TOL-LOSSLESS is then evaluated AT a singular MNA solve, where the real
#       part is conditioning rather than loss. MEASURED on L4: |Re/Im| = 5.04e-4
#       at f/f_top = 1.00000000 exactly (|Z| = 6.1e12), against < 1e-9 at every
#       other one of the 20001 samples. No LOSSLESS network can meet the frozen
#       gate when a sample lands on a pole, so as frozen it is a tolerance the
#       instrument cannot meet -- the failure mode the prereg's own
#       instrument-resolution clause names.
# AMENDMENT: the coarse band's upper edge becomes 1.05 x f_top. The COMPARISON
# band is UNCHANGED (interior 0 < theta < pi, per F1); the extra samples are
# instrument and are never compared. BOTH bands are run and BOTH are reported --
# this is a robustness fix with its receipts, not a rescue.
EC2_BAND_HI_FROZEN = 1.0
EC2_BAND_HI = 1.05
EC3_REFINE_ROUNDS = 3
EC4_PROBE_DELTA = 1.0e-6
EC5_RANK_TOL = 1.0e-2
MULT_SEPARATION_FLOOR = 1.0e2
POSITIVE_CONTROL_FACTOR = 1.05

# ── ONE interior/boundary definition, shared by BOTH sides of the comparison ──
# The solver side has always filtered on TOL_FREQ*pi < theta < pi*(1-TOL_FREQ)
# (`run_rung`): a root within TOL-FREQ of a band edge IS a band edge at this
# comparison's own resolution. The REFERENCE side used an independent margin of
# 1e-9 in theta, which is a LATENT DEFECT -- see `arccos_reference`. Both sides
# now name the same margin, so the partition is one definition rather than two
# and no new knob is minted.
BOUNDARY_THETA_MARGIN = TOL_FREQ * math.pi

#: The prereg's own sec 3.6 frozen L4 expectation table -- the ten interior rows
#: `(theta, omega/omega_C, multiplicity)` exactly as frozen at 737ba888
#: (`research/2026-08-25_solver-crosscheck-phase1_prereg-FROZEN.md`, the L4 table).
#: NOT an input to any comparison: prereg sec 3.4 step 7 makes the comparison
#: consume the FRESH reference, and the table's own closing sentence says the
#: table "is the frozen expectation, not the input to the comparison". It is
#: registered here solely to execute the rest of that sentence -- "any drift
#: between this table and the fresh values is itself a finding banked under a
#: dated note" -- which was previously unexecuted because these ten rows sat in
#: no drift registry at all.
PREREG_S36_L4_FROZEN: list[tuple[float, float, int]] = [
    (0.635563, 1.100821, 6),
    (0.729728, 1.263929, 6),
    (0.955317, 1.654648, 4),
    (1.230959, 2.132133, 9),
    (1.432283, 2.480786, 6),
    (1.709310, 2.960614, 6),
    (1.910633, 3.309314, 9),
    (2.186276, 3.786800, 4),
    (2.411865, 4.177519, 6),
    (2.506030, 4.340627, 6),
]

TD = X.bond_delay()                       # the R2 delay, imported through the exporter
F_TOP = 1.0 / (2.0 * TD)                  # theta = pi
OMEGA_LINK_OVER_C = 1.0 / ANALYTIC_NETWORK_FACTOR


def theta_of_f(f: float) -> float:
    return 2.0 * math.pi * f * TD


def f_of_theta(th: float) -> float:
    return th / (2.0 * math.pi * TD)


def w_over_wc(th: float) -> float:
    """theta -> omega/omega_C. The single reporting axis (prereg sec 1)."""
    return th * OMEGA_LINK_OVER_C


# ═════════════════════════════════════════════════════════════════════════════
# ngspice interface (reuses the in-tree hook; Rule 14 -- no second runner)
# ═════════════════════════════════════════════════════════════════════════════
#: ngspice DC-operating-point diagnostics that are BENIGN for a linear `.AC`
#: analysis of a lossless network. A lossless line network has no DC path to
#: ground, so the operating-point solve is singular by construction; ngspice
#: falls back to its transient-op path and the AC solution -- which is
#: operating-point-independent for a LINEAR circuit -- is unaffected. Anything
#: OUTSIDE this allow-list routes to INCONCLUSIVE rather than being read through
#: (reconcile-don't-declare: the gate computes its pass).
BENIGN_DIAGNOSTICS = (
    "singular matrix",
    "gmin stepping",
    "source stepping",
    "transient op",
    "no compatibility mode",
    "has no value, dc 0 assumed",
    "using sparse",
    "using klu",
    "doing analysis at temp",
    # How this driver invokes ngspice: `.AC` under -b produces no output without
    # a `.control` block, so ngspice notes that it ran from one. Benign by
    # construction of the batch-mode contract.
    "simulation executed from .control section",
)
FATAL_MARKERS = ("fatal error", "no simulations run", "error on line", "cannot", "aborted")


@dataclass
class SpiceRun:
    """One ngspice invocation and its parsed AC data."""

    freqs: np.ndarray
    z: dict[str, np.ndarray]       # node name -> complex driving/transfer impedance
    diagnostics: list[str] = field(default_factory=list)
    fatal: list[str] = field(default_factory=list)


def _scan_output(res) -> tuple[list[str], list[str]]:
    diags, fatal = [], []
    for line in (res.stdout + "\n" + res.stderr).splitlines():
        s = line.strip()
        if not s:
            continue
        low = s.lower()
        if not (low.startswith(("warning", "error", "note", "fatal")) or "error" in low):
            continue
        if any(m in low for m in FATAL_MARKERS):
            fatal.append(s)
        elif any(b in low for b in BENIGN_DIAGNOSTICS):
            diags.append(s)
        else:
            fatal.append(s)          # unknown diagnostic => NOT read through
    return diags, fatal


def ac_run(netlist: str, cir_path: Path, out_path: Path, vectors: list[str],
           *, timeout: float = 300.0) -> SpiceRun:
    """Run one netlist and parse its single wrdata sink.

    Column layout (the caller owns it, per ``read_wrdata``'s contract): with
    ``wr_singlescale`` and no ``wr_vecnames``, an `.AC` file is
    ``freq, Re(v0), Im(v0), Re(v1), Im(v1), ...``.
    """
    if out_path.exists():
        out_path.unlink()
    res = run_ngspice(netlist, cir_path, timeout=timeout)
    diags, fatal = _scan_output(res)
    if not out_path.exists():
        fatal.append(f"ngspice wrote no data to {out_path.name}")
        return SpiceRun(np.array([]), {}, diags, fatal)
    cols = ["f"] + [c for v in vectors for c in (f"{v}.re", f"{v}.im")]
    data = read_wrdata(out_path, cols)
    z = {v: data[f"{v}.re"] + 1j * data[f"{v}.im"] for v in vectors}
    return SpiceRun(data["f"], z, diags, fatal)


# ═════════════════════════════════════════════════════════════════════════════
# Pole extraction (prereg sec 3.4)
# ═════════════════════════════════════════════════════════════════════════════
def bracket_poles(f: np.ndarray, zdiag: np.ndarray) -> list[tuple[float, float]]:
    """Bracket poles of a LOSSLESS driving-point impedance.

    Foster's reactance theorem: on a lossless one-port, X(f) = Im Z is strictly
    increasing between singularities, so poles and zeros strictly alternate. A
    sign change of X is therefore either a pole (|X| diverges on approach) or a
    zero (|X| -> 0). Classify by which.
    """
    x = zdiag.imag
    out = []
    for i in range(len(x) - 1):
        if x[i] == 0.0 or x[i + 1] == 0.0:
            continue
        if (x[i] > 0) == (x[i + 1] > 0):
            continue
        # A pole: |X| is LARGE at both bracket ends and grows toward the crossing.
        # A zero: |X| is small at both ends. Compare against the local median.
        lo, hi = max(0, i - 20), min(len(x), i + 22)
        scale = float(np.median(np.abs(x[lo:hi])))
        if scale <= 0.0:
            continue
        if abs(x[i]) > scale and abs(x[i + 1]) > scale:
            out.append((float(f[i]), float(f[i + 1])))
    return out


def refine_pole(evaluate, f_a: float, f_b: float) -> tuple[float, float]:
    """Secant iteration on 1/X, which vanishes LINEARLY at a pole.

    ``evaluate(freq) -> complex Z``. Returns (f_pole, achieved_relative_step).
    Uses EC3_REFINE_ROUNDS iterations and NO other parameter -- the step size is
    set by the function, not by a knob.
    """
    y_a = 1.0 / evaluate(f_a).imag
    y_b = 1.0 / evaluate(f_b).imag
    step = abs(f_b - f_a) / max(abs(f_b), 1.0)
    for _ in range(EC3_REFINE_ROUNDS):
        if y_b == y_a:
            break
        f_c = f_a - y_a * (f_b - f_a) / (y_b - y_a)
        if not math.isfinite(f_c) or f_c <= 0.0:
            break
        step = abs(f_c - f_b) / abs(f_c)
        f_a, y_a = f_b, y_b
        f_b, y_b = f_c, 1.0 / evaluate(f_c).imag
    return f_b, step


def residue_multiplicity(zmat: np.ndarray) -> tuple[int, float, list[float]]:
    """Multiplicity from the rank of the residue matrix at a pole.

    Near a pole, Z ~ (-j Z_0 / (z (theta - theta_k))) * P_k with P_k an ORTHOGONAL
    PROJECTOR (prereg sec 3.1), so P_k's nonzero singular values are all EQUAL and
    its rank is the multiplicity. Returns (multiplicity, separation_ratio, sigmas).
    """
    sig = np.linalg.svd(zmat, compute_uv=False)
    s0 = float(sig[0])
    if s0 <= 0.0:
        return 0, 0.0, []
    keep = int(np.sum(sig > EC5_RANK_TOL * s0))
    sep = float(sig[keep - 1] / sig[keep]) if 0 < keep < len(sig) else float("inf")
    return keep, sep, [float(v) for v in sig[: min(len(sig), keep + 3)]]


def cluster(values: list[float], rel_tol: float = 1.0e-5) -> list[list[float]]:
    """Group nearly-equal frequencies (the same physical pole seen from many
    drive nodes). rel_tol is 2 decades looser than TOL_FREQ, so clustering can
    never merge two modes the comparison is meant to distinguish."""
    out: list[list[float]] = []
    for v in sorted(values):
        if out and abs(v - out[-1][-1]) <= rel_tol * abs(v):
            out[-1].append(v)
        else:
            out.append([v])
    return out


# ═════════════════════════════════════════════════════════════════════════════
# Engine-side references
# ═════════════════════════════════════════════════════════════════════════════
def adjacency(edges: list[tuple[int, int]], n: int) -> np.ndarray:
    a = np.zeros((n, n))
    for u, v in edges:
        a[u, v] += 1.0
        a[v, u] += 1.0
    return a


def boundary_class(theta: float, margin: float) -> str:
    """``'dc'`` | ``'top'`` | ``'interior'`` for one theta under a stated margin.

    Factored out of ``arccos_reference`` so the margin can be exercised DIRECTLY
    on a supplied theta, in both directions, without having to find a graph whose
    adjacency spectrum happens to land where the test needs it. See
    ``src/tests/test_scx_arccos_boundary_margin.py``.
    """
    if theta < margin:
        return "dc"
    if theta > math.pi - margin:
        return "top"
    return "interior"


def arccos_reference(edges, n, degree) -> dict:
    """The canonical arccos TL map on the graph's adjacency spectrum.

    ``omega_n = omega_link * arccos(mu_n / z)`` (srs-band-structure.md sec 2).
    Returns the INTERIOR set (0 < theta < pi) with multiplicities, plus the two
    boundary blocks -- the F5-AC accounting the prereg froze.

    BOUNDARY MARGIN -- REPAIRED, and the repair closes a Phase-2 blocking defect.
    ---------------------------------------------------------------------------
    This classifier previously used an independent ``eps = 1e-9`` stated in
    THETA. Near ``mu = +-z`` the arccos map is SQUARE-ROOT SINGULAR:

        mu = -z + delta   =>   theta = pi - sqrt(2*delta/z)

    so a margin of 1e-9 in theta demands ``|mu + z| <= z*(1e-9)**2/2 = 1.5e-18``
    -- about three decades BELOW double-precision resolution at ``|mu| = 3``
    (``3 * DBL_EPSILON = 6.7e-16``). The test could then only be satisfied by
    ``np.clip`` firing; a boundary eigenvalue that missed its exact integer by a
    few ULPs in the WRONG direction classified INTERIOR and minted a spurious
    mode. This is the same floating-point-accident failure mode AMENDMENT A1 was
    written to fix, in the reference-side classifier.

    MEASURED, on this driver's OWN recorded value
    ``reproduction_gate.fresh.srs_L3_mu_min = -2.9999999999999987``:
    the old margin gives ``theta = pi - 2.98e-08`` => INTERIOR => a spurious
    217th interior mode on srs L=3. The repaired margin classifies it BOUNDARY.
    L=3 is out of Phase-1's frozen scope, so NO Phase-1 number moves (the L3 rung
    is the ``K_4`` primitive cell, mu = {3,-1,-1,-1}, and L4 is srs L=2 whose
    ``mu_min = -3.000000000000002`` clips) -- but Phase 2 runs at L=3 and above.

    The repaired margin is ``BOUNDARY_THETA_MARGIN = TOL_FREQ*pi``, i.e. the
    SOLVER side's own interior filter, so both sides of the comparison partition
    interior-from-boundary on ONE definition. In mu-space that is
    ``|mu + z| <= z*(TOL_FREQ*pi)**2/2 = 1.5e-13`` -- ~330 ULPs of headroom above
    double resolution, and ~12 decades below the nearest genuine interior
    eigenvalue's distance from the band edge on any rung this lane runs.
    Regression (fires in both directions): ``src/tests/test_scx_arccos_boundary_margin.py``.
    """
    mu = np.linalg.eigvalsh(adjacency(edges, n))
    th = np.arccos(np.clip(mu / degree, -1.0, 1.0))
    eps = BOUNDARY_THETA_MARGIN
    interior: dict[float, list[float]] = {}
    n_dc, n_top = 0, 0
    for t in th:
        cls = boundary_class(float(t), eps)
        if cls == "dc":
            n_dc += 1
        elif cls == "top":
            n_top += 1
        else:
            key = round(float(t), 9)
            interior.setdefault(key, []).append(float(t))
    items = sorted(interior.items())
    return {
        "interior_theta": [k for k, _ in items],
        # RAW block means alongside the 9-dp dict keys: the engine-leg receipt
        # compares against a leg that keys at 6 dp, and a key-to-key compare
        # would measure the coarser rounding rather than the agreement.
        "interior_theta_mean": [float(np.mean(v)) for _, v in items],
        "interior_mult": [len(v) for _, v in items],
        "interior_total": int(sum(len(v) for _, v in items)),
        "n_dc": n_dc,
        "n_top": n_top,
        "mu_min": float(mu.min()),
        "mu_max": float(mu.max()),
    }


def latticenet_from_edges(edges, n, degree, *, carrier: str) -> LatticeNet:
    """Assemble a ``LatticeNet`` from an edge list so the ENGINE's own
    ``scalar_tlm_step`` can be run on it.

    DISCLOSED (`ave-driver-script-honesty`): for L3 this driver assembles the net
    rather than calling an engine builder -- the EDGES come from the engine's
    primitive-cell motif, but the LatticeNet packaging is the driver's. L4 uses
    ``build_srs_net(2)`` directly and needs none of this.
    """
    neighbors: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    for u in range(n):
        if len(neighbors[u]) != degree:
            raise AssertionError(f"node {u} has degree {len(neighbors[u])}, expected {degree}")
    reverse_port = [[neighbors[v].index(u) for v in neighbors[u]] for u in range(n)]
    for u in range(n):
        for p, v in enumerate(neighbors[u]):
            assert neighbors[v][reverse_port[u][p]] == u, "reverse-port map is inconsistent"
    return LatticeNet(
        name=f"driver-assembled[{carrier}]", handedness="n/a", degree=degree,
        pos=np.zeros((n, 3)), neighbors=neighbors, reverse_port=reverse_port,
        bond_unit=[[np.zeros(3)] * degree for _ in range(n)], box=1.0, carrier=carrier,
    )


def tlm_operator_spectrum(net: LatticeNet) -> dict:
    """Eigenphases of the ENGINE's one-step scatter+connect operator.

    Assembled by applying ``chiral_lattice.scalar_tlm_step`` -- the engine's
    shipped stepper -- to unit port basis vectors. This is the engine leg of the
    three-way anchor: the engine's own code path, not a re-implementation.
    """
    conn = net.connect_index()
    s = scatter_matrix(net.degree)
    n, d = net.n_nodes, net.degree
    m = np.zeros((n * d, n * d))
    for k in range(n * d):
        v = np.zeros((n, d))
        v.flat[k] = 1.0
        m[:, k] = scalar_tlm_step(net, v, s, conn).flatten()
    ortho = float(np.abs(m.T @ m - np.eye(n * d)).max())
    th = np.sort(np.abs(np.angle(np.linalg.eigvals(m))))
    # NOT the square-root-singular case `arccos_reference` documents. Here theta
    # is the ARGUMENT of an eigenvalue of an ORTHOGONAL matrix, whose eigenvalue
    # perturbation is LINEAR in the backward error (normal matrix), so a boundary
    # block sits within ~DBL_EPSILON of 0 or pi, not within its square root. 1e-8
    # is therefore ~8 decades of headroom, not 3 decades of deficit. Measured
    # orthogonality residual on the rungs this lane runs: <= 1.8e-15.
    eps = 1e-8
    interior: dict[float, list[float]] = {}
    n_dc, n_top = 0, 0
    for t in th:
        if t < eps:
            n_dc += 1
        elif t > math.pi - eps:
            n_top += 1
        else:
            key = round(float(t), 6)
            interior.setdefault(key, []).append(float(t))
    items = sorted(interior.items())
    return {
        "orthogonality_residual": ortho,
        "interior_theta": [k for k, _ in items],
        # RAW block means. The dict keys above round at 6 dp; comparing 6-dp keys
        # against `arccos_reference`'s 9-dp keys measures the coarser rounding
        # (6.5e-07 at L4), not the agreement between the two formulations.
        "interior_theta_mean": [float(np.mean(v)) for _, v in items],
        "interior_mult": [len(v) for _, v in items],
        "n_dc": n_dc,
        "n_top": n_top,
        "n_ports": n * d,
    }


def engine_leg_receipt(tlm: dict, ref: dict) -> dict:
    """ENGINE (port-space TLM operator) vs ARCCOS (node-space closed form).

    THE THIRD LEG OF THE EPIC'S THREE-WAY ANCHOR, AT THE RUNG THAT CARRIES THE
    INDEPENDENCE WEIGHT. Added 2026-08-25 after the PR clearing review found that
    ``tlm_operator_spectrum(net2)`` was COMPUTED AND DISCARDED: only ``n_dc``,
    ``n_top``, ``n_ports`` and the orthogonality residual were persisted, so the
    L4 engine leg produced NO RECORDED RECEIPT and the result doc's marquee
    column was in fact solver-vs-arccos.

    WHY THIS LEG CARRIES CONTENT THE GATED COMPARISON DOES NOT. The arccos map is
    derived (prereg sec 3.1) FROM ``Y = (D cos theta - A)/(j Z0 sin theta)`` --
    the same MNA formulation ngspice solves -- so solver-vs-arccos is
    closed-form-vs-numerics on ONE formulation. The engine leg is a DIFFERENT
    formulation: ``scalar_tlm_step`` + ``scatter_matrix(3)``, i.e. scatter+connect
    with Gamma = -1/3 on the port space, never assembling a nodal admittance
    matrix at all.

    REPORTED, NOT GATING. The frozen prereg's bins consume TOL-FREQ/-MULT/-COUNT/
    -LOSSLESS on the solver-vs-reference comparison. This receipt was landed after
    those criteria were frozen, so it is banked and reported and does NOT feed any
    bin -- adding a gate to a frozen prereg mid-lane is the move the discipline
    forbids. Its tolerance is the frozen TOL-FREQ; no new knob is minted.

    Port-space multiplicity is exactly TWICE node-space multiplicity: eigenphases
    come in +-theta pairs and ``tlm_operator_spectrum`` folds them with
    ``abs(angle(.))``, so both members of a pair land in one block.
    """
    te, rt = tlm["interior_theta_mean"], ref["interior_theta_mean"]
    tm, rm = tlm["interior_mult"], ref["interior_mult"]
    same_n = len(te) == len(rt)
    rec = {
        "status": "REPORTED, NOT GATING (landed after the prereg froze its bins)",
        "engine_leg": "ave.core.chiral_lattice.scalar_tlm_step + scatter_matrix(3), PORT space",
        "reference_leg": "arccos_reference, NODE space, closed form of "
                         "Y = (D cos theta - A)/(j Z0 sin theta)",
        "orthogonality_residual": tlm["orthogonality_residual"],
        "engine_interior_theta_mean": te,
        "reference_interior_theta_mean": rt,
        "engine_interior_mult": tm,
        "reference_interior_mult": rm,
        "engine_n_distinct": len(te),
        "reference_n_distinct": len(rt),
        "engine_total_mult": int(sum(tm)),
        "reference_total_mult": int(sum(rm)),
        "engine_dc_block": tlm["n_dc"],
        "engine_top_block": tlm["n_top"],
        "tolerance": TOL_FREQ,
        "tolerance_name": "TOL-FREQ (frozen; this receipt mints no new tolerance)",
        "boundary_theta_margin": float(BOUNDARY_THETA_MARGIN),
    }
    rec["max_rel_dev"] = (max(abs(a / b - 1.0) for a, b in zip(te, rt))
                          if same_n else float("inf"))
    rec["n_distinct_match"] = bool(same_n)
    rec["mult_is_exactly_double"] = bool(same_n and all(a == 2 * b for a, b in zip(tm, rm)))
    rec["freq_within_tolerance"] = bool(same_n and rec["max_rel_dev"] <= TOL_FREQ)
    rec["pass"] = bool(rec["freq_within_tolerance"] and rec["mult_is_exactly_double"])
    return rec


# ═════════════════════════════════════════════════════════════════════════════
# Reproduction gate (epic sec 5.2) -- runs BEFORE anything is exported
# ═════════════════════════════════════════════════════════════════════════════
#: Phase-0 banked receipts (requirements sec 7, taken at ff0fde8b). NOT
#: load-bearing: they are the comparison target for DRIFT DETECTION only.
PHASE0_BANKED = {
    "TD_R2": 7.436783388682972e-22,
    "TD_R1": 1.2880886674083153e-21,
    "ratio": 1.732050807568877,
    "band_top_over_wc": 5.4414,
    "gamma_multiplet_over_wc": 3.3093,
    "srs_L3_mu_min": -3.0,
    "srs_L3_mu_max": 3.0,
    "srs_L3_lambda_max": 6.0,
    "k4_interior_theta": 1.910633,
    "srs_L2_cycle_block": 34,
    "srs_L2_interior_distinct": 10,
    "srs_L2_interior_total": 62,
}


def prereg_s36_drift(ref2: dict) -> dict:
    """Drift of the prereg's frozen sec 3.6 L4 table against the fresh reference.

    The prereg's own rule, on the line closing that table: *"any drift between
    this table and the fresh values is itself a finding banked under a dated
    note"*. Those ten rows sat in NO registry -- ``PHASE0_BANKED`` never carried
    them -- so the rule had no machinery. This is the machinery.

    REPORTED, NOT GATING, and deliberately NOT folded into ``reproduction_gate``'s
    ``pass``: the prereg makes drift a FINDING TO BANK, not a gate, and sec 3.4
    step 7 makes the comparison consume the FRESH reference, so no verdict can
    turn on this. Folding it into the gate would be a post-hoc criterion.

    Each row is scored against its own PRINT-ROUNDING FLOOR (0.5 in the last
    printed decimal), because a 6-dp table cannot agree with a double to better
    than that. Drift ABOVE that floor is a real inconsistency in the frozen
    table; drift below it is transcription precision.
    """
    th_fresh = ref2["interior_theta"]
    rows, worst_t, worst_w = [], 0.0, 0.0
    for i, (t_frozen, w_frozen, m_frozen) in enumerate(PREREG_S36_L4_FROZEN):
        t_fresh = th_fresh[i]
        w_fresh = w_over_wc(t_fresh)
        rel_t = abs(t_frozen / t_fresh - 1.0)
        rel_w = abs(w_frozen / w_fresh - 1.0)
        floor_t, floor_w = 0.5e-6 / t_frozen, 0.5e-6 / w_frozen
        worst_t, worst_w = max(worst_t, rel_t), max(worst_w, rel_w)
        rows.append({
            "row": i + 1,
            "theta_frozen": t_frozen, "theta_fresh": t_fresh,
            "theta_rel_drift": rel_t, "theta_print_floor": floor_t,
            "theta_within_print_precision": bool(rel_t <= floor_t),
            "w_over_wc_frozen": w_frozen, "w_over_wc_fresh": float(w_fresh),
            "w_over_wc_rel_drift": rel_w, "w_over_wc_print_floor": floor_w,
            "w_over_wc_within_print_precision": bool(rel_w <= floor_w),
            # What single conversion factor the frozen row implies. The frozen map
            # is w/wC = theta / ANALYTIC_NETWORK_FACTOR, one constant for all ten
            # rows; a row-varying implied factor means the frozen column was not
            # produced from the frozen theta column by that map.
            "implied_factor_from_fresh_theta": float(w_frozen / t_fresh),
            "mult_frozen": m_frozen, "mult_fresh": ref2["interior_mult"][i],
            "mult_match": bool(m_frozen == ref2["interior_mult"][i]),
        })
    off_t = [r["row"] for r in rows if not r["theta_within_print_precision"]]
    off_w = [r["row"] for r in rows if not r["w_over_wc_within_print_precision"]]
    factors = [r["implied_factor_from_fresh_theta"] for r in rows]
    return {
        "status": "REPORTED, NOT GATING -- banked per the prereg's own drift rule",
        "source": ("research/2026-08-25_solver-crosscheck-phase1_prereg-FROZEN.md, "
                   "sec 3.6 L4 table, as frozen at 737ba888"),
        "frozen_map": "w/wC = theta / ANALYTIC_NETWORK_FACTOR",
        "analytic_network_factor": float(ANALYTIC_NETWORK_FACTOR),
        "rows": rows,
        "theta_max_rel_drift": worst_t,
        "w_over_wc_max_rel_drift": worst_w,
        "w_over_wc_max_drift_in_TOL_FREQ_units": worst_w / TOL_FREQ,
        "theta_rows_beyond_print_precision": off_t,
        "w_over_wc_rows_beyond_print_precision": off_w,
        "mult_all_match": all(r["mult_match"] for r in rows),
        "implied_factor_min": min(factors),
        "implied_factor_max": max(factors),
        "implied_factor_spread": max(factors) - min(factors),
        "finding": (
            "The frozen theta column reproduces to print precision on all ten rows. "
            "The frozen omega/omega_C column does NOT: it drifts beyond its own "
            "print-rounding floor on the rows listed, and the single conversion "
            "factor it implies VARIES row to row, so that column was not produced "
            "from the frozen theta column by the frozen map. No verdict moves -- "
            "prereg sec 3.4 step 7 makes the comparison consume the fresh reference "
            "and it does."
        ),
    }


def reproduction_gate() -> dict:
    """Re-derive every engine-side reference on the CURRENT engine.

    Drift between the Phase-0 banked values and these is itself a finding, banked
    under a dated note, never silently overwritten (`ave-reproduction-gate`).
    """
    out: dict = {"banked_at": "ff0fde8b (Phase-0 requirements sec 7)", "fresh": {}, "drift": {}}
    fresh = out["fresh"]
    fresh["TD_R2"] = TD
    fresh["TD_R1"] = X.bond_delay_r1_NOT_OURS()
    fresh["TD_III"] = X.bond_delay_iii_NOT_OURS()
    fresh["ratio"] = fresh["TD_R1"] / fresh["TD_R2"]
    fresh["band_top_over_wc"] = w_over_wc(math.pi)
    fresh["gamma_multiplet_over_wc"] = w_over_wc(math.acos(-1.0 / 3.0))

    net3 = build_srs_net(3)
    a3 = adjacency(X.edges_from_net(net3), net3.n_nodes)
    mu3 = np.linalg.eigvalsh(a3)
    fresh["srs_L3_nodes"] = net3.n_nodes
    fresh["srs_L3_mu_min"] = float(mu3.min())
    fresh["srs_L3_mu_max"] = float(mu3.max())
    fresh["srs_L3_lambda_max"] = float(np.linalg.eigvalsh(np.diag(a3.sum(1)) - a3).max())
    # Bipartiteness VERIFIED by 2-colouring, not inferred from the spectrum.
    colour = {0: 0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in net3.neighbors[u]:
            if v not in colour:
                colour[v] = 1 - colour[u]
                stack.append(v)
            elif colour[v] == colour[u]:
                raise AssertionError("srs L=3 is NOT bipartite -- the OBS-2 premise fails")
    fresh["srs_L3_parts"] = [sum(1 for c in colour.values() if c == 0),
                             sum(1 for c in colour.values() if c == 1)]

    k4 = X.srs_primitive_cell_edges()
    ref_k4 = arccos_reference(k4, 4, 3)
    fresh["k4_interior_theta"] = ref_k4["interior_theta"][0]
    fresh["k4_interior_mult"] = ref_k4["interior_mult"][0]
    fresh["k4_mu_min"] = ref_k4["mu_min"]
    tlm_k4 = tlm_operator_spectrum(latticenet_from_edges(k4, 4, 3, carrier="srs-z3"))
    fresh["k4_tlm_interior"] = list(zip(tlm_k4["interior_theta"], tlm_k4["interior_mult"]))
    fresh["k4_tlm_dc_top"] = [tlm_k4["n_dc"], tlm_k4["n_top"]]

    net2 = build_srs_net(2)
    e2 = X.edges_from_net(net2)
    ref2 = arccos_reference(e2, net2.n_nodes, 3)
    tlm2 = tlm_operator_spectrum(net2)
    fresh["srs_L2_nodes"] = net2.n_nodes
    fresh["srs_L2_bonds"] = len(e2)
    fresh["srs_L2_interior_distinct"] = len(ref2["interior_theta"])
    fresh["srs_L2_interior_total"] = ref2["interior_total"]
    fresh["srs_L2_cycle_block"] = tlm2["n_dc"]
    fresh["srs_L2_ports"] = tlm2["n_ports"]
    fresh["srs_L2_tlm_top_block"] = tlm2["n_top"]
    fresh["srs_L3_bonds"] = len(X.edges_from_net(net3))
    fresh["k4_tlm_orthogonality"] = tlm_k4["orthogonality_residual"]
    fresh["srs_L2_tlm_orthogonality"] = tlm2["orthogonality_residual"]
    fresh["srs_L2_cycle_space"] = len(e2) - net2.n_nodes + 1
    fresh["srs_L2_highest_interior_over_wc"] = w_over_wc(ref2["interior_theta"][-1])
    # tlm2's INTERIOR spectrum used to be computed here and thrown away, which
    # left the L4 engine leg with no receipt in the record. Persisted now.
    fresh["srs_L2_tlm_interior_theta"] = list(tlm2["interior_theta"])
    fresh["srs_L2_tlm_interior_mult"] = list(tlm2["interior_mult"])
    fresh["boundary_theta_margin"] = float(BOUNDARY_THETA_MARGIN)

    for key, banked in PHASE0_BANKED.items():
        got = fresh.get(key)
        if got is None:
            continue
        drift = abs(got - banked) / max(abs(banked), 1e-300)
        # The banked table carries 4-5 dp for the rounded entries; treat a match
        # to the banked precision as zero drift and report the raw number anyway.
        out["drift"][key] = {"banked": banked, "fresh": got, "rel": drift,
                             "match": drift < 1e-4}
    out["pass"] = all(d["match"] for d in out["drift"].values())
    # Both blocks below are REPORTED and deliberately do NOT feed out["pass"]:
    #   * engine_leg_L4 is a receipt landed AFTER the prereg froze its bins, so it
    #     may not become a gate mid-lane;
    #   * prereg_s36_drift executes the prereg's own rule, which makes drift a
    #     FINDING TO BANK, not a gate (and sec 3.4 step 7 already makes the
    #     comparison consume the fresh reference).
    out["engine_leg_L4"] = engine_leg_receipt(tlm2, ref2)
    out["prereg_s36_drift"] = prereg_s36_drift(ref2)
    return out


# ═════════════════════════════════════════════════════════════════════════════
# Rung runner
# ═════════════════════════════════════════════════════════════════════════════
@dataclass
class Rung:
    name: str
    title: str
    edges: list
    n_nodes: int
    drive_nodes: list
    reference: dict
    native: bool = False
    perturb: tuple | None = None
    keep_netlist: bool = True


def _emit(rung: Rung, drive: int, analyses, convention: str) -> str:
    if rung.edges is None:                       # L0: the lumped smoke test
        return X.emit_lc_tank(analyses, title=rung.title, native=rung.native)
    return X.emit_tl_network(
        rung.edges, rung.n_nodes, drive, analyses, title=rung.title,
        convention=convention, native=rung.native, perturb_bond=rung.perturb,
    )


def _archive(rung: Rung, drive: int, analyses, convention: str, name: str) -> None:
    """Write the TRACKED copy of a netlist (the sec 6.1(a) hand-audit artifact).

    Re-emitted with BASENAME-ONLY wrdata sinks so the tracked bytes carry no
    session-specific temp path and are stable across runs and checkouts.
    """
    stable = [X.AcAnalysis(n=a.n, f1=a.f1, f2=a.f2, out=Path(a.out).name,
                           vectors=a.vectors, kind=a.kind) for a in analyses]
    NETLIST_DIR.mkdir(parents=True, exist_ok=True)
    (NETLIST_DIR / name).write_text(_emit(rung, drive, stable, convention), encoding="utf-8")


def run_rung(rung: Rung, work: Path, *, convention: str = X.CONVENTION,
             band: tuple[float, float] | None = None, archive: bool = True) -> dict:
    """Export, sweep, extract, and report -- one rung of the ladder.

    Returns a record; it does NOT decide the bin. Binning is done once, at the
    end, against the frozen criteria (reconcile-don't-declare: this function
    reports COMPUTED quantities, the verdict reads them).
    """
    scale = 1.0 if not rung.native else TD          # native: f is in units of 1/TD
    f_top = F_TOP * scale
    lo, hi = band or (EC2_BAND_LO * f_top, EC2_BAND_HI * f_top)
    names = [X.node_name(i) for i in range(rung.n_nodes)]
    rec: dict = {"name": rung.name, "convention": convention, "native": rung.native,
                 "band_hz": [lo, hi], "drive_nodes": list(rung.drive_nodes),
                 "diagnostics": [], "fatal": [], "per_node": {}}

    # ── 1. coarse sweep, one run per drive node (diagonal only: 3 columns) ────
    lossless_max, brackets = 0.0, []
    for j in rung.drive_nodes:
        out = work / f"{rung.name}_coarse_n{j}.dat"
        an = [X.AcAnalysis(n=EC1_COARSE_POINTS, f1=lo, f2=hi, out=str(out), vectors=(names[j],))]
        cir = work / f"{rung.name}_coarse_n{j}.cir"
        netlist = _emit(rung, j, an, convention)
        if archive and rung.keep_netlist and j == rung.drive_nodes[0]:
            _archive(rung, j, an, convention, f"{rung.name}_coarse_n{j}.cir")
        run = ac_run(netlist, cir, out, [names[j]])
        rec["diagnostics"] += run.diagnostics
        rec["fatal"] += run.fatal
        if run.fatal:
            rec["status"] = "INCONCLUSIVE"
            return rec
        z = run.z[names[j]]
        finite = np.isfinite(z.real) & np.isfinite(z.imag) & (np.abs(z.imag) > 0)
        lossless_max = max(lossless_max, float(np.max(np.abs(z.real[finite] / z.imag[finite]))))
        br = bracket_poles(run.freqs, z)
        rec["per_node"][str(j)] = {"n_brackets": len(br),
                                   "bracket_f": [0.5 * (a + b) for a, b in br]}
        brackets += [(a, b, j) for a, b in br]
    rec["lossless_max_re_over_im"] = lossless_max
    rec["lossless_pass"] = lossless_max <= TOL_LOSSLESS

    # ── 2. cluster the union, refine each distinct pole by secant on 1/X ──────
    centres = [0.5 * (a + b) for a, b, _ in brackets]
    groups = cluster(centres)
    poles = []
    for grp in groups:
        target = float(np.mean(grp))
        a, b, j = min(brackets, key=lambda t: abs(0.5 * (t[0] + t[1]) - target))
        cir = work / f"{rung.name}_refine_n{j}.cir"

        def evaluate(freq: float, _j=j, _cir=cir) -> complex:
            out = work / f"{rung.name}_pt_n{_j}.dat"
            an = [X.AcAnalysis(n=1, f1=freq, f2=freq, out=str(out), vectors=(names[_j],))]
            r = ac_run(_emit(rung, _j, an, convention), _cir, out, [names[_j]])
            if r.fatal or len(r.freqs) == 0:
                raise RuntimeError(f"{rung.name}: point evaluation failed at {freq!r}")
            return complex(r.z[names[_j]][0])

        f_pole, step = refine_pole(evaluate, a, b)
        poles.append({"f": f_pole, "refine_step": step,
                      "theta": theta_of_f(f_pole / scale),
                      "w_over_wc": w_over_wc(theta_of_f(f_pole / scale)),
                      "seen_by": sorted({t[2] for t in brackets
                                         if abs(0.5 * (t[0] + t[1]) - target) < 1e-5 * target}),
                      "refined_at_node": j})
    poles.sort(key=lambda p: p["f"])
    # INTERIOR FILTER -- the frozen comparison rule (prereg sec 3.4 step 7:
    # "interior band 0 < theta < pi per F1 and F5-AC"). A root within TOL_FREQ of
    # a band edge IS a band edge at this comparison's own resolution, so the
    # margin is tied to the tolerance rather than being a new knob.
    # BOUNDARY_THETA_MARGIN is literally `TOL_FREQ * math.pi`; naming it here is
    # what makes "one interior/boundary definition on BOTH sides" structural
    # rather than a comment. `arccos_reference` uses the same constant.
    th_lo, th_hi = BOUNDARY_THETA_MARGIN, math.pi * (1.0 - TOL_FREQ)
    for p in poles:
        p["interior"] = bool(th_lo < p["theta"] < th_hi)
    interior = [p for p in poles if p["interior"]]
    boundary = [p for p in poles if not p["interior"]]
    rec["poles"] = poles
    rec["poles_boundary"] = [{"theta": p["theta"], "w_over_wc": p["w_over_wc"],
                              "rel_dev_from_pi": abs(p["theta"] / math.pi - 1.0)}
                             for p in boundary]
    rec["n_boundary_poles"] = len(boundary)
    poles = interior
    rec["n_distinct_poles"] = len(poles)
    rec["refine_max_step"] = max((p["refine_step"] for p in rec["poles"]), default=0.0)
    rec["refine_pass"] = rec["refine_max_step"] <= TOL_REFINE

    # ── 3. multiplicity from the residue rank (full Z matrix at f*(1+delta)) ──
    if poles and len(rung.drive_nodes) > 1:
        probes = [p["f"] * (1.0 + EC4_PROBE_DELTA) for p in poles]
        cols = {}
        for j in rung.drive_nodes:
            out = work / f"{rung.name}_res_n{j}.dat"
            an = [X.AcAnalysis(n=1, f1=f, f2=f, out=str(out), vectors=tuple(names))
                  for f in probes]
            # ngspice overwrites a wrdata sink per analysis, so one file per probe.
            an = [X.AcAnalysis(n=1, f1=f, f2=f, out=str(work / f"{rung.name}_res_n{j}_p{i}.dat"),
                               vectors=tuple(names)) for i, f in enumerate(probes)]
            cir = work / f"{rung.name}_res_n{j}.cir"
            netlist = _emit(rung, j, an, convention)
            res = run_ngspice(netlist, cir, timeout=300.0)
            diags, fatal = _scan_output(res)
            rec["diagnostics"] += diags
            rec["fatal"] += fatal
            colj = []
            for i in range(len(probes)):
                pth = work / f"{rung.name}_res_n{j}_p{i}.dat"
                d = read_wrdata(pth, ["f"] + [c for v in names for c in (f"{v}.re", f"{v}.im")])
                colj.append(np.array([d[f"{v}.re"][0] + 1j * d[f"{v}.im"][0] for v in names]))
            cols[j] = colj
        for i, p in enumerate(poles):
            zmat = np.array([cols[j][i] for j in rung.drive_nodes])     # rows = drives
            mult, sep, sig = residue_multiplicity(zmat)
            p["multiplicity"] = mult
            p["separation"] = sep
            p["sigmas"] = sig
    rec["separation_min"] = min((p.get("separation", float("inf")) for p in poles),
                                default=float("inf"))
    rec["separation_pass"] = rec["separation_min"] >= MULT_SEPARATION_FLOOR

    # ── 4. compare against the frozen reference ──────────────────────────────
    ref = rung.reference
    rec["reference"] = ref
    if ref.get("interior_theta"):
        ref_f = [f_of_theta(t) * scale for t in ref["interior_theta"]]
        spacing = min((abs(b - a) for a, b in zip(ref_f, ref_f[1:])), default=float("inf"))
        step_hz = (hi - lo) / (EC1_COARSE_POINTS - 1)
        if math.isfinite(spacing):
            rec["tol_grid"] = step_hz / spacing
            rec["tol_grid_pass"] = rec["tol_grid"] <= TOL_GRID
        else:
            # Fewer than two interior reference modes => no mode SPACING exists,
            # so TOL-GRID is UNDEFINED here, not zero. Reporting 0.0 would print
            # a fabricated pass (UNRUN != PASSED).
            rec["tol_grid"] = None
            rec["tol_grid_pass"] = None
            rec["tol_grid_note"] = "undefined: fewer than two interior reference modes"
        matched, dev = [], 0.0
        for t_ref in ref["interior_theta"]:
            f_ref = f_of_theta(t_ref) * scale
            if not poles:
                matched.append({"theta_ref": t_ref, "matched": False})
                continue
            best = min(poles, key=lambda p: abs(p["f"] - f_ref))
            rel = abs(best["f"] / f_ref - 1.0)
            dev = max(dev, rel)
            matched.append({"theta_ref": t_ref, "w_over_wc_ref": w_over_wc(t_ref),
                            "theta_solver": best["theta"], "rel_dev": rel,
                            "matched": rel <= TOL_FREQ,
                            "mult_ref": None, "mult_solver": best.get("multiplicity")})
        for m, mu in zip(matched, ref["interior_mult"]):
            m["mult_ref"] = mu
        rec["matched"] = matched
        rec["max_rel_dev"] = dev
        rec["freq_pass"] = bool(matched) and all(m["matched"] for m in matched)
        rec["count_ref"] = len(ref["interior_theta"])
        rec["count_solver"] = len(poles)
        rec["count_pass"] = rec["count_solver"] == rec["count_ref"]
        have_mult = bool(matched) and all(m["mult_solver"] is not None for m in matched)
        rec["mult_measured"] = have_mult
        rec["mult_pass"] = (all(m["mult_solver"] == m["mult_ref"] for m in matched)
                            if have_mult else None)
        if not have_mult:
            # A residue RANK needs the full Z matrix, i.e. >1 drive node. A
            # single-port rung cannot measure multiplicity at all -- say so
            # rather than letting a None read as a pass.
            rec["mult_note"] = ("NOT MEASURED: residue rank needs >1 drive node; this rung "
                                "is single-port")
        rec["mult_total_solver"] = (sum(m["mult_solver"] for m in matched) if have_mult else None)
        rec["mult_total_ref"] = ref.get("interior_total")
    else:
        rec["tol_grid_pass"] = True
        rec["count_ref"] = 0
        rec["count_solver"] = len(poles)
        rec["count_pass"] = rec["count_solver"] == 0
        rec["freq_pass"] = True
        rec["mult_pass"] = None
        rec["mult_measured"] = None
        rec["mult_note"] = "vacuous: this rung has no interior reference mode"
        rec["max_rel_dev"] = 0.0
    rec["status"] = "RUN"
    return rec


# ═════════════════════════════════════════════════════════════════════════════
# AUX-B — the ave_chart two-junction composite (SUPPLEMENTARY, NON-GATING)
# ═════════════════════════════════════════════════════════════════════════════
AUXB_POINTS = 361          # frozen: theta in [0, 2pi] inclusive, LIN in theta


def run_auxb(work: Path) -> dict:
    """Cross-solver check of ``ave.viz.ave_chart.two_junction_gamma``.

    Two independent computational routes on the SAME composite: the chart's ABCD
    transfer matrix vs ngspice's MNA. This validates a PLOTTING INSTRUMENT, not
    the engine, and CANNOT move the epic's bin (prereg sec 9).

    The two Z_0/2 resistors are PORTS -- semi-infinite matched bond pairs -- not
    dissipative substrate elements, so TOL_LOSSLESS does not apply here.
    """
    from ave.core.constants import Z_0 as _Z0
    from ave.viz.ave_chart import two_junction_gamma

    theta = np.linspace(0.0, 2.0 * math.pi, AUXB_POINTS)
    f_max = float(theta[-1] / (2.0 * math.pi * TD))
    out = work / "auxb.dat"
    an = [X.AcAnalysis(n=AUXB_POINTS, f1=0.0, f2=f_max, out=str(out), vectors=("n0",))]
    title = "AUX-B two-junction composite (cold, A=0)"
    netlist = X.emit_two_junction(an, title=title)
    # Tracked copy: basename-only sink, so the artifact carries no temp path.
    stable = [X.AcAnalysis(n=a.n, f1=a.f1, f2=a.f2, out=Path(a.out).name,
                           vectors=a.vectors, kind=a.kind) for a in an]
    NETLIST_DIR.mkdir(parents=True, exist_ok=True)
    (NETLIST_DIR / "AUXB_two_junction.cir").write_text(
        X.emit_two_junction(stable, title=title), encoding="utf-8")
    run = ac_run(netlist, work / "auxb.cir", out, ["n0"])
    rec: dict = {"diagnostics": run.diagnostics, "fatal": run.fatal, "n_points": AUXB_POINTS}
    if run.fatal:
        rec["status"] = "INCONCLUSIVE"
        return rec
    z_in = run.z["n0"] / _Z0                                    # normalised by Z_0
    g_spice = (z_in - 1.0) / (z_in + 1.0)
    th_meas = 2.0 * math.pi * run.freqs * TD
    g_chart = two_junction_gamma(th_meas, A_line=0.0, A_ends=0.0)
    dev = np.abs(g_spice - g_chart)
    rec["max_abs_dev"] = float(dev.max())
    rec["locus_pass"] = bool(rec["max_abs_dev"] <= TOL_GAMMA)
    rec["gamma_dc"] = [float(g_spice[0].real), float(g_spice[0].imag)]
    rec["gamma_dc_dev"] = float(abs(g_spice[0] - (-3.0 / 5.0)))
    i_q = int(np.argmin(np.abs(th_meas - math.pi / 2.0)))
    rec["theta_quarter"] = float(th_meas[i_q])
    rec["gamma_quarter"] = [float(g_spice[i_q].real), float(g_spice[i_q].imag)]
    rec["gamma_quarter_dev"] = float(abs(g_spice[i_q] - (-3.0 / 7.0)))
    rec["anchor_pass"] = bool(rec["gamma_dc_dev"] <= TOL_GAMMA
                              and rec["gamma_quarter_dev"] <= TOL_GAMMA)
    rec["status"] = "RUN"
    return rec


# ═════════════════════════════════════════════════════════════════════════════
# main
# ═════════════════════════════════════════════════════════════════════════════
def build_rungs() -> dict:
    """Every rung's graph + frozen reference, all engine-sourced."""
    k4 = X.srs_primitive_cell_edges()
    net2 = build_srs_net(2)
    e2 = X.edges_from_net(net2)
    empty = {"interior_theta": [], "interior_mult": [], "interior_total": 0, "n_top": 1}
    l2_edges = [(0, 1), (0, 2), (0, 3)]           # z=3 vertex + 3 open stubs
    l2_ref = {"interior_theta": [math.pi / 2.0], "interior_mult": [2], "interior_total": 2,
              "n_top": 1}
    return {
        # L0's reference is the FROZEN prereg's own: sec 2.2 gates on "pole within
        # TOL-FREQ of omega_C" and sec 3.6 freezes omega_0/omega_C = 1 exactly.
        # Encoded on the shared theta axis: w/wC = theta/ANALYTIC_NETWORK_FACTOR,
        # so w/wC = 1 <=> theta = ANALYTIC_NETWORK_FACTOR. The tank has no TD of
        # its own -- theta here is only the reporting coordinate, and it maps back
        # to f_0 = OMEGA_C/(2*pi) exactly.
        "L0": Rung("L0", "L0/P1-A bare cell tank (solver-numerics smoke test)",
                   None, 1, [0],
                   {"interior_theta": [float(ANALYTIC_NETWORK_FACTOR)],
                    "interior_mult": [1], "interior_total": 1}),
        "L1": Rung("L1", "L1/P1-B one bond, open-open (half-wave / Bragg object)",
                   [(0, 1)], 2, [0], dict(empty)),
        "L2v": Rung("L2v", "L2/P1-C vertex + 3 open stubs, DRIVEN AT THE VERTEX",
                    l2_edges, 4, [0], dict(empty)),
        "L2s": Rung("L2s", "L2/P1-C vertex + 3 open stubs, DRIVEN AT A STUB END",
                    l2_edges, 4, [1, 2, 3], l2_ref),
        "L3": Rung("L3", "L3/P1-D srs 4-site primitive cell, periodic wrap (K_4 complete)",
                   k4, 4, [0, 1, 2, 3], arccos_reference(k4, 4, 3)),
        "L4": Rung("L4", "L4/OBS-4 srs supercell L=2 (N=64, B=96), periodic wrap",
                   e2, net2.n_nodes, list(range(net2.n_nodes)),
                   arccos_reference(e2, net2.n_nodes, 3)),
    }


def main() -> int:
    if not ngspice_available():
        print("STUCK-POINT: ngspice is not on PATH. Install with `brew install ngspice`.\n"
              "This lane does NOT substitute a different solver -- T1 ratified ngspice.")
        return 2
    work = Path(tempfile.mkdtemp(prefix="scx_phase1_"))
    report: dict = {
        "lane": "SCX Phase 1 (external-solver cross-check)",
        "class": "IMPLEMENTATION-VERIFICATION",
        "prereg": "research/2026-08-25_solver-crosscheck-phase1_prereg-FROZEN.md",
        "prereg_frozen_at": "737ba888",
        "go_gate": "_orchestration/docket-entries/2026-08-24-ruling-r56-scx-trades.md (R56)",
        "solver": ngspice_version(),
        "convention_emitted": X.CONVENTION,
        "frozen_tolerances": {
            "TOL_GRID": TOL_GRID, "TOL_REFINE": TOL_REFINE, "TOL_FREQ": TOL_FREQ,
            "TOL_LOSSLESS": TOL_LOSSLESS, "TOL_GAMMA": TOL_GAMMA,
            "EC1_COARSE_POINTS": EC1_COARSE_POINTS,
            "EC2_BAND_as_frozen": [EC2_BAND_LO, EC2_BAND_HI_FROZEN],
            "EC2_BAND_amended_A1": [EC2_BAND_LO, EC2_BAND_HI],
            "EC3_REFINE_ROUNDS": EC3_REFINE_ROUNDS, "EC4_PROBE_DELTA": EC4_PROBE_DELTA,
            "EC5_RANK_TOL": EC5_RANK_TOL,
        },
    }

    print("=" * 78, "\nREPRODUCTION GATE (epic 5.2) -- before anything is exported\n", "=" * 78)
    gate = reproduction_gate()
    report["reproduction_gate"] = gate
    for k, v in gate["drift"].items():
        print(f"  {k:32s} banked={v['banked']!r:26s} fresh={v['fresh']!r:26s} "
              f"{'MATCH' if v['match'] else 'DRIFT'}")
    print(f"  REPRODUCTION GATE: {'PASS' if gate['pass'] else 'DRIFT DETECTED'}")
    el = gate["engine_leg_L4"]
    print(f"  ENGINE LEG L4 (REPORTED, NOT GATING): engine-TLM port space vs arccos node "
          f"space -- {el['engine_n_distinct']} vs {el['reference_n_distinct']} distinct, "
          f"max rel dev {el['max_rel_dev']:.3e} (tol {el['tolerance']:.0e}), "
          f"mult exactly 2x = {el['mult_is_exactly_double']}, "
          f"orthogonality residual {el['orthogonality_residual']:.3e}")
    s36 = gate["prereg_s36_drift"]
    print(f"  PREREG sec 3.6 DRIFT (REPORTED, NOT GATING): theta max {s36['theta_max_rel_drift']:.3e} "
          f"(rows beyond print precision: {s36['theta_rows_beyond_print_precision']}); "
          f"w/wC max {s36['w_over_wc_max_rel_drift']:.3e} = "
          f"{s36['w_over_wc_max_drift_in_TOL_FREQ_units']:.0f}x TOL-FREQ "
          f"(rows beyond print precision: {s36['w_over_wc_rows_beyond_print_precision']})")
    if not gate["pass"]:
        print("  Drift is a FINDING, banked -- not silently overwritten. Continuing so the "
              "drift and its consequence are both on the record.")

    rungs = build_rungs()
    report["rungs"] = {}
    for key in ("L0", "L1", "L2v", "L2s", "L3", "L4"):
        print(f"\n--- {key}: {rungs[key].title}")
        rec = run_rung(rungs[key], work)
        report["rungs"][key] = rec
        _print_rung(rec)

    # ── CONTROLS (prereg sec 5) ──────────────────────────────────────────────
    print("\n" + "=" * 78, "\nCONTROLS\n", "=" * 78)
    report["controls"] = {}

    # AMENDMENT-A1 PAIRED CONTROL: re-run the AS-FROZEN band and report BOTH,
    # so the amendment carries its own receipts rather than replacing a number.
    as_frozen = {}
    for key in ("L1", "L3", "L4"):
        rec = run_rung(rungs[key], work, archive=False,
                       band=(EC2_BAND_LO * F_TOP, EC2_BAND_HI_FROZEN * F_TOP))
        amd = report["rungs"][key]
        as_frozen[key] = {
            "frozen_band": {
                "lossless_max_re_over_im": rec["lossless_max_re_over_im"],
                "lossless_pass": rec["lossless_pass"],
                "n_interior": rec["n_distinct_poles"],
                "n_boundary": rec["n_boundary_poles"],
                "max_rel_dev": rec.get("max_rel_dev"),
            },
            "amended_band": {
                "lossless_max_re_over_im": amd["lossless_max_re_over_im"],
                "lossless_pass": amd["lossless_pass"],
                "n_interior": amd["n_distinct_poles"],
                "n_boundary": amd["n_boundary_poles"],
                "max_rel_dev": amd.get("max_rel_dev"),
            },
            "interior_verdict_unchanged": (rec["n_distinct_poles"] == amd["n_distinct_poles"]
                                           and rec.get("freq_pass") == amd.get("freq_pass")),
        }
        f, a = as_frozen[key]["frozen_band"], as_frozen[key]["amended_band"]
        print(f"  A1 paired {key}: lossless frozen-band {f['lossless_max_re_over_im']:.3e} "
              f"({'PASS' if f['lossless_pass'] else 'FAIL'}) vs amended-band "
              f"{a['lossless_max_re_over_im']:.3e} ({'PASS' if a['lossless_pass'] else 'FAIL'}); "
              f"interior poles {f['n_interior']} vs {a['n_interior']}; "
              f"interior verdict unchanged = {as_frozen[key]['interior_verdict_unchanged']}")
    report["controls"]["amendment_a1_paired"] = as_frozen

    # CONVENTION CONTROL: the sqrt(3) hazard, MEASURED
    r2 = report["rungs"]["L1"]
    r1 = run_rung(rungs["L1"], work, convention="R1", archive=False,
                  band=(EC2_BAND_LO * F_TOP / math.sqrt(3.0),
                        EC2_BAND_HI * F_TOP / math.sqrt(3.0)))
    f_r2 = r2["poles"][0]["f"] if r2["poles"] else float("nan")
    f_r1 = r1["poles"][0]["f"] if r1["poles"] else float("nan")
    ratio = f_r2 / f_r1 if f_r1 else float("nan")
    conv = {"f_R2": f_r2, "f_R1": f_r1, "ratio": ratio, "sqrt3": math.sqrt(3.0),
            "rel_dev": abs(ratio / math.sqrt(3.0) - 1.0)}
    conv["pass"] = conv["rel_dev"] <= TOL_FREQ
    report["controls"]["convention"] = conv
    print(f"  CONVENTION CONTROL: R2/R1 resonance ratio = {ratio!r} vs sqrt3 = "
          f"{math.sqrt(3.0)!r}  rel dev {conv['rel_dev']:.3e}  "
          f"{'PASS' if conv['pass'] else 'FAIL'}")

    # POSITIVE CONTROL: plant a defect, confirm the comparison RESOLVES it
    bad = Rung("L3_planted", rungs["L3"].title + " [PLANTED DEFECT]",
               rungs["L3"].edges, 4, [0, 1, 2, 3], rungs["L3"].reference,
               perturb=(2, POSITIVE_CONTROL_FACTOR))
    rec_bad = run_rung(bad, work)
    report["rungs"]["L3_planted"] = rec_bad
    detected = not (rec_bad.get("freq_pass") and rec_bad.get("count_pass")
                    and rec_bad.get("mult_pass"))
    report["controls"]["positive"] = {
        "factor": POSITIVE_CONTROL_FACTOR, "detected": bool(detected),
        "n_interior": rec_bad["n_distinct_poles"], "count_ref": rec_bad["count_ref"],
        "max_rel_dev": rec_bad.get("max_rel_dev"), "freq_pass": rec_bad.get("freq_pass"),
        "count_pass": rec_bad.get("count_pass"), "mult_pass": rec_bad.get("mult_pass"),
    }
    print(f"  POSITIVE CONTROL (one bond TD x{POSITIVE_CONTROL_FACTOR}): "
          f"{'DEFECT RESOLVED' if detected else 'DEFECT MISSED -- instrument not validated'} "
          f"(interior poles {rec_bad['n_distinct_poles']} vs ref {rec_bad['count_ref']}, "
          f"max rel dev {rec_bad.get('max_rel_dev')})")

    # T6 SI/NATIVE PAIRED CONTROL
    t6 = {}
    for key in ("L1", "L3"):
        base = rungs[key]
        nat = Rung(base.name + "_native", base.title + " [native units]", base.edges,
                   base.n_nodes, base.drive_nodes, base.reference, native=True)
        rec_n = run_rung(nat, work, archive=False)
        si = report["rungs"][key]
        th_si = sorted([p["theta"] for p in si["poles"]])
        th_nat = sorted([p["theta"] for p in rec_n["poles"]])
        dev = (max((abs(a / b - 1.0) for a, b in zip(th_si, th_nat)), default=0.0)
               if len(th_si) == len(th_nat) else float("inf"))
        t6[key] = {"n_si": len(th_si), "n_native": len(th_nat), "max_rel_dev": dev,
                   "pass": dev <= TOL_FREQ}
        print(f"  T6 SI/native {key}: {len(th_si)} vs {len(th_nat)} modes, "
              f"max rel dev {dev:.3e} {'PASS' if t6[key]['pass'] else 'FAIL'}")
    report["controls"]["t6_si_native"] = t6

    # NEGATIVE CONTROL
    neg = {"object": "L1 single bond (no srs content)",
           "interior_poles": report["rungs"]["L1"]["n_distinct_poles"],
           "boundary_roots": report["rungs"]["L1"]["n_boundary_poles"]}
    neg["pass"] = neg["interior_poles"] == 0 and neg["boundary_roots"] == 1
    report["controls"]["negative"] = neg
    print(f"  NEGATIVE CONTROL: {neg['interior_poles']} interior / "
          f"{neg['boundary_roots']} boundary  {'PASS' if neg['pass'] else 'FAIL'}")

    # ── AUX-B ────────────────────────────────────────────────────────────────
    print("\n--- AUX-B: two-junction composite (SUPPLEMENTARY, NON-GATING)")
    report["auxb"] = run_auxb(work)
    a = report["auxb"]
    if a["status"] == "RUN":
        print(f"  locus max |dGamma| = {a['max_abs_dev']:.3e}  "
              f"{'PASS' if a['locus_pass'] else 'FAIL'} (tol {TOL_GAMMA:.0e})")
        print(f"  Gamma(0)    dev from -3/5 = {a['gamma_dc_dev']:.3e}")
        print(f"  Gamma(pi/2) dev from -3/7 = {a['gamma_quarter_dev']:.3e}")

    report["verdict"] = verdict(report)
    print("\n" + "=" * 78)
    print(f"VERDICT: {report['verdict']['bin']}")
    for line in report["verdict"]["why"]:
        print(f"  - {line}")
    print("=" * 78)

    RESULT_JSON.parent.mkdir(parents=True, exist_ok=True)
    RESULT_JSON.write_text(json.dumps(report, indent=2, default=float), encoding="utf-8")
    print(f"\nwrote {RESULT_JSON.relative_to(_ROOT)}")
    print(f"netlists in {NETLIST_DIR.relative_to(_ROOT)}")
    shutil.rmtree(work, ignore_errors=True)
    return 0


def _print_rung(rec: dict) -> None:
    if rec.get("status") == "INCONCLUSIVE":
        print(f"  INCONCLUSIVE -- {rec['fatal'][:2]}")
        return
    print(f"  lossless max|Re/Im| = {rec['lossless_max_re_over_im']:.3e} "
          f"{'PASS' if rec['lossless_pass'] else 'FAIL'} (tol {TOL_LOSSLESS:.0e})")
    if rec.get("tol_grid") is not None:
        print(f"  TOL-GRID = {rec['tol_grid']:.3e} "
              f"{'PASS' if rec['tol_grid_pass'] else 'FAIL'} (tol {TOL_GRID:.0e})")
    elif "tol_grid_note" in rec:
        print(f"  TOL-GRID = UNDEFINED ({rec['tol_grid_note']})")
    print(f"  refine max step = {rec['refine_max_step']:.3e} "
          f"{'PASS' if rec['refine_pass'] else 'FAIL'} (tol {TOL_REFINE:.0e})")
    print(f"  interior poles: solver {rec['count_solver']} vs reference {rec['count_ref']} "
          f"{'PASS' if rec['count_pass'] else 'FAIL'}   boundary roots: {rec.get('n_boundary_poles', 0)}")
    for m in rec.get("matched", []):
        print(f"    w/wC ref {m['w_over_wc_ref']:.9f}  rel dev {m['rel_dev']:.3e}  "
              f"mult {m['mult_solver']} vs {m['mult_ref']}  "
              f"{'ok' if m['matched'] else 'OUT OF TOLERANCE'}")
    for b in rec.get("poles_boundary", []):
        print(f"    boundary root w/wC {b['w_over_wc']:.9f}  |theta/pi - 1| = "
              f"{b['rel_dev_from_pi']:.3e}")
    if rec.get("mult_pass") is not None:
        print(f"  TOL-MULT {'PASS' if rec['mult_pass'] else 'FAIL'} "
              f"(total {rec['mult_total_solver']} vs {rec['mult_total_ref']}); "
              f"min separation {rec['separation_min']:.3e} "
              f"{'PASS' if rec['separation_pass'] else 'FAIL'}")
    elif rec.get("mult_note"):
        print(f"  TOL-MULT NOT ASSERTED -- {rec['mult_note']}")


def verdict(report: dict) -> dict:
    """Bin the run against the FROZEN criteria.

    Reconcile-don't-declare: every clause below reads a COMPUTED field. Nothing
    here consumes a self-declared status string.
    """
    gating = ("L0", "L1", "L2v", "L2s", "L3", "L4")
    why: list[str] = []
    fatal, failures = [], []
    for key in gating:
        rec = report["rungs"][key]
        if rec.get("fatal"):
            fatal.append(f"{key}: solver diagnostics {rec['fatal'][:2]}")
            continue
        if rec.get("status") == "INCONCLUSIVE":
            fatal.append(f"{key}: INCONCLUSIVE")
            continue
        for label, ok in (("TOL-LOSSLESS", rec.get("lossless_pass")),
                          ("TOL-GRID", rec.get("tol_grid_pass")),
                          ("TOL-FREQ", rec.get("freq_pass")),
                          ("TOL-COUNT", rec.get("count_pass")),
                          ("TOL-MULT", rec.get("mult_pass"))):
            if ok is False:
                failures.append(f"{key}: {label}")
        if rec.get("refine_pass") is False:
            fatal.append(f"{key}: TOL-REFINE not met")
        if rec.get("separation_pass") is False:
            fatal.append(f"{key}: multiplicity separation below the floor")

    ctrl = report["controls"]
    if not ctrl["positive"]["detected"]:
        fatal.append("POSITIVE CONTROL missed the planted defect -- instrument not validated")
    else:
        why.append(f"positive control resolved a {POSITIVE_CONTROL_FACTOR}x planted bond-delay "
                   "defect and binned it as a divergence")
    if not ctrl["negative"]["pass"]:
        failures.append("NEGATIVE CONTROL: the single bond did not present as the bare "
                        "wiring-theorem half-wave")
    if not ctrl["convention"]["pass"]:
        failures.append("CONVENTION CONTROL: R2/R1 ratio is not sqrt(3)")
    else:
        why.append(f"convention control measured the R2/R1 ratio at "
                   f"{ctrl['convention']['ratio']!r} vs sqrt(3) "
                   f"(rel dev {ctrl['convention']['rel_dev']:.2e}) -- the FL-1 sqrt(3) hazard "
                   "is measured, not assumed")
    for key, t in ctrl["t6_si_native"].items():
        if not t["pass"]:
            failures.append(f"T6 SI/native paired control disagrees at {key}")

    if fatal:
        return {"bin": "INCONCLUSIVE", "why": why + fatal,
                "note": "MANDATORY bin -- never folded into any other."}
    if failures:
        return {"bin": "DIVERGE-ATTRIBUTED" if len(set(f.split(':')[0] for f in failures)) <= 2
                else "DIVERGE-UNATTRIBUTED", "why": why + failures}
    mult_run = [k for k in gating if report["rungs"][k].get("mult_measured")]
    mult_not = [k for k in gating if not report["rungs"][k].get("mult_measured")]
    grid_run = [k for k in gating if report["rungs"][k].get("tol_grid") is not None]
    why.insert(0, "every gating rung L0-L4 met TOL-FREQ, TOL-COUNT, TOL-REFINE and "
                  "TOL-LOSSLESS")
    why.insert(1, f"TOL-MULT asserted and PASSED on {mult_run}; NOT ASSERTED on {mult_not} "
                  "(single-port or no interior reference mode -- UNRUN, not passed)")
    why.insert(2, f"TOL-GRID defined and PASSED on {grid_run}; UNDEFINED elsewhere "
                  "(fewer than two interior reference modes, so no mode spacing exists)")
    why.append("SCOPE: this is IMPLEMENTATION-VERIFICATION. It validates that the engine "
               "solves its own equations; it says NOTHING about whether the axioms describe "
               "the vacuum, and it is not a chord, an emergence, or a falsification.")
    return {"bin": "AGREE", "why": why}


if __name__ == "__main__":
    sys.exit(main())
