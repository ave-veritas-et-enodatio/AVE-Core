# KICKOFF BRIEF — Baryon per-channel coupling (R2 closure): is k=1 forced by the knot crossings?

**Date:** 2026-06-01
**Type:** Theoretical-physics investigation — cross-repo (AVE-Core L3 derivation + read-only AVE-HOPF reference)
**Status:** READY — run in a dedicated analysis session (branch off `main`, push, do NOT merge)
**Feeds:** the Parameter Ledger walk-back — see [`2026-05-28_parameter-count-framing-walkback.md`](2026-05-28_parameter-count-framing-walkback.md). Decides whether the canonical ledger's baryon row (`backmatter/02_full_derivation_chain.tex:1047`) reads **"derived"** vs **"derived modulo R2"**.
**Origin:** 2026-06-01 V=2 dual-reactance closure session (Grant-posed: *"map the knot crossings to the transformer turns-ratio"*).

---

## Context (from the 2026-06-01 V=2 dual-reactance closure)

The baryon mass eigenvalue is `m_p = I_scalar / (1 − V·p_c) + 1` (Black's regenerative-loop form).
- **V = 2** is FORCED (the node's two reactance sectors, X_C capacitive-E + X_L inductive-B). Closed.
- **p_c = 8πα** is DERIVED (packing fraction at the K=2G operating point).
- **The one open residual ("R2", the "1-residual Skyrme"):** the per-channel coupling coefficient **k is ASSUMED = 1** (bare p_c, no projection factor) because it lands on `m_p = 1836` — it is not yet derived.

Leptons carry a **non-unity** coupling coefficient `√(3/7)` (chirality-mismatch projection); the baryon uses **bare p_c**. R2 is precisely: *is k = 1 forced, or fit-to-mass?*

## Hypothesis to test (Grant's turns-ratio idea)

k is set by the knot's **crossing structure**, via the canonical per-crossing transformer coupling
`M/L = exp(−d²/4σ²) = 1/√2`. Cascade the `(2,c)` knot's `c` crossings as `1/√2` transformer
couplings (a turns-ratio per crossing) and check whether the net per-channel k comes out:
- **= 1** (bare p_c) → **R2 CLOSES**; the baryon row is genuinely "derived"; or
- **≠ 1** → changes `m_p` (a refinement, or a problem to report).

This is not a green field — the corpus already has the same `1 − (crossing-count)·(packing-fraction)`
algebra in the orbital sector (`k_pair = (2/Z)(1 − P_C/2)`, the `P_C/2` arising from Hopf crossing
number c=2). The investigation is whether the **baryon** per-channel k falls out of the **same machinery**.

## Keep distinct — DO NOT FUSE

| Symbol | Meaning | Status |
|---|---|---|
| **V = 2** | reactance-SECTOR count (Black's-loop multiplicity) | FORCED — not the question |
| **c** | knot CROSSING number (5 for the proton) | topological input |
| **k** | per-channel coupling COEFFICIENT (inside V·p_c) | THE residual under investigation |

The investigation concerns only **k**. V stays 2.

## Canonical hooks (verify each — then build on)

- R2 framing + honest status: `research/2026-06-01_baryon-V2-dual-reactance-closure.md` §4 + `manuscript/ave-kb/common/dual-reactance-storage-taxonomy.md`
- Baryon mass form: `manuscript/backmatter/01_appendices.tex:97` (m_p formula), `:98` (M/L = 1/√2 at crossing)
- V_total from crossing mutual-inductance: `manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/thermal-softening.md:75,79`
- Hopf coupling — same algebra, orbital sector: `manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/stepped-impedance-resonator.md:48` + `radial-eigenvalue-solver.md:579` (`k_pair = (2/Z)(1 − P_C/2)`, `P_C/2 ← Hopf c=2`)
- Nuclear crossing→phase→prefactor: `manuscript/ave-kb/vol2/proofs-computation/ch11-overdrive/overdrive-nuclear.md:18` (each crossing → π/2 phase → c·π/2 prefactor)
- Transformer turns-ratio machinery: `manuscript/ave-kb/vol5/molecular-foundations/organic-circuitry/first-principles-bond-force-constants.md:151` (split-core transformer, N_min/N_max = n*_min/n*_max)
- Canonical ledger (the consumer of this result): `manuscript/backmatter/02_full_derivation_chain.tex:982–1071` (scorecard; baryon row `:1047`)
- HOPF gate (read-only sibling repo — this CLOSES one of its 4 open AVE-Core-gated derivations): `AVE-HOPF/.agents/HANDOFF.md:49,127` + `AVE-HOPF/manuscript/vol_hopf/chapters/03_standard_model_baseline.tex:30,103`

## Reconcile FIRST (potential corpus inconsistency — flag-don't-fix if it bites)

The proton is variously described as (a) a Borromean 3-loop halo (the V=2 dual-reactance framing),
(b) a `(2,5)` cinquefoil with 5 crossings (`overdrive-nuclear.md:18`), (c) a c=5 ladder rung.
**Pin down the crossing count that feeds k, and how it relates to the V=2 reactance sectors,
BEFORE the cascade arithmetic.** If these descriptors genuinely conflict, surface it with verbatim
evidence rather than papering over it.

## Success criteria / discriminator

- **CLOSE (best):** the crossing-cascade of `1/√2` couplings over `(2,c)` forces **k = 1** (bare p_c),
  with the no-chirality-mismatch argument explaining why the baryon carries no `√(3/7)` projection
  (the lepton self-energy has a chirality mismatch; the baryon core↔halo reactance coupling is a pure
  radial cross-sectional overlap). → R2 → derived; the ledger baryon row is genuinely "derived".
- **REFINE:** cascade gives `k ≠ 1` but self-consistent → `m_p` prediction shifts; report the new
  value against CODATA `m_p/m_e = 1836.153`.
- **STAYS-RESIDUAL:** no crossing structure forces k → R2 confirmed residual; the ledger discloses
  "baryon: k = 1 assumed (per-channel coupling), pending crossing-cascade derivation."

## Skill discipline (write a skill-selection plan FIRST)

- `ave-ee-first-mapping` — crossing ↔ transformer turns-ratio is the EE-native frame; run it FIRST.
- `ave-canonical-leaf-pull` — enumerate the matched-coupling + crossing canon as a SET before deriving.
- `substrate-native-check` — K4 + Cosserat, not continuum.
- `ave-prereg` — corpus-grep across all repos + pre-register the expected k BEFORE computing.
- `pre-test-physics-check` Trigger 7 — if the derivation produces repeated negatives, surface the
  plumber-reframe before concluding "negative" (this is the V=2 lesson that motivated the trigger).

## Scope guard

This is the **R2-physics investigation only.** It FEEDS the Parameter Ledger walk-back (decides the
baryon row's classification) but does **NOT** touch the manuscript walk-back PR (separate, awaiting
the ledger). **Output:** a `research/` result doc + prereg in AVE-Core. Do **NOT** edit AVE-HOPF
(read-only reference). Branch off `main`, push the branch, do **NOT** merge — orchestration session
does the PR merge.
