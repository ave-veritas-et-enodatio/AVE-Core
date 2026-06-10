# PREREG — Phase 5: rarefaction / cavitation vacuum-pump drive (the suction half)

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-08-rrad-l-darkwake` (continues Phases 1–4)
**Companions:** Phases 1–4 (the COMPRESSION half — stiffening/saturation, n≫1 — all OUTCOME B + a mundane radiator).
**Frame correction (Grant 2026-06-09):** stop importing GR negative-energy/exotic-matter blockers; reason as a vacuum engineer.

> **SCAFFOLD** (orchestration-written, for review before compute). Tests the untested SUCTION half of the dipole.

---

## 0. FRAME — vacuum-engineer, NOT GR (read first)

The vacuum is a **real compressible LC medium**. **Rarefaction = a below-baseline-density region made by REDISTRIBUTION (compress elsewhere) + PUMP WORK** — mundane: the suction side of a pump, the low-pressure wake behind a moving body, a cavitation void. **No negative energy / exotic matter** — that requirement is a GR category error (treating the vacuum as spacetime geometry instead of as the material AVE says it is; corpus's own line, [04_superluminal_transit.tex:11](../../AVE-Propulsion/manuscript/vol_propulsion/chapters/04_superluminal_transit.tex)). The honest check is the **pump energy-momentum ledger** (work-in vs momentum-ejected), like any reaction engine — **NOT** "negative energy is impossible." Do not smuggle GR blockers into this test.

## 1. Target

Phases 1–4 drove the **compression** half with a **single, sector-trapped chirality** (ω/shear) → mundane radiator + B (sector mismatch + no temporal symmetry-breaker). This tests the **rarefaction / cavitation** suction side (n≪1, `Tr(ε)<0`) — where the corpus puts the exotic behavior (v_eff>c, *"the exact topological basis of Warp Mechanics,"* [01_local_refractive_control.tex:34](../../AVE-Propulsion/manuscript/vol_propulsion/chapters/01_local_refractive_control.tex)) — **driven by COUNTERACTING (counter-propagating, opposite-handed) chirality** (Grant 2026-06-09). **Does an asymmetric, polarization-controlled, sub-yield counter-propagating opposite-handed drive net directed thrust with an honest pump ledger?**

### 1a. Why counteracting chirality (the primary mechanism — addresses BOTH diagnosed failures)

The corpus's own electron-genesis is *counteracting chirality*: [pair-production-axiom-derivation.md:51,77](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) — two **counter-propagating opposite-handed** drives breaching yield → *"longitudinal phase velocity crashes to zero... blocked linear kinetic potential shatters **sideways into transverse DOF**... contra-rotating vortex dipoles"* (LH + RH). That is a **sector-conversion event** (longitudinal↔transverse via the phase-tear) AND a temporal **event** — exactly the two ingredients Phases 1–4 lacked (single chirality = sector-trapped + steady = time-symmetric).

- **Counteracting** (counter-propagating opposite-handed) → phase-tear sector bridge + temporal event.
- **Polarizing** → control the `(V_inc, V_ref)` phasor trajectory / d-q state (where the (2,3) winding + the ledger enclosed area live; *"Polarization Mismatch"* is the canonical coupling knob, [04_chiral_impedance_matching.tex:11](../../AVE-Propulsion/manuscript/vol_propulsion/chapters/04_chiral_impedance_matching.tex)). An **open/asymmetric** phasor loop = nonzero enclosed area = rectification.
- **Softening** → stay **sub-yield** (below the pair-production tear) so conversion is partial + directed; energy → momentum, not rest-mass.

### 1b. The honest bound (vacuum-engineer)

The FULL breach = **pair production** (e⁺e⁻, 1.022 MeV/pair — an energy SINK), and a **symmetric** counteraction → symmetric contra-rotating pair → **zero net momentum**. So thrust lives in the **sub-yield, asymmetric** regime only. **Pair-production is the loss line to stay under** — cross it and energy goes to matter, not thrust. The ledger must track it.

## 2. substrate-native-check FIRST (Grant directive — keep SM reflexes out)

Before any code, walk the substrate — NOT an SM-imported fluid/friction model:
- **Can the engine represent rarefaction** (`Tr(ε)<0` / below-baseline volumetric strain)? Corpus `ρ̄ ∈ [−1,1]` ([04:89]) says the model allows it; confirm the engine DOF supports dilation, not just the compression-A drive.
- **The substrate's rarefaction/tensile limit.** Compression → saturation **ceiling** (A=1, Γ=−1, stiffening). Rarefaction → cavitation/void **floor** (density→0), tensile-failure extreme = **pair production** (the 511 kV *"tensile strength of a single flux tube,"* [11_experimental_falsification.tex:270](../../AVE-Core/manuscript/vol_4_engineering/chapters/11_experimental_falsification.tex); the vacuum tears → e⁺e⁻). Ceiling vs floor = **different events** → the source of the asymmetry.
- **Is the medium response asymmetric?** Canonical `S(A)=√(1−A²)` is even-in-A — the *small-signal* approximation. The asymmetry lives at the **limits** (saturation ceiling vs cavitation/tensile floor). The drive must probe the asymmetric (near-limit) regime, not the symmetric small-signal one.
- Design the rarefaction drive substrate-natively (a dilational/tension drive on the volumetric strain + cavitation onset), grounded in the corpus rarefaction/cavitation/tensile leaves.

## 3. Mechanism (vacuum-engineer)

The compress-bow / rarefy-stern **dipole** is GENERATED by **counter-propagating opposite-handed chiral drives** (§1a): their interference compresses one region and rarefies the other, and at the focal interface the phase-tear converts longitudinal↔transverse (the canonical sector bridge). Compression (stiffens, saturation ceiling) vs rarefaction (cavitates/voids, tensile floor) is the **asymmetric material response**; the **asymmetric polarization trajectory** (one handedness softened/shaped relative to the other) is the temporal symmetry-breaker (open phasor loop = enclosed area). If both asymmetries are present and the drive stays **sub-yield**, the dipole forces don't cancel → net directed thrust. Mundane — a **counter-rotating cavitating pump on the vacuum**, paid for by pump-work + redistribution; energy conserved. (Symmetric counteraction → symmetric pair → zero net; full breach → pair production sink — §1b.)

## 4. The honest check — the SPINE (pump energy-momentum ledger, NOT the SM blocker)

- **ENERGY:** pump-work-in vs thrust-energy-out. Must close like a pump (`W_pump ≥` kinetic energy of the ejected wake). **Compute and report it.**
- **MOMENTUM:** net thrust = momentum ejected into the medium (the wake), conserved (reaction engine, not reactionless).
- **Discriminator:**
  - SYMMETRIC medium response (even-in-A throughout) → bow/stern cancel → `∮=0`, no net thrust.
  - ASYMMETRIC response → net thrust → **then check the ledger: closes (honest pump) or requires overunity (free energy)?**

## 5. Outcomes

- **A — REAL:** sub-yield **asymmetric** counter-propagating opposite-handed drive → directed partial sector-conversion → net directed thrust, **pump ledger closes** (no overunity), and the drive **stays below the pair-production tear** → a genuine **counter-rotating cavitating vacuum pump**, mundane medium mechanics. The chord — a pump, not a warp.
- **B — DEAD:** **symmetric** counteraction → symmetric contra-rotating pair → zero net momentum; OR symmetric medium response → dipole cancels. The mechanism nets nothing directed → the counteracting-chirality / rarefaction route is dead too.
- **C — SINK / CRANK:** nets "thrust" only by (i) **overunity** (ledger violation → smuggled free energy) or (ii) **breaching to pair production** (energy → rest-mass, e⁺e⁻ created — it's a particle-maker, not a thruster). Either way NOT a thruster — and the *ledger + the pair-production loss line* catch it, no a-priori SM veto needed.

## 6. Guards

- Rarefaction/tensile/cavitation/pair-production limits + the asymmetry from CANON, **not tuned**.
- The pump ledger is computed + reported every run; **overunity → automatic C**.
- **Two mandatory controls:** (i) a **symmetric counteraction** (equal-and-opposite, no polarization asymmetry) must give zero net momentum (the symmetric-pair null); (ii) verify the drive **stays sub-yield** — if net "thrust" only appears once the focal amplitude breaches the pair-production threshold, that's the **particle-maker sink (C)**, not a thruster.

## 7. Skills + deliverables

- **Skills:** **substrate-native-check (FIRST, leading)** · ave-canonical-leaf-pull (rarefaction / cavitation / tensile-limit / pair-production leaves) · ave-canonical-source (limits from canon) · ave-driver-script-honesty (the pump-ledger spine — report W_in / momentum-out, flag overunity) · consistency-vs-emergence + ave-discrimination-check (is a working vacuum-pump thrust AVE-distinct — pumping a *mechanical* vacuum medium — or does it reduce to ordinary EM radiation pressure?).
- **Deliverables:** `research/2026-06-08_rrad-l-rarefaction-phase5_result.md` (A/B/C + the symmetric control + the pump energy-momentum ledger numbers + DERIVED/VERIFIED/BLOCKED); driver (rarefaction/cavitation drive + pump-ledger diagnostics). Commit on the branch; orchestration handles PR #144. Do NOT push/merge.
