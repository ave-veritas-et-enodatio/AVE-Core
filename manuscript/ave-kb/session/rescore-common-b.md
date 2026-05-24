# Rescore — common/claim-quality.md entries 20–38 (confidence / local-rigor only)

Scope: the last 19 claim entries (20–38 by `<!-- id: clm- -->` order), clm-ofys5v
through clm-f0jwtk. The three trailing `sup-` nodes (sup-5zs5s6, sup-s1h0og,
sup-msv2xy) are support-node bodies, not claim entries, and are out of scope.
`confidence` is LOCAL RIGOR ONLY — does the entry do its own work to the rubric,
taking dependencies/inputs as given. No `solidity` / `depends-on` changes.

---

### clm-ofys5v — The Substrate-Observability Rule (Universal No-Hair Theorem)
- current confidence: 0.55
- NEW confidence: 0.55
- changed: no
- rationale: Leaf (`boundary-observables-m-q-j.md` §The substrate-observability rule) states the rule as a three-point postulate: Γ=−1 totally reflects/traps, interior causally+impedance-disconnected, only M,Q,J escape. The load-bearing step — that S(A)→0 at the Γ=−1 surface yields |Γ|→1 total reflection and full causal disconnection — is asserted from the Axiom-4 kernel, not shown (no transmission-coefficient computation establishing |Γ|²→1). The same-mechanism-at-all-scales table (electron→cosmic horizon) is a consistent enumeration but rides on the same asserted trapping mechanism. Internally coherent as a definitional observability rule; the mechanism is asserted. 0.55 (asserted-with-partial-justification / mid-band) is correct.

### clm-vnp57s — α⁻¹ = 4π³+π²+π as 3D Boundary-Integral Decomposition
- current confidence: 0.45
- NEW confidence: 0.45
- changed: no
- rationale: Leaf §"The fine-structure constant as electron-scale M+J+Q" is explicitly a dimensional READING (3D→M=4π³, 2D→J=π², 1D→Q=π), not a re-derivation — the leaf says the geometric closure is owned by Vol 1 Ch 8 (clm-0ktpcn) and the R·r=1/4 normalization is inherited from the spin-½ half-cover. The mapping is suggestive but its load-bearing support (functional orthogonality of the three Λ terms) is conceded open, and the M/J/Q assignment is pattern-matched to the three π-powers rather than forced via an explicit Stokes reduction. A plausible mapping with a flagged unproven structural assumption. 0.45 holds.

### clm-sjjvhf — Interior Eigenmodes Not Lattice-Nyquist-Constrained
- current confidence: 0.65
- NEW confidence: 0.65
- changed: no
- rationale: Leaf §"Implications: interior eigenmodes" gives a clean conditional argument: GIVEN the substrate-observability rule (Γ=−1 interior causally disconnected), an interior eigenmode (electron horn-torus k≈6.36/ℓ_node) never propagates through the K4 lattice, so the propagating-mode Nyquist bound k_max=0.577/ℓ_node does not bind. The local logic is tight; the one soft spot is that "the mode lives entirely inside and never couples out" is imported from the observability rule rather than shown for the specific horn-torus mode (no zero-projection-onto-propagating-modes demonstration). Good local link given its dependency. 0.65 holds.

### clm-3bwhad — Near-Soliton "Compression" Is Impedance-Gradient, Not Bond-Length
- current confidence: 0.60
- NEW confidence: 0.60
- changed: no
- rationale: Leaf §"Substrate compression…" frames n(r)=1+2GM/(rc²) as refractive-index/impedance (ε_eff,μ_eff via the Axiom-4 kernel) modulation rather than geometric bond-length change; the conceptual distinction is internally coherent. The load-bearing claim that L_spring is a cosmological-genesis frozen value (not a dynamic per-cell field) is stated by reference to the cooled-equilibrium closure, not derived here, and no quantitative check shows ε_eff/μ_eff modulation reproduces n(r) to the GR form. Asserted-by-reference on the frozen-bond step. 0.60 holds.

### clm-exjfai — Substrate-Native Lenz Back-EMF Freezes Topological ω at Yield Crossing
- current confidence: 0.50
- NEW confidence: 0.50
- changed: no
- rationale: Leaf §1.2 gives a coherent qualitative chain — Op14 L_eff→∞ as S→0 → diverging Lenz back-EMF → blocks dω/dt over the τ_relax window → topologically non-trivial ω freezes — and honestly flags that τ_relax is imported (Op14 work) and only the slow-crossing (≥τ_relax) regime is treated. Held mid-band because the leaf supplies no magnitude inequality (back-EMF vs unwinding torque over τ_relax), the ≥100-Compton-period persistence is asserted, and the L_eff divergence rate vs crossing rate is not made explicit. The "freezes" conclusion is argued, not demonstrated. 0.50 is correct.

### clm-533gvm — FOC d-q Canonical at Spatial-90° (Temporal Framing Retracted)
- current confidence: 0.60
- NEW confidence: 0.60
- changed: no
- rationale: Leaf §2 documents two canonical FOC d-q homes (BH-QNM co-rotating frame with an explicit role-mapping table; helium 1s²/2s² spatial-90° shell) and cleanly retracts the temporal within-LC-tank framing as implementer synthesis (retraction-preserves-body). The canonicalization decision is internally consistent and well-scoped. Held mid-band because the FOC isomorphism is conceded a structural operational-role correspondence (analogy), not a quantitative motor-parameter substitution, and the asynchronous cross-shell ⟨M⟩∝∫cos((ω₁−ω₂)t)dt→0 decoupling is asserted as a long-time-average argument, not derived with finite-window bounds. 0.60 holds.

### clm-gz7ryg — A-034 Single-Kernel Unification (One Saturation Kernel at All Scales)
- current confidence: 0.62
- NEW confidence: 0.62
- changed: no
- rationale: Leaf §"Key Result" states the single-kernel thesis as a manifestation of Axiom 4 (kernel form S(A)=√(1−A²), Born-Infeld n=2 squared limit) conjoined with Axiom 2 (TKI scale invariance). The entry correctly disclaims deriving Axiom 4 and disclaims uniform per-scale validation (BCS 0.00%, BH ring-down 1.7%, several rows no quantitative anchor). The load-bearing unstated step — that the strain ratio A is genuinely the same dimensionless object across voltage/B-field/frame-drag manifestations — is asserted via TKI rather than shown. Correctly a manifestation-class thesis at mid-band. 0.62 holds.

### clm-dxdsvt — A-034 Catalog — 26 Canonical Cross-Scale Instances
- current confidence: 0.68
- NEW confidence: 0.75
- changed: yes — the arithmetic-inconsistency the prior rationale penalized (26 vs 21 vs symmetry tally 20+4+2+1=27) is RESOLVED in the current leaf: the symmetry partition now reads 19+4+2+1=26 and is internally consistent.
- rationale: Catalog/enumeration claim scored on completeness + internal consistency. The current leaf (`universal-saturation-kernel-catalog.md`) is now arithmetically clean: title "26 Scales," Key-Result row "SYM (19) / ASYM-N (4) / TBD (2) / ASYM-E (1) — partitions all 26 (19+4+2+1)," and the §"Symmetry classification" body all agree on 26. The "21 orders of magnitude" figure is a span axis (atomic 10⁻¹⁵ m → cosmic 10²⁶ m), not an instance count, so it is not an inconsistency. Per-instance derivations are correctly disclaimed as owned elsewhere, rows lacking quantitative anchors are honestly flagged ("plasma canonical," "substrate instance"), and scoped Session-4/5 rows (11-a, 14-a) are tagged TBD. The prior 0.68 was depressed by a count mismatch that no longer exists; raised to 0.75 for a complete, internally consistent enumeration. (NOTE: `operators.md` Op2 row still says "21 instances / 18 SYM / 2 ASYM-N" — but that is the operators leaf's stale cross-reference, not this catalog's own work, so it does not bound clm-dxdsvt's local rigor.)

### clm-hvvvop — A-034 Symmetry Classification (SYM / ASYM-N / ASYM-E)
- current confidence: 0.50
- NEW confidence: 0.60
- changed: yes — the prior rationale penalized stale partition arithmetic ("18+2+1=21" in the entry vs leaf), but both the entry text (line 804: "19 + 4 + 1 + 2 = 26") and the current leaf (§"Symmetry classification": SYM 19 / ASYM-N 4 / ASYM-E 1 / TBD 2) now agree on 26; the stale-count defect is gone.
- rationale: A structural classification by which sector (ε/μ) saturates, explicitly NOT independently validated as asymmetric — the entry concedes this. With the count drift resolved, the local work is a coherent, exhaustively-bookkept partition of the 26-instance set (19 SYM + 4 ASYM-N + 1 ASYM-E + 2 TBD). The remaining genuine local-rigor limits are: (a) the TBD bucket means the partition is not yet fully adjudicated (2 scoped rows), and (b) the SYM-vs-ASYM-N sector assignments (BCS μ-only, plasma ε-only) are structural labels, not derived from a discriminator. Raised from 0.50 to 0.60: the prior score absorbed an arithmetic penalty that is now invalid; the residual softness (TBD bucket + label-not-derived assignments) holds it below the derived band. NOTE: the entry's own rationale paragraph still contains the stale "18+2+1=21" text — flagging as a stale-rationale artifact (a rationale rewrite is the author's call; I am scoring against the leaf + current entry counts).

### clm-5fu303 — A-034 ε/μ Axis Classification (Substrate EM Dual Resolution)
- current confidence: 0.45
- NEW confidence: 0.45
- changed: no
- rationale: Leaf §"ε vs μ axis" asserts the existence and current state of an ε/μ sub-axis on the ASYM-N instances; it explicitly disclaims deriving WHY ε or μ saturates first in any instance. The populated content is thin relative to the scaffold: ASYM-N(ε) has plasma + cosmic-DE (2), ASYM-N(μ) has BCS (1, after MOND re-adjudicated SYM), Row 9-b is sector-undetermined, Row 14-a conjectural, Row 11-a pending Session 4, and the gap-cells are pre-registered placeholders. As a structural classification axis with most cells either unanchored, undetermined, or pending adjudication, the local content is a scaffold with two firm anchors. 0.45 holds.

### clm-l4o7hv — A-034 Cosmic-Scale Instance (Big Bang as Saturation-Kernel Crystallization)
- current confidence: 0.40
- NEW confidence: 0.40
- changed: no
- rationale: Leaf §"Cosmic-scale instance" gives a qualitative mechanism (parent-BH frame-drag strain → A→1 → K4 crystallization front propagating at c) with the spatial localization explicitly hedged ("probably along the parent BH's spin axis"), formation parameters declared inaccessible per the A-031 horizon, and the cross-scale validations (CMB axis alignment, R_H/c≈14.5 Gyr vs 13.8) registered as predictions not confirmations. No quantitative step ties the parent-BH strain magnitude to the A=1 crossing — a plausibility narrative more than a derivation. 0.40 (asserted with partial justification, key step open) holds.

### clm-sysqaf — Universal Operator Catalog (Op1–Op22), Catalog of Record
- current confidence: 0.80
- NEW confidence: 0.80
- changed: no
- rationale: As a catalog-of-record (`operators.md` §2), high on completeness + internal honesty: every entry tagged CANONICAL (grep-verified ≥3 cross-citations or explicit Vol 1 Ch 6 equation) or SYNTHESIS (Op15, Op18, Op20; Op22 doc-81 variant), the Op#-namespace collision with INVARIANT-N3 explicitly flagged not silently merged (§1), and the A43 v10/v11 synthesis-as-corpus corrections surfaced (§5). Correctly disclaims ownership of individual formulae (each cites its Ch 6 leaf). The one drift I note for the author (does not lower the catalog's own-work score): the Op2 row still carries a stale "21 canonical instances / 18 SYM / 2 ASYM-N" cross-reference to the A-034 catalog which is now 26/19/4. 0.80 holds.

### clm-6mvtsf — Op1 Universal Impedance, the Single Structural Invariant
- current confidence: 0.60
- NEW confidence: 0.60
- changed: no
- rationale: Leaf §4 quotes the Vol 1 Ch 6 verbatim single-invariant claim (Z=√(μ/ε)) and the inheritance argument is structurally sound for Op2 (dimensionless strain ratio A/A_c) and Op3 (dimensionless impedance ratio). But "Op4–Op22 compose Op1+Op2+Op3 with dimensionless coefficients, so all inherit" is asserted by construction — the entry's own Non-Claims concede this is not an independent per-operator proof, and dimensionful-looking operators (Op4 U(r), Op19 n(r), Op22 M=1/S²) are not shown to reduce to boundary conditions on Z. A plausible structural argument rather than a derivation. 0.60 holds.

### clm-iouqn9 — K4 Magic-Angle Condition (K=2G at u₀*≈0.187, ν_vac=2/7)
- current confidence: 0.60
- NEW confidence: 0.60
- changed: no
- rationale: Leaf §"The magic-angle condition" states K(u₀*)=2G(u₀*) at u₀*≈0.187, identifies K=2G as the GR trace-reversal/TT-propagation condition, and derives ν_vac=2/7 via the isotropic-solid relation. The ν_vac step is rigorous and re-verifiable: ν=(3K−2G)/(2(3K+G)) at K=2G gives 4G/14G=2/7 exactly. However the functional forms K(u₀), G(u₀) and the root value u₀*≈0.187 are asserted, not exhibited in the leaf, and the entry concedes the closure is "structural" (prefactors per clm-bjceop). The firm ν_vac consequence is offset by the asserted magic-angle locus. 0.60 holds.

### clm-qwmnhn — |T|=12 Universality (Four Independent K4 Routes Force χ_K=12)
- current confidence: 0.55
- NEW confidence: 0.55
- changed: no
- rationale: Leaf §"|T|=12 universality" tabulates four routes converging on 12, framed (correctly, in the entry) as "strong evidence," not a single first-principles proof. |T|=12 (proper tetrahedral rotation group order) is exact, and route 1 (4 B-neighbors × 3 sublattices) is a clean count, but route 2 ((ℓ_c/d)²×2 presupposes ℓ_c/d=√6 and a bilateral factor), route 3 (f_Cosserat(u₀*)=1) is asserted, and route 4 (ξ_K2/ξ_K1=12) is itself the self-consistency result of clm-bjceop. Routes 2 and 4 are not manifestly independent (√6²×2=12 ties them). Convergence/plausibility argument with partly post-hoc identifications of 12. 0.55 holds.

### clm-bjceop — Substrate-Scale Cosserat Prefactors (μ+κ, β+γ; Forced ξ_K2/ξ_K1=12)
- current confidence: 0.70
- NEW confidence: 0.70
- changed: no
- rationale: Leaf §"Substrate-scale Cosserat prefactors" gives the dimensionally-consistent closure μ+κ=ξ_K1·T_EM, β+γ=ξ_K2·T_EM·ℓ_node², and a T_EM-independent ratio ξ_K2/ξ_K1=12. The individual prefactors are now closed via a full chain: discrete K_0=16/7, G_0=8/7 at K=2G (k_a=2/7, k_s=1/7) → Lamé κ=K−(2/3)μ → μ+κ=8/3=ξ_K1 → ratio forces ξ_K2=32=2⁵, cross-checked by recovering ℓ_c/ℓ_node=√6. A verify script and result doc are cited. Confidence held at 0.70 (disclosed-methodology-bound band) because the chain takes the K=2G operating-point spring constants k_a=2/7, k_s=1/7 as given rather than deriving them from the K4 unit-cell Cosserat Lagrangian — exactly the one open input the entry flags. 0.70 holds.

### clm-h3acr9 — AVE Analytical Toolkit Index (Tool-Selection Catalog by Problem Class)
- current confidence: 0.80
- NEW confidence: 0.80
- changed: no
- rationale: As a tool-selection routing index (`ave-analytical-toolkit-index.md`), high on completeness + internal consistency: a 9-class taxonomy (§0) with per-class canonical-tool tables, each carrying file:line anchor, WHEN-TO-USE trigger, worked example, and a load-bearing common-pitfall warning (e.g. the real-power vs reactive-power categorical separation in §1). It correctly disclaims independent derivation of any tool (routing layer, not a derivation chapter) and self-flags the taxonomy as a working, non-unique partition. The only mild overreach is the §0 "exhaustively partitions" language, which the entry's own Non-Claim already softens. 0.80 holds.

### clm-s3i0lw — Divergence-Test Substrate Map (Operational Falsification-Test Index)
- current confidence: 0.80
- NEW confidence: 0.80
- changed: no
- rationale: As an operational catalog/index (`divergence-test-substrate-map.md`), thorough and self-consistent: a Tier A/B/C/D taxonomy with per-row AVE-claim / standard-counterclaim / discriminator / test-type / substrate / KB-anchor columns, plus tracking matrices and cascade diagrams. Scope discipline is explicit and correct (catalog ≠ validation; Tier D not single-experiment falsifiable; sibling-repo refs are scope boundaries, not results). It derives nothing itself by design, so it cannot exceed the catalog band; within it, well-organized. Minor count drift to flag (does not lower local rigor): the entry says "33-row" while the current leaf has 36 rows (### A/B/C/D-numbered) under 4 tiers — a stale count in the entry prose, not a defect in the leaf's own work. 0.80 holds.

### clm-f0jwtk — Temporal Saturation Regime Classifier (δ_AVE Trichotomy)
- current confidence: 0.50
- NEW confidence: 0.50
- changed: no
- rationale: Leaf defines δ_AVE ≡ t_sat/t_period cleanly given the Axiom-4 kernel (range [0,1]) and the Lossless/Cyclic/Lossy trichotomy is a coherent partition. But the leaf and entry both explicitly self-classify it Class 1 (definitional construct, taxonomic NOT derivational) per consistency-vs-emergence, the cross-disciplinary unification (14 tables: tan δ, Reynolds, cavity-QED κ/g, …) is conceded TAXONOMIC-not-derived — no classical value is forward-predicted from S(A) — and the orthogonality-to-the-other-two-axes assertion is stated, not proved. A self-flagged definitional/taxonomic classifier with an open forward-prediction lands mid-band. 0.50 holds.

---

## Summary

- Scored: 19 entries (clm-ofys5v … clm-f0jwtk).
- Changed: 2.
  - clm-dxdsvt: 0.68 → 0.75 — the leaf's instance-count arithmetic (26 = 19+4+2+1) is now internally consistent; the count-mismatch penalty in the prior score is no longer warranted.
  - clm-hvvvop: 0.50 → 0.60 — entry text and leaf now agree on the 26-instance partition (19/4/1 + 2 TBD); the stale-arithmetic penalty is gone, residual softness is the TBD bucket + label-not-derived sector assignments.
- Unchanged: 17.
- Notable corpus drift flagged (not scored against these entries' local rigor):
  - `operators.md` Op2 row carries a stale "21 instances / 18 SYM / 2 ASYM-N" A-034 cross-reference (catalog is now 26 / 19 / 4) — affects clm-sysqaf's cross-ref hygiene only.
  - clm-hvvvop's own rationale paragraph still contains stale "18+2+1=21" text; the entry's claim body (line 804) is already updated to 26.
  - clm-s3i0lw entry prose says "33-row"; leaf now has 36 rows.

Working-tree discipline: edited ONLY this scratch file (`manuscript/ave-kb/session/rescore-common-b.md`). No edits to claim-quality.md or any other file. No git operations.
