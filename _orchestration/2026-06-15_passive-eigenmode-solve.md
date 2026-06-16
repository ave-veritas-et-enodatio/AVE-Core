# Passive winding-protected electron eigenmode — the structural keystone (ORCHESTRATION)

> **STATUS: 🔴 NEGATIVE-A REFUTED by the adversarial-verify panel (`ww03eo0v5`) — it is a FALSE
> NEGATIVE (under-resolved seed + a defective G1 gate). The keystone is STILL OPEN. Held for Grant on
> a corrected re-run + the wall/winding co-resolvability framing question.** Lane worktree
> `AVE-Core-eigenmode-wt`, branch `analysis/2026-06-15-passive-eigenmode-solve` off `main@40a2a2e7`.
> **main is PROTECTED — Grant merges; this lane does NOT merge. Result NOT banked** (driver branch
> `analysis/2026-06-15-eigenmode-driver`, result doc REFUTED-pending-re-run). **Panel:** dim-1
> bin-conformance **CONFIRM** (honestly *derived* — reproduces exactly, clean code, Rule-11 holds);
> dim-4 floor-not-artifact **REFUTE** (the breather EXISTS at the v14/cage eigen-resolution
> dx=0.5/~5 cells → retention 0.75; the driver ran ~3 cells/dx=1.0/4× box → disperses; AND G1 was a
> *relative* gate that passed while the sech dispersed = the t2-genesis detector-can't-certify defect
> recurring); dim-3 cage-tension **FLAG** (box-size-scoped, not coupling, not the n-exponent → cage
> gets a Rule-12 scope-annotation, not a walk-back). **The pre-flight #2 breather was REAL; the
> production under-resolved it. My last-turn "consolidating toward echo" read is RETRACTED.**
>
> **KEYSTONE REFRAME (Grant 2026-06-15):** the lane rests on **EXISTENCE + STABILITY** of the
> passive high-Q hybrid mode (PRIMARY); the measured **Q is SECONDARY** — **α is an ECHO for the
> z₀ route** (Lane-1: z₀=52 is a path-product, honest count ≈16→α⁻¹≈49; neither 137 nor 49 is an
> α-free map), so the cross-lane chord very likely will NOT fire. Don't hang the lane on Q.
>
> **GRANT RULINGS (2026-06-15):** (1) **B1 green-lit** — run the hybrid-coupled solve; B2
> ("nothing to find, negative pre-loaded") is the α-lane over-closure trap (conflates "no
> eigen-principle SELECTS the winding" [true] with "no stable mode EXISTS given the winding"
> [untested]). (2) **DROP "lossless" — the electron is HIGH-Q, Q = 1/α = 137; the residual
> leak IS α** (radiative coupling to the photon continuum). Solve for the **dissipationless,
> stable (real-eigenvalue) COUPLED mode AND measure its radiative Q**; **a finite Q≈137 is
> the POSITIVE.** Q=∞ (truly lossless) = the α=0 decoupled limit = wrong object = false
> negative. (3) Flag-C: **add radiative Q as the third detector output** (it's α). (4) Flag-D:
> shear clock `(1−A²)^{1/4}` confirmed. (5) Flag-A: hybrid (V,ω) is the right object and
> **bears on** the A1-vs-T2 sector but does **NOT resolve** it — don't let the lane claim
> resolution.

---

## §0.5 — PRE-FLIGHT RESULT (agent `a12b397d4d347be90`, 2026-06-15): option (a) DEAD + coordinate-mismatch reframe

**Verdict: option (a)-DEAD.** `CoupledK4Cosserat` reaches the magnetic-branch SIGN (Γ<0, S_μ<S_ε)
but **cannot render a stable Z→0/Γ→−1 wall**: the only Γ≈−1 reads are **clip-floor artifacts** (S_μ
pinned at the 1e-5 numerical floor, A²_μ>1 clipped) that exist **only at step 0**; the first
evolution step **runs away** (energy explodes 6–11 OOM, the A28 coupling-runaway channel). The
deepest *genuine* sub-clip wall is **Γ≈−0.45…−0.49 (Z≈0.14·Z₀)** and it does not persist.
**This independently reproduces the canonical graft-v2 "−1 NOT demonstrated, clip-bound" status
(`engine-capability-map.md:113`) on a SECOND engine.**

**Three load-bearing findings (flag-don't-fix; Grant adjudicates):**

1. **(a) dead — no stable self-consistent matter wall.** Two engines now clip-floor + run away
   toward Z→0. Accessor: `_impedance_gamma_shared` (`k4_cosserat_coupling.py:647,673`); clip source
   `cosserat_field_3d.py:585`; runaway `k4_cosserat_coupling.py:265`.
2. **The chiral term does NOT drive the wall (CONTRADICTION-flag, touches Lane 3).** Chiral OFF vs
   ON differ <10% (~0.9% perturbation; κ_chiral≈1.2α too small). The magnetic SIGN comes from the
   **structural curvature-vs-strain asymmetry** (∇×ω vs strain), NOT κ_chiral. This **contradicts
   the engine docstring** (`cosserat_field_3d.py:148-153`, which claims the chiral drive creates the
   wall) **AND** Lane-3's "matter wall = chiral-broken." → Lane-3's call; flag.
3. **COORDINATE-MISMATCH (the deepest — A46, `phase-space-coordinate-check`).** The engine reads Γ
   from **Cosserat ω-curvature**; the canonical electron winding lives in the **K4 V-tank
   `(V_inc,V_ref)` PHASE-SPACE** (`theory.md:16`, `ch8:29`). The pre-flight drove the wall with a
   **real-space (2,3) ω seed** — which the canon flags as **PROTON-family (5₁/5₂)**, NOT the
   electron — because the canonical **unknot** electron seed gave **NO wall** (Γ≳−0.10). The K4
   V-sector contributed **nothing** (`|V_inc|=0`, S_ε≡1). **So the engine's wall read is in the
   wrong sector/coordinates for the electron**, and even the DEAD verdict is about the *ω-curvature*
   impedance, not a faithful independent-μ / V-tank-phasor read this engine structurally cannot give.

**Consequence:** the platform question is NOT just "(a) vs build-(b)" — the pre-flight surfaced that
the electron's wall must be read in the **K4 V-tank `(V_inc,V_ref)` phasor**, not Cosserat
ω-curvature, AND that the ω-curvature wall is proton-family. **This re-scopes (b) and entangles the
platform with the unresolved Flag-A (which sector carries the electron's wall).** Freeze +
production driver HELD for Grant. **Decision options surfaced to Grant (2026-06-15) — see the
session thread:** (b) build cross-firewall A1-cage⊗Cosserat as-posed · (b′) re-scope the platform to
read impedance in the K4 V-tank phasor (coordinate-faithful; points back toward `crystal_engine` =
the V-tank/A1 scalar engine as the wall host, ω-carrier as the orthogonal winding) · (c) treat the
two-engine clip-floor+runaway as mounting evidence the stable Z→0 matter wall is not a renderable
fixed point (suggestive structural negative, but the coordinate-mismatch blocks banking it clean).

**GRANT RULED (2026-06-15): option 1 — run the V-tank pre-flight before any build commitment.**
NOT (c) (the cage SECH_ANCHOR already shows the V-tank self-focuses → calling a structural negative
now is the over-closure trap); NOT (b′)-sign-off-direct (the cage persistence was the `gamma_bulk_min`
PROXY, not the actual impedance Γ — the V-tank could also clip-floor; committing the build before the
cheap probe is the anti-pattern). **V-tank pre-flight DISPATCHED (agent `a9ce00462badb0d85`):** reads
the ACTUAL impedance Γ on `crystal_engine`'s sech self-focus. **Decisive either way** — STABLE Z→0 →
wall-half real → (b′) bounded build + sign-off; CLIP-FLOOR+RUNAWAY → (c), the honest structural
negative (the THIRD engine → it stops being a coordinate problem and becomes a real keystone signal).

**V-TANK PRE-FLIGHT RETURNED (agent `a9ce00462badb0d85`): a genuine BREATHER, NOT a clip-floor —
(c) is OFF, the third-engine watch-item did NOT trigger.** `crystal_engine`'s V-tank self-focuses to
a **GENUINE deep TIR wall** (Γ_TRUE≈−0.43 on **fully-UNCLIPPED** cells; amp=0.50 walls to −0.19 with
**ZERO clips ever**), **bounded, NO runaway** (max|V|≈V_yield then relaxes), **recurrent** (re-focuses
at steps 375–450). **Right sector** (A1/V-tank longitudinal Z=1/c_eff — the electron's matter wall;
distinct from pre-flight #1's wrong-sector ω-curvature). Categorically HEALTHIER than the two coupled
engines: genuine unclipped physics that BREATHES, vs a clip-artifact that DETONATES. It is **NOT a
STABLE STATIC Z→0** (the deep wall flashes, Γ_persist≈−0.03, then relaxes) — **but "stable static"
was a MIS-FRAMING.** The electron eigenmode is a **LIMIT CYCLE / BREATHER**, not a frozen core (cage
ratified "persistent breathing cage" 2026-06-13; `selftrap` limit-cycle; `master-equation.md:20` "the
A1 breather"; the high-Q "stable real-eigenvalue mode" = a **NON-DECAYING oscillation**, not a static
wall). **So the V-tank renders the RIGHT object → crystal_engine V-tank is the VIABLE wall host
(b′ confirmed).** Read the eigenmode **time-averaged/cyclic** with the **TRUE n=√S** impedance, NOT
the proxy `gamma_bulk`=S^{1/4} (**exponent-defect FLAG**, `crystal_engine.py:421-432`,
`master_equation_fdtd.py:165-168` — proxy floor −0.240 vs true −0.454, ~2×). **Surfaced to Grant:
confirm the breather/limit-cycle framing + the (b′) bounded-build anti-loophole sign-off.**

---

## §0 — Derivation target (charter + the high-Q correction)

Does a self-consistent nonlinear **STANDING** eigenmode exist — find $\psi$ such that the
saturation $S[\psi]$ forms a $\Gamma=-1$ cavity whose **own eigenmode IS $\psi$** — with the
conserved $(2,3)$ winding as a **TOPOLOGICAL boundary condition**, in the **T2 / phase-space
channel**, as a **fixed-point** (NOT autoresonant gain-driven)?

**Grant's correction to his own charter (2026-06-15):** drop **"lossless."** The electron is
**high-Q (Q = 1/α = 137)**, not lossless. The bound mode is **dissipationless and stable
(real eigenvalue)** but **radiatively COUPLED to the photon continuum**, and that residual
leak **is α**. So the object is the **dissipationless, stable, coupled mode with a finite
radiative Q ≈ 137** — NOT a Q=∞ decoupled mode (that is the α=0 limit and finds nothing).

---

## §1 — Why this is DIFFERENT from the banked *genesis* negative

`research/2026-06-14_t2-genesis-selflock_result.md` (PR #233): the ACTIVE autoresonant
self-lock tested NO-GENESIS at every $A_0$; anti-lock signature $\omega_{local}$ RISING. It
**explicitly scopes its null** to "this engine/regime/precursor." That is an **initial-value**
null and says nothing about whether the **passive fixed-point exists.**

| Axis | Genesis self-lock (banked) | THIS effort (passive eigenmode) |
|:---|:---|:---|
| Problem class | initial-value (seed→evolve→watch) | boundary-value / fixed-point |
| Energetics | active, gain loop | dissipationless fixed-point, **finite radiative Q** |
| Question | does it *dynamically form*? | does the standing mode *exist + is it stable*, and **what is Q**? |
| Winding | (not the discriminator) | **imposed** as a topological BC on the ω-carrier |
| Detector | PLV (DEFECTIVE) | self-consistency residual + stability eigenvalue + **radiative Q** |

---

## §2 — Prior-work inventory (corpus sweep `wte7dhv5v`, grep-confirmed) — NOT greenfield

### 2a — DONE and NEGATIVE
1. **Energy/S11 gradient-flow stationary-point solve → FALSIFIED.** `cosserat_field_3d.py:1453`
   `relax_to_ground_state`, `:1317` `relax_s11`; coupled `coupled_s11_eigenmode.py` (F17-K
   Phase 5). Seeded AT Golden Torus, **both objectives drift away at iteration 1**: *"GT is
   NOT a stationary point of either … selected by topological-quantization ANSATZ, not by
   gradient flow on any objective the engine knows"* (`…abcd-handoff…retrofit.md:24,50`).
   Methodology verdict: energy stationary-point = SM/QM-style energy-stationarity (Rule 6, avoid)
   (`72_vacuum_impedance_design_space.md:238` — auditor-corrected; VEM:1692 is the *replacement*
   method, not the avoid-verdict).
2. **Decoupled wave-eigensolve (V = output eigenvector) → Mode III, no bound state at ω_C**
   (`74_r7_k4tlm_lctank_run_result.md:57`; `126_…standing_wave_eigenmode…:17`; the hybrid-untried
   residue at `72_vacuum_impedance_design_space.md:158`).
3. **ABCD direct eigensolver → proposed-then-retired, no code written.**

### 2b — The ONE untried residue (the target)
**Fully-coupled HYBRID eigenmode — V≠0 AND ω≠0 simultaneously, Op14 cross-coupling the
load-bearing binder** — *"the decoupled-block solve CANNOT find it by construction … Round 8
question"* (`72_…:158`); the open Layer-8 "smallest stable soliton, m_e nowhere in inputs"
(`2026-06-11_nyquist-binding-route_CLOSED.md:54-58`).

### 2c — Constraints the imposed-BC framing clears
- **ω≡0 exact-fixed-point trap:** `W_refl` even in ω → pure-V seed can't break ω=0
  (`simulation-assumptions-audit.md:13`). The imposed winding-BC supplies the odd ω.
- **Binder-must-be-nucleated:** impose (2,3) → 91% retention; withhold → disperses
  (`option-B-discrete-emergence-result.md:348,358`). The charter imposes it. ✓

### 2d — Infrastructure (and the gap)
- **Fixed-point half EXISTS:** `eigenvalue_root_finder.py:60` `find_eigenstate`;
  `universal_operators.py:347` λ_min(S†S); `cosserat_field_3d.py:1453/1317` relax_*.
- **Stability + radiative-Q half MUST BE BUILT:** no Jacobian-eig / growth-rate / sparse-eigsh
  exists (`electron_spec_suite.py:85` is only a perturb-kick). The gradient + Verlet stepper
  to build a finite-difference Jacobian→eigvals layer DO exist.

### 2e — Winding carrier + coordinate discipline (hazard-free)
- Winding on the **independent Cosserat-ω carrier**: `fast_winding_extractor.py:165`
  `extract_2_3_omega_fast(omega, pi_omega,…)`; charge = Beltrami helicity
  (`cosserat_field_3d.py:450`); the **α-FREE** topological factor `kappa_tilde_torus(p,q)=pq/(p+q)`
  → (2,3)→`κ̃=1.2` (`cosserat_field_3d.py:98`, docstring: "α should NOT be an input"); the
  **α-bearing** coupling `κ_chiral = α·κ̃` is `KAPPA_CHIRAL_ELECTRON` (`:131`; α injected `:124`) —
  this is the line that makes α an **input** (→ echo, §5.5). **Phasor SHAPE (R/r=φ²) is
  necessary-not-sufficient** (`…transverse-selftrap-result.md:90,144`).
- **HARD HAZARD** (`master-equation.md:20`): never wire winding into `(V_inc,V_ref)` — `V_ref`
  is a read-only projection of `V` (`k4_tlm.py:346`); `w_pol=0` double-count.

---

## §3 — Discriminator (keystone = existence+stability; full bins/falsifiers in the prereg)

**KEYSTONE = EXISTENCE + STABILITY (PRIMARY, decided by F1+F2+F4); Q = SECONDARY (Grant
2026-06-15).** The lane's verdict is *does a stable passive high-Q hybrid mode EXIST* — NOT
Q-agreement (the chord won't fire, §5.5).

- **POSITIVE:** a **stable real-eigenvalue** hybrid (V,ω) mode EXISTS at ω_C; (2,3) winding
  conserved on the ω-carrier (F4, G4-gated) → eigencavity STRUCTURE real. **(The radiative Q
  is measured + binned 137/114 as a SECONDARY characterization, tagged echo — not bin-deciding.
  A stable mode with Q→∞ is still POSITIVE — "exists but radiatively decoupled" — and refutes
  bind=leak=α.)**
- **NEGATIVE-A** (no mode / disperses) · **NEGATIVE-B** (unstable / requires gain) →
  structural eigenmode fails.
- **EXCLUDED** = ONLY the explicit α=0 decoupled control "finds nothing"; **no coupled run can
  be EXCLUDED** (auditor fix — closes the relabel-a-real-negative loophole).

---

## §4 — Method skeleton (driver brief; the prereg §7 carries detail)

Substrate-native passive solve = a **wave eigenmode** with V as OUTPUT (NOT gradient descent
on energy/S11 — falsified + SM-leakage, §2a):

1. **Impose** the (2,3) winding as a topological BC on the **independent Cosserat-ω carrier**
   (clears the ω=0 trap). Never wire into `(V_inc,V_ref)`.
2. **Closed-cavity hybrid eigensolve:** Op14 saturation $z(x)=S[\psi]$ → Γ=−1 cavity rendered
   as a **boundary condition** (`substrate-native-check` CP10 — NOT a bulk term, which
   detonates); solve the coupled (V,ω) wave-eigenproblem (both sectors nonzero, Op14
   cross-coupling load-bearing) → eigenmode φ + **real** eigenfrequency ω_C (= dissipationless,
   stable).
3. **Self-consistency** $\psi\leftarrow\phi$ (winding-preserving) → fixed point (residual→0;
   reuse `find_eigenstate`/relax_*).
4. **Stability (BUILD):** finite-difference Jacobian about the fixed point → eigenvalues;
   largest real-part ≤ 0 = stable/dissipationless.
5. **Open-cavity radiative Q (BUILD):** the Γ=−1 wall is the self-induced impedance boundary;
   its **residual transmission = the radiative coupling = α**. Measure $Q = \omega_C\cdot
   (\text{stored}/\text{radiated})$. **Predict Q ≈ 137 = 1/α.** (The same Op14 cross-coupling
   that BINDS the mode also LEAKS it — bind and leak are one coupling.)
6. **`ave-conserved-vs-pumped`:** the mode must stand with NO drive; a drive-sustained state
   = NEGATIVE.
7. ω_C rides the **shear** clock `c_shear = c₀(1−A²)^{1/4}` (INVARIANT-S2), NOT the stale ½.

**Detector validation pair:** sech eigen-profile **converges** (positive control, cage
`SECH_ANCHOR`, `cage_stiffening_wall.py:109`, `cage-stiffening-wall_result.md:12`) / generic
Gaussian **disperses** (negative control, `:13`). Plus a **decoupled (α=0) control** that
finds nothing → confirms the coupling is load-bearing (the false-negative guard is real).

**Platform** (per `ave-loop-gap-harness-discipline` — auditor-flagged FIREWALL issue, resolved to
option (a), Grant framing-gate prereg §11): the A1/bulk Γ=−1 stiffening cage lives ONLY on branch-1
(`crystal_engine`) and **canonically cannot carry the Cosserat winding** (irrotational↮winding
firewall, `engine-capability-map.md` §3.1); the coupled engine cannot host that cage. Spanning both
= the non-existent "substrate-complete engine" (needs Grant sign-off). **Default = option (a):**
run on `CoupledK4Cosserat` with the Γ=−1 wall as the engine's **own impedance-Γ clamp**
(`k4_cosserat_coupling.py:674-686`), firewall-legal, **no `crystal_engine`** — at the cost that its
scalar is a `v_scalar_from_v_inc` **projection** (restricted hybrid, not the full A1-cage⊗T2; a
NEGATIVE may reflect the projection's limit). No new `*_vN` file. **Grant's call: (a) restricted vs
(b) cross-firewall full cage + sign-off.**

---

## §5 — Flags (RATIFIED by Grant 2026-06-15)

- **Flag-A — A1-vs-T2 mass sector: hybrid object ACCEPTED; bears-on but does NOT resolve.**
  Frame the solve on the hybrid (V,ω) mode. Grant's frame-reconciliation is a **SYNTHESIS, not
  corpus-verbatim** (auditor flag): **provenance = T2** (the PROVENANCE-vs-STATE ruling is at
  `photon-identification.md:11,13` — "self-trapped photon is PROVENANCE not STATE") · **state = A1**
  (`master-equation.md:20`, the A1-dilatation rest-mass). ⚠ `cosserat-mass-gap.md:108` is itself a
  T2-mass-**STATE** claim ("T2 carries the mass-gap content"), so the A1-vs-T2 tension is genuinely
  **unreconciled at the leaf-body level**; "two frames of one mode" is the lane's reading, not corpus
  text. The lane reports this as a **note**, NOT a derivation ($m_ec²$ magnitude hypothesis-class,
  `photon-identification.md:19`). **Do not claim resolution.**
- **Flag-B — SCOPING: B1 (run the hybrid-coupled solve). RATIFIED.** B2 is the over-closure
  trap. Both outcomes are results.
- **Flag-C — detector: residual + stability eigenvalue + radiative Q (3rd output = α). RATIFIED.**
- **Flag-D — shear clock `(1−A²)^{1/4}`. RATIFIED.**

---

## §5.5 — Cross-lane triangulation (the headline — Grant 2026-06-15)

**All three lanes measure/derive ONE number — the electron's α = 1/Q — at ONE operating
point.** This lane is the middle leg:

- **Lane 3 (wall)** fixes the operating point. **SHARPENED (Lane 3, 2026-06-15):** SYMMETRIC
  co-saturation = the **GRAVITY lens** (Z=Z₀, Γ=0); the **MATTER WALL requires the CHIRAL
  asymmetry** (Z→0, Γ=−1). So **K=2G is the symmetric/GRAVITY lock**, and matter *breaks* it. →
  **load-bearing for THIS lane's pre-flight: it must check the engine reaches the chirally-broken
  Z→0 wall, not the symmetric Z=Z₀ lens** (and K=2G's provenance rests on the amorphous EMT, now
  under reconstruction — a separate lane).
- **Lane 2 (THIS) solves the hybrid eigenmode at that point — and measures its radiative
  Q** (SECONDARY — α is echo, §3).
- **Lane 1 (post crystalline pivot)** is *to* derive that same Q = 1/α from geometry — **but
  that α-free leg is the OPEN frontier (Path C), NOT an established route** (auditor flag,
  correcting the headline): z₀=52 → α⁻¹≈**138.9**, **1.5% off** 137.036, and "z₀=52 is not
  physically forced" (`2026-06-08_ave-electron-definitive.md:40,45`;
  `2026-05-18_z0-first-principles-attempt-result.md:90`). Both lift-routes closed NEGATIVE.

**The orchestration move (downstream dependency of THIS lane's result):** wire Lane 2's
**measured Q** into Lane 1 as a cross-check. **The CHORD is CONTINGENT — it fires ONLY IF Lane-1
Path C closes** (α-free z₀≈51.25); a Lane-2 positive banked against the present z₀=52 leg would
**manufacture an apparent chord from two α-absorbing routes** (forbidden). This lane's deliverable
is a **measured Q** that becomes a chord *candidate*, not an immediate cross-check. (The chord also
needs ~1.5% Q precision, which the ~3.2% shear-clock ω_C systematic currently exceeds.)

> **Echo-vs-chord discipline on the Q value (`ave-discrimination-check` + memory
> `project_alpha_keystone_echo_resolved`):** `Q_TANK = 1/α` is a **calibration identity, NOT
> a derivation**. If α enters the solve as an input (the coupling `κ ∝ α`), then Q≈137 is a
> **consistency identity (ECHO)** — the lane must NOT overclaim it "derives α." The **CHORD**
> is the cross-lane agreement of two **independent** geometric routes to Q, not Lane 2 alone.
> The result must tag its Q with the echo/chord classification.

### §5.6 — Cross-lane records from the pre-flight (Grant 2026-06-15; NOT Lane-2's to resolve)

1. **First ENGINE-level Flag-A discriminant → points to A1.** Converging: Lane 3 (mass = A1 state),
   THIS pre-flight (the V-tank/A1 wall self-focuses — cage SECH_ANCHOR; the ω-curvature object is
   PROTON-family 5₁/5₂), `master-equation.md:20`, and the two-"3"s — all say **the electron's
   wall/mass is A1 (read in the `(V_inc,V_ref)` phasor); charge/spin is the orthogonal T2 winding.**
   **Evidence, NOT resolution** (m_ec² still hypothesis-class) — but **now THREE converging signals**
   (Lane 3, this pre-flight, the two-"3"s — Grant 2026-06-15), real weight toward mass=A1. Lane-2 still
   reports Flag-A as **bears-on-not-resolve** (correct).
2. **Chirality contradiction → K=2G lane: FORK CLOSING.** This pre-flight found chiral OFF-vs-ON differ
   <10%, magnetic sign present at κ_chiral=0 (structural curvature/strain split) — contradicting Lane-3's
   "Z→0 wall *requires* chirality-broken." **The K=2G lane CONFIRMED (Grant 2026-06-15): likely an
   off-K=2G artifact** — the crystal doesn't sit at the symmetric co-saturation point; **K=2G is a TUNED
   operating point, not a geometric one**, so the coupled engine reading a structural asymmetry at κ=0
   is consistent with simply not being at K=2G. Fork **closing**, in the K=2G lane (not Lane 2's).
3. **WATCH-ITEM — RESOLVED: the third-engine threshold did NOT cross.** The V-tank does **NOT**
   clip-floor (genuine breather, no runaway) — so **(c) is OFF** and the two-engine clip-floor pattern
   stays a coordinate problem (the two coupled engines read the wrong sector), not a structural negative.
   The wall-half is real on the A1/V-tank wire.

---

## §6 — Skill-selection plan

| Skill | Where | Why |
|:---|:---|:---|
| `ave-prereg` | Phase 0 ✅ | caught the non-greenfield finding |
| `phase-space-coordinate-check` | prereg + driver | winding on ω-carrier/phasor, not real-space (A46) |
| `substrate-native-check` (CP8/9/10) | driver | impose winding-BC; Γ as BC not bulk; dynamical not algebraic |
| `ave-conserved-vs-pumped` | driver + result | dissipationless fixed-point; drive-sustained = NEGATIVE |
| `consistency-vs-emergence` | result | existence/stability = emergence; Q value classified separately |
| `ave-discrimination-check` | result | **echo/chord tag on the measured Q** (don't overclaim α-derivation) |
| `pre-test-physics-check` (T7/T8) | gate ✅ | surfaced the reframe + ontology before dispatch |
| `ave-loop-gap-harness-discipline` | platform | hybrid spans crystal_engine ⊗ Cosserat; no new `*_vN` |
| `ave-driver-script-honesty` + `ave-apparatus-floor-attribution` | result | convergence/Q = physics or solver artifact |

---

## §7 — Arc + gates

| Phase | Gate | Owner | State |
|:---|:---|:---|:---|
| 0. Corpus-grep prereg | sweep `wte7dhv5v` → inventory | THIS lane | ✅ |
| 1. Ontology + flags | **GRANT GATE** | Grant | ✅ (B1 + high-Q) |
| 2a. Prereg draft (v1→v2) | discriminator/bins/falsifiers + auditor fixes | THIS lane | ✅ (v2) |
| 3. Auditor-gate | READ-ONLY `ave-auditor` panel `wyxwc215e` (4 dims) | auditor | ✅ all FLAG/freeze-after-fix; v2 addresses must-fix |
| 1b. Framing-gate | **GRANT GATE** — prereg §11: platform fork · F3 137-vs-114 · chord contingency | Grant | **← HERE** |
| 2b. Rule-11 freeze | → `_FROZEN` + re-gate confirm | THIS lane | blocked on 1b |
| 4. Driver | ave-implementer, own worktree, §7 + stability/Q layers + G1–G4 gates | implementer | gated on 1b–2b |
| 5. Result | honest bin + measured Q (137/114, echo/chord tag) | implementer | — |
| 6. Adjudicate + cross-lane | result → Grant; Q → Lane 1 **iff Path C closes** | Grant | — |

---

## §8 — Phase log

- **2026-06-15 (Phase 0)** — Lane founded; read charter + index + KB CLAUDE.md + harness skill;
  verified grounded anchors; worktree off `main@40a2a2e7`. Corpus sweep `wte7dhv5v` (8 agents)
  → §2 inventory: NOT greenfield; one untried residue = hybrid-coupled (V,ω) imposed-BC
  eigenmode. Brief committed `347d67d1`.
- **2026-06-15 (Phase 1)** — **Grant-gated.** B1 green-lit; **"lossless" dropped → high-Q
  (Q=1/α=137), measure Q, false-negative guard on Q=∞**; radiative Q = 3rd detector output;
  shear clock confirmed; hybrid object accepted (bears-on not resolves Flag-A); cross-lane
  triangulation (Lane 2 measures Q → Lane 1 cross-check = the chord). Prereg v1 + brief
  committed `39f5d425`.
- **2026-06-15 (Phase 3 auditor-gate)** — Read-only adversarial panel `wyxwc215e` (4 dims:
  discriminator, citations, echo/chord, hazard/platform). **All FLAG (freeze-after-fix), none
  FAIL** — core verified verbatim (untried residue, high-Q reframe, scope discipline, echo/chord
  all corpus-grounded). Load-bearing must-fix landed in **prereg v2**: (1) **platform-firewall** —
  the Γ=−1 cavity is the A1 stiffening cage (branch-1 `crystal_engine`) which canonically cannot
  carry Cosserat winding; spanning both = the non-existent substrate-complete engine → resolved to
  **option (a)** (CoupledK4Cosserat + Γ-impedance-clamp BC, firewall-legal, with honest
  projected-scalar scope caveat) but flagged to Grant; (2) **find_eigenstate `f_fn` pinned to the
  wave-operator residual** (not energy/S11 — closes the gradient-flow loophole); (3) **F3 Q binned
  137 (bare-α) vs 114 (κ_chiral=α·1.2) with ±5% tolerance** (was ambiguous by κ̃=1.2); (4)
  **EXCLUDED operationalized** to the α=0 control only (no coupled run can be EXCLUDED) + bind=leak=α
  demoted to hypothesis-under-test (no corpus anchor); (5) **chord re-framed CONTINGENT** on Lane-1
  Path C (z₀=52 is the open frontier, 1.5% off, not an established α-free leg); (6) **G1–G4
  instrument-validation gates** added (plant-at-scale winding gate at this (N,R,r); known-pos/neg for
  stability-eig; analytic-resonator + Nyquist for radiative-Q) — closes the t2-genesis
  detector-can't-certify defect; (7) citation fixes (`:98`→`:131` α-input; SM-leakage→`72_:238`;
  Mode-III→`74_:57`; shear-clock→Op16; Flag-A provenance→`photon-id:11`). **NEXT: Grant framing-gate
  (prereg §11, 3 forks) → freeze → dispatch driver.**
- **2026-06-15 (Phase 1b — Grant §11 RULED + cross-lane immune-system catch)** — All three lanes
  (incl. this orchestrator) caught the chord overstatement. **Grant owned it: α is an ECHO for the
  z₀ route** (z₀=52 is a path-PRODUCT coincidence dressed with 8πα; honest additive count ≈16 →
  α⁻¹≈49, off 3×; neither 137 nor 49 is an α-free map). Rulings → prereg **v3**: (1) **Fork-1
  platform: run the magnetic-branch PRE-FLIGHT** before locking — dispatched as background
  ave-implementer `a12b397d4d347be90` (own worktree `analysis/2026-06-15-eigenmode-preflight`):
  does `CoupledK4Cosserat` reach Z→0/Γ→−1 (the matter wall, chiral ON) on the sech, or only Z→∞ /
  Z₀? **(a)-VIABLE iff Z→0; don't take (b) sign-off until (a) is DEAD.** (2) **Fork-2:** 137-vs-114
  pre-registered, awareness only, **not bin-deciding**. (3) **Fork-3:** chord confirmed contingent →
  **Q demoted to SECONDARY; the KEYSTONE = EXISTENCE + STABILITY** of the passive high-Q hybrid mode
  (§3/§4 reframed; F3 no longer decides the bin; Q→∞ on a coupled stable mode = POSITIVE-with-
  decoupled-Q, refutes bind=leak=α). Cross-lane sharpening recorded: SYMMETRIC co-saturation =
  GRAVITY lens (Z=Z₀, Γ=0); MATTER WALL = chiral-broken (Z→0, Γ=−1); K=2G = the symmetric/gravity
  lock (provenance on the amorphous EMT, under reconstruction — separate lane). **NEXT: pre-flight
  result → resolve Fork-1 → freeze (`_FROZEN`) → dispatch production driver.**
- **2026-06-15 (Phase 1b — PRE-FLIGHT RESULT: option (a) DEAD; §0.5)** — Background diagnostic
  `a12b397d4d347be90` returned: `CoupledK4Cosserat` reaches the magnetic SIGN but **clip-floors a
  pseudo-Γ→−1 wall that is a numerical artifact and immediately runs away** (deepest genuine wall
  Γ≈−0.49, non-persistent) — **reproducing graft-v2's clip-bound "−1 NOT demonstrated" on a SECOND
  engine.** Three findings: (1) (a) dead; (2) the chiral term is **<10% / not load-bearing** for the
  wall — the structural curvature-vs-strain split drives the sign, **contradicting both the engine
  docstring and Lane-3's chiral-broken claim** (cross-lane flag); (3) **COORDINATE-MISMATCH** — the
  engine reads Γ from Cosserat ω-curvature, but the canonical electron winding lives in the K4 V-tank
  `(V_inc,V_ref)` phasor; the real-space (2,3) ω seed that produced a wall is canon-flagged
  PROTON-family, and the canonical unknot electron gave NO wall. **Pre-flight-before-driver discipline
  earned its cost** (saved a coordinate-mismatched, clip-contaminated production run). **HELD: freeze
  + production driver blocked on a Grant platform/coordinate decision — (b) build-as-posed / (b′)
  V-tank-phasor coordinate-faithful re-scope / (c) mounting-negative-but-untestable. Surfaced to
  Grant; entangled with the unresolved Flag-A.**
- **2026-06-15 (Phase 1c — Grant RULED option 1; V-tank pre-flight dispatched)** — Grant: run the
  V-tank pre-flight before any build (not (c) over-closure, not (b′) build-before-probe). **Dispatched
  agent `a9ce00462badb0d85`** (own worktree `analysis/2026-06-15-vtank-preflight`): reads the ACTUAL
  impedance Γ on `crystal_engine`'s sech self-focus (vs the cage's `gamma_bulk_min` PROXY) — STABLE
  Z→0 → wall-half real → (b′)+sign-off; CLIP-FLOOR+RUNAWAY → (c), the third engine = honest structural
  negative. Cross-lane records (§5.6): (1) first engine-level Flag-A discriminant → A1 (evidence, not
  resolution); (2) chirality contradiction → K=2G lane (likely off-K=2G artifact); (3) watch-item:
  third-engine clip-floor would convert the coordinate caveat into a keystone structural signal.
  **NEXT: V-tank pre-flight result → (b′)+sign-off OR (c) honest negative.**
- **2026-06-15 (Phase 1d — V-TANK PRE-FLIGHT: a BREATHER, (c) OFF; breather reframe)** — `crystal_engine`
  V-tank renders a **genuine, bounded, recurrent BREATHING TIR wall** (Γ_TRUE≈−0.43 unclipped; amp=0.50
  walls to −0.19 with zero clips; no runaway) — categorically HEALTHIER than the two coupled engines.
  **Third-engine watch-item did NOT trigger → option (c) is OFF.** NOT a stable static Z→0, but that
  was a **mis-framing**: the electron eigenmode is a **LIMIT CYCLE / BREATHER** (cage "persistent
  breathing cage", `selftrap` limit-cycle, `master-equation.md:20` "A1 breather", high-Q
  real-eigenvalue = non-decaying oscillation). **→ V-tank is the VIABLE wall host (b′ confirmed).**
  Surfaced to Grant: (i) confirm the breather/limit-cycle framing (the implementer's flag-don't-fix:
  read the eigenmode time-averaged/cyclic, not instantaneous-static); (ii) the **(b′) bounded
  cross-firewall build sign-off** (couple Cosserat-ω winding to the crystal_engine breathing V-tank
  wall). **EXPONENT-DEFECT FLAG:** the production read must use the TRUE n=√S impedance, NOT the
  proxy `gamma_bulk`=S^{1/4} (`crystal_engine.py:421-432`). **NEXT: Grant framing-confirm + (b′)
  sign-off → freeze → production driver.**
- **2026-06-15 (Phase 1e — Grant ADJUDICATED: breather CONFIRMED + (b′) GRANTED)** — Grant confirmed
  the breather/limit-cycle framing (checked the post-hoc-bin-shift risk himself: NOT a rescue — a
  stable real-eigenvalue mode IS a non-decaying oscillation, corpus-canonical). **(b′) GRANTED** (skip
  the cheap A1-only-Q probe — it wouldn't predict the hybrid Q, and the wall-half is established by two
  converging results) **with two conditions:** (1) **the G0 double-count smoke-gate is build-step-zero**
  (hard, before any production run — does Op14 keep the winding strictly ⊥ the A1 `(V_inc,V_ref)`
  phasor, the exact genesis-24 failure?); (2) **eyes-open precedent** — this authorizes the FIRST
  substrate-complete cross-firewall engine (the anti-loophole guard's exact target), justified by
  empirical force but a precedent future lanes will over-trust. **Deliverable framed on EXISTENCE (the
  form / structural chord-candidate); Q is the echo — headline must not drift to "we measured Q."**
  Cross-lane: Flag-A now 3 converging signals → mass=A1 (still bears-on-not-resolve); chirality fork
  CLOSING (K=2G lane confirmed off-K=2G artifact — K=2G is a tuned, not geometric, point); exponent
  defect (TRUE n=√S) logged. **NEXT: final referential-integrity auditor pass → freeze (`_FROZEN`) →
  dispatch (b′) build (G0 gate first).**
- **2026-06-15 (Phase 2 — integrity pass + 🔒 FREEZE)** — Final read-only referential-integrity
  auditor (`aff859d8759e39bae`) returned **FLAG** and caught **exactly the cage-A3 superseding-
  amendment orphan** it was commissioned to find: the breather reframe pinned §4 (Q→∞ on a coupled
  stable mode = POSITIVE-with-decoupled-Q) but left the OPPOSITE verdict standing in F3 (NEGATIVE-B)
  and a third in §2 (NEGATIVE-B-adjacent) — one observation → three bins. **Fixed:** pinned §2/§5-F3 to
  the §4-ratified disposition; repointed dangling §-pointers (§8.9→§8 item 9; §7.6/§7.7→§7 item 6/7);
  closed the F5 numbering gap (F6→F5, ledger now contiguous F0–F5); reworded the stale dead-(a) scope
  clause. PASS items confirmed: G0 anchors verified verbatim (`master-equation.md:20`, `k4_tlm.py:346`),
  (b′) scope bounded + TRUE n=√S, stale-language sweep clean, A47 obligations correctly gated into
  G3/G4. **Prereg FROZEN** (Rule-11) → `research/2026-06-15_passive-eigenmode_prereg_FROZEN.md`.
  **NEXT: dispatch the (b′) build to an implementer (own worktree) — G0 double-count smoke-gate FIRST
  (hard), then the hybrid production driver only if G0 passes.**
- **2026-06-15 (Phase 2b — G0 PASS + representation-capability flag)** — G0 smoke-gate
  (`a048bd279cd6741d1`) **PASSED**: the minimal Op14 cross-coupling (`trilinear_buckle_forces`,
  CrystalGraft-v4 — `cross_sector_coupling.py:110-139`; `f_w≡0`; g_wall = CP10 boundary window) is
  **double-count-clean** — `w_pol` stays nonzero on the ω-carrier (the step-59 drift to 2 is
  free-evolution, confirmed by the κ̃→0 control giving identical drift), and **V_ref-leak ≤ 4.3e-16**
  (the winding is wholly absent from the A1 `(V_inc,V_ref)` phasor; reading the extractor on the V-tank
  phasor returns (0,0)). Coupling-binding declaration: `KAPPA_TILDE=6/5`, **α-FREE** (α imported only
  to declare it is NOT a coupling input). **🔴 REPRESENTATION-CAPABILITY FLAG (`ave-representation-
  capability-check`):** the brief-named seeder `initialize_electron_2_3_sector` writes a **z-flat
  rotor** (ω·ê_z≡0), so `extract_2_3_omega_fast`'s toroidal projection is **structurally w_tor=0** —
  a G4 plant/read MISMATCH, NOT a coupling collapse. The extractor is SOUND on its **matched** plant
  `planted_winding_field(traveling)` (the D15 class certified by the FROZEN prereg's G4 anchor
  `test_unified_quadrature_v7.py:142,153`) → reads (2,3), rel 0.73–0.98; G0 PASS used that carrier.
  **So the FROZEN prereg's G4 already specifies the `planted_winding_field`-class carrier; the
  "electron"-named z-flat-rotor seeder would fail G4 instrumentally.** Surfaced to Grant: is the
  traveling-(2,3) the physical electron winding (proceed), or is the z-flat rotor canonical (→
  re-scope: extend extractor / new prereg)? **PRODUCTION DRIVER HELD on this representation call.**
- **2026-06-15 (Phase 3 — representation RESOLVED + G0 banked + production driver DISPATCHED)** —
  Grant: **proceed with the traveling-(2,3)** — the z-flat `initialize_electron_2_3_sector` is
  **corpus-DEPRECATED for the electron** (its docstring `cosserat_field_3d.py:932-945` flags it
  "misleading", valid for the **proton 5₁/5₂**, redirects to the unknot); the traveling-(2,3) is the
  G4-certified carrier the FROZEN prereg already specifies, so this **corrects a loose dispatch ref to
  match the frozen spec, NOT a re-scope.** **GUARD (third-time wrong-object check):** the production
  seed **asserts the 0₁ UNKNOT envelope** — "reads (2,3)" backed by "on the unknot = electron, not a
  heavier knot" (the G4 mixed-frame read is correct, NOT the A46 real-space trap). **G0 banked as a
  standalone result** (`research/2026-06-15_g0-double-count-clean_result.md`): the first
  substrate-complete engine is double-count-clean — the authorized precedent does NOT re-inflict the
  genesis-24 failure. **Production driver DISPATCHED** (`a42cabffd2989fa1b`, branch
  `analysis/2026-06-15-eigenmode-driver` off the lane branch): the hybrid breather solve + G0–G4 gates
  + the §4 bins; headline EXISTENCE, Q the echo. **NEXT: driver result → adversarial-verify Workflow
  → adjudicate to Grant. (This is the one genuinely-open physics question left; the rest is docs +
  merges.)**
- **2026-06-15 (Phase 3b — PRODUCTION RESULT: BIN = NEGATIVE-A; adversarial-verify running)** —
  Driver `a42cabffd2989fa1b` returned **NEGATIVE-A**: the passive winding-protected hybrid (V,ω)
  breather **does NOT exist** on the (b′) platform. **F1 existence = FALSE** (V_peak tail/seed=0.181,
  Γ_true_tail=−0.003 — wall vanishes, FWHM grows 64×); **F4 winding = FALSE** (w_pol 3→1→0). **ALL
  gates G0–G4 + unknot PASS** (G2 sign-read ✓, G3 Q_analytic to 0.06% ✓, G4 (2,3) rel 0.73/0.94 ✓)
  → the negative is **credible physics, not a detector artifact**; two-lattice reproduction; **F0
  decoupled (α=0) control ALSO disperses → the dispersion is INTRINSIC to the V-tank, not the
  coupling.** Q=363.8 (neither band) = dispersing-remnant echo, no weight. (`make verify` passes;
  the EFT magic-number gate caught + the implementer fixed a hardcoded 137.036 literal → import
  identity.) **FLAG 1 (load-bearing):** contradicts pre-flight #2's "bounded recurrent breather
  (Γ≈−0.43, re-focus 375–450)" — the production TRUE-Γ min is always at step 0, never deepens
  (the −0.43 was the SEEDED depth); reconciliation hypothesis = the pre-flight mis-read dispersing
  ringing as self-focus. Bears on whether (b′) was correctly characterized as a viable breather host.
  **Result NOT yet banked — adversarial-verify panel `ww03eo0v5` (4 auditors: bin-conformance /
  pre-flight contradiction / cage tension / floor-not-artifact) scrutinizing first.** NEXT: panel →
  adjudicate to Grant.
- **2026-06-15 (Phase 3c — ADVERSARIAL-VERIFY PANEL: NEGATIVE-A REFUTED as a FALSE NEGATIVE)** —
  Panel `ww03eo0v5` (3/4 returned; pre-flight-contradiction dim died on a socket but is COVERED by
  dims 3+4). **Dim-1 bin-conformance CONFIRM:** honestly *derived* — a live re-run reproduced every
  bin-deciding number EXACTLY; all hazards precluded in code; TRUE n=√S exact; Rule-11 holds (fails by
  17×, no tuned knob). **Dim-4 floor-not-artifact REFUTE (load-bearing):** a **FALSE NEGATIVE from
  seed/grid UNDER-RESOLUTION.** The A1/V-tank breather is a corpus-established positive
  (`test_master_equation_v14_mode_i.py:29-36`; cage `:53`) on this exact engine, and PASSES the
  driver's OWN F1 (retention 0.75, Γ_true median −0.069) at the **v14 eigen-resolution (dx=0.5, ≥5
  core cells)**. The driver ran `v_width=3.0/dx=1.0/N=48` = **~3 core cells in a 4×-larger box** → the
  sech under-resolves → disperses to 0.18. **AND G1 is DEFECTIVE** — coded *relative* (`sech>1.1×Gauss`,
  `driver:430`), banked PASS while the sech retained 10% (breather needs ~68%): **the exact t2-genesis
  "detector-can't-certify-the-known-positive" defect the G-gates were built to prevent.** The "two
  lattices" + F0 inherit the identical under-resolved seed (R/r vary the ω-torus, not the V-tank seed
  resolution). **Dim-3 cage-tension FLAG:** box-physical-size (cage 12-phys confined vs production
  48-phys isolated), NOT coupling (F0), NOT the n-exponent (cage self-focus = max|A| growth,
  exponent-immune by Amendment-A1) → cage gets a **Rule-12 SCOPE-ANNOTATION**, NOT a walk-back; the
  FLAG-1 "transient ringing" attribution was WRONG (the pre-flight breather was REAL). **CONSEQUENCE:
  result NOT banked; the keystone is STILL OPEN.** Path = a **corrected re-run** (G1 → absolute
  known-positive; V-tank seed at its eigen-resolution; sweep v_width/dx/box; commit JSON) — fixing
  driver defects within the FROZEN prereg, **NOT a re-scope**. Auditor's open framing question → Grant:
  are the wall (eigen-res dx=0.5/~5 cells) and the winding (R=10/r=4) **co-resolvable on one lattice**,
  or is that incompatibility itself the structural obstruction? **My last-turn "consolidating toward
  echo" read is RETRACTED** (the negative that would support it is false). **HELD for Grant. Cross-lane:
  cage scope-annotation → auditor COLLABORATION_NOTES queue.**
