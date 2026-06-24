# PATHWAY — the complete dynamic multi-soliton, all-modes vacuum engine

**Created:** 2026-06-23 · orchestrator-tracked · **Status:** SCOPED (grounded, workflow `wrpjr2t1y`); awaiting Stage-0 go
**Directive (Grant 2026-06-23):** "the full pathway to a fully dynamic multi-soliton and wave-interaction tracking engine with all propagation modes supported." Supersedes the narrow cage⊗winding charter ([`2026-06-23_cage-winding-engine-charter.md`](2026-06-23_cage-winding-engine-charter.md)) — that charter's Gate 0 becomes Stage 0 here.

## End state
ONE engine, ONE reconciled K4 grid, the full **6-DOF micropolar node**: {2 transverse — photon c_EM=c0/S, shear/GW c_shear=c0√S; 1 longitudinal-bulk — A1 dilatation c_bulk=√2·c0 (K=2G); 3 micro-rotational — gapped Cosserat ω(k), charge=winding}, all four impedance channels coupled through **one conserved H_couple** (no pump; dual energy+|L| canary), each mode carrying a **CI-gated validate-on-known** at a pinned tolerance. Fully dynamic, multi-soliton, all interactions tracked.

## Architecture decision (Gate 0's inversion)
**Build on the α-CLEAN cage + ring-down-Q foundation and ADD the DOF — do NOT adopt the α-baked `CosseratField3D` as host.** The clean foundation exists and is armed: `_bulk.py:466 ringdown_Q` (honest cold ring-down, returns ∞ for a lossless cage), the guard triad (`graded_vacuum_network.py:111-114` asserts ALPHA/Q_TANK/ELECTRON/RHO_BULK not in globals), the literal scrubber (`charge_quantization.py:104` forbids '137','0.00729'), the landing-zone CI gate. `CosseratField3D` is host-contaminated (imports ALPHA :56, bakes KAPPA_CHIRAL=α·κ̃ :131, carries the golden-torus Q closed-form = α⁻¹ at :2422, live at 4 callers) — its DOF are reused, its Q-readout is not.

## The 8 stages

| # | Name | +DOF/mode | Validate-on-known | Cost | Dominant risk |
|---|---|---|---|---|---|
| **0** | Foundation + α-clean spine lock (re-scoped Gate 0) | none — cold CrystalEngine + c_eff(V) cage on the K4 node set; `ringdown_Q` the ONLY Q-extractor | cold lossless cage rings down Q=∞ honestly (NOT 137); guard triad fires at load; literal scrubber + landing-zone gate green | CHEAP (wiring) | subtle α re-leak via a default kwarg / Q_TANK class default |
| **1** | EM-transverse + transverse shear (srs chiral grid) | 2 transverse: photon c_EM=c0/S, shear c_shear=c0√S | T1.6 (real pytest gate): lossless drift<1e-8, dispersion<0.05, \|c\|/c_net±5%, transverse_dof==2 | CHEAP | the n_eff √S-vs-1/√S overload must be wave-typed now |
| **2** | c_eff(V) stiffening cage + self-trap | none — adds c_eff(V)→∞ co-located on the chiral grid | recover c_eff²=c0²/S, n_em=S^0.5; precursor self-traps at A→1 and stays localized | MODERATE | self-trap returns Mode III on the chiral grid |
| **3** | **Two-grid bridge** (FIRST RECONCILIATION MILESTONE) | none — STRUCTURAL: collapse Yee-EM / continuum-cage / K4-ω onto ONE K4 node set; Cartesian ∇²V → K4 graph-Laplacian (z=3) | re-pass every prior gate, no regression; close CFL/Nyquist at the shared dt BEFORE any formation run | **EXPENSIVE** | tighter shared-dt slow, OR K4 under-resolves a (2,3) winding → reads back as (2,2)/garbage at r≤1.1 cells |
| **4** | A1 longitudinal-bulk as a REAL vector grade | 1 longitudinal: c_bulk=√2·c0 (K=2G); mass = propagating dilatation, NOT a projection | c_bulk=√2·c0 MEASURED (T1.7 longitudinal_dof flips False→True); new CI gate | MOD–EXPENSIVE | longitudinal couples spuriously into transverse, breaks T1.3 |
| **5** | Cosserat micro-rotation as INDEPENDENT gapped DOF (charge=winding) | 3 micro-rotational: genuine ω 3-vector, gapped ω²=c²k²+m², m²=4G_c/I_ω; **c_R [⚠ value under adjudication, see below]** distinct from c_bulk | mass-gap period 0.35% as a SHA-pinned CI gate (today only driver/leaf-recorded); gapless c_R check | EXPENSIVE | a (2,3) winding reads back as (2,2)/garbage below the minor radius |
| **6** | Conservative cross-sector coupling — ONE H_couple | none — couples A1/shear/EM/Cosserat via a single conserved H_couple | skew-Hermitian/rotation generator transfers norm-preserving (1.1e-12/40k); DUAL canary every run: \|dH/H\|<1e-8 + the \|L\| pump canary | **EXPENSIVE** (most fragile) | the keystone energize-LOCK negative — coupling pumps H at dt→0 |
| **7** | **Writhe-aware force kernel** + multi-soliton observables (the chord) | none — inter-soliton force kernel: co-vs-anti-handed \|F\| (Observable-C), gravity-refraction, scattering | writhe-aware (RMF-bend/Bishop holonomy) kernel: signed equal-magnitude enantiomorph holonomy + EXACT achiral null | **EXPENSIVE** | the false-zero (chord invisible if the kernel reads only local bond geometry); the chord's bankable MAGNITUDE is OPEN |

## Critical path + schedule
**Stage 0 → Stage 3 (two-grid bridge) → Stage 6 (conservative H_couple) → Stage 7 (writhe kernel).** The cheap stages (1, 2, 4, 5 — wiring + live-fire on existing primitives) are NOT on the critical path; the schedule is gated by the **three expensive open-research items**: the two-grid bridge (every multi-mode test is blocked on it), the conservative coupling (the documented trilinear-detonation / keystone-pump risk), and the writhe-aware kernel (the chord's make-or-break, with the false-zero trap).

## First milestone
**Re-scoped Gate 0 (Stage 0):** on the α-clean foundation, show (a) the cold lossless cage rings down to Q=∞ honestly via `_bulk.py:466` (NOT 137 — Q measured, not closed-form); (b) the guard triad fires at module load on every engine module; (c) the literal scrubber + landing-zone gate stay green. (The original Gate 0 HARD-STOP, PR #394, was on the wrong host — this re-scopes it onto the clean spine.)

## Open items folded in
- **⚠ c_R value (Stage 5):** the grounding gives c_R=√(γ/I_ω)=**1** natural and warns √2 is the K=2G *bulk* ratio (a DISTINCT speed; `dual-reactance-storage-taxonomy.md:51` "do not fuse with V=2"). This **contradicts** clm-kmliqx / #395 (c_R=√2). **#395 is HELD** pending the read-AND-run adjudication (agent `a179…`). Stage 5's c_R is pinned to the adjudication outcome.
- **Stale corpus:** `engine-capability-map.md:121` still flags the S^0.25-vs-S^0.5 exponent defect as open — it was FIXED 2026-06-17 (`master_equation_fdtd.py:169` now returns S^0.5). Needs a Rule-12 "landed" header.
- **CI gap:** the Cosserat mass-gap validate (0.35%, T=π) is script/leaf-recorded, NOT a CI-gated pytest assertion — Stage 5 must SHA-pin it.
- **Grep-completeness:** the prior "cosserat_master_equation_fdtd.py missing" was a false-negative (it exists, `src/ave/core/`, a 2-scalar toy — NOT the micropolar carrier; `CosseratField3D` is).
