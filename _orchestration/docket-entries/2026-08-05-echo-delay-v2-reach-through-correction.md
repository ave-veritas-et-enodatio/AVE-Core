# Correction — echo-delay v2 fragment (orchestrator, 2026-08-05, post Tier-2 verify)

Corrections to `2026-08-05-echo-delay-v2-reach-through.md` (one-per-lane rule: corrections land
as this dated companion, the original is untouched):

1. The fragment's "Γ_in cannot converge" is SOFTENED to "Γ_in at a near-wall plane is not
   plane-invariant / ill-posed as posed" — the measured sequence is monotone-decreasing and
   consistent with a limit; only plane-dependence is proven.
2. FT-DISC: adjudicated by the orchestrator (fireability reading governs; the literal ≥0.02
   sub-clause is arithmetically unsatisfiable by construction — receipt in the result doc's
   review block). CFG-B certification STANDS; Grant may override.
3. FLAG-PLANE-RT option set extended to three (fixed-reference-impedance renormalization added).

**Propagation-citable delta (audit-landed, for the eventual propagation pass):**
`BIN-DISC`: NOT-ADJUDICATED (v1, PR #880) → **ADJUDICATED, FIRES** (v2, prereg `db98550b`), on
the UNCHANGED v1 criterion `abs(T_return^B − T_return^A) > tau_ring(M) at EVERY mass on the
frozen grid`; margins 38.57–43.21×; branch ratio 48.76–54.50; scope: FORK-3(b) is
TIMING-DISCRIMINABLE, no branch preferred, FLAG-ECO applies in full. v1's routed follow-on #1 is
DISCHARGED in full.
