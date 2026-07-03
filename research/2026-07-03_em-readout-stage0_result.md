# RESULT — EM-readout derivation, Stage 0 (analytic)

**Status:** RUN-COMPLETE (analytic). **VERDICT: [STUCK]** — a framing-level fork the analytics cannot settle, surfaced to Grant per his standing instruction (charter §3, "come to me if you get stuck"). The four candidate lanes are worked to the point where the fork is exposed; the fork is a physical-picture question (which sector carries the static Coulomb readout, and whether AVE's EM-transverse channel admits a static longitudinal solution at all), NOT a fork-to-computable Stage-1/2 can decide without a prior framing decision.
**Prereg (FROZEN):** [`2026-07-03_em-readout-stage0_prereg.md`](2026-07-03_em-readout-stage0_prereg.md) @ commit `b1e1cc18`.
**Charter:** [`_orchestration/2026-07-03_em-readout-derivation-charter.md`](../_orchestration/2026-07-03_em-readout-derivation-charter.md) @ `240cd1e2`.
**Branch:** `analysis/em-readout-stage0` (off `origin/main` @ `5bdc8d41`). NO self-merge.
**Classification (`consistency-vs-emergence`):** the derivation is FORM-EXISTENCE-class (does the medium have the coupling / the sector?), NOT a value/emergence claim. NO chord minted. The [STUCK] verdict mints no closure claim of any kind.

---

## 0. WHAT THIS DOC DOES

Works the four candidate mechanism lanes (prereg §2) against the four physics checkpoints (prereg §7) and the un-riggability ledger (prereg §4), grounded in the axioms first. Two lanes are killed with named contradictions; two survive to the point where they collide on a single unresolved framing fork. The fork is stated as the [STUCK] point and formulated as a plumber-physical question for Grant (§7).

Every step is tagged `consistency-vs-emergence`-class and carries an un-riggability ledger tag where a term is load-bearing.

---

## 1. THE AXIOM GROUND (what the substrate gives us before any mechanism)

Established from the canon (prereg §0.1 leaf-pull), verified verbatim @ `5bdc8d41`:

### 1.1 The three-channel impedance structure (sector-ownership, load-bearing)

The canonical three-impedance law (`three-channel-impedances.md`, Grant-ratified 2026-06-11) fixes the arena:

| Channel | Impedance | Domain | Γ at saturation | Owns |
|---|---|---|---|---|
| **EM-transverse (T2)** | Z_EM ≡ Z₀ ≈ 376.73 Ω | **electrical (Ω)** | **Γ_EM = 0 (matched, gapless)** | the photon (free); the (2,3) winding = charge (bound) |
| Shear / GW | Z_shear = ρc_shear | mechanical (Pa·s/m) | Γ_shear → −1 | deviatoric strain; the biquaternion leaf's "charge = shear/charge-3" slot |
| Bulk-longitudinal (A1) | Z_bulk = √2·ρc₀ | mechanical (Pa·s/m) | Γ_bulk → −1 | the A1 dilatation breather = **mass** (mₑc² = reactive bulk energy) |

**The load-bearing fact (`three-channel-impedances.md` discipline note):** only Z_EM is electrical. The "massless matched EM channel" the charter targets — the one that must carry the exact-1/r Coulomb readout — is the **EM-transverse (T2)** channel, Γ_EM = 0, gapless. `AXIOM-DERIVED` (three-impedance law; `electron-bh-isomorphism.md:24` Γ_EM=0 under SYM scaling; `z0-derivation.md`).

### 1.2 The Axiom-3 action is TRANSVERSE (curl-only)

Axiom 3's continuum action (`axiom-definitions.md:38–48`) is
$$\mathcal{L}_{node} = \tfrac{1}{2}\varepsilon_0\,|\partial_t \mathbf{A}_n|^2 - \tfrac{1}{2\mu_0}\,|\nabla \times \mathbf{A}_n|^2.$$
This has a `|∇×A|²` (curl) term and NO `|∇·A|²` or `|∇φ|²` (divergence/scalar) term. Its Euler–Lagrange equation is the transverse wave equation; its static limit is ∇×(∇×A) = 0, which for the transverse (∇·A=0) sector is ∇²A = 0 — but it carries **no longitudinal/scalar source term**. This is exactly why the compositeness engine leg found `fdtd_3d` curl-only with no Gauss sector (`compositeness-defense_engine-leg_result.md §1`): the AVE action-as-written IS the transverse-EM (Heaviside) action. `AXIOM-DERIVED`.

### 1.3 The A1/T2 port decomposition + the Heaviside precision note

The K4 4-port decomposes A₁ ⊕ T₂ (`k4-port-irrep-decomposition.md`). A₁ (common-mode, longitudinal, translational u) **DISSIPATES** in free vacuum via Op3 destructive interference; T₂ (transverse ω) survives as the photon. The leaf's §5 states this realizes "Gauss's law forbids longitudinal EM." **But** the decisive precision note (`historical-precedents.md:20–22`, Rule-12) sharpens it: "forbids longitudinal EM" is precise only for a *propagating* longitudinal WAVE — **the static Coulomb-longitudinal E is KEPT by Gauss's law itself (∇·E = ρ/ε₀ is a longitudinal component).** And: "the electron is where it returns: saturation is a volumetric/longitudinal effect… the longitudinal scalar re-engages as the confined state." `AXIOM-DERIVED` (K4 T_d symmetry) + the precision note is `CANONICAL` (a corpus disambiguation, not a new derivation).

### 1.4 The two "3"s / three-channel charge assignment (the sector-ownership tension, surfaced)

`master-equation.md:20` (the two-"3"s, Grant-ratified): the A1 dilatation-MASS "3" (Heaviside-excised longitudinal compression scalar, = mass) is ORTHOGONAL to the T2 Cosserat (2,3) WINDING "3" (= charge = Beltrami helicity H_bel = ∫ω·(∇×ω)). **A1 ⊥ T2 is the grade orthogonality.** The scope fence: "never wire the winding into the breather's own phasor."

**⚑ Flag (`flag-don't-fix`) — an intra-corpus sector-assignment tension I do NOT resolve:** the biquaternion leaf (`biquaternion-…-network-equations.md:70–71`) assigns charge = 𝓠_wind to the **shear/charge-"3"** slot (Im(w)), and A1 dilatation to bulk/mass. But `master-equation.md:20` + `k4-port-irrep-decomposition.md:26` put the (2,3) winding = charge on **T2/microrotational ω** (the EM-transverse channel). And `three-channel-impedances.md` says the charge readout must be on **EM-transverse (T2), the only electrical channel**. So the corpus carries the charge-winding in at least two named sectors (T2-microrotational-ω vs shear), which are different mechanical channels. This is not mine to adjudicate; it is surfaced because it is load-bearing for WHICH channel's dispersion sets the exterior falloff (§7 fork). Both readings agree the charge is NOT on the A1/bulk/mass channel — so the sector carrying charge is a transverse/shear (Γ→−1-at-saturation-in-mechanical / Γ=0-in-EM) sector, NOT the longitudinal-bulk mass sector.

---

## 2. LANE (a) — DYNAMIC PUMPING — KILLED (staticness + pump-null)

**The picture (prereg §2a):** the (2,3) winding is a persistent circulation in the ω (T2) sector at ω_C = c/ℓ_node. Via Ax1's intra-node LC coupling (rotation↔translation, μ↔ε; `axiom-definitions.md:16`), that circulation drives the translational sector, producing an exterior field.

**The derivation attempt + the checkpoint it fails.** The intra-node coupling is the LC oscillator relation: ∂ₜu ↔ ∇×ω (translation-rate couples to the curl of the rotation), which is `AXIOM-DERIVED` (`axiom-definitions.md:16`, the ε₀/E ⊥ μ₀/B LC coupling). A persistent winding gives ω(t) ∝ e^{iω_C t} (the circulation runs at the Compton frequency; `electron-identification.md` framing 7, LC-tank at ω_C). Feeding this through the LC coupling drives the translational sector at the SAME frequency ω_C:
$$\partial_t u \propto \nabla\times\omega \propto e^{i\omega_C t} \;\Rightarrow\; u(t) \propto e^{i\omega_C t}.$$

**STATICNESS checkpoint (prereg §7.1) — FAILS.** The driven translational field oscillates at ω_C; it is NOT static. A static exterior field needs ⟨exterior field⟩_time ≠ 0. Two sub-cases:

- **Linear coupling ⇒ zero DC.** The LC coupling as written is linear (∂ₜu ∝ ∇×ω); the time-average of a pure e^{iω_C t} drive is exactly zero. ⟨u⟩_time = 0. No static residual. This is the SAME null the Cleave displacement→charge pump computed (`clm-clvchn`: "the displacement→charge pump computed to zero," charter §1). The pump-null is not a coincidence — a linear reactive (lossless, Ax3) coupling of an oscillatory source time-averages to zero by construction.

- **Nonlinear rectification ⇒ needs a derived rectifier.** A non-zero DC residual requires a nonlinear (rectifying) term — a ⟨ω²⟩ or ⟨ω·∂ₜω⟩ that does not average to zero. The only nonlinearity in the axioms is Axiom 4's saturation kernel S(A) = √(1−A²), which enters as an even function of amplitude. To get a static DC field one would need to DERIVE a rectifying coupling from S(A) that produces a non-zero ⟨drive⟩_time. **No such rectifier is derivable at Stage-0 grade without inserting one** — and inserting a rectifier chosen to give 1/r is a `FORBIDDEN-INSERTION` (it back-fits the answer). The Beltrami-helicity charge H_bel = ∫ω·(∇×ω) IS a time-even quadratic invariant (a candidate DC source), but it is a BULK INTERIOR integral (violates the boundary-locality checkpoint §7.3, no-hair) and it is the charge LABEL itself, not a driver of an exterior translational field — reading it as a source of exterior E is exactly the winding-as-charge-source insertion the un-riggability rule forbids.

**Un-riggability ledger (lane a):**

| Term | Role | Tag | Cite / rejection |
|---|---|---|---|
| ∂ₜu ∝ ∇×ω (intra-node LC) | rotation drives translation | AXIOM-DERIVED | `axiom-definitions.md:16` |
| ⟨e^{iω_C t}⟩ = 0 (linear time-avg) | kills DC | AXIOM-DERIVED | Ax3 lossless-reactive ⇒ linear coupling ⇒ zero time-average |
| a rectifier giving ⟨drive⟩≠0 ∝ 1/r | would source static 1/r | FORBIDDEN-INSERTION | no derived rectifier; choosing one to give 1/r back-fits the answer |
| H_bel = ∫ω·(∇×ω) as exterior-E source | would source static field | FORBIDDEN-INSERTION (+no-hair) | this is the charge LABEL (bulk interior integral); reading it as exterior-E source = winding-as-charge-source insertion; violates boundary-locality |

**Verdict lane (a): KILLED.** The dynamic-pumping picture drives an OSCILLATORY exterior field at ω_C; its time-average is zero for the linear (lossless-reactive, Ax3) coupling — reproducing the pump-null (clm-clvchn) — and the only escape (a nonlinear rectifier) has no axiom-derived form and cannot be inserted without rigging. The winding's persistent circulation does not, by dynamic pumping, source a static exterior field. **The Cleave pump-null is the empirical shadow of this analytic kill.**

## 3. LANE (b) — STATIC STRAIN / DC-OFFSET — SURVIVES TO THE FORK

**The picture (prereg §2b):** the persistent winding imposes a STATIC strain on the surrounding lattice — a quiescent-point (DC) displacement in the translational sector that equilibrates outward with some falloff. Unlike lane (a), this is not a driven oscillation but a frozen offset: the winding is a permanent topological defect (Ax2, the loop cannot untie), so the neighboring nodes sit at a shifted operating point that does not oscillate. This is the substrate analog of a lattice dislocation's static strain field.

**The derivation.** A persistent topological defect in a Cosserat elastic crystal imposes a static displacement field u(r) satisfying the STATIC (∂ₜ=0) equilibrium equation of the translational sector. From Ax3's action, the static Euler–Lagrange equation of the translational sector is (with no time-derivative) the Cosserat micropolar equilibrium:
$$\nabla\cdot\boldsymbol\sigma = 0 \quad\text{(static, source-free exterior)},$$
which for the linear isotropic translational displacement reduces (exterior to the defect core) to the Navier/Laplace-class equation ∇²u = 0 outside the source (`AXIOM-DERIVED`: the static limit of Ax3's translational sector; the corpus's own gravity-strain treatment `n(r) = 1 + 2GM/rc²` `master-equation.md:104` is exactly a static-strain-equilibrating-outward field of this class).

**The falloff.** A static harmonic field (∇²u = 0) sourced by a localized defect, in 3D, has the multipole expansion u ∝ (monopole)/r + (dipole)/r² + …. **IF the defect carries a net monopole moment in the translational sector, the leading exterior term is 1/r (potential-shaped), field ∝ 1/r² — Coulomb.** This is the corpus's A_geom(r) = ℓ_node/r geometric confinement ratio (`claim-quality.md` clm-4r4jiy: A_geom ∝ 1/r is the potential; A_field ∝ 1/r² is the field). So lane (b), IF the winding sources a translational-sector monopole, gives exactly the 1/r potential / 1/r² field the anchor requires.

**MASSLESSNESS checkpoint (prereg §7.2).** The static equilibration is massless (∇²u = 0, Laplace, gapless ⇒ 1/r) ONLY IF the translational sector the strain lives in is gapless. Here is the sector-ownership crux (§1.4): the A1/bulk/translational sector is where the static strain would live — but that sector is the MASS sector (Z_bulk, Γ_bulk → −1 at saturation, mechanical), and the mass sector at saturation is NOT gapless (it forms the Γ=−1 wall). Two readings:
  - **(b-massless)** the static strain lives in the FAR-ZONE (r ≫ ℓ_node) linear regime where A → 0, S → 1, the lattice is cold, and the translational sector is the unsaturated massless bulk (c_bulk = √2·c₀, "Massless (propagates at c√2)" per `k4-port-irrep-decomposition.md:133`). Then ∇²u = 0 exterior ⇒ 1/r. This is the reading that gives Coulomb.
  - **(b-gapped)** if the readout rides the saturated bulk (the mass channel), it inherits the Γ_bulk → −1 mass and gives a gapped/Yukawa tail — which would be the gravitational-mass-scale field (the corpus's 1/r² gravitational refractive tail, Op14), NOT the electric Coulomb. This is Leaf B's exponential hedgehog (`substrate-perspective-electron.md:109`).

**LOCALITY-TO-BOUNDARY checkpoint (prereg §7.3).** A dislocation-style strain field is sourced by the defect's Burgers content (Ax2: the Burgers vector IS ℓ_node, `axiom-definitions.md:21`), which is a BOUNDARY/topological quantity, not an interior profile — this PASSES no-hair (the exterior 1/r monopole coefficient is set by the topological charge 𝓠, not by interior plumbing). `AXIOM-DERIVED` consistency with the boundary-observability rule.

**SUPERPOSITION checkpoint (prereg §7.4).** Linear static elasticity (∇²u = 0) is linear in the source ⇒ two windings' strain fields ADD ⇒ ∮ counts total 𝓠 EMERGENTLY (superposition of two 1/r monopoles gives monopole-2). PASSES — IF the far-zone is linear (reading b-massless).

**Un-riggability ledger (lane b):**

| Term | Role | Tag | Cite / rationale |
|---|---|---|---|
| ∇²u = 0 (static translational equilibrium, exterior) | the field equation | AXIOM-DERIVED | static limit of Ax3 translational sector; cf. `master-equation.md:104` gravity-strain |
| monopole term ∝ 𝓠/r | the 1/r potential | AXIOM-DERIVED **iff** the winding sources a translational monopole (see FORK) | the multipole leading term of a harmonic field; coefficient = topological content |
| the winding sources a translational-sector MONOPOLE | the load-bearing premise | **UNRESOLVED** — this is the fork (§7) | NOT derivable at Stage-0: is the (2,3) winding a monopole or a higher-multipole source in the translational sector? |
| far-zone = cold/linear/massless bulk (reading b-massless) | gives 1/r not Yukawa | ENGINEERING-CHOICE (physically motivated: A→0 far away) | rationale: at r ≫ ℓ_node, A→0, S→1; but WHICH sector (EM-transverse-T2 vs bulk-A1) the readout rides is the fork |

**Verdict lane (b): SURVIVES to the fork.** Static-strain equilibration gives a clean, un-riggable path to 1/r IF (i) the winding sources a net MONOPOLE in the translational sector, and (ii) that sector is the gapless far-zone bulk. Both (i) and (ii) are the fork (§7): the analytics cannot decide whether the (2,3) winding — which is a T2/microrotational (transverse) or shear object (§1.4), NOT an A1/longitudinal object — sources a net A1/longitudinal monopole at all, given the A1 ⊥ T2 orthogonality the corpus enforces.

## 4. LANE (c) — BOUNDARY / TOPOLOGICAL — SURVIVES TO THE FORK

**The picture (prereg §2c):** the linking integer 𝓠 = Link(∂Ω, F) as a BOUNDARY CONDITION on the translational sector's solution space. The exterior is source-free (∇²φ = 0); the integer 𝓠 forces a specific harmonic — a topologically-required monopole term — whose coefficient is 𝓠, like a residue / flux-quantization condition. This is the most un-riggability-exposed lane (it must derive Gauss-counting EMERGENTLY, without inserting ∮E·dA = 𝓠/ε₀).

**The derivation.** The winding 𝓠 = Link(∂Ω, F) is a linking number: the flux F threads the boundary ∂Ω a net 𝓠 times. In a source-free exterior, a harmonic field is fixed by its boundary data. A LINKING integer is precisely the data that fixes a multi-valued potential's period / the flux through a surface. There is a rigorous substrate-native candidate here: **the exterior field is source-free, and the linking integer sets the FLUX through any enclosing surface** — ∮ F·dA = 𝓠 (the linking number IS the enclosed flux, by definition of Link). IF the field whose flux is counted is the exterior E-field, then ∮E·dA = 𝓠·(unit) EMERGES from the definition of the linking number, and a source-free harmonic exterior with fixed total flux 𝓠 through every enclosing sphere is forced to be the 1/r² monopole (Coulomb) — because ∮E·dA = const over all radii, with ∇²φ = 0 exterior, uniquely gives E ∝ 1/r² (Gauss's theorem applied as a DIAGNOSTIC to the derived flux-quantization, not inserted as a constraint on ρ).

**This is the cleanest candidate — and it is where the un-riggability line is thinnest.** The move "∮E·dA = 𝓠 because 𝓠 = Link = enclosed flux" is EITHER:
  - **(c-emergent)** a genuine derivation: IF Link(∂Ω, F) is literally the flux of the exterior EM field E through ∂Ω (i.e. the field F in the linking definition IS the electric field, and the winding of that field through the boundary is what "charge = linking number" means), then ∮E·dA = 𝓠 is a THEOREM of the topology, and 1/r² follows. Gauss-counting is emergent (superposition of two linkings ⇒ total flux 2 ⇒ monopole-2, PASSES §7.4). This would be the [MECHANISM-DERIVED + 1/r] outcome.
  - **(c-inserted)** a disguised insertion: IF the field F in "𝓠 = Link(∂Ω, F)" is NOT the exterior E-field but the substrate flux (the Cosserat ω / Beltrami F_substrate, `boundary-observables-m-q-j.md:20` says F_substrate), then identifying its linking with the electric flux ∮E·dA is exactly the winding-as-charge-source step — `FORBIDDEN-INSERTION`. The linking of the SUBSTRATE flux is a T2/ω-sector (or shear-sector) quantity; asserting it equals the flux of the A1/longitudinal E-field is the cross-sector identification the whole exercise must DERIVE, not assert.

**The fork is: is F (in 𝓠 = Link(∂Ω, F)) the exterior E-field, or the substrate ω-flux — and if the latter, what DERIVES that its linking equals the electric flux?** The canonical definition (`boundary-observables-m-q-j.md:20`) says 𝓠 = Link(∂Ω, **F_substrate**) — the SUBSTRATE field, and its EE-projection is charge. So the corpus identifies substrate-flux-linking WITH charge by the projection dictionary (Ax2 TKI, [Q]≡[L]) — but that dictionary is a DEFINITIONAL identity (`def-tk1xfm`, "identity-by-translation, NOT a derivation," charter §1), not a derivation that the linking of the substrate flux SOURCES a 1/r exterior E-field. The `def-tk1xfm` ceiling is exactly the wall this lane hits.

**MASSLESSNESS / STATICNESS / BOUNDARY-LOCALITY.** IF (c-emergent) holds, all three pass: source-free exterior (static ∇²φ=0), gapless (1/r² not Yukawa), boundary-local (∮ over ∂Ω reads only 𝓠). The lane is clean on every checkpoint EXCEPT the one load-bearing identification (F = E-field vs F = substrate-flux).

**Un-riggability ledger (lane c):**

| Term | Role | Tag | Cite / rationale |
|---|---|---|---|
| ∇²φ = 0 (source-free harmonic exterior) | the field equation | AXIOM-DERIVED | static limit, source-free exterior |
| ∮E·dA = 𝓠 ⇒ E ∝ 1/r² (Gauss as DIAGNOSTIC of fixed flux) | forces Coulomb | AXIOM-DERIVED **iff** the counted flux is the exterior E-flux | Gauss's theorem applied to a derived flux-quantization; NOT ρ-inserted |
| **F (in Link) = the exterior E-field** | the load-bearing identification | **UNRESOLVED** — the fork (§7); `def-tk1xfm` ceiling | canon says F = F_substrate; equating its linking with electric flux is the definitional TKI, "identity-by-translation NOT a derivation" |
| ∮E·dA = 𝓠/ε₀ inserted as a constraint on ρ | the trap | FORBIDDEN-INSERTION | Gauss-with-winding-ρ is the refused coupling (charter §3.1); rejected |

**Verdict lane (c): SURVIVES to the fork.** The topological-boundary lane gives a rigorous 1/r² via flux-quantization IF the linking integer's flux IS the exterior electric flux. Whether that identification is a derivation (c-emergent) or a definitional restatement of Ax2's dictionary (c-inserted, the def-tk1xfm ceiling) is the fork (§7). It converges with lane (b) on the SAME unresolved question: does the T2/shear winding source a static A1/longitudinal (electric) monopole flux, or is that identity assumed?

## 5. LANE (d) — OTHER (saturation-boundary rectification) — SUBSUMED / KILLED

**The picture:** a mechanism specific to the Γ=−1 saturation wall — the wall rectifies the oscillatory winding into a static DC exterior condensate (a genesis-frozen DC offset that survives because the wall is a one-way / phase-change boundary). This is the most physically suggestive escape from lane (a)'s staticness kill (the historical-precedents note: "the longitudinal scalar re-engages as the confined state," `historical-precedents.md:22`).

**Why it is subsumed / killed at Stage-0 grade.** The Γ=−1 wall is a BULK/mechanical channel boundary (Z_bulk, Γ_bulk → −1; `three-channel-impedances.md`), and — critically — the EM-transverse channel is MATCHED at the wall (Γ_EM = 0; `electron-bh-isomorphism.md:24`). So the wall is EM-TRANSPARENT: it does not rectify the EM-transverse (charge-carrying) channel, because it presents no impedance mismatch there. A rectification at the wall produces a static field in the BULK/mass channel (the mass condensate, mₑc² = A1 breather) — which is the mass readout, NOT the electric Coulomb readout. This is exactly the sector-conflation the charter's leading hypothesis warns of: the wall's static longitudinal condensate is the MASS/gravitational sector (1/r² gravitational tail, Op14), not the electric 1/r. To get an electric static field from wall-rectification, one would need the wall to rectify the EM-transverse channel — but that channel is matched (Γ_EM=0), so there is no wall there to rectify against. `AXIOM-DERIVED` kill (Γ_EM=0 at the wall).

The FLASH-vs-LOCK / snap-channel that would birth such a condensate is itself corpus-UNRESOLVED (`the-abandoned-interior.md` Thread B: "the snap channel is structurally unavailable in the current engine, not falsified") — so even the mass-sector rectification is not derivable at grade. Lane (d) does not open a new route to a static ELECTRIC field; it re-lands on the mass sector, which is the wrong sector.

**Verdict lane (d): KILLED for the electric readout** (it produces a mass-sector, not EM-sector, static field, because the EM-transverse channel is matched at the wall) and SUBSUMED (its snap/rectification premise is corpus-unresolved).

## 5. LANE (d) — OTHER (saturation-boundary rectification) — SUBSUMED / KILLED

*[filled below]*

## 6. THE VALIDATE-ON-KNOWN GATE (why no lane can be declared MECHANISM-DERIVED yet)

Per prereg §8, no lane is declared MECHANISM-DERIVED until the known-EM anchors are reproduced. Both surviving lanes (b, c) converge on ONE unresolved identification (does the T2/shear winding source a static A1/longitudinal electric monopole?). Applying the gate:

| Known anchor | Lane (b) | Lane (c) | Gate status |
|---|---|---|---|
| test charge → 1/r² field | reproduced IFF the winding sources a translational monopole (the fork) | reproduced IFF Link's flux is the electric flux (the fork) | **BLOCKED at the fork** — the reduction to Coulomb requires the unresolved identification |
| superposition (fields add) | PASSES (linear static elasticity) IF far-zone linear | PASSES (linear flux-count) | passes, conditional on the fork resolving to the linear/massless reading |
| charge conservation (∮E·dA = 𝓠) | emergent from superposition of monopoles | emergent from Link = flux | passes, conditional on the fork |
| masslessness (long-range, atoms exist) | 1/r IFF far-zone is gapless bulk (b-massless); Yukawa if it rides the saturated mass channel | 1/r² IFF gapless EM channel | **the fork decides massless-vs-gapped** |

**The gate result:** every anchor reduces to Coulomb ONLY on the far side of the single fork (§7). The analytics establish that IF the winding sources a net static monopole in a GAPLESS channel, the 1/r Coulomb readout + F₁≡1 + Gauss-counting all follow cleanly and un-riggably. What the analytics CANNOT establish is the antecedent: whether the (2,3) winding — a transverse/shear (T2) topological object, held at 90° to the A1/longitudinal sector by the corpus's own grade orthogonality — sources a net static longitudinal-electric monopole at all, and if so in which of the three channels. No lane clears the validate-on-known gate; all are BLOCKED at the fork.

## 7. THE [STUCK] POINT — THE FORK, AND THE PLUMBER-QUESTION FOR GRANT

**Why this is [STUCK] and not [MECHANISM-AMBIGUOUS] (fork-to-computable).** Lanes (b) and (c) do not disagree on an observable Stage-1/2 could measure — they converge on a single PRIOR framing decision that no measurement resolves without first being made: **which substrate channel does the electron's static charge-field live in, and does the (2,3) winding source a static monopole in that channel across the A1 ⊥ T2 grade orthogonality?** A Stage-2 readout that measures "the exterior field of a seeded winding" cannot answer this, because the corpus does not yet say which channel's field to measure as "the charge field" — the three-channel structure (EM-transverse / shear / bulk) assigns charge to T2/shear and mass to bulk, and a static-longitudinal-electric field is not cleanly any of them. The measurement's INTERPRETATION depends on the framing decision. This is a `pre-test-physics-check` trigger-8 ontology fork, not a trigger-9 fork-to-computable — it must go to Grant before Stage-1 is even specified. (Guessing a channel and building Stage-1 to it would be exactly the "30+ commits then Mode-III" failure the discipline exists to prevent.)

**The two things the analytics DID settle (so the fork is sharp, not vague):**
1. Dynamic pumping (lane a) is KILLED — the winding's oscillation time-averages to zero (the pump-null); no static field comes from driving.
2. IF a net static monopole exists in a gapless channel, the 1/r Coulomb readout + F₁≡1 + Gauss-counting follow cleanly and un-riggably (lanes b, c agree). The ENTIRE weight of the derivation rests on the single antecedent below.

**The un-settleable antecedent (the fork):** the (2,3) winding = charge is a **T2/microrotational (transverse) or shear** object (`master-equation.md:20`, `k4-port-irrep-decomposition.md:26`, `biquaternion-…:71`). A static exterior Coulomb E-field is a **longitudinal** object (∇·E ≠ 0; `historical-precedents.md:20` "static Coulomb-longitudinal E"). The corpus enforces **A1 ⊥ T2** (mass-longitudinal ⊥ charge-transverse) as a grade orthogonality with a scope fence ("never wire the winding into the breather's phasor"). So the derivation needs a T2/shear (transverse/rotational) topological object to source a static longitudinal-electric monopole — a cross-grade coupling. The ONLY axiom-native place for it is Ax1's intra-node LC coupling (rotation↔translation) — but that coupling is OSCILLATORY (it killed lane a on staticness). The static version (lane b/c) requires the winding to impose a static longitudinal offset, which the grade orthogonality appears to forbid (T2 and A1 share no phasor). **Either the grade orthogonality has a static exception the corpus has not named, or the charge's exterior field is NOT a longitudinal-electric monopole (and "charge = winding" reaches the far zone by some other channel — or does not reach it at all, the SCREENED/ABSENT negative branch).** The analytics cannot pick; it is a framing decision about what the substrate physically does.

### 7.1 THE PLUMBER-QUESTION FOR GRANT (per your standing invitation)

> **The static-charge-field channel question.** In the vacuum-as-real-medium picture: the electron's *charge* is a transverse/rotational winding (the (2,3) on the Cosserat ω / shear sector — the "flywheel" side of the A1⊥T2 split). Its *mass* is the longitudinal A1 breather (the bulk-compression depression). A static Coulomb field that a distant test charge feels is a *longitudinal* thing — it has ∇·E ≠ 0, it pushes radially, it is the pressure-like field, not the shear-like or the circulating field. **So which pipe does the charge's static field actually come out of?** Three physically-distinct plumber pictures, and I cannot tell them apart from the axioms without your call:
>
> - **(A) Same pipe as mass, different valve.** The winding, being a permanent frozen defect, imposes a *static longitudinal offset* on the surrounding bulk (a DC depression, like a dislocation's static strain), and THAT longitudinal offset is the Coulomb field — sharing the A1/bulk channel with mass but as a separate DC component. This *works* (lane b gives clean 1/r) but it seems to violate the A1 ⊥ T2 grade orthogonality you ratified ("never wire the winding into the breather's phasor"). **Is there a static exception** — can a T2 winding impose a *static* (not oscillatory) A1 longitudinal offset without sharing the breather's oscillating phasor? (A frozen DC bias vs an AC drive — different objects; the orthogonality was stated for the phasor/AC coupling.) If yes, lane (b) closes at 1/r.
>
> - **(B) The charge field is the flux-quantization of the transverse winding itself, and "longitudinal" is the wrong frame.** The linking integer 𝓠 = Link(∂Ω, F_substrate) literally *is* the flux of the substrate field through the boundary; ∮ of that flux is 𝓠 by definition, and a source-free exterior with fixed enclosed flux is forced to 1/r² — no longitudinal A1 offset needed, the "charge field" is just the far-zone tail of the transverse/shear winding's own flux, and it *looks* radial (1/r²) because that is what a fixed-flux source-free harmonic must look like. This *also* works (lane c gives clean 1/r²) — **but it hinges on whether the linking flux of the substrate ω/shear field IS the electric flux a test charge feels, or whether equating them is just restating the Ax2 dictionary ([Q]≡[L]) without deriving that the far-zone tail is electric.** Is the `𝓠 = Link → charge` dictionary a *derivation* that the winding's flux reaches the far zone as an electric 1/r² field, or is it the identity-by-translation (`def-tk1xfm`) that stops at "we CALL the linking number the charge"?
>
> - **(C) It doesn't come out as a clean 1/r electric field at all — the charge's far field is the same as its mass's (gravitational 1/r²), and electrostatics-as-we-know-it is not what a lone winding sources.** The corpus's Leaf B (`substrate-perspective-electron.md:109`) says the winding's own field decays as an *exponentially-suppressed hedgehog*, with the only long-range survivor being the 1/r² *gravitational* refractive tail (Op14) — no separate electric Coulomb 1/r stated. If that is the literal truth of a single isolated winding, then "charge sources a Coulomb field" is a statement about winding-PAIR *interactions* (the clm-wcoul2 gapped-ω force between two windings), not about a single winding's static exterior field — and the single-charge Coulomb field would be a framework-level GAP (the SCREENED/ABSENT negative branch, charter §2), colliding with atoms-exist. **Is the single-winding exterior field genuinely a Coulomb 1/r, or is Coulomb only an emergent pair-interaction property, with the isolated winding's own tail being the hedgehog + gravitational-only?**
>
> **What each implies, one line each:** (A) → charge shares the bulk pipe with mass via a static-DC exception to A1⊥T2; lane (b) closes 1/r, Ax2 closes, F₁≡1 earned. (B) → charge's far field is the transverse winding's own flux-quantized tail; lane (c) closes 1/r², but only if `𝓠=Link→charge` is a derivation not a dictionary-restatement — which is the def-tk1xfm ceiling you'd be ruling on. (C) → the single-charge Coulomb field is NOT derivable / is a gap; Coulomb is a pair-interaction echo; the readout leg is a framework-negative, booked honestly.
>
> **The one thing I need from you:** which pipe (A, B, or C) — i.e., does a *lone* winding push a *static longitudinal* field into the far vacuum (A), or does its *transverse flux* quantize into the radial far field (B), or does a lone winding NOT source a clean electric Coulomb tail at all (C, Coulomb = pair-property only)? The math downstream of each is clean; I can't choose the physical picture without your read on whether the A1⊥T2 orthogonality has a static exception (A), whether `𝓠=Link` is a derivation or a dictionary (B), or whether Leaf B's hedgehog is the literal single-winding truth (C).

**Per your standing instruction, I STOP here and do not guess past the fork.** Stage-1 (the 6-DOF engine) and Stage-2 (the seeded readout) are NOT specified until the channel picture (A/B/C) is chosen, because the engine's coupling (which sector sources the exterior field) and the readout's interpretation (which channel's field is "the charge field") both depend on it. Building Stage-1 to a guessed channel is the pre-registered failure mode.

## 8. LEDGER SUMMARY + DISCIPLINE LEDGER

### 8.1 Per-lane verdict summary

| Lane | Verdict | Killed-by / survives-to | Exponent if derived |
|---|---|---|---|
| (a) dynamic pumping | **KILLED** | staticness: oscillatory drive time-averages to 0 (the pump-null, clm-clvchn); only escape (nonlinear rectifier) is a FORBIDDEN-INSERTION | — |
| (b) static strain / DC-offset | **SURVIVES to the fork** | clean 1/r IFF winding sources a translational monopole in a gapless channel — the fork | 1/r potential (1/r² field) *conditional* |
| (c) boundary / topological | **SURVIVES to the fork** | clean 1/r² via flux-quantization IFF Link's flux IS the electric flux (vs def-tk1xfm dictionary) — the fork | 1/r² field *conditional* |
| (d) other (wall rectification) | **KILLED for electric readout** | Γ_EM=0 at the wall ⇒ wall is EM-transparent ⇒ rectifies only the bulk/MASS channel, wrong sector; snap-channel corpus-unresolved | — (mass sector only) |

### 8.2 Un-riggability ledger tally (across all four lanes)

- **AXIOM-DERIVED terms:** 8 (the intra-node LC coupling; the Ax3-lossless linear time-average = 0; ∇²u=0 / ∇²φ=0 static equilibrium; the multipole leading term; boundary-locality via Burgers=ℓ_node; superposition via linearity; Γ_EM=0 at the wall; three-impedance channel structure).
- **ENGINEERING-CHOICE terms:** 1 (the far-zone = cold/linear/massless reading in lane b; physically motivated by A→0 but the sector is the fork).
- **FORBIDDEN-INSERTION terms (rejected on sight, NOT used):** 4 (a rectifier chosen to give 1/r; H_bel read as an exterior-E source; Gauss-with-winding-ρ; equating substrate-flux-linking with electric-flux by declaration).
- **UNRESOLVED (the fork):** 2 (does the winding source a translational monopole; is F-in-Link the electric field) — these are the SAME physical question in two lane-dialects, and they are the [STUCK] point.

**No term giving the 1/r answer was inserted.** The derivation reached the honest boundary: it can DERIVE that 1/r follows FROM a static monopole in a gapless channel, but it cannot DERIVE that the transverse/shear winding produces such a monopole, without a framing decision (A/B/C, §7.1) that is Grant's to make. This is the discipline working: the un-riggability constraints held; the answer was not back-fitted; the gap is named exactly where canon leaves it open (`claim-quality.md:1311`, `def-tk1xfm`).

### 8.3 Relation to the corpus's leading hypothesis (charter §1.8 sector-conflation ruling)

The derivation is CONSISTENT with, and sharpens, the leading hypothesis:
- **Leaf A** (`translation-circuit.md:541`, "~ℓ_node/r Coulomb leak") = the A_geom ∝ 1/r *potential* (clm-4r4jiy), the far-zone tail — which lanes (b)/(c) would produce as 1/r IFF the fork resolves to (A) or (B). Consistent.
- **Leaf B** (`substrate-perspective-electron.md:109`, exponential hedgehog + 1/r² gravitational-only) = the single-winding's own field per fork-option (C), OR the gapped-ω/mass-sector object. Consistent.
- The derivation does NOT confirm the ruling (it does not derive that Leaf A is the massless EM 1/r); it LOCALIZES the ruling's open half to the exact fork (A/B/C), which is the framing decision the ruling's "both true, different sectors" presupposes but does not establish. The sector-conflation ruling is the hypothesis that fork-option (A)-or-(B) is true and (C) is false; the derivation shows that is a framing choice, not yet a derivation. **Leaf sector-header corrections remain GATED / FLAGGED (not landed)** per the engine-leg prereg §5 gating rule — the fork must resolve first.

### 8.4 The bins that did NOT fire (and why)

- NOT [MECHANISM-DERIVED + 1/r]: no lane cleared the validate-on-known gate (§6); the 1/r is conditional on the unresolved fork, so F₁≡1 is NOT earned yet (it would be earned on fork-resolution to A or B).
- NOT [MECHANISM-DERIVED + non-1/r]: no departure profile was DERIVED (the fork blocks even the departure computation).
- NOT [MECHANISM-AMBIGUOUS]: the surviving lanes do not disagree on a Stage-1/2-measurable observable; they converge on a prior FRAMING decision no measurement resolves un-framed (§7 opening). This is why it is [STUCK], not fork-to-computable.
- **[STUCK] FIRED:** the framing fork (A/B/C, §7.1) is a physical-picture question routed to Grant per his standing instruction.

### 8.5 Discipline ledger

- **`substrate-native-check`:** the SM defaults (ρ(r), Poisson-solve, energy-basin) were walked and kept out (prereg §0); the derivation stayed in the three-channel / A1⊥T2 substrate frame throughout. CP4 (phase-space vs real-space) + CP10 (boundary-not-bulk) enforced (lane b/c boundary-locality checks).
- **`ave-canonical-leaf-pull`:** 12 canonical leaves enumerated BEFORE deriving (prereg §0.1); the coupling-class problem was grounded in the axiom+sector structure first.
- **`consistency-vs-emergence`:** every step tagged; the would-be closure is FORM-EXISTENCE / CONSISTENCY-class (matches dictionary-translated EM per prereg §5), NOT emergence, NOT a chord. NO claim minted (STUCK).
- **`ave-discrimination-check` Step 2.7:** the dictionary-translated comparison (prereg §5) is baked into the bins — a derived 1/r would be COULOMB-RECOVERY consistency (standard EM predicts 1/r-from-a-counted-integer via Gauss+multipole), not an AVE chord. Held.
- **`verify-before-cite`:** every file:line re-verified @ `5bdc8d41` this session (axiom-definitions:16/38-48; boundary-observables:20; k4-port-irrep:26/108-112/133; historical-precedents:20-22; the-abandoned-interior myth-guard; master-equation:20/24/104; translation-circuit:541; substrate-perspective-electron:109/113; claim-quality clm-4r4jiy/:1311; electron-identification:24-29/55; three-channel-impedances; biquaternion:70-71/80; engine-leg + gate0 results). PR #472 merge-state verified before branching.
- **`flag-don't-fix`:** TWO tensions surfaced with verbatim citations, NOT resolved: (1) the intra-corpus charge-sector assignment (T2-ω vs shear vs the biquaternion Im(w) slot, §1.4); (2) the core fork (A/B/C, §7). Neither was reframed to fit.
- **`pre-test-physics-check` trigger 8/9:** the framing fork surfaced mid-derivation was classified trigger-8 (ontology, → Grant) NOT trigger-9 (fork-to-computable), with the reasoning stated (§7 opening) — no Stage-1/2 measurement resolves it un-framed.
- **`phase-space-coordinate-check`:** the (2,3) phase-space label was kept distinct from the real-space exterior E(r) target throughout (prereg §0.3).
- **INVARIANT-N1:** no new substrate noun introduced; all substrate objects (A1 breather, T2 winding, Cosserat ω, Γ=−1 wall) are existing prose-only nouns.
- **Lattice-derived discipline (Grant memory):** no forbidden hand-wired coupling introduced; the 1/r answer was NOT back-fitted; the gap is named where canon leaves it open.

---

> **Next step (gated on Grant):** the fork-resolution (A/B/C, §7.1). On (A) or (B) → lane (b)/(c) closes at 1/r, Stage-1/2 become VERIFICATION of a derived result, the Ax2 readout leg closes, F₁≡1 earned (auditor lands the axiom-register + sector-header updates). On (C) → the framework-negative branch is booked (single-charge Coulomb is a gap; Coulomb = pair-property; charter §2 highest-stakes negative), no rescue (Rule 11). Either verdict is recorded per Grant's standing instruction.
