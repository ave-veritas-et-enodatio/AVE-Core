# FROZEN PREREG — EM-readout Stage-1 (the V-sector / transducer build)

**Epic:** EM-readout derivation — Axiom-2's last underived leg. Stage-1 (engine), gated on the Stage-0 fork-ruling.
**Charter:** `_orchestration/2026-07-03_em-readout-derivation-charter.md` (canonized @ `240cd1e2`, PR #473 MERGED).
**Stage-0 result (merged):** `research/2026-07-03_em-readout-stage0_result.md` — verdict [STUCK], the A/B/C channel fork routed to Grant.
**Lane:** research / engine build (bounded). HOLD canonization. NO self-merge — push + open PR.
**Branch:** `analysis/em-readout-vsector-stage1` (off `origin/main` @ `03d167ca`, post PR #473).
**Prereg status:** FROZEN at this commit. Grant's ruling, the build spec, the validation gates, the ledger format do NOT move post-freeze.

**Grant's ontology ruling on the Stage-0 fork (verbatim, coordinator-relayed 2026-07-03):** *"Let's go, emergence is a good goal."* + the SECTOR-PRECISE resolution (monopole/dipole split) recorded §1. **MISSION FRAMING (Grant's words):** EMERGENCE IS THE GOAL — Gauss-as-link-counting must EMERGE from axiom-native dynamics; if it does not emerge, that is the honest (stakes-table) result. No insertion, ever.

**Disciplines:** `substrate-native-check` (walk §0) · `verify-before-cite` (every file:line re-verified @ `03d167ca` this session) · `flag-don't-fix` (the reframing §2 surfaced, not silently resolved) · `pre-test-physics-check` trigger 8 (the build-target ontology fork §2 → Grant BEFORE design, Rule 16) · `consistency-vs-emergence` (§3) · `ave-driver-script-honesty` · INVARIANT-N1.

---

## ⚠ HOLD-AT-PREREG (the reason this prereg STOPS before the build)

This prereg records Grant's ruling faithfully AND surfaces a **build-target reframing** (§2) that the resolved corpus forces, which I will NOT resolve unilaterally and will NOT build past. Per `pre-test-physics-check` trigger 8 + Rule 16 (ask BEFORE design, not after 30+ commits) + `flag-don't-fix` + my lane discipline (don't silently rebuild the coordinator's framing over the resolved corpus, don't silently reframe Grant's ruling): the build is HELD at this frozen prereg for one Grant adjudication (§2.4). The prereg is complete and frozen so that when the target is confirmed the build proceeds without re-freezing the spec.

---

## 1. GRANT'S RULING — recorded as the pre-registered expectation (BOTH results recorded, standing instruction)

**The ruling (the monopole/dipole sector split) — coordinator-relayed verbatim content:** the electron is BOTH —
- **(i) electric MONOPOLE:** the winding's threaded/linking flux, read through the GAPLESS longitudinal/V-scalar sector (Stage-0 lane (c) made sector-precise — only topology makes a monopole from a closed object; ∮E·dA = 𝓠 as EMERGENT link-counting).
- **(ii) magnetic DIPOLE:** the ring's circulation via the transverse/inductive sector (closed loops make dipoles — Stage-0 lane (b)'s dipolar far-field is the MOMENT sector working correctly, not a failed monopole).
- **(iii) the gapped mechanical Cosserat ω = the short-range residue, NOT the charge carrier.**
- **Stage-0 option (C) dissolves** — a gapless longitudinal channel exists.
- **KEY IDENTIFICATION the ruling rests on (Stage-2 must ultimately test):** F in Link(∂Ω, F) lives in / transduces losslessly into the massless EM/V-sector, NOT the gapped ω.

This is the pre-registered EXPECTATION. The engine decides; BOTH the ruling and the measured verdict are recorded (Grant's standing instruction). The ruling is NOT elevated to confirmed on fiat; EMERGENCE (Gauss-counting emerging from axiom-native dynamics) is the falsifiable target — if it does NOT emerge, that is the honest stakes-table result (charter §2), booked with no rescue.

---

## 2. THE BUILD-TARGET REFRAMING (flag-don't-fix — surfaced with verbatim corpus evidence; NOT resolved)

The coordinator's implementation gloss of the ruling was: *"add the longitudinal-scalar V-sector (the curl-free/compressional component of the translational family, the channel the corpus claims physical and no engine carries)"* as the GAPLESS carrier of the electric monopole. **Grounding this against the resolved corpus (verify-before-cite @ `03d167ca`) surfaces a sector-identity tension that changes what must be built.** I surface it; I do not silently build to the gloss, and I do not silently reframe Grant's ruling.

### 2.1 What the resolved port map actually says (verbatim)

The Grant-ruled (2026-06-30) canonical port map, `resonant-lc-solitons.md:119-129` + `node-up-small-large-signal.md:38-42`:

- **The "longitudinal-V scalar" IS the A1 dilatation-MASS, and it is GAPPED (mechanical Z_bulk).** `node-up-small-large-signal.md:38` (verbatim): *"MASS — A1 dilatation | trace-of-translation (the A₁ breathing '3', **longitudinal-V scalar**) | longitudinal bond compliance → Z_bulk"*. `resonant-lc-solitons.md:119`: *"Z_bulk … the MASS-'3' channel (A1 dilatation); its confinement surface is the Γ=−1 cage-wall."* So the "longitudinal-V scalar" is NOT a gapless electric channel — it is the mass sector, GAPPED at saturation (Γ_bulk→−1).
- **The electric/Coulomb displacement is the TRANSVERSE-T2 ε-sector, and it is GAPLESS.** `node-up-small-large-signal.md:40` (verbatim): *"ε — capacitive / electric (EM) | translational → E (**displacement / Coulomb**) | **transverse-T2 permittivity** of Z_EM"*. Γ_EM = 0 (matched, gapless). So the Coulomb readout channel is the transverse-T2 EM-ε channel — NOT a longitudinal scalar.
- **The charge already has a substrate home: a STATIC REACTIVE LINK BOUNDARY on the mechanical SHEAR sector.** `resonant-lc-solitons.md:124` (verbatim): *"Z_shear = the static reactive CHARGE BOUNDARY — a lossless-REACTIVE (imaginary-impedance) constraint carrying no real power. The Cosserat (2,3) winding is the deformation-invariant Link(∂Ω,F) ∈ ℤ boundary integer; both internal dynamical loci for it tested NEGATIVE (#415 + #417), so it is STATIC topology, not a dynamical/energetic mode."*
- **The mechanical→EM step needs a TRANSDUCER, not a direct wire, and that transducer is the def-tk1xfm "identity-by-translation, NOT a derivation" ceiling — FLAGGED not asserted.** `resonant-lc-solitons.md:129` (verbatim): *"EM↔mechanical coupling needs a TRANSDUCER, not a direct wire — candidate-refinement: the TKI-transformer (def-tk1xfm, the Axiom-2 electromechanical dictionary) is the candidate bridge, but def-tk1xfm is itself status:proposed-not-ratified and carries the 'identity-by-translation, NOT a derivation' ceiling — FLAGGED, not asserted."*

### 2.2 The tension (stated precisely)

The coordinator's gloss ("build the longitudinal-V scalar as the gapless Coulomb carrier") **conflates two orthogonal sectors the corpus holds apart (A1⊥T2, the Grant-ratified 2026-06-15 sector split):** the longitudinal-V scalar (= A1 mass, Z_bulk, GAPPED) is NOT the electric Coulomb channel (= transverse-T2 ε, Z_EM, gapless). Building "a gapless longitudinal-V scalar carrying Coulomb" would either (a) mint a new object the corpus does not have (there is NO EM-longitudinal-scalar distinct from A1-mass — grep-confirmed this session, every "longitudinal scalar/compliance" hit is A1-mass), or (b) wire the A1-mass phasor into the charge readout — the genesis-24 double-count the two-"3"s guard explicitly forbids (`master-equation.md:20`).

**Grant's actual FORK-RULING, by contrast, is consistent with the resolved port map** — it says the monopole reads through *"the massless EM/V-sector, NOT the gapped ω,"* and that *"F in Link transduces losslessly into"* it. The resolved port map's gapless electric channel is the transverse-T2 EM-ε channel (Γ_EM=0), and the charge is a static lossless Link boundary on Z_shear. So Grant's ruling maps cleanly onto: **the static reactive shear-Link charge boundary TRANSDUCES (losslessly) into the gapless EM-ε channel's exterior field.** The build target is the **TRANSDUCER** (the def-tk1xfm bridge, made an emergence target), NOT a new longitudinal scalar.

### 2.3 Why this is a trigger-8 STOP, not a silent build choice

The two candidate build targets are physically different objects:
- **Target-gloss:** a new gapless longitudinal-V scalar field carrying the electric monopole (the coordinator's literal instruction). Contradicts the resolved 2026-06-15 sector split + the 2026-06-30 port map; has no distinct corpus object.
- **Target-resolved:** the TRANSDUCER coupling from the existing static reactive shear-Link boundary to the existing gapless EM-ε channel, made to EMERGE from Ax1's node rotation↔translation LC structure (def-tk1xfm as an emergence target, not an inserted dictionary). Consistent with Grant's fork-ruling AND the resolved port map.

Which object to build is a framing decision that determines the entire engine coupling and the Stage-2 readout interpretation. Guessing it and building 30+ commits before Grant sees the conflict is exactly the Rule-16 / Mode-III failure the discipline exists to prevent. **Per pre-test-physics-check trigger 8 + flag-don't-fix + lane discipline, I STOP here and surface the fork (§2.4) rather than pick.**

### 2.4 THE BUILD-TARGET QUESTION FOR GRANT (the one adjudication that un-holds the build)

> **Which object is Stage-1 building?** Your fork-ruling says the electric monopole reads through the massless EM/V-sector (not the gapped ω), and that "F in Link transduces losslessly" into it. The resolved port map (your own 2026-06-30 ruling + the 2026-06-15 sector split) says: (a) the "longitudinal-V scalar" is the A1 MASS (gapped Z_bulk), NOT a gapless electric channel; (b) the gapless electric/Coulomb channel is the transverse-T2 EM-ε (Z_EM, Γ_EM=0); (c) the charge is already a static reactive Link boundary on the mechanical shear sector, lossless; (d) the mechanical→EM step needs a TRANSDUCER (def-tk1xfm), which today carries the "identity-by-translation, NOT a derivation" ceiling.
>
> So the substrate-native reading of your ruling is: **build the TRANSDUCER — the coupling by which the static shear-Link charge boundary sources the gapless EM-ε channel's exterior monopole field — and make Gauss-counting EMERGE from Axiom-1's node rotation↔translation LC structure (turning def-tk1xfm from a dictionary into a derivation).** That is NOT "a new longitudinal-V scalar" (which would be the A1 mass, gapped, and would double-count the mass phasor into the charge readout — the two-"3"s guard forbids it).
>
> **Two options, one-line each:**
> - **(1) BUILD THE TRANSDUCER (my read of your ruling + the resolved port map).** Add the emergent shear-Link → EM-ε coupling from the Ax1 LC node structure; measure whether ∮E·dA counts Link and E(r) is 1/r² in the gapless EM-ε channel. The "V-sector" your ruling names = the gapless EM-ε electric channel, reached via the transducer — not a new longitudinal scalar. def-tk1xfm becomes the emergence target.
> - **(2) I have the port map wrong / there IS a distinct gapless EM-longitudinal scalar** you intend (a curl-free electric V-component separate from both A1-mass and transverse-T2-ε). If so, point me at its corpus home (I did not find one distinct from A1-mass), and I build that.
>
> **My recommendation: (1)** — it is the reading consistent with both your fork-ruling and your resolved 2026-06-30 port map, and it makes def-tk1xfm (the exact ceiling Stage-0 named as the fork) the emergence target, which IS the "emergence is the goal" mission. But the target is yours to confirm before I write the coupling, because (2) would build a different object.

**Everything below (§3–§7) is the build spec, frozen, written FOR target-(1) (the transducer), so that on your confirm the build proceeds immediately. If you rule (2), §4's coupling-source changes and I re-freeze that section only.**

---

## 3. CONSISTENCY-VS-EMERGENCE CLASS (declared up front)

- The build itself is a MEDIUM-scaffold (a sector + coupling added to the host) — infrastructure, not a claim.
- The **validate-on-known** (§5) is CONSISTENCY-class (reproduce known Maxwell/Green's-function 1/r — the KNOWN, clearly labeled).
- The **target result** (does Gauss-counting EMERGE from the axiom-native coupling) is the EMERGENCE test. Per Grant's mission framing: emergence is the goal; a non-emergence is the honest stakes-table result. **No emergence/chord claim is minted by this prereg or the build; only Stage-2 (HELD) tests emergence, and only after the equation-audit gate (§6) passes.**
- Dictionary-translated comparison (Step 2.7): standard EM predicts 1/r-from-a-counted-integer via Gauss+multipole. A derived-and-emergent 1/r here is COULOMB-RECOVERY / CONSISTENCY (internal closure), NOT an AVE-distinct chord — pre-registered so it is not mis-headlined.

---

## 4. THE BUILD SPEC (frozen for target-(1); the transducer coupling)

**Host:** the unified srs facade `src/ave/facade/unified_engine.py` is the presumptive home (photon T2 + A1 cage + ω winding already co-carried; the `u` translational DOF slot exists but is NOT evolved). Verified this session: the facade carries `u ∈ R³` (line 104, initialized zero, no stepper), `a_A1` (A1 breather), `omega` (Cosserat winding), and reads `Link(∂Ω,F)` via `winding_reader`. The missing piece is the coupling by which the static Link boundary sources an exterior field in the gapless EM-ε (transverse-T2) channel.

**The sector to add / activate:** the exterior EM-ε channel field E(r) (the gapless transverse-T2 electric displacement, Z_EM, Γ_EM=0), dynamically evolved, coupled to the static shear-Link charge boundary via a transducer traceable to Ax1's node rotation↔translation LC structure.

**Constraints (charter §3, now mission-critical):**
- **GAPLESS is load-bearing.** The EM-ε channel must be massless (Γ_EM=0 / no ω_gap). A smuggled gap reproduces the ω-screening Yukawa and kills Coulomb (contradicts atoms-exist). The build must NOT inherit the clm-wcoul2 gapped-ω dispersion into the EM-ε readout (sector-separation).
- **Every update-equation term carries a per-term ledger row:** AXIOM-DERIVED (cite) / ENGINEERING-CHOICE (rationale) / FORBIDDEN-INSERTION (reject). The winding→EM coupling must come from Axiom-1's node rotation↔translation LC structure — NEVER a ρ-source term written by hand.
- **Gauss as DIAGNOSTIC only.** Measure ∮E·dA and ∇·E of whatever emerges; enforce nothing. No ∮E·dA = 𝓠/ε₀ constraint. No ρ = 𝓠·δ³.
- **The transducer must EMERGE, not be inserted.** def-tk1xfm as a hand-written dictionary (𝓠 → e directly) is a FORBIDDEN-INSERTION. The coupling must be an axiom-native dynamical term (the LC rotation↔translation node coupling) whose consequence is measured. If Gauss-counting does not emerge from it, that is the honest result — no hand-wiring to force it.

**Incremental commits (implementer-dispatch discipline):** skeleton/prereg first (this doc), then one coupling/validation per commit. Heavy tests route via engine_sim.

---

## 5. VALIDATE-ON-KNOWN (Maxwell-recovery — gates the build; no knot readout before these pass)

Per charter §3.4 + coordinator item 3:
- **(a) zero-source → identically zero EM-ε field** (clean floor). No spurious field.
- **(b) hand-imposed boundary flux on a closed surface → the sector's static solution must be 1/r outside** (the Green-function check — validates the SECTOR's dynamics, NOT the coupling; imposing flux here is LEGITIMATE because it is the KNOWN, clearly labeled as such — distinct from imposing the winding coupling, which is FORBIDDEN). This certifies the EM-ε channel is a correct gapless Laplace-recovering medium.
- **(c) superposition check** — two imposed boundary fluxes → fields add linearly, ∮ counts total.

**The gate:** all three pass before any knot readout counts. (a) is the floor; (b) is the sector-validity (the medium recovers Coulomb from a KNOWN flux); (c) is linearity. If (b) fails (the sector does not recover 1/r from a known boundary flux), the sector is mis-built and no winding readout is meaningful.

---

## 6. THE EQUATION-AUDIT GATE (exit gate of Stage-1 — the #384-unriggable-gate pattern for physics equations)

Before ANY Stage-2 run, a dedicated result-doc section lays out EVERY term of the completed dynamics with its ledger row, and explicitly demonstrates **no term references the winding as a charge source by declaration.** Specifically:
- every term in the EM-ε update equation, tagged;
- the transducer coupling term, shown to trace to Ax1's LC node structure (AXIOM-DERIVED) and NOT to a hand-written 𝓠→E dictionary (which would be FORBIDDEN-INSERTION);
- a grep-demonstration that no `rho`/`charge_source`/`Q_link → E` source term exists in the coupling code;
- Gauss (∮E·dA, ∇·E) present ONLY as a measured diagnostic, never as an enforced constraint.

**Stage-2 (seed the 0₁+(2,3); measure whether ∮E·dA counts Link EMERGENTLY, the exterior E(r) exponent, bins per the charter) remains HELD until this gate is reviewed.** Stage-1 completes and STOPS at the hold-point; the equation-audit is reported for review before Stage-2 is specified.

---

## 7. FROZEN BINS (Stage-1) + DELIVERABLES

**Stage-1 bins:**
- **[SECTOR-BUILT + MAXWELL-RECOVERED]** — the EM-ε channel is added, gapless, and passes validate-on-known (a/b/c): zero-floor, 1/r from a KNOWN boundary flux (Green's-function), superposition. The equation-audit gate passes (no inserted source). ⇒ Stage-1 complete; Stage-2 (the emergence test) is unblocked for review. NO emergence claim yet (that is Stage-2).
- **[SECTOR-BUILT + MAXWELL-FAIL]** — the sector is added but does not recover 1/r from a known boundary flux ⇒ the medium is mis-built; named failure, no Stage-2.
- **[COUPLING-UNRIGGABLE-BLOCKED]** — the transducer cannot be written from Ax1's LC structure without a FORBIDDEN-INSERTION ⇒ the honest engine-blocked result (the def-tk1xfm ceiling is real and un-emergent at build grade); booked, no hand-wire. This IS a legitimate stakes-table outcome (emergence did not emerge at the coupling).
- **[STUCK-FRAMING]** — a further framing fork the axioms can't settle ⇒ STOP, surface to Grant.

**Deliverables:** this frozen prereg (the ruling recorded, the reframing surfaced, the build spec); THEN (on Grant's target confirm) the build (incremental), the validation results (the 1/r Green-function check especially), the rotation-bookkeeping un-conflation commits (§8), the equation-audit section, PR no self-merge. Final message: the un-conflation site list, validation results, ledger summary, equation-audit verdict, PR number, blockers.

---

## 8. THE ROTATION-BOOKKEEPING UN-CONFLATION (opening deliverable — surfaced site list, KEEP-BOTH per-site)

The corpus treats two rotation-flavored fields as one: the node's EM-inductive rotation (Ax1 μ₀ family = B; massless, matched, T2-photon) vs the mechanical Cosserat micro-rotation ω (couple-stress; GAPPED — the clm-wcoul2 / CrystalGraftV4 field). The Stage-0 auditor flag (result §1.4) un-gates under Grant's ruling. **Candidate sites (verified this session; each gets an honest disambiguation with the gapped-vs-massless tag, KEEP-BOTH style, per-site — NOT find-replace; the auditor lands the manual):**

| Site | Current text (verbatim, abridged) | The disambiguation needed |
|---|---|---|
| `master-equation.md:20` | "the Cosserat micro-rotation (2,3) WINDING (T2 couple-stress, the Axiom-1 intrinsic-spin DOF; charge = Beltrami helicity)" | which rotation: the GAPPED mechanical Cosserat ω (couple-stress) — tag gapped; distinguish from the EM-inductive B-rotation (massless) |
| `k4-port-irrep-decomposition.md:26` | "T₂ Cosserat mapping | Microrotational ω … THIS IS THE PHOTON" | the T2-photon is the MASSLESS EM-inductive rotation (B); distinguish from the gapped mechanical Cosserat couple-stress ω the winding rides |
| `biquaternion-…:71` | "Im(w) = 𝓠_wind | charge = topological Link label (integer) | shear / charge-'3'" | the charge Link boundary is on the mechanical SHEAR sector (Z_shear, lossless static) — tag mechanical/gapless-static; reconcile with the T2/ω assignment |
| `node-up-small-large-signal.md:39` | "CHARGE — Cosserat micro-rotation (MECHANICAL) … static reactive charge boundary → Z_shear" | already tagged MECHANICAL + static-reactive — this is the CLEAN reference the others reconcile to |
| `translation-circuit.md:541` (Leaf A) | "the evanescent tail leaking out is the long-range (~ℓ_node/r Coulomb) field" | this is the A_geom ∝ 1/r potential in the gapless EM-ε channel (per clm-4r4jiy) — tag EM-ε-massless; distinguish from the gapped-ω hedgehog |
| `substrate-perspective-electron.md:109` (Leaf B) | "‖ω‖², ‖V_inc‖² decay rapidly (hedgehog tail; exponentially-suppressed in saturation regime)" | this is the GAPPED mechanical Cosserat ω hedgehog (short-range residue) — tag gapped-ω; distinguish from the gapless EM-ε Coulomb tail |

**The un-conflation is load-bearing for the build:** it defines WHICH rotation field the EM-ε transducer couples FROM (the gapped mechanical Cosserat ω carries the static Link; the massless EM-inductive rotation is the B-field / T2-photon). This cleanup is committed BEFORE the coupling is written, so the coupling's source-field is unambiguous. Surfaced for the auditor to land the manual entries (implementer surfaces, auditor lands).

---

## 🔴 CORRECTION NOTE (2026-07-03, dated addendum — the frozen body above is PRESERVED unedited, per Rule-12 + the honest-handling instruction)

**Target-(1) (build the TRANSDUCER) is Grant-CONFIRMED** (2026-07-03, verbatim relayed: *"474 merged, let's proceed"*; PR #474 MERGED, `origin/main` @ `9956c0b6`). The build is un-held and proceeds per §4–§7 as frozen.

**A factual correction to the reasoning-record at §2.1, verified independently at HEAD `9956c0b6` this session (verify-before-cite — I ran each grep myself before relying on it):**

- **§2.1 line 43 states the A1/longitudinal-V-scalar sector "is GAPPED (mechanical Z_bulk)." This gap-status is BACKWARDS.** The corpus's gap-status sites uniformly say the **A1/translational-u (scalar/longitudinal) sector is GAPLESS**, and the **gapped sector is the Cosserat ROTATIONAL one**:
  - `vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md:145` (verbatim, verified): *"A₁ (scalar/longitudinal/translational u) is massless, T₂ (transverse/microrotational ω) carries the mass-gap content."*
  - `vol1/claim-quality.md:1077` (clm-4mmwb6, verified): the rotational sector's ω²=c²k²+m² is *"a massive (gapped) mode, in contrast to the gapless scalar sector."*
  - `research/2026-06-23_cosserat-band-structure-two-sublattice_prereg-result.md:74,77` (engine-measured, verified): *"translational branches gapless"*; *"The gap appears in the rotational sector ONLY; the translational sector stays gapless."*

- **The IDENTITY argument that grounded the HOLD is UNAFFECTED.** The hold rested on a *sector-ownership/double-count* argument — the "longitudinal-V scalar" IS the A1 MASS sector, so wiring it into the charge readout double-counts the mass phasor (A1⊥T2, the two-"3"s guard) — which never depended on gap-status. The A1 sector being GAPLESS in fact *strengthens* the target: it means a gapless static-supporting translational channel exists (consistent with item 2 below), which is exactly the sector the transducer must reach. **The hold was right; the target (build the transducer) is right; only the incidental gap-status phrase at §2.1:43 is wrong, and it is corrected here rather than by silently rewriting the frozen prereg.**

- **REFINEMENT (item 2, verified) — the static Coulomb-longitudinal E is RETAINED by Gauss, and this is what Stage-2 measures.** `common/historical-precedents.md:21` (Rule-12 note 2026-06-17, verified verbatim): *"the static Coulomb-longitudinal E is KEPT by Gauss's law itself — ∇·E = ρ/ε₀ is a longitudinal (non-transverse) component"*; there is NO propagating longitudinal EM wave. **Build consequence (folded into §6 equation-audit):** the EM-ε sector must have a solution space that INCLUDES the static curl-free E component (this is what validate-on-known (b) Green-function certifies) while having NO propagating longitudinal mode (which the corpus forbids). The equation-audit makes this pair explicit: `static-curl-free-supported` / `propagating-longitudinal-absent`. This also reconciles Grant's original "gapless longitudinal V-scalar" wording — it maps onto THIS retained static curl-free object, reached in the gapless EM-ε channel, not onto a (nonexistent) propagating longitudinal EM mode.

- **ADDITIONAL §8 un-conflation sites (item 3, verified) — the G2 label inversion, folded into the §8 site list below.** Two more same-disease sites: (1) `cosserat-mass-gap.md:145` + `vol1/claim-quality.md:1126,1131` call the massless A1/translational-u sector "the photon" and put the mass-gap on T2/ω — the INVERSE of `master-equation.md:20/27` (A1=mass, T2=charge/spin). This is flagged in-corpus as GAP G2 at `_orchestration/2026-06-07_electron-synthesis-epic.md:319` ("ORCHESTRATOR CHANNEL→DOF MAPPING INVERTED"). (2) `master-equation.md:27` + `cosserat-mass-gap.md:151` hedge: mass=A1 is RATIFIED-CONSISTENCY (PR#260 grade-assignment), NOT driver-validated — the `cosserat-mass-gap.md:108` Verlet driver attributes the mass-gap to T2 with placeholder S4 moduli. **These are DISAMBIGUATE-don't-adjudicate: where the inversion needs a physics ruling, tag it and leave it Grant-gated (I make the collision explicit per-site; I do not resolve it).** Added to §8 as sites 7–8 in the result doc's landed un-conflation list.

**Everything else in §1–§8 stands as frozen.** This note corrects one incidental phrase and folds in the two build-refinements (static-curl-free/no-propagating-longitudinal pair; the two G2 sites), all verified at HEAD. The build target and the hold rationale are unchanged.

---

## 🔴 STAGE-1B PANEL-RETRACTION ADDENDUM (2026-07-03, dated — frozen body above PRESERVED)

The first Stage-1 build run (merged in PR #475) reported a **[NON-EMERGENCE]** transducer verdict. A 3-lane HOLD-POINT panel (A=FAIL, B/C=MIXED) found that verdict UNPROVEN, and I re-verified each finding independently before accepting it. **The emergence verdict is RETRACTED:**

- **The observable was structurally blind.** The emergence readout used the GLOBAL divergence-sum `np.sum(b_EM)`, which telescopes to ≈0 for ANY field on the closed periodic graph (readout antisymmetry + the topology-forced jellium neutrality `b -= b.mean()`). A radial-hedgehog control (genuinely divergent, max local |div|=22.5) read the same machine-zero. The observable could not have detected a monopole.
- **The stated mechanism was false.** "∇·(∇×ω)=0 identically on the discrete operators" is wrong — div∘curl on random ω is pointwise O(1) (max≈1.4, RMS≈0.35); the curl/div heuristics are not an adjoint/DEC pair. The zero was readout antisymmetry, not a curl identity.

**Consequence for this prereg:** the frozen bins §7 stand; **[NON-EMERGENCE] was NOT a pre-registered bin** — it was a post-hoc label and is withdrawn. The §6-style framing fork (X/Y/Z) survives as PRE-REGISTRATION for the future emergence run, **now with lane (W): the two-winding PAIR construction** (the field BETWEEN two windings) broken out of (X) as its own testable option. The Stage-1b rework (LOCAL enclosed-charge observable + mandatory positive control + operator-consistent diagnostics + hardened reconcile-gate + committed artifacts + ngspice cross-solve) STOPS BEFORE the emergence run; the emergence test runs ONLY after the panel + orchestrator review the hardened gate (charter §3.3 sequence, this time enforced — the original run predated the audit function).
