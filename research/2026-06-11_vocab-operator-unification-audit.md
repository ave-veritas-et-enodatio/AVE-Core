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

_(section pending — next commit)_

---

## §3 — The conflict / adjudication queue for Grant

_(section pending — next commit)_

---

## §4 — The three-impedance law + the α-turns-ratio framing

_(section pending — next commit)_

---

## §5 — The consistent-language conclusions digest

_(section pending — next commit)_
