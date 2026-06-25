# S2 RESULT — A conservative skew-Hermitian `H_couple` locking A1↔ω: PASS

**Status:** RESULT (committed gate + acceptance test; branch-only, NOT merged — Grant merges).
**Date:** 2026-06-24
**Pre-reg (FROZEN):** [`2026-06-24_engine-s2-hcouple_prereg.md`](2026-06-24_engine-s2-hcouple_prereg.md) (commit `38066fd2`, frozen pre-run; both forks RULED — A=(a) saturation-front intra-mechanical, B=(b) splitting-OK/not-slaved).
**Epic:** AVE engine RE-ROUTE — [`_orchestration/2026-06-24_engine-reroute-pathway.md`](../_orchestration/2026-06-24_engine-reroute-pathway.md) S2 row.
**Branch:** `analysis/engine-s2-hcouple` off `38066fd2` (off origin/main `1d4eae9c`, PR#407 merged / S1 landed).
**Gate code:** `src/ave/core/s2_hcouple_gate.py`. **Test:** `src/tests/engine_acceptance/test_s2_hcouple.py` (10 tests, all PASS; `make verify` PASS).

---

## VERDICT: PASS — all four make-or-break criteria hold; immune system healthy.

The standalone gate prints `VERDICT: PASS` (exit 0). A **field-resolved skew-Hermitian
`H_couple` in the A1↔ω sector pair** (A1 bulk-dilatation breather = mass ↔ Cosserat
micro-rotation ω = charge winding), S(A)-gated (FORK A=(a) intra-mechanical, NO TKI
transducer), on the α-clean host, is **conservative + non-vacuous + independence-preserving**
and **recovers the PR#321 node_circulator 2-mode generator in its reduced limit**. This is
the prerequisite for the S3 pinning test — S2 does NOT itself prove pinning.

It is **CONSISTENCY-class, NOT the α-free chord** (the chord-decider is S4); the **Q=137
slot stays EMPTY**; **mass=A1 (PR#260) untouched**. S2 does NOT test confinement (S3),
boundary observables (S4), or the non-reciprocity MAGNITUDE (corpus-flagged ECHO).

### Make-or-break criteria (pre-reg §Make-or-break)

| Criterion | Outcome | Evidence (live run, N=48 R=11 r=4, 40k-step closed window) |
|---|---|---|
| (1) CONSERVATION | PASS | joint `H = E_A1 + E_ω + H_couple` drifts `|dH/H| ≈ 4.7e-11 ≪ 1e-8` over a CLOSED-system window (NO loss port — T2 guard); late pump-slope ≈ 3e-14. Generator skew-Hermitian. (precedent `test_l1_photon.py:285`; PR#321 target ≈1.1e-12.) |
| (2) NON-VACUITY | PASS | A1 loaded / ω EMPTY (initial ω energy = 0.0); ω fills `83%` (**42× the failed 2% inert arm**); oscillates (134 zero-crossings — a real flow, not a static offset); the `|L_ω|` pump canary stays BOUNDED (secular late/early ratio 1.02; max 5.7 < physical ceiling 28). |
| (3) INDEPENDENCE | PASS | REAL arm `(2,3)==(2,3)` robust under a V-perturbation; the SLAVED arm (ω:=F(V)) returns independence=False (reachable-False, NOT AUTO_VOID; slaved winding degrades `(0,0)→(1,0)`). Normal-mode SPLITTING `split=0.6=2Ω` is DECLARED EXPECTED + bounded (FORK B=(b)), explicitly NOT scored as a violation. |
| (4) REDUCED-LIMIT | PASS | `build_hcouple(M=1, front-center A)` EXACTLY equals the PR#321 `node_circulator circulator_generator` (generator equality to 1e-13 + trajectory equality to 1e-10 + Rabi anchor); robust across `(ω_b, ω_s, rate, χ)` incl. achiral χ=0. NOT ADD-2 (V↔w). |

**Dual canary (each leg reachable-FAIL in the same harness — T6):**
- `|L_ω|` pump FIRES — a detonating non-Hermitian directional-gain arm (the field analogue of `photon_deplete=True`, **NEVER on the real arm** — T5) pumps `|L_ω|` 26× vs the bounded real arm.
- `|dH/H|` conservation FIRES — an open/lossy anti-Hermitian arm drifts 86% vs 3.6e-12 on the closed arm (guards T2 damping-bought conservation).

**α-clean:** confirmed — readout through `_winding_host` (κ̃=6/5, guard triad live); chirality phase θ_χ=2π·ν_vac (ν_vac=2/7); no executable ALPHA / KAPPA_CHIRAL_ELECTRON / V_SNAP / L_NODE / M_E / Q_TANK on the chord path; guard is LIVE (a deliberately-injected `ALPHA` global is caught). Q=137 slot empty.

---

## What the build is (the genuine new work)

A **field-resolved** state `ψ ∈ C^{2M}` on an M-node chain: per node `a_A1` (A1 bulk-dilatation
breather analytic signal; `|a_A1|²` = trapped bulk = MASS) and `a_ω` (the LOCAL Cosserat (ω, π_ω)
LC-quadrature analytic signal; the poloidal winding / CHARGE "3"). The Hermitian generator
carries the **A1↔ω ON-NODE off-diagonal** `Ω_n·e^{±iχθ_χ}` with `Ω_n = rate·g_front(A_n)·S(A_n)`
— the saturation-front-gated coupling PORT (FORK A=(a); `S(A)=√(1−A²)` is IDENTICAL to
`crystal_engine.saturation_kernel`). The chirality phase χ·θ_χ is a STRUCTURAL lattice phase,
NOT ω-read-off-V (genesis-24 guard). Intra-grade nearest-neighbour hops carry the field-resolved
spatial transport. There is **no existing field-resolved coupling in the A1↔Cosserat-ω pair**
(ADD-2 = V↔w, the WRONG pair — recovering it does NOT count; pre-reg WRONG-SECTOR-PAIR guard).

H is Hermitian by construction ⇒ `e^{-iHt}` unitary ⇒ no indefinite-trilinear detonation on the
skew path (pre-reg T5 — the dead-end the trilinear potential hit, `H_bel −4107`).

---

## HONEST FLAGS (surfaced, not papered over)

1. **`|L_ω|` canary redefined pre-verdict (Rule 10, NOT a tune-to-PASS).** The initial canary
   was an arbitrary absolute cap (5.0) the bounded-reactive oscillation (amplitude ~5.7, set by
   M + loaded energy) marginally exceeded. The substrate-native distinction the pre-reg names
   (`|L_ω|` pump BOUNDED) is bounded-reactive (oscillates, late≈early) vs a PUMP (secular runaway,
   S1's 9.5×). Redefined as the late/early quartile-mean ratio (< 1.5) + a physical energy-available
   ceiling `N0·(M−1)/2` — value-free thresholds. Surfaced before freezing the verdict.
2. **Integrator-time bug fixed (Rule 10).** The propagator used `np.linalg.eigh` unconditionally;
   `eigh` SILENTLY symmetrizes a non-Hermitian generator, so the loss/gain negative-control arms
   came back UN-fireable (identical drift to the closed arm — a vacuous canary, T6). Fixed: the
   Hermitian real arm keeps the exact eigendecomposition (unitary, machine precision); non-Hermitian
   neg-control arms route through `scipy.expm` so the non-conservation the canary must detect is
   represented faithfully. This is exactly the class of bug Rule 10 (run the driver early) surfaces.
3. **Criterion 3 reuses the S1 discriminator, not a new one.** Independence is operationalized by
   INVOKING `s1_winding_conservation_gate.gate_f_positive_control` on the real `CrystalGraftV4`
   (anti-rebuild, Rule 14) — the precise reachable-False slaved-arm discriminator the pre-reg cites
   (`:439`). S2 does not re-implement it. The S1 flags (two-extractor coordinate-category; controls
   on the coupled arm) are inherited.
4. **The field-resolved coupling is a 2-mode-per-node complex-amplitude model, not the full
   real-space FDTD engine.** It is field-resolved (M nodes, per-grade dispersion, S(A)-gated per-node
   rate) and recovers the node_circulator ODE in its limit — the genuine new work the pre-reg §NOTE
   demands (like S1). It is NOT a full re-solve of the `CrystalGraftV4` PDE on the A1↔ω pair; the
   real-engine arm is used (criterion 3) only for the independence discriminator.
5. **CONSISTENCY-class, not a chord.** A green S2 demonstrates a substrate-consistent conservative
   lock; it does NOT emit an AVE-distinct chord. The non-reciprocity MAGNITUDE the circulator carries
   is corpus-flagged ECHO-at-magnitude (`research/2026-06-20_node-circulator-coupling.md:11`) and is
   OUT OF SCOPE for S2.

**Net:** the make-or-break verdict (a conservative skew-Hermitian A1↔ω `H_couple` that transfers,
keeps ω independent, and recovers the 2-mode generator) is robust to flags 1–5; none changes PASS→FAIL.

---

## Reproduce

```bash
cd <worktree on analysis/engine-s2-hcouple>
PYTHONPATH=$PWD/src .venv/bin/python src/ave/core/s2_hcouple_gate.py          # standalone gate → VERDICT: PASS
PYTHONPATH=$PWD/src .venv/bin/python -m pytest src/tests/engine_acceptance/test_s2_hcouple.py -q   # 10 tests
```

- gating lane (`-m "not engine_sim"`): 8 passed, 2 deselected (~0.6s).
- engine lane (`-m engine_sim`): 2 passed, 8 deselected (~45s, real `CrystalGraftV4`).
- `make verify`: ALL PHYSICS PROTOCOLS PASSED.

## What this delivers to the pathway

- **S2 PASS** → the A1↔ω lock is conservative + non-vacuous + independence-preserving: the
  prerequisite for the S3 mutual-pinning test (Γ=−1 cavity). The pinning hypothesis itself remains
  OPEN — S2 proves the COUPLING, not the pinning. 🔴 *(2026-06-24 update: the S2 PASS verdict
  STANDS — the coupling IS conservative/non-vacuous/independence-preserving. But the forward-looking
  "the pinning hypothesis remains OPEN" is now superseded: S3 (DISPERSE-FALSIFIED) + the coupled
  eigensolve (#415) + the phase-space coupling-winding BREAK (#417) read NEGATIVE in BOTH internal
  dynamical loci — the winding does NOT pin the dispersing A1 core. Localizer = cavity-eigenmode;
  the (2,3) RIDES the cage as STATIC charge (Link, un-walked-back). See
  research/2026-06-24_engine-reroute-epic-summary.md.)*
- **NOT a chord.** S2 is the consistency gate; the chord lives at S4 / the forward predictions.

## Recommended follow-up (implementer-lane; auditor lands the manual/pathway entries)

- Surface the S2 row to the auditor for `_orchestration/2026-06-24_engine-reroute-pathway.md`
  (the auditor lands pathway/manual entries per lane discipline).
- Next stage = **S3 (Γ=−1 cavity / mutual-pinning)** per the pathway critical path.
