# AVE-Native Terminology Canonical Translation Table

**Purpose.** Single source of truth for translating common physics terms (SM / QFT / CondMat / cosmology / standard EE) into their AVE-native equivalents. Prevents framework leakage: terms like "Kibble-Zurek", "Meissner effect", "Hopfion" import their parent framework's conceptual baggage if used unreflectively in AVE derivations.

**Last comprehensive sweep:** 2026-05-14. **Upstream canonical:** AVE-QED `manuscript/vol_qed_replacement/appendices/G_substrate_vocabulary.tex` (App G) + `docs/glossary.md` §5m. All entries below have been audited for compatibility with App G's substrate-native vocabulary. Where this file uses older language ("vacuum" instead of "substrate", "field" instead of "state"), the projection is harmless if the row's mapping target is unambiguous; the substrate-native default is documented in §0 below.

**Rules of use:**
1. In a derivation, use the AVE-native term throughout.
2. When citing an SM/QFT analog, use "[AVE term] (analogous to [SM term])" — only in comparison paragraphs, never in the derivation chain.
3. Never import functional forms from the SM/QFT concept (e.g., do not assume Kibble-Zurek scaling until the AVE-native derivation has produced its own scaling; only compare at the end).
4. When a mapping is missing, STOP — either find the AVE-native equivalent or flag to Grant for adjudication. Do not paper over.
5. **Default to substrate-native vocabulary** (per §0 / App G). Name the projection (EE / ME) explicitly when the math is committed to an observation frame.

**Marker conventions:**
- **(CREEPER)** — a phrase that recurs in prior agents' framing despite being incorrect; treat as a red flag when seen.
- **(IMPORTED)** — a result/concept currently used in AVE that is not yet axiom-derived; candidate for derivation work.
- **(SUBSTRATE-NATIVE)** — term carries no projection-frame baggage; usable in any context.

---

## §0 — Substrate-native vocabulary (canonical, 2026-05-14, AVE-QED App G)

The substrate is a wave-supporting topological network. Every observable physical quantity is a relational integral over a boundary or between boundaries (substrate-observability rule). No quantity is intrinsic to "matter"; every quantity is Machian. **Default to these terms when writing about substrate dynamics without committing to an observation-frame projection.**

| Substrate-native | EE projection | ME projection | Use when |
|---|---|---|---|
| **Substrate** | (vacuum / EM field) | (spacetime / elastic medium) | Default. Reserve EE/ME for when probe is specific. |
| **Node** | (circuit node) | (lattice point) | Default. The K4 4-port tetrahedral active site. |
| **Bond** | Transmission line | Spring | Default. Inter-node connection carrying state. |
| **State** | Voltage / V_inc | Force / displacement | Default. Oriented propagating quantity on a bond. |
| **Propagation** | Current flow | (no clean analog) | Default. How state evolves between nodes. |
| **Impedance** $Z$ | already universal | already universal | Use freely. |
| **Saturation kernel** $S(A) = \sqrt{1-A^2}$ | Schwinger / breakdown | yield / rupture | Use freely; Axiom 4 canonical. |
| **Boundary** | (charged surface) | (yield surface) | Default. Localized region where $\Gamma \to -1$. NOT "particle" or "horizon" — those are projections. |
| **Envelope** | (wavefunction support) | (zone of influence) | Default. What the substrate **actually sees**, per substrate-observability rule. |
| **Linking** $\mathcal{Q}$ | charge $Q$ | (no clean analog) | Use universal substrate; project to $Q$ for standard physics. Integer per boundary. |
| **Winding** $\mathcal{J}$ | spin $J$ / mag.~moment | rotation | Use universal substrate; project for QFT / ME. Half-integer per SU(2) double-cover. |
| **Integrated strain integral** $\mathcal{M}$ | inductance $L$ / inertia (kg) | inertia | Use universal substrate. The mass-equivalent boundary observable. |
| **Strain** $A$ | voltage gradient | already universal | Default: substrate. Local deviation from equilibrium. |
| **Machian** | (no clean analog) | (no clean analog) | Use freely. A boundary's relational property w.r.t. the rest of the substrate. |
| **Kernel** | (no clean analog) | (no clean analog) | Use freely; Axiom 4 canonical operator. |

### Three substrate invariants $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ (Grant-locked 2026-05-14 evening, AVE-QED Q1 closure)

| Symbol | Canonical name | Operational definition |
|---|---|---|
| $\mathcal{M}$ | Integrated strain integral | $\int_\Omega (n(\mathbf{r}) - 1)\,dV$; mass quantum $\hbar/(\ell_{\text{node}} c)$ |
| $\mathcal{Q}$ | Boundary linking number | $\mathrm{Link}(\partial\Omega, \mathbf{F}_{\text{substrate}}) \in \mathbb{Z}$ |
| $\mathcal{J}$ | Boundary winding number | $\mathrm{Wind}(\partial\Omega)$; half-integer per SU(2) double-cover |

**These are the only three integrated invariants the substrate observes at any local $\Gamma = -1$ boundary.** No-hair theorem applied at every scale — same mechanism at BH horizon and electron horn-torus tube wall (Vol 3 Ch 2:43; App F multi-scale Machian network).

### Substrate-observability rule (canonical, doc 109 §13 + AVE-QED App G §3)

The substrate observes a boundary, not its interior. For any localized region $\Omega \subset \mathcal{M}_A$ enclosed by a $\Gamma = -1$ saturation surface $\partial\Omega$:

1. The boundary is an impedance-mismatch surface; substrate waves are totally reflected (outside) or totally trapped (inside).
2. The interior is causally / impedance-disconnected from the substrate. Only the three integrated observables ($\mathcal{M}, \mathcal{Q}, \mathcal{J}$) are visible externally.
3. The interior structure (topology, eigenmode wavelength, microrotation profile) is invisible to the substrate.
4. **Same mechanism at all scales** (App F): Schwarzschild horizon $r_s = 2GM/c^2$ is structurally identical to horn-torus tube wall at $\ell_{\text{node}}/(2\pi)$.

**Operational consequence:** a substrate-native simulation does NOT need to resolve interior eigenmode wavelengths. Only the boundary envelope plus its three integrated observables need to be resolvable on the lattice. The pre-2026-05-14 framing (forcing multi-cell propagating-eigenmode tests on what is canonically a single-cell bounded boundary object) was a misframing. Doc 92 Nyquist wall ($k = 6.36/\ell_{\text{node}}$) measured an interior observable that is not substrate-visible.

### Cross-references

- **Upstream canonical:** AVE-QED `manuscript/vol_qed_replacement/appendices/G_substrate_vocabulary.tex` (full 7-section appendix)
- **Upstream glossary:** AVE-QED `docs/glossary.md` §5m
- **Grant adjudication:** AVE-Core `research/L3_electron_soliton/109_elastic_substrate_finite_strain_investigation.md` §13 (boundary-envelope reformulation, Grant-confirmed canonical)
- **Multi-scale extension:** AVE-QED `manuscript/vol_qed_replacement/appendices/F_local_machian_network.tex` (electron / nucleus / atom / helio / BH / cosmic boundaries)
- **Three substrate invariants matrix:** AVE-QED `docs/analysis/2026-05-14_three_substrate_invariants_matrix.md`

---

## Foundational scope / framing

| Common term | AVE-native term | Justification | Source(s) |
|---|---|---|---|
| "Aether" | "Vacuum" / "Applied Vacuum Engineering substrate" | User directive — AVE = Applied Vacuum Engineering, never "Aether" | `MEMORY.md` user_ave_terminology |
| Phase transition / symmetry breaking | V_yield crossing (Bingham-plastic transition: solid η₀ → slipstream η=0) | Universal mechanism; not order-parameter-driven | [Vol 4 Ch 1:189-203](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L189) |
| Mass / inertia | Inductive resistance (Lenz-law back-EMF from diverging L_eff) | Inertia derives from impedance, not particle property | [vol2 newtonian-inertia-as-lenz](../../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/newtonian-inertia-as-lenz.md) |
| Newton's 3rd law / reaction momentum | Dark-wake back-propagation via K4 mutual-inductance | Reaction is τ_zx strain wave | [49_ §1.1-1.2](../L3_electron_soliton/49_dark_wake_bemf_foc_synthesis.md) |
| Gravity / G / curvature | Localized vacuum impedance polarization → refractive index n(r) = 1+2GM/(c²r) | No spacetime curvature; impedance gradient | [vol3 refractive-index-of-gravity](../../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md) |
| Little g (gravitational acceleration) | Local strain field, g = -c²·∇n(r) = (1/ρ)·∇·σ from Cosserat stress | Mechanical not geometric | Derived from refractive-index + Cosserat stress |
| Big G (Newton constant) | Lattice's macro-scale self-inductance/tension (integrated Machian) | XI_MACHIAN | [constants.py:379](../../src/ave/core/constants.py#L379) |
| Time (rate) | τ_local = n(r) · τ_unstrained — local clock rate from lattice strain | Twice the strain → half the refresh rate | [66_ §17.1](../L3_electron_soliton/66_single_electron_first_pivot.md) |

## Saturation, regimes, impedance

| Common term | AVE-native term | Justification | Source(s) |
|---|---|---|---|
| Impedance Z | Op1 (primary operator) | Universal-operator basis | [universal_operators.py:41-54](../../src/ave/core/universal_operators.py#L41) |
| Saturation kernel S | Op2 (Ax4) | Universal-operator basis | [universal_operators.py:57-85](../../src/ave/core/universal_operators.py#L57) |
| Reflection coefficient Γ | Op3 | Universal-operator basis | [universal_operators.py:88-103](../../src/ave/core/universal_operators.py#L88) |
| Dynamic impedance Z_eff | Op14 = Z_0/√S, fast-limit of memristive dynamics | Memristive identity | [k4_tlm.py:229-260](../../src/ave/core/k4_tlm.py#L229) |
| Saturation A² ⟺ density | Same scalar field, two framings: A² = local field-energy density; S = √(1−A²) = "free capacity" of unfilled lattice | Cosmological matter = low-density slipstream pockets | [66_ §17.2](../L3_electron_soliton/66_single_electron_first_pivot.md) |
| Critical slowing down / relaxation time | τ_relax = ℓ_node/c (Ax1 + Ax3) | Native | [Vol 4 Ch 1:214](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L214) |
| Memristor (Chua) | Vacuum's thixotropic hysteresis: M(q) = dΦ/dq | Native | [Vol 4 Ch 1 §3.3](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L209-L228) |
| Dielectric breakdown / TVS | V_yield Bingham-plastic transition (solid η₀ → slipstream η=0) | Native | [Vol 4 Ch 1:189-207](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L189) |
| Schwinger pair production | C1∧C2 gate firing at V_yield saturation + autoresonant lock | Native (Phase 5 gate) | [54_ §7](../L3_electron_soliton/54_pair_production_axiom_derivation.md) |

## Cross-sector dynamics (creepers — watch carefully)

| Common term | AVE-native term | Justification | Source(s) |
|---|---|---|---|
| "K4→Cosserat coupling" / "cross-sector coupling" / "multiplicative bilinear coupling term" **(CREEPER)** | One LC tank per K4 node with two orthogonal saturation pathways — magnetic (κ²/ω_yield²) and electric (ε²/ε_yield² + V²/V_SNAP²) — sharing the Pythagorean A²_total = A²_μ + A²_ε. NOT separate sectors. κ_chiral = 1.2α is topologically derived from parallel-channel impedance combination, not a coupling constant. | Persistent prior-agent miswording; correction surfaces repeatedly | [54_ §6](../L3_electron_soliton/54_pair_production_axiom_derivation.md); [20_ Sub-Theorem 3.1.1](../L3_electron_soliton/20_chirality_projection_sub_theorem.md); [66_ §7](../L3_electron_soliton/66_single_electron_first_pivot.md) |
| "Cross-sector PLL" **(CREEPER)** | Single-tank PLL tracking combined softening Ω_node = ω₀·(1 − A²_total)^(1/4). Q = 1/α and δ_lock = ω₀·α apply to the shared node tank at its TIR saturation boundary. No inter-sector synchronization. | Persistent miswording | [27_](../L3_electron_soliton/27_step6_phase_space_Q.md); [66_ §7](../L3_electron_soliton/66_single_electron_first_pivot.md) |
| "Two projections of one tank" (re K4↔Cosserat) **(CREEPER, retracted)** | Two **complementary** LC tanks (K4 V↔Φ_link bond tank vs Cosserat ω↔θ rotational tank) coupled via L_c. Doc 66_ §14.1 retracted the "two projections" framing. | Active correction zone | [66_ §14.1](../L3_electron_soliton/66_single_electron_first_pivot.md) |
| "Hessian-of-W" / "stationary point of W" / "W-minimum basin" / "energy minimum" for vacuum bound states **(SECTOR-DEPENDENT — REVISED 2026-04-26)** | **K4 sector:** Hessian-of-W is INCORRECT. The K4 substrate runs scatter+connect wave propagation; bound-state operator is the K4-TLM scatter+connect transmission eigenvalue problem `T·ψ = exp(i·ω·dt)·ψ` with `T = C_op3 · S(z_local)`, sparse complex non-Hermitian. Continuum graph-Laplacian approximations DO NOT lift to discrete K4-TLM at finite N (A37 catastrophic-error finding). **Cosserat sector:** Hessian-of-W IS correct. The (u, ω) LC tank's small-oscillation linearization gives a real-symmetric sparse generalized eigenvalue problem `K_cos · ψ = ω² · M_cos · ψ`. The original "creeper" framing (universal Hessian-of-W rejection) was over-broad; refined per doc 73_ §3 + §6. Four reframes of R7.1 in one session (basin-audit → multi-seed Hessian-on-joint → continuum Helmholtz → K4-TLM scatter+connect + Cosserat Hessian + Op14 cross-coupling) trace through this refinement. **Operator construction must respect sectoral structure — see A-005 for the principle.** | Sectoral nuance — operator choice depends on which sector's physics is being captured | [doc 73_ §3 + §6 + §1.1 reframe table](../L3_electron_soliton/73_discrete_k4_tlm_lctank_operator.md#L11); [doc 72_ §1 + §4.4:L11-L191](../L3_electron_soliton/72_vacuum_impedance_design_space.md#L11) (original framing) |
| "Joint operator over (V_inc, V_ref, u, ω)" or "single Hessian on the full state vector" **(CREEPER)** | **Block-structured operator** with K4-block (scatter+connect transmission eigenvalue, sparse complex) and Cosserat-block (LC-tank Hessian-of-W, sparse real-symmetric), coupled via Op14 z-modulation cross-block at the seed configuration. The two sectors implement structurally different physics — operator construction must respect that. A36 finding: operator-over-joint-state misses sectoral structure. | Persistent miswording in operator framings | [doc 73_ §1.1 + §4 + A-005](../L3_electron_soliton/73_discrete_k4_tlm_lctank_operator.md#L13) |
| "Frequency-PASS alone" as bound-state criterion **(METHODOLOGY LESSON, 2026-04-26)** | **Frequency PASS is necessary but not sufficient** at high N, because lattice mode density grows with N — finding an eigenvalue near the target frequency may be hitting a bulk mode from a denser spectrum, NOT a (2,3) localized bound state. Topology check (shell fraction, c_eigvec) is required. Doc 74_ §7 third-flip: N=64 V-block GT_corpus passed frequency PASS at gap 0.45% < α/√2 tolerance, but topology check FALSIFIED it as BULK mode (shell fraction 1.13%, not (2,3) localized). Future bound-state predicates must include frequency + topology jointly. | New methodology constraint surfaced empirically | [doc 74_ §7](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L231) |
| "Mode III-orbit" / "Mode III-spatial" / "Mode III-both" **(adjudication-class distinctions, 2026-04-26)** | **Mode III** = pre-registered "no bound state detected" verdict. **Mode III-orbit** = nonlinear time-domain orbit hunt verdict (E-060 Move 5: persistence threshold failed); the empirical signal can still be qualitatively positive (e.g., sub-corpus self-stable plateau) — separate framing axis from pre-reg per A47. **Mode III-spatial** = bond-cluster spatial-envelope verdict (E-008 Test B v2/v3: rel_std below threshold; bond cluster uniform, no (2,3) topology). **Mode III-both** = dual-criterion verdict where BOTH frequency and topology fail (E-059 Test A: gap 1.25% > α + c_via_Op10 = 0). All three are sub-classes of strict Mode III adjudication; subclass labels disambiguate which test class produced the verdict. | Adjudication taxonomy emerging from R7+R8 arc | [doc 74_ §10 + §11.3](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L416); [A-007 (A47 pre-reg-vs-narrative)](axiom_derivation_status.md) |
| "Corpus Golden Torus" (R = φ/2, r = (φ−1)/2 in canonical units; R_anchor=10, r=R/φ²≈3.82 at engine N=32; peak \|ω\|=0.3π) **(EMPIRICALLY FALSIFIED at engine PARAMETERS, 2026-04-26)** | **Geometry where corpus claims the (2,3) electron lives** per Vol 1 Ch 8. Round 7+8 empirical work (7 tests across V/Cos/pair/spatial sectors) returned Mode III at corpus GT — the engine does NOT host the (2,3) bound state at these specific parameters. Round 8 Move 5 found a **self-stable sub-corpus (2,3) orbit** at peak \|ω\|=0.3044 (≈1/3 of corpus) which migrated AWAY from the corpus shell. Framework qualitatively right (electron IS a self-trapped (2,3) soliton); specific parameters wrong. Move 6 (E-062) tests whether the φ² RATIO survives at non-corpus absolute scale (Mode I-geometry → corpus ratio vindicated, recalibrate R_anchor; Mode II-geometry → ratio also wrong). | Major framework-level empirical finding; reframes corpus zero-parameter-closure claim | [A-006 canonical entry](axiom_derivation_status.md); [doc 74_ §9-§11](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L322); [E-057 manuscript reframe gated on Move 6](manuscript_pending.md) |
| "Cosserat mass-gap m_Cosserat = 2 vs Compton frequency ω_C = 1" **(SPIN-½ HALF-COVER IDENTIFICATION, 2026-04-27)** | NOT a mismatch — m_Cosserat = 2 is the medium's full-cover SO(3) twist rate; ω_C = 1 is the spin-½ projection (SU(2) → SO(3) is 2-to-1, so observable rate is half the underlying medium rate). Same Dirac-belt-trick / 720°-return-to-identity that gives R·r=1/4 per doc 03_ §4.3, propagated to the mass scale. Both correct, no surgery. **Test consequences:** Cos-block tests at σ = m_Cosserat² = 4 (medium structural mode), drives at ω = 2 to engage SO(3) directly. R7.1's σ=1 missed the structural mode — Mode III at σ=1 was at the wrong target. Engine at default G_c = I_ω = 1 is correctly tuned; no moduli surgery needed. | Resolves what looked like §6.1 catastrophic-error candidate without engine-side change | [A-008 RESOLVED canonical entry](axiom_derivation_status.md); doc 41 §T2 + §6 forward-flag; doc 03_ §4.3 |
| "Op14 saturation as local clock-rate modulation" **(METHODOLOGY CONSTRAINT, 2026-04-27 + clarification)** | Op14 `Z_eff(r) = Z_0/√S(r)` makes local wave speed `c_eff(r) = c·√(1−A²(r))` → local clock rate `ω_local(r) = ω_global·√(1−A²(r))`. SAME physics as gravitational n(r) refractive-index slowing (per E-015 + Vol 3 Ch 3) — saturation IS the lattice's intrinsic refractive-index source. At rupture boundary (A² → 1): local clock freezes. **CRITICAL CLARIFICATION: uniform SLOWING ≠ uniform DAMPING.** Op14 modulates clock rate REACTIVELY (energy redistributed in time, NOT dissipated). Three distinct regimes: (I/II/III symmetric saturation) uniform slowing, all waves see same c_eff, conservative; (III asymmetric S_μ ≠ S_ε per chiral polarization) polarization-selective slowing, creates Γ → -1 confinement walls, still conservative; (IV rupture A² → 1) actual dissipation per Vol 3 Ch 11 Ŝ entropy operator. "Lattice strain dampens energy uniformly" is WRONG outside Regime IV. **Methodology rule for eigsolve at uniform global σ:** must report eigvec localization vs A²_local(r) distribution at load-bearing sites; Mode III at uniform σ conflates "no mode at this frequency" with "no global mode because local saturation modulates ω_local across the seed." Static fixed point per Move 5+7+7b is saturation-frozen-clock at core (A²_core ≈ 0.95 → ω_local(core) ≈ 0.22·ω_global), NOT damped configuration. | New methodology constraint + slowing-vs-damping disambiguation | [A-010 canonical entry](axiom_derivation_status.md); [E-067 manuscript entry](manuscript_pending.md); [E-069 engine + tests scope](engine_pending.md); E-015 (gravity τ_local — same physics, different source) |
| "Basin" (re vacuum bound states) | Use freely for AVE-Protein / Ramachandran context (where it's appropriate). For VACUUM bound states, prefer **"S₁₁-min basin"** (concept §1.4 of doc 72_). The "W-minimum basin" framing is a CREEPER (see above row). | Cross-repo concept loan; OK with disambiguation | [doc 72_ §4.4:L187](../L3_electron_soliton/72_vacuum_impedance_design_space.md#L187) |
| "Smith chart for the vacuum" | Direct EE loan, well-grounded. **3D extension** (frequency × Γ_real × Γ_imag) is the AVE-native generalization. Use freely with explicit `Z₀ = √(μ₀/ε₀) ≈ 376.73 Ω` specified. 4D extension (over scale, via Vol 1 Ch 6 universal-operator scale invariance) flagged for later. | New canonical visualization | [doc 72_ §2 + §4.4:L68-L188](../L3_electron_soliton/72_vacuum_impedance_design_space.md#L68) |

## Topology / soliton structure

| Common term | AVE-native term | Justification | Source(s) |
|---|---|---|---|
| "Hopfion" with $(w_1, w_2)$ winding pair | (2,3) phase-space soliton characterized by **scalar c=3 Op10 invariant** (universal-operator basis) | AVE-native invariant is scalar crossing count, not a winding pair | [07_ §4.1](../L3_electron_soliton/07_universal_operator_invariants.md); [02_ §7.2](../L3_electron_soliton/02_lagrangian_derivation.md#L182) |
| "Spin-½ as imported QM" | Extended-unknot Finkelstein-Misner kink + numerically verified gyroscope-spinor isomorphism (10⁻⁸ deviation) | AVE-native classical-topology derivation | [vol2 spin-half-paradox](../../manuscript/ave-kb/vol2/appendices/app-b-paradoxes/spin-half-paradox.md); [vol2 spin-gyroscopic-isomorphism](../../manuscript/ave-kb/vol2/appendices/app-b-paradoxes/spin-gyroscopic-isomorphism.md); [`simulate_gyroscopic_spin.py`](../../src/scripts/vol_2_subatomic/simulate_gyroscopic_spin.py) |
| Real-space trefoil | **Real-space unknot** + phase-space (2,3) winding (Vol 1 Ch 8 prose says "Trefoil Knot $3_1$" — see ch08 editor handoff comment for F1/F2 fix-needed) | Doc 28_ phase-space synthesis | [28_](../L3_electron_soliton/28_two_node_electron_synthesis.md); [08_alpha_golden_torus.tex:1-56 handoff comment](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex) |
| Right-hand rule / handedness convention | K4 port vectors p₀=(+,+,+), p₁=(+,-,-), p₂=(-,+,-), p₃=(-,-,+) encode RH tetrahedral genesis. Mirror-image K4 = LH universe with identical physics | Native | [54_ §1:40-43](../L3_electron_soliton/54_pair_production_axiom_derivation.md); [66_ §3](../L3_electron_soliton/66_single_electron_first_pivot.md) |
| Achromatic lensing (selective) | Chirality selects matched mode (L/C invariant through asymmetric saturation) → that mode sees Z₀-preserved (achromatic, lossless); opposite-chirality excluded at Γ=−1 walls. Rest mass = energy trapped in matched standing wave | Cross-corpus result | [Vol 3 Ch 3:125-142](../../manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex#L125-L142); [54_ §6](../L3_electron_soliton/54_pair_production_axiom_derivation.md); [66_ §4](../L3_electron_soliton/66_single_electron_first_pivot.md) |

## Engine fields ↔ physical quantities

| Common term | AVE-native term | Justification | Source(s) |
|---|---|---|---|
| Three A²-contributing fields | **ε² (Cosserat strain) → electric / capacitive** ; **κ² (Cosserat curvature ∇ω) → magnetic / inductive** ; **V² (K4 port voltage) → pressure / stored potential**. A² sums these. S = √(1−A²) is the free-substrate density. Conjugate pairs (90° phase-locked in standing waves): K4 V_inc ↔ Φ_link ; Cosserat u ↔ u_dot ; Cosserat θ ↔ ω | Engine layout | [66_ §17.2.1](../L3_electron_soliton/66_single_electron_first_pivot.md); [cosserat_field_3d.py:245](../../src/ave/topological/cosserat_field_3d.py#L245); [54_ §6](../L3_electron_soliton/54_pair_production_axiom_derivation.md) |
| Φ_link (re "Kelvin topological-protection") | Φ_link is a derived flux observable in K4-TLM, NOT an independent dynamical state. Direct seeding leaves a value that doesn't couple to V_inc evolution; constancy is "nothing in the K4 dynamics is touching this slot," NOT physical persistence | A29 finding (Round 6) | [70_ §7.2](../L3_electron_soliton/70_phase5_resume_methodology.md#L174); [k4_tlm.py:391](../../src/ave/core/k4_tlm.py#L391) |

## Black hole / cosmology

| Common term | AVE-native term | Justification | Source(s) |
|---|---|---|---|
| Black hole (mirror vs absorber) | **Symmetric saturation** (μ and ε scale together) → Z=Z₀ invariant → Γ=0 (no reflection, EM enters); **asymmetric saturation** (electron, only μ) → Z→0 → Γ=-1 (mirror capsule wall). Inside BH: G_shear → 0, lattice topology destroyed (Regime IV rupture), EM dissipates thermally | Native | [Vol 3 Ch 21:114](../../manuscript/vol_3_macroscopic/chapters/21_black_hole_interior_regime_iv.tex#L114); [Vol 3 Ch 15:19-29](../../manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex#L19-L29) |
| BH information paradox | Regime IV rupture destroys crystallized-lattice topology; destroyed-lattice is thermal bath leaking info via Hawking radiation (residual elastic coupling through imperfect phase boundary). "Loss" vs "thermalization" not adjudicated | Native | [59_ §13](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md) |
| BH entropy | **Three distinct quantities**: Ŝ_geometric = A·log(2)/ℓ_node² (AVE-native Ch 11 op applied to A-B interface, \|Γ\|²=1/2) **vs** S_BH = A/(4ℓ_P²) (standard thermodynamic, GR-imported) **vs** hypothetical cell-count Boltzmann microstates (rejected). Ratio Ŝ/S_BH ~ 10⁻⁴⁴ is Machian dilution. Distinct physics, not in competition | Native (3-way distinction) | [62_ §10](../L3_electron_soliton/62_ruptured_plasma_bh_entropy_derivation.md) |
| Geometric/impedance entropy (AVE-native) | Ŝ = -k_B Σᵢ ln(1 − \|Γᵢ\|²) — wave-scattering irreversibility at impedance mismatches. Vol 3 Ch 11 EXPLICITLY REJECTS Boltzmann S = k_B ln(Ω) and Shannon info-theoretic entropy. Impedance-mechanical, not statistical | Native | [Vol 3 Ch 11:50-68](../../manuscript/vol_3_macroscopic/chapters/11_thermodynamics_and_entropy.tex#L50-L68) |
| First law of BH thermodynamics **(IMPORTED)** | Currently imported from standard GR; not axiom-derived in AVE. Hawking 1971 area theorem absent. Any S_BH derivation using T·dS = dE relies on this import. Candidate Ax5: derive first law from Ax1+Ax4 + rupture thermodynamics | Open derivation gap | [62_ Flag 62-A](../L3_electron_soliton/62_ruptured_plasma_bh_entropy_derivation.md) |
| Matter/antimatter | A/B sublattice partition at LATTICE scale (Ax1 bipartite K4; commit `9ecc2ca` injects LH on A, RH on B). **NOT applicable at cosmological scale** — BH interior is topology-destroyed plasma, not opposite-sublattice | Cosmological clarification | [59_ §8.4](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md) |
| Lattice genesis | Primordial crystallization from pre-geodesic plasma. Single seed sets chirality; subsequent crystallization inherits via coherent wavefront. Universe is one giant single-domain. B-matter lives in pre-genesis plasma or causally-disconnected seed-patches | Grant framing; Flag G | [59_ §5.4](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md) |
| Baryogenesis / Sakharov conditions | Lattice-genesis single-seed inheritance — no CP violation, baryon-number violation, or out-of-equilibrium conditions required | Native | [59_ §5.4](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md) |

## Other condensed-matter / EE imports

| Common term | AVE-native term | Justification | Source(s) |
|---|---|---|---|
| Back-EMF / Lenz's Law | Dark wake = back-propagating τ_zx strain in K4 lattice | Native | [49_ §1.1-1.2](../L3_electron_soliton/49_dark_wake_bemf_foc_synthesis.md) |
| Meissner-like flux expulsion | Γ→−1 TIR walls at asymmetric (S_μ, S_ε) saturation boundary | Native | [54_ §6](../L3_electron_soliton/54_pair_production_axiom_derivation.md) |
| Kibble-Zurek defect freezing | **BEMF-blocked topology unwinding** near saturation: diverging L_eff → diverging Lenz EMF → dω/dt blocked → topology can't relax during yield-crossing | Native (linear scaling for topological defect density; KZ-like only for chirality domain-wall density in fast-quench regime) | [59_ §5](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md) |
| Spin Seebeck effect | Thermal gradient drives chirality (h_local) current via memristive response at yield crossing | Native | [59_ §13](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md) |
| ∇·B = 0 | Kirchhoff's Current Law on the discrete lattice's flux graph (every node has flux in = flux out) | Native (Ampère-as-KVL is pedagogical gap, Flag 66-C) | [Vol 2 Ch 7:1316-1358](../../manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex#L1316-L1358) |
| PML (perfectly matched layer) | Radiation absorber at simulation boundary — one role only, not a gravity mechanism | Engine convention | [k4_tlm.py:174-190](../../src/ave/core/k4_tlm.py#L174) |
| "the electron" (as a single object at a single scale) | Soliton + lattice-wake dual view (per A-023, agent-proposed synthesis 2026-04-30, A43 v2 verification pending) — soliton (O1 unknot flux tube, ℓ_node scale, Op14-trapped photon, dynamic) + lattice-wake (BEMF/standing-wave-cavity at K4 LC tank nodes, multi-node scale, eigenmode response, static); two simultaneous views of one object, NOT competing descriptions; Track A measures soliton side, Track B measures wake side, A47 v7 caught V_inc-only IC missing the wake | Synthesis (pending corpus-grep) | [A-023](axiom_derivation_status.md); A47 v7 in [COLLABORATION_NOTES line 195](../../.agents/handoffs/COLLABORATION_NOTES.md); doc 28:64-67 + doc 68 §7 (dual-IC seeder) |

---

**Maintenance:** Add a row when a new SM/QFT term surfaces in a research-doc sweep without an existing AVE-native equivalent. Mark it `(IMPORTED)` if currently used without derivation, or flag for Grant adjudication.
