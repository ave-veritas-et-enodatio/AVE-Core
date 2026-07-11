# FRAMING NOTE — three walks: muon/tau ringdown, the anisotropic Nyquist edge, and the π-register audit (2026-07-11)

**★ FRAMING, NOT DERIVATION — nothing canonized; every claim awaits its own gate.**

**Date:** 2026-07-11 · **Status:** in-chat walked pictures (Grant-walked 2026-07-10/11 + orchestrator-elaborated), captured verbatim-faithful. Nothing below is canon. Every §-claim is a candidate framing awaiting its own derivation/registration gate; the cited PRs/leaves/research walks are *pointers* to where the load-bearing work either lives or is owed. Companion to the impedance-register framing note (`research/2026-07-10_impedance-register-walks_framing.md`), the R-B fossil-walk framing note (`research/2026-07-10_rb-fossil-walk_framing.md`), and the rulings docket (`_orchestration/2026-07-10_rulings-docket.md`).

---

## §1 THE RINGDOWN PICTURE — muon/tau decay as an above-band spectral ringdown

Grant-walked 2026-07-10/11: *"bullets traveling too fast to propagate freely through their mediums, shedding energy until they can."*

**SECTOR / REGIME / PHASE-STATE.** MODE = **spectral content vs the lattice band**, NOT translation through it. REGIME = **cold lattice, single excitation** (one soliton ringing, not a driven many-body bath). The whole picture reasons about where a particle's internal clock sits relative to the band, not about its motion through space.

**(a) The "too fast" HOMONYM.** "Too fast" has two unrelated senses and the picture rides the second:
- **Translational** (Cherenkov / accelerator-wake class): a charge moving `v > c_medium` sheds radiation until `v ≤ c_medium`. Endpoint = **the same object, slower**. This is drag, and it is NOT the decay picture.
- **Spectral**: a muon **at rest** decays — nothing translates. Its *internal clock* `ω = m c²/ℏ` sits **~103× above the lattice band edge** `ω_max = 2c/ℓ_node` (the muon clock is `m_μ/m_e = 206.77` electron-clocks, and the electron sits at half the band edge, so `206.77/2 ≈ 103`). Endpoint = **a DIFFERENT object** whose clock fits **in-band**. The "shedding until it can propagate" is spectral relaxation, not deceleration.

**(b) The picture.** Generations = **excited modes ringing down through a nearly-closed port** to the **in-band ground state**. The electron is the **lossless in-band configuration at half the band edge** (`ω_e = ω_max/2`). The exponential decay law is then a **constant-hazard single-jump ringdown** (excited-atom class: one photon-like emission at a fixed per-unit-time hazard), NOT projectile drag (which would give a power-law slowdown, not a clean exponential).

**(c) THE Q ARITHMETIC.** Read as a resonator ringing down, each generation has a quality factor `Q = ω·τ`:
- `Q_μ = ω_μ·τ_μ ≈ (1.605×10²³ rad/s)(2.197×10⁻⁶ s) ≈ 3.5×10¹⁷`;
- `Q_τ = ω_τ·τ_τ ≈ 7.8×10¹¹`.

These are **absurdly high Q**. A **bare** above-band mismatch at **order-unity coupling** would dump its energy in `~1/ω ≈ 10⁻²³ s` — 40+ orders of magnitude faster than the muon actually lives. So the drain **cannot** be a bare mismatch; it **must be a nearly-closed port** (a tiny coupling leaking a huge stored energy very slowly). The corpus already has the matching named component: the **weak sector is a below-cutoff evanescent channel** keyed on the Cosserat couple-stress modulus `γ_c`, with characteristic length `l_c = √(γ_c/G_vac)` setting the weak-force range (`manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md:39`), and its EE-translation names that same `γ_c`/`l_c` the **transformer leakage-inductance** characteristic length (`manuscript/ave-kb/common/translation-tables/translation-circuit.md:200`, `:556`). A nearly-closed port = a large leakage inductance = a below-cutoff evanescent tail: **a genuine named-component convergence, not a new invention** — the "nearly-closed port" the Q arithmetic demands is a component the corpus already carries.

**(d) ★FROZEN KILL-TEST (the bankable form target).** Any AVE port mechanism for this drain must reproduce **Sargent's rule** `Γ ∝ ω⁵` (`Γ ∝ m⁵`). Empirical check: `(m_τ/m_μ)⁵ = 16.817⁵ ≈ 1.345×10⁶` versus `(τ_μ/τ_τ)·BR(τ→μνν ≈ 0.174) ≈ 1.32×10⁶` — **~2% agreement**. The exponent is the discriminator:
- **`ω`** (bare above-band mismatch) → dies;
- **`ω³`** (dipole-class radiation) → dies;
- **`ω⁵`** (phase-space of a three-body port) → the only survivor.

The frozen form target is **`Γ ∝ ω⁵`, or the picture dies honestly.** No AVE-distinct number is claimed here — only the *shape* the mechanism must produce.

**(e) The ν channel = the matched drain.** The energy the ringdown sheds leaves through the neutrino channel — the **mode-gated parity content** (the left-handed-only propagating mode of the chiral LC bandgap). The neutrino is the port's matched load, not a spectator.

**(f) NAMED DEBTS.** Nothing here is discharged: (1) the **port calculation is underived** — the `γ_c`/leakage-inductance drain is named by analogy, not computed to give `ω⁵`; (2) the **overtone-vs-scaled-knot fork is open** — is a generation an *overtone* of one knot or a *scaled* knot? (the picture leans overtone, unforced); (3) **band-edge-evanescence is a localization rhyme only**, not a derivation of the mass ratios.

**SEDUCTION ACCOUNTING.** This is the **6th convergence-shaped move** of the 2026-07-10 register arc (after the parity meter, circulator escape, nucleation swirl, entanglement walk, and loaded screw). The program's **0-for-7 hopeful-interior-mechanism miss-ledger** is cited (`research/2026-07-10_impedance-register-walks_framing.md:7`). A convergence this pretty is exactly the shape the ledger warns about — **a rhyme until the `ω⁵` port calculation pays to kill it and fails.**

## §2 THE ANISOTROPIC NYQUIST EDGE — the licensing question for loaded-continuum descriptions

Walked in the Grant-directed eigencavity satellite; captured here for the core record.

**SECTOR / REGIME / PHASE-STATE.** This is a **geometric / licensing question about DESCRIPTIONS**, NOT a new observable. It asks: *when is a continuum (effective-medium) description of the loaded lattice licensed, and when does the discrete Nyquist edge forbid it?* No number moves on the answer; the point is which calculations are allowed to be believed.

**(a) Liquid/solid = two phase-characters of ONE crystal.** The "liquid vs solid" language is the **continuum vs discrete** phase-character of the *same* srs crystal, keyed on `λ_probe/ℓ_node` — the phonon↔sound analogy (long-wavelength probes see a continuum "sound" medium; short-wavelength probes see the discrete lattice). Two registers coexist and both are true:
- the **Brillouin / Nyquist edge is genuinely barrier-like for spatial content** — sub-2-cell structure is **evanescent, `|Γ|→1`** (the lattice cannot represent it, so it reflects);
- the **effective-medium change is a crossover** — a smooth handover, not a wall.
Barrier (for spatial content) and crossover (for the medium description) are **different registers**, not a contradiction.

**(b) The muonic system STRADDLES the line.** `a_μ = 284.75 fm = 0.737 ℓ_node` — the orbit is **sub-cell**. Naively that says "continuum description dead." But the barrier bites **directionally**:
- **Azimuthal** — the `n=1` closure wavelength is the circumference `= 2π(0.737) ≈ 4.6 cells`, which is **ABOVE Nyquist**, so the azimuthal **ladder mechanism is licensed**;
- **Radial** — the well is order-a-cell across and is treated as a **graded continuum** cascaded through thousands of sub-cell sections (the `saturate=False` driver discretizes a `geomspace` scan over a graded well), which is **sub-Nyquist** → the **radial-continuum grading is the fiction**.

This **converges with the #634 review finding that the radial port-language (`Z(r)`) path was dead code** (`research/2026-07-10_x42-atomic-eigencavity_RESULT.md:55-84`, the port-language derivation path; the review found it non-load-bearing) — **two independent knives on the same joint**: the geometry says the radial continuum is sub-Nyquist fiction, and the code audit says the radial `Z(r)` path never fired.

**(c) ★THE LICENSING CAVEAT — corrects the core session's own earlier relay (logged honestly).** X42's `saturate=True` muonic discriminator **integrates to `r_min ≈ 10⁻⁴·a_μ`** — four orders below the pitch (PR #639; RESULT cross-check `V/V_yield ~ Zα² ≈ 10⁻⁴`, `:66`). So the non-Rydberg "wreckage" (the dense spurious root cluster, `research/2026-07-10_x42-atomic-eigencavity_RESULT.md:158`) is produced **where the continuum kernel has NO license**. The consequence, stated against the earlier relay:
- the muonic spectrum **votes against an UNLICENSED CALCULATION, not cleanly against loading physics** — the earlier reading (that the muonic wreckage was a spectral vote for transparency / against loading) over-claimed;
- canon's **static-sector scope-out fence gains footing** (the fence that says the static loading question is out of scope for this discriminator);
- the **licensed R-A discriminators** are therefore (1) the **CVR bench** (macroscopic, in-continuum — where the continuum kernel *is* licensed) and (2) a **DISCRETE-LATTICE muonic eigencavity solve** (a named candidate arc, **NOT dispatched** — gated on Grant's two open answers: *which two liquids*, and *barrier-vs-crossover*);
- the repair lane (**PR #639**) showed the **spurious-cluster numbers are window-dependent** — ~17 roots with a spurious more-bound ground ~3.6 keV under the widened window, vs the review's earlier ~14–15 / ~2.58 keV under the old narrow window — **unphysical under either, but quote-with-window** (the exact count is not a physical number).

**(d) Cross-ref — the crystalline-vs-continuum seam.** The two signatures a discrete 386-fm-pitch chiral medium threatens that the Lorentz velocity-theorem does NOT protect — **preferred-axis anisotropy** and **energy-dependent dispersion** — are exactly the seam this walk lives on (`manuscript/ave-kb/common/the-abandoned-interior.md:183`; the leaf also pins `ℓ_node ≈ 386 fm`, the reduced Compton identity that makes `a_μ/ℓ_node = 0.737`).

## §3 THE π-REGISTER AUDIT — is `4π³+π²+π` using π in one consistent register?

_(section content lands next commit)_

---

*Standing caveat (applies to all three walks): every claim above is FRAMING. Nothing here upgrades any observable, mints any def-node, or is cited as evidence FOR AVE; the gate is the thing, the walk only points at it. Cross-refs: the impedance-register + R-B fossil-walk framing notes (2026-07-10), the rulings docket, and the orchestration board (`_orchestration/2026-07-10_orchestration-board.md`).*
