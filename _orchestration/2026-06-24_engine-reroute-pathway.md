# PATHWAY (RE-ROUTED) — the boundary/topological-localization engine to the α-free chord

**Created:** 2026-06-24 · orchestrator-tracked · implementer lane.
**SUPERSEDES:** [`2026-06-23_full-engine-pathway.md`](2026-06-23_full-engine-pathway.md) — its **Stage 2 ("THE NATIVE CAGE")** is 🔴 **FALSIFIED** (MODE-III DISPERSE, energy-conservation-certified), so its **S0✅→S1✅→S2→S5→S6 critical path is DEAD**. Source of the falsification: [`../research/2026-06-24_engine-stage2-native-cage_result.md`](../research/2026-06-24_engine-stage2-native-cage_result.md).
**Scope-lock (read first):** This re-route changes the **localization mechanism only**. It is **NOT** "the electron is falsified." **mass = A1 (PR#260) is UNTOUCHED.**

---

## 0. What died / what is kept

### DEAD (do not rebuild)
- **The bulk self-trap cage.** A seeded localized precursor does NOT self-trap at A→1 on the native K4 stencil WITH c_eff(V) — it disperses (MODE-III, rel_drift −8.8e-6, energy-conservation-certified). The bulk self-focusing well was a **Cartesian-grid artifact**, not a substrate property.
- **The old critical path** S2→S5→S6 that hung the chord off the bulk-self-trap cage as the load-bearing localizer.
- **The "autonomous bulk self-focusing well"** as the pin for the A1 core. Per the falsification doc forward statement (`../research/2026-06-24_engine-stage2-native-cage_result.md:5`, verbatim):
  > "the A1 core is pinned by the (2,3) winding + `H_couple` + the Γ=−1 boundary cavity, **not** by an autonomous bulk self-focusing well."

### KEPT (the re-route stands on these)
- **mass = A1 (PR#260).** The A1 dilatation IS the mass; settled independently of the localization mechanism. UNTOUCHED by the Stage-2 falsification.
- **Boundary/topological localization.** Localization is now BOUNDARY (the Γ=−1 cavity) + TOPOLOGICAL (the (2,3) winding + `H_couple`), NOT bulk self-focusing.
- **The legit-`H_couple` class.** The conservative, skew-Hermitian, ω-independent circulator class (norm-preserving cross-sector coupling) survives — it is the topology/coupling pin, distinct from the falsified bulk well.
- **The one-time buckle (snap-overshoot formation).** Formation overshoots the drive past the A²=1 cap, sheds once, settles — a droplet pinch-off, NOT a steady-state bulk well.
- **The α-clean discipline from Stage 0** — guard triad, the SOLE Q-extractor (`ringdown_Q`, never the golden-torus closed form), the literal scrubber, the 117–157 landing-zone gate, **κ̃=6/5 not κ_chiral=α·κ̃**.

---

## 1. The operating point + the unifying notation (settled this session)

- **Operating point = V_snap** (A²=1; Grant-ruled), with a **snap-overshoot formation refinement**: formation overshoots the drive past the A²=1 cap, sheds once, settles (droplet pinch-off). This is the formation FORK that S3 carries (snap vs gentle-trapping).
- **The biquaternion is the unifying NOTATION** (echo-class, canonized to nothing new — it is a bookkeeping isomorphism, NOT a new substrate primitive): scalar grade = mass, complex coeff = phasor, unit-quaternion = SU(2) = spin-½, vector/bivector = E/B.

### ⚑ COORDINATE-CATEGORY CAVEAT (load-bearing — standing constraint for the whole program)
**spin-½ (real-space 720° SU(2) on the unknot BODY) ≠ the (2,3) winding (phase-space Clifford-torus).** These are TWO DIFFERENT "2"s. Keep them separate; do **NOT** conflate them. Conflating them is the **(2)×(2)=4 double-count** error. Any test or notation that touches both must declare which "2" it is measuring, and in which coordinate space (real-space body vs phase-space Clifford torus). Per A46: a phase-space corpus claim must be tested in phase-space coordinates; a real-space lattice-Cartesian measurement compared against a phase-space prediction is uninformative.

---

## THE CENTRAL GUARD — α-circularity (gates the whole chord program)

Every unit bridge in `constants.py` routes through m_e / e / ℏ:
- `L_NODE = ℏ/(m_e·c)`  (`src/ave/core/constants.py:278`, verified 2026-06-24)
- `V_SNAP = m_e·c²/e`  (`src/ave/core/constants.py:451`, verified 2026-06-24)
- `NATIVE_TO_SI_ENERGY = m_e·c²`  (`src/ave/core/constants.py:397`, verified 2026-06-24)

So **ANY boundary 𝓜/𝓠/𝓙 → SI extraction returns CODATA BY CONSTRUCTION** = an instance-bake **ECHO** (Class C consistency at best, never Class D emergence). The α-free chord is reachable **ONLY as a DIMENSIONLESS RATIO the substrate fixes WITHOUT routing through L_NODE / V_SNAP / M_E.**

### FORBIDDEN re-poses (standing — do not re-open)
- **"derive Q=137 / 1/α from the loaded port"** is adjudicated **CIRCULAR** (gate `wmighcz1z`). The **Q=137 slot stays EMPTY** (anti-substitution, Rule 12 — do not refill the slot with a new unverified hypothesis).
- **M/Q/J → SI** as the chord decider is circular (routes through the m_e/e/ℏ bridges above). The chord decider MUST be an α-FREE dimensionless ratio.

---

## 2. The stages

> Convention: each stage carries its make-or-break (the pre-stated falsifier) and its validate-on-known (the known-good cross-check). Status reflects 2026-06-24.

| # | Name | Make-or-break | Validate-on-known | Status |
|---|---|---|---|---|
| **L0** | **α-clean host de-risk (HARD-STOP)** | the winding-host chord path is α-clean: the import-guard fires live (inject ALPHA → trips), κ̃=6/5 not α·κ̃, no 137-echo Q-form reachable | guard triad mirrors `graded_vacuum_network.py:108–114` (proven-live precedent); the literal scrubber + 117–157 landing-zone (Stage-0 precedent) | **THIS PR** |
| **S1** | **the (2,3) winding as a SEPARATE conserved DOF** | a dynamical winding-TRANSFER + winding-CONSERVATION gate (this upgrades "A1-sustains-rotation" from legitimate-CLASS to REAL) | winding integer is conserved under evolution; transfer between two solitons conserves total winding | **UNBUILT — the key make-or-break** |
| **S2** | **`H_couple` keeping ω independent** | the conservative skew-Hermitian circulator transfers norm-preserving while ω stays independent (no frequency pull) | DUAL canary: \|dH/H\|<1e-8 AND the \|L\| pump canary; norm-preserving generator | UNBUILT |
| **S3** | **the Γ=−1 boundary cavity** (confinement) | confinement at the operating point V_snap; the snap-overshoot formation fork resolved (snap vs gentle-trapping) | the Γ=−1 wall reaches −1 natively (vs the Cartesian base-crack clip to ≈−0.45) | UNBUILT |
| **S4** | **the boundary-observable extractor** 𝓜/𝓠/𝓙 | **chord-decider = an α-FREE DIMENSIONLESS RATIO** (NOT M/Q/J→SI, which is circular) | the ratio is finite, substrate-fixed, and does NOT route through L_NODE/V_SNAP/M_E | UNBUILT |

### Stage detail

**L0 — α-clean host de-risk (HARD-STOP).** The first stage, this PR's build (Task B). GOAL: establish that the winding-host's CHORD PATH is α-clean. The re-route found `cosserat_field_3d.py` α-contaminated on the readout path (ALPHA import `:56`, `KAPPA_CHIRAL_ELECTRON = ALPHA·κ̃` `:131`, the golden-torus closed-form Q `extract_quality_factor` `:2422` returning 137.036 at R·r=¼). De-risk: stand up an α-stripped host for the winding DOF that imports ONLY the α-free symbols, carrying the ported guard triad + scrubber + landing-zone. **If the host CANNOT be made α-clean → HARD-STOP, report (do not paper over).**

**S1 — the (2,3) winding as a SEPARATE conserved DOF.** In the full k4_cosserat field engine, the winding must have its **own field / momentum / LC**, NOT be downstream of the A1 (V_inc, V_ref) phasor — this is the **genesis-24 guard** (do NOT wire the winding into the A1 phasor; that is the double-count). Currently the winding is only a real-space holonomy SIGN + a static linking integer; S1 makes it a **dynamical, conserved** DOF. **Make-or-break: a dynamical winding-transfer + winding-CONSERVATION gate** — this is the gate that upgrades "A1-sustains-rotation" from a legitimate CLASS (asserted) to REAL (derived). **This is the key make-or-break of the whole re-route.**

**S2 — `H_couple` keeping ω independent.** The conservative skew-Hermitian circulator. Cross-sector coupling that is norm-preserving and leaves ω independent. ⚑ FLAGS: the **indefinite-trilinear-detonates** risk (an indefinite trilinear coupling is unbounded-below and detonates — must stay skew-Hermitian/bounded); the **unratified TKI-transducer** for EM↔mechanical (the topological-Kirchhoff-impedance transducer that bridges the EM and mechanical sectors is NOT yet ratified — flag, do not assume).

**S3 — the Γ=−1 boundary cavity.** Confinement as a BOUNDARY condition (Γ=−1 impedance short), NOT a bulk force term (substrate-native-check Checkpoint 10: render saturation/confinement as a boundary Γ, not a bulk energy/force, which is singular at the wall and detonates). The operating point is V_snap. The snap-overshoot formation fork (snap vs gentle-trapping) is resolved here.

**S4 — the boundary-observable extractor 𝓜/𝓠/𝓙.** The chord-decider. **It MUST be an α-FREE DIMENSIONLESS RATIO** — NOT M/Q/J → SI (which is circular by the central guard above). This is where the chord-vs-echo verdict is rendered.

---

## 3. The critical path

**L0 (host de-risk, HARD-STOP) → S1 (the winding DOF) → S2 (`H_couple`) → S3 (Γ=−1 cavity) → S4 (α-free ratio chord-decider).**

- **L0 is a HARD-STOP gate:** if the winding host cannot be made α-clean, the whole chord program is circular before it starts. This PR clears (or stops) L0.
- **S1 (the winding-DOF) is THE key make-or-break.** The legitimacy of "A1-sustains-rotation" is currently a CLASS claim (asserted). Only a dynamical winding-transfer + conservation gate upgrades it to REAL. If the winding cannot be a separately-conserved DOF (i.e. it collapses back into being downstream of the A1 phasor — the genesis-24 double-count), the boundary/topological-localization re-route fails at its load-bearing joint.
- **S2** is the most fragile after S1 (the indefinite-trilinear-detonates + unratified-TKI-transducer risks).
- **S4** is the chord's false-zero / circularity trap (the α-free-ratio discipline lives here).

---

## 4. Standing constraints (carry through every stage)

1. **The α-circularity guard** (Section "THE CENTRAL GUARD" above): the chord is reachable ONLY as a dimensionless ratio that does not route through L_NODE/V_SNAP/M_E.
2. **The forbidden re-poses:** no "derive Q=137 from the loaded port" (gate `wmighcz1z`); the Q=137 slot stays EMPTY; no M/Q/J→SI as the chord decider.
3. **The coordinate-category caveat:** spin-½ (real-space 720° SU(2) on the unknot body) ≠ the (2,3) winding (phase-space Clifford torus). Two different "2"s; do not conflate (the (2)×(2)=4 double-count).
4. **The genesis-24 guard:** the winding gets its OWN field/momentum/LC; it is NOT wired into the A1 (V_inc, V_ref) phasor.
5. **The α-clean discipline:** κ̃=6/5 not α·κ̃; `ringdown_Q` the sole Q-extractor; the golden-torus closed-form Q (`cosserat_field_3d.py:2422`) is EXCLUDED from the chord path; the guard triad + literal scrubber + 117–157 landing-zone gate stay green.

---

## 5. Provenance / verification

All cited file:line verified by 2-pattern grep on `origin/main` @ `31d0ac43` (2026-06-24):
- `src/ave/core/constants.py` :278 (L_NODE), :397 (NATIVE_TO_SI_ENERGY), :451 (V_SNAP) — all route through M_E/e/HBAR. ✓
- `src/ave/topological/cosserat_field_3d.py` :56 (import ALPHA, V_SNAP), :94 (KAPPA_TILDE_ELECTRON=6/5, the α-free form), :115 (`kappa_chiral_from_topology` default `alpha=ALPHA`), :131 (KAPPA_CHIRAL_ELECTRON=ALPHA·κ̃), :2422 (`extract_quality_factor` closed-form 137-echo). ✓
- `src/ave/solvers/graded_vacuum_network.py` :108–114 (the import-guard triad to port). ✓
- `research/2026-06-24_engine-stage2-native-cage_result.md:5` (the forward statement). ✓
