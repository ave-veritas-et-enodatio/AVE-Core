#!/usr/bin/env python3
"""SCX Phase-1 exporter — engine adjacency to an ngspice netlist.

Lane: external-solver cross-check (SCX), Phase 1.
Prereg (FROZEN): ``research/2026-08-25_solver-crosscheck-phase1_prereg-FROZEN.md``
GO gate: ``_orchestration/docket-entries/2026-08-24-ruling-r56-scx-trades.md`` (R56).

CLASS
-----
IMPLEMENTATION-VERIFICATION (a sub-class of CONSISTENCY). This module mints no
physics. It translates a graph the ENGINE built into a netlist an INDEPENDENT
integrator can read, so that two integrators can be handed the same network.
Agreement validates that the engine solves its own equations; it says nothing
about whether the axioms describe the vacuum.

SECTOR DECLARATION (prereg sec 1)
---------------------------------
MODE numerical-infrastructure / REGIME I cold sub-yield lossless-reactive
(A = 0, S(A) = 1, Op14 not engaged) / PHASE-STATE cold crystalline quiescent /
CHANNEL scalar-translational ONLY (no Cosserat / T2 microrotation DOF is
exported, driven or read) / CARRIER srs-z3.

THE RATIFIED BOND REPRESENTATION (R56 item 1, T2 = option (a))
--------------------------------------------------------------
One SPICE lossless ``T`` element per srs bond, parameters (Z_0, TD), with the
z = 3 vertex realised as an ORDINARY SHUNT NODE. The Gamma = (2-z)/z = -1/3
junction mismatch emerges from the shunt node; it is not modelled. No lumped
L-C ladder is emitted on any srs rung -- a one-section-per-bond ladder IS the
lumped graph-Laplacian model the corpus rejected for failing the frozen
1/sqrt(3) velocity gate, and avoiding it is the load-bearing substrate-native
constraint on this module (prereg sec 1.5, CP3).

*** THE DELAY CONVENTION (R56 item 2) -- READ BEFORE TOUCHING TD ***
--------------------------------------------------------------------
THREE live in-tree symbols encode THREE DIFFERENT bond delays. Reaching for the
wrong one applies a uniform sqrt(3) (or 3x) offset to every frequency this lane
measures, which reads as a spectacular "engine defect" and is nothing but a
label mismatch:

  R2  (PINNED HERE)  TD = ANALYTIC_NETWORK_FACTOR / OMEGA_C   = 1/(sqrt3*w_C)
                     ave.core.chiral_lattice_dynamics.ANALYTIC_NETWORK_FACTOR
  R1  (NOT ours)     TD = ell_node / c_0                      = 1/w_C
                     ave.core.chiral_lattice.bond_lc()  <-- the symbol NAMED
                     "bond_lc", i.e. the one an exporter author reaches for.
  (iii) (NOT ours)   TD = sqrt(3)*ell_node / c_0              = sqrt3/w_C
                     src/scripts/vol_1_foundations/r10_v8_ee_phase_a.py:255

R56 item 2, verbatim: "R2 is PINNED as a TAGGED ENGINEERING CONVENTION for the
exporter only ... The corpus's physics-level R1-vs-R2 adjudication flag
(srs-band-structure.md:157, 'Flagged for adjudication') stays OPEN -- this
ruling selects the exporter's emitted label and mandates the machine check that
the emitted delay matches it; it does NOT adjudicate the corpus flag."

That machine check is ``src/tests/test_scx_spice_export.py`` and it fires in
BOTH directions (it asserts the R2 form holds AND that the R1/(iii) forms would
fail it). The hazard is caught by a test, not by vigilance.

ANTI-TAUTOLOGY (prereg sec 5)
-----------------------------
This module imports NO band-structure symbol and reads NO reference frequency.
It knows the graph and two line parameters. A comparison whose netlist knows the
answer is a checklist, not a gate; a test asserts the import restriction.

ZERO FREE PARAMETERS
--------------------
Topology comes from the engine; values come from ``ave.core.constants`` plus the
two canonical engine symbols named in SCX-REQ-ELEMENTS. Nothing is typed. Any
knob that would let the export be tuned toward agreement is a design defect
(epic sec 5.4), not a feature.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

from ave.core.chiral_lattice import _SRS_8A, _SRS_NN, LatticeNet, bond_lc
from ave.core.chiral_lattice_dynamics import ANALYTIC_NETWORK_FACTOR
from ave.core.constants import C_CELL, L_CELL, OMEGA_C, Z_0

__all__ = [
    "CONVENTION",
    "assert_canonical_source",
    "bond_delay",
    "bond_delay_r1_NOT_OURS",
    "bond_delay_iii_NOT_OURS",
    "edges_from_net",
    "srs_primitive_cell_edges",
    "AcAnalysis",
    "emit_tl_network",
    "emit_lc_tank",
    "emit_two_junction",
    "GROUND",
    "node_name",
]

#: The delay convention this module emits. R56 item 2. Machine-checked.
CONVENTION = "R2"

#: ngspice's global reference node.
GROUND = "0"


# ─────────────────────────────────────────────────────────────────────────────
# Canonical-source guard (SCX-REQ-ELEMENTS.2)
# ─────────────────────────────────────────────────────────────────────────────
def assert_canonical_source() -> Path:
    """Assert ``ave.core.constants`` resolves to the AVE-Core canonical module.

    Runs before a single netlist line is emitted (``ave-canonical-source``
    step 4). Returns the resolved path so a caller can echo it into a receipt.
    """
    import ave.core.constants as _c

    path = Path(_c.__file__).resolve()
    if path.parts[-4:] != ("src", "ave", "core", "constants.py"):
        raise RuntimeError(
            "canonical-source guard: ave.core.constants resolved to "
            f"{path}, which is not <repo>/src/ave/core/constants.py. "
            "Refusing to emit a netlist against a non-canonical constants module."
        )
    return path


# ─────────────────────────────────────────────────────────────────────────────
# The three bond delays. ONE of them is ours.
# ─────────────────────────────────────────────────────────────────────────────
def bond_delay() -> float:
    """The bond one-way electrical delay THIS EXPORTER EMITS: the R2 convention.

    ``TD = ANALYTIC_NETWORK_FACTOR / OMEGA_C`` -- two imported symbols, no typed
    sqrt(3), no typed number. R56 item 2.
    """
    return float(ANALYTIC_NETWORK_FACTOR / OMEGA_C)


def bond_delay_r1_NOT_OURS() -> float:
    """The R1 delay, ``ell_node/c_0``, built from ``bond_lc()``. NOT emitted.

    Present for exactly two consumers: the prereg's CONVENTION CONTROL (which
    measures the sqrt(3) hazard instead of paraphrasing it) and the FL-1 machine
    check (which asserts the emitted delay is NOT this). The screaming name is
    deliberate -- ``bond_lc`` is the symbol whose NAME invites the mistake.
    """
    lc = bond_lc()
    return float(lc["ell_node"] * math.sqrt(lc["L_per"] * lc["C_per"]))


def bond_delay_iii_NOT_OURS() -> float:
    """The THIRD live convention, ``sqrt(3)*ell_node/c_0``. NOT emitted.

    ``r10_v8_ee_phase_a.py:255`` sets ``bond_length_SI = np.sqrt(3.0) * L_NODE``
    and builds L/C from it, giving a delay 3x the R2 delay -- and moving the
    label the OPPOSITE direction from R2. FL-1(iii); present so the machine
    check is three-way rather than a clean binary fork.
    """
    return float(math.sqrt(3.0) * bond_delay_r1_NOT_OURS())


_DELAYS = {
    "R2": bond_delay,
    "R1": bond_delay_r1_NOT_OURS,
    "III": bond_delay_iii_NOT_OURS,
}


def _delay_for(convention: str) -> float:
    if convention not in _DELAYS:
        raise ValueError(f"unknown delay convention {convention!r}; expected one of {sorted(_DELAYS)}")
    return _DELAYS[convention]()


# ─────────────────────────────────────────────────────────────────────────────
# Graph source (T3 = engine adjacency export; SCX-REQ-GRAPH)
# ─────────────────────────────────────────────────────────────────────────────
def edges_from_net(net: LatticeNet, *, require_carrier: str = "srs-z3") -> list[tuple[int, int]]:
    """Undirected edge list from an ENGINE-BUILT ``LatticeNet``.

    Walks ``net.neighbors`` -- the engine's own adjacency, never a hand-built
    fixture (SCX-REQ-GRAPH.1: a fixture can silently drift from the engine's
    graph, which would make agreement meaningless and disagreement
    unattributable).

    Asserts ``net.carrier == require_carrier`` FIRST, so exporting the z = 4
    diamond instrument fails loudly rather than silently (SCX-REQ-GRAPH.2 --
    the diamond net is a non-canonical instrument, not the substrate).

    Raises if the net is a multigraph (two distinct bonds joining the same node
    pair): the caller must then decide to emit parallel ``T`` elements, and
    silently collapsing them would change the network.
    """
    if net.carrier != require_carrier:
        raise ValueError(
            f"carrier guard: net.carrier is {net.carrier!r}, expected {require_carrier!r}. "
            "Refusing to export -- SCX-REQ-GRAPH.2 fences the z=4 diamond instrument "
            "out of every phase of this epic."
        )
    seen: set[tuple[int, int]] = set()
    edges: list[tuple[int, int]] = []
    for u, nbrs in enumerate(net.neighbors):
        for v in nbrs:
            key = (u, v) if u < v else (v, u)
            if u == v:
                raise ValueError(f"self-loop at node {u}: not a valid TL bond")
            if key in seen:
                continue
            seen.add(key)
            edges.append(key)
    # Multigraph detection: each undirected pair must appear exactly twice in
    # directed walk (once from each end). More means parallel bonds.
    directed = sum(len(nbrs) for nbrs in net.neighbors)
    if directed != 2 * len(edges):
        raise ValueError(
            f"multigraph: {directed} directed ports collapse to only {len(edges)} "
            "distinct node pairs. Parallel bonds must be emitted as parallel T "
            "elements; refusing to silently merge them."
        )
    return edges


def srs_primitive_cell_edges() -> list[tuple[int, int]]:
    """The 4-site srs BCC primitive cell under real periodic wrap.

    Built from the ENGINE's own motif symbols (``_SRS_8A``, ``_SRS_NN`` in
    ``ave.core.chiral_lattice``) -- the same 8a Wyckoff coordinates and the same
    nearest-neighbour distance the engine's ``build_srs_net`` uses. The 8 sites
    split into 4 body-centred pairs {i, i+4} related by +(1/2,1/2,1/2); the BCC
    lattice absorbs the centring, so the 4-site basis carries the whole cell.

    Under real periodic wrap the resulting graph is 3-regular on 4 vertices,
    which is the complete graph K_4 (any simple 3-regular graph on 4 vertices
    is). Asserted here, not assumed.

    NOTE on the name: "K4" is adjudicated-overloaded (FL-4). This function
    returns the K_4 COMPLETE GRAPH, which is a third distinct object from both
    the Sunada-K4/srs net and the engine's z=4 diamond instrument.
    """
    motif = _SRS_8A
    basis = motif[:4]
    for i in range(4):  # the BCC pairing is exact -- verify, don't assume
        for axis in range(3):
            got = (motif[i][axis] + 0.5) % 1.0
            want = motif[i + 4][axis] % 1.0
            if abs(got - want) > 1e-12:
                raise AssertionError(f"srs BCC pairing broken at site {i}, axis {axis}")
    seen: set[tuple[int, int]] = set()
    for i in range(4):
        for m in range(8):
            for nx in range(-2, 3):
                for ny in range(-2, 3):
                    for nz in range(-2, 3):
                        d = (
                            motif[m][0] + nx - basis[i][0],
                            motif[m][1] + ny - basis[i][1],
                            motif[m][2] + nz - basis[i][2],
                        )
                        r = math.sqrt(d[0] * d[0] + d[1] * d[1] + d[2] * d[2])
                        if abs(r - _SRS_NN) < 1e-9:
                            j = m % 4
                            if i == j:
                                raise AssertionError("srs primitive cell produced a self-bond")
                            seen.add((i, j) if i < j else (j, i))
    edges = sorted(seen)
    if len(edges) != 6:
        raise AssertionError(f"srs primitive cell wrapped to {len(edges)} bonds, expected 6 (K_4 complete)")
    deg = [0, 0, 0, 0]
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    if deg != [3, 3, 3, 3]:
        raise AssertionError(f"srs primitive cell degrees {deg}, expected 3-regular")
    return edges


# ─────────────────────────────────────────────────────────────────────────────
# Emission
# ─────────────────────────────────────────────────────────────────────────────
def node_name(idx: int) -> str:
    """Netlist node name for graph node ``idx``. Never ``0`` (that is ground)."""
    return f"n{idx}"


def _fmt(x: float) -> str:
    """Emit a float so it re-reads to the IDENTICAL double.

    Python's ``repr`` is the shortest round-tripping representation. The
    prereg's CTRL-RT round-trip control asserts this property on every emitted
    number -- the one place a ``%g`` format could silently truncate a canonical
    constant and move a verdict.
    """
    return repr(float(x))


@dataclass(frozen=True)
class AcAnalysis:
    """One ``.AC`` analysis + its ``wrdata`` sink.

    ``kind`` is ngspice's sweep type (``lin``/``dec``/``oct``); ``n`` its point
    count; ``f1``/``f2`` the endpoints (equal for a single-point evaluation).
    ``out`` is the wrdata path; ``vectors`` the node names to write.
    """

    n: int
    f1: float
    f2: float
    out: str
    vectors: tuple[str, ...]
    kind: str = "lin"


def _control_block(analyses: list[AcAnalysis]) -> list[str]:
    """ngspice batch-mode contract: ``.AC`` under ``-b`` produces NO output
    unless the netlist carries an explicit ``.control`` block with a
    ``wrdata``/``print`` directive (established in-tree by the SPICE lane,
    ``src/ave/bench/spice_runner.py`` module docstring)."""
    lines = [
        ".control",
        "set numdgt=17",  # EC-6: output precision. Default 7 would report the formatter.
        "set filetype=ascii",
        "set wr_singlescale",
        "set wr_vecnames",
    ]
    for a in analyses:
        lines.append(f"ac {a.kind} {a.n} {_fmt(a.f1)} {_fmt(a.f2)}")
        lines.append("wrdata " + a.out + " " + " ".join(f"v({v})" for v in a.vectors))
    lines.append(".endc")
    return lines


def _header(title: str, convention: str, scaling: str, extra: list[str] | None = None) -> list[str]:
    """The netlist header. Echoes every imported symbol into the artifact.

    SCX-REQ-ELEMENTS.2 requires this: the netlist IS the epic sec 5.3(a)
    hand-audit artifact, so an auditor must be able to check it against
    ``constants.py`` without reading any Python.
    """
    td = _delay_for(convention)
    src = assert_canonical_source()
    lines = [
        f"* {title}",
        "*",
        "* SCX Phase-1 external-solver cross-check. CLASS: IMPLEMENTATION-VERIFICATION.",
        "* Prereg (FROZEN): research/2026-08-25_solver-crosscheck-phase1_prereg-FROZEN.md",
        "* GO gate: _orchestration/docket-entries/2026-08-24-ruling-r56-scx-trades.md (R56)",
        "* Emitted by: src/ave/solvers/scx_spice_export.py",
        "*",
        "* SECTOR: MODE numerical-infrastructure / REGIME I cold sub-yield lossless-reactive",
        "*         (A=0, S(A)=1, Op14 off) / PHASE-STATE cold crystalline quiescent /",
        "*         CHANNEL scalar-translational ONLY / CARRIER srs-z3.",
        "*",
        f"* CANONICAL SOURCE: {src}",
        "*",
        "* IMPORTED SYMBOLS (nothing below is typed; every value enters by import):",
        f"*   Z_0                      = {_fmt(Z_0)}  ohm     [ave.core.constants]",
        f"*   OMEGA_C                  = {_fmt(OMEGA_C)}  rad/s   [ave.core.constants]",
        f"*   ANALYTIC_NETWORK_FACTOR  = {_fmt(ANALYTIC_NETWORK_FACTOR)}          "
        "[ave.core.chiral_lattice_dynamics]",
        f"*   L_CELL                   = {_fmt(L_CELL)}  H       [ave.core.constants]",
        f"*   C_CELL                   = {_fmt(C_CELL)}  F       [ave.core.constants]",
        "*",
        f"* DELAY CONVENTION EMITTED: {convention}   (R56 item 2 pins R2 for the exporter;",
        "*   the corpus's physics-level R1-vs-R2 flag, srs-band-structure.md:157",
        "*   'Flagged for adjudication', STAYS OPEN -- this label is an engineering",
        "*   convention on the emitted netlist, NOT a physics adjudication.)",
        f"*   R2  TD = ANALYTIC_NETWORK_FACTOR/OMEGA_C = {_fmt(bond_delay())} s",
        f"*   R1  TD = ell_node/c_0                    = {_fmt(bond_delay_r1_NOT_OURS())} s",
        f"*   III TD = sqrt(3)*ell_node/c_0            = {_fmt(bond_delay_iii_NOT_OURS())} s",
        f"*   EMITTED TD                               = {_fmt(td)} s",
        "*",
        f"* UNITS SCALING: {scaling}   (T6; the observables are dimensionless ratios,",
        "*   so this cannot move a verdict -- it is a conditioning/readability choice.)",
    ]
    if extra:
        lines.append("*")
        lines.extend(f"* {e}" for e in extra)
    lines.append("*")
    return lines


def emit_tl_network(
    edges: list[tuple[int, int]],
    n_nodes: int,
    drive_node: int,
    analyses: list[AcAnalysis],
    *,
    title: str,
    convention: str = CONVENTION,
    native: bool = False,
    perturb_bond: tuple[int, float] | None = None,
    extra_header: list[str] | None = None,
) -> str:
    """Emit the ratified T2(a) network: ONE lossless ``T`` element per bond.

    The z = 3 vertex is an ordinary shunt node -- no junction model is emitted,
    because the Gamma = -1/3 mismatch IS the shunt node. Open terminations are
    expressed by simply not connecting a node (SCX-REQ-ANCHOR.1: open is the
    termination with the least exporter machinery between the graph and the
    solver; matched would give no resonance at all).

    Drive is a unit AC current source from ground INTO ``drive_node``, so
    ``v(n<drive>)`` IS the driving-point impedance Z_jj. An ideal current source
    is an open circuit to the homogeneous problem, so the poles of that
    impedance are the natural frequencies of the UNMODIFIED network.

    ``native`` emits the T6 normalised companion (Z_0 = 1, TD = 1); the
    dimensionless observables must agree with the SI run (prereg sec 5, T6
    paired control).

    ``perturb_bond = (index, factor)`` multiplies ONE bond's TD -- the prereg's
    POSITIVE CONTROL planted defect. It is recorded in the header, so a
    perturbed netlist can never be mistaken for a clean one.
    """
    td = _delay_for(convention)
    z0 = Z_0
    if native:
        td, z0 = 1.0, 1.0
    extra = list(extra_header or [])
    extra.append(f"GRAPH: {n_nodes} nodes, {len(edges)} bonds, drive at {node_name(drive_node)}")
    if perturb_bond is not None:
        idx, factor = perturb_bond
        extra.append(
            f"*** PLANTED DEFECT (POSITIVE CONTROL): bond #{idx} TD scaled by {factor!r}. "
            "THIS NETLIST IS DELIBERATELY WRONG."
        )
    lines = _header(title, convention, "native (Z0=1, TD=1)" if native else "SI", extra)
    lines.append(f"I_drv {GROUND} {node_name(drive_node)} AC 1")
    for k, (u, v) in enumerate(edges):
        td_k = td
        if perturb_bond is not None and perturb_bond[0] == k:
            td_k = td * perturb_bond[1]
        lines.append(
            f"T{k} {node_name(u)} {GROUND} {node_name(v)} {GROUND} "
            f"Z0={_fmt(z0)} TD={_fmt(td_k)}"
        )
    lines.extend(_control_block(analyses))
    lines.append(".end")
    return "\n".join(lines) + "\n"


def emit_lc_tank(analyses: list[AcAnalysis], *, title: str, native: bool = False) -> str:
    """Emit L0 / P1-A: one ``L_CELL`` in parallel with one ``C_CELL``.

    *** THIS RUNG CARRIES ZERO srs TOPOLOGY AND IS NOT A SUBSTRATE TEST. ***
    It is a solver-numerics smoke test only (SCX-REQ-ANCHOR.2/.3): its job is to
    prove a SPICE-class solver integrates 1e-19 H against 1e-24 F without
    tolerance pathology. Its "engine side" is an ARITHMETIC IDENTITY from
    ``constants.py``, not an engine run, so it is solver-vs-arithmetic and must
    never be reported as a two-integrator comparison.

    It is also the ONLY rung on which a lumped L-C pair is emitted at all -- see
    the module docstring's CP3 note.
    """
    ell, cee = (1.0, 1.0) if native else (L_CELL, C_CELL)
    lines = _header(
        title,
        CONVENTION,
        "native (L=C=1)" if native else "SI",
        ["L0/P1-A: lumped tank, NO srs topology. Solver-numerics smoke test ONLY",
         "(SCX-REQ-ANCHOR.2/.3). Engine side is an arithmetic identity, not an engine run."],
    )
    lines.append(f"I_drv {GROUND} {node_name(0)} AC 1")
    lines.append(f"L0 {node_name(0)} {GROUND} {_fmt(ell)}")
    lines.append(f"C0 {node_name(0)} {GROUND} {_fmt(cee)}")
    lines.extend(_control_block(analyses))
    lines.append(".end")
    return "\n".join(lines) + "\n"


def emit_two_junction(analyses: list[AcAnalysis], *, title: str, convention: str = CONVENTION) -> str:
    """Emit AUX-B: the bond-between-two-z3-junctions composite.

    Mirrors ``ave.viz.ave_chart.two_junction_gamma``: a near vertex whose other
    two bonds appear as a shunt Z_0/2, a Z_0 line of electrical length theta,
    and a far vertex terminating the line in Z_0/2.

    *** THE TWO RESISTORS ARE PORTS, NOT SUBSTRATE ELEMENTS. *** A Z_0/2
    resistor is the SPICE rendering of a reflectionless semi-infinite lossless
    bond pair: no energy is dissipated in the substrate, it leaves through a
    matched port. AUX-B is therefore the one rung whose netlist is not
    resistor-free, and the prereg's TOL-LOSSLESS does not apply to it.

    SCOPING inherited verbatim from ``two_junction_gamma``: an isolated /
    incoherent composite (per-vertex reading), NOT a claim about in-band
    collective transport.
    """
    td = _delay_for(convention)
    lines = _header(
        title,
        convention,
        "SI",
        ["AUX-B: two-junction composite (ave_chart.two_junction_gamma cross-solver check).",
         "The two Z_0/2 resistors are PORTS (semi-infinite matched bond pairs), NOT",
         "dissipative substrate elements. SUPPLEMENTARY / NON-GATING for the epic bin."],
    )
    lines.append(f"I_drv {GROUND} {node_name(0)} AC 1")
    lines.append(f"R_near {node_name(0)} {GROUND} {_fmt(Z_0 / 2.0)}")
    lines.append(f"T0 {node_name(0)} {GROUND} {node_name(1)} {GROUND} Z0={_fmt(Z_0)} TD={_fmt(td)}")
    lines.append(f"R_far {node_name(1)} {GROUND} {_fmt(Z_0 / 2.0)}")
    lines.extend(_control_block(analyses))
    lines.append(".end")
    return "\n".join(lines) + "\n"
