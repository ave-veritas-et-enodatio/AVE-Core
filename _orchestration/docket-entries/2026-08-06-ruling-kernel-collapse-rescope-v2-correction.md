# 🔴 Correction — kernel-collapse rescope v2 record (2026-08-06, post-merge Tier-2)

Correction fragment for `2026-08-06-ruling-kernel-collapse-rescope-v2.md` (merged,
#905), from the independent Tier-2 verification that completed after Grant's merge.
Post-merge correction-PR pattern; the v2 record body is preserved unedited. Two blocking
findings (both the orchestrator's), plus advisory repairs folded in.

## C1 (blocking, D1) — the v2 ruled text's full delta-from-v1, now DECLARED

Word-diff of the v1 blockquote against the v2 blockquote yields THREE deltas; the v2
header declared only the first two:

1. Header stamp: "(2026-08-05)" → "(2026-08-05; member-fenced 2026-08-06)". **Declared.**
2. The cross-grade combine-member fence sentences. **Declared.**
3. "(a coupled two-channel scattering computation, routed as the approach-leak lane)" →
   "(the approach-leak lane, computed: PR #903/#904)". **Was UNDECLARED — a
   status-currency update, factually true (#903/#904 merged) and physics-neutral, but
   ruled text propagates byte-identically, so every delta must be enumerated.** It is
   hereby declared and stands.

## C2 (blocking, D2) — the corrected engine statement, RE-CORRECTED (residence)

The v2's engine paragraph placed all three amplitude definitions "in the same sum". The
accurate residence map (Tier-2-verified at merge commit `5e7f367a`):

- **Definition 1 (per-grade):** kernels built at `cosserat_field_3d.py:761-762`, applied
  in the saturated elastic sum at `:767-768`, inside `_energy_density_saturated`.
- **Definition 2 (aggregated normalized-L2):** `_reflection_density:486-488`; its
  `W_refl` term DOES enter the same saturated sum, at `:770`, at unit weight
  (`k_refl=1.0`, `:944`). The same formula appears independently at
  `_s11_density:409-413` — which feeds the SEPARATE S11 objective
  (`_total_s11:436-438` → `_val_and_grad_s11:800`), NOT the energy sum.
- **Definition 3 (sym-only strain + V²/V_SNAP², chirality-biased):** built at
  `:618-619`/`:680-681` with the chirality bias at `:624-625`/`:684-685`
  (`_reflection_density_asymmetric:573`, `_update_saturation_kernels:652`), consumed by
  `k4_cosserat_coupling.py:157` inside `_coupling_energy_total_asymmetric:128` — a
  DIFFERENT functional, and per its own docstring (`:114-116`) the DEFAULT under Phase 4
  (`use_asymmetric_saturation=True`).

The v2's conclusion is UNCHANGED and re-affirmed: the engine codes the saturation
amplitude three ways across two live functionals plus a separate objective; "the member
the engine actually codes" is over-broad; and the carve-out's structural receipt stands
(γ·W_κ never rides an ε-dependent kernel in the saturated elastic sum).

## C3 (advisory A1) — the test-pinning sentence, made exact

"`k_refl` is zeroed in the tests" is true at the two sites that isolate saturation but
false as a universal: `test_cosserat_field_3d.py:547` sets `k_refl=1.0` under
`use_saturation=True` (inequality assertion only, `:548`) and `:602` sets it to `1.0` in
the FD-gradient test (moduli zeroed). Accurate form: **the aggregated kernel is live in
two tests but only under inequality/FD-consistency assertions; no test discriminates the
members.** The load-bearing claim — no test pins the split — holds.

## C4 (advisory A9) — un-audited tag rider

The v2's routing paragraph cites "the substance-monism walk (framing note §5)" without
the UN-AUDITED tag its every other mention carries. The tag rides that mention too; in
citable ruling records the tag accompanies EVERY mention of walk-level material.

## C5 (advisory A6) — census numbers in R1/R2 are unpinned

The decision-batch record prints the lane-reported census figures (216/60, ~2,998,
~2,230) without a SHA pin while ruling that briefs must pin census numbers. Those figures
are hereby tagged QUOTED-FROM-LANE-REPORT, non-authoritative; the executing lane
re-derives at execution SHA (its brief already fences this).

## C6 (advisory A7) — "amorphous is retired" gains its scope word

R7's vocabulary fence retires "amorphous" in its **primary-lattice sense**
(`substrate-native-terminology.md:50`); the secondary-EMT-scale "amorphous network"
sense remains under the OPEN D3 adjudication and is not classified by R7. The pre-bond
rename census (follow-on brief item 7) must not touch D3-scoped sites.

## C7 (advisory A8) — a self-granted status, reclassified

R7's closing sentence ("the substance-level ('melt') law is hereby the program's named
deepest open object") is ORCHESTRATOR-FRAMING, not part of Grant's quoted GO. It stands
as a proposal pending Grant's word, not as a ruling.

## Routed elsewhere (same Tier-2 report)

A2 (the vacated-cite is a within-vs-across-grade misclassification, and the same
misread + drifted `:600` cite sits in canon at `trampoline-framework.md:255`) → Ax4
residence brief, dated scope update. A3 (wall-taxonomy §10.2 quotes the superseded v1
ruled text byte-identically; its "the ruled text above does NOT carry it" sentence is now
false) + A4 (five "engine actually codes" sites, `wall-taxonomy.md:528` live in a canon
table) + A5 (two of those are frozen result docs — surface-note pattern, not rewrite) +
A11 (docket fragments missing `### ENTRY` headers; gate warn-only) → doc-lane follow-on
brief, dated update. A10 noted: `verify-md-links` is warn-only for frozen/docket files —
green verify does not certify record cites; manual Tier-2 passes remain the certifying
instrument for records-class PRs.
