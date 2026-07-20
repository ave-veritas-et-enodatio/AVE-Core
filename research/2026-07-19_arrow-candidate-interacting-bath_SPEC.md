# Interacting-bath arrow candidate — derivation + SPEC + design-walk brief (BUILD-GATED)

**Date:** 2026-07-19 · **Class:** SPEC (derivation + re-cert spec + design-walk brief). **This lane STOPS at the build gate** — no meter/engine edits, no instrument build, no arm firing. Rationale: this candidate is a *physics change* to the certified instrument (it breaks the #721 identity-conservation certificate ⇒ full re-cert), and instrument-design walks happen with Grant in chat before any build (RULING-22 precedent).

**Provenance of the seed (verify-before-cite, content-verified at HEAD `1be045a1`):**
- `research/2026-07-19_f6-thermal-floor-arm_result.md` §0(b) + §4 — the tri-form verdict; the routed SPEC seed: *"a dephasing arrow needs an INTERACTING (mode-coupled / nonlinear / dissipative) bath — a meter/physics change (breaks the #721 identity ⇒ full re-cert), NOT built"* and *"an interacting-bath arm should gate on the ensemble-average-first coherent-revival metric."*
- `research/2026-07-19_noise-floor-arrow-walk_RECORD.md` §1e — the lowpass-on-coherence framing (linear engine = cross-mode correlation-decay that *looks like* a downshift to an envelope detector; nonlinear channel = genuine spectral downconversion to `n·ω_d`).
- `research/2026-07-16_f6-bath-meter_CHARTER.md` — the certified instrument (§0–§9 + §A/§B/§B-post/§C/§C-post/§D/§D-post); the #721/W2 identity-class scope caveat (§B-post R-1); the κ·g degeneracy (`f6_bath_meter.py:198`).
- The mechanism sentence being escaped (the #734 identity-class result): the Caldeira–Leggett bath is a set of INDEPENDENT oscillators with no mode–mode coupling ⇒ a static random floor *superposes with* the coherent revival, it cannot *dephase* it — structurally inexpressible on the lossless-reactive junction.

> **★ WHAT THIS DOC RESOLVES, IN ONE LINE.** The lattice **does** provide a substrate-native mode–mode coupling (the shared-`S(A)` intermodulation — DERIVED, axiom-grounded), so a *dephasing arrow is derivable in principle*; but at the certified MILD operating point it is **~40× below the resonance-overlap threshold** (which retro-predicts the #734 null), and — a second barrier the #734 framing under-weighted — the meter's **scalar-port + global-rescale bath↔lattice coupling is phase-blind**, so even a fully interacting bath cannot imprint its phases on the signal through it. A genuine floor-dephasing arm therefore needs **TWO** structural changes plus a **near-knee operating point**, each of which breaks a named certificate. **Verdict: DERIVED-YES (thresholded) on the interaction FORM; a GENUINE FORK on the operating point + the port change — Grant's calls, walk-brief §7.**

---

## 1 · Sector / regime / phase-state header (mandatory before any substrate claim)

- **Sector:** R7 — thermal / entropy-sink (T2 latent-heat channel; the F6 ε→T2 candidate), **same sector as the certified meter** (charter §0). The bath is a **T2 dissipation-sink DOF**; it carries **no** Cosserat (2,3) winding/charge and **no** A1 dilatation mass. Sector-ownership discipline (memory `feedback_sector_ownership_a1_t2_crosswiring`): the floor does not confine or hold charge; the "arrow" it might set is an *entropic-sink* arrow, not a chirality/winding arrow (consistent with `dark-energy-latent-heat-definition.md:77` "arrow of time = the T2 entropic sink, NOT chirality", walk-record anchor 5).
- **Mode:** classical reactive TLM lattice (K4, z=3 srs, 4 ports) coupled to a bath comb. **The decisive change vs the certified meter:** the bath comb is now **INTERACTING** (mode-mode-coupled), NOT the Caldeira–Leggett *independent*-oscillator comb the meter certifies (charter §2 / §8 "Caldeira–Leggett (independent-oscillator)").
- **★ Regime — this is the load-bearing distinction.** The candidate is **structurally inexpressible in the cold/MILD linear regime** where the certified floor-arm ran (`A_max≈0.10`, κ=0.030, the regime where the op3 bond `Γ(A)` amplitude-dependence is *second-order and negligible* — charter §B1 FACT-2/FACT-4). A dephasing arrow **requires** the driven-**nonlinear** regime where the Ax4 saturation kernel is *first-order* load-bearing (`A_max` at or approaching the near-knee, charter §B1 operating-point table: moderate `A≈0.30`, near-knee `A≈0.50`). **Regime/phase-state discipline (memory `feedback_regime_phase_state_discipline`):** a null measured in the linear regime is an **artifact-of-regime, not a falsification** of the nonlinear mechanism — exactly the #734 scope caveat ("does NOT falsify arrow-from-thermalization in an *interacting* bath, untested"). This SPEC therefore lives in a **different regime** from the fired arm.
- **Phase-state:** driven-then-source-off, closed cavity (PML=0), **Op14 saturation ACTIVE** (op3_bond_reflection=True with `A` large enough that `S(A)=√(1−A²)` curvature is load-bearing) — a partially-saturated driven lattice, NOT the cold plant. Memristive/Regime-IV hysteresis stays **OUT of scope** (`use_memristive_saturation=False`) — the instantaneous Op14 kernel only, so the measurement is not confounded by a lossy hysteresis leak (charter §B1 operating-point note).
- **Coordinate discipline (A46 / `phase-space-coordinate-check`):** the revival and its dephasing are **phase-space** objects — a comb re-phasing (Poincaré recurrence) in the bath's modal/spectral coordinate `E_m = ½p_m² + ½ω_m² x_m²`. The primary observable (the ensemble-average-first coherent revival, §5) is read in **that matching coordinate**, not a real-space lattice-Cartesian surrogate. This inherits the meter's certified A46 discipline (charter §0/§8: `N_occ` read in the modal coordinate). A dephasing-vs-`ρ` (or -vs-`A`) claim measured in the modal coordinate is coordinate-matched; a real-space φ² surrogate would be uninformative.
- **Consistency-vs-emergence tag (`consistency-vs-emergence`):** the arm this SPEC gates would be a **CONSISTENCY-class** instrument test of a **mechanism FORM** (does a *derived* interacting comb thermalize a coherent return, above a *derived* threshold?). It is **not** an emergence claim: the floor level, the comb `{ω_m}`, and the operating point `A` are **ENGINEERING CHOICES tagged as such** (inherited from charter §0); nothing is CODATA-derived. The one thing that would be *derived-not-imported* is the **crossover threshold** `A²/4·ω_scale ~ Δω` (§3) — a FORM-level forward prediction, not a value-level emergence.


## 2 · The substrate-native interaction form (DERIVED — candidate (a) load-bearing; (b) is a second, separate barrier)

**The question this section answers:** what mode–mode coupling does the *lattice itself* provide — without importing a phenomenological `λ·x_i·x_j`? Two candidates were routed; the derivation finds (a) is the axiom-grounded interaction, and (b) is **not** reducible to (a) — it is a **second, independent barrier** the #734 framing under-weighted.

### 2.1 · Candidate (a) — the Ax4 saturation kernel as a shared-medium (varactor) nonlinearity [DERIVED]

**The chain, every link content-verified in `src/ave/core/k4_tlm.py` at HEAD `1be045a1`:**

| link | form | provenance | cite |
|---|---|---|---|
| local strain | `A = |V_inc|_total / V_SNAP`, the **total** incident magnitude at a site | DERIVED (Op2 strain register) | `k4_tlm.py:280-281` |
| saturation kernel | `S(A) = √(1 − A²)` | DERIVED (Op2 / Ax4 saturation kernel) | `k4_tlm.py:282-283` |
| local impedance | `z_local = 1/√S = (1 − A²)^(−1/4)` | DERIVED (Op14 canonical `Z_eff = Z_0/√S`) | `k4_tlm.py:315-318` |
| bond reflection | `Γ = (z_B − z_A)/(z_B + z_A)`, `T = √(1 − Γ²)` | DERIVED (impedance-mismatch reflection, EE-native) | `k4_tlm.py:397, 432-448` |

**The mode-coupling term, derived (not imported).** The crucial fact is that `z_local` is a function of the **total** local amplitude `A = |V_inc|/V_SNAP`, and `V_inc` at a collar site is the **superposition of all modes/excitations riding there**. Write the local field as a sum of comb components `V = Σ_m V_m` (each `V_m` the mode-`m` contribution at that site). Then

```
A² = |V|²/V_SNAP² = ( Σ_m |V_m|²  +  Σ_{m≠m'} V_m V_m'*  ) / V_SNAP²
                      └── self (DC) ──┘   └── cross-mode (intermodulation) ──┘
```

Expand the canonical impedance kernel to leading order in `A²`:

```
z_local = (1 − A²)^(−1/4) = 1 + (1/4)·A² + (5/32)·A⁴ + O(A⁶)
```

The `(1/4)·A²` term **carries the cross-mode products** `Σ_{m≠m'} Re(V_m V_m'*) / (2 V_SNAP²)`. Because `Γ = (z_B − z_A)/(z_B + z_A)` transmits this amplitude-dependent `z_local` to **every** other mode crossing that bond, mode `m'` sees its reflection/transmission coefficient *modulated by the instantaneous amplitude of mode `m`*. **This is a genuine cubic (χ⁽³⁾ / Kerr-type) mode–mode coupling** — the substrate-native analog of *intermodulation in a shared varactor* (the EE mapping the task named): the varactor's capacitance depends on the total voltage across it, so two tones sharing it beat against each other's bias.

**Provenance verdict for (a):** **DERIVED, axiom-grounded.** The *form* is a Kerr/four-wave-mixing cubic; the *leading coefficient* `1/4` is **fixed by the canonical `(1−A²)^(−1/4)` kernel** (not a free parameter). Nothing imported: no phenomenological `λ`, no open-quantum-systems spectral density beyond the comb the meter already carries. FORM derived + the coupling *value* forced by the kernel — this is the FORM-deriving / VALUE-forced posture, not a VALUE import.

### 2.2 · Candidate (b) — bond-mediated coupling in a genuine T2 manifold vs the scalar-port abstraction [a SECOND, SEPARATE barrier — NOT reducible to (a)]

The certified meter couples the bath to the lattice through a **scalar collective coordinate** `q = Σ_{s∈collar} mean_p V_inc[s,p]` (charter §2), and the back-reaction is a **GLOBAL, spatially-uniform, phase-blind amplitude rescale** (charter §A1: *"spatially uniform and phase-blind — no bath phase re-enters the lattice"*; §A8: the back-reaction is ~90% uniform attenuation, ~10% spatial residual). This scalarization is a **second barrier**, independent of the bath's internal coupling:

- **Even a fully interacting bath cannot dephase the signal through a scalar port.** The bath modes are driven by the single scalar `q` and push back through a single global scalar rescale. A global scalar multiple of an on-shell TLM state carries **no per-mode phase** (it is exactly the §A1 argument that makes conservation an identity). So the *floor's random phases cannot reach the signal's individual modes* — the channel is "amount, not phase" **regardless of whether the bath is Caldeira–Leggett or Kerr-coupled**. The #734 result named the bath's *independence* (barrier B1) as the reason the arrow is inexpressible; **the scalar-port + global-rescale bottleneck (barrier B2) is a second, load-bearing reason that persists even after B1 is lifted.**
- **Why (b) is NOT reducible to (a).** Candidate (a) lives in the **lattice's** op3 bonds — it couples the *lattice's own* comb modes among themselves. But the floor-arrow hypothesis needs the **bath (floor) → lattice (signal)** phase channel, which passes through the scalar port. Lifting (a) alone gives lattice-internal thermalization the floor cannot access; lifting (b) alone (a spatially-resolved, phase-carrying port) lets the floor's phase reach the lattice, but if the bath is still independent oscillators at MILD, and the lattice Kerr is sub-threshold (§3), there is still nothing to thermalize. **Both barriers must be lifted, and they are physically distinct changes.**
- **The linear bond network alone does NOT provide mode-mixing.** `build_scattering_matrix(z)` is **z-independent** (`0.5 − δ` for N=4 — charter §B1 FACT-1, `k4_tlm.py:64-85`), so the K4 4-port scatter is a *fixed orthogonal* map when `A` is small. A spatially-resolved *linear* port would give linear mode-conversion (scattering between spatial modes) that **preserves superposition** → cannot dephase a coherent revival any more than the independent-oscillator bath. So barrier B2's fix is only meaningful **in combination with** the nonlinear `z_local(A)` of (a): the amplitude-dependence is what lets a spatial port carry phase-scrambling information.

**Provenance verdict for (b):** the *port geometry* (a real K4 collar bond-network coupling instead of the scalar `q`) is DERIVED-available (the K4 lattice already has it); the **decision to promote the abstraction is a meter/physics change**, and it is the change that **breaks the #721 identity hardest** (§4). It is **not** a phenomenological import — but it is **not free either**: a structured, phase-carrying back-reaction is no longer a global scalar multiple, so the arithmetic-exact conservation identity (§A1) no longer holds and the pump can resurrect empirically.

### 2.3 · REJECTED forms (flag-don't-fix — recorded with reasons)

- **A generic phenomenological `λ·x_i·x_j` bath-mode coupling — REJECTED (no axiom provenance).** This is the open-quantum-systems / Fermi–Pasta–Ulam default. It has no K4/Op14 derivation; its coupling constant `λ` would be a free knob (a VALUE import with no forcing), and it would smuggle a chosen nonlinearity rather than reading the substrate's own. The substrate-native replacement is (a) — the shared-`S(A)` intermodulation, whose coefficient is fixed by the kernel.
- **An `Re(Z)` dissipative bath (a literal resistor) — REJECTED for the arrow claim (would be a smuggled valve).** A genuine dissipative bath *would* dephase, but the arrow-from-counting license is explicit that the arrow comes from **mode-count or a click, never a valve** (`retention-transition-split.md:36`, walk-record anchor 4). An `Re(Z)` bath dephases by *loss*, which is the forbidden valve — it would validate a disabled-Ax3 leak as "the arrow", not derive it. (This is *not* the friction plant, which is a certified **control** for the meter, charter §4/§A5 — it is deliberately the thing the arrow must be shown to differ from.) The honest interacting-bath channel is **reactive** mode-mixing (Kerr/FWM), which conserves total energy and produces irreversibility *by counting over mode-mode scrambling*, not by loss.
- **A memristive / Regime-IV hysteresis bath — OUT OF SCOPE (lossy, confounds).** `use_memristive_saturation` is a lossy hysteresis (charter §B1) that would introduce a real dissipation channel and confound the reactive measurement. Excluded, consistent with the meter's certified scope.


## 3 · The dephasing structure — does the derived interacting comb thermalize a coherent return?

### 3.1 · The two regimes, mapped onto the walk-record's lowpass framing

The derived Kerr/FWM coupling (§2.1) sits underneath **both** halves of the walk-record's §1e precision note:

- **Correlation-decay (linear-looking, REVERSIBLE) — `A` small / coupling sub-threshold.** With the cubic coupling weak, the comb of incommensurate `{ω_m}` dephases by ordinary *linear* mode-spreading: the cross-mode phase correlation decays and, to an envelope detector, energy *looks like* it drains from the carrier line into the baseline. But this is the certified **"heat = reversible phase-scramble"** (`thermal-phase-registers.md:25`, walk-record anchor 2) — **Poincaré-recurrent / bounded**: superposition holds, so the coherent revival re-phases and **returns** within the recurrence window. This is precisely the #734 measured null (revival flat), and it is *window-relative reversibility*, not thermalization.
- **Real downconversion (nonlinear, IRREVERSIBLE) — `A` non-negligible / coupling above threshold.** The cubic term performs genuine **four-wave mixing**: modes at `ω_m, ω_{m'}, ω_{m''}` generate content at `ω_m + ω_{m'} − ω_{m''}`. When these products land on *other comb teeth*, energy migrates across the comb with no single return path — irreversibility **by counting over mode-mode scrambling** (the retention/transition counting license, `retention-transition-split.md:31`, walk anchor 4; no valve). This is the walk's *literal* spectral downconversion — and it is **already observed**: op3 self-generated harmonics at `n·ω_d` are measured (`research/2026-07-17_f6-meter-nonlinear-reval_result.md:69-74`, W4: 10 occupied modes, 5 at `n·ω_d`, `ω_d=0.524`; walk anchor 6). The FWM channel is real; the question is whether it is *dense and strong enough* to thermalize a **coherent return** (not just generate harmonics).

### 3.2 · What sets the crossover — a DERIVED resonance-overlap threshold [FORM-level forward prediction]

Thermalization (an irreversible scramble that a coherent return does not survive) is a **stochasticity threshold**, not a smooth onset — the Chirikov resonance-overlap criterion. The Kerr term produces an amplitude-dependent frequency shift per mode

```
δω_nl  ~  g_Kerr · ⟨A²⟩ · ω_scale ,   with  g_Kerr = 1/4  (DERIVED, §2.1 leading coefficient)
```

The nonlinear resonances (FWM products) **overlap** — and the motion becomes chaotic/thermalizing — when this shift reaches the comb spacing:

```
   δω_nl  ≳  Δω           (resonance overlap ⇒ real downconversion ⇒ revival dies)
⟺  (1/4)·A²·ω_scale  ≳  Δω
⟺  A²  ≳  4 Δω / ω_scale                          [THE DERIVED CROSSOVER]
```

- Below it (`A² ≪ 4Δω/ω_scale`): KAM tori intact, quasi-periodic, **correlation-decay only** — revival survives (the linear lowpass that *looks like* a downshift).
- Above it (`A² ≳ 4Δω/ω_scale`): resonance overlap, **real downconversion** — revival thermalizes and does not return in-window.

**The crossover is a FORM-level derived prediction:** the revival should die *at* `A²/4·ω_scale ~ Δω`, and denser combs (smaller `Δω`) should cross **earlier** in `A`. That "dies-at-a-derived-amplitude" curve — not merely "dies" — is the discriminating chord an interacting-bath arm would test (§5).

### 3.3 · ★ The honest number — at instrument scale the derived coupling is TOO WEAK at MILD (this retro-predicts #734)

Plug in the certified operating point (charter §D-post Dp-4 densest-viable comb + §B1 MILD point):

| quantity | value | source |
|---|---|---|
| MILD amplitude | `A ≈ 0.10` ⇒ `A² ≈ 0.010` | charter §B1 operating-point table |
| comb spacing | `Δω = 0.050` | charter §D-post Dp-4 (densest-viable) |
| drive scale | `ω_scale ~ ω_d ~ 0.5` | charter §A8 (`ω_d = 0.5`), walk anchor 6 (`ω_d=0.524`) |
| **realized** `δω_nl/Δω` | `(1/4)(0.010)(0.5) / 0.050` ≈ **`0.025`** | **derived** |

**`δω_nl/Δω ≈ 0.025 ≪ 1` — the derived nonlinearity is ~40× below the resonance-overlap threshold at MILD.** This is not a failure — **it is a result**: the derived interaction *predicts the #734 null*. The floor-arm ran in exactly the regime where the substrate-native coupling is sub-threshold, so a flat coherent revival is what the derivation expects. The #734 "structural inexpressibility" is thus **sharpened**: on the non-interacting Caldeira–Leggett bath it is an *exact* identity (barrier B1, superposition), and on the *interacting* bath it is *quantitatively* sub-threshold at MILD (barrier: coupling `~40×` too weak) — two different reasons, both pointing the same way at the certified operating point.

**To clear the threshold** you need `A² ≳ 4Δω/ω_scale = 4(0.050)/0.5 = 0.40 ⟹ A ≳ 0.63` — the **near-knee** regime (charter §B1 near-knee `A≈0.50`, run-peak `~0.60`). So the derived dephasing arrow is expected to fire **only at or beyond the near-knee**, which is at the edge of / outside the certified `A≤0.50` envelope — and pushing a *dense* comb to `A≈0.63` is exactly where the meter's identity-conservation is at risk (over-transfer / clamp firing, charter §D-post Dp-1). **This is why the candidate needs full re-cert, not a config tweak.**

### 3.4 · Dephasing-structure verdict

**DERIVED-YES (thresholded), with a GENUINE FORK on the operating point + a second required barrier (the port).**

- The **interaction FORM is derived unambiguously**: the shared-`S(A)` Kerr/FWM coupling (§2.1) is the axiom-grounded mode–mode channel; candidate (b) is a *separate* barrier, not an alternative form; the phenomenological `λ·x_i·x_j` is rejected. **No genuine fork on the FORM.**
- The **dephasing STRUCTURE is derived-yes conditionally**: the interacting comb *does* thermalize a coherent return, but only **above** the derived overlap threshold `A²/4·ω_scale ≳ Δω`, which at instrument scale sits at `A ≳ 0.63` (near-knee) — **outside** the MILD envelope where #734 was measured. At MILD it is `~40×` sub-threshold (retro-predicting the null).
- **The genuine forks are two, and they are Grant's calls (§7):** (i) the **operating point** — fire near-knee (breaks the envelope + κ-band + identity ⇒ full re-cert) vs. accept a derived-too-weak null vs. abandon-and-route-to-the-X40-click; and (ii) the **bath↔lattice port** — the scalar-port + global-rescale bottleneck (barrier B2) means *even a near-knee interacting bath cannot dephase the signal unless the port is promoted to a phase-carrying one*, which is the single largest identity-breaking change.


## 4 · Certificates that break + the re-cert battery scope

### 4.1 · Which certificates break (enumerated precisely, with charter cites)

| # | Certificate | Where certified | Why the interacting-bath candidate breaks it |
|---|---|---|---|
| C1 | **#721 identity-conservation** — energy conservation is an **ALGEBRAIC IDENTITY** on STANDALONE-K4 (orthogonal 4-port scatter + orthogonal bond connect + arithmetic-exact quadratic global rescale) | charter §B-post **R-1** (*"pump-immunity was STRUCTURALLY GUARANTEED, not empirically survived"*) + the **★SCOPE CAVEAT**: *"ANY genuine irreversible ε→T2 depletion primitive BREAKS the conservation identity ⇒ the W-battery must be RE-VALIDATED"* | **Both barrier-lifts break it.** Lifting B2 (a spatially-structured, phase-carrying back-reaction) means the back-reaction is **no longer a global scalar multiple**, so the §A1 *"a scalar multiple of an on-shell TLM state stays on-shell"* argument (charter §A1) fails ⇒ conservation is no longer arithmetic-exact ⇒ **the pump the §B1 risk feared can resurrect and must be EMPIRICALLY bounded** (W2 stops being a structural pass). This is exactly the caveat's *"genuine irreversible ε→T2 depletion primitive"* clause. |
| C2 | **W-battery METER-VALID-NONLINEAR-ENVELOPE** (`A ≤ ~0.50`) | charter §B3 / §B-post Verdict (scoped to STANDALONE-K4) | The near-knee operating point (`A ≳ 0.63`, §3.3) sits **at/over the `A≤0.50` envelope edge**; W2's *structural* pass (C1) no longer holds ⇒ W1–W6 re-run required on the interacting coupler. |
| C3 | **κ-band `METER-VALID-KAPPA-BAND[0.030,0.030]`** | charter §C-post §C-pr1/§C-pr2 | The candidate's stronger drive + near-knee amplitude push past the single certified κ=0.030 point; the X-battery (X1–X6) was validated only there ⇒ X-battery re-run at the arm's κ. |
| C4 | **§D floor-band `FLOOR-METER-VALID-BAND[0,5]`** (`Δω=0.050`) | charter §D-post **Dp-5** | The floor-band identity ledger (`LEDGER_ID_TOL=1e-6`) rests on the C1 identity; an interacting bath at near-knee re-opens the over-transfer/clamp risk (Dp-1) *at lower ρ* ⇒ FB1–FB5 re-run required. |
| C5 | **κ·g degeneracy** — coupling enters only as the product `κ·g` | `f6_bath_meter.py:198` (`self.p += dt * kappa * self.g * q`) | The Kerr cross-term (§2.1) makes the effective coupling **amplitude-dependent** (`z_local(A)`), so the coupling is no longer a single scalar product `κ·g` — the degeneracy that let the meter treat `κ·g` as one knob is lifted; the re-cert must track `κ`, `g`, **and** `A` independently. |
| C6 | **Nyquist / harmonic-aliasing guard** (`M≤95`, `ω_max·dt<π`) | charter §A4 / §B W4 | A Kerr/FWM bath *generates* new spectral content (`n·ω_d`, sum/difference tones); harmonics can alias past the guard the linear bath never populated ⇒ the aliasing guard (A4) + W4 harmonic-honesty must be re-validated with the FWM spectrum live. |

**Not broken (structural carry-over, if the bath comb structure is unchanged):** the **M-invariance / twin-64 kill** (charter §B W4 / V2 — an interacting bath still adds only *undriven* high-ω teeth per `M`), the **Nyquist envelope assert itself** (a code guard, unaffected), and the **friction-vs-reactive discriminator** (charter §4/§A5/V4 — still a valid control, and now doubly load-bearing as the "thermalization ≠ loss" reference). These can be **inherited**, not re-derived — flagged in §4.2.

### 4.2 · The re-cert battery scope (SPEC — not run in this lane)

A re-cert of the interacting coupler is **not** the §9 V1–V6 re-run (charter §9); per the R-1 caveat it is a **full W/X/floor re-validation** plus one new leg. Scoped:

1. **W2 becomes GENUINE (the biggest change).** On STANDALONE-K4, W2 was a structural pass (C1). With the phase-carrying port (B2), a scalar rescale no longer conserves arithmetic-exactly, so **W2 is now an empirical drift test that can KILL** — the §B1 secular-pump risk is live for the first time. This is the load-bearing re-cert leg: the interacting coupler must be shown to conserve `E_lat+E_bath` to `R_BATH_MAX` of the transfer over the arm's longest horizon, *empirically*, with a signed-slope anatomy read (charter §C1 method).
2. **A NEW leg — thermalization-vs-loss discrimination (the hardest new certificate).** The arm must prove its dephasing is **substrate-native reversible-but-window-long thermalization** (energy redistributed across the comb, closed ledger) and **NOT** a smuggled `Re(Z)` / integrator leak (energy gone). This is the closed-ledger fraction `R` (charter §4) applied to the *dephasing* event: `R<0.2` (energy found in the redistributed comb — thermalization) vs `R>0.8` (energy gone — a valve, disqualifying). Without this leg a "revival died" result is *ambiguous between the arrow and a bug* (the memory `feedback_structural_null_needs_stencil_lens` failure mode, inverted: a positive that validates a disabled-Ax3 leak).
3. **W1/W3/W4/W5/W6 re-run** on the interacting coupler at the arm's operating point (nonlinear baseline floor, detuning soul-check — now with FWM harmonics in the confound-placement, per charter §B W3's harmonic-aware rule + §C-post R-6 — N_occ honesty under self-generated harmonics, tare residual, friction discriminator).
4. **X1–X6 re-run** at the arm's κ (charter §C2): the over-extraction clamp sub-mode (X1), coupling-broadened detuning collapse (X2), broadened-floor occupancy (X3), two-tank break (X4), tare residual vs κ (X5), dressed-comb/level-repulsion `pulling(κ)<0.005` (X6) — the last is *especially* live because Kerr coupling *dresses* the comb (level repulsion is now a physical prediction, not just an artifact risk).
5. **FB1–FB5 re-run** (charter §D3) on the seeded interacting floor, multi-seed (the §D-post Dp-2 strengthening), with the C1 identity ledger now empirical not structural.
6. **Inherited (not re-derived), flagged:** M-invariance/twin-64 (C2-adjacent), the Nyquist assert, the friction control's *existence* (its calibration is re-run in W6/2 above).

**The re-cert verdict-class posture:** follow the charter's own precedent — a **bounded envelope** (`METER-VALID-INTERACTING-ENVELOPE[A_lo, A_hi]`) with a hard **KILL** if W2 shows a genuine secular pump OR the new thermalization-vs-loss leg lands the dephasing in the `R>0.8` (loss) bin. Rule 11: no retune-to-rescue; a single mechanism explaining all failures is the discipline working.


## 5 · The arm design (gated on the re-cert) — frozen primary observable + kill shapes

**Gate:** this arm does **not** fire until the §4.2 re-cert returns `METER-VALID-INTERACTING-ENVELOPE`. The design below is frozen *now* (before any re-cert code) so the primary observable is pre-registered, **not invented at fire time** — the direct fix for the #734 **R-1 CRITICAL** (the eaf metric was fabricated-as-pre-registered; here it is frozen up front).

### 5.1 · The FROZEN primary observable (per the routed SPEC seed)

**The ensemble-average-first coherent-revival metric (`eaf`).** Over the frozen floor-seed ensemble, **average the excess ledger FIRST** (cancels the per-realization amount-jitter `√N`), *then* read the coherent revival amplitude at the recurrence `T_rec = 2π/Δω`, in the bath's **modal/spectral coordinate** (§1 A46 discipline). This is the metric the #734 fire found *well-behaved* (jackknife-stable), routed forward by the disposition seed (`…f6-thermal-floor-arm_result.md` §4: *"a future interacting-bath arm should pre-register the ensemble-average-first coherent-revival metric … this time frozen, not invented at fire time"*). **It is the frozen primary — no headline may lean on any post-hoc substitute.**

**The co-primary discriminator (frozen): the closed-ledger fraction `R` at the dephasing event** — energy that leaves the coherent revival must be **found redistributed across the comb** (`R<0.2`, thermalization), not gone (`R>0.8`, loss/valve). Without this, a dead revival is ambiguous between the arrow and a smuggled-loss bug (§4.2 leg 2).

**The forward quantitative chord (frozen): the crossover.** Sweep `A` (and comb density `Δω`) across the derived overlap threshold `A²/4·ω_scale ~ Δω` (§3.2) and test that the revival dies **AT** the predicted amplitude, with denser combs crossing earlier. This is the AVE-distinct content — "dies at a derived `A`", not merely "dies" (memory `ave-discrimination-check`).

### 5.2 · Frozen kill shapes (Rule 11 — declared before any fire)

- **DEPHASING-CONFIRMED** — the `eaf` revival is **monotonically suppressed** with interaction strength (`A` / comb density / κ), **AND** the suppression **exceeds the seed-ensemble budget** `CoV ≈ 0.17–0.23` (the FROZEN arm-ensemble budget, charter §D-post Dp-2/Dp-4), **AND** `R<0.2` (energy redistributed — thermalization, not loss), **AND** the death onset tracks the derived crossover `A²/4·ω_scale ~ Δω` within a frozen tolerance. All four required — the conjunction is the anti-artifact guard.
- **NO-DEPHASING (the live falsifier)** — the `eaf` revival stays **flat** (the #734 ride-on-top, now in the interacting regime). Interpreted per §3.3: the derived coupling is sub-threshold at the tested `A` (a *quantified* null — a result, not a failure; record `δω_nl/Δω` and the `A` reached).
- **ARTIFACT-LOSS (disqualifying, NOT a positive)** — the `eaf` revival is suppressed **but** `R>0.8` (energy gone, ledger open). This is a smuggled `Re(Z)`/integrator leak masquerading as the arrow ⇒ **the meter is invalid, STOP** — do not bank a "dephasing arrow" (the honest-closure trap the §4.2 leg-2 certificate exists to catch).
- **PORT-BLIND (structural null, expected if B2 is not lifted)** — if the arm keeps the scalar-port + global-rescale coupling, the `eaf` revival stays flat *even at near-knee* because the floor's phases cannot reach the signal (barrier B2, §2.2). This is the pre-registered expectation absent the port change; it **confirms** the two-barrier derivation rather than falsifying the arrow.

### 5.3 · Rule-10 empirical-driver discipline (baked into the frozen design)

- **Reactance-pair tracking (mandatory).** Record BOTH the C-state (`V_inc/ω`, per-mode) AND the L-state (`Φ_link/ω_dot`) at **every step** over the recording window, at ρ∈{0, at-signal, past-signal} × A∈{mild, near-knee}. A nonlinear bath caught at one phase is consistent with both a thermalized scramble and an oscillator at peak — the pair is required to distinguish (memory Rule-10 corollary; the #734 arm already banked this at ρ∈{0,1,5}).
- **PML-cell exclusion + density-peak sampling.** Inherit the meter's collar-site read (native active sites, no Cartesian stencil); the closed cavity runs PML=0, but any top-K field-density extraction filters PML cells and samples at `top-K |field|²` energy-density peaks, not centroid+offset (memory Rule-10 corollary).
- **Local-clock modulation (Op14 active).** With saturation load-bearing at near-knee, report eigvec localization vs `A²_local` at the collar sites and `ω_local(r) = ω_global·√(1 − A²(r))` — a uniform-global-σ read would miss the locally-modulated modes that carry the Kerr coupling (memory Rule-10 corollary).


## 6 · Rough compute cost

Single-node, CPU (no GPU regime — same plant class as the certified meter, small M).

- **Per-step overhead of the interacting coupler:** the shared-`S(A)` Kerr coupling (§2.1) is *already computed* by the op3 bond pass (`_update_z_local_field` + `_connect_all`) — the lattice pays it whether or not the bath reads it, so the intra-lattice cost is **marginal**. A phase-carrying bath port (B2) adds either O(M·n_collar) (spatial projection) or, for an all-pairs bath-internal coupling, O(M²) — at `M∈{15,24}` that is a few hundred ops/step, **negligible** vs the lattice `step()`.
- **Re-cert battery volume:** W1–W6 × 3 operating points + X1–X6 × 3 κ + FB1–FB5 × 6 ρ × 6 seeds + the new thermalization-vs-loss leg + the crossover sweep (≥3 `A` × ≥2 `Δω`). Each cell is a 3000-step (up to `11·T_rec`) run on the standalone-K4 plant. **Order 10³ integrator-runs.**
- **Wall-clock estimate:** the certified §D battery (6 ρ × 6 seeds × ~3000 steps) runs in minutes on one core; the full re-cert is ~100–300× that volume ⇒ **~1–2 node-days single-core, or a few node-hours parallelized** across the (κ, A, ρ, seed) grid (embarrassingly parallel). The crossover sweep roughly doubles it. **No new engine primitive is needed for the estimate** — the cost is dominated by ensemble × grid × horizon, not per-step complexity.
- **Caveat on the estimate:** if barrier B2's fix requires a genuinely spatially-resolved bath field (not a scalar port), the plant leaves STANDALONE-K4 and the per-step cost rises to the full 3D lattice `step()` per bath channel — that would push the estimate up by the number of independent bath channels. This is a **design-fork-dependent** cost (walk-brief decision #2), flagged not resolved.


## 7 · DESIGN-WALK BRIEF for Grant (the decisions only he should make)

**This is a physics change to a certified instrument — RULING-22 precedent: the design walk happens with Grant in chat BEFORE any build.** Below are the decisions the derivation cannot make for you. Each carries the lattice-first physical picture, the circuit, options, and my recommendation (marked ★REC). The derivation is settled on the *form* (§2) and the *threshold* (§3); these are the *judgment* calls.

### Decision 1 — the operating point (the resonance-overlap threshold sits at near-knee)

**Lattice-first picture.** At a gentle tap (`A≈0.10`) the comb modes ride the shared lattice *independently* — each feels its own bit of the saturation curve, but they don't feel *each other's*. Only when they swing hard enough (`A ≳ 0.63`, near-knee) does the saturation curvature bend enough that one mode's amplitude shifts another mode's frequency past a comb-spacing — the point where the tones start scrambling each other. **Circuit:** a shared varactor whose bias only moves enough to inter-modulate the tones when they drive it hard.

- **(a) Fire near-knee (`A≈0.6`), dense comb** — clears the derived threshold, tests the forward "dies-at-a-derived-`A`" chord. **Cost:** breaks the `A≤0.50` W-envelope (C2), the κ-band (C3), and re-opens over-transfer (C4) ⇒ full re-cert.
- **(b) Stay `A≤0.50`, accept a null** — the derived coupling is `~40×`→ still `~2×` sub-threshold; pre-register NO-DEPHASING as an honest *quantified* null (a result, §5.2).
- **(c) Abandon as instrument-scale-negligible** — route the arrow to the X40 boundary/topological *click* candidate instead (the other open arrow, `…f6-thermal-floor-arm_result.md` §4).

**★REC: (a), scoped as a discrimination test with (b)'s null pre-registered as an honest outcome.** The derived crossover is a genuine forward prediction; it is worth the re-cert *iff* you want the interacting-bath arrow adjudicated rather than routed to the click. If the click (c) is the more promising arrow to you, say so and this whole program defers.

### Decision 2 — the bath↔lattice port (barrier B2 — the biggest identity-breaker)

**Lattice-first picture.** Right now the floor pushes on the whole cavity like a single piston — it changes the *amount* of energy uniformly, but it can't push on individual modes with its own random phases. To *dephase* the signal, the floor has to become a **phased array**: reach into the lattice mode-by-mode and imprint its randomness. **Circuit:** the certified coupling is a single series reactance (scalar `q` in, global rescale out — "amount"); a phase-carrying port is a *distributed* coupling network (per-site, phase-resolved).

- **(a) Keep the scalar port + global rescale** — faithful to the certificate, but the floor-arrow stays **structurally inexpressible even nonlinear** (barrier B2 persists; §2.2). The arm would only ever thermalize the lattice's *own* modes, never carry the floor's phase to the signal ⇒ pre-registered PORT-BLIND null (§5.2).
- **(b) Promote to a spatially-resolved, phase-carrying port** — the change that lets the floor dephase the signal. **This is the single largest re-cert driver:** a structured back-reaction is no longer a global scalar multiple, so the #721 conservation identity (C1) is broken *by construction* and W2 becomes an empirical pump-hunt (§4.2 leg 1). It also potentially leaves STANDALONE-K4 (compute caveat, §6).

**★REC: (b) is REQUIRED for a genuine floor-dephasing test — but flag it plainly: this decision turns "a re-cert" into "effectively a new instrument."** If you are not ready to build a new instrument, Decision 1(a)+2(a) is a *coherent but pre-doomed* configuration (it will return PORT-BLIND), and the honest move is Decision 1(b) or 1(c). **The pre-test-physics question I'd want answered first (memory `pre-test-physics-check`): is the floor physically a piston or a phased array?** i.e. does the T2 sink couple to the lattice as a single collective amount-channel (Grant's own #734 "static noise floor / effectively constant" ruling leans *piston*), or does it have per-mode phase access? Your ruling on that *is* the port decision.

### Decision 3 — the interaction-form provenance sub-fork (does the T2 bath itself saturate?)

**Lattice-first picture.** Two ways to make the bath modes feel each other: (i) they all ride the *lattice's* one shared varactor (`S(A_lattice)` — the derived §2.1 channel, weakest, most faithful), or (ii) the *bath itself* is a saturable medium (each bath mode carries its own `A`, and they share a bath-side `S(A_bath)`). Option (ii) is stronger coupling — but it asserts the **T2 entropic register carries its own Ax4 rupture ceiling**, which is a sector-ownership claim (does heat saturate, or only the lattice draining into it?). **Circuit:** (i) = tones sharing the lattice's varactor; (ii) = the heat-sink is itself a nonlinear (saturable) reservoir.

- **(a) Bath couples only through the shared *lattice* `S(A)` (candidate §2.1 as-derived)** — no new axiom; tests whether the lattice-native coupling suffices.
- **(b) Promote the bath to a saturable T2 medium (`S(A_bath)`)** — stronger, but requires a sector ruling that T2 carries an Ax4 kernel (a genuine substrate-ownership question, memory `feedback_ee_is_substrate_native_language` / `feedback_sector_ownership`).

**★REC: (a) first — it is the faithful, axiom-minimal channel; only escalate to (b) if (a) is derived-too-weak AND you rule that the T2 sink saturates.** This is a real substrate question I should *not* answer for you: whether the entropic register has a rupture ceiling is Grant/corpus territory, not a derivation this lane can force.

### Decision 4 — the re-cert scope (how much of the certified meter carries over?)

**Lattice-first picture.** The #721 identity underwrote *half* the certificates *structurally* (W2 couldn't fail because conservation was algebra). Once you break the identity (Decision 2b), that structural guarantee is gone — how much do you re-measure vs trust?

- **(a) Full re-cert** — W + X + FB batteries all re-run on the interacting coupler (§4.2).
- **(b) Targeted re-cert** — only the identity-dependent legs (W2 empirical drift + FB1/FB2 ledger + the NEW thermalization-vs-loss leg), inheriting M-invariance / Nyquist / friction-existence (§4.1 "not broken").

**★REC: (b)+the new leg, with the inherited legs explicitly *listed* as structural-carryover (not silently assumed).** Re-running the twin-64 kill or the Nyquist assert buys nothing if the bath comb structure is unchanged; the load-bearing re-cert is W2-now-empirical + FB-ledger + the thermalization-vs-loss discriminator. Mark the carry-over set in the re-cert charter so an auditor can check each inheritance is legitimate (the `feedback_structural_null_needs_stencil_lens` guard).

### Decision 5 — ratify the frozen primary observable (confirm the freeze; not a physics fork)

**Picture.** The #734 fire's R-1 CRITICAL was that the coherent-revival metric (`eaf`) was *invented at fire time* and mis-attributed as pre-registered. §5.1 freezes it up front. This is a **ratification**, not a fork.

- Confirm: **`eaf` (ensemble-average-first coherent revival) = FROZEN primary**; **closed-ledger `R` (thermalization ≠ loss) = FROZEN co-primary discriminator**; **the derived crossover `A²/4·ω_scale ~ Δω` = the frozen forward chord** (§5.1). Kill shapes per §5.2.

**★REC: ratify as frozen.** If you want a *different* primary, it must be frozen *now* (before any interacting-bath code) — the whole point of this SPEC-before-build gate is to avoid a second fire-time-invention.


## 8 · Verdict + disposition (Rule 11 / Rule 12)

**Derived interaction form:** the **shared-`S(A)` intermodulation** (Kerr/four-wave-mixing, §2.1) — the axiom-grounded mode–mode coupling the lattice itself provides; leading coefficient `1/4` fixed by the canonical `(1−A²)^(−1/4)` kernel. Candidate (b) (scalar-port → phase-carrying port) is a **second, separate barrier**, not an alternative form; the phenomenological `λ·x_i·x_j` and the `Re(Z)` valve are REJECTED with reasons (§2.3). **Provenance: DERIVED throughout; no VALUE import.**

**Dephasing-structure verdict: DERIVED-YES (thresholded).** The interacting comb *does* thermalize a coherent return — but only **above** the derived resonance-overlap threshold `A²/4·ω_scale ≳ Δω`, which at instrument scale is `A ≳ 0.63` (near-knee). At the certified MILD point it is **`~40×` sub-threshold**, which **retro-predicts the #734 null**. The genuine **FORK is not on the form — it is on the operating point + the port** (Decisions 1 & 2), both of which break named certificates and both of which are Grant's calls.

**Certificates broken (⇒ full re-cert, not a config tweak):** #721 identity-conservation (C1), the W-envelope (C2), the κ-band (C3), the §D floor-band (C4), the `κ·g` degeneracy (C5), the Nyquist/harmonic guard (C6) — §4.1. The re-cert makes **W2 empirical for the first time** and adds a **thermalization-vs-loss** certificate (§4.2). Rough cost: ~10³ integrator-runs, ~1–2 node-days single-core (§6).

**Disposition (Rule 11 / Rule 12):**
- This lane **STOPS at the build gate** (per charge). No meter/engine edits, no build, no arm fire. The deliverable is this derivation + SPEC + the walk brief.
- **Nothing is refilled into the #734 slot** (Rule 12): the #734 FLOOR-ARROW prediction stays retracted; this SPEC is a **new, separately-versioned candidate** with its own verification chain (the re-cert battery), not a rescue of the falsified reactive-floor mechanism. It earns a charter + frozen prereg **only if** Grant's Decision 1/2 rulings green-light a build.
- **Owed to the auditor lane (implementer surfaces, auditor lands):** the two-barrier sharpening of the #734 result (barrier B2 — the scalar-port bottleneck — is a *second* structural reason the arrow is inexpressible, under-weighted in the #734 framing); and the retro-prediction that the derived coupling is `~40×` sub-threshold at MILD (a *quantitative* consistency between the derivation and the #734 null). This lane does **not** edit the #734 result doc nor draft the auditor's engine-capability-map §8c entry — it surfaces the finding for adjudication.

**Contradiction flagged (flag-don't-fix), NOT resolved here:** the #734 result §0(b) headlines the inexpressibility as *"the bath is a set of INDEPENDENT harmonic oscillators … no mode–mode coupling"* (barrier B1 only). This derivation finds that **even lifting B1 does not suffice** — the scalar-port + global-rescale bottleneck (barrier B2) independently blocks floor→signal phase transfer (§2.2). The two docs are not in conflict on the *verdict* (arrow inexpressible on the certified instrument), but the #734 *mechanism sentence* is **incomplete** (names one of two barriers). Surfaced with both file paths for Grant/auditor adjudication; the #734 doc is not edited by this lane.

---

*SPEC (derivation + re-cert spec + design-walk brief), BUILD-GATED. The lattice provides a substrate-native mode–mode coupling (shared-`S(A)` intermodulation, DERIVED), so a dephasing arrow is derivable in FORM — but it is `~40×` sub-threshold at the certified MILD point (retro-predicting the #734 null) and blocked by a second scalar-port barrier the #734 framing under-weighted. A genuine floor-dephasing arm needs a near-knee operating point AND a phase-carrying port, each breaking a named certificate ⇒ full re-cert. Verdict: DERIVED-YES (thresholded) on the FORM; GENUINE FORK on the operating point + port (Grant's calls, §7). This lane stops at the build gate; nothing is refilled into the #734 slot (Rule 12). All anchors content-verified at HEAD `1be045a1`.*

