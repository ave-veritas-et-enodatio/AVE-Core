# Substrate Temporal Values — careful definitions + reconciliation (DRAFT)

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-saturation-temporal-preregs` (off `main` @ f1f927c8)
**Status:** DRAFT definition doc (Grant directive 2026-06-09: *"the voxels of the lattice are what freeze, they are our gears… define these temporal values carefully and document"*). Asserts the solid parts; **one assignment flagged OPEN for Grant** (§5). Feeds: the Vol-9 datasheet temporal section + a KB-leaf reconciliation of three contradicting leaves (§4, PR-gated).

> **Why this doc exists.** Three canonical leaves state the clock-vs-strain exponent *three different ways* (§4) — a live coherence contradiction surfaced by the time-dilation prereg corpus-grep. Grant's gear/voxel picture cuts through it: there is not ONE clock; there are SECTOR clocks, and the "contradiction" is leaves describing different sectors without labels. To avoid the root cause (an overloaded symbol `S`), **everything here is written in the physical strain `A` directly.** Canonical kernel: `S(A) ≡ √(1−A²)` (datasheet ch.01, constants.py) — but `S` is used inconsistently elsewhere, so we avoid it in the definitions.

---

## 1. The clock quantum — the voxel IS the gear tooth

The K4-TLM lattice computes by scatter+connect, one cell at a time ("the lattice IS the computation"). The irreducible tick is **one signal-crossing of one voxel**:

$$\tau_0 = \ell_{\text{node}}/c_0 \approx 1.288\times10^{-21}\ \text{s}, \qquad \ell_{\text{node}} \approx 0.386\ \text{pm}$$

Two facts make this exactly Grant's "minimum latch/gear/tooth":
- `ℓ_node` is the **electron reduced Compton wavelength** (ℏ/m_e c = 0.386 pm), so `τ₀ = ℓ_node/c₀` is the **electron Compton time**. The electron is a ~one-voxel object in real space (its (2,3) winding lives in phase-space, not many cells) — **the electron's Compton clock IS the voxel tick.** The cubic node-cell the electron occupies is literally the minimum tooth.
- `τ₀` is the unstrained value of the canonical relaxation time `τ_relax = ℓ_node/c` (`tau-relax-derivation.md:11`). Same quantity: the cell-crossing time.

**"Freezing" = the gear seizing.** Under load the local crossing speed changes; when it → 0, a signal can no longer cross a cell in finite time → the tooth stops advancing → the clock stops. Freezing is a substrate-mechanical statement about voxel-crossing, not an abstraction.

## 2. Sector speeds (written in A, not the overloaded S)

The substrate carries distinct wave sectors at distinct speeds. Two are canonically fixed; a third is the compressional/density wave:

| sector | speed vs strain A | behavior under load (A↑) | role |
|---|---|---|---|
| **EM (transverse), phase** | `c_EM = c₀·(1−A²)^(−1/2)` | **RISES** (→∞ at A→1) | Maxwell phase velocity; the speed that enters α (clm-8nkvwy, INVARIANT-S2:64) |
| **mechanical (matter/rest-mass)** | `c_shear = c₀·(1−A²)^(+1/4)` | **FREEZES** (→0 at A→1) | group/energy-transport/rest-mass speed; tracks Schwarzschild c√(1−r_s/r) (clm-8nkvwy, INVARIANT-S2:65; Op16 operators.md:56) |
| **compressional (longitudinal density)** | `c_dens = c₀·√(1 + ρ̄/(1−ρ̄²))` | rises for ρ̄>0; → 0 at the cavitation floor **ρ̄_cav = −1/φ** | the rarefaction/superluminal relation (`04_superluminal_transit.tex:86`); a DIFFERENT wave from c_shear |

## 3. The two confirmed times (tick = ℓ_node / c_sector)

| clock | period vs A | rate | verdict under load |
|---|---|---|---|
| **Matter / gravitational clock** (rides c_shear) | `τ_matter = τ₀·(1−A²)^(−1/4)` | `ω_matter = ω₀·(1−A²)^(+1/4) = ω₀√S` | **DILATES** (slows) — gravitational time dilation |
| **EM-phase "clock"** (rides c_EM) | `τ_EM = τ₀·(1−A²)^(+1/2)` | `ω_EM = ω₀·(1−A²)^(−1/2)` | phase advances FASTER (this is the α-speed, not a proper matter clock) |

**The matter clock is the one that means "time dilation"** — a person, a chemical reaction, an atomic clock are mechanical wave-packets; packets move at the group/mechanical speed `c_shear`, which freezes as `(1−A²)^(1/4)`. **This answers the time-dilation prereg's exponent gate: p = ¼ (clock ∝ √S)** — and now with the physical *why*: matter is a packet, packets ride c_shear, c_shear freezes. Not "because INVARIANT-S2 says so."

## 4. Reconciliation of the three contradicting leaves (corpus-coherence; PR-gated walk-back)

| leaf | states | disposition |
|---|---|---|
| `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2:65,71 | gravitational clock = **c_shear ∝ (1−A²)^¼** | **CORRECT** — the matter clock (§3). Highest authority. |
| `op14-local-clock-modulation.md:17,31` | `ω_local = ω₀√(1−A²)` ∝ (1−A²)^**½** | **STALE** — a pre-split single-speed model (`c_eff = c₀√(1−A²)`) from before the c_EM/c_shear split (clm-8nkvwy). Off by a factor of 2 in the exponent. Flag for correction. |
| `04_superluminal_transit.tex:41` (Sleep Pod) | clock = `c = 1/√(με)` = **c_EM** | **MISLABELED** — that's the EM-phase speed, not the matter clock; the exact c_EM/c_shear category error S2 warns against (Pitfall #5). Flag for correction. |

Root cause: (i) the symbol `S` is overloaded (`√(1−A²)` vs `(1−A²)`) across leaves; (ii) "the clock" was stated without naming WHICH sector. Both fixed by §2–§3 (define in A, label the sector). **This reconciliation, applied to the three leaves, is a PR-gated walk-back — not done here.**

## 5. OPEN — flagged for Grant (the heart of "longitudinal vs transverse time")

Canon fixes the EM sector as transverse (light is transverse) and fixes the matter clock as riding `c_shear ∝ (1−A²)^¼`. **But canon never states whether `c_shear` is the transverse-mechanical shear or a longitudinal-torsional mode** (grep returned zero characterization), AND there is a *separate* longitudinal compressional/density speed `c_dens` (the ρ̄ relation, §2). So:

- **Q1 — c_shear's polarization.** Is the matter/rest-mass speed `c_shear = c₀(1−A²)^¼` the **transverse** mechanical shear, or the **longitudinal** torsional shear (the dark-wake sector was explicitly "longitudinal-shear")? In standard elasticity "shear" = transverse, but AVE used "longitudinal-shear" for τ_zx — so the label is ambiguous and the physics is unpinned.
- **Q2 — is there a distinct longitudinal time?** The compressional `c_dens` (ρ̄ relation) is a genuinely different wave from `c_shear`. Does it carry its OWN clock (a "longitudinal/compressional time") distinct from the matter clock? If so, "longitudinal vs transverse time" is THREE times, not two: EM-transverse (c_EM), shear (c_shear), compressional-longitudinal (c_dens).

**Plumber question for Grant:** when matter's clock freezes, is the freezing mode the *transverse* mechanical oscillation of the node, or a *longitudinal* (torsional / compressional) one — and is the compressional density wave a separate time we should track? Your call pins the §2 polarization labels and decides whether the temporal taxonomy is 2-time or 3-time. Until then §2's "transverse/longitudinal" tags on the mechanical rows are PROVISIONAL.

## 6. Deliverable targets (once §5 is called)

- **Vol-9 datasheet** (the figure-build): a "temporal characteristics" set — the speed curves (§2) and the clock curves (§3) vs A on one panel, dilating matter clock vs rising EM phase, with τ₀ = Compton tick as the baseline. Pairs with the ρ̄_cav rarefaction-floor figure already registered.
- **KB-leaf reconciliation** (§4) — the canonical temporal-values definition + the three-leaf walk-back. PR-gated, Core main.
- **Feeds** the time-dilation prereg (p=¼ confirmed for the matter clock, §3).
