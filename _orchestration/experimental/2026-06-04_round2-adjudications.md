# Round-2 Hardening — Adjudication Ledger (2026-06-04)

**Companion to** the epic spine [`2026-06-03_experimental-protocol-revamp-orchestration.md`](../2026-06-03_experimental-protocol-revamp-orchestration.md) §12 (round-2 verdicts). The spine records *what happened*; this ledger records *why each decision was made* — each round-2 adjudication, EE-mapped (`ave-ee-first-mapping`) + skill-disciplined, with Grant's decision + execution pointer. This is **Layer 2** (reasoning) of the orchestration-documentation architecture; the corpus deltas (Layer 3) are the *result* of each adjudication, the audit tags (Layer 4) the ancestry, the capstone the closing narrative.

**Format per entry:** substrate picture → EE map → means-test → skills applied → decision (Grant) → execution pointer.

## Index

| # | Item | EE map (crux) | Decision | Status |
|---|---|---|---|---|
| 1 | HOPF reciprocity | Pasteur (reciprocal, P-odd) vs Tellegen (non-recip, T-odd) | reciprocal-Pasteur at linear → C3/C4 retire labels; ADD 2-port reciprocity sweep | **AGREED** 2026-06-04 |
| 2 | Cleave CPD / SM≠0.0 | Kelvin probe / patch potentials (CPD real, gap-dep ∝1/g²) | confirm + propagate SM≠0.0 + gap-sweep | **AGREED** 2026-06-04 |
| 3 | per-node-conflation sweep | series-cell voltage division (V_yield is per-node, not terminal) | scoped sweep, inventory-first; PONDER-05 carve-out | **AGREED** 2026-06-04 |
| 4 | constants.py cite content-anchor | N/A (tooling, not physics) | convention + ξ_topo lockstep + head-sweep folded; informal tail | **AGREED** 2026-06-04 |
| 5 | birefringence-e4 index-convention | permittivity-depth (1−S) mislabeled as index-shift (√S−1); √ε factor | correct clm-pp3qwf + E²/E⁴ reframe (auditor) | **SURFACED** 2026-06-04 (pending) |

---

## §1 — HOPF reciprocity  [AGREED 2026-06-04]

**Decision context.** HOPF round-2 (`analysis/2026-06-04-hopf-round2-chiral-counterfactual`, `d240d70`) found C3 (medium-independence) + C4 (enantiomer sign-flip) form-shared with classical reciprocal chiral media; verdict PARTIAL (chirality channel survives only as non-reciprocity, above-yield). The call: is AVE's chirality reciprocal-Pasteur (→ C3/C4 retire their "AVE-DISTINCT" labels) or does it inherit *linear* non-reciprocity (→ legs partially stand)?

**Substrate picture.** Handed (parity-odd, P-odd) vs spinning (time-reversal-odd, T-odd). Reciprocity is a T-symmetry statement: a passive medium is non-reciprocal only with a frozen T-odd order.

**EE map** (`ave-ee-first-mapping`, constitutive-level):

| Candidate | EE device | Constitutive | Symmetry | Reciprocal? |
|---|---|---|---|---|
| Sugar-water / Pasteur | helical antenna, twisted-pair, optical-activity cell | D = εE + iξB | P-odd, T-even | YES (S₂₁=S₁₂) |
| Ferrite isolator / Tellegen | circulator, Faraday rotator | +T-odd magnetoelectric | T-odd | NO (S₂₁≠S₁₂) |

Plumber's-eye: a ferrite isolator only works *because of the magnet*. Remove the static B-bias and a passive handed structure cannot be a one-way valve — Lorentz reciprocity forbids it without a frozen T-odd order.

**Means-test.** (a) Canonical chiral dispersion ω²=c²k²∓γ_c k keys to *handedness*, not direction (k→−k) → P-odd → reciprocal Pasteur (own modeling maps to a Pasteur ξ, `AVE-HOPF/docs/analysis/2026-05-04_tool_agreement_and_ave_modeling.md:82`). (b) The one frozen T-odd order is Ω̂_freeze (cosmic, ~H₀ ~ 10⁻¹⁸ s⁻¹) → bench non-reciprocity ~10⁻¹⁸, unmeasurable. (c) The metamaterials-designbox zero-magnet non-reciprocity (|Γ_L|≈0.519 ≠ |Γ_R|≈0.553) is produced by thixotropic hysteresis = memristive T-breaking = **above-yield**. → at the $123 linear bench (r ~ 10⁻¹⁸, 13 OOM below yield), the vacuum is sugar-water (reciprocal Pasteur) to any measurable precision.

**Skills applied.** `consistency-vs-emergence` (C3/C4 = consistency-class — AVE *reproduces* optical activity — NOT emergence → "AVE-DISTINCT" labels miscategorized); `ave-discrimination-check` (only zero-field non-reciprocity is classically-forbidden, and it's above-yield); `pre-test-physics-check` (the sugar-vs-ferrite plumber question surfaced to Grant).

**Decision (Grant AGREED 2026-06-04).** (a) reciprocal-Pasteur at the linear bench → §6.2 C3/C4 "AVE-DISTINCT" labels **retire to consistency-class**; (b) **ADD** the 2-port S₂₁-vs-S₁₂ reciprocity sweep to HOPF-02a (two-sided, ~$0 extra: power-independent + non-magnetic imbalance > 0.05 dB = major AVE-distinct find; null = clean retire of the chirality channel at the linear scale).

**Execution (pending merge-call).** The round-2 branch already *proposes* the §6.2 relabel (flag-don't-fix); on merge it lands + the reciprocity-sweep leg is added. New `translation-circuit.md §4` row (Pasteur-reciprocal vs Tellegen-above-yield correspondence). `closure-roadmap §0.5` row. Sequenced after the auditor-gate.

---

## §2 — Cleave CPD / SM≠0.0  [AGREED 2026-06-04]

**Decision context.** Cleave round-2 (`analysis/2026-06-04-cleave-round2-smcounterfactual`, `76f66b9`) found round-1's foundational claim *"Standard EM predicts 0.0 mV"* FALSE — contact-potential-difference (CPD) gives a non-zero, polarity-ODD, ~21%-of-floor charge that form-shares with the ξ_topo floor on magnitude + polarity. Cure: CPD is gap-DEPENDENT (∝1/g²), the floor is gap-INDEPENDENT → a gap-sweep separates them (4-corner symmetry discriminator). The call: confirm the correctness finding + authorize the SM≠0.0 propagation + adopt the gap-sweep leg.

**Substrate picture.** The Cleave electrometer reads the topological linking charge 𝒬 = ξ_topo·x = (e/ℓ_node)·x on a floating electrode as the PZT displaces it. Question: is the classical (SM) background really 0.0?

**EE map** (`ave-ee-first-mapping`). A moving floating electrode with a work-function difference is a **Kelvin probe / vibrating capacitor**: Q_CPD = C(x)·V_CPD → dQ/dx = V_CPD·dC/dx. Canonical EE instrument (scanning Kelvin probe, vibrating-reed electrometer). CPD + surface **patch potentials** are THE dominant systematic in precision electrostatic / Casimir / Kelvin-probe metrology — never exactly zero in a real bench. → round-1's "SM = 0.0" holds ONLY for a perfectly equipotential, single-work-function, patch-free surface; in any real bench it is non-zero.

**Means-test (the cure).** Parallel-plate C ∝ εA/g → dQ_CPD/dx ∝ V_CPD/g² → **gap-dependent**. The ξ_topo floor = e/ℓ_node, a pure constant → **gap-independent**. A ≥4× gap-sweep: CPD drops ∝1/g²; floor unchanged. ✓ Separated. The other classical fakers fail other corners: electrostriction/flexo/secondary-piezo are even-in-drive-V (removed by polarity-reversal at *any* magnitude); tribo is decaying (removed by time-gating). NO single classical mechanism fakes all 4 corners {linear ∧ polarity-odd ∧ material-indep ∧ gap-indep}.

**Skills applied.** `ave-audit-of-audit` (verified the CPD claim against the geometry — it is settled EE/metrology, the dominant Casimir/Kelvin-probe systematic; finding SOUND); `consistency-vs-emergence` (the 4-corner floor = Ax2 emergence; CPD/patch = classical-consistency background — the correction correctly separates them); `ave-discrimination-check` (moves the discriminator from P1 "presence-of-charge" — which CPD fakes — to the 4-corner symmetry signature, which it cannot); `ave-walk-back` (SM≠0.0 propagation, sites below).

**Located propagation sites** (`verify-before-cite`): `project-cleave-01.md:22` ("separating two uncharged plates in hard vacuum generates exactly zero charge"), `:44` ("Standard EM predicts $0.0$ mV" — the agent's "L44"), `:65` ("0.0 mV observed"); `research/2026-06-03_topological-charge-occupation-robustness.md:95` ("vs SM's 0.0 mV in clean vacuum"); Femto `hardware/TEST_PROCEDURE.md` (agent-corrected locally). The agent's cited "AVE-Core Phase-3 prereg §4 (liberates no net charge)" was NOT located by grep in AVE-Core `research/` — pin at execution (may be the Femto-side prereg, cross-repo).

**Flag for auditor (not Grant's intuition call).** The floor's measured VOLTAGE (mV) is gap-independent only at FIXED C_in (readout capacitance) — the gap-sweep must hold C_in fixed (or account for it), per the occupation-robustness framing (`:95` "hold C_in fixed and read the floor"). Protocol-design subtlety; does not change the adjudication.

**Decision (Grant AGREED 2026-06-04).** Confirmed the CPD correctness finding (SM≠0.0) + the gap-sweep cure; authorized propagating the correction to the located sites; adopt the gap-sweep + 4-corner framing as the canonical Cleave discriminator. (Settled EE/metrology; STRENGTHENS Cleave: magnitude argument → symmetry argument.)

**Execution (on agreement).** Propagate SM≠0.0 to the 4 located sites (per `ave-walk-back`, corrected statement: *"the polarity-odd, gap-INDEPENDENT component is classically 0.0; the raw vacuum charge is not — CPD gives a polarity-odd, gap-dependent term"*); the round-2 branch's TEST_PROCEDURE edit lands on merge; new `translation-circuit.md §4` row (CPD ↔ Kelvin probe / patch potentials); `closure-roadmap §0.5` row. Sequenced after the auditor-gate.

---

## §3 — Per-node-V_yield / apparatus-voltage conflation sweep  [AGREED 2026-06-04]

**Decision context.** Over-determined: IVIM (`c3fdb53`) + Q-G42 (`fdd88c3`) round-2 BOTH rooted their feasibility-kills in the same error — reading apparatus (gap) voltage as if it were the per-node V_yield. Flagged BLOCKING in epic §10; round-2 surfaced 8+ verbatim sites. The call: run the corpus-wide re-scope now, or keep parked?

**Substrate picture.** V_yield is a PER-NODE quantity — the yield voltage across ONE lattice cell (ℓ_node = 0.386 pm). Saturation A = E_local·ℓ_node/V_yield is a per-cell phenomenon. The conflation reads A = V_apparatus/V_yield (whole-gap voltage / per-node yield), off by d_gap/ℓ_node ≈ 2.6×10⁸.

**EE map** (`ave-ee-first-mapping`, distributed-element). A vacuum gap is a SERIES STACK of N = d_gap/ℓ_node ≈ 2.6×10⁸ distributed LC cells (the corpus's own "R_H/ℓ_node cells along a distributed transmission line" framing). The voltage across ONE cell = V_apparatus/N. Saturation/breakdown is PER-CELL. The conflation compares the WHOLE-STACK voltage to a SINGLE-CELL rating — a series-string voltage-division error (like asking "will this cap break?" by comparing the voltage across a 10⁸-cap series string to one cap's rating).

**The seductive trap.** V_YIELD ≈ 43.65 kV (canonical = √α·V_SNAP) numerically LOOKS bench-reachable (43 kV is achievable!) — but it is the voltage across ℓ_node = 0.386 pm, i.e. the yield FIELD E_YIELD = V_YIELD/ℓ_node ≈ 1.13×10¹⁷ V/m. Applying 43 kV across a 100 µm gap gives only 4.4×10⁸ V/m → A ≈ 3.9×10⁻⁹ (matches both round-2 agents). The 43.65 kV coincidence is why this is "the most common Vol 4 reading error" (`claim-quality.md:51`).

**Means-test.** The corpus's own distributed-TL model (R_H/ℓ_node cells; Machian-G = TL input impedance) IS the per-cell framework. The conflated camp violates the corpus's own model → the honest camp (per-node) is canonical-consistent. **Physics SETTLED** — not a coin flip; the real call is SCOPE / blast-radius.

**Sites** (round-2 inventory, full enumeration pending): conflated camp — `vacuum-impedance-mirror.md` (IVIM-rescoped already), `measurement-hierarchy-snr.md:66`, `universal-saturation-kernel-catalog.md:72`, `translation-circuit.md:111/191/481`, `op14-local-clock-modulation.md:106`, `divergence-test-substrate-map.md:126/466`, `17_noise_floor_boundary.tex:84`. Honest camp (template) — Q-G42, `trampoline-framework.md:439`, `claim-quality.md:51/393`.

**Skills applied.** `ave-sweep-audit` (this IS the N>10 mechanical-sweep class — scope-bound, class-taxonomy, honest-camp template, batch + auditor + closure-roadmap); `ave-walk-back` (each conflated site = a per-node re-scope); `consistency-vs-emergence` (the PONDER-05 27.4% ε-collapse vacuum-vs-material question — vacuum kernel = emergence, or quartz electrostriction = material-consistency background? — is a SEPARATE adjudication, carved out, NOT folded into this sweep); `substrate-native-check` (saturation lives at the node/cell scale).

**Blast-radius caution.** The sweep may deflate kernel-MAGNITUDE headlines beyond IVIM/Q-G42 (anywhere the kernel was read at apparatus scale). The SIGN-based + zero-free-param discriminators (Q-G42 sign, Cleave geometry) are UNAFFECTED. → recommend INVENTORY-FIRST (read-only blast-radius report) before any leaf is edited.

**Decision (Grant AGREED 2026-06-04).** (a) Authorized the scoped per-node-conflation sweep — executed INVENTORY-FIRST (read-only enumeration of all conflated sites + what each correction deflates), surfaced for review BEFORE any leaf is touched, then batch re-scope with the honest-camp template, auditor-gated. (b) PONDER-05 vacuum-vs-material carved out as a SEPARATE consistency-vs-emergence adjudication.

**Execution (on agreement).** Phase 1 = read-only inventory sweep (enumerate universe, class-taxonomy {conflated / honest / borderline}, blast-radius per site) → surface to Grant. Phase 2 (on blast-radius review) = batch re-scope, auditor-gated, `closure-roadmap §0.5`. PONDER-05 vacuum-vs-material = separate adjudication doc.

---

## §4 — constants.py citation content-anchoring (ξ_topo + general)  [AGREED 2026-06-04]

**Decision context.** Cleave round-2 F-R2-2: `XI_TOPO` is cited at `constants.py:246` but has drifted to `:251` (verified; `:205` is now `ALPHA_COLD`). Recurring — the §9 flag-don't-fix queue already logged a ":205→:246" drift. The call: how to fix durably?

**EE map: N/A.** This is citation-tooling hygiene, not a substrate-physics adjudication — `ave-ee-first-mapping` explicitly does not fire on tooling/framing. (ξ_topo's *physics* is already EE-canonical: e/ℓ_node = the charge-per-length electromechanical transduction constant, `clm-fy05jc`. The question here is only how to CITE it.) Recognizing when EE-mapping does NOT apply is part of "apply relevant skills."

**Skills applied.** `verify-before-cite` (line-number cites to a growing file are inherently fragile — they go stale on every insertion above them); `ave-sweep-audit` (the bulk fix is a mechanical sweep — but Class-C cosmetic, so opportunistic, not big-bang); `ave-evidence-framing-discipline` (honest scope below — it is NOT "a few sites").

**Scope (honest — bigger than first framed).** Immediate ξ_topo lockstep: 3 located `:246` cites (`2026-06-04_alpha-class2-bijection-result.md:169`, `2026-06-03_topological-charge-occupation-robustness.md:20` + `:120`) + the Femto `:205` cite → re-point to `XI_TOPO` / `:251`. But the GENERAL exposure is large: **~100+ `constants.py:NNN` line-number cites corpus-wide**, every one drift-exposed (`:133` (α) has 10 cites, `:79` 7, `:619` 7, `:432`/`:333`/`:194` 6 each). 52 docs already cite XI_TOPO by symbol (the good, stable pattern) — the corpus is MIXED.

**Precedent.** Content-anchoring is already established corpus practice: `ff9a2b1a` + `d9d33d00` (double-slit-ee) "content-anchor volatile citations (was stale 'line 139' post-merge)."

**Decision (Grant AGREED 2026-06-04).** (a) Adopt **content-anchoring as the convention** for constants.py cites — cite the symbol (`XI_TOPO`), not the line (formalize the `ff9a2b1a` practice; new cites symbol-anchored). (b) Immediate lockstep: fix the 3–4 ξ_topo stale cites. (c) **Fold the high-traffic head-sweep** (~7 lines ≥5 cites: `:133` α, `:79`, `:619`, `:432`, `:333`, `:194`, `:78` — ~47 cites, ~50% of exposure) into the lockstep — these are where one line-move cascades. The scattered tail (~50 singletons) is **informal/self-healing** (a stale singleton is a 10-sec re-grep; no hook/tracker built — that machinery is overkill for cosmetic debt). Rationale: opportunistic only works with a trigger+tracker, which isn't worth building here; the honest version is head-now + informal-tail.

**Execution (on agreement).** Lockstep ξ_topo + `:133` now (rides with the #3 inventory pass — overlapping files); convention noted in contributor guidance; bulk fix opportunistic. `closure-roadmap §0.5` row.

---

## §5 — vacuum-birefringence-E4 index-convention (δn = −A²/4 vs "Δn" = +A²/2)  [SURFACED 2026-06-04 — pending Grant]

**Decision context.** IVIM round-2 flagged a cross-leaf inconsistency: `vacuum-impedance-mirror.md` gives δn ≈ **−A²/4** while `vacuum-birefringence-e4.md` (clm-pp3qwf) + `divergence-test-substrate-map.md:63` give "Δn" ≈ **+A²/2** — same E-field family, but factor-2 AND sign differ. The call: which is right, and how to reconcile?

**Hypothesis revised (worked-adjudication discipline — `ave-discrimination-check` "don't anchor on first-plausible").** My first read was "different quantities — absolute index vs two-channel birefringence, just disambiguate." **Reading the actual e4 leaf falsified that.** The e4 leaf literally defines `Δn_eff = 1 − √(1 − (E/E_yield)²)`. That is **1 − S(A)**, the *permittivity saturation depth*, NOT a refractive index shift.

**EE map** (`ave-ee-first-mapping`): n = √(ε_eff μ_eff / ε₀μ₀); for ε-only modulation, **n = √(ε_eff/ε₀) = √S**. The saturation kernel S = √(1−A²) ≈ 1 − A²/2, so:
- permittivity depth: `1 − S ≈ +A²/2` ← what the e4 leaf computed and mislabeled "Δn_eff".
- **actual index shift**: `δn = √S − 1 = (1−A²)^¼ − 1 ≈ −A²/4` ← the mirror leaf's value, **correct**.
- ratio (1−S)/δn ≈ (A²/2)/(−A²/4) = **−2** → *exactly* the agent's "factor-2 + sign". The factor-½ is the √ in n=√ε (the EE wave-speed/index identity); the sign is depth (1−S, positive) vs shift (√S−1, negative, the vacuum softens → index drops). The e4 leaf **forgot the √**.

**Secondary issue.** The e4 leaf's prose ("the optical shift is driven by an **E⁴** term; if the slope stays E², AVE is falsified") is sloppy: 1−S ≈ A²/2 + A⁴/8 is **E²-leading**, same leading order as QED's Euler-Heisenberg. The AVE-distinct signature is the **E⁴+ DEVIATION** (saturation-arc steepening as E→E_yield), not an E⁴-leading effect. The discriminator needs reframing to "deviation from QED's pure-E² baseline," not "E⁴-leading."

**Skills applied.** `consistency-vs-emergence` (n = √(εμ) is the load-bearing identity; the e4 leaf's quantity is a consistency-class permittivity depth, not the index observable it claims); `ave-walk-back` (correct clm-pp3qwf + propagate to `divergence-test-substrate-map.md:63`); `ave-discrimination-check` (revised the first-plausible hypothesis after reading the source); `ave-audit-of-audit` (the agent's flag was sound; the root is a √ε conflation, sharper than "factor-2 + sign").

**Decision (pending Grant).** Determinate part: the mirror leaf (−A²/4) is **correct**; the e4 leaf conflates permittivity-depth (1−S) with index-shift (√S−1) — fix clm-pp3qwf (relabel 1−S as permittivity saturation depth; give the correct index shift δn = √S−1 ≈ −A²/4). Intent part (your confirm): reframe the E²/E⁴ discriminator as "AVE's saturation arc deviates from QED's pure-E² via higher-order E⁴+ terms as E→E_yield" (not E⁴-leading). Lean: fix the √ε conflation (determinate) + reframe the discriminator (confirm with you). Auditor-gate executes the leaf correction.

**Execution (on agreement).** Auditor-gate: correct clm-pp3qwf (`vacuum-birefringence-e4.md`) + `divergence-test-substrate-map.md:63` per `ave-walk-back`; verify the E²/E⁴ falsifiable claim's viability (it's facility-class, E→10¹⁶–10¹⁷ V/m — ties to #3 per-node scale). `closure-roadmap §0.5` row.

---

*All 5 adjudications worked. Next: auditor-gate (verifies + executes the determinate corrections) → round-2 merge-calls → the agreed sweeps/edits.*
