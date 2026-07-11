# Handoff brief — C13B BULLET-CLUSTER RUN satellite (2026-07-11)

**Launch:** Grant launches this himself and picks the model + effort. **This is an ENGINE / DERIVATION arc**
(a quantitative astro-comparison run of a frozen prereg) — **recommend a strong model for the derivation lane.**

**SECTOR / REGIME / PHASE-STATE (the frame this run reasons in).** Macroscopic gravity / dark-sector. The
load-bearing object is a **ponderomotive substrate-strain halo** (limb (ii) of the dm-sector unification) —
a **static, geometric** Axiom-2 (TKI) + Axiom-4 (saturation) strain field co-moving with the stellar source
mass, read as lensing through the **Gordon optical metric** (transverse index `n = 1 − h_⊥`). Regime = the
long-wavelength linear regime (`λ ≫` atomic scale), where halos pass ballistically and the atomic-scale gas
decouples. This is **NOT** the Vol-1-Ch4 TT-shockwave picture (see the adjudication note below).

**Standing stack (applies throughout):** pure-AVE-corpus · only-Grant-merges ·
`[DO-NOT-MERGE][REVIEW: pending-orchestrator]` PR title · KEEP-BOTH · incremental commits · self-isolate in a
throwaway worktree (do not touch the main checkout) · verify-before-cite (LaTeX-aware greps) · backtick-pointer
cites · trailer `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.

---

## MISSION

Execute the **frozen** Bullet-Cluster offset prereg `research/2026-05-17_C13b_bullet_cluster_prereg.md`
(frozen 2026-05-17, **NEVER RUN**). **Verify its exact frozen content and freeze state first** (open the file,
confirm the `Status: PREREG ONLY (no derivation performed)` header, confirm no result doc exists). The prereg's
branch definitions are quoted verbatim in the next section — **re-verify them against the file before acting.**

**The corpus context this run is the test of.** The dm-sector unification's cluster mechanism —
`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md:52-64` (§3, limb (ii), the
ponderomotive substrate-strain halo) — currently rests on a **QUALITATIVE single-cluster geometric match**,
with its quantitative test explicitly pending:

> `:64` — "**Empirical status (2026-05-17)**: Qualitatively confirmed via single-cluster geometric match.
> Quantitative cross-cluster lensing-vs-baryon correlation test pending engineering work (SLOAN + HST +
> Chandra cross-correlation across N merging-cluster systems per matrix C13b row)."

**This run is that quantitative test.**

---

## ★ FROZEN PREREG — VERBATIM BRANCH DEFINITIONS (re-verify against the file)

The frozen prereg is a **physics-judgment fork**: it derives no number and offers **three interpretations**
(α / β / γ) of the bullet-cluster offset, each a distinct derivation path. Its verbatim branch summaries
(`research/2026-05-17_C13b_bullet_cluster_prereg.md:34-36`):

> **(α) Propagating sub-luminal**: corpus needs a κ-coupling or Gordon-metric-drag mechanism that reduces
> effective `v_T` at cluster scale by factor ~300 (no precedent in corpus)
>
> **(β) Standing-mode reframing**: lensing isn't tracking a *propagating shockwave* but a *coherent standing
> TT-mode* at the collision site that decays slowly via Q-factor + damping. Parallel to DAMA refresh-rate
> reframing … Picture: bell STILL RINGING from the strike, lensing tracks the standing acoustic mode that
> decays over ~150 Myr.
>
> **(γ) Wrong framing entirely**: bullet cluster offset is geometric (linear superposition of static
> halo-strain fields per Vol 3 Ch 5), not shockwave-derived. The Vol 1 Ch 4 TT-shockwave story is itself
> wrong; the right framing is Vol 3 Ch 5's η_eff halo superposition that the driver actually implements.

The prereg's **load-bearing physics tension** (`:26-38`) is why the fork exists: the substrate transverse wave
speed is `v_T = c` (three loci, e.g. `photon-propagation-baseline.md:16`), so a TT shockwave from a 150-Myr-old
collision would have propagated **46 Mpc**, not the observed ~150 kpc — a ~300× contradiction. The prereg
therefore explicitly **defers to Grant**: `:38` "Needs Grant's physics-judgment call before solo derivation can
proceed"; `:108` "Awaits Grant's physics-judgment call on (α)/(β)/(γ) before any solo derivation session."

---

## ★ CRITICAL AMENDMENT CONTEXT — Grant already adjudicated (γ) [flag-don't-fix, CONFIRM before run]

**The prereg's own α/β/γ gate is stale relative to the corpus.** The frozen prereg (2026-05-17) says it "awaits
Grant's call", but the corpus records that call as **already made — Grant adjudicated (γ)** the same day:

> `dm-mechanism-unification.md:54` — "**Canonical derivation**: `vol1/…/bullet-cluster.md` (**rewritten
> 2026-05-17 per Grant adjudication (γ)**). Each cluster's baryonic mass generates an inhomogeneous
> substrate-strain halo via Axiom 2 (TKI …) + Axiom 4 (saturation)."

(Verified: the `bullet-cluster.md` leaf exists at `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/`;
the corpus's live cluster mechanism is limb (ii), the ponderomotive/geometric halo = the **(γ) family**.)

**Consequence for the run (flag-don't-fix — surface, do not silently adapt):**
- The **fireable branch is (γ)** — the geometric/ponderomotive substrate-strain halo offset, quantitatively.
- **(α) and (β) are BOTH superseded (by the γ adjudication) AND non-fireable under the current engine** — the
  frozen prereg's own ingredients table (`:78-81`) marks the TT-shockwave **source term**, **propagation
  equation**, **cluster-scale dispersion/attenuation**, and **dynamic Gordon-metric-strain → offset** as
  **MISSING (✗)**. There is no substrate machinery to fire α or β without new derivation.
- **This is the P10 statement:** under the current engine, **only (γ) can genuinely fire**; α/β cannot.
- **But the α/β/γ adjudication is 2 months old and the cluster sector is the program's honest liability
  (below).** Do **NOT** silently assume γ is still Grant's call. **Surface the prereg-vs-corpus tension to Grant
  and confirm (γ) is the branch to run** before executing. If Grant re-opens α/β, that is a HALT (they are
  non-fireable) — surface it, do not adapt.

---

## STAKES (embed — the honest-liability framing)

The **cluster sector is the honest liability** of the kernel-only dark-sector story. The galaxy-scale kernel
(limb (i)) succeeds — `dm-mechanism-unification.md:50` reports SPARC 135-galaxy mean |residual| 15.51%
(11.5% for the Q=1 sample), zero free parameters. But **MOND-class kernels are known to fail clusters by
~2×** — and the AVE cluster sector (limb (ii)) has, to date, **only a qualitative single-cluster match**.
**C13b is the mechanism's first quantitative exposure.** A negative here is a **REAL negative** and must be
**banked as one** — the miss-ledger pattern: honest negatives are the program's currency. Do not debug toward
a rescue; if the ponderomotive form misses the offset (wrong sign, wrong scaling with collision time, wrong
magnitude beyond fit-class), record the falsification cleanly, name the mechanism, and hand it back.

---

## REQUIREMENTS

1. **The ORIGINAL frozen prereg governs.** Any modernization (constants drift, engine API drift since May) is
   logged as a **dated amendment pushed BEFORE the amended code runs** (freeze-by-push, P9); the original prereg
   file stays **untouched**. The γ-adjudication (`dm-mechanism-unification.md:54`, dated 2026-05-17) is part of
   the amendment context — record it in the amendment, do not edit the frozen prereg to reflect it.
2. **P10 — state which branches can genuinely fire.** As above: (γ) fires; (α)/(β) are superseded + non-fireable
   (missing source term / propagation eq / dispersion / dynamic-strain→offset). If, on inspection, **even (γ)
   cannot fire lattice-derived under the current engine** (e.g. the driver turns out to be a pure kinematic
   prescription with no substrate-derived offset), **HALT and surface** rather than adapt silently.
3. **P11 sabotage.** Every gate proven fireable by disabling the physics (a planted-violation proof: e.g. zero
   the halo-strain amplitude and confirm the offset prediction collapses / the gate goes red). Note the driver
   honesty flag below feeds directly into this.
4. **Every input lattice-derived OR honestly tagged.** An experiment counts as a test only when every aspect is
   lattice-derived. For an **astro comparison**, imported observations are legitimate — but **tag them
   `IMPORTED-OBSERVATIONAL` explicitly**: the cluster masses, relative velocity (~4700 km/s), collision time
   (~150 Myr), redshift (z=0.30), and the empirical ~150 kpc offset anchor are all **IMPORTED-OBSERVATIONAL**
   (the prereg `:22` flags they are "NOT in corpus" and "would need to land first"). What must be
   **substrate-derived** is the **offset PREDICTION** (the halo geometry → lensing-peak-vs-gas separation), not
   the observational anchors it is compared against.
5. **Honest branches include outright failure of the ponderomotive form.** The falsifier is explicit in the
   prereg (`:104`): if the geometric halo-superposition offset conflicts with the bullet-cluster geometry beyond
   fit-class, the ponderomotive/η_eff framing for DM-class observables needs fundamental revision. Bank that as
   a clean negative if it fires.
6. **NO canonization in-lane.** Result doc + PR only. The `dm-mechanism-unification.md` leaf (and the
   `bullet-cluster.md` γ-derivation leaf) get touched **ONLY in a gated follow-on after Grant rules on the
   outcome** — not in this run.

---

## DRIVER-HONESTY FLAG (feeds P10 + P11)

The only existing driver is `src/scripts/vol_3_macroscopic/simulate_bullet_cluster_fdtd.py`. The frozen prereg
flags it **mislabeled** (`:20`, `:93`): it does **NOT** compute FDTD, TT-shockwave, Gordon metric, or an offset
distance — it computes a **kinematic-prescription + static MOND-saturation-halo superposition** (the (γ)
mechanism), the same anti-pattern class as the retired `vlbi_impedance_parallax.py`. Three sibling animation
scripts (`animate_2d_bullet_cluster.py`, `animate_bullet_timelapse.py`, `extract_bullet_stills.py`) share the
same η_eff-halo pattern. **P10/P11 consequence:** confirm what the driver actually computes before trusting any
"offset" it emits; if it only lays down a prescribed kinematic separation (rather than deriving the offset from
the halo geometry), that is a P10 HALT for γ, not a pass. The prereg's Outcome C (`:103`) notes that under γ
"the driver is already correct (just needs honest rename + scope note)" **only if** it genuinely implements the
halo-superposition offset — verify that claim, do not assume it.

---

## DELIVERABLES

- A **result doc** (`research/2026-…_C13b_bullet_cluster_result.md`) recording: the freeze-state verification;
  the P10 branch-fireability statement (γ fires, α/β superseded+non-fireable); the amendment (γ-adjudication
  context + any constants/API modernization, pushed before the amended code); the substrate-derived offset
  prediction vs the IMPORTED-OBSERVATIONAL ~150 kpc anchor, with the residual reported per the precision house
  rule (Δ ± σ, sign, experiment-supported digits); the P11 sabotage receipt; and an **honest verdict** (match /
  miss / HALT), with a clean-negative bank if the ponderomotive form misses.
- **NO edits** to `dm-mechanism-unification.md` or `bullet-cluster.md` (canonization is a gated follow-on).
- Incremental commits (freeze-by-push ordering git-checkable).

## REVIEW

Adversarial review **before CLEARED**. Lenses:
- **prereg-discipline** — the May-freeze verification (the original file is untouched; the γ-adjudication +
  any modernization is a dated amendment pushed before the amended code); the P10 branch-fireability statement
  is honest (γ fires, α/β non-fireable, not glossed); the prereg-vs-corpus tension was surfaced to Grant, not
  silently resolved.
- **live-fire reproduction** — the offset prediction is genuinely computed from the halo geometry (not a
  restated kinematic prescription); the sabotage gate goes red when the halo amplitude is zeroed; the
  IMPORTED-OBSERVATIONAL inputs are tagged and not laundered as substrate-derived.

## GATES (before push)

`make verify` · `make verify-md-links` · `make verify-provenance-stamps`. Avoid the provenance-stamp token set
(`driver-confirmed`, `test-locked`, `sympy-verified`, `sympy-confirmed`, `engine-confirmed`, `engine-verified`,
`FEM-verified`) in the `research/` result doc; use "verified" / "grep-confirmed" / "reproduced" instead.

---

*Cross-refs: the frozen prereg `research/2026-05-17_C13b_bullet_cluster_prereg.md` (the governing artifact,
untouched); the dm-sector unification `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md`
§3 / :52-64 (limb (ii) ponderomotive halo, γ-adjudicated at :54, quantitative test pending at :64); the
γ-derivation leaf `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/bullet-cluster.md`; the
driver `src/scripts/vol_3_macroscopic/simulate_bullet_cluster_fdtd.py` (mislabeled per prereg :20/:93); the
rulings docket `_orchestration/2026-07-10_rulings-docket.md` (Continuation 2026-07-11, item 14 — C13b GO). This
brief mints and canonizes nothing; it hands the frozen prereg to a satellite for a lattice-derived quantitative
run under the standing stack, with the α/β/γ adjudication tension surfaced for Grant.*
