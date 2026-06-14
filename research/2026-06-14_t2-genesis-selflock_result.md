# T2 — genesis self-lock (photon-at-a-field → autoresonant bulk breather) — RESULT

> **STATUS: NEGATIVE (clean, Rule-11 honest closure).** Prereg
> `research/2026-06-13_t2-genesis-selflock_prereg_FROZEN.md` (FROZEN, auditor-cleared).
> Driver `src/scripts/vol_1_foundations/t2_genesis_selflock.py` (DRIVER-NOT-BUILD on
> `crystal_engine.py`). Data `src/scripts/vol_1_foundations/t2_genesis_selflock_results.json`
> (production, 700 steps).
> **🔴 NO CHORD / GENESIS CLAIM.** This doc reports the four-way bin HONESTLY; a
> READ-ONLY auditor verifies against the discriminator before any framework move.

---

## 0. Headline (the four-way discriminator verdict)

**❌ NO-GENESIS at EVERY valve-open A₀ ∈ {0.69, 0.78, 0.866, 0.95}.** The (C) arm
(photon + generic field, converter ON) **DISPERSES** exactly like the (A′)/(A)
controls — the flowing transverse photon adds nothing. The asserted **autoresonant
self-lock** (the standing ✗ GAP at `photon-ee-mapping.md:98`) is **NOT realized on
`crystal_engine` in the near-yield forming regime**. The **PUMP** control
**DETONATES** at every A₀ (conserved-vs-pumped guard fires). The below-floor (C)
arm is **EXCLUDED** (valve-shut apparatus artifact, confirming the F6 floor exists).

This maps to the prereg §6 table **row 3** ("DISPERSE, A₀ ≥ g_front floor → ❌ no
genesis on `crystal_engine`: valve open, photon still can't build it"), uniformly
across the window. It is **not** the ✅ target-positive cell and **not** the ⚠️
field-self-genesis cell.

A null **is** meaningful here (prereg §4: the self-lock effect *can* exist in
near-yield forming; this is not a wrong-regime artifact). This is a valid result;
**no knobs were tuned to force a lock** (`ave-driver-script-honesty`, Rule 11).

---

## 1. Per-arm table (production, N=37, dx=1.0, σ=3.0, 700 steps)

`A0` = peak seed strain (= `frac`); `g_front` = converter-valve opening at A0
(engine `_front_window`); `Apk/Apersist/Aend` = max|A|ᵢₙₜₑᵣᵢₒᵣ peak / post-transient
envelope mean / end; `maxV` = boundedness monitor; `A²pk` = rupture check;
`ω_loc` = ω_local start→end (= ω₀·√S_core, the **corrected √S** matter-clock, NOT
√(1−A²), NOT refractive_index S^0.25); `PLV` = phasor phase-coherence (CP9, F3);
`dE` = total-energy drift (**REPORTED, not binned**). Bin per the prereg §3/§6.

| A₀ | g_front | arm | Apk | Apersist | Aend | maxV | A²pk | ω_loc | PLV | dE% | **bin** |
|---:|---:|:---|---:|---:|---:|---:|---:|:---|---:|---:|:---|
| 0.690 | 0.620 | **C** | 0.690 | 0.087 | 0.128 | 0.69 | 0.48 | 0.394→0.461 | 0.545 | −5 | **DISPERSE** |
| 0.690 | 0.620 | A′ | 0.690 | 0.086 | 0.126 | 0.69 | 0.48 | 0.394→0.461 | 0.542 | +2 | DISPERSE |
| 0.690 | 0.620 | A  | 0.690 | 0.086 | 0.127 | 0.69 | 0.48 | 0.394→0.461 | 0.554 | −4 | DISPERSE |
| 0.690 | 0.620 | PUMP | 78.4 | 46.2 | 35.0 | 78.4 | 6152 | 1.047→0.462 | 0.974 | +29.9M | **DETONATE** |
| 0.780 | 0.892 | **C** | 0.780 | 0.099 | 0.146 | 0.78 | 0.61 | 0.367→0.461 | 0.562 | −2 | **DISPERSE** |
| 0.780 | 0.892 | A′ | 0.780 | 0.097 | 0.143 | 0.78 | 0.61 | 0.367→0.461 | 0.556 | +16 | DISPERSE |
| 0.780 | 0.892 | A  | 0.780 | 0.098 | 0.147 | 0.78 | 0.61 | 0.367→0.461 | 0.563 | −3 | DISPERSE |
| 0.780 | 0.892 | PUMP | 79.0 | 46.2 | 35.1 | 79.0 | 6246 | 0.973→0.462 | 0.969 | +23.7M | **DETONATE** |
| 0.866 | 1.000 | **C** | 0.866 | 0.110 | 0.162 | 0.87 | 0.75 | 0.328→0.461 | 0.591 | +2 | **DISPERSE** |
| 0.866 | 1.000 | A′ | 0.866 | 0.107 | 0.158 | 0.87 | 0.75 | 0.328→0.461 | 0.578 | +36 | DISPERSE |
| 0.866 | 1.000 | A  | 0.866 | 0.109 | 0.167 | 0.87 | 0.75 | 0.328→0.460 | 0.572 | −0 | DISPERSE |
| 0.866 | 1.000 | PUMP | 77.2 | 46.2 | 35.8 | 77.2 | 5967 | 0.870→0.462 | 0.966 | +18.8M | **DETONATE** |
| 0.950 | 0.897 | **C** | 0.950 | 0.121 | 0.180 | 0.95 | 0.90 | 0.259→0.460 | 0.595 | +7 | **DISPERSE** |
| 0.950 | 0.897 | A′ | 0.950 | 0.116 | 0.174 | 0.95 | 0.90 | 0.259→0.460 | 0.587 | +57 | DISPERSE |
| 0.950 | 0.897 | A  | 0.950 | 0.121 | 0.187 | 0.95 | 0.90 | 0.259→0.460 | 0.572 | +3 | DISPERSE |
| 0.950 | 0.897 | PUMP | 76.1 | 46.1 | 36.0 | 76.1 | 5786 | 0.688→0.462 | 0.954 | +15.3M | **DETONATE** |

**F6 below-floor (C):** A₀=0.400, g_front=0.035 → Apk=0.400, Apersist=0.049,
maxV=0.40, A²pk=0.16, PLV=0.511 → **DISPERSE → EXCLUDED-VALVE-SHUT** (valve never
opened; apparatus artifact, NOT a physics null — `ave-apparatus-floor-attribution`).

**Ablation (opposite helicity h=−1 at R_II):** Apk=0.866, Apersist=0.110, PLV=0.591
→ **DISPERSE** — identical to h=+1. Chirality does not rescue the lock.

---

## 2. The load-bearing reads (why it is DISPERSE, not LOCK)

1. **No ring-up.** `max|A|` never exceeds the seed in any (C)/(A′)/(A) arm
   (Apk = A₀ to float precision). The core does not fill — the field sheds
   (Apersist falls to ~0.09–0.12, ~13–14 % of seed). The cage's static result
   (generic Gaussian disperses, profile-selective) holds **dynamically** with a
   flowing photon present.

2. **The photon is inert (the discriminator).** At every A₀ the (C) summaries are
   indistinguishable from (A′)/(A): at R_II, PLV is **0.591 (C) ≈ 0.578 (A′) ≈
   0.572 (A)**; Apersist 0.110/0.107/0.109. The single new variable — the photon —
   does **not** lift coherence, ring-up, or persistence. This is the prereg F2
   discriminator reading "photon adds nothing," not "field self-genesises."

3. **Phase-coherence (CP9/F3) is sub-lock and photon-independent.** PLV ≈ 0.55–0.60
   in the forming arms — **below the PLV_LOCK = 0.80 gate**, and the phasor radius
   collapses as the field disperses (`phasor_radius_persist` < PERSIST_FRAC). The
   moderate (not ~0) PLV is the slowly-dispersing field retaining *some* phase
   relation to the *rising* ω_local; it is not an autoresonant lock (the (C)=(A′)=(A)
   equality is decisive).

4. **ω_local RISES — the anti-lock signature.** In every forming arm ω_local climbs
   (e.g. 0.328→0.461 at R_II) because A *drops* as the field sheds → S_core rises →
   the matter clock speeds back up toward ω₀. A genuine self-lock requires the
   **opposite** (core fills, A grows, S drops, ω_local **drops**). The only arm
   where ω_local drops is the **PUMP** (0.870→0.462) — because the fixed-ω free-work
   drive pumps the core to A²≈6000, i.e. a **detonation**, not a lock.

5. **Boundedness vs persistence.** (C)/(A′)/(A) are **bounded** (maxV ≤ 0.95,
   A²pk ≤ 0.90 — near-yield forming, sub-rupture R_III=1) but **not persistent**
   (Apersist ≪ seed). Success requires **bounded AND persistent** (prereg §7); these
   are bounded-and-dispersing. The **PUMP** is **neither** (maxV ≈ 76–79, A² ≈ 6000,
   energy drift +1.5×10⁷–3×10⁷ %) → DETONATE (🔴 pump artifact, prereg §6 row 5).

---

## 3. Falsifier ledger (prereg §6)

| Falsifier | Reading | Verdict |
|:---|:---|:---|
| **F0** baseline (no seed → no wall) | inherited from cage; (A) converter-OFF disperses | consistent ✓ |
| **F1** (C) lock (grow + coherent + bounded + persist) | Apk=seed, PLV<0.80, Apersist≪seed | **NOT met → ❌** |
| **F2** (A′) discriminator (field+converter, no photon DISPERSES) | (A′) DISPERSES at all A₀ | **holds ✓** (⚠️ self-genesis row pre-excluded, confirmed dynamically) |
| **F3** autoresonance signature (CP9 phase-coherence sustained as ω_local drops) | ω_local RISES; PLV sub-lock; (C)=(A′)=(A) | **ABSENT → ✗** (the GAP, now tested-negative) |
| **F4** conserved-not-pumped (PUMP detonates/pumps) | PUMP DETONATES at all A₀ (control) | **fires ✓** |
| **F5** regime (lock in near-yield forming A²≤1; post-rupture excluded) | (C)/(A′)/(A) A²≤0.90 (in-regime); PUMP A²≈6000 excluded | **in-regime, valid null ✓** |
| **F6** g_front floor (below-floor (C) = valve-never-opened, EXCLUDED) | A₀=0.40 g_front=0.035 → EXCLUDED-VALVE-SHUT | **floor confirmed ✓** |

**Single mechanism explaining all (C)/(A′)/(A) disperse results** (Rule 11): the
front-gated converter sources only a small bulk V from the photon's Ω_w
(`f_V = −κ̃·g_front·Ω_w`), and the generic Gaussian's dispersive shedding dominates
that transient injection by orders of magnitude. The photon's energy is far too
small, and delivered over too brief a transit, to nucleate a self-focusing breather
from a non-eigen (generic) precursor. This is consistent with — and the dynamic
extension of — the cage's static profile-selectivity (generic disperses; only the
sech eigen-profile self-focuses).

---

## 4. Flags (flag-don't-fix — for auditor adjudication, NOT resolved here)

- **FLAG-1 — `converter_work` is not a clean photon-attribution signal.** The
  converter is **bidirectional**: `f_w = ±κ̃·∂(g·V)` sources shear `w` from the bulk
  front **even with no photon**, which then back-sources V. So `converter_work` is
  nearly identical with/without the photon (e.g. ~−0.74 both at A₀=0.866 over the
  characterization run). It is **reported in the JSON but NOT used as a headline**.
  (This is engine behavior, surfaced, not changed.)

- **FLAG-2 — converter-ON arms grow energy more than converter-OFF.** Total-energy
  drift: (A′) converter-ON-no-photon reaches +36 %/+57 % (A₀=0.866/0.95) vs (A)
  converter-OFF ≈ 0 % and (C) ≈ +2 %/+7 %. The converter (ON in both A′ and C)
  bidirectionally sources shear from the bulk → modest leapfrog energy growth.
  **REPORTED, not binned** (per cage Amendment 3 the verdict axis is
  boundedness+persistence, not energy-flatness). Notably (C) drifts *less* than (A′),
  i.e. the photon does not pump the ledger either.

- **FLAG-3 — disperse-arm PLV is moderate (~0.55–0.60), not ~0.** Driven by the
  slow-dispersal phase relation to the rising ω_local, not a lock. The discriminator
  is robust because (C)≈(A′)≈(A) and the phasor radius collapses; but the absolute
  PLV floor is a property of the metric on a slowly-shedding field, flagged so the
  auditor reads "sub-lock + photon-independent," not "low absolute coherence."

- **FLAG-4 — negative is robust to photon config (pre-freeze characterization).**
  The disperse verdict is unchanged across photon amplitude 0→4×, σ (dwell) 3→15,
  wavelength 6→12, and offset-incidence — so the null is not a too-weak / too-brief
  / too-localized-photon artifact. One fixed config (amp=1.0, wl=6, σ=3, h=+1) is
  reported, chosen for energy-parity with the seed, **not** swept to force a lock.

---

## 5. Scope + classification (`consistency-vs-emergence`)

- **H1 (emergence-test: (C) locks where (A) disperses):** **FALSIFIED** on
  `crystal_engine`, near-yield forming. (C) disperses like (A).
- **H2 (consistency: generic sub-critical field disperses alone):** **CONFIRMED**
  ((A)/(A′) disperse; dynamic extension of the cage static result).
- **H3 (the (C) lock is autoresonant):** **moot — there is no (C) lock**; the
  autoresonance signature (F3) is **absent** (the `photon-ee-mapping.md:98` ✗ GAP is
  now **tested-negative**, not merely underived).
- **H4 (fixed-ω PUMP detonates/pumps, not locks):** **CONFIRMED** (control).

**Honest scope.** This is a negative for **this engine** (`crystal_engine`, the
front-gated κ̃=6/5 converter), **this regime** (near-yield forming, A²≤1), **this
precursor** (generic Gaussian, CP8-compliant). It does **NOT** prove photon→mass is
impossible; it shows the asserted autoresonant self-lock is **not realized by this
converter mechanism in this regime**. The (B) from-vacuum path is out of scope
(physically forbidden + engine-nulled; anti-loophole, no 4th engine). Per lane
discipline, this doc does **not** propose a new converter strength, regime, or
methodology pivot — that is corpus+Grant adjudication, not the implementer's call.

**Rule 12 note (substitution-not-retraction):** nothing is retracted — the
autoresonance was a standing GAP (✗, never a claim). This converts it from
"untested" to "tested-negative on `crystal_engine`/near-yield-forming." Any future
re-test (different engine/regime) gets its own prereg + version + verification chain.

---

## 6. Reproduce

```
PYTHONPATH=src .venv/bin/python src/scripts/vol_1_foundations/t2_genesis_selflock.py --production
```

Outputs `t2_genesis_selflock_results.json` next to the driver (repo convention,
mirrors `cage_stiffening_wall_results.json`). `--smoke` for CI budget. Canonical
constants cross-check (`verify_constants`) runs before any output and **aborts on a
bad bench** (no output on a failed cross-check). `make verify` passes.
