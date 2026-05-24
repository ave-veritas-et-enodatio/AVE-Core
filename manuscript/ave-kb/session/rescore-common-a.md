# Re-score: common/claim-quality.md entries 1–19 (confidence / local-rigor only)

Scope: entries 1–19 by `<!-- id -->` order (clm-sxn6eo … clm-ze4clw). Confidence = local rigor,
dependencies/inputs taken AS GIVEN (no solidity discounting). Each score checked against the cited leaf.

### clm-sxn6eo — Mathematical Closure Status ("Structurally Zero-Parameter," Not Absolutely)
- current confidence: 0.70
- NEW confidence: 0.70
- changed: no
- rationale: `mathematical-closure.md` §Explicit Closure DAG + §Outstanding Rigour Gaps + §Acyclicity verdict, and `full-derivation-chain.md` §Layer 7→8, do exactly the work the entry claims: the forward DAG is constructed edge-by-edge and verified acyclic by inspection; the three Layer-8 back-edges (α, m_e, G) are individually identified with their acyclicity conditions; and the one fitted scalar (δ_strain ≈ 2.225×10⁻⁶, `DELTA_STRAIN = 1 − (1/ALPHA)/ALPHA_COLD_INV`) is explicitly back-subtracted-from-CODATA, not hidden. The four Outstanding Rigour Gaps are tabulated honestly. This is a meta-disclosure entry; its own work (the reduction of 26 SM params to {m_e,α,G}+4 axioms and the conditional-on-Layer-8 framing) is sound and self-bounding. The 0.70 cap correctly reflects that the headline rides on still-open closures the leaf itself flags. Classification: largely manifestation/consistency-disclosure of the closure status, not a fresh derived number.

### clm-ibfyda — Full Derivation Chain (Acyclicity + Identified Methodology Disclosures)
- current confidence: 0.65
- NEW confidence: 0.65
- changed: no
- rationale: `full-derivation-chain.md` is a complete layer-by-layer chain with the disclosures the entry asserts present and binding: Layer 2 carries the explicit "Framing (consistency check, not derivation of α)" preamble and states p_c = 8πα is α's SI definition rearranged; Layer 5 carries the boxed Methodology disclosure (three Cosserat sectors → three generations matched-not-derived; muon α√(3/7); tau 8π/α; PMNS {5,7,9} pattern-identified, with the 2026-05-17 scope-correction that Δc=2 IS derived from ν_vac but c₁=5 is open); the δ_CP^PMNS ≈ 4.26 vs δ_CP^B ≈ 0.126 disambiguation is in-text. The substantive open elements (Layer-5 identifications, PMNS absolute starting value) are exactly what hold local confidence at derived-with-disclosed-methodology-bound (≈0.7 band) and slightly below; 0.65 is well-placed.

### clm-t5ybqw — Experimental Falsification Index (Catalog Status, Not Validation)
- current confidence: 0.85
- NEW confidence: 0.85
- changed: no
- rationale: `appendix-experiments.md` is precisely a catalog: per-Volume designed protocols with chapter locators, explicit RETRACTED / DEMOTED / SUPERSEDED / corroborative-null status markers (VLBI retracted; DAMA demoted; Sagnac/GEO retired to corroborative null), and the Vol 5 chiral-FRET entry flagged "currently unfalsifiable / future target." The leaf does the catalog-with-honest-status work to a high local standard and self-bounds as catalog ≠ validation. 0.85 (well-done enumeration, not an axiom-to-measurement derivation) is correct.

### clm-m7qd0w — Universal Solver Toolchain (Operator Reuse, Not Per-Domain Derivation)
- current confidence: 0.65
- NEW confidence: 0.65
- changed: no
- rationale: `solver-toolchain.md` lays out the five-step method and the worked eigenvalues match the entry: BH QNM 18/49 = 0.3673 (1.7% vs GR), pion (45/7)√(m_e m_p) = 140.8 MeV (+0.9%), protein backbone 21.7 THz (+0.1% on MEASURED v_backbone; sub-derivation gives 5470 m/s, −5.2%), Kerr Q sub-2% for a*∈[0.3,0.8] degrading to ~40% at 0.99. The Poisson-projection form r_eff = r_sat/(1+ν_vac) is asserted as one valid 3D projection (alternatives not ruled out) — the substantive open local element. Cross-domain table correctly self-bounds as structural reuse. 0.65 (derived with an open identification step) holds.

### clm-fy05jc — Translation Tables (Notation Mappings, Not Physical Equivalences)
- current confidence: 0.85
- NEW confidence: 0.85
- changed: no
- rationale: Cited via the seven translation-tables leaves + INVARIANT-C3; the circuit-row identities (Q↔x, I↔v, V↔F, L↔m, C↔κ, R↔η) are dimensionally exact once ξ_topo is fixed (Axiom 2), and the entry correctly frames every row as a re-rendering, not an independent prediction, with medical/therapy rows flagged as interpretive-not-therapeutic. The leaf-level work (consistent notation maps given the ξ_topo mechanism, a framework input) is done to a high local standard; substantive predictions live in target leaves with their own entries. 0.85 holds. [Note: translation-tables/* not re-opened individually this pass; the appendices-overview index of them was read and is consistent — high-confidence on the per-table content, verified on the framing.]

### clm-hmiytz — ξ_topo Traceability (Conversion Constant, Not Free Parameter)
- current confidence: 0.85
- NEW confidence: 0.85
- changed: no
- rationale: `xi-topo-traceability.md` defines ξ_topo = e/ℓ_node directly from Axiom 2, gives the six-row scaling table, documents the 51-files/6-of-8-volumes reuse as reuse (not 51 confirmations), and carries the canonical three-scope ξ de-collision table (ξ_topo C/m vs Machian ξ ~10³⁸ vs Cosserat ξ_K1,ξ_K2). The Zero-Free-Parameter-Chain sub-claim is explicitly marked conditional on the δ_strain closure. Entry-local work is identity-grade given Axiom 2 plus honest reuse bookkeeping; 0.85 is correct (not 1.0 because the entry also carries the conditional chain sub-statement and the namespace-discipline content, which are claims about the corpus, not pure definition).

### clm-zi6t1e — Derived Numerology Appendix (Derivation Trace, Not Empirical Coincidence)
- current confidence: 0.70
- NEW confidence: 0.70
- changed: no
- rationale: `appendix-derived-numerology.md` carries an explicit axiom-trace column for every constant; z₀≈51.25 derived from the Feng-Thorpe-Garboczi EMT quadratic at K=2G (physical root, second root rejected as unphysical); n_3D = 2(1−ν_vac/3) = 38/21 ≈ 1.8095; C_K = 1/η = 4/3 from the K4 S-matrix cascade (η = 3·(1/2)² = 3/4); and the FDTD `sponge_damping = 0.8` is explicitly excluded as a numerical artifact (model honest-numerology disclosure). The empirical agreements are correctly scoped (n_3D vs single solar-flare figure; C_K vs classical value — structural, not precision-dataset). 0.70 (derived-with-disclosed-bound) is well-placed.

### clm-yawl6z — Appendices Overview (Theoretical Stress Tests, Not Independent Proofs)
- current confidence: 0.75
- NEW confidence: 0.75
- changed: no
- rationale: `appendices-overview.md` presents the three stress tests (Spin-½ via Finkelstein-Misner kink; holography via Φ_A ≡ α²; Peierls-Nabarro via STZ) as framework-internal resolutions, the Summary of Exact Analytical Derivations as a cross-reference index, the dropped τ_yield Bingham-Plastic claim as an HTML-comment editorial-transparency record (2026-04-20 audit), and the DCVE/Computational-Graph specs as engine instantiation constraints — all matching the entry. As a meta-summary its own framing work is solid (0.75); substantive solidity lives in the per-claim entries it points to. Holds.

### clm-pfocn6 — SPICE Verification Manual (Toolchain Status, Not Validation Claim)
- current confidence: 0.85
- NEW confidence: 0.85
- changed: no
- rationale: `appendix-spice-verification.md` documents the Tier 1→2→3 architecture (compiler never re-derives operators), the compile→write→ngspice→compare protocol, explicit dependencies (ngspice ≥42, Python ≥3.10), and self-bounds as a code-correctness cross-check (Python solver vs SPICE netlist), NOT physics-vs-measurement. The leaf does this scoping work cleanly and completely. 0.85 holds.

### clm-io8hft — VCA Schematic Symbol Vocabulary
- current confidence: 0.82
- NEW confidence: 0.82
- changed: no
- rationale: `appendix-vca-symbols.md` is a complete self-contained catalogue — five design rules, seven markers, seventeen components — with constants consistent across rows (V_snap = m_e c²/e ≈ 511 kV; Z₀ = 376.73 Ω on circulator + transducer). The two caps are real and present in the leaf: entry 9 (Klopfenstein) shows only the generic local-reflection integrand Γ(x) = ½ d/dx ln Z(x) without the Klopfenstein weighting/passband condition, and the Coanda "No kT barrier" (entry 11) vs Thermal-Baffle Landauer kT (entry 8) tension is reconciled only in the entry's non-claims footer, not at the catalogue-row level. 0.82 (just below top band on those two presentation gaps) is correctly placed.

### clm-zgllr2 — A-027 Two-Engine Architecture (Regime-Partitioned Simulation)
- current confidence: 0.75
- NEW confidence: 0.75
- changed: no
- rationale: `two-engine-architecture-a027.md` §The two engines gives the tool-to-regime assignment with source files (k4_tlm.py for A≪1; master_equation_fdtd.py for A→1), the disjoint-regime partition, and the v14 Mode I PASS scoped to one breathing soliton at the Golden Torus geometry. Explicitly a computational-architecture claim, not a physical postulate. The entry's caps (qualitative A≪1 vs A→1 threshold; handoff mode-matching open; single bound-state validation) match the leaf. 0.75 holds.

### clm-zfqd9v — Wave-Speed Modulation Is Required to Localize a Bound State
- current confidence: 0.55
- NEW confidence: 0.55
- changed: no
- rationale: §Why two engines now states the canonical Vol 1 Ch 4 form (c_eff = c₀/√S, wave speed RISES in the saturated core since ε_eff = ε₀S → 0, Γ→−1 reflects at the boundary trapping a breathing soliton; kernel bounds the soliton's BOUNDARY rate) and explicitly supersedes the prior "wave slows at core" framing — the sign drift the entry says was resolved 2026-05-18/21 is indeed resolved in the leaf. The residual local-rigor gap is exactly as the entry states: the NECESSITY of c_eff modulation for localization is read off engine behaviour and the d'Alembertian form ("without wave-speed modulation … propagating modes simply propagate") rather than proven via a no-go argument from the four axioms. 0.55 (derived with a substantive matched-not-derived step) holds.

### clm-gr8d63 — Two-Engine Convergence on p* = 8πα
- current confidence: 0.60
- NEW confidence: 0.60
- changed: no
- rationale: §Two-engine convergence example correctly frames this as a multi-model consistency check, not a determination of α: the FDTD route grounds in the Golden Torus α = 1/(4π³+π²+π) and p_c ≡ 8πα is Axiom-4 definitional; the K4-TLM route obtains z₀≈51.25 by inverting the EMT quadratic GIVEN p* = 8πα (circular if read as a determination). Two distinct mechanisms (static elastic vs dynamic soliton) landing on the identical definitional value is a clean consistency demonstration with no independent predictive content for α. The entry concedes "identical" is asserted without a stated tolerance. 0.60 holds.

### clm-dsb560 — Three-Route Framework: α, G, J_cosmic from a Single Ω_freeze
- current confidence: 0.55
- NEW confidence: 0.55
- changed: no
- rationale: `omega-freeze-cosmic-grain-cascade.md` §1 + Key Results give the three routes, each MAPPING an externally-measured constant (α via Vol 1 Ch 8; G via the Machian impedance integral; J_cosmic via Ω_freeze = J/I) onto a common u₀* ≈ 0.187; the load-bearing route derivations are owned elsewhere and not restated. The leaf's own statement is that convergence on a single u₀* is the FALSIFIABLE COMMITMENT, not a demonstrated result. As a Class-E operating-point-projection framing it is internally coherent, but the single-u₀* convergence is asserted, not shown locally. 0.55 holds.

### clm-a7cbqq — Ω_freeze Freeze-In at Lattice Genesis
- current confidence: 0.45
- NEW confidence: 0.45
- changed: no
- rationale: §2 describes the freeze-in mechanism (rotating-frame bond lock → u₀* over-bracing + chirality direction → I4₁32 right-handed) qualitatively, by analogy to water→ice, and §6 explicitly flags the Landau minimization of U_chiral^add as open / not-yet-executed (the texture-projection-onto-G piece called "the genuinely open piece"). Ω_freeze's value/source is cited (universes-inside-BHs closure), not derived. The chirality-direction-locking step is structurally plausible but asserted at the descriptive level. 0.45 (asserted with partial justification, key derivation step open) is correctly placed.

### clm-pe8lpx — Eight Cosmic-Axis Observables Aligned with the Ω_freeze Axis
- current confidence: 0.50
- NEW confidence: 0.50
- changed: no
- rationale: §3 lists the eight channels and the per-channel caveats match the entry: channel 5 conditional on asymmetric crystallization (K/G≠2); channel 7 amplitude conjectural (scored separately at clm-fndptx); LSS channel on a contested ~1–2σ SDSS direction; no positive detection for any channel. "All eight share the Ω_freeze axis" is a manifestation of the single-axis premise; the per-channel Ω_freeze→observable coupling is largely asserted, not derived. (Note: the entry's strengthen-by about reconciling the l≈174° placeholder vs the Planck pin l=60.28° is now partly stale — the leaf already uses the 2026-05-19 Planck PR3 SMICA pin at (60.28°, 50.48°) and labels 174° a literature placeholder; this is a strengthen-by note, not a confidence driver.) 0.50 holds.

### clm-fndptx — G-Anisotropy Angular Shape P₂(cos θ): Sharp Profile, Bracketed Amplitude
- current confidence: 0.55
- NEW confidence: 0.55
- changed: no
- rationale: §3.2 derives the P₂(cos θ) angular shape and the 4π/15 ≈ 0.838 Kirkwood-Frohlich-analog projection coefficient structurally ("this IS derived structurally"), while explicitly stating the amplitude suppression order N≥2 is NOT derived from first principles and δ_χ ~ α² (bipartite K4 cancellation) is conjectural-not-derived. Clean "structure predicted, magnitude only bracketed": shape side solid, amplitude side acknowledged open conjecture. 0.55 holds.

### clm-ze4clw — Three Exhaustive Boundary Observables M, Q, J at Every Γ=−1 Surface
- current confidence: 0.60
- NEW confidence: 0.60
- changed: no
- rationale: `boundary-observables-m-q-j.md` §The three invariants gives the M/Q/J catalog with the Stokes-theorem dimensional structure (M = 3D volume ∫(n−1)dV; J = 2D surface winding, half-integer per SU(2) double-cover; Q = 1D line/loop linking) and the consistent cross-dialect EE/ME/QFT projection columns (with the ME column honestly empty for Q). The load-bearing exhaustiveness claim ("no fourth integrated boundary observable") is explicitly NOT proven — it rests on the dimensional-reduction heuristic that a 3D bulk admits exactly three lower-dimensional integrals (entry concedes this; leaf states it as structure, not theorem). Consistent complete catalogue + one acknowledged unproven structural assertion. 0.60 (derived/structured with an open exhaustiveness step) holds.

---

## Summary
- Scored: 19 / 19 (clm-sxn6eo … clm-ze4clw).
- Changed: 0.
- Every current confidence is well-grounded in its cited leaf and consistent with the rubric; the recent
  migration (sign-drift resolution on clm-zfqd9v 2026-05-18/21; Planck-pin update in the omega-freeze leaf;
  retractions/demotions in appendix-experiments) is already reflected in the existing entries' rationales,
  so no re-scoring was warranted.
- One non-scoring observation: clm-pe8lpx's strengthen-by axis-reconciliation item is partly stale (the leaf
  already adopts the Planck PR3 pin); flagged for the author but it does not affect confidence.
