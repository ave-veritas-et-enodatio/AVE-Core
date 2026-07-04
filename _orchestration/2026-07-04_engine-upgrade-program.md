# Engine-upgrade program — tracker (2026-07-04)

> **Class:** INFRASTRUCTURE / ENGINE-HARDENING. No physics chord/echo/emergence
> claim is minted by this program. `mass = A1` (PR#260 / #311 ECHO-final) is
> untouched by everything here. The program hardens the *instruments* so that a
> future physics verdict cannot be an operator-bug artifact.

> **✅ PROGRAM COMPLETE (2026-07-04).** All five items delivered: items 1/2/5 LANDED
> via PR #512 (DEC canonicalization + operator-registry CI, validation-harness library,
> carrier-declaration guard); item 4 LANDED via PR #513 (the ngspice-46 validate-on-known
> ladder, **5/5 PASS**); item 3 (Lorentz-on-srs, the P1 make-or-break) DELIVERED via
> PR #515 — the migration's **P1 Lorentz acceptance gate CLEARS** `[ISOTROPY-EMERGES]` on
> srs-z3 (first full consumer of items 1/2/5). Completion rows mirrored to the capability
> map §8b.6. **Honesty note:** PR #515 is open (REVIEW: pending-orchestrator, no self-merge);
> the item-3 row reads DELIVERED-pending-merge, flips to LANDED on merge. The α-chain P1 leg
> is a SEPARATE gate (not this program). The two SPICE-lane varactor ADJUDICATION-PENDING
> questions stay OPEN (Grant-gated).

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
| **1** | **DEC canonicalization** — inventory every discrete div/curl/grad; route live consumers through the exact DEC set (`srs_dec.py` ∂₁/∂₂; weighted `BᵀDB`) or scope-tag the heuristic with a DEC pointer (KEEP-BOTH for frozen provenance); CI adjoint-consistency + ∂∂=0 check over the registered operator sets. | `srs_dec.py` (built) | **THIS ARC — ✅ LANDED** | see §1-log |
| **2** | **Validation-harness library** — extract the proven gate machinery into `src/ave/validation/`: planted-source positive-control, structural-degeneracy checks, runtime-independence assert, hardened equation-audit, spectral-liveness re-export. Retrofit one driver as the demo consumer. | 1 (operator sets registered) | **THIS ARC — ✅ LANDED** | see §2-log |
| **5** | **Carrier-declaration guard** — every lattice-constructing entry point declares its carrier (`srs-z3` / `diamond-z4-instrument` / `cartesian-reference` / `k-space`); diamond-stencil consumers REQUIRE an explicit `instrument_scope=` acknowledgment or raise. Additive + backward-compatible. | independent (uses 5's own enum) | **THIS ARC — ✅ LANDED** | see §5-log |
| **4** | **SPICE phase-1 ladder** — ngspice-backed circuit-domain ladder (now installed). | independent | **PARALLEL ARC** (`analysis/spice-phase1`) — **✅ LANDED (PR #513, 5/5 PASS)** | see §8b.6 / `spice-phase1-ladder_result.md` |
| **3** | **Lorentz-on-srs** — the P1 make-or-break: photon isotropy / emergent-Lorentz chain on the srs carrier (uses `micropolar_bloch` + the canonical operators + the declared carrier). | 1 (canonical operators) + 5 (declared carrier) + `micropolar_bloch` | **✅ DELIVERED (PR #515 — P1 gate CLEARS `[ISOTROPY-EMERGES]`)** | open, REVIEW: pending-orchestrator; flips LANDED on merge; §8b.6 |

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

### §1-log — DEC canonicalization  [LANDED 2026-07-04]

**Inventory of discrete div/curl/grad across `src/ave/` (grep census + read).**
Every operator set a LIVE `src/ave/` solver drives a verdict on is now REGISTERED
in `src/ave/topological/operator_registry.py::OPERATOR_SETS` with its carrier +
adjoint spec, and CERTIFIED by the parameterized CI check
`src/tests/test_operator_adjoint_consistency.py`.

**Routed / certified (4 sets, all adjoint-consistent + ∂∂=0 where applicable):**

| Set | Carrier | div=s·gradᵀ | Exactness | Frozen | adj residual |
|:--|:--|:--:|:--|:--:|:--|
| `srs_dec` (∂₁/∂₂) | srs-z3 | s=−1 | exact_integer | no | 0.0 (∂∂=0 exact-int) |
| `srs_incidence` (B) | srs-z3 | s=+1 | exact_integer | no | 0.0 |
| `diamond_native_cage` | diamond-z4 | s=+1 | machine | **yes** | 0.0 |
| `gw_native` | diamond-z4 | s=+1 | machine | **yes** | 0.0 |

**FLAG (flag-don't-fix) — sign-convention split, reconciled not forced.** The
srs-z3 DEC set ships the NEGATIVE-adjoint convention (`div = −∂₁`, so `L0 = −PSD`);
the solver incidence + both diamond native sets ship the POSITIVE-adjoint
convention (`div = +gradᵀ`, so the Laplacian is `+PSD`). Both are valid — the
physics invariant is `div∘grad` SYMMETRIC. The registry records `adjoint_sign`
per set rather than forcing one convention onto frozen provenance. Empirical catch
(Rule 10): the first draft assumed `Div = −Gradᵀ` for the diamond sets; running
the check gave residual 0.5, and the direct probe showed `Div = +Gradᵀ` EXACTLY
(`Div−Gradᵀ` max=0.0) — the load-bearing `L_D = GradᵀDGrad` +PSD invariant. Fixed
the registry, not the frozen operator.

**Scope-tagged heuristics (2, NOT registered — non-adjoint, must not drive a
verdict; DEC-alternative pointer recorded in `SCOPE_TAGGED_HEURISTICS`):**
- `_srs_curl_nodes` / `_srs_node_divergence` — non-adjoint (`div∘curl` RMS ≈ 0.35);
  live in `src/scripts/vol_2_subatomic/em_readout_vsector_transducer.py` (a driver
  OUTSIDE `src/ave/`, retired instrument per capability-map §8b.3). Already flagged
  ENGINEERING-CHOICE + non-adjoint in that driver's own `equation_audit` ledger
  (:694-697). NOT touched (collision-guard: that driver also carries
  `ngspice_cross_solve`, in the sibling SPICE arc's zone). DEC alternative =
  `ave.topological.srs_dec`.
- `universal_topological_curl` / `universal_topological_divergence` (Op11/Op12,
  `universal_operators.py:673,711`) — Yee-staggered FDTD; E-curl and H-curl live
  on different staggered meshes, so NOT a mutual negative-adjoint pair BY FDTD
  DESIGN (not a bug). Cartesian-reference carrier; not a verdict-driving substrate
  operator. Recorded for inventory completeness.

**Provenance-frozen driver byte-identity.** ITEM 1 added only two NEW files
(`operator_registry.py`, `test_operator_adjoint_consistency.py`); it changed NO
existing operator code, so every merged-result driver is bit-identical by
construction. Cross-check: `native_cage_imex` `L_D` (N=6, graded D) sha256
`30986dc1538bf4c5c9ddbcd82f6c957e…` recomputed at HEAD; the DEC↔solver Laplacian
reconciliation (`L_srs = BᵀB = −L0`) asserted exactly in the CI check.

**CI check:** 15 passed / 3 skipped (the 3 skips are the no-∂₂ 1-complex sets,
correctly declared `dd_zero=False`).

### §2-log — validation-harness library  [LANDED 2026-07-04]

Extracted the proven gate machinery into `src/ave/validation/` (6 modules:
`__init__` + 5 guards), each carrying its live-fire provenance in its module
docstring and a positive+negative test:

| Guard | Module | Retires | Live-fire source |
|:--|:--|:--|:--|
| (a) planted-source positive control | `planted_source.py` | the blind null read | srs localization positive-control eigenmode; em_readout point-δ VoK |
| (b) structural-degeneracy | `structural_degeneracy.py` | the Stage-1 global-sum blind readout | closed-graph `Σ(∇·E)=0` topology-forced; em_readout jellium ledger |
| (c) runtime-independence | `runtime_independence.py` | smuggled-dependency (α-into-RHS) | em_readout `Q_link`-stub bit-identity (#4d, reconcile-grade) |
| (d) hardened equation-audit | `equation_audit.py` | smuggled forbidden constant | #482-era em_readout `equation_audit` (import-closure + allowlist + strip) |
| (e) spectral-liveness | `spectral_liveness.py` (re-export) | energy-gate-mistaken-for-liveness | `ave.solvers.spectral_liveness` (Step-3.8a) — RE-EXPORTED, not duplicated |

**RETROFIT DEMO — the five-line adoption** on the Stage-2 micropolar Bloch
pipeline (`ave.core.micropolar_bloch.micropolar_phi`, the newest/cleanest
micropolar computation; the `srs_chiral_micropolar` driver builds on it).
`src/tests/test_validation_retrofit_micropolar.py` wires all five guards onto the
real 48×48 Φ(k) and gives the copy-paste `test_micropolar_five_line_adoption`
template. NB: the Stage-2 driver script itself lives in `src/scripts/` and carries
a SPICE-adjacent cross-check → NOT edited in-place (collision-guard + domain); the
retrofit is demonstrated as an in-domain test consumer.

**Two Rule-10 empirical findings baked into the demo (running the driver caught
both):**
1. With `kappa_rot>0` the micropolar Φ0 has a **3-dim** rigid nullspace (the 3
   uniform translations), NOT 6 — the micro-rotations are GAPPED. The naive
   "6 rigid modes" assumption is wrong when rotational stiffness is on.
2. The global-sum degeneracy detector's flat-`1` weight is **scalar-operator-only**.
   For a block/multi-DOF operator the forcing weight is the STRUCTURED
   translation-null vector (`v[axis::6]=1`). Generalized `detect_global_sum_
   degeneracy` to take a `weight=` argument; the flat-`1` default is documented as
   correct only when `1` really is L's constant. The detector correctly returns
   safe-to-use for the WRONG (flat) weight on Φ0 — proving it is not a rubber-stamp.

**Also caught (equation-audit generalization):** the α-leak GUARD assertions the
DEC modules ship (`assert "ALPHA" not in globals()`) self-fired the naive scan; the
extracted audit strips `assert "…" not in globals()` in every file so a defensive
guard is not read as a use (grep-completeness trap). srs_dec now audits
`driver_clean=True` while its transitive `ALPHA@constants.py` closure leak is
honestly reported (scope-honesty preserved from the em_readout original).

**Tests:** 20 collected (14 harness keepers + 6 retrofit), all green; flake8-clean;
each guard has a positive AND a negative test (a guard that only ever passes is a
checklist, not a gate).

### §5-log — carrier-declaration guard  [LANDED 2026-07-04]

**Carrier vocabulary** (`src/ave/core/carrier.py`): `Carrier` enum with the
D1-ratified values `srs-z3` | `diamond-z4-instrument` | `cartesian-reference` |
`k-space`; `DIAMOND_Z4.is_instrument = True`. `require_instrument_scope()` is the
guard; `coerce_carrier()` rejects an unknown carrier.

**Lattice-constructing entry points declare their carrier** (additive, defaulted).
`LatticeNet` gains a `carrier: str = "unknown"` field (backward-compatible — a net
built without a declaration reports `"unknown"`). `build_srs_net` → `"srs-z3"`;
`build_diamond_net` → `"diamond-z4-instrument"` (threaded through
`_build_net_from_points` via a new defaulted `carrier=` param).

**Diamond-stencil consumers require an `instrument_scope=` acknowledgment.** The two
diamond-stencil builders (`native_cage_imex.build_grad_div_periodic`,
`gw_propagation._build_native_grad_div`) gain a keyword-only `instrument_scope`. The
guard behavior:
- **non-instrument carrier** (srs / cartesian) → no acknowledgment needed.
- **diamond + no ack, NEW construction** → **RAISES** `ValueError` (the target).
- **diamond + no ack, frozen-provenance driver** → **DeprecationWarning** (KEEP-BOTH;
  does not break the merged byte-identical output). Both diamond builders are frozen
  (Stage-2 DISPERSE / #86 back-reaction), so they warn rather than raise on a naked
  legacy call.
- **diamond + ack** → clean.

The 6 internal frozen callers (`native_cage_imex` ×2, `coupled_cage_winding`,
`gw_propagation`, `backreaction` ×2) now pass an explicit `instrument_scope=`
naming their provenance, so the normal engine paths are warning-free and
self-documenting; only a NAKED legacy `build_grad_div_periodic(N)` call (e.g. an
old test) trips the deprecation nudge — the intended behavior.

**Byte-identity preserved** (the guard is a gate, not a computation change):
`native_cage L_D` (N=6, graded D) sha256 `30986dc1538bf4c5c9ddbcd82f6c957e`,
IDENTICAL to the ITEM-1 baseline; `gw Div = +Gradᵀ` still exact. Verified by
recompute at HEAD.

**Test:** `src/tests/test_carrier_declaration.py`, 12 keepers — constructing a
diamond-carrier operator without the acknowledgment RAISES (new-construction path);
the frozen path WARNS; srs is clean; the builders' carrier fields are correct; the
frozen builder still runs byte-identical WITH the guard active. Regression: the
affected consumer suites (native-cage / stage-3 back-reaction / chiral-lattice)
stay green (57 pass; the only warnings are pre-existing test files that call the
diamond builder nakedly — the guard nudging them, not a failure).
