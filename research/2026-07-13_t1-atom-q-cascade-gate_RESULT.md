# T1 — the atom-Q cascade gate — RESULT

**Date:** 2026-07-13 · **Lane:** satellite derivation + consistency driver (self-contained).
**FROZEN prereg (gated on):** `research/2026-07-13_t1-atom-q-cascade-gate_prereg_FROZEN.md`
(freeze commit `7fa58e16`, PUSHED before this doc + all code — git ordering = freeze proof).
**Brief (binding):** `_orchestration/2026-07-13_t1-atom-q-cascade-gate-handoff.md`
**Driver:** `src/scripts/vol_2_subatomic/t1_atom_q_cascade_gate.py` ·
**Tests:** `src/tests/test_t1_atom_q_cascade_gate.py` (12 pass).
**PR:** `[DO-NOT-MERGE]` — only Grant merges.

---

## SECTOR HEADER (declared before any substrate claim)

- **MODE:** derivation-from-canon + numerical consistency driver. **NOT engine-fire.** NO new
  primitive: the instrument evaluates a loss channel on x42's *existing* de Broglie dispersion
  (`x42.local_wavenumber_sq`), which x42 rendered but never used for a loss-Q.
- **REGIME:** cold lattice, deep sub-yield (`V/V_yield ~ Zα² ≈ 10⁻⁴`); Axiom-3 losslessness holds
  below rupture.
- **PHASE-STATE:** a bound standing matter-wave (bulk-modulus, **Z_bulk**) trapped between its
  turning-point reflections in the off-line, source-slaved Coulomb dress (bin-3: `|Γ|=1` at ω→0,
  radiates nothing, **no `Re(Z)`**).
- **SECTOR:** A1 ⊥ T2. Trapping walls = longitudinal **Z_bulk**; radiative loss = transverse
  **Z_EM** — a *different* sector (three-impedance law). Charge = Cosserat (2,3) winding, untouched.

---

## HEADLINE — the kill-shape FIRES (bin (ii)), not rescued

**The substrate does NOT produce a distinct intermediate loss-Q for the atom rung.** Run on x42's
own dispersion, the atom's wall insertion-loss `Q_wall → ∞` — the electron-**intrinsic endpoint** —
for H(1s), H(2s), He⁺(1s), and the reduced-mass leg, **α-free**. The observed `~10⁷` "excited
atom" rung is **not** a wall loss-Q at all: it is the **transverse-EM (Z_EM) radiative port** — a
*different sector* x42's longitudinal Hermitian eigencavity does not express (bin (iii)) — and it
is **α-sourced** (`Q_rad = 4 α⁻³` exactly; the QM value `≈ 9.6 α⁻³ ≈ 2.5×10⁷` is the measured rung).

**Verdict: BIN (ii) NO-DISTINCT-VALUE, with a BIN (iii) rider on the radiative channel.** On the
channel the brief names (insertion loss of the graded Coulomb-dress walls) the framework returns the
lossless-line **endpoint**; on the channel that carries the number (transverse radiative decay) the
value is the **α-echo** at a higher power (the electron's loaded `α⁻¹` → the atom's `α⁻³`). **The
"cascade filter" is the homogeneous vacuum line relabeled on this rung — a vocabulary echo. The
kill-shape fired and I do not rescue it.**

Honest verb (Step 3.10): **DEMONSTRATED, not adjudicated.** A sub-threshold bound state has no open
channel ⇒ the outer Coulomb barrier is infinitely thick ⇒ `T=0` ⇒ `Q_wall→∞` is *entailed by the
physics the gate names*. The run demonstrates the sub-yield wall is lossless (the endpoint); it did
not choose between open branches. The atom rung is **structurally forced** to the endpoint — which
is exactly why it is not a distinct filter section.

---

## DELIVERABLE 1 — THE INSTRUMENT (loss as a BOUNDARY transmission, not a bulk term)

Substrate-native (Ckpt-10): the loss is rendered as the **transmission `T` through the wall
surface** (a Gamow/WKB reflection coefficient — the wall is a reactive reflecting boundary,
`|Γ|=1`), **never** a bulk absorber. Coordinate register = transmission/impedance plane (matched to
the corpus `Γ`/`Z(r)` claim), not real-space localization. Three legs, one shared `gamow_Q`
integrator:

- **Leg A — `wall_leakage_Q`** (α-free): for a bound level `(Z,n)` at `E_n<0`, find the outer
  turning point `r_turn` (root of x42's `local_wavenumber_sq`), integrate the evanescent decay
  `I(R)=∫_{r_turn}^{R}√(−k²)dr`, `T=e^{−2I}`, `Q_wall=2π/T`. This is the round-trip leakage of the
  trapped mode through its outer wall — the literal insertion loss of the graded walls.
- **Leg B — `positive_control_Q`** (Step 3.8a): the SAME integrator on a planted **finite** barrier
  (width `3 a₀`, height `4 Ry` — prereg-declared synthetic knobs) — a fireability witness.
- **Leg C — `radiative_diagnostic_Q`** (quarantined, NOT a bin-(i) candidate): the classical
  Lorentz radiative Q, `Q_rad=(3/2) m_e c²/(α ℏω)`, for Lyman-α — classification only.

---

## DELIVERABLE 2 — LEG A: the wall-Q collapses to the intrinsic endpoint (α-free)

Beyond `r_turn` the Coulomb tail vanishes, so `√(−k²) → √(2m|E_n|)/ℏ = 1/(n a₀)` (the known
hydrogenic evanescent decay). The forbidden region extends to `∞`, so `I(R)` grows **linearly and
without bound**, `T→0`, `Q_wall→∞`. Driver output:

| state | r_turn | κ_inf | dI/dR | I(50·r_turn) | Q_wall(widest) | verdict |
|---|---|---|---|---|---|---|
| H (Z=1,n=1) | 2.000 a₀ | 1.000/a₀ | 0.993/a₀ | 93.7 | `2.8×10¹⁶⁸` ↗ | → ∞ |
| H (Z=1,n=2) | 8.000 a₀ | 0.500/a₀ | 0.497/a₀ | 187.4 | `inf` (underflow) | → ∞ |
| He⁺ (Z=2,n=1) | 1.000 a₀ | 2.000/a₀ | 1.986/a₀ | 93.7 | `2.8×10¹⁶⁸` ↗ | → ∞ |
| H reduced-mass | 2.001 a₀ | 0.9995/a₀ | 0.993/a₀ | 93.7 | `2.8×10¹⁶⁸` ↗ | → ∞ |

- **Divergence, not a plateau:** `I(R)` climbs monotonically (`dI/dR → κ_inf`, the true asymptotic
  decay — a physics constant, not a grid artifact). `Q_wall` is already `≥10¹²` (the bin-(ii)
  endpoint threshold) at modest `R` and grows without bound. **Q_wall → ∞ = the intrinsic endpoint.**
- **α-free / coupling-independent:** `I(R)` at matched `R/r_turn` is **identical** for H (Z=1) and
  He⁺ (Z=2) to `rel<1e-9` — the leakage is a pure geometric property of the sub-threshold bound
  state, carrying **no `Zα` coupling signature**. The result is not an α-seeded value; it is
  α-independent.
- **Probe-mass invariant:** the `m_e → m_r,H` reduced-mass correction leaves the divergence
  unchanged.

## DELIVERABLE 3 — LEG B: the instrument is FIREABLE (bin (i) is reachable)

The SAME `gamow_Q` on a finite-width barrier (`w=3 a₀`, `ΔV=4 Ry`) returns `I=6.000`,
**`Q_control=1.02×10⁶`** — a finite value **in the bin-(i) window `[10⁵,10⁹]`**. So Leg A's `∞` is a
**physics verdict** (the atom's outer barrier is infinitely thick), **not** an instrument that
cannot fire bin (i). The `test_gate_discriminates_finite_vs_infinite_barrier` gate confirms: finite
forbidden region → finite Q → adjudicates bin (i); infinite region → `∞` → adjudicates bin (ii).
**A gate that cannot fire is a checklist; this one fires both ways.**

## DELIVERABLE 4 — LEG C: the observed ~10⁷ is the α-echo (a different sector)

`Q_rad(classical) = 1.029×10⁷ = 4.000·α⁻³` (exact, Lyman-α, oscillator strength `f=1`); with the
QM oscillator strength `f_Lyα≈0.416`, `Q_rad ≈ 2.47×10⁷ ≈ 9.6·α⁻³` = the measured atomic
linewidth-class rung. **`Q_rad ∝ α⁻³`: two powers of α from the Rydberg transition scale (`∝α²`),
one from the radiative coupling** — the electron's loaded-Q echo (`α⁻¹`) at a higher power, the same
coupling constant, not a distinct filter cutoff. This is the **transverse-EM (Z_EM) port**, a
*different sector* than the longitudinal trapping walls, and one x42's bin-3 (no `Re(Z)`), Hermitian
(real-`E`) eigencavity does not express (bin (iii) instrument gap). Corpus-corroborated as a known
echo family (birefringence `α⁻³`, `research/2026-06-24_e4-im3-vacuum-distortion.md:179`).

**Symmetric-standard note (consensus-bias lens):** QED's atomic-linewidth coefficient is *equally*
α-rooted — computing the linewidth from `α³` is a fine peer result in both frameworks. The α-echo
disqualifies the value only as a **cascade-distinct filter cutoff** (the specific claim under test),
not as a linewidth; SM makes no cascade-filter claim, so there is no double standard.

## DELIVERABLE 5 — the kill is ROBUST to the X41 K1∧K2 open fork

The corpus caveats that "the walls are unconditionally transparent / `|Γ|=1`" rides the **X41
`[UNDERDETERMINED — K1 ∧ K2]`** fork (`research/2026-07-10_x41-radiative-scoping-why_RESULT.md:37`;
standing canon `manuscript/ave-kb/CLAUDE.md:75` has a held static-E *loading* `S_ε<1`). **This does
not threaten the kill.** That fork is whether the held dress *reactively LOADS* the ε kernel (an
`S_ε<1` amplitude/dispersion shift, `~10⁻⁴` in deep-linear H) — it is **not a dissipation
question**. Axiom-3 makes the sub-yield substrate lossless (`Re(Z)=0`); saturation `S<1` is a
reactive softening, not a resistive loss (`Re(Z)` appears only at/above rupture). A loaded *reactive*
wall is still lossless ⇒ `Q_wall→∞` regardless of how X41 resolves. Leg A does not assume
unconditional losslessness; it computes the transmission directly, and a `~10⁻⁴` well-depth rescale
does not make the infinite outer barrier finite. **The verdict leans on `Re(Z)=0` sub-yield, not on
a decreed `|Γ|=1`.**

---

## ADJUDICATION against the frozen bins

| bin | frozen threshold | outcome | fires? |
|---|---|---|---|
| **(i) DISTINCT** | finite α-free `Q_wall ∈ [10⁵,10⁹]` | `Q_wall→∞` (not finite) | **no** |
| **(ii) NO-DISTINCT** | `Q_wall≥10¹²` or `≤10³` or degenerate | `Q_wall→∞ ≥ 10¹²` | **YES (DEMONSTRATED)** |
| **(iii) MACHINERY-INSUFF.** | radiative `Z_EM` port not expressible by x42 | `~10⁷` lives only in the transverse port x42 lacks; α-sourced | **YES (rider)** |

**Instrument fireable:** True (Leg B returned `1.02×10⁶`, in-window). The bin-(ii) fire is therefore
a real verdict, not an unfireable checklist. **The kill-shape fired; not rescued.**

## DISCRIMINATION-CHECK (ave-discrimination-check — false-kill guard + SM-counterfactual)

- **Am I false-killing?** The one way bin (i) could legitimately fire is an α-free finite-Q *wall*
  leakage channel. I checked the candidates: (a) tunneling escape — the outer Coulomb barrier is
  infinitely thick for any sub-threshold bound state (no open channel), so `T=0` exactly, verified
  numerically and Z-/n-/mass-invariant; (b) shape resonance — needs a barrier with propagating
  regions on both sides; the monotone attractive Coulomb+centrifugal has none for bound levels; (c)
  external-cavity / apparatus Q — a bench object (`parametric-coupling-kernel.md:213`), not an
  intrinsic wall property; (d) near-nucleus saturation — the muonic X41 regime, an absorption at the
  nucleus, not a linewidth of the bound mode, and excluded from the hydrogen rung. None is an α-free
  finite-Q wall channel. The kill is not a false-kill.
- **SM-counterfactual:** in SM/QED the atomic linewidth is likewise `∝α³` and the bound state is
  likewise stationary absent radiation — the *same* physics. The gate is AVE-specific (does the
  *cascade-filter* relabel carry distinct content?), not a linewidth computation; SM gets no free
  pass it is denied, because SM does not make the cascade claim.

## CLASSIFICATION (consistency-vs-emergence)

**Class: CONSISTENCY / FRAMING-DEMOTION (a NEGATIVE), no new primitive, no emergence.** Every
quantity is pre-existing (`ALPHA, A_0, RY_EV, M_E, M_R_H`, x42's `local_wavenumber_sq`). **AC/DC
sector (`clm-acdc07`):** the loss-Q is a **pure-AC dispersion quantity** → per the carve it cannot
be a framework-level empirical discriminator, and this null is **NOT an axiom falsification**. This
gate is an **internal framing-coherence test**; its kill is a **framing demotion of the cascade
relabel at the atom rung**, explicitly not a falsification of AVE.

## WHAT THIS DOES TO THE CORPUS (routed, not decreed)

- **Instantiates the R2 rhyme's principle at the atom rung** (`collapse-target-registry.md:783-788`,
  candidate-gen): the "dissipative-Q relations do not transfer to a reactive tank; only the tiny
  `R_rad` port gives a real linewidth — vocabulary-not-mechanism trap" framing-flag is here given a
  **computed** instance. *(Scope note, post-review finding #2: R2 proper is an **electron-tank
  forward observable** (`Δω/ω=α`, ~137-cycle ring-down) explicitly **GATED ON T9** (the
  complex-Poynting Re/Im split); T1 computes the **atom** wall-Q, a different object, and runs no
  Re/Im split — so T1 does not **close** R2, which stays open/T9-gated. It corroborates R2's
  mechanism at a second rung.)*
- **The Q-ladder atom rung** (`keying-register-walk_framing.md:117`, FRAMING walk-estimate `~10⁷`)
  is **DEMONSTRATED endpoint-degenerate on the wall channel**; the `~10⁷` is the transverse
  radiative α-echo, not a wall loss-Q. **Recommendation (framing follow-on, auditor lane — NOT this
  lane):** annotate the atom rung as "radiative `Z_EM` port, `α⁻³` echo; the *wall* loss-Q is the
  intrinsic endpoint `Q→∞`", so no downstream cite reads it as an independent cascade cutoff. The
  BH endpoint stays canon and distinct (`Q=ℓ`, Op21 at the at/above-rupture `Γ=−1` boundary — a
  genuine structural cutoff, the contrast that sharpens the atom's collapse).

## FLAGS SURFACED (flag-don't-fix; Grant/auditor adjudicate — this lane resolves none)

1. **⚑ `Q_wall→∞` is entailed, so the gate DEMONSTRATES rather than adjudicates.** This is disclosed
   as such (Step 3.10); bin (i) was fireable (Leg B), so the gate is not vacuous, but the atom-rung
   endpoint-collapse is structurally forced, not a contingent measurement.
2. **⚑ The `Z(r)` register.** The brief cited "impedance/mismatch profile `Z(r)`" at
   `x42 RESULT.md:84`; that is the **superseded pre-repair** rendering (KEEP-BOTH-logged). The live
   register is the **defect's dispersion/index `n(r,ξ)`** (lattice `Z₀=377Ω` everywhere, Regime I).
   The wall is a *dispersion* turning point, not a medium-impedance step — which is *why* it is
   reactive (`Re(Z)=0`) and the leakage is a pure geometric divergence. Surfaced, not a contradiction.
3. **⚑ The X41 K1∧K2 fork is open** (Deliverable 5). The kill is robust to it, but the fork itself is
   not resolved here (Grant + CVR bench own it).

## DISCIPLINE

- **Freeze-by-push:** prereg commit `7fa58e16` pushed to origin **before** any code committed (git
  ordering = freeze proof; auditable from GitHub API push timestamps). No bin/tolerance/observable
  edited post-run (Rule 11).
- **Substrate-native (Ckpt-10):** loss rendered as a boundary transmission `T`/`Γ`, never a bulk
  absorber. **phase-space-coordinate-check:** the comparison is in the transmission/impedance plane,
  matched to the corpus `Γ`/`Z(r)` claim, not real-space localization.
- **Rail (no α-seed):** Leg A is α-independent (Z-/coupling-invariant divergence, machine-checked);
  Leg C uses α only to *classify* the observed rung as the echo, never to seed `Q_wall`; the
  adjudicator reads only `Q_wall` (a bin-(i)-magnitude `Q_rad` cannot flip the verdict — machine-
  checked by `test_radiative_value_does_NOT_flip_the_verdict`).
- **ave-driver-script-honesty:** the driver forward-computes and reports `Q_wall→∞`/endpoint; it
  prints no "AVE predicts 10⁷"; the `~10⁷` appears only labelled as the quarantined α-echo diagnostic.
- **Consistency-vs-emergence:** consistency/framing-demotion class; new-primitive scan = NONE; no
  emergence headline; not an axiom falsification (AC sector).
- **verify-before-cite:** all anchors re-grepped at base `046d883c`; the brief's `RESULT.md:84`
  "impedance/mismatch" cite is the superseded pre-repair rendering (flagged, not propagated).
- **No KB/canon edits from this lane** — `research/` + `src/` only. The Q-ladder relabel is *routed*
  to the auditor lane, not applied here.

## Adversarial-review repair log (2026-07-13; 5 lenses, 3 findings, all MINOR/EVIDENCE-VOID)

The mandated `ave-adversarial-pr-review` (5 lenses → per-finding adversarial verify) confirmed **3
findings, all MINOR / all EVIDENCE-VOID (repair-and-bank) — no verdict flips.** The **load-bearing
false-kill lens could NOT refute the kill**: *"the BIN (ii) NO-DISTINCT-VALUE verdict is a
TRUE-KILL, not a false-kill"* — all four wall-leakage refutation channels (tunneling escape, shape
resonance, `ℓ>0` centrifugal, autoionization) tested and closed. The α-cleanliness lens proved Leg A
α-free two independent ways; the corpus-fidelity lens grep-confirmed every citation verbatim (no
stitched/fabricated quote; the `RESULT.md:84`-superseded flag is accurate); the AC/DC classification
was verified correct.

| # | finding (MINOR / EVIDENCE-VOID) | fix |
|---|---|---|
| **1** | The frozen bins don't tile the line — bin (i)=`[1e5,1e9]`, bin (ii)=`{≥1e12, ≤1e3, degenerate}` leave `(1e3,1e5)` and `(1e9,1e12)` UNDECLARED; `adjudicate()` silently routed a finite gap-value to `"(ii) degenerate"`. | **Code repaired** (`adjudicate()`): finite gap-values now route to an explicit `(iii/AMBIGUOUS) UNDECLARED-BAND — REWORK` (Outcome C), not mislabeled degenerate; `test_undeclared_gap_routes_to_ambiguous_not_degenerate` added. The FROZEN prereg is **unedited** (Rule 11) — this aligns the code to it and discloses the gap. **Shipped verdict unaffected:** actual `Q_wall=inf` → prereg-degenerate → clean bin (ii). |
| **2** | RESULT said "Discharges the R2 rhyme"; R2 is an **electron-tank** forward observable **gated on T9**, a different object — T1 does not close it. | RESULT reworded to "**instantiates** R2's principle at the atom rung", with a scope note that R2 proper stays open/T9-gated. PR body reworded to match. |
| **3** | The FROZEN prereg's *counterfactual* Outcome-B / falsifier calls a hypothetical bin-(i) pass "a chord", contradicting its own `clm-acdc07` classification (`Q_wall` is pure-AC → "never a chord"). | **Erratum (frozen prereg unedited, Rule 11):** a bin-(i) pass would be a **distinct STRUCTURAL cutoff** (a genuine filter section) — which, per the AC/DC carve (`claim-quality.md:1369` clause iii, "AC … consistency, never a chord"), is a **framing-content / consistency result, NOT a chord** (chords live DC-side / in DC→AC coupling). The counterfactual did not occur (the run landed Outcome A / bin (ii)), so the verdict is unaffected. The driver's `adjudicate()` bin-(i) verdict string now carries the corrected "NOT a chord" wording. |

All fixes are repair-and-bank on the *evidence/precision*; the **conclusion (bin (ii) kill, α-echo
radiative rung) is untouched and independently reconfirmed** by the false-kill and α-cleanliness
lenses. Tests after repair: **13 pass** (was 12; +`test_undeclared_gap_routes_to_ambiguous`).
