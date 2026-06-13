# CVR EE-Sweep + BH-Extreme Documentation — Orchestrator Epic

> **Role:** documentation orchestrator (producer). The read-only auditor lane SPECs + AUDITS
> (`AUDITOR_STATE.md` workspace root); this lane PRODUCES on a branch; Grant merges (protected main).
> **Branch:** `analysis/2026-06-13-cvr-ee-sweep-doc` (fresh worktree off clean `origin/main` 79fae7ed).
> **Started:** 2026-06-13.

## Mission

Document the EE/CVR circuit-analysis work + the lattice-extreme↔BH rationality test into the KB +
Vol 9 LaTeX, every claim DERIVED/STATED/CONSISTENCY/AVE-DISTINCT-tagged and skill-disciplined, built on
the **corrected magnetic branch** (electron = `μ_eff→0`, `Z→0`, `Γ=−1`; NOT the superseded `Z→∞`).

## Skill-selection plan (60-sec, per feedback_skill_selection_planning)

| Phase | Primary skills (applied) | Why |
|---|---|---|
| 0 orient/brief | `ave-canonical-leaf-pull`, `verify-before-cite`, `ave-handoff-canonical-locale` | enumerate the VCA/BH canon before producing; brief lands here not ~/.claude/plans |
| 1 scripts+figures | `ave-canonical-source`, `substrate-native-check`, `ave-driver-script-honesty`, `ave-analytical-tool-selection` | import constants (never hard-code); H(s) is the constitutive-law object, not an SM default; every curve from the kernel |
| 2 KB leaf-set | `ave-evidence-framing-discipline`, `consistency-vs-emergence`, `ave-discrimination-check`, `verify-before-cite`, `phase-space-coordinate-check` | DERIVED vs STATED vs CONSISTENCY; |Γ|²=1−α is the AVE-distinct line, ringdown-match is consistency; phasor coords not lattice-Cartesian |
| 3 BH leaf + clm-ir8h78 | `ave-walk-back`, `verify-before-cite`, `ave-discrimination-check` | the 7GM/2GM reconciliation is a walk-back (needs Grant greenlight); find BOTH halves before reconciling |
| 4 Vol 9 LaTeX | `verify-before-cite`, `ave-evidence-framing-discipline` | datasheet sections thread into existing ch4/ch5/ch10/ch12/ch14; cite computed figures |
| 5 toolkit + translation §4.5 | `ave-ee-first-mapping` (Step 6b maintenance), `verify-before-cite` | flip the ⚠/✗ rows the new leaves close |
| 6 validation | `ave-driver-script-honesty`, `verify-before-cite` | re-run every figure; grep-confirm every citation; hand to auditor |

Retroactive-pass before commit if the applied-set drifts (per the skill).

## Verified substrate (grep-confirmed anchors — the producer's foundation)

- **Electron = magnetic branch (CANONICAL, already-correct on clean main):**
  `master-equation.md:78-79` (clm-lv3uw1): magnetic `μ_eff→0 → Z→0 → Γ=−1` (short, trapped knot, rest mass).
  Echoed at `translation-circuit.md:115`, `photon-ee-mapping.md` §2 (the resultbox at :42-48).
  The **electric branch** (`ε_eff→0, Z→∞, Γ=+1`, open) is **dielectric rupture — a different object**, NOT the electron.
  ch1 index already states: "Particle confinement | Γ = −1 at saturated boundary (Z_core → 0 Ω)".
- **α = 1/Q (DERIVED, two paths):** `theorem-3-1-q-factor.md:15,38` — `α⁻¹ = Q_tank = 4π³+π²+π = 137.036`;
  per-cycle leak = `1/Q = α` (:81). This is the H(s) pole's distance from the jω axis.
- **|Γ|² = 1−α (AVE-DISTINCT):** α is the hair Γ falls short of the unit circle (Thm 3.1' leak/cycle). The wall
  is NOT a perfect short — it leaks exactly α per cycle = the radiative linewidth.
- **Varactor / DC op-point:** `nonlinear-vacuum-capacitance.md`, `resonant-lc-solitons.md:29-39`,
  `translation-circuit.md:111-112` — `C_eff(A₀) = C₀/S(A₀)`, `S(A)=√(1−(A/A_yield)²)`, V_yield≈43.65 kV.
- **BH extreme:** `electron-bh-isomorphism.md` (clm-ir8h78) — horizon `r_sat = 7GM/c² = 3.5 r_s` (shear+bulk,
  `G_shear→0, c_bulk→0`); EM stays matched (`Γ_EM=0`, photons see GR). `ave-bh-horizon-area-theorem.md`
  (clm-law1ho) — area theorem from Ax 4. `constructive-destructive-paradox.md:15` (clm-ir8h78) — SAME exterior,
  inverted interior (electron constructive / BH destructive).
- **Canonical constants** (`src/ave/core/constants.py`): `Z_0`≈376.73 Ω (:98), `ALPHA` (:133),
  `L_NODE`=ħ/(m_e c) (:239), `XI_TOPO` (:273), `V_SNAP`≈511 kV (:400), `V_YIELD`=√α·V_snap≈43.65 kV (:409).
  `ALPHA_COLD_INV`=4π³+π²+π. `ω_C = c₀/ℓ_node ≈ 7.76e20 rad/s` (derive from primitives).

## H(s) spine (the central object — AUDITOR_STATE:33)

2×2 chiral transfer function. Pole pair at `s = −αω₀/2 ± jω_d`, `ω₀ = ω_C = c₀/ℓ_node`, `Q = 1/α`
(real part = −ω₀/2Q = the leak), `ω_d = ω₀√(1−1/4Q²)≈ω₀`. Bode: `Q=1/α`, `BW = αω₀ = ω₀/Q`.
Off-diagonal = winding handedness (`S_LR ≠ S_RL*` = parity-odd, the (2,3) winding). Built on DC op-point A₀
+ AC small-signal. All 6 views derive from this + the constitutive law.

## Carried flags (flag-don't-fix — do NOT silently resolve)

1. **SECTOR-ATTRIBUTION (AUDITOR_STATE:19 FLAG-2):** the electron's `Z→0/Γ=−1` wall has TWO corpus routes —
   **magnetic** (`μ_eff→0`; master-equation.md:78-79, clm-lv3uw1 — HANDOFF-MANDATED PRIMARY) vs **capacitive**
   (`C_eff→∞`; resonant-lc-solitons.md:29-39, clm-kezk9z). Both → Γ=−1; disagree on sector; no engine-validated
   trajectory distinguishes. **PRIMARY = magnetic; CARRY the capacitive route as the flagged co-attribution.**
   Do NOT edit resonant-lc-solitons.md (existing canonical leaf) — cross-link + flag for auditor.
2. **EXPONENT DEFECT (master_equation_fdtd.py:165):** code returns `n = S^0.25` but the in-code FLAG says
   physical `n = c₀/c_eff = S^0.5` (since c_eff²=c₀²/S). Engine Γ-from-n magnitudes UNDERSTATE wall depth.
   Carry on every n-derived curve: show both, flag the engine understatement. FIX = physics-review item (Grant).
3. **S_min CLIP:** the kernel clips at S_min (graft-v2 floor) — magnitudes apparatus-capped, not physical wall depth.
4. **clm-ir8h78 RECONCILIATION (PENDING — Phase 3):** auditor flagged `7GM/c²(shear+bulk)` vs
   `2GM/c²(r_s, dielectric-rupture)` under ONE claim-id, "resolved 2026-06-06" but dielectric leaf unreconciled.
   The 7GM is consistent across ch15 leaves; the 2GM appears only as the GR reference scale in compactness/
   photon-sphere formulae. **MUST FIND the actual 2GM-dielectric-rupture horizon statement (grep hunt) before
   reconciling** — likely a channel-subscript (shear+bulk horizon vs EM photons-see-GR) distinction. Goes through
   ave-walk-back → Grant greenlight.

## Discrimination ledger (ave-discrimination-check — tag every result)

- **CONSISTENCY (NOT AVE-distinct):** LC-tank → E=mc²; Q=1/α as α's Sommerfeld meaning (re-expression);
  ringdown 18/49 match; ω_C as definitional-given-primitives (Class C).
- **AVE-DISTINCT:** `|Γ|²=1−α` (wall falls short of unit circle by exactly α = measurable radiative leak);
  2×2 chiral S (`S_LR≠S_RL*` = winding handedness, parity-odd); pole at −αω₀/2 (radiative linewidth);
  BH echoes (Γ=−1 reflector vs GR absorption) + 2/7 compactness + Iron-Kα sub-peaks.
- **CHANNEL SPLIT (honor):** gravity = SYM detune (Z=Z₀ invariant, reflectionless, clocks slow) vs
  GW-shear-radiation (separate channel); electron = bulk-TIR; BH = shear+bulk. Every Z/Γ/speed carries a subscript.

## Production plan (dependency order)

- **P1 scripts+figures** (`src/scripts/vol_9_device/cvr_ee_sweep/`): H(s) spine + 6 views, canonical constants,
  deterministic, re-runnable. THE FOUNDATION (leaves+LaTeX cite the computed figures).
- **P2 KB leaf-set** (`vol4/circuit-theory/ch1`): cvr-transfer-function, cvr-dc-operating-point,
  cvr-reflection-smith, cvr-phasor-reactance, cvr-stability-eigenmode. One leaf per commit. Heavy cross-link to
  existing ch1 leaves (don't re-derive). Each fills a tracked translation-circuit §4.5 gap.
- **P3 BH-extreme leaf** (`vol3/cosmology/ch15`): the lattice-extreme↔BH rationality test (one kernel, two
  extremes: compression→electron/BH, rarefaction→cavitation) + clm-ir8h78 reconciliation (ave-walk-back).
- **P4 Vol 9 LaTeX**: CVR full circuit analysis + extreme-map sections threaded into datasheet ch4/ch5/ch10/
  ch12/ch14, computed figures.
- **P5 toolkit-index + translation-circuit §4.5**: CVR sweep as worked resonator instance; flip the H(s)/Smith/
  Nyquist/root-locus/autoresonance/I-Q rows (currently ⚠:181,189 / ✗:206-208).
- **P6 validation**: re-run all figures, verify-before-cite sweep, hand to auditor.

## Audit gates (acceptance — this lane satisfies; auditor verifies)

every figure re-runs+matches · DERIVED/STATED/CONSISTENCY/AVE-DISTINCT tags · H(s) poles ↔ Q=1/α ·
|Γ|²=1−α ↔ per-cycle leak · exponent-defect (S^0.5-vs-S^0.25) + S_min clip carried · magnetic branch (Z→0)
not Z→∞ · discrimination-check applied · gravity-vs-GW channel split honored · pure-AVE · Rule-11/12.

---

## COMPLETION + AUDITOR HANDOFF (2026-06-13)

**Status: P1–P6 COMPLETE.** Branch `analysis/2026-06-13-cvr-ee-sweep-doc` (worktree
`/Users/grantlindblom/AVE-staging/AVE-Core-cvrdoc-wt`), 5 commits off clean origin/main 79fae7ed, tree clean,
**unpushed** (Grant decides push/PR; main protected). Commit range `4c94cb4e..8d25eac5`.

| Phase | Commit | Deliverable |
|---|---|---|
| P1 | 4c94cb4e | scripts (`cvr_model.py` spine + `cvr_ee_sweep.py`) + 6 figures + metrics JSON |
| P2 | 5763fe4b | 5 KB leaves vol4/circuit-theory/ch1 (cvr-transfer-function/dc-operating-point/reflection-smith/phasor-reactance/stability-eigenmode) + ch1 index |
| P3 | 5df65fb6 | NEW ch15 leaf `lattice-extreme-bh-rationality.md` + clm-ir8h78 2GM/7GM channel walk-back (dielectric-rupture-event-horizon.md) + ch15 index |
| P4 | 17a40780 | Vol 9 datasheet: ch5 CVR section (3 hero figures) + ch14 extreme-map cross-link + graphicspath |
| P5 | 8d25eac5 | toolkit-index §2 worked-instance + translation-circuit §4.5 row flips (15✓/9⚠/2✗) |

**Audit gates — all satisfied (evidence):**
- ✅ figures re-run+match: re-run byte-identical metrics JSON AND PNGs (deterministic, tree clean)
- ✅ H(s) poles ↔ Q=1/α: `pole_real/ω₀ = −0.00364868 = −α/2` exactly (metrics JSON)
- ✅ |Γ|²=1−α ↔ leak: `0.9927026 = 1−α` exactly; the AVE-distinct radiative-gap-to-unit-circle result
- ✅ exponent defect (S^0.5 vs S^0.25) + S_min/A_cap clip: drawn on fig1, flagged in dc-operating-point §3 + datasheet warningbox
- ✅ magnetic branch (Z→0) not Z→∞: every leaf cites master-equation.md:78-79 (clm-lv3uw1); electric branch (Z→∞) named as the DIFFERENT object (dielectric rupture)
- ✅ discrimination-check: CONSISTENCY (ringdown 18/49, Q=1/α-as-Sommerfeld) vs AVE-DISTINCT (|Γ|²=1−α, chiral S_LR≠S_RL*, echoes, 2/7, Iron-Kα) tagged per leaf
- ✅ gravity-vs-GW channel split: the clm-ir8h78 reconciliation — EM/transverse 2GM (Z_EM=Z₀, Γ_EM=0) vs shear+bulk 7GM (Γ=−1)
- ✅ pure-AVE; Rule-12 (walk-back preserves the 2GM historical result, additive)
- ✅ Vol 9 compiles: latexmk exit 0, 197pp, 3 CVR figures confirmed embedded (main.fls INPUT lines)
- ✅ verify-kb-metadata PASS; verify-md-links clean for all 11 new/edited source files

**🔴 ONE LOAD-BEARING PHYSICS ADJUDICATION FOR GRANT (the only thing that needs his physics eye):**
the clm-ir8h78 walk-back direction. I resolved 2GM-vs-7GM as a CHANNEL split (EM/transverse horizon at r_s=2GM,
Γ_EM=0 no-reflection; shear+bulk rupture at r_sat=7GM, Γ=−1) — forced by the canonical three-impedance law
(electron-bh-isomorphism.md:24,26; existing-signatures.md:34), applied conservatively (KEEP-BOTH, Rule-12,
additive, trivially revertible). The 2026-06-06 pass explicitly DEFERRED this as "needs physics adjudication."
**Grant ratifies or redirects at merge.**

**Residual flags carried (NOT resolved — by design):** (1) sector-attribution μ→0 vs C→∞ (FLAG-2, both→Z₀√S,
magnetic PRIMARY); (2) chiral off-diagonal χ magnitude STATED (needs chiral-crystal engine); (3) the SYM-row
Γ=−1 mechanism-label sites (universal-saturation-kernel-catalog.md:53) — the separate follow-up adjudication,
NOT touched here; (4) autoresonance self-lock still ✗ (only the eigenmode structure mapped).

**Auditor: verify via** — re-run `PYTHONPATH=$PWD/src python src/scripts/vol_9_device/cvr_ee_sweep/cvr_ee_sweep.py`
(figures+metrics regenerate byte-identical); `make verify-kb-metadata` + `make verify-md-links`; spot-check the
DERIVED/STATED tags against claim-quality (clm-rtdmsn/lv3uw1/kezk9z/eemap1/ir8h78/law1ho).
