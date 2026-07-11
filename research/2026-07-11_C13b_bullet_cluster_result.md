# C13b Bullet-Cluster Offset — Quantitative γ Run (RESULT)

**Status:** RESULT (quantitative run of the frozen γ branch). **Verdict: MISS — banked as a REAL negative.**
**Date:** 2026-07-11
**Governing prereg (FROZEN, untouched):** [`research/2026-05-17_C13b_bullet_cluster_prereg.md`](2026-05-17_C13b_bullet_cluster_prereg.md)
**Branch run:** (γ) — geometric/ponderomotive η_eff halo superposition (Grant-adjudicated 2026-05-17).
**Matrix row:** C13b-BULLET · **Driver:** [`src/scripts/vol_3_macroscopic/derive_bullet_cluster_offset.py`](../src/scripts/vol_3_macroscopic/derive_bullet_cluster_offset.py)
**Lane:** satellite orchestration; NO canonization in-lane (result doc + PR only; `dm-mechanism-unification.md` / `bullet-cluster.md` untouched — a gated follow-on after Grant rules).

---

## 0. Headline (truth-content first)

**Is the AVE ponderomotive/η_eff cluster mechanism, run quantitatively against the Bullet Cluster, TRUE?**
**No — it misses, and the miss is structural, not a fit-tune.** Sourced honestly (halo amplitude ∝ the local
baryonic mass, exactly as its own SPARC-validated galaxy-scale definition prescribes, `multi-galaxy-validation.md:23`
uses `M_disk = M_* + M_gas`), the superposed η_eff lensing peak lands **on the gas** (the dominant baryon), giving a
predicted sub-cluster lensing–gas offset of **≈ 5 kpc (peak) / ≈ 70 kpc (mass-weighted centroid)** against an observed
**150–194 kpc**. **Δ = −145 kpc (−4.8σ) on the peak measure; −80 kpc (−2.7σ) on the softest (centroid) measure** —
predicted offset far too SMALL, i.e. AVE predicts lensing tracks the baryons, and the Bullet Cluster's entire
significance is that it does **not**.

The **only** way to recover the offset is to source the halo from the **stellar mass alone** (H_star → 196 kpc), but
that assignment is an **UNDERIVED ASSERTION** — the corpus's own claim-quality ledger already grades it
"asserted, not derived … matched-by-construction" ([`vol1/claim-quality.md:480`](../manuscript/ave-kb/vol1/claim-quality.md)),
and nothing in Ax2/Ax4/η_eff makes a neutral, sub-dominant stellar mass out-source the dominant gas.

**Epistemic status:** clean quantitative falsification of the ponderomotive form **as it is actually derived**. This is
the cluster sector's first quantitative exposure and it fails the way MOND-class kernels are known to fail clusters —
consistent with the handoff STAKES framing. Banked as a REAL negative per the miss-ledger; **not** debugged toward a
rescue.

---

## 1. Freeze-state verification (P9)

- The governing prereg [`2026-05-17_C13b_bullet_cluster_prereg.md:3`](2026-05-17_C13b_bullet_cluster_prereg.md) still reads
  **`Status: PREREG ONLY (no derivation performed)`** — grep-confirmed this run. It is **untouched** by this run.
- **No prior C13b result doc existed** (grep-confirmed: `research/` held only the prereg). This is the first run.
- **No engine/constants modernization was required.** The May-frozen API is intact and used as-is (grep-confirmed at
  HEAD `222d9809`): `A0_LATTICE` and `ave_saturation_acceleration` in `ave.regime_3_saturated.galactic_rotation`;
  `G`, `M_SUN`, `C_0`, `H_INFINITY` in `ave.core.constants`. Because nothing was modernized, the freeze-by-push
  ordering (amendment before amended code) is trivially satisfied — there is no amended frozen code; the driver is
  new work, and the original prereg stays frozen.

## 2. Amendment context (recorded, NOT written into the frozen prereg)

1. **The prereg's α/β/γ gate is stale; Grant adjudicated (γ) on 2026-05-17.** The frozen prereg (`:38`, `:108`) says it
   "awaits Grant's call", but the corpus records the call as made: [`dm-mechanism-unification.md:54`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md)
   — "rewritten 2026-05-17 per Grant adjudication (γ)". Grant re-confirmed (γ) at this run's launch. **α/β are HALT if
   re-opened** (non-fireable, see P10). This run executes (γ) only.
2. **Provenance line-cite drift corrected (verify-before-cite).** The frozen prereg's ingredient cites have drifted
   against HEAD and are corrected here (prereg left untouched):
   - `boundary-trapping-test.md:11` → the `h_⊥ ∝ 1/r` form is at **`:15`** at HEAD (`:11` is prose/scope).
   - `einstein-lensing-deflection.md:13` → the `δ = 4GM/bc²` form is at **`:21`** at HEAD.
   - The canonical static profile is total-mass-sourced (Poisson δ³): [`gordon-optical-metric.md:25`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md)
     `−(c⁴/7G)∇²ε₁₁ = 4πMc²δ³(r)` → `ε₁₁ = 7GM/(c²r)` (`:33`); `h_⊥ = ν_vac·ε₁₁`, `ν_vac = 2/7`
     ([`transverse-refractive-index.md:23`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/transverse-refractive-index.md)).
   - `δ = 4GM/bc²` is a **consistency-check with GR, not an AVE-distinct emergence** ([`einstein-lensing-deflection.md:14`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/einstein-lensing-deflection.md));
     it is used here for the profile *form*, not claimed as an AVE-distinct prediction.

## 3. P10 — which branches can genuinely fire

| Branch | Fireable under the current engine? | Basis |
|---|---|---|
| **(γ)** geometric/ponderomotive η_eff halo | **YES — fires** | The prediction is a computed field **argmax** of the superposed η_eff halos (this run). Not a kinematic prescription. |
| (α) propagating sub-luminal TT shockwave | **NO — superseded + non-fireable** | Missing source term / propagation eq / cluster-scale dispersion (prereg `:78-81`, all ✗). Superseded by the (γ) adjudication. |
| (β) standing TT-mode | **NO — superseded + non-fireable** | Missing dynamic-Gordon-strain→offset machinery (prereg `:81`, ✗). Superseded by the (γ) adjudication. |

**Driver-honesty check (P10 HALT resolved).** The pre-existing `simulate_bullet_cluster_fdtd.py` **meets the P10 HALT
condition**: it places 100% of each cluster's mass at a single point advanced at hardcoded velocities (`:71,:85,:100-101`),
models **no gas component**, and therefore never computes a halo-vs-gas offset — its "offset" is a prescribed kinematic
separation. Rather than HALT, this run **resolves** the condition by building a driver that models the honest
two-component (gas + stars) baryonic source and extracts the offset as a genuine field peak. (The old driver is left
untouched; it remains a qualitative visualization. Its rename/scope-note is a separate cleanup, out of scope here.)

## 4. Method (what is lattice-derived vs imported)

**LATTICE-DERIVED (the prediction):**
- η_eff halo profile: `g_eff = g_N + √(g_N·a₀)·√(1 − g_N/a₀)` via `ave_saturation_acceleration`
  ([`effective-galactic-acceleration-mond.md:15`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/effective-galactic-acceleration-mond.md)).
  Projected effective lensing surface density Σ_eff(R) built from `M_eff(r) = g_eff·r²/G → ρ_eff → Abel projection`.
- `a₀ = A0_LATTICE = c·H_∞/(2π) = 1.071912×10⁻¹⁰ m/s²` (no telescope parameter; `constants.py` full-double, house-rule (a)).
- **Linear superposition** of the static halos (Ax1 + Ax4 linear regime; leaf [`bullet-cluster.md:28`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/bullet-cluster.md)).
- Cross-check profile: static Gordon 1/r halo (`h_⊥ ∝ M/r`), a different radial law, to test robustness of the
  peak-location verdict.
- `G, M_SUN, C_0, H_INFINITY` imported from `constants.py` (never retyped; house-rule (a)).

**IMPORTED-OBSERVATIONAL (the geometry the prediction runs on — legitimately imported, tagged):**

| Quantity | Value (frame: origin = bullet gas peak; +x West; +y North) | Source |
|---|---|---|
| bullet (sub) X-ray gas peak | (0, 0) kpc | Clowe+ 2006 (ApJ 648 L109) |
| bullet (sub) mass/galaxy peak (8σ lensing) | (+193, −22) kpc | Clowe+ 2006 |
| main X-ray gas peak | (−334, −26) kpc | Clowe+ 2006 |
| main mass/galaxy peak (12σ lensing) | (−523, −116) kpc | Clowe+ 2006 |
| **frame validation** | main↔sub mass-peak sep = **722 kpc** vs lit. **720 kpc** | Springel & Farrar 2007 (MNRAS 380 911) |
| stellar mass (core, ~11% of R<250 kpc lensing) | M_*,sub ≈ 2.2×10¹³, M_*,main ≈ 2.75×10¹³ M_⊙ | Paraficz+ 2016 (A&A 594 A121) |
| M_gas/M_* (cluster-wide, gas-dominant) | ≈ 5–7 | Clowe+ 2006 abstract ("plasma … dominant baryonic component") |
| M_gas/M_* (stripped-core census, R<250 kpc) | ≈ 0.8 (gas 9% vs stars 11%; gas stripped OUT) | Paraficz+ 2016 |
| bullet gas core (compact, dense) | ~80 kpc; main ICM β-core θ_c=112.5″≈300–500 kpc; galaxy core ~50 kpc | Paraficz+ 2016; cluster-typical |
| **observed sub lensing–gas offset (ANCHOR)** | **~150 kpc** (dense-tip, along-axis) … **194 kpc** (gas-centroid frame) | Clowe+ 2006; JWST 2025 (arXiv:2503.21870) |
| offset significance | **8σ** (total-mass vs baryonic-mass centroid) | Clowe+ 2006 |

Absolute mass normalization is irrelevant to the **peak location** (only per-subcluster ratios, positions, and core
scales matter); this is why the result is reported as a function of M_gas/M_* rather than an absolute mass fit.

## 5. Results — predicted sub-cluster lensing–gas offset

**Primary (η_eff profile, cluster-wide gas/star = 5), reproduced this run:**

| Hypothesis (halo source) | predicted offset — PEAK | predicted offset — centroid | Δ vs 150 kpc (peak) | verdict |
|---|---|---|---|---|
| **H_baryon** (∝ total baryons; gas-dominated) | **5 kpc** (on the gas) | 70 kpc | **−145 ± 30 kpc (−4.8σ)** | **MISS** |
| H_star (∝ stellar mass only) | 196 kpc (on the galaxies) | 136 kpc | +46 ± 30 kpc (+1.5σ) | recovers offset — but underived |

**Robustness — the offset is governed entirely by the star-vs-gas source ratio (η_eff, peak measure):**

| M_gas/M_* | H_baryon peak-offset | reading |
|---|---|---|
| 0.8 (stripped-core census) | 196 kpc | stars locally dominate → peak on stars |
| 2.0 | 196 kpc | stars still win |
| **3.0** | **7 kpc** | **gas dominates → peak collapses onto gas** |
| 5.0 | 5 kpc | MISS |
| 7.0 | 5 kpc | MISS |

There is a **sharp transition at M_gas/M_* ≈ 2–3**: once the halo is sourced by the gas-dominant baryon budget (the
cluster-wide reality, and the SPARC-validated `M_*+M_gas` prescription), the predicted lensing peak snaps onto the gas
and the offset collapses. **The entire pass/fail hinges on the source ratio — the exact quantity the corpus leaves
underived.**

**Profile robustness:** the Gordon 1/r cross-check gives H_baryon peak-offset = 0 kpc, H_star = 196 kpc — same verdict,
so the MISS is not an artifact of the η_eff radial law.

**Precision (house-rule (d)/(e)):** predicted H_baryon peak-offset = 5 kpc; observed = 150 kpc (canonical dense-tip)
to 194 kpc (Clowe gas-centroid). **Δ = −145 kpc (−4.8σ) against the 150 kpc anchor; −189 kpc against the 194 kpc
in-frame value.** The residual is **negative** (predicted offset too small) and exceeds the ~30 kpc anchor uncertainty
by ≳4×; the softest measure (centroid, 70 kpc) still gives **Δ = −80 kpc (−2.7σ)**. No measure reaches the observed
band. (The word "match" is not used for H_baryon: the σ forbids it.)

## 6. The load-bearing crux (flag-don't-fix) — routed to Grant

The whole result reduces to one physics question the corpus does **not** answer: **does the ponderomotive/η_eff halo
track the (gas-dominated) total baryons, or the stars only?**

- The leaf is **internally contradictory**: [`bullet-cluster.md:21`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/bullet-cluster.md)
  sources the halo from "each cluster's mass (stars + … baryonic content)" (→ total, gas-dominated); `:23`/`:27`
  restrict it to "stars … a small fraction of the cluster's mass-by-weight". Nowhere is "stars out-source gas" derived.
- **Ax2 (TKI) gives no basis for it:** Ax2 couples **charge** to strain (`[Q]≡[L]`, [`axiom-definitions.md:21`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md));
  clusters are neutral and stars carry no net charge, so Ax2 offers no route by which neutral stellar mass sources a
  halo that neutral gas does not.
- **The η_eff kernel is a pointwise function of local g_N**, sourced by whatever mass is present; its own
  SPARC-validated galaxy-scale definition uses **`M_disk = M_* + M_gas`** (total baryons, `multi-galaxy-validation.md:23`).
  Applied to a cluster where the gas is the dominant baryon at the collision center, the enhancement peaks on the gas.
- **The corpus already concedes it:** [`vol1/claim-quality.md:480`](../manuscript/ave-kb/vol1/claim-quality.md) grades
  this leaf "the AVE-distinct discriminator … is asserted, not derived, and the ~150 kpc offset is matched-by-construction
  … significant-gap band". The (γ) adjudication resolved the *propagation framing* (static vs shockwave), **not** the
  source question — which was never on the adjudication table.
- **The observation forecloses the force-law escape.** Clowe+ 2006 abstract (verbatim, retrieved this run): *"An 8σ
  significance spatial offset of the center of the total mass from the center of the baryonic mass peaks **cannot be
  explained with an alteration of the gravitational force law**."* AVE η_eff **is** a baryon-sourced alteration of the
  effective force law. This is the literature stating directly that this mechanism class fails here.

**Two questions for Grant (the gated follow-on turns on these):**
1. *Physically:* in your substrate picture, why would a neutral star source a lensing halo that neutral gas (the
   dominant baryon, sitting at the collision center) does not — given η_eff is a function of local g_N and its own
   galaxy-scale validation sources `M_* + M_gas`? The entire γ offset lives or dies on this one sentence.
2. *Bookkeeping:* accept the MISS as the honest quantitative status of limb (ii) and re-scope
   `dm-mechanism-unification.md:19,:62,:154` ("qualitatively confirmed ~150 kpc") to "**quantitatively MISSES under the
   derived (gas-sourced) halo**; recovery requires an underived stars-only source" — in a gated follow-on? (Not done
   in-lane.)

## 7. P11 sabotage receipt (gates proven fireable)

All reproduced this run (assertions in-driver):

- **[A] zero the gas-halo amplitude (M_gas→0):** H_baryon peak-offset **5 → 196 kpc** (jumps to the H_star value) —
  proves the gas amplitude is precisely what drags the predicted peak onto the gas (the cause of the miss).
- **[B] move the stellar halos onto the gas peaks:** H_star peak-offset **196 → 5 kpc** (collapses) — proves the offset
  is read from the input geometry via the field peak, **not** hardcoded to 150/194.
- **[C] zero all halo amplitudes:** `max(κ) = 0` — no field, no signal.

The prediction is a genuine function of the halo physics and the geometry; the gate is not rigged to pass.

## 8. Verdict

**MISS — banked as a REAL negative.** The ponderomotive/η_eff cluster mechanism (limb (ii)), run quantitatively for the
first time, predicts the lensing peak on the gas (offset ≈ 5–70 kpc) where the data place it 150–194 kpc away on the
galaxies (8σ). The failure is the canonical MOND-class cluster failure and is **structural** — it follows from sourcing
the halo by the (gas-dominated) baryons, which is what the mechanism's own SPARC-validated definition prescribes. The
qualitative "~150 kpc match" in the corpus was matched-by-construction (it placed the halo on the galaxies by fiat); the
quantitative test removes that fiat and the match does not survive. The lone escape (stars-only source) is an underived
assertion the corpus itself grades as such and that Clowe+ 2006 explicitly rules out for any force-law modification.

**No canonization in-lane.** `dm-mechanism-unification.md` and `bullet-cluster.md` are untouched; §6's re-scope and the
crux question are handed to Grant for a gated follow-on.

---

### Provenance
- Frozen prereg (untouched): `research/2026-05-17_C13b_bullet_cluster_prereg.md`.
- Corpus crux audit (grep-confirmed, this run): findings summarized in §6; loci `bullet-cluster.md:21,23,27`,
  `axiom-definitions.md:21`, `effective-galactic-acceleration-mond.md:15`, `multi-galaxy-validation.md:23`,
  `gordon-optical-metric.md:25,33`, `transverse-refractive-index.md:23`, `einstein-lensing-deflection.md:14,21`,
  `boundary-trapping-test.md:15`, `vol1/claim-quality.md:480`, `dm-mechanism-unification.md:54,179`.
- Observational geometry retrieved + cross-checked (this run): Clowe+ 2006 (ApJ 648 L109 / astro-ph/0608407);
  Bradač+ 2006 (ApJ 652 937); Markevitch 2006 (astro-ph/0511345); Springel & Farrar 2007 (MNRAS 380 911, frame
  validation 720 kpc); Paraficz+ 2016 (A&A 594 A121); JWST "High-Caliber View" 2025 (arXiv:2503.21870).
- Driver (reproduced): `src/scripts/vol_3_macroscopic/derive_bullet_cluster_offset.py`; figure
  `assets/sim_outputs/bullet_cluster_offset_gamma.png` (regenerable; gitignored).
