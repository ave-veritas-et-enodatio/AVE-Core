# Full-electron Option B — (2,3)-emergence on the DISCRETE engine (the real test)

**Status:** PENDING — implementor dispatch (worktree-isolated). Follows Option C (Mode II,
`2026-06-04_full-electron-binding-reseed-probe.md` §RESULT): the continuum Maxwell engine
self-traps a transverse photon into mass but has **no carrier** for the (2,3) winding (the
SU(2) U(1)-fibre poloidal-"3" is projected out per `06_winding_index_projection.md` §4). Option B
moves the headline onto the engine that **has** the carrier.

## §1 Target + physical picture (Checkpoint 8 — generative-precursor discipline, substrate-native-check v1.1)

**Target:** On **`VacuumEngine3D`** (K4-TLM + Cosserat — native (V_inc,V_ref) ports + Cosserat ω +
the **Op10 winding-extractor**, all of which `fdtd_3d.py` lacked), seed the **generative precursor**
(a structured transverse photon) and test whether (a) it **self-traps** and (b) the **(2,3) winding
EMERGES** — i.e. **Grant's hypothesis: "a transverse wave across multiple nodes SETS the 2,3."**

**Picture (per Checkpoint 8 — seed the precursor, let the dynamics build up; do NOT plant the
finished (2,3) end-state):**
1. Generative precursor = a structured transverse photon (counter-propagating opposite-handed
   focused pulses, multi-node, E⊥B⊥k) — same precursor that self-trapped cleanly in Option C.
2. Let the dynamics build up: at saturation the photon self-traps; the question is whether, on an
   engine that **carries** (V_inc,V_ref) + Cosserat ω, the **(2,3) winding emerges** in the phasor
   sector as the trap forms (read it with Op10 in (V_inc,V_ref) phase-space — phase-space-coordinate-check).
3. The (2,3) is the layer under test — it must EMERGE, not be planted (ave-driver-script-honesty:
   the emergence arm must not impose the winding it tests for). The Option-D nucleation rule
   (`pair-production-axiom-derivation.md:121`) is the IMPOSED control, clearly labeled.

## §2 Architectural context (load-bearing — the implementor must know this)

| Engine | c_eff self-trap (mass) | (2,3) carrier (charge/spin) |
|---|---|---|
| `fdtd_3d.py` (continuum Maxwell) | ✓ (nonlinear ε/μ) | ✗ — no (V_inc,V_ref) ports, no Cosserat (Option C → Mode II) |
| Master Eq FDTD | ✓ (breather) | ✗ — scalar |
| **`VacuumEngine3D` (K4-TLM + Cosserat)** | **? — K4-TLM is Z(V)-only, no explicit c_eff (v14 was Mode III on the planted bound state)** | **✓ — native ports + Cosserat ω + Op10** |

So VacuumEngine3D is the only engine with the (2,3) carrier, **but its self-trap is uncertain**
(Op3 bond-reflection + Cosserat dynamics + the topology may provide binding; or c_eff may be absent
— the doc-111 Path A gap). **Test as-is FIRST.** Do NOT free-build the ~1-2 wk c_eff refactor —
if the self-trap fails, surface the Path-A decision to Grant (pre-test-physics-check).

## §3 Skill discipline (mandatory)
**ave-prereg** (frozen prereg first; pull `VacuumEngine3D` API + Op10 winding-extractor +
`pair-production-axiom-derivation.md` + the staged starting point `r10_v8_t_st_self_trap.py` that
Option C left as the discrete-Cosserat comparison arm) → **substrate-native-check v1.1** (Checkpoints
1-7 for the sector/coordinate/reactance physics + **Checkpoint 8** for the generative-precursor /
build-up strategy) → **phase-space-coordinate-check** (the (2,3) lives in (V_inc,V_ref) Clifford-torus
phasor; Op10 must read THAT field — A47 v3: verify which field Op10 reads matches the winding claim)
→ **ave-canonical-source** → **ave-canonical-leaf-pull** (the (2,3)/Beltrami/Op10/pair-production canon)
→ **ave-driver-script-honesty** (the (2,3) must EMERGE, not be hardcoded) → **consistency-vs-emergence**
(headline: emergent vs imposed — a Class-D dynamic emergence test; the (2,3)-emergence is the
load-bearing claim) → **ave-fundamental-ground-up-implementation** (substrate-derive PASS bars; matched
baseline not random) → **ave-evidence-framing-discipline** → **ave-ee-first-mapping** (transverse photon
↔ (V_inc,V_ref) on the discrete engine) → **pre-test-physics-check** (surface any framing ambiguity —
especially the self-trap/Path-A question — to Grant, do NOT free-build).

## §4 Discriminating outcomes (the verdict)
- **(i) Self-traps AND (2,3) EMERGES** (Op10 winding = (2,3), zero imposed) → **Grant's hypothesis
  CONFIRMED — the transverse wave SETS the (2,3); the full electron (mass+spin+charge) hosts on
  `VacuumEngine3D`.** The deep result.
- **(ii) Carries the (2,3) structure but does NOT self-trap** (disperses, like K4-TLM v14 Mode III)
  → the carrier-engine lacks the binder; **c_eff(V) must be added (doc-111 Path A)** — a structural-
  capability finding. Surface the Path-A go/no-go to Grant; do NOT build it unbidden.
- **(iii) Self-traps but the (2,3) does NOT emerge** (only persists when IMPOSED via the nucleation
  rule) → the transverse wave does NOT set the (2,3); it's topological-selection, not transverse-set.
  **Grant's hypothesis refuted** on the discrete engine.

## §5 Deliverables
- Driver `src/scripts/vol_1_foundations/r10_vacuumengine3d_transverse_2_3_emergence.py` (build on the
  staged `r10_v8_t_st_self_trap.py`; incremental commits, skeleton-first).
- `research/2026-06-04_full-electron-option-B-discrete-emergence-result.md` (prereg + result + the
  §4 verdict).
- `make verify` PASS (run with main-checkout venv). Push the branch
  `analysis/2026-06-04-full-electron-option-B-discrete`; do NOT merge.
- Report: the §4 outcome (Grant's hypothesis confirmed / refuted / needs-c_eff), branch + paths,
  make-verify, + any surfaced-for-Grant question.
