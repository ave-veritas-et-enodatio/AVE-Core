# SYNTHESIS — Four historical survival-class exposure audits (A–D) + yield residuals

**Date:** 2026-07-03
**Lane:** research / synthesis (bounded). HOLD canonization. Do NOT merge without review — push + report.
**Branch:** `analysis/exposure-residuals` (off `origin/main` @ `53f6c3bc`, post PR #466 + #467)
**Source:** four survival-class exposure audits (electron compositeness; LIV/SME + chirality; longitudinal energy budget; cosmic-rotation bounds), Grant-authorized 2026-07-03.
**Discipline:** `verify-before-cite` (every file:line re-verified against origin/main this session; lines had drifted) + `flag-don't-fix` (contradictions surfaced, none resolved) + `consistency-vs-emergence` + `phase-space-coordinate-check` + `regime/phase-state discipline`.
**Companion in-situ flags:** deliverable 1 (`manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex`, GW-channel warningbox) and deliverable 2 (`manuscript/ave-kb/common/trampoline-framework.md`, Ω_freeze observability flag) land the two UNRESOLVED contradictions this doc catalogs in-situ. This doc is the consolidated verdict record; it adjudicates nothing.

---

## 0. VERDICT (one line each)

- **A (extended-electron):** SURVIVES-WITH-OPEN-GAP. Collider-compositeness coverage is the single sharpest exposure (zero corpus hits, HIGH); no-hair screening is unconditioned on probe q²; the lepton excitation spectrum is DEFENSIBLE (muon = +1 Cosserat torsional quantum, consistency-class).
- **B (LIV/SME + chirality):** SURVIVAL PASS on both weak-C branches — low-k isotropy is protected by the cubic 2nd-moment identity INDEPENDENT of weak-C; the exposed anisotropy is band-edge, not low-k; δ_aniso ≈ 2.2e-22 at optical q, 2–3 OOM under cavity bounds. SME coefficient sketch is auditor-supplied context, not corpus.
- **C (longitudinal energy budget):** OPEN-GAP + one live UNRESOLVED contradiction (tex:79 bulk-routing vs the transverse-shear canon, deliverable 1). Monopole/breathing GW emission is the corpus's own "[VIRGIN]"; binary-emission power is imported (Peters–Mathews); no scalar-tensor comparison exists; the energy-budget defense is currently SILENT.
- **D (Ω_freeze):** OPEN-GAP (bounds unaddressed), NOT falsified. Ω_freeze is purely formal as a rate (no value committed); the genesis-epoch IC with a structural present-day residue is DEFENSIBLE vs rotation bounds; the Kerr-language + unwritten spin-down ledger cross-wire (deliverable 2).
- **Yield residuals:** the `A_yield` identifier is overloaded (three meanings across code) — a code-hygiene ticket; the B_SNAP-vs-E_yield/c ~5× discrepancy remains Grant-deferred (pvlas verdict FLAG).

---

## A — EXTENDED-ELECTRON EXPOSURE LEDGER

**Verdict: SURVIVES-WITH-OPEN-GAP.** The killer for extended-electron programs is compositeness; the corpus does not name it. The killer for extended solitons (no internal-mode spectrum) is already answered.

### A1 — Collider-compositeness coverage = OPEN-GAP, severity HIGH (the single sharpest exposure)

`git grep -i` for `compositeness`, `contact.interaction`, `\bLEP\b`, `bhabha`, `substructure`, `charge.radius` across ALL tracked files on origin/main returns **zero genuine hits** (the `substructure` hits are carbon/neutron-isotope contexts; archive `scattering` hits are incidental substrings — verified false-positives, cross-confirmed with `rg` per grep-false-negative discipline). The two coverage docs — `research/2026-06-17_electron-coverage-matrix.md` and `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md` — self-report `grep "mott" = 0` and enumerate scattering cross-sections as gaps, but **neither has a row for compositeness / contact-interaction / LEP-Λ / charge-radius bounds.**

- **The tension (symmetric standard):** the modern killer is the LEP contact-interaction bound Λ ≳ 10 TeV ⇒ substructure ≲ 1e-19 m. The AVE electron's real-space body is the 0₁ unknot at the Compton loop ≈ 2.4e-12 m — **~7 OOM larger** than the naive bound. The corpus's coverage matrix is honest about scattering-cross-section gaps but blind precisely where the discriminating constraint lives: it never states the contact-interaction bound, never names the tension, never cites the reconciling mechanism.
- **Not yet a falsification:** the contact-interaction bound is a four-fermion effective-operator limit whose translation to a topological-soliton real-space extent is non-trivial, and the no-hair boundary (A2) is a candidate mechanism — just not derived at the required q². Grant's physics adjudication (flag-don't-fix).
- **This is a chord opportunity, not only an exposure:** if the extended 𝓠 distribution produces a q²-dependent form factor F(q²) departing from QED's pointlike unity, that is the falsifiable teeth — an AVE-distinct prediction. QED is pointlike-by-fiat (F(q²)≡1 at tree level); AVE is not obligated to match a derivation QED lacks, but IS obligated to show its extended 𝓠 does not over-produce the eeqq/eeℓℓ contact operators LEP constrains.

### A2 — No-hair screening UNCONDITIONED on probe q² = OPEN-GAP, severity HIGH (the mechanism A1 needs)

`boundary-observables-m-q-j.md` (substrate-observability rule): the Γ=−1 TIR boundary "totally reflects substrate waves outside and totally traps them inside … Only 𝓜, 𝓠, 𝓙 are externally measurable." A grep of that leaf for `probe|q^2|high.energy|adiabatic|frequency|hard|resolve|penetrat` returns **zero hits** — the screening carries NO conditioning on probe energy/wavelength.

- The Γ=−1 wall is an impedance boundary from Ax4 saturation (`S(A)→0 ⇒ Z→0 ⇒ Γ→−1`). TIR at the substrate impedance is a statement about *substrate-wave* reflection. Whether it also screens a high-q² external EM probe (a ~100 GeV virtual photon resolving 1e-19 m, wavelength ~10⁷× smaller than the wall) is a DIFFERENT claim, asserted without the frequency-dependent derivation. As written it cannot discharge A1.
- **The defense leaf's minimal deliverable:** derive |Γ(q²)| ≈ 1 (opaque) up to the LEP scale, OR expose the q² at which the wall becomes transparent as a falsifiable form-factor departure (the A1 chord). Requires first a real-space 𝓠(r) on the 0₁ loop (A5) — charge is currently a boundary linking integer 𝓠 = Link(∂Ω, F) ∈ ℤ, not a spatial density ρ(r), so F(q²) = ∫ρ(r)e^{iq·r}dV is not yet computable.

### A3 — Lepton excitation spectrum = DEFENSIBLE (consistency-class, self-tagged)

`lepton-spectrum.md`: "The muon is the 0₁ unknot absorbing exactly one quantum of chiral torsional coupling"; **m_μ/m_e = 1/(α√(3/7)) ≈ 209**, m_μ ≈ 107.0 MeV (exp 105.66, **+1.24%**); tau = one bending quantum. `q-g27-muon-cosserat-saliency.md` corroborates. This directly answers the "extended soliton with no internal modes" killer: the muon IS the first excited state, with computed spacing.

- **Consistency, not emergence (self-tagged):** the leaf marks these "matched closed-form CONSISTENCY — NO solver"; the muon factor is "asserted", the tau factor "identified rather than derived." So the spacing is a consistency-match, not an emergent eigenvalue — it does not PROVE no intermediate mode exists between 0.511 and 105 MeV; it asserts the coupling ladder skips there. The α-suppression (×209) IS the gap-protection mechanism.
- **Consistency-vs-emergence tag: MANIFESTATION/CONSISTENCY.** m_μ/m_e = 1/(α√(3/7)) consumes CODATA α; it is a consistency ratio, not an emergence. Solver-promotion (a Cosserat eigenmode solve landing the lowest torsional excitation at exactly the α√(3/7)-suppressed level, nothing below) would graduate it — track as a gated follow-on, not a gap.

### A4 / A5 — phase-space-vs-real-space is principled (not a dodge); charge is a topological integer (no ρ(r) yet)

`electron-identification.md`: "The (2,3) 'trefoil' is the phase-space winding pattern, NOT a real-space trefoil knot." The distinction is coordinate-honest (phase-space-coordinate-check) and load-bearing — but it *strengthens* the A1 exposure rather than dodging it: the real-space body IS extended (0₁ unknot, Compton-scale loop). A probe couples to the real-space 𝓠 distribution, which is where the form-factor constraint bites. Do NOT let the phase-space label be quoted as if it answered compositeness. `constants.py:115` `e_charge = 1.602176634e-19` is hardcoded CODATA (not α-derived); there is no independent charge-distribution model to compute a form factor from.

### A — severity table

| Exposure | Class | Severity |
|---|---|---|
| Compositeness / contact-interaction / LEP-Λ | OPEN-GAP | HIGH (discriminating; currently un-named) |
| No-hair screening under HARD probe (q²) | OPEN-GAP | HIGH (the mechanism A1 needs) |
| Scattering cross-sections (Compton/Mott) | ALREADY-ADDRESSED-as-gap | MEDIUM |
| Excitation spectrum / internal modes | DEFENSIBLE (muon = 1st excited, α-gap) | LOW (consistency-tier) |
| Phase-space-vs-real-space | DEFENSIBLE (principled) | LOW |

No exposure rises to ALREADY-FALSIFIED-RISK. **Open question for Grant:** does the Γ=−1 TIR wall screen a hard (high-q²) external EM probe, or only substrate waves at the wall impedance? (Plumber: is the electron's mirror a mirror at all colors, or does a hard-enough photon punch through and see the loop?)

---

## B — LIV/SME + CHIRALITY EXPOSURE

**Verdict: SURVIVAL PASS on BOTH weak-C branches.** The key result: low-k Lorentz isotropy is protected by a group-theory fact INDEPENDENT of the (still-open) weak-C gate, so weak-C-fails does not open a low-k LIV collision.

### B1 — Per-branch: weak-C-fails does NOT create a low-k anisotropy collision (the exposed anisotropy is BAND-EDGE)

The load-bearing fact: the cubic point group's **2nd-moment identity** `Σ_b(q̂·d̂_b)² = 4/3` holds to spread **6.7e-16** (`research/2026-06-22_k4-bloch-dispersion-quartic_result.md:56`, verbatim: "$\Sigma_b(\hat q\cdot\hat d_b)^2$ across all dirs | $4/3$, spread $6.7\times10^{-16}$ | ISOTROPIC (2nd moment carries no anisotropy)"). This is a group-theory fact **independent of weak-C**. The FIRST *anisotropic* invariant enters only at the 4th moment (`:57`). The leaf's blockquote (`k4-bloch-dispersion-quartic.md:114`, verbatim) states the eigensolve establishes "the small-$k$ emergent-Lorentz ISOTROPY … so this is **band-edge anisotropy, NOT a low-$k$ Lorentz violation**; the small-$k$ isotropy SURVIVES."

| Branch | What is exposed | anisotropy order at optical q | Collision with cavity bounds? |
|---|---|---|---|
| weak-C HOLDS | photon anisotropy pushed to (qℓ)⁴; δ_aniso ≈ 2.2e-22 | ~1e-22 | NO — 2–3 OOM under cavity (~1e-19–1e-20) |
| weak-C FAILS | photon keeps the zone-edge O(k²) term (band-edge slope ≈2). But that O(k²) term is the ISOTROPIC 2nd moment (Σ(q̂·d̂)²=4/3, machine-precision isotropic). The FIRST *anisotropic* invariant is STILL quartic. | anisotropy still ~(qℓ)⁴ ≈ 1e-22 at low k | NO |

The slope-2 the genuine 24×24 chiral-srs eigensolve measures (`srs_bloch_dispersion.py`, branch `engine/p1b-modes-live` — cited-by-path, NOT on main) is a **band-edge** quantity probed at kℓ≈0.08, and its O(k²) term is direction-INDEPENDENT. A Hughes–Drever / cavity bound tests **anisotropy** (frame-dependent δc/c), not an isotropic scalar dispersion. So the isotropic O(k²) term, even if present, does not collide. weak-C-fails costs only the *distinctiveness/derivation status* of the quartic-photon horn (`clm-k4d4ph` 0.70→0.60, DEMOTED not refuted), NOT emergent-Lorentz safety.

### B2 — δ_aniso magnitude + the numeric anchor

`preferred-frame-and-emergent-lorentz.md:22` (verbatim): "$\delta_{aniso} \sim (q\ell_{node})^4 \approx 2.2 \times 10^{-22}$ at $\lambda = 633$ nm; current cavity bounds $\sim 10^{-19}$ to $10^{-20}$ per SME operator (Nagel 2015, Sanner 2019); 2-3 OOM below bound." At optical q≈1e7 m⁻¹, ℓ_node≈3.86e-13 m (`constants.py`), qℓ≈3.86e-6, (qℓ)²≈1.5e-11, (qℓ)⁴≈2.2e-22 raw (corpus δ_aniso folds κ_γΞ as O(1)). **Arithmetic note (auditor-supplied, verified):** the raw (qℓ)⁴ is ~2.2e-22, not ~5.8e-22 — the corpus figure is the smaller/tighter number, which TIGHTENS the survival margin, it does not loosen it.

### B3 — OA severity: survival rides the k→0 extraction; the wash-out is ASSERTED-not-demonstrated

`field-free-optical-activity.md` (leaf): the substrate-derived bulk g₀ ~ 2.0e12 rad/m is "**40 orders of magnitude OVER** the cosmic bound (~4e-29 rad/m). The k→0 continuum extraction is **OPEN**." `research/2026-06-23_chiral-vector-tlm-phase1_result.md:143` (§9): the g₀ result "does NOT touch the AVE cosmic-birefringence observable … the literal lattice-scale value is ~40 OOM too large to be that anomaly."

- **Correct severity is a three-way distinction the corpus already draws — keep it:** (1) FORM (parity zero-vs-nonzero) = AVE-distinct chord, live-confirmed, does NOT ride on the extraction; (2) MAGNITUDE = NOT bankable (the 40-OOM lattice-scale value is a wrong-regime artifact: a per-node pitch holonomy at k~π/a, and a 633 nm photon averages over it — the same diamond-crystal-isotropy averaging as B1); (3) the cosmic-birefringence β~0.3° anomaly = a SEPARATE mechanism (E/B decoupling from K/G≠2), explicitly NOT this g₀.
- **The honest caveat (regime/phase-state discipline):** the corpus ASSERTS the 633 nm photon "averages over" the pitch holonomy but has NOT demonstrated the wash-out numerically (the k-resolved Bloch-split failed its positive control, §9:142). So the honest statement is "the wash-out is ASSERTED-not-demonstrated; the k→0 extraction is the OPEN gate that would confirm it" — NOT "survival is falsified." IF a completed extraction returned a converged, bound-violating continuum g₀ (not a wash-out), THEN it would become a live falsifier — a contingent future finding, not the current state.

### B4 — SME coefficient sketch = auditor-supplied context (NOT corpus content)

The corpus mentions "SME" only in passing (`preferred-frame…md:22` cites Nagel/Sanner "per SME operator"; the foreword lists "SME bounds" as untested). There is **NO corpus SME-coefficient mapping.** The minimal-SME photon sector (auditor scaffolding, marked as such): k_AF (CPT-odd, chiral/Chern-Simons — the SME image of the OA g₀; tightest bound ~1e-42 GeV via cosmic birefringence; = the OA continuum-extraction gate, so k_AF and OA are ONE gate not two); k_F birefringent (9 coeffs — check whether I4₁32/Fd̄3m point-group selection rules forbid them, a plausible symmetry-forbidden escape); k_F non-birefringent (the (qℓ)⁴ cubic story already covers this — DEFENSIBLE); matter-sector Hughes–Drever (c̃_μν on carriers — the genuinely uncovered exposure, since matter carriers are lattice-LOCKED and keep the (qℓ)² zone-edge term). Recommend the implementer NOT canonize the SME table as corpus; it is exposure-surface scaffolding for a future reconciliation leaf.

**Foreword-lag note (out of THIS PR's scope — foreword is on the exclusion list):** audit B also found the foreword's Thread-3 (`:16`) asserts the preferred-frame leaf as unconditional while the leaf carries a 🟡 P1b-DEMOTED-to-CONDITIONAL banner (`:104`), and the foreword's live-falsifiers block still lists a GRB *dispersion* forward test that the leaf RETRACTED (weak-C 2026-06-15, `:98`) in favor of the GRB NULL. This is a sign-inverted honesty-lag. Surfaced here for the auditor/foreword-lane; NOT edited (00_foreword.tex is a concurrent-implementor exclusion).

---

## C — LONGITUDINAL-CHANNEL ENERGY-BUDGET LEDGER

**Verdict: OPEN-GAP with one live UNRESOLVED internal contradiction.** The question — does accelerated ordinary matter radiate into the A1/bulk channel, and is any such radiation bounded against the binary-pulsar budget — is SILENT in the corpus, and the corpus's own `alpha-hand-of-god-framing.md:246` names it "[VIRGIN]".

### C1 — The channel contradiction (deliverable 1; tex:79 bulk-routing vs the transverse-shear canon)

- `08_gravitational_waves.tex:79` (verbatim): "An electrical reactive tank experiencing a forced phase slip must bleed real power. The phase defect un-aligns the orthogonality, and **real power radiates radially outwards into the bulk lattice network** ($P_{real} \approx Q \cdot \delta$)." — "radially outwards" + "bulk lattice network" = the longitudinal/A1/monopole channel.
- Same file `:142` (summarybox, verbatim): "Gravitational waves propagate exclusively as lossless, **trace-free, transverse** impedance modulations…" — trace-free transverse = SHEAR, the opposite channel.
- KB `gw-propagation-lossless.md:13` (verbatim): "Gravitational waves are **transverse inductive shear waves** in the LC lattice." KB `three-channel-impedances.md:21`: the "Shear / GW" row binds GW to the SHEAR channel canonically.
- Independently flagged by `research/2026-06-23_vacuum-impedance-probe-phase-a-feasibility_result.md:85` (verbatim): "the corpus consistently assigns **GW to the SHEAR channel** … the bulk/V-sector is in fact the *un*-instrumented channel."

This is a verbatim internal contradiction on a load-bearing sector assignment. "Radially outwards" is a monopole/longitudinal descriptor and cannot be the transverse-shear channel. If the pulsar's radiated power genuinely goes into the bulk/A1 channel, the corpus is *asserting* the very A1-radiation-from-accelerated-matter the rest of the framework needs to bound — with an imported (not derived, not channel-decomposed) magnitude. **UNRESOLVED — flagged in-situ (deliverable 1), awaits Grant.** Candidate route to decisive resolution: engine channel-decomposition of the binary's radiated power (shear vs bulk), forking this from a prose ambiguity to a computable ratio P_bulk/P_shear at the Hulse-Taylor operating point.

### C2 — The impedance-mismatch defense is FALSIFIED by the corpus's own constants

`constants.py:711-713` (verbatim): "Longitudinal wave speed v_long = √(K_bulk / ρ_bulk) = √(2G/ρ) … `V_LONG: float = np.sqrt(2.0 * G_VAC / RHO_BULK)`" — finite, ≈ √2·c₀. `three-channel-impedances.md`: `Z_bulk = √2·ρ_bulk·c₀` — finite, same order as `Z_shear`, NOT a ~1e15 mismatch. The only Γ_bulk = −1 (no-escape) condition is at the *saturation* short (r_sat = 7GM/c², `03a_device_circuit_models.tex:59`), a horizon-scale short — NOT the weak-field far zone where a binary orbits. So a "Z_bulk mismatch suppresses radiation" defense is not available; the numbers contradict it. (Symmetric standard: SM/GR bounds extra scalar channels by exactly these pulsar budgets; AVE gets no free pass, and no higher bar.)

### C3 — The no-monopole/dipole theorem is ASSERTED in a docstring, never derived

`orbital_lc_damping.py` docstring (verbatim): "Because **linear dipole radiation is nullified by momentum conservation**, the lowest mode coupling is the quadrupole, causing the slip to scale strictly as (v/c)^5." — asserted, then the module hard-codes k_quad = 32/5 and the Peters–Mathews f(e) coefficients (73/24, 37/96), imported wholesale. No Birkhoff-analog exists (`git grep -i Birkhoff` returns only Poincaré-Birkhoff/KAM). The EM sector has an honest statement of why there is no propagating longitudinal EM wave (`historical-precedents.md:21` — a concurrent-implementor exclusion, cited read-only), but the *mechanical* A1 channel — which AVE explicitly ADDS as a real compressional DOF — has no corresponding theorem. Mass IS A1-content (`grqed-stage3-backreaction_result.md:65-67`: "Mass = A1-dilatation"), so a time-varying mass distribution is a time-varying A1 source: the structural expectation is that it *should* radiate longitudinally unless a conservation law forbids it, and that law is not derived. **This is the load-bearing gap.**

### C4 / C5 — the two natural defenses: one scope-limited, one deferred

- **(b) "same orthogonality gates coupling-out"** exists but covers only the ELECTRICAL port (`phase-a…:25`: "You cannot have clean rejection **and** easy coupling from one **electrical port**"). It is an instrument coupling-in/EM-readout-rejection symmetry, NOT a matter→A1-radiation-out suppression. The Phase-A result itself concedes the bulk channel is "genuinely uninstrumented" (`:76`) — uninstrumented ≠ unradiated. Do NOT cite §25 as a radiation-suppression result.
- **(#438 back-reaction) is STATIC/elliptic** (`grqed-stage3-backreaction_result.md:6-8`: the reversible back-reaction only; the irreversible depletion / DE-tracks-matter primitive is DEFERRED to Stage-4). A static field does not radiate, so #438 introduces no contradiction — but it REINFORCES C3's premise by placing mass/binding-energy ON the bulk/A1 channel. **Stage-4 gating dependency:** when the F6 dynamic matter↔bulk exchange primitive is built, it MUST be reconciled with the pulsar A1-radiation budget — a dynamic exchange and a "matter does not radiate into bulk" theorem cannot both hold without an explicit channel/mode distinction.

### C — severity + the exposure statement

The corpus is SILENT on the load-bearing question; `alpha-hand-of-god-framing.md:246` (verbatim): "**Breathing / monopole GW emission from a melt event. [VIRGIN] No leaf predicts it.**" No leaf compares to a scalar-tensor / Brans-Dicke channel (0 hits). The energy-budget defense is currently SILENT: defense (c) impedance-mismatch is falsified-by-corpus, (b) orthogonality is out-of-scope, and the load-bearing (a) no-monopole theorem is asserted-only. **A defense leaf must DERIVE** the mechanical monopole/dipole suppression (monopole ∝ d²M/dt² = 0 by rest-energy conservation — the missing Birkhoff-analog; dipole ∝ d/dt(total momentum) = 0 — the docstring claim, derive don't assert), compute any surviving A1 multipole power, and gate P_bulk against the ≲0.2% Peters–Mathews residual (PSR B1913+16). **Open questions for Grant:** (1) does binary orbital-decay damping live in the transverse-shear channel (tex:79 = wording error) or is a real bulk/A1 loss intended (needs derivation + pulsar-budget check)? (2) Is the mass/momentum-conservation "no monopole/dipole A1 wave" mechanical Birkhoff-analog obvious-from-substrate, or genuinely underived?

---

## D — Ω_freeze vs COSMIC-ROTATION BOUNDS

**Verdict: OPEN-GAP (bounds unaddressed), NOT falsified.**

### D1 — Ω_freeze is purely formal as a rate (no value, no range, anywhere)

Grep for numeric assignments to `Omega_freeze|Ω_freeze|ω_freeze` across `*.md|*.tex|*.py` returns **zero magnitude commitments**. The operative definition is `Ω_freeze = 𝒥_cosmic / I_cosmic` (`trampoline-framework.md:135`). The ONLY pinned quantitative content is the axis DIRECTION: (l=60.28°, b=50.48°) galactic (Planck PR3 SMICA empirical pin; `cmb_axis_alignment_driver.py` encodes `OMEGA_FREEZE` as a `GalacticAxis` — a direction object, not a rate).

### D2 — Genesis-epoch IC with a STRUCTURAL present-day residue = DEFENSIBLE vs rotation bounds

`trampoline-framework.md:101` (verbatim): "At the moment of crystallization, bond rest lengths lock at the rotating-frame equilibrium value. **When the rotation slows** (or the seed exits the rotating region)…" The strongest defense: `research/2026-06-05_trampoline-metaphor-audit-result.md:60` (verbatim): "ω=0 at rest is an EXACT FIXED POINT of the even-in-ω coupling … Net ω is an excited-soliton flywheel property, never a rest DC field. Ω_freeze = cosmic-boundary 𝒥/I; **its only per-node imprint is the STATIC over-bracing u₀**." So the canonical present-day residual = u₀ over-bracing + I4₁32 chirality + the frozen grain axis — NOT ongoing rotation. Ω_freeze does not collide head-on with the ω/H ≲ 1e-9 rotation bounds at leading order.

### D3 — CMB-isotropy/Bianchi bounds are NOWHERE addressed = OPEN-GAP

A corpus-wide grep for the Barrow / Gödel / Saadeh rotation-bound lineage (`Bianchi`, `Godel`, `Saadeh`, `anisotropic expansion`, `isotropy bound`, `rotation bound`, `ω/H`) returns **zero on-point hits** ("Bianchi" appears only as a discrimination *alternative* in the C1 thread, never as a constraint on AVE's own claims). The eight/five observability channels carry no predicted amplitudes (except Observable 7 ΔG/G ~ 4.4e-5, explicitly conjectural/NOT-derived). "Hubble flow anisotropy" — the channel Bianchi bounds constrain most directly — carries no amplitude at all.

### D4 — Two cross-wires against the clean picture (deliverable 2)

- **Kerr-language ongoing-rotation flavor:** `trampoline-framework.md:139-144` advertises "frame-dragging signatures in distant clock comparison" + "cosmic shear" + "Hubble flow anisotropy" — ongoing-rotation observables whose amplitudes are unstated and unbounded, in tension with the STATIC-residue canon of D2. **Flagged in-situ (deliverable 2).**
- **Unwritten spin-down ledger:** `research/2026-06-07_cosmic-operating-point-dilution-trajectory-scope.md:142` — the "where did the rotation go" ledger (Ω_freeze = 𝒥_cosmic/I_today with dilution dynamics) is explicitly unwritten (inference-not-leaf).
- **Fenced-if-revived:** `research/2026-06-05_c1-cosmic-rotation-knee-result.md:112` transiently priced ω_freeze ~ H_∞ as a present-day frame-drag rate (ω/H ~ 1, ~9 OOM over bound). Rejected in-doc for scaling reasons — NOT for rotation bounds (the bounds were never invoked). ALREADY-FALSIFIED-RISK *if revived*.

### D — recommended follow-up (single bound-reconciliation leaf, future session)

(a) state the present-day rotation residual (0 at leading order, or Ω_today = 𝒥_cosmic/I_today with spin-down dynamics written); (b) quantify or explicitly zero the shear/frame-drag/Hubble-anisotropy channel amplitudes against the Bianchi/ω-H bounds; (c) fence the C1 Reading-3 ω_freeze ~ H_∞ usage as bound-excluded if ever revived.

---

## §yield-residuals — the `A_yield` identifier overload + the B-scale discrepancy

### Y1 — The `A_yield` identifier overload (code-hygiene ticket, NOT a physics contradiction)

The identifier `A_yield` / `A_YIELD` carries **three distinct meanings** across the code, which is a naming-collision hazard even though each is locally correct for its regime:

| Site | Value | Meaning |
|---|---|---|
| `src/ave/core/loop_gap_seeds.py:26` | `A_YIELD = float(np.sqrt(ALPHA))` | √α — the α-anchored measurable yield amplitude (apparatus/seed floor ∝ √α) |
| `src/ave/core/chiral_lattice_v10.py:29-30` | `A_yield = sqrt(2α)`, `A_YIELD_SQ = 2.0 * float(ALPHA)` | √(2α) — the three-regime knee (A²_yield = 2α) |
| kernel-canonical (`src/ave/gravity/__init__.py:236` "A_yield = 1 (unitary strain)"; `src/ave/axioms/scale_invariant.py:149` `|A/A_yield| > 1.0`; `universal_operators.py` clips `A/A_yield` to [−1,1]) | 1.0 | the S(A)=√(1−A²) kernel's unitary-strain normalization (A_yield ≡ 1 in kernel units; note the engine also uses `A²_yield = A²_total/α` to convert V_SNAP-normalized amplitudes, `vacuum_engine.py:554`) |

These are three regime-appropriate quantities (measurable-floor √α; knee √(2α); kernel-unit 1.0) wearing one name. **Ticket:** rename to regime-explicit identifiers (e.g. `A_YIELD_MEASURABLE = √α`, `A_YIELD_KNEE = √(2α)`, `A_YIELD_KERNEL = 1`) or add a module-level docstring cross-reference table, so a future reader does not conflate the √α measurable-floor with the unitary-strain kernel normalization. Code-hygiene only — no physics is wrong; flagged so it does not become a silent unit-bug at a call boundary. The α-anchored measurable identity itself is corpus-canonical (`V_yield = √α·V_snap` EXACTLY, `resonant-lc-solitons.md:127`).

### Y2 — The B_SNAP-vs-E_yield/c ~5× discrepancy (still Grant-deferred)

`pvlas-static-b-verdict.md` FLAG (verbatim): "the two magnetic yield-scales in the corpus disagree by ~5×: the **energy-density-matched** $B_{SNAP}=1.89\times10^9$ T … vs the **ε-proxy** $E_{yield}/c \approx 3.77\times10^8$ T … The ratio is $B_{SNAP}/(E_{yield}/c)\approx 5.0$. Two corpus magnetic-birefringence treatments key on these inconsistent scales." The leaf notes this does NOT touch the R3 static-B verdict (A_I=0 ⇒ δn_μ=0 regardless of which B-scale is adopted) and that a scale is deliberately NOT picked pending Grant adjudication. **Status unchanged: Grant-deferred.** Recorded here for completeness in the yield-residuals ledger; no action taken.

### Y3 — Yield consumer-map (AVE-Core-internal)

Per deliverable 5: the interlock-register is a CI-gated machine-materialized leaf (each `## <title>` + `<!-- id: ilk- -->` heading is parsed into claims.jsonl by `refresh-kb-metadata`), so a free-form consumer table does not fit its node schema. Per the deliverable's fallback, the table lives here and the register carries one pointer line. Each row: consumer → what it needs from the yield object → breaks-if.

| Consumer | What it needs from yield | Breaks if |
|---|---|---|
| E-route birefringence (`src/ave/qed/birefringence.py:122`) | KERNEL SHAPE + the identity `E_crit = α^(−1/2) E_yield` ⇒ (E_crit/E_yield)² = 1/α | the √α relation between E_crit and E_yield shifts (the α⁻³ echo magnitude rides on it) |
| Vacuum IM3 (intermodulation) | same kernel SHAPE + circulation keying (the relativistic-inductor μ-grade keyed on circulation, not flux) | the kernel is not the √(1−A²) shape, or the keying is on flux not circulation |
| Pair-production / portmap | BOTH yield VALUES + exact √α + the T2/A1 sector split; A = √α operating point | either value drifts, the √α is inexact, or the T2 (charge) / A1 (mass) sectors are cross-wired |
| cRIO benchtop | SHAPE only (by design — the bench reads the C_eff(V) saturation curve shape, not an absolute value) | the saturation curve SHAPE is not √(1−A²)-derived |
| Ruptured-core | the boundary as a derivation OBJECT (the yield surface as the compactness endpoint); EOS-gated | the ruptured-core EOS closes and the boundary is not the yield surface |
| Meissner | the hard S→0 endpoint (full saturation) | S→0 is not the physical Meissner endpoint |
| Vacuum memristor | the at/above-yield regime (hysteretic, above A_yield) | there is no distinct above-yield regime (kernel stays reversible past yield) |

**Sibling-repo exposure (one line, no sibling edits this session):** PONDER-05 is the hardest value-rider on the yield object across the workspace; AVE-Fusion carries a `V_yield`-as-bulk-rupture cross-wire that is flagged for a sibling-repo session (the fusion sense of yield-as-rupture must be reconciled against the AVE-Core kernel yield, but that reconciliation is out of AVE-Core scope and is NOT edited here).

---

## Appendix — drift log (audit file:line vs origin/main @ 53f6c3bc)

The four audits were run against HEAD `73ac831c`; this session re-verified every load-bearing cite against `origin/main` @ `53f6c3bc` (post PR #466 + #467). Per verify-before-cite. Drifts found and reconciled:

| Cite (as in audit) | Verified location @ 53f6c3bc | Note |
|---|---|---|
| GW summary "trace-free transverse" at `08_gravitational_waves.tex:85` (audit C) | actually `:142` (summarybox) | audit C internally already used `:142`; the `:85` in the task brief is the `\section{GW Detection}` header, not the summary. Flag anchored to `:79` + `:142` correctly. |
| trampoline Kerr/observability list "~:139-144" (audit D) | list items `:140-144`, framing `:139`, precision-note `:146` | flag placed after `:146` (after the precision note), list left intact. |
| k4-bloch "leaf :56 + :113-115" (audit B, deliv 4) | the `Σ_b(q̂·d̂)²=4/3` identity is in the RESULT doc `research/2026-06-22_…_result.md:56`; the leaf's "band-edge anisotropy NOT low-k" blockquote is at `k4-bloch-dispersion-quartic.md:114`; the moment-table narrative at `:124` | deliv-4 anchors re-pinned to result:56 + leaf:114/124. |
| preferred-frame "post-P1b-demotion section" (deliv 4) | the 🟡 P1b-DEMOTED banner is at `preferred-frame-and-emergent-lorentz.md:104`; §2 quartic-tell at `:48,:50`; weak-C scope-note at `:66` | deliv-4 note placed after the `:104` demotion banner. |
| `A_yield` cites (deliv 3 §yield) | `loop_gap_seeds.py:26` (√α ✓), `chiral_lattice_v10.py:29-30` (√(2α) ✓), kernel-1.0 at `gravity/__init__.py:236` + `scale_invariant.py:149` | all three confirmed exact. |
| pvlas B-scale FLAG "ratio ~5.013×" (deliv 3 §yield) | `pvlas-static-b-verdict.md` FLAG states ratio `≈ 5.0` (B_SNAP=1.89e9 T, E_yield/c≈3.77e8 T) | cited as the leaf states it (≈5.0). |
| δ_aniso arithmetic (audit B) | corpus δ_aniso ≈ 2.2e-22 (`preferred-frame…md:22`); raw (qℓ)⁴ ≈ 2.2e-22 not ~5.8e-22 | the corpus figure is the tighter number; survival margin unchanged/tightened. |

No cite was carried forward without re-verification. Where a line drifted, the flag/note was re-anchored to the verified location and the drift recorded above.
