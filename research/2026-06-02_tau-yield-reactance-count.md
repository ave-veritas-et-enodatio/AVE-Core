# Does τ_yield *scale with* the dual-reactance count? — substrate walk to the crux

**Date:** 2026-06-02
**Branch:** `analysis/tau-yield-reactance-count` (off `main` @ `ac5ed5f4`)
**Type:** Substrate-physics derivation — provenance-upgrade + unification candidate
**Discipline:** `ave-prereg`, `ave-ee-first-mapping`, `substrate-native-check`, `consistency-vs-emergence`, `pre-test-physics-check` Trigger 7, `verify-before-cite`
**Prereg:** [`2026-06-02_tau-yield-reactance-count-prereg.md`](2026-06-02_tau-yield-reactance-count-prereg.md)
**Status:** **CRUX SURFACED — AWAITING GRANT.** No verdict, no propagation, no matrix change until the plumber-physical call in §5 is made.

> **One-line:** Three independent substrate-level arguments — the corpus's own master equation, the bond-LC conjugacy, and the local-clock freeze — all point the same way: the τ_yield event is **single-sector** (capacitive breakdown, μ intact), so the clean "×2 = E_C + E_L at breakdown" does **not** fall out as forced. But whether the vacuum "yields" by *breaking down a pre-existing node-tank* (→ inherited) or *nucleating a new two-sector defect* (→ could force 2) is a **framing choice that is Grant's to make**, and the substrate walk lays out both. The repeated negatives are the `pre-test-physics-check` Trigger-7 signal to surface a reframe, not to declare "negative."

---

## §1 — What the "2" actually multiplies (EE first-principles + the non-circularity problem)

The compact numerator `e²/(8πε₀ℓ⁴)` is, exactly (using `α = e²/(4πε₀ℏc)`, `ℓ_node = ℏ/(m_e c)`):

```
e²/(8πε₀ℓ_node)      = ½·α·m_e c²                 ← the Coulomb electrostatic SELF-ENERGY
e²/(8πε₀ℓ_node⁴)     = ½·α·(m_e c²/ℓ_node³)        ← per-sector energy DENSITY (α-suppressed)
τ_yield = 2·[above]  = α·(m_e c²/ℓ_node³) ≈ 1.04×10²² Pa   ✓
```

So the candidate's "per-sector energy density" is the **α¹ Coulomb self-energy density**, and the 2 takes "half the α-scaled rest-energy density" up to "the full α-scaled rest-energy density." Structurally this *is* an equipartition-doubling shape — which is why the candidate is plausible.

**Non-circularity guard — currently UNMET.** `e²/(8πε₀ℓ⁴)` is not derived anywhere in the corpus independently of τ_yield; it appears only *as* the τ_yield numerator (corpus-grep negative). To produce it from first principles as `½Q²/C` requires the **isolated-sphere self-capacitance** `C = 4πε₀ℓ` (which gives `½e²/(4πε₀ℓ) = e²/(8πε₀ℓ)`). But the canonical AVE node capacitance is `C_cell = ε₀·ℓ_node` (`tau-relax-derivation.md:34`, grep) — differing from `4πε₀ℓ` by **4π**, and the canonical node self-energy is the **ropelength** form `U = T_EM·ℓ_node = m_e c²` (`electron-unknot.md:43`), which *deliberately replaces* the `e²/(8πε₀r)` Coulomb integral to avoid the divergence. So the per-sector density is **reverse-engineered to match the 8π**, not yet independently grounded. This gap stands regardless of the yield-event-class verdict.

## §2 — The substrate walk: three reinforcing arguments that the yield is single-sector

### §2.1 — The corpus's own master equation: dielectric yield is the ε-only branch

`master-equation.md:77-81` (verified verbatim) splits the saturation regime into **two branches of the same kernel `S(A)`**, differing in *which constitutive parameter saturates first*:

- **`:78` — Asymmetric (electric-only):** *"only ε_eff → 0 while μ_eff remains intact ... `Z = √(μ₀/ε_eff) → ∞` ... **the dielectric-rupture branch (electric breakdown).**"* ← **this is the τ_yield event.**
- **`:79` (clm-lv3uw1) — Magnetic branch:** *"B saturates μ_eff first ... `Z → 0` ... `Γ → −1` (short-circuit) ... a stabilised topological knot (a Fermion) ... rest mass."* ← particle confinement.

The corpus thus states the dielectric yield is **ε-only**: the capacitive sector saturates, the inductive sector (`μ`) is **explicitly intact**. The two reactance sectors do not co-saturate within *one* event — they are the **two separate branches**. By the corpus's own classification, the energy density delivered at the dielectric-yield threshold is a **one-sector** quantity.

### §2.2 — Bond-LC conjugacy: `V_inc ↔ Φ_link` trade off in time (peak ≠ average)

`substrate-native-check` Ckpt 6: the C-state (capacitive, `V_inc`) and L-state (inductive, `Φ_link`) of the bond LC are **conjugate — they trade off in time**. In an oscillating tank they are 90° out of phase: when `V_inc` peaks (the capacitive amplitude that reaches `A_yield` and triggers rupture), `Φ_link` is at its **trough (empty)**. So at the rupture *instant*, the energy is concentrated in the saturating sector; `E_total = E_C(peak)`, not `E_C + E_L`. The equipartition `E_C = E_L = E_total/2` is a **time-average**; the yield is a **peak/threshold** event. Time-averaged 50/50 ≠ both-sectors-at-peak-simultaneously.

### §2.3 — Local-clock freeze: the oscillation stops exactly at the yield point

`substrate-native-check` Ckpt 5 (A-010 local-clock corollary): `ω_local(r) = ω_global·√(1−A²)`. At the rupture boundary `A²→1`, **`ω_local → 0` — the local clock freezes.** The resonant-tank CLOSE argument *requires ongoing oscillation* to invoke time-averaged equipartition; but at `A_yield` the oscillation has frozen, so the energy is locked in whichever sector was at peak when it froze. The equipartition argument breaks down **exactly where the CLOSE outcome needs it to hold.**

### §2.4 — The α-order category error

The corpus equipartition is the **virial** result for a *stable soliton at rest*: `E_C = E_L = ½m_e c²` (`relativistic-inductor-newtonian-limit.md:22-24`; `resonant-lc-solitons.md:17-19`), an **α⁰** decomposition (total energies summing to `m_e c²`). The τ_yield per-sector is the **α¹** Coulomb self-energy `½α·m_e c²` (§1). These are **different energies** (off by `1/α ≈ 137`). Invoking the virial 50/50 to license doubling the *Coulomb* self-energy conflates two distinct decompositions — the canonical "three distinct 2's must NOT be fused" discipline (`dual-reactance-storage-taxonomy.md:42-60`) applies precisely here: the candidate would convert the equipartition "coincidence-2" into a load-bearing identity across an α-order gap.

**EE means-test (`ave-ee-first-mapping`):** the canonical EE analog of the Axiom-4 kernel is the **varactor C-vs-V near dielectric breakdown** (means-test #11, ✓). In EE, dielectric breakdown is a **capacitor event** — the dielectric fails when the field exceeds its strength; the **inductor is not involved**. This independently reproduces §2.1 (single-sector capacitive). PASS for "single-sector," not for "resonant-tank ×2."

## §3 — The steelman for CLOSE (and where it still has a gap)

The fairest pro-CLOSE reading is **nucleation, not breakdown**: τ_yield is not the breakdown of one pre-existing oscillating tank, but the **energy density to nucleate a new node-defect** (the Γ=−1 boundary = a new mini-soliton). A stable topological defect is *intrinsically two-sector* — it cannot exist with only a charge sector and no flux sector — so creating it costs `E_C + E_L`, and the 2 = the two sectors the defect must populate. This is genuinely different physics from §2 (a co-requirement, not a first-to-saturate threshold), and it would make the 2 **forced**.

**Remaining gaps even under nucleation:**
1. The "per-sector" being doubled is still the **α¹ Coulomb self-energy**, not the **α⁰ virial half-rest-mass** — so the relevant claim is "the nascent defect's *inductive* self-energy density equals its *capacitive Coulomb* self-energy density," which needs its own derivation (it is **not** the virial result).
2. The non-circularity 4π gap (§1) is independent of picture.

So even the steelman does not deliver a *clean, derived* ×2 on current corpus content — it relocates the burden to "magnetic self-energy = electric self-energy for a nascent defect," which is underived.

## §4 — The reframe that the negatives point to

`pre-test-physics-check` Trigger 7: 3+ reinforcing negatives signal a wrong *framing*, not a settled "negative." The reframe the substrate keeps offering:

> The dual-reactance **count of 2 is real and canonical** (X_C + X_L, mass-confirmed) — but at the *yield* level it manifests as the **two branches of the master equation**, not as a summed energy inside one event. **Electric breakdown** (`τ_yield`, ε-only) and **magnetic confinement** (mass/Fermion, μ-only) are the **two single-sector saturation thresholds** of the same two-sector node. `τ_yield` is the threshold of **one** branch; its `2` is the **inherited count-tag** from `𝒱_total`, not a within-event sum.

Under this reframe the honest answer to the literal question ("does the yield *stress* = E_C + E_L?") is **STAYS-INHERITED**, while the genuine cross-scale unification is the **dual-branch / dual-threshold** structure (same X_C, X_L as baryon `V=2`) — a real result, but a *different* claim than "the yield stress scales with the count."

## §5 — The crux (plumber-physical question for Grant)

Everything above is substrate-walk; **this one call is yours.** When the vacuum "yields" at `τ_yield`, which event is it physically?

- **(A) First-sector breakdown of a pre-existing node-tank** — the corpus's current picture (`master-equation.md:78`, ε-only; varactor breakdown). The capacitive sector hits `A_yield`; the inductive sector (`μ`) is a spectator. Energy at rupture = **one** sector's worth. → the 2 is a **count-tag**, **STAYS-INHERITED** (with the §4 dual-branch reframe as the real unification).
- **(B) Nucleation of a new two-sector defect** — the Γ=−1 boundary is a *new* mini-soliton that must populate **both** `E_C` and `E_L` to exist. → the 2 = the two sectors it must fill, **forced** → **CLOSE** (pending the §3.1 "magnetic self-energy = electric self-energy" sub-derivation + the §1 4π reconciliation).

The substrate physics that *would* decide it on its own keeps landing on (A): at `A→A_yield` the local clock freezes (§2.3) and the C/L states are conjugate (§2.2), so a single oscillating tank has its energy in one sector at the rupture instant. (B) requires the yield to be a two-sector **co-requirement** (a creation event), which is a different physical claim than a tank's first-sector breakdown.

**One sentence from you collapses it:** *Is `τ_yield` the field at which an existing patch of vacuum tears (one sector lets go first) — or the energy density it costs to mint a brand-new defect (which has to carry both charge and flux to be a thing)?*

## §6 — Classification + verdict status

- **consistency-vs-emergence:** Trigger-8 classification-promotion question. Canonical ceiling = *"a re-interpretation, not a derivation"* (`dual-reactance-storage-taxonomy.md:165`). CLOSE is earned **only** if (B) is the physical call **and** the §3.1 sub-derivation closes the α-order gap; otherwise classification stays at the inherited ceiling. Observable axis = Class 4 consistency / provenance (no empirically-variable sector count) — **not** a new prediction, per brief scope.
- **Verdict:** **HELD — awaiting Grant's §5 call.** On current evidence the substrate points to **STAYS-INHERITED + §4 dual-branch reframe**; the CLOSE path is live only under reading (B) with two named sub-derivations outstanding. No τ_yield-site edits, no matrix change, no open-item closure until Grant adjudicates.
