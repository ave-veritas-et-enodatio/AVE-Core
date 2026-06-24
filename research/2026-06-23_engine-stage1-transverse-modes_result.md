# STAGE 1 RESULT — EM-transverse + transverse shear on the chiral srs grid

**Created:** 2026-06-23 · implementer lane · branch `analysis/engine-stage1-transverse-modes`
**Prereg:** [`2026-06-23_engine-stage1-transverse-modes_prereg.md`](2026-06-23_engine-stage1-transverse-modes_prereg.md) (FROZEN pre-run)
**Epic:** [`_orchestration/2026-06-23_full-engine-pathway.md`](../_orchestration/2026-06-23_full-engine-pathway.md) Stage 1
**Stacks on:** Stage 0 (`analysis/engine-stage0-alpha-clean-spine`, PR #399 — NOT yet on main; rebases onto main once #399 merges)
**Code:** `_transverse.py` (wave-typed constitutive helpers + α-guard); `test_stage1_transverse_modes.py` (4 gates)

---

## VERDICT: **PASS** — the 2 transverse modes are wave-typed; the split is wired correctly.

All four Stage-1 frozen-bin gates pass. The 2-DOF transverse field is lossless on
the spine (T1.6 re-confirmed); the EM-photon and transverse-shear modes split the
RIGHT way off S=1 (c_EM rises, c_shear falls); the three live indices are pinned
and the legacy alias is hard-scoped so Stage 4 cannot re-conflate c_EM/c_shear; the
α-guard triad is extended to the transverse/srs modules. **No α re-leak in the
Stage-1 path — no STOP triggered.**

| Gate | Outcome | Verdict |
|---|---|---|
| **T1.6** 2-DOF transverse lossless on the spine (cold, S=1) | drift 5.1e-14 (<1e-8); dispersion 0.0078 (<0.05); \|c\|/c_net 0.9931 (±5%); transverse_dof==2 | **PASS (re-confirm)** |
| **S1.1** the 2 modes SPLIT the RIGHT way off S=1 (driven smoke-check) | at A=0.6 (S=0.8): c_EM/c₀=1.250 (=1/S, RISES); c_shear/c₀=0.894 (=√S, FALLS); opposite-direction, monotonic | **PASS** |
| **S1.2** three indices pinned, alias hard-scoped (both engines) | n_EM_group·n_shear=1 (exact reciprocals); refractive_index() is n_em_index() (GROUP √S); n_EM_phase=S distinct from √S off S=1 | **PASS** |
| **S1.3** α-guard triad extends to transverse/srs | no α-carrier in _transverse/_em_media/chiral_lattice_vector; guard LIVE (injected leak trips); ETA_ROT_PER_WRITHE=1.0 tagged-not-bankable; _sat α-import NAMED out-of-scope | **PASS** |

---

## The report-questions (directive)

### Real engine paths found? (verify-before-cite — the pathway mis-cited TWO)

YES — and **two pathway-doc mis-cites corrected by grep before any code**:

- **`chiral_lattice_vector.py` DOES exist** at `src/ave/core/chiral_lattice_vector.py`
  (the pathway claimed it "does NOT exist"). It is the srs transverse vector-TLM
  engine (the FROZEN v9 medium). `fdtd_3d.py` confirmed at `src/ave/core/fdtd_3d.py`.
- **`ETA_ROT_PER_WRITHE=1.0`** lives at `src/ave/core/chiral_lattice_vector.py:27`
  (the optical-activity rate scale; the tagged engineering decree, NOT a bankable α).
- **`gravity_sign_freq_modulation.py` is NOT in `src/ave/core/`** — it is a VERIFY
  SCRIPT at `src/scripts/verify/gravity_sign_freq_modulation.py` (the pathway placed
  it in core). Its `:92,97` carry the PHASE-index convention n_EM_phase=S (c_EM=c₀/S).

### The 3 indices wave-typed + legacy alias killed/scoped?

YES — wave-typed and PINNED. The taxonomy (verified against `ave-kb/CLAUDE.md:79-80`,
clm-8nkvwy phase/group; `gravity_sign_freq_modulation.py:92-97`):

| Index | Form | Speed | Role | Engine anchor |
|---|---|---|---|---|
| **n_EM PHASE** | **S** | c_EM = c₀/S (RISES) | Maxwell phase velocity; the α-speed | `_em_media.em_params` (SYM); `gravity_sign_freq_modulation.py:92,97` |
| **n_EM GROUP** | **√S** | c_group = c₀·√S | optical/birefringence SIGNAL index | `master_equation_fdtd.n_em_index():169`; `crystal_engine:436` |
| **n_shear** | **1/√S** | c_shear = c₀·√S | Shapiro/gravitational (reciprocal of GROUP) | `master_equation_fdtd.n_shear_index():175`; `crystal_engine:441` |

**The legacy alias is HARD-SCOPED, not killed** (the honest resolution): the
`refractive_index()` METHOD on both engines was ALREADY a back-compat alias to
`n_em_index()` (the GROUP index √S), resolved in sign-lock w35sn2bq3 (2026-06-17) —
the pathway's "ambiguous, poisons later stages" claim was **stale**. Killing it
would break 30+ green callers (the v14 Mode-I / gamma-sign / L3 / apparatus-floor
diagnostics, all reading the "n→0 in core" sense). So Stage 1:

1. **PINS** all three index forms + the alias identity in a CI-gated regression gate
   (`S1.2`) — the gate FAILS if `refractive_index()` drifts off `n_em_index`, if
   n_EM_group·n_shear ≠ 1, or if phase==group off S=1. Stage 4 inherits this pin.
2. **HARD-SCOPES** the alias docstrings (`master_equation_fdtd.py:183`,
   `crystal_engine.py:447`) with a Stage-1 anchor naming the GROUP-index scope + the
   three-index taxonomy. The alias is now CI-pinned, documented, and gated.

The FREE FUNCTION `refractive_index(M, r)` (`gravity/__init__.py:41`,
`orbital_resonance.py:39`) is the unrelated Schwarzschild lensing form — DIFFERENT
signature `(M, r)`, NOT a conflation risk with the engine saturation index.

### T1.6 green on the spine?

YES. On the Stage-1 worktree spine: drift 5.089e-14 (<1e-8), dispersion spread
0.0078 (<0.05, linear), |c|/c_net 0.9931 (within 5%), transverse_dof==2. The
inherited gate (`test_l1_multiwave.py:154`) re-runs green; no regression.

### Do c_EM / c_shear split the right way off S=1?

YES — the substance. Sweeping A into the sub-yield regime (the driven smoke-check):

| A | S=√(1−A²) | c_EM/c₀ = 1/S (ε,μ; RISES) | c_shear/c₀ = √S (G; FALLS) |
|---|---|---|---|
| 0.00 | 1.0000 | 1.00000 | 1.00000 |
| 0.20 | 0.9798 | 1.02062 | 0.98985 |
| 0.40 | 0.9165 | 1.09109 | 0.95735 |
| 0.60 | 0.8000 | 1.25000 | 0.89443 |

At A=0 (S=1) the modes are DEGENERATE at c₀ (the foundation property). As A rises
(S falls below 1): **c_EM RISES strictly above c₀** (c_EM=c₀/S, the ε,μ PHASE
constitutive) while **c_shear FALLS strictly below c₀** (c_shear=c₀·√S, the G
identity) — **monotonic, opposite directions, diverging from the c₀ degeneracy.**
The wave-typing is wired: the two speeds read DIFFERENT moduli and are NOT equal off
S=1 (gate (d): the conflation would make them equal). **The 2 modes are genuinely
distinct and the wave-typing is correct.**

**SCOPE (regime-labelled per ave-regime-phase-state-check):** this is the SUB-YIELD
sanity check (A ≤ 0.6, below near-yield r₂=0.866), NOT the full near-yield √S-shear
validation (Stage 4). The driven c_EM split runs in the matching IMPEDANCE-PLANE
coordinates (the α-clean `_em_media.em_params` SYM varactor), NOT the 3D real-space
srs lattice (where a localized index step washes out, A46). The observable is a
SCALAR ⟨S⟩-deficit propagation-speed shift → achromatic-compatible, exists in every
regime (NOT the rate-asymmetry/∮≠0 near-yield trap). c_shear here is the
CONSTITUTIVE IDENTITY c₀·√S at the operating point — the desk-calc Stage 4's
saturated G-modulus DYNAMICAL engine must reproduce.

### Guards extended?

YES. The Stage-0 guard triad (no ALPHA / ALPHA_COLD_INV / Q_TANK / ELECTRON /
RHO_BULK reachable) is extended to the Stage-1 transverse code path:
`_transverse` (import-time + runtime), `_em_media`, `chiral_lattice_vector`. The
guard is LIVE (a deliberately-injected ALPHA into `chiral_lattice_vector` trips the
assert). STRUCTURAL chirality is ON (the lossless optical-activity rotation,
Axiom-3) but `ETA_ROT_PER_WRITHE=1.0` is the tagged engineering scale, NOT inherited
as a bankable α-dressed magnitude.

### PASS or STOP?

**PASS.** No α re-leak in the Stage-1 path; the modes split the right way; the
wave-typing is wired correctly.

---

## ⚑ HONEST FINDINGS (flag-don't-fix — surfaced, not silently resolved)

### Finding 1 — the pathway doc mis-cited two file paths (verify-before-cite)

The pathway `_orchestration/2026-06-23_full-engine-pathway.md` (and the build brief)
mis-cited: (a) `chiral_lattice_vector.py` as "does NOT exist" — it DOES, at
`src/ave/core/chiral_lattice_vector.py`; (b) `gravity_sign_freq_modulation.py` as
living "in `master_equation_fdtd.py` + gravity_sign_freq_modulation.py" in core — it
is a verify SCRIPT at `src/scripts/verify/`. Both corrected by grep before any code.
Surfaced for the orchestrator to correct the pathway doc (I did not edit the pathway
doc — it lands on main via a separate PR; the orchestrator owns it).

### Finding 2 — the "ambiguous legacy alias" was STALE; the alias was already resolved

The brief framed the legacy `refractive_index()` alias as ambiguous and
"poisons later stages." Verify-before-cite at build time: the alias was ALREADY
hard-scoped to `n_em_index()` (the GROUP index √S) in sign-lock w35sn2bq3
(2026-06-17), and `test_gamma_sign_gate.py:130` already asserts it. So the Stage-1
"fix" is NOT a code rewrite of already-correct functions — it is (a) a CI-gated
PIN of all three index forms + the alias identity (so Stage 4 cannot re-conflate),
and (b) a docstring hard-scope with a Stage-1 anchor. This is the honest scope; I did
not manufacture a fix for a non-bug. The load-bearing deliverable is the regression
PIN, which did not previously exist.

### Finding 3 — the saturated genesis engine `_sat` imports ALPHA (Stage-4-blocking)

`chiral_lattice_vector_sat.py:15` does `from ave.core.constants import ALPHA, R_I`.
This is the Phase-2 self-lock genesis engine, NOT the Stage-1 transverse wave-typing
substrate. The Stage-1 driven smoke-check routes through the α-CLEAN
`_em_media.em_params` (imports only EPSILON_0/MU_0/Z_0/C_0), so the Stage-1 path is
verified α-clean. But `_sat` is the natural host for the SATURATED c_shear DYNAMICS
that Stage 4 needs — and it carries an α-import. **Recorded as a NAMED Stage-4-
blocking contaminant** (`sat_engine_alpha_import_is_out_of_scope()`), NOT silently
rewritten (out of Stage-1 scope per the brief's grid-scope constraint). Stage 4 must
clean the `_sat` α-import (or build the saturated shear dynamics on an α-clean host)
before it can host the dynamical shear mode. Surfaced for the Stage-4 build.

---

## Classification (consistency-vs-emergence — Stage 1 is CONSISTENCY, NO chord)

- **T1.6** = **Class-C consistency** — lossless 2-DOF transverse propagation is a
  foundation property of the lossless vector-TLM (Axiom-3 reactive cycling).
- **S1.1** = **Class-C consistency** — the canonical wave-speed identities
  (c_EM=c₀/S, c_shear=c₀·√S) reproduced; the split is the DEFINITION of the two
  channels (which-modulus-responds), not an emergent prediction.
- **S1.2** = **Class-A identity** — the index forms are structural pins.
- **S1.3** = **Class-A identity / foundation** — the guard asserts ARE the immune system.

**No Class-D emergence / chord claim anywhere in Stage 1.** Correct — Stage 1 is a
foundation stage (the 2 transverse modes wave-typed), not a chord. The AVE-distinct
chord lives in the FORWARD predictions (Stage 7), not here.

---

## What Stage 1 delivers to the pathway

- The 2 transverse DOF WAVE-TYPED: the EM-photon (c_EM=c₀/S, ε,μ) and the
  transverse-shear (c_shear=c₀·√S, G) are separated by which modulus responds, and
  the split off S=1 is confirmed correct-direction (driven smoke-check).
- The THREE-INDEX PIN (`S1.2`): n_EM_phase=S, n_EM_group=√S, n_shear=1/√S, the alias
  hard-scoped to GROUP — a CI gate Stage 4 inherits so it cannot re-conflate c_EM
  and c_shear (the twice-conflated category error).
- The α-guard triad EXTENDED to the transverse/srs modules; the `_sat` α-import
  named as a Stage-4-blocking contaminant.
- The grid scope held: Stage 1 runs on the srs transverse grid (T1.6) + the matching
  impedance-plane (driven split), NOT co-located with the cage grid (that is Stage 3).

**Next stage (NOT this session):** Stage 2 — the c_eff(V) stiffening cage + self-trap
co-located on the chiral grid (the cheap wiring stages 1/2 are off the critical
path; Stage 3 the two-grid bridge is the first expensive item). Per the pathway doc.
The full near-yield √S-shear validation (the saturated G-modulus dynamics) is Stage 4
— which must FIRST clean the `_sat` α-import (Finding 3).

---

## Reproduce

```bash
cd <worktree>
PYTHONPATH=$PWD/src <repo>/.venv/bin/python -m pytest \
    src/tests/engine_acceptance/test_stage1_transverse_modes.py -v -s
# 4 passed: T1.6 (lossless 2-DOF), S1.1 (driven split right way), S1.2 (3-index pin),
#           S1.3 (guard extension)
```
