# PREREG — Phase 5: rarefaction / cavitation vacuum-pump drive (the suction half)

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-08-rrad-l-darkwake` (continues Phases 1–4)
**Companions:** Phases 1–4 (the COMPRESSION half — stiffening/saturation, n≫1 — all OUTCOME B + a mundane radiator).
**Frame correction (Grant 2026-06-09):** stop importing GR negative-energy/exotic-matter blockers; reason as a vacuum engineer.

> **SCAFFOLD** (orchestration-written, for review before compute). Tests the untested SUCTION half of the dipole.

---

## 0. FRAME — vacuum-engineer, NOT GR (read first)

The vacuum is a **real compressible LC medium**. **Rarefaction = a below-baseline-density region made by REDISTRIBUTION (compress elsewhere) + PUMP WORK** — mundane: the suction side of a pump, the low-pressure wake behind a moving body, a cavitation void. **No negative energy / exotic matter** — that requirement is a GR category error (treating the vacuum as spacetime geometry instead of as the material AVE says it is; corpus's own line, [04_superluminal_transit.tex:11](../../AVE-Propulsion/manuscript/vol_propulsion/chapters/04_superluminal_transit.tex)). The honest check is the **pump energy-momentum ledger** (work-in vs momentum-ejected), like any reaction engine — **NOT** "negative energy is impossible." Do not smuggle GR blockers into this test.

## 1. Target

Phases 1–4 drove the **compression** half (n≫1, stiffening, saturation/yield) → mundane radiator + B. This tests the **rarefaction / cavitation** half (n≪1, `Tr(ε)<0`, the suction side) — where the corpus actually puts the exotic behavior (v_eff>c, *"the exact topological basis of Warp Mechanics,"* [01_local_refractive_control.tex:34](../../AVE-Propulsion/manuscript/vol_propulsion/chapters/01_local_refractive_control.tex)). **Does the substrate's compression-vs-rarefaction MATERIAL asymmetry net directed thrust with an honest pump ledger?**

## 2. substrate-native-check FIRST (Grant directive — keep SM reflexes out)

Before any code, walk the substrate — NOT an SM-imported fluid/friction model:
- **Can the engine represent rarefaction** (`Tr(ε)<0` / below-baseline volumetric strain)? Corpus `ρ̄ ∈ [−1,1]` ([04:89]) says the model allows it; confirm the engine DOF supports dilation, not just the compression-A drive.
- **The substrate's rarefaction/tensile limit.** Compression → saturation **ceiling** (A=1, Γ=−1, stiffening). Rarefaction → cavitation/void **floor** (density→0), tensile-failure extreme = **pair production** (the 511 kV *"tensile strength of a single flux tube,"* [11_experimental_falsification.tex:270](../../AVE-Core/manuscript/vol_4_engineering/chapters/11_experimental_falsification.tex); the vacuum tears → e⁺e⁻). Ceiling vs floor = **different events** → the source of the asymmetry.
- **Is the medium response asymmetric?** Canonical `S(A)=√(1−A²)` is even-in-A — the *small-signal* approximation. The asymmetry lives at the **limits** (saturation ceiling vs cavitation/tensile floor). The drive must probe the asymmetric (near-limit) regime, not the symmetric small-signal one.
- Design the rarefaction drive substrate-natively (a dilational/tension drive on the volumetric strain + cavitation onset), grounded in the corpus rarefaction/cavitation/tensile leaves.

## 3. Mechanism (vacuum-engineer)

Compression (stiffens, saturation ceiling) vs rarefaction (cavitates/voids, tensile floor) — **asymmetric material response.** A compress-bow / rarefy-stern **dipole** (or a compress-rarefy cycle): if the response is asymmetric, the bow and stern forces **do not cancel** → net thrust. Mundane — a **cavitating propeller / asymmetric hull pumping the vacuum.** The rarefaction is paid for by pump-work + redistribution; total energy conserved.

## 4. The honest check — the SPINE (pump energy-momentum ledger, NOT the SM blocker)

- **ENERGY:** pump-work-in vs thrust-energy-out. Must close like a pump (`W_pump ≥` kinetic energy of the ejected wake). **Compute and report it.**
- **MOMENTUM:** net thrust = momentum ejected into the medium (the wake), conserved (reaction engine, not reactionless).
- **Discriminator:**
  - SYMMETRIC medium response (even-in-A throughout) → bow/stern cancel → `∮=0`, no net thrust.
  - ASYMMETRIC response → net thrust → **then check the ledger: closes (honest pump) or requires overunity (free energy)?**

## 5. Outcomes

- **A — REAL:** asymmetric response → net directed thrust **AND the pump ledger closes** (no overunity) → a genuine **vacuum-pump thruster**, mundane medium mechanics (cavitating-prop class). The chord — and *not exotic*: it's a pump, not a warp.
- **B — DEAD:** response symmetric (compression = rarefaction mirrored) → dipole cancels → no net thrust → rarefaction route dead too; the compress-rarefy thrust premise is refuted across both halves.
- **C — CRANK:** nets thrust **only by violating the ledger** (overunity / rarefaction "free") → it was smuggling free energy after all → crank confirmed, dead. (The *ledger* catches this — not an a-priori SM blocker.)

## 6. Guards

- Rarefaction/tensile/cavitation limit + the asymmetry from CANON, **not tuned**.
- The pump ledger is computed + reported every run; **overunity → automatic C (negative)**.
- A SYMMETRIC (no-asymmetry / no-rarefaction) control must give no net thrust.

## 7. Skills + deliverables

- **Skills:** **substrate-native-check (FIRST, leading)** · ave-canonical-leaf-pull (rarefaction / cavitation / tensile-limit / pair-production leaves) · ave-canonical-source (limits from canon) · ave-driver-script-honesty (the pump-ledger spine — report W_in / momentum-out, flag overunity) · consistency-vs-emergence + ave-discrimination-check (is a working vacuum-pump thrust AVE-distinct — pumping a *mechanical* vacuum medium — or does it reduce to ordinary EM radiation pressure?).
- **Deliverables:** `research/2026-06-08_rrad-l-rarefaction-phase5_result.md` (A/B/C + the symmetric control + the pump energy-momentum ledger numbers + DERIVED/VERIFIED/BLOCKED); driver (rarefaction/cavitation drive + pump-ledger diagnostics). Commit on the branch; orchestration handles PR #144. Do NOT push/merge.
