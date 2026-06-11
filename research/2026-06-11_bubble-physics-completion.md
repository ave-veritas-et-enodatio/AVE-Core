# Bubble-physics completion — σ-from-ℓ_c, the forward-first Minnaert check, and the death-channel design note

**Date:** 2026-06-11
**Branch:** `analysis/2026-06-11-bubble-physics` (worktree off `analysis/2026-06-10-genesis-v6-transducer` @ `7484dd0b`; not pushed/merged)
**Check script:** `src/scripts/vol_1_foundations/bubble_physics_completion_check.py` (every number below is printed by it; forward-first ordering is git-provable in the file)
**Governing discipline (HARD stack):** pure-AVE-corpus · canonical-AVE-only · verify-before-cite · ave-canonical-source · **ave-live-fire-derivation-provenance** (the Minnaert forward is computed + stated BEFORE the comparison — Rule 11, no retrofitting) · consistency-vs-emergence · coincidence-magnet discipline · substrate-native-check · flag-don't-fix.

**Class tags (stated up front):**
- **σ-from-ℓ_c** — DERIVED-THIS-ARC, **CANDIDATE** (gradient-energy *scaling*, O(1) prefactor; not a coexistence surface tension).
- **Minnaert check** — FORWARD CONSISTENCY-CLASS check. The functional form is standard textbook bubble-acoustics, used as the consistency lens; the substrate-adapted version is derived from the canonical `c_bulk`/EOS, not imported blind.
- **Death channel** — DESIGN NOTE / HYPOTHESIS. Explicitly NOT implemented here; feeds the annihilation arc's follow-up (own prereg, Rule 12).

---

## 0. INPUTS — verified, each with provenance (verify-before-cite)

Engine-native units throughout: `c0 = 1` (bulk P-wave / dilatation speed = velocity unit), `ρ0 = 1` (ambient density), `ℓ_node = 1` (length unit), `dx = 1 cell`. All results are **dimensionless engine-native** quantities; the comparison (a frequency ratio) is unit-free.

| input | value | provenance (file:line, grep-verified this session) |
|---|---|---|
| ℓ_c (Cosserat coupling length) | √6·ℓ_node ≈ 2.4495 | `src/ave/core/constants.py:255` `ELL_C = √6·L_NODE` |
| cavitation floor ρ̄_cav | −1/φ ≈ −0.618034 | `src/ave/core/cavitation_flow.py:64` `RHO_CAV = −1/PHI` |
| cavitation EOS | c_bulk²(ρ̄)=c0²(1+ρ̄/(1−ρ̄²)) | `src/ave/core/cavitation_flow.py:21-28, 153-157` |
| EOS softening slope at floor | d(c²)/dρ̄\|_cav = 2+φ ≈ 3.618 | `04_superluminal_transit.tex:86`; reproduced analytically by the script |
| K = 2G canon (ν=2/7 ⇒ c_L²/c_T²=10/3) | K = 0.6 ρ0c0²; M = 1.0 ρ0c0² | `src/ave/core/crystal_engine.py:95-96` |
| measured ring-down f₀ | w_est = 0.324462 rad/time ⇒ f₀ = 0.05164 cyc/time | `src/scripts/vol_9_device/_output/electron_s11_results.json` `unknown.w_est_ringdown` (PR #166, main) |
| f₀ measurement config | N=40, S_min=0.0125, A_cap=0.999, **planted (2,3) R=10.4, r=4.0 cells**, V-sector drive | `research/2026-06-10_electron-s11-sweep_result.md §2`; driver `electron_s11_sweep.py:277,287-288` |
| V-breather seed | Gaussian `seed_bulk(σ=3.5, frac=0.9)` (the trapped mass) | `electron_s11_sweep.py:287` |
| snapped-pocket geometry | genesis-v6 3D pocket 1704–5256 cells (N=48) → r≈7.4–10.8 cells; sonic-horizon 2D 1280 cells (N=160) → r≈20 cells | `research/2026-06-10_genesis-v6-self-limiting-snap_result.md §1`; `…_sonic-horizon-closure_result.md §2` |
| rim over-pressure (PE reservoir) | ρ̄>0 rim; LOCK recovers ρ̄_core→≈−0.08 | `…_sonic-horizon-closure_result.md §0,§2,§6` |

**⚠ LOAD-BEARING DISAMBIGUATION (flag-don't-fix) — two pockets, two EOS branches.** The measured f₀ is the **STIFFENING** saturated-core V-dilatation breather (`CrystalGraftV4`, c_eff²=c0²/√(1−A²)→∞, self-creating a Γ=−1 wall; `crystal_engine.py:197-200`, `crystal_graft_v2.py:16-18`). The "bubble"/snapped pocket in the Minnaert/σ picture is the **SOFTENING** cavitation void (`CavitationFlow2D`, c_bulk²→0 at ρ̄_cav). `cavitation_flow.py:28` **explicitly firewalls these**: the cavitation pocket is "a FOURTH object — NOT Rayleigh-Plesset, NOT photon bubble, **NOT Γ=−1**." This doc treats both under one "bubble" lens to TEST whether they share a song; the firewall means a tight match would be a *claim*, not a given. **Surfaced for Grant — see §4 the plumber-physical question.**

---

## 1. σ FROM ℓ_c — the snapped shell's interface energy per area  *(DERIVED-THIS-ARC, CANDIDATE)*

### 1.1 The energy functional (substrate-native, CP2 BULK-K sector)
The bulk-density sector carries, beyond the homogeneous EOS energy `f0(ρ̄)`, a **gradient (Korteweg / couple-stress) term** — the continuum shadow of the K4 micropolar lattice's finite coupling length. The free-energy density of a non-uniform density field is

```
f(ρ̄, ∇ρ̄) = f0(ρ̄) + ½ · λ_grad · |∇ρ̄|²
```

Dimensional closure fixes `λ_grad`: the gradient term must carry the bulk-energy scale `K` (energy/volume) over the couple-stress length `ℓ_c` (the length at which gradient stiffness balances bulk stiffness). Hence

```
λ_grad = K · ℓ_c²          (the couple-stress length sets the interface width to ℓ_c)
```

This is the substrate identification: **ℓ_c = √6·ℓ_node is the diffuse-interface width** of any bulk-density step, because it is the K4/Cosserat length at which `λ_grad|∇ρ̄|²` (gradient) equals `K(Δρ̄)²` (bulk) for `|∇ρ̄| ~ Δρ̄/ℓ_c`.

### 1.2 The interface energy per area (square-gradient integral)
For a diffuse interface of width ℓ_c between the pocket interior (ρ̄ = ρ̄_cav) and ambient (ρ̄ = 0), with a tanh profile `ρ̄(x) = (Δρ̄/2)·tanh(x/ℓ_c)`, the square-gradient (Cahn-Hilliard) surface tension integrates to

```
σ  =  ∫ [Δf0 + ½ λ_grad (dρ̄/dx)²] dx  =  c_σ · K · ℓ_c · (Δρ̄)²
```

with `c_σ = 1/3` for the tanh profile by gradient/bulk equipartition (the prefactor is **O(1), profile-dependent** — this is the candidate-class caveat). The structural form `σ ~ K·ℓ_c·(Δρ̄)²` is exactly the task-stated couple-stress/Korteweg class.

### 1.3 The value (engine-native units)
With `Δρ̄ = 1/φ` (the jump from ρ̄_cav to ambient), `(Δρ̄)² = 1/φ² = 2−φ = 0.38197`, `ℓ_c = √6`:

| modulus | σ = (1/3)·K·ℓ_c·(Δρ̄)² | engine units |
|---|---|---|
| **K = 2G (canon)** | (1/3)·0.600·2.4495·0.38197 = **0.187** | ρ0c0²·ℓ_node |
| M = P-wave | (1/3)·1.000·2.4495·0.38197 = **0.312** | ρ0c0²·ℓ_node |

Headline (canonical bulk modulus): **σ ≈ 0.19 engine E/area** (range 0.19–0.31 over the modulus choice).

### 1.4 Laplace pressure, and: does surface tension MATTER at pocket scale?
3D Laplace over-pressure `ΔP = 2σ/r_pocket` (σ = 0.187, K=2G):

| pocket radius (cells) | ΔP_Laplace | % of K=2G |
|---|---|---|
| 4.0 ((2,3) tube r23) | 0.094 | 15.6% |
| 5.0 (breather core) | 0.075 | 12.5% |
| 7.4 (genesis-3D 1704c) | 0.051 | 8.4% |
| 10.8 (genesis-3D 5256c) | 0.035 | 5.8% |
| 20 (sonic-2D 1280c) | 0.019 | 3.1% |

The **rim over-pressure** (the PE reservoir that the sonic-horizon work found drives the LOCK refill; `…sonic-horizon-closure_result.md §6`) is order `|ρ̄_rim|·c0² ~ 0.05–0.10` (the LOCK recovers ρ̄_core→≈−0.08).

**VERDICT — surface tension MATTERS.** `ΔP_Laplace ~ 0.04–0.09` is the **same order** as the rim over-pressure. So σ is a **co-equal contributor to the restoring/collapse pressure**, not a negligible correction: it reinforces the reversible-spring LOCK (it pushes the void closed alongside the rim PE). **Coalescence implication:** for two touching shells, total interface area falls on merging, so `ΔE ~ −σ·ΔA < 0` — coalescence is energetically **favorable**, driven by exactly this σ. This is the bridge to the death channel (§3): two electron-pockets in contact want to merge, and the merge is surface-tension-driven.

**Coincidence-magnet check (§1):** `ℓ_c·(Δρ̄)² = √6/φ² = 0.9356` is a clean golden/√6 number, but σ's headline value rides on the O(1) `c_σ=1/3` AND on K vs M — so the value is candidate-class, not a pinned prediction. No golden-ratio "identity" is claimed for σ. The honest content is the *scaling form* and the *order-of-magnitude* (σ matters, surface tension is not negligible).

**Honest ceiling (the candidate caveat).** The strict Cahn-Hilliard σ presumes a **double-well** `f0` with two coexisting minima. The canonical cavitation EOS is NOT a coexistence double-well — the pocket is a *dynamical tensile-failure* state (`cavitation_flow.py:28`), not a thermodynamic phase. So §1 is a **gradient-energy scaling** (λ_grad = K·ℓ_c² is sound; the σ integral uses an assumed tanh profile), NOT a rigorous coexistence surface tension. Tagged CANDIDATE accordingly.

---

## 2. THE MINNAERT CHECK — forward-first (Rule 11)

### 2.1 The substrate Minnaert form (derived, stated BEFORE any comparison)
Standard Minnaert: a spherical bubble of radius `a` breathes; the restoring spring is the compressional stiffness `K_eff`, the inertia is the surrounding-medium density `ρ_eff`, and the spherical geometry (δV/V = 3 δR/R) supplies the factor 3:

```
ω₀ = (1/a)·√(3 K_eff / ρ_eff) = √3 · c_eff / a ,   with K_eff/ρ_eff ≡ c_bulk²
f₀ = √(3 K / ρ0) / (2π a)
```

The surrounding-medium linear speed is `c_bulk(ρ̄=0) = c0 = 1` in **both** EOS branches (the softening and stiffening EOS agree at ambient ρ̄=0), so the inertia loading is `c0`-set regardless of branch.

**The boundary-condition question (task-flagged): the snapped shell is a REFLECTOR, not a free surface — does that change the mode form?** Partially. The Γ=−1 shell is an **impedance collapse** `Z_bulk = ρ·c → 0` (`…sonic-horizon-closure_result.md §7`), which is a **pressure-release** boundary (`p = 0` at the wall) — the **SAME** boundary condition as a free gas-liquid surface. So the √3 Minnaert prefactor (global sub-wavelength pulsation against the external inertia) carries over. What the reflector *does* change is **radiation vs confinement**: a free bubble radiates into an infinite liquid (Minnaert, ω=√3 c/a); a Γ=−1 reflector *confines* the mode, whose lowest pressure-release standing wave is `ω = π c/a` (a factor `π/√3 ≈ 1.81` higher). The two forms bracket the physics; which one the trapped breather realizes is a *measured-mode-shape* question (named as the missing input in §2.4).

### 2.2 The forward number (COMPUTED — no access to the measured f₀)
Pre-committed radius (stated before computing, no retrofit): the f₀ was measured on a V-breather seeded as a Gaussian `seed_bulk(σ=3.5)` (`electron_s11_sweep.py:287`). The principled "bubble radius" of a Gaussian field is the **field 1/e radius `a = σ√2 = 4.95 cells`**. The two natural compression moduli `{M = P-wave = 1.0, K = 2G = 0.6}` bracket the spring stiffness.

**FORWARD (printed by the script Section C, before Section D loads the measured):**

```
a = σ√2 = 4.95 :  f₀_fwd[K=2G] = 0.04314 cyc/time
                  f₀_fwd[M    ] = 0.05569 cyc/time
⇒ FORWARD BAND  f₀_fwd ∈ [0.04314, 0.05569] cyc/time
```

Radius sensitivity (honesty, also forward): a=σ → [0.061, 0.079]; a=2σ → [0.031, 0.039]; a=r23=4.0 → [0.053, 0.069]; a=R23=10.4 → [0.021, 0.027].

### 2.3 THE COMPARISON (measured loaded only now)
Measured: `f₀ = w_est/2π = 0.05164 cyc/time` (`electron_s11_results.json`). **CAVEAT (load-bearing):** the bulk channel is **MULTI-MODE / low-contrast** (`…electron-s11-sweep_result.md §0,§2`) — f₀ is the dominant ring-down peak, NOT a clean single high-Q resonance (there is a subharmonic at f₀/2).

```
forward band (a=σ√2):  [0.04314, 0.05569]      measured 0.05164  → INSIDE the band
  f₀_fwd[M=P-wave]/f₀_meas = 0.05569/0.05164 = 1.078   (residual +7.8%)
  f₀_fwd[K=2G    ]/f₀_meas = 0.04314/0.05164 = 0.835   (residual −16.5%)
```

### 2.4 THE BIN — **UNDERDETERMINED** (leaning CONSISTENT)

The measured f₀ sits **INSIDE** the forward Minnaert band at the principled radius → the bubble-breathing identity is **NOT refuted**. But it is **NOT a tight MATCH**, for four honest reasons:
1. **Modulus**: the spring is K=2G *or* M=P-wave — ±15% on f₀.
2. **Radius**: σ vs σ√2 vs 2σ — a factor ~2 on f₀ (the forward band spans 0.031–0.079 across these).
3. **Boundary form**: free-surface √3 vs confined-cavity π — ×1.81.
4. **The measured spectrum is itself multi-mode** — there is no single clean Q to match.

Multiple `(radius, modulus)` combos land near 0.052 (e.g. a=r23=4.0 with K=2G → 0.0534; a=σ√2 with M → 0.0557) — a textbook **coincidence-magnet** tell. The agreement is real at the *order/prefactor-class* level but **over-determined** for a "MATCHES" headline.

**MATCHES would mean:** a forward number inside a *tight* (say ±10%) tolerance with the geometry pinned independently — *the bubble identity's first quantitative confirmation*. We do not have that.
**DIFFERENT would mean:** a clean integer/√ mismatch (e.g. f_fwd/f_meas = π/√3, or 2, or √(10/3)). We do not have that either.
**UNDERDETERMINED (this result):** consistent at the factor level; **the missing geometric input** to promote is (a) the **measured mode-shape** (eigenvector spatial extent → the effective `a`, and whether the pressure node sits at σ, σ√2, r23, or R23), (b) a **single-mode high-Q** ring-down (the current spectrum is multi-mode), and (c) which **boundary form factor** (√3 vs π) the confined breather realizes.

**So what is the song?** At the principled radius the breather rings at `f ≈ √3·c0/(2π·σ√2)` — i.e. **the sub-wavelength Minnaert pitch of a c0-stiffness bubble the size of the saturated core** — to within the (wide) geometric ambiguity. The data are *consistent* with the electron-as-breathing-bubble picture but do not yet *confirm* it quantitatively; the firewall disambiguation (§0) means even a future tight match must reconcile the stiffening-breather (measured) vs softening-cavitation (Minnaert) branch identity.

---

## 3. THE DEATH-CHANNEL NOTE — un-storing as propagating longitudinal V-waves  *(DESIGN NOTE / HYPOTHESIS — NOT implemented here)*

**The mirror of the birth pulse.** Genesis stores a mass by a **birth flash**: the snap fires, the latent longitudinal energy is released as a burst, and the residual is locked as a standing V-breather behind a Γ=−1 wall (`…genesis-v6-transducer_result.md §5`, 561 bursts at 40–70× the F-BURST gate). The death channel is the **time-reverse**: the un-storing of that locked latent as **propagating longitudinal V-waves directly** — the annihilation engine's job. Mirror symmetry: birth = inward snap + lock (Axiom-4 engage); death = boundary release + outward radiation (Axiom-4 relax). No QED Kramers-Heisenberg / Rabi — absorb/emit is Axiom-4 engage/relax of the real longitudinal V-sector (the "3").

**What the annihilation engine minimally needs (CP10-compliant — a BOUNDARY release, not a bulk term):**
1. **A boundary release at shell contact.** The Γ=−1 wall is a perfect reflector that *holds* the breather (the LOCK). Un-storing requires *opening* the wall — a boundary operation at the shell `g_wall(r)` (the same CP10 thin-shell locus the buckle uses, `crystal_graft_v2.py:123-137`), not a bulk-volume sink. When two shells touch, the contact patch is where the two Γ=−1 reflectors meet; releasing there converts the held standing V into an outgoing longitudinal V-wave on *both* sides — the mirror of the inward birth snap.
2. **The surface-tension-driven collapse as the trigger (the §1 bridge).** §1.4 shows coalescence of two touching shells is energetically favorable (`ΔE ~ −σ·ΔA`, σ ≈ 0.19, Laplace ΔP same order as the rim over-pressure). So the **trigger is not an imposed coupling — it is the σ-driven merge**: two pockets in contact coalesce, the shared wall is annihilated (area→0), and the previously-confined latent un-stores as a longitudinal burst. The death pulse is **surface-tension-gated**, exactly as the birth pulse is snap-gated.
3. **The V-sector longitudinal un-storing channel.** The released energy must couple OUT as the longitudinal/scalar V-wave (the Heaviside-set-aside scalar grade, physical — NOT Gauss-deleted), propagating at the bulk speed (c_bulk, the K-sector clock), as the *direct* radiation mode. This is the mirror of the birth flash's longitudinal burst (D6 detector, `…genesis-v6-transducer_result.md §5`); the same `seed_bulk`/breather sector, run in release rather than capture.

**CP10-compliant coupling shape (the design constraint):** the release operator must be a **post-substep boundary op localized to the contact shell** (Gaussian `g_wall` at the merged interface), passive (`E_radiated ≥ 0`, energy leaves — the time-reverse of the lock's one-way sink), and triggered by the σ-coalescence geometry (shell contact), NOT a free-running bulk EOM term. This mirrors the transducer's verified CP10 boundary-locality (`…genesis-v6-transducer_result.md §2`, "Gaussian shell in A, post-substep boundary op, no bulk EOM term").

**Explicitly NOT implemented.** No engine term is added here. This is a design note for the annihilation arc; it needs its **own frozen prereg + verification chain** (Rule 12 — a new hypothesis with its own version, not a refill of any closed slot). Open discriminator for that prereg: does the un-stored pulse carry the **mirror handedness** of the birth pulse (matter/antimatter sign via `n̂_χ`, `crystal_graft_v2.py:37`), and does the released energy equal the stored latent (the birth-pulse mirror, energy-balanced)?

---

## 4. FLAGS + the plumber-physical question (flag-don't-fix; auditor lands manual entries)

1. **THE LOAD-BEARING PHYSICS QUESTION FOR GRANT (pre-test-physics-check):** the measured f₀ is the **stiffening** saturated-core V-breather; the Minnaert/σ "bubble" is the **softening** cavitation void, which `cavitation_flow.py:28` firewalls as "a FOURTH object — NOT Γ=−1". **Are these the same bubble (so the Minnaert consistency is meaningful), or two different objects whose breathing pitches merely land in the same band?** The whole quantitative weight of the "bubble identity" rests on this. Surfaced, NOT silently resolved.
2. **σ is a gradient-energy SCALING, not a coexistence surface tension** (§1 honest ceiling): λ_grad = K·ℓ_c² is sound; the σ integral assumes a tanh profile across a non-double-well EOS. CANDIDATE-class; O(1) prefactor.
3. **The Minnaert bin is UNDERDETERMINED by construction** (§2.4): the measured spectrum is multi-mode (no single Q), and the forward spans a factor ~2 over the radius/modulus/boundary ambiguity. The "INSIDE the band" result is consistent, not confirmatory. Do not headline it as the bubble identity's confirmation.
4. **ρ̄_cav remains CANDIDATE-CLAIM** (zero KB/constants hits beyond `cavitation_flow.py`; consistent with `…sonic-horizon-closure_result.md §8 #5`). This doc does not promote it.

**Corpus-state deltas to QUEUE (auditor lands; implementer surfaces only):**
- NEW derivation (candidate): σ = (1/3)K·ℓ_c·(Δρ̄)² ≈ 0.19 engine E/area, with the couple-stress length as the interface width; Laplace ΔP same order as the rim over-pressure ⇒ surface tension is co-equal at pocket scale; coalescence favorable.
- NEW forward check: substrate Minnaert f₀_fwd ∈ [0.043, 0.056] (a=σ√2) brackets the measured 0.0516 — UNDERDETERMINED/consistent; not a confirmation.
- NEW design note: the death channel = σ-coalescence-triggered CP10 boundary release of the locked latent as outgoing longitudinal V-waves (birth-pulse mirror); feeds the annihilation arc (own prereg).

---

## 5. DERIVED / VERIFIED / BLOCKED (honest split)
**DERIVED (this arc, candidate):** σ ~ K·ℓ_c·(Δρ̄)² from the couple-stress gradient energy; the Laplace-vs-rim comparison.
**VERIFIED (engine-native, reproducible by the script):** ℓ_c=√6, Δρ̄=1/φ, EOS slope 2+φ; the Minnaert forward band; the measured f₀=0.05164 sits inside it.
**BLOCKED / out of scope:** absolute SI units (engine-native throughout); the stiffening-vs-softening bubble-identity reconciliation (§4 flag 1, needs Grant); a single-mode high-Q ring-down + measured mode-shape (would promote the Minnaert bin); the death-channel engine implementation (own prereg, Rule 12).
