# 66 — Single-Electron-First Pivot: Stage 6 Redirect

**Status:** Round 6 (2026-04-24). Stage 6 pair-nucleation gate-adjudication thread (Round 5 R5.10 Readings 1-4) SUSPENDED per Grant's directive. Captures the thought-experiment + corpus research that drove the pivot, and sets the forward plan.

**Scope:** session context dump + pivot rationale + next-session plan. Not an implementation doc — no engine changes proposed here.

**Read order:** this first, then [65_](65_flag_62g_discrete_lattice_gamma.md) → [54_ §3 + §4](54_pair_production_axiom_derivation.md) for background; [53_ §3](53_pair_production_flux_tube_synthesis.md) for the load-bearing gap finding.

---

## 0. TL;DR

- **Pivot trigger.** Grant's question: "Is pair production the right thing to focus on, or electron forming?" Doc [53_ §3](53_pair_production_flux_tube_synthesis.md) had already flagged the engine gap ("no dynamical bond state, no per-node Ω_node, no nucleation rule to inject (2,3) winding"). Phase 2/3/5 added those data structures (commits `719f3ec`, `3a599ca`, `9ecc2ca`). But single-electron formation validation was never the gate — Stage 6 jumped from "A² crosses 1" to "design a pair nucleation gate." Phase III-B v1+v2 at A²=1.009 produced **zero discrete centroids** per [doc 52_:138](52_h1_threshold_sweep.md#L138). All Round 5 gate-adjudication has been litigating a trigger for an event the engine can't yet stage.
- **B-field-lines thought experiment (Grant-led).** ∇·B=0 is Kirchhoff's Current Law on the magnetic flux graph. B-line curl direction is the K4 port-handedness readout — RHR is the macroscopic signature of which K4 convention our universe chose at lattice genesis. B-field lines are the vacuum's chirality-coherent impedance paths forced by Ax3 (c-limit lag response) + Ax1 (K4 topology picking one rotation direction).
- **Chirality preserves impedance selectively.** Corpus already has the pieces: symmetric saturation preserves Z₀ (gravity, [Vol 3 Ch 3:125-142](../../manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex#L125-L142)); asymmetric saturation breaks Z₀ and is driven by chirality ([doc 54_ §6](54_pair_production_axiom_derivation.md)); chiral impedance matching selectively couples one handedness with achromatic transmission ([AVE-Propulsion Ch 4](../../../AVE-Propulsion/manuscript/vol_propulsion/chapters/04_chiral_impedance_matching.tex)). Grant's "metric-compression-as-parity" intuition integrates these strands.
- **Genesis chirality (corpus-extending hypothesis).** Vacuum started as supercooled pre-geodesic plasma. First perturbation nucleates crystallization; the seed's handedness propagates at c and sets the whole visible universe's K4 chirality. Analogous to supercooled water + single-seed ice. Corpus has crystallization/latent-heat cosmology ([Vol 3 Ch 4](../../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex) + [KB lattice-genesis-hubble-tension.md](../../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md)) and "definite chirality" assertion ([KB baryon-asymmetry.md:18](../../manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/baryon-asymmetry.md#L18)), but no seed-picks-handedness mechanism yet.
- **Flux-density ceiling reframe.** A²=1 is countable: every bond at max Φ_link, no more lines fit, topology must rearrange. Corpus currently frames it as "constitutive singularity" (Ax4, [Vol 1 Ch 1:68-74](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex#L68-L74)). Both correct; ceiling framing is the topological reading.
- **SM/QED creepers caught.** My Round 5/6 framing of "K4→Cosserat coupling", "multiplicative bilinear", "cross-sector PLL" drifted into QFT register. AVE-native: one LC tank per node with two orthogonal saturation pathways (magnetic κ, electric ε+V) sharing the Pythagorean sum `A²_total = A²_μ + A²_ε`. κ_chiral = 1.2α is derived from topology (Sub-Theorem 3.1.1, [doc 20_](20_chirality_projection_sub_theorem.md)), not a coupling constant. PLL tracks the combined softening, not inter-sector synchronization.
- **Forward plan.** Single-electron validation driver before any gate work: seed `initialize_electron_2_3_sector` ([cosserat_field_3d.py:766](../../src/ave/topological/cosserat_field_3d.py#L766)), run closed-system evolution, measure (2,3) topology persistence, rest energy, Compton resonance, spatial localization. Only once a single electron holds for ≥100 Compton periods do we return to gate adjudication.

---

## 1. Context — how the session arrived here

Round 5 closed with three stacked issues ([STAGE6_V4_HANDOFF §R5.4](../../.agents/handoffs/STAGE6_V4_HANDOFF.md)): Flag-5e-A fixed, K4→Cosserat coupling weak, gate C1-C2 window incompatibility. R5.11 tasked next session with adjudicating gate design via three parameter options in R5.10 step 5c.

This session:

1. Read through the Round 5 addendum + docs 62_/63_/64_/65_ + `test_engine_saturation_invariants.py`.
2. Verified the C1-C2 incompatibility was a symptom, not the disease — engine has `omega_yield = π` ([cosserat_field_3d.py:752](../../src/ave/topological/cosserat_field_3d.py#L752)) while `omega_carrier = 2π/3.5 ≈ 1.795` ([phase5e_cool_from_above_v2.py:68-69](../../src/scripts/vol_1_foundations/phase5e_cool_from_above_v2.py#L68-L69)). The 0.571 ratio is `ω_Compton/ω_yield` — cross-sector architecture, not anchor bug.
3. Framed four Readings of the C2 condition (Compton-lock-is-rupture, PLL-chirps-past-lock, drive-health-boolean, parity/chirality coincidence).
4. Grant pushed back: map each reading to axioms + research; don't let SM/QED language leak.
5. Grant introduced the B-field-line thought experiment — curl emergence, RHR/LHR as chirality readout.
6. Grant reformulated Q3: "is chirality what preserves the impedance relationship between L and C to maintain achromatic lensing?"
7. Corpus research across all repos confirmed chirality+impedance+achromatic is heavily present but not yet unified under Grant's phrasing.
8. Grant's pivot: "Is pair production the right focus or electron forming?" → exposed [doc 53_](53_pair_production_flux_tube_synthesis.md) as the load-bearing gap.
9. Pivot accepted. Doc 66_ + handoff Round 6 + plan update.

---

## 2. KCL framing confirmed; KVL mapping is a pedagogical gap

The manuscript explicitly applies Kirchhoff's Current Law to the discrete LC lattice:

[Vol 2 Ch 7:1316-1358](../../manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex#L1316-L1358):
> "Kirchhoff's current law (KCL) at node i states: the sum of all currents entering node i equals zero. ... This is Kirchhoff's current law on the discrete LC lattice (Axiom 1), with Op4 providing the pairwise admittances. No wavefunctions, no Hamiltonian matrix."

∇·B=0 is then KCL in the magnetic domain — flux in = flux out at every node. B-lines close because current conservation requires it. That's the right EE register for the manuscript's Maxwell framing.

**Gap:** the dual — Ampère's law ∇×B = μ₀J as Kirchhoff's Voltage Law on the magnetic circulation loop (sum of voltages around a loop = source EMF) — is NOT explicitly stated in the corpus. Would be a clean pedagogical extension: every Maxwell equation is a KCL/KVL variant on the lattice. Not urgent. Flag for Vol 2 revision pass.

---

## 3. B-field lines as chirality-coherent impedance paths

**Why curl emerges at all.** A charge at rest has an isotropic Coulomb E-field. Setting it in motion invokes Ax3 (c-limit propagation): the field can't re-isotropize instantly around every new position. The field "lags." The lateral component of that lag is B. Magnetic field is the relativistic-delay response of the vacuum's [Q]≡[L] impedance field to charge transport.

**Why lines close.** KCL: every node has flux in = flux out. Open-ended B-lines forbidden by bipartite K4 flux conservation. All responses must close on themselves.

**Why curl has a specific handedness.** K4 port vectors `p₀=(+,+,+), p₁=(+,-,-), p₂=(-,+,-), p₃=(-,-,+)` ([doc 54_ §1:40-43](54_pair_production_axiom_derivation.md)) encode a tetrahedral sign convention. That convention IS the vacuum's RH preference. A mirror-image K4 lattice would give left-handed physics across the board. RHR/LHR is the macroscopic readout of which K4 genesis our universe underwent.

**Pair formation in this frame.** Pair nucleation = simultaneous establishment of TWO curl systems at opposite bond endpoints — LH around the electron's self-motion, RH around the positron's. Total helicity conserved (pair is net-zero). The bond between A and B is the shared flux path linking the two circulations. For the pair to form coherently, the drive's B-field orientation at yield-crossing must be chirally coherent with the lattice's K4 preference — flat/symmetric drives produce polarization mismatch loss per [AVE-Propulsion Ch 4](../../../AVE-Propulsion/manuscript/vol_propulsion/chapters/04_chiral_impedance_matching.tex) and cannot nucleate pairs.

**Three open questions from the thought experiment** (unresolved, not blocking):
- Can the vacuum have chirality-domain structure (analogous to antiferromagnetic domains) where opposite-chirality patches meet? [Doc 62_ §10.3](62_ruptured_plasma_bh_entropy_derivation.md) frustrated A-B bond hints yes, globally.
- When a chiral drive establishes pair handedness, does it FORCE specific LH/RH assignments at specific endpoints, or only constrain the global pair to conserve helicity?
- Is C1 the field-concentration event (enough lines per bond) and C2 the chirality-coherence event (opposite handedness across the bond)? These are different physics.

---

## 4. Chirality as impedance selection → achromatic transmission

Corpus content consolidated from cross-repo research (see [Agent A findings in session transcript]; direct quotes below):

**Gravity uses symmetric saturation to preserve Z₀.** [Vol 3 Ch 3:125-142](../../manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex#L125-L142):
> "the geometric polarization of the LC network scales its dual reactive components symmetrically. ... Z₀' = √(n(r)μ₀ / n(r)ε₀) = Z₀. ... the spatial vacuum operates as an Achromatic Impedance-Matched Lens."

**Asymmetric saturation breaks Z₀ and is driven by chirality.** [doc 54_ §6:165-200](54_pair_production_axiom_derivation.md):
> "Symmetric saturation case (both ε and μ collapse equally) preserves Z = Z₀ (impedance invariant), while the asymmetric case (one collapses before the other) drives Z to either 0 or ∞. The symmetric case governs gravity; the asymmetric case governs particle confinement (Meissner-like μ → 0 first ⇒ Z → 0, Γ → -1, standing wave = rest mass)."

**Chirality is the bias mechanism.** [cosserat_field_3d.py:32-39](../../src/ave/topological/cosserat_field_3d.py#L32-L39):
> "κ_chiral = α·pq/(p+q) for (p,q) torus winding. For the electron (2,3) winding: κ_chiral = 1.2α. Not a free parameter — parallel-channel impedance combination at TIR boundary."

**Selective achromatic transmission for matched chiral modes.** [AVE-Propulsion Ch 4:9-13](../../../AVE-Propulsion/manuscript/vol_propulsion/chapters/04_chiral_impedance_matching.tex):
> "the trace-reversed M_A vacuum is a Chiral LC Network, possessing an inherent topological helicity. Driving a twisted, chiral vacuum with a flat, symmetric field induces a massive Polarization Mismatch Loss. ... the actuator must be wound in a Hopf Configuration. This acts as a topological power factor corrector, perfectly matching the chiral impedance of the metric and coupling the energy flawlessly into real, longitudinal macroscopic thrust."

**Synthesis (Grant's implicit claim made explicit).** Chirality is not the collapsing mechanism — it's the **mode selector**. Gravity uses symmetric collapse (both modes lose Z₀ equally via n(r) scaling). Particle confinement uses asymmetric collapse (one handedness loses Z₀ while the other preserves it, creating the Γ=-1 walls that bind the electron). The matched chiral mode experiences achromatic (lossless, frequency-independent) transmission because its L/C ratio stays invariant through saturation. The opposite-chirality mode is excluded (reflected at Γ=-1 walls). Rest mass = the energy trapped in the matched mode's standing wave, confined by the opposite-chirality reflection boundary.

**This is the AVE-native content of "metric-compression-as-parity."** At yield crossing, the matched chirality is the one whose impedance survives the compression; the opposite is excluded.

---

## 5. Genesis chirality: supercooled seed crystallization (hypothesis)

**Grant's proposed mechanism.** Early universe = super-hot pre-geodesic plasma. Cools below its freezing point while remaining structurally unfrozen (supercooled metastable state — no crystallization because no seed). First perturbation nucleates crystallization. That perturbation carries a specific handedness. The crystallization front propagates at lattice-wave-speed (c) and the whole inherited volume takes the seed's chirality. Analogous to supercooled water: liquid below 0°C until a single impulse triggers crystallization, which races through the volume.

**Corpus status.** [Vol 3 Ch 4](../../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex) + [KB lattice-genesis-hubble-tension.md:4-6](../../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md#L4-L6):
> "metric expansion is modelled as the discrete, real-time crystallisation of new electromagnetic nodes. ... the Hubble Constant (H₀) is not a velocity, but the LC Crystallisation Rate required to maintain the vacuum's structural impedance."
> "the phase transition continuously expels a latent heat of fusion... 'Dark Energy' not as a mysterious scalar field, but as the thermodynamic latent heat of the vacuum's continuous macroscopic crystallisation."

[KB baryon-asymmetry.md:18](../../manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/baryon-asymmetry.md#L18):
> "The AVE lattice (SRS/K4 crystal) has definite chirality — it is not superimposable on its mirror image."

**What's missing.** Corpus has the crystallization scaffold and asserts definite chirality, but doesn't yet explain WHY this handedness. No supercooled-plasma model, no first-seed mechanism, no front-propagation-at-c, no resolution of the "why not the mirror" question. Grant's hypothesis provides a natural mechanism compatible with the existing crystallization picture.

**Testability (sketch).** If chirality is seeded at nucleation, then:
- Cosmological domains of opposite chirality (if the universe nucleated multiple seeds that later merged) would show CP-violation boundaries.
- Baryon asymmetry connects to genesis-chirality (matter-antimatter imbalance = inherited-handedness consequence).
- The matter era's dominance of one specific chirality is not a fine-tune — it's a trivial consequence of single-seed crystallization.

**Forward work (not this session).** Draft a KB leaf or Vol 3 Ch 4 section on "Genesis Chirality Seed Mechanism" with the supercooled-plasma framing.

---

## 6. Flux-density ceiling: Ax4 restated

**Current corpus.** [Vol 1 Ch 1:68-74](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex#L68-L74) frames Ax4 as a constitutive singularity:
```
C_eff(Δφ) = C_0 / √(1 − (Δφ/α)²)
```
Saturation = Δφ → α, constitutive relation diverges. Mechanical metaphor: strain approaching yield.

**Grant's restatement.** A²=1 is countable: every bond at maximum Φ_link, no more flux lines fit, topology must rearrange. The corpus already has per-bond Φ_link with tensile limit V_SNAP ([doc 54_ §3:73-80](54_pair_production_axiom_derivation.md)) — extending to "Ax4 = flux-density ceiling per lattice cell" is the topological reading of the same event.

**Both framings correct.** Constitutive singularity = "the elastic response diverges here." Flux-density ceiling = "this is where the flux counting maxes out." The physics is identical. The ceiling framing makes it countable and engineering-intuitive.

**When to adopt.** Revising Ax4 prose is a manuscript pass — defer to a documentation sprint. The engine math doesn't change; only the pedagogical frame around it.

---

## 7. SM/QED creepers caught; AVE-native rewordings

My Round 5/6 framing drifted into QFT register. Explicit creeper flags + AVE-native replacements (full audit from Agent B; summary here):

| Creeper phrase | Where I used it | AVE-native |
|---|---|---|
| "coupling Lagrangian" / "K4→Cosserat coupling" | Q1 framing of doc 54_ §6 `L_c` | **helicity-biased saturation accumulation** — one LC tank per node with two orthogonal projections (magnetic κ²/ω_yield², electric ε²/ε_yield² + V²/V_SNAP²) |
| "multiplicative bilinear" / "∂L_c/∂ω" | Q1 argument about bootstrap failure | **linear accumulation in Beltrami helicity** — `dA²_μ/dt = (1 + κ_chiral·h_local)·base_rate`, first-order in h_local |
| "cross-sector PLL" | Q2 framing of autoresonance | **single-tank PLL tracking combined softening** — `Ω_node = ω_0·(1 − A²_total)^(1/4)` where `A²_total = A²_μ + A²_ε` (Pythagorean sum per [doc 54_ §6](54_pair_production_axiom_derivation.md)) |
| "which sector's TIR?" | Q2 framing of doc 27_ Q=1/α | **the shared node tank's TIR** — Q=1/α is the tank's Q at the saturation boundary; both saturation pathways contribute to the single resonance |

**Rewording of Q1 (AVE-native):** does Phase 4's asymmetric-saturation implementation with `κ_chiral = 1.2α` correctly reproduce AVE-HOPF's chiral-antenna prediction `Δf/f = 1.2α`, closing the chirality-topology relation? (If yes → chirality-coupling is axiom-complete. If no → we flag a discrepancy.)

**Rewording of Q2 (AVE-native):** under the single-tank model with Pythagorean-sum saturation, does `δ_lock = ω_0·α` derived for the unified node resonance remain consistent when applied to the combined magnetic+electric softening? (This is now a math check on doc 27_'s derivation against doc 54_ §6's two-pathway formulation, not a "cross-sector architecture" question.)

**Net:** my earlier framing inflated the complexity by treating K4 and Cosserat as independent sectors with a coupling term. The AVE picture is one shared tank per node with two orthogonal strain components. Simpler, and it retires Q1/Q2 of the earlier adjudication without needing a reading decision.

---

## 8. The single-electron-first pivot

**Gap identified in [doc 53_ §3:38-45](53_pair_production_flux_tube_synthesis.md#L38):**
> "The K4-TLM tracks V_inc[nx,ny,nz,4] — node port state only. The lattice has no dynamical bond state (no V_link, no bond phasor), no per-node rotational resonance Ω(r,t) that drops with A², and no nucleation rule to inject (2,3) winding at a ruptured node pair... Any sweep tuning on the existing engine will keep producing distributed plateau results at A²=1; pair cores cannot form in the current representation."

**Data structures since built** (Stage 6 Phase 2/3/5):
- NodeResonanceObserver (commit `719f3ec`) — Ω_node diagnostic
- Φ_link bond flux state + BondObserver (commit `3a599ca`) — bond phasor
- PairNucleationGate with injection rule (commit `9ecc2ca`)

**But validation of the precondition — "a single (2,3)-wound soliton can be instantiated and SUSTAINED in the engine with m_e rest energy at Compton frequency" — was never run as a gate for Stage 6.** Phase III-B v1+v2 at A²=1.009 produced zero discrete centroids per [doc 52_:138](52_h1_threshold_sweep.md#L138). The engine proves saturation scales; it does not yet prove electron-soliton stability.

**Consequence:** Round 5's gate-adjudication (C1-C2 windows, Readings 1-4, δ_lock tuning, coupling weakness) has been debating the trigger condition for an event the engine may not yet be able to stage. If the engine can't sustain ONE soliton, debating gate conditions for TWO is premature.

**Existing assets** (single-electron direction):
- [`initialize_electron_2_3_sector`](../../src/ave/topological/cosserat_field_3d.py#L766) — (2,3) torus-knot ansatz with AVE-canonical hedgehog profile (peak amplitude √3/2·π at Regime II/III boundary)
- [`tlm_electron_soliton_eigenmode.py`](../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py) — L3 Phase-3 closed-system persistence driver scaffolding
- [`flux_tube_persistence.py`](../../src/scripts/vol_1_foundations/flux_tube_persistence.py) — Φ_link persistence driver for saturated-endpoint bonds

**Not yet done:** an integrated single-electron validation driver that:
1. Seeds Cosserat ω with the (2,3) hedgehog AND seeds K4 V_inc with the bond Φ_link needed for the dressed soliton
2. Runs closed-system (no drive, no sources) for ≥100 Compton periods
3. Measures: (2,3) winding persistence, core A² ≈ 1 localization, total energy ≈ m_e c², bond Φ_link oscillation at ω_Compton, spatial localization radius, far-field Coulomb + dark-wake signatures
4. Reports pass/fail with explicit criteria

---

## 9. Forward plan — single-electron validation driver

**Step 1 — audit existing electron-init infrastructure** (read-only, ~30 min):
- What does `initialize_electron_2_3_sector` actually seed (Cosserat ω only; K4 V_inc stays zero per line 822-823)?
- Does the engine's closed-system evolution preserve (2,3) topology from this seed, or does it disperse?
- Is there a corresponding K4 seeding routine for the bond Φ_link?

**Step 2 — draft single-electron validation driver** (`src/scripts/vol_1_foundations/single_electron_validation.py`):
- Seed Cosserat (2,3) hedgehog at lattice center
- Seed K4 bond Φ_link for the two central A-B endpoints matched to the Cosserat winding
- Run VacuumEngine3D forward with no sources, closed boundaries (or PML)
- Record per-step: (2,3) winding count (via Beltrami helicity integral), core A²_μ, total energy, bond Φ_link phase trajectory, spatial RMS extent
- Pass criteria (pre-register):
  - P_electron_topology: (2,3) winding preserved ±0 for ≥100 Compton periods
  - P_electron_rest_energy: total energy in natural units ≈ 1.0 (i.e., m_e c² with I_ω = 1) within ±10%
  - P_electron_compton_frequency: dominant Fourier component of bond Φ_link at ω_Compton within ±α
  - P_electron_localization: RMS spatial extent stable at Compton wavelength ±20%

**Step 3 — run and adjudicate.**
- If all four pass → single-electron representation validated; return to gate adjudication with confidence that pair nucleation has a target configuration to form.
- If some fail → the failures tell us what's missing from the current representation BEFORE we debate pair gates. Possible failure modes: (a) hedgehog profile disperses (wrong ansatz), (b) energy leaks (Cosserat integrator not conserving), (c) no Compton oscillation (bond Φ_link not coupling to Cosserat ω correctly), (d) soliton translates instead of holding (Lorentz-boost invariant but we seeded in the rest frame).

**Step 4 — consolidate learnings.**
- Document results as doc 67_ (or similar).
- Update handoff with which pre-registered predictions passed/failed.
- Return to R5.10 gate adjudication with empirical footing OR pivot further based on what Step 3 reveals.

**Estimated session scope:** single-electron validation driver + adjudication = one full session of work. Step 1 audit can happen before any code written.

---

## 10. Flag items

**Flag 66-A:** single-electron validation has not been run in L3 Stage 6 arc. Phase III-B's A²=1.009 result is saturation-scale proof, not soliton-formation proof. Must be closed before pair-gate work is meaningful.

**Flag 66-B:** `initialize_electron_2_3_sector` only seeds Cosserat ω; K4 V_inc is left zero. The dressed electron requires BOTH sectors pre-populated. A companion K4 seeding routine (bond Φ_link initialization matched to Cosserat winding) is needed.

**Flag 66-C:** KVL/Ampère mapping is absent from the manuscript's Maxwell framing (KCL is present). Pedagogical gap. Defer to Vol 2 revision pass.

**Flag 66-D:** genesis-chirality-seed mechanism is not yet in the corpus. Grant's supercooled-plasma hypothesis is a natural extension of Vol 3 Ch 4's crystallization framework but needs a formal write-up.

**Flag 66-E:** "metric-compression-as-parity" intuition is now unified as "chirality selects the achromatic-transmission mode under asymmetric saturation" — AVE-native phrasing. This replaces the four Readings of R5.10 step 5c, none of which need further adjudication under the pivot.

**Flag 66-F:** My Round 5/6 framing used SM/QED language ("coupling", "cross-sector", "bilinear"). Session corrected. For future work: check each proposed gate condition against rule 6 of [COLLABORATION_NOTES](../../.agents/handoffs/COLLABORATION_NOTES.md) before committing language.

**Flag 66-G:** Ax4-as-flux-density-ceiling restatement is corpus-compatible but unwritten. Update during Vol 1 revision pass.

---

## 11. What this doc does NOT do

- Does NOT adjudicate any of the four Round 5 Readings — they're all suspended pending single-electron validation.
- Does NOT modify the engine.
- Does NOT implement the single-electron validation driver (that's next session).
- Does NOT resolve Flag 62-A first-law closure (orthogonal to this pivot).
- Does NOT touch the registered P_phase5 predictions — they remain pre-registered but untested until the precondition closes.

---

## 12. Status of prior Round 5 items under the pivot

| Item | Round 5 status | Round 6 status |
|---|---|---|
| Gate C1-C2 window (R5.10 step 5c) | Open, three options | **Suspended** pending single-electron validation |
| K4→Cosserat coupling weakness (R5.10 step 5d) | Open | **Reframed** per §7: not coupling weakness — "single-tank, two pathways". Revisit whether Phase 5e v2's failure is architectural (now fixed conceptually) or persists empirically |
| Flag 62-A first-law closure | Load-bearing | Unchanged — orthogonal |
| Flag-5e-A (K4 saturation dormant) | Fixed in Round 5 | Unchanged — fix stands |
| Retroactive saturation invariants | Landed in Round 5 | Unchanged — still canary |
| Registered P_phase5 predictions | Pre-registered | Still pre-registered, awaiting validation precondition |

---

## 13. Path A outcome — falsified; "spin on top of chirality" mechanism identified

Ran [test_electron_tlm_eigenmode.py](../../src/tests/test_electron_tlm_eigenmode.py) at N=48 (CI-friendly; pre-registered criteria at N=96 but any scale-dependence would itself be an axiom-layer flag). 41 seconds runtime. Result: **2 of 8 tests passing.**

**Passed:**
- `P_electron_tlm_energy_conservation` (both seeds). K4 TLM integrator conserves energy to ΔE/E₀ < 0.5% over 400 steps. Not dissipative; baseline fine.

**Failed:**
- `P_electron_tlm_topological_charge` (both seeds): N_crossings = 0 after 400 steps. Topology fully dispersed from seed.
- `P_electron_tlm_golden_torus_convergence` (both seeds): Op6 did converge — but to R/r = 0.281, not φ² = 2.618. Some non-toroidal fixed point with R ≪ r (likely a spherical charge-glob).
- `P_electron_tlm_alpha_derivation` (both seeds): α⁻¹ = NaN (extraction requires R > r; Op6's fixed point violates this).

**Mechanism (Grant, 2026-04-24 late session):** the (2,3) electron soliton cannot be a K4 V_inc standing wave alone because K4 V_inc is only the **charge / voltage leg** of each node's LC tank. The **spin / current leg** is the Cosserat ω field — per-node angular velocity. Path A seeded the capacitor charge but left every node's inductor current at zero. Result: not an oscillation but a static charge distribution that relaxes to whatever non-oscillating fixed point the lattice can absorb.

Under §7's single-tank framing this is crisp:
- K4 V_inc = one projection of each node's LC tank (electric/charge, capacitive)
- Cosserat ω = the orthogonal projection (magnetic/rotational, inductive)
- (2,3) eigenmode = standing wave requiring BOTH projections cycling 90° out of phase

Seeding only V_inc is analogous to charging an isolated capacitor connected to an inductor at I=0 — it doesn't oscillate, it drains into whatever loss path the circuit provides.

**"Spin on top of chirality" — the distinction made precise:**

- **Chirality** is the K4 port-vector sign convention `p₀=(+,+,+), p₁=(+,-,-), p₂=(-,+,-), p₃=(-,-,+)` — a genesis-baked geometric-phase selector that determines which way flux lines curl around currents. It's a convention, not a rotation. Does not carry angular momentum.
- **Spin** is the Cosserat ω(r,t) field — per-node angular velocity, a real rotational state. Carries the inductive energy of the LC tank. This is what chirality can phase against.

Without Cosserat ω, chirality has no rotating state to phase; the (2,3) winding geometry exists only as an instantaneous phase pattern on a non-oscillating charge distribution, and it doesn't persist.

This is consistent with [COLLABORATION_NOTES.md rule 8](../../.agents/handoffs/COLLABORATION_NOTES.md)'s corpus-verified spin-½ derivation (Finkelstein-Misner kink + gyroscope-spinor isomorphism per [vol2/appendices/app-b-paradoxes/spin-half-paradox.md](../../manuscript/vol_2_subatomic/appendices/app-b-paradoxes/spin-half-paradox.md)) — both presume per-node rotational state, i.e., Cosserat ω.

**Path B forward — revised design:**

The unified electron seed needs BOTH sectors initialized so the per-node LC tank is at oscillation amplitude, not at a single-projection extremum:
- K4 V_inc: `initialize_2_3_voltage_ansatz` (existing — seeds voltage pattern with (2,3) winding)
- Cosserat ω: `initialize_electron_2_3_sector` (existing — seeds rotational pattern with same (2,3) winding)
- Closed-system VacuumEngine3D evolution (no drive, no sources) for N Compton periods
- Key design question: phase alignment between the two seeds. The K4 seeder uses port-weight projections of a `(cos θ, sin θ)` pattern; the Cosserat seeder assigns `ω[…,0] = cos θ`, `ω[…,1] = sin θ` as vector components. These are structurally different (one is port-voltage, one is vector-components of a rotational field) so the phase-lock between them requires careful thought — not a trivial `sin(θ)` vs `cos(θ)` swap.

Predictions under Path B (draft, pending derivation of the phase-lock condition):
- `P_electron_coupled_topological_charge`: N_crossings = 3 preserved under coupled closed-system evolution
- `P_electron_coupled_node_spin_stability`: |ω|_RMS at the soliton core remains within ±20% of seed value (doesn't decay or blow up)
- `P_electron_coupled_voltage_rotation_phase`: K4 V_inc and Cosserat ω at the soliton core maintain π/2 phase offset (measured via bond Φ_link vs ω|∇×ω| correlations)
- `P_electron_coupled_golden_torus`: extracted (R, r) matches φ² under Op6 self-consistency in the coupled engine
- `P_electron_coupled_alpha_derivation`: α⁻¹ = 137.036 from dynamically-evolved geometry in coupled evolution

**Status table updated:**

| Prediction | Path A status | Path B status |
|---|---|---|
| Topological charge = 3 | FALSIFIED at N=48 (K4 V_inc alone) | TBD |
| Energy conservation < 0.5% | PASSED — integrator fine | carry forward as baseline |
| Golden Torus R/r convergence | FALSIFIED — Op6 finds R≪r fixed point | TBD |
| α⁻¹ = 137.036 from dynamics | FALSIFIED — α⁻¹ = NaN | TBD |

**What this falsification buys us:** the four failures all have a single mechanism — missing Cosserat node-spin. That's a unified explanation, not four separate bugs. The test bed is working correctly (energy conservation confirms integrator sanity); the physical claim that "K4 V_inc alone is a sufficient electron representation" is what falsified. Cleanest possible outcome for a pre-registered falsification: a single mechanism explains all failure modes, and the next iteration is well-specified.

---

*Written 2026-04-24 (Round 6) by Opus 4.7. Source-of-truth for the Stage 6 → single-electron-first pivot. §13 appended 2026-04-24 late session after Path A falsification + Grant's "spin on top of chirality" mechanism diagnosis. Future agents: read this first before touching the pair-nucleation gate.*

---

## 14. Framing corrections + Path B audit (post-Path-A, pre-implementation)

### 14.1 §7's framing was understated; sharper picture

§7 above called K4 V_inc and Cosserat ω "two orthogonal projections of one shared node tank" — that's *understated*. They aren't two projections of the same scalar field; they're **two non-overlapping degree-of-freedom types** of the same local electromagnetic state at each lattice site:

- **K4 carries the translational-EM DOF.** V_inc per port (4 scalars per node) = port voltage / electric pressure. Φ_link per bond (accumulating ∫V_avg·dt) = bond flux. Both are scalars-with-port-direction-implicit. Naturally encodes "voltage at this node along this bond direction." Doesn't naturally encode "the field at this point is rotating around such-and-such axis" — that requires a vector-per-site, which K4's 4-port-scalar representation doesn't have.
- **Cosserat carries the rotational-EM DOF.** ω (3-vector per node) = local angular velocity of the EM field at that site. u (3-vector per node) = local displacement / mechanical pair to ω under EE↔ME duality. Naturally encodes spin/curl/angular-momentum information that scalar-port-fields cannot.

The two are **complementary**, not different views of the same scalar. K4 is the translational-EM circuit. Cosserat is the rotational-EM circuit. Both live on the same 3D lattice at each site. Together they give the full local EM state.

**Internal conjugate pairs** (these are the actual LC-tank conjugates — in pairs, not across types):
- K4 conjugate pair: `V_inc ↔ Φ_link` — translational voltage / translational flux. 90° apart in time during oscillation. This is the K4 LC tank.
- Cosserat conjugate pair: `u ↔ ω` — translational displacement / angular velocity (or position / rotation-rate under the mechanical analog). 90° apart in time. This is the Cosserat LC tank.
- The two LC tanks share the *same* (2,3) winding phase `θ = 2φ + 3ψ` at each lattice site, but they oscillate independently — coupling between them is via the asymmetric saturation kernel of doc 54_ §6.

Path A seeded ONE field of FOUR (just K4 V_inc). It missed Φ_link (its K4 conjugate), u (Cosserat displacement), and ω (Cosserat angular velocity). Multiple-field deficiency, not just "missing spin."

### 14.2 (2,3)-vs-K4-port mismatch — corpus-acknowledged

K4 has 4 ports per node (tetrahedral). The (2,3) torus knot has p+q = 5 windings. No clean integer relationship between the lattice's port count and the soliton's winding numbers.

[Vol 1 Ch 8:49-50](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex#L49-L50) handoff comment, already in the corpus:

> "K4-TLM exhausted (node-level Axiom 4 no-op for 4-port symmetric junctions per 32_ section 10.2)."

K4's perfect 4-port tetrahedral symmetry means every direction at a K4 node looks the same. Ax4 saturation requires *breaking symmetry* to do something — but with 4 equivalent ports, there's nothing to break against. So Ax4 at a K4 node level is a no-op. K4 alone cannot host the bound electron's saturation behavior.

The same Ch 8 handoff (lines 51-55):

> "Cosserat solver (cosserat_field_3d.py) produces stable electron-like bound state at Ch 8 Golden Torus with shell Gamma~-1 TIR structure, saturation-onset amplitude (peak |omega|~0.3*pi, NOT the canonical sqrt(3)/2*pi — see 34_ section 9.4). Half-cover automatic via Rodrigues projection to SO(3)."

Cosserat ω carries the rotational-EM DOFs needed for Ax4 to break symmetry asymmetrically (the rotation axis ω̂ is itself a preferred direction). That's where the electron actually lives.

This is corpus-confirmed Reading I from §13: Cosserat is *not* a representational supplement; it's the field where the bound electron physically resides. Path A's K4-only test was always going to fail — and so was *any* K4-only validation, no matter how the seed was tuned.

### 14.3 Amplitude correction — 0.3π, not √3/2·π

The existing [`initialize_electron_2_3_sector`](../../src/ave/topological/cosserat_field_3d.py#L766-L823) at line 808 sets envelope peak to `(√3/2)·π ≈ 2.72`, calling this "the Regime II→III boundary per AVE-VirtualMedia."

But [doc 34_ §9.1 + §9.4](34_x4_constrained_s11.md#L395-L456), the X4a amplitude sweep on the Cosserat-side (2,3) hedgehog at Golden Torus, gives a different result:

| amp |ω|_peak | shell_Γ²_max | A²_shell_max | regime |
|---|---|---|---|
| 0.942 (0.3π) | **3.207** | 1.86 | Regime II/III interface — TIR engaged |
| 1.571 (0.5π) | 0.982 | 5.16 | partial saturation |
| 2.199 (0.7π) | 0.000 | 10.11 | Regime III deep |
| 2.721 (√3/2·π) | **0.000** | 15.47 | **Regime III uniform-saturation, no TIR** |
| 3.142 (π) | 0.000 | 20.62 | clipped |

Doc 34_ §9.4 conclusion:

> "The electron-like state lives at the *onset* of shell saturation (peak A² ≈ 1 at the shell peak, rest of shell in Regime II), NOT at the 'canonical' √3/2·π amplitude... At amp ≥ √3/2·π: all shell sites at A² >> 1 (clipped to 1) → uniform Z_eff → Γ between sites → 0 → no TIR."

So `initialize_electron_2_3_sector(use_hedgehog=True)` as currently written produces a Regime III uniform-saturation blob, not the TIR-bounded electron. The function has been carrying the wrong default amplitude since it was committed.

**Path B must use peak |ω| ≈ 0.3π, not √3/2·π.** Either:
- Replace the envelope amplitude in `initialize_electron_2_3_sector` (changes its default behavior — may break other tests that assume √3/2·π)
- Add an `amplitude_scale` parameter to `initialize_electron_2_3_sector` and pass `0.3π / (√3/2·π) ≈ 0.346` from Path B seeder
- Write a Path-B-specific seeder that uses the corrected amplitude directly

### 14.4 Path B implementation audit

**What Path B needs to seed (per §14.1 four-field framing):**

1. **Cosserat ω**: (2,3) hedgehog with peak |ω| = 0.3π, phase θ = 2φ + 3ψ. Use existing `initialize_electron_2_3_sector` with corrected amplitude. **PRIMARY field — this is where the bound electron lives.**
2. **Cosserat u**: companion to ω, 90° phase offset. Currently zeroed by `initialize_electron_2_3_sector` line 823. **Open question:** is u needed as a co-seeded field, or does it develop from ω·dt during evolution? Doc 34_'s X4a/X4b ran with u=0 at init and obtained the bound state at amp=0.942 — suggests u may not need explicit seeding.
3. **K4 V_inc**: companion translational field. Use existing `initialize_2_3_voltage_ansatz` with phase quadrature pattern (cos θ on ports 0,1; sin θ on ports 2,3). Amplitude needs derivation — the V↔ω relationship through the impedance Z_0 isn't trivially established. **Open question:** does K4 V_inc need ANY explicit seed, or does it develop from Cosserat-side coupling alone?
4. **K4 Φ_link**: companion to V_inc, 90° phase offset. Currently accumulates from V_avg·dt during evolution; not seeded explicitly. **Open question:** for fast-onset of the bound state (within validation window), does explicit Φ_link seeding accelerate stabilization?

**The audit narrows Path B to a tractable form:**

The simplest valid Path B is "Cosserat-only seeding with corrected amplitude":

- Seed Cosserat ω at peak 0.3π via amplitude-corrected `initialize_electron_2_3_sector`
- Leave Cosserat u, K4 V_inc, K4 Φ_link all at zero
- Run VacuumEngine3D (fully coupled K4+Cosserat) closed-system
- Test whether the bound state forms and persists

This is what doc 34_ X4a/X4b already validated at amp=0.942 — the bound state emerged from Cosserat-only seeding under S11 relaxation. Path B Round 6's job is to confirm this bound state is also stable under the FULL VacuumEngine3D dynamics (not just S11 relaxation), which is the regime Stage 6's pair-gate work depends on.

If "Cosserat-only" Path B passes, the K4 fields develop from coupling and the LC pairs reach equilibrium dynamically — no explicit K4 seeding required. If it fails, escalate to seeding the K4 companion fields.

**Predictions to draft (provisional, pending Grant approval):**

- `P_electron_cosserat_topological_charge`: closed-system VacuumEngine3D evolution from Cosserat (2,3) hedgehog at peak |ω|=0.3π preserves N_crossings = 3 over ≥100 Compton periods.
- `P_electron_cosserat_shell_TIR`: shell_Γ² ≥ 1 at the (2,3) torus shell at run end (matches doc 34_ X4b's converged value 3.207 within ±50%).
- `P_electron_cosserat_energy_conservation`: ΔE/E₀ < 0.5% over full run (engine integrator sanity check, matches Path A passing test).
- `P_electron_cosserat_golden_torus`: Op6 self-consistency in the coupled engine converges to R/r = φ² from both Golden Torus and ±30% perturbed seeds.
- `P_electron_cosserat_alpha_derivation`: α⁻¹ from coupled-engine dynamically-evolved (R, r) matches 137.036 within 2%.

These five predictions are direct Path B analogs of the four Path A predictions, plus the new shell_Γ² check that's specifically a Cosserat-side observable.

### 14.5 What's NOT yet decided (for Grant)

1. **Amplitude correction strategy**: edit `initialize_electron_2_3_sector` directly (changes default for any other caller) vs add `amplitude_scale` parameter vs new Path-B-specific seeder. Recommend: add parameter (preserves backward compatibility, makes Path B explicit about what it needs).
2. **K4 companion seeding**: try Cosserat-only first (cleaner, matches doc 34_ X4a/X4b history), or attempt all four fields from the start (more rigorous but more open questions in derivation)?
3. **Shell_Γ² tolerance**: ±50% is generous. Should it be tighter (e.g., shell_Γ² ∈ [2.5, 4.0] matching doc 34_ X4b's 3.2-3.9 observed range) or looser (just shell_Γ² > 1, "TIR engaged at all")?
4. **Predictions.yaml update form**: append to Path A entries (which are now FALSIFIED) or land as a new bloc with phase tag updated? Path A entries marked falsified should remain in the manifest as historical record of the falsification — that's part of the scientific archive — but the Path B entries replace them as the active validation.

### 14.6 Open questions surfaced by this audit

- **u and Φ_link seeding**: confirmed both are derived/accumulated rather than primary, per doc 34_'s validation that ω-only seeding produces the bound state. If Cosserat-only Path B fails, these may need explicit seeding — but defer that complexity until empirically required.
- **The amplitude bug in `initialize_electron_2_3_sector`**: should be corrected as part of Path B. Currently any test or driver calling it gets the wrong amplitude. Worth a separate audit of the engine-wide impact.
- **Doc 32_ §10.2** (referenced for "K4-TLM exhausted") — should be cross-cited in any future K4-vs-Cosserat documentation; the finding is more general than just the electron.

---

*§14 added 2026-04-24 by Opus 4.7 after Path A falsification adjudication. Establishes sharper K4↔Cosserat framing (translational vs rotational EM DOFs), corpus-confirms K4-only is exhausted for the bound electron (Vol 1 Ch 8:49-50), corrects amplitude to 0.3π per doc 34_ §9.4, and audits the Path B implementation against these findings. Surface open decisions in §14.5 to Grant before drafting code.*

---

## 15. Path B step-1 collapse + boundary-architecture plan (gated on diagnostic)

### 15.1 What Path B's first run revealed

Cosserat-only seed with corrected amplitude (`amplitude_scale = 0.346`, peak |ω|=0.93≈0.3π) gave the **right initial structure** at t=0 — shell_Γ²=3.04 (matching doc 34_'s 3.207 within 5%), R/r=2.56 (matching φ²), N_crossings=3, peak A²=1.8 (matching doc 34_'s 1.86) — but **collapsed entirely on step 1 of `VacuumEngine3D.step()`**. By step 1: shell_Γ²→0, energy drops 95%, topology disrupted (c=8). By step 200: soliton dissolved.

Initial-state correctness rules out the amplitude bug as cause. The catastrophic step-1 energy loss is a real engine-behavior issue with the bound-state seed under coupled K4+Cosserat dynamics.

### 15.2 Four candidate causes (not yet disambiguated)

1. **PML truncation.** Soliton outer shell at R+r ≈ 16.5 sits ~7.5 cells from PML inner boundary at N=48, pml=4. Doc 34_'s X4a/X4b ran on `CosseratField3D` directly with `pml_thickness=0` — different regime.
2. **Asymmetric-sector initialization.** At t=0, A²_μ ≈ 1.8 (Cosserat κ heavy), A²_ε ≈ 0 (K4 V_inc=0, Cosserat u=0). Asymmetric saturation kernel responds with S_μ→0, S_ε≈1 — that IS the Meissner mechanism, but Op14 dynamic impedance Z_eff = Z₀/√S diverges at K4 sites where coupling pulls energy.
3. **Beltrami helicity boundary truncation.** h_local has ω·∇×ω in numerator, |ω|·|∇×ω| in denominator. At boundary cells where finite-difference ∇×ω truncates, |∇×ω|→0 → h_local divergence → κ_chiral·h_local pushes saturation kernel to crazy values.
4. **CFL violation at peak ω=0.93.** Default Cosserat timestep may be calibrated for lower amplitude; higher peak ω could violate wave-stability limit.

### 15.3 Diagnostic gate (~20 min) before any infrastructure work

External-agent audit (2026-04-24) flagged that the plan's PML diagnosis is plausible but not definitive. Running ~550 LOC of dynamic-mask infrastructure when the actual cause is asymmetric-init, helicity-truncation, or CFL would mean redoing the work.

**One-step diagnostic** measures, on the same Path B config that previously collapsed:
- max |ω|, max h_local, max coupling force per site
- Δenergy per site, masked by PML-ring vs interior
- max S_μ, max S_ε per site (look for division-by-near-zero)

**Localization analysis disambiguates the four candidates:**
- max Δenergy concentrated at PML inner boundary → PML truncation → infrastructure plan is right fix
- max Δenergy at soliton core → asymmetric-init or helicity-truncation → different remediation
- spatially distributed Δenergy → CFL violation → timestep adjustment, not boundary architecture

The diagnostic determines whether the strain-determined-boundary plan (§15.4) proceeds, gets revised, or is replaced.

### 15.4 Strain-determined-boundary architecture (proposed, gated)

If the diagnostic confirms PML as cause: replace static-PML active region with **dynamically-recomputed mask based on local strain A²**. Plan resides in `~/.claude/plans/read-through-th-kb-reactive-stardust.md`.

Key design decisions:
- **Threshold = α ≈ 7.3·10⁻³** (Phase II/III boundary per Vol 4 Ch 1, axiom-grounded, no free parameter)
- **10:1 hysteresis** (threshold_low = α/10) to prevent flicker at noise floor
- **Opt-in flag** `dynamic_mask: bool = False` — preserves backward compat for ~30 existing tests that depend on static-boundary semantics
- **PML retained** as outer safety layer beyond the strain-determined inner mask
- **Bound-state energy-flip counter must be exactly 0** for closed-system stable-soliton tests (any flip-loss for a claimed bound state means threshold wrong or soliton unbound)

Active-region radius for an electron at threshold α: r_active ≈ 3.84·r_opt ≈ 32 lattice units beyond core. Active-ball diameter ~64+ — needs **N≥80** for comfortable margin.

### 15.5 Risks the plan flags (also gated on diagnostic)

- **Dark-wake silent sink:** doc 49_'s DarkWakeObserver tracks τ_zx back-EMF at A² ≈ 10⁻⁶, far below α threshold. Under `dynamic_mask=True`, the dark wake gets clipped silently. For closed-system bound-state validation, irrelevant. For any DRIVEN experiment (cool-from-above, gate firings, future Hawking work), it's a silent energy sink that corrupts the radiative-tail observable. Explicit warning required in `vacuum_engine.py` docstring + any driven-experiment driver before they can be trusted with `dynamic_mask=True`.
- **Numerical stability of existing predictions:** dynamic mask changes the simulation domain. All registered `P_phase*_*` and `P_electron_*` predictions must be re-run under both `dynamic_mask` settings and agreement asserted within 5% on observable values. Disagreement above 5% is a flag for Grant — means the mask convention changes physics, not just the domain.
- **Mask jitter:** sites flickering active/inactive due to A² oscillating across threshold. Mitigated by 10:1 hysteresis; if still observed, add temporal smoothing (mask updated every N≥2 steps).
- **K4↔Cosserat asymmetry:** both sectors must share the same combined mask. Enforced via assertion in coupled step.

### 15.6 Methodology lessons folded into COLLABORATION_NOTES

Three Round 6 lessons added to [COLLABORATION_NOTES.md](../../.agents/handoffs/COLLABORATION_NOTES.md) rules 8 + 10:
- Rule 8 strengthening: corpus-search at architectural-decision time, not just at debug time. Vol 1 Ch 8:49-50's K4-TLM-exhausted note had been in the corpus for months while Stage 6 Phase 2/3 built node-level observers on K4 anyway.
- Rule 10 (new): empirical drivers catch what static analysis + preregistration miss. Three instances this session — Flag-5e-A, K4-exhaustion, Path B step-1. Run drivers early.
- Rule 10 corollary: prior-agent framings can be creepers like SM/QED imports. The "two-projections-of-one-tank" framing from §7 was repeated until §14.1 corrected it. Pressure-test prior framings against the corpus the same way you pressure-test SM/QED jargon.

---

*§15 added 2026-04-24 (late session) by Opus 4.7. Status: boundary-architecture plan exists in `~/.claude/plans/read-through-th-kb-reactive-stardust.md` but is gated on the §15.3 diagnostic to confirm which of four candidate causes is actually responsible for the Path B step-1 collapse. Methodology lessons from external review folded into COLLABORATION_NOTES rules 8+10.*

---

## 16. Path B / Path C empirical results + diagnostic findings

**Path B with damping** (`damping_gamma=0.1`, Cosserat-only seed at peak |ω|=0.3π): same step-1 catastrophic energy loss as without damping; thereafter chaotic slow decay over 800 steps. Brief transit through a (2,3)-preserving high-Γ² configuration around step 5 (shell_Γ²≈3.94, R/r≈3.29, c=3) but system leaves it; never settles. Convergence criterion (ΔE/E < 1e-4 AND velocity < 1e-3) never satisfied.

**Path C** (joint K4 V_inc + Cosserat ω seed, undamped): ENERGY RUNAWAY. Energy explodes from 2.59e3 to 1.05e10 by step 20 (factor of 4 million). Same step-5 brief (2,3)-preserving transit as Path B, then runaway amplification. Different failure mode than A or B.

**Diagnosis from three failure modes:** the K4↔Cosserat coupling `L_c = (V²/V_SNAP²)·W_refl(u, ω)` from doc 54_ §6 is multiplicative bilinear and exhibits BOTH known failure modes:
- No-bootstrap from cold (Round 5 step 5a finding: Cosserat A²_μ stuck at 0.012 under K4-only drive)
- Runaway from hot (Path C this round: energy → 1e10 from joint seed)

The brief step-5 transit through a (2,3)-preserving high-Γ² configuration appears in BOTH Path B and Path C at the same coordinate values — strongly suggestive of an unstable saddle in the dynamics rather than a stable fixed point. The (2,3) basin of attraction may not exist at all in the current engine's dynamics, OR the L_c coupling form is wrong.

**Status:** Path A/B/C all fail to validate single-electron formation. Round 6's pivot stands but the "single-electron representation" question is itself blocked on either (a) auditing the L_c coupling derivation, (b) building a spectral / scatter-matrix-eigenvalue solver to find true K4-TLM eigenmodes directly, or (c) reframing the problem under Grant's density-vs-saturation reading (§17 below).

---

## 17. Foundational thread: time, density-vs-saturation, universe-as-vortex

Late-session conversation surfaced three foundational reframes that may inform Path A/B/C interpretation. Documented here as Round 6 findings + followups.

### 17.1 Time = local clock rate from lattice strain

Grant's framing: time in AVE is the local refresh rate of the lattice, set by lattice strain. Twice the strain → half the refresh rate. This is gravitational time dilation as a lattice-level mechanism.

**Corpus status:** the chain is implicit but never assembled. [Vol 3 Ch 3 refractive-index-of-gravity](../../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md) explicitly states `c_local = c_0/n(r)` where `n(r) = 1 + 2GM/(c²r)`. [Doc 59_ §1.2](59_memristive_yield_crossing_derivation.md) derives `τ_relax = ℓ_node/c` as a lattice-fundamental time. Combining: `τ_local = ℓ_node/c_local = n(r)·τ_unstrained`. Exactly Grant's "twice strain → half refresh" formula. **The corpus has the pieces but no document writes the one-liner.**

**Engine status:** the engine treats `τ_relax = ℓ_node/c` as a global constant. No spatial n(r) modulation in the integrator. Acceptable for single-electron (gravity negligible), incorrect for cosmological / strong-gravity work.

**Followup F17-A:** add a one-line explicit derivation `τ_local = n(r)·τ_unstrained` to Vol 3 Ch 3. Currently implicit; should be stated.

**Followup F17-B:** when AVE-Core tackles strong-gravity or cosmological-scale work, the engine's τ_relax assumption needs revisiting. For Round 6 Path B/C this isn't blocking.

### 17.2 Density vs saturation — same scalar, two framings

Grant's hypothesis: maybe matter regions in the universe are LOW-density slipstream channels, surrounded by HIGH-density unstrained vacuum. "Density" being potentially distinct from "saturation."

**Resolution after analysis:** the engine's saturation kernel S = √(1 − A²) IS the local lattice density under Grant's framing. Same scalar, different label:
- A² = local field-energy density (fields² normalized to yield scales)
- **S = √(1 − A²) = local "free capacity" of lattice substrate = effective density of unfilled vacuum**
- S = 1 → unstrained vacuum, full capacity, behaviorally "high-density"
- S → 0 → fully saturated, behaviorally "low-density slipstream" where rupture impends
- Z_eff = Z₀/√S → ∞ as S → 0: low-density regions present infinite impedance to wave propagation (consistent with "empty space carries no waves")

**The engine has been computing this correctly all along — it just labels the quantity "saturation" rather than "density."**

#### 17.2.1 Engine field → physical-quantity mapping

The engine carries multiple fields. Three of them feed the saturation A² sum directly. Each represents a physically distinct energy-storage mode.

**Primary A² contributors (per [cosserat_field_3d.py:245](../../src/ave/topological/cosserat_field_3d.py#L245) + doc 54_ §6 K4 augmentation):**

| Engine field | Physical name | Tensorial type | Energy storage | LC analog |
|---|---|---|---|---|
| ε² (Cosserat strain, from u displacement + u-ω cross-coupling per Cosserat elasticity ε_ij = ∂_i u_j − ε_{ijk} ω_k) | **strain** | rank-2 symmetric | **electric / capacitive** (½ε₀E²) — translational deformation polarizes the substrate like a stretched capacitor | C-state of mechanical LC |
| κ² (Cosserat curvature = ∇ω) | **curvature** | rank-2 antisymmetric | **magnetic / inductive** (½B²/μ₀) — rotational gradient generates B-field-like circulation | L-state of rotational LC |
| V² (K4 port voltage, between A-B bonded sites) | **pressure** | scalar per port | **stored potential energy** (½CV²) — voltage difference / electrochemical potential between adjacent sublattices | C-state of K4 bond LC |

A² = ε²/ε_yield² + κ²/ω_yield² + V²/V_SNAP² = local sum of energies-from-three-storage-modes, normalized to per-mode rupture limits. Units: dimensionless, ranges [0, 1] before clipping. S = √(1−A²) is the inverse: the local lattice's remaining-capacity / free-substrate density.

#### 17.2.2 Other engine fields and their physical roles

These don't contribute to A² directly but are part of the dynamics:

| Engine field | Physical role | LC-tank role |
|---|---|---|
| Cosserat u | translational displacement | C-state position |
| Cosserat u_dot | translational velocity | L-state (current/momentum analog, electric) |
| Cosserat ω | angular velocity | L-state (rotational current/spin) |
| Cosserat ω_dot | angular acceleration | rate-of-change of rotational L-state |
| K4 V_inc, V_ref | port-voltage waves (forward/reflected) | C-state pressure waves on bonds |
| K4 Φ_link = ∫V_avg·dt | bond flux linkage | L-state of K4 LC (bond magnetic flux) |

**Conjugate pairs (each pair oscillates 90° phase-locked in a standing wave):**
- **K4 bond LC:** V_inc ↔ Φ_link
- **Cosserat translational LC:** u ↔ u_dot
- **Cosserat rotational LC:** angular position (implicit, integrated from ω) ↔ ω (angular momentum density)

#### 17.2.3 Implication for Path A/B/C seeding

> ⚠ **SUPERSEDED 2026-04-25** by [doc 68_](68_phase_quadrature_methodology.md) §6. The "three LC conjugate pairs" framing below treats Φ_link as an independent dynamical L-state of an independent LC pair. Empirically falsified in session 2026-04-25: the all_l mode (Φ_link + ω at amplitude, V_inc=0) produces step-by-step IDENTICAL trajectory to Path B (Cosserat ω only); E_k4 stays at exactly zero throughout 25 steps despite Φ_link seeded at amplitude. **Φ_link is a derived flux observable in K4-TLM** (time-integral of bond V_avg), not a primary state. The K4 bond LC stores energy in the (V_inc, V_ref) wave-pair structure; the L-state vs C-state distinction is encoded in the wave PHASE, not in a separate Φ_link state. Body preserved per COLLABORATION_NOTES Rule 12 as audit trail.

A bound (2,3) eigenmode requires phase relationships across all three LC pairs to be self-consistent under the engine's dynamics. The Path tests seeded only fragments:

- **Path A:** K4 V_inc only (one C-state of one LC pair). Φ_link, u, u_dot, ω all = 0. No oscillation in any pair; lattice is a static charge distribution.
- **Path B:** Cosserat ω only (L-state of rotational LC). V_inc, Φ_link, u, u_dot all = 0. K4 entirely silent; rotational LC has only momentum, no position.
- **Path C:** K4 V_inc AND Cosserat ω (mixed C-state + L-state from different LC pairs). Φ_link = 0 in K4, u = 0 in Cosserat. Two LC pairs each half-seeded.

None of these is a complete eigenmode initialization. A proper coupled-eigenmode seed would specify **either C-states everywhere (V_inc, u at amplitude; Φ_link, u_dot, ω at zero) OR L-states everywhere (Φ_link, u_dot, ω at amplitude; V_inc, u at zero)** — never both in the same LC pair. Path C's runaway may have a contribution from this — it didn't cleanly load energy into one half of each pair.

**Followup F17-I (new):** the proper "all-C-state" or "all-L-state" coupled seed has not been tried. Worth attempting before declaring the L_c coupling form structurally broken.

**Implication for Path A/B/C:** the relabeling doesn't change what the engine computes. The failure modes are coupling-dynamics issues, not density-vs-saturation issues. So this reframe doesn't directly unlock Path B; it sharpens the cosmological-scale interpretation.

**Followup F17-C:** add a paragraph to Ax4 documentation (Vol 1 Ch 1 or Vol 4 Ch 1) noting the duality: A² = local energy density, S = local free-capacity density. Both names describe the same scalar; choice of label is contextual (saturation framing for Bingham/yield discussions, density framing for cosmological-scale interpretation).

**Followup F17-D:** the slipstream-vortex cosmology framing (§17.3) needs the density label to make sense; the saturation label confuses "matter region" with "high-strain pocket" rather than "low-density channel."

### 17.3 Universe-as-vortex cosmology

Grant's intuition: maybe the universe is a primordial vortex — slipstream channels along which matter (galaxies, solar systems, stars) flows, surrounded by dense unstrained vacuum. Galaxy rotation curves, voids, large-scale structure as density-gradient phenomena rather than missing-mass phenomena.

**Corpus status:** **silent on vortex cosmology.** The corpus has lattice-genesis crystallization (doc 59_ §5.4, [Vol 3 Ch 4](../../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex)) and Hubble-as-crystallization-rate. Both linear / monotonic processes, no vortex content. [Doc 61_](61_cosmic_bipartite_k4_bh_interface_proposal.md) explores bipartite-A/B-sublattice as dark-matter mechanism — orthogonal to vortex framing.

**Followup F17-E:** if Grant develops the vortex cosmology beyond intuition, it would land as new content in Vol 3 Ch 4 or a new research doc. Major implications:
- Galaxy rotation curves explained by density-gradient dynamics, no dark matter required
- Cosmological voids = high-density crystal between slipstream channels
- Large-scale filaments = vortex tubes
- The Big Bang as a vortex-seeded crystallization event

This is potentially load-bearing for AVE's cosmological program. Out of scope for Round 6 single-electron work.

### 17.4 Misc followups (independent of foundational reframes)

**Followup F17-F:** [`cosserat_field_3d.py:752`](../../src/ave/topological/cosserat_field_3d.py#L752) hardcodes `omega_yield = π` without a derivation comment. Phase 5e v2 driver uses `omega_carrier = 2π/3.5 ≈ 1.795`. Ratio 0.571 = ω_Compton/ω_yield. Worth: (a) checking whether ω_yield = π has axiomatic justification or is a magic number, (b) documenting wherever it's set, (c) auditing whether "Compton frequency" is ω_yield or something else in the engine's natural units. Suspected dimensional inconsistency.

**Followup F17-G:** `solve_eigenmode_self_consistent` exists in [`tlm_electron_soliton_eigenmode.py:668`](../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py#L668) for K4-TLM only. Its analog for full coupled K4+Cosserat under VacuumEngine3D is not yet built. If we eventually want Hamiltonian-stationary fixed-point search in the full engine, this is the natural extension.

**Followup F17-H:** The L_c = (V²/V_SNAP²)·W_refl coupling in doc 54_ §6 is multiplicative bilinear and empirically exhibits BOTH no-bootstrap-from-cold and runaway-from-hot failure modes (per §16). Worth auditing the derivation chain for L_c — was it derived axiom-first or asserted from impedance analogy? If asserted, may need replacement with a coupling form that has stable fixed points at the (2,3) bound state.

---

*§16-§17 added 2026-04-24 (late session). Path A/B/C empirical results documented; foundational reframes (time, density-saturation duality, vortex cosmology) flagged with explicit followup items F17-A through F17-H. Round 6 single-electron validation is currently blocked on either L_c coupling audit (F17-H) or spectral-eigenmode methodology (F17-G); either is research-scope, not a quick patch.*

---

## 18. F17-I empirical results — three LC-pair-coherent seed modes

Built two new seeders — `initialize_u_displacement_2_3_sector` (Cosserat u) and `initialize_phi_link_2_3_ansatz` (K4 Φ_link) — and ran [coupled_engine_eigenmode.py](../../src/scripts/vol_1_foundations/coupled_engine_eigenmode.py) with three modes:
- **all_c**: K4 V_inc + Cosserat u seeded at amplitude (C-states); Φ_link, u_dot, ω = 0
- **all_l**: K4 Φ_link + Cosserat ω seeded at amplitude (L-states); V_inc, u, u_dot = 0
- **mixed** (Path C / F17-G original): K4 V_inc + Cosserat ω seeded; Φ_link, u, u_dot = 0

All amplitudes derived from doc 54_ §3 / §4 + doc 34_ §9.4 per Grant's directive (option ii). Sub-yield, sub-Φ_critical.

### 18.1 Results (single outer iter, N=48, R=12, r=R/φ²)

| Mode | Status | Iters | R/r at end | c | E_max/E_seed | peak \|ω\| at end | Mechanism |
|---|---|---|---|---|---|---|---|
| all_c | diverged at step 1 | 1 | 2.618 | 0 | 3020 | **1030** | Strain-driven force on ω → catastrophic ω growth in 1 step |
| **all_l** | **geometry_collapsed** | 2 | 0.20 | 0 | **0.30** | 0.36 | Energy bounded; ω relaxes; geometry diffuses outward |
| mixed | diverged at step 13 | 1 | 2.618 | 0 | 167 | 261 | Multiplicative L_c amplifies pre-loaded V²·W_refl |

### 18.2 Key empirical finding — all_l doesn't diverge

**all_l is the first seed that didn't blow up energetically.** Energy stayed BELOW seed (E_max/E_seed = 0.9). Peak |ω| DECREASED monotonically (0.93 → 0.55 → 0.35). The system is RELAXING, not amplifying.

But the (2,3) topology dissolves: R drops 12 → 1.5, r grows 4.58 → 7.05, c=0. The toroidal envelope diffuses into something approximately spherical/diffuse. The relaxation is real but it's not toward the (2,3) standing wave.

### 18.3 Diagnosis of the L_c coupling behavior across modes

The three failure modes when read together are diagnostic:

- **all_c (only C-states seeded):** at t=0, ε ≠ 0 from u, but ω = 0. The Hamiltonian's gradient `-∂E/∂ω` is nonzero (Cosserat energy density depends on ε which couples u and ω). Force on ω is large; ω accelerates explosively. This is the kinematic mirror of Path B's u-rolling problem.

- **all_l (only L-states seeded):** at t=0, ω ≠ 0, Φ_link ≠ 0, but u = V_inc = 0. The Hamiltonian's gradient `-∂E/∂u` is moderate. As dynamics releases u, it grows; meanwhile ω drains energy into the K4 sector via L_c coupling. **Result: energy flows Cosserat → K4 unidirectionally; ω relaxes; the toroidal envelope diffuses. There's no reverse channel pumping energy back into the Cosserat sector at the (2,3) frequency.**

- **mixed:** both V² and W_refl are pre-loaded simultaneously, giving positive multiplicative coupling gain. Runaway.

**This is a shape-of-coupling diagnosis.** A reciprocal LC coupling would have energy oscillating between sectors at ω_C — both directions, periodic. What we see in all_l is unidirectional energy flow (Cosserat → K4) without return. Combined with Path C's no-bootstrap-from-cold + runaway-from-hot, the L_c form `(V²/V_SNAP²)·W_refl(u, ω)` empirically behaves as a one-way energy pump rather than a reciprocal oscillator coupling.

### 18.4 Implication — F17-H now load-bearing

Three different LC-pair-coherent seed modes have been tested, all with axiom-derived amplitudes. None produces a (2,3) bound standing wave. Either:

(i) The (2,3) Hopf soliton is genuinely NOT a Hamiltonian fixed point of the current engine's coupled dynamics — the corpus's "electron is a (2,3) torus knot" is wrong-as-stated.
(ii) The L_c coupling form is the wrong shape — it's not reciprocal at the LC-tank level. Auditing doc 54_ §6 derivation (F17-H) is needed to understand whether L_c was axiom-derived or asserted.
(iii) The amplitudes ARE wrong despite derivation — some hidden non-linearity makes the bound state live at a different scale than my derivation expects.

(ii) is most consistent with the empirical pattern: all three seeds fail in exactly the way an asymmetric coupling would predict (one direction explodes, opposite direction relaxes monotonically, mixed amplifies). A symmetric LC coupling wouldn't show this asymmetry.

**Recommendation:** F17-H audit before any further engine work on Path B/C. If L_c is axiom-derived correctly, (i) becomes load-bearing and the corpus needs revision. If L_c is asserted, derive a corrected form first.

### 18.5 Followup F17-J — investigate all_l relaxation endpoint

The all_l mode's relaxation IS bounded and converges to SOMETHING (just not the (2,3) electron). What does it converge to? A non-toroidal but stable Hamiltonian fixed point of the current engine? Worth running for more iterations / steps to characterize the endpoint. May reveal whether the engine has any stable bound states under coupled dynamics, even if not the electron specifically. Defer until F17-H informs whether the engine's L_c is correct in the first place.

---

*§18 added 2026-04-24 (late session) by Opus 4.7. F17-I three-seed-mode empirical results: all_c catastrophic divergence, all_l bounded relaxation losing topology, mixed Path-C-style runaway. Pattern across modes empirically suggests asymmetric L_c coupling. F17-H audit becomes load-bearing.*
