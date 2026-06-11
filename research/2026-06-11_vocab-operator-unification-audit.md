# AVE Vocabulary & Operator Unification Audit — 2026-06-10/11 session harvest (research-doc DRAFT)

**Date:** 2026-06-11
**Branch:** `analysis/2026-06-11-vocab-operator-audit` (off `origin/main` @ `f6ffd98d`)
**Lane:** implementer. Surfaces the empirical nomenclature findings + stages the candidates; the auditor lands the `common/`-leaf and Vol-9 manual entries and adjudicates the RENAME-QUEUE / promotion; Grant adjudicates the framing-level calls (the srs-vs-diamond collision, the α-turns-ratio framing, the LOOP GAP diagnosis).

> **Status: research-doc DRAFT — NOT canon. Auditor/Grant-gated.** This doc unifies the vocabulary
> and the new mathematical objects minted across the 2026-06-10/11 session branch set into one
> consistent language, per Grant's directive ("consistent language unified across these efforts for
> the conclusions"). It **renames nothing** in existing canon and **edits no settled registry row.**
>
> **KEEP-BOTH with the merged registry (`research/2026-06-10_field-symbol-registry.md`, PR #176).**
> Everything here is an **extension layer**: §1 adds NEW rows in the registry's row-format; it does not
> touch the §3 table, the §4 collision ledger, or the §5 RENAME-QUEUE of the merged registry. The
> rename-queue rows **R1–R8 + N11 are SETTLED law** (Grant 2026-06-10, EXECUTED PR #178) and are **not
> re-opened** here. New collisions surfaced in §3 are *additions* to the §4 ledger, staged for the
> auditor — flag-don't-fix, never silently renamed.
>
> **Discipline tags applied:** `verify-before-cite` (every term cited to its branch/PR/commit; every
> operator's defining equation quoted verbatim from source; the α·m_ec² store, the LOOP-GAP anchor, and
> the Tellegen-VIRGIN result were grep-confirmed this session against `AVE-Core @ origin/main f6ffd98d`
> or the named branch via git objects — receipts inline), `flag-don't-fix`, `consistency-vs-emergence`
> (every conclusion class-tagged), `ave-power-category-check` (every energy/power term classified
> Q_reactive vs P_real-port-local per the orbital-friction-paradox ruling), `ave-evidence-framing-discipline`
> (origin/main vs UNMERGED-branch vs LOCAL-ONLY vs SESSION-RECORD tagged on each anchor),
> `substrate-native-check` (the three-impedance law is the K4/Cosserat channel discipline made normative),
> `KEEP-BOTH`.

## Scope & method

- **Harvest scope (grep-verified this turn):** the merged set at `main` (registry PR #176, datasheet
  #166, abandoned-interior #179, foreword #177) + the open PR branches #180–#195 + the two parked
  LOCAL-ONLY branches (`analysis/2026-06-11-screened-winding-probe`,
  `analysis/2026-06-11-chiral-angle-of-attack` — both UNPUSHED, no origin ref; cited as local-only).
- **Baselines (not re-litigated):** `research/2026-06-10_field-symbol-registry.md` (§3 rows, §4
  collisions, §5 settled rulings) + `research/2026-06-10_novel-objects-report.md` (N1–N11) +
  `manuscript/ave-kb/common/operators.md` (Op1–Op22 catalog of record).
- **Evidence-class legend (used throughout):** `(main)` = merged at `origin/main`; `[branch #N]` =
  committed on an open PR branch, UNMERGED; `[LOCAL-ONLY]` = committed on an unpushed local branch;
  `SESSION-RECORD` = no committed anchor anywhere (cited honestly as conversation-only).
- **Citations are backtick `path:line` (not markdown links)** so `verify-md-links` has nothing to break.

---

## §1 — Registry-v2 extension table (KEEP-BOTH with PR #176)

Registry-v2 row format (per Grant directive): **symbol/term | name | real/phase-space | channel |
units | class tag | defining source | one-line definition.** Channels use the §1 sector map of the
merged registry (EM-transverse / shear / bulk-longitudinal / Cosserat / phasor / topology / kernel /
ports / operators). Class tags: `engine-construct` / `candidate-physics` / `hypothesis` / `framing` /
`instrument` / `object-qualifier` / `bin` / `session-record`. These are **extension rows** — none
edits a settled registry row; collisions they create are queued in §3, not resolved here.

### §1.1 — New nouns (engine-constructs, candidate-physics, hypotheses, framings)

| Term | Name | real/phase | channel | units | class | defining source | one-line definition |
|---|---|---|---|---|---|---|---|
| the rotation column | energized rotation column (ex-"bubble") | real | Cosserat ω + bulk | engine-native | engine-construct (re-scope) | `[branch #194]` `genesis-v8-threaded_prereg.md:19,29`; `[branch #191]` ledger:156-158 | the v6 made object settles COMPRESSED (max ρ̄ +0.949) as a column+transducer assembly, NOT a tensile bubble — the carrier whose axial flux must thread the shell |
| the snapped shell / snap shell | snapped-void interface shell | real | bulk | engine-native | engine-construct + candidate-physics (interface energy) | `[branch #194]` prereg:29,91,124; `[branch #190]` bubble-physics:36 | the largest connected `snap_mask` component (`scipy.ndimage.label`, 6-conn); a Meissner-class condensate whose interface energy/area is the σ-from-ℓ_c candidate |
| the pocket (two-pockets) | saturated-core breather pocket vs cavitation void | real | bulk | engine-native | candidate-physics (extends N5) | `[branch #190]` bubble-physics:32; `[branch #191]` ledger:156-158 | TWO objects on OPPOSITE EOS branches: STIFFENING saturated-core breather (c_eff²→∞, Γ=−1 wall) vs SOFTENING cavitation void (c_bulk²→0 at ρ̄_cav) — disambiguation surfaced for Grant (§3.4) |
| the threaded channel | un-snapped axial channel through the shell | real / topology | bulk + topology | engine-native | engine-construct → candidate-physics | `[branch #194]` prereg:31,36,55,111 | a connected un-snapped tube spanning the shell's axial extent, encircled by snapped shell cells; its locus DEFINES the field-derived read torus R (the v7 A46 fix); type-II penetration analog |
| the slats | helical slats (chiral boundary) | real | EM-transverse / boundary | n/a | hypothesis | `[LOCAL-ONLY]` `chiral-angle-of-attack.md:1`; `[branch #195]` `chiral_lattice_optical_activity.py:81` | the chiral boundary read as four helical surfaces ("slats"); promotion auditor-gated per the doc header |
| the chiral mirror | "the mirror from inside" | real / phase | EM-transverse / boundary | n/a | hypothesis + collision | `[LOCAL-ONLY]` `chiral-angle-of-attack.md:286-288,35,41,73-87` | Grant's framing: the same chiral boundary turns into a mirror viewed from inside (cholesteric-LC analog); static control 0.5434, R_co≈0.015-0.018 — COLLIDES with ≥3 other session "mirror" senses (§3.4) |
| the melt (phase region) | melt / pre-geodesic plasma | real | bulk (state) | K (T_melt≈5.93e9 K) | extends-canon + new rendering | `[branch #185]` `14_phase_diagrams.tex:12,31,36,67` | the (T,ρ̄)-plane thermodynamic phase region where shear cannot propagate (k_B·T=m_ec²); the r=A/A_c four-regime map is DEMOTED to "the excitation map of the solid phase" |
| the melt-coupling channel | the sole solid↔melt propagating channel | real | bulk-longitudinal | engine-native | hypothesis (VIRGIN) | `[branch #187]` `alpha-hand-of-god-framing.md:216,222-227,243` | claim that the longitudinal/bulk channel is the ONLY channel that propagates across the solid↔melt boundary (shear cannot propagate in melt); tagged `[VIRGIN]` — not stated anywhere in canon; three owed numbers |
| the transducer + δL | chiral boundary transducer + exchange quantum δL | real / phase | Cosserat (ADD-2 velocity-space rotation) | engine-native (Ω_add=δL/I_wall) | engine-construct (extends N9; N9 "δL UNVERIFIABLE" now STALE) | `[branch #180]` `genesis-v6-transducer_prereg.md:90-91` | δL defined EXACTLY (Δs=χ̃·g_wall·s_density, Σ Δs·dV ≡ δL); a LIVE passive helicity-odd depleting chiral boundary coupling whose net deposit (∓3.6e-5) is drained by the lock |
| chiral boundary coupling | the demoted-restatement of the transducer | real | Cosserat | engine-native | engine-construct | `[branch #180]` result:84,92 | the post-adversarial-panel restatement of the transducer's verdict: a rigid-azimuthal field deposit removed by `_lock_relax` (the deposit feeds exactly the mode the lock drains) |
| Meissner-class condensate shell | type-II penetration-depth analog | real | bulk | engine-native | hypothesis (inside N11 RECONCILED bound) | `[branch #194]` prereg:29,111,115 | the snap shell as a Meissner-class condensate (expulsion → normal channel, ball→torus); stays a LENS not an identity per N11; UNTESTED (SHELL-NEVER-FORMS gated it out) |
| polyphase rotating-field stator | the traveling deposit | phase | topology/drive | engine-native | engine-construct (drive architecture) | `[branch #194]` prereg:42,62,113 | N_phase≥2 quadrature injection driving a TRAVELING phase wave; helicity sets the phase SEQUENCE; D13-FAITHFUL keeper; predicts T_travel≲450-step sustain |
| chiral trivalent (srs) lattice | I4₁32 / I4₃32 enantiomorph pair | real | lattice (substrate) | n/a | engine-construct (Phase-0 scaffold, adjudication-gated) | `[branch #195]` `genesis-v9-chiral-lattice_design.md:21,112,176`; `chiral_lattice.py` | the chiral trivalent (degree-3, girth-10, 432) net + its mirror; NO genesis run; the design's own flag: canon's computed object is degree-4 achiral diamond — the big collision (§3.1) |
| the death channel | un-storing as propagating longitudinal V-waves | real | bulk-longitudinal | engine-native | hypothesis (time-reverse of N4 birth pulse) | `[branch #190]` bubble-physics:11,85,149-151 | DESIGN NOTE (NOT implemented): annihilation as the time-reverse of the birth pulse, Axiom-4 engage/relax, "No QED Kramers-Heisenberg/Rabi"; feeds the annihilation arc's follow-up |
| the MADE object | the v6 made object (de-novo vs planted) | real | bulk | engine-native | object-qualifier | `[branch #193]` `s11-de-novo_result.md:1,15` | distinguishes the engine-BUILT de-novo object (S11ProbeUnified probe-off byte-identical to UnifiedGenesisEngine, max\|diff\|=0) from the planted-seed object; both legs UNRESOLVED |
| the two-deletions thesis | two deletions, one restoration | n/a | n/a (framing) | n/a | framing (consistency-class) | `(main #177)` `foreword-proposal_two-deletions.md:1,24,110` | foreword PROPOSAL (replaces nothing): two historical deletions (the medium; the constitutive question), one earned victory each; self-declared consistency-class ceiling |
| THE THIRD DELETION — the frame | the frame / freeze frame / wind gauge | n/a | n/a (framing) | km/s (CMB dipole 369.82) | framing (auditor-gated; Rule-12 extension) | `(main #179 + ext)` `the-abandoned-interior.md:112,148,156,157` | retired-not-refuted: "the frame" (the medium's rest frame, 1905) = the CMB-isotropic freeze frame; the CMB dipole = "the visible wind gauge"; consistency-class |
| the constitutive question | abandoned, not answered | n/a | n/a (framing) | n/a | framing (merged) | `(main #179)` `the-abandoned-interior.md:12,121` | the historical claim that the medium's constitutive question was abandoned rather than answered; a restored medium makes it cheaply re-attackable; carries its own anti-triumphalism fences |
| fluid-analog bench program | seven named bench experiments | n/a | n/a (program) | n/a | program (DRAFT-FOR-REVIEW) | `[branch #183]` `fluid-analog-bench-program.md:1` | vortex-ring collisions (RANK 1), Kondepudi stirred crystallization, walking droplets, Taylor columns, pump-loop vapor lock, single-bubble sonoluminescence, flume horizon + validation ladder §8 |
| hand-of-God framing | α = the one measured IC + the menu | n/a | n/a (framing) | n/a | framing + hypothesis (Grant-gated) | `[branch #187]` `alpha-hand-of-god-framing.md:6,144-152` | α as the single measured initial condition; the "menu" = discrete allowed operating points (polymorph analogy); MUST clear the reconstruction-stop fence (§5) before any α-emergence framing |
| moving-defect pilot-channel fork | C-transport/C-neutral/C-localize/C-bound gates | real | bulk + shear | n/a | prereg + capability-gate | `[branch #186]` `moving-defect-doubleslit_prereg.md:97,123,149,160` | the dynamically-moving-defect double-slit fork held open behind four capability gates; all must pass or bin ENGINE-GAP (the a-priori most probable bin) |

### §1.2 — New operators (term rows; full mathematical audit in §2)

| Symbol | Name | real/phase | channel | units | class | defining source | one-line definition |
|---|---|---|---|---|---|---|---|
| σ | surface tension from ℓ_c | real | bulk | energy/area (engine-native) | derived-this-arc, CANDIDATE | `[branch #190]` bubble-physics:57,65 | gradient-energy scaling σ = c_σ·K·ℓ_c·(Δρ̄)² (c_σ=1/3 tanh); a SCALING not a coexistence surface tension; COLLIDES with σ=seed-width (§3.4) |
| ω₀ / f₀ | substrate Minnaert form | real / phase | bulk | rad/time; cyc/time | forward consistency-class | `[branch #190]` bubble-physics:95-99,105 | ω₀=(1/a)√(3K_eff/ρ_eff)=√3·c_eff/a; substrate-adapted textbook bubble-acoustics; measured f₀ lands INSIDE the forward band (+7.8%) |
| Z_eff(A²) | dynamic impedance + three realization classes | real / phase | EM-transverse / impedance plane | Ω | canonical-rendered (Op14) + new taxonomy | `[branch #188]` `dark-sector-response-characterization.md:197` | Z_eff=Z₀√(S_μ/S_ε); SYM / μ-only / ε-only realization classes = "the master gate"; fourth z/Z-glyph (§3.4 C-z0) |
| Z_eff(r) | impedance approach profile | real | EM-transverse | Ω | derived-this-arc | `[branch #188]` doc:225-233 | the radial Z_eff(r) approach to r_s per realization class (ε-only diverges, μ-only→0, SYM flat) |
| ∫ d ln Z/dx | the reflectivity / echo predictor | phase | EM-transverse / impedance plane | dimensionless | derived-this-arc (WKB, tagged) | `[branch #188]` doc:244-246,262 | graded-line/WKB mismatch integral; echo yes/no inherits the realization class; d ln Z/dx≡0 for SYM |
| H_shear / H_EM / H_bulk | dilation transfer functions | phase | per-channel | dimensionless | derived-this-arc | `[branch #188]` doc:282-285,359 | GW/line rows ride H_shear=(1−A²)^{1/4}; EM-phase rows ride H_EM=(1−A²)^{−1/2}; renders the three-speed split as frequency-domain transfer functions |
| slew | the slew spec | real | kernel (large-signal) | amplitude/time | datasheet-layer operator | `[branch #188]` doc:8,56-60 | op-amp-style large-signal rate limit imported as an ANALYSIS STYLE (not an SM number default); α-slew 2π note |
| Wr | writhe pseudoscalar (ring writhe / circuit helicity) | phase / topology | topology | dimensionless (signed) | Phase-0 observable, consistency-class | `[branch #195]` design:89-103; prereg DRAFT:30-32 | reflection-odd pseudoscalar = mean ring-writhe of the shortest closed rings; srs-R −4.087e-2, srs-L +4.087e-2 (exact sign flip), diamond 0.0 |
| — | Bishop transport (minimal-twist) | real | EM-transverse | rad/length | measurement-operator (frame pre-exists) | `[branch #195]` design:277; `chiral_lattice_dynamics.py:26,175-184` | a transverse polarization frame Bishop-transported along the 4₁ screw orbit; per-length rate not converged at Phase-0 (~9% 4-gon wobble) |
| S_ij | trivalent scatter matrix | phase | phasor / Smith | dimensionless | new Op5 instantiation | `[branch #195]` design:204,215,217 | S_ij=⅔−δ_ij, i.e. S=(2/3)J−I; SᵀS=I exactly (unitary); reduces to canon ½−δ at n=4 (§2) — joins the W6 S-cluster (§3.4) |
| F-GENUS | the topology gate | topology | topology | bin | instrument (executable) | `[branch #194]` prereg:31,124-125 | `assert_topology()` over `snap_mask` connectivity → {THREADED / NO-PENETRATION / SHELL-NEVER-FORMS}; task-name "genus gate" is a PARAPHRASE (§3.3) |
| F-TRAVEL | traveling-vs-standing discriminator | phase | topology | bin | instrument (validated) | `[branch #194]` prereg:127,179 | `assert_travel_vs_standing()`: standing plant must read w_pol=0, traveling plant w_pol=q; a probe reading w_pol≠0 on a standing plant is DISQUALIFIED |
| w_pol (F-WPOL) | poloidal-winding extractor floor | phase / topology | topology | integer | extends registry §3.6 | `[branch #194]` prereg:78,162 | reliability gate w_pol_rel>0.1, ≥16 contour samples, r≥3 cells, on a FIELD-DERIVED read torus (not a choice) — repairs the v7 A46 obstruction |
| De | the Deborah ratio (rate-lock) | n/a | n/a | dimensionless (De≈10³) | SESSION-RECORD | SESSION-RECORD (no committed anchor) | the rate-lock candidate; cited honestly as conversation-only; namespace hazard vs D13-D17 design IDs and F0d floor (§3.4) |
| C_eff(V) | cRIO saturation-onset discriminator | real | bench (EE) | F, V | first real-hardware bench prereg (DRAFT) | `[branch #181]` `crio-ceff-saturation-onset_prereg-draft.md:1-12` | NI cRIO-9014+9263+9215 DC-40 kHz 4×4 lock-in; validation-ladder-first; freezes only when Grant schedules bench time |
| tr_min | rupture witness (two-object sign-ledger) | real | bulk | engine-native | consistency-class (NOT emergence) | `[branch #189]` `annihilation-evaporation_result.md:112`; prereg:49 | per-run rupture witness (tr_min crossing r₃ / ρ̄→RHO_CAV); the two-object SIGN ledger composes exactly |

### §1.3 — New bins / verdict-classes (the night's outcome vocabulary)

| Bin | Where it fired | class | defining source | one-line definition |
|---|---|---|---|---|
| SHELL-NEVER-FORMS | v8 (FIRED — shell_cells=0 all arms) | bin | `[branch #194]` prereg:31; smoke JSON | no connected snapped shell exists → topology gate VOID; "the converged object was never a bubble" |
| DEPOSIT-DRAINED-AGAIN | v7 re-bin (ISO 3.34 / FULL 4.03 OOM) | bin | `[branch #184]` v7 result:12,172 | the deposit's net field drained ≈4 OOM below the survival gate; lock exonerated; "D13 never actually tested" |
| ROTATES-ENANTIOMORPH-ODD | v9 Smoke B | bin | `[branch #195]` prereg DRAFT:34 | signed rotation +75.5°/unit (srs-R) vs −75.5°/unit (mirror); carried with the discreteness-wobble + handedness-ambiguity limitations |
| UNDERDETERMINED-leaning-CONSISTENT | bubble-physics Minnaert | bin (compound) | `[branch #190]` bubble-physics:131; `[branch #191]` ledger:147 | measured f₀ INSIDE the forward Minnaert band, not a tight match; the lean is IN the bin name, not a silent upgrade |
| UNRESOLVED (apparatus-floor) | s11-de-novo (both legs) | bin (extends apparatus-floor skill) | `[branch #193]` result:1,17,19 | gate PASS but operating window SUB-PERIOD at the made object's scale; "a floor from a different config is invalid" |
| DEMOTED-PARTIAL | v6 (KEEP-BOTH demotion) | bin | `[branch #180]` v6 result:80,84,92 | headline ∓0.539 = by-construction accumulator ~4 OOM above net field; §§0-9 preserved; T1 mass converges stands |
| ENGINE-GAP | moving-defect double-slit | bin | `[branch #186]` prereg:123,149 | a capability gate fails → clean Rule-11 closure (NOT a failure to debug around); fork awaits a c_eff(V) self-trapping engine |
| UNRESOLVED (wrong-regime artifact) | annihilation | bin (extends regime-check skill) | `[branch #189]` result:12; prereg:49 | the encounter never happens (transport-absent, release-channel-absent, handedness-inert); this architecture cannot pose the question dynamically |
| NO-SCREENING | screened-winding probe | bin | `[LOCAL-ONLY]` `screened-winding-probe_result.md:1,14` | w_pol≡0 is a GENUINE absence, NOT an apparatus screen; written FROM evaluated gate booleans (Rule 11); UNPUSHED |
| gate-as-comment failure class | v7 process demotion | bin / failure-class | `[branch #184]` v7 result:12,195 | a frozen gate existing only as a DOCSTRING is not a gate; every prereg gate must have an executable assertion; task-name "gate-as-docstring" is a PARAPHRASE (§3.3) |
| ROUTE CLOSED (Nyquist-binding) | Nyquist-binding route | bin (Rule-12 closure record) | `[branch #192]` `nyquist-binding-route_CLOSED.md:1-9` | demolished on four independent grounds (k_C=k_max/π — factor-π below the zone edge); ⚠ ANTI-PATTERN MARKER; successor = canon's Layer-8 acceptance test |

### §1.4 — Session-record terms (no committed anchor — cited honestly)

| Term | status | note |
|---|---|---|
| De ≈ 10³ / "rate-lock" | SESSION-RECORD | grep for "Deborah"/"rate-lock" = 0 hits across all session refs (incl. local-only); the De NOUN has no committed home (its concept feeds the thixotropy LOOP-GAP link, §4(c2)) |
| "the foundry" | SESSION-RECORD | 0 hits across research/, _orchestration/, manuscript/ at all branch tips; nearest committed kin = the fab-traveler / electron-manufacturing-process-flow doc (pre-session, main) |
| "umbilical" | SESSION-RECORD | 0 hits; if Grant used "umbilical" it is conversation vocabulary — the COMMITTED home of the concept is the §6.3 sole-solid↔melt-channel claim (`[branch #187]:243`, the melt-coupling channel row above) |
| the blackness mechanism | SESSION-RECORD (scout existence committed) | `[branch #191]` ledger:39,224-227 commits the scout's EXISTENCE (READ-ONLY by design, lands only on Grant's blessing); no blackness CONTENT doc exists; prior sense = archive `59_memristive_yield_crossing_derivation.md:510` (Regime-IV) — collision watch |

> **Two staleness corrections against the settled baseline (mechanical, not Grant-queue):** (1)
> novel-objects **N9's "δL has NO committed anchor / UNVERIFIABLE"** is now STALE — δL is committed at
> `[branch #180]` v6 prereg:90-91. (2) novel-objects **N7's "[branch edatasheet, UNMERGED]"** tag is
> STALE — PR #166 is MERGED at `main`; the registry §3 rows citing `[branch edatasheet]` (the C-w w₀
> entry; the photon-w `crystal_engine` anchor) should re-tag `(main)` on next registry revision.

---

## §2 — Operator audit table (every new mathematical object + the Tellegen check)

Columns: **object | defining equation (verbatim) | units / dimensional check | derivation status |
reduction check (reduces to the canonical form in the known limit?) | where used | POWER CATEGORY.**

**Power-category basis (Grant-ratified 2026-06-11):** *"reactance as the universe's bookkeeping — in a
lossless lattice the only fundamental power category is reactive; every R is a port-local view of energy
crossing into an untracked account."* Canon anchor for the ruling: `orbital-friction-paradox.md:35`
(`clm-v6ti0v`), the Power Domain Classification table — stable orbit / electron orbital ride θ=90°,
**P_real=0, Q_reactive** (lossless LC tank); the photon is the lone **P_real** object (θ=0°, pure
travelling wave). Companion ruling **inertia-is-reactance**: `entrainment-vortex-trapping-deep-dive.md:361`
"the entrained/displaced reactive field IS the stored ½L\|A\|²; m_add ↔ L_eff" — mass is the inductive
(L-sector) reactive store. Each row below is classified **Q_reactive** (+ the conjugate pair / the
account it exchanges with) or **P_real-port-local** (+ the receiving account). `ave-power-category-check`
applied per row.

### §2.1 — The audit table

| Object | Defining equation (verbatim) | Units / dim check | Derivation status | Reduction check | Where used | POWER CATEGORY |
|---|---|---|---|---|---|---|
| σ (surface tension) | `σ = ∫[Δf0 + ½ λ_grad (dρ̄/dx)²] dx = c_σ·K·ℓ_c·(Δρ̄)²` (`[branch #190]` bubble-physics:57) | [K]·[ℓ]·[ρ̄]² = (energy/vol)·length = **energy/area** ✓ | derived-this-arc, **CANDIDATE** | reduces to a gradient (Korteweg/couple-stress) energy; the doc's own ceiling: this is a SCALING, NOT a coexistence surface tension (`:89`) | bubble-physics σ≈0.19-0.31; death-channel coalescence bridge | **Q_reactive** — stored interface energy; conjugate pair (ρ̄, gradient stress); account = the bulk-K compression store |
| ω₀ (Minnaert) | `ω₀=(1/a)·√(3 K_eff/ρ_eff)=√3·c_eff/a; f₀=√(3K/ρ0)/(2π a)` (`[branch #190]` :95-99) | √([K]/[ρ]) / [a] = (vel/length) = **1/time** ✓ | forward consistency-class | substrate-adapts the textbook Minnaert bubble form via c_eff=√(K/ρ); measured f₀ INSIDE forward band (+7.8%) | bubble-physics f₀ check | **Q_reactive** — breathing LC resonance; conjugate pair (compression PE ↔ radial KE); the bubble IS a reactive tank |
| Z_eff(A²) | `Z_eff = Z₀·√(S_μ/S_ε), S_x=√(1−A_x²), ε_eff=ε₀S_ε, μ_eff=μ₀S_μ` (`[branch #188]` :197; `constants.py:465`) | √(Ω²)=**Ω** ✓ | canonical-rendered (Op14, `operators.md:54`) | at S_μ=S_ε (SYM) → Z₀: **recovers Op1 invariant exactly** ✓; ε-only/μ-only diverge | dark-sector BH-matrix master gate | impedance (not a power) — **sets the split**: SYM (Γ=0) → all **P_real** crosses; asymmetric (Γ≠0) → a **Q_reactive** reflected store |
| Z_eff(r) | per-class radial profile (ε-only diverges, μ-only→0, SYM flat at r_s) (`[branch #188]` :225-233) | Ω(r) ✓ | derived-this-arc (canonical-exponent flagged) | SYM → flat (Γ=0 maintained to r_s) ✓ | dark-sector approach profile | as Z_eff(A²) — the radial reading of the same split |
| reflectivity / echo predictor | `∫ d ln Z/dx` (graded-line/WKB) (`[branch #188]` :244-246,262) | dimensionless ✓ | derived-this-arc (standard WKB, tagged honestly) | d ln Z/dx≡0 for SYM → **no converged reflectivity** (no echo) ✓ | dark-sector echo yes/no | the echo IS the **Q_reactive** near-field store reading; transmitted remainder = **P_real** into the far account |
| H_shear / H_EM / H_bulk | GW/line ride `H_shear=(1−A²)^{1/4}`; EM-phase ride `H_EM=(1−A²)^{−1/2}` (`[branch #188]` :359) | dimensionless transfer ✓ | derived-this-arc | at A²→0 all H→1 (free space) ✓; renders registry §1 three-speed split as transfer functions | dark-sector derating/observed-frequency curves | dilation of the **Q_reactive** store's resonant frequency (per channel) — \|H\|² is the power-ratio view |
| slew spec | large-signal rate limit (op-amp idiom); α-slew 2π note (`[branch #188]` :8,56-60) | amplitude/time ✓ | datasheet-layer operator (analysis style, adapted) | α-slew ν_slew=(α/2π)ω_Compton is the canonical refresh rate (consistency) | dark-sector slew band comparison | rate limit on the **Q_reactive** store's slewing (dV/dt at the boundary); the parametric refresh is reactive |
| Wr (writhe pseudoscalar) | reflection-odd ring-writhe; srs-R −4.087e-2, srs-L +4.087e-2, diamond 0.0 (`[branch #195]` design:89-103) | dimensionless (signed) ✓ | Phase-0 observable, consistency-class | exact sign-flip under mirror; box-independent (a clean pseudoscalar) ✓ | v9 Smoke-B chirality discriminator | **n/a (topological invariant)** — a LOCKED conserved charge (helicity), not a pumped power (`ave-conserved-vs-pumped`) |
| Bishop transport | transverse frame Bishop-transported along the 4₁ screw orbit (`[branch #195]` design:277; `chiral_lattice_dynamics.py:175-184`) | rad/length ✓ | measurement-operator (the Bishop FRAME pre-exists at `electron_trefoil_visuals.py:94`) | per-length rate does NOT converge at Phase-0 (~9% 4-gon wobble) — deferred to vector-TLM Phase-1 | v9 optical-activity measurement | **n/a (measurement frame)** — reads the reactive (EM-transverse) channel; no power of its own |
| S_ij (trivalent scatter) | `S_ij = 2/n − δ_ij`, n=3: `S_ij=⅔−δ_ij`, `S=(2/3)J−I` (`[branch #195]` design:215) | dimensionless ✓ | new Op5 instantiation (`operators.md:45`), audited | **at n=4 → ½−δ_ij = canon `k4_tlm.py:64-93` diamond junction EXACTLY** ✓; SᵀS=I (eigenvalues ±1) | v9 trivalent net scatter | **Q_reactive (lossless)** — SᵀS=I ⇒ UNITARY ⇒ NO R port; conjugate pair (V_inc, V_ref); the unitarity IS Grant's "only reactive in a lossless lattice" |
| F-GENUS (topology gate) | `assert_topology()` over `snap_mask` connectivity → {THREADED/NO-PENETRATION/SHELL-NEVER-FORMS} (`[branch #194]` :31) | bin ✓ | instrument (executable, real topology code) | genus-0 sphere → genus-1 torus under threading | v8 threading test (fired SHELL-NEVER-FORMS) | **n/a (instrument)** — a geometry decider, not an energy term |
| F-TRAVEL | `assert_travel_vs_standing()`: standing→w_pol=0, traveling→w_pol=q (`[branch #194]` :127) | bin ✓ | instrument (validated, banked) | a probe reading w_pol≠0 on a standing plant is DISQUALIFIED | v8 traveling-vs-standing heart | **n/a (instrument)** — discriminates the carrier of a winding |
| w_pol (F-WPOL) | reliability gate w_pol_rel>0.1, ≥16 samples, r≥3, FIELD-DERIVED torus (`[branch #194]` :78) | integer winding ✓ | extends registry §3.6 extractor floor | the field-derived torus repairs the v7 A46 N-collapse (~7 OOM) | v8/v9 winding reads | **n/a (topological observable)** — reads the locked (2,3) charge |
| C_eff(V) (cRIO) | `C_eff = C₀/S(V/V_y)` saturation-onset (`[branch #181]` :1-12; canon `vacuum varactor` `circuit-theory/index.md:21`) | **F** ✓ | first real-hardware bench prereg (DRAFT, not frozen) | reduces to canon's metric varactor C_eff(V)=C₀/√(1−(V/V_y)²) | cRIO EE-bench discriminator | **Q_reactive** — capacitive (E-sector) store; conjugate pair (V, Q); validate on a known nonlinear cap first |
| tr_min (rupture witness) | per-run tr_min crossing r₃ / ρ̄→RHO_CAV (`[branch #189]` prereg:49) | engine-native scalar ✓ | consistency-class (explicitly NOT emergence) | the two-object SIGN ledger composes exactly | annihilation rupture detection | **n/a (witness scalar)** — flags the bulk store's rupture into the cavitation account |

### §2.2 — Tellegen's theorem: CHECK CANON → VIRGIN (named EE-first import candidate)

**Result: VIRGIN.** `grep -rniE 'tellegen'` over `manuscript/`, `research/`, `src/`, `docs/` at
`origin/main f6ffd98d` = **0 hits** (grep-confirmed this session). Tellegen's theorem is the EE-native
topological conservation law: for ANY network obeying KCL + KVL, `Σ_branches v_k·i_k = 0` **by network
topology alone, independent of the branch constitutive laws.** It is the exact formal statement of
Grant's "reactance as the universe's bookkeeping" ruling — in a lossless lattice the branch-power sum
vanishes, so every real-power port (every R) must be exactly balanced by energy crossing into an
untracked account elsewhere in the network. It also generalizes to the **quasi-power** form (one
network's voltages with another's currents), which is the natural language for the L↔C cross-sector
trades the engine already measures (`op14-cross-sector-trading.md`, ρ=−0.990). **Staged as the named
EE-first import candidate** in the §3 adjudication queue (§3.5) — NOT imported here (flag-don't-fix; a
new EE-first axiom-adjacent import is a Grant/auditor call, with its own verification chain per Rule 12).

### §2.3 — Power-category synthesis (reactance-is-bookkeeping, applied)

Reading the table as one ledger makes the night's physics legible in one sentence: **every object the
engine BUILDS is Q_reactive; the only P_real objects are the radiating/transmitting ports, and each
names its receiving account.**

- **The made object's mass is Q_reactive (inertia-is-reactance).** The rotation column's converged mass
  (`E_V^cons≈12.9`, v6) is an inductive store, the same class as the electron's `Q_react=m_ec²·α`
  reactive shell (`orbital-friction-paradox.md:35`) and the orbital LC tank. A "v6-class mass has no
  V-sector transport DOF" (`[branch #189]`) is the same statement: a pure reactive store does not carry
  real power.
- **The transducer deposits Q_reactive, drained as P_real into an untracked account.** The transducer's
  rigid-azimuthal deposit (∓3.6e-5) is reactive; `_lock_relax` removes exactly that mode — i.e. the lock
  is the R that ports the deposit's energy into the undersampled-mode account (the DEPOSIT-DRAINED-AGAIN
  bin is this ledger entry made explicit: ≈4 OOM into the drain).
- **The receiving accounts, named (per the ruling):** R_rad,L → **the far field** (the radiated dark
  wake); a matched boundary (Γ=0, SYM Z_eff) → **the transmitted channel** (the melt, when the boundary
  is the solid↔melt interface); thermalization/dephasing (v7's 3→1 decohere; the De rate-lock) →
  **undersampled / untracked modes.** S_ij being unitary (no R) is the lossless-limit statement: a clean
  shunt node has NO receiving account — all energy stays reactive.

---

## §3 — The conflict / adjudication queue for Grant

Everything here is **surfaced, not resolved** (flag-don't-fix). Both records of every conflict are
quoted verbatim so the tension is visible without reframing either side. Grant adjudicates the framing
calls (§3.1, §3.5); the auditor lands the bin/term harmonizations (§3.2–§3.4) as registry §4 additions.

### §3.1 — THE BIG ONE: the srs (z=3) vs diamond (z=4) lattice collision

v9 (`[branch #195]`) builds a **chiral trivalent (degree-3) srs net**. `origin/main` carries a
**resolution-of-record that settled against exactly this object.** Both texts verbatim:

**Side A — the canon resolution-of-record (the side v9 challenges)**
`_orchestration/2026-06-07_lattice-net-resolution.md` (main):
> *"**Resolution: z=4 diamond.** It is the net the framework actually computes on."* (line 4)
> *"The computational weight is **entirely z=4** — λ_G=4/21 → α, the foreword Lorentz-suppression, the
> trampoline moduli are **all computed on diamond; no z=3 computation exists.** The z=3 'srs' leaves are
> **unbacked numerology — the outliers.**"* (Conclusion 1)
> *"Chirality = a `k_χ` Cosserat order-parameter on the diamond … The cold lattice is achiral;
> chirality is **excited**."* (Conclusion 3)
> *"**Engine action:** none — the engine is the grounded choice. **Do NOT rebuild on z=3 srs** (would
> invalidate the α + Lorentz chains)."* (line 24)

**Side B — the v9 design's own flag (it quotes Side A and does not reframe it)**
`[branch #195]` `genesis-v9-chiral-lattice_design.md:§0`:
> *"This is surfaced for Grant, not resolved here. Phase-1 MUST NOT be frozen until this is adjudicated."*
> Two honest framings, **Grant picks one**: **(A) deliberate challenge** — a passing Smoke B (signed
> optical activity per enantiomorph, zero on the diamond control) is positive structural evidence the
> srs reading carries physics the diamond cannot inject, "and the resolution's α/Lorentz-chain-
> invalidation warning becomes the explicit cost to weigh"; **(B) reconcile** — the trivalent net is a
> *model of* the excited `k_χ` decoration's geometric content, the substrate stays diamond, nothing is
> "rebuilt on z=3."

**The unpropagated canon self-contradiction sitting underneath (both readings live on main at once)**
`manuscript/common_equations/eq_axiom_1.tex:20` (main), quoted in both texts:
> *"a **chiral Laves K4 Cosserat crystal** … governed by the right-handed `I4_1 32` chiral space group,
> with **4-fold K4 nearest-neighbor connectivity** at each node."*

The Laves/`I4₁32` name implies degree-3 (srs); the stated connectivity is degree-4 (diamond). The
z4-coordination walk-back that drops the "permanently bipartite ⇒ natively chiral" non-sequitur is
**PR #143, UNMERGED** (`origin/analysis/2026-06-08-vacuum-z4-coordination-walkback @ 28026bed`), its
naming gate held for Grant. **Status: OPEN COLLISION — Phase-1 frozen pending Grant.** This audit takes
no side; it presents both records and the underlying axiom tension. The clean discriminator v9 already
built — the **signed reflection-odd writhe** (§2 Wr row: srs-R −4.087e-2 / srs-L +4.087e-2 / diamond
0.0) — is the instrument that would make framing (A) decidable IF Grant authorizes reading a passing
Smoke B as substrate evidence.

### §3.2 — The bubble→column ontology propagation list

PR #194 body (verbatim): *"the converged ~13.0-class object is a V-sector saturated seed, not a void
wrapped in a shell — the 'bubble' vocabulary inherited from v6/v7 described a structure this recipe
never builds (independently confirmed by the S11 arc's pocket_cells=0 [= PR #193])"* and *"The ontology
correction: the converged-mass 'bubble' was never a bubble — KB vocabulary re-examination queued for
promotion time."* The replacement carrier vocabulary already in the v8 prereg: **"the energized rotation
column"** (`prereg:19`), "the rotation column's axial flux must THREAD the shell" (`prereg:29`).

**Proposed Rule-12 treatment (NOT executed here — promotion-time, auditor-landed):** frozen prereg
bodies stay UNTOUCHED (Rule 11); the correction lands as a dated Rule-12 annotation at the KB/result
level, exactly as the rename-queue R1–R8 executions did.

| Site (file:line) | current "bubble" usage | proposed annotation | class |
|---|---|---|---|
| `[branch #194]` v8 prereg:29 (D16 header) | "THREAD THE BUBBLE (the superconducting-bubble step)" | Rule-12 note: "the converged object is the energized rotation column, not a void-bubble (PR #194 SHELL-NEVER-FORMS)" | frozen prereg — annotate only |
| `[branch #190]` bubble-physics doc (title + §1) | "Bubble-physics completion … the snapped shell" | Rule-12 note distinguishing the STIFFENING saturated-core breather (the measured object) from the SOFTENING cavitation void (the Minnaert object) — the §3.4 two-pockets firewall | branch doc — annotate at promotion |
| novel-objects N5 (pocket/void) | "pocket" lens spanning both EOS branches | split N5 into N5a stiffening-breather / N5b cavitation-void (the firewall is `cavitation_flow.py:28`) | report row — auditor |
| Vol-9 / KB "photon bubble" / "superconducting bubble" leaves (promotion targets) | inherited "bubble" identity | re-examine at promotion time per PR #194; the carrier term is "rotation column" | KB leaves — promotion-gated |

**Companion flag for Grant (NOT resolved):** `[branch #190]` bubble-physics §4 surfaces *"Are these the
same bubble … or two different objects whose breathing pitches merely land in the same band?"* — the
Minnaert match is **consistent-not-confirmatory**; "Do not headline it as the bubble identity's
confirmation." Surfaced, not silently resolved.

### §3.3 — Bin-language harmonization proposals

Two task-brief / PR-title names are **paraphrases** of the committed coinages (naming drift — Grant-queue
for which form is normative; flag-don't-fix, not silently unified):

| Task / PR-title term | Committed in-doc name | Anchor | Proposal |
|---|---|---|---|
| "the genus gate" | **THE TOPOLOGY GATE** / **F-GENUS** | `[branch #194]` prereg:31,124-125 (exact phrase "genus gate" = 0 hits) | adopt F-GENUS as normative (it is the executable assertion's name); "genus gate" = informal alias |
| "gate-as-docstring" | **the "gate-as-comment" failure class** | `[branch #184]` v7 result:195 (the PR title uses "gate-as-docstring") | pick ONE for the auditor's process-skill lane; "gate-as-comment" is the in-doc coinage |

**Verdict-class register proposal (a controlled bin vocabulary):** the session minted a coherent set of
outcome bins that should land as a single normative register (extends the pre-existing UNDERDETERMINED
bin from the mfg-flow/coax-ring docs). Two harmonization calls for the auditor:
- **The `UNRESOLVED(reason)` schema.** Two sub-bins fired this session — `UNRESOLVED (apparatus-floor)`
  (`[branch #193]`) and `UNRESOLVED (wrong-regime artifact)` (`[branch #189]`). Propose the normative
  form `UNRESOLVED (<reason>)` with reason ∈ {apparatus-floor, wrong-regime artifact, r-floor-VOID,
  under-resolved} so the cause is always carried in the bin name (the `ave-evidence-framing-discipline`
  pattern of carrying the lean/reason IN the name, as `UNDERDETERMINED-leaning-CONSISTENT` already does).
- **Keep the compound bin forms.** `UNDERDETERMINED-leaning-CONSISTENT` and `DEPOSIT-DRAINED-AGAIN`
  carry their lean/history in the name by design — do NOT silently flatten to the base bin (that would
  be the post-hoc upgrade `ave-evidence-framing-discipline` forbids).

### §3.4 — Term collisions (additions to the merged registry §4 ledger)

These EXTEND the registry §4 collision ledger (C-Γ, C-0.117, C-φ, C-ν, C-z0, C-ℓc, C-Park, C-L, C-w,
C-two-3s). New rows, staged for the auditor — **flagged, not renamed** (Rule 1 split candidates):

| New tag | Glyph / word | Referents (with channel) | Live? | Anchors |
|---|---|---|---|---|
| C-σ | σ | (a) surface tension `σ=c_σ·K·ℓ_c·(Δρ̄)²` (bulk) **vs** (b) Gaussian seed width σ=3.5 (`a=σ√2=4.95 cells`) **vs** (c) N3's proposed snap-state `σ_cell` — (a) and (b) collide **inside the same #190 doc** | LIVE | `[branch #190]` bubble-physics:57 vs :28,:110 vs novel-objects N3 |
| C-mirror | "mirror" | (a) chiral-AoA boundary-mirror (EM/boundary) **vs** (b) v6 passive lossy `E_absorb` sink **vs** (c) #193 "no mirror claim" (resonance-coupling sense) **vs** (d) v9 "mirror operation" (parity/reflection-odd discriminator) | LIVE (≥4 senses) | `[LOCAL-ONLY]` chiral-AoA:35,286-288 / `[branch #180]` prereg:90 / `[branch #193]` result:1 / `[branch #195]` prereg DRAFT:~40 |
| C-z0 (extend) | z/Z | the existing cluster (Z₀ impedance / z₀ coordination ≈51.25 / z_local bond impedance) gains a **fourth** member: **Z_eff** (Op14 dynamic impedance, dark-sector) | LIVE | adds `[branch #188]` :197 to the existing registry C-z0 row |
| W6 (extend) | S | the existing five-way S-cluster (S(A) kernel / Op5 [S] / S11 / S_d,S_q / S_min) gains a **sixth** member: **S_ij=⅔−δ** (trivalent scatter) | LIVE | adds `[branch #195]` design:215 to the existing registry W6 row |
| C-column | "column" | the genesis **rotation column** (Cosserat ω + bulk, engine-construct) **vs** fluid-bench **Taylor columns** (classical-fluid analog, §4) — same glyph, distinct objects | near-miss | `[branch #194]` prereg:19 vs `[branch #183]` fluid-bench §4 |
| C-De | De | the **Deborah ratio** De (rate-lock, SESSION-RECORD) **vs** the **D13–D17** design-decision IDs **vs** the **F0d** floor — Rule-1 subscripting advised at De's first committed use | near-miss (pre-emptive) | SESSION-RECORD vs `[branch #194]` D13-D17 vs floor F0d |

### §3.5 — The named EE-first import candidate: Tellegen's theorem

Per §2.2, Tellegen's theorem is **VIRGIN** in canon (grep=0). It is staged here as the named EE-first
import candidate for Grant/auditor adjudication:

- **What it imports:** `Σ_branches v_k·i_k = 0` for any KCL+KVL network, **by topology alone**,
  constitutive-law-independent — plus the quasi-power generalization (cross-network v·i).
- **Why it fits the corpus:** it is the formal closure of the Grant-ratified "reactance is the
  universe's bookkeeping" ruling (`orbital-friction-paradox.md:35`) and the natural conservation law for
  the L↔C cross-sector trades the engine already measures (`op14-cross-sector-trading.md`, ρ=−0.990).
- **Why it is NOT imported here:** an axiom-adjacent EE-first import is a Grant/auditor framing call
  (Rule 16), and any import gets its own version number + verification chain (Rule 12). Flag-don't-fix:
  staged, not landed. **Candidate prereg:** verify the engine's per-step branch-power sum vanishes
  to floor on a lossless config (a Tellegen consistency check on the K4 TLM scatter+connect), as the
  empirical entry-point before any axiom-level adoption.

---

## §4 — The three-impedance law + the α-turns-ratio framing

### §4(a) — The three-impedance law (registry-v2 LAW rows)

**THE LAW (Grant-ratified framing 2026-06-11):** *every Z / Γ / boundary symbol carries a channel
subscript henceforth.* **`Z₀` is the TRANSVERSE-EM impedance only** (`Z_EM`); it is NOT the shear or
bulk impedance. The corpus already owns the three-channel ledger (`field-symbol-registry.md:39-52`,
Rule 3) and the K≡2G bulk-vs-shear relation (`cauchy-implosion-resolution.md:14`); this makes the
subscript discipline NORMATIVE for every impedance/reflection statement.

| Channel | LAW symbol | Z formula | speed (saturation behavior) | boundary Γ at a saturated/melted wall | anchor |
|---|---|---|---|---|---|
| **EM-transverse** | `Z_EM ≡ Z₀` | `√(μ/ε)=376.73 Ω` | `c_EM=c₀(1−A²)^{−1/2}` (**rises**) | **Γ_EM=0** under SYM scaling (μ,ε scale together) | registry:45; `operators.md:41` (Op1); `electron-bh-isomorphism.md:24` |
| **Shear (deviatoric)** | `Z_shear` | `ρ·c_shear=ρc₀(1−A²)^{1/4}` | `c_shear=c₀(1−A²)^{1/4}` (**freezes**) | `G→0 ⇒ Z_shear→0 ⇒ ` **Γ_shear→−1** (perfect reflector) | registry:46; `operators.md:56` (Op16); `electron-bh-isomorphism.md:30-34` |
| **Bulk-longitudinal** | `Z_bulk` | `ρ·c_bulk` (K≡2G_vac) | `c_bulk=c₀√(1+ρ̄/(1−ρ̄²))` (**freezes at ρ̄_cav**) | `c_bulk→0 at snap ⇒ Z_bulk→0 ⇒ ` **Γ_bulk→−1** (sonic-horizon reflector) | registry:47; `cauchy-implosion-resolution.md:14`; engine-scale `bubble-physics:107` |

The corpus has the EM row right everywhere, the shear row right in the *mechanism* but mislabeled (§4b
#3), and the bulk row **unwritten at the astrophysical-leaf level** (§4b AMBIGUOUS). The three-valued
boundary contradiction (§4d) is exactly the absence of these subscripts.

### §4(b) — The impedance-gap table (Harvest D: MIS-SCOPED + AMBIGUOUS)

**flag-don't-fix** — each carries a proposed Rule-12 channel-subscript correction for the Grant queue;
none is applied here. (verify-before-cite catch: the de-Broglie anchor is `:48`, not the Harvest-D
draft's `:46-47` — line drift, corrected this session.)

**MIS-SCOPED (shear/bulk physics written with the EM `Z₀`):**

| # | Site (verbatim) | the mis-scope | proposed Rule-12 correction (channel the physics indicates) |
|---|---|---|---|
| 1 | `invariant-gravitational-impedance.md:11,25-28`: "Gravitational waves are **transverse inductive shear waves**" … then `Z(r)=√(μ_eff/ε_eff)≡Z₀ ⇒ Γ=0` | derives GW reflectionlessness from the **EM** constitutive pair | the GW reflection is governed by `Z_shear=ρ·c_shear`, and `c_shear` FREEZES under saturation → `Γ_shear≠0` is NOT excluded by the EM algebra. Subscript `Z→Z_shear` |
| 2 | `gw-impedance-perturbation.md:9-15`: "The passing GW strain h perturbs the local vacuum impedance: `δZ = Z₀·h`" | GW (shear) strain written as a perturbation of the **EM** `Z₀` | `δZ_shear = Z_shear·h`; also internal tension with #1 (symmetric scaling leaves `Z₀` exactly invariant vs `h` modulating it linearly) — the channel subscript is what disambiguates |
| 3 | `electron-bh-isomorphism.md:30-34`: "perfect reflector for shear waves — **NOT through impedance mismatch (Γ)**, but through the phase transition that eliminates the shear restoring force" | the leaf has the MECHANISM right (`G_shear→0`) but DENIES the impedance reading — because its `Z` symbol is EM-scoped | by Op3 in the shear channel `G_shear→0 ⇒ Z_shear=√(ρG)→0 ⇒ Γ_shear→−1`: the "perfect reflector" **IS** a shear-channel mismatch. Write `Γ_shear=−1` (the leaf's own solid–liquid-boundary analogy is exactly `Z_shear→0`) |
| 4 | `03_pin_port_configuration.tex:146,183`: "`Z₀=√(μ/ε)` is invariant: `Γ=0` at every interior point" AND "`c_shear=c₀√S` … `c_EM=c₀/S`" in the SAME leaf; ":183 surrounding `Z₀≈376.73Ω` forms a `Γ=−1` mirror" | the datasheet port spec is EM-only; the split speeds in its own sentence break the all-channel `Γ=0`; the `Γ=−1` wall is the **bulk** acoustic wall quoted at the EM value | add `Z_shear` and `Z_bulk` port rows to the datasheet; the confinement `Γ=−1` mirror is `Z_bulk→0` (engine: `bubble-physics:107`), not the EM `Z₀` |
| 5 | `de-broglie-standing-wave.md:48`: "the cavity is formed by **Transverse Shear Waves** (photons **or gravity waves**) … perfectly impedance-matched to empty space (`Z = 377 Ω`)" | photon (EM, `Z₀` correct) and gravity wave (shear, `Z_shear=ρc_shear`) merged into one class at the EM impedance | subscript the one clause: gravity wave = `Z_shear` (the rest of the leaf, the bulk-acoustic matter-wave section :50, is the corpus's BEST channel-scoped exemplar) |

**AMBIGUOUS (the channel the physics indicates is absent at the leaf):**

| Site | the gap | channel the physics indicates |
|---|---|---|
| `manuscript/ave-kb/vol3/{cosmology,gravity}` BH/horizon leaves | NO leaf states `Z_bulk` at `r_s`/`r_sat` (grep-confirmed; only `cauchy-implosion:14` K≡2G and heliopause acoustic-matching exist) | **bulk-longitudinal**: the only corpus `Z_bulk→0 ⇒ Γ_bulk→−1` statements are engine-scale (`registry:197` snap, coax result:41, `bubble-physics:107`). The third value of the three-valued boundary is simply unwritten astrophysically — a verified absence, not an inferred one |

### §4(c) — The α-turns-ratio framing (hypothesis-class, WITH canon anchor)

**Grant-ratified framing 2026-06-11 (verbatim):** *"the turns ratio for alpha is a perfect framing
and… the energy exchange is potentially the energy contained versus the amount of energy needed in the
longitudinal mode or whatever mode the bubble is that creates the boundary layer for the Soliton."*

**The canon anchor (VERIFIED this session — the row this framing rests on):** the reactive/near-field
store = `α·m_ec²`. Verbatim:
- `orbital-friction-paradox.md:35` (`clm-v6ti0v`): electron orbital, θ=90°, P_real=0, **`Q_reactive = m_e c²·α`** = "Quantized reactive shell" (lossless LC tank).
- `[branch #166→main]` `electron-device-datasheet_draft.md:52`: "Reactive store | **`Q_react = m_ec²·α`** = the 'Quantized reactive shell' (θ=90°, P_real=0 — lossless LC tank) | canonical | `orbital-friction-paradox.md:35`".
- the companion port reading: **per-cycle reactive leak `1/Q = α`** (Sommerfeld coupling strength, `theorem-3-1-q-factor.md:81`) with self-impedance **`Q = α⁻¹ = 4π³+π²+π`** (`ch8-alpha-golden-torus.md:115-117`).

**The framing (hypothesis-class — the unification, NOT the canonical store):** α is the transformer
**turns-ratio-squared / k²** between the **transverse content** (primary) and the **longitudinal
boundary-layer mode** (secondary, "the mode … that creates the boundary layer for the Soliton"):
$$\frac{E_{boundary}}{E_{content}} = \alpha = k^2 = \left(\frac{N_{sec}}{N_{pri}}\right)^2 = \frac{1}{Q}.$$
This unifies the three extant α readings as ONE transformer: the **`Q⁻¹` (port / per-cycle leak)**
reading, the **`k²` (coupling-coefficient)** reading, and the **turns-ratio (windings)** reading are
three views of the same primary↔secondary coupling. Consistent with the power-category ledger (§2.3):
both stores are reactive; α is the reactive transfer ratio between them, not a loss.

**The named test (prereg-CANDIDATE — stated, NOT derived here):** derive `E_boundary` from the
boundary-layer mode's **own** stored energy — the standing **longitudinal V** of the soliton wall (the
"3", `Z_bulk` channel) — and check `E_boundary/E_content = α` **forward** (compute-then-compare, Rule 11,
no retrofitting). A forward pass is consistency-class (α is CODATA-anchored at the inputs); only a
parameter-free derivation of the turns-ratio from the wall geometry would be emergence-class — and that
must clear the §5 reconstruction-stop fence first. **Owner: a future prereg, own version + verification
chain.** Not derived in this audit.

### §4(c2) — The saturable-core matter-creation analogue + THE LOOP GAP

**Grant-proposed 2026-06-11 (verbatim):** *"we should have direct EE analogues for matter creation in
the forms of potentially a ferrite inductor saturating its core."* The full mapping:

| Ferrite/saturable-core EE behavior | AVE matter-creation analogue | canon status |
|---|---|---|
| linear region (low H) | **Regime I** (sub-yield, `A≪1`) | EXISTS — `regimes-of-operation.md:29`; the four-regimes ladder |
| core saturation (B flattens) | **the snap / pair production** | EXISTS — Axiom-4 kernel `S(A)`; `B_snap`/`V_snap`/Regime IV signatures (`CLAUDE.md:58`) |
| inrush current spike (at energize) | **the birth pulse** (N4 vent) | NEW-this-framing — maps the inrush transient to the genesis birth pulse |
| **remanence `B_r`** (B at H=0) | **mass** — the persistent state needing NO drive | **NEW-this-framing — and the GAP (below)** |
| **coercivity `H_c`** (H to zero B) | **the annihilation threshold** | NEW-this-framing — the death-channel coercive field |
| **B-H loop area** | **latent heat** (both directions) | NEW-this-framing — the loop area = energy dissipated/stored per creation-annihilation cycle |
| transformer-rating overdrive (exceed VA) | **creation as exceeding the α turns-ratio's linear range** | NEW-this-framing — ties to §4(c): matter-creation = driving past the α-transformer's linear regime |

**CHECK CANON — what already exists vs new-this-framing.** EXISTS: the vacuum **varactor** `C_eff(V)`
(electric sector, `circuit-theory/index.md:21`); the **relativistic inductor** (magnetic sector, the
SAME Axiom-4 kernel with `V→I`, `V_yield→I_max` — "projections of the single Axiom 4 kernel onto the
magnetic and electric sectors", `vol4/claim-quality.md:129`); the **ferrite-below-Curie** analog (μ-side
frozen, `delta-strain-cosmic-tcc.md:101-105`); the four-regimes ladder; `B_snap`. NEW: the explicit
**B-H LOOP** reading — remanence↔mass, coercivity↔annihilation, loop-area↔latent-heat — and the
inrush↔birth-pulse, overdrive↔creation maps.

**⚠ THE LOOP GAP (the diagnosis — hypothesis-class but sharp, with a hard canon anchor).** Canon's
kernel **`S(A)=√(1−A²)` is the ANHYSTERETIC curve** — a saturation curve with **NO loop → no remanence
→ the medium as canonically rendered cannot RETAIN matter, only store it under drive.** The canon
anchor is exact and explicit: `06_spice_verification_manual.tex:127-133` — the "**Memristor
(Thixotropic Hysteresis)**" is *"documented but not implemented"*, and *"the lattice responds purely
elastically — **the hysteresis loop has zero enclosed area.**"* This is **exactly** the nine-architecture
genesis record: every made object stores mass under drive (the reactive `Q_react`) but no architecture
RETAINED it without a quantizer/lock (v6/v7 `w_pol≡0`, the v7 `3→1` decohere, v5 snap = CLIP /
hysteresis-by-bookkeeping). **The constitutive loop is THE missing piece** — remanence is the
zero-drive persistence the kernel cannot currently express. And the canon memristor's `τ_relax=ℓ_node/c`
RATE parameter ties the two candidates together: **the rate-lock / thixotropy candidate and the ferrite
loop are plausibly ONE mechanism** (real ferrite loops ARE rate / domain-wall dynamics; canon's missing
loop is literally named "Thixotropic Hysteresis"). The De≈10³ rate-lock (§1.4, SESSION-RECORD) is the
rate-dependence of this same loop.

**The bench row (consistency-class):** run a **ferrite-core B-H loop on the cRIO** as the matter-creation
analogue experiment — saturation-onset / remanence / coercivity / loop-area mapping to
genesis / mass / annihilation / latent-heat. Cross-ref the fluid-bench program (`[branch #183]` §8) and
the cRIO C_eff(V) validation ladder (`[branch #181]`); validate on a known nonlinear core first (the
cRIO discipline). Class: consistency — it characterizes the EE analogue, it does not emerge the kernel.

### §4(d) — The three-valued-boundary re-frame (candidate-resolution for Grant)

`[branch #187]` surfaced two unresolved canon contradictions: the shear-BC is **three-valued** (:233)
and BH echoes are **yes-vs-no** (:239). The channel-subscript law (§4a) dissolves the first into a
clean per-channel reading of ONE boundary — **candidate-resolution for Grant, with per-pole evidence:**

| "Pole" / view | Channel | Γ at the saturated/melted wall | evidence |
|---|---|---|---|
| **transparent (matched)** | EM-transverse `Z_EM` | **Γ_EM = 0** (DERIVED) | `Z(r)=√(μ'/ε')=Z₀` invariant under SYM scaling — `electron-bh-isomorphism.md:24`; `03_pin_port_configuration.tex:146` |
| **reflector** | shear `Z_shear` | **Γ_shear = −1** (IMPLIED, currently unwritten as Γ) | `G_shear→0 ⇒ Z_shear→0`; "perfect reflector for shear waves" `electron-bh-isomorphism.md:34` (= a shear mismatch, §4b#3) |
| **reflector / horizon** | bulk `Z_bulk` | **Γ_bulk = −1** (engine-scale; astrophysically UNSTATED) | snap `Z_bulk=ρc→0` `registry:197`; `bubble-physics:107`; the §4b AMBIGUOUS gap |

**The candidate resolution:** the "three-valued boundary" is **three channels' views of ONE boundary** —
EM-transparent (Γ_EM=0), shear-reflecting (Γ_shear=−1), bulk-reflecting (Γ_bulk=−1). The contradiction
is an artifact of the missing channel subscripts; under the §4(a) law it dissolves. The **BH-echo
yes/no** then inherits the realization class (§2 reflectivity row): the echo is **EM-channel NO**
(Γ_EM=0, transparent) but **shear/bulk-channel YES** (Γ=−1) — so "does the BH echo?" is itself a
channel question, and the `[branch #187]` FLAG-2 contradiction is the same missing-subscript artifact.
**Surfaced as candidate-resolution; the BH-echo and shear-BC contradictions are NOT closed here** —
Grant adjudicates whether the channel-subscript reading is the resolution or whether a deeper physics
distinction remains (flag-don't-fix).

---

## §5 — The consistent-language conclusions digest

_(section pending — next commit)_
