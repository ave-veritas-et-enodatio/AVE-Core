# PRE-REG (FROZEN) — L0: α-clean host de-risk (the winding host) — HARD-STOP gate

**Date frozen:** 2026-06-24 · **Lane:** engine re-route (implementer) · **Stage:** L0 (the first stage; a HARD-STOP).
**Pathway:** [`../_orchestration/2026-06-24_engine-reroute-pathway.md`](../_orchestration/2026-06-24_engine-reroute-pathway.md) (Stage L0).
**Base:** `origin/main` @ `31d0ac43` (PRs #403→#404 merged).
**Status at freeze:** PRE-RUN. Predictions below are committed BEFORE the acceptance suite is executed.

---

## 0. Goal (one line)

Establish that the **winding-host's CHORD PATH is α-clean** — i.e. that the (2,3) winding DOF can be hosted WITHOUT the α-carrier (ALPHA / κ_chiral=α·κ̃ / the baked-137 golden-torus Q) being reachable on the verdict-determining path. If it cannot → **HARD-STOP**.

## 1. Why this gate exists (the central guard)

The re-route chord program (S1–S4) decides chord-vs-echo at S4 via a dimensionless ratio the substrate fixes. That verdict is only meaningful if the host carrying the winding DOF is α-FREE. The re-route audit found the natural winding host, `src/ave/topological/cosserat_field_3d.py`, **α-contaminated on the readout path**. L0 either de-risks that contamination off the chord path or HARD-STOPs.

This mirrors the **original Gate 0** (PR #394 HARD-STOP), which targeted `CosseratField3D` and correctly stopped because the host was α-contaminated; Stage 0 was then re-scoped onto the cold CrystalEngine spine, **never importing the cosserat host** (`test_stage0_alpha_clean_spine.py:10-15`). The re-route NEEDS the winding, which lives in the cosserat host — so L0 must do for the WINDING DOF what Stage 0 did for the bulk spine: import ONLY the α-free symbols, carry the guard triad.

## 2. The contamination (VERIFIED 2026-06-24, 2-pattern grep + live numeric)

| Site | Content | Disposition |
|---|---|---|
| `cosserat_field_3d.py:56` | `from ave.core.constants import ALPHA, V_SNAP` | ALPHA must NOT be reachable on the chord path |
| `cosserat_field_3d.py:115` | `def kappa_chiral_from_topology(p, q, alpha: float = ALPHA)` | default-arg ALPHA — must NOT be invoked on the chord path |
| `cosserat_field_3d.py:131` | `KAPPA_CHIRAL_ELECTRON = ALPHA * KAPPA_TILDE_ELECTRON` (≈8.757e-3) | chord path uses the α-FREE κ̃=6/5 (`:94`), NOT α·κ̃ |
| `cosserat_field_3d.py:2422` | `extract_quality_factor` returns `16π³(R·r)+4π²(R·r)+π·d` | EXCLUDED from the chord path; **= 137.036304 at R·r=¼** (verified), in the 117–157 band, matches 1/α=137.035999 — a closed-form α⁻¹, NOT a measured ring-down (the baked-137 echo) |

Live-numeric confirmations (2026-06-24): golden-torus Q(R·r=¼)=**137.036304**; KAPPA_CHIRAL/KAPPA_TILDE = α = 7.297353e-3; KAPPA_TILDE_ELECTRON = 1.2 = 6/5.

## 3. The de-risk DESIGN (committed before build)

**Approach: stand up an α-stripped winding host** (NOT strip the shared `cosserat_field_3d.py` in place — its α-baked symbols are legitimately used by α-aware callers; in-place stripping would break them). The α-stripped host **selectively imports ONLY the α-free cosserat symbols**:
- `KAPPA_TILDE_ELECTRON` (=6/5, `:94`) — the α-FREE winding factor
- the native K4 stencil functions `tetrahedral_gradient`, `adjoint_tetrahedral_divergence`, `TETRA_OFFSETS`

and NEVER imports `ALPHA`, `KAPPA_CHIRAL_ELECTRON`, `kappa_chiral_from_topology`, `extract_quality_factor`, `Q_TANK`, `ELECTRON`, `RHO_BULK`, `V_SNAP`, `ALPHA_COLD_INV`.

VERIFIED (2026-06-24) that `from cosserat_field_3d import KAPPA_TILDE_ELECTRON, TETRA_OFFSETS, tetrahedral_gradient, adjoint_tetrahedral_divergence` leaks NONE of the forbidden symbols into the importer's globals (Python `from X import name` binds only `name`). This is the same selective-import precedent `graded_vacuum_network.py:100-114` already relies on.

**PORTED guard pattern:** the import-guard triad mirrors `graded_vacuum_network.py:108-114` (the proven-LIVE precedent) — `assert <sym> not in globals()` at module body for each forbidden symbol; a deliberately-injected ALPHA must TRIP it.

## 4. PRE-REGISTERED PREDICTIONS (committed pre-run)

- **L0.1** — the import-guard fires LIVE: importing the α-stripped winding host runs the load-time triad clean; injecting ALPHA into a host dependency's namespace and re-asserting TRIPS an `AssertionError`. **Predict: PASS** (the guard is live, not vacuous).
- **L0.2** — the winding-DOF chord path is α-FREE: it carries κ̃=6/5 (`KAPPA_TILDE_ELECTRON`), invokes NO α·κ̃ (`KAPPA_CHIRAL_ELECTRON` / `kappa_chiral_from_topology`), and reaches NO 137-echo Q-form (`extract_quality_factor` is NOT on the path). **Predict: PASS.**
- **L0.3** — the LITERAL SCRUBBER + LANDING-ZONE: no `'137'` / `'0.00729'` literal in the chord-path verdict-determining code; any α-relevant numeric the host computes on the chord path does NOT land in the 117–157 band. **Predict: PASS.**

## 5. ACCEPTANCE (the HARD-STOP gate — adjudication criteria, frozen)

PASS (all three required):
1. the import-guard fires live (inject ALPHA → assert trips);
2. the winding-DOF chord path is α-free (κ̃=6/5; no 137-echo Q-form; no ALPHA);
3. the literal scrubber is clean (no '137' / '0.00729' on the chord path) AND the 117–157 landing-zone exclusion holds.

**HARD-STOP** = ANY of: a live-injected ALPHA that does NOT trip the guard (vacuous guard); the chord path reaching α·κ̃ or `extract_quality_factor` or ALPHA; a '137'/'0.00729' literal on the chord path; a chord-path numeric landing in 117–157. **If the host CANNOT be made α-clean → HARD-STOP, report (do not paper over).** Per Rule 11 (honest closure): a HARD-STOP is the discipline working, not a failure to debug around.

## 6. Classification (consistency-vs-emergence)

L0 is **Class A — identity / foundation** (the import-guard asserts ARE the immune system; structural, not predictive) + the **anti-emergence / anti-substitution stance**: the Q=137 slot stays EMPTY (gate `wmighcz1z`). There is **NO Class D (emergence) claim** anywhere in L0 and **NO chord** — L0 only establishes that the host on which the (later) chord will be decided is α-clean. NO α-readout, no Q-derivation, no value-claim.

## 7. Substrate-native walk (pre-build, the relevant checkpoints)

- L0 is NOT a solver/integrator/eigsolve and plants NO finished composite — it is a host de-risk (import-guard + scrubber). Checkpoints 1–9 are largely N/A (no dynamics evolved).
- **Substrate structure preserved:** the winding lives on the **K4 diamond** as the Cosserat (2,3) grade (phase-space Clifford torus); the α-free factor is κ̃=6/5, NOT α·κ̃. The native stencil functions (tetrahedral gradient / adjoint divergence / TETRA_OFFSETS) are the K4 operators — NO Cartesian 7-pt Laplacian is imported.
- **Coordinate-category caveat (load-bearing):** spin-½ (real-space 720° SU(2) on the unknot body) ≠ the (2,3) winding (phase-space Clifford torus) — two different "2"s; do NOT conflate (the (2)×(2)=4 double-count). L0 hosts the (2,3) phase-space winding factor κ̃ only; it does NOT touch the real-space SU(2) spin DOF.
