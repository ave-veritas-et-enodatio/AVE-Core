# T2 — genesis self-lock (photon-at-a-field → autoresonant bulk breather) — RESULT

> **STATUS: NEGATIVE (clean, Rule-11 honest closure) — with a 🔴 DETECTOR FLAG on the
> LOCK bin (§0.5), pending auditor+Grant adjudication.** Prereg
> `research/2026-06-13_t2-genesis-selflock_prereg_FROZEN.md` (FROZEN, auditor-cleared).
> Driver `src/scripts/vol_1_foundations/t2_genesis_selflock.py` (DRIVER-NOT-BUILD on
> `crystal_engine.py`). Data `src/scripts/vol_1_foundations/t2_genesis_selflock_results.json`
> (production, 700 steps; sech positive-control 600 steps).
> **🔴 NO CHORD / GENESIS CLAIM.** This doc reports the four-way bin HONESTLY; a
> READ-ONLY auditor verifies against the discriminator before any framework move.
> **🔴 The SECH positive control (§0.5) did NOT validate the LOCK detector** (the
> known self-focusing v14 sech bins **UNRESOLVED**, not LOCK — PLV-gate too strict).
> The NEGATIVE's **load-bearing legs (ring-up + persistence) ARE validated**; the
> **PLV/F3 coherence leg is NOT** and is downgraded to uninformative. The verdict is
> reported as-is (flag-don't-fix); the LOCK-detector limitation is surfaced for
> adjudication, **not tuned away**.

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

## 0.5 Instrument validation — SECH positive control (🔴 DETECTOR FLAG)

> **Role (`consistency-vs-emergence`): DETECTOR-VALIDATION / positive-control — NOT a
> frozen-prereg arm, NOT part of the four-way discriminator.** `ave-apparatus-floor-
> attribution` validate-on-**known-positive**: before reading the (C) DISPERSE as a
> real negative, the LOCK-detector must be shown to **fire on a genuine self-focus**.
> The cage proved the v14 Mode-I **sech eigen-profile self-focuses** (cage `SECH_ANCHOR`,
> PR #222). So we seed **that exact sech** (`1/cosh(r/R)`, direct-assign to `V`,
> ∂ₜV=0) in the cage's self-focus box (N=24, dx=0.5, R=2.5), **converter OFF, NO
> photon**, and run it through the **EXACT committed detector** (same `evolve` loop,
> same `_carrier_omega0`/phasor, same `classify()` + LOCK criterion — unchanged), with
> the v14-box `dt` (`_DT_SECH`, half the T2-box dt; mis-using the T2 dt would mis-scale
> ω_local and *worsen* PLV — this is the best-case read). **substrate-native-check:**
> deliberately planting the known self-focusing end-state is **correct** for a detector
> check (CP8's seed-the-precursor guard governs the *emergence*-test arms, not the
> detector validation).

**Result — the sech SELF-FOCUSES but bins UNRESOLVED, NOT LOCK** (production, 600 steps):

| amp | A₀ | Apk | **ring-up apk/a0** | grew_F1 | Apersist | (Apersist/A₀) | A²pk | maxV | PLV | radpersist | **bin** |
|---:|---:|---:|---:|:---:|---:|---:|---:|---:|---:|---:|:---|
| 0.20 | 0.200 | 0.396 | **1.979×** | True | 0.185 | 93 % | 0.157 | 0.40 | 0.538 | 0.954 | **UNRESOLVED** |
| 0.30 | 0.300 | 0.583 | **1.942×** | True | 0.270 | 90 % | 0.339 | 0.58 | 0.530 | 0.934 | **UNRESOLVED** |
| 0.50 | 0.500 | 0.899 | **1.798×** | True | 0.411 | 82 % | 0.808 | 0.90 | 0.530 | 0.850 | **UNRESOLVED** |

**Robustness (pre-report characterization).** The sech bins UNRESOLVED across amp
0.20–0.50 **and** nsteps 600/1000/1400; ring-up is invariant (1.80–1.98×) and PLV
peaks at **0.770** (amp 0.50, n=1000) — **never crossing the 0.80 gate**, and
non-monotonic (drops to ~0.45–0.52 at n=1400). So the sub-lock PLV is **structural**,
not an under-resolution artifact.

**What this validates (the load-bearing legs — ✅):**

1. **Ring-up discriminates.** The sech grows (Apk = **1.8–2.0× A₀**, grew_F1=True);
   the (C)/(A′)/(A) photon arms show **no ring-up** (Apk = seed to float precision).
2. **Persistence discriminates.** The sech persists (Apersist = **82–93 % of A₀**,
   radpersist 0.85–0.95); the photon arms shed to **~13 % of seed** (Apersist 0.09–0.12).
   The (C) **DISPERSE** verdict is produced by `classify()`'s `not persisted` branch —
   **this is the validated leg.** The sech, being `persisted=True`, is correctly **not**
   binned DISPERSE.

**What this does NOT validate (🔴 the detector flag):**

3. **The PLV phase-coherence LOCK-gate does NOT fire on a genuine self-focus.** The
   sech's PLV (**0.530–0.538**) is **statistically indistinguishable from the disperse
   photon arms' PLV (0.55–0.60)** — the metric does **not** separate self-focus from
   disperse. The forming/breathing sech is not a clean single-tone carrier
   (spectral concentration ≈ 0.17–0.22), so its core phasor does not advance
   coherently at the predicted ω_local. **The LOCK bin (which requires PLV ≥ 0.80) is
   therefore unreachable by even a genuine self-focus.**

**Consequences (flag-don't-fix; do NOT tune; auditor+Grant adjudicate):**

- **The harness could not have certified a TARGET-POSITIVE via LOCK.** Had the photon
  actually induced a self-focus, it would have binned **UNRESOLVED** (self-focus the
  PLV-gate refuses to certify), not LOCK / TARGET-POSITIVE. The positive control lands
  **exactly in the UNRESOLVED bin** that §Cleanup-queue item 1 flagged as "reached by
  no arm" — so UNRESOLVED is **live**, the "self-focus the PLV-gate won't certify" bin,
  not dead.
- **The NEGATIVE still stands on its load-bearing legs.** (C) DISPERSE is driven by
  *persistence* (validated, legs 1–2 above), so "photon adds nothing" is sound:
  the photon arms neither ring up nor persist, the known-positive does both.
- **The F3 / PLV "autoresonance-signature-absent" leg is downgraded to UNINFORMATIVE.**
  §2 point 3, §3 row F3, and FLAG-3 read sub-lock PLV as anti-lock evidence; the
  positive control shows the **known-positive also has sub-lock PLV**, so PLV<0.80 is
  **not** a negative discriminator here. Those passages are **left intact** (flag-don't-
  fix) and cross-flagged to this section; the auditor adjudicates whether to rest the
  negative on ring-up/persistence **only** (recommended) and whether the PLV-gate /
  ω_local-phasor instrument needs a redesign before any future positive could be read.
- **Per task discipline: STOP + report; do NOT proceed** to "detector validated →
  NO-GENESIS confirmed." The negative is reported as-is with this flag attached; the
  LOCK-detector limitation is an auditor+Grant decision, **not the implementer's** to
  resolve (Rule 15/16 lane discipline).

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
   **🔴 DOWNGRADED (see §0.5):** the known-positive sech *also* reads sub-lock PLV
   (~0.53), indistinguishable from these arms — so sub-lock PLV is **not** a negative
   discriminator. The decisive read in this point is the **(C)=(A′)=(A) equality + the
   absence of ring-up/persistence**, NOT the absolute PLV value. (Body left intact;
   flag-don't-fix.)

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
| **F3** autoresonance signature (CP9 phase-coherence sustained as ω_local drops) | ω_local RISES; PLV sub-lock; (C)=(A′)=(A) | **ABSENT → ✗** (🔴 see §0.5: PLV-leg uninformative — the known-positive sech is *also* PLV-sub-lock; the **ω_local-RISES + (C)=(A′)=(A)** sub-reads carry F3, NOT the PLV value) |
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
  **🔴 ESCALATED by §0.5:** the metric's sub-lock floor is now shown to apply to a
  **genuine self-focus** too (the v14 sech PLV ≈ 0.53, radpersist 0.85–0.95) — so the
  PLV-gate cannot certify *any* positive, not just these disperse arms. The
  discriminator's robustness rests entirely on ring-up/persistence (validated, §0.5),
  not on PLV.

- **FLAG-4 — POST-DATA robustness characterization (NOT a frozen-prereg arm).**
  *(`ave-evidence-framing-discipline` reframe — this is post-data supporting evidence,
  not a pre-registered "robust" claim.)* The single **headline** photon config
  (amp=1.0, wl=6, σ=3, h=+1) is the **only** frozen-prereg config; it was chosen for
  **energy-parity with the seed**, **not** swept to lock. Separately, **after** the
  data, the disperse verdict was checked to be unchanged across photon amplitude
  0→4×, σ (dwell) 3→15, wavelength 6→12, and offset-incidence. **The mechanism that
  makes this null structural** (not a too-weak / too-brief / too-localized-photon
  artifact): the **front-gated converter sources too little bulk-V from the photon's
  Ω_w *regardless of photon amplitude*** — `f_V = −κ̃·g_front·Ω_w` injects only a thin
  saturation-front transient, which the generic Gaussian's dispersive shedding
  dominates by orders of magnitude (§3 single-mechanism). Scaling the photon scales
  that small injection but does not change the regime, so the null **persists by
  construction**, not because the swept photons happened to be too weak. Read this as
  **post-data support + a named mechanism**, NOT as a pre-registered robustness sweep.

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

## 5.5 Cleanup queue (deferred — NOT retrofitted)

Surfaced during the §0.5 positive-control work; **not fixed here** (they do not change
the current result, and the LOCK-criterion is frozen-as-committed per task discipline —
`flag-don't-fix`). For auditor+Grant review:

1. **The `UNRESOLVED` bin** (`classify()` `t2_genesis_selflock.py:382`, "persistent but
   not phase-coherent") was reached by **no four-way arm** — was it a needed safety bin
   or dead code? **§0.5 answers this empirically:** the sech positive control lands
   **exactly** in UNRESOLVED (self-focus + persist + grow + bounded, but PLV<0.80). So
   the bin is **live and load-bearing** — it is where a genuine self-focus that the
   PLV-gate refuses to certify falls. Keep; review whether a true positive *should* be
   routed here vs LOCK (i.e. whether the PLV-gate belongs in the LOCK condition at all).

2. **`grew` is computed but OMITTED from the LOCK condition.** `grew` is evaluated at
   `t2_genesis_selflock.py:372` but is **absent** from the LOCK test at
   `t2_genesis_selflock.py:378` (`if persisted and bounded and coherent and not
   decaying`). The committed LOCK criterion is therefore **weaker than prereg F1**,
   which requires **max|A| GROWS + coherent + bounded + persists** (`prereg §6 F1`).
   Queue: **add `grew` to the LOCK condition** to match F1. *Not fixed now* — it does
   not change the current result (no arm reaches LOCK regardless; and the §0.5 sech
   *does* satisfy `grew`, so adding it would not rescue the sech's bin — the binding
   gate is `coherent`/PLV, item 3).

3. **(escalated by §0.5) The `coherent`/PLV-gate in the LOCK condition is the binding
   defect.** `coherent = PLV ≥ 0.80 ∧ radpersist ≥ 0.50` (`t2_genesis_selflock.py:378`
   neighborhood) does **not** fire on a genuine self-focus (§0.5: sech PLV ≈ 0.53). Even
   F1-corrected (item 2), the sech would still bin UNRESOLVED on this gate. Queue for
   adjudication: does the ω_local-phasor PLV instrument need a redesign (e.g. an
   instantaneous-frequency / chirp-tolerant coherence metric) before *any* positive
   (TARGET-POSITIVE LOCK) could be read on `crystal_engine`? **This is the gate that
   makes the LOCK bin currently unreachable** — the auditor+Grant call, not the
   implementer's (Rule 15/16).

---

## 6. Reproduce

```
PYTHONPATH=src .venv/bin/python src/scripts/vol_1_foundations/t2_genesis_selflock.py --production
```

Outputs `t2_genesis_selflock_results.json` next to the driver (repo convention,
mirrors `cage_stiffening_wall_results.json`). The four-way arms are deterministic and
reproduce byte-identically; the **SECH positive control** (§0.5) is under the JSON key
`sech_positive_control` (box, per-amp records, `bins`, `all_lock`, `message`). `--smoke`
for CI budget. Canonical constants cross-check (`verify_constants`) runs before any
output and **aborts on a bad bench** (no output on a failed cross-check). `make verify`
passes.
