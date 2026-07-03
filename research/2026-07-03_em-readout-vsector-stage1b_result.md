# RESULT — EM-readout Stage-1b (rework after the panel HOLD-POINT retraction)

**Status:** RUN-COMPLETE. **STAGE-1B VERDICT: [SECTOR-BUILT + MAXWELL-RECOVERED (VoK caveats honestly characterized)] + [OBSERVABLE REBUILT & PROVEN NON-BLIND] + [EMERGENCE TEST GATED — NOT run].** The blind global-sum observable is replaced by a LOCAL enclosed-charge profile that is proven (via a mandatory positive control) to detect a real monopole and discriminate it from a divergence-free field. The emergence interpretation is HELD per the panel PROCESS directive — it runs only after the hardened-audit review.
**Supersedes** the retracted Stage-1 result (`..._stage1_result.md`, corrected in PR #477). This doc records the rework.
**Prereg (FROZEN + panel-retraction addendum):** [`2026-07-03_em-readout-vsector-stage1_prereg.md`](2026-07-03_em-readout-vsector-stage1_prereg.md).
**Charter:** `_orchestration/2026-07-03_em-readout-derivation-charter.md`. **Grant-CONFIRMED target-(1).**
**Branch:** `analysis/em-readout-stage1b` (off the PR #477 retraction branch, off `origin/main`). NO self-merge.
**Driver:** [`src/scripts/vol_2_subatomic/em_readout_vsector_transducer.py`](../src/scripts/vol_2_subatomic/em_readout_vsector_transducer.py). **Results JSON:** `..._results.json`. **ngspice .cir:** `em_readout_srs_poisson_crosscheck.cir`.
**Classification (`consistency-vs-emergence`):** channel + observable = infrastructure (validated); emergence = GATED (no verdict). NO chord/emergence claim minted.

---

## 0. THE ONE-SCREEN SUMMARY (all re-verified this session)

| Deliverable | Result |
|---|---|
| Carrier finding (committed, Blocker-4 fix) | diamond-K4 TETRA_OFFSETS BIPARTITE (nullspace dim 12, static solve max\|φ\|=3.4e16 ill-posed); srs (z=3) WELL-POSED (nullspace=1). `carrier_diagnostics()` |
| VoK (a) zero-source floor | PASS — φ≡0, E≡0 exactly |
| VoK (b) Coulomb Green's fn (jellium-honest, MAJOR-d) | PASS — jellium-corrected A/r fit: **A=0.459, R²=0.9966**; bare near exponent −1.47 reported as a bare fit (the finite-box parabola bends it), spec-deviation (point-source ≡ boundary-flux by div-thm) recorded |
| VoK (c) superposition + Gauss counting | PASS — field linearity exact; LOCAL enclosed charge 1 src→1.00, 2 src→1.96 (ratio 1.96) |
| **Observable rebuilt (Blocker-1)** | LOCAL `enclosed_charge_profile(r)` = Σ_Ω(∇·E), operator-consistent |
| **POSITIVE CONTROL (Blocker-3)** | **VALID** — KNOWN +1 monopole reads Q_enc[0]=**+1.00** through the identical path; curl(div-free) reads structured/no-plateau → discriminates=True |
| ngspice cross-solve (Grant-directed) | **MATCH 2.5e-11** — solve_static == independent MNA/KCL (SPICE's math) + dense pseudo-inverse; ngspice NOT installed (named limitation) |
| Equation-audit gate (hardened, MAJOR-a/b) | **PASS** — 8 AXIOM-DERIVED / **6 ENGINEERING-CHOICE** (was falsely 0) / 3 FORBIDDEN-rejected; scans ALL 5 solve-path modules; alpha guard CONSUMED (alpha_clean=True) |
| Winding readout | **GATED — Q_enc recorded (curl[0]=−0.095, ω[0]=−1.068), NOT interpreted** |
| Mechanism claim (Blocker-2) | CORRECTED everywhere — "∇·(∇×ω)=0 identically" is FALSE (div∘curl RMS≈0.35 pointwise); retracted in code + docs |

---

## 1. WHAT THE PANEL FOUND, AND WHY IT WAS RIGHT (re-verified before accepting)

I re-verified every blocker myself at the branch head before reworking (flag-don't-fix applies to panel claims too — but every finding held):

- **Blocker 1 (observable blind):** `np.sum(b_EM)` telescopes to ≈0 for ANY field on the closed periodic graph. Controls: random → −3.6e-15, constant → 0, **radial HEDGEHOG (max local \|div\|=22.5) → 1.7e-13**. A real monopole reads the same 8.9e-16. The global sum was the wrong question in principle (periodic-graph total charge is FORCED zero by the jellium background). CONFIRMED.
- **Blocker 2 (false mechanism):** div∘curl on random ω is pointwise max≈1.4, RMS≈0.35 — NOT zero. The curl (1/deg) and div (½ face-average) are independent heuristics, not an adjoint/DEC pair. The zero was readout antisymmetry, not a curl identity. CONFIRMED.
- **Blocker 3 (no positive control):** the "magnetic dipole" existed only in comments. CONFIRMED.
- **Blocker 4 (uncommitted artifacts):** drive=ω, helicity, diamond-nullspace were not in committed code/JSON. CONFIRMED.

All four accepted; the [NON-EMERGENCE] headline was retracted (PR #477).

## 2. THE REBUILT OBSERVABLE + POSITIVE CONTROL (the core fix)

The observable is now LOCAL and operator-consistent: `enclosed_charge_profile(r) = Σ_{u : |r_u − r_core| < r} (∇·E)[u]`, with `∇·E = +Lφ` (the discrete divergence of the SOLVER's own L — sign-corrected, MAJOR-c). By the discrete divergence theorem of L this equals the enclosed charge inside radius r (minus the growing jellium background).

**The mandatory positive control (Blocker-3) — the observable is PROVEN non-blind:**
- KNOWN +1 point source → Q_enc[0] = **+0.9997** (rises to +1 at the core, slow jellium decay to +0.47 at box edge). The observable reads a real monopole through the IDENTICAL solve+diagnostic path.
- A divergence-free field (curl of random ω) → Q_enc = {+0.62, −0.89, +1.68, +2.78, ...} — STRUCTURED, no +1 plateau. The observable DISCRIMINATES monopole from non-monopole.
- `observable_valid = True`.

This is exactly what the blind global-sum could not do: distinguish a real monopole from a divergence-free field.

## 3. VALIDATE-ON-KNOWN (honestly characterized, MAJOR-d)

- **(a)** zero-source floor: exact.
- **(b)** the Coulomb Green's function is now reported honestly: the **bare** near-field power-law exponent (−1.47) is a bare fit that the periodic finite-box parabola bends; the **certification** is the jellium-corrected model φ(r) = A/r + c₀ + c₂r² → **A=0.459 (the Coulomb coefficient), R²=0.9966**. The spec-deviation (the frozen prereg §5(b) said "boundary flux on a closed surface"; this uses the equivalent KNOWN point source — the point-charge Green's function IS the 1/r Coulomb test, and the two are the same Poisson Green's function by the divergence theorem) is RECORDED, not silent.
- **(c)** superposition: field linearity exact; the LOCAL enclosed charge scales 1 src → 1.00, 2 src → 1.96. Honest caveat: for a KNOWN imposed source, ∇·E = +(source − mean) by construction of the solve — this confirms the discrete Gauss theorem of L; the NON-trivial emergence question (does the WINDING source such a ∇·E) is the GATED test.

## 4. THE ngspice CROSS-SOLVE (independent-solver VoK, Grant-directed)

A resistor network with unit conductances IS the srs graph Laplacian (KCL at each node: Σ(V_u−V_v)/R = I ⇒ L·V = I). SPICE's MNA is exact by construction (no hand-rolled operator), so it is the independent check the panel's findings demand.

- `solve_static` matches the independent grounded-MNA elimination AND a dense pseudo-inverse (both SPICE's own KCL math) to **2.53e-11** on the SAME physical problem (same jellium-corrected RHS).
- **Honest diagnosis en route:** a naive grounded +1A-source/1-sink `.cir` differs from the mean-zero/jellium solve by EXACTLY 50% — a known uniform-background GAUGE difference (a different physical BC: Dirichlet sink vs periodic uniform background), NOT a solver bug. The certification uses the jellium-consistent RHS; documented in `cir_note`.
- **Named limitation (surfaced, not skipped):** ngspice is NOT installed in this environment, so the external-binary leg is a NAMED LIMITATION; the `.cir` is emitted (ngspice-runnable when installed), and the independent MNA math IS run and matches.

## 5. THE HARDENED EQUATION-AUDIT (reconcile-not-declare, MAJOR-a/b)

- **Ledger reconciled (MAJOR-a):** every choice tagged — **8 AXIOM-DERIVED** (incl. the `b −= b.mean()` jellium projection, TOPOLOGY-FORCED by the periodic-graph solvability Σb=0; ∇·E=+Lφ operator-consistent), **6 ENGINEERING-CHOICE** (½ face-average div weight, 1/deg curl norm, CG rtol, fit windows, acceptance bands, the imposed KNOWN source — the false "0 ENGINEERING-CHOICE" is fixed), **3 FORBIDDEN-INSERTION** (𝒬·δ³, Gauss-enforced, helicity-as-source — all demonstrated absent). The b_EM row no longer cites the false "∇·(∇×ω)=0".
- **Gate hardened (MAJOR-b):** scans EVERY ave-module in the solve import path (`srs_cage_winding`, `charge_quantization`, `chiral_lattice`, `native_cage_imex`) — not self-scoped — for forbidden source patterns; all ABSENT. The `_FORBIDDEN_ALPHA` guard is now CONSUMED (was dead code): no α-carrier is imported/used-as-value in the coupling path; `alpha_clean=True`. Every `solve_static` source is a labeled KNOWN or the emergent b_EM (`unexpected_solve_sources=[]`). **gate_passed=True.**
- **Un-riggability held TRUE by construction:** no 𝒬/ρ/helicity reaches any solve, in any scanned module. The helicity is measured for the audit only, never fed to `solve_static`.

## 6. WHAT IS GATED (the emergence test — NOT run)

Per the panel PROCESS directive (the original emergence run predated the audit function — the charter §3.3 gate was a self-audit after the fact, this time enforced): Stage-1b ENDS at the rebuilt observable + positive control + VoK + ngspice cross-solve + hardened audit + this doc, and STOPS. The winding readout is run as a GATED diagnostic (both couplings committed; the LOCAL Q_enc recorded — curl[0]=−0.095, ω[0]=−1.068 — NON-trivial, unlike the blind global sum) but **emits NO emergence verdict.** The emergence test runs ONLY after the panel + orchestrator review this hardened gate.

**The pre-registered fork for the future emergence run** (from the retracted §6, KEEP-BOTH, with lane W added): (X) FINAL negative — a lone winding has no electric monopole (Coulomb = pair/boundary property); (Y) dynamical/Ax4-rectified coupling; (Z) topological-boundary flux-quantization; **(W) NEW — the two-winding PAIR construction** (the field BETWEEN two windings, the pair-interaction the corpus's clm-wcoul2 already measures in the ω-sector). The emergence run measures the LOCAL Q_enc profile of each and interprets against these.

## 7. DISCIPLINE LEDGER

- **`verify-before-cite` / flag-don't-fix on panel claims:** every blocker re-verified by me before acceptance; all four held (§1). Where I found the ngspice 50% mismatch, I DIAGNOSED it (gauge/RHS difference) rather than accept a false "solver disagreement" — the honest fix matched to 2.5e-11.
- **Rule 11 (honest closure):** the [NON-EMERGENCE] headline was RETRACTED (not defended); the panel caught a real error and the reaction was retraction + rebuild, not a rescue.
- **Rule 10 (empirical driver):** the rebuilt observable's positive control + the ngspice cross-solve are integrator-time checks that the blind observable lacked.
- **Un-riggability (charter §3):** held TRUE by construction across all 5 scanned modules; no 𝒬/helicity/ρ reaches any solve; Gauss diagnostic-only; the answer was NOT back-fitted.
- **`consistency-vs-emergence`:** infrastructure validated; emergence GATED, no verdict, no claim minted.
- **PROCESS:** Stage-1b STOPS before the emergence run; the emergence gate is now enforced BEFORE the run (not a self-audit after).

---

> **STAGE-1B COMPLETE. HOLD-POINT.** The emergence test is GATED until the panel + orchestrator review this hardened audit. Final message reports the rebuilt-observable + positive-control numbers, the ngspice cross-check, the hardened-audit output, the revised verdict, and the remaining gated fork (X/Y/Z/W). Corpus updates (the §8 un-conflation manual entries) remain surfaced for the auditor to land.
