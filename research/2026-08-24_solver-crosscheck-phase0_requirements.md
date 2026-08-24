# External-Solver Cross-Check — Phase-0 Requirements (DERIVED)

**Date:** 2026-08-24 · **Lane:** external-solver cross-check, Phase 0 (implementer) · **Status:** DERIVED requirements datasheet; NOT canonized, mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`. Requirements are physics-set or explicitly engineering-tagged; every design CHOICE lives in the sibling trade study (STATUS: OPEN throughout).

**Epic this executes:** [`_orchestration/2026-08-23_external-solver-crosscheck-epic.md`](../_orchestration/2026-08-23_external-solver-crosscheck-epic.md) §4 Phase 0. **No implementation is authorized by this document** — Phase 1 gates on its own Grant GO.

**Sibling docs.**
- [`research/2026-08-24_solver-crosscheck-phase0_tradestudy.md`](2026-08-24_solver-crosscheck-phase0_tradestudy.md) — the OPEN decision space (T1–T6). **Derived = here. Open = there.**
- [`research/2026-08-24_solver-crosscheck-phase1-prereg-skeleton.md`](2026-08-24_solver-crosscheck-phase1-prereg-skeleton.md) — the frozen Phase-1 prereg SKELETON (bins/tolerances STRUCTURED, values marked `FROZEN-AT-PHASE-1-GO`).
- Structural template: the CVR/CLEAVE-01 bench-doc pattern — [`research/2026-07-13_cvr-requirements_DERIVED.md`](2026-07-13_cvr-requirements_DERIVED.md) (REQ-ID single-source-of-truth discipline) + [`research/2026-07-13_cvr-trade-study_DECISIONS-OPEN.md`](2026-07-13_cvr-trade-study_DECISIONS-OPEN.md) (options-with-consequences, selects nothing).

---

## §0 — SECTOR DECLARATION (binding; read before any requirement)

| axis | declaration |
|---|---|
| **MODE** | Numerical-infrastructure. **No new physics claim is minted by this epic or this doc.** |
| **REGIME** | Regime I — sub-yield, **lossless-reactive**, linear small-signal. Ax-4 saturation is OFF (`A = 0`); Op14 is not engaged. |
| **PHASE-STATE** | Cold lattice, quiescent (Axiom-5 clause Q operating point: $\varepsilon_{11}=0$). |
| **CHANNEL** | **Scalar / translational ONLY.** The vector/Cosserat channel is FENCED OUT (§6.3). |
| **CARRIER** | **srs-z3** — the D1-ratified production carrier ([`manuscript/ave-kb/common/axiom-register.md:147`](../manuscript/ave-kb/common/axiom-register.md), verified verbatim: *"the chiral z=3 srs net is the production carrier"*). |
| **consistency-vs-emergence** | **IMPLEMENTATION-VERIFICATION** — a sub-class of CONSISTENCY. Two independent integrators agreeing on the *same* network validates that the engine solves its own equations correctly. It says **nothing** about whether the axioms describe the vacuum, and no result from any phase of this epic may be framed as emergence, chord, or falsification of AVE. (Epic §1, re-declared here per the epic's §7 requirement that the register be re-declared in every doc.) |

**Does the engine carry the DOF under test?** Yes: the scalar/translational TLM channel is carried by `chiral_lattice.scalar_tlm_step` on `build_srs_net`, and its Bloch band structure by `srs_band_survey.py`. Both are in-tree and both are exercised below under a reproduction gate (§7).

---

## §0.5 — `substrate-native-check` walk (done BEFORE any requirement was written)

| checkpoint | walk result |
|---|---|
| **CP1 — substrate dynamics** | Discrete **scatter + connect** wave propagation on a distributed LC transmission-line network (Op5 TLM). NOT Lagrangian minimisation, NOT gradient descent, NOT continuum-Helmholtz, NOT an energy basin. The comparison target is a **network transient/AC response**, which is what a SPICE-class solver natively computes — the tool and the substrate agree on ontology, which is the whole reason this epic is cheap. |
| **CP2 — sector** | V-sector (scalar TLM) only. Cos-sector fenced out (§6.3). No cross-coupling (Op14 off at `A = 0`). |
| **CP3 — AVE-native objective** | TLM transmission eigenmode / network AC response. Explicitly **not** $\omega=\sqrt\lambda$ graph-Laplacian eigenmodes — that lumped model FAILS the frozen $1/\sqrt3$ velocity gate ([`srs-band-structure.md:49-67`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md), the load-bearing methods fact). **This is the single most important substrate-native constraint on the exporter**: a naive netlist of lumped $L$–$C$ per node reproduces the lumped model, i.e. the model the corpus already REJECTED. See T2. |
| **CP4 — coordinates** | The canonical claim is in **frequency space** ($\omega$ in units of $\omega_C$) and **reciprocal space** ($k$ on the BCC reciprocal lattice). Every comparison below is stated in those coordinates. The $\omega$-vs-$k$ discipline note ([`srs-band-structure.md:69-76`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md)) is binding: $\pi\sqrt3\,\omega_C$ is a **frequency**, not a wavevector, and must never be compared against the $k_{\max}$ family. |
| **CP5 — local clock** | Not applicable: `A = 0` everywhere, so $S(A)=1$ and $\omega_{local}=\omega_{global}$ uniformly. Recorded so its absence is a declared scope, not an omission. |
| **CP6 — reactance pair** | Applies only if T4 selects transient ringdown. If it does, BOTH the C-state and the L-state must be recorded over the window (a snapshot at one phase cannot distinguish static from oscillator-at-peak). Carried into the prereg skeleton as a conditional requirement. |
| **CP7 — sampling** | No PML anywhere in this epic (all networks are closed or explicitly port-terminated), so the PML-exclusion corollary is vacuously satisfied. No top-K density extraction is used. |
| **CP8–CP10** | CP8 (generative precursor) N/A — no emergence/hosting test. CP9 — every observable below is a **dynamically evolved / directly solved** network quantity in both integrators (no algebraic heuristic on either side). CP10 — no bulk force term anywhere; terminations are rendered as boundary conditions ($\Gamma$ at a port), which is also the only way SPICE can express them. |

---

## REQ-ID INDEX

`SCX-REQ-<NAME>` are the canonical, stable requirement identifiers for this epic (descriptive, reorder-proof; CLEAVE-01/CVR single-source-of-truth rule). Stamping an ID changes no derived number and selects no design knob.

| REQ-ID | One-line requirement | Class |
|---|---|---|
| `SCX-REQ-FRAME` | The binding epistemic frame: implementation-verification only; no phase of this epic can confirm or falsify AVE | frame (binding) |
| `SCX-REQ-GRAPH` | The exported graph is the engine's own srs-z3 adjacency, obtained by calling the engine — never a hand-built fixture, never the z=4 diamond instrument | physics-set + topology BC |
| `SCX-REQ-ELEMENTS` | Every element value is imported by symbol from `src/ave/core/constants.py`; the exporter has zero free parameters | physics-set |
| `SCX-REQ-LABEL` | The $\omega_C$ scale-label convention is **R2**, and the bond one-way delay is $\mathrm{TD} = \texttt{ANALYTIC\_NETWORK\_FACTOR}/\texttt{OMEGA\_C}$ — pinned so a $\sqrt3$ convention offset cannot masquerade as a defect | physics-set (convention-pinned) |
| `SCX-REQ-ANCHOR` | The Phase-1 pilot object and its **termination** are named explicitly; the anchor's resonance must be closed-form exact | physics-set |
| `SCX-REQ-OBS` | Each observable is named WITH its engine-side reference path AND that path's demotion status | physics-set + provenance |
| `SCX-REQ-FENCE` | The four comparison fences: first-branch-only, Bloch-inexpressibility, scalar-channel-only, wiring-theorem-scoping | scope BC (binding) |
| `SCX-REQ-REPRO` | Every engine-side reference number is re-derived on the current engine at comparison time (epic §5.2) | validation BC |

---

## §1 — `SCX-REQ-GRAPH` — which graph

**The graph is the chiral srs net, $z=3$, $I4_132$, obtained from the engine.**

| item | value | source (verified this branch) |
|---|---|---|
| Carrier | `srs-z3` | [`axiom-register.md:147`](../manuscript/ave-kb/common/axiom-register.md) (D1 RATIFIED, PR #486) |
| Builder | `build_srs_net(L, enantiomorph, a_cell)` → `LatticeNet` | [`src/ave/core/chiral_lattice.py:206`](../src/ave/core/chiral_lattice.py) |
| Self-reported carrier tag | `net.carrier == "srs-z3"` | [`src/ave/core/chiral_lattice.py:109-134`](../src/ave/core/chiral_lattice.py) (`LatticeNet.carrier`) |
| Node count | $8L^3$ (8-site conventional cell) | verified: `build_srs_net(L=3)` → 216 nodes, degree 3 (§7) |
| Bond count | $12L^3$ (each node degree 3, each bond shared) | $8L^3\cdot3/2$ |
| Bond length | exactly $\ell_{node}$ | `_SRS_NN = √2/4` cell units ([`chiral_lattice.py:60`](../src/ave/core/chiral_lattice.py)) with the physical `a_cell = 2√2·L_NODE` ([`chiral_lattice.py:210-215`](../src/ave/core/chiral_lattice.py)) ⇒ NN bond $=1.0\,\ell_{node}$ |
| Bipartite | **YES** — verified, not assumed | §7 receipt: `build_srs_net(L=3)` 2-colours 108/108; adjacency $\mu_{\min}=-3.0000000000$, $\mu_{\max}=+3.0000000000$ |
| Primitive cell | 4-site BCC (the 8 Wyckoff-8a sites split into 4 body-centred pairs) | [`srs_band_survey.py:56-80`](../src/scripts/vol_1_foundations/srs_band_survey.py) `srs_primitive_bcc` |

**`SCX-REQ-GRAPH.1` — the graph comes from the engine, not from a fixture.** The exporter calls `build_srs_net` (or the primitive-cell helper) and walks `net.neighbors` / `net.bond_unit`. A hand-built netlist fixture can silently drift from the engine's graph, which would make an agreement result meaningless and a disagreement unattributable. (T3 records the option space; the requirement here is the physics-side reason it matters.)

**`SCX-REQ-GRAPH.2` — "K4" is NOT offered as a graph option.** The surface name *K4* is adjudicated-overloaded: Axiom 1's object is the Sunada-**K4** / Laves / (10,3)-a / **srs** net (degree 3), whereas the engine's historical `k4_tlm.py` / `TETRA_OFFSETS` module is the achiral **diamond z=4** net, re-tagged a *non-canonical instrument* ([`engine-capability-map.md:186-205`](../manuscript/ave-kb/common/engine-capability-map.md) §8b.0). Exporting the diamond net would be exporting the instrument, not the substrate. **The z=4 diamond is out of scope for every phase** (epic §4, blind-audit finding 3.12).

> **⚑ Naming note, surfaced not fixed.** The Γ-point Bloch adjacency of the 4-site srs primitive cell is exactly $K_4$ the *complete graph* (spectrum $\{3,-1,-1,-1\}$, verified §7) — a third distinct object wearing the same two letters. Where this doc needs it, it is written **"$K_4$ complete graph"** in full. Flagged for the vocabulary lane; no rename attempted here.

---

## §2 — `SCX-REQ-ELEMENTS` — which element values (all imported by symbol)

**Every value below is an import-path citation. The exporter hard-codes nothing** (`ave-canonical-source`; the exporter therefore has no free parameter, epic §5.4).

| quantity | canonical symbol | import path | value at HEAD (§7 receipt) |
|---|---|---|---|
| Characteristic impedance | `Z_0` | [`src/ave/core/constants.py:113`](../src/ave/core/constants.py) | $376.73031346177066\ \Omega$ |
| Node cutoff | `OMEGA_C` | [`constants.py:305`](../src/ave/core/constants.py) | $7.76344071105011\times10^{20}$ rad/s |
| Lattice pitch | `L_NODE` | [`constants.py:293`](../src/ave/core/constants.py) | $3.8615926772428334\times10^{-13}$ m |
| Speed of light | `C_0` | [`constants.py:110`](../src/ave/core/constants.py) | $299\,792\,458.0$ m/s |
| Permeability | `MU_0` | [`constants.py:111`](../src/ave/core/constants.py) | $1.2566370614359173\times10^{-6}$ H/m |
| Permittivity | `EPSILON_0` | [`constants.py:112`](../src/ave/core/constants.py) | $8.854187817620389\times10^{-12}$ F/m |
| Cell tank inductance | `L_CELL` $=Z_0/\omega_C=\mu_0\ell_{node}$ | [`constants.py:321`](../src/ave/core/constants.py) | $4.85262047439289\times10^{-19}$ H |
| Cell tank capacitance | `C_CELL` $=1/(Z_0\omega_C)=\varepsilon_0\ell_{node}$ | [`constants.py:322`](../src/ave/core/constants.py) | $3.41912668394556\times10^{-24}$ F |
| Network projection | `ANALYTIC_NETWORK_FACTOR` $=1/\sqrt3$ | [`src/ave/core/chiral_lattice_dynamics.py:48`](../src/ave/core/chiral_lattice_dynamics.py) | $0.5773502691896258$ |
| Coordination | $z=3$ | `net.degree` from `build_srs_net`; `Z_DEG` at [`srs_band_survey.py:45`](../src/scripts/vol_1_foundations/srs_band_survey.py) | 3 |

**`SCX-REQ-ELEMENTS.1` — the two element pairs are DIFFERENT OBJECTS; do not substitute one for the other.**

- **The per-unit-length line pair** — `bond_lc()` ([`chiral_lattice.py:431-438`](../src/ave/core/chiral_lattice.py)) returns `L_per = Z_0/C_0` and `C_per = 1/(Z_0·C_0)`. Verified at HEAD: these are *bit-identical to* $\mu_0$ and $\varepsilon_0$ (§7). Units H/m and F/m.
- **The per-node lumped tank pair** — `L_CELL`, `C_CELL`. Units H and F. Round-trips: $\sqrt{L_{CELL}/C_{CELL}}=Z_0$ (rel. err. $1.5\times10^{-16}$) and $\sqrt{L_{CELL}C_{CELL}}=1/\omega_C=1.2880886674083153\times10^{-21}$ s (bit-identical), verified §7.

Both pairs give $Z_0$ on the $\sqrt{L/C}$ round trip; they differ in what the $\sqrt{LC}$ round trip means. **The $\sqrt{LC}$ round trip is where the exporter can silently pick a convention — see `SCX-REQ-LABEL` (§3), which is the load-bearing requirement of this whole document.**

**`SCX-REQ-ELEMENTS.2` — canonical-source cross-check is mandatory in the exporter.** Per `ave-canonical-source` Step 4, the exporter asserts `ave.core.constants.__file__` resolves to the AVE-Core canonical module before emitting a single netlist line, and echoes every imported symbol into the netlist as a comment header (which also makes the §5.3(a) hand-audit mechanical).

---

## §3 — `SCX-REQ-LABEL` — the $\omega_C$ scale-label convention, and the bond delay it fixes

**(Epic §4 Phase-0 named input 4.) This is the load-bearing requirement of Phase 0.** It is stated first as a rule, then as the flag that makes the rule necessary.

### §3.1 — THE RULE (binding on the exporter)

**Convention adopted: R2**, exactly as the canonical leaf adopts it ([`srs-band-structure.md:153-157`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md), verified verbatim):

> *"The $\omega_C$ **scale label** adopts **R2** ($c_0=$ the long-wavelength acoustic-branch velocity $=c_{\text{link}}/\sqrt3$, so $\omega_C=c_0/\ell_{\text{node}}=511$ keV; the microscopic link speed $c_{\text{link}}=\sqrt3\,c_0$ is sub-lattice, unobservable). Under R1 (calling $c_{\text{link}}=c_0$) every $\omega_C$ band label divides by $\sqrt3$ (top $\to\pi=3.142\,\omega_C$). Only the scale LABEL changes under R1, not the k-space band SHAPE or the gap inventory. Flagged for adjudication."*

Under R2 the bond's one-way electrical delay is therefore

$$
\boxed{\ \mathrm{TD} \;=\; \frac{\ell_{node}}{c_{link}} \;=\; \frac{1}{\omega_{link}} \;=\; \frac{1}{\sqrt3\,\omega_C} \;=\; \frac{\texttt{ANALYTIC\_NETWORK\_FACTOR}}{\texttt{OMEGA\_C}}\ }
$$

**Written that way on purpose**: the exporter obtains `TD` as `ANALYTIC_NETWORK_FACTOR / OMEGA_C` — two imported symbols, no typed $\sqrt3$, no typed number. Numerically at HEAD (§7): $\mathrm{TD} = 7.436783388682972\times10^{-22}$ s.

The bond line's characteristic impedance is `Z_0` unmodified ($376.73031346177066\ \Omega$), which is $\sqrt3$-invariant and therefore carries no convention risk.

**Consequences the requirement pins:**

| | R1 (`c_link = c_0`) | **R2 (ADOPTED)** |
|---|---|---|
| bond one-way delay TD | $1/\omega_C = 1.2880886674083153\times10^{-21}$ s | $\mathbf{1/(\sqrt3\,\omega_C) = 7.436783388682972\times10^{-22}}$ **s** |
| $\omega_{link}=1/\mathrm{TD}$ | $\omega_C$ | $\sqrt3\,\omega_C$ |
| scalar band top $\pi\,\omega_{link}$ | $3.1416\,\omega_C$ | $\mathbf{5.4414\,\omega_C = \pi\sqrt3\,\omega_C}$ |
| Γ optical multiplet | $1.9106\,\omega_C$ | $\mathbf{3.3093\,\omega_C}$ |
| acoustic phase velocity | $c_0/\sqrt3$ | $\mathbf{c_0}$ |

Both computed in §7. **A netlist built on R1 and compared against an R2 engine reference returns a uniform $\sqrt3=1.732$ ratio on every frequency observable** — which, absent this requirement, reads as a spectacular "engine defect" and is nothing but a label mismatch. That is precisely the masquerade epic §4 input 4 named.

### §3.2 — ⚑ FLAG-DON'T-FIX: two live engine symbols encode the two different conventions

**Surfaced with both paths and verbatim content; NOT resolved here, and nothing is edited.**

**Site A — `bond_lc()`, [`src/ave/core/chiral_lattice.py:431-438`](../src/ave/core/chiral_lattice.py)** (verbatim):

```python
def bond_lc():
    """Per-bond L, C from canonical constants (Z_0 = sqrt(L/C), c0 = 1/sqrt(LC))."""
    # c0 per node pitch: a node pitch L_NODE traversed in tau = L_NODE / C_0
    # Z_0 = sqrt(L/C), c0 = 1/sqrt(LC) -> L = Z_0/c0, C = 1/(Z_0 c0) per unit length.
```

Read as line parameters for a bond of physical length $\ell_{node}$, this gives $\mathrm{TD}=\ell_{node}\sqrt{\mu_0\varepsilon_0}=\ell_{node}/c_0=1/\omega_C$ — **the R1 delay**. Its own comment says it explicitly: *"a node pitch L_NODE traversed in tau = L_NODE / C_0"*.

**Site B — `ANALYTIC_NETWORK_FACTOR`, [`src/ave/core/chiral_lattice_dynamics.py:41-48`](../src/ave/core/chiral_lattice_dynamics.py)** (verbatim):

```python
# Analytic anchor: the 3D link-line TLM network velocity is c_link / sqrt(D=3).
# One scatter+connect step advances a signal exactly one bond (c_link = bond/step);
# the long-wavelength scalar mode propagates at the 3D-isotropic projection
# c0 = c_link / sqrt(3).
ANALYTIC_NETWORK_FACTOR = 1.0 / np.sqrt(3.0)
```

and its consumer [`srs_band_survey.py:46-47`](../src/scripts/vol_1_foundations/srs_band_survey.py):

```python
FACTOR = ANALYTIC_NETWORK_FACTOR  # 1/√3, imported (never hard-coded)
OMEGA_LINK_OVER_C = 1.0 / FACTOR  # ω_link / ω_C = √3 (derived from the symbol)
```

This gives $\mathrm{TD}=1/\omega_{link}=1/(\sqrt3\,\omega_C)$ — **the R2 delay**.

**Why the existing green gate does not catch it.** Acceptance test T0.2 ([`src/tests/engine_acceptance/test_l0_medium.py:118-155`](../src/tests/engine_acceptance/test_l0_medium.py)) asserts three things on `bond_lc()`: $\sqrt{L/C}=Z_0$, $Z_0=\sqrt{\mu_0/\varepsilon_0}$, and `1/√(LC) != c₀` fails — i.e. it *asserts* $1/\sqrt{L_{per}C_{per}}=c_0$. The first two are $\sqrt3$-invariant. The third is the R1 statement, asserted as a Class-A identity. So T0.2 is green under R1 by construction and is silent about R2's link speed. **Nothing in the suite compares the two sites.**

**Scope of the flag.** This is a **naming/reading hazard, not a demonstrated numerical bug**: `bond_lc()` is consumed only for the *impedance* identity and for reading $\varepsilon_0$/$c_0$ back off the medium ([`_em_media.py:301-303`](../src/tests/engine_acceptance/_em_media.py), [`test_p1b_photon_l2_on_srs.py:265-269`](../src/tests/engine_acceptance/test_p1b_photon_l2_on_srs.py)) — never as a bond transit time — so no in-tree result is known to be wrong. The hazard is that the symbol is *named* `bond_lc` and *worded* per-bond, so an exporter author reaching for "the bond's L and C" lands on R1 and gets a uniform $\sqrt3$ offset. **Routed to the auditor lane for adjudication** (is `bond_lc` the emergent-medium constitutive pair mis-named per-bond, or is the R1/R2 fork genuinely open at bond level?). This lane does not rename, re-word, or re-derive either site.

### §3.3 — the same fork couples into T2

The bond-representation trade (T2) is not convention-neutral: the **lumped-LC-ladder** option most naturally reaches for `L_CELL`/`C_CELL` per section, whose $\sqrt{LC}$ is $1/\omega_C$ — i.e. it lands on R1 unless deliberately rescaled — while the **TL-element** option takes $(Z_0,\mathrm{TD})$ directly and lands on R2. This coupling is recorded in the trade study and is part of why T2 is Grant's call.

---

## §4 — `SCX-REQ-ANCHOR` — the Phase-1 pilot object and its termination

**(Epic §4 Phase-0 named input 3.)** *"Single cell"* is ambiguous and must be defined. The epic states the reason verbatim: an srs $z=3$ vertex is *"an intrinsically MISMATCHED reciprocal 3-port"* with $\Gamma=(2-z)/z=-1/3$ ([`translation-circuit.md:189`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md), verified verbatim: *"A wave down one bond sees the other two in parallel ($Z_0/2$), so the bare junction reflects $\Gamma=(2-z)/z=-1/3$"*), so a bare vertex has **no resonance at all** until its bonds are terminated.

### §4.1 — the pilot ladder (three objects, in order; each closed-form exact)

| # | object | termination | closed-form resonances (R2) | what it tests |
|---|---|---|---|---|
| **P1-A** | **Bare cell LC tank** — one `L_CELL` + one `C_CELL` | closed loop (no ports) | $\omega_0 = 1/\sqrt{L_{CELL}C_{CELL}} = \omega_C$ **exactly** | **Solver numerics ONLY.** Zero srs topology, zero exporter graph path. Its job is to prove a SPICE-class solver integrates $10^{-19}$ H against $10^{-24}$ F without tolerance pathology (see T6). It is **not** a substrate test and must never be reported as one. |
| **P1-B** | **One bond** — a single lossless TL, $Z_0$, delay TD | both far ends **OPEN** | $\omega_n = n\pi/\mathrm{TD} = n\pi\,\omega_{link}$, $n=1,2,\dots$; first at $\pi\sqrt3\,\omega_C = 5.4414\,\omega_C$ | The **half-wave / Bragg** object itself. Makes the Phase-2 structural band-top check a *single-bond* fact, and is the cleanest possible three-way anchor (analytic / engine / solver). |
| **P1-C** | **One vertex + 3 bonds** ($z=3$ shunt junction, three stubs) | all three far ends **OPEN**, identical | symmetric mode: $\omega=n\pi/\mathrm{TD}$; two-fold degenerate differential modes: $\omega=(2n-1)\pi/(2\,\mathrm{TD})$, first at $\tfrac{\pi}{2}\sqrt3\,\omega_C = 2.7207\,\omega_C$ | The **first object where the $z=3$ mismatch is load-bearing.** The 2-fold degeneracy of the differential modes is the junction's own $\Gamma=-1/3$ physics showing up as a spectrum, and it is the first place an exporter connectivity bug can appear. |
| **P1-D** | **Smallest nontrivial cluster** — the 4-site srs primitive cell, real periodic wrap (= the $K_4$ complete graph of 6 lossless lines) | periodic (no external ports) | first branch: $\{0,\ 3.3093,\ 3.3093,\ 3.3093\}\,\omega_C$ — the Γ-point acoustic zero + the **triply-degenerate optical multiplet** $\sqrt3\arccos(-1/3)$ | The GATE to Phase 2. Reproduces the canonical Γ-point multiplet exactly (§7), and it is a genuine **Bloch** object a netlist CAN carry (§5.1). |

**`SCX-REQ-ANCHOR.1` — OPEN, not SHORT, not MATCHED.** The termination is **open-circuit** at every far end in P1-B/P1-C, for three reasons: (i) matched ($Z_0$) terminations give $\Gamma=0$ and therefore *no resonance at all* — nothing to compare; (ii) short-circuit gives the same $n\pi/\mathrm{TD}$ ladder for P1-B but a *different* mode assignment in P1-C, so open-vs-short is itself a discriminating structural check and must be pinned rather than left to the exporter's default; (iii) open is what a netlist expresses by simply not connecting the node, so it is the termination with the least exporter machinery between the graph and the solver.

**`SCX-REQ-ANCHOR.2` — P1-A is a numerics smoke test, not the epic's anchor.** The epic's Phase-1 adjudication anchor (*"the single cell's resonance is analytically exact, so BOTH the engine and the solver are first checked against the closed-form value independently"*) is satisfied by **P1-B**, which is analytically exact AND carries the substrate's bond object. P1-A is retained below it purely to localise a numerics failure before it contaminates P1-B.

**`SCX-REQ-ANCHOR.3` — the engine side of P1-A has no TLM reference.** `L_CELL`/`C_CELL` are constants, not a network the TLM steps. So P1-A's "engine side" is an arithmetic identity from `constants.py`, not an engine run. Stated so P1-A is not miscounted as a two-integrator comparison — it is solver-vs-arithmetic.

**`SCX-REQ-ANCHOR.4` — the engine's TLM primitive currently cannot express a 1-port termination.** `scatter_matrix(n)` raises `ValueError("n must be >= 2")` ([`chiral_lattice.py:99-100`](../src/ave/core/chiral_lattice.py)), so an open-terminated leaf node is not constructible with the engine primitive as it stands. The closed form the function implements, $S_{ij}=2/n-\delta_{ij}$, extends to $n=1$ giving $S=[+1]$ (i.e. $\Gamma=+1$, open) — so this is a guard, not a physics gap. **Consequence for Phase 1:** either (a) the guard is relaxed at Phase-1 GO (a small engine touch that needs its own justification and is NOT authorized here), or (b) P1-B / P1-C are run as **two-way** analytic-vs-solver comparisons rather than the epic's three-way anchor. Recorded so the choice is made deliberately rather than discovered at integrator time. **This is a T-study input, surfaced not decided.**

**`SCX-REQ-ANCHOR.5` — verified mode sets (§7 receipts, not assertions).** The P1-B and P1-C ladders above were checked by building the TLM one-step operator $M=\mathrm{Connect}\cdot\mathrm{blockdiag}(S)$ directly and diagonalising it (orthogonality confirmed to $\le1.8\times10^{-16}$):

| object | TLM eigenphases $\theta=\omega\,\mathrm{TD}$ | reading |
|---|---|---|
| P1-B | $\{0,\ \pi\}$ | the single half-wave resonance at $\pi\,\omega_{link}=5.4414\,\omega_C$ |
| P1-C | $\{0,\ \pi/2\ (\times4),\ \pi\}$ | $\pi/2$ with multiplicity 4 $=$ the **2-fold degenerate differential pair** counted with its $e^{\pm i\theta}$ partner; $\pi$ $=$ the symmetric half-wave mode. Exactly the analytic prediction. |
| P1-D ($K_4$ complete graph) | $\{0\ (\times4),\ 1.910633\ (\times6),\ \pi\ (\times2)\}$ | $1.910633 = \arccos(-1/3)$, i.e. the Γ optical multiplet $3.3093\,\omega_C$, ×3 bands ×2 for the $\pm$ pair. See F5 for the $\theta\in\{0,\pi\}$ blocks. |

---

## §5 — `SCX-REQ-OBS` — the observables, each with its engine-side reference path and that path's demotion status

**(Epic §4 Phase-0 named inputs 1, 2 and 5.)** Every row names the engine-side path that computes the reference AND records whether that path walks through a demoted claim. **Epic §10 is binding: no reference ⇒ no test.**

### §5.0 — demotion audit of the reference leaf (input 5)

`srs-band-structure.md` carries two dated demotion notes. **Verified this branch, by line:** the demoted rows are `:89`, `:94`, `:102`/`:104`, `:116`, `:120`/`:122`, `:131` — **every one of them is in §3 (vector/Cosserat channel), §4 (per-branch velocity map) or §5 (consumers)**, and every one is a *longitudinal/bulk-branch* row killed by the Axiom-5 bound-response ruling (R40 batches 1 and 2a).

**§1 (scalar band top + gap inventory, `:27-47`) and §2 (the arccos TL methods fact, `:49-76`) carry NO demotion marker and are the only sections this epic extracts from.** That is the epic's own scoping and it verifies. Every OBS row below cites §1 or §2 only.

> ⚑ Two stale line-cites noticed inside `srs-band-structure.md` while doing this audit, **surfaced not fixed**: `:145` cites `constants.py:294` for `OMEGA_C` (actually `:305`) and `:117` cites `constants.py:770` for `V_LONG` (actually `:781`). Pure line-drift, content correct at both real sites. Routed to the auditor lane; not repaired by this lane.

### §5.1 — the Bloch-expressibility problem and how each observable answers it (input 1)

**The problem, stated exactly.** The canonical scalar band structure is a **3D Bloch object** on the 4-site srs primitive cell: $\omega_n(\mathbf k)=\omega_{link}\arccos(\mu_n(\mathbf k)/3)$, where $\mu_n$ are eigenvalues of the $4\times4$ **complex** Bloch adjacency $A_{ij}(\mathbf k)=\sum_{bonds}e^{i\mathbf k\cdot\boldsymbol\delta}$ ([`srs_band_survey.py:83-96`](../src/scripts/vol_1_foundations/srs_band_survey.py)). **A SPICE netlist cannot impose a complex Bloch phase** — a wire either connects two nodes or it does not; there is no `e^{i\mathbf k\cdot\boldsymbol\delta}` boundary element in the lumped/TL device set.

**What IS expressible.** Real periodic wrap. A netlist that wraps an $L\times L\times L$ supercell with ordinary wires realises exactly the $\mathbf k$-points where every Bloch phase is real and consistent — i.e. the **commensurate mesh** $\mathbf k \in \{(2\pi/L)\,\mathbf n\}$, all sampled *simultaneously and unlabelled*. The two tractable substitutes, and exactly what each does and does not compare:

| substitute | WHAT IT COMPARES | WHAT IT DOES **NOT** COMPARE |
|---|---|---|
| **(A) Finite 3D supercell eigenfrequency SET** (real periodic wrap, $L^3$ cells) | The **unlabelled multiset** of band frequencies over the commensurate $\mathbf k$-mesh: band edges reachable on that mesh, the *absence* of an internal gap on that mesh, the band top, the Γ multiplet, and every degeneracy multiplicity. Verified to reproduce the arccos map exactly for $L=2$ (§7). | The **$\mathbf k$-LABEL.** The set carries no assignment of frequency→wavevector, so it cannot test the *dispersion relation* $\omega(\mathbf k)$ — only its image. It also cannot resolve any band feature finer than the mesh spacing $2\pi/L$: at $L=2$ the highest interior mode is $0.7977\pi\,\omega_{link}=4.339\,\omega_C$, well below the true top, so **"the top is missing" at small $L$ is a mesh artefact, not a divergence** (see §5.3 OBS-4). |
| **(B) Long open-chain $S_{21}$ phase-unwrap** | The dispersion of **a 1D chain of srs cells** — a genuine, well-defined object with a genuine $\beta(\omega)$ extractable from the two-port phase. | **The canonical $\omega(\mathbf k)$.** The srs net is a 3D $z=3$ net, not a chain; a chain built from it is a *different network* with its own band structure. Comparing a chain's $\beta(\omega)$ to the 3D Bloch bands is a category error of the same family as comparing a frequency to a wavevector (`srs-band-structure.md:69-76`). Additionally, the chain's own terminations enter its $S_{21}$, so the object is termination-dependent in a way $\omega(\mathbf k)$ is not. |

**RULING FOR THIS EPIC (lane's call, recorded here, T-study T4 carries the option space): the dispersion observable is (A), the finite 3D supercell eigenfrequency SET.** (B) is retained only as an optional Phase-2 *supplementary* run, and if run must be reported as *"the 1D-reduced chain's dispersion"* and never as *"the srs band structure"*.

### §5.2 — the observable table

| OBS | observable | engine-side reference path | demotion status of that path | wiring-theorem? |
|---|---|---|---|---|
| **OBS-1** | **P1-B single-bond half-wave resonance** $=\pi\,\omega_{link}=5.4414\,\omega_C$ | closed form from `Z_0` + `TD` (§3.1); TLM cross-check by direct diagonalisation of $M$ (§4, `SCX-REQ-ANCHOR.5`) | leaf-free (closed form) | **YES** — it is the definition of a half-wave line. Its job is the analytic anchor, not independence. |
| **OBS-2** | **Scalar band TOP** $=\pi\sqrt3\,\omega_C=5.4414\,\omega_C$, presenting as a **Bragg / half-wave resonance, not a stop-band edge** | [`srs-band-structure.md:32-39`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md) §1 Resultbox + §2 model table `:62`; class fact at [`translation-circuit.md:884-888`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md) carve 4 (verified verbatim: *"the srs net has NO internal stop-band — its band top is a **Bragg / half-wave resonance** … not a band-gap edge"*) | **CLEAN** (§1/§2, no marker) | **YES** — a theorem of {3-regular, bipartite, identical lossless lines}, attained iff the adjacency spectrum reaches $\mu=-3$, which srs's bipartiteness guarantees (**bipartiteness VERIFIED, §7**). **Exporter-integrity gate ONLY** (epic §4 Phase 2, blind-audit finding 3.8). |
| **OBS-3** | **The srs INTERIOR band-edge set** $\{1.6547,\ 2.1321,\ 3.3093,\ 3.7867\}\,\omega_C$ (band-1 bottom; band-0 top = band-2 bottom; band-1 top = band-3 bottom; band-2 top) **plus the no-internal-gap overlap structure** | [`srs-band-structure.md:41-45`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md) §1 gap inventory; recomputed by [`srs_band_survey.py:151-172`](../src/scripts/vol_1_foundations/srs_band_survey.py) `dense_scan` | **CLEAN** (§1, no marker) | **NO** — see §5.3. **This is the epic's input-2 deliverable: the quantitative observable whose value is NOT fixed by {3-regular, bipartite, identical lossless lines} alone.** |
| **OBS-4** | **Finite supercell eigenfrequency SET** (real periodic wrap, $L=2$ then $L=3$) | $\omega=\omega_{link}\arccos(\mu/3)$ on $\mathrm{eig}(A)$ of `build_srs_net(L)` — the same construction as [`srs_band_survey.py:137-148`](../src/scripts/vol_1_foundations/srs_band_survey.py) `direct_graph_laplacian_lambda_max`, extended from $\lambda_{\max}$ to the full spectrum; **plus the cycle-space block, F5** | **CLEAN** (engine path, no leaf claim consumed beyond §2's map) | **NO** — the whole spectrum depends on the supercell's exact geometry. This is the Phase-1/2-class Bloch substitute (A). |
| **OBS-5** | *(optional, supplementary)* **N-cell open-chain $S_{21}$** phase-unwrap $\beta(\omega)$ | none in-tree — would have to be built | n/a | n/a — **NO ENGINE REFERENCE ⇒ NOT A TEST** under epic §10 unless a reference is built first. Retained as an option in T4, gated on that. |
| **OBS-6** | **Γ-point spectrum** $\{0,\ 3.3093\ (\times3)\}\,\omega_C$, the triply-degenerate optical multiplet $\sqrt3\arccos(-1/3)$ | [`srs-band-structure.md:44-45`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md) §1; recomputed by `bands_at(0, bonds)` [`srs_band_survey.py:91-96`](../src/scripts/vol_1_foundations/srs_band_survey.py) | **CLEAN** (§1, no marker) | **PARTLY** — at $\mathbf k=0$ the 4-site Bloch adjacency is the $K_4$ complete graph (any simple 3-regular graph on 4 vertices is), so $\mu=\{3,-1,-1,-1\}$ follows from the primitive-cell SIZE plus 3-regularity. Useful as a second integrity gate; **must not be headlined as independence.** |

### §5.3 — why OBS-3 is NOT a wiring theorem (the input-2 argument, with a receipt)

The premise set OBS-2 is a theorem of is **{3-regular, bipartite, identical lossless lines}**. The **honeycomb net satisfies all three** and gives, under the same arccos TL map (§7 receipt):

- **2 bands, not 4** — envelopes $[0,\ 2.7155]$ and $[2.7259,\ 5.4414]\,\omega_C$ (the small gap between them is a finite-mesh artefact of the $400\times400$ scan; the analytic Dirac touching is at $\sqrt3\arccos(0)=\tfrac{\pi\sqrt3}{2}=2.7207\,\omega_C$);
- **the SAME band top** $5.4414\,\omega_C=\pi\,\omega_{link}$ — confirming the top is the wiring theorem;
- **not one of srs's four interior edges** $\{1.6547, 2.1321, 3.3093, 3.7867\}$ appears, and honeycomb has a **Dirac touching** where srs has a fully-overlapping four-band manifold.

**Therefore the interior edge set and the overlap structure are fixed by the srs geometry — the bond displacement vectors $\boldsymbol\delta$ — and not by the premise set.** A solver reproducing them has reproduced something the exporter's wiring alone does not force, which is exactly the independence weight epic §4 Phase 2 says the quantitative comparison must carry.

**Residual honesty (named, not hidden).** The honeycomb contrast differs from srs in *primitive-cell size* as well as in geometry, and cell size is not in the premise set — so the contrast establishes *"not fixed by {3-regular, bipartite, identical lossless lines}"*, which is the claim the epic asks for, but it does **not** establish *"not fixed by {3-regular, bipartite, identical lossless lines, 4-site primitive cell}"*. A tighter contrast (a second 4-site 3-regular bipartite 3D net) would close that gap and is named here as an **optional Phase-1 hardening**, not a Phase-0 debt.

---

## §6 — `SCX-REQ-FENCE` — the comparison fences (binding on every phase)

Each fence names a way a **correct** export can look like a divergence. Pre-registering them is the difference between an attributable result and a debugging spiral.

**F1 — FIRST-BRANCH ONLY (aliasing fence).** The engine's TLM is a **discrete-time** map: one scatter+connect step advances a signal exactly one bond ([`chiral_lattice_dynamics.py:42-43`](../src/ave/core/chiral_lattice_dynamics.py)), so its step is $\Delta t=\mathrm{TD}$ and its representable band is $\theta=\omega\,\mathrm{TD}\in[0,\pi]$, i.e. $\omega\le\pi\,\omega_{link}$ — the band top. A **continuous-time** SPICE TL network has the full ladder $\theta=\pi,2\pi,3\pi,\dots$ (verified: P1-B's continuous resonances are $n\pi/\mathrm{TD}$, of which the TLM operator carries only $n=1$; §4 `SCX-REQ-ANCHOR.5`). **Every comparison is restricted to $\omega\le\pi\,\omega_{link}=5.4414\,\omega_C$. Solver modes above the band top are EXPECTED and are not divergences.** *(This fence is about instrument scope only. It does not touch, and must not be read as touching, the canonical statement at `srs-band-structure.md:69-76` that $\pi\cdot\omega_{link}$ is a physical Bragg/half-wave resonance and "**not** a temporal-Nyquist artifact" — that is a statement about the physics of a half-wave line, this is a statement about what a discrete-time integrator can represent. See §8 Q1, which asks Grant the physics question the coincidence raises.)*

**F2 — NO BLOCH PHASE.** §5.1. Only real periodic wrap is exportable; only substitute (A) is used; the $\mathbf k$-label is not compared.

**F3 — SCALAR CHANNEL ONLY.** The vector/Cosserat channel is out of scope for every phase of this epic. Its band top is a live bracket $[5.441,17.011]\,\omega_C$ **whose upper arm is itself DEMOTED** ([`srs-band-structure.md:89,94,102-104`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md), R40 batches 1/2a) and gated on a PENDING-Grant single-scale-vs-stiffness-lifted ruling. **There is no stable reference number to compare against, so there is no test** (epic §10). The exporter emits one scalar node variable per node and nothing else.

**F4 — WIRING-THEOREM SCOPING.** OBS-2 and OBS-6 are exporter-integrity gates. **The independence weight rests on OBS-3 and OBS-4.** Any result doc that headlines the band-top reproduction as independence is out of scope by construction (epic §3 SCOPE-KILL).

**F5 — THE CYCLE-SPACE BLOCK (Phase-0-surfaced; not in the epic's named inputs).** A finite TLM network's natural-frequency set is **NOT** the arccos-map set. Verified by direct diagonalisation of $M$ (§7):

| network | $N$ | $B$ | arccos-map values | TLM operator spectrum |
|---|---|---|---|---|
| $K_4$ complete graph | 4 | 6 | $\theta\in\{0,\ 1.910633(\times3)\}$ | $\theta\in\{0(\times4),\ 1.910633(\times6),\ \pi(\times2)\}$ |
| srs supercell $L=2$ | 64 | 96 | 64 values, incl. $\theta=0(\times1)$, $\theta=\pi(\times1)$ | 192 values; **$\theta=0$ has multiplicity 34 and $\theta=\pi$ has multiplicity 34** |

The excess is the graph's **cycle space**: $B-N+1$ independent cycles (33 for the $L=2$ supercell), appearing as a degenerate block at $\theta=0$ **and** at $\theta=\pi$ — i.e. **piled exactly at DC and at the band top**. Interior arccos values appear with doubled multiplicity (the $e^{\pm i\theta}$ pair). **Consequence:** a naive set-comparison of "resonances SPICE reports" against "arccos values" sees ~66 unexplained modes on an $L=2$ supercell and reads them as a divergence. They are not. **The prereg must compare the INTERIOR spectrum ($0<\theta<\pi$) with multiplicities halved, and treat the $\theta\in\{0,\pi\}$ blocks as separately-counted cycle-space degeneracies.**

**F6 — DARK MODES AT A DRIVEN PORT (observability fence).** A driven-port observable (driving-point impedance, $S_{11}$, $S_{21}$) sees only modes with nonzero response at that port. Worked case: P1-C's two differential modes at $\theta=\pi/2$ have **zero voltage at the vertex**, so a source driving the vertex cannot excite them and a driving-point sweep there returns only the symmetric $\theta=\pi$ family. **Whichever observable T4 selects, the prereg must state the drive/observe points and which modes are consequently unobservable — an unobservable mode is not a missing mode.**

---

## §7 — `SCX-REQ-REPRO` — reproduction-gate receipts taken while writing this datasheet

**Status of these numbers.** Phase 0 authorizes **no implementation** (epic §4), so the checks below were run as **untracked scratch verification** against the current worktree HEAD, purely to keep this datasheet's statements from being un-audited assertions. **They are NOT banked receipts.** At Phase-1 GO every one of them is re-derived by a tracked driver under the epic §5.2 reproduction gate, and any drift between these and the fresh values is itself a finding to be banked under a dated note — never silently overwritten.

**Environment:** worktree `research/2026-08-24-solver-crosscheck-phase0` off `origin/main` at `ff0fde8b`; `PYTHONPATH=<worktree>/src` (worktree-aware import discipline, `CLAUDE.md` § *Worktree-aware local validation*).

### R1 — canonical constants and the two candidate bond delays

| quantity | value |
|---|---|
| `Z_0` | 376.73031346177066 Ω |
| `OMEGA_C` | 7.76344071105011e+20 rad/s |
| `L_NODE` | 3.8615926772428334e-13 m |
| `L_CELL` | 4.85262047439289e-19 H — **bit-identical** to `MU_0*L_NODE` |
| `C_CELL` | 3.41912668394556e-24 F — equals `EPSILON_0*L_NODE` to machine precision (not bit-identical) |
| $\sqrt{L_{CELL}/C_{CELL}}$ | 376.7303134617706 (vs `Z_0`, rel. err. 1.5e-16) |
| $\sqrt{L_{CELL}C_{CELL}}$ | 1.2880886674083153e-21 s — **bit-identical** to `1/OMEGA_C` |
| `bond_lc()["L_per"]` | 1.2566370614359173e-06 H/m — **bit-identical to `MU_0`** |
| `bond_lc()["C_per"]` | 8.854187817620389e-12 F/m — **exactly `EPSILON_0`** (rel. diff 0.000e+00) |
| $\mathrm{TD}$ under **R1** ($\ell_{node}/c_0$) | 1.2880886674083153e-21 s → band top **3.1416** $\omega_C$ |
| $\mathrm{TD}$ under **R2** (`ANALYTIC_NETWORK_FACTOR/OMEGA_C`) | **7.436783388682972e-22 s** → band top **5.4414** $\omega_C$ |
| ratio | 1.732050807568877 (vs $\sqrt3$ = 1.7320508075688772) |

### R2 — scalar band structure reproduces the banked numbers at HEAD

Dense 48³ scan of the 4-site BCC primitive cell, arccos TL map, `OMEGA_LINK_OVER_C` imported:

| band | computed envelope ($\omega_C$) | banked ([`srs-band-structure.md:43-44`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md)) |
|---|---|---|
| 0 | [0.0000, 2.1321] | [0, 2.132] ✓ |
| 1 | [1.6547, 3.3093] | [1.655, 3.309] ✓ |
| 2 | [2.1321, 3.7867] | [2.132, 3.787] ✓ |
| 3 | [3.3093, **5.4414**] | [3.309, **5.441**] ✓ |

- global top 5.4414 vs $\pi\sqrt3=5.4414$ ✓
- Γ: $\mu=\{3,-1,-1,-1\}$ → $\omega/\omega_C=\{0,\ 3.3093,\ 3.3093,\ 3.3093\}$; banked $\sqrt3\arccos(-1/3)=3.3093$ ✓
- H: $\mu=\{-3,1,1,1\}$ ✓ (banked *"at the $H$ point … $\mu=-3,\ \lambda=6$"*)

**REPRODUCTION GATE: PASS on every scalar-channel number this datasheet consumes.**

### R3 — srs bipartiteness (the OBS-2 premise), verified not assumed

`build_srs_net(L=3)`: $N=216$, degree 3, `carrier == "srs-z3"`. Two-colouring succeeds, parts **108 / 108**. Adjacency spectrum $\mu_{\max}=+3.0000000000$, $\mu_{\min}=-3.0000000000$ (bipartite $\iff \mu_{\min}=-\mu_{\max}$ for a connected regular graph). Graph-Laplacian $\lambda_{\max}=6.0000000000$, matching the banked gate (ii) *"$\lambda_{\max}=6.000000$ vs direct `build_srs_net`"*.

### R4 — the wiring-theorem contrast (OBS-3 / input 2)

Honeycomb net (3-regular, bipartite, identical lossless lines), same arccos TL map, 400² scan: 2 bands, envelopes $[0,\ 2.7155]$ and $[2.7259,\ 5.4414]\,\omega_C$; **global top 5.4414 $\omega_C$ — identical to srs**; Dirac touching (analytic) at $\sqrt3\arccos(0)=2.7207\,\omega_C$. Band count and interior edges differ from srs entirely. See §5.3.

### R5 — TLM one-step operator spectra (F5, F6, `SCX-REQ-ANCHOR.5`)

$M=\mathrm{Connect}\cdot\mathrm{blockdiag}(S)$ built directly and diagonalised; orthogonality $\|M^TM-I\|\le1.8\times10^{-15}$ in every case.

| network | $N$ / $B$ / ports | eigenphases $\theta$ (multiplicity) |
|---|---|---|
| $K_4$ complete graph | 4 / 6 / 12 | 0 (×4); 1.910633 (×6); π (×2) |
| srs supercell $L=2$ | 64 / 96 / 192 | 0 (×34); 12 interior values matching the arccos map with doubled multiplicity; π (×34) |
| P1-C (vertex + 3 open stubs) | 4 / 3 / 6 | 0 (×1); π/2 (×4); π (×1) |
| P1-B (one bond, open–open) | 2 / 1 / 2 | 0 (×1); π (×1) |

The $L=2$ interior values reproduce the arccos map exactly (0.635563, 0.729728, 0.955317, 1.230959, 1.432283, 1.709310, 1.910633, 2.186276, 2.411865, 2.506030 — each at exactly twice the adjacency multiplicity), which is the direct verification that **substitute (A) samples the bands**.

> **Method note (`ave-driver-script-honesty`).** The 1-port open termination used in the P1-B/P1-C rows is **not** the engine's `scatter_matrix` (which raises for $n<2$, `SCX-REQ-ANCHOR.4`); it is the same closed form evaluated at $n=1$, $S=[+1]$, supplied locally in the scratch script. The engine was not modified. This is disclosed because it means those two rows are a check of the *formula*, not of an engine code path that exists.

---

## §8 — Open questions and routed flags

### §8.1 — ★ ONE PLUMBER-PHYSICAL QUESTION FOR GRANT (`pre-test-physics-check`, asked BEFORE the prereg freezes)

> **Q1 — Does a vacuum bond ring at its FULL-wave, or is the half-wave the top by construction?**
>
> A single srs bond, exported as a lossless line of impedance $Z_0$ and one-way delay TD with both ends open, is a resonator. Continuous transmission-line theory says it rings at $\omega=n\pi/\mathrm{TD}$ for $n=1,2,3,\dots$ — half-wave, full-wave, three-halves-wave, forever. The engine's TLM, being a discrete-time scatter+connect at exactly one bond per step, **structurally cannot carry $n\ge2$**: its whole representable band stops at $\theta=\pi$, which is the $n=1$ half-wave (verified §7 R5 — the one-bond TLM operator's only nonzero eigenphase is $\theta=\pi$).
>
> So when SPICE reports a resonance at $2\pi\sqrt3\,\omega_C$ on a single bond, is that
>
> - **(a) real substrate physics the discrete engine is blind to** — the bond genuinely supports a full-wave standing pattern, and the TLM's band top is an instrument ceiling that happens to coincide with the physical Bragg resonance; or
> - **(b) an artefact of over-resolving a line that has no interior** — the bond has no sub-$\ell_{node}$ structure to hold a full-wave pattern in, so the half-wave IS the top by construction and everything above it is the continuum model inventing degrees of freedom the lattice does not have?
>
> **Why it must be answered before the prereg freezes:** F1 currently caps every comparison at $\pi\,\omega_{link}$ on instrument grounds. If (a), that cap is hiding a real prediction and the epic should say so. If (b), the cap is physics and should be stated as physics. The corpus is not silent but it does not settle this: `srs-band-structure.md:69-76` says $\pi\cdot\omega_{link}$ is a *"first Bragg / half-wave-line resonance, physical, **not** a temporal-Nyquist artifact"* — which asserts the top is real without saying whether anything lives above it. **Not resolved by this lane.**

### §8.2 — routed flags (surfaced, not fixed)

| # | flag | route |
|---|---|---|
| **FL-1** | **`bond_lc()` vs `ANALYTIC_NETWORK_FACTOR` encode different bond delays** ($1/\omega_C$ vs $1/(\sqrt3\,\omega_C)$), and acceptance test T0.2 asserts the R1 form as a Class-A identity while the band survey uses the R2 form. No in-tree result is known to be wrong (§3.2 scope), but the symbol *named* `bond_lc` is the one an exporter author will reach for. | auditor lane — is `bond_lc` the emergent-medium constitutive pair mis-named per-bond, or is the R1/R2 fork genuinely open at bond level? |
| **FL-2** | Two stale line-cites inside `srs-band-structure.md`: `:145`→`constants.py:294` (real site `:305`) and `:117`→`constants.py:770` (real site `:781`). Pure line-drift; content correct at both real sites. | auditor lane (cite-repair sweep) |
| **FL-3** | `scatter_matrix` raises for $n<2$, so the engine cannot build a 1-port-terminated network; the closed form extends cleanly to $S=[+1]$. Blocks the epic's three-way anchor for P1-B/P1-C unless relaxed. | Phase-1 GO decision (engine touch vs two-way comparison); recorded in the trade study |
| **FL-4** | *"K4"* now names **three** distinct objects in reach of this epic: the Sunada-K4/srs net (Axiom 1), the engine's z=4 diamond instrument, and the $K_4$ complete graph that is literally the srs primitive cell's Γ adjacency. | vocabulary lane (`def-` register); this doc writes *"$K_4$ complete graph"* in full wherever it means the third |

### §8.3 — what Phase 0 does NOT decide

Every T1–T6 decision (solver, bond representation, graph source, observable extraction, results home, units/scaling) is **OPEN** in the sibling trade study. This datasheet constrains them; it selects none of them. **T2 (bond representation) is Grant's call and is the gate on Phase-1 GO** (epic §4 Phase-0 GATE: *"Grant ratifies the trade-study decisions marked his"*).

---

## Skill-selection retro-pass (applied set, per the epic §7 plan)

| skill | fired | where |
|---|---|---|
| `substrate-native-check` | ✅ | §0.5 walk, done before any requirement was written (trigger 6: prose pre-planning of a numerical method) |
| `ave-canonical-source` | ✅ | §2 — every value an import-path citation; §7 R1 receipts |
| `consistency-vs-emergence` | ✅ | §0 — IMPLEMENTATION-VERIFICATION register declared and re-declared |
| `verify-before-cite` | ✅ | every KB/code cite re-verified this branch; FL-2 is its output |
| `ave-reproduction-gate` | ✅ | §7 — banked scalar numbers re-derived at HEAD before being consumed |
| `phase-space-coordinate-check` | ✅ | §0.5 CP4 + F2 — frequency/reciprocal-space coordinates matched to the corpus claim; $\omega$-vs-$k$ discipline carried |
| `pre-test-physics-check` | ✅ | §8.1 Q1, asked before the prereg skeleton freezes |
| `ave-driver-script-honesty` | ✅ | §7 method note (the local $n=1$ scatter is disclosed as not-an-engine-path) |
| `ave-regime-phase-state-check` | ✅ | §0 sector declaration |
| stop-and-ask | ✅ | Q1 surfaced rather than resolved; FL-1/FL-3 routed rather than fixed |

**Drift from the epic's planned set:** none removed; `ave-regime-phase-state-check` added (sector header discipline).

