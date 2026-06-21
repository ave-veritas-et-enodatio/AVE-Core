# Vol 1 — Foundations — Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from vol1/index.md bootstrap directive -->

> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting claim-quality register](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth for which tripwires are project-wide; do not infer the list from this preamble). Entries below are scoped to Vol 1; cross-cutting tripwires with vol1-specific manifestations are noted but not duplicated.

---

## Electron Body Topology — $0_1$ Unknot with $(2,3)$ Phase-Space Winding
<!-- id: clm-unk0bd -->

The electron's intrinsic body in physical 3D space is a $0_1$ unknot — a single closed flux-tube loop (topologically trivial in real space) at minimum ropelength $= 2\pi$, with circumference $\ell_{node}$ and tube radius $\ell_{node}/(2\pi)$. The $(2,3)$-torus-knot ("trefoil") structure is the electron's **phase-space Clifford-torus winding pattern** (2 windings on the d-axis, 3 on the q-axis), not a real-space body knot. **Canonical as of the 2026-05-17 body-topology resolution** (`framing-concordance.md` sweep C) — superseding the former `clm-trf3bd` real-space-trefoil-body position, which is retired. Held across Vol 1 Ch 0, Ch 1 (calibration-cutoff-scales), Ch 3, Ch 5, Ch 8 (α derivation), and the Vol 6 periodic table.

- _Specific Claims_
  - The electron's real-space body is the $0_1$ unknot — a single closed flux-tube loop of trivial knot type, at minimum ropelength $= 2\pi$ in $\ell_{node}$ units.
  - The $(2,3)$ trefoil winding is a **phase-space** structure (on the Clifford torus $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$), not a real-space knot. It is the geometric basis for the cold-lattice α derivation $\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi$ via the three-regime closure (entry `clm-0ktpcn`).
  - Mass formula: $m_e = T_{EM} \cdot \ell_{node}/c^2 = \hbar/(c \cdot \ell_{node})$, from the unknot's 2π ropelength × the EM tension $T_{EM}$.
  - Spin-1/2 arises from the AVE-native $SU(2) \to SO(3)$ 2-to-1 cover: K4 rotation group $T = A_4$ → double cover $2T \subset SU(2)$ → the Finkelstein–Misner / Dirac-belt-trick mechanism acting on the extended $0_1$ unknot defect (Vol 1 Ch 8 §Topological identity of the electron; Ch 1 k4-rotation-group).
  - The three lepton generations (electron, muon, tau) arise from Cosserat-sector excitations (translation, torsion, curvature-twist) of this unknot geometry.
  - Stability comes from impedance mismatch: at the saturated boundary $Z \to 0, \Gamma \to -1$, internal acoustic energy is fully reflected inward as a standing wave (= rest mass).

- _Specific Non-Claims and Caveats_
  - **Topological protection is established at the phase-space level, scope-correct (closed 2026-05-25 Phase 2 sub-item 4).** The $0_1$ unknot real-space body is trivially knotted — no real-space knot-theoretic invariant to preserve. Genuine topological protection comes from the $(2,3)$ phase-space winding numbers on the Clifford torus, which ARE bona-fide topological invariants. K4-TLM lattice simulation (32³ Diamond lattice with two saturated walls + $2\pi$ phase-wound thread, canonical at [`phase-locked-topological-thread.md`](./dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md), clm-zuf7g1) empirically demonstrates that vacuum and $T \ll T_{pair}$ noise scenarios are statistically indistinguishable — the winding is topologically protected against continuous deformations. Topology change above the Schwinger pair-creation threshold ($T \gg T_{pair} \approx 1.19 \times 10^{10}$ K, $V \to V_{snap} \approx 511$ kV) occurs via the canonical AVE pair-creation mechanism (clm-ezai5b); above that threshold the substrate undergoes a phase transition rather than a continuous deformation, so the topological invariant is broken by topology change, not by violation. Read leaves' "topologically protected soliton" language at the phase-space level, scoped to sub-pair-threshold dynamics.
  - **The spin-1/2 / photon-720° compatibility issue is resolved (closed 2026-05-25 Phase 2 sub-item 3).** The Möbius / $720°$ structure is canonical for the electron's chiral $K_4$ extended-defect topology (per [`phase-locked-topological-thread.md`](./dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md) line 112, clm-zuf7g1). The loose framing that motivated the photon-720° concern — "the substrate-as-a-whole carries $4\pi$, therefore every wave on it inherits $4\pi$" — is scope-clarified, not retracted: the Möbius mechanism applies to closed extended defects (electron unknot, other torus-knot solitons), not to bulk propagation modes. The Finkelstein-Misner derivation ([`finkelstein-misner-spin-half-derivation.md`](../vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md) §6.5, clm-salw2h) makes this explicit via two independent arguments: (i) the FM theorem requires extended closed loops in SO(3) — photons are open propagating modes, the theorem does not apply; (ii) the Hopf-fibration projection $SU(2) \to S^2$ drops the U(1) fibre phase that carries the $4\pi$ closure — photons live at the Hopf-projected $S^2$ level, having already been integrated past the SU(2) double-cover. Both arguments are structural; no "final determination deferred" is outstanding.
  - The $m_e = \hbar/(c \cdot \ell_{node})$ relation carries one input scale: one of $\{m_e, \ell_{node}\}$ remains an empirical input (see Closure Status `clm-5xon03`).

> **Leaf references:** [calibration-cutoff-scales](./axioms-and-lattice/ch1-fundamental-axioms/calibration-cutoff-scales.md), [ch8-alpha-golden-torus](./ch8-alpha-golden-torus.md), [phase-locked-topological-thread](./dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md), [quantum-foam-virtual](./dynamics/ch3-quantum-signal-dynamics/quantum-foam-virtual.md), [scale-invariance](./operators-and-regimes/ch5-universal-spatial-tension/scale-invariance.md), [scale-invariant-predictions](./operators-and-regimes/ch5-universal-spatial-tension/scale-invariant-predictions.md).

### Quality
- confidence: 0.65
- depends-on:
  - Axiom 1 (Substrate Topology — the electron body is a $0_1$-unknot flux-tube in the K4 substrate at the $\ell_{node}$ scale)
  - clm-8c3yhs — $(2,3)$ torus-knot uniqueness derivation in `vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md` supplies the coprimality + both-windings-$\geq 2$ + minimality + electron-is-lightest chain that forces $(2,3)$ as the electron's phase-space winding (Phase 2 sub-item 1; the $(2,3)$ vs $(4,3)$, $(5,2)$, etc. enumeration is derived, not asserted)
  - clm-salw2h — Finkelstein-Misner spin-½ derivation in `vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md` supplies the extended-defect $SU(2) \to SO(3)$ double-cover mechanism that establishes spin-½ as K4-native AND explains why open propagating photons do NOT inherit the $4\pi$ closure (Phase 2 sub-item 3, §6.5 of the FM leaf)
  - clm-zuf7g1 — Phase-locked entanglement-thread + K4-TLM topological-protection empirical demonstration in `vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md` (32³ Diamond lattice simulation with $2\pi$ phase-wound thread, vacuum + $T \ll T_{pair}$ statistically indistinguishable; $T \gg T_{pair}$ destroys winding via Schwinger pair creation per clm-ezai5b) establishes that the $(2,3)$ phase-space winding gives topological protection against continuous deformations below the pair-creation threshold (Phase 2 sub-item 4)
- solidity: 0.65 (ok to build on, see caveats) [= min(0.65, 0.65)]
- rationale: The 0_1-unknot real-space body + (2,3) phase-space winding is the canonical post-2026-05-17 position and the mass relation m_e = ℏ/(c·ℓ_node) is dimensionally clean. **2026-05-25 Phase 1**: the Finkelstein-Misner spin-1/2 derivation landed as canonical leaf at `vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md` (clm-salw2h promotion of L3 doc 23): extended-unknot twist-and-unwind mechanism + group-theoretic $K_4 \to A_4 \to 2T \subset SU(2)$ chain + gyroscopic-isomorphism numerical anchor at $10^{-8}$ + K4-native-vs-imported decomposition. **2026-05-25 Phase 2 sub-item 1**: the prior "(2,3) winding asserted, not derived" caveat closed via depends-on edge to `torus-knot-uniqueness.md` (clm-8c3yhs, confidence 0.70, solidity 0.70) — coprimality + both-windings-≥2 + minimality + electron-is-lightest. **2026-05-25 Phase 2 sub-item 3**: the spin-1/2 / photon-720° compatibility caveat closed via the FM leaf's new §6.5 — the $4\pi$ lives on the extended unknot defect via two independent arguments (FM extended-defect requirement + Hopf-fibration projection drops the U(1) fibre); photons are open propagating modes, do not inherit. **2026-05-25 Phase 2 sub-item 4**: the topological-protection caveat closed via depends-on edge to `phase-locked-topological-thread.md` (clm-zuf7g1, confidence 0.60, solidity 0.55) — K4-TLM 32³ simulation empirically demonstrates phase-space-winding-protection against continuous deformations below $T_{pair}$; topology change above $T_{pair}$ is the canonical Schwinger pair-creation mechanism (clm-ezai5b), not a violation of the protection. Note that clm-unk0bd is co-hosted on the same leaf (`phase-locked-topological-thread.md` frontmatter `claims: [clm-zuf7g1, clm-b9eura, clm-unk0bd]`) as its new depends-on target clm-zuf7g1; the depends-on edge expresses the load-bearing dependency (electron protection mechanism rests on the K4-TLM empirical demonstration that the entanglement-thread leaf hosts), distinct from the leaf-level co-hosting. With all 4 strengthen-by items closed (sub-items 1+2+3+4), confidence bumps 0.55 → 0.65. The remaining caveat is the empirical $\{m_e, \ell_{node}\}$ input-scale (closure-status `clm-5xon03` dependency), which is a structural-closure question rather than a body-topology gap. **Solidity LIFTED 0.55 → 0.65 on 2026-05-26 Phase 2-A closure**: clm-ldmvwi (Born Rule from Ohmic Measurement Work) was strengthened from solidity 0.55 → 0.65 via the master-equation-derivation-path workstream (5-session arc on `analysis/clm-ldmvwi-master-eq-stochastic-derivation`; full derivation-path documented in clm-ldmvwi rationale). The cascade clm-ldmvwi 0.65 → clm-zuf7g1 0.65 (capped by own confidence) → clm-unk0bd 0.65 (= min(own confidence 0.65, clm-8c3yhs 0.70, clm-salw2h 0.70, clm-zuf7g1 0.65) — at the 0.65 confidence ceiling) closes the cone-lift. **clm-unk0bd is now at its own confidence ceiling**; to lift further would require closing the remaining caveat in the Non-Claims block (substrate-mechanism-class question on real-space topological protection vs phase-space-only protection — see Non-Claims caveat above; framework-extension question, not a derivation gap).
- strengthen-by:
  - (Currently empty after Phase 2-A closure. The prior "Strengthen clm-zuf7g1" item is retired — clm-zuf7g1 is now at its own confidence ceiling 0.65, equal to clm-unk0bd's confidence, so further work on clm-zuf7g1 alone would NOT lift clm-unk0bd until clm-unk0bd's own confidence rises. The next solidity lift on clm-unk0bd is a framework-extension question — see Non-Claims caveat block on real-space topological protection vs phase-space-only protection — not a derivation gap.)
---

## Zero-Parameter Closure Status (Conditional on Embedding-Selection AND Thermal Closure)
<!-- id: clm-5xon03 -->

The framework's "zero free parameters" headline rests on a layered closure that is currently *conditional on two distinct open formal items*. Vol 1's own ch0 introduction and Ch.8 disclose both; reviewers should not read the headline without the conditions.

**Gating item 1 (upstream — RESOLVED 2026-05-31 via Q-EMBED-SEL-1 Phase 1+2+3).** The 2026-05-28 sharpened gating clause that made the closure contingent on ropelength-minimality embedding-selection is RESOLVED by the Q-EMBED-SEL-1 substrate-mechanism work (commits `66d63503` + `b509767a` + `ecfe9c13`; audit tag `audit/2026-05-31_q-embed-sel-1-substrate-mechanism`; merged via PR #59 at `7529f7ce`). The substrate-mechanism for $R \cdot r = 1/4$ now closes at Class B substrate-mechanism manifestation via Axiom 4 self-saturation + Op14 Meissner-asymmetric + named phasor-area-equals-Nyquist-cell-area identification (canonical at [`research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md`](../../../research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md) §2.3); cross-particle universal at Phase 2; cross-domain universal at Phase 3. Class B caveat: the named identification is substrate-canonical INPUT (not Class 2 axiom-emergence from K4 + Cosserat primitives alone); a Class 2 lift candidate workstream is identified per Phase 1 result §7.3. Canonical anchor: [`ch8-alpha-golden-torus.md`](./ch8-alpha-golden-torus.md) §"Substrate-mechanism provenance of regime (c)".

**Gating item 2 (downstream — δ_strain magnitude; thermal-closure route CLOSED NEGATIVE).** With Gating item 1 resolved at Class B substrate-mechanism manifestation level via Q-EMBED-SEL-1, the cold-lattice asymptote $\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi$ bridges to CODATA at $T_{\text{CMB}}$ via the CMB-strain coefficient $\delta_{\text{strain}}$. The structure (existence + sign) is substrate-predicted; the **magnitude** route was attempted as Q-DELTA-MAP-1-quant (FT-1, 2026-05-31) and **CLOSED NEGATIVE** — the E-mode Bose-Einstein occupation undershoots $\eta_\varepsilon$ by ~31 OOM and is generic-thermal (not AVE-distinct), so $\delta_{\text{strain}}$'s magnitude stays a **definitional residual** ($1-$CODATA$/\alpha_\text{cold}$), not a derivable thermal observable (see below). All three NAMED α-routes to a Class 2 lift are now closed-negative: per the 2026-06-04 golden-torus bijection closure, both named lift-routes (selection + bijection) closed Class B, and the separate $z_0$-from-K4 (rigidity-percolation) route closed-NEGATIVE 2026-06-15 via the exact $z_{\text{eff}} \to 6$ Maxwell–Calladine count (`alpha_free_map_to_137_exists = False`). <!-- 🔴 Rule-12 2026-06-19 z₀-route propagation: prior wording "leaving only the separate $z_0$-from-K4 route open" superseded — that route is now closed-NEGATIVE per `research/2026-06-15_alpha-crystal-mc-count_result.md`. --> Scoped-echo register (Grant ratified 2026-06-18): the α-value is a **standing echo** — closed-negative on all named routes, flip-condition live ($R \cdot r = 1/4$ forced without α-circularity would flip it), route-space not provably exhausted. The framework is **Class B substrate-mechanism manifestation** with α a **named geometric identification**.

- _Specific Claims_
  - Vol 1 reduces 26 Standard Model parameters to a 3-element bounding set $\{m_e, \alpha, G\}$ + four axioms.
  - **Predicted (axiom-derived):** the cold-lattice asymptote $\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038$ (Ch.8); the existence and sign of a positive thermal running of $\alpha^{-1}$ below this asymptote at $T > 0$; the falsifiable claim that $\alpha^{-1}$ decreases further in regions of higher local thermal energy.
  - **Definitional residual (one scalar at $T_{\text{CMB}}$):** the numerical magnitude $\delta_{strain} \approx 2.225 \times 10^{-6}$ is back-subtracted from CODATA, definitional given the engine's `DELTA_STRAIN = 1 - (1/ALPHA)/ALPHA_COLD_INV` — NOT a derived thermal observable. The substrate-mechanism class for this loading is **identified** as Cosserat-rotation-sector mass-gap thermal-mode-population ASYM (Q-DELTA-MAP-1 closed at mechanism-class identification 2026-05-28; canonical leaf [`delta-strain-cosmic-tcc.md`](../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md), clm-hp7nlm), and it correctly predicts the SIGN of α-vs-T running. But the candidate quantitative derivation **Q-DELTA-MAP-1-quant** was **ATTEMPTED and CLOSED NEGATIVE** (FT-1, 2026-05-31): the E-mode Bose-Einstein occupation undershoots $\eta_\varepsilon$ by ~31 OOM (BE suppresses below equipartition at $T_{CMB} \ll \Theta_\text{Debye}$, cannot amplify) and is generic-thermal, not AVE-distinct. The genuine thermal α-drift the mechanism predicts is $\sim 10^{-38}$ (unobservable; sign-only). So the magnitude is **not** derived — it is a definitional residual.
  - **Tested:** that *one* thermal scalar suffices to bridge the cold-lattice asymptote to CODATA across temperature regimes (collider cores, primordial $\alpha$, ultracold cavity).
- _Specific Non-Claims and Caveats_
  - Does NOT claim full ab-initio derivation of the CODATA $\alpha$ from axioms alone in the current edition. The cold-lattice α value $\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi$ is a **named geometric identification** (Class B substrate-mechanism manifestation, not Class 2 axiom-emergence; both golden-torus lift-routes — selection + bijection — closed Class B 2026-06-04), and the $\delta_{strain}$ magnitude bridging it to CODATA is a **definitional residual** ($1-$CODATA$/\alpha_\text{cold}$), NOT a derivable thermal observable. The earlier "structurally zero-parameter conditional on thermal closure of $\delta_{strain}$" framing is superseded: the thermal-closure route was **attempted and closed NEGATIVE**. Q-DELTA-MAP-1 (substrate-saturation-class identification for low-amplitude electromagnetic thermal-bath loading) is **closed at mechanism-class identification** 2026-05-28 via the Cosserat-rotation-sector mass-gap thermal-mode-population ASYM mechanism (canonical at [`delta-strain-cosmic-tcc.md`](../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md), clm-hp7nlm), and it predicts the SIGN correctly. But **Q-DELTA-MAP-1-quant** — the quantitative E-mode dispersion + Bose-Einstein-occupation derivation of $\eta_\varepsilon$ — was **CLOSED NEGATIVE** (FT-1, 2026-05-31): it undershoots by ~31 OOM and is generic-thermal, not AVE-distinct. The mechanism-class identification + its weak-force $\gamma_c$ joint-constraint SURVIVE; only the magnitude-derivation route is closed. (See [`research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md`](../../../research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md) for the forward derivation + honest closure; [`research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md`](../../../research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md) §3 for the original candidate paths P1/P2/P3; clm-hp7nlm hosts the fourth path P4.)
  - Does NOT claim $\ell_{node}$ and $m_e$ are independently derived. Per Ch.8 closure status (c): one of $\{m_e, \ell_{node}\}$ remains the input mass scale; the other follows via the unknot ground state.
  - Summaries that cite "$4\pi^3 + \pi^2 + \pi = 137.0363038$" without the CMB-correction caveat conflate the predicted cold-lattice asymptote with the measured CODATA value (these differ at the ~$2\times 10^{-6}$ level, requiring the fitted $\delta_{strain}$).

> **Leaf references:** [calibration-cutoff-scales](./axioms-and-lattice/ch1-fundamental-axioms/calibration-cutoff-scales.md), [ch0-intro](./ch0-intro.md), [ch8-alpha-golden-torus](./ch8-alpha-golden-torus.md).

### Quality
- confidence: 0.70
- depends-on:
  - clm-unk0bd — Electron Body Topology = Unknot (solidity 0.65) [closure condition (c) "via the unknot ground state" formulation]
- solidity: 0.65 (ok to build on, see caveats) [= min(0.70, 0.65)]
- rationale: Structural reduction of 26 SM parameters to $\{m_e, \alpha, G\}$ + four axioms is sound and explicit; conditionality on $\delta_{strain}$ magnitude derivation, Nyquist-independence proof for $m_e/\ell_{node}$, and $G$ closure independent of $R_H$ is correctly disclosed. **Refined (2026-05-06 session):** closure condition (c) — "one of $\{m_e, \ell_{node}\}$ being computable from the other via the unknot ground state" — is body-topology-dependent. The 2026-05-17 body-topology resolution (`clm-unk0bd` canonical — $0_1$ unknot real-space body with $(2,3)$ phase-space winding) closed the prior trefoil-vs-unknot conditionality; condition (c)'s "via the unknot ground state" formulation is consistent with the canonical body topology. The dimensional formula $m_e = \hbar/(c \cdot \ell_{node})$ holds regardless, but the derivation chain that closes one input from the other requires body-topology-specific argument. Local confidence 0.70 reflects honest disclosure of the closure conditions. **Post-Phase-2-A cascade lift (2026-05-26):** solidity is 0.65 (= min(0.70, 0.65)) following the clm-unk0bd lift to solidity 0.65 — closure condition (c) now inherits the strengthened body-topology root rather than the 2026-05-06-era trf3bd-rebound 0.40 figure. **2026-05-27 Phase 3-A3 WALK-BACK** (branch `analysis/phase-3-a3-delta-strain-machian-projection`): the open closure-condition item on $\delta_{strain}$ magnitude derivation reworded substrate-natively from "G_vac + equipartition" (SM-vocabulary) to **Q-DELTA-MAP-1** substrate-saturation-class adjudication. Phase 3-A3 attempted to formalize $\delta_{strain}$ as a 5th Machian-G Class E operating-point projection but Step 3.5 audit found the proposed derivation chain inconsistent with canonical clm-3zz0f6 SYM α-invariance (the $c_{eff} = c_0\sqrt{S}$ substitution corresponds to $c_{shear}$, not $c_{EM}$, per clm-8nkvwy; substituting the correct $c_{EM} = c_0/S$ in SYM gives α invariance per clm-3zz0f6). Class E framework membership in the Machian-G cosmic-substrate family is canonical; promoting $\delta_{strain}$ to a 5th projection was GATED on Q-DELTA-MAP-1 substrate-mechanism closure. Confidence STAYS at 0.70 (no derivation-rigor improvement; vocabulary cleanup only). Full result documentation at [`research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md`](../../../research/2026-05-28_phase-3-a3-delta-strain-machian-projection-result.md). **2026-05-28 Q-DELTA-MAP-1 closure at mechanism-class identification**: the substrate-mechanism class for δ_strain is now identified as Cosserat-rotation-sector mass-gap thermal-mode-population ASYM (canonical at [`delta-strain-cosmic-tcc.md`](../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md), clm-hp7nlm). The Class E promotion gate then stood on **Q-DELTA-MAP-1-quant** (quantitative substrate-statistical-mechanics derivation of $\eta_\varepsilon$ within the now-identified mechanism class) rather than the mechanism-class-identification step. Confidence STAYS at 0.70 (mechanism-class identification is a substrate-physics content gain at clm-hp7nlm). **2026-05-31 FT-1 — Q-DELTA-MAP-1-quant CLOSED NEGATIVE** (landed via the 37a946da walk-back; anchor [`research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md`](../../../research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md)): the quantitative E-mode Bose-Einstein occupation derivation of $\eta_\varepsilon$ undershoots by ~31 OOM and is generic-thermal, not AVE-distinct. So the closure-status framing is now sharpened: the cold-lattice α is a **named geometric identification** (both golden-torus lift-routes closed Class B 2026-06-04) and the $\delta_{strain}$ magnitude is a **definitional residual**, NOT pending a thermal derivation — the magnitude-derivation route is closed negative. The SIGN-mechanism + weak-force $\gamma_c$ joint-constraint SURVIVE. clm-5xon03 confidence STAYS at 0.70 (magnitude-only re-scope; no derivation-rigor change either direction).
- strengthen-by:
  - **Q-DELTA-MAP-1-quant** — **ATTEMPTED → NEGATIVE (FT-1, 2026-05-31)**: the quantitative substrate-statistical-mechanics derivation of $\eta_\varepsilon$ at $T_{CMB}$ within the Cosserat-Curie mechanism (compute substrate E-mode dispersion + Bose-Einstein occupation, couple to substrate dielectric response, match to canonical $\eta_\varepsilon \approx 4.45 \times 10^{-6}$) was run and **undershoots the target by ~31 OOM** (BE occupation gives $\sim 10^{-38}$; at $T_{CMB} \ll \Theta_\text{Debye}$ it suppresses *below* equipartition by ~28.5 OOM and cannot amplify), AND per the SM-counterfactual even a match would be generic-thermal, not AVE-distinct. This magnitude-derivation route is **closed**; δ_strain stays a **definitional residual** ($1-$CODATA$/\alpha_\text{cold}$), not substrate-derived. The mechanism-class identification at clm-hp7nlm + its weak-force $\gamma_c$ joint-constraint are unaffected. Anchor: [`research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md`](../../../research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md). (Reinforced by the 2026-06-04 golden-torus bijection closure: $\alpha^{-1} = 4\pi^3+\pi^2+\pi$ is a named identification on both lift-routes.)
  - Demonstrate Nyquist-resolution-of-smallest-stable-soliton without circular reference to $m_e$ (closes the $\{m_e, \ell_{node}\}$ input scale)
  - Derive $G$ from local thermodynamic balance (lattice tension, generation rate per node) independent of $R_H$ (closes the $H_\infty$ identity into a true downstream prediction)
---

## Golden Torus α Derivation (Three-Regime Closure)
<!-- id: clm-0ktpcn -->

- $\alpha^{-1}_{\text{ideal}} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038$
- _Specific Claims_
  - Three independent physical regimes — Nyquist quantization (regime a, $d = 1$), self-avoidance at trefoil crossings (regime b, $R - r = 1/2$), and Q-EMBED-SEL-1 Phase 1 substrate-mechanism (regime c, $R \cdot r = 1/4$ via Axiom-4 self-saturation + Op14 Meissner-asymmetric + named phasor-area-equals-Nyquist-cell-area identification, 2026-05-31) — together fix the Golden Torus geometry $R = \varphi/2$, $r = (\varphi-1)/2$.
  - The $\pi^2$ surface normalization derives substrate-mechanically from $R \cdot r = 1/4$ via $\Lambda_{\text{surf}} = 4\pi^2(R \cdot r) = \pi^2$ at the Golden Torus geometry (Q-EMBED-SEL-1 Phase 1 substrate-mechanism). The prior provenance via $\Lambda_{\text{surf}} = \tfrac{1}{2}A_{\text{standard}}$ with $A_{\text{standard}} = 2\pi^2$ (spinor half-cover of the standard Clifford torus surface area on $S^3$) is retired as load-bearing per doc 29 F5 + doc 39 §3.4 (QED-imported SU(2) projective-ray concern).
  - The $4\pi$ in $\Lambda_{\text{vol}}$ derives from bipartite K4 lobe-count (2 sublattices × $2\pi$ phasor rotation per lobe = $4\pi$ temporal-phase closure per observable Compton cycle, per `l3-electron-soliton-synthesis.md:103-105`) — substrate-native. The standard-physics translation reference is "SU(2) → SO(3) double cover applied temporally"; the substrate-mechanism content is K4 bipartite lobe-count, not an SU(2) postulate.
  - Numerical convergence is verified by an independent ropelength + Clifford-screening optimization (`ropelength_trefoil_golden_torus.py`) converging from arbitrary starting point to $(R, r) = (\varphi/2, (\varphi-1)/2)$.
- _Specific Non-Claims and Caveats_
  - The sum $\alpha^{-1}_{\text{ideal}} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}}$ is an **identification step** (the three orthogonal codimensions of the Clifford embedding map onto the three independent self-impedance contributions), not an additional derivation step. Orthogonality of the three sectors is what justifies the absence of cross-terms; this identification is a non-trivial part of the argument and should not be hand-waved as "obvious".
  - The cold-lattice value $137.0363038$ is the **absolute-zero asymptote**, not the measured CODATA value. CODATA $\alpha^{-1} = 137.035999$ requires the additional CMB-strain correction $\delta_{strain} \approx 2.225\times 10^{-6}$; see Zero-Parameter Closure Status entry above for the predicted/fitted split on $\delta_{strain}$.
  - $\Lambda_{\text{line}} = \pi \cdot d$ takes $\pi$ (not $2\pi$) because regime (b) self-avoidance fixes $d$ as the tube *diameter* (not radius). Summaries that quote $\Lambda_{\text{line}} = \pi$ without this convention warning lose the derivation of why it is not $2\pi$.

> **Leaf references:** [ch8-alpha-golden-torus](./ch8-alpha-golden-torus.md).

### Quality
- confidence: 0.63
- depends-on:
  - clm-unk0bd — Electron Body Topology = 0_1 Unknot with (2,3) Phase-Space Winding [supplies the (2,3) phase-space Clifford-torus winding the three-regime geometry is built on]
  - clm-8c3yhs — $(2,3)$ torus-knot uniqueness derivation (vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md) [direct dependency: regime (b) self-avoidance and regime (c) Ax 4 self-saturation (per Q-EMBED-SEL-1 Phase 1 substrate-mechanism, 2026-05-31) both presuppose the $(2,3)$ winding pattern as the electron's phase-space topology, now derived rather than asserted]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.63, 0.65)]
- rationale: The three regimes (Nyquist d=1, self-avoidance R−r=1/2, Ax 4 self-saturation R·r=1/4 per Q-EMBED-SEL-1 Phase 1 substrate-mechanism) cleanly fix the Golden Torus geometry and Λ_surf=π² is established at **Class B substrate-mechanism manifestation** per Q-EMBED-SEL-1 (`research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md` §2.3), but the sum α⁻¹ = Λ_vol+Λ_surf+Λ_line is an asserted multipole identification whose claimed orthogonality is not derived — and the leaf's own forms give Λ_vol=16π³(R·r) and Λ_surf=4π²(R·r), i.e. Λ_vol≡4π·Λ_surf, so the (R,r,d)→Λ map has only 2-dimensional image and "orthogonality" cannot mean parameter-independence. Reproducing CODATA to ~10⁻⁶ is a consistency match against the cold-lattice asymptote (with the separate fitted δ_strain), not an independent local derivation of the combination rule. **2026-05-25 Phase 2 sub-item 1**: the prior "(2,3) winding asserted as simplest stable" caveat is closed — `torus-knot-uniqueness.md` (clm-8c3yhs, confidence 0.70) provides the uniqueness via coprimality + both-windings-≥2 + minimality + electron-is-lightest. depends-on edge wired directly (the (2,3) winding is load-bearing in regime (b) self-avoidance AND regime (c) half-cover, so the direct edge is semantically appropriate). The dominant remaining gap is the sum-decomposition orthogonality (Λ_vol ≡ 4π·Λ_surf collinearity issue), which is unaffected by this closure. Confidence bumped 0.50 → 0.55 on 2026-05-25 to reflect one of four strengthen-by items closed. **2026-05-26 Phase 3-A1+Q2 prose reframe** (branch `analysis/clm-0ktpcn-phase-3-A1-Q2-prose-reframe`): chapter prose at `vol1/ch8-alpha-golden-torus.md` reframed to apply `consistency-vs-emergence` v1.2 dual-axis classification throughout — Class 2 axiom-manifestation for $(R, r, d)$ derivation from Ax 1+2+3 explicitly separated from Class B substrate-mechanism manifestation + Class 4 observable consistency for the additive assembly; standard-physics-community names ("fine-structure constant α", "multipole expansion", "SU(2) → SO(3) double cover") appear only as parenthetical translation references; the open functional-orthogonality / Schur question is preserved verbatim and labeled honestly. Q2 hygiene cleanup of 7 cascaded claim-quality entries (clm-2dwzib, clm-5xon03, clm-3kzmt9, clm-8ep2b4, clm-zw6mut, clm-82dxbj, clm-b2anl4) — stale 2026-05-06-era trf3bd-rebound breadcrumbs replaced with post-2026-05-17-resolution + post-2026-05-26-cascade-lift accurate language. Confidence bumps 0.55 → 0.60 to reflect the prose-reframe + hygiene-cleanup lift (no derivation work — classification-precision lift only). Solidity bumps to 0.60 (= min(0.60, 0.65)). The bigger structural gap — functional orthogonality of the additive assembly — remains open and is the explicit target of Phase 3-A2 (Schur orthogonality derivation; spawned in parallel with this work). **2026-05-26 Phase 3-A2 Schur-orthogonality WALK-BACK closure** (branch `analysis/clm-0ktpcn-phase-3-A2-schur-orthogonality`): four pre-registered routes attempted (Hodge/de Rham on S³; T_d on V_{4-port}; U(1)×U(1) Peter-Weyl on Clifford-torus angles; Op21 multi-mode mode-counting). Schur orthogonality of substrate-symmetry-group irreducible representations is NOT the load-bearing theorem — the canonical substrate group action (T_d on V_{4-port}) gives 2 irreps (A_1 ⊕ T_2, dims 1+3=4), not three irreps matching the 1+2+3 codimensional ordering of Λ_line, Λ_surf, Λ_vol. Routes 1, 2, 3 fail to close the additive assembly; Route 4 (Op21 mode-counting at Γ=-1 saturation boundary) DOES close at the Class B substrate-mechanism-manifestation level. The substrate-mechanism content is Nyquist-cell-count additivity over codimensional mode-categories at saturation boundary, canonical at `theorem-3-1-q-factor.md` §"Op21 multi-mode generalization" (paragraph-level statement). The (R·r)-collinearity issue is reframed: Λ_vol/Λ_surf = 4π IS the spinor-temporal phase factor (substrate SU(2) double-cover) per ch8 line 105, consistent with substrate-mechanism mode-category independence even where (R,r) parameter-space collinearity holds. Confidence STAYS at 0.60 (no derivation-rigor improvement — the substrate-mechanism path is already canonical, just under-cited from ch8 before this commit). Strengthen-by item reformulated below from "establish functional orthogonality (Schur)" to "promote Op21 multi-mode generalization to fully-derived canonical leaf". The chapter prose at `vol1/ch8-alpha-golden-torus.md` is updated to reflect the Op21 mode-counting reframe; the previously-listed "Schur orthogonality at substrate symmetry-group level" framing is replaced with the substrate-mechanism mode-counting path. Speculative future workstream candidate identified: T = A_4 has irreps A + E + T of dimensions 1+2+3 matching the codimensional ordering, but no canonical substrate Hilbert space carrying this representation is currently identified — substantive future workstream, not a near-term tweak. Full result documentation at [`research/2026-05-26_clm-0ktpcn-phase-3-A2-schur-orthogonality-result.md`](../../../research/2026-05-26_clm-0ktpcn-phase-3-A2-schur-orthogonality-result.md). **2026-05-27 Phase 3-A4 Op21 multi-mode mode-counting formalization closure** (branch `analysis/clm-0ktpcn-phase-3-A4-op21-formalization`; **AMENDED 2026-05-27 post-PR-#47-auditor — PARTIAL band lift, not PASS band**): the substrate-mechanism path for the additive assembly is now FORMALIZED at canonical-leaf rigor at [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md) under the **substrate-orthogonal-channel framing** (each $\Lambda_k$ INDEPENDENTLY constrained by its own substrate-axiom source: $\Lambda_{\text{line}}$ by Ax 1 Nyquist + Ax 2 (b)-diameter convention; $\Lambda_{\text{surf}}$ by Ax 3 spatial half-cover via K4 rotation-group chain $T = A_4 \to 2T \subset SU(2) \to SO(3)$; $\Lambda_{\text{vol}}$ by Ax 3 + same K4 chain expressed temporally — substrate-spinor temporal-4π closure). Cross-term-freeness in the additive assembly is identified as a *consequence* of Nyquist-cell-category mutual exclusivity at the saturation boundary (per ch8 line 125 verbatim *"modes in distinct Nyquist-cell categories at the saturation boundary are mutually exclusive cell categories and add without cross-terms"*), NOT a separate additivity postulate. The substrate-mechanical reason $\Lambda_{\text{line}} = \pi$ (NOT $\pi\varphi = 2\pi R$) is made explicit: $\Lambda_{\text{line}}$ is the substrate Ampère 1-cycle around the tube's cross-section perimeter at Nyquist-quantized $d = 1$, NOT the Clifford-torus major-loop perimeter at the Golden Torus major radius. The substrate-foundational Op21 form $Q = \ell$ at Γ = -1 is cross-scale canonical with two distinct channel-multiplicity modes (single-channel wavelength-counting at BH ringdown / QNM / knot-mode isomorphism / universal substrate-Q derivation procedure; substrate-orthogonal-channel mode-counting at electron LC tank multi-codim assembly). The operators.md:61 dual-identification annotation is softened per ave-evidence-framing-discipline: the Bardeen $Q \sim 1/\ln(Z_1/Z_0)$ form is *conjectured* to be a Cooper-pair-phase-transition specialization of the substrate-foundational $Q = \ell$ form, but the explicit reduction $Q = \ell \to 1/\ln(Z_1/Z_0)$ via substrate-impedance integration is NOT yet derived (logged as Q-OP21-BARDEEN-1 candidate framework-extension question, NOT closure-asserted). Classification: **Class B substrate-mechanism manifestation** on the additive-assembly substrate-mechanism axis — matches `ch8-alpha-golden-torus.md:148` self-classification verbatim — NOT lifted to Class 2 axiom-manifestation by Phase 3-A4 (the Clifford-torus codimensional embedding remains canonical input from upstream leaves rather than re-derived from K4 substrate primitives; a Class 2 lift would require that further substrate-mechanism workstream). Confidence bumps **0.60 → 0.63** (PARTIAL band lift, NOT PASS band; reflects formalization-rigor improvement + load-bearing-assumption explicit-naming, NOT Class 2 emergence). The original 2026-05-27 implementor cycle reported 0.60 → 0.65 PASS band; auditor PR #47 review walked back to 0.60 → 0.63 PARTIAL band per Rule 12 substitution-not-retraction discipline. Cascade lifts the 21+ dependents whose own confidence ≥ 0.63 to solidity 0.63; those below stay at own ceiling. Full prereg at [`research/2026-05-27_clm-0ktpcn-phase-3-A4-op21-formalization-prereg.md`](../../../research/2026-05-27_clm-0ktpcn-phase-3-A4-op21-formalization-prereg.md); full result documentation (with amended §4 classification, §8 PARTIAL verdict, §11 walk-back provenance) at [`research/2026-05-27_clm-0ktpcn-phase-3-A4-op21-formalization-result.md`](../../../research/2026-05-27_clm-0ktpcn-phase-3-A4-op21-formalization-result.md).
- strengthen-by:
  - **(PARTIAL closure — amendment-revised 2026-05-27 post-PR-#47-auditor)** Promote the Op21 multi-mode generalization at `theorem-3-1-q-factor.md` §"Op21 multi-mode generalization" to a fully-derived substrate-mechanism canonical leaf. *Partial closure status*: Phase 3-A4 delivered the canonical-leaf formalization at [`op21-multi-mode-mode-counting.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md) with the substrate-orthogonal-channel framing (each Λ_k INDEPENDENTLY constrained by its own substrate-axiom source; cross-term-freeness as a consequence of Nyquist-cell-category mutual exclusivity) replacing the Phase 3-A2-falsified Schur orthogonality framing — but at **Class B substrate-mechanism manifestation** rigor only (NOT Class 2 axiom-manifestation: the Clifford-torus codimensional embedding remains canonical input from upstream leaves, not re-derived from K4 substrate primitives). The formalization-rigor lift is real; the Class 2 closure remains open. See next strengthen-by item for the Class 2 closure path.
  - **(NEW 2026-05-27 post-PR-#47-auditor)** Substrate-mechanism derivation of the Clifford-torus codimensional embedding ($\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ with the three codimensional sub-manifolds — flux-tube transverse cross-section 1-cycle / Clifford-torus surface / Clifford-torus surface × spinor-temporal $S^1_{4\pi}$) from K4 substrate primitives. The Phase 3-A4 substrate-orthogonal-channel framing makes each per-channel Λ_k INDEPENDENTLY constrained by its own substrate axiom, but treats the codimensional embedding as canonical input from upstream leaves. A Class 2 axiom-manifestation lift on the additive assembly $Q_{\text{tank}} = \sum_k \Lambda_k$ would require re-deriving the embedding itself from the K4 lattice's discrete cell structure (i.e., showing why K4 substrate phase-space self-organizes into the three codimensional sub-manifolds at the $\Gamma = -1$ saturation boundary, rather than treating the embedding as canonical content). This would lift Phase 3-A4 from Class B substrate-mechanism manifestation to Class 2 substrate-mechanism axiom-manifestation. Substantive substrate-mechanism workstream candidate.
  - **Q-DELTA-MAP-1-quant** — **ATTEMPTED → NEGATIVE (FT-1, 2026-05-31)**: the quantitative substrate-statistical-mechanics derivation of the δ_strain magnitude at $T_{CMB}$ within the Cosserat-rotation-sector mass-gap thermal-mode-population ASYM mechanism (canonical at [`delta-strain-cosmic-tcc.md`](../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md), clm-hp7nlm) was run and **undershoots by ~31 OOM** (E-mode Bose-Einstein occupation gives $\sim 10^{-38}$; suppresses *below* equipartition at $T_{CMB} \ll \Theta_\text{Debye}$) and is generic-thermal, not AVE-distinct. The magnitude does **not** lift to substrate-derived — δ_strain stays a **definitional residual** ($1-$CODATA$/\alpha_\text{cold}$); the cold-lattice α is a **named geometric identification** (all three named routes closed-negative — both golden-torus lift-routes closed Class B 2026-06-04; $z_0$-from-K4 rigidity-percolation closed-NEGATIVE 2026-06-15 via the exact $z_{\text{eff}} \to 6$ Maxwell–Calladine count). <!-- 🔴 Rule-12 2026-06-19 z₀-route propagation: prior "only $z_0$-from-K4 open" superseded — closed-NEGATIVE per `research/2026-06-15_alpha-crystal-mc-count_result.md`; α-value = scoped standing echo (Grant ratified 2026-06-18). --> This closes the magnitude-derivation route; the mechanism-class identification + weak-force $\gamma_c$ joint-constraint are unaffected. Anchor: [`research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md`](../../../research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md).
  - (Speculative future workstream) Identify a canonical substrate Hilbert space on which T = A_4 acts with irrep decomposition A + E + T (dims 1 + 2 + 3 matching codimensional ordering); if such a substrate Hilbert space can be identified and the (R, r, d)-fixed substrate kernel decomposes onto its irreps, Schur orthogonality WOULD close the additive assembly at the Class 2 axiom-manifestation level via a distinct path. This is a substantive future workstream, not a near-term tweak — Phase 3-A2 establishes it as the most promising structural-match candidate. **Note (2026-05-27, AMENDED)**: Phase 3-A4 formalized the additive-assembly substrate-mechanism path via substrate-orthogonal-channel mode-counting at Class B substrate-mechanism manifestation rigor (NOT Class 2 axiom-manifestation — Clifford-torus codimensional embedding is canonical input, not K4-substrate-primitive-derived). The $T = A_4$ workstream remains an open structural-match candidate for a deeper Class 2 substrate-mechanism alternative; it is one of (at least) two paths to Class 2 closure (the other path being K4-substrate-primitive derivation of the Clifford-torus codimensional embedding, named in the strengthen-by item above).
---

## Vacuum Strain Coefficient $\delta_{\text{strain}}$ (CMB Thermal Running of $\alpha^{-1}$ — SIGN-only; magnitude a definitional residual)
<!-- id: clm-009nkt -->

- $\delta_{\text{strain}} = 1 - \alpha^{-1}_{\text{exp}}/\alpha^{-1}_{\text{ideal}} = 1 - 137.035999/137.0363038 \approx 2.225 \times 10^{-6}$
- _Specific Claims_
  - The cold-lattice asymptote $\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038$ (a named geometric identification; see clm-0ktpcn) is the $T \to 0$ limit; the measured CODATA value $137.035999$ sits below it by the fractional vacuum strain coefficient $\delta_{\text{strain}}$, narratively attributed to **substrate spatial-metric response to the cosmological CMB photon-bath operating environment** at $T_{\text{CMB}} \approx 2.725$ K. The substrate-mechanism class for this loading is **identified** as Cosserat-rotation-sector mass-gap thermal-mode-population ASYM (Q-DELTA-MAP-1 closed at mechanism-class identification 2026-05-28; canonical leaf [`delta-strain-cosmic-tcc.md`](../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md), clm-hp7nlm), and predicts the SIGN of the running — but the quantitative substrate-statistical-mechanics derivation of $\eta_\varepsilon$ at $T_{CMB}$ (Q-DELTA-MAP-1-quant) was **attempted and CLOSED NEGATIVE** (FT-1, 2026-05-31: ~31 OOM undershoot, generic-thermal not AVE-distinct), so the $\delta_{\text{strain}}$ magnitude is a **definitional residual**, not a derived thermal observable.
  - **Predicted (axiom-derived):** the *existence* of a positive thermal running of $\alpha^{-1}$ below the asymptote at any $T > 0$; the *sign* (substrate softens / expands at higher $T$); the falsifiable claim that $\alpha^{-1}$ decreases further in regions of higher local thermal energy (collider cores, early universe).
  - **Fitted (one scalar at $T_{\text{CMB}}$):** the numerical magnitude $\delta_{\text{strain}} \approx 2.225 \times 10^{-6}$, computed by back-subtraction from CODATA, $\delta_{\text{strain}} \equiv 1 - \alpha^{-1}_{\text{CODATA}}/\alpha^{-1}_{\text{ideal}}$, definitional given the engine's `DELTA_STRAIN = 1 - (1/ALPHA)/ALPHA_COLD_INV` (`src/ave/core/constants.py`).
  - **Tested:** that *one* thermal scalar suffices to bridge the cold-lattice asymptote to CODATA; multi-temperature $\alpha$ measurements (collider cores, primordial-nucleosynthesis $\alpha$, ultracold cavity experiments) test the same one-scalar structural claim at different $T$.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the *magnitude* is derived: it is one back-subtracted scalar (a Class A identity at the back-substitution step / **definitional residual**), not a substrate-physics derivation. The narrative attribution to substrate spatial-metric response to the CMB photon-bath operating environment is consistent with the predicted sign + the now-identified Cosserat-Curie mechanism (clm-hp7nlm at [`delta-strain-cosmic-tcc.md`](../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md)), but is not a magnitude derivation — and the candidate quantitative computation of $\eta_\varepsilon$ from substrate E-mode dispersion + Bose-Einstein occupation at $T_{CMB}$ (Q-DELTA-MAP-1-quant) was **attempted and CLOSED NEGATIVE** (FT-1, 2026-05-31): it undershoots by ~31 OOM (BE suppresses below equipartition at $T_{CMB} \ll \Theta_\text{Debye}$) and is generic-thermal, not AVE-distinct. The magnitude therefore stays a definitional residual; only the SIGN holds.
  - This is the **third distinct thermal running of $\alpha$** in AVE and must not be conflated with (a) standard QED vacuum polarization (different mechanism, different scale, above the $e^+e^-$ threshold), nor (b) the proton Skyrme thermal correction $\delta_{th} = 1/(14\pi^2) \approx 7.21 \times 10^{-3}$ at the $10^{13}$ K proton core (different temperature regime, different quantity — the Faddeev-Skyrme coupling $\kappa_{FS}$, not $\alpha$ directly).

> **Leaf references:** [ch8-alpha-golden-torus](./ch8-alpha-golden-torus.md).

### Quality
- confidence: 0.55
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation [the cold-lattice asymptote $\alpha^{-1}_{\text{ideal}} = 4\pi^3+\pi^2+\pi$ this residual is measured against]
  - clm-hp7nlm — δ_strain Substrate-Mechanism: Cosserat-Rotation-Sector Mass-Gap Thermal-Mode-Population ASYM [the substrate-mechanism identification closing Q-DELTA-MAP-1 at mechanism-class identification level; this entry is the observable identity, clm-hp7nlm is the substrate-mechanism leaf]
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.55, 0.55)]
- rationale: definitional-identity (the magnitude). The sign and existence of a positive thermal running of $\alpha^{-1}$ below the cold-lattice asymptote are axiom-derived (substrate spatial-metric response to finite-$T$ photon-bath loading); the magnitude $\delta_{\text{strain}} \approx 2.225 \times 10^{-6}$ is FITTED — one scalar back-subtracted from CODATA, definitional given the engine constant `DELTA_STRAIN`. It is NOT yet derived from substrate primitives. Distinct from QED vacuum polarization and from the proton Skyrme thermal correction $\delta_{th} = 1/(14\pi^2)$. Confidence 0.45 set by the applied-mathematician pass. **2026-05-27 Phase 3-A3 WALK-BACK** (branch `analysis/phase-3-a3-delta-strain-machian-projection`): the prework brief proposed deriving $\delta_{\text{strain}}$ from a Machian-G operating-point cascade ($u_0^* \to A_0^{cosmic}/A_{yield} \to$ INVARIANT-S2 SYM scaling $\to \alpha_{eff}/\alpha_{cold} = 1/S^{3/2}$). Step 3.5 audit found this derivation chain has a substantive substrate-physics inconsistency with canonical clm-3zz0f6 (α Invariance Under Symmetric Gravity, confidence/solidity 0.85): SYM-class scaling produces $\alpha$ exactly invariant via the canonical algebraic substitution $\alpha = e^2/(4\pi (\varepsilon_0 nS) \hbar (c_0/(nS))) = \alpha_0$, NOT modulated. The prework brief's $c_{eff} = c_0\sqrt{S}$ substitution corresponds to $c_{shear}$ (group/rest-mass-freeze velocity per clm-8nkvwy line 113), NOT the $c_{EM}$ phase velocity that enters $\alpha$ ($c_{EM,sym} = c_0/S$ per clm-8nkvwy line 111). The canonical saturation-class taxonomy (SYM mass-energy loading + ASYM strong-EM loading per clm-8nkvwy) does NOT include a third class for low-amplitude electromagnetic thermal-bath loading (CMB at 2.725 K). Phase 3-A3 surfaced this as framework-extension question **Q-DELTA-MAP-1**: three candidate substrate-physics paths P1/P2/P3 (new third class; ASYM at thermal-bath amplitude; substrate-bond rest-length thermal contraction independent of saturation kernel) — all three failing at order-of-magnitude under naive estimates. **2026-05-28 Q-DELTA-MAP-1 closure at mechanism-class identification** (branch `analysis/section9-ideal-lattice-corrections-plus-delta-strain-canonical-leaf`): per `ave-ee-first-mapping` v1.0 + Grant 2026-05-28 adjudication, a fourth substrate-physics path P4 emerged — **Cosserat-rotation-sector mass-gap thermal-mode-population ASYM**, canonical at [`delta-strain-cosmic-tcc.md`](../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (clm-hp7nlm). Substrate's Ax 1 bipartite-DOF structure carries gapless E-modes + Cosserat-couple-stress-gapped B-modes ($\omega_m \sim 1$ MeV per canonical [`trampoline-framework.md:188`](../common/trampoline-framework.md)); at $T_{CMB}$, B-modes thermally completely frozen ($k_B T_{CMB}/\hbar\omega_m \sim 2 \times 10^{-10}$), only E-modes participate in substrate thermal-mode population. Asymmetric occupation breaks SYM-class scaling: $\varepsilon$ modulated, $\mu$ frozen → α drifts. Same Cosserat couple-stress modulus $\gamma_c$ underlies both weak force range ([`gauge-boson-masses.md:39`](../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md)) AND δ_strain mechanism; falsification of either via the right-handed-neutrino kill-switch (clm-gw2wgc) falsifies both. Confidence bumps **0.45 → 0.55** (PARTIAL band per `consistency-vs-emergence` v1.3 Step 8d): substrate-mechanism identified + load-bearing-assumption explicit-named (Class B substrate-mechanism manifestation), but the quantitative substrate-statistical-mechanics computation of $\eta_\varepsilon$ from substrate E-mode dispersion + Bose-Einstein occupation at $T_{CMB}$ holds rigor below Class 2 emergence and confidence below 0.60. **2026-05-31 FT-1 — Q-DELTA-MAP-1-quant CLOSED NEGATIVE** (branch `analysis/ft-1-delta-strain-eta-epsilon`; landed via the 37a946da walk-back): the candidate E-mode Bose-Einstein occupation derivation of $\eta_\varepsilon$ was run forward (no target fed in) and **undershoots the ~$4.45 \times 10^{-6}$ target by ~31 OOM** ($\Theta_\text{Debye} \approx 2.3 \times 10^{10}$ K $\gg T_{CMB}$ forces the Debye-$T^4$ regime, below equipartition by ~28.5 OOM), AND is **generic-thermal, not AVE-distinct** (SM-counterfactual). The Class B → Class 2 lift via this route does **NOT** occur; the magnitude stays a **definitional residual** ($1-$CODATA$/\alpha_\text{cold}$); the thermal mechanism is **sign-only**. **Confidence STAYS 0.55** (no Class-2 lift; magnitude-only re-scope). The mechanism-class identification at clm-hp7nlm + its weak-force $\gamma_c$ joint-constraint SURVIVE. Anchor: [`research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md`](../../../research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md). Class E framework membership in the Machian-G cosmic-substrate family ({α, G, H_∞, Ω̂_freeze}) is canonical at [`omega-freeze-cosmic-grain-cascade.md`](../common/omega-freeze-cosmic-grain-cascade.md); promoting $\delta_{\text{strain}}$ to a 5th joint-constrained projection within that family was GATED on a magnitude closure that did not arrive — the SIGN-mechanism membership stands, the magnitude-derivation gate is closed negative.
- strengthen-by:
  - **Q-DELTA-MAP-1-quant** — **ATTEMPTED → NEGATIVE (FT-1, 2026-05-31)**: the quantitative E-mode dispersion + substrate-Bose-Einstein occupation derivation of $\eta_\varepsilon$ at $T_{CMB}$ was run and **undershoots the target $\eta_\varepsilon \approx 4.45 \times 10^{-6}$ by ~31 OOM** (BE occupation gives $\sim 10^{-38}$; at $T_{CMB} \ll \Theta_\text{Debye}$ it suppresses *below* equipartition by ~28.5 OOM and cannot amplify). The Class B → Class 2 lift via this route **does NOT occur**; confidence STAYS 0.55. The thermal mechanism is **sign-only** — δ_strain's magnitude is a **definitional residual** ($1-$CODATA$/\alpha_\text{cold}$); and per the SM-counterfactual even a match would be generic-thermal, not AVE-distinct. Anchor: [`research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md`](../../../research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md). (Reinforced by the 2026-06-04 golden-torus bijection closure: $\alpha^{-1}=4\pi^3+\pi^2+\pi$ is a named identification on both lift-routes.)
  - Cosmic-temperature-dependent α-drift forward prediction (§6.1 of clm-hp7nlm leaf): substrate α should drift roughly linearly with cosmic $T$ for $T_{CMB} \ll T \ll T_{B-gap} \sim 10^{10}$ K. Quasar absorption-line $\Delta\alpha/\alpha$ measurements at higher redshift test the substrate Cosserat-Curie TCC scaling; current bounds at $|\Delta\alpha/\alpha| \lesssim 10^{-5}$ are loose enough that the substrate prediction is not yet falsified, but tighter $T_{universe}$-dependent measurements would constrain it. This would lift the observable axis from Class 4 consistency to Class E new prediction.
---

## EMT $p_c = 8\pi\alpha$ — Consistency Relation, NOT α Derivation
<!-- id: clm-9s9apq -->

The Ch.2 dielectric-rupture argument shows that the AVE lattice's packing fraction sits at the EMT trace-reversal point ($K = 2G$). It is sometimes summarized as "$\alpha$ from EMT" — this conflation is wrong.

- $p_c = V_{node}/\ell_{node}^3 = 2e^2/(\epsilon_0 \hbar c) \equiv 8\pi\alpha$
- _Specific Claims_
  - Given $\alpha$ from Ch.8, the Schwinger yield density $u_{sat}$ places the lattice at $p_c \approx 0.1834$, which **is** the EMT trace-reversal operating point ($K = 2G$).
  - The 3D amorphous central-force EMT quadratic at $K/G = 2$ uniquely fixes coordination $z_0 \approx 51.25$, which fixes the rigidity threshold $p_G = 6/z_0 \approx 0.117$ — the vacuum operates 56.7% above the fluid–solid transition.
  - The "Over-Bracing Factor" $\mathcal{R}_{OB} = 0.3068/0.1834 \approx 1.673$ implies an effective secondary connectivity reach $r_{\text{secondary}} \approx 1.187\,\ell_{node}$, identifying the substrate as a chiral SRS net (coordination $z = 3$) rather than a Cauchy-Delaunay solid.
- _Specific Non-Claims and Caveats_
  - The identity $p_c = 8\pi\alpha$ is **$\alpha$'s SI definition rearranged via $p_c$**, not an independent derivation of $\alpha$'s numerical value. The $4\pi$ in $\alpha = e^2/(4\pi\epsilon_0 \hbar c)$ cancels the $8\pi$ in the numerator of $p_c$ — the equation is algebraic, not predictive.
  - The Schwinger yield density $u_{sat} = \tfrac{1}{2}\epsilon_0 (m_e^2 c^3/(e\hbar))^2$ is **taken as an external QED input** in this section. Deriving $u_{sat}$ from the four AVE axioms is not attempted here.
  - Read this section as: "given $\alpha$ from Ch.8, the lattice is at the $K = 2G$ point" — not "$\alpha$ is derived from EMT". The EMT argument is downstream of the Golden Torus closure, providing a self-consistency cross-check.

> **Leaf references:** [zero-parameter-universe](./axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md), [dielectric-rupture](./axioms-and-lattice/ch2-macroscopic-moduli/dielectric-rupture.md), [dielectric-snap-limit](./axioms-and-lattice/ch2-macroscopic-moduli/dielectric-snap-limit.md).

### Quality
- confidence: 0.85
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation [α enters every numerical claim downstream of the identity]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.85, 0.63)]
- rationale: Local work is solid and correctly scoped: p_c=8πα is algebraically exact (the 4π in α=e²/(4πε₀ℏc) cancels the 8π), it is explicitly framed as a consistency relation NOT an α derivation, and the K=2G operating point with z₀≈51.25 from amorphous central-force EMT is a sound cross-check given α. Non-claims are explicit (u_sat taken as external QED input; "α from EMT" disclaimer), so the only unrepaired local input is u_sat.
- strengthen-by:
  - Derive u_sat (Schwinger yield density) from the four AVE axioms rather than importing it as a QED input
  - State that p_c=8πα is an identity (zero predictive content) wherever it is cited, to prevent the "α from EMT" misreading
  - Cross-check the z₀≈51.25 / p_G≈0.117 chain against an independent EMT coordination estimate
---

## $V_{snap}$ vs $V_{yield}$ — Two Distinct Thresholds
<!-- id: clm-2dwzib -->

- $V_{snap} = m_e c^2/e \approx 511.0$ kV; $V_{yield} = \sqrt{\alpha}\cdot V_{snap} \approx 43.65$ kV
- _Specific Claims_
  - $V_{snap}$ is the **absolute snap limit**: the maximum inter-node potential difference before the lattice structurally ruptures (per-node breakdown).
  - $V_{yield}$ is the **kinetic onset of nonlinearity** (Axiom 2): where saturation effects become dominant and a soliton begins to self-confine.
  - Lab/engineering applications operate near $V_{yield}$, not $V_{snap}$; even the most extreme macroscopic fields ($10^{10}$ V/m) impart $\Delta V_{lab}/V_{snap} \sim 7.5\times 10^{-9}$ across a single node.
- _Specific Non-Claims and Caveats_
  - Conflating $V_{snap}$ and $V_{yield}$ is explicitly catalogued as the first entry in [LIVING_REFERENCE.md "Critical Distinctions"](../../../LIVING_REFERENCE.md). Summaries that cite a single "saturation threshold" without specifying which one are wrong.
  - The Ch.7 regime boundary $r_3 = 1.0$ is the same physical phase transition as the Ch.3 zero-impedance boundary; both correspond to $V_{yield}$, viewed as either trapped-mode standing wave (matter assembly) or super-threshold rupture (topology destroyed). One transition, two faces — not two distinct boundaries.

> **Leaf references:** [dielectric-snap-limit](./axioms-and-lattice/ch2-macroscopic-moduli/dielectric-snap-limit.md), [zero-impedance-boundary](./dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md), [four-regimes](./operators-and-regimes/ch7-regime-map/four-regimes.md).

### Quality
- confidence: 0.95
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity 0.63) [for $V_{yield}$'s $\sqrt{\alpha}$ factor]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.95, 0.63)]
- rationale: Both thresholds are direct consequences of axiom-level definitions — $V_{snap} = m_e c^2/e$ is the per-node energy-equivalent voltage; $V_{yield} = \sqrt{\alpha}\cdot V_{snap}$ follows from Axiom 2. Local distinction work is rock-solid and explicitly catalogued in LIVING_REFERENCE.md Critical Distinction #1. Solidity is bounded by $\alpha$ via $V_{yield}$'s $\sqrt{\alpha}$ factor; $V_{snap}$ alone (depending only on framework inputs) carries solidity ≈ 0.95. Current solidity 0.63 (= min(0.95, 0.63)) tracks `clm-0ktpcn`'s α derivation. (The 2026-05-06-era 0.52 → 0.39 drop reflected the trf3bd-rebound chain that has since been superseded by the 2026-05-17 body-topology resolution and the 2026-05-26 Phase-2-A cascade lift; 0.55 reflected the post-2026-05-26 Phase 3-A1+Q2 prose-reframe cascade; current 0.63 reflects the post-2026-05-27 Phase 3-A4 PARTIAL-band amendment cascade per PR #47+#48.)
- strengthen-by:
  - Strengthen Golden Torus α Derivation (the only dependency reducing this entry's solidity; closing it lifts $V_{yield}$ numerical solidity to the local-confidence level of 0.95)

---

## ξ vs ξ_topo — Distinct Quantities, Same Greek Letter
<!-- id: clm-3kzmt9 -->

- $\xi \approx 8.15\times 10^{43}$ (dimensionless Machian hierarchy coupling; gravity derived from Axioms 1 + 4); $\xi_{topo} = e/\ell_{node} \approx 4.149\times 10^{-7}$ C/m (electromechanical transduction, Axiom 2 mechanism)
- _Specific Claims_
  - $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ is the cosmological-horizon dilution that converts the un-shielded gravitational coupling ($G_{true} = \hbar c/m_e^2$) into the macroscopic Newton's $G$.
  - $\xi_{topo} = e/\ell_{node}$ is the topological conversion constant grounding the $[Q] \equiv [L]$ isomorphism; it carries dimensions C/m.
- _Specific Non-Claims and Caveats_
  - These are **different quantities sharing a Greek letter**. CLAUDE.md Axiom 3 explicitly flags this and the axiom-definitions leaf carries an inline notation warning.
  - Does NOT claim $\xi$ is independently observable; the Machian dilution factor of $\sim 10^{45}$ between $G_{true}$ and macroscopic $G$ is the "staggering" ratio that motivates the Machian framing — it is a derivation step, not a measurement.

> **Leaf references:** [axiom-definitions](./axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md), [lc-resonant-network-vacuum](./axioms-and-lattice/ch1-fundamental-axioms/lc-resonant-network-vacuum.md).

### Quality
- confidence: 0.90
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity 0.63) [for $\xi$'s $\alpha^{-2}$ factor]
  - clm-5xon03 — Zero-Parameter Closure Status (solidity 0.65) [for $\xi$'s $R_H/H_\infty$ factor — $H_\infty$ is a consistency identity conditional on $G$ closure]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.90, 0.63)]
- rationale: Local distinction work is correctly enforced — $\xi_{topo} = e/\ell_{node}$ from Axiom 2's topo-kinematic isomorphism mechanism; $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ from the derived-gravity Machian dilution (Axioms 1 + 4). $\xi_{topo}$'s numerical value alone carries solidity 0.90 (depends only on framework inputs); $\xi$ inherits the dependency chain. Solidity bounded by the α dependency $clm-0ktpcn$ (currently solidity 0.63) and the Closure Status dependency $clm-5xon03$ (currently solidity 0.65); the tighter bottleneck is $clm-0ktpcn$, so $\xi$ tracks the α derivation strength. (The 2026-05-06-era 0.50 → 0.25 drop reflected the trf3bd-rebound dependency chain that has since been superseded by the 2026-05-17 body-topology resolution and the 2026-05-26 Phase-2-A cascade lift; current 0.63 reflects the post-2026-05-27 Phase 3-A4 PARTIAL-band amendment per PR #47+#48.)
- strengthen-by:
  - Strengthen Golden Torus α Derivation (dominant solidity bottleneck for $\xi$)
  - Close the $H_\infty/R_H$ circularity via independent $G$ derivation (raises Closure Status solidity, tightening $\xi$'s secondary bound)

---

## "True Planck Length = $\ell_{node}$" — Algebraic Consequence, Interpretive
<!-- id: clm-219e8j -->

- $\ell_{P,\text{true}} = \sqrt{\hbar G_{true}/c^3} \equiv \hbar/(m_e c) = \ell_{node}$
- _Specific Claims_
  - Substituting the un-shielded $G_{true} = \hbar c/m_e^2$ into the standard Planck-length expression algebraically collapses to $\ell_{node}$.
  - The $G/G_{true} \sim 1.75 \times 10^{-45}$ ratio is the cumulative Machian/holographic shielding factor across the cosmological horizon mass.
- _Specific Non-Claims and Caveats_
  - This is an **algebraic identity** within the AVE definition of $G_{true}$, not an independent measurement-versus-prediction comparison. Both sides match because $G_{true}$ is defined to make this hold.
  - The interpretive claim ("$\ell_{node}$ is the true microscopic cutoff, the standard Planck length is a macroscopic-$G$ artifact") is a **framework-internal ontological** statement; it does not introduce new observables vs the standard Planck-length picture at the formula level.
  - See cross-cutting [vol3 Dirac Large Numbers and Planck Mass entry](../vol3/claim-quality.md) for the same algebraic-identity caveat applied to $m_P = m_e\sqrt{7\xi}$.

> **Leaf references:** [lc-resonant-network-vacuum](./axioms-and-lattice/ch1-fundamental-axioms/lc-resonant-network-vacuum.md).

### Quality
- confidence: 0.95
- solidity: 0.95 (ok to build on)
- rationale: The identity $\ell_{P,\text{true}} = \sqrt{\hbar G_{true}/c^3} \equiv \ell_{node}$ is algebraic given the AVE definition of $G_{true} = \hbar c/m_e^2$, and the entry explicitly discloses this as algebra-not-prediction. The interpretive claim ("$\ell_{node}$ is the true microscopic cutoff") is correctly framed as framework-internal ontology, not a new observable. Depends only on framework inputs ($m_e$, $\hbar$, $c$) and the framework-internal definition of $G_{true}$; no entry-level dependencies that propagate solidity reduction.
- strengthen-by:
  - none — algebraic identity within the framework's existing definitions; the entry is correctly self-bounded as interpretive

---

## Master Equation EFT Validity (Leading-Order Regime)
<!-- id: clm-efo113 -->

- $\nabla^2 V - \mu_0 \varepsilon_0 \sqrt{1 - (V/V_{yield})^2}\,\partial^2 V/\partial t^2 = 0$
- _Specific Claims_
  - The unifying Master Equation is the leading-order long-wavelength EFT obtained by substituting $\varepsilon_{eff}(V)$ into the linear D'Alembert form.
  - In Regime I ($V \ll V_{yield}$): exactly recovers the linear Maxwell-Heaviside wave equation.
  - In the saturation regime: governs particle confinement (magnetic-branch saturation $\mu_{eff} \to 0$, $Z \to 0$, $\Gamma \to -1$, standing wave = rest mass) and the symmetric-gravity refractive index $n(r) = 1 + 2GM/(c^2 r)$.
- _Specific Non-Claims and Caveats_
  - Direct substitution of $\varepsilon_{eff}(V)$ is **exact only in the leading-order EFT regime**. The form drops the field-gradient corrections that arise from $\nabla \cdot \mathbf{D} = \varepsilon_{eff}\nabla\cdot\mathbf{E} + (\nabla\varepsilon_{eff})\cdot\mathbf{E} = 0$. These are subdominant in the linear limit (where $d\varepsilon_{eff}/dV \to 0$); particle-confinement and standing-wave claims at $V \to V_{yield}$ depend on the dropped first-derivative gradient terms remaining negligible by symmetry at saturation.
  - Quantitative claims that depend on the wave-equation **form** near $V_{yield}$ (rather than on the saturation kernel $S$ alone) require a higher-order correction including $\nabla\varepsilon_{eff}\cdot\nabla V$. That correction is not derived in Vol 1.
  - The leaf flags this caveat explicitly; reviewers should not summarize the master equation as "exact" without the EFT qualifier.

> **Leaf references:** [master-equation](./dynamics/ch4-continuum-electrodynamics/master-equation.md).

### Quality
- confidence: 0.50
- solidity: 0.50 (use as input only, don't build deeper)
- rationale: The leading-order EFT form $\nabla^2 V - \mu_0\varepsilon_0 \cdot S \cdot \partial^2 V/\partial t^2 = 0$ is sound and exactly recovers linear Maxwell-Heaviside in Regime I. The particle-confinement and refractive-index claims at saturation depend on the dropped first-derivative gradient terms ($\nabla\varepsilon_{eff}\cdot\nabla V$) remaining negligible by symmetry — this assumption is explicitly disclosed in the leaf but not derived from the axioms, which lands the entry in the 0.5 rubric band. No entry-level dependencies (the unverified-symmetry assumption is internal to the entry's claim space; Axiom 4 is a framework input at solidity 1.0).
- strengthen-by:
  - Derive whether $\nabla\varepsilon_{eff}\cdot\nabla V$ gradient corrections vanish by symmetry at saturation, OR carry the higher-order EFT correction and re-evaluate the particle-confinement and standing-wave claims at $V \to V_{yield}$ with the corrected form

---

## Magnetic-Branch Confinement vs Electric-Branch Rupture
<!-- id: clm-lv3uw1 -->

The two saturation symmetry cases are catalogued in the cross-cutting [Symmetric vs Asymmetric Saturation](../claim-quality.md) entry. Vol 1's master-equation leaf is where this distinction is **first introduced** within the volume; Vol 1-specific clarification:

- _Specific Claims_
  - Particle confinement proceeds via the **magnetic branch** (a sub-case of the symmetric sector): at a torus-knot self-intersection, $\mathbf{B}$ saturates $\mu_{eff}$ first, driving $Z = \sqrt{\mu_{eff}/\varepsilon_0} \to 0$ and $\Gamma \to -1$ (short-circuit). The reflected wave traps as a standing mode = invariant rest mass, with no Higgs mechanism invoked.
  - Dielectric rupture (electric breakdown) proceeds via the **asymmetric (electric-only) branch**: $\varepsilon_{eff} \to 0$ with $\mu_{eff}$ intact drives $Z = \sqrt{\mu_0/\varepsilon_{eff}} \to \infty$ — the medium becomes evanescent (no energy transport), not a conductor.
  - Both branches are governed by the **same** kernel $S(A) = \sqrt{1 - (A/A_{yield})^2}$; they differ only in which constitutive parameter saturates first.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the AVE confinement mechanism *competes* with the Higgs mechanism — it is a different ontology (impedance reflection vs gauge-symmetry breaking) reaching the same observable (mass).
  - Does NOT claim the magnetic branch is "asymmetric" in the cross-cutting sense. The magnetic-confinement branch is **a third sub-case of the symmetric sector** (see Ch.7 regime-equation-sets footnote): it saturates $\mu$ rather than $\varepsilon$, but is symmetric in that $Z \to 0$ rather than $Z \to \infty$.
  - For the canonical SYMMETRIC vs ASYMMETRIC tabulation (gravity, BH interior, GW shear vs strong EM), see [cross-cutting](../claim-quality.md).

> **Leaf references:** [zero-impedance-boundary](./dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md), [master-equation](./dynamics/ch4-continuum-electrodynamics/master-equation.md), [regime-equation-sets](./operators-and-regimes/ch7-regime-map/regime-equation-sets.md).

### Quality
- confidence: 0.65
- depends-on:
  - clm-efo113 — Master Equation EFT Validity (solidity 0.50)
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.65, 0.50)]
- rationale: The structural classification — magnetic branch as a sub-case of the symmetric sector ($Z \to 0$ via $\mu_{eff} \to 0$); asymmetric/electric branch with $Z \to \infty$ via $\varepsilon_{eff} \to 0$ alone; both governed by the same kernel $S(A)$ — is sound algebra given the impedance and saturation definitions. However, the load-bearing AVE claim — that magnetic-branch confinement at a torus-knot self-intersection IS the mechanism for invariant particle rest mass — depends on the leading-order Master Equation EFT remaining valid through saturation, which itself is asserted-not-derived (gradient corrections negligible by symmetry). The classification alone has local quality ≈ 0.65; the rest-mass mechanism claim transitively inherits Master Equation EFT Validity's 0.50, dropping this entry to 0.32 overall. **Scope (wall-fork H3, 2026-06-15):** the "magnetic branch PRIMARY" labeling (FLAG-2, the cvr handoff) is scoped to a **chirality-conventional SIGN-assignment**, NOT a substrate-privileged branch — the $\Gamma=-1$ wall requires the chirality-broken asymmetry (symmetric co-saturation is the impedance-matched gravity $Z=Z_0$ null), and μ-first ($\Gamma=-1$) vs ε-first ($\Gamma=+1$) are the spin-conjugate signs. The wall is mute on the mass sector (mass = A1 dilatation, `master-equation.md:20`). This does not change the entry's solidity.
- strengthen-by:
  - Strengthen Master Equation EFT Validity (the dominant solidity bottleneck for this entry; closing the gradient-corrections-at-saturation assumption raises this entry's solidity to local-confidence level)
  - Provide an axiom-grounded derivation that the standing-wave reflected mode at $\Gamma \to -1$ quantitatively reproduces invariant rest-mass spectra (currently a structural identification, not a derivation of mass values)

---

## GUP — Independent-Variances Assumption
<!-- id: clm-nq2kcc -->

- $\Delta x_{AVE} = \sqrt{(\Delta x_{SM})^2 + (\ell_{node}/2)^2} \ge \ell_{node}/2$
- _Specific Claims_
  - On a discrete graph with pitch $\ell_{node}$, the canonical momentum is bounded to the Brillouin zone $[-\pi\hbar/\ell_{node}, +\pi\hbar/\ell_{node}]$; the discrete-graph commutator evaluates to $i\hbar\cos(\ell_{node}\hat p_c/\hbar)$.
  - In the low-energy limit $p_c \ll \hbar/\ell_{node}$, the cosine $\to 1$ and standard Heisenberg ($\Delta x\,\Delta p \ge \hbar/2$) is recovered.
  - The **GUP gap** $\ge \ell_{node}/2 \approx 1.93\times 10^{-13}$ m provides a built-in UV regularization — pressure waves cannot be localized below the lattice pitch.
- _Specific Non-Claims and Caveats_
  - The root-sum-square $\Delta x_{AVE} = \sqrt{(\Delta x_{SM})^2 + (\ell_{node}/2)^2}$ assumes the SM continuous-momentum uncertainty and the lattice node-spacing uncertainty are **statistically independent**. The leaf states this assumption explicitly; it is plausible (the SM bound arises in any single Brillouin zone; the lattice floor arises from Nyquist resolution independent of Bloch state) but should not be summarized as a derivation without the independence premise.
  - Does NOT claim the GUP magnitude is independently measurable at the engineering level; $\ell_{node}/2 \sim 10^{-13}$ m is far below current localization-experiment resolution.

> **Leaf references:** [gup-derivation](./dynamics/ch3-quantum-signal-dynamics/gup-derivation.md).

### Quality
- confidence: 0.70
- solidity: 0.70 (ok to build on, see caveats)
- rationale: The discrete-graph commutator $i\hbar\cos(\ell_{node}\hat p_c/\hbar)$ follows from Brillouin-zone bounds on canonical momentum given Axiom 1's lattice pitch; recovery of standard Heisenberg in the low-energy limit is direct algebra; the GUP gap $\ge \ell_{node}/2$ derives from Nyquist resolution of the lattice. The root-sum-square combination $\Delta x_{AVE} = \sqrt{(\Delta x_{SM})^2 + (\ell_{node}/2)^2}$ explicitly assumes statistical independence of the SM continuous-momentum uncertainty and the lattice node-spacing uncertainty — the leaf flags this as a plausible-but-not-derived assumption (the SM bound arises in any single Brillouin zone; the lattice floor arises from Nyquist resolution independent of Bloch state). Methodology bound is properly disclosed, which lands the entry in the 0.7 rubric band. No entry-level dependencies — $\ell_{node}$ is treated as a framework input.
- strengthen-by:
  - Derive statistical independence of SM continuous-momentum uncertainty and lattice node-spacing uncertainty from the underlying Bloch-state theory of the discrete-graph wavefunction, OR derive the corrected combination rule (covariance-aware) if the variances are not independent

---

## Schrödinger Equation from Paraxial Envelope (Mechanism, Not Independent Derivation)
<!-- id: clm-7zuwtm -->

- $i\hbar\,\partial_t\Psi = -(\hbar^2/2m)\nabla^2\Psi + V(\mathbf{r})\Psi$ with $V(\mathbf{r}) = \tfrac{1}{2}m c^2\chi(\mathbf{r})$
- _Specific Claims_
  - Klein-Gordon arises as circuit resonance: a localized inductive load with $\omega_m = mc^2/\hbar$ mathematically transforms the Maxwell wave equation into the massive form.
  - Paraxial factoring $\mathbf{A} = \Psi\,e^{-i\omega_m t}$ for non-relativistic $v \ll c$ recovers the free-particle Schrödinger equation.
  - Spatial modulation $\varepsilon_{eff}(\mathbf{r}) = \varepsilon_0[1+\chi(\mathbf{r})]$ in the linear limit ($|\chi| \ll 1$) recovers the full Schrödinger equation with on-site potential $V(\mathbf{r}) = \tfrac{1}{2}mc^2\chi(\mathbf{r})$ — atomic Coulomb wells, applied static fields, and other knot strain fields enter through this same mechanism.
- _Specific Non-Claims and Caveats_
  - The bound-state derivation of $V(\mathbf{r})$ is **leading-order in $|\chi|$** (linear regime). Strong-field cases ($\chi$ approaching saturation) do not reduce to a simple position-dependent potential.
  - Recovery of hydrogenic energy levels $E_n = -m_e c^2\alpha^2/(2n^2)$ from the impedance-matching $2\pi r = n\lambda$ condition is asserted via a Vol 2 cross-reference; the explicit derivation lives in Vol 2 Ch 7, not in this leaf.
  - "No quantum postulates are imported" applies to the *form* of the equation. The Born rule (probability = $|\Psi|^2$) is derived separately in §3.5 from Ohmic measurement work; the two derivations together close the standard QM formalism, but each step is its own claim.

> **Leaf references:** [ohmic-decoherence-born](./dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md), [schrodinger-from-circuit](./dynamics/ch3-quantum-signal-dynamics/schrodinger-from-circuit.md).

### Quality
- confidence: 0.50
- solidity: 0.50 (use as input only, don't build deeper)
- rationale: Paraxial factoring of Klein-Gordon to recover free-particle Schrödinger is standard math; spatial modulation $\varepsilon_{eff}(\mathbf{r})$ recovering on-site potential $V(\mathbf{r})$ is leading-order linear-in-$\chi$ (correctly disclosed). The substantively open element is the Klein-Gordon emergence step itself: a localized inductive load (topological defect with $\omega_m = mc^2/\hbar$) is asserted to produce a spatially uniform $(mc/\hbar)^2 \mathbf{A}$ mass term in the wave equation — but a localized load mathematically produces a localized $\delta(\mathbf{r}-\mathbf{r}_0)$ source, not a uniform background coefficient. This step is asserted by analogy rather than derived, lands the entry at the 0.5 rubric band. No entry-level scored dependencies; the Born rule cross-reference points at a sister leaf (`ohmic-decoherence-born.md`) not yet a separate claim-quality entry.
- strengthen-by:
  - Derive the spatially uniform Klein-Gordon mass term from the LC network's response to a localized topological defect (e.g., via long-wavelength averaging over distributed knot density, or via spectral analysis showing the localized resonance acts as a uniform background mode for waves in the surrounding medium)
  - Provide the explicit derivation of hydrogenic energy levels from the impedance-matching condition $2\pi r = n\lambda$ (currently cross-referenced to Vol 2 Ch 7, not present in this leaf)

---

## Born Rule from Ohmic Measurement Work
<!-- id: clm-ldmvwi -->

- $P(\text{click} \mid x_n) = |\partial_t \mathbf{A}(x_n)|^2 / \int |\partial_t \mathbf{A}(\mathbf{x})|^2\, d^3x \equiv |\Psi|^2$
- _Specific Claims_
  - A macroscopic detector couples to the lattice $\mathbf{A}$-field via a resistive mechanical load — by Axiom 1's impedance algebra, $1\,\Omega \equiv \xi_{topo}^{-2}\,\text{kg/s}$ — and extracts kinetic energy.
  - Classical Joule heating ($P = V^2/R$) over interval $\Delta t$ gives $W_{extracted} \propto |\partial_t \mathbf{A}(x_n)|^2 / Z_{detector} \cdot \Delta t$.
  - **The probability that extracted work triggers a macroscopic discrete event ("click") scales with $|\partial_t \mathbf{A}|^2$ — DERIVED from the substrate's stochastic master vacuum equation via Vol 3 Ch 11 FDT + threshold-crossing first-passage + cumulant truncation (Phase 2-A workstream, 2026-05-26)**. Click rate $\lambda_{signal}(x_n, t) = |\partial_t \mathbf{A}(x_n, t)|^2 / (E_{th} \cdot Z_{det})$ across two detector classes (voltage-threshold + energy-bucket); universal scaling, class-specific proportionality constants (substrate form of QM "detector efficiency $\eta$"). Identifies $P(\text{click} \mid x_n) \equiv |\Psi|^2$ — the Born rule as the substrate-derived thermodynamic equation for momentum extraction from a wave-bearing lattice by a thresholded Ohmic load.
  - **The exponent $p = 2$ is uniquely selected** by substrate physics — three convergent arguments (cumulant truncation under Joule extraction; dimensional analysis on substrate scales; counterfactual elimination of $p = 1, 3, 4, $ fractional). $p \neq 2$ would require contradiction of substrate-pinned Joule + Gaussian + Markovian primitives.
  - Decoherence is the irreversible thermalization of the spatial pressure wave at the detector, attenuating interference gradients.
- _Specific Non-Claims and Caveats_
  - Does NOT derive the entire QM measurement formalism — only the $|\Psi|^2$ scaling of click probability.
  - **(2026-05-26 Phase 2-A closure)** The "click probability $\propto$ extracted work" identification — formerly asserted as a thermal-substrate stochastic property — is now **DERIVED end-to-end from the master vacuum equation** via Vol 3 Ch 11 FDT + Joule extraction + Gaussian Langevin noise + threshold-crossing first-passage + cumulant truncation. Full derivation chain across A.2 + A.3 + A.4 result docs (see rationale). The prior "asserted not derived" caveat is RETIRED.
  - **Scope of the derivation**: applies to **AC signals or sign-symmetric signal ensembles** (the canonical Born-rule photodetection regime — oscillating EM fields from photon sources). For DC or sign-asymmetric signals where $\langle V_s \rangle \neq 0$, a linear-in-$V_s$ contribution survives and the $|V_s|^2$ scaling becomes sub-leading. Born-rule canonical test regime IS the AC case; non-canonical regimes are out of scope.
  - Does NOT address the spin-statistics theorem or fermion anti-symmetric wavefunction structure — those are separate claims.
  - The detector model is a thresholded Ohmic load (voltage-threshold OR energy-bucket detector classes — both covered by A.3 result); non-thresholded or quantum-coherent detectors (homodyne, heterodyne, photon-number-resolving) are out of scope.
  - **3 forward-prediction candidates flagged for downstream-epic seeding** (NOT load-bearing for this claim's current solidity; candidate AVE-distinct predictions for future workstreams): (1) non-linear-regime corrections at $V \to V_{yield}$ (saturation kernel introduces $V_s^4$ terms); (2) nanoscale CLT failure regime (single-photon avalanche detectors, transmon qubits, mesoscopic Josephson — could exhibit substrate-distinct non-Gaussian corrections); (3) non-Markovian Poisson violation under detector memory effects.

> **Leaf references:** [ohmic-decoherence-born](./dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md).

### Quality
- confidence: 0.65
- depends-on:
  - INVARIANT-S2 / Axiom 1 (Ohmic detector boundary; impedance algebra $1\,\Omega \equiv \xi_{topo}^{-2}\,\text{kg/s}$)
  - INVARIANT-S2 / Axiom 3 (master vacuum equation effective action; linear-regime $\Box V = 0$ form)
  - clm-yiyyi3 — Dielectric Lagrangian $\mathcal{L}_{AVE} = \tfrac{1}{2}\varepsilon_0\|\partial_t\mathbf{A}\|^2 - \tfrac{1}{2\mu_0}\|\nabla\times\mathbf{A}\|^2$ (solidity 0.70) [load-bearing for step 5 of the derivation chain — V↔$\partial_t \mathbf{A}$ identification]
- solidity: 0.65 (ok to build on, see caveats) [= min(0.65, 0.70)]
- rationale: The full master-equation-derivation-path for $|\Psi|^2$ click-probability scaling is closed end-to-end as of 2026-05-26 (Phase 2-A workstream, 5-session arc on branch `analysis/clm-ldmvwi-master-eq-stochastic-derivation`). The 7-step chain: (1) master vacuum equation linear regime $\Box V = 0$ → (2) FDT-derived Langevin forcing at detector boundary per Vol 3 Ch 11:75-138 (Nyquist on $Z_0$ literal-not-analogy + boundary-impedance thermalization + Ohmic damping balance; canonical substrate-thermal-noise scaffold cited in prose) + Ohmic damping balance → (3) stochastic master vacuum equation $\Box V + 2\gamma_n \delta^3 \partial_t V = f_n \delta^3$, $\langle f_n(t) f_n(t')\rangle = 2 k_B T Z_{det} \delta(t-t')$ (A.2 §2.4) → (4) Joule extraction $W(t) = \int V^2/Z_{det}\, dt$ with signal/noise decomposition (A.2 §3.2-3.3) → (5) V↔$\partial_t \mathbf{A}$ identification via AVE-canonical Lagrangian $\mathcal{L}_{AVE}$ (clm-yiyyi3, depends-on edge wired; A.2 §3.4) → (6) Gaussian $V_\eta$ via FDT + CLT on independent boundary-node thermal contributions (A.3 §2.1) → (7) threshold-crossing first-passage (Rice's formula for voltage-threshold detectors + Wald mean-rate for energy-bucket detectors; Markovian → Poissonian via FDT white-noise structure) yielding $\lambda_{signal} \propto V_s^2 \propto |\partial_t\mathbf{A}|^2$ (A.3 §3.4+§3.6) → $p=2$ uniqueness via 3 convergent arguments (cumulant truncation + dimensional + counterfactual; A.4 §3). **NO Born rule input anywhere in the chain — derivation is acyclic with Born rule (which is the downstream identification, not upstream input).** Per consistency-vs-emergence-UPGRADED discipline (Grant 2026-05-26: derivation-path-tracing from master vacuum equation must be explicit for any "AVE reproduces standard physics rule X" claim): **Class 2 substrate-mechanism emergence** on derivation-path axis (every step traces to master eq + canonical Vol 3 Ch 11 + Axiom 1 + clm-yiyyi3 Lagrangian); **Class 4 observable consistency** on prediction axis (no experimentally distinguishable predictions vs standard QM Born rule in canonical photodetection regime — 3 forward-prediction candidates flagged for downstream-epic seeding, not load-bearing). Confidence bumps 0.55 → 0.65 reflecting closure of 2 of 3 strengthen-by items (click-probability derivation + $p=2$ uniqueness) via substantive master-eq-derivation-path work; **the empirical regime-of-applicability bound (single-photon detector statistics validation — the one remaining strengthen-by item) is the explicit chokepoint for any further lift toward 0.70+ band**. Solidity = min(0.65, 1.00, 1.00, 0.70) = 0.65 (Axiom 1 + Axiom 3 framework inputs at solidity 1.0; clm-yiyyi3 at 0.70). Result docs at `research/2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md` (A.2) + `research/2026-05-26_clm-ldmvwi-phase-2a-3-threshold-crossing-result.md` (A.3) + `research/2026-05-26_clm-ldmvwi-phase-2a-4-uniqueness-result.md` (A.4) document the full derivation with auditor passes + ave-walk-back-at-amendment-time discipline applied throughout.
- strengthen-by:
  - Validate quantitatively against single-photon detector statistics (detector dead time, non-Poissonian regimes) to bound the regime of applicability — the one remaining strengthen-by item; engineering validation work, not derivation gap

---

## CHSH Violation $|S|_{\max} = 2\sqrt{2}$ (Tsirelson Bound)
<!-- id: clm-zuf7g1 -->

The phase-locked entanglement-thread leaf derives full quantum-mechanical angular correlations from AVE first principles.

- $E(\hat a, \hat b) = -\cos\theta_{ab}$; $|S|_{\max} = 2\sqrt{2}$ at $\delta = \pi/4$
- _Specific Claims_
  - Three AVE ingredients (spin-1/2 Möbius $\to$ half-angle coupling, Axiom 4 binary saturation outcome, Born rule from Ohmic extraction) yield the Bell correlation $E = -\cos\theta_{ab}$ and the Tsirelson bound $|S|_{\max} = 2\sqrt{2}$ — exactly matching the experimental CHSH violation envelope.
  - The "phase-locked topological thread" is identified as a lossless short-short LC resonator with $Z_0 \approx 377\,\Omega$, $Q = \infty$, fundamental mode $E_1 = \hbar\pi c/d$ (anti-confining: lighter as particles separate).
  - **Falsifiable prediction (distinguishing AVE from standard QM):** entanglement decoherence has a sharp temperature-dependent onset at the pair-creation threshold $T_{pair} = 2m_e c^2/k_B \approx 1.19\times 10^{10}$ K. Below this, only environmental coupling at thread endpoints causes decoherence; above it, the $2\pi$ winding can be unwrapped via spontaneous pair creation. Standard QM has no analogous intrinsic temperature threshold.
  - K4-TLM lattice simulation confirms vacuum and $T \ll T_{pair}$ noise scenarios are statistically indistinguishable (winding is topologically protected); $T \gg T_{pair}$ noise destroys the winding.
- _Specific Non-Claims and Caveats_
  - Does NOT claim CHSH violation > $2\sqrt{2}$; the AVE result hits the Tsirelson bound exactly, **the same** as standard QM. CHSH is **not** an experimental discriminator between AVE and QM at any laboratory temperature.
  - The no-signalling theorem is preserved (Bob's marginal is $1/2$ regardless of Alice's setting); the "topological thread" is **not** a faster-than-light communication channel.
  - The decoherence-temperature falsifiability is currently testable only in quark-gluon plasma / heavy-ion environments at $\sim 10^{12}$ K; standard cryogenic decoherence experiments operate at $T \ll T_{pair}$ where AVE and standard QM make identical predictions.
  - "Mechanically identical to the Meissner effect" is a structural identification (same saturation operator $S$ at $\Gamma \to -1$), not a literal claim that entanglement *is* superconductivity.

> **Leaf references:** [ohmic-decoherence-born](./dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md), [phase-locked-topological-thread](./dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md).

### Quality
- confidence: 0.65
- depends-on:
  - clm-ldmvwi — Born Rule from Ohmic Measurement Work (solidity 0.65) [Bell-correlation derivation uses Born rule as one of three ingredients]
  - clm-salw2h — Finkelstein-Misner spin-½ derivation in `vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md` (solidity 0.70) [supplies the spin-1/2 Möbius half-angle coupling — the AVE Bell-correlation derivation's "spin-1/2 Möbius → half-angle coupling" ingredient IS the SU(2) → SO(3) double-cover via FM kink mechanism on the extended unknot, formerly a sister cross-reference now wired as a real graph edge; closes strengthen-by items 3+4 (Möbius derivation explicit pointer + separate claim-quality entry)]
- solidity: 0.65 (ok to build on, see caveats) [= min(0.65, 0.65)]
- rationale: The Bell correlation $E(\hat a, \hat b) = -\cos\theta_{ab}$ and the Tsirelson bound $|S|_{\max} = 2\sqrt{2}$ emerge as algebra given three AVE ingredients (spin-1/2 Möbius half-angle coupling, Axiom 4 binary saturation at measurement, Born rule from Ohmic extraction); hitting Tsirelson exactly is significant corroboration. The substantive open element local to this entry is the structural identification "phase-locked topological thread = lossless short-short LC resonator implementing the Bell correlation" — asserted as a constructive picture, not derived from axioms. The decoherence-onset prediction at $T_{pair} \approx 1.19 \times 10^{10}$ K is genuinely falsifiable (in QGP regimes). **2026-05-26 Phase 1 (clm-zuf7g1 strengthen workstream)**: depends-on edge to clm-salw2h wired — the Finkelstein-Misner derivation at `finkelstein-misner-spin-half-derivation.md` (clm-salw2h, confidence 0.80, solidity 0.70) supplies the spin-1/2 Möbius half-angle coupling structure that this entry consumes as Bell-correlation ingredient (i). The Möbius / 720°-closure / SU(2) → SO(3) double-cover is one mechanism described under two names; clm-salw2h §2 (extended-defect FM kink) + §3 (K_4 → A_4 → 2T ⊂ SU(2) chain) cover the AVE-native derivation. Verbatim corpus anchor: phase-locked-topological-thread.md §3.5 *"The Möbius-strip topology of the chiral labyrinth requires 720° for a complete cycle, producing a physical half-angle coupling: when a detector axis â makes angle θ with the defect's rotation axis n̂, the effective phase mismatch is θ/2"* — this IS the manifestation of clm-salw2h's $4\pi$ double-cover in the Bell-correlation context, not a separate mechanism (independence-check confirmed via auditor-pass 2026-05-26 + verbatim grep on both leaves; ave-discipline-translate non-firing because translation-qm.md row 7 confirms "spin / unknot chirality / two orientations of the unknot twist ±1/2" is the AVE-native form being consumed — no QM-formalism import). Two of four prior strengthen-by items close via this single graph edge (item 3: Möbius derivation explicit pointer; item 4: separate claim-quality entry — clm-salw2h IS that separate entry, now scored in the chain). Confidence bumps 0.60 → 0.65 to reflect closure of 2/4 strengthen-by items. Solidity unchanged at 0.55 at that time because clm-ldmvwi (Born Rule) at solidity 0.55 remained the dep-cap. **2026-05-26 Phase 2-A (clm-ldmvwi-master-eq-stochastic-derivation workstream)**: clm-ldmvwi was strengthened from solidity 0.55 → 0.65 via the master-equation-derivation-path workstream — the previously-asserted "click probability ∝ extracted work" step is now derived end-to-end from substrate physics (master vacuum equation + Vol 3 Ch 11 FDT + Joule extraction + cumulant truncation). The cascade lifts clm-zuf7g1 solidity 0.55 → 0.65 (= min(0.65 own confidence, 0.65 clm-ldmvwi, 0.70 clm-salw2h) — now at the 0.65 confidence ceiling, equal-tied with clm-ldmvwi's solidity). The Born-rule-rigor strengthen-by item that capped clm-zuf7g1 is now RETIRED; further lift on clm-zuf7g1 requires closing its own derivation gap (lossless LC resonator structural identification — remaining strengthen-by item) AND/OR clm-ldmvwi's empirical regime-of-applicability bound (single-photon detector validation). **2026-05-26 Phase 3a (clm-zuf7g1 strengthen workstream, Z₀ substrate-mechanism derivation)**: WALK-BACK outcome — the substrate-impedance Z₀ ≈ 377 Ω derivation does NOT close Class 2 substrate-mechanism emergence on the numerical-value sub-axis. The dual-axis classification per `consistency-vs-emergence` v1.2 yields a compound result: **Class 2 substrate-mechanism emergence on the scale-invariance sub-axis** (K4-TLM topology via Ax 2 TKI forces $L_{\text{cell}} \propto \ell_{\text{node}}$ and $C_{\text{cell}} \propto \ell_{\text{node}}$, producing pitch cancellation in Z₀'s value at every lattice scale — substrate-distinct content), **Class B substrate-mechanism manifestation on the numerical-value sub-axis** (the value 376.73 Ω is recovered via SI substitution at the per-bond lumped-element step $L_{\text{cell}} = \mu_0 \ell_{\text{node}}, C_{\text{cell}} = \epsilon_0 \ell_{\text{node}}$ where μ₀ and ε₀ are SI engineering inputs at `src/ave/core/constants.py` (`MU_0`, `EPSILON_0`), not derived from K4 substrate primitives — confirmed against the existing canonical clm-kezk9z classification at vol4/claim-quality.md:104 as "category (i) identity"), **Class 4 observable consistency** (matches Maxwell vacuum impedance exactly in canonical regime). The structural identification step "topological-thread mode inherits substrate-impedance Z by lattice-continuity" at phase-locked-topological-thread.md line 27 is asserted-without-tracing in current corpus and deferred to Phase 3b alongside the Q = ∞ derivation. Per `ave-walk-back` v1.1 Type B (demotion-via-honest-classification, no Predictions-matrix-row retirement): clm-zuf7g1 confidence 0.65 and solidity 0.65 unchanged; the strengthen-by item is REFRAMED (not retired) to surface Q-LCR-1 (is the numerical value derivable from substrate primitives independent of SI?) + Q-LCR-2 (does a Phase 3a-pre workstream deriving μ₀/ε₀ from K4 geometry need to land first?) as framework-extension questions for Grant adjudication. Result doc: [`research/2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-result.md`](../../../research/2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-result.md); pre-reg: [`research/2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-prereg.md`](../../../research/2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-prereg.md).
- strengthen-by:
  - **Q-LCR-1 (framework-extension question, surfaced 2026-05-26 Phase 3a)**: is the substrate-impedance Z₀ numerical value 376.73 Ω derivable as substrate-mechanism emergence from Ax 1 + Ax 2 K4-TLM lattice parameters (per-bond geometric inductance + per-node geometric capacitance from chiral Laves K4 geometry alone), or is it definitionally fixed by the μ₀/ε₀ canonical-source link to standard continuum-electrodynamics values (the current state, per `src/ave/core/constants.py` `MU_0`/`EPSILON_0`)? See [`research/2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-result.md`](../../../research/2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-result.md) §4. Grant adjudication needed before a Phase 3a-rev workstream is scoped.
  - **Q-LCR-2 (framework-extension question, surfaced 2026-05-26 Phase 3a)**: does the corpus need a separate workstream that derives μ₀ and ε₀ themselves from K4-TLM substrate primitives BEFORE Z₀ can earn Class 2 substrate-mechanism emergence on the numerical-value sub-axis? See result doc §4. Three candidate paths sketched (derive μ₀ first, derive ε₀ first, or derive both jointly from a single K4 geometric primitive). Pre-survey did not surface any of these in corpus; this is plausibly a real corpus gap.
  - **Close step 7 (RESCOPE-path, deferred to Phase 3b)**: make explicit the substrate-mechanism content of "topological-thread mode inherits substrate-impedance Z by lattice-continuity" at `phase-locked-topological-thread.md` line 27. Currently asserted-without-tracing. Lattice-eigenvalue-continuity argument (the bound mode's characteristic-impedance equals the K4-TLM substrate's transverse-mode eigenvalue by substrate-mode-spectrum continuity, not by tuned external coupling) is the substrate-mechanism content to be made explicit. Recommended sequencing: alongside Q = ∞ derivation in Phase 3b since both involve substrate-mode-spectrum arguments.

---

## Quantum Foam as RMS Noise; Virtual Particles as Failed Topologies
<!-- id: clm-t1okz0 -->

- _Specific Claims_
  - The "Quantum Foam" of standard cosmology is reframed as the irreducible thermal RMS noise floor of the LC network at $T > 0$ — the chaotic baseline electrical AC transients, not a literal boiling of geometry.
  - "Virtual particles" are reframed as **failed topologies**: transient localized phase twists from thermal node noise that lack the sustained inductive tension to close into a stable unknot, unwinding back into the noise floor.
  - This provides a deterministic mechanical origin for Zero-Point Energy bounded by the finite local node geometry.
- _Specific Non-Claims and Caveats_
  - Does NOT claim AVE solves the Cosmological Constant Problem at the formula level — the leaf cites the $\sim 120$-orders-of-magnitude discrepancy as motivation, but does not derive the observed dark energy density from the noise-floor reframing in this leaf. Cosmological-constant resolution lives in the Vol 3 dark-energy / phantom-energy chain (lattice latent-heat reinterpretation), not in Vol 1 Ch.3.
  - The "failed topologies" picture is **interpretive**; it does not produce new observables relative to standard QFT virtual-particle calculations at the perturbative level. Falsifiability rests on unrelated AVE predictions (running $\alpha$, GUP cutoff, etc.), not on the foam-as-noise reframing per se.

> **Leaf references:** [quantum-foam-virtual](./dynamics/ch3-quantum-signal-dynamics/quantum-foam-virtual.md).

### Quality
- confidence: 0.70
- solidity: 0.70 (ok to build on, see caveats)
- rationale: The reframe — "Quantum Foam = irreducible thermal RMS noise of the LC network at $T > 0$" and "virtual particles = failed topologies (transient phase twists lacking sustained inductive tension to close into stable unknots)" — is a coherent ontological reinterpretation given Axiom 1's discrete LC network. The claim-quality entry correctly self-bounds: this is interpretive, not a new prediction; doesn't claim cosmological-constant resolution at the formula level; falsifiability rests on unrelated AVE predictions. Methodology is properly disclosed, lands the entry at the 0.7 rubric band. No entry-level scored dependencies.
- strengthen-by:
  - Quantitatively map AVE thermal-noise-floor predictions to specific QFT virtual-particle calculations at the perturbative level, establishing operational equivalence (or producing a falsifiable divergence)
  - Connect to the Vol 3 dark-energy / phantom-energy chain to clarify what the "failed topologies" reframe predicts (vs reframes) about cosmological-constant magnitude

---

## Asymptotic Hubble Constant $H_\infty$ and MOND $a_0$ (Vol 1 Derivation; Cross-Cutting Caveats)
<!-- id: clm-m3z5ux -->

Vol 1 Ch.4.5 contains the original $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2) \approx 69.32$ km/s/Mpc derivation and the MOND $a_0 = cH_\infty/(2\pi) \approx 1.07\times 10^{-10}$ m/s² hoop-stress projection. The substantive boundary caveats are catalogued in the [vol3 Asymptotic Hubble Constant entry](../vol3/claim-quality.md) and [vol3 MOND Acceleration Scale entry](../vol3/claim-quality.md). Vol 1-specific notes:

- _Specific Claims_
  - The two formulae are derived once in Vol 1 Ch.4.5 from the canonical hardware scales $\{\ell_{node}, \alpha, G\}$ + the Unruh-Hawking de Sitter horizon temperature; downstream chapters reuse them.
  - The hoop-stress projection $a_{genesis} = a_r/(2\pi)$ applies the classical continuum-mechanics result $T = F_r/(2\pi)$ to a 1D closed topological loop embedded in a 3D radially expanding manifold.
- _Specific Non-Claims and Caveats_
  - The Hubble-derivation "geometric-consistency-proof" caveat (the Machian $\xi$ embeds $R_H \equiv c/H_\infty$ in the definition of $G$) lives in the Vol 3 lattice-genesis leaf, not in Vol 1 Ch.4.5. The Vol 1 derivation should not be summarized as an independent ab-initio prediction of $H_0$ without consulting the Vol 3 claim-quality entry.
  - The MOND $a_0$ deficit (-10.7%) and the Pitfall #4 (no MOND drag at high $g$, $S(g_N/a_0) = 0$ when $g_N \gg a_0$) are documented in detail in the vol3 sidecar; flagged here because Vol 1 introduces the formula.
  - Vol 1 dark-sector framings ("Bullet Cluster as decoupled refractive shockwave"; "DAMA/LIBRA vs XENON as transverse-shear impedance mismatch") are **interpretive reinterpretations**, not quantitative predictions. They reframe established observations within the LC-substrate ontology but do not output new numerical values to test.

> **Leaf references:** [dark-sector](./dynamics/ch4-continuum-electrodynamics/dark-sector.md), [mond-hoop-stress](./dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md).

### Quality
- confidence: 0.55
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation [α^-2 factor in H_∞]
  - clm-5xon03 — Zero-Parameter Closure Status [consistency-proof framing of H_∞]
  - clm-crbl60 — Vacuum Bulk Mass Density and Shear Modulus [G_vac/ρ_bulk for the √2 c = √(K/ρ) bulk-modulus (dilatational) compression speed; per 2026-06-08 c_L reconciliation this √2 c is the bulk-modulus speed, NOT the longitudinal P-wave √(10/3) c = √((K+4G/3)/ρ)]
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.55, 0.62)]
- rationale: The leaf now honestly discloses H_∞ = 28π m_e^3 cG/(ℏ^2 α^2) as a Class E operating-point projection / geometric-consistency identity (G taken as CODATA input; the Machian ξ embeds R_H in G) rather than an ab-initio prediction, and a_0 = cH_∞/(2π) inherits Class E status via the Hoop-Stress projection. The MOND a_0 carries a real -10.7% deficit, and the 1/(2π) hoop-stress factor is imported from classical continuum mechanics rather than derived from AVE micropolar dynamics; ~~the prior √2-vs-√(10/3) longitudinal-speed flag is resolved here as v_longitudinal = √(2G_vac/ρ_bulk) = √2 c, consistent with the K=2G operating point.~~ **[2026-06-08 c_L reconciliation — Rule 12 reversal, Grant-accepted: the √2-vs-√(10/3) flag is REVERSED. The canonical LONGITUDINAL P-WAVE speed is c_L = √((K+4G/3)/ρ) = √(10/3) c ≈ 1.83c at K=2G (Poisson ν=2/7; canonical vol_2 Ch 7, eq cp_from_nu). The √2 c = √(K/ρ) = √(2G/ρ) form is the BULK-MODULUS (dilatational/fluid) speed, which DROPS the 4G/3 shear term and is NOT the solid P-wave; it is retained only as the bulk-modulus quantity — e.g. the K4 A_1 scalar port-mode (clm-uu1qbo) measured at cardinal-axis v/c=1.45. This rescope does NOT touch the MOND a_0 result (a_0 = c·H_∞/2π never used the longitudinal speed) nor the cardinal-axis measurement (which is the bulk-modulus A_1 mode, not the P-wave).]** Two imported/identity steps (CODATA G + the classical 1/(2π) hoop-stress projection) plus the unresolved −10.7% a_0 deficit place the local rigor in the 0.5 band — just below the prior 0.60.
- strengthen-by:
  - Derive the 1/(2π) hoop-stress projection from AVE micropolar dynamics rather than importing the classical T = F_r/(2π) result
  - Close the cosmic-scale 2π via explicit de Sitter-horizon Hoop-Stress closed-loop integration (Step 5 of the rigorous-derivation prereg, still open) instead of routing through Unruh-Hawking
  - Close the MOND a_0 -10.7% deficit by carrying higher-order corrections or re-deriving the hoop-stress geometry from first principles
  - Convert the H_∞ consistency identity into a true downstream prediction by deriving G from local thermodynamic balance independent of R_H (open Chain B')
---

## Bullet Cluster as Ponderomotive Halo + Einstein Lensing on Gordon Optical Metric
<!-- id: clm-527k22 -->

The bullet-cluster lensing-baryon spatial offset is explained as **ponderomotive-class substrate-strain halos that co-move with stars + standard Einstein lensing through the Gordon optical metric**, with no exotic particles and no propagating shockwave. Stars source inhomogeneous $h_\perp$ halos via Axiom 2 TKI charge-to-strain coupling + Axiom 4 saturation kernel; the halos pass through each other ballistically during cluster collision (long-wavelength substrate modes superpose linearly); baryonic gas is collisionally stopped at the X-ray bow shock; lensing tracks the halos = star centers, not the gas. This replaces the prior TT-tensor-shockwave mechanism (retired 2026-05-17 audit; full prereg at `research/2026-05-17_C13b_bullet_cluster_prereg.md`).

- _Specific Claims_
  - Each cluster's mass generates an inhomogeneous substrate-strain halo via Axiom 2 (TKI charge-to-strain) + Axiom 4 (saturation kernel); the same mechanism as AVE-PONDER lab-scale ponderomotive tests scaled up by ~$10^{20}$ in mass and length.
  - The halo co-moves with stars because stars source the strain; the halo is a substrate response to the mass distribution, locked to its generating mass.
  - During cluster collision: baryonic gas is collisionally stopped (forming the visible X-ray bow shock); stars + their substrate-strain halos pass through each other ballistically; strains do not collide with strains because the substrate is linear at cluster wavelengths.
  - Lensing tracks the substrate-strain halos via standard Einstein deflection through the Gordon optical metric ($n_\perp = 1 - h_\perp$); lensing peaks align with halos = star centers, not with gas.
  - The lensing-baryon offset (~150 kpc projected, ~25 arcsec at z = 0.30) is the post-collision kinematic separation between gas (stuck at collision point) and stars + halos (moved apart with cluster centers); no propagation physics required.
  - AVE-distinct quantitative prediction (vs WIMP DM): halo strength is determined entirely by baryonic content + geometry — halo-to-baryon ratio is a UNIVERSAL function, not a per-cluster fit parameter. WIMP picture allows substantial scatter; AVE picture requires tight correlation across merging-cluster systems. Ultra-diffuse galaxies supposedly lacking dark matter (NGC 1052-DF2 / DF4) or cD galaxies with high DM-to-baryon ratios, if real, would falsify the AVE universal-correlation prediction.
- _Specific Non-Claims and Caveats_
  - The qualitative bullet-cluster offset is reproduced by both AVE-ponderomotive-halo and WIMP DM pictures; this leaf's discrimination claim is the tight halo-to-baryon UNIVERSAL correlation (testable via weak-lensing convergence vs baryonic content across many merging-cluster systems), NOT the qualitative offset itself.
  - The prior TT-tensor-shockwave framing (over-parameterized, contradicted $v_T = c$) is explicitly retired per Grant adjudication 2026-05-17 evening (commit d953ccf). The DAMA section is also reframed (transverse-phonon → refresh-rate interpretation per `research/2026-05-17_C14-DAMA_amplitude_prereg.md`).
  - Standard Einstein lensing is taken as the mechanism for light deflection through $h_\perp$ gradients; this is shared with GR Shapiro/Einstein deflection and is not AVE-distinct in isolation. The AVE-distinct content is the substrate-strain halo SOURCE (Axiom 2 + Axiom 4 ponderomotive mechanism, not exotic-particle DM).

> **Leaf references:** [bullet-cluster](./dynamics/ch4-continuum-electrodynamics/bullet-cluster.md).

### Quality
- confidence: 0.40
- depends-on:
  - clm-dfaiwj — Topo-Kinematic Isomorphism [Axiom 2 charge-to-strain coupling that sources the halo]
  - clm-crbl60 — Vacuum Bulk Mass Density and Shear Modulus [linear substrate response at cluster wavelengths]
- solidity: 0.40 (do not build on, rework needed) [= min(0.40, 0.62)]
- rationale: The leaf is an internally consistent qualitative mechanism (ponderomotive strain halos co-move with stars, gas decouples, Einstein lensing on the Gordon metric tracks halos) and honestly concedes the qualitative offset is degenerate with WIMP DM; but the AVE-distinct discriminator — a UNIVERSAL halo-to-baryon correlation — is asserted, not derived, and the ~150 kpc offset is matched-by-construction ("cluster centers separated by 150 kpc") rather than predicted, with the 10^20 AVE-PONDER scale-up stated without a scaling derivation. Qualitative where the framing implies quantitative discrimination, so the local link sits in the significant-gap band.
- strengthen-by:
  - Derive the universal halo-to-baryon ratio as an explicit function of baryonic content + geometry (currently asserted), so the discrimination claim becomes a numerical prediction rather than a correlation expectation
  - Justify the ~10^20 mass/length scale-up from AVE-PONDER lab physics to cluster scale — show the Axiom 2 + Axiom 4 mechanism survives the regime change rather than asserting "same physics, different scale"
  - Predict the lensing-baryon offset distance from collision kinematics + cluster mass profiles rather than matching it to the observed 150 kpc post hoc
  - Quantify a falsifiable scatter bound for the universal correlation against the WIMP-allowed scatter (NGC 1052-DF2/DF4 framed as falsifier but no quantitative threshold given)
---

## Macroscopic Yield Stress $\tau_{yield}$ — Order-of-Magnitude Bound, Not Precision
<!-- id: clm-8ep2b4 -->

- $\tau_{yield} = (\rho_{bulk} c^2)\cdot(6\,\mathcal{V}_{crossing})\cdot(p_c/8\pi) \approx 1.04\times 10^{22}$ Pa
- _Specific Claims_
  - The macroscopic yield stress is constructed from baseline bulk energy density $\rho_{bulk}c^2$, the dual-reactance count ($\mathcal{V}_{total} = 2.0$ — the node's two reactance sectors $X_C + X_L$, Axiom 1; counted, not integrated; canonical at `common/dual-reactance-storage-taxonomy.md`), and the geometric porosity factor $\alpha = p_c/8\pi$. (The $6\,\mathcal{V}_{crossing}$ writing is a circular re-factoring of the same $\mathcal{V}_{total} = 2.0$, a vestige of the retired geometric halo-volume framing, not an independent geometric derivation.)
  - The Sagnac-RLVE rotational-shear interferometer is proposed as a tabletop falsification test; the predicted phase shift scales with rotor density and shear rate, distinct from Lense-Thirring (which scales with Newtonian potential).
- _Specific Non-Claims and Caveats_
  - The "Asteroid Belt / Oort Cloud as transition traps at the saturation isocline" framing is an **interpretive prediction**, not a quantitative match to observed orbital-debris distributions. Specific numerical agreement (where present) lives in the vol3 solar-system entries.
  - The Sagnac-RLVE proposal requires the $1000:1$ asymmetric chevron geometry (1 µm tips against 1 mm troughs). The expected phase-shift magnitude is not given in this leaf; falsifiability is asserted in principle, not characterized in detail.
  - "Mutual inductance is annihilated ($\eta \to 0$) inside saturated regions" is the same claim as cross-cutting Symmetric Saturation ($Z = Z_0$ invariant, $\Gamma = 0$); it is not "drag goes to zero from infinity" — drag is bounded and structured throughout the regimes.

> **Leaf references:** [magnetic-saturation](./dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md).

> **🔴 $X_L$ = the FLYWHEEL (spin/frequency-regulation) sector, NOT the rest-mass store (2026-06-20, Rule 12 — the rationale's "magnetic→$X_L$→rest mass (clm-lv3uw1)" gloss below PRESERVED unedited; Grant-CONFIRMED mass-sector ruling; SYNCS this entry to the PR#260 banner at `common/dual-reactance-storage-taxonomy.md:189`).** Where the rationale glosses the **magnetic** saturation branch ($\mu_{eff}\to0$) inductive sector "$X_L$" as **rest mass**, the **$X_L$ = the inductive FLYWHEEL = the T2 / Cosserat micro-rotation ($\omega$) spin sector** (the spin/Larmor clock), whose mass-gap is the Compton/Larmor *clock* gap, **NOT** the rest-mass store. The **rest mass is the A1 longitudinal DILATATION** depression (`vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20` "A1 dilatation-MASS"). The dual-reactance **COUNT** ($\mathcal{V}_{total}=2.0$, $X_C+X_L$) — the load-bearing factor in $\tau_{yield}$ here — is **UNAFFECTED**; only the "$X_L$ = rest mass" *label* is re-scoped. Consistency-class relabel, body preserved per Rule-12.

### Quality
- confidence: 0.50
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity 0.63) [for $p_c = 8\pi\alpha$ in the porosity factor]
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.63)]
- rationale: The formula $\tau_{yield} = (\rho_{bulk} c^2)\cdot\mathcal{V}_{total}\cdot(p_c/8\pi)$ uses the dual-reactance count $\mathcal{V}_{total} = 2.0$ (the node's two reactance sectors $X_C + X_L$, Axiom 1; counted, not integrated; NOT a FEM-integrated volume — the prior "FEM-verified to 0.13%" Borromean-halo-volume provenance was fabricated and is dropped, see `common/dual-reactance-storage-taxonomy.md`; the $6\,\mathcal{V}_{crossing}$ writing is a circular re-factoring of the same value, not an independent derivation) as a load-bearing factor in a formula presented as governing **macroscopic / cosmological** lattice mechanics (planetary slipstreams, asteroid belts, dark-sector boundary-layer transitions). The justification for embedding the proton-provenanced reactance count in a macroscopic vacuum formula is asserted, not derived — this is the substantive open structural question that lands the entry at the 0.5 rubric band. **(The separate "does the yield *stress* scale with the reactance-sector count" open item is now RESOLVED — STAYS-INHERITED, Grant 2026-06-02: the yield event is the electric (ε-only) single-sector branch (`master-equation.md:78`), so the ×2 is the inherited $\mathcal{V}_{total}$ count-tag naming which Axiom-4 branch this is, NOT an $E_C + E_L$ within-event sum; the count-2 manifests at the yield scale as the two mutually-exclusive saturation branches — electric→$X_C$→$\tau_{yield}$, magnetic→$X_L$→rest mass (clm-lv3uw1) — the same $X_C + X_L$ count as baryon $\mathcal{V} = 2$, a Class B manifestation with no empirical discriminator; see `common/dual-reactance-storage-taxonomy.md` §τ_yield + `research/2026-06-02_tau-yield-reactance-count.md` §7. This resolution does NOT lift confidence — it is a provenance/structural identification, not a derivation; the macroscopic-embedding question above is the binding open item and is unaffected.)** Order-of-magnitude framing is correctly disclosed; quantitative claims (specific $1.04\times 10^{22}$ Pa value, asteroid-belt / Oort-cloud isocline matching) are interpretive at this scope. Solidity is 0.50 (= min(0.50, 0.63)) capped by the local confidence; the α dependency via $p_c = 8\pi\alpha$ (clm-0ktpcn currently solidity 0.63 post-2026-05-27 Phase 3-A4 PARTIAL-band amendment per PR #47+#48) is the dep-cap upper bound but the local-confidence floor 0.50 is the tighter bottleneck so own ceiling binds and amendment cascade does NOT change this entry's solidity. (The 2026-05-06-era 0.28 → 0.21 drop reflected the trf3bd-rebound dependency chain that has since been superseded by the 2026-05-17 body-topology resolution and the 2026-05-26 Phase-2-A cascade lift.)
- strengthen-by:
  - Justify (or replace) the use of the proton-provenanced dual-reactance count ($\mathcal{V}_{total} = 2.0$) in a formula governing macroscopic / cosmological lattice mechanics; either derive why the proton's reactance-sector count is universally embedded in the macroscopic vacuum, or replace with a generic topological factor derived from lattice properties alone
  - Quantify the predicted Sagnac-RLVE phase shift (currently "asserted in principle, not characterized in detail")
  - Quantitatively match "asteroid belt / Oort cloud" formation positions to $\tau_{yield}$ isoclines (currently interpretive, not numerical)
  - Strengthen Golden Torus α Derivation (`clm-0ktpcn`); $p_c = 8\pi\alpha$ enters the formula

---

## Universal Spatial Tension Mass Scaling (Lepton + Nuclear)
<!-- id: clm-zw6mut -->

- $M_{topo} = (\hbar/c)/\oint \vec r_{ij}\cdot d\vec\ell$
- _Specific Claims_
  - The same $1/r$ universal tension governs both lepton mass hierarchies and nuclear pairwise binding. Three Cosserat sectors (translation, rotation, curvature-twist) produce three lepton generations:
    - Electron: ground-state unknot, $m_e = \hbar/(c\,\ell_{node})$ (definitional).
    - Muon: torsion sector $\alpha\sqrt{3/7}$, $m_\mu \approx 107.0$ MeV ($+1.24\%$ vs CODATA).
    - Tau: curvature sector $8\pi/\alpha$, $m_\tau \approx 1760$ MeV ($-0.95\%$).
  - Nuclear binding uses the same operator: Neon-20 = $5\alpha$ Triangular Bipyramid with $K_{mutual} = m_p c^2$ summed over the 10 pairwise $\binom{5}{2}$ inductive links.
- _Specific Non-Claims and Caveats_
  - The Neon-20 result is **NOT zero-parameter ab initio**. Per the leaf's explicit "Methodology disclosure": within the $(Z,A)$-forced bipyramid topology, the inter-alpha distance $R_{bipyramid}$ is **the single fitted scalar adjusted per nucleus**. The optimizer converges at $R_{bipyramid} \approx 81.158\,d$.
  - The reported $<0.001\%$ Neon-20 residual is the **optimizer's convergence tolerance on $R$**, not an independent prediction error on the mass.
  - The falsifiable axiomatic content of the nuclear chain is: (1) cluster topology as a function of $(Z,A)$ via minimum-impedance packing, (2) coupling $K_{mutual} = m_p c^2$, and (3) the parameter count = one scalar per nucleus (vs $\sim 5$ in liquid-drop / shell models). This is **the** Vol 6 methodology; the Vol 1 Neon-20 mention is one application, not a demonstration of zero-parameter nuclear masses.
  - Lepton-mass derivations are quoted with errors ($+1.24\%$, $-0.95\%$). These are not sub-percent; summary tables that drop the error column over-claim. The full Cosserat-sector derivation lives in Vol 2 Ch 5; Vol 1 provides the headline result.

> **Leaf references:** [mass-unification](./operators-and-regimes/ch5-universal-spatial-tension/mass-unification.md), [scale-invariance](./operators-and-regimes/ch5-universal-spatial-tension/scale-invariance.md), [scale-invariant-predictions](./operators-and-regimes/ch5-universal-spatial-tension/scale-invariant-predictions.md).

### Quality
- confidence: 0.60
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity 0.63) [for muon's $\alpha\sqrt{3/7}$ and tau's $8\pi/\alpha$ sector factors]
  - clm-unk0bd — Electron Body Topology = Unknot (solidity 0.65) [the "ground-state unknot" framing is load-bearing for the lepton mass formula and the "three structural dimensions of the unknot" Cosserat-sector argument]
- solidity: 0.60 (use as input only, don't build deeper) [= min(0.60, 0.63)]
- rationale: The cross-scale operator framing — same universal $1/r$ tension governs lepton and nuclear binding — is structurally claimed but the three-Cosserat-sector-to-three-lepton-generation identification (translation/torsion/curvature-twist) is asserted, not derived from the four axioms. Lepton-mass deviations are non-trivial: muon $+1.24\%$, tau $-0.95\%$ — correctly disclosed but not sub-percent. Nuclear methodology is honestly disclosed as **one fitted scalar per nucleus** (Vol 6); the Vol 1 Neon-20 mention is one application. The reported "$<0.001\%$ Neon-20 residual" is the optimizer convergence tolerance, not an independent prediction error — claim-quality entry correctly flags this. Local confidence held at 0.6 because the structural identifications and the residual lepton-mass percentages are real open work. **Body-topology dependency (post-2026-05-17 resolution + 2026-05-26 Phase-2-A cascade lift + 2026-05-27 Phase 3-A4 PARTIAL-band amendment per PR #47+#48):** the cited leaves (`scale-invariance.md`, `scale-invariant-predictions.md`, `mass-unification.md`) explicitly use the "ground-state unknot" framing for the electron and "the three structural dimensions of the unknot" for the lepton-generation hierarchy. Under the canonical `clm-unk0bd` (solidity 0.65 post-cascade) and `clm-0ktpcn` (solidity 0.63 post-Phase-3-A4-amendment), this entry inherits solidity 0.60 (= min(0.60, 0.63, 0.65)), **capped by the local confidence 0.60** (own ceiling binds; clm-0ktpcn dep-cap at 0.63 is the upper bound but no longer the binding constraint). The asserted "three structural dimensions" argument is unknot-specific and stable under the post-2026-05-17 body-topology resolution; the 2026-05-06-era trf3bd-vs-unknot cross-leaf conflict is closed.
- strengthen-by:
  - Derive the three-Cosserat-sectors-to-three-lepton-generations identification (translation/torsion/curvature-twist) from the four axioms (currently a structural identification with sector-specific coupling factors $\alpha\sqrt{3/7}$ and $8\pi/\alpha$ that are asserted, not derived)
  - Reduce the lepton-mass deviations (muon $+1.24\%$, tau $-0.95\%$) by carrying higher-order corrections in the Cosserat sector chain
  - Strengthen Golden Torus α Derivation (`clm-0ktpcn`); α appears in both muon and tau sector factors
  - Add a separate claim-quality entry for the proton mass derivation; it feeds the Vol 6 nuclear methodology and the Vol 1 Neon-20 application as an unscored upstream input

---

## Universal Operators (Z, S, Γ) — Same Function, Different Scales
<!-- id: clm-gdd70j -->

The eight Ch.6 universal operators are the engine-level shared code paths. Boundary entries:

- _Specific Claims_
  - Each operator (Z impedance, S saturation, Γ reflection, U pairwise, Y→S multiport, $\lambda_{\min}$ eigenvalue target, FFT spectral, $\Gamma_{pack}$ packing) is implemented as **one function** called by every domain — the cross-scale identity is computational, not analogical.
  - The cross-scale Z table spans 8 distinct domains (vacuum lattice, plasma, seismic, gravitational, protein, lattice-Boltzmann fluid, galactic, antenna), all routed through `scale_invariant.impedance(mu, eps)`.
- _Specific Non-Claims and Caveats_
  - Operator-identity claims are **structural** (same code path), not predictive at any single scale. Numerical agreement at any specific application is the responsibility of the per-domain leaf, not the operator's universal status.
  - The "Universal Reflection Coefficient" cross-scale list (Pauli exclusion at $\Gamma = -1$, Moho seismic $\Gamma \approx 0.17$, antenna $S_{11}$, etc.) exemplifies this: same operator, different inputs $(Z_1, Z_2)$, different physical phenomena. Summaries that quote a list of $\Gamma$ values as "AVE predicts" should be qualified with "the operator is universal; the inputs come from per-domain physics".
  - Cross-cutting [vol3 Seismic Reflection Coefficient (Moho) entry](../vol3/claim-quality.md) makes this distinction explicit.

> **Leaf references:** [operators](../common/operators.md), [eigenvalue-target](./operators-and-regimes/ch6-universal-operators/eigenvalue-target.md), [impedance-operator](./operators-and-regimes/ch6-universal-operators/impedance-operator.md), [packing-reflection](./operators-and-regimes/ch6-universal-operators/packing-reflection.md), [pairwise-potential](./operators-and-regimes/ch6-universal-operators/pairwise-potential.md), [reflection-coefficient](./operators-and-regimes/ch6-universal-operators/reflection-coefficient.md), [saturation-operator](./operators-and-regimes/ch6-universal-operators/saturation-operator.md), [spectral-analyser](./operators-and-regimes/ch6-universal-operators/spectral-analyser.md), [y-to-s-conversion](./operators-and-regimes/ch6-universal-operators/y-to-s-conversion.md).

### Quality
- confidence: 0.80
- depends-on:
  - Axiom 4 (Universal Saturation Kernel — the S saturation operator and the impedance/reflection algebra are built on the saturation kernel)
- solidity: 0.80 (ok to build on, see caveats) [= min(0.80, 1.00)]
- rationale: The eight universal operators (Z, S, Γ, U, Y→S, λ_min, FFT, Γ_pack) are framework-level constructs derived from Axiom 4's saturation kernel and from impedance/reflection algebra; the cross-scale identity is **structural** (same code path called by every domain), not predictive at any single scale. The claim-quality entry correctly self-bounds — operator identity claims do not certify per-domain numerical agreement, which is the responsibility of each per-domain leaf. This separation of concerns is exactly right; the entry's only caveat is that summaries which list cross-domain $\Gamma$ values as "AVE predicts" are misreading the structural-identity claim. No entry-level scored dependencies — operators are framework-level.
- strengthen-by:
  - none entry-local — per-domain numerical validations live in their own claim-quality entries; this entry's claim is just the operator-reuse structural identity, which is correctly bounded

---

## Four-Regime Map — Boundary Derivations are Sector-Dependent
<!-- id: clm-b2anl4 -->

- $r_1 = \sqrt{2\alpha} \approx 0.121$ (Linear → Nonlinear); $r_2 = \sqrt{3}/2 \approx 0.866$ (Nonlinear → Yield, **spin-2 sector**); $r_3 = 1$ (Yield → Ruptured)
- _Specific Claims_
  - $r_1 = \sqrt{2\alpha}$ is derived: the leading Taylor correction $\Delta S = r^2/2$ equals the lattice's own self-coupling $\alpha$ at this point — sub-$\alpha$ corrections are physically unresolvable.
  - $r_3 = 1$ is axiomatic from Axiom 4 ($S = 0$, topology destroyed).
  - The $r_2 = \sqrt{3}/2$ boundary derives from $Q = 1/S = \ell_{\min}$ with $\ell_{\min} = 2$ for the **spin-2 sector** (gravitational waves, shear modes; minimum non-trivial multipole).
- _Specific Non-Claims and Caveats_
  - $r_2 = \sqrt{3}/2$ is **sector-dependent**, not universal. Other sectors have different $\ell_{\min}$ and thus different $r_2$:
    - Scalar sector ($\ell_{\min} = 0$): no avalanche-onset boundary in this sector; practical onset is set by other physics.
    - Photon / vector sector ($\ell_{\min} = 1$): $r_2 = 0$ (avalanche concurrent with linear breakdown); no separate Regime III.
    - Spin-2 sector ($\ell_{\min} = 2$): $r_2 = \sqrt{3}/2$ as derived.
  - The "universal regime map" framing in chapter titles is the **spin-2 form**; the lower-spin sectors collapse two boundaries together. Citations of $r_2 = \sqrt{3}/2$ without sector qualification implicitly assume spin-2.
  - The semiconductor analogy (Miller factor $M$, avalanche multiplication) is a **structural identity** (same $S$ operator), not a derivation of semiconductor breakdown from AVE axioms.

> **Leaf references:** [domain-catalog](./operators-and-regimes/ch7-regime-map/domain-catalog.md), [four-regimes](./operators-and-regimes/ch7-regime-map/four-regimes.md), [regime-equation-sets](./operators-and-regimes/ch7-regime-map/regime-equation-sets.md).

### Quality
- confidence: 0.75
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation (solidity 0.63) [for $r_1 = \sqrt{2\alpha}$ numerical value]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.75, 0.63)]
- rationale: The boundary derivations are individually sound — $r_1 = \sqrt{2\alpha}$ from leading-order Taylor truncation of $S(r)$ matching the lattice's self-coupling $\alpha$; $r_3 = 1$ axiomatic from Axiom 4 ($S = 0$); $r_2 = \sqrt{3}/2$ from $Q = 1/S = \ell_{\min}$ with $\ell_{\min} = 2$ for the spin-2 sector. The substantive open element is the **sector-specific identification of $\ell_{\min}$** (scalar/vector/spin-2 ℓ_min values are stated as "minimum non-trivial multipole" rather than derived from a specific axiom-grounded harmonic decomposition). Local confidence held at 0.75. Solidity bounded by α via $r_1$'s numerical value (currently 0.63 = min(0.75, 0.63)). The structural form $r_1 = \sqrt{2\alpha}$ survives any reasonable α value; the **numerical** boundary at 0.121 is α-dependent and tracks `clm-0ktpcn`'s solidity. (The 2026-05-06-era 0.41 → 0.31 drop reflected the trf3bd-rebound dependency chain that has since been superseded by the 2026-05-17 body-topology resolution and the 2026-05-26 Phase-2-A cascade lift; current 0.63 reflects the post-2026-05-27 Phase 3-A4 PARTIAL-band amendment per PR #47+#48.)
- strengthen-by:
  - Derive the sector-specific $\ell_{\min}$ values (scalar 0, vector 1, spin-2 2, ...) from axiom-grounded multipole decomposition rather than pattern-matching to "minimum non-trivial multipole"
  - Strengthen Golden Torus α Derivation (`clm-0ktpcn`); $r_1 = \sqrt{2\alpha}$ inherits α's solidity for numerical evaluation

---

## Domain Catalog Operating-Point Examples
<!-- id: clm-82dxbj -->

The Ch.7.2 domain catalog tabulates $r$ values across EM, gravitational, BCS, magnetic, nuclear, GW, and galactic domains. Vol 1-specific tripwires:

- _Specific Claims_
  - Solar surface, white dwarf interiors, lab capacitors and magnets, MRI scanners, LIGO GW signals: all explicitly sit deep in **Regime I** ($r \ll 1$), justifying use of unmodified standard equations.
  - Neutron star at $1.4\,M_\odot$, $R = 10$ km: $\varepsilon_{11} \approx 1.46 > 1$ — **Regime IV** (ruptured topology). This is the AVE analog of the Buchdahl limit.
  - Black hole at $r_s = 2GM/c^2$: $\varepsilon_{11} = 7/2 = 3.5$ (the factor 7 arises from the K4/SRS lattice's 7 compliance modes via $\nu_{vac} = 2/7$). Deep Regime IV.
  - LIGO GW150914 strain $h \sim 10^{-21}$ corresponds to $r \sim 10^{-20}$ — "the most deeply linear measurement in physics".
- _Specific Non-Claims and Caveats_
  - The neutron-star Regime IV identification (lattice-strain $> 1$) is **the AVE-internal compactness bound**; the cross-cutting [vol3 AVE Compactness Limit entry](../vol3/claim-quality.md) elaborates that this is stricter than the GR Buchdahl bound but is **not** validated against observed neutron-star equations of state. It is what the AVE bound implies given canonical NS parameters.
  - The galactic-domain operating point uses the empirical $a_0 \approx 1.2\times 10^{-10}$ m/s², not the AVE-derived $a_0 \approx 1.07\times 10^{-10}$. Mixing the two leads to inconsistent regime locations.
  - LIGO's "sub-$\alpha$" classification (the $\Delta S = 0.007$ correction at NS-merger surface strain $h \sim 0.01$ is below the lattice's own $\alpha \sim 1/137$ coupling) means AVE corrections are **physically unresolvable** at LIGO sensitivities — not zero, but below the noise floor of the lattice itself.

> **Leaf references:** [domain-catalog](./operators-and-regimes/ch7-regime-map/domain-catalog.md), [experimental-design-space](./operators-and-regimes/ch7-regime-map/experimental-design-space.md).

### Quality
- confidence: 0.70
- depends-on:
  - clm-b2anl4 — Four-Regime Map (solidity 0.63) [uses $r_1, r_2, r_3$ boundaries to classify domains]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.70, 0.63)]
- rationale: The catalog correctly applies the four-regime structure to specific physical systems (Solar surface, WD interiors, lab fields, NS interior, BH horizons, LIGO GW signals); the claim-quality entry honestly discloses that the AVE-internal compactness bound ($R_{\min} = 7GM/c^2$) is stricter than the GR Buchdahl bound but is **not validated** against observed neutron-star equations of state, and that the galactic-domain operating point uses empirical $a_0$ (not AVE-derived). Local confidence is sound for the application work. Solidity is heavily bounded transitively through Four-Regime Map's α dependency — every $r$ value tabulated for a specific system inherits regime-boundary numerical solidity. Current solidity 0.63 (= min(0.70, 0.63)) tracks the Four-Regime Map's α-bounded value. (The 2026-05-06-era 0.29 → 0.22 drop reflected the trf3bd-rebound chain that has since been superseded by the 2026-05-17 body-topology resolution and the 2026-05-26 Phase-2-A cascade lift; current 0.63 reflects the post-2026-05-27 Phase 3-A4 PARTIAL-band amendment per PR #47+#48.)
- strengthen-by:
  - Validate the AVE-internal compactness bound ($R_{\min} = 7GM/c^2$) against observed neutron-star equations of state (currently disclosed as not-validated)
  - Reconcile the galactic operating-point's use of empirical $a_0 \approx 1.2\times 10^{-10}$ with the AVE-derived $a_0 \approx 1.07\times 10^{-10}$ from Asymptotic Hubble Constant + MOND (`clm-m3z5ux`); using empirical introduces an undeclared empirical input
  - Strengthen Four-Regime Map (`clm-b2anl4`); regime-boundary numerical solidity propagates here
  - Strengthen Golden Torus α Derivation (`clm-0ktpcn`) transitively

---

## Vacuum Bulk Mass Density and Shear Modulus
<!-- id: clm-crbl60 -->

- $\rho_{bulk} = \xi_{topo}^2\mu_0/(p_c\ell_{node}^2) \approx 7.92\times 10^6$ kg/m³; $G_{vac} = \rho_{bulk}c^2 \approx 7.11\times 10^{23}$ Pa
- _Specific Claims_
  - The dimensionally-corrected bulk mass density is derived via $L = \xi_{topo}^{-2}m$ inductance-mass isomorphism + Voronoi cell volume $V_{node} = p_c\ell_{node}^3$.
  - $G_{vac}$ is the macroscopic 3D shear modulus of the substrate; the Cauchy bulk modulus is fixed at $K_{vac} = 2G_{vac}$ (Cauchy relation for the isotropic lattice).
  - Kinematic mutual inductance $\nu_{kin} = \alpha c\,\ell_{node} \approx 8.45\times 10^{-7}$ m²/s — close to liquid water's value, asserted as parameter-free with the identification $\kappa \equiv \alpha$.
- _Specific Non-Claims and Caveats_
  - $G_{vac}$ (3D continuum shear modulus, $\sim 10^{23}$ Pa) must NOT be confused with $G_{string} = T_{EM}/\ell_{node} \approx 5.49\times 10^{11}$ N/m (1D string tension modulus, governing single-edge stiffness). These differ by $\sim 10^{12}$; the leaf flags this distinction explicitly.
  - The $\nu_{kin}$ "close to liquid water" comparison is an order-of-magnitude consistency observation, not a derivation that the vacuum *behaves like* water in any operationally relevant sense.
  - The identification $\kappa \equiv \alpha$ (geometric scattering threshold = packing-fraction-derived self-coupling) is **asserted** in the leaf as a consequence of the porosity argument; reviewers should treat it as a structural claim, not as an independent measurement of $\kappa$.

> **Leaf references:** [lc-electrodynamics](./dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md).

### Quality
- confidence: 0.62
- depends-on:
  - clm-dfaiwj — Topo-Kinematic Isomorphism [supplies L = ξ_topo^-2 m used in m_node]
  - clm-0ktpcn — Golden Torus α Derivation [p_c = 8πα in ρ_bulk and α in ν_kin = αcℓ_node]
- solidity: 0.62 (use as input only, don't build deeper) [= min(0.62, 0.63)]
- rationale: ρ_bulk = ξ_topo^2 μ_0/(p_c ℓ_node^2) and G_vac = ρ_bulk c^2 are sound dimensional construction from ξ_topo, μ_0, p_c, ℓ_node, c, and the v_T = √(G_vac/ρ_bulk) = c cross-check passes; the 13-OOM error from conflating G_vac (3D shear) with G_string (1D edge tension) is now corrected and the two are explicitly separated. The substantive open element is the κ≡α identification for ν_kin — asserted as a consequence of the porosity argument, not derived — and the "ν_kin close to liquid water" is an order-of-magnitude observation only; the Cauchy K=2G operating point is structurally consistent with the rest of the corpus.
- strengthen-by:
  - Derive the κ≡α identification (geometric scattering threshold = packing-fraction self-coupling) from first principles rather than asserting it from the porosity argument
  - Justify the Cauchy relation K_vac = 2G_vac for the chiral micropolar lattice (it is stated as the isotropic-lattice Cauchy relation but the substrate is explicitly non-Cauchy/micropolar per the implosion-paradox argument)
  - Strengthen the Golden Torus α derivation (clm-0ktpcn); ρ_bulk, G_vac, and ν_kin all inherit α through p_c and the ν_kin prefactor
  - Drop or formalize the "close to liquid water" comparison so it is not read as a physical correspondence
---

## Implosion Paradox $\to$ Micropolar Vacuum
<!-- id: clm-9gh0a1 -->

- _Specific Claims_
  - A classical Cauchy elastic solid satisfying MacCullagh's transverse-wave condition ($\lambda = -\mu$) yields $K = -\mu/3 < 0$ — runaway implosion.
  - This forces the substrate to be a **Chiral LC (Micropolar) Continuum** with independent rotational degrees of freedom, decoupling transverse-wave propagation from the bulk modulus and permitting $K > 0$ alongside pure transverse gauge-boson propagation.
- _Specific Non-Claims and Caveats_
  - This is a **structural / no-go argument**: it rules out a Cauchy substrate, motivating the micropolar Chiral LC continuum. It does not derive the chiral SRS lattice geometry (that comes from the K4 packing / EMT closure separately).
  - Does NOT claim micropolar continua are uniquely the AVE substrate; the leaf rules out one alternative (Cauchy) and the rest of Vol 1 motivates the specific chiral choice.

> **Leaf references:** [implosion-paradox](./axioms-and-lattice/ch2-macroscopic-moduli/implosion-paradox.md).

### Quality
- confidence: 0.85
- depends-on:
  - Axiom 1 (Substrate Topology — the no-go argument forces the chiral micropolar/Cosserat substrate of the K4 vacuum)
- solidity: 0.85 (ok to build on) [= min(0.85, 1.00)]
- rationale: A clean structural / no-go argument grounded in standard continuum mechanics: a classical Cauchy elastic solid satisfying MacCullagh's transverse-wave condition ($\lambda = -\mu$) requires $K = -\mu/3 < 0$, which is unphysical. The claim-quality entry correctly bounds this as a no-go argument that *rules out* a Cauchy substrate — it does not claim to uniquely identify the AVE substrate as micropolar (the chiral SRS specifics come from K4 packing / EMT, separately disclosed). No entry-level scored dependencies — pure classical continuum mechanics + Axiom 1's transverse-wave constraint.
- strengthen-by:
  - none — the no-go argument is correctly self-bounded; further pin-down of "the substrate must be chiral SRS specifically" lives in EMT (`clm-9s9apq`) and Vacuum Bulk Mass Density (`clm-crbl60`) entries

---

## Topo-Kinematic Isomorphism $[Q] \equiv [L]$
<!-- id: clm-dfaiwj -->

- $\xi_{topo} \equiv e/\ell_{node}$ [C/m]; $1\,\Omega = \xi_{topo}^{-2}$ kg/s
- _Specific Claims_
  - The Axiom 2 mechanism reframes charge as a discrete geometric dislocation (localized phase twist); the SI dimensions of charge and length become identified at scaling $\xi_{topo}$.
  - The full SI-dimensional table (V↔F, I↔v, Z↔kinematic impedance, L↔m, C↔1/k, $\mu_0$↔linear density, $\varepsilon_0$↔inverse tension) follows from this single identification.
- _Specific Non-Claims and Caveats_
  - This is a **dimensional isomorphism**, not a claim that charge "becomes" length in any operationally measurable sense at the engineering scale. SI conversions are exact within the framework's definitions; experimental discrimination depends on AVE's downstream predictions, not on the isomorphism itself.
  - $\xi_{topo}$ is INVARIANT-C2 in the cross-volume invariants (Vol 2/4/5 reuse it for atomic mappings, circuit engineering, biological mass/stiffness translations). Its canonical leaf-level definition lives in Vol 5; Vol 1 establishes it via Axiom 2 mechanism.

> **Leaf references:** [axiom-definitions](./axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md), [constitutive-moduli](./axioms-and-lattice/ch2-macroscopic-moduli/constitutive-moduli.md), [topo-kinematic-isomorphism](./axioms-and-lattice/ch2-macroscopic-moduli/topo-kinematic-isomorphism.md).

### Quality
- confidence: 0.80
- depends-on:
  - Axiom 2 (Topo-Kinematic Isomorphism — charge as a discrete geometric dislocation, $[Q] \equiv [L]$ at scaling $\xi_{topo}$)
- solidity: 0.80 (ok to build on, see caveats) [= min(0.80, 1.00)]
- rationale: $\xi_{topo} = e/\ell_{node}$ is direct from Axiom 2's topo-kinematic isomorphism mechanism; the SI-dimensional table (V↔F, I↔v, Z↔kinematic impedance, L↔m, C↔1/k, μ_0↔linear density, ε_0↔inverse tension) follows from this single identification by dimensional algebra. The claim-quality entry correctly self-bounds: this is a **dimensional isomorphism**, not an operational claim that charge becomes length at the engineering scale. The cross-volume reuse (Vol 2 atomic mappings, Vol 4 circuit engineering, Vol 5 biology mass/stiffness translations) is structural. INVARIANT-C2 carries the same bound at project-wide invariant level. No entry-level scored dependencies — Axiom 2's mechanism is framework-input.
- strengthen-by:
  - none entry-local — the isomorphism is correctly self-bounded as a dimensional identity given Axiom 2's mechanism

---

## Pauli Exclusion as Impedance Reflection (Vol 1 Mechanism Statement)
<!-- id: clm-b9eura -->

- $\Gamma = (Z_{knot} - Z_{vacuum})/(Z_{knot} + Z_{vacuum}) = (0 - 377)/(0 + 377) = -1$
- _Specific Claims_
  - At the saturated knot core, dynamic RF impedance drops to $0\,\Omega$ (RF short circuit); incoming waves at the $377\,\Omega$ vacuum boundary reflect with $\Gamma = -1$ (total phase-reversed reflection).
  - This provides the macroscopic impedance-mismatch mechanism for the Pauli Exclusion Principle and for cross-sectional area in particle physics. Two saturated knots cannot occupy the same coordinates because their respective $0\,\Omega$ boundaries reflect each other's inductive phase energy.
  - Solid matter emerges from vacuum wave mechanics through this macroscopic impedance reflection.
- _Specific Non-Claims and Caveats_
  - The "$Z_{knot} = 0$" boundary refers to **dynamic RF impedance** (transverse-wave reflection condition), not static DC impedance. Confusion of the two leads to the apparent contradiction with the Vol 3 Einstein-field-equation leaf which says "$Z \to 0$ at the horizon" while GW leaves say "$Z = Z_0$ invariant" (see [vol3 Einstein Field Equation Reinterpretation entry](../vol3/claim-quality.md) and followups file for the unresolved cross-leaf tension).
  - Does NOT claim derivation of the spin-statistics theorem or anti-symmetric wavefunction structure; the impedance-mismatch argument provides the *mechanism* for exclusion (no-overlap), not the algebraic structure of fermion statistics.
  - The cross-domain $\Gamma \to -1$ translation matrix (particle confinement / plasma cutoff / superconductor / entanglement thread) is a **structural-identity** claim across Vol 1, Vol 1 EM, Vol 3 condensed matter, Vol 1 quantum-info — same operator, different sectors.

> **Leaf references:** [phase-locked-topological-thread](./dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md), [zero-impedance-boundary](./dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md).

### Quality
- confidence: 0.55
- depends-on:
  - clm-efo113 — Master Equation EFT Validity (solidity 0.50) [the saturated-knot $Z \to 0$ behavior depends on master-equation dynamics at saturation]
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.55, 0.50)]
- rationale: The $\Gamma = -1$ formula is straightforward impedance algebra given $Z_{knot} = 0$ and $Z_{vacuum} = 377\,\Omega$. The mechanism chain (saturated knot → $\mu_{eff} \to 0$ → $Z \to 0$ → reflection $\Gamma = -1$ → standing wave = no-overlap = exclusion) shares the same load-bearing dependency as Magnetic-Branch Confinement (`clm-lv3uw1`): the master-equation EFT must remain valid through saturation. A separate concern is the cross-leaf tension flagged in the claim-quality entry: Vol 1 says $Z \to 0$ at the saturated knot core, while Vol 3 GW leaves say $Z = Z_0$ invariant in symmetric saturation — these may describe distinct physical situations (knot core vs GW horizon in symmetric gravity) but the impedance-operator usage is currently ambiguous across leaves. The entry also does NOT derive the spin-statistics theorem or anti-symmetric wavefunction structure from this mechanism — it provides exclusion-by-no-overlap, not the algebraic structure of fermion statistics.
- strengthen-by:
  - Strengthen Master Equation EFT Validity (`clm-efo113`); $\Gamma \to -1$ at saturation depends on master-equation dynamics correctly describing $\mu_{eff} \to 0$
  - **RESOLVED (2026-06-06 doc-reconcile):** the contexts are distinct, disambiguated canonically at [`electron-bh-isomorphism.md` lines 23–34](../vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md): the electron's saturated knot core is an EM impedance-mismatch wall ($Z \to 0$, $\Gamma = -1$ at the knot boundary), whereas the Vol 3 GW (symmetric-gravity) horizon keeps $Z = Z_0$ invariant ($\Gamma = 0$) and confines via a SHEAR-mode lattice phase transition ($G_{shear}\to0$). Distinct physical situations, not a contradiction; the impedance-operator usage is disambiguated by sector (asymmetric knot vs symmetric gravity).
  - Provide an axiom-grounded derivation that Pauli exclusion's NO-OVERLAP constraint follows from the impedance mismatch (currently a structural identification, not a derivation that produces fermion statistics)

---

## Discrete Kirchhoff Network Solver Methodology
<!-- id: clm-q39qct -->

Vol 1 Ch.1 §1.5 specifies the explicit-discrete numerical engine that maps the four axioms into Symplectic Euler updates on a graph of $C$-nodes and $L$-edges, and tabulates the master-constants pipeline.

- _Specific Claims_
  - The simulation engine is a strict Discrete Kirchhoff Network Solver (e.g., `simulate_ponder_01_srs_lc_mesh.py`); the continuous PDE evaluations elsewhere in the manuscript are a macroscopic-fluid approximation, not the canonical engine.
  - Edge-strain and node-displacement updates take the explicit Symplectic-Euler form $I_{new} = I_{old} + (\Delta t/L)(V_A - V_B)$ and $V_{new} = V_{old} + (\Delta t/C)(\sum I_{in} - \sum I_{out})$ respectively, enforcing local gauge invariance and energy conservation across the discrete crystal.
  - The §1.5 master-constants table maps each AVE quantity ($\ell_{node}$, $Z_0$, $\alpha$, $V_{yield}$, $\xi_{topo}$, $V_{snap}$, $G$, $S(A)$) to a single derivation source (Axiom 1 / Axiom 2 / Axiom 2 mechanism / Axiom 4 / Ch.8 Golden Torus / derived Ax 1+4).
- _Specific Non-Claims and Caveats_
  - Symplectic Euler is **first-order**; it preserves an approximate energy invariant on bounded steps but is not a long-time-stable symplectic integrator on its own. Quantitative claims that depend on long-horizon integration accuracy require a higher-order method or step-size control; the leaf does not characterize the regime of validity.
  - The §1.5 master-constants pipeline is a **routing summary**, not an independent derivation. Each row's derivation lives in the cited source (notably $\alpha$ in Ch.8 Golden Torus, $G$'s $\xi$ closure in Vol 1 Ch.4 / Vol 3); summarizing this table as "all constants derived in §1.5" misreads the routing.
  - The 3-strut-per-node connectivity assumption is the K4/SRS choice elaborated in Ch.2; this leaf states it as a methodology fixture, not a derivation. The justification for $z = 3$ (over Cauchy-Delaunay $z \approx 6$) lives in `dielectric-rupture.md` (`clm-9s9apq`), not here.

> **Leaf references:** [kirchhoff-network-method](./axioms-and-lattice/ch1-fundamental-axioms/kirchhoff-network-method.md).

### Quality
- confidence: 0.75
- depends-on:
  - clm-9s9apq — EMT Consistency Relation [supplies the z=3 chiral-SRS justification for the 3-strut-per-node connectivity used as a fixture]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.75, 0.63)]
- rationale: As a methodology spec, the leaf is complete and internally consistent: the explicit Symplectic-Euler edge-strain and node-displacement updates are correct standard Kirchhoff/leapfrog forms, and the entry's caveats accurately flag the first-order integrator limitation and that the §1.5 master-constants table is a derivation-routing summary, not an in-leaf derivation. It scores in the solid methodology band on completeness and consistency, held just below higher because the leaf states the energy-conservation/gauge-invariance property without demonstrating it and does not characterize the integrator's regime of validity.
- strengthen-by:
  - Demonstrate the claimed approximate energy/symplectic invariant numerically (bounded-step drift) rather than asserting it
  - State the stability/step-size regime for the first-order Symplectic Euler updates
  - Make explicit that the 3-strut connectivity is the K4/SRS z=3 choice and link the derivation rather than presenting it as a bare fixture
  - Add a worked validation run (e.g. recovering a known wave-speed or dispersion relation) to anchor the engine's fidelity
---

## Dielectric Lagrangian and Vector Potential as Mass Flow
<!-- id: clm-yiyyi3 -->

- $\mathcal{L}_{AVE} = \tfrac{1}{2}\epsilon_0|\partial_t\mathbf{A}|^2 - \tfrac{1}{2\mu_0}|\nabla\times\mathbf{A}|^2$; $[\mathbf{A}] = \xi_{topo}^{-1}\,[\text{kg/s}]$
- _Specific Claims_
  - The standard QFT electromagnetic Lagrangian density is recast as bulk continuous mechanical stress (Pa) on the substrate via the topological conversion $\xi_{topo} = e/\ell_{node}$; capacitive edge energy plays the role of kinetic, inductive node energy the role of potential.
  - Dimensional analysis with $\xi_{topo}$ substitution shows $[\mathbf{A}] = \xi_{topo}^{-1}\,[\text{kg/s}]$ (mass flow rate scaled by $\xi_{topo}^{-1}$), and the kinetic-energy density $\tfrac{1}{2}\epsilon_0|\partial_t\mathbf{A}|^2$ reduces to $[\text{N/m}^2]$ once $\epsilon_0 \equiv \xi_{topo}^2[\text{N}^{-1}]$ cancels the topological factor.
  - Minimizing the quantum action is therefore mathematically equivalent to minimizing inductive bulk stress in Pa.
- _Specific Non-Claims and Caveats_
  - This is a **dimensional / SI-units identification**: $[\mathbf{A}]$ acquires mass-flow units after multiplying by $\xi_{topo}^{-1}$, but the operational measurement of $\mathbf{A}$ does not change. It is a framework-internal isomorphism, not a new observable.
  - Does NOT derive the form of the Lagrangian from the four axioms; the standard EM Lagrangian is taken from Maxwell theory and rewritten in mechanical units. The identification of $\mathcal{T}$ with capacitive energy and $\mathcal{U}$ with inductive energy follows from Axiom 1 + the choice of $\mathbf{A}$ as the canonical field variable (whose generalized velocity is $\mathbf{E}$).
  - $\xi_{topo}$ is INVARIANT-C2; this leaf is one of the canonical Vol 1 sites where it is exercised (see `clm-dfaiwj` Topo-Kinematic Isomorphism for the standalone identity).

> **Leaf references:** [dielectric-lagrangian](./dynamics/ch3-quantum-signal-dynamics/dielectric-lagrangian.md).

### Quality
- confidence: 0.70
- depends-on:
  - clm-dfaiwj — Topo-Kinematic Isomorphism [Q]≡[L] [supplies ξ_topo=e/ℓ_node used in the C≡ξ_topo·m substitution throughout]
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.80)]
- rationale: The dimensional derivation is worked explicitly line by line — [A]=V·s/m=kg·m/(s·C), substitution C≡ξ_topo·m yields [A]=ξ_topo⁻¹[kg/s], and the ε₀ factor cancels the ξ_topo² to deliver [N/m²] — and I verified these unit reductions; it is a careful, self-consistent dimensional/SI identification. The entry correctly flags that it does NOT derive the Lagrangian form from the axioms (taken from Maxwell and rewritten) and that the ε₀≡ξ_topo²[N⁻¹] substitution is imported from Ch.2 rather than established here, which is the one clearly-flagged matched step.
- strengthen-by:
  - Carry the ε₀≡ξ_topo²[N⁻¹] capacitive-compliance result into this leaf (or tighten the Ch.2 link) since the Pa cancellation hinges on it
  - State that this is a dimensional isomorphism with no change to the operational measurement of A, to forestall over-reading it as a new observable
  - Verify the potential-energy term (1/2μ₀)|∇×A|² reduces to the same N/m² units, not only the kinetic term
  - Make the T↔capacitive / U↔inductive role assignment a derived consequence of E=-∂ₜA rather than an assignment-by-choice
---

## Paley-Wiener / Quantum Hilbert-Space Isomorphism
<!-- id: clm-yc7fgm -->

- $\Psi(\mathbf{x},t) = \mathbf{A}(\mathbf{x},t) + i\,\mathcal{H}_{transform}[\mathbf{A}(\mathbf{x},t)]$
- _Specific Claims_
  - The substrate lattice acts as a spatial Nyquist sampling grid; band-limited signals on it form a Reproducing Kernel Hilbert Space — the Paley-Wiener space $PW_{\pi/\ell_{node}}$ with maximum spatial frequency $k_{max} = \pi/\ell_{node}$.
  - The complex quantum state vector $\Psi(\mathbf{x},t)$ is constructed from the real lattice potential $\mathbf{A}(\mathbf{x},t)$ via the standard signal-processing Hilbert transform (analytic-signal extension).
  - The complex Hilbert space of standard QM is **formally identical** to the Paley-Wiener / analytic-signal representation of the discrete vacuum hardware.
- _Specific Non-Claims and Caveats_
  - The identification is a **formal isomorphism** between two function spaces (band-limited signals on a Nyquist grid $\leftrightarrow$ complex QM state vectors) — it does not by itself derive the dynamical evolution (Schrödinger equation), the Born rule, or operator algebra. Those derivations live in sister leaves (`clm-7zuwtm` Schrödinger from circuit, `clm-ldmvwi` Born rule).
  - The Paley-Wiener / analytic-signal construction is **standard signal-processing mathematics**; the AVE-specific claim is the identification of the discrete lattice with the Nyquist grid (Axiom 1), not the analytic-signal machinery itself.
  - Does NOT claim the Hilbert transform is an operationally distinguishing experiment vs. standard QM; once the isomorphism is established, all standard-QM Hilbert-space predictions transfer automatically.

> **Leaf references:** [paley-wiener-hilbert](./dynamics/ch3-quantum-signal-dynamics/paley-wiener-hilbert.md).

### Quality
- confidence: 0.65
- depends-on:
  - clm-nq2kcc — GUP / Brillouin Zone [shares the Nyquist/discrete-graph foundation resting on Axiom 1's lattice pitch]
- solidity: 0.65 (ok to build on, see caveats) [= min(0.65, 0.70)]
- rationale: Each mathematical step is standard and correctly stated (Nyquist pitch k_max=π/ℓ_node, Whittaker-Shannon reconstruction → Paley-Wiener RKHS, analytic-signal/Hilbert-transform extension), and the AVE-specific content is cleanly isolated to identifying the physical lattice with the Nyquist grid via Axiom 1. The "formally identical to standard-QM Hilbert space" step is a strong identification that the entry correctly flags as a formal function-space isomorphism not deriving Schrödinger dynamics, the Born rule, or operator algebra — a clearly-flagged matching step that caps the local rigor at the upper-sound band.
- strengthen-by:
  - State explicitly that the PW↔QM identification is an isomorphism of function spaces only, and that no dynamical content transfers without the sister Schrödinger/Born derivations
  - Verify the analytic-signal construction is well-defined on the 3D lattice (the Hilbert transform is natively 1D; multidimensional analytic signals require a chosen orientation/Riesz transform)
  - Confirm band-limitedness and the RKHS reproducing kernel explicitly for the chiral-K4 Brillouin zone rather than a generic cubic Nyquist grid
  - Identify any operationally distinguishing prediction (or state none exists, deferring falsifiability to sibling leaves)
---

## Nonlinear Telegrapher / Euler-Heisenberg $E^4$ / Kerr $\chi^{(3)}$
<!-- id: clm-ph2uux -->

- $U \approx \tfrac{1}{2}\epsilon_0(\Delta\phi)^2 - \tfrac{3}{8\alpha^2}\epsilon_0(\Delta\phi)^4$
- _Specific Claims_
  - The 1D continuous-transmission-line nonlinear telegrapher equation is the dimensional-homogeneity-preserving form on a single-edge limit of the Master Equation, with $\epsilon(\Delta\phi)$ supplied by Axiom 4's saturation kernel.
  - Taylor-expanding $\epsilon(\Delta\phi) = \epsilon_0\sqrt{1-(\Delta\phi/\alpha)^2}$ to leading order produces the $D \propto (\Delta\phi)^3$ Kerr ($\chi^{(3)}$) optical nonlinearity and the $U \propto (\Delta\phi)^4$ correction structurally identical to the **Euler-Heisenberg QED Lagrangian** density.
  - As $\Delta\phi \to \alpha$, the local wave speed $c_{eff} = c_0[1-(\Delta\phi/\alpha)^2]^{-1/4}$ diverges; the high-amplitude peak overruns its base, producing a forward structural shockwave that provides a continuous-mechanical origin for discrete pair-production.
- _Specific Non-Claims and Caveats_
  - The Euler-Heisenberg / Kerr identification is a **structural / dimensional match** at leading order in $\Delta\phi/\alpha$: the AVE expansion produces the same polynomial-in-field structure that QED produces. It does **not** independently derive the Euler-Heisenberg coefficient from the four AVE axioms vs. the QED loop-integral derivation; both arrive at compatible leading-order forms but the higher-order coefficients are derived from different machinery and have not been compared term-by-term.
  - Inherits the same EFT-validity caveat as `clm-efo113` (Master Equation EFT Validity): the 1D telegrapher form drops field-gradient corrections that may matter near $\Delta\phi \to \alpha$.
  - The "shockwave produces pair-production" claim is **mechanical / heuristic**; it does not predict the Schwinger pair-production rate $\propto \exp(-\pi m_e^2 c^3/(eE\hbar))$ from the shockwave dynamics. The $u_{sat}$ Schwinger threshold is treated as an external QED input elsewhere (`clm-9s9apq`).

> **Leaf references:** [nonlinear-telegrapher](./dynamics/ch3-quantum-signal-dynamics/nonlinear-telegrapher.md).

### Quality
- confidence: 0.65
- depends-on:
  - clm-efo113 — Master Equation EFT Validity [the 1D telegrapher form drops field-gradient corrections near Δφ→α]
  - clm-0ktpcn — Golden Torus α Derivation [α in ε(Δφ) sets the 1/α^2 coefficient of the E^4 term]
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.65, 0.50)]
- rationale: The local algebra is verified: ε(Δφ) = ε_0√(1-(Δφ/α)^2) ≈ ε_0[1-½(Δφ/α)^2], D = ε(Δφ)Δφ gives D ≈ ε_0Δφ - (ε_0/2α^2)Δφ^3, and U = ∫Δφ dD integrates to ½ε_0Δφ^2 - (3ε_0/8α^2)Δφ^4 exactly as stated, with c_eff = c_0[1-(Δφ/α)^2]^{-1/4} diverging as ε→0 (dimensionally consistent v = 1/√(μ_0 ε)). The one clearly-flagged caveat is the Euler-Heisenberg/Kerr identification: the leaf is explicit that this is a structural/dimensional match at leading order — the same polynomial-in-field form — and does NOT derive the EH coefficient term-by-term, and the shockwave→pair-production link is heuristic.
- strengthen-by:
  - Compare the AVE E^4 coefficient (3ε_0/8α^2) to the QED Euler-Heisenberg coefficient term-by-term rather than asserting structural identity at leading order
  - Bound the next-order (gradient / higher-Taylor) correction near Δφ→α where the EFT-validity caveat (clm-efo113) bites
  - Make the "shockwave produces pair-production" claim quantitative — connect the c_eff divergence/steepening to a Schwinger-rate prediction instead of treating u_sat as an external QED input
  - Verify the χ^(3) Kerr coefficient implied by D ∝ (Δφ)^3 against measured vacuum/medium Kerr values for a sanity check
---

## Three-Regime Fluidic Classification (Ch.4 Operating Regimes)
<!-- id: clm-xy252u -->

- _Specific Claims_
  - Vol 1 Ch.4.3 categorises the spatial medium into **three** fluidic operating regimes by control parameter $\Delta\phi/\alpha$: Linear Acoustic ($\ll 1$, $C_{eff} \approx C_0$), Non-Linear Tensor ($\to 1$, $C_{eff} \propto 1/\sqrt{1-x^2}$), Dielectric Rupture ($\ge 1$, $\eta \to 0$).
  - The Dielectric Rupture regime is identified with Black-Hole Event Horizons, Tokamak L-H transitions, and thermal fusion ignition limits via the $V_{yield} \approx 43.65$ kV topological yield bound.
  - Linear Maxwell + scalar Newtonian gravity produce negligible error in Regime I; the full nonlinear stress-energy tensors (GR / nonlinear electrodynamics) are required as $\Delta\phi \to \alpha$ in Regime II.
- _Specific Non-Claims and Caveats_
  - This three-regime fluidic table is **coarser** than the Ch.7 four-regime universal map (`clm-b2anl4`): Ch.7 splits "Non-Linear Tensor" into "Nonlinear" and "Yield" via the spin-2 sector boundary $r_2 = \sqrt{3}/2$; Ch.4's "Dielectric Rupture" corresponds to Ch.7's "Ruptured" ($r \ge 1$). The two classifications are **the same physics expressed at different granularities** — they should not be cited as independent regime maps.
  - The dielectric-rupture-as-event-horizon identification is a **structural / interpretive** claim within the LC-substrate ontology; quantitative event-horizon predictions (e.g., $r_s = 7GM/c^2$ AVE compactness limit) live in `clm-82dxbj` Domain Catalog and the Vol 3 gravity sidecar, not in this leaf.
  - The L-H transition and fusion-ignition identifications are **structural** (same Axiom 4 saturation operator); per-domain numerical agreement with tokamak / ICF experimental thresholds is the responsibility of the per-domain leaves, not of this regime-table summary.

> **Leaf references:** [operating-regimes-table](./dynamics/ch4-continuum-electrodynamics/operating-regimes-table.md).

### Quality
- confidence: 0.70
- depends-on:
  - clm-b2anl4 — Four-Regime Map [same physical regime structure at finer granularity]
  - clm-0ktpcn — Golden Torus α Derivation [supplies the α control-parameter denominator]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.70, 0.63)]
- rationale: As a regime-classification table the leaf is internally consistent and complete: the three regimes follow from the Axiom-4 saturation kernel (C_eff ∝ 1/√(1-(Δφ/α)²) divergence, η→0 rupture) anchored to the V_yield≈43.65 kV bound, and the entry correctly flags that this is the coarse view of the Ch.7 four-regime map and that the BH/L-H/fusion identifications are structural, with per-domain numerics owned elsewhere. It sits in the upper-sound band for a catalog scored on completeness/consistency, held below higher because the cross-domain identifications are interpretive and unquantified in this leaf.
- strengthen-by:
  - Make explicit the reconciliation with the Ch.7 four-regime map (which boundary r₂=√3/2 splits Regime II) so the two are not read as independent
  - Note that the control parameter is Δφ/α here but A/A_c elsewhere; confirm these denominators are the same quantity
  - Cite the per-domain leaves that carry the quantitative BH-horizon / L-H / fusion-ignition agreement
  - Clarify the regime-boundary inequalities (≪1, →1, ≥1) into sharp threshold values where possible
---

## FDTD Yee Lattice Determinism (Continuous Maxwellian Propagation)
<!-- id: clm-nu1ir7 -->

- _Specific Claims_
  - Continuous spatial propagation of LC impedance via a Transverse-Magnetic (TMz) FDTD Yee lattice is sufficient to execute topological geometric defects (e.g., the $0_1$ Unknot) without invoking discrete "virtual photons" as force mediators.
  - In the Yee scheme, $\vec E$ and $\vec H$ tensors are staggered by half a phase step, eliminating division-by-zero in macroscopic curl operations and generating the invariant $c$ limit from the discrete-update structure.
  - The FDTD environment is **deterministic**; ontological probability is reframed as a finite-resolution observation artifact of high-frequency phase-locking dynamics, not a fundamental property.
- _Specific Non-Claims and Caveats_
  - The "no virtual photons needed" claim is **mechanism-level** (continuous Maxwellian update vs. perturbative QED quanta exchange); it does not derive QED scattering cross-sections from the FDTD update at a quantitative level. Operational equivalence with QED at the level of measurable scattering observables is asserted, not demonstrated, in this leaf.
  - The "ontological probability is an illusion" framing is an **interpretive ontological** claim. It does not produce a falsifiable distinction between FDTD determinism and standard QM at any current laboratory scale; falsifiability rests on unrelated AVE predictions (running $\alpha$, GUP cutoff, decoherence-onset $T_{pair}$ — see `clm-zuf7g1`), not on the determinism reframe per se.
  - The Yee lattice is a **standard computational electrodynamics** scheme; the AVE-specific claim is the identification of the physical substrate lattice with the Yee grid, not the Yee scheme itself. Methodological details (numerical stability, Courant condition $c\Delta t \le \Delta x/\sqrt{D}$) are not derived in this leaf.

> **Leaf references:** [fdtd-yee-proof](./operators-and-regimes/ch5-universal-spatial-tension/fdtd-yee-proof.md).

### Quality
- confidence: 0.40
- depends-on:
  - clm-q39qct — Discrete Kirchhoff Network Solver Methodology [supplies the discrete-update engine ontology that the Yee-grid identification specializes]
- solidity: 0.40 (do not build on, rework needed) [= min(0.40, 0.63)]
- rationale: The leaf is short and largely qualitative/interpretive: it asserts that a TMz Yee FDTD lattice can execute topological defects without virtual photons and reframes ontological probability as a resolution artifact, but it documents no reproducible simulation, derives neither the Courant stability condition nor the defect-execution result, and (per the entry's own caveats) the QED-equivalence and determinism claims are asserted, not demonstrated. The Yee half-step staggering and emergence of an invariant c are standard computational-electrodynamics facts correctly stated, which keeps it above the speculative band.
- strengthen-by:
  - Provide an actual reproducible FDTD run executing the 0₁ Unknot defect with an acceptance criterion, not a prose assertion
  - Derive the Courant condition cΔt ≤ Δx/√D and state the stability regime for the claimed invariant-c emergence
  - Replace the "ontological probability is an illusion" prose with a stated, falsifiable distinguishing prediction (or cite the leaf where one exists)
  - Show at least one quantitative QED observable reproduced by the continuous update to support the "no virtual photons needed" mechanism claim
---

## Universal Dimensionless Master Equation
<!-- id: clm-rtgmg5 -->

- $\partial^2\phi/\partial t^2 = c_0^2(1-r^2)^{1/2}\,\nabla^2\phi$
- _Specific Claims_
  - When the equations of motion in any AVE domain are expressed in the dimensionless control parameter $r = A/A_c$, they take a **single universal form**: $\partial_t^2\phi = c_0^2 S(r)\,\nabla^2\phi$ with $S(r) = (1-r^2)^{1/2}$.
  - $\phi$ is the generalized displacement field (voltage, strain, temperature, GW perturbation, etc.); the domain merely specifies the physical meaning of $\phi$, $A$, and $A_c$.
  - This is "a single equation governing all of physics" (the leaf's framing) under the unifying-form interpretation.
- _Specific Non-Claims and Caveats_
  - The universality claim is **structural / dimensional**: domain-specific substitution of $\phi$, $A$, $A_c$ recovers the master equation, but the equation does not by itself predict the $A_c$ values. Each $A_c$ comes from per-domain physics (cataloged in `domain-catalog.md`, scored under `clm-82dxbj`); the dimensionless form is the **wrapper**, not a parameter-free derivation of every domain's threshold.
  - The form $S(r) = \sqrt{1-r^2}$ is the symmetric-saturation kernel; asymmetric (electric-only) saturation produces $Z = Z_0/(1-r^2)^{1/4}$ instead of the symmetric $Z = Z_0$ invariant. The dimensionless master equation as written assumes the **symmetric** sector (per `regime-equation-sets.md`).
  - The "single equation governing all of physics" framing is **rhetorically strong**; it captures the recurring leading-order EFT structure across domains but elides regime-specific corrections (Tier-1 EFT validity caveat from `clm-efo113`; sector-specific $\ell_{\min}$ from `clm-b2anl4`).

> **Leaf references:** [dimensional-analysis](./operators-and-regimes/ch7-regime-map/dimensional-analysis.md).

### Quality
- confidence: 0.50
- depends-on:
  - clm-efo113 — Master Equation EFT Validity [the dimensionless form is the same leading-order EFT recast in r]
  - clm-b2anl4 — Four-Regime Map [sector structure underlying the r-control-parameter classification]
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.50)]
- rationale: The leaf is a one-equation assertion: it states the universal form ∂ₜ²φ = c₀²(1-r²)^{1/2}∇²φ with no in-leaf derivation showing why each domain's equations of motion reduce to it, and the (1-r²)^{1/2} coefficient is a direct restatement of the Axiom-4 saturation kernel rather than a derived result. The entry's caveats correctly mark it as a structural wrapper that does not predict the per-domain A_c and assumes the symmetric sector, so locally it is a plausible unifying claim with a notable not-derived universality step.
- strengthen-by:
  - Show explicitly, for at least two distinct domains, the nondimensionalization that maps their EOM onto the master form (currently asserted)
  - State precisely the symmetric-sector assumption and where the asymmetric Z=Z₀/(1-r²)^{1/4} sector breaks the claimed universality
  - Distinguish what is Axiom-4-restatement from what is genuinely cross-domain content, to avoid overstating "single equation governing all of physics"
  - Bound the dropped field-gradient/regime corrections (Tier-1 EFT validity) as r→1
---

## K4 Rotation Group $T = A_4$
<!-- id: clm-ys0xl1 -->

The action of 3D rotations on the K4 tetrahedral 4-port basis is a faithful representation of the tetrahedral rotation group $T = A_4$ (order 12).

- _Specific Claims_
  - The K4 diamond lattice has a 4-port tetrahedral basis $p_0 = (+1,+1,+1)$, $p_1 = (+1,-1,-1)$, $p_2 = (-1,+1,-1)$, $p_3 = (-1,-1,+1)$; pairwise dot product $-1$, tetrahedral angle $\arccos(-1/3) \approx 109.47°$.
  - The rotation symmetry of this tetrahedron is the tetrahedral group $T$, isomorphic to the alternating group $A_4$, order $|T| = 12$: identity (1) + $C_3$ class (8 rotations $\pm 120°$ about 4 vertex axes) + $C_2$ class (3 rotations $180°$ about 3 edge-midpoint axes).
  - All 12 group elements are enumerated explicitly as permutations of $\{0,1,2,3\}$; they are all even, distinct, and closed under composition — bijective onto the 12 even permutations of $A_4$, so the representation is faithful.
- _Specific Non-Claims and Caveats_
  - The leaf treats the rotation subgroup only; reflections (the full $T_d = S_4$, order 24) are the subject of the separate point-symmetry claim.
  - The faithful-representation result is a group-theory verification of K4's stated symmetry, not an independent derivation of the K4 lattice structure itself (Axiom 1 stipulates the lattice).

> **Leaf references:** [k4-rotation-group](./axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md).

### Quality
- confidence: 0.92
- solidity: 0.92 (ok to build on)
- rationale: Leaf §2–§4 carries the full derivation: all 12 group elements enumerated as explicit permutations (1 identity + 8 C_3 + 3 C_2), each shown even, with a worked C_2 axis check (x-axis 180° maps p0↔p1, p2↔p3) and a closure/bijection-onto-A_4 faithfulness argument; this is exact, standard group theory carried in the leaf. The only non-derived input is identifying the code-stated port basis {p_j} with the tetrahedron, which is a definitional/Axiom-1 stipulation rather than a local gap.
- strengthen-by:
  - Show explicit closure (a composition/Cayley-table sample) rather than asserting "form a closed group under composition"
  - State the homomorphism kernel is trivial explicitly to nail "faithful" beyond the bijection count
  - Cite that the 4 vertex axes give 4×2=8 distinct C_3 elements with the matching permutation for each (table is present; one worked composition would close it)
---

## K4 Full Point Symmetry $T_d = S_4$ and the A↔B Sublattice Swap
<!-- id: clm-7pvh9i -->

The full point symmetry of the K4 lattice including reflections is $T_d = S_4$ (order 24); the 4 mirror planes in $T_d \setminus T$ swap the bipartite A and B sublattices.

- _Specific Claims_
  - Including reflections, the K4 point group is the full tetrahedral group $T_d$, isomorphic to the symmetric group $S_4$, order 24.
  - Under the rotation subgroup $T = A_4$ alone, the bipartite A and B sublattices are each preserved (rotations about a bipartite-cell vertex respect the bipartite structure).
  - The 4 mirror planes — the elements of $T_d \setminus T$ — exchange A ↔ B by swapping vertex pairs; an A↔B swap therefore requires the reflection sector (full $T_d$), not pure rotations.
- _Specific Non-Claims and Caveats_
  - The leaf notes the A↔B swap is "needed for the bipartite-spinor argument leading to spin-½" but states that obtaining the swap requires either including reflections or "some other physical mechanism" — it does not assert that $T_d$ reflections are themselves the realized spin-½ mechanism (that role is the Finkelstein–Misner double-cover claim).
  - Cosserat constitutive relations are stated to involve A↔B-swapping reflections; the leaf records this as a structural feature, not a step-by-step constitutive derivation.

> **Leaf references:** [k4-rotation-group](./axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md).

### Quality
- confidence: 0.82
- depends-on:
  - clm-ys0xl1 — K4 Rotation Group T=A_4 [the rotation subgroup T_d\T is defined relative to]
- solidity: 0.82 (ok to build on, see caveats) [= min(0.82, 0.92)]
- rationale: T_d=S_4 (order 24) and "rotations preserve the bipartite A/B sublattices" are standard and correct; the load-bearing A↔B-swap claim is asserted at the level of "the 4 mirror planes exchange A↔B by swapping vertex pairs" without the per-element worked verification that §3 supplies for the rotation classes. The leaf is honest that obtaining the swap "requires reflections or some other physical mechanism," so the claim is sound but carries one un-worked identification step.
- strengthen-by:
  - Enumerate the 4 mirror planes explicitly (as reflection matrices) and show each swaps A↔B, paralleling §3's rotation verification
  - Make precise what "swapping vertex pairs" means at the bipartite-cell level (which A-site maps to which B-site)
  - Separate the pure-group fact (T_d=S_4) from the lattice-action claim (mirrors swap sublattices) so the confidence of each is visible
---

## K4 Double Cover $2T \subset SU(2)$ — Substrate-Native Spin-½
<!-- id: clm-rkisb8 -->

The double cover of $T = A_4$ is the binary tetrahedral group $2T \subset SU(2)$ (order 24), in which a $2\pi$ rotation maps to $-I$ and only $4\pi$ to $+I$ — the K4-native source of spin-½ via the Finkelstein–Misner mechanism.

- _Specific Claims_
  - The double cover of $A_4$ is the binary tetrahedral group $2T$, order 24, a discrete subgroup of $SU(2)$, via the exact sequence $1 \to \mathbb{Z}_2 \to 2T \to A_4 \to 1$.
  - Each $A_4$ element has two $2T$ preimages differing by the central $-I \in SU(2)$; $-I$ is the lift of a $2\pi$ SO(3) rotation, so $2\pi \to -I$ and $4\pi \to +I$ — the spin-½ characteristic.
  - For spin-½ to be derived from K4 (not imported from QM), physical fields on the lattice must transform under $2T$ rather than $T$; this is supplied by the Finkelstein–Misner mechanism on the extended $0_1$ unknot defect embedded in the SO(3) manifold, via the chain $K_4 \to A_4 \to 2T \subset SU(2)$.
- _Specific Non-Claims and Caveats_
  - The leaf states the requirement that fields transform under $2T$ and attributes the realization to the Finkelstein–Misner mechanism; the full spin-½ derivation chain is deferred to the cited spin-half-paradox leaf and Vol 1 Ch 8 — this entry does not re-derive it.
  - The electron's real-space body is the $0_1$ unknot; the double-cover argument is a property of the defect's embedding in SO(3), not a claim about a real-space trefoil.

> **Leaf references:** [k4-rotation-group](./axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md).

### Quality
- confidence: 0.72
- depends-on:
  - clm-ys0xl1 — K4 Rotation Group T=A_4 [the group whose double cover is taken]
- solidity: 0.72 (ok to build on, see caveats) [= min(0.72, 0.92)]
- rationale: The pure group theory is correct and standard: 1→Z_2→2T→A_4→1, |2T|=24, 2π→−I and 4π→+I are exact SU(2) facts. The physics step that earns the title — fields actually transforming under 2T (substrate-native spin-½) via the Finkelstein–Misner mechanism — is explicitly deferred to the spin-half-paradox leaf and Vol 1 Ch 8, so locally this entry establishes the double-cover structure but only asserts (does not derive) the spin-½ realization. **REPRESENTABILITY established (2026-06-19, #299):** the spin-doublecover gate (`research/2026-06-19_spin-doublecover-gate_result.md`, `CosseratField3D.probe_spin_doublecover_holonomy`) showed the AVE substrate ADMITS the 2T⊂SU(2) double-cover action on the extended unknot's frame as a distinct, lattice-level frame transport — the SU(2)-lift holonomy returns −I@2π and +I@4π and DIFFERS from the trivial-vector (SO(3)/T=A4) baseline (which returns to +I@2π to machine precision), stable across R=4,6,8 cells. This is REPRESENTABILITY (the 2T action is representable and observable), Class-D — it is **NOT dynamics-selection**: the gate does not show the seeded field DYNAMICALLY selects 2T over T (kinematic only — no energy minimization, no time-stepping; that selection is the FM-on-K4 *physical* argument, not re-derived here). So the claim is upgraded from "asserts (does not derive)" to "the necessary lattice-level representability condition is now demonstrated; the dynamical selection remains the FM argument, not derived."
- strengthen-by:
  - Pull the minimal Finkelstein–Misner argument into this leaf, or downscope the title to "double-cover structure" with spin-½ as a forward pointer
  - Justify why physical K4 fields must lift to 2T rather than represent A_4 directly (the crux of "native, not imported")
  - Give the two 2T preimages of at least one A_4 element explicitly to ground the Z_2 central extension
  - **[partly addressed]** The lattice-level REPRESENTABILITY of the 2T action is now demonstrated (#299, the spin-doublecover gate: −I@2π / +I@4π, distinct from the SO(3) baseline). What remains is the DYNAMICAL selection — show the seeded field settles into the 2T action rather than merely admits it (the gate is kinematic; energy minimization / time-stepping is out of scope there)
---

## Cosserat Mass-Gap Formula $m^2 = 4 G_c / I_\omega$
<!-- id: clm-jz0xaw -->

The micropolar rotational sector of the Cosserat substrate carries a mass gap $m^2 = 4 G_c / I_\omega$; the factor 4 arises from the antisymmetric-strain energy density $W_{\text{micropolar}} = 2|\omega|^2$ (in units of $G_c$).

- _Specific Claims_
  - The micropolar coupling term $W_{\text{micropolar}} = G_c \sum_{ij}(\varepsilon_{\text{antisym},ij})^2$, with $\varepsilon_{\text{antisym},ij} = \tfrac{1}{2}(\partial_i u_j - \partial_j u_i) - \epsilon_{ijk}\omega_k$, evaluates for uniform $\omega_z$ ($u=0$) to $2 G_c |\omega_z|^2$ — the $xy$ and $yx$ antisymmetric components contribute equally.
  - The resulting mass term in the equation of motion gives the mass gap $m^2 = 4 G_c / I_\omega$; the factor 4 = 2 (antisymmetric-pair doubling in $\sum_{ij}$) × 2 (Lagrangian-to-EOM conversion).
- _Specific Non-Claims and Caveats_
  - The factor-4 result is derived for the uniform-$\omega_z$ configuration; the leaf does not claim the same prefactor for arbitrary non-uniform $\omega$ configurations beyond what the dispersion relation captures.
  - The gap is a property of the Cosserat micropolar Lagrangian; converting it to the electron mass requires the separate electron-calibration claim.

> **Leaf references:** [cosserat-mass-gap](./axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md).

### Quality
- confidence: 0.82
- solidity: 0.82 (ok to build on, see caveats)
- rationale: Verified locally — for uniform ω_z (u=0) the antisymmetric strain gives ε_xy=−ω_z, ε_yx=+ω_z so W_micropolar = G_c[ω_z²+ω_z²] = 2G_c|ω_z|², and the EOM I_ω ω̈ = −∂W/∂ω = −4G_c ω yields m²=4G_c/I_ω, with the factor 4 transparently 2 (antisymmetric-pair sum) × 2 (potential→force derivative). The one caveat keeping it below 0.85 is the explicitly-flagged restriction to the uniform-ω_z configuration (the prefactor is not claimed for arbitrary non-uniform ω beyond the dispersion relation).
- strengthen-by:
  - Show the prefactor 4 survives (or how it changes) for non-uniform ω configurations, not just uniform ω_z.
  - State the convention for the micropolar coupling normalization (factor placement in W) so the "units of G_c" framing is unambiguous.
---

## Gapped Dispersion of the Cosserat Rotational Sector
<!-- id: clm-4mmwb6 -->

The Cosserat rotational sector obeys a gapped dispersion relation $\omega^2 = c^2 k^2 + m^2$ at long wavelengths, following from the micropolar Lagrangian's Euler-Lagrange equations.

- _Specific Claims_
  - The Cosserat micropolar Lagrangian $L = \tfrac{1}{2}\rho|\dot u|^2 + \tfrac{1}{2}I_\omega|\dot\omega|^2 - W(u,\omega)$ yields Euler-Lagrange equations $\rho\ddot u = -\partial W/\partial u$ and $I_\omega\ddot\omega = -\partial W/\partial\omega$.
  - The rotational sector's long-wavelength dispersion combines a curvature term and a mass term: $\omega^2 = c^2 k^2 + m^2$ — a massive (gapped) mode, in contrast to the gapless scalar sector.
  - This validates Axiom 3 (Minimum Reflection Principle): the Lagrangian produces the correct Euler-Lagrange equations, confirmed by Hamiltonian conservation in the velocity-Verlet integration.
- _Specific Non-Claims and Caveats_
  - $W(u,\omega)$ is a general Cosserat energy density (Cauchy, micropolar, curvature, Op10, reflection, Hopf terms); the dispersion statement is for the rotational sector with the mass and curvature terms active.
  - The companion gapped-wave test (T1b) shows a 34% group-velocity error attributed to stiffer gapped-band lattice dispersion; the dispersion-relation claim is the long-wavelength form, not a finite-$k$ precision claim.

> **Leaf references:** [cosserat-mass-gap](./axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md).

### Quality
- confidence: 0.80
- depends-on:
  - clm-jz0xaw — Cosserat Mass-Gap Formula m²=4G_c/I_ω [supplies the mass term m² entering the gapped dispersion]
- solidity: 0.80 (ok to build on, see caveats) [= min(0.80, 0.82)]
- rationale: The Lagrangian L = ½ρ|u̇|²+½I_ω|ω̇|²−W gives standard Euler-Lagrange equations ρü=−∂W/∂u, I_ω ω̈=−∂W/∂ω, and the rotational sector's long-wavelength gapped form ω²=c²k²+m² follows directly from combining the curvature (gradient) term with the mass term — a textbook-level local derivation. Held below 0.85 by the flagged finite-k caveat (the T1b companion shows 34% group-velocity error at finite k, so the claim is rigorously the long-wavelength form only) and the "validates Axiom 3" line, which is a consistency observation rather than part of the dispersion derivation.
- strengthen-by:
  - State the long-wavelength expansion explicitly (the k→0 limit of the lattice dispersion) so the c²k²+m² form is shown as leading order with a bounded next-order correction.
  - Separate the Axiom-3 validation remark from the dispersion derivation, since Hamiltonian conservation tests the integrator, not the gapped form.
---

## Cosserat Mass-Gap Empirical T2 Validation
<!-- id: clm-dhvhwi -->

The uniform-$\omega$ mass-gap oscillation test reproduces the predicted oscillation period to 0.35% (measured 3.1307 vs theory $\pi$), with bounded energy drift ($9.0 \times 10^{-3}$ over 5 periods).

- _Specific Claims_
  - The T2 test seeds a uniform $\omega_z = A_0 = 0.05$ with zero velocity and $\nabla\omega = 0$, isolating the mass term (curvature contributes nothing); the predicted oscillation has $\omega_m = \sqrt{4 G_c/I_\omega} = 2$, period $T = 2\pi/\omega_m = \pi \approx 3.1416$.
  - Measured: $\omega_{\text{mass}} = 2.0070$ and period $T = 3.1307$, both 0.35% from theory; energy drift $|\Delta H/H|_{\max} = 9.0 \times 10^{-3}$ (0.9%) over 5 periods with no secular trend.
  - The match confirms the velocity-Verlet integrator conserves energy to $O(dt^2)$ and that the mass gap is exactly $m^2 = 4 G_c/I_\omega$.
- _Specific Non-Claims and Caveats_
  - The test runs with parameters $\rho = I_\omega = G_c = 1$, $N = 32$ — it validates the mass-gap structure of the Cosserat Lagrangian, not the electron-specific calibration.
  - Companion tests T1a/T1b carry larger errors (14% gapless velocity, 34% gapped group velocity) attributed to finite-$k$ lattice dispersion; only T2 (mass term isolated) achieves the 0.35% figure.
  - Per the leaf's Phase-I scope: Axiom 1 (K4 substrate) and Axiom 4 (saturation) are not exercised by this test; Cosserat-alone is a development step, not an Axiom-1-compliant physics substitute.

> **Leaf references:** [cosserat-mass-gap](./axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md).

### Quality
- confidence: 0.80
- depends-on:
  - clm-jz0xaw — Cosserat Mass-Gap Formula m²=4G_c/I_ω [supplies the predicted ω_m=√(4G_c/I_ω)=2, T=π that the test measures against]
- solidity: 0.80 (ok to build on, see caveats) [= min(0.80, 0.82)]
- rationale: Verified — with ρ=I_ω=G_c=1 the predicted ω_m=√4=2 and T=2π/2=π≈3.1416 against measured 3.1307 is 0.35%, and the uniform-ω/∇ω=0 design genuinely isolates the mass term (kills curvature), so this is a clean numerical consistency check that the velocity-Verlet integrator reproduces the analytic gap (energy drift 0.9%, no secular trend). It is a consistency check of the gap formula, not a derived prediction or electron calibration (correctly disclaimed); local rigor is high but caps just below 0.85 because the "confirms the gap is EXACTLY 4G_c/I_ω" reading is a 0.35%-level numerical match, not an exactness proof.
- strengthen-by:
  - Report a dt-convergence study showing the 0.35% residual scales as O(dt²) toward zero, separating integrator error from any structural offset.
  - Add a non-trivial-parameter run (I_ω≠G_c) confirming ω_m tracks √(4G_c/I_ω) across values, not just at the symmetric point.
---

## Cosserat Rotational Mode as the Structural Electron-Mass Mechanism
<!-- id: clm-g0mkne -->

The Cosserat rotational sector's massive mode supplies the electron's mass content, while the K4 scalar sector remains separately massless (the photon).

- _Specific Claims_
  - The rotational massive mode at $m^2 = 4 G_c/I_\omega$ inherits the substrate's mass content; the electron's specific calibration uses the (2,3) Clifford-torus phase-space winding shell with quality factor $Q = 1/\alpha = 137.036$ at the Vol 1 Ch 8 Golden Torus geometry $R = \varphi/2$, $r = (\varphi-1)/2$.
  - The electron rest energy $m_e c^2 = \hbar\omega_C = T_{EM}\cdot\ell_{\text{node}}$ inherits from the mass-gap formula at substrate parameters $\rho, I_\omega, G_c$ calibrated to $\ell_{\text{node}} = \hbar/(m_e c)$.
  - The Cosserat $\rho, I_\omega$ set the rotational-sector mass scale; the K4 scalar sector ($A_1$, longitudinal/translational $u$) stays massless — the photon — while $T_2$ (transverse/microrotational $\omega$) carries the mass-gap content.
- _Specific Non-Claims and Caveats_
  - The (2,3) trefoil is the electron's phase-space (Clifford-torus) winding label; the electron's real-space body is the $0_1$ unknot. The leaf explicitly flags this — it is not a real-space trefoil.
  - The electron-specific calibration is Phase-II + III work coupling K4 ⊗ Cosserat at saturation; the Phase-I T2 test validates the mass-gap structure, not the calibration.
  - The massless-scalar / massive-rotational split is asserted as consistent with the photon = $T_2$-only identification (cross-referenced photon-identification leaf); this entry does not independently re-derive the photon identification.

> **Leaf references:** [cosserat-mass-gap](./axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md).

### Quality
- confidence: 0.45
- depends-on:
  - clm-jz0xaw — Cosserat Mass-Gap Formula m²=4G_c/I_ω [supplies the rotational massive mode that carries the electron's mass content]
  - clm-unk0bd — Electron Body Topology = 0_1 Unknot with (2,3) Phase-Space Winding [supplies the (2,3) Clifford-torus winding the electron calibration is attached to]
  - clm-0ktpcn — Golden Torus α Derivation [supplies Q=1/α and the R=φ/2, r=(φ−1)/2 geometry used in the calibration]
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.45, 0.63)]
- rationale: The structural split — rotational T₂/ω sector carries the mass gap while the A₁/scalar/u sector stays massless (photon) — is a coherent assignment, but the actual electron-specific step (mass content "inherits" via Q=1/α at the Golden Torus geometry, with m_e c² = ℏω_C = T_EM·ℓ_node) is asserted as inheritance, not derived: §4 strings together the gap formula, the α Q-factor, and the calibration ℓ_node = ℏ/(m_e c) without a derivation closing them, and §5 explicitly defers the calibration to Phase-II/III coupling work not present here. Locally this is a structural-assignment-plus-asserted-calibration claim, landing in the significant-local-gap band.
- strengthen-by:
  - Derive the Q=1/α quality-factor calibration of the rotational sector rather than importing it from Ch 8.
  - Show the massless-A₁ / massive-T₂ split from the K4 ⊗ Cosserat coupling explicitly rather than cross-referencing the photon-identification leaf.
  - Produce the Phase-II/III coupled calculation that converts the generic gap m²=4G_c/I_ω into the electron-specific m_e, closing the inheritance step.
---

## Cubic K4 Anisotropy at Saturation Collapse
<!-- id: clm-u1o2lo -->

At saturation collapse ($A^2 \to 1$) the K4 substrate's bipolar attractor is cubic (6-vertex / 8-face / 12-edge), the empirical signature of the $T = A_4$ tetrahedral rotation group; a perfectly spherical collapse would falsify the K4 substrate.

- _Specific Claims_
  - When seeded near saturation amplitude and evolved, the K4-Cosserat coupled engine produces a stable attractor with cubic — not spherical, not isotropic — symmetry; the saturated $|V|$ envelope develops 6 face-centered protrusions aligned with the lattice Cartesian axes.
  - The cubic structure is the projection of the $T = A_4$ / $T_d$ symmetry: the 3 face-midpoint $C_2$ axes align with $\pm\hat x, \pm\hat y, \pm\hat z$; the same anisotropy appears in the linear regime as the cardinal-axis $v = c\sqrt{2}$ vs diagonal-axis $v = c$ photon-propagation split.
  - The signature is empirically observed (path-α saturation-collapse 5-sampler-view bipolar +x/−x $R/r$ split; v14 cubic-emergence visualizations) and group-theoretically expected.
  - Falsifiable: any model claiming to be K4-Cosserat that collapses to perfectly spherical symmetry at saturation is inconsistent with its claimed underlying symmetry.
- _Specific Non-Claims and Caveats_
  - The cubic anisotropy is read off simulation outputs (saturation-collapse attractor + propagation-baseline kinematics); it is the empirical signature of the K4 symmetry, not an independent derivation of the lattice.
  - The per-direction observables ($R/r$ across sampler views) require bipolar (per-cluster +x/−x) adjudication to capture both lobes; quoted medians are per-cluster.
  - The leaf flags engine-design implications (PML placement, mode-eigsolve assuming spherical symmetry) as methodological cautions, not physical claims.

> **Leaf references:** [cubic-k4-empirical-anisotropy](./axioms-and-lattice/ch1-fundamental-axioms/cubic-k4-empirical-anisotropy.md).

### Quality
- confidence: 0.45
- depends-on:
  - clm-ys0xl1 — K4 Rotation Group T=A_4 [the T=A_4/T_d symmetry the cubic signature is attributed to]
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.45, 0.92)]
- rationale: The cubic-anisotropy result is an empirical observation read off simulation outputs (path-α bipolar +x/−x R/r medians, v14 visualizations) plus a qualitative group-theoretic expectation (3 face-midpoint C_2 axes align with ±x/±y/±z); the leaf is explicit it is a signature, not a derivation. The link from T_d to specifically cubic (6/8/12) envelope geometry is asserted qualitatively, and the per-direction R/r numbers are descriptive medians, so quantitative predictive content is thin where it is implied.
- strengthen-by:
  - Derive the predicted cubic harmonic content (e.g. which cubic-symmetric multipoles dominate) so the signature becomes quantitative, not just "not spherical"
  - Quantify the +x/−x bipolar split against a predicted ratio rather than reporting medians
  - Clarify why T_d (tetrahedral) projects to a cubic 6/8/12 envelope rather than a tetrahedral one in the lattice frame
---

## $|T| = 12$ Universality — Four Independent Routes Converge
<!-- id: clm-15nwqy -->

Four independent routes (K4 coordination path-count, Cosserat dimensional, magic-angle orbit multiplicity, the axiom-level ratio $\xi_{K2}/\xi_{K1}$) all converge on 12, indicating $\chi_K = 12$ is forced by K4 tetrahedral symmetry rather than fit.

- _Specific Claims_
  - Route 1 (baseline K4 coordination): 4 nearest-neighbor B-nodes per A-node × 3 other-A sublattices reachable via shared-B-node propagation = 12 secondary paths per node.
  - Route 2 (Cosserat dimensional): $(\ell_c/d)^2 \times 2 = 12$, with $\ell_c \approx \sqrt{6}\,\ell_{\text{node}}$ the Cosserat characteristic length and the factor 2 the bilateral chiral symmetry.
  - Route 3 (magic-angle unity): $f_{\text{Cosserat}}(u_0^*) = 1$ at the substrate saturation boundary — the orbit-count multiplicity of $T$ acting on the K4 unit cell.
  - Route 4 (axiom-level constitutive ratio): $\xi_{K2}/\xi_{K1} = 12$, where $\mu + \kappa = \xi_{K1}T_{EM}$ and $\beta + \gamma = \xi_{K2}T_{EM}\ell_{\text{node}}^2$; the ratio is independent of $T_{EM}$ and K4-symmetry-forced.
  - The convergence replaces "$\chi_K = 12$ as a calibration fit" with "$\chi_K = |T|$, the tetrahedral rotation group order."
- _Specific Non-Claims and Caveats_
  - Status is **structural-hypothesis**, not theorem. The four-route convergence is verified, but the rigorous Session 19+ derivation of $\xi_{K1}, \xi_{K2}$ individually from K4 unit-cell Cosserat-Lagrangian integration is pending (multi-week analytical work). Route 4 is not yet rigorously closed; only if that derivation explicitly recovers $\xi_{K2}/\xi_{K1} = 12$ does the convergence become a four-route theorem.
  - Three of the four routes (1, 3, 4) are derivable from K4 geometry alone; route 2 brings in the Cosserat constitutive structure — the four are windows into the same Axiom 1 symmetry, so the convergence is expected, with the independent derivations providing the cross-check.

> **Leaf references:** [tetrahedral-t-universality](./axioms-and-lattice/ch1-fundamental-axioms/tetrahedral-t-universality.md).

### Quality
- confidence: 0.55
- depends-on:
  - clm-ys0xl1 — K4 Rotation Group T=A_4 [|T|=12 is the group order all four routes target]
  - clm-gx1mpl — A-029 Secondary Scale [route 1 path-count scaffold: 4 B-neighbors × 3 other-A sublattices]
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.55, 0.50)]
- rationale: The leaf itself flags status as structural-hypothesis, not theorem: route 4 (ξ_K2/ξ_K1=12) is explicitly not rigorously closed pending multi-week Cosserat-Lagrangian integration, and route 2's (ℓ_c/d)²×2 = (√6)²×2 = 12 is a suggestive dimensional coincidence rather than a derivation. Routes 1 and 3 are clean geometric/orbit counts, so the convergence is real but rests partly on un-closed and numerological legs — a notable acknowledged gap.
- strengthen-by:
  - Close route 4 by deriving ξ_K1, ξ_K2 individually from K4 unit-cell Cosserat integration and showing the ratio is 12 (the leaf's own stated bar for theorem status)
  - Justify route 2's factor structure — why ℓ_c≈√6 ℓ_node and why ×2 — rather than presenting it as a matched product
  - Address that routes 1/3/4 are admittedly windows into the same Axiom-1 symmetry, so quantify how independent the cross-check truly is
---

## A-029 Secondary Scale — Geometrically Forced Shared-B-Node Distance
<!-- id: clm-gx1mpl -->

The K4 shared-B-node next-nearest-neighbor distance $r_{\text{secondary}} = \sqrt[3]{\mathcal{R}_{\text{OB}}}\cdot\ell_{\text{node}} \approx 1.187\,\ell_{\text{node}}$ is geometrically forced by K4 topology plus packing fractions, not a free parameter; the magic-angle $u_0^*$ sits exactly here.

- _Specific Claims_
  - In the bipartite K4 lattice, the next-nearest-neighbor distance between two A-nodes is set by the shortest path through a shared B-node: $r_{\text{secondary}} = \sqrt[3]{\mathcal{R}_{\text{OB}}}\cdot\ell_{\text{node}}$, with $\mathcal{R}_{\text{OB}} = p_{\text{Delaunay}}/p_c = 0.3068/0.1834 \approx 1.673$, giving $r_{\text{secondary}} \approx 1.187\,\ell_{\text{node}}$.
  - The number 1.187 is forced by three inputs — K4 graph topology (4-neighbor connectivity, Axiom 1), the vacuum packing fraction $p_c = 8\pi\alpha \approx 0.1834$ (from the $K=2G$ trace-reversal identity, Axiom 4 + EMT), and the standard amorphous-network Delaunay packing $p_{\text{Delaunay}} \approx 0.3068$ — so it is not a calibration choice.
  - The over-bracing parameter $u_0$ at the magic value $u_0^* \approx 0.187$ (where $K(u_0^*) = 2G(u_0^*)$) places the bond midpoint at the saturation point $A = 1$ — the substrate-scale instance of A-034. The shared-B-node propagator is the mechanism by which the substrate projects a coherent gravity response across distances $> \ell_{\text{node}}$.
- _Specific Non-Claims and Caveats_
  - The load-bearing claim is specifically that 1.187 is not free; the geometric derivation from K4 graph + EMT packing fraction is presented as straightforward, conditional on the cited $p_c$ and $p_{\text{Delaunay}}$ values (the $p_c = 8\pi\alpha$ identity carries its own consistency-vs-derivation status elsewhere).
  - A-029 is the geometric scaffold for route 1 of the $|T| = 12$ universality framework; the entry asserts the secondary-scale distance, not the full four-route convergence.

> **Leaf references:** [secondary-scale-shared-b-node](./axioms-and-lattice/ch2-macroscopic-moduli/secondary-scale-shared-b-node.md).

### Quality
- confidence: 0.5
- depends-on:
  - clm-ys0xl1 — K4 Rotation Group T=A_4 [K4 4-neighbor graph topology underlying the shared-B-node path]
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.92)]
- rationale: The arithmetic checks (R_OB=0.3068/0.1834≈1.673, cbrt(1.673)≈1.187, p_c=8πα≈0.1834 all verified), but the load-bearing form r_secondary=cbrt(R_OB)·ℓ_node is asserted, not derived — the leaf does not explain why a packing-fraction ratio enters as a cube root to set a next-nearest-neighbor length. The "1.187 is not free" claim is sound only conditional on inputs (p_c=8πα carries its own status elsewhere) and on this un-justified cube-root structural step.
- strengthen-by:
  - Derive the cube-root relation (volume packing-fraction → linear-distance ratio scales as the 1/3 power) explicitly rather than stating it
  - Separate the geometric NNN-distance claim from the magic-angle u_0*≈0.187 placement, which the leaf conflates with the 1.187 distance
  - Make the dependence on the p_c=8πα identity explicit and link its (consistency-vs-derivation) status so the conditional nature is visible
---

## K4 4-Port Irrep Decomposition — $A_1 \oplus T_2$ under $T_d$
<!-- id: clm-j550uh -->

Under the tetrahedral group $T_d$, the K4 4-port amplitude space decomposes as $V_{\text{4-port}} = A_1 \text{ (1D)} \oplus T_2 \text{ (3D)}$; the K4-TLM scattering matrix $S = (1/2)\mathbf{1} - I$ has eigenvalues $\{+1, -1, -1, -1\}$.

- _Specific Claims_
  - The K4 4-port space decomposes under $T_d$ as $A_1$ (totally symmetric, 1D, basis $(1,1,1,1)/2$, scalar/longitudinal) plus $T_2$ (3D triplet, traceless subspace $\sum_i v_i = 0$, vector-like/transverse).
  - The scattering matrix $S_{ij} = (1/2) - \delta_{ij}$ (for $z_{\text{local}} = 1$) has eigenvalue $+1$ on $A_1$ and $-1$ (triply degenerate) on $T_2$; the eigenvalue sum is $4$.
  - The empirical port-correlation eigenvalues (`phasor_discovery.py`, $N=64$, steps 100/200/300) are $\{1.65, 1.22, 1.13, 0.00\}$ — the smallest eigenvalue is exactly zero and stable, confirming the soliton's port-space lives in the 3D $T_2$ subspace.
  - $A_1$ maps to the Cosserat translational sector $u$; $T_2$ maps to the microrotational sector $\omega$. $A_1$ propagates at $c\sqrt{2}$ (bulk modulus), $T_2$ at $c$ (shear modulus).
- _Specific Non-Claims and Caveats_
  - Does NOT claim a new group-theory result — $A_1 \oplus T_2$ is the standard $T_d$ reduction of a 4-element permutation-like representation; the claim is its application to the K4 port space.
  - The empirical $\lambda_4 = 0$ is measured under one specific seeded $(2,3)$ Golden-Torus ansatz at amplitude $0.5$; it is the observed steady state of that run, not an analytic proof that $A_1$ must vanish for every initial condition.
  - The bare scattering matrix is unitary ($A_1$ would propagate forever, $T_2$ reflect forever); the $A_1$-to-zero dissipation is an Op3 effect (separate claim `clm-9kd2t3`), not a property of $S$ alone.

> **Leaf references:** [k4-port-irrep-decomposition](./operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md).

### Quality
- confidence: 0.85
- depends-on:
  - clm-ys0xl1 — K4 Rotation Group T=A_4 [T_d is the point group whose irreps decompose the port space]
- solidity: 0.85 (ok to build on) [= min(0.85, 0.92)]
- rationale: Leaf §2 works the eigenvalue computation exactly — S=(1/2)𝟙−I gives +1 on (1,1,1,1)/2 (since 𝟙·v=4v) and −1 on the traceless subspace (𝟙·v=0), trace=4 — and §1's A_1⊕T_2 is the standard T_d reduction (the leaf correctly disclaims novelty). The empirical λ_4=0 (stable across steps 100/200/300) supports the T_2-only steady state, with the honest caveat that it is one seeded (2,3) ansatz, not a proof A_1 must vanish for all ICs.
- strengthen-by:
  - Show A_1 and T_2 are genuinely T_d-irreducible on this basis (character/projection-operator argument), not just S-eigenspaces
  - Test λ_4→0 under a second, non-(2,3) initial condition to separate "T_2 subspace" from "this run's steady state"
  - State the eigenvector basis of the T_2 triplet explicitly to confirm the traceless-subspace identification
---

## Op3 Asymmetric Dissipation Realizes the Gauss's-Law No-Longitudinal-EM Constraint
<!-- id: clm-9kd2t3 -->

The bond-level Op3 reflection dissipates the $A_1$ sector to zero while the $T_2$ triplet settles quasi-stable — realizing, via $T_d$ symmetry alone, the Gauss's-law constraint that longitudinal EM is forbidden in vacuum.

- _Specific Claims_
  - The bond-level Op3 reflection adds an impedance mismatch $Z_{\text{eff}} = Z_0/\sqrt{S_{\text{sat}}}$ ($S_{\text{sat}}$ the Axiom-4 saturation factor) at each bond, breaking the bare-scattering unitarity.
  - The dissipation is asymmetric: $A_1$ (common-mode, no spatial gradient in port space) loses energy monotonically to zero via destructive interference; $T_2$ (spatially structured) dissipates more slowly and settles into a quasi-stable standing-wave configuration.
  - This asymmetry is physically correct for EM waves on a Maxwell-substrate: longitudinal components ($\nabla \cdot \mathbf{E} \neq 0$) are forbidden in vacuum by Gauss's law, so any $A_1$-type excitation must dissipate. The K4 scattering enforces this automatically through $T_d$ symmetry, with no additional postulate.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a quantitative dissipation-rate law for either sector; the claim is the qualitative monotone-to-zero ($A_1$) vs quasi-stable ($T_2$) split, supported by the empirical $\lambda_4 = 0$ observation.
  - Does NOT derive Gauss's law from the four axioms; it observes that the $T_d$-symmetric K4 scattering reproduces the Gauss's-law constraint's consequence (longitudinal sector dissipates), an internal-consistency match rather than an independent derivation of Maxwell's equations.
  - "Realizes the constraint automatically" is a mechanism claim about the K4-TLM engine's behavior; it does not assert operational equivalence with QED at the level of measurable cross-sections.

> **Leaf references:** [k4-port-irrep-decomposition](./operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md).

### Quality
- confidence: 0.42
- depends-on:
  - clm-j550uh — K4 4-Port Irrep Decomposition [supplies A_1/T_2 sectors and the bare S-matrix this dissipation acts on]
- solidity: 0.42 (do not build on, rework needed) [= min(0.42, 0.85)]
- rationale: The mechanism is qualitative only — A_1 (common-mode, no port-space gradient) "loses energy monotonically to zero via destructive interference" while T_2 "settles quasi-stable" — with the leaf explicitly disclaiming any quantitative dissipation-rate law and explicitly framing the Gauss's-law correspondence as an internal-consistency match, not a derivation of Maxwell. Support is the single empirical λ_4=0 observation; the "destructive interference forces A_1→0" step is asserted rather than shown from the Op3 impedance mismatch Z_eff=Z_0/√S_sat.
- strengthen-by:
  - Derive (even to leading order) that the Op3 mismatch drives the A_1 eigen-amplitude monotonically to zero, vs T_2 quasi-stable, instead of asserting it
  - Show the dissipation asymmetry under more than one initial condition to separate mechanism from the single (2,3) run
  - State plainly this is a consistency check (reproduces a known Gauss's-law consequence) and not novel content, matching the leaf's own caveat
---

## Photon Identification — the $T_2$-Only Cosserat Microrotation (Four Tightly-Coupled Properties)
<!-- id: clm-3npynp -->

The AVE-native photon is the K4-TLM's stable $T_2$-only bound state: under $T_d$ the 4-port space is $A_1 \oplus T_2$, the $A_1$ longitudinal sector dissipates via Gauss's law, and the surviving $T_2$ transverse triplet — a Cosserat microrotation with $u=0$, $\omega\neq0$ — is the photon.

- _Specific Claims_
  - The photon is the stable $T_2$-only configuration with **four tightly-coupled properties** (equivalent statements; any one implies the others): (1) purely transverse, (2) microrotation sector only ($u=0$, $\omega\neq0$), (3) sub-saturation ($\Delta\phi \ll \alpha$, lattice stays linear, no Axiom 4 kernel engagement), (4) impedance-matched at $Z_0$ ($Z_{\text{local}} = Z_0 \approx 376.7$ Ω perfectly matched everywhere; $\Gamma = 0$ at every bond; the wave-engineer's restatement of property 3).
  - The empirical port-correlation steady state ($\lambda_4 = 0$ exactly, $\lambda_{1\ldots3} = 1.65, 1.22, 1.13$) satisfies all AVE-photon properties simultaneously: zero longitudinal amplitude, pure microrotation content, sub-yield amplitude.
  - The identification is consistent with the Vol 3 Ch 2 and Vol 4 Ch 1 manuscript characterizations of the photon as a purely transverse Cosserat shear wave that does not geometrically saturate the lattice.
- _Specific Non-Claims and Caveats_
  - The $A_1 \oplus T_2$ group-theoretic decomposition is NOT this entry's claim — it is owned by `clm-j550uh` (K4 4-Port Irrep Decomposition); this leaf cites it as a cross-reference and applies it to identify the photon.
  - Per the leaf's Doc 107 correction: doc 105's dual-sector helical-photon framing ($u\neq0$ AND $\omega\neq0$) is superseded as empirically wrong; the canonical photon is single-sector. The engine's observed "$u$ driven by $\omega$" coupling is a sub-saturation Op14 effect, not photon content.
  - Property 4 (impedance match at $Z_0$) is an equivalent restatement of property 3 (sub-saturation), not an independent fifth property — added as the fourth canonical property to make the wave-engineer's framing explicit per the canonical cross-corpus §7 translation guide added 2026-05-17.
  - The identification rests on one seeded $(2,3)$ Golden-Torus ansatz run at amplitude $0.5$; it is the observed steady state of that engine run.

> **Leaf references:** [photon-identification](./dynamics/ch4-continuum-electrodynamics/photon-identification.md).

### Quality
- confidence: 0.62
- depends-on:
  - clm-j550uh — K4 4-Port Irrep Decomposition [the A1 ⊕ T2 group theory this entry applies]
- solidity: 0.62 (use as input only, don't build deeper) [= min(0.62, 0.85)]
- rationale: The identification cleanly applies the cross-referenced A1 ⊕ T2 decomposition (owned by clm-j550uh): A1 longitudinal dissipates via Gauss's law, T2 transverse triplet survives as the photon, and the four "tightly-coupled properties" are honestly disclosed with property 4 (Z_0 match) flagged as a restatement of property 3 (sub-saturation), not an independent fifth property. The empirical anchor (λ_4 = 0 exactly, λ_1..3 = 1.65/1.22/1.13, trace = 4) is a real consistency observation but rests on a single seeded (2,3) Golden-Torus ansatz run at amplitude 0.5, which caps confidence at the upper-mid band.
- strengthen-by:
  - Reproduce the λ_4 = 0 / T2-survival result across multiple seeds, amplitudes, and lattice sizes rather than the single (2,3) amplitude-0.5 run
  - Show the A1 dissipation is monotonic and complete from the Op3 saturation mechanism analytically, not only empirically
  - Demonstrate that the four properties are genuinely equivalent (any one implies the others) rather than asserting it
  - Confirm the steady state is the photon specifically (vs any T2-content soliton) by an independent observable
---

## Electron = Photon + TIR Confinement
<!-- id: clm-i4p11y -->

The electron is a self-trapped photon: when a $T_2$ photon's amplitude crosses $V_{\text{yield}}$, Axiom 4 drives $C_{\text{eff}}\to\infty$, $Z\to0$, $\Gamma\to-1$, and the lattice self-creates a total-internal-reflection cavity that traps the photon into a standing wave.

> **🟡 COEXIST FLAG (2026-06-10, Rule 12 — this claim is PRESERVED UNEDITED per the Grant adjudication "do NOT edit clm-i4p11y"; this is a flag-for-the-auditor note, not a claim edit).** Grant adjudicated the apparent tension between this leaf (electron = the *trapped transverse standing wave*) and the genesis-arc finding (electron *end-state* = the *longitudinal bulk* mode) as **COEXIST**, not contradiction: clm-i4p11y's trapped transverse standing wave is the **photon precursor**; the electron **end-state** is the longitudinal bulk mode. The directive was to **build the end-state separately** (do not rewrite this claim) and flag it here. Adjudication recorded at the crystal-graft-v2 verdict, `_orchestration/2026-06-09_ion-compression-rectifier-arc.md:139` ("TENSION 1 = COEXIST … the photon *precursor* … the electron *end-state* = the longitudinal bulk mode — … do NOT edit clm-i4p11y, flag it for the auditor"); the end-state build is the graft-v3/v4 line (`analysis/2026-06-10-graft-v4-photon-helicity`, Outcome LOCK-FAIL — the end-state is not yet realized). *(Verify-before-cite note: Deliverable-3 brief said "v4 prereg record"; the actual COEXIST adjudication record is the graft-v2 verdict cited above — the v4 prereg does not restate it.)*

> **🟡 OBSERVABLE-PROJECTION GATE-SUPPORT NOTE (2026-06-20, Rule 12 — flag-for-the-auditor, NOT a claim/rationale edit; the "do NOT edit clm-i4p11y" directive above is held).** The claim's observable-projection list (Specific Claim 3, "charge = topological winding, spin-½ = Finkelstein–Misner 4π double-cover") now has merged gate support for two of its projections — recorded here as a flag, **at exact honest scope, not promoted to "derived":**
> - **spin-½ = 4π double-cover → REPRESENTABILITY** (#299, `research/2026-06-19_spin-doublecover-gate_result.md`): the substrate ADMITS the 2T⊂SU(2) double-cover action (SU(2)-lift holonomy −I@2π / +I@4π, distinct from the SO(3) baseline, stable R=4,6,8). This is the *representability* condition, Class-D — **NOT dynamics-selection** (kinematic gate; it does not show the field dynamically settles into 2T). See clm-rkisb8 (same gate, upgraded there).
> - **charge = winding → FORCED-INTEGER GIVEN [Q]≡[L]** (#300, `research/2026-06-19_charge-quantization-gate_result.md`): GIVEN the TKI posit that charge is the topological winding/linking integer of the Cosserat ω grade, the quantization is structurally FORCED (𝒬=3 on the planted (2,3), integer, deformation-robust, α-free, sign=chirality). **Conditional on the asserted [Q]≡[L] posit (the gate does NOT derive the posit); the winding is PLANTED, not self-formed (NOT a self-formation / emergence claim).** **Caveat (load-bearing):** C.3 closes by the p·q **product-formula** (𝒬_H = int(w_tor·w_pol)), NOT by two independent integrals agreeing — the genuinely-independent Beltrami helicity integral returns **~18% of p·q** at this lattice scale and does NOT normalize to the integer. So C.3 is **ADDRESSED-BY-FORMULA, not CONFIRMED-BY-TWO-INTEGRALS**; STAYS OPEN.
> Both are filed as gate-support for the already-asserted projections; neither converts this claim's solidity band, and neither is "derived." (The third projection, mass = ℏω_C, and α = leakage rate, are unaffected by these gates.)

- _Specific Claims_
  - When a transverse $T_2$ photon at $\omega = \omega_C$ drives a single-bond LC tank at resonance, reactive energy accumulates until $V \to V_{\text{yield}} = \sqrt{\alpha}\,V_{\text{snap}} \approx 43.65$ kV.
  - At yield, Axiom 4 engages: $C_{\text{eff}} = C_0/\sqrt{1-(V/V_{\text{yield}})^2} \to \infty$, local impedance $Z = \sqrt{\mu_0/C_{\text{eff}}} \to 0$, and $\Gamma = (Z_{\text{local}}-Z_0)/(Z_{\text{local}}+Z_0) \to -1$ — a self-created perfect TIR mirror.
  - The trapped transverse standing wave is the electron; all electron observables are projections of this bound configuration (rest mass = resonant trapped energy, charge = topological winding, spin-½ = Finkelstein–Misner $4\pi$ double-cover, $\alpha$ = TIR leakage rate per cycle).
  - Electron and photon are two phases of the same substrate dynamics — bound (saturated) and free (unsaturated) — with photon emission the reverse process when the TIR condition transiently fails.
- _Specific Non-Claims and Caveats_
  - The electron's real-space body is the $0_1$ unknot soliton; the $(2,3)$/trefoil structure is the phase-space (Clifford-torus) winding label, not the real-space body topology.
  - The mechanism is presented step-by-step as a substrate narrative; the leaf does not provide an engine-validated quantitative trajectory of the $C_{\text{eff}}\to\infty$, $\Gamma\to-1$ trapping event (the breathing-soliton bound state is validated separately — see `clm-utnwkc`).
  - The observable-projection list (mass, charge, spin, $g$-factor) is asserted as a structural mapping; each individual observable carries its own derivation and quality status elsewhere in the corpus.
  - Pair-production and Compton-scattering consequences (§5) are stated as mechanism narratives consistent with the TIR picture, not as independently validated cross-section predictions.

> **Leaf references:** [photon-identification](./dynamics/ch4-continuum-electrodynamics/photon-identification.md).

### Quality
- confidence: 0.45
- depends-on:
  - clm-3npynp — Photon = T2-Only Cosserat Microrotation [the object being trapped]
  - clm-fr3mos — Compton Frequency Threshold [ω_C resonance + V_yield = √α V_snap that triggers the trap]
- solidity: 0.45 (use as input only, don't build deeper) [= min(0.45, 0.55)]
- rationale: The trapping chain (resonant build-up to V_yield → Axiom 4 C_eff→∞ → Z→0 → Γ→-1 self-created TIR mirror → standing wave) is internally consistent algebra given the saturation kernel and is a clean qualitative mechanism, but the leaf explicitly provides NO engine-validated quantitative trajectory of the C_eff→∞/Γ→-1 trapping event, and the observable-projection list (mass = ℏω_C, charge = winding, spin-½ = 4π double-cover, α = leakage rate) is asserted as a structural mapping with each observable's derivation living elsewhere. Qualitative-where-quantitative-is-implied lands this in the significant-gap band.
- strengthen-by:
  - Provide an engine-validated trajectory of the C_eff→∞, Γ→-1 trapping event (currently a step-by-step narrative only)
  - Derive (not assert) that the trapped standing-wave energy equals m_e c^2 = ℏω_C as a self-consistent eigenvalue of the self-created cavity
  - Show the reactive-energy build-up to V_yield is actually achievable at resonance (step C asserts off-resonance shedding paths are closed without quantifying the Q required)
  - Tie each observable-projection (charge, spin, g-factor) to its own validated derivation rather than listing them as a structural mapping
---

## Compton Frequency $\omega_C$ as Photon→Electron Transition Threshold
<!-- id: clm-fr3mos -->

The Compton frequency $\omega_C = c/\ell_{\text{node}}$ is a genuine dynamical threshold for the photon-to-electron transition: it partitions photon behavior into three regimes, and the electron rest energy is $m_e c^2 = \hbar\omega_C$.

- _Specific Claims_
  - $\omega_C = c/\ell_{\text{node}}$ is the single-bond-scale natural frequency of the lattice — a consequence of lattice geometry and $Z_0 = \sqrt{\mu_0/\varepsilon_0}$, not an independent calibration.
  - The electron rest energy is $m_e c^2 = \hbar\omega_C = \hbar c/\ell_{\text{node}}$ — the energy of a photon at the lattice self-saturation frequency.
  - Three regimes: $\omega < \omega_C$ (off-resonance, photon passes transparently), $\omega = \omega_C$ (full resonance, saturation engages, photon → bound → electron), $\omega > \omega_C$ (off-resonance, transient saturation only, Compton-like scattering).
  - $\omega_C$ is a genuine qualitative threshold, analogous to a Josephson junction's critical current or a varactor's breakdown voltage.
- _Specific Non-Claims and Caveats_
  - The relation $m_e c^2 = \hbar\omega_C = \hbar c/\ell_{\text{node}}$ carries one input mass scale — one of $\{m_e, \ell_{\text{node}}\}$ is the empirical input (consistent with the Vol 1 closure-status disclosure, `clm-5xon03`); it is not an independent ab-initio derivation of $m_e$.
  - The three-regime partition is a mechanism description; it does not derive Compton-scattering cross-sections quantitatively.
  - $V_{\text{yield}} = \sqrt{\alpha}\,V_{\text{snap}}$ inherits $\alpha$; under the trefoil/unknot body-topology dependence, the numerical threshold is $\alpha$-conditioned.

> **Leaf references:** [photon-identification](./dynamics/ch4-continuum-electrodynamics/photon-identification.md).

### Quality
- confidence: 0.55
- depends-on:
  - clm-5xon03 — Zero-Parameter Closure Status [the one-empirical-input-mass-scale disclosure]
- solidity: 0.55 (use as input only, don't build deeper) [= min(0.55, 0.65)]
- rationale: ω_C = c/ℓ_node is essentially definitional once ℓ_node is fixed (single-bond natural frequency), and m_e c^2 = ℏω_C = ℏc/ℓ_node is correct algebra but, as the leaf honestly states, carries one empirical input mass scale (one of {m_e, ℓ_node}) — it is not an ab-initio m_e derivation. The three-regime partition (ω<ω_C transparent / ω=ω_C bound / ω>ω_C Compton) is a qualitative mechanism description that does not derive scattering cross-sections; the claim is largely a restatement of the lattice-scale relation rather than a fresh derivation, holding it mid-band.
- strengthen-by:
  - Make explicit which of {m_e, ℓ_node} is the empirical input and propagate that into the closure-status accounting so the relation is not read as an independent m_e prediction
  - Derive the regime boundaries quantitatively (e.g., the resonance bandwidth around ω_C) rather than asserting the three-regime partition qualitatively
  - Connect ω = ω_C resonance to a quantitative saturation-engagement condition (link to the i4p11y trapping trajectory)
  - Show the V_yield = √α V_snap threshold's α-conditioning consistently with the trefoil/unknot body-topology dependence
---

## Photon Propagation Baseline — $v/c = \sqrt{2}$ Cardinal-Axis Kinematics
<!-- id: clm-djpx2v -->

A free photon on the linear K4-TLM substrate propagates at $v = c\sqrt{2}$ along cardinal axes (measured $v/c = 1.450$) and $v = c$ along diagonal/port axes — a pure Axiom-1 substrate-geometry anisotropy, not a relativity violation.

- _Specific Claims_
  - The measured cardinal-axis ($+\hat{x}$) wavefront speed is $v_{\text{meas}} = 4.348 \times 10^8$ m/s, i.e. $v/c = 1.450 \approx \sqrt{2}$, from peak-energy-density arrival times at two pre-registered reference planes.
  - Along diagonal axes (port unit vectors $\hat{p}_n$) the predicted speed is $v = c$; the $\sqrt{2}$ factor is a cardinal-axis lattice-projection artifact (port projections $\pm1/\sqrt{3}$; the 4-port pattern advances each step by one full cardinal cell).
  - The test runs at $0.01\,V_{\text{SNAP}} \approx 5.1$ kV — sub-yield, linear-vacuum (Regime I) throughout: no Axiom 4 engagement, no TIR wall, $Z_{\text{eff}} \approx Z_0$, $c_{\text{eff}} \approx c_0$. The free photon is not the electron.
  - This is the calibration baseline for photon-physics work on K4-TLM; deviation from it at the baseline level indicates an engine-implementation issue, not framework physics.
- _Specific Non-Claims and Caveats_
  - The cardinal-axis $\sqrt{2}$ is a lattice-projection artifact that disappears in the continuum limit and at diagonal injection; it is NOT a claim that physical light travels faster than $c$.
  - The diagonal-axis $v = c$ is a prediction; the leaf's companion diagonal script is flagged numerical-only (GIF pending), so the diagonal result is not reported as an executed measurement here.
  - The visualization wavelength ($\lambda_{\text{cells}} = 10$) is a visualization choice, not matched to the Compton scale or any SM scale.
  - The measurement is a single pre-registered run on a $96^3$ lattice; $v/c = 1.450$ vs $\sqrt{2} = 1.414$ is an approximate match (lattice-discretization-level agreement).

> **Leaf references:** [photon-propagation-baseline](./dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md).

### Quality
- confidence: 0.70
- depends-on:
  - clm-uu1qbo — A1/T2 Propagation-Speed Split [supplies the √2 = √(K/G) at magic-angle K=2G underpinning the cardinal-axis kinematic]
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.78)]
- rationale: The √2 cardinal-axis factor is cleanly tied to the K=2G magic-angle moduli condition (v_A1/v_T2 = √(K/G) = √2) and the single 96³ pre-registered run measures v/c = 1.450 vs √2 = 1.414 (~2.5% lattice-discretization agreement); the leaf honestly frames this as a substrate-geometry projection artifact that vanishes in the continuum limit, NOT a superluminal physical-light claim. Minor caveats hold confidence below 0.85: the diagonal-axis v=c is an unmeasured prediction (companion script numerical-only), and the result rests on one seeded run at one lattice size.
- strengthen-by:
  - Execute the diagonal-axis v=c measurement (companion script is numerical-only / GIF pending) to confirm the predicted port-axis isotropy
  - Run a lattice-size convergence study (beyond the single 96³ run) to show v/c → √2 as discretization error shrinks
  - Derive the cardinal-axis √2 directly from the port-projection geometry (±1/√3 projections advancing one full cardinal cell) rather than only cross-checking against the moduli ratio
  - State the expected continuum-limit residual so "approximate match" becomes a bounded prediction
---

## $A_1$/$T_2$ Propagation-Speed Split — $c\sqrt{2}$ vs $c$ at the Magic Angle
<!-- id: clm-uu1qbo -->

The K4-substrate $A_1$ and $T_2$ port-modes propagate at distinct speeds — $A_1$ at $c\sqrt{2} = \sqrt{K_{\text{bulk}}/\rho}$, the $T_2$ photon at $c = \sqrt{G/\rho}$ — and the magic-angle condition $K = 2G$ makes the ratio exactly $\sqrt{2}$.

- _Specific Claims_
  - The $A_1$ (scalar/longitudinal) mode propagates at $c\sqrt{2} = \sqrt{K_{\text{bulk}}/\rho}$, governed by the bulk modulus; the $T_2$ (transverse photon) mode propagates at $c = \sqrt{G/\rho}$, governed by the shear modulus.
  - The K4 magic-angle macroscopic-moduli condition $K = 2G$ (Vol 1 Ch 2) makes the speed ratio $v_{A_1}/v_{T_2} = \sqrt{K/G} = \sqrt{2}$ exactly.
  - This is the same $\sqrt{2}$ that appears in the cardinal-axis wavefront kinematics, tying the port-mode speed split to the measured anisotropy.
- _Specific Non-Claims and Caveats_
  - The underlying $A_1 \oplus T_2$ group-theoretic decomposition is NOT this entry's claim — it is owned by `clm-j550uh`; this leaf cites it and measures the speed split it implies.
  - The speeds $\sqrt{K_{\text{bulk}}/\rho}$ and $\sqrt{G/\rho}$ are stated from the macroscopic-moduli relations; the $K = 2G$ magic-angle condition is itself a Vol 1 Ch 2 result this claim depends on, not re-derived here.
  - The split is a substrate-geometry property; it carries the same continuum-limit caveat as the cardinal-axis $\sqrt{2}$.
  - **(2026-06-08 c_L reconciliation)** The $A_1$ speed $\sqrt{K_{\text{bulk}}/\rho} = \sqrt{2}\,c$ is the **bulk-modulus pure-dilatation** port-mode, NOT the isotropic-solid longitudinal **P-wave** $\sqrt{(K+\tfrac{4}{3}G)/\rho} = \sqrt{10/3}\,c$ ($\nu=2/7$; canonical vol_2 Ch 7). Both are real and distinct; this entry's $\sqrt{2}$ (and the cardinal-axis measurement) is the bulk-modulus quantity, correctly used as such.

> **Leaf references:** [photon-propagation-baseline](./dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md).

### Quality
- confidence: 0.78
- depends-on:
  - clm-j550uh — K4 4-Port Irrep Decomposition [supplies the A_1/T_2 split whose speeds this entry measures]
  - clm-ys0xl1 — K4 Rotation Group T=A_4 [underlying T_d symmetry of the port modes]
- solidity: 0.78 (ok to build on, see caveats) [= min(0.78, 0.85)]
- rationale: Given the cited K=2G magic-angle condition, v_{A_1}/v_{T_2}=√(K/G)=√2 is exact algebra, and v_{A_1}=√(K_bulk/ρ) (bulk modulus, pure-dilatation scalar mode), v_{T_2}=√(G/ρ) (shear modulus, transverse photon) are the K4 port-mode speeds; the empirical cardinal-axis v/c=1.450 confirms √2 to ~2.5%. One clearly-flagged matched step: the K=2G condition is imported from Vol 1 Ch 2 (a dependency, not penalized locally), and the √2 carries a continuum-limit caveat the leaf states. **[2026-06-08 c_L reconciliation — Rule 12 correction: the prior wording called √(K_bulk/ρ) and √(G/ρ) "the standard continuum-elasticity longitudinal/shear speeds." That mischaracterizes the longitudinal case — the standard isotropic-solid longitudinal P-wave speed is √((K+4G/3)/ρ)=√(10/3) c (Poisson ν=2/7; canonical vol_2 Ch 7), NOT √(K/ρ). The A_1 mode here is the BULK-MODULUS pure-dilatation port-mode √(K/ρ)=√2 c — correct as the bulk-modulus quantity and as the measured cardinal-axis speed, but distinct from the continuum P-wave. The √2 quantity is RETAINED; only the "continuum-elasticity longitudinal" label is corrected.]**
- strengthen-by:
  - Note the 2.5% empirical-vs-√2 gap and bound it (lattice-dispersion vs continuum) rather than rounding 1.450→√2
  - Make the identification of the elastic bulk/shear speeds with the A_1/T_2 port modes explicit (not just asserted by table row)
  - State the continuum-limit condition under which the cardinal √2 disappears, tying the two √2's together quantitatively
---

## K4 Photon Thermal Noise — Equipartition $\langle V^2\rangle_T$
<!-- id: clm-viawy9 -->

Classical equipartition on the K4 substrate gives the photon-field thermal-noise variance $\langle V^2\rangle_T = k_B T/(\varepsilon_0\ell_{\text{node}})$, equivalently $k_B T \cdot 4\pi/\alpha$ in lattice natural units.

- _Specific Claims_
  - Each bond's capacitance $C_{\text{cell}} = \varepsilon_0\ell_{\text{node}}$ gives classical Johnson-Nyquist noise $\langle V^2\rangle_T = k_B T/C_{\text{cell}} = k_B T/(\varepsilon_0\ell_{\text{node}})$.
  - In lattice natural units ($\varepsilon_0 = \alpha/(4\pi)$) this is $\langle V^2\rangle_T = k_B T \cdot 4\pi/\alpha$.
  - The numerical $\sigma_V/V_{\text{SNAP}}$ values follow per temperature (e.g. $3.96\times10^{-4}$ at $T_{\text{CMB}}$; $1.0$ at $T_{V\text{-rupt}}$; $7.63$ at $10^9$ K).
- _Specific Non-Claims and Caveats_
  - The "$T$" is the temperature of the K4 lattice substrate itself (the thermal amplitude of the scalar $V$ field on bond capacitance), NOT the kinetic temperature of any particle residing in the vacuum — this distinction is load-bearing.
  - The derivation is classical equipartition (each quadratic DOF gets $k_B T/2$); it is not a quantum/Bose-Einstein treatment and inherits the classical-equipartition regime of validity.
  - The result feeds the vacuum-rupture-temperature claim (`clm-f4urxy`) but is itself only the $\langle V^2\rangle_T$ formula and its numerical table.

> **Leaf references:** [thermal-lattice-noise](./dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md).

### Quality
- confidence: 0.80
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation [supplies α in the natural-units form ⟨V²⟩_T = k_B T·4π/α via ε₀=α/4π]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.80, 0.63)]
- rationale: Verified — per-bond capacitance C_cell=ε₀ℓ_node gives the standard Johnson-Nyquist single-mode result ⟨V²⟩_T=k_B T/C_cell=k_B T/(ε₀ℓ_node), and the natural-units rewrite ⟨V²⟩_T=k_B T·4π/α follows directly from ε₀=α/(4π); the substrate-T vs particle-T caveat and the classical-equipartition regime are explicitly flagged. This is essentially a textbook Nyquist relation applied to one lattice capacitor, which is rigorous; it sits at 0.80 rather than higher because "per port" mode-counting (4 ports/node) and how the per-bond ⟨V²⟩ aggregates to the field variance is asserted rather than worked, and the numerical σ_V table rows inherit that.
- strengthen-by:
  - Make the per-port / per-bond mode-counting explicit (how the 4-port-per-node structure maps the single-capacitor Nyquist result onto the field variance).
  - Note the regime of validity for classical equipartition (k_B T vs ℏω_bond at the relevant temperatures) so the table rows at high T are bounded against quantum corrections.
---

## AVE-Native Vacuum Rupture Temperature $T_{V\text{-rupt}} \approx 3.44 \times 10^6$ K
<!-- id: clm-f4urxy -->

An AVE-native vacuum-substrate temperature threshold: at $T_{V\text{-rupt}} \approx 3.44 \times 10^6$ K the thermal $V$ fluctuation reaches $\sigma_V = V_{\text{SNAP}}$ and the vacuum spontaneously ruptures into pairs — a temperature-stated analog of the Schwinger limit, falsifiable.

- _Specific Claims_
  - The rupture condition $\sigma_V = V_{\text{SNAP}}$ gives $k_B T_{V\text{-rupt}}/(m_e c^2) = \alpha/(4\pi) \approx 5.805\times10^{-4}$, i.e. $k_B T_{V\text{-rupt}} \approx 296.7$ eV, $T_{V\text{-rupt}} \approx 3.44\times10^6$ K.
  - If the K4 substrate itself were in thermal equilibrium above $3.44$ MK, the $V$ fluctuations would exceed $V_{\text{SNAP}}$ and the vacuum would rupture; below it, the vacuum sustains thermal noise without breaking.
  - It is an AVE-native analog of the Schwinger limit stated as a vacuum-substrate temperature rather than a field strength, and is falsifiable: heating the vacuum itself (not merely a plasma) above 3.44 MK without spontaneous pair generation would falsify AVE.
  - The vacuum-substrate temperature is distinct from particle-plasma temperature — e.g. the Sun's core has $\sim10^7$ K plasma but a still-cold ($\sim2.7$ K) vacuum substrate; only matter-radiation-coupled early-universe conditions heat the substrate itself.
- _Specific Non-Claims and Caveats_
  - The threshold rests on the classical-equipartition $\langle V^2\rangle_T$ (entry `clm-viawy9`) and inherits that derivation's classical regime of validity.
  - "$\sigma_V = V_{\text{SNAP}}$" is a one-sigma criterion — the vacuum reaches rupture amplitude at one-sigma fluctuation; it is a threshold definition, not a rate calculation for pair-production yield.
  - $T_{V\text{-rupt}}$ inherits $\alpha$ through $\alpha/(4\pi)$; the value is $\alpha$-conditioned.
  - Canonization to the manuscript is queued (E-042, manuscript_pending) — the leaf is the current canonical statement; the manuscript anchor is pending.

> **Leaf references:** [thermal-lattice-noise](./dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md).

### Quality
- confidence: 0.72
- depends-on:
  - clm-viawy9 — K4 Photon Thermal Noise ⟨V²⟩_T [supplies the equipartition variance whose σ_V=V_SNAP condition defines the threshold]
  - clm-0ktpcn — Golden Torus α Derivation [supplies α entering k_B T/(m_e c²)=α/(4π)]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.72, 0.63)]
- rationale: Given the ⟨V²⟩_T formula, the threshold follows cleanly: σ_V=V_SNAP ⟹ k_B T_rupt/(m_e c²)=α/(4π)≈5.805×10⁻⁴ ⟹ k_B T≈296.7 eV ⟹ T≈3.44 MK, arithmetic verified, and the vacuum-substrate-T vs particle-plasma-T distinction is clearly stated and load-bearing. It is a manifestation/consistency-style result (a temperature restatement of the saturation/Schwinger threshold) and is honestly flagged as a one-sigma threshold definition, not a pair-production rate; the local derivation is sound modulo the inherited classical-equipartition regime and the σ_V=V_SNAP one-sigma criterion choice, which keep it in the upper-mid band.
- strengthen-by:
  - Justify the one-sigma σ_V=V_SNAP rupture criterion versus a rate/probability threshold (a tail-integral pair-production rate would sharpen "rupture temperature" into a calculable yield).
  - Bound the classical-equipartition error against a Bose-Einstein treatment at ~296.7 eV, where quantum corrections to ⟨V²⟩_T may be non-negligible.
  - State explicitly how the vacuum substrate would be heated (the matter-radiation-coupling mechanism) so the falsification protocol "heat the vacuum itself" is operational.
---

## Cosserat Rotational Thermal Noise — Finite at the Origin via the Mass Gap
<!-- id: clm-qimsgq -->

The Cosserat microrotation field $\omega$ has thermal noise $\sigma_\omega \approx 0.17\sqrt{k_B T}$ (natural units) — finite at the origin (not UV-divergent) because the $\omega$ field is massive, with mass gap $m^2 = 4G_c/I_\omega$.

- _Specific Claims_
  - The rotational Lagrangian carries a kinetic term $\tfrac{1}{2}I_\omega|\dot\omega|^2$, a mass-gap potential $2G_c|\omega|^2$, and a gradient potential $\tfrac{1}{2}\gamma|\nabla\omega|^2$; the $\omega$ field has a nonzero mass gap $m^2 = 4G_c/I_\omega$.
  - Because the field is massive, its classical-equipartition thermal noise is finite at the origin (not UV-divergent): $\langle\omega^2\rangle_T = \tfrac{k_B T}{4\pi^2 I_\omega}\int_0^{k_{\max}} k^2\,dk/(c_R^2 k^2 + m^2)$.
  - In natural units ($I_\omega = \gamma = G_c = 1$, $m^2 = 4$) this gives $\langle\omega^2\rangle_T \approx 0.0288\,k_B T$, i.e. $\sigma_\omega \approx 0.17\sqrt{k_B T}$.
  - At $T_{\text{CMB}}$, $\sigma_\omega \approx 3.6\times10^{-6}$ — effectively zero for pair creation, confirming cold-vacuum cannot produce pairs by thermal noise alone; pair-creation engine runs need $T \sim 10^8$ K ($\sigma_\omega \sim 0.02$).
- _Specific Non-Claims and Caveats_
  - The mass-gap value $m^2 = 4G_c/I_\omega$ is taken from the Cosserat mass-gap leaf (a dependency created separately); this entry uses it, does not derive it. The dependency link is to be filled in a later rescore pass.
  - The derivation is classical equipartition, not a quantum field-theoretic treatment.
  - The "finite at the origin" property is a consequence of the field being massive; if the mass gap were revised, $\sigma_\omega$ would change.
  - The $\sigma_\omega \approx 0.17\sqrt{k_B T}$ coefficient holds in natural units with $G_c = I_\omega = \gamma = 1$; the mode-factor $\approx 1.14$ is a specific integral evaluation.

> **Leaf references:** [thermal-lattice-noise](./dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md).

### Quality
- confidence: 0.62
- depends-on:
  - clm-jz0xaw — Cosserat Mass-Gap Formula m²=4G_c/I_ω [supplies the mass gap that makes the k-integral finite at the origin]
- solidity: 0.62 (use as input only, don't build deeper) [= min(0.62, 0.82)]
- rationale: The qualitative core is sound — a massive ω field has classical-equipartition variance ⟨ω²⟩_T = (k_B T/4π²I_ω)∫k²dk/(c_R²k²+m²) that is finite at k→0 (the gap regularizes the IR), in genuine contrast to the massless u sector. But the headline coefficient is matched-not-shown: the integral still needs the same UV cutoff k_max as the massless case (the integrand →k_B T/4π²I_ω·c_R² at large k, so ∫k²dk/(c²k²+m²) diverges linearly in k_max), so "finite at the origin" addresses only the IR, and the "mode-factor ≈1.14 = π−2·arctan(π/2)" and σ_ω≈0.17√(k_B T) follow from a specific cutoff choice not stated in the entry. That undisclosed-cutoff/specific-integral step puts the quantitative coefficient in the matched-not-derived band.
- strengthen-by:
  - State the UV cutoff used in the σ_ω integral and show the 1.14 mode-factor explicitly (the integral is UV-sensitive, so "finite at the origin" should be qualified as IR-finiteness, with the cutoff carrying the UV scale).
  - Fill in the depends-on to clm-jz0xaw in the leaf (the entry notes the mass gap is imported, not derived here).
  - Bound the classical-equipartition error and confirm the numerical σ_ω table rows against a direct mode-sum on the lattice.
---

## Cosserat Translational Thermal Noise — Massless Field, Nyquist-Cut
<!-- id: clm-rebdw1 -->

The Cosserat translation field $u$ is massless; its thermal noise requires a UV cutoff at the lattice-Nyquist wavenumber $k_{\max} = \pi/\ell_{\text{node}}$, giving $\sigma_u = \sqrt{k_B T/2\pi}$ in natural units.

- _Specific Claims_
  - The $u$ field is massless, so its thermal noise is UV-divergent without a cutoff; the cutoff is the lattice-Nyquist wavenumber $k_{\max} = \pi/\ell_{\text{node}}$.
  - The variance is $\langle u^2\rangle_T = \tfrac{k_B T}{G}\cdot\tfrac{k_{\max}}{2\pi^2} = \tfrac{k_B T}{2\pi G\ell_{\text{node}}}$.
  - In natural units ($G = \rho = 1$, $\ell_{\text{node}} = 1$): $\sigma_u^2 = \sigma_{\dot u}^2 = k_B T/2\pi$ — both the field and its velocity have characteristic scale $\sqrt{k_B T/2\pi}$.
- _Specific Non-Claims and Caveats_
  - The UV cutoff is necessary precisely because the $u$ field is massless — contrast the Cosserat rotational field (`clm-qimsgq`), which is finite at the origin without a cutoff; the lattice cutoff is what makes the massless-field noise finite.
  - The derivation is classical equipartition.
  - The $\sqrt{k_B T/2\pi}$ scale holds in natural units with $G = \rho = \ell_{\text{node}} = 1$.

> **Leaf references:** [thermal-lattice-noise](./dynamics/ch3-quantum-signal-dynamics/thermal-lattice-noise.md).

### Quality
- confidence: 0.70
- solidity: 0.70 (ok to build on, see caveats)
- rationale: Locally sound — the u field is massless so its equipartition noise is UV-divergent and the lattice supplies a physical cutoff k_max=π/ℓ_node, giving ⟨u²⟩_T = (k_B T/G)·(k_max/2π²) = k_B T/(2πGℓ_node) and σ_u=√(k_B T/2π) in natural units; the regime contrast against the massive ω sector (clm-qimsgq) is correctly drawn. Held at 0.70 because the k_max/2π² density prefactor and the 3D mode-counting that turns the cutoff into exactly k_max/2π² are stated, not shown in the entry, and the result is cutoff-convention-dependent (a different UV regularization shifts the prefactor).
- strengthen-by:
  - Show the 3D mode-count integral that yields the k_max/2π² prefactor explicitly, so the σ_u coefficient is derived rather than asserted.
  - State whether the cutoff is a hard sphere |k|<π/ℓ_node or the first Brillouin zone of the K4 lattice (the geometry changes the numerical prefactor).
  - Confirm the equipartition assignment of equal k_B T/2 to field and velocity DOFs is consistent with the lattice dispersion at the cutoff scale.
---

## Breathing-Soliton v14 Mode-I PASS on the Master Equation FDTD Engine
<!-- id: clm-utnwkc -->

The Master Equation FDTD engine autonomously hosts a sustained breathing soliton bound state (sech seed, 4/4 acceptance) at one active cell — closing the v14 pre-registered test and validating the boundary-envelope reformulation at the dynamic-engine level.

- _Specific Claims_
  - On a sech seed ($A = 0.85$, $R = 2.5$, $N = 32$ grid) run for 5000 timesteps, the Master Equation FDTD engine (`master_equation_fdtd.py`) sustains a breathing soliton bound state.
  - All four acceptance criteria pass: $V_{\text{peak}}$ late-phase mean $= 0.250$ ($> 0.2$); FWHM range $0.97$–$3.68\times$ (within $0.4$–$4.0$); $\Delta n = 0.0111$ ($> 0.01$); Q-factor integral $\Lambda_{\text{total}} = 102.8$ vs $137.0$ (relative error $0.25 < 0.5$) — net 4/4 = Mode I PASS.
  - The K4-TLM engine at the same geometry yields Mode III (no autonomous bound state across 4 seed variants); the Master Equation FDTD succeeds at exactly the task K4-TLM cannot, consistent with the A-027 two-engine architecture.
- _Specific Non-Claims and Caveats_
  - The PASS validates that the Master Equation engine sustains one breathing soliton at this geometry — it does not validate all bound-state physics or every electron observable.
  - The Q-factor criterion 4 is met within a $50\%$ tolerance ($\Lambda_{\text{total}} = 102.8$ vs canonical $137.0$, $1.33\times$ off) — a tolerance-band pass, not a precision match.
  - A truly stationary (non-breathing) soliton of the Master Equation is NOT found with current seed profiles; finding it would need imaginary-time propagation or Newton-Raphson on the time-independent profile (post-Mode-I engineering, flagged open).
  - The Picard renormalization scheme introduced discontinuities producing extra radiation (a Mode III failure mode); the Master Equation FDTD is a scalar engine with Cosserat $(u,\omega)$ not currently coupled — both flagged open, not blocking v14 closure.

> **Leaf references:** [breathing-soliton-v14-mode-i](./dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md).

### Quality
- confidence: 0.70
- depends-on:
  - clm-usflef — Test-1b Acceptance Criterion [supplies the breathing-appropriate criterion 1 used in the 4/4 adjudication]
- solidity: 0.70 (ok to build on, see caveats) [= min(0.70, 0.70)]
- rationale: The leaf documents a reproducible test with a fully specified configuration (sech seed A=0.85, R=2.5, N=32 grid, 5000 steps, named engine master_equation_fdtd.py) and four explicit acceptance criteria with measured values all met, plus a decisive cross-engine contrast against K4-TLM Mode III — exactly the reproducible-PASS-with-clear-criterion pattern. It is held below the solid band because criterion 4 (Q-factor) is met only within a 50% tolerance band (Λ=102.8 vs canonical 137.0, 1.33× off) and the criterion thresholds (0.4–4.0 FWHM, >0.01 Δn) are loose, so the PASS validates one bound state at one geometry, not precision physics.
- strengthen-by:
  - Tighten or independently justify the criterion-4 50% Q-factor tolerance band; explain the 1.33× offset from the canonical 137.0
  - Demonstrate seed-independence (multiple seed profiles converging to the same breather) to show the result is not seed-tuned
  - Report numerical-convergence under grid refinement and timestep variation (Courant margin)
  - State the energy/charge/angular-momentum (M,Q,J) integrated invariants of the hosted structure to connect the PASS to the physical observables
---

## Test-1b Breathing Acceptance Criterion Is Canonical
<!-- id: clm-usflef -->

The Test-1b breathing-soliton acceptance criterion — mean late-phase $V_{\text{peak}} > 0.2\times$ initial — is canonical, retiring the strict stationary criterion; the breathing solution IS the physical electron state.

- _Specific Claims_
  - The original Test 1 criterion ($V_{\text{center}} > 0.5\times$ initial at $t > 1000\,dt$) is correct for a stationary bound state but wrong for a breathing soliton, whose $V_{\text{center}}$ oscillates through zero.
  - The canonical replacement is Test 1b: $\text{mean}(V_{\text{peak}}) > 0.2\times$ initial over the late phase — capturing sustained energy in the localized structure without requiring a static profile.
  - Test 1b is load-bearing because the Master Equation predicts breathing solutions natively (nonlinear $\sqrt{1-(V/V_{\text{yield}})^2}$ coefficient → frequency-locked oscillation), the seed is not a stationary eigenmode, the mean is the natural breathing-cycle average, and it matches Route B's time-averaged-observable methodology.
  - The breathing solution is the physical state of the canonical electron (Cosserat $\omega$ rotating at the Compton bulk-spin rate drives the $V$ oscillation), consistent with the doc 101 three-layer canonical electron — not a numerical artifact.
- _Specific Non-Claims and Caveats_
  - Retiring the strict stationary criterion (Test 1a) does NOT claim a stationary solution is impossible — it claims the breathing solution is the physical one; finding a stationary solution is flagged as open post-Mode-I engineering.
  - The $0.2\times$-initial threshold is a chosen criterion value; the leaf considers three Test 1 interpretations (1a strict, 1b breather, 1c envelope-bounded) and adopts 1b.
  - "The breathing solution IS the physical electron state" rests on the doc 101 three-layer canonical electron picture, an interpretive identification carried by the leaf.

> **Leaf references:** [breathing-soliton-v14-mode-i](./dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md).

### Quality
- confidence: 0.70
- solidity: 0.70 (ok to build on, see caveats)
- rationale: The leaf lays out three Test-1 interpretations and gives a coherent four-point physical justification for adopting 1b (native breathing from the √(1-(V/V_yield)²) coefficient, seed is not a stationary eigenmode, mean is the natural breathing-cycle average, parity with Route B time-averaging); it is a well-reasoned, internally consistent criterion-spec. It is downgraded from solid because the 0.2×-initial threshold is an admitted chosen value and "the breathing solution IS the physical electron" rests on the interpretive doc-101 three-layer identification carried by the leaf.
- strengthen-by:
  - Justify the specific 0.2× threshold quantitatively (e.g. tie it to the breather V_min/V_max envelope ratio rather than asserting it)
  - Provide an independent derivation that the seed relaxes to a breather (not a stationary attractor) rather than asserting non-eigenmode relaxation
  - Pin the doc-101 "breathing IS the electron" identification to a derived Compton-rate ω-V coupling, not interpretation
  - Show robustness of the 1b verdict to late-phase window choice and grid resolution
---

## Six-Fold Lattice Impedance Decomposition
<!-- id: clm-nxc9gy -->

The AVE corpus's multiple senses of "impedance" are canonically decomposed into six distinct concepts: free-space $Z_0$, per-cell $Z_{\text{cell}} (= Z_0)$, saturation-modulated $Z_{\text{eff}}(r) = Z_0/\sqrt{S}$, mutual inductance $\eta_{\text{vac}}$, mechanical $Z_{\text{mech}} = \xi_{\text{topo}}^2 Z_0$, and event-horizon $Z_{\text{EH}} \to 0$.

- _Specific Claims_
  - $Z_0 = \mu_0 c = \sqrt{\mu_0/\varepsilon_0} \approx 376.73$ Ω is the classical free-space (continuum) impedance; $Z_{\text{cell}} = \sqrt{L_{\text{cell}}/C_{\text{cell}}}$ is the per-bond lattice impedance.
  - $Z_{\text{cell}} = Z_0$ numerically because $\ell_{\text{node}}$ cancels (it appears in both $L_{\text{cell}} = \mu_0\ell_{\text{node}}$ and $C_{\text{cell}} = \varepsilon_0\ell_{\text{node}}$), but the two are conceptually distinct (physical bond vs continuum field ratio) — the equality is the substrate's Axiom-2 scale-invariance signature.
  - $Z_{\text{eff}}(r) = Z_0/\sqrt{S}$ with $S = \sqrt{1-A^2(r)}$ is the Op14 position-dependent saturation-modulated impedance, diverging as $A^2 \to 1$; $Z_{\text{mech}} = \xi_{\text{topo}}^2 Z_0 \approx 6.485\times10^{-11}$ kg/s is the Axiom-2 mechanical dual; $Z_{\text{EH}} \to 0$ is the full-saturation $\Gamma = -1$ TIR limit.
  - The mutual inductance $\eta_{\text{vac}}$ (via $R_{\text{vac}} = \xi_{\text{topo}}^{-2}\eta_{\text{vac}}$) is the node-to-node inductive coupling — implicitly encoded in the K4 scattering matrix's off-diagonal $0.5$ but with no explicit engine symbol.
- _Specific Non-Claims and Caveats_
  - $\eta_{\text{vac}}$ has no canonical symbol or explicit named operator yet — flagged (doc 45) as a missing operator symbol; the engine carries the cascade-coupling implicitly via the S-matrix and cannot independently tune it. A future axiom-homologation pass would add the explicit symbol.
  - The cascade-saturation timescale is a known engine limitation: the cascade lives on the outer K4-step $dt$ ($\approx 0.707$ in natural units) vs the bond-traversal $\tau_{\text{relax}} = 1$; these are comparable, so a single step may miss fast sub-step rebound effects. Flagged as an engine limitation, not a framework gap.
  - This decomposition is distinct from the related $Z = \sqrt{\mu/\varepsilon}$ scale-invariance result in the impedance-operator leaf — adjacent, not duplicate.
  - Several SI values are cited from Vol 4 Ch 1 (lines 118-120, 240, 278, 283, 364); the leaf collates and decomposes them rather than re-deriving each.

> **Leaf references:** [lattice-impedance-decomposition](./operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md).

### Quality
- confidence: 0.74
- depends-on:
  - clm-k6quve — Lattice-Native Units [the dimensional/natural-units table the decomposition is read in]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.74, 0.63)]
- rationale: This is a catalog/taxonomy that is internally consistent and dimensionally clean: Z_cell=Z_0 via ℓ_node cancellation in √(L_cell/C_cell) is shown, Z_eff=Z_0/√S, Z_mech=ξ_topo²Z_0, and Z_EH→0 are collated coherently. It scores as a well-organized catalog rather than a fresh derivation; one of the six (mutual inductance η_vac) is explicitly flagged as having no symbol and no explicit derivation, and several SI values are cited from Vol 4 rather than re-derived here.
- strengthen-by:
  - Give η_vac an explicit definition/derivation or mark it clearly as a placeholder rather than a sixth peer member
  - Re-derive (or one-line-cite the derivation of) the Vol 4 values for Z_mech and Z_EH so the catalog is self-contained
  - Confirm the dimensional consistency of Z_mech (ξ_topo²Z_0 → kg/s) inline to close the units check
---

## Lattice-Native Units — $V_{\text{YIELD}} = 1$, Not $V_{\text{SNAP}}$
<!-- id: clm-k6quve -->

In lattice natural units the engineering yield threshold is $V_{\text{YIELD}} = 1$ (not $V_{\text{SNAP}}$); because engine code normalizes to $V_{\text{SNAP}} = 1$, an amplitude of $0.5\,V_{\text{SNAP}}$ is in fact far above yield.

- _Specific Claims_
  - In lattice-native units ($\ell_{\text{node}} = m_e = c = \hbar = 1$), $V_{\text{YIELD}} = \sqrt{\alpha}\cdot V_{\text{SNAP}}$ evaluates to $1.0$, while $V_{\text{SNAP}} = m_e c^2/e = 1/\sqrt{\alpha} \approx 11.7$.
  - Engine code typically uses $V_{\text{SNAP}} = 1.0$ as the user-facing normalization; an input `amp = 0.5·V_SNAP` is therefore $0.5/\sqrt{\alpha} = 5.85$ in units where $V_{\text{YIELD}} = 1$ — massively above yield, below rupture.
  - The Axiom 4 operator normalizes $A$ to $V_{\text{SNAP}}$, so the $\sqrt{2\alpha}$ Regime I/II boundary is $A = 0.121$ in $V/V_{\text{SNAP}}$ units, equivalently $A = 1.42$ in $V_{\text{YIELD}}$ units.
  - The full dimensional table maps each Phase III simulator quantity to its lattice-native value (e.g. $e = \sqrt{\alpha}$, $\xi_{\text{topo}} = \sqrt{\alpha}$, $Z_0 = 1$, $\tau_{\text{relax}} = 1$).
- _Specific Non-Claims and Caveats_
  - The $V_{\text{YIELD}} = 1$ vs $V_{\text{SNAP}} = 1$ distinction is a units/normalization-convention claim — load-bearing for correctly scoping amplitude in engine experiments; it is not a new physical result.
  - The numerical lattice-native values inherit $\alpha$ (e.g. $e = \sqrt{\alpha}$, $V_{\text{SNAP}} = 1/\sqrt{\alpha}$); they are $\alpha$-conditioned.
  - $L_{\text{cell}}$ and $C_{\text{cell}}$ lattice-native values "depend on $\mu_0$/$\varepsilon_0$ choice" — the table flags these as not fully fixed by the $\ell_{\text{node}} = m_e = c = \hbar = 1$ convention alone.
  - The caveat "always verify which normalization is active" is the operative warning; mis-reading the normalization mis-scopes whether a run is sub-yield or above-yield.

> **Leaf references:** [lattice-impedance-decomposition](./operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md).

### Quality
- confidence: 0.85
- depends-on:
  - clm-0ktpcn — Golden Torus α Derivation [supplies α, which sets V_YIELD=√α·V_SNAP=1 and the √α-conditioned native values]
- solidity: 0.63 (use as input only, don't build deeper) [= min(0.85, 0.63)]
- rationale: This is a units/normalization-convention claim and is locally airtight: with ℓ_node=m_e=c=ℏ=1, V_SNAP=m_e c²/e=1/√α≈11.7 and V_YIELD=√α·V_SNAP=1.0 follow by direct substitution, the 0.5·V_SNAP = 0.5/√α = 5.85-in-V_YIELD-units arithmetic checks, and the dimensional table is internally consistent. It correctly disclaims being a new physical result and flags the L_cell/C_cell entries as not fully fixed by the convention; a clean convention catalog of this completeness sits at the top of the band rather than at 0.9+ because two table rows are explicitly under-determined.
- strengthen-by:
  - Pin the L_cell/C_cell lattice-native values by stating the μ₀/ε₀ convention used, removing the two "depends on choice" rows.
  - Cross-check the √(2α) Regime I/II boundary (A=0.121 in V_SNAP units, 1.42 in V_YIELD units) against the Axiom-4 saturation kernel definition to confirm the boundary placement.
---

## Cubic-Symmetry Suppression of Lorentz-Violating Signatures (Emergent Lorentz Invariance from K4)
<!-- id: clm-yr6tu4 -->

The K4 lattice has a preferred rest frame (identified empirically with the CMB rest frame to high precision), yet strict Lorentz invariance at observable wavelengths is consistent with current cavity-comparison bounds. These two facts are not in tension: the diamond-cubic ($Fd\bar{3}m$) symmetry of the K4-bipartite tetrahedral lattice suppresses observable anisotropy at low momentum $q \ll \pi/\ell_{node}$ to $\delta_{aniso} \sim (q\ell_{node})^4$ — at optical wavelengths ($\lambda = 633$ nm), $\delta_{aniso} \approx 2.2 \times 10^{-22}$, two to three orders of magnitude below the tightest current cavity-comparison bound. **Strict Lorentz invariance at observable wavelengths is an EMERGENT consequence of K4 cubic symmetry, not an AVE axiom.** The framework derives Lorentz invariance at observable scales, predicts the precise momentum scale at which it must break down ($q \sim \pi/\ell_{node}$, i.e. Trans-Planckian wavelengths), and names the empirical signature (GRB dispersion at $\lambda \to \ell_{node}$). The leaf classifies every preferred-frame / Sagnac test in the AVE divergence matrix by probe scale (rotor-local Sagnac, bulk preferred-frame, scalar gradient, Trans-Planckian, Regime-IV planetary-mass-saturated drag) under this synthesis.

- _Specific Claims_
  - The K4 lattice has a preferred rest frame, identified empirically with the CMB rest frame per AVE-QED Q-G24; Earth moves at $\sim 370$ km/s through it, measurable as the CMB dipole anisotropy.
  - The first anisotropic invariant for the cubic point group is QUARTIC: $q^0$ and $q^2$ corrections are isotropic; $q^4$ is the first order at which $q_x^4 + q_y^4 + q_z^4$ differs from $|q|^4$. Anisotropic corrections are therefore suppressed by $(q\ell_{node})^4$, not the naive $(q\ell_{node})^2$ a non-cubic lattice would give.
  - At optical scale ($\lambda = 633$ nm, $q\ell_{node} \approx 3.86 \times 10^{-6}$), $\delta_{aniso} \sim 2.2 \times 10^{-22}$ — 2-3 OOM below current cavity bounds ($\sim 10^{-19}$ to $10^{-20}$ per SME operator, Nagel 2015 + Sanner 2019). Consistency with existing null Lorentz-violation results is BY DERIVATION.
  - At microwave scale (30 GHz), $\delta_{aniso} \sim 2.5 \times 10^{-34}$.
  - At Trans-Planckian probe wavelengths ($q \sim \pi/\ell_{node}$), the cubic symmetry no longer averages; preferred-frame effects ARE observable. ~~GRB dispersion at $\lambda \to \ell_{node}$ is the surviving forward-prediction.~~ **🔴 Weak-C 2026-06-15, Rule 12 (bullet above PRESERVED):** the lattice-resolution $(q\ell_{node})^2$ breakdown applies to **matter carriers** (node-locked), NOT the free continuum photon — which has no zone-edge dispersion → AVE predicts the GRB NULL (corroborated by GeV–TeV GRB). The surviving *photon* forward-prediction is the $(q\ell_{node})^4$ optical birefringence ($\delta \approx 2.2 \times 10^{-22}$, bullet above), NOT GRB dispersion. See rationale walk-back below + `preferred-frame-and-emergent-lorentz.md` §4.1.
  - The synthesis classifies the divergence-test matrix by probe scale: A2 (rotor-local, NOT a preferred-frame probe) — predictions unchanged; C17 (bulk preferred-frame, optical wavelength) — retired to corroborative-null; C18 (scalar gradient, AVE-$n(r)$ = GR-$n(r)$) — retired to corroborative-null; C7 GRB dispersion — ~~surviving Trans-Planckian probe~~ **🔴 corroborated NULL (weak-C 2026-06-15): no continuum-photon dispersion; (qℓ)² is a matter-carrier property; surviving *photon* test is the (qℓ)⁴ birefringence**; Earth-flyby — distinct fifth category (Regime-IV planetary-mass-saturated LC drag).
- _Specific Non-Claims and Caveats_
  - "Identification of K4 lattice rest frame with the CMB rest frame" is **empirical**, not derived. Vacuum crystallization at recombination defines the CMB as the universe's rest frame; the K4 lattice was cast at that boundary. This is NOT a Maxwell-Lorentz ether (which was undetectable in principle); AVE's preferred frame IS detectable — the CMB dipole is the detection.
  - The $(q\ell_{node})^4$ suppression is at LOW MOMENTUM only ($q \ll \pi/\ell_{node}$). It does NOT apply at lattice resolution; it does NOT apply to scalar-gradient probes ($q^0$ order survives cubic symmetry); it does NOT apply to local rotor-induced perturbations of a moving substrate.
  - The plumber-physical "diamond crystal not visibly birefringent at optical wavelength" analogy is a pedagogical translation, not an independent derivation. The substrate analogy carries the same mechanism but does not constitute additional evidence.
  - The numerical bounds compared (Nagel 2015 *Nat Commun* 6:8174; Sanner 2019 *Nature* 567:204) are cited as the tightest current cavity-comparison bounds; tighter future cavity tests could narrow but not close the AVE-prediction gap (the gap is 2-3 OOM).

> **Leaf references:** [preferred-frame-and-emergent-lorentz](./dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md), [sagnac-parallax](../vol4/falsification/ch11-experimental-bench-falsification/sagnac-parallax.md), [advanced-protocols](../vol4/falsification/ch11-experimental-bench/advanced-protocols.md).

### Quality
- confidence: 0.78
- depends-on:
  - clm-9gh0a1 — Implosion Paradox to Micropolar Vacuum [supplies the K4 cubic substrate whose point-group symmetry drives the suppression]
- solidity: 0.78 (ok to build on, see caveats) [= min(0.78, 0.85)]
- rationale: The load-bearing step is standard crystallographic group theory — the first anisotropic invariant of the cubic point group is the quartic q_x^4+q_y^4+q_z^4, so observable anisotropy is suppressed by (qℓ_node)^4 not (qℓ_node)^2 — and the numerical evaluation δ_aniso ≈ 2.2×10^-22 at 633 nm is a clean, checkable calculation 2-3 OOM below the cited Nagel/Sanner cavity bounds. The CMB=K4-frame identification is explicitly flagged empirical (not derived), and the framing as emergent-not-axiomatic Lorentz invariance with a named Trans-Planckian breakdown signature is well-bounded; minor caveat is the loose phrasing of the q^2 isotropy argument, but the conclusion is correct. **🔴 WEAK-C PARTIAL/KEEP-BOTH WALK-BACK (2026-06-15, Rule 12 — rationale above PRESERVED; gate `wejkhvnfb`, Grant-confirmed 2026-06-14; prereg at repo-root `research/2026-06-15_weak-c-photon-continuum_prereg.md`):** this claim carried TWO horns under the "Trans-Planckian breakdown signature" heading. (1) **RETRACT the (qℓ_node)² GRB-dispersion horn** — the framing of "GRB dispersion at λ→ℓ_node" as AVE's *surviving forward prediction* is walked back. Under weak-C the free photon is the continuum EM field (LC-ladder long-wavelength regime, sub-saturation, Z₀-matched, unlocked) → no zone-edge (qℓ_node)² dispersion; AVE predicts the GRB NULL (corroborated by GeV–TeV nulls, GRB090510 31 GeV / LHAASO 221009A 13 TeV). The (qℓ_node)² zone-edge bending is a lattice-mode property that survives for *matter* carriers (node-locked), not the continuum photon. (2) **KEEP the (qℓ_node)⁴ optical birefringence horn** — δ_aniso ≈ 2.2×10⁻²² at 633 nm (the crystallographic-group-theory result above) is the *surviving forward prediction*; the continuum photon retains it by inheriting the lattice's cubic symmetry. It is distinct from the (qℓ_node)² GRB dispersion and is NOT falsified. Solidity UNCHANGED at 0.78 (the load-bearing (qℓ)⁴ group-theory step is untouched; the walk-back removes the over-reaching (qℓ)² GRB-prediction horn, not the (qℓ)⁴ content). Full reconciliation at `preferred-frame-and-emergent-lorentz.md` §4.1. Honest-scope (A47 v11b): no-dispersion is regime-grounded + empirically-corroborated, NOT a derived theorem.
- strengthen-by:
  - Tighten the q^2-isotropy argument (the "cube root of |q|^2" phrasing) into a clean statement that the cubic point group has no rank-2 anisotropic invariant, with the quartic as the first survivor
  - Derive the coefficient in front of (qℓ_node)^4 from the K4 dispersion relation rather than treating the suppression as order-of-magnitude only
  - Carry the comparison against the SME operator basis explicitly (the bound is per-operator; show which SME coefficients the K4 quartic maps onto)
  - ~~Quantify the GRB-dispersion forward prediction at λ→ℓ_node so the surviving Trans-Planckian signature has a numerical target~~ **🔴 SUPERSEDED (weak-C 2026-06-15, Rule 12):** the (qℓ_node)² GRB-dispersion horn is RETRACTED (see rationale walk-back above) — under weak-C the continuum photon has no zone-edge dispersion, so there is no GRB forward signature to quantify; AVE predicts the GRB NULL. The surviving *photon* forward prediction to quantify is the (qℓ_node)⁴ optical birefringence (δ ≈ 2.2×10⁻²²), already numerically targeted in §2.
---

## Substrate-Equilibrium Velocity Prediction $v_{\text{substrate}} = \alpha c / (2\pi)$
<!-- id: clm-ce8dg1 -->

For LSR-class local-region kinematics (Sun + nearby thin-disk stars) through the K4 rest frame, AVE predicts a zero-parameter substrate-equilibrium velocity $v_{\text{substrate}} = \alpha c / (2\pi) \approx 348.18$ km/s. Derived from the Schwinger anomalous-moment substrate-rate $\nu_{slew} = a_e \cdot \omega_{Compton}$ ($a_e = \alpha/(2\pi)$ acting on the *angular* Compton clock $\omega_{Compton} = c/\ell_{node}$; equivalently $\alpha\,\nu_{Compton}$), then $v_{\text{substrate}} = \nu_{slew} \cdot \ell_{node} = \alpha c/(2\pi)$; the same $\nu_{slew}$ independently reproduces the DAMA quantum $E_{slew} = h\nu_{slew} = \alpha m_e c^2 = 3.728$ keV. Structurally identical to the canonical MOND Hoop-Stress-2π projection ($a_0 = c H_\infty / (2\pi)$). Empirical anchor: Gaia DR3 thin-disk subset (N=11,690 stars, $|v_{LSR}|<30$) clusters at 375.2 km/s with σ=11.2 km/s; AVE prediction sits at 4.08%ile (lower envelope). The directional alignment of this LSR-class bulk velocity with the CMB-dipole direction (~2.75° offset) is the cleanest AVE-distinct signature and remains a positive across three walk-back iterations; the magnitude prediction is approximate (9% gap reflects LSR participation in CMB-dipole-aligned cosmic flow). Scope narrows to LSR-class ONLY per Globular Cluster test 2026-05-17 night Outcome III: GC population (N=165) median $|v_{CMB}|$ = 563.88 km/s does NOT cluster near $\alpha c/(2\pi)$, falsifying any universal "decoupled-population" floor interpretation.

- _Specific Claims_
  - Zero-parameter derivation: $v_{\text{substrate}} = \alpha c / (2\pi) \approx 348.18$ km/s from $\nu_{slew} = a_e \cdot \omega_{Compton}$ ($a_e = \alpha/(2\pi)$ Schwinger anomalous moment on the angular Compton clock $\omega_{Compton} = c/\ell_{node} = m_e c^2/\hbar$, with $\ell_{node} = \hbar/(m_e c)$), then $v = \nu_{slew}\cdot\ell_{node}$. The chain closes to $\alpha c/(2\pi)$ and the same $\nu_{slew}$ independently gives the DAMA line $E_{slew} = h\nu_{slew} = \alpha m_e c^2 = 3.728$ keV.
  - Scope is LSR-class local-region kinematics ONLY (Sun + nearby thin-disk stars); does NOT extend to GC-class or halo populations per the 2026-05-17 night GC test Outcome III walk-back.
  - Hoop Stress 2π projection unifies the substrate-scale prediction with cosmic-scale MOND $a_0 = c H_\infty / (2\pi)$; both follow the same substrate-bulk-drift-projected-through-2π-Hoop-Stress pattern.
  - The 2π in the substrate-scale prediction is RIGOROUSLY EXACT at substrate scale: the electron $0_1$ unknot's ideal ropelength is exactly $2\pi \times \ell_{node}$ per Cantarella-Kusner-Sullivan 2002 knot-theory topological invariant, and Hoop Stress integration around this loop gives exact $T = F_r/(2\pi)$.
  - Empirical match (Gaia DR3 magnitude statistics): 29,466 nearby thin-disk G/K dwarfs cluster at 379.5 km/s median (σ=25.7); thin-disk subset ($|v_{LSR}|<30$, N=11,690) clusters tightly at 375.2 km/s with σ=11.2 km/s — narrower than expected from random galactic kinematics (~σ=47).
  - Directional structure: Gaia DR3 cluster mean direction agrees with CMB-dipole to 2.75° (consistency check per `ave-discrimination-check`, not independent AVE evidence — both AVE-with-K4=CMB and SM-with-CMB-rest-as-baseline predict alignment); 133.71° anti-aligned with galactic rotation (rules out galactic-dynamics interpretation); cluster tightness σ=11 km/s and anti-alignment-with-galactic-rotation ARE substantive AVE-distinct signatures.
- _Specific Non-Claims and Caveats_
  - The magnitude prediction is APPROXIMATE at stellar scale: 9% gap between AVE prediction (348 km/s) and Gaia thin-disk cluster center (375 km/s). The gap reflects LSR participation in CMB-dipole-aligned cosmic flow (Local Group → Great Attractor), NOT local-disk-specific systematics, NOT a universal "decoupled-population" floor.
  - The FLOOR interpretation (αc/(2π) as the population FLOOR with additional dynamics driving cluster center above) was FALSIFIED 2026-05-17 late evening via the Toomre-stratified halo test: halo populations have INCREASING $|v_{CMB}|$ with peculiar dispersion, OPPOSITE of what a floor interpretation predicts.
  - Scope-narrowing to LSR-class only is canonical per Globular Cluster test Outcome III (2026-05-17 night, N=165, Baumgardt+Vasiliev 2021): GC median $|v_{CMB}|$ = 563.88 km/s matches √(543² + 150²) cosmic-flow + GC-orbital-velocity quadrature to <1%, far from $\alpha c/(2\pi)$ and very close to Local Group cosmic-flow scale.
  - The directional 2.75° CMB-dipole alignment was DEMOTED from STRONG POSITIVE to CONSISTENCY CHECK per `ave-discrimination-check` audit: alignment + anti-alignment-with-galactic-rotation are NOT independent AVE evidence — both follow from K4=CMB identification (Q-G24) + basic astronomy of LSR motion through CMB + basic geometry (CMB-dipole + galactic-rotation directions are ~131° apart). Substantive AVE-distinct content remains: (i) magnitude approximate match; (ii) cluster tightness σ=11 km/s.
  - The cosmic-scale 2π rigor remains OPEN: an earlier version of the leaf asserted "cosmic-scale 2π similarly exact via de Sitter horizon 3-sphere great-circle integration"; external reviewer correctly caught this elides a category distinction (unknot Ropelength is a knot-theory topological invariant; great-circle = 2π is basic Euclidean geometry). Per `ave-independence-check` retroactive: only 2 INDEPENDENT instances of the motif (cosmic + substrate); $v_{\text{substrate}}$ is derived from $\nu_{slew} \times \ell_{node}$; $E_{slew}$ has 2π cancel via $h = 2\pi\hbar$ identity.
  - The (1 + 1/(4π)) geometric correction (matches cluster center to 0.5 km/s) was DOWNGRADED to "would-require-new-canonical-derivation" pending Q-G47 Path B+ K4-discrete + Cosserat-continuum decomposition work that found NO continuum correction for the soft-shear E-irrep eigenvalue.
  - The framing iterated through THREE walk-backs (Sun-22-km/s peculiar → LSR-bulk-population, FLOOR interpretation considered → FLOOR FALSIFIED, scope GC-test → scope narrows to LSR-class only). The current LSR-class-bulk-motion framing is the post-3-walk-back current canonical reading.

> **Leaf references:** [preferred-frame-and-emergent-lorentz](./dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md).

### Quality
- confidence: 0.50
- depends-on:
  - clm-yr6tu4 — Cubic-Symmetry Suppression / Emergent Lorentz [supplies the K4=CMB preferred-frame identification the prediction is referenced to]
  - clm-0ktpcn — Golden Torus α Derivation [α enters v = αc/(2π) linearly]
- solidity: 0.50 (use as input only, don't build deeper) [= min(0.50, 0.63)]
- rationale: The derivation chain now closes (2026-05-23 fix): the Schwinger factor a_e = α/(2π) acts on the *angular* Compton clock ω_Compton = c/ℓ_node, so ν_slew = a_e·ω_Compton = αc/(2πℓ_node) and v = ν_slew·ℓ_node = αc/(2π) — and the same ν_slew independently reproduces the DAMA line E = hν_slew = α m_e c² = 3.728 keV (the prior αc/(4π²) discrepancy was a ν-vs-ω double-count of 2π, now corrected; the leaf's consumers already used the angular form). Remaining local-rigor limiters cap confidence below "derived end-to-end": the 2π's physical origin still rests on importing the classical Hoop-Stress T = F_r/(2π) projection + identifying the unknot Ropelength = 2π as the loop circumference (not derived from AVE micropolar dynamics); the headline magnitude is approximate (~9% off, 348 vs 375 km/s) with the gap qualitatively attributed to cosmic flow; scope narrowed through walk-backs to LSR-class only; the directional alignment was demoted to a consistency check. Solidity remains dep-gated well below confidence — now by clm-0ktpcn (Golden-Torus α derivation, the genuine linear-α input), so the real lever for this claim is the strength of the α derivation, not anything local to the velocity chain. (The former clm-m3z5ux/MOND-a_0 depends-on edge was removed 2026-05-23: it is a *parallel* Hoop-Stress-2π motif instance — a_0 takes ε=H_∞, v takes ε=α — not a derivation input, so it was spuriously gating; the parallel survives in prose, not as an edge.)
- strengthen-by:
  - Derive the Hoop-Stress T = F_r/(2π) projection onto the electron unknot from AVE micropolar dynamics rather than importing classical continuum mechanics + invoking Ropelength as the loop circumference (this is now the load-bearing local-rigor gap, the 2π-closure having been resolved 2026-05-23)
  - Close the 9% magnitude gap from first principles (cosmic-flow contribution is currently a qualitative attribution) or state the predicted LSR bulk velocity with an error budget
  - Establish a genuinely AVE-distinct directional or magnitude signature not shared by SM-with-CMB-rest-baseline (current alignment is a consistency check by the leaf's own audit)
