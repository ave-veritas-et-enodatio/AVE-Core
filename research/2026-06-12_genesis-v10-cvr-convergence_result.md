# Genesis v10 — CVR Convergence Result (PRODUCTION — 2026-06-12)

> **REGIME QUARANTINE (`_POST_RUPTURE`):** Production `max(A²) ≈ 15–22` on srs cells — post-rupture class per A-027. **Exclude** from D1 framing and snap/IC load-bearing adjudication (`_orchestration/2026-06-12_loop-gap-orchestration-plan.md` §3). CVR-SET = **reactive under drive**; snap-OFF and Ω-free ablations match ON — **not bin-isolating**.

> **Prereg:** `research/2026-06-12_genesis-v10-cvr-convergence_prereg_FROZEN.md`
> **Engine class:** discrete srs TLM + Op14/Op3 + **rate-gated snap** + **tri-channel χ** + **Ω_freeze IC**
> **Run class:** **PRODUCTION** — P6 L=10, 8000-node srs cells; diamond L=10 (250 nodes);
> amp `{0.25, 0.5}` on four-cell grid; χ sweep `{0, 0.25, 0.5, 1.0}`; snap/Op3/Op14/Ω-free ablations.
> **Driver:** `python src/scripts/vol_1_foundations/chiral_lattice_v10_genesis.py` (no `--smoke`).
> **Wall time:** ~42 min.

## Implementation

| Artifact | Path |
|----------|------|
| v10 integrator | `src/ave/core/chiral_lattice_v10.py` |
| Tests | `src/tests/test_chiral_lattice_v10.py` |
| Driver | `src/scripts/vol_1_foundations/chiral_lattice_v10_genesis.py` |
| JSON (local, gitignored) | `assets/sim_outputs/genesis_v10_cvr_convergence.json` |
| Log | `assets/sim_outputs/genesis_v10_production.log` |

**Platform notes:** `κ_chiral = 0` throughout. Snap fires on yield crossing with equal
χ on EM/shear/bulk. Ω_freeze IC ON by default; Ω-free ablation cell included.

---

## P6 — genesis-by-precursor (production cells)

Best bin per cell (amp ranking as driver):

| Cell | Best amp | Bin | plateau % | e_driveoff | θ concordant | E_diss,snap |
|------|----------|-----|-----------|------------|--------------|-------------|
| srs-R:+z | 0.5 | **CVR-SET** | 0.25 | 0.505 | yes | 3516.5 |
| srs-R:-z | 0.25 | **TRANSIENT** | 0.06 | 0.493 | no | 3148.6 |
| srs-L:+z | 0.5 | **CVR-SET** | 0.12 | 0.505 | yes | 3564.7 |
| srs-L:-z | 0.25 | **TRANSIENT** | 0.33 | 0.493 | no | 3167.3 |
| diamond:+z | 0.25 | SET-ACHIRAL | 27.48 | 1.000 | no | 111.7 |
| diamond:-z | 0.25 | SET-ACHIRAL | 27.48 | 1.000 | no | 111.7 |

**P6 any CVR-SET:** **True** (2/4 srs cells at +z arms).

**P6-C:** Diamond \|Δθ\| / srs max = **1.7%** — achiral null satisfied (≤ 5%). −z arms fail
θ concordance (A2 direction sensitivity preserved).

**Matched baseline (prereg §5):**

| Control | e_driveoff |
|---------|------------|
| srs-R:+z (snap+IC ON) | **0.505** |
| snap-OFF | 0.515 |
| Ω-free IC | 0.506 |
| Op3-OFF | 0.517 |
| Op14-OFF | 0.517 |
| diamond | 1.000 |

**structure_driven_2x = FAIL** — srs snap+IC does **not** exceed any control by ≥2× on energy
retention. Snap-OFF and Ω-free ablations **match or beat** the ON arm.

**Ablation reads:**
- **snap-OFF:** still **CVR-SET** at e_ret=0.515 — snap is **not uniquely load-bearing** for bin label at this amp.
- **Ω-free:** still **CVR-SET** at e_ret=0.506 — Ω_freeze IC does **not** gate CVR-SET assignment.
- **Op3-OFF / Op14-OFF:** SET-ACHIRAL with higher e_ret (~0.517) — reactive trap without θ concordance.

**Saturation:** `max(A²)` ≈ 15–22 on srs cells; deep past yield. Runs are post-rupture class per A-027.

---

## P6-χ — snap sweep (srs-R:+z, amp=0.25)

| χ | E_diss,snap | e_driveoff | Bin |
|---|-------------|------------|-----|
| 0.0 | 0.0 | 0.514 | SET-ACHIRAL |
| 0.25 | 1355.6 | 0.505 | SET-ACHIRAL |
| 0.5 | 3148.6 | 0.493 | TRANSIENT |
| 1.0 | 12995.5 | 0.438 | TRANSIENT |

- **P6-χ-MONO:** **PASS** — E_diss,snap non-decreasing with χ.
- **P6-χ-RET vs v9:** **PASS** — χ=0 arm e_ret=0.514 ≥ v9 Phase-2 best (0.514); χ=0.25 also ≥0.505.

Higher χ **increases** one-way dissipation but **degrades** drive-off retention (0.438 at χ=1).

---

## Hypothesis ledger

| Hypothesis | Verdict | Note |
|------------|---------|------|
| **H10** (snap enables set leg) | **WEAKENED** | P6-χ gates pass, but matched-baseline 2× fails; snap-OFF ≥ snap-ON retention |
| **H11** (Ω_freeze IC biases chirality) | **INCONCLUSIVE** | Ω-free still CVR-SET; θ concordance not isolated to IC arm |
| **H12** (CVR-SET conjunction) | **PARTIAL** | 2/4 cells CVR-SET; −z arms TRANSIENT; promotion blocked by baseline + ablations |

---

## Honest closure (Rule 11 + prereg §7)

| Combination | Reading |
|-------------|---------|
| P6 any CVR-SET + structure_driven_2x FAIL | **Do not promote BIN-G / genesis** — same honest closure as v9 Phase-2 |
| snap-OFF still CVR-SET | v10 snap leg is **diagnostic**, not bin-isolating at production depth |
| Ω-free still CVR-SET | D5 IC is **not** load-bearing for CVR-SET label on this grid |
| Lower plateau % vs v9 | amp=0.5 winners localize more weakly (0.12–0.25%) than v9 amp=0.25 (1.5–1.8%) |

**Production verdict:**
- **P6 machinery: EXECUTES** — snap ledger, χ sweep, IC/ablation grid all land.
- **P6 genesis: INCONCLUSIVE** — partial CVR-SET on +z enantiomorphs only; **matched baseline fails**;
  **snap and Ω-free ablations do not falsify** the ON-arm bin. Report as **partial precursor localization
  under snap-equipped integrator**, not CVR-SET genesis promotion.
- **LOOP GAP:** unchanged — Ω_freeze IC and snap do not close the constitutive loop (see
  `manuscript/ave-kb/common/substrate-hysteresis-index.md` §5b).

---

## Next

1. Orchestration: fold v10 honest closure into CVR / lattice epic (no corpus promotion).
2. Optional: amp=0.25-only rerun for apples-to-apples v9 plateau comparison.
3. Apparatus-floor branch (`analysis/2026-06-10-apparatus-floors`) still gates any leak→α attribution.
