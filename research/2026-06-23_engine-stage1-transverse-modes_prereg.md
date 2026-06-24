# STAGE 1 PREREG — EM-transverse + transverse shear on the chiral srs grid

**Created:** 2026-06-23 · implementer lane · branch `analysis/engine-stage1-transverse-modes`
**Epic:** [`_orchestration/2026-06-23_full-engine-pathway.md`](../_orchestration/2026-06-23_full-engine-pathway.md) Stage 1
**Stacks on:** Stage 0 (`analysis/engine-stage0-alpha-clean-spine`, PR #399 — NOT yet on main).
This branch branches off the Stage-0 spine; the PR rebases onto main once #399 merges.

**Status:** FROZEN (pre-run). Result doc lands separately.
**Classification:** CONSISTENCY / foundation — **NO chord** (per the brief + Stage-0 precedent).

---

## SUBSTRATE-FIRST SECTOR HEADER (prereg, before any standard word)

- **SECTOR:** the **2 TRANSVERSE DOF** — the srs vector field's 2 polarizations.
  This ONE field carries BOTH:
  - the **EM-transverse PHOTON** (ε,μ modulus → c_EM = c₀/S, the α-bearing optical
    channel; Z_EM ≡ Z₀ at SYM loading), AND
  - the **transverse SHEAR / GW** (G_shear modulus → c_shear = c₀·√S, the
    matter/gravitational clock).
  At **S=1 (cold)** these are **DEGENERATE at c₀** — the constitutive split is
  **DRIVEN-only** (it appears only when S drops below 1 under loading). The split
  is keyed by **which modulus responds** (ε,μ for EM vs G for shear), NOT by a
  different field.
- **REGIME:** primarily **COLD** (T1.6 at S=1, linear/reversible/achromatic);
  PLUS **one DRIVEN smoke-probe** stepping S below 1 in the sub-yield / weak-load
  regime (NOT near-yield, NOT a rectification test). The FULL √S-shear validation
  (the saturated G-modulus machinery) is **DEFERRED to Stage 4** — explicitly NOT
  pulled forward.
- **NO winding / NO coupling:** the optical-activity rotation is a transverse SO(2)
  twist (def-0pt1ac, gyrotropy), NEVER the Cosserat (2,3) micro-rotation winding
  (charge). A1 ⊥ T2 (`master-equation.md:20`). Stage 1 carries STRUCTURAL chirality
  (lossless rotation ON, Axiom-3) but does NOT inherit the α-dressed
  `ETA_ROT_PER_WRITHE` as a bankable scale.
- **GRID:** the srs transverse grid (the FROZEN v9 vector-TLM medium). Stage 1 is
  NOT co-located with the Stage-0 cage grid — the photon is NOT forced onto the
  cage grid (that is Stage 3, the two-grid bridge). The driven c_EM phase-velocity
  smoke-check runs in the matching IMPEDANCE-PLANE coordinates (the graded-line
  varactor, `_em_media.em_params`), NOT the 3D-irregular real-space srs lattice
  (where a localized index step washes out, verified empirically 2026-06-17 —
  phase-space-coordinate-check, A46).

## VCA (vacuum-circuit-analysis) FRAMING — MANDATORY (Grant directive)

Frame circuit-native:

- The **photon** = the transmission-line transverse I/Q mode at **Z_EM ≡ Z₀**
  (the matched, reflectionless transverse channel; SYM loading scales ε,μ
  together so Z stays invariant → Γ=0).
- The **shear** = the **transverse-momentum channel** (the deviatoric / G-modulus
  transverse grade; Z_shear = ρ·c_shear).
- **Wave-type the refractive index by WHICH MODULUS responds** — ε,μ for the EM
  photon (c_EM = c₀/S) vs G for the shear (c_shear = c₀·√S). **NEVER substitute
  one for the other** — that IS the twice-conflated category error
  (`ave-kb/CLAUDE.md:71`; genesis-24 double-count).
- At S=1 (cold) BOTH channels reduce to c₀ — the degeneracy is the foundation
  property the T1.6 gate confirms; the DRIVEN split is what distinguishes them.

---

## FULL SKILL DISCIPLINE (Grant directive — all applied)

| Skill | Applied as |
|---|---|
| **ave-regime-phase-state-check** (THE key one) | The S=1 degeneracy is this skill's exact domain. MODE: 2 transverse DOF (BOTH c_EM achromatic AND c_shear the matter clock). REGIME: linear/cold (T1.6) + sub-yield-weak driven probe. PHASE-STATE: cold lattice (T1.6) / weakly-loaded (probe). **Structural-possibility check (load-bearing):** the driven smoke-check measures a SCALAR ⟨S⟩-deficit (propagation speed c(S)) — per the skill, a scalar/DC effect is **achromatic-compatible, EXISTS in every regime** (not gated to near-yield); only its magnitude scales with amplitude. So measuring c_EM→c₀/S and c_shear→c₀·√S at sub-yield S<1 is structurally VALID — NOT the rate-asymmetry/rectification (∮≠0) trap that needs bulk near-yield. The smoke-check is well-posed. |
| **ave-discrimination-check** | The deliverable does NOT re-conflate c_EM and c_shear: the wave-typing gate PINS the three index forms (n_EM_phase=S, n_EM_group=√S, n_shear=1/√S) and the alias identity so they cannot silently swap. No AVE-distinct chord is claimed (consistency-class). |
| **vacuum-circuit-analysis** | VCA framing above: photon = I/Q transverse mode at Z₀; shear = transverse-momentum channel; index wave-typed by responding modulus. |
| **substrate-native-check** | CP1 discrete srs-TLM scatter+connect (NOT Maxwell-vector FDTD / Lagrangian / gradient-descent). CP2 transverse 2-vector sector (A1⊥T2; winding never wired into the phasor). CP9 reads dynamically-evolved observables. CP10 the driven step is an impedance-plane constitutive, not a bulk well. |
| **phase-space-coordinate-check (A46)** | The driven c_EM split runs in the EM-sector IMPEDANCE-PLANE / phase-velocity coordinates (`_em_media.em_params`: c_EM, Z_EM, n_EM), the SAME coordinates the corpus claim lives in — NOT the 3D real-space srs lattice where a localized index step washes out. The T1.6 lossless/dispersion observables are real-space/spectral (the photon's native coordinates). Coordinates MATCH. |
| **consistency-vs-emergence** | Stage 1 is **CONSISTENCY / foundation, NO chord**. T1.6 = Class-C consistency (lossless transverse propagation is a foundation property). The driven split = Class-C consistency (the canonical wave-speed identities c_EM=c₀/S, c_shear=c₀·√S, reproduced — NOT an emergence). The wave-typing gate = Class-A identity (a structural pin, not a prediction). |
| **ave-canonical-source** | All constants imported from `constants.py` (EPSILON_0, MU_0, Z_0, C_0); the kernel S(A) is the canonical Axiom-4 form. **NEVER import ALPHA into the engine** — the guard triad is extended to the transverse/srs modules to enforce it. Engine-natural ratios in the dynamical path. |
| **ave-prereg** | corpus-grep done (Step 2 below); no prior Stage-1 transverse-mode result doc exists. T1.6 + the index functions + the `_em_media` varactor ALREADY exist + battle-tested; Stage 1 assembles + PINS them, does NOT reinvent. |
| **verify-before-cite** | The pathway doc mis-cited TWO paths (`chiral_lattice_vector.py` "does not exist" — it DOES, `src/ave/core/chiral_lattice_vector.py`; `gravity_sign_freq_modulation.py` in `src/ave/core/` — it lives in `src/scripts/verify/`). Both corrected by grep before any code. The "ambiguous legacy alias" claim is also stale — the alias was already hard-scoped in sign-lock w35sn2bq3 (2026-06-17). All paths re-verified at build time (§ Real engine paths). |

## Step 2 — corpus-grep outcome (ave-prereg)

- **No prior Stage-1 / transverse-mode result doc** (`ls research/ | grep -iE
  'stage1|transverse-mode'` → only the unrelated `2026-06-09_rectifier-stage1-...`).
  First build of Stage 1.
- **The substrate already exists** (do NOT reinvent): the T1.6 transverse-shear
  gate (`test_l1_multiwave.py:154-255`, green on the spine); the three wave-typed
  index methods (`master_equation_fdtd.py:169/175/183`, `crystal_engine.py:436/441/447`);
  the α-clean EM varactor (`_em_media.em_params`, imports only EPSILON_0/MU_0/Z_0/C_0);
  the srs vector-TLM (`chiral_lattice_vector.py`). Stage 1 PINS + extends, does not rebuild.

---

## Real engine paths (verify-before-cite — the pathway doc mis-cited two)

| What | Real path (grep-verified) | Pathway-doc claim | Verdict |
|---|---|---|---|
| chiral srs transverse vector engine | `src/ave/core/chiral_lattice_vector.py` | "does NOT exist" | **mis-cite** — it DOES exist |
| `fdtd_3d.py` | `src/ave/core/fdtd_3d.py` | (cited) | confirmed |
| `ETA_ROT_PER_WRITHE=1.0` α-leak constant | `src/ave/core/chiral_lattice_vector.py:27` | (cited) | confirmed |
| n_em GROUP = √S | `master_equation_fdtd.py:169` (`n_em_index`) | :169 | confirmed |
| n_shear = 1/√S | `master_equation_fdtd.py:175` (`n_shear_index`) | (cited) | confirmed |
| n_em PHASE = S (c_EM=c₀/S) | `src/scripts/verify/gravity_sign_freq_modulation.py:92,97` + `_em_media.em_params` (SYM) | "in `master_equation_fdtd.py` + `gravity_sign_freq_modulation.py`" | **path mis-cite** — the verify script is in `src/scripts/verify/`, not `src/ave/core/`; the engine method `master_equation_fdtd.n_em_index` is the GROUP index √S, not the phase index S |
| legacy `refractive_index()` alias | `master_equation_fdtd.py:183` + `crystal_engine.py:447` | "ambiguous, poisons later stages" | **stale** — already hard-scoped to `n_em_index()` (=√S GROUP) in sign-lock w35sn2bq3 (2026-06-17); `test_gamma_sign_gate.py:130` asserts the alias |

---

## THE THREE LIVE INDICES — WAVE-TYPING PLAN (the load-bearing fix)

The corpus carries THREE distinct refractive indices on the transverse field;
they are RECIPROCAL/distinct and a single scalar cannot serve all three. The
canonical taxonomy (`ave-kb/CLAUDE.md:79-80`, clm-8nkvwy phase/group;
`gravity_sign_freq_modulation.py:92-97`):

| Index | Form | Speed | Observable / role | Engine anchor |
|---|---|---|---|---|
| **n_EM PHASE** | **S** | c_EM = c₀/S (RISES) | Maxwell phase velocity; the α-speed; the constitutive | `gravity_sign_freq_modulation.py:92,97`; `_em_media.em_params` n_EM=√(S_ε·S_μ)→S at SYM |
| **n_EM GROUP** | **√S** | c_group = c₀·√S | optical/birefringence/ray-bending SIGNAL index | `master_equation_fdtd.n_em_index():169`; `crystal_engine:436` |
| **n_shear** | **1/√S** | c_shear = c₀·√S | Shapiro/gravitational ray-bending (reciprocal of n_EM_group) | `master_equation_fdtd.n_shear_index():175`; `crystal_engine:441` |

PLUS the FREE FUNCTION `refractive_index(M, r)` (`gravity/__init__.py:41`,
`orbital_resonance.py:39`) — the Schwarzschild isotropic-coordinate gravitational
n(r). DIFFERENT signature `(M, r)`; NOT a conflation risk with the engine
saturation index (the signature disambiguates).

**THE PLAN (what Stage 1 actually does — NOT a rewrite of already-correct code):**

1. **PIN all three index forms + the alias identity in a CI-gated regression gate**
   so Stage 4 (which inherits this) cannot silently re-conflate them. The gate
   asserts, at a swept set of A values (cold S=1 + driven S<1):
   - `n_em_index() == S^(+1/2)` (GROUP, →0 in core);
   - `n_shear_index() == S^(−1/2)` (→∞ in core); the two are EXACT reciprocals;
   - `refractive_index() is n_em_index()` (the alias holds, on BOTH engines);
   - the PHASE index n_EM_phase = S (via `em_params` at SYM, c_EM=c₀/S) is DISTINCT
     from the GROUP index √S — pin that they are NOT equal off S=1.
2. **HARD-SCOPE the legacy alias docstring** with a Stage-1 anchor so no future
   caller silently reads the wrong index — the alias stays (back-compat, 30+
   callers) but its scope is now CI-pinned (the gate fails if the alias drifts off
   `n_em_index`). NO alias is KILLED (killing it would break 30+ green callers);
   it is HARD-SCOPED (pinned + documented + gated).
3. **The driven smoke-check selects the RIGHT index by wave-type:** c_EM via the
   PHASE constitutive c₀/S (`em_params`, impedance-plane), c_shear via the
   canonical √S identity. They are computed from DIFFERENT moduli — never one
   substituted for the other.

---

## PRE-REGISTERED BINS (frozen pre-run)

### T1.6 VALIDATE-ON-KNOWN (cold, S=1) — must stay GREEN on the spine

- **PASS:** the transverse field carries 2 DOF LOSSLESSLY — lossless drift < 1e-8
  AND dispersion spread < 0.05 (linear) AND |c|/c_net within 5% AND
  transverse_dof == 2. (`test_l1_multiwave.py:227-232`, frozen 2026-06-17.)
- **FAIL:** lossy OR dispersive in-band OR wrong speed OR not 2-DOF.
- This is the inherited gate; Stage 1 RE-CONFIRMS it on the spine, does not modify it.

### S1.1 DRIVEN-SPLIT SMOKE-CHECK (the substance) — do the 2 modes split the RIGHT way off S=1?

Sweep A from 0 (S=1) upward into the sub-yield regime (A ∈ {0, 0.2, 0.4, 0.6}).
At each A, compute BOTH constitutive speeds in matching coordinates:
- c_EM/c₀ = 1/S (PHASE, via `em_params` SYM loading — the impedance-plane varactor);
- c_shear/c₀ = √S (the canonical matter-clock identity).

- **PASS (the modes are genuinely distinct + wave-typing wired correctly):**
  - at A=0 (S=1): c_EM/c₀ == c_shear/c₀ == 1 (DEGENERATE, within 1e-9);
  - as A rises (S falls below 1): c_EM/c₀ RISES strictly above 1 (c_EM = c₀/S > c₀)
    AND c_shear/c₀ FALLS strictly below 1 (c_shear = c₀·√S < c₀);
  - the split is MONOTONIC and in OPPOSITE directions (c_EM up, c_shear down) —
    they diverge from the c₀ degeneracy;
  - the wave-typing is wired: c_EM reads the ε,μ PHASE constitutive, c_shear reads
    the G √S identity — DIFFERENT moduli (the gate fails if they read the same form).
- **FAIL / STOP-and-report:** if they do NOT split, OR split the WRONG way (c_EM
  falls or c_shear rises), OR both read the same form — the wave-typing is BROKEN.
  Per the brief: STOP + report; do NOT patch around it.
- **SCOPE (regime-labelled per ave-regime-phase-state-check):** this is the
  sub-yield sanity check that the 2 modes are distinct + wave-typed, NOT the full
  near-yield √S-shear validation (Stage 4). The c_shear value here is the
  CONSTITUTIVE IDENTITY c₀·√S evaluated at the operating point — it is the
  desk-calc the saturated G-modulus dynamical engine (Stage 4) must reproduce.

### S1.2 WAVE-TYPING / ALIAS GATE — the three indices pinned (CONSISTENCY)

- **PASS:** all three index identities hold at every swept A (n_EM_group=√S,
  n_shear=1/√S exact reciprocals; alias `refractive_index() is n_em_index()` on
  both engines; n_EM_phase=S distinct from √S off S=1). The wave-typing cannot
  silently swap.
- **FAIL:** any index drifts off its canonical form, OR the alias points
  elsewhere, OR phase==group off S=1 (the conflation).

### S1.3 GUARD-TRIAD EXTENSION — the α-clean immune system covers the transverse/srs modules

- **PASS:** the guard triad (ALPHA / ALPHA_COLD_INV / Q_TANK / ELECTRON / RHO_BULK
  absent from globals) covers the transverse-mode code path. STRUCTURAL chirality
  is ON (lossless optical-activity rotation, Axiom-3) but the α-dressed
  `ETA_ROT_PER_WRITHE` is NOT inherited as a bankable magnitude (it is the tagged
  engineering scale, flagged not baked).
  - ⚑ KNOWN α-IMPORT (flag-don't-fix): `chiral_lattice_vector_sat.py:15` imports
    `ALPHA, R_I`. This is the genesis self-lock engine (Phase-2), NOT the Stage-1
    transverse wave-typing substrate. The Stage-1 driven smoke-check routes through
    the α-CLEAN `_em_media.em_params` (imports only EPSILON_0/MU_0/Z_0/C_0), NOT
    `_sat`. The guard gate asserts the Stage-1 code path is α-clean AND records the
    `_sat` α-import as a NAMED out-of-scope contaminant (Stage 4 must clean it
    before it can host the saturated c_shear dynamics). Surfaced, not silently fixed.
- **FAIL / HARD-STOP:** any α-carrier reachable in the Stage-1 transverse code path,
  OR a measured speed/index in an α-leak band, OR `ETA_ROT_PER_WRITHE` promoted to
  a bankable scale.

---

## Classification (consistency-vs-emergence — Stage 1 is CONSISTENCY, NO chord)

- **T1.6** = **Class-C consistency** — lossless 2-DOF transverse propagation is a
  foundation property of the lossless vector-TLM (Axiom-3 reactive cycling).
- **S1.1** = **Class-C consistency** — the canonical wave-speed identities
  (c_EM=c₀/S, c_shear=c₀·√S) reproduced; the split is the DEFINITION of the two
  channels, not an emergent prediction.
- **S1.2** = **Class-A identity** — the index forms are structural pins, not predictions.
- **S1.3** = **Class-A identity / foundation** — the guard asserts ARE the immune system.

**No Class-D emergence / chord claim anywhere in Stage 1.** Correct — Stage 1 is a
foundation stage (the 2 transverse modes wave-typed), not a chord. The AVE-distinct
chord lives in the FORWARD predictions (Stage 7), not here.
