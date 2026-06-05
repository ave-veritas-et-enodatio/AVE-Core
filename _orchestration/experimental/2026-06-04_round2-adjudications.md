# Round-2 Hardening — Adjudication Ledger (2026-06-04)

**Companion to** the epic spine [`2026-06-03_experimental-protocol-revamp-orchestration.md`](../2026-06-03_experimental-protocol-revamp-orchestration.md) §12 (round-2 verdicts). The spine records *what happened*; this ledger records *why each decision was made* — each round-2 adjudication, EE-mapped (`ave-ee-first-mapping`) + skill-disciplined, with Grant's decision + execution pointer. This is **Layer 2** (reasoning) of the orchestration-documentation architecture; the corpus deltas (Layer 3) are the *result* of each adjudication, the audit tags (Layer 4) the ancestry, the capstone the closing narrative.

**Format per entry:** substrate picture → EE map → means-test → skills applied → decision (Grant) → execution pointer.

## Index

| # | Item | EE map (crux) | Decision | Status |
|---|---|---|---|---|
| 1 | HOPF reciprocity | Pasteur (reciprocal, P-odd) vs Tellegen (non-recip, T-odd) | reciprocal-Pasteur at linear → C3/C4 retire labels; ADD 2-port reciprocity sweep | **AGREED** 2026-06-04 |
| 2 | Cleave CPD / SM≠0.0 | Kelvin probe / patch potentials (CPD real, gap-dep ∝1/g²) | confirm + propagate SM≠0.0 + gap-sweep | **SURFACED** 2026-06-04 (pending) |
| 3 | per-node-conflation sweep | per-node V_yield vs apparatus voltage (scale bridge) | — | queued |
| 4 | ξ_topo content-anchor | content-anchor vs line-number cite (hygiene) | — | queued |
| 5 | IVIM index-convention | δn≈−A²/4 vs Δn≈+A²/2 (factor-2 + sign) | — | queued |

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

## §2 — Cleave CPD / SM≠0.0  [SURFACED 2026-06-04 — pending Grant]

**Decision context.** Cleave round-2 (`analysis/2026-06-04-cleave-round2-smcounterfactual`, `76f66b9`) found round-1's foundational claim *"Standard EM predicts 0.0 mV"* FALSE — contact-potential-difference (CPD) gives a non-zero, polarity-ODD, ~21%-of-floor charge that form-shares with the ξ_topo floor on magnitude + polarity. Cure: CPD is gap-DEPENDENT (∝1/g²), the floor is gap-INDEPENDENT → a gap-sweep separates them (4-corner symmetry discriminator). The call: confirm the correctness finding + authorize the SM≠0.0 propagation + adopt the gap-sweep leg.

**Substrate picture.** The Cleave electrometer reads the topological linking charge 𝒬 = ξ_topo·x = (e/ℓ_node)·x on a floating electrode as the PZT displaces it. Question: is the classical (SM) background really 0.0?

**EE map** (`ave-ee-first-mapping`). A moving floating electrode with a work-function difference is a **Kelvin probe / vibrating capacitor**: Q_CPD = C(x)·V_CPD → dQ/dx = V_CPD·dC/dx. Canonical EE instrument (scanning Kelvin probe, vibrating-reed electrometer). CPD + surface **patch potentials** are THE dominant systematic in precision electrostatic / Casimir / Kelvin-probe metrology — never exactly zero in a real bench. → round-1's "SM = 0.0" holds ONLY for a perfectly equipotential, single-work-function, patch-free surface; in any real bench it is non-zero.

**Means-test (the cure).** Parallel-plate C ∝ εA/g → dQ_CPD/dx ∝ V_CPD/g² → **gap-dependent**. The ξ_topo floor = e/ℓ_node, a pure constant → **gap-independent**. A ≥4× gap-sweep: CPD drops ∝1/g²; floor unchanged. ✓ Separated. The other classical fakers fail other corners: electrostriction/flexo/secondary-piezo are even-in-drive-V (removed by polarity-reversal at *any* magnitude); tribo is decaying (removed by time-gating). NO single classical mechanism fakes all 4 corners {linear ∧ polarity-odd ∧ material-indep ∧ gap-indep}.

**Skills applied.** `ave-audit-of-audit` (verified the CPD claim against the geometry — it is settled EE/metrology, the dominant Casimir/Kelvin-probe systematic; finding SOUND); `consistency-vs-emergence` (the 4-corner floor = Ax2 emergence; CPD/patch = classical-consistency background — the correction correctly separates them); `ave-discrimination-check` (moves the discriminator from P1 "presence-of-charge" — which CPD fakes — to the 4-corner symmetry signature, which it cannot); `ave-walk-back` (SM≠0.0 propagation, sites below).

**Located propagation sites** (`verify-before-cite`): `project-cleave-01.md:22` ("separating two uncharged plates in hard vacuum generates exactly zero charge"), `:44` ("Standard EM predicts $0.0$ mV" — the agent's "L44"), `:65` ("0.0 mV observed"); `research/2026-06-03_topological-charge-occupation-robustness.md:95` ("vs SM's 0.0 mV in clean vacuum"); Femto `hardware/TEST_PROCEDURE.md` (agent-corrected locally). The agent's cited "AVE-Core Phase-3 prereg §4 (liberates no net charge)" was NOT located by grep in AVE-Core `research/` — pin at execution (may be the Femto-side prereg, cross-repo).

**Flag for auditor (not Grant's intuition call).** The floor's measured VOLTAGE (mV) is gap-independent only at FIXED C_in (readout capacitance) — the gap-sweep must hold C_in fixed (or account for it), per the occupation-robustness framing (`:95` "hold C_in fixed and read the floor"). Protocol-design subtlety; does not change the adjudication.

**Decision (pending Grant).** Confirm the CPD correctness finding (SM≠0.0) + the gap-sweep cure; authorize propagating the correction to the located sites; adopt the gap-sweep + 4-corner framing as the canonical Cleave discriminator. **Lean: strong confirm** — this is settled EE/metrology, and it STRENGTHENS Cleave (magnitude argument → symmetry argument).

**Execution (on agreement).** Propagate SM≠0.0 to the 4 located sites (per `ave-walk-back`, corrected statement: *"the polarity-odd, gap-INDEPENDENT component is classically 0.0; the raw vacuum charge is not — CPD gives a polarity-odd, gap-dependent term"*); the round-2 branch's TEST_PROCEDURE edit lands on merge; new `translation-circuit.md §4` row (CPD ↔ Kelvin probe / patch potentials); `closure-roadmap §0.5` row. Sequenced after the auditor-gate.

---

*Entries #3 (per-node-conflation sweep), #4 (ξ_topo content-anchor), #5 (IVIM index-convention) logged as adjudicated.*
