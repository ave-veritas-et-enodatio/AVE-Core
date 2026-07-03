# RESULT — EM-readout Stage-1b (rework after the panel HOLD-POINT retraction)

**Status:** RUN-COMPLETE (revision round, panel items 1–7 + Grant cell-closure ruling folded in). **STAGE-1B VERDICT: [SECTOR-BUILT + MAXWELL-RECOVERED (VoK caveats characterized)] + [OBSERVABLE REBUILT — ARITHMETIC certified; the round-trip is an IDENTITY] + [STATIC-LINEAR-COLD CELL: CLOSED (Grant-ratified) on the tautology basis].** The blind global-sum observable is replaced by a LOCAL enclosed-charge profile; a mandatory positive control certifies its ARITHMETIC (a KNOWN charge is read back), **NOT** independent physical detection — the solve+readout is a mathematical identity `Q_enc(r) = Σ_Ω(b − mean)` (§2b, panel item 2). Grant ratified a CELL-scoped closure (§6): the **{static, LINEAR, cold, local-coupling, {∇×ω, ω}, this-operator-pair} cell is CLOSED** — no Link-counting in the static source profile of either tested axiom-native coupling; the verdict is a property of the ENGINEERING-CHOICE operator pair. **Explicitly NOT closed:** strain/S(A)-modulated couplings, self-consistent nonlinear statics, dynamics, topological-boundary, pairs (§6). The emergence-run for the other cells is chartered separately (the Y-redesign arc).
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
| **Observable rebuilt (Blocker-1)** | LOCAL `enclosed_charge_profile(r)` = Σ_Ω(∇·E), operator-consistent — but a ROUND-TRIP IDENTITY: Q_enc = Σ_Ω(b−mean) (item 2) |
| **CONTROL (Blocker-3, re-scoped item 2)** | round-trip **ARITHMETIC certified** — KNOWN +1 charge read back (+1.00); jellium prediction 0.4764 matches Q_enc(box/2)=0.4748; cg converged. A curl-TYPE-DRIVE control (NOT div-free — item 1) reads a non-plateau. Certifies arithmetic, NOT physical detection |
| ngspice cross-solve (Grant-directed) | **MATCH 2.5e-11** — solve_static == independent MNA/KCL (SPICE's math) + dense pseudo-inverse; ngspice NOT installed (named limitation) |
| Equation-audit gate (hardened r2, item 4) | **PASS** — 8 AXIOM / **11 ENGINEERING-CHOICE** / 3 FORBIDDEN; scans the LIVE import CLOSURE (13 modules, not a hardcoded 5); α-carriers in the closure honestly reported (6, incl. cosserat_field_3d); THIS-module α-clean; **runtime RHS bit-identical when Q_link stubbed to garbage** (the load-bearing guarantee, item 4d) |
| Winding readout | **GATED/UNBLINDED — Q_enc at enclosing r≥8 recorded (curl −1.11, ω −24.6), NO verdict authored by me below the cell-closure; the cell-scoped ruling is Grant's (§6)** |
| Mechanism claim (Blocker-2) | CORRECTED everywhere — "∇·(∇×ω)=0 identically" is FALSE (div∘curl RMS≈0.35 pointwise); the global-sum zero was readout antisymmetry, not a curl identity |

---

## 1. WHAT THE PANEL FOUND, AND WHY IT WAS RIGHT (re-verified before accepting)

I re-verified every blocker myself at the branch head before reworking (flag-don't-fix applies to panel claims too — but every finding held):

- **Blocker 1 (observable blind):** `np.sum(b_EM)` telescopes to ≈0 for ANY field on the closed periodic graph. Controls: random → −3.6e-15, constant → 0, and a **radial hedgehog (a genuinely divergent field) → machine-zero** as well — a real monopole reads the same 8.9e-16. (Item-3 correction: the earlier "max local \|div\|=22.5" figure came from an UN-normalized `pos−mean` hedgehog whose magnitude scales with box size; a physically-obvious UNIT radial hedgehog gives max local \|div\|≈1.3, matching the panel's construction. The qualitative claim — a genuinely divergent field reads machine-zero on the global sum — holds and is independently confirmed; the specific 22.5 number is demoted to qualitative prose.) The global sum was the wrong question in principle (periodic-graph total charge is FORCED zero by the jellium background). CONFIRMED.
- **Blocker 2 (false mechanism):** div∘curl on random ω is pointwise max≈1.4, RMS≈0.35 — NOT zero. The curl (1/deg) and div (½ face-average) are independent heuristics, not an adjoint/DEC pair. The zero was readout antisymmetry, not a curl identity. CONFIRMED.
- **Blocker 3 (no positive control):** the "magnetic dipole" existed only in comments. CONFIRMED.
- **Blocker 4 (uncommitted artifacts):** drive=ω, helicity, diamond-nullspace were not in committed code/JSON. CONFIRMED.

All four accepted; the [NON-EMERGENCE] headline was retracted (PR #477).

## 2. THE REBUILT OBSERVABLE + CONTROL — AND THE ROUND-TRIP IDENTITY (panel item 2)

The observable is now LOCAL and operator-consistent: `enclosed_charge_profile(r) = Σ_{u : |r_u − r_core| < r} (∇·E)[u]`, with `∇·E = +Lφ` (the discrete divergence of the SOLVER's own L — sign-corrected, MAJOR-c).

### 2b. THE ROUND-TRIP IDENTITY (load-bearing honesty correction — panel item 2, re-verified)

**Because `∇·E = Lφ` and `φ` solves `Lφ = (b − mean)`, the observable is a mathematical identity:** `Q_enc(r) = Σ_{u∈Ω(r)}(∇·E)[u] = Σ_{u∈Ω(r)}(b − mean)` to machine precision (re-verified: diff ~1e-9 for arbitrary b). **The solve+readout RE-READS the source RHS `b`** (jellium-corrected) over the enclosing node-set; it does **NOT** independently "detect" a field. Consequence, stated plainly:
- The positive control certifies the **ARITHMETIC** (a KNOWN point source `b=+δ` → `Σ_Ω(b−mean)=+1` near the core, minus the jellium `1−(4π/3)(r/box)³` → 0.476 at box/2, measured 0.4748 ✓), **NOT** "physical monopole detection." The earlier "PROVEN NON-BLIND detecting a real monopole" framing is softened accordingly.
- For the WINDING, `Q_enc(r) = Σ_Ω(∇·(drive))` under the two ENGINEERING-CHOICE non-adjoint operators (`_srs_curl_nodes` / `_srs_node_divergence`). **Any counting result is a property of THAT operator pair, not an axiom consequence.** This is exactly the tautology basis on which Grant ratified the cell-scoped closure (§6).

### 2c. The control's actual content
- KNOWN +1 point source → charge read back +0.9997 near the core; jellium prediction matches at box/2. `arithmetic_certified = True`, `cg_converged = True`.
- A curl-TYPE-DRIVE control (`b = ∇·(∇×ω_rand)`, seed committed) → a NON-plateau profile. **NOTE (item 1):** this control is **NOT divergence-free** — under the non-adjoint pair `∇·(∇×ω) ≠ 0` (panel RMS 0.352). It is labeled a *curl-type-drive* control, not a div-free control; the earlier "distinguishes a real monopole from a divergence-free field" claim is corrected.

What this establishes: the arithmetic round-trip is correct and the observable is not the blind global sum. What it does NOT establish: independent physical detection (there is none — it re-reads b).

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

- **Ledger reconciled (MAJOR-a + item 5):** every choice tagged — **8 AXIOM-DERIVED** (incl. the `b −= b.mean()` RHS jellium projection, TOPOLOGY-FORCED by the periodic-graph solvability Σb=0; ∇·E=+Lφ operator-consistent), **11 ENGINEERING-CHOICE** (½ face-average div weight, 1/deg curl norm, CG rtol, fit windows, acceptance bands, the imposed KNOWN source, the `φ−=mean` OUTPUT gauge, the winding-seed params, the radii-set + profile-center, the negative-control rng seed, the A-symmetrization — the false "0 ENGINEERING-CHOICE" is fixed), **3 FORBIDDEN-INSERTION** (𝒬·δ³, Gauss-enforced, helicity-as-source — all demonstrated absent). Dead `node_field_mag` deleted; `cg_info` exported + asserted for ALL solves.
- **Gate hardened round 2 (item 4):** (a) the scanned-module list is now derived from the **LIVE import CLOSURE** (13 modules — catches `cosserat_field_3d`, `constants`, `graded_vacuum_network`, `universal_operators` the hardcoded 5 missed); all forbidden source patterns ABSENT across the closure. (b) the allowlist is now **EXACT-MATCH** (the prefix regex that passed `source_from_Qlink`/`srcQ`/`b_EM_plus_Q` is closed); `unexpected_solve_sources=[]`. (c) the α-guard is extended to the closure + bare-call-args and honestly scoped: **α-carriers DO appear in the closure** (6, incl. `ALPHA@cosserat_field_3d`) — the gate does NOT claim the closure is α-free; it claims THIS module is α-clean (`this_module_alpha_clean=True`). (d) the **load-bearing guarantee — a RUNTIME INDEPENDENCE CHECK:** stubbing `compute_Q_link_srs` to return garbage (Q_link=999999) leaves the winding RHS `b_EM` **BIT-IDENTICAL** → **no integer/Link routes into the RHS by construction, name-independent** (`runtime_RHS_independent_of_Qlink=True`). **gate_passed=True** on this honest basis.
- **Un-riggability held TRUE by construction:** no 𝒬/ρ/helicity reaches any solve in any closure module; the runtime check proves the winding RHS does not depend on the Link integer.

## 6. THE STATIC-LINEAR-COLD CELL CLOSURE (Grant-ratified) + UNBLINDING + the continuation

### 6a. UNBLINDING acknowledgment (panel item 6)
The gated Q_enc profiles for both couplings are **committed → UNBLINDED**. Per pre-registration discipline, **no static-branch verdict bin authored after this point counts as pre-registered.** The static-local branch's adjudication therefore moved to the orchestrator + Grant level.

### 6b. THE CELL-SCOPED CLOSURE (Grant adjudicated 2026-07-03, verbatim "yes, i) ratify")
Grant ruled the static-cell adjudication (after a regime challenge). The verdict is **scoped to the CELL, not the branch**:

> **CLOSED = the {static, LINEAR, cold, local-coupling, {∇×ω, ω}, this-operator-pair} cell only.** Booked as: **no Link-counting in the static source profile of either tested axiom-native coupling.** The verdict is a **property of the ENGINEERING-CHOICE operator pair** (the tautology basis, §2b: `Q_enc = Σ_Ω(b−mean)` identically — the readout re-reads `∇·(drive)` under the two non-adjoint operators). Upgradeable to **theorem-grade for the whole curl class** via a DEC-operator derivation — a **sibling arc is now building exactly that** (cited as pending; not waited on).

**Explicitly NOT closed (stated per Grant's ruling):**
- **strain-dependent / S(A)-modulated couplings** — the electron's own T2 wall sits AT V_yield; the *cold* cell is not the object's home regime;
- **self-consistent nonlinear statics** — a found-not-imposed operating point is a legitimate instrument;
- **dynamical settling;**
- **topological-boundary;**
- **pairs.**

**I do NOT author any verdict language beyond this cell** (the branch adjudication is Grant's). The unblinded Q_enc values (curl −1.11, ω −24.6 at r≥8) are recorded as data under the tautology caveat; they are NOT interpreted as an emergence result.

### 6c. The continuation (chartered separately — NOT scoped into here)
The **Y-redesign arc** (both instruments — the strain/S(A)-modulated and self-consistent-nonlinear-statics couplings) is chartered as a separate epic; this doc references it as the continuation and does **not** scope-creep into it. The other pre-registered cells remain: (Y) dynamical/Ax4-rectified, (Z) topological-boundary, **(W) two-winding PAIR** (the field BETWEEN two windings — the pair-interaction clm-wcoul2 measures in the ω-sector).

## 7. DISCIPLINE LEDGER

- **`verify-before-cite` / flag-don't-fix on panel claims (BOTH panel rounds):** every blocker AND every revision-round item re-verified by me before acceptance — the round-trip identity (Q_enc=Σ_Ω(b−mean), item 2), the closure α-imports (cosserat_field_3d, item 4a), the allowlist evasion (item 4b), the hedgehog 22.5-vs-1.3 (item 3) all held; the code was corrected accordingly. Where I found the ngspice 50% mismatch, I DIAGNOSED it (gauge/RHS difference) rather than accept a false "solver disagreement" — matched to 2.5e-11.
- **Rule 11 (honest closure):** the [NON-EMERGENCE] headline was RETRACTED (not defended); the "PROVEN NON-BLIND detecting a monopole" framing was SOFTENED to "arithmetic certified" once the round-trip identity was shown. The panel caught real errors; the reaction was retraction + honest re-scope, not a rescue.
- **Rule 10 (empirical driver):** the positive control, the runtime-independence check, and the ngspice cross-solve are integrator-time checks the blind observable lacked.
- **Un-riggability (charter §3):** held TRUE by construction across the 13-module LIVE closure; the runtime check proves the winding RHS is bit-identical when the Link reader is stubbed to garbage (no integer routes into the RHS); Gauss diagnostic-only; the answer was NOT back-fitted.
- **`consistency-vs-emergence`:** infrastructure validated; the CELL closure is Grant-ratified (§6b), scoped to {static,linear,cold,local,{∇×ω,ω},this-operator-pair} on the tautology basis; NOT extended to other cells; NO chord/emergence claim minted.
- **Scope discipline (lane):** I authored the cell-scoped closure Grant ratified, and did NOT author branch-level verdict language or scope-creep into the Y-redesign continuation (§6c) — that arc is chartered separately.

---

> **STAGE-1B COMPLETE (revision round landed).** The STATIC-LINEAR-COLD CELL is CLOSED (Grant-ratified §6b, tautology basis); the emergence-run for the OTHER cells (strain/S(A)-modulated, nonlinear-statics, dynamics, boundary, pairs) is the separately-chartered Y-redesign continuation (§6c). The observable is rebuilt (arithmetic certified, round-trip identity §2b); the gate is hardened on the live import closure with a runtime independence guarantee (§5). Corpus updates (the §8 un-conflation manual entries) remain surfaced for the auditor to land. No emergence-run and no branch-level verdict authored here.
