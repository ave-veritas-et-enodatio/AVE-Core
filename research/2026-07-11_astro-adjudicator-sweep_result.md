# RESULT — the astrophysical adjudicator sweep (D2)

**Status.** Not canon. Not a ruling. This satellite **recommends**; **Grant rules**; nothing is canonized in-lane (no KB / Letter / manuscript edit). Every verdict below is `PENDING-GRANT`. Companion freeze: `research/2026-07-11_astro-adjudicator-sweep_branch-signature-map_FROZEN.md` (commit pushed **before** any retrieval output was read — the freeze-by-push proof). Handoff: `_orchestration/2026-07-11_astro-adjudicator-sweep-handoff.md`.

**Method (disclosed).** External literature entered at **TENTATIVE** standing through the external-retrieval pipeline: a gate-specified retrieval brief per adjudicator (frozen retrieval briefs archived in the appendix), then satellite adjudication against the frozen map. Retrieval this round ran **in-session** (WebSearch/WebFetch retrieval agents) rather than the Gemini gray-literature substrate of the ratified pipeline — all six adjudicators target mainstream high-profile astrophysics literature (SPARC / Chae / Banik / Genzel / Abedi–Afshordi / GW170817 / LLR), not the gray-lit case the Gemini substrate was built for. Every citation remains a **pointer to be verified**, not a fact; a hallucinated reference is a review-CRITICAL finding, and the retrieval-fidelity review lens re-fetches a sample independently. The frozen retrieval briefs are shipped in the appendix so this can be re-run through Gemini for gray-lit depth if desired.

**Contested-data discipline.** Where the discriminating data are disputed (Chae-vs-Banik wide binaries; Genzel-class high-z reanalyses; Abedi/Afshordi echoes), the deliverable is the **contested state reported honestly** — `NO CALL (contested)` — never a picked winner.

---

## SUMMARY TABLE

All six adjudications held the freeze, ran the symmetric-standard check, and (where data are disputed) reported the contested state rather than picking a winner. Every row is `PENDING-GRANT`.

| # | Adjudicator | Decides | Verdict | Recommendation (PENDING-GRANT) |
|---|---|---|---|---|
| A1 | RAR environmental dependence | T4 keying (internal/total/tide) | **NO CALL (contested)** | Keep all 3 branches open; flag `g_ext`-vs-`∇g_ext` test as green-field (never run) |
| A2 | Wide binaries vs Crater-II | tide-branch discriminator | **NO CALL (contested)** | Chae-vs-Banik dispute blocks it; do NOT demote tide; log contested state |
| A3 | High-z rotation curves / a₀(z) | G-provenance WHEN axis | **LEANS live** (retrieval-limited) | Key WHEN axis to live; attractor = demotion-candidate NOT retired; gated on replication |
| A4 | Ringdown echoes + absorption | T3 (Γ=−1 loss-character) | **NO CALL (contested)**; branch-(ii) consistent-not-confirmed | Keep T3 open; no AVE-distinct chord (branch-(ii)≡GR) |
| A5 | GW170817 one-c | channel-speed identity book | **BOOKED — passes** | Book one-substrate-`c`; verified at `10⁻¹⁵`; fix brief gate `+7e-15→+7e-16` |
| A6 | Ġ bounds | live/fossil/attractor fork | **BOOKED** | Demote naive-live (~190–7600×); survivors flatness-live/attractor/fossil; fork open |

**One-line read.** Nothing in existing data forces a fork closed *for* AVE: the two decisive contests (A1, A2) are genuinely unresolved and strain the standard picture symmetrically; A3 is the only branch-mover (a real but single-group `a₀(z)` rise favoring **live**, pending replication); A4 confirms **no AVE-distinct chord** at the horizon (branch-(ii) is GR-degenerate); A5/A6 are clean consistency books (one-`c` passes; `Ġ` kills only *naive*-live). The highest-value forward test the sweep surfaced is the **absent `g_ext`-vs-`∇g_ext` discriminator** (A1) — a green-field opportunity, not a closed question.

---

## A1 — RAR ENVIRONMENTAL DEPENDENCE → T4 keying (internal / total / TIDE)

### Frozen map (copied verbatim from the pushed freeze — for freeze-vs-result diff)

- **internal-only** (`A` keys on the source's `g_N`) → **zero environmental dependence** of the RAR.
- **total-field** (`A` keys on internal + external `g_ext`) → **deviations track `g_ext`**.
- **tide** (`A` keys on `∇g_ext`) → **deviations track external TIDAL stress**, not `g_ext` itself.
- **Demotion:** deviation tracking `g_ext` but not tide demotes internal-only + tide (favors total-field); deviation tracking tide but not `g_ext` demotes internal-only + total-field (favors tide); a confirmed null demotes total-field + tide (favors internal-only).

### Retrieval summary (TENTATIVE)

Citations (TENTATIVE; ✓ = independently re-fetched this turn on arxiv.org):

- ✓ **Chae et al. 2020**, "Testing the Strong Equivalence Principle: Detection of the External Field Effect in Rotationally Supported Galaxies", ApJ 904, 51 — `arXiv:2009.11525`. **EFE detected at 8σ–11σ in "golden" strong-field galaxies, >4σ from a blind test of 153 SPARC galaxies**, keyed to external-field strength `g_ext`. [HIGH]
- **Chae 2021** (SEP II), ApJ 921, 104 — `arXiv:2109.04745`. The fitted external-field parameter `e_N` tracks large-scale-structure overdensity (underdense ≈ 0; overdense ≈ 2× larger). [HIGH]
- ✓ **Sargent et al. 2025**, "On the Evidence for Violation of the Equivalence Principle in Disk Galaxies", Particles 8(3), 65 — `arXiv:2511.03839` (submitted 2025-11-05). Argues the same pattern is reproducible by **morphology–environment–dynamics confounding under GR/ΛCDM**; "a re-analysis … does not permit us to confidently assess the presence of an EFE." [HIGH]
- **Desmond 2023**, "The underlying radial acceleration relation", MNRAS 526, 3342 — `arXiv:2303.11314`. Joint-Bayesian nuisance treatment → intrinsic scatter `σ_int ≈ 0.034 dex` and only **"weak evidence for the external field effect."** [HIGH]
- **Lelli et al. 2017** (`arXiv:1610.08981`) / **McGaugh et al. 2016** (`arXiv:1609.05917`) — RAR scatter: abstract gives `<0.13 dex` (2017) / qualitative "small" (2016). The commonly-cited **`~0.11 dex` was NOT abstract-verified** (likely body-text/review-attributed).

**Contested state (reported, not adjudicated):** Chae 2020/2021 (EFE real, tracks `g_ext`) vs Sargent 2025 (confounding; cannot confirm) vs Desmond 2023 ("weak evidence" middle). **Load-bearing gap:** no retrieved source performs the `g_ext`-vs-tide (`∇g_ext`) separation T4 turns on — a genuine literature *absence*, not a suppressed result.

### Adjudication

**Verdict — `NO CALL (contested)`; KEEP ALL THREE T4 BRANCHES OPEN (`PENDING-GRANT`).**

- **Demotions:** none land firmly. All are contingent on resolving the Chae-vs-Sargent dispute. *Conditional (does not apply now):* IF Grant verifies Chae's `g_ext`-tracking detection and discounts Sargent's confounder, internal-only and tide would be demoted in favor of total-field — **but only if the deviation is shown to track `g_ext` and NOT tide, which no source establishes.** The tide branch is **untouched** — no source separates high-`g_ext`/low-tide vs high-tide systems. Retrieval-limited on that axis.
- **Symmetric-standard check:** the strain is **symmetric, framework-wide**. Chae's EFE is a SEP-violating signature that ΛCDM+GR also forbids in internal dynamics; Sargent rescues ΛCDM with exactly the confounding escape-hatch the AVE internal-only branch would use. No branch (AVE or standard) gets a free pass → reinforces `NO CALL`, does not single out an AVE branch.
- **Freeze integrity:** no signature loosened. Freeze-tension resisted: (1) reading "EFE tracks `g_ext`" as a total-field confirmation that demotes tide requires the high-`g_ext`/low-tide vs high-tide comparison the map mandates — never run — so a raw `g_ext`-tracking claim cannot demote tide without loosening the tide signature into "any environmental proxy"; (2) Chae's "ΛCDM neighbor-tides too weak" argument is an argument against a *ΛCDM confounder*, not a measurement of `∇g_ext`-keyed internal dynamics — not laundered into tide-vs-total-field evidence.
- **Docket recommendation (`PENDING-GRANT`):** mark registry T4 (`research/2026-07-10_collapse-target-registry.md:47`) = `NO CALL (contested)`, retrieval-limited on the discriminating axis; **keep internal-only / total-field / tide all open — do not collapse.** Flag as a **green-field opportunity**: a dedicated `g_ext`-vs-`∇g_ext` discriminating analysis (split samples into high-`g_ext`/low-tide vs high-tide bins) is the missing decisive test — an absent test, not a closed question.
- **TENTATIVE flags:** `0.11 dex` not abstract-verified (`<0.13 dex` per Lelli 2017; `0.034 dex` intrinsic per Desmond 2023); Sargent 2025 very recent (no Chae rebuttal yet — dispute evolving); the `∇g_ext`-vs-`g_ext` test is a genuine literature gap; deeper non-detection sweep (Banik & Zhao, Kroupa group) not exhausted.

---

## A2 — WIDE BINARIES vs CRATER-II-CLASS → the tide-branch discriminator

### Frozen map (copied verbatim)

- **standard-EFE** (total-field) → **suppression in BOTH** wide binaries and Crater-II-class.
- **tide** → **NO suppression in wide binaries** (strong `g_ext ≈ 1.8–2.0 a₀`, negligible tide); **suppression allowed in Crater II** (strong MW tide).
- **internal-only** → **no suppression in EITHER**.
- **Demotion:** confirmed wide-binary suppression demotes tide + internal-only (favors standard-EFE); wide-binary isolated-MOND + Crater-II suppression demotes standard-EFE + internal-only (favors tide); no suppression anywhere demotes standard-EFE + tide (favors internal-only).

### Retrieval summary (TENTATIVE)

Citations (TENTATIVE; ✓ = re-fetched this turn):

- ✓ **Chae 2023**, "Breakdown of the Newton-Einstein Standard Gravity at Low Acceleration in Internal Dynamics of Wide Binary Stars", ApJ 952, 128 — `arXiv:2305.04613`. **`g_obs/g_pred = 1.43±0.06`** at `g_N = 10⁻¹⁰·¹⁵ m/s²`; "agrees with the boost factor that AQUAL predicts." [HIGH]
- **Chae 2024**, "Robust Evidence … from Statistically Pure Binaries Free of Hidden Companions", ApJ — `arXiv:2309.10404`. Companion-free subsample (N=2,463). [HIGH; IOP page 403'd, arXiv verified]
- ✓ **Banik et al. 2024**, "Strong constraints on the gravitational law from Gaia DR3 wide binaries", MNRAS — `arXiv:2311.03436`. **Newtonian preferred at 19σ; MOND excluded at 16σ** (`α_grav = −0.021`), N=8,611 binaries. [HIGH; MNRAS vol/page (527, 4573) from snippet, UNVERIFIED]
- **Pittordis & Sutherland 2023**, "Wide Binaries from Gaia EDR3: preference for GR over MOND?", OJAp 6 — `arXiv:2205.02846`. [MED; id from title-match, not re-fetched]
- **McGaugh 2016**, "MOND Prediction for the Velocity Dispersion of … Crater II", ApJL 832, L8 — `arXiv:1610.06189`. **A-priori `σ = 2.1 (+0.9/−0.6) km/s`.** [HIGH]
- **Caldwell et al. 2017**, "Crater 2: An Extremely Cold Dark Matter Halo", ApJ 839, 20 — `arXiv:1612.06398`. **Measured `σ = 2.7±0.3 km/s`** (anomalously cold for CDM). [HIGH; IOP 403'd, arXiv verified]

**Contested state (reported, not adjudicated):** Chae 2023/2024 (anomaly, boost ~1.4, AQUAL-consistent) vs Banik 2024 / Pittordis–Sutherland (Newtonian, MOND excluded) — **same Gaia data, opposite conclusions at high formal significance** (≈10σ vs 19σ) → unresolved systematics: unresolved/hidden tertiary companions, eccentricity priors, acceleration estimator/selection cuts. Neither retracted.

### Adjudication

**Verdict — `NO CALL (contested)`; do NOT demote the tide branch (`PENDING-GRANT`).**

- **Dispute blocks the call: YES** — the Chae-vs-Banik wide-binary dispute is the discriminating datum and is unresolved (opposite conclusions from the same data ⇒ systematics, not a settled result). Crater II is confirmed-cold (McGaugh a-priori `2.1` matched by measured `2.7±0.3`) but **non-discriminating** for tide-vs-EFE (both allow Crater-II suppression) — a live-vs-dead-MOND check, not a tie-breaker.
- **Demotions (conditional only, none enacted):** IF Chae holds → wide-binary anomaly demotes internal-only; the boost magnitude (~1.4, AQUAL/EFE-consistent) leans **standard-EFE over tide**. IF Banik holds → no anomaly demotes **both tide and standard-EFE**, favoring internal-only (Crater II parked as its separate puzzle).
- **Symmetric-standard check:** clears the tide branch of unique strain. Banik's 16σ MOND exclusion would kill **standard-EFE MOND** exactly as it strains AVE's tide branch; Chae's anomaly would strain pure-Newtonian/ΛCDM. On Crater II the strained party is **ΛCDM** (anomalously cold), while the a-priori MOND-EFE prediction matched — a pass the tide branch shares.
- **Freeze integrity:** no signature loosened. Freeze-tension **refused**: Chae frames his boost as AQUAL/EFE-consistent = a *total-field/standard-EFE* signature under the frozen map, NOT the tide branch's *isolated-MOND* wide-binary signature. Blurring isolated-MOND-vs-EFE to read Chae as a tide confirmation would relax the tide signature — refused. (Note: in the wide-binary regime isolated-MOND and EFE-suppressed boosts are both ≈1.4, so the fine-magnitude discriminator is retrieval-limited even setting the dispute aside.)
- **Docket recommendation (`PENDING-GRANT`):** record the D1 §4 tide-branch row = `NO CALL (contested)` / OPEN; log the contested wide-binary state verbatim, log Crater II as confirmed-suppressed-but-non-discriminating, attach the freeze-tension note. Gate to reopen: resolution (or a decisive systematics paper) on Chae-vs-Banik + a fetch of the un-opened rebuttal/eccentricity-prior papers.
- **TENTATIVE flags:** Banik MNRAS vol/page (527, 4573) unverified (arXiv content verified); Pittordis–Sutherland id from title-match (MED); Chae 2024 / Caldwell 2017 IOP pages 403'd (arXiv substituted, verified); **not fetched** — Hernández-Chae-Aguayo-Ortiz (2024) rebuttal of Banik, `arXiv:2312.03162` critical review, and the eccentricity/orbital-modeling-sensitivity papers — all bear on the dispute and should be retrieved before any reopen.

---

## A3 — HIGH-Z ROTATION CURVES / a₀(z) → the WHEN axis (live vs attractor)

### Frozen map (copied verbatim)

- **live** (`a₀ ∝ H(z)`) → a **larger MOND scale at `z ~ 1–2`** (`H` was `~2–3×` today's).
- **attractor** (`a₀ = cH_∞/2π`, ∞ subscript, `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/derived-mond-acceleration-scale.md:15`) → **redshift-constant `a₀`.**
- **Demotion:** confirmed `a₀(z)` rising with `H(z)` demotes attractor; confirmed redshift-constant `a₀` to `z ~ 1–2` demotes live.

### Retrieval summary (TENTATIVE)

Citations (TENTATIVE; ✓ = re-fetched this turn):

- ✓ **★ Ciocan et al. 2026**, "MUSE-DARK III: The evolution of the radial acceleration relation at intermediate redshifts", A&A — `arXiv:2604.22613` (submitted 2026-04-24; authors incl. Bouché, Freundlich, Desmond, Famaey). **Direct `a₀(z)` fit over `0.33 < z < 1.44`: `a₀(z~1) = 2.38±0.1 ×10⁻¹⁰ m/s²`, linear slope `a₁ = 1.59±0.1 ×10⁻¹⁰`** — `a₀` RISES with redshift vs local `~1.2×10⁻¹⁰`. **The single on-axis datum.** [HIGH — re-fetched — but single-group, unreplicated]
- **Genzel et al. 2017**, "Strongly baryon-dominated disk galaxies …", Nature 543, 397 — `arXiv:1703.04310`; **Lang et al. 2017**, ApJ 840, 92 — `arXiv:1703.05491`. Declining outer rotation curves at `z~1–2`. [HIGH; framed in DM-fraction, NOT `a₀`]
- **Tiley et al. 2019** (`arXiv:1811.05982`) / **Sharma et al. 2021** (`arXiv:2005.00279`) / **RC100 (Nestor Shachar et al. 2023)** (`arXiv:2209.12199`) — beam-smearing / pressure-support / disk-scale-length critiques; flat-after-correction camp. [HIGH]

**Two distinct threads (do NOT conflate):** (1) the RC-**shape** dispute (Genzel/Lang declining vs Tiley/Sharma flat) is **OFF the `a₀` WHEN-axis** — neither camp frames results in `a₀`/RAR terms, and declining high-z curves are read as baryon-domination (Newtonian `a > a₀` regime), compatible with BOTH live and attractor. (2) The direct `a₀(z)` measurement (Ciocan 2026) is the only on-axis datum, and it is single-group/unreplicated — **not disputed, just unreplicated.**

### Adjudication

**Verdict — `LEANS live` (retrieval-limited); attractor = demotion-candidate, NOT retired (`PENDING-GRANT`).**

- **Demotions:** **attractor** (`a₀ = cH_∞/2π`, redshift-constant) is demoted by the Ciocan 2026 `a₀(z)` rise — precisely the frozen trigger ("`a₀(z)` rising with `H(z)` demotes attractor"). **Contingent** on verifying the citation (done: real ✓) + an independent replication (not yet). A single unreplicated paper should not book a canonical-axis demotion alone. **Fossil** is NOT discriminated (near formation epoch, live and fossil both predict higher `a₀` at higher `z`); it leans dead on the storage-medium argument, not this datum. The RC-shape dispute demotes **nothing** on-axis.
- **Symmetric-standard check:** the `a₀`-rise strains the standard alternative *at least as much* — standard MOND holds `a₀ ~ cH₀/2π` **constant**, the functional twin of AVE-attractor, so a genuine `a₀(z)` rise is equally awkward for it. AVE-attractor is **not uniquely strained**; AVE-live is the branch aligned with the data. (ΛCDM gets a pass only by being off-axis — it uses no `a₀`, reading the same signal as baryon/missing-mass evolution.)
- **Freeze integrity:** no signature loosened. Live confirmed in **direction** only (`a₀` rises ~2× by `z~1` vs `H(z)/H₀ ≈ 1.76` — order-consistent, **not** forced to match). Freeze-tension noted: Ciocan uses `a₀(z) = a₀(0) + a₁z` (linear-in-`z`), NOT the `∝H(z)` functional form — **do not upgrade to a strict functional-form confirmation.** Attractor anchor (`derived-mond-acceleration-scale.md:15`) preserved frozen, demoted-if-verified, not reinterpreted.
- **Docket recommendation (`PENDING-GRANT`):** tentatively key the D1 §5 WHEN axis to **LIVE** (`a₀ ∝ H(z)`); mark the attractor branch (`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/derived-mond-acceleration-scale.md:15`) **DATA-STRAINED / demotion-candidate, NOT retired.** Booking gated on **two** conditions: (1) Grant verifies Ciocan 2026 (done here: real, transcribed correctly ✓); (2) ≥1 independent-group `a₀(z)` measurement corroborates the rise. Until (2) clears, this is a `LEANS-live` row and the attractor anchor **stays frozen in canon**.
- **TENTATIVE flags:** **Ciocan 2026 (`arXiv:2604.22613`) is the sole load-bearing datum** — re-fetched and real, but single-group/single-survey (MUSE-UDF), unreplicated; no independent `a₀(z)` measurement found to corroborate/contest. Genzel 2017 Nature text not verbatim-checked vs published version (arXiv proxy); RC100 abstract centers on DM-fraction-within-Re, not an outer-decline re-assertion. All RC-shape material is off-axis and non-load-bearing.

---

## A4 — RINGDOWN ECHOES + ABSORPTION → T3 (Γ=−1 loss-character)

### Frozen map (copied verbatim)

- **branch (i) — lossless-reflective short** (same `Γ=−1` object as the electron cage) → **post-ring-down ECHOES** + **sub-unity horizon absorption.**
- **branch (ii) — dissipative fuse/matched** → **no echoes**, **horizon-grade absorption** (regime-legal above yield, `manuscript/ave-kb/vol4/claim-quality.md:1168`).
- **Demotion:** confirmed echo detection at credible significance demotes branch (ii); confirmed absorption null / horizon-grade absorption with no echoes demotes branch (i). D1 lean: branch (ii).

### Retrieval summary (TENTATIVE)

Citations (TENTATIVE; ✓ = re-fetched this turn):

- ✓ **Abedi, Dykaar & Afshordi 2017**, "Echoes from the Abyss: Tentative evidence for Planck-scale structure at black hole horizons", PRD 96, 082004 — `arXiv:1612.00266`. **Tentative echoes at 1% false-detection prob (~2.5σ)** across GW150914/GW151226/LVT151012. [HIGH]
- **Abedi & Afshordi 2019**, "Echoes … for GW170817", JCAP 11 (2019) 010 — `arXiv:1803.10454`. **~4.2σ** echo claim from the BNS remnant (single-group). [HIGH]
- ✓ **Westerweck et al. 2018**, "Low significance of evidence for black hole echoes in gravitational wave data", PRD 97, 124037 — `arXiv:1712.09966`. Reduced significance **"entirely consistent with noise … does not provide any observational evidence."** [HIGH]
- **Abedi et al. 2018** comment (`arXiv:1803.08565`) reads Westerweck's own `2±1%` p-value as "moderate evidence"; **Nielsen et al. 2019** (`arXiv:1811.04904`) parameter-estimation follow-up. [HIGH]
- **LVK, "Tests of GR with GWTC-3" 2022** — summary `arXiv:2204.00662` (full `arXiv:2112.06861`). No collaboration-level echo confirmation; IMR consistency holds. [HIGH summary; full-text figures UNVERIFIED]
- **"Bring the Heat: Tidal Heating Constraints …" 2024** — `arXiv:2404.14641`. Tidal-heating/absorption consistent with **near-unity** (`H₀=1` inside a wide CI). [MED; single fetch pass]

**Contested state (reported, not adjudicated):** Abedi/Afshordi positive (2.5σ O1; 4.2σ GW170817, single-group) vs Westerweck null — the disagreement is driven by **method** (background/trials estimation, template-bank p-value vs full-likelihood Bayes factor, echo-template choice), not new data. The literature explicitly does not adjudicate.

### Adjudication

**Verdict — `NO CALL (contested)` on the primary echo discriminator; T3 stays OPEN (`PENDING-GRANT`). D1 branch-(ii) lean is CONSISTENT-WITH-but-NOT-CONFIRMED.**

- **Demotions:** none enacted (echo axis contested). On the *non-contested* axes both weakly point to **branch (ii)** / the D1 lean: (a) no LVK-level echo confirmation (GWTC-3 TGR), (b) tidal-heating absorption consistent with near-unity. So branch (ii) is weakly favored on those axes; **branch (i) is soft-strained but NOT demoted at credible significance.**
- **Symmetric-standard check:** cuts both ways and yields **no asymmetric AVE penalty**. Branch (ii)'s signature (no echoes, horizon-grade absorption) is observationally **degenerate with a classical GR black hole** → the data "favoring" branch (ii) confirm **nothing AVE-distinct** (consistency only, no chord). Branch (i)'s strain is the **identical** strain mainstream ECO/firewall/Planck-structure models carry under the same reanalyses — AVE's echo branch is not uniquely over-strained.
- **Freeze integrity:** no signature loosened. Freeze-tension **resisted**: the tidal-heating CI is wide (a sub-unity value sits inside it), so it is **consistent-with** near-unity but does NOT **exclude** branch (i)'s sub-unity signature — treating consistency as exclusion would weaponize a demotion branch (ii) has not earned. Branch (i)'s sub-unity-absorption and detectable-echo signatures both stay frozen and un-demoted.
- **Docket recommendation (`PENDING-GRANT`):** keep registry T3 (`research/2026-07-10_collapse-target-registry.md:46`) loss-character **OPEN — do not collapse.** Log the contested echo state verbatim; record the D1 branch-(ii) lean (dissipative/matched, near-unity absorption, no confirmed echoes) as **consistent with current data but not confirmed**; explicitly do NOT demote branch (i) on the non-exclusionary wide-CI bound; note the branch-(ii)/GR observational degeneracy (**no AVE-distinct chord here**). Revisit trigger: O4/O5 or independent-group echo searches reaching collaboration-level significance either way, OR a tightened absorption bound that actually excludes sub-unity absorption.
- **TENTATIVE flags:** GWTC-3 TGR full-text IMR figures (`arXiv:2112.06861`) from a WebSearch summary, UNVERIFIED (clean anchor is the summary `2204.00662`); tidal-heating CI (`arXiv:2404.14641`) MED, single fetch — re-fetch before treating as load-bearing since it is the only non-contested lean toward branch (ii); the 4.2σ GW170817 result is single-group, not independently reproduced.

---

## A5 — GW170817 ONE-c → books the channel-speed identity (already passed)

### Frozen map (copied verbatim)

- Consistency **book, not a fork** (no live AVE branch predicts a split). `c_gw = c_light` to `~10⁻¹⁵` reads as shear + EM riding **ONE substrate `c`**; the bound **excludes channel-split propagation** at the `10⁻¹⁵` level.
- Corpus flags this as an external bound requiring verification: `research/2026-06-11_chiral-vacuum-reactor-framing.md:393`.

### Retrieval summary (TENTATIVE)

Citations (TENTATIVE; ✓ = re-fetched this turn):

- ✓ **Abbott et al. 2017**, "Gravitational Waves and Gamma-Rays from a Binary Neutron Star Merger: GW170817 and GRB 170817A", ApJL 848, L13 — `arXiv:1710.05834`. **Bound `−3×10⁻¹⁵ ≤ (c_gw − c)/c ≤ +7×10⁻¹⁶`; gamma-ray delay `+1.74±0.05 s`.** [HIGH]
- **Abbott et al. 2017** (companion detection), PRL 119, 161101 — `arXiv:1710.05832`. Source distance `40 (+8/−14) Mpc` (provenance of the distance, distinct from L13). [HIGH]

### Adjudication

**Verdict — `BOOKED` (consistency book, not a fork); the bound PASSES verification (`PENDING-GRANT`).**

- **What it books:** `c_gw = c_light` to `~10⁻¹⁵` reads as the shear and EM channels riding **ONE substrate `c`**; the bound **excludes channel-split propagation modifications** at the `10⁻¹⁵` level. No live AVE branch predicts a split → no winner to pick.
- **Symmetric-standard check:** PASS / symmetric. This datum **kills Horndeski / modified-gravity dark-energy** (modified-propagation models), **not** GR — GR predicts `c_gw = c` and passes trivially; the AVE one-substrate-`c` book passes identically. Both ride the bound comfortably; the models it strains are precisely the ones AVE's book does not invoke.
- **Freeze integrity:** no signature loosened. Freeze-tension is **inverted** — the retrieved bound (`+7×10⁻¹⁶` upper) is ~1 OOM *tighter* than the frozen "`~10⁻¹⁵`"; kept frozen at `~10⁻¹⁵` (conservative; the `−3×10⁻¹⁵` side sets the order).
  - **★ Brief-side correction (not a freeze issue):** the *retrieval-brief inclusion gate* wrote the upper bound as `+7×10⁻¹⁵`, one OOM too loose; the actual value is `+7×10⁻¹⁶`. The **frozen branch-signature map itself said `~10⁻¹⁵` (correct order)** — freeze integrity intact; only the retrieval-brief gate text is corrected here.
- **Docket recommendation (`PENDING-GRANT`):** mark the external bound flagged at `research/2026-06-11_chiral-vacuum-reactor-framing.md:393` **VERIFIED at the `10⁻¹⁵` level** (Abbott et al. 2017, ApJL 848 L13 / `arXiv:1710.05834`); **book** the "shear + EM channels ride one substrate `c`" consistency identity as confirmed. Note the brief inclusion-gate correction (`+7×10⁻¹⁵ → +7×10⁻¹⁶`).
- **TENTATIVE flags:** IOP/ApJL page 403'd (arXiv preprint used, standard citable equivalent); the `~40 Mpc` distance is from the companion PRL 119 161101 (`arXiv:1710.05832`), correct provenance but a distinct paper from the brief's named source (distance not load-bearing — only sets the OOM of the bound, which L13 quotes directly).

---

## A6 — Ġ BOUNDS vs MACHIAN-G READINGS → constrains live/fossil/attractor

### Frozen map (copied verbatim)

- **LLR** `|Ġ/G| ≲ 1.5×10⁻¹³/yr` (+ pulsar-timing + BBN cross-checks); the **`~500×` exclusion of naive-live** (`~ H₀ ≈ 7×10⁻¹¹/yr` is `~470×` over LLR); Sciama coincidence **non-discriminating under flatness**.
- **Demotion:** bounds already demote naive-live; do NOT by themselves demote flatness-protected-live or attractor. **Job:** book bounds + state which branches survive.
- **★ SCOPE FENCE:** the flatness-Ġ self-cancellation derivation is a THEORY item, OUT of scope.

### Retrieval summary (TENTATIVE)

Citations (TENTATIVE; ✓ = re-fetched this turn):

- **Hofmann, Müller & Biskupek 2010**, "LLR test of the Nordtvedt parameter and a possible variation in `G`", A&A 522, L5 — DOI `10.1051/0004-6361/201015659`. `Ġ/G₀ = (−0.7±3.8)×10⁻¹³/yr`. [HIGH]
- ✓ **Biskupek, Müller & Torre 2021**, "Benefit of New High-Precision LLR Data …", Universe 7(10), 383 — `arXiv:2012.12032`. **`Ġ/G₀ = (−5.0±9.6)×10⁻¹⁵/yr`** (current-tightest LLR). [HIGH]
- **Hofmann & Müller 2018**, "Relativistic tests with LLR", CQG 35, 035015 — DOI `10.1088/1361-6382/aa8f7a`. Presumptive source of the frozen `1.5×10⁻¹³/yr` book value + the `~470×` arithmetic. [**LOW — IOP 403'd + empty ADS; exact number UNVERIFIED**]
- ✓ **Zhu et al. 2019**, "Tests of Gravitational Symmetries with Pulsar Binary J1713+0747", MNRAS 482, 3249 — `arXiv:1802.09206`. **`Ġ/G = (−0.1±0.9)×10⁻¹²/yr`** (pulsar-timing). [HIGH]
- **Copi, Davis & Krauss 2004**, "New Nucleosynthesis Constraint on the Variation of `G`", PRL 92, 171301 — `arXiv:astro-ph/0311334` (BBN, `~3–4×10⁻¹³/yr`-class); **Alvey et al. 2020** (`arXiv:1910.10730`, improved BBN). [HIGH]

### Adjudication

**Verdict — `BOOKED` (consistency-book lane); demotes naive-live G; fork stays OPEN per scope fence (`PENDING-GRANT`).**

- **Demotions:** **naive-live G — DEMOTED.** A naive live rate `~H₀ ≈ 7×10⁻¹¹/yr` exceeds the verified LLR endpoints by **~190×** (vs 2010 `3.8×10⁻¹³`), **~470×** (vs the frozen `1.5×10⁻¹³` book value), and **~7600×** (vs 2021 `9.6×10⁻¹⁵`) — robust across LLR / pulsar / BBN, and independent of the unverified exact book number (every verified LLR endpoint excludes naive-live by ≥2 OOM). **flatness-protected-live / attractor / fossil — NOT demoted** (all satisfy the bound; fossil trivially, `Ġ=0`).
- **Dispute:** none — all three probe classes agree `Ġ≈0` with no mutual tension (the Alvey BBN linear-rate looseness vs Copi is a known epoch-weighting/model-sensitivity artifact, not tension).
- **Symmetric-standard check:** GR/ΛCDM predicts `Ġ=0` exactly and passes trivially — so naive-live is **genuinely (uniquely) strained**, a real exclusion, NOT a consensus-bias artifact. The surviving AVE branches satisfy the bound on the same footing as GR — none uniquely strained.
- **Freeze integrity:** no signature loosened. Frozen book `|Ġ/G| ≲ 1.5×10⁻¹³/yr` kept (conservative); freeze-tension is **tightening-only** (adopting the verified 2021 `9.6×10⁻¹⁵` would *strengthen* the exclusion to ~7600×, never weaken it). The demotion of naive-live is not at risk under any verified value.
- **★ Scope fence honored:** the flatness-`Ġ` self-cancellation *derivation* (does the Machian form self-cancel to `Ġ=0`, or leave an era-transition residual at the LLR bound) is a **THEORY item, OUT of scope** — this books empirical bounds only.
- **Docket recommendation (`PENDING-GRANT`):** feeds the D1 §5 G-provenance fork (`Ġ` side). (1) **Book** the bounds — LLR primary `≲1.5×10⁻¹³/yr` with verified brackets `3.8×10⁻¹³` (2010) / `9.6×10⁻¹⁵` (2021), plus pulsar (`~10⁻¹²`) and BBN (`~3–4×10⁻¹³`) cross-checks; (2) **demote naive-live** (excluded ~190×–7600×); (3) record **survivors = flatness-protected-live + attractor + fossil**, fork UNRESOLVED (self-cancellation derivation deferred); (4) Sciama coincidence booked as **non-discriminating under flatness**.
- **TENTATIVE flags:** **Hofmann & Müller 2018** (source of the exact `1.5×10⁻¹³` and the `~470×`) — IOP 403'd, exact number UNVERIFIED; the `~470×` multiplier is self-consistent only with a `~1.5×10⁻¹³` bound (verified brackets give 190× / 7600×). If Grant wants `470×` stated as fact (not OOM), the 2018 value is load-bearing and needs authenticated access. Williams-Turyshev-Boggs (secondary LLR) not fetched. The book and the naive-live demotion rest on the verified 2010/2021 LLR + Zhu 2019 and are safe even if 2018 stays unverified.

---

## LINEAGE-MAP AMENDMENT CANDIDATES (flagged, NOT landed)

Flags for the lineage map — **NOT landed** (the lineage map is not edited in-lane; the core session decides). Recorded so the novelty claim stays honest:

- **Milgrom modified-inertia MOND** — the **tide branch's** possible lineage (D1 §4 kill-test 3). Modified-inertia MOND variants carry a weakened/altered EFE; the tide branch (EFE ∝ `∇g_ext`, not `g_ext`) may be that class in lattice clothing. *Relevance reinforced by the sweep:* A1/A2 show the EFE's `g_ext`-vs-tide character is exactly the unmeasured axis, so the modified-inertia lineage is live, not settled.
- **Brans–Dicke / Dirac large-numbers hypothesis** — the **live-G branch's** lineage (D1 §5 prior-art node). Both died on exactly the `Ġ` bounds A6 books. *Relevance reinforced:* A6 confirms naive-live G is excluded ~190–7600× — the same bound that killed Brans–Dicke/Dirac — so any AVE live-G branch must be the flatness-protected (self-cancelling) variant, not the naive one.

---

## APPENDIX — FROZEN RETRIEVAL BRIEFS (gate-specified; re-runnable through Gemini)

Archived so the sweep is re-runnable through the Gemini gray-lit substrate (the ratified-pipeline half) if deeper non-mainstream coverage is wanted. Shared discipline for every brief: **retrieve-and-transcribe only, do not adjudicate; every citation must be a fetched, resolving URL with a verbatim quote — never invent an arXiv id / DOI / author / year / volume; unverifiable items go to a gaps list, not into the citations; where a result is disputed, map the dispute state and pick no winner.**

- **A1 — RAR environmental dependence.** Does the galaxy RAR show environmental dependence, and does it track external acceleration `g_ext` or external tide `∇g_ext`? Anchors: SPARC RAR scatter (`~0.11 dex` claim → verify source); Chae et al. EFE-detection claims (2020/2021) **and** their contested status; any test of RAR residuals vs environment / `g_ext` vs tide. Report (a) no dependence / (b) tracks `g_ext` / (c) tracks tide; map the Chae-EFE dispute.
- **A2 — Wide binaries vs Crater-II.** Current DISPUTE state of the Gaia wide-binary low-acceleration test + Crater II velocity dispersion. Anchors: Chae 2023/2024 (MOND-consistent anomaly) vs Banik 2024 / Pittordis–Sutherland 2023 (Newtonian) — verify each, the significances, and the debated systematics (hidden companions, eccentricity priors, estimator); Crater II `σ` (Caldwell 2017) + MOND-EFE prediction (McGaugh 2016). Wide binaries are the discriminating datum; report contested, pick no winner.
- **A3 — High-z rotation curves / a₀(z).** Does the MOND scale `a₀` (or effective DM behavior) evolve with redshift to `z~1–2`? Anchors: Genzel 2017 / Lang 2017 (declining high-z curves) **and** contested reanalyses (Tiley 2019, Sharma 2021 — beam-smearing/pressure-support); any direct `a₀(z)` constraint. Report whether the scale looks larger (rising with `H(z)`) or redshift-constant; map both sides.
- **A4 — Ringdown echoes + absorption.** State of (a) post-ringdown GW echo searches and (b) horizon absorption / QNM consistency. Anchors: Abedi/Afshordi echo claims (2.5σ O1; 4.2σ GW170817) **and** null reanalyses (Westerweck 2018, Nielsen 2019, LVK); IMR consistency (GWTC-3); tidal-heating/absorption bounds. Report significances + both sides; pick no winner on echoes.
- **A5 — GW170817 one-c (cheap lane).** Verify the GW170817/GRB 170817A arrival-coincidence bound on `(c_gw − c)/c`. Anchor: Abbott et al. 2017 (ApJL 848 L13). Verify the exact bound (`−3×10⁻¹⁵ ≤ · ≤ +7×10⁻¹⁶` — **note the corrected upper bound**), the `~1.74 s` delay, and the `~40 Mpc` distance. Booking, not a dispute.
- **A6 — Ġ bounds.** Book the best bounds on `Ġ/G`. Anchors: LLR (Hofmann/Müller/Biskupek — 2010 A&A 522 L5, 2018 CQG 35 035015, 2021 `arXiv:2012.12032`); pulsar timing (Zhu 2019, J1713+0747); BBN (Copi 2004, Alvey 2020). Verify the tightest bound; check the arithmetic that a naive-live rate `~H₀` is ~10²–10³× above the LLR bound.

---

*End of result. Companion freeze: `research/2026-07-11_astro-adjudicator-sweep_branch-signature-map_FROZEN.md`. Docket-continuation stub for the core session: `_orchestration/2026-07-11_astro-adjudicator-sweep_docket-continuation-stub.md`.*
