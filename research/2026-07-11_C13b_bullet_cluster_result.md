# C13b Bullet-Cluster Offset — Quantitative γ Run (RESULT)

**Status:** RESULT (quantitative run of the frozen γ branch). **Verdict: MISS — banked as a REAL negative.**
**Date:** 2026-07-11
**Governing prereg (FROZEN, untouched):** [`research/2026-05-17_C13b_bullet_cluster_prereg.md`](2026-05-17_C13b_bullet_cluster_prereg.md)
**Branch run:** (γ) — geometric/ponderomotive η_eff halo superposition (Grant-adjudicated 2026-05-17).
**Matrix row:** C13b-BULLET · **Driver:** [`src/scripts/vol_3_macroscopic/derive_bullet_cluster_offset.py`](../src/scripts/vol_3_macroscopic/derive_bullet_cluster_offset.py)
**Lane:** satellite orchestration; NO canonization in-lane (result doc + PR only; `dm-mechanism-unification.md` / `bullet-cluster.md` untouched — a gated follow-on after Grant rules).

---

## 0. Headline (truth-content first)

**Does the AVE ponderomotive/η_eff cluster mechanism DERIVE the Bullet-Cluster offset?**
**No. The offset is NOT lattice-derived — the outcome is SOURCE-FORK-CONDITIONAL on an *underived* choice, and
under the mechanism's own derived operator it MISSES.** The one free, un-derived degree of freedom is *what sources
the halo*:

- **Sourced by the mechanism's own operator + validated definition (→ MISS).** The η_eff kernel is a pointwise
  function of the local Newtonian field g_N (it acts on whatever mass is present), and its SPARC-validated
  galaxy-scale definition sources it from `M_disk = M_* + M_gas` (`multi-galaxy-validation.md:23`). In the Bullet
  Cluster the **gas is the dominant baryon** and sits at the collision center, so the superposed lensing peak lands
  **on the gas**: predicted sub-cluster lensing–gas offset **≈ 5 kpc (peak) / ≈ 70 kpc (mass-weighted centroid)** vs
  observed **150–194 kpc** → **Δ = −145 kpc (−4.8σ) on the peak measure; −80 kpc (−2.7σ) on the softest (centroid)
  measure** — predicted offset far too SMALL (lensing on the baryons), with the correct **negative** sign.
- **Sourced by the cluster leaf's *asserted-but-underived* stellar narrative (→ HIT).** `bullet-cluster.md:23,:27`
  and `dm-mechanism-unification.md:54` assert the halo "co-moves with the stellar source mass" (a small,
  collisionless fraction). That reading recovers the offset — predicted **196 kpc (peak)** — but it is a bare
  assertion the **corpus's own ledger grades "asserted, not derived … matched-by-construction … significant-gap
  band"** (`vol1/claim-quality.md:480`, solidity 0.40, "do not build on").

**The consensus-symmetric verdict is a MISS, banked as a REAL negative.** Crediting the stellar-only escape would hold
AVE to a *lower* standard than MOND — which is refused the same unmotivated escape and fails the Bullet Cluster
identically (Clowe+ 2006: the 8σ offset "cannot be explained with an alteration of the gravitational force law", and
η_eff is one). The honest bottom line: **the mechanism does not DERIVE the offset — it MISSES under its derived source
and only matches by an underived, fiat stellar assignment.**

**Kernel-independence (strengthens the negative; adversarial review 2026-07-11).** In the cluster core the Newtonian
field has g_N ≫ a₀ (g_N/a₀ ≈ 2–8 across R < 230 kpc), so the η_eff saturation kernel is **DORMANT** there
(`g_eff/g_N = 1.000`; it engages only at R ≳ 600 kpc — `bullet-cluster.md:28`: "cluster-scale strains are far below
saturation"). The peak LOCATION is therefore set by *linear superposition of ~Newtonian baryon mass*, **independent
of the AVE saturation kernel and radial law** — a Newtonian-null counterfactual (saturation disabled) reproduces the
identical verdict (H_baryon 5 kpc, H_star ~192 kpc), and the Gordon-1/r profile agrees. The MISS is thus more robust,
not less: it is the generic statement that a baryon-sourced lensing tracks the dominant baryon (the gas).

Nothing in Ax2/Ax4/η_eff makes a neutral, sub-dominant stellar mass out-source the dominant (also neutral) gas; the
stellar-source recovery is the leaf's fiat, not a derivation.

**Epistemic status:** the ponderomotive form does **not derive** the offset. Its outcome is source-fork-conditional on
an underived choice; under the derived operator it is a **clean quantitative miss**, and the escape that recovers the
offset is graded fiat by the corpus itself. This is the cluster sector's first quantitative exposure and it fails the
way MOND-class kernels are known to fail clusters — consistent with the handoff STAKES framing. Banked as a REAL
negative per the miss-ledger; **not** debugged toward a rescue.

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

1. **The prereg's α/β/γ gate is stale; Grant adjudicated (γ) on 2026-05-17.** The frozen prereg still defers the
   choice to Grant (`:38` "Needs Grant's physics-judgment call before solo derivation can proceed"; `:108` "Awaits
   Grant's physics-judgment call on (α)/(β)/(γ) before any solo derivation session"), but the corpus records the call
   as made: [`dm-mechanism-unification.md:54`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md)
   — "rewritten 2026-05-17 per Grant adjudication (γ)". Grant re-confirmed (γ) at this run's launch. **α/β are HALT if
   re-opened** (non-fireable, see P10). This run executes (γ) only.
2. **Provenance line-cite drift corrected (verify-before-cite).** The frozen prereg's ingredient cites have drifted
   against HEAD and are corrected here (prereg left untouched):
   - `boundary-trapping-test.md:11` → the `h_⊥ ∝ 1/r` form is at **`:15`** at HEAD (`:11` is prose/scope).
   - `einstein-lensing-deflection.md:13` → the `δ = 4GM/bc²` form is at **`:21`** at HEAD.
   - The canonical static profile is total-mass-sourced (Poisson δ³): [`gordon-optical-metric.md:25`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md)
     `−(c⁴/7G)∇²ε₁₁ = 4πMc²δ³(r)` → `ε₁₁ = 7GM/(c²r)` (`:33`); `h_⊥ = −ν_vac·ε₁₁` (leaf `:16`), with `ν_vac = 2/7`
     (value at [`transverse-refractive-index.md:12`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/transverse-refractive-index.md);
     composed index `n = 1 − h_⊥ = 1 + ν_vac·ε₁₁ > 1` at `:23`). The overall sign/normalization of `h_⊥` does not
     affect the peak location (an argmax of convergence *magnitude*).
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

> **Kernel-dormancy caveat (do not over-read causal agency into the kernel).** Although `a₀` and the η_eff kernel are
> lattice-derived, the kernel is **DORMANT in the peak region**: the cluster-core Newtonian field has g_N ≫ a₀
> (g_N/a₀ ≈ 2–8 across R < 230 kpc), so `g_eff/g_N = 1.000` there (it engages only at R ≳ 600 kpc). The peak
> **location** is therefore governed by *linear superposition of ~Newtonian baryon mass* (which baryon dominates +
> core scales), **not** by the saturation physics. The driver reproduces the identical verdict with saturation
> disabled (Newtonian null: H_baryon 5 kpc, H_star ~192 kpc) and with the Gordon-1/r profile — so the MISS is
> kernel- and radial-law-independent. The AVE-distinct saturation content matters for the cluster *mass-normalization*
> (the separate MOND cluster-mass deficit), not for the *offset* tested here.

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
  … significant-gap band" (solidity 0.40, "do not build on"). The (γ) adjudication resolved the *propagation framing*
  (static vs shockwave); it did **not** derive the source — it left the source in a **contradictory, asserted state**
  (`dm-mechanism-unification.md:54` "co-moves with the stellar source mass" vs `:57` "amplitude scales with baryonic
  mass"; `bullet-cluster.md:21` total vs `:23`/`:27` stellar). The cluster leaf's *majority prose* (items 2/3/5)
  leans **stellar** — i.e. canon leans toward the branch that recovers the offset — which only sharpens that the
  recovery rides on an **underived, fiat** assignment, not a derivation.
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

**MISS (source-fork-conditional) — banked as a REAL negative.** The ponderomotive/η_eff cluster mechanism (limb (ii)),
run quantitatively for the first time, does **not derive** the offset: the outcome depends on an *underived* source
assignment. Sourced by the mechanism's own operator + its SPARC-validated `M_*+M_gas` definition, the lensing peak
lands on the (dominant) gas → offset ≈ 5–70 kpc vs observed 150–194 kpc (8σ) → **MISS** (Δ = −145 kpc, −4.8σ). Sourced
by the leaf's asserted-but-underived stellar narrative → HIT (196 kpc). Because the source is underived — graded
"matched-by-construction … significant-gap band" (solidity 0.40) by the corpus's own ledger — and because crediting the
stellar-only escape would hold AVE below the standard MOND is held to (Clowe+ 2006: the offset "cannot be explained
with an alteration of the gravitational force law"), **the consensus-symmetric verdict is a MISS**. It is the canonical
MOND-class cluster failure, and (per the kernel-dormancy caveat) it is *kernel- and radial-law-independent* — the
generic statement that a baryon-sourced lensing tracks the dominant baryon. The qualitative "~150 kpc match" in the
corpus was matched-by-construction (halo placed on the galaxies by fiat); the quantitative test removes that fiat and
the derived mechanism misses.

**No canonization in-lane.** `dm-mechanism-unification.md` and `bullet-cluster.md` are untouched; §6's re-scope and the
crux question are handed to Grant for a gated follow-on.

---

### Provenance
- Frozen prereg (untouched): `research/2026-05-17_C13b_bullet_cluster_prereg.md`.
- Corpus crux audit (grep-confirmed, this run): findings summarized in §6; loci `bullet-cluster.md:21,23,27`,
  `axiom-definitions.md:21`, `effective-galactic-acceleration-mond.md:15`, `multi-galaxy-validation.md:23`,
  `gordon-optical-metric.md:25,33`, `transverse-refractive-index.md:12,16,23`, `einstein-lensing-deflection.md:14,21`,
  `boundary-trapping-test.md:15`, `vol1/claim-quality.md:480`, `dm-mechanism-unification.md:54,179`.
- Observational geometry retrieved + cross-checked (this run): Clowe+ 2006 (ApJ 648 L109 / astro-ph/0608407);
  Bradač+ 2006 (ApJ 652 937); Markevitch 2006 (astro-ph/0511345); Springel & Farrar 2007 (MNRAS 380 911, frame
  validation 720 kpc); Paraficz+ 2016 (A&A 594 A121); JWST "High-Caliber View" 2025 (arXiv:2503.21870).
- Driver (reproduced): `src/scripts/vol_3_macroscopic/derive_bullet_cluster_offset.py`; figure
  `assets/sim_outputs/bullet_cluster_offset_gamma.png` (regenerable; gitignored).
- **Adversarial review (2026-07-11, PR #645, 3 lenses + per-finding refute-pass):** 5 findings CONFIRMED, all
  MINOR / EVIDENCE-VOID (repair-and-bank) — the MISS verdict survives every lens and is confirmed *kernel-independent*.
  Repairs applied this run: (1) kernel-dormancy disclosure + Newtonian-null counterfactual (finding on over-attributing
  agency to the dormant η_eff kernel); (2) source-fork-conditional framing lifted into §0/§8 (was read as unconditional);
  (3) `h_⊥ = −ν_vac·ε₁₁` sign + `ν_vac` value-cite corrected to `transverse-refractive-index.md:12`; (4) removed
  quote-marks on the non-verbatim "awaits Grant's call" paraphrase; (5) §6 source-state reworded to "contradictory,
  asserted" (canon majority-prose leans stellar). The one MAJOR was DOWNGRADED to MINOR (consensus-symmetric call = MISS).
