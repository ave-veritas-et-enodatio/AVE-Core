# Substrate Temporal Values — careful definitions + reconciliation (DRAFT)

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-saturation-temporal-preregs` (off `main` @ f1f927c8)
**Status:** DRAFT definition doc (Grant directive 2026-06-09: *"the voxels of the lattice are what freeze, they are our gears… define these temporal values carefully and document"*). The §5 mode-assignment is **RESOLVED by Grant 2026-06-09: shear vs bulk, each with a saturation & desaturation time** (the two locked K=2G mechanical moduli + the EM phase). One residual physics question (limit-asymmetry → time-asymmetry) routes to the thixotropy prereg. Feeds: the Vol-9 datasheet temporal section + a KB-leaf reconciliation of three contradicting leaves (§4, PR-gated).

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

| sector | speed vs strain | behavior under load | role |
|---|---|---|---|
| **EM (transverse), phase** | `c_EM = c₀·(1−A²)^(−1/2)` | **RISES** (→∞ at A→1) | Maxwell phase velocity; the speed that enters α (clm-8nkvwy, INVARIANT-S2:64). Electromagnetic, NOT one of the two mechanical modes below. |
| **SHEAR — mechanical deviatoric (modulus G=μ)** | `c_shear = c₀·(1−A²)^(+1/4)` | **FREEZES** (→0 at A→1) | group/energy-transport/rest-mass speed; the **matter clock**; tracks Schwarzschild c√(1−r_s/r) (clm-8nkvwy, INVARIANT-S2:65; Op16 operators.md:56) |
| **BULK — mechanical volumetric (modulus K)** | `c_bulk = c₀·√(1 + ρ̄/(1−ρ̄²))` | stiffens at compression ceiling ρ̄→+1; **freezes at the cavitation floor ρ̄_cav = −1/φ** | the rarefaction/superluminal relation (`04_superluminal_transit.tex:86`); a DISTINCT wave from shear |

**Canonical backing for the shear/bulk split (Grant 2026-06-09):** the substrate sits at the **K = 2G operating point** (`claim-quality-closure-roadmap.md:149`: k_a=2/7, k_s=1/7 → K_0=16/7, G_0=8/7, ratio 2) → **Poisson ratio ν_vac = 2/7** as an algebraic identity, with Cosserat couple-stress length ℓ_c = √6·ℓ_node. Shear (G) and bulk (K) are not ad-hoc — they are the substrate's two locked elastic moduli.

> **Naming note (2026-06-10, Grant rename-queue adjudication R4 — line above preserved unedited):** "Cosserat couple-stress length" here is a first-use alias for the **normative name "Cosserat coupling length"** (ℓ_c = √6·ℓ_node). One object, three names in canon ("coupling" normative; "couple-stress" here; "characteristic" at `claim-quality.md:1036`). Registry §5 R4; Rule 1.

## 3. The two confirmed times (tick = ℓ_node / c_sector)

| clock | period | rate | verdict under load |
|---|---|---|---|
| **SHEAR clock = matter / gravitational** (rides c_shear) | `τ_shear = τ₀·(1−A²)^(−1/4)` | `ω_shear = ω₀·(1−A²)^(+1/4) = ω₀√S` | **DILATES** (slows) — gravitational time dilation |
| **BULK clock = compressional** (rides c_bulk) | `τ_bulk = τ₀/√(1+ρ̄/(1−ρ̄²))` | inverse | dilates toward the cavitation floor ρ̄_cav=−1/φ; faster under compression |
| **EM-phase "clock"** (rides c_EM) | `τ_EM = τ₀·(1−A²)^(+1/2)` | `ω_EM = ω₀·(1−A²)^(−1/2)` | phase advances FASTER (this is the α-speed, not a proper matter clock) |

**Sat vs desat (Grant 2026-06-09):** each mechanical mode has a **saturation** time (loading, strain↑) and a **desaturation** time (unloading, strain↓). The thixotropy question is whether they differ *per mode* (τ_sat ≠ τ_desat). The bulk mode already has **asymmetric LIMITS** — compression ceiling ρ̄→+1 (stiffen) vs rarefaction floor ρ̄_cav=−1/φ (cavitate) — so its sat (compress) and desat (rarefy) traverse different endpoints; whether that limit-asymmetry becomes a *time*-constant asymmetry is exactly the [thixotropy prereg](2026-06-09_thixotropy-amplitude-dependent-tau_prereg.md).

**The matter clock is the one that means "time dilation"** — a person, a chemical reaction, an atomic clock are mechanical wave-packets; packets move at the group/mechanical speed `c_shear`, which freezes as `(1−A²)^(1/4)`. **This answers the time-dilation prereg's exponent gate: p = ¼ (clock ∝ √S)** — and now with the physical *why*: matter is a packet, packets ride c_shear, c_shear freezes. Not "because INVARIANT-S2 says so."

## 4. Reconciliation of the three contradicting leaves (corpus-coherence; PR-gated walk-back)

| leaf | states | disposition |
|---|---|---|
| `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2:65,71 | gravitational clock = **c_shear ∝ (1−A²)^¼** | **CORRECT** — the matter clock (§3). Highest authority. |
| `op14-local-clock-modulation.md:17,31` | `ω_local = ω₀√(1−A²)` ∝ (1−A²)^**½** | **STALE** — a pre-split single-speed model (`c_eff = c₀√(1−A²)`) from before the c_EM/c_shear split (clm-8nkvwy). Off by a factor of 2 in the exponent. Flag for correction. |
| `04_superluminal_transit.tex:41` (Sleep Pod) | clock = `c = 1/√(με)` = **c_EM** | **MISLABELED** — that's the EM-phase speed, not the matter clock; the exact c_EM/c_shear category error S2 warns against (Pitfall #5). Flag for correction. |

Root cause: (i) the symbol `S` is overloaded (`√(1−A²)` vs `(1−A²)`) across leaves; (ii) "the clock" was stated without naming WHICH sector. Both fixed by §2–§3 (define in A, label the sector). **This reconciliation, applied to the three leaves, is a PR-gated walk-back — not done here.**

## 5. RESOLVED by Grant 2026-06-09 — shear vs bulk, each with sat & desat

The taxonomy is **not** "longitudinal vs transverse" loosely — it's the canonical elastic decomposition **shear (deviatoric, G) vs bulk (volumetric, K)**, locked at K=2G, **each with a saturation (loading) and a desaturation (unloading) time:**

- **Q1 resolved:** the matter/gravitational clock is the **SHEAR** mode (deviatoric distortion, modulus G=μ) — `c_shear = c₀(1−A²)^¼`, freezing at the saturation ceiling. (It is the mechanical-shear sector, distinct from the EM-transverse sector, which is electromagnetic, not one of the two mechanical moduli.)
- **Q2 resolved:** the compressional density wave **IS** a distinct time — the **BULK** mode (volumetric, modulus K), `c_bulk`, which freezes at the **cavitation floor ρ̄_cav = −1/φ**. So the taxonomy is **EM-transverse + shear + bulk** — three speeds, of which the two mechanical ones (shear, bulk) are the substrate's locked K=2G pair.

**The temporal value-set, then, is a 2×2 over the mechanical modes + the EM phase:**

| | saturation (load, strain↑) | desaturation (unload, strain↓) |
|---|---|---|
| **shear (G, matter clock)** | τ_shear,sat | τ_shear,desat |
| **bulk (K, density)** | τ_bulk,sat (→ compression ceiling ρ̄→+1) | τ_bulk,desat (→ cavitation floor ρ̄_cav=−1/φ) |

plus the EM-phase time τ_EM (electromagnetic, c_EM). Limits cleanly partition: **shear saturation = the A→1 ceiling; bulk desaturation = the ρ̄_cav=−1/φ floor** — the ceiling and the floor are different modes' freeze-points.

**Residual flag (the genuine open physics → the derivations, not a definition gap):**
- Does the bulk mode's **amplitude-limit** asymmetry (ceiling ρ̄=+1 vs floor ρ̄=−1/φ) become a **relaxation-TIME** asymmetry (τ_bulk,sat ≠ τ_bulk,desat)? If yes → the thixotropy/rectification door is open in the **bulk** mode; if no → closed. This is precisely the [thixotropy prereg](2026-06-09_thixotropy-amplitude-dependent-tau_prereg.md), now sharpened to the bulk sat-vs-desat channel.
- Is the shear strain `A` independent of the volumetric strain `ρ̄`, or coupled (does shearing a node also dilate it)? The derivation must state whether shear and bulk saturate independently or share a strain budget.

## 6. Deliverable targets (once §5 is called)

- **Vol-9 datasheet** (the figure-build): a "temporal characteristics" set — the speed curves (§2) and the clock curves (§3) vs A on one panel, dilating matter clock vs rising EM phase, with τ₀ = Compton tick as the baseline. Pairs with the ρ̄_cav rarefaction-floor figure already registered.
- **KB-leaf reconciliation** (§4) — the canonical temporal-values definition + the three-leaf walk-back. PR-gated, Core main.
- **Feeds** the time-dilation prereg (p=¼ confirmed for the matter clock, §3).
