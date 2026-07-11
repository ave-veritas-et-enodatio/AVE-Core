# RESULT — X43: the ringdown-port decay-rate exponent Γ(ω) → **CLEAN NEGATIVE (the picture dies)**

**Date:** 2026-07-11 · **Branch:** `analysis/x43-ringdown-port` · **Pre-reg (FROZEN, pushed first):** `research/2026-07-11_x43-ringdown-port_prereg.md` (commit `8d672d3a`, pushed before any derivation — P9 freeze proof).
**Class (consistency-vs-emergence):** the emergent exponent is **emergence-class** (derived from mode/multipole counting with zero Sargent/CODATA input; both anti-install traps CLEAN) — but it is a **NEGATIVE emergence**: the form the substrate produces does **not** match observation. **This is a fully banked outcome** (the brief: "an honest negative is a fully banked outcome"; Rule-11 honest closure).

---

## SECTOR HEADER

- **MODE.** Spectral (muon at rest, internal clock `ω_int = mc²/ℏ` above the band), NOT translation.
- **SECTOR.** Longitudinal / V-sector parity-gated neutrino drain (Cosserat torsional channel, keyed on `γ_c`), NOT transverse EM.
- **REGIME / PHASE-STATE.** Cold lattice, single excitation, above-band evanescent, sub-yield (the drain is a boundary/port coupling, Axiom-3 lossless bulk).

---

## ★ VERDICT

> **The ringdown-port picture DIES. Under no verified reading does the lattice produce Sargent's `Γ ∝ ω⁵`.**
>
> The honest lattice derivation gives an **electric-dipole `Γ ∝ ω³`** (from shedding the muon's **one** Cosserat torsion quantum, `ΔJ = Δc = 1 → ℓ = 1`) — **the `ω³` "picture-dies / dipole-class" bin.** And even that `ω³` is **voided at the physical muon energy**: `ω_μ = 206.77 ω_C` sits **~12× above the drain band top** (`≤ 17.011 ω_C`), so the resonant drain DOS `ρ_drain(ω_μ) = 0` (a 3D-robust obstruction); the surviving leak is **evanescent, wrong-sign (heavier → slower), and non-universal → no clean power law** — the **"no-law / wrong-circuit" bin**.
>
> **Result lands CONTESTED between the `ω³` and `no-law` bins — BOTH are "the picture dies."** The two are separated by exactly **one unadjudicated corpus fork** (§"The fork"). **Neither is `ω⁵`.**
>
> **Anti-install audit: CLEAN.** TRAP 1 (no SM three-body phase-space import): **CLEAN** in every frame. TRAP 2 (multipole order derived, not asserted): **CLEAN** — `ℓ=1` fell out of the single shed quantum; the anti-install tell is that the honest derivation lands on `ω³` (the "wrong" answer) rather than reaching for the `ℓ=2` that would reproduce observation. **Electron-stability boundary anchor: RESPECTED** (all live frames give `Γ = 0` in-band).

---

## THE HONEST DERIVATION (both traps clean)

`Γ` per cycle = (leak rate through the port) / (stored energy). Fermi golden rule `Γ = (2π/ℏ)|M|² ρ_drain(ω)`. The exponent `n` is the ω-scaling of `|M|²·ρ_drain`.

**Step 1 — the multipole order `ℓ` (TRAP 2, DERIVED not asserted).**
The muon is the electron's `(2,3)` topology plus **exactly ONE quantum of Cosserat torsional excitation** (`ch14-leaky-cavity-particle-decay/theory.md`; `Q-G27`). The decay `μ→e` sheds that one quantum. Torsion is a rotational DOF, so one quantum carries **one unit of torsional angular momentum**: `ΔJ = Δc = 1`. The radiation must carry it away → the **lowest allowed multipole is `ℓ = |ΔJ| = 1` (electric-dipole class)**. Two independent exclusions of the lower order: (i) a monopole `ℓ=0` carries **zero** angular momentum and cannot conserve the shed `ΔJ=1`; (ii) `ℓ=0` is the A1-longitudinal-scalar sector, orthogonal to the T2 shear that carries the torsion (`A1 ⊥ T2` sector orthogonality). The quadrupole `ℓ=2` is **not reached** — shedding one quantum is `ΔJ=1`, not `2`. **Chiral gate check:** `Δc = 1 ≤ Δc_crit = 3`, so the parity gate is OPEN and the left-handed drain mode couples (`chiral-screening.md:13-20`; a `Δc > 3` process would be evanescently screened — the right-handed-ν parity-violation mechanism). **`ℓ = 1` is forced by "one quantum → one unit of angular momentum," not tuned to a target.**

**Step 2 — the drain DOS (TRAP 1, honest srs count, NOT imported phase space).**
The parity-gated V-sector drain is the srs vector/Cosserat channel: **3 acoustic branches, `ω ∝ k` near `k=0`** (`srs-vector-band-survey_result.md:141,165`), giving a **3D Debye density of states `ρ(ω) ∝ ω²` below the band top**. **This `ω²` is the lattice acoustic count — NOT a relativistic three-body final-state factor `ρ(E) ∝ E⁵`.** The lattice forces a **single** emitted Cosserat quantum (`N=1`), so there is no three-body counting to import.

**Step 3 — the product.** `|M_ℓ|² ∝ ω^(2ℓ−1) = ω¹` (dipole) `× ρ_drain ∝ ω²` `⇒ Γ ∝ ω³`. (`n=3` is the mechanism's **in-band** limit; all three live frames land here or below — see the void, next.)

---

## WHY IT IS A NEGATIVE — TWO INDEPENDENT KNIVES

**Knife (a) — `ω³ ≠ ω⁵`, and the gap is exactly the forbidden import.**
The observed Sargent law is `Γ ∝ ω⁵` (`(m_τ/m_μ)⁵ ≈ 1.345×10⁶` vs measured `≈ 1.32×10⁶`, ~2%). The lattice gives `ω³`. **The two-power deficit is precisely the SM three-body final-state phase space** — the *second* neutrino. The lattice forces **one** shed quantum (`N=1`, a dipole, effectively a 2-body emission → a *line* spectrum), whereas the observed 3-body Michel continuum (`μ → e ν̄_e ν_μ`) needs a **second** emitted quantum, adding one `∝ω²` phase-space factor. There is **no derived lattice reason** for that second neutrino; supplying it is exactly TRAP 1. **The honest exponent stays `ω³`.** (Anti-install tell: a frame reverse-engineering the answer would have picked `ℓ=2`/`Δc=2` to reach `ω⁵`; none did.)

**Knife (b) — the above-band void (3D-robust): even `ω³` is not live at the muon energy.**
`ω_μ = 206.77 ω_C` sits **~12× above** the vector/Cosserat drain band top (`≤ 17.011 ω_C`, `srs-band-structure.md:83-96`) — the muon clock would need a drain wavevector `k_μ/k_BZ ≈ 66×` the zone edge. So **`ρ_drain(ω_μ) = 0`**: there are no propagating drain modes at the emission energy, and the resonant `ρ∝ω²` circuit is void there. The `ω³` law is an **extrapolation of the in-band Debye DOS past its domain.** What survives is an **evanescent** leak (the banked above-band result: an above-band drive is evanescent-only, `V_n ∝ (−1)^n e^{−κn}`, `cosh κ = ω²/2 − 1`, `superband-carrier-fork_result.md §0`). Since `κ(ω)` **grows** with `ω` (`κ_μ ≈ 10.7`, `κ_τ ≈ 16.3`), the overlap `e^{−κd}` and rate `~e^{−2κd}` **DECREASE with mass** — **wrong sign** (heavier → slower; but observed `τ_μ = 2.2 μs` ≫ `τ_τ = 0.29 ps`, heavier → *faster*), and non-universal in the port distance `d`. **Wrong sign is a picture-death signal → no clean power law.**

---

## ELECTRON STABILITY (boundary anchor — RESPECTED)

All three live frames give `Γ = 0` for the electron **by construction, not by cancellation**: the electron is the ground `(2,3)` winding with **zero** surplus Cosserat quanta (`Δc = 0`), sitting in-band (`ω_C` below every band top) and below the yield voltage. There is **no surplus quantum to shed**, so the port has no source to couple. A model predicting electron decay would be dead on arrival; this one gives electron stability identically. ✔

---

## ★ THE FORK (flag-don't-fix; substrate-adjudicates — the ONE thing between the two negative bins)

The two negative outcomes (`ω³` vs `no-law`) are separated by a single **corpus-unadjudicated** question about the drain channel:

> **Is the neutrino V-sector drain a lattice Cosserat channel (band top `≤ 17 ω_C` → `ρ_drain(ω_μ) = 0` → no-law / wrong-sign), or a genuine non-lattice longitudinal-scalar continuum (no cutoff → a *would-be* `ω³`, but with an *uncomputed* emitter-drain overlap form factor at `k ≈ 66×` Nyquist)?**

- The `ω³` frames (golden-rule, ee-impedance) get the correct sign **only** by assuming a propagating drain mode exists AT `ω_μ` — golden-rule by extrapolating the in-band Debye law past the band top (self-flagged), ee-impedance by positing a trans-Nyquist longitudinal-scalar continuum drain (self-flagged as its largest caveat; note the corpus stance "the longitudinal V-sector scalar is real, Heaviside-excised" is *consistent* with a continuum reading but does not settle whether it is band-limited on the srs lattice).
- The evanescent frame is anchored in the **verified** facts (12-band lattice survey top `≤17 ω_C`; banked evanescent-only above-band result) and leans **no-law / wrong-sign**.

**Both branches are negative.** Per flag-don't-fix and substrate-adjudicates-forks, this fork is **surfaced, not fiat-resolved** — the engine/corpus decides, not this lane. **One-sentence open question for Grant:** *does the parity-gated neutrino drain live on the srs Cosserat lattice band (top `≤17 ω_C`) or is it a genuine non-lattice longitudinal continuum?* — that single fork is all that stands between `ω³`-dipole-death and no-law-death.

---

## FORM/VALUE + ESCAPE HATCHES (un-run, honestly named)

- **FORM/VALUE law respected.** The exponent is the FORM (what was under derivation); it emerged `= 3` (or no-law), not `5`. The absolute coupling / `Q` (the `G_F`-analog, `Q_μ ≈ 3.5×10¹⁷`) would be a VALUE-import — but that question is **moot**, because even the FORM (the exponent) does not match. No chord.
- **Escape hatches NOT run (each would need its own gate; none rescues the picture without new physics):** (1) the 3D above-band **skin-suppression magnitude** is 1D-scoped (superband) — the `ρ=0` obstruction is 3D-robust but the exponential magnitude is un-run; (2) a **multi-quantum cascade / lattice-forced pair-emission** (a second neutrino from chiral handedness conservation) is the *only* route that could reach `ω⁵` — but it would **reconstruct the forbidden Sargent three-body counting** and must be shown lattice-forced without importing it (TRAP 1); un-run, flagged; (3) the **trans-Nyquist continuum-drain overlap form factor** at `k ≈ 66×` Nyquist is uncomputed (the ee-impedance frame admits it "could suppress rather than power-law-scale").

---

## THE TWO PRE-REG TENSIONS (carried forward; still flag-don't-fix)

- **Tension A (Zener-shatter vs nearly-closed port) — SHARPENED, recommend a walk-back flag.** The **canonical** decay leaf `ch14-leaky-cavity-particle-decay/theory.md` (claim `clm-c54kdd`) models the muon as being in **continuous above-yield breakdown** (voltage eclipses `V_yield`, `R_eff` drops `1 GΩ → 50 Ω`, "half-life from RC-discharge time constants") — the `Γ=−1` shatter side. But a continuous `50 Ω` breakdown gives **`Q ~ 1`, not `Q_μ ≈ 3.5×10¹⁷`** — the observed lifetime is ~40 OOM longer than a bare breakdown allows. The high `Q` **forces** the nearly-closed-port reading; a reconciliation is available (the breakdown is the *rare terminal jump*, its **low duty cycle** IS the nearly-closed port / high `Q`), but it means the canonical `ch14` "continuous rupture → RC-discharge" model is **quantitatively wrong on the lifetime as written.** **Recommend for Grant:** flag `ch14` (+ the two `Γ=−1` shatter leaves) for a Q-consistency walk-back; do not resolve in-lane.
- **Tension B (naive `2ω_C` vs canonical band tops) — used the canonical tops.** The derivation used the canonical srs band structure (scalar `5.44 ω_C`, vector `[5.441, 17.011] ω_C`), not the naive `2ω_C`. The above-band premise SURVIVES (muon above every top) and the electron-stability anchor SURVIVES; "103×" is not headlined; the drain-count used the canonical vector-channel DOS. This tension is **resolved in favor of the canonical tops** and is in fact the load-bearing fact behind Knife (b).

---

## MISS-LEDGER

This ringdown convergence was the **6th convergence-shaped move** of the 2026-07-10/11 register arc; the program's hopeful-interior-mechanism ledger stood at **0-for-7** (`impedance-register-walks_framing.md:7`). It **paid to kill and failed** — exactly as the ledger warns a pretty convergence will. **Ledger → 0-for-8.** The `γ_c`/leakage-inductance "named-component convergence" was a rhyme: the port is real, but the exponent it forces (`ω³`, or no-law above-band) is not Sargent's `ω⁵`.

---

## PROVENANCE (the immune system functioned as designed)

Blind independent-derivation panel (workflow `x43-exponent-blind-derivation`, run `wf_b4467fe8-cfd`): **4 frames derived `n` WITHOUT being told the target bins** (golden-rule, multipole-radiation, evanescent-tunneling, ee-impedance) + an adversarial adjudicator that **was** shown the bins. Results: golden-rule `n=3`, ee-impedance `n=3`, evanescent-tunneling `no-law`; the multipole-radiation frame **errored** (StructuredOutput retry cap) but its content was fully covered — `ℓ=1` was derived independently by the other three. **The adversarial lens caught the key artifact:** the `2-1` majority for `ω³` rests on over-applying the (supplied-for-orientation) multipole identity `ω^(2ℓ+1)` **past the band top**, where `ρ_drain(ω_μ)=0` and it is invalid — precisely the shared-blind-spot failure mode the redundancy methodology exists to catch. All citations grep-confirmed against `origin/main`. Both traps independently verified CLEAN; the honest-derivation-lands-on-the-wrong-answer (`ω³`, not `ℓ=2`/`ω⁵`) is the strongest anti-install tell.
