# Piezo-mechanical "fourth transducer" — prereg + corpus-grep outcome (2026-06-03)

**Trigger:** Grant's instinct that PONDER-05 might be rescued from consistency-class by the
*crystalline structure / grain* coupling the piezo effect to the lattice/vacuum itself — i.e.
a **mechanical** substrate channel distinct from PONDER-05's dead DC-**field** channel.

**Outcome (one line):** GREEN-FIELD on magnitude, but the channel's very existence is gated on
an **already-adjudicated, unresolved foundational fork** (locked vs sliding substrate — Grant's
own doc-109 trampoline question). Even granting the favorable reading, the signal is ~10⁻⁸ and
the discriminator (grain-dependence) is open. **It does NOT rescue PONDER-05. Q-G42 remains the
one clean forward discriminator of the saturation kernel.**

> **🔴 CORRECTION (2026-06-03, post full doc-109 + L3-archive read; Rule 12 substitution-not-retraction):**
> This prereg repeatedly calls doc-109's locked-vs-sliding question "unresolved / deferred / gated."
> **That framing is WRONG.** Verify-before-cite on the full doc-109 + docs 110–114 shows it was
> **reframed AND empirically closed:** (1) doc 109 §13 boundary-envelope reformulation (Grant-confirmed
> 2026-05-14 evening) settled it toward **impedance-only** — the substrate sees the *boundary* not the
> interior (no-hair, BH↔electron), "compression" is the refractive-index gradient n(r) **not** geometric
> bond-length change, and Reading C1 (locked/geometric) was deemed *canonically inconsistent with
> gravity-as-impedance* (§13.4, §15), **not** deferred; (2) the §14 test was **run and closed at v14
> Mode I** (doc 113) — K4-TLM cannot host the bound electron (Mode III) but the **Master Equation FDTD**
> engine (`src/ave/core/master_equation_fdtd.py`) hosts a sustained breathing soliton (4/4 PASS). So the
> mechanical "fourth transducer" is **RULED OUT, not gated** — the geometric-locked channel it needs was
> reframed-against + empirically unneeded. **The conclusion below is UNCHANGED and strengthened:** the
> fourth transducer is not viable; Q-G42 is the one clean kernel discriminator. Read every "gated on the
> unresolved fork" below as "ruled out by the closed fork." Flagged tension T1 (§"Two flagged tensions")
> also **dissolves** — the neutron-lifetime "phonons shake 𝓜_A" is impedance-shaking (doc 109 §3.3/§13.8),
> consistent with impedance-only. The body is preserved as originally written per Rule 12.

---

## PREREG

- **Target:** Does a piezo-*mechanical* strain reach a measurable, grain-dependent per-node
  substrate saturation amplitude A_mech, distinguishable from standard electrostriction + phonon
  physics?
- **Corpus state:** GREEN-FIELD for A_mech magnitude (no substrate-piezo *mechanical* amplitude
  exists; every piezo result is the DC-field/ξ_topo channel), but the load-bearing fork is
  ADJUDICATED-and-deferred. Prior work: `research/_archive/L3_electron_soliton/109_elastic_substrate_finite_strain_investigation.md` (locked-vs-sliding);
  `chiral-thrust-derivation.md:61` (ν_vac=2/7 strain-transfer); `2026-05-17_kappa-quality-defect-density-derivation-result.md` (grain→coupling);
  `2026-05-17_parametric-coupling-kernel-prereg.md:83` (κ_entrain real-power exclusion);
  `common/translation_condensed_matter.tex:25` (phonon = consistency-class).
- **Prediction:** the mechanical channel is real-but-negligible *iff* the substrate is locked
  (finite-strain Lagrangian); it is *zero* in the canonical sliding (Eulerian) engine; either way
  it does not reach the 0.687 / 27.4% headline.
- **Discriminating outcomes:**
  - **A (most likely, realized):** channel exists only in the locked reading; magnitude ~10⁻⁸;
    discriminator = grain-dependence (open). → not a rescue; Q-G42 stays the clean test.
  - **B:** a corpus doc already derives A_mech with a magnitude/coefficient. → FALSIFIED (none found).
  - **C (null):** mechanical strain couples to the kernel only via the piezo E-field it generates
    (= the dead field channel) in the canonical engine. → CONFIRMED for the sliding reading.
- **Falsifier of my framing:** finding a substrate-native A_mech derivation, or a locked-reading
  resolution that's already canonical. Neither exists.

## Step 3.5 — dimensional analysis (magnitude even granting LOCKED)

| Quantity | Value | Source |
|---|---|---|
| Quartz d₁₁ | 2.31×10⁻¹² m/V | materials (X-cut α-quartz) |
| PONDER-05 bias field E | 0.60 MV/m | `04_ponder_05_dc_biased_quartz.tex:94` |
| Piezo strain ε_mech = d₁₁·E | **1.4×10⁻⁶** | this calc |
| E_yield = V_yield/ℓ_node | 1.13×10¹⁷ V/m | `constants.py` (V_YIELD :382, L_NODE :234) |
| Field-channel A_field = E/E_yield | **5.3×10⁻¹²** | this calc |
| Locked A_mech ~ O(1)·ε_mech | **~10⁻⁶** (drive), ~3×10⁻⁴ (fracture) | locked reading |
| Kernel response δε/ε = −A_mech²/2 | ~10⁻¹³ → ~10⁻⁸ | this calc |

A_mech/A_field ~ 10⁵ (mechanical wins by ~5 OOM in the locked reading), **but A_mech ≪ 0.687**:
the 27.4%-collapse operating point is unreachable by *any* channel. PONDER-05's headline is dead
regardless — the conflation was treating V_DC/V_yield as the strain (see `2026-06-03_ivim-RA-adjudication.md` §4).

## Corpus-grep findings — the three walls

1. **Locked-vs-sliding fork (THE keystone — `109_elastic_substrate_finite_strain_investigation.md`).**
   This is Grant's OWN prior question, verbatim (line 25): *"using our trampoline and spring analogy
   it's really the springs that set that distance right? … Have we defined the elastic dynamic or
   inductive stretching of the trampoline material itself?"* Adjudication: the **canonical engine is
   SLIDING** — `dx ≡ ℓ_node` is a fixed scalar, only bond impedance `Z_eff = Z_0/√S` modulates
   ("the springs change stiffness, but their physical length never changes"; small-strain Eulerian).
   The **physical claim AVE wants is LOCKED** (finite-strain Lagrangian). Status: "Reading C2 [sliding]
   canonical; Reading C1 [locked] deferred." UNRESOLVED, `dx_local` refactor gated (~1–2 wk).
   **Consequence:** in the canonical engine a mechanical strain does NOT displace the node → it couples
   to the kernel *only* through the piezo E-field it generates (= the dead field channel). **The
   mechanical "fourth transducer" exists only in the locked reading. Whether it exists at all is
   identical to resolving doc 109.**

2. **κ_entrain real-power categorical exclusion (`parametric-coupling-kernel-prereg.md:83`).** The
   natural "locked" coupling coefficient — mass-density drag κ_entrain = ρ/ρ_bulk — was adjudicated by
   Grant (β) as **REAL-power class, categorically distinct from the REACTIVE saturation kernel; mixing
   forbidden (violates Axis A).** So the obvious locked-coupling route is walled off from the kernel.
   (The `sapphire-phonon-centrifuge.md` acoustic bench uses exactly this entrainment/drag channel for
   artificial gravity — NOT a kernel A_mech drive.)

3. **Phonon↔substrate is consistency-class (`translation_condensed_matter.tex:25`: "same transverse
   shear modes; no virtual exchange").** Precedent: the 2026-06-03 Casimir demotion
   (`closure-roadmap.md:98`) — a relabeled acoustic mechanism with "no new observable" = consistency-class.
   The mechanical bench must clear this. The **only** candidate escape is **grain-dependence**:
   κ_quality = exp[−α⁻²ρ_def(Δω/ω)²] (`kappa-quality-defect-density…:393`) makes substrate coupling
   grain-sensitive where standard electrostriction is grain-insensitive — but it is DAMA-bound,
   α-slew-governed, and the σ_θ↔materials-metric map is "GENUINELY OPEN" (§6 of that doc). No piezo
   application; no X-cut quartz anywhere in the corpus.

## Verdict

The "fourth transducer" is **green-field but blocked**, not a rescue:
- It exists **only in the locked (finite-strain) reading** = Grant's unresolved doc-109 question; the
  canonical (sliding) engine collapses it to the dead field channel.
- Even granting locked, magnitude δε/ε ~ 10⁻⁸ (≫ below the 27.4% headline; A=0.687 unreachable).
- Its only discriminator (grain-dependence) is real-as-precedent but DAMA-bound + materials-map open.
- The natural locked coefficient (κ_entrain) is categorically excluded from the reactive kernel.

→ **PONDER-05's headline stays dead; the kernel-convergence "three transducers" deflates to Q-G42 as
the one clean forward field-channel discriminator.** The mechanical-grain bench is not viable as a
near-term forward test; it is gated behind a *foundational* framework question (Reading C1 / finite-strain
substrate), not a bench-design choice.

## Two flagged tensions (flag-don't-fix — surfaced for Grant)

- **T1 — manuscript vs engine on locked/sliding:** `11_experimental_falsification.tex:123` (neutron-lifetime)
  asserts phonons *"actively shake the 𝓜_A substrate"* (LOCKED), while doc 109's engine is rigid-grid
  impedance-only (SLIDING). Unreconciled internal inconsistency.
- **T2 — the locked coefficient is fenced off:** any mass-density-drag route for A_mech hits the
  κ_entrain real-power exclusion (`parametric-coupling-kernel-prereg.md:83`). A locked *reactive* strain
  transfer (ν_vac-governed) would need to be shown distinct from the excluded real-power drag.

## Recommendation

Park the mechanical-grain bench as **gated on the doc-109 locked-vs-sliding (finite-strain) resolution** —
it is a foundational-physics fork, not a bench. If Grant wants to pursue, the entry point is Reading C1
(finite-strain Lagrangian substrate), already scoped in doc 109 §14, not a new PONDER variant.
