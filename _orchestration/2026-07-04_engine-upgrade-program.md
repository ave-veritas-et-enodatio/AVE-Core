# Engine-upgrade program — tracker (2026-07-04)

> **Class:** INFRASTRUCTURE / ENGINE-HARDENING. No physics chord/echo/emergence
> claim is minted by this program. `mass = A1` (PR#260 / #311 ECHO-final) is
> untouched by everything here. The program hardens the *instruments* so that a
> future physics verdict cannot be an operator-bug artifact.

## Why this program exists — the operator-failure provenance it eliminates

The week's engine-verdict-exposure sweep and the EM-readout Stage-1/1b/2a
reviews surfaced a **class** of failure: a merged or in-flight verdict that
rested on an operator whose behavior was never certified against a
substrate-native reference. Three concrete instances (the class this program
retires), each verified at HEAD against
[`manuscript/ave-kb/common/engine-capability-map.md`](../manuscript/ave-kb/common/engine-capability-map.md)
§8b.3:

- **The blind Stage-1 readout** — a merged null read on a *structurally-
  degenerate global-sum observable* with no same-pipeline positive control. On a
  closed graph the global Σ(∇·E) is forced to zero by topology (the constant is
  L's nullspace), so a "zero" verdict was pre-ordained by the observable's
  structure, not by physics. This catch triggered the whole verdict-exposure
  sweep (capability-map §8b.3, CLASS-2 blind-readout pathology).
- **The Stage-1b non-adjoint operator pair** — `_srs_curl_nodes` (1/deg-weighted
  per-node 3-vector) + `_srs_node_divergence` (½ face-average), in
  `src/scripts/vol_2_subatomic/em_readout_vsector_transducer.py`. These are two
  independent Cartesian-embedded heuristics that do NOT compose to zero:
  `div∘curl` on a random field is pointwise O(1) (RMS ≈ 0.35, max ≈ 1.4). The
  merged curl-class closure was consequently scoped as an *operator-pair
  property*, not a class theorem. (Verbatim provenance:
  [`src/ave/topological/srs_dec.py`](../src/ave/topological/srs_dec.py):11-24.)
- **The Stage-2a nonlinear-static anchor** — `em_readout_stage2_nonlinear_op.py`,
  RETIRED: its only readable signal is the anchor-source `κτ` (not physics), and
  a source-free version returns `φ ≡ const` by theorem. It could not answer the
  winding-emergence question (capability-map §8b.3).

The common failure is **an uncertified operator or observable driving a
verdict.** The DEC theorem (`srs_dec.py`) fixed the curl-class instance. This
program generalizes the fix into standing infrastructure so the *next* uncertified
operator is caught at construction / test time, not at post-merge review.

Routing companion: the carrier axis + module migration ladder is the
capability-map §8b.1 table + [`2026-07-03_srs-migration-policy.md`](2026-07-03_srs-migration-policy.md).

## The five items — order + status

Order is dependency-forced: canonicalize the operators (1) before generalizing
the gate machinery that certifies them (2); declare the carrier every solver
speaks (5) before the Lorentz transport (3) that must run on a declared carrier;
the SPICE ladder (4) is carrier-independent and runs in parallel; Lorentz-on-srs
(3) is queued behind this arc because it needs the canonical operators AND
`micropolar_bloch` (which exists, `src/ave/core/micropolar_bloch.py`).

| # | Item | Depends on | Arc | Status |
|:-:|:--|:--|:--|:--|
| **1** | **DEC canonicalization** — inventory every discrete div/curl/grad; route live consumers through the exact DEC set (`srs_dec.py` ∂₁/∂₂; weighted `BᵀDB`) or scope-tag the heuristic with a DEC pointer (KEEP-BOTH for frozen provenance); CI adjoint-consistency + ∂∂=0 check over the registered operator sets. | `srs_dec.py` (built) | **THIS ARC** | see §1-log |
| **2** | **Validation-harness library** — extract the proven gate machinery into `src/ave/validation/`: planted-source positive-control, structural-degeneracy checks, runtime-independence assert, hardened equation-audit, spectral-liveness re-export. Retrofit one driver as the demo consumer. | 1 (operator sets registered) | **THIS ARC** | see §2-log |
| **5** | **Carrier-declaration guard** — every lattice-constructing entry point declares its carrier (`srs-z3` / `diamond-z4-instrument` / `cartesian-reference` / `k-space`); diamond-stencil consumers REQUIRE an explicit `instrument_scope=` acknowledgment or raise. Additive + backward-compatible. | independent (uses 5's own enum) | **THIS ARC** | see §5-log |
| **4** | **SPICE phase-1 ladder** — ngspice-backed circuit-domain ladder (now installed). | independent | **PARALLEL ARC** (`analysis/spice-phase1`) | not in this arc |
| **3** | **Lorentz-on-srs** — boost/transport operator on the srs carrier. | 1 (canonical operators) + 5 (declared carrier) + `micropolar_bloch` | **QUEUED behind this arc** | reopens after this arc merges |

## NOT-NOW items (recorded with reopen-conditions)

- **u-sector stepper** (full 6-DOF micropolar time-domain: 3 translation +
  3 micro-rotation as independent dynamical fields). NOT-NOW: the current
  engines carry the winding as a static `Link` riding the cage, and the DOF
  coverage the electron needs is topological/boundary, not 6-DOF bulk dynamics
  (capability-map §1 localizer relabel). **Reopen condition:** a physics target
  that genuinely requires 6-DOF dynamics — e.g. a driven-regime micro-rotation
  response that cannot be read off the band structure (`micropolar_bloch`) or the
  static coupling.
- **JAX-ification** (port the srs / DEC operators + solvers to JAX for autodiff /
  GPU). NOT-NOW: the gating-lane operators are sparse-scipy and sub-second; JAX
  buys nothing for a certification harness and adds a dependency surface.
  **Reopen condition:** a driven-regime campaign (many-body / long-time / swept
  many-seed) where the wall-clock or gradient-through-solver actually gates the
  science.

## Item logs

### §1-log — DEC canonicalization
(populated by the arc)

### §2-log — validation-harness library
(populated by the arc)

### §5-log — carrier-declaration guard
(populated by the arc)
