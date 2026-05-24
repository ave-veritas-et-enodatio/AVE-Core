# Vol 6 Local-Rigor Rescore Worksheet

Graded against canonical leaves (per INVARIANT-S7). Confidence = LOCAL derivation quality only (solidity untouched). Document order is a valid topological order; all intra-vol6 clm-deps cited point at-or-before the depending entry.

| clm-id | confidence | one-line local-rigor justification |
|---|---|---|
| clm-llqd1n | 0.7 | Binding formula + axiom-derived constants close cleanly; semiconductor leaf explicitly discloses the per-nucleus single-scalar R *fit*. Disclosed-methodology bound. |
| clm-lqanmt | 0.6 | K assembled from c=5, π/2 phase, αℏc, 1/(1−α/3); π/2-per-crossing and α/3 proximity correction asserted by EE analogy, not derived in-leaf. Between disclosed-bound and asserted-partial. |
| clm-7tk051 | 0.7 | Solver hits ≤2.80% over Z=1–14 with structure-gated corrections; Be Correction A shows a closed numeric chain. Rests on the radial-eigenvalue ODE solver + correction derivations imported from referenced leaves; zero-free-param is a disclosed methodology claim. |
| clm-nk6c43 | 0.6 | Tier-A/B near-exact closures are clean; Tier-C is an openly-disclosed Fibonacci *proxy* with residuals up to ~1.5%, and abcd leaf flags Z≥15 topology as the open problem. Honest tiering pins the band. |
| clm-l416hl | 0.4 | 4π solid-angle piece is Gauss-law clean; −√2/2 subleading term asserted with no derivation; R_halo itself is the per-nucleus fit. Sketch-plus-partial-support. |
| clm-8psuqe | 0.3 | Qualitative directional claim (large R↔halogen, small R↔alkali); R values are per-nucleus fits, no quantitative χ mapping. Structural assertion, not a closed derivation. |
| clm-sjixaw | 0.3 | First four magic numbers tabled against Platonic/Archimedean geometries; "achieves S₁₁→0" asserted, no per-geometry impedance-match calculation shown. Asserted-partial, partial coverage. |
| clm-ome498 | 0.5 | α_s=α^{3/7}, λ_H=1/8, g_*=7³/4 each carry a structural projection argument but the functional forms are asserted; leaves themselves carry author scope-corrections downgrading to 3.5σ tension / consistency-check. Substantive open step. |
| clm-mlwm3h | 0.6 | φ forced by the unique Thomson N=12 icosahedral minimizer is a sound structural argument (load-bearing Cr-52); "only/equidistant" phrasing is loose and Cr-52 R is still a fit. Disclosed-proxy bound. |
| clm-86gq2d | 0.4 | E_max=α·M_p c²=6.847 MeV is an exact substitution given α, M_p; the bridge to the ~8 MeV observed peak via Miller amplification is asserted ("smoothly brackets"), not derived. Sketch + identity base. |
| clm-o9xphr | 0.3 | Q-factor and S₁₁ presented as qualitative stability/reactivity proxies; numeric Q values stated as solver outputs without in-leaf calculation; decay magnitudes from CODATA. Asserted-partial. |
| clm-5965y1 | 0.5 | Explicitly and honestly an OPEN PROBLEM: ABCD cascade order + junction impedances for Z≥15 unsolved. The claim *is* the disclosed gap — substantive open dependency. |
| clm-jy8h1x | 0.7 | Three-regime V_R/V_BR classification + S-32 boundary derive cleanly from V_BR (axiom-derived) and the fit; "explains silicon microelectronics" is disclosed-interpretive, 75 MeV Q-value is empirical. Disclosed bound. |
| clm-a95yx1 | 0.9 | a₀=l_node/α and E₀=½m_e(αc)² follow by direct substitution of Axiom 1/2 definitions; n=2πa₀/λ_e≡1.00000 closes algebraically. Clean closed derivation (the leaf's own framing: identity/consistency-check). |
| clm-6tuqjh | 1.0 | Notation convention per INVARIANT-N2 (roman ℓ in vol6); true by construction, no physical claim. Definitional. |
| clm-qjwj12 | 0.5 | Mass→L, ε₀→C, Δm→M_ij, Γ→Q identifications presented as Axiom-1-consistent conventions, not independently derived; load-bearing physics lives downstream. Substantive open identification. |
| clm-jqnzz7 | 0.3 | Orbital/Lewis/VSEPR mapped to topological re-identifications; no quantitative bond-angle/length derivation (water 104.5° is analogy). Asserted ontological mapping. |
| clm-f5ucdo | 0.4 | Per-element topology identifications + post-hoc isotope-stability narratives; geometric scales are per-nucleus fits (inherits clm-llqd1n bound). Structural identification with disclosed fit. |
| clm-f8k2um | 0.3 | Per-element macroscopic-chemistry identifications are explicitly structural/interpretive; Si V_bi=1.0496V asserted as solver output, not derived in-leaf. Asserted-partial. |
| clm-rw7jqo | 0.6 | Single-ratio regime gate on V_R/V_BR is mechanically applied per element; 0.000000% closures disclosed as optimizer tolerance under assumed topology (inherits clm-llqd1n/clm-jy8h1x). Disclosed bound. |
| clm-sd04x4 | 0.3 | EE-archetype names are analogies; coupling-pair/SPICE counts follow combinatorially from assumed topology (not independent predictions); C-12 92.16 MeV is the fit summation. Asserted-structural. |
| clm-y7uvdc | 0.3 | Per-element soliton placements (angles/tracks) are structural identifications extracted from figure captions; no quantitative IE/fine-structure derivation here. Asserted-partial. |
| clm-h8nmpu | 0.3 | Visualization leaves: flux-pattern callouts + narrative captions, no equations beyond the established 1/r field; anisotropy→property links interpretive. Asserted-structural. |

## Flags

- **clm-ome498 (g_* row):** the baryon-asymmetry η agreement is a multi-factor composite (g_*, α_W⁴, C_sph=28/79, κ_FS=8π) and the claim-quality prose itself notes overlap with vol3 `effective-degrees-of-freedom`. A vol3 clm-dep likely exists but I could not confidently identify the id from vol6 alone — OMITTED to avoid a wrong/cyclic edge. The two λ_H/g_* author scope-corrections (shared N_K4) are preserved verbatim; both pin the 0.5 band.
- **clm-7tk051 depends on the radial-eigenvalue ODE solver + per-correction derivation leaves** (Be cascade, Mg SIR, Al/Si Op10, Correction D). These are framework/operator imports, not separate clm- entries in vol6; expressed as framework deps. No vol≤5 clm- for the base ODE solver was confidently locatable — noted, not invented.
- **Per-element manifestation cluster (f5ucdo, f8k2um, rw7jqo, sd04x4, y7uvdc, h8nmpu):** all 14-leaf bundles; I sampled boron/silicon/hydrogen representative leaves rather than all 84 leaves. Sampling was consistent with the claim-quality prose; no stale/inconsistent leaf found. Cross-links among these point earlier in doc order (acyclic).
- **ACYCLIC-BUT-LISTING-FORWARD edge to verify:** clm-llqd1n (entry #1 in the file) declares `depends-on: clm-lqanmt` (entry #2). This is physically correct — the mass-defect accuracy *uses* the mutual coupling constant K — and is **acyclic in the claim graph**: clm-lqanmt's own depends-on is only Axiom 1/2, with NO back-edge to clm-llqd1n (verified at the lqanmt entry). It is "forward" only in document listing order, not in the dependency DAG. A topological-sort-based CI check will accept it; a naive line-order check would flag it. Flagging for the central verifier: the edge should be kept (reversing or dropping it would be wrong physics). If CI uses strict file-order acyclicity, the fix is to reorder the two entries (K before mass-defect), not to drop the edge.
- No other cyclic or missing intra-vol6 clm-deps detected; all 23 ids resolve via grep; every other cited clm-dep points strictly earlier in document order.
