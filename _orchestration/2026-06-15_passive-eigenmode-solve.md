# Passive winding-protected electron eigenmode — the structural keystone (ORCHESTRATION)

> **STATUS: OPTION C RETURNED (recovery `a89a0c883912c60cd`) — BIN = DISQUALIFY. The hard-projection
> (2,3)-hold on the Cosserat-ω carrier PUMPS energy (ω-sector Hamiltonian ramps 56×, reproduced).
> DISQUALIFY ≠ NEGATIVE — the pump MASKS the persistence
> question. The implementer caught its OWN false-positive (the `sum(ω²)` pump-witness was blind to the
> pump — magnitude-locked by construction; fixed to read the full ω-Hamiltonian).** **PANEL `wvd0c2oib`
> RETURNED: DISQUALIFY SOUND but METHOD-OPEN — do NOT conclude echo/negative.** The hard hold pumps
> 56× (reproduced) — but (1) the **"no conservative window" generalization is UNBACKED** (the soft
> sweep was NEVER run; header-prose only — I took it at face value and leaned echo: premature,
> corrected); (2) the hold enforced the **WRONG object** — a real-space director PHASE TEMPLATE, NOT
> the conserved **Beltrami helicity H_bel = ∫ω·(∇×ω)** the corpus says IS the charge
> (`master-equation.md:20`; the engine doesn't even compute H_bel). FUNDAMENTAL for THIS construction
> (hard director-overwrite of a non-free-conserved phase pattern → fights the gradient flow → does
> work); METHOD-OPEN for an **H_bel-Lagrange-constraint hold** (symplectic-orthogonal / no-work) + a
> **phase-space (V_inc,V_ref) representation** (DEC-01 tension). **A-as-specified is dead; ontology
> question → Grant: hold the conserved H_bel, not the director template? → C′.** §9 + the CLEAN
> pre-landing sweep below.
>
> _(prior status, retained:)_ **VERIFY PANEL `w92ft1gkc` UNANIMOUS — do NOT bank NEGATIVE-A (mis-binning + the keystone
> is UN-TESTED).**
> Lane worktree `AVE-Core-eigenmode-wt`, branch `analysis/2026-06-15-passive-eigenmode-solve` off
> `main@40a2a2e7`. **main is PROTECTED — Grant merges; this lane does NOT merge. Result NOT banked.**
> **SOLID (bankable):** the first NEGATIVE-A is REFUTED (false negative); the **wall-half breather is
> VINDICATED** (real+stable, qualified to **≥10 core cells**; the banked N=26/5-cell F1=True is a
> step-count knife-edge; G1 cert is box-scoped); G0 double-count-clean. **UN-TESTED:** the keystone —
> the driver seed-and-evolved the winding as an IC + did forward-integration, NOT the **held-BC +
> residual→0 eigensolve** the charter/§7.1-7.3/§8.3 specify. F4=False = un-held-BC apparatus floor
> (coupling-independent), NOT a winding-physics null. **A faithful keystone test = a RE-SCOPE (new
> prereg + version).** Lane worktree
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
engines: genuine unclipped physics that BREATHES, vs a clip-artifact whose energy DIVERGES (a +λ
gain/runaway — an integrator instability, not a substrate event; cf. terminology note, Phase 4). It is **NOT a
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
   as a **boundary condition** (`substrate-native-check` CP10 — NOT a bulk term, which is
   singular at the wall and blows up); solve the coupled (V,ω) wave-eigenproblem (both sectors nonzero, Op14
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
  `photon-identification.md:19`). **Do not claim resolution** of the mass-magnitude.
  > **🟢 IMPEDANCE-SECTOR HALF RESOLVED (terminology-guide review, 2026-06-15; Phase 4):** the
  > `INVARIANT-S2` "Q1 = (B)" ratification (Grant 2026-06-15, `2026-06-15_ceff-epsilon-monotonicity_result.md`)
  > canonically splits the two sectors at the IMPEDANCE level: **Z→0 = the A1 LONGITUDINAL bond-
  > compliance tank √(L/C_comp)** ($C_{comp}=C_0/S$ diverges as the bond yields) = **CONFINEMENT** =
  > this lane's electron matter-wall; **Z→∞ = the T2 transverse permittivity** ($\varepsilon_0 S$) =
  > RUPTURE — both $|\Gamma|=1$, differing only in boundary phase. So **the wall-half = the canonical
  > A1 Z→0 confinement** (pre-flight #2 finding now = ratified invariant, not a one-off probe), and the
  > pre-flight #1 ω-curvature object is a different (proton) sector. The A1⊥T2 orthogonality (= the
  > genesis-24 double-count) is canon. **Only the mass-MAGNITUDE provenance (A1 confinement vs T2
  > rotational gap) stays hypothesis-class** — the impedance-sector attribution no longer is.
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
- **2026-06-15 (Phase 3d — Grant ratified (a); corrected re-run DISPATCHED)** — Grant: **option (a)**
  (co-resolving re-run), hold **(b)** (wall/winding scale-incompatibility) as the follow-up if needed.
  **Corrected re-run DISPATCHED** (agent `ad08960e56e04bca8`, on driver branch
  `analysis/2026-06-15-eigenmode-driver`): (1) **G1 → ABSOLUTE** known-positive (sech must reach the
  v14 retention ~0.68, not just beat the Gaussian — if it can't at the chosen resolution, G1 FAILS →
  don't bank a negative); (2) **V-tank seed at the v14 eigen-resolution** (dx=0.5, ≥5 cells, amp≈0.85);
  (3) **co-resolving lattice** — BOTH G1 (wall) AND G4 (winding) must pass on ONE lattice, else STOP +
  report the **(b) structural finding**; (4) **sweep v_width/dx/box** as a first-class robustness axis;
  (5) **commit JSON** (SHA-pin). Reuses the working G2/G3/G0/unknot infra — only G1 + seed-resolution +
  sweep change. Re-bin per §4 (POSITIVE iff the breather exists at the correct resolution with a
  VALIDATED absolute-G1; NEGATIVE only with the validated detector; option-(b) if no co-resolution).
  **NEXT: re-run result → adversarial-verify panel again → adjudicate to Grant.**
- **2026-06-15 (Phase 3e — CORRECTED RE-RUN: wall-half VINDICATED; FLAG-WIND = keystone un-tested?)**
  — Re-run `ad08960e56e04bca8` (driver `3565a660`, JSON `4f7cc7e5`, result `803e2263`). **G1-absolute
  CERTIFIES** (sech 0.687, matching v14 0.670 — the t2-genesis detector defect is CLOSED). **Co-
  resolution SUCCEEDS** (G1 wall + G4 winding both PASS on N=26/R=5/r=2.5/dx=0.5 → option (b) NOT
  triggered). **WALL-HALF VINDICATED:** F1=TRUE (0.681), F2=TRUE — the V-tank breather is REAL+STABLE
  at ≥5–10 cells; **the first NEGATIVE-A was a resolution false negative (confirmed).** BIN=NEGATIVE-A
  banked on the **F4 path** (winding not conserved, frac_tail_2_3=0.00). Q=56.0 (wall-half leak, echo,
  no keystone mode). **🔴 FLAG-WIND (bin-controlling, implementer self-flagged):** the driver imposes
  the winding as a **SEEDED IC, NOT the HELD topological BC** the prereg §7.1/§8.3 charters — the
  attribution probe shows the bare ω-carrier disperses the winding **bit-identically with/without the
  coupling**, so **F4=False is the un-held-BC APPARATUS FLOOR, not a coupling-physics null → the
  keystone's imposed-BC thesis is UN-TESTED by seed-and-evolve.** A held-BC re-run = a RE-SCOPE (new
  prereg + version) — the implementer correctly did NOT make that call. **🟢 SHARPENED (terminology-
  guide review, Phase 4): FLAG-WIND is a TOPOLOGY-CATEGORY ERROR, not merely an apparatus floor.**
  Per `substrate-native-terminology.md` ("EE owns dynamics, **topology owns the integers**"), the
  (2,3) winding is a **conserved topological INTEGER** (charge = the phase-space (p,q) winding,
  `ch8-alpha-golden-torus.md:31` / `electron-identification.md` — cite the (p,q) home, NOT `def-3638f2`
  which the updated guide flags as the `ambiguous` homonym node), not a continuous field
  — a topological integer is **held by definition**, it does not "evolve and disperse." Seed-and-
  evolve mis-categorizes it as a continuous IC; its smoothing-to-garbage is the predicted result, not
  a physics null. **→ holding the winding is the only categorically-correct test** (reinforces the
  held-BC re-scope). FLAG-RES (F1 resolution-
  dependent: False@5 cells, True@10); FLAG-APPARATUS (~0.68 retention partly small-box). **Result NOT
  banked — verify panel `w92ft1gkc` (wall-half / FLAG-WIND attribution / bin-appropriateness)
  scrutinizing.** NEXT: panel → adjudicate to Grant (bank-with-flags vs held-BC re-scope). Cross-lane:
  retract first NEGATIVE-A + cage scope-annotation → auditor queue.
- **2026-06-15 (Phase 3f — VERIFY PANEL on the re-run: do NOT bank NEGATIVE-A)** — Panel `w92ft1gkc`
  (3/3): **dim-1 wall-half FLAG** (vindication real but FRAGILE — the banked N=26 F1=True is a
  step-count knife-edge straddling the −0.05 γ-gate by 3 parts in 10⁴, `driver:752,1036`; robust only
  at **≥10 cells**; G1 cert is **box-scoped** — the same sech falls below the 0.60 floor at N=48);
  **dim-2 FLAG-WIND CONFIRM** (the implementer's self-flag is correct: the driver seeds the winding as
  a one-shot IC + free-evolves, zero held-BC enforcement; F4=False is coupling-independent
  (bit-identical) → the un-held-BC **apparatus floor**; the keystone's imposed-BC thesis is
  **UN-TESTED** — it ran the "withhold→disperse" arm §3 already predicts; **deeper gap: §7.2/§7.3
  charter a residual→0 EIGENSOLVE, the driver did forward-integration with no root-finder**);
  **dim-3 bin-appropriateness FLAG — do NOT bank as NEGATIVE-A** (a MIS-BINNING: §4 NEGATIVE-A = "the
  solve disperses / no standing mode", but F1+F2 PASS — a stable breather EXISTS; the (F1-pass,
  F4-fail) outcome §4 never provisioned). **HONEST corpus-state: first-negative REFUTED + wall-half
  VINDICATED (≥10 cells, box-scoped) + keystone UN-TESTED (held-BC + eigensolve not implemented).**
  **Held for Grant: (A) held-BC re-scope (new prereg/version + held-BC + residual→0 eigensolve) / (C)
  cheap held-BC PROBE first (hold the winding on the co-resolving driver, de-risk) / (B) bank-what's-
  solid + defer.** Cross-lane (auditor queue): retract the first NEGATIVE-A; bank the wall-half
  vindication; record keystone UN-TESTED; cage scope-annotation.
- **2026-06-15 (Phase 4 — terminology-guide review against `substrate-native-terminology.md`)** —
  Grant-prompted leak-check of the lane's vocabulary against the EE-native discipline. **Net: the
  register PASSED** — Γ/Z/impedance/reflection/resonance/Q/breather/soliton/saturation/winding-as-
  topology are all substrate-native; no dissipation/amorphous/QFT/GR leak. The **high-Q / Q=1/α /
  breather** reframe is the *literal* canonical statement (guide: "the only loss channel is the
  controlled radiative leak Q=1/α, NOT internal friction"; "soliton/breather = EE-compatible PASS") —
  the reframe was substrate-native, not just a good call. **THREE clarifications folded in:** (1)
  **Flag-A impedance half RESOLVED** → cite `INVARIANT-S2` Q1=(B) (Z→0 = A1 longitudinal compliance
  confinement = the wall-half; Z→∞ = T2 permittivity rupture); only the mass-magnitude stays
  hypothesis-class. (2) **FLAG-WIND sharpened → topology-category error** (the (2,3) winding is a
  conserved topological integer, held by definition; seed-and-evolve mis-categorizes it; reinforces
  the held-BC re-scope). (3) **"detonate" → "energy diverges / +λ gain"** (loose explosion-metaphor
  for a numerical instability; tightened). Frozen prereg carries a Rule-12 terminology annotation
  (body preserved). No physics-result change; no walk-back.
- **2026-06-15 (Phase 4b — re-review of the REGIME-SCOPED guide rewrite)** — The guide was rewritten
  from a hard PASS/FAIL retire-list into a **regime-scoped default-register guide** ("declare the
  regime, then leak-check; scope, don't blanket-retire"; the substrate is **not globally lossless** —
  radiative Q=1/α, Op3 A1-mode monotonic decay, boundary-Joule/Ohmic-decoherence, Regime-IV rupture
  are real loss channels; what it lacks is only *internal viscous friction → heat in the reactive
  regime*). **Impact on this lane (small, all confirming):** (i) the **high-Q / Q=1/α** framing is
  *more* canonical — the rewrite lists the electron's per-cycle Q=1/α leak as THE radiative channel
  (`resonant-lc-solitons.md:96`); the F2 "stable/non-decaying" read is the **bound, sub-yield interior
  mode** (the reference regime), distinct from the *free* A1 mode's Op3 monotonic loss — a regime
  distinction worth carrying. (ii) **Corrected the def cite:** charge → the (p,q) home, NOT
  `def-3638f2` (now the `ambiguous` homonym). (iii) **"amorphous" nuance:** the lane's only "amorphous"
  is the **secondary-EMT z₀≈51.25 route** (the α-echo cross-lane finding) — the rewrite puts that
  under the **open D3 amorphous-retirement adjudication → do NOT classify either way**; so my Phase-4
  "no amorphous leak" was imprecise — the lane *names* the secondary-EMT route (correct, not the
  primary-lattice geometric-disorder leak), it does not clear it. (iv) **"detonate" regime-scope:** it
  was a near-yield over-driven *numerical* runaway (+λ gain), NOT the canonical Regime-IV irreversible
  rupture (which the rewrite confirms is a real phase). (v) The rewrite's **"photon IS transverse"**
  precision (transverse-true; the trap is the inference "⇒ no longitudinal grade") — the lane
  **respected it**: the longitudinal A1 mass-wall and the T2 winding were kept orthogonal, never wired
  into the photon. Q1=(B) (case-law #4) and topology-owns-the-integers are unchanged.
- **2026-06-15 (Phase 5 — pre-landing consistency sweep `wnzdlzndz`: CLEAN; + propagation map)** —
  Read-only sweep (3 ave-corpus-grep angles, parallel to C). **ZERO prematurely-RESOLVED sites** across
  the KB leaves (12 says-OPEN / 6 neutral-structure-only), the merged sibling PRs #260/#261/#262 + L3
  archive (7 / 6; the three PRs establish wall/operating-point/sector and are MUTE on eigenmode
  existence — exactly correct), and the orchestration trackers + this lane's docs (10 / 5; the index
  doesn't list the un-merged lane; the electron is framed STRUCTURE-only). **The landing zone is
  verified OPEN-consistent — the C/A verdict can land without contradicting any canonical site.**
  Corroboration: the corpus **already** flags the held-BC route as the open re-aim
  (`genesis-chord-falsification-ledger.md:30`: "impose the saturation-TIR as a boundary-impedance /
  moving Γ=−1 wall ... a different, untested mechanism ... the boundary-impedance route is open").
  **PROPAGATION MAP (the canonical sites the C/A verdict UPDATES when it lands — auditor/walk-back
  queue):** (1) `genesis-chord-falsification-ledger.md:29-30` (the boundary-impedance/held-BC route =
  open); (2) `cvr-stability-eigenmode.md:5,57` (autoresonance/self-lock UNDERIVED); (3)
  `breathing-soliton-v14-mode-i.md:52,115` ("strict stationary eigenmode not found — needs
  imaginary-time / Newton-Raphson" = the A eigensolve); (4) `electron-unknot-cosserat-seeder.md:102`
  ("a self-consistent ground-state search would tune to canonical" = the A eigensolve); (5)
  `vol1/claim-quality.md:1323-1324` (clm-i4p11y strengthen-by: "Derive (not assert)... as a
  self-consistent eigenvalue of the self-created cavity" — the keystone strengthen-by). These all say
  OPEN now and receive the verdict on landing.
- **2026-06-15 (Phase 5a — Option C v1 DIED silently mid-build; recovery dispatched)** — First C
  implementer (`a9fc078b54026a57c`) wrote `held_bc_winding.py` (332 lines, the hold module) then died
  WITHOUT a completion notification (verified: TaskOutput "no task found" + 147-byte 23-min-stale
  transcript). I'd over-confidently reported it "still building" — **lesson: verify liveness
  (TaskOutput + transcript mtime), don't infer it from silence.** Recovery `a89a0c883912c60cd`
  dispatched into the same worktree (commit the orphan module first; audit; integrate; run; COMMIT
  INCREMENTALLY).
- **2026-06-15 (Phase 5b — OPTION C result: BIN = DISQUALIFY; the held-BC hold PUMPS)** — Recovery
  completed (branch `analysis/2026-06-15-eigenmode-heldbc`, `make verify` passes). **Audit:** winding-
  maintenance TRUE (hold reads (2,3) 100% vs 15% free; kinetic magnitude-lock exact ~5e-14);
  **energy-neutral claim FALSIFIED** — the hard per-cell phase-projection re-aligns *evolved*
  ω-directions to the smooth template each step → ω-sector `total_hamiltonian` ramps **56× (12.2→691)**
  vs a flat free run. **NO conservative window** (soft g∈[0.01,0.5] fails to maintain, frac~0.05; hard
  pumps) — structural, not a code bug. **Implementer caught its OWN false-positive:** first pump-witness
  read `sum(ω²)` (held bounded by the magnitude-lock → blind to the pump, printed false POSITIVE
  0.84×); fixed to `HoldLedger.total_after = eng_w.total_hamiltonian()` (the 56× pump). **BIN =
  DISQUALIFY** (3 corners, ramp 43–56×). F1/F2 *appear* to persist (0.681, λ −0.011) but DISQUALIFY is
  decided BEFORE persistence (§9). **DISQUALIFY ≠ NEGATIVE** (the pump prevents reaching "decays when
  held CONSERVATIVELY" — no conservative hold exists for this construction). **A-as-specified inherits
  the pump → re-design needed.** Verify panel `wvd0c2oib`: **FUNDAMENTAL (any hold fights the free
  dynamics → pumps → keystone leans negative/echo) vs METHOD-SPECIFIC (a symplectic/Lagrangian or
  PHASE-SPACE-representation hold could be conservative + double-count-clean → A re-designs the hold)**.
  **NEXT: panel → adjudicate to Grant.**
- **2026-06-15 (Phase 5c — verify panel `wvd0c2oib`: DISQUALIFY SOUND but METHOD-OPEN; do NOT conclude
  echo)** — **Dim-1 (DISQUALIFY-sound) FLAG:** the pump is REAL + reproduced (H_total 56.76×; `sum(ω²)`
  genuinely blind, bounded 0.84×; witness fix correct; magnitude-lock ~1e-13; winding maintained 0.77
  vs 0.0 free; ω-carrier-only, never the A1 phasor). **BUT the "no conservative window / structural"
  GENERALIZATION is UNBACKED** — no soft-hold g-blend in the code, no sweep script, no extra-corner
  JSON; header-prose only (`held_bc_winding.py:12-15`). DISQUALIFY sound **at the single N26 corner**;
  the structural claim is asserted. (⚠ I took that prose at face value last turn and leaned "echo" —
  premature; **2nd unverified-prose face-value slip this session** [1st = C-liveness]. Corrected.)
  **Dim-2 (FUNDAMENTAL vs METHOD) FLAG:** the free Cosserat-ω dynamics do NOT conserve the (2,3) (it's
  a **phase pattern in a gradient-energy field**, not a conserved charge; hold-OFF frac=0.0) → a hard
  director-overwrite must do gradient-W work → FUNDAMENTAL *for THIS construction*. **BUT the geometry
  does NOT forbid a no-work hold, and the hold enforced the WRONG object:** the corpus's conserved
  charge is **Beltrami helicity H_bel = ∫ω·(∇×ω)** (`master-equation.md:20`), which the **engine
  doesn't even compute** — the hold pinned a real-space director TEMPLATE, not the helicity integral.
  **A Lagrange-constraint on the conserved H_bel (symplectic-orthogonal / no-work) is UNTESTED + could
  be conservative.** **VERDICT: do NOT promote "the hard hold pumps" → "keystone leans echo" (over-read
  trap). Keystone STILL OPEN.** Ontology question → Grant: **hold the (2,3) as a constraint on the
  conserved H_bel, not a per-cell director overwrite? → C′.** + DEC-01 (theory.md:16 "(2,3) lives in
  (V_inc,V_ref) phasor" vs master-equation.md:20 "never wire it there" — signature-vs-DOF bridge
  auditor-asserted, not a canonical leaf; load-bearing for a phase-space hold). + persist the missing
  soft-sweep artifact (A47). **NEXT: Grant adjudicates — C′ (hold H_bel) / phase-space rep / defer.**

- **2026-06-16 (Phase 6 — C′ DISPATCHED: hold the conserved H_bel via a no-work constraint)** —
  Grant greenlit C′ (§9.1 amendment, commit `47b25c0c`). Pre-dispatch verification (3rd-slip guard):
  `_beltrami_helicity` confirmed `cosserat_field_3d.py:450` (LOCAL density, integral NOT tracked);
  the real (2,3)-pair readout is `extract_2_3_omega_fast` at `src/ave/utils/fast_winding_extractor.py:165`
  (signature `(omega,pi_omega,R,r,N,n_ang=240,n_walks=12)->Dict`; usage `electron_spec_suite.py:58`) —
  NOT a field method (§9.1's symbol name was slightly off, corrected in the dispatch brief). heldbc-wt
  clean on `analysis/2026-06-15-eigenmode-heldbc` at the C result `adbffb20`. **Dispatched** background
  `ave-implementer` (`a8c699dca7…`) to: build H_bel = Σ`_beltrami_helicity`·dx³; a NO-WORK constraint
  (correction projected ⊥ the energy gradient via Gram-Schmidt `g_perp = g − (⟨g,e⟩/⟨e,e⟩)e`,
  energy-neutral BY CONSTRUCTION); ω-carrier ONLY (never A1 phasor — G0-clean); co-resolving lattice;
  full-Hamiltonian ledger FIRST (not `sum(ω²)`); KEY CHECK = does scalar-H_bel conservation MAINTAIN the
  (2,3) pair (if too coarse → FINDING, don't force); bin POSITIVE→A / NEGATIVE-earned / DISQUALIFY;
  KEEP-BOTH (new class alongside `WindingHold`, new `--hold-helicity` flag, C path stays runnable).
  **NEXT: C′ returns → adversarial-verify panel → Option A (residual→0 eigensolve, target Q=α⁻¹≈137) iff clean.**

- **2026-06-16 (Phase 7 — C′ RAN + verify panel `w4wkm2erq`: NOT clean → re-binned DISQUALIFY-WRONG-OBJECT;
  keystone reshaped to C″ "hold the PAIR"; A NOT triggered)** — C′ built+ran on the heldbc branch
  (commits `d8a3d2f9`/`5c17e8ab`/`4ea054cf`/`d79fbcbb`; module `held_helicity_winding.py`, driver
  `--hold-helicity`, result `research/2026-06-16_…cprime_helicity-hold_result.md`, JSON
  `results/passive_eigenmode_cprime_helicity_N26.json`). Implementer reported **NEGATIVE (earned)**; the
  2-lens code+structural panel **VERIFIED every number against source** and **re-binned it
  DISQUALIFY-WRONG-OBJECT (method-artifact)**. What's REAL+verified: (a) the **no-work construction is
  genuine** — `held_helicity_winding.py:264` `g_perp=g−(⟨g,e⟩/⟨e,e⟩)e` ⊥ the *full-Hamiltonian* energy
  gradient (cos=1.86e-17), ramp **0.999×** = the free 0.998× (DECAYING, **no pump** — clears C's 56×
  DISQUALIFY bar); (b) **the 137 IS an artifact** — `_beltrami_helicity` (`cosserat_field_3d.py:450`)
  returns NORMALIZED handedness ∈[−1,1] (91.5% vacuum-cell from the `eps_h=1e-12` regularizer);
  C′ correctly held the **RAW** corpus integral (target 5.296e-5), the 137.19 is a box-cell-count
  coincidence, **flagged-not-resolved**; (c) the **scalar-can't-pin-the-pair is sound + has a smoking
  gun** — H_bel pinned to 9.4e-9 while (2,3)→(1,1)→(1,0)… drifts **BIT-IDENTICALLY to the hold-OFF run**
  (frac_tail_2_3=0.0 both): the codim-1 scalar constraint is geometrically ⊥ the two pair-preserving
  integer directions, so the hold did **exactly nothing** to the pair. **THE RE-BIN:** C held a director
  template (wrong object→pumped→DISQUALIFY); C′ held a global **scalar** H_bel (still wrong object — a
  scalar, not the PAIR). `master-equation.md:20` (Grant-ratified Rule-12): the electron is "the unknot
  dilatation-mass **CARRYING** the (2,3) winding — **two objects, not one**." Two wrong-object misses do
  NOT sum to a tested negative on sector-cohabitation. **BANK (narrow, earned): the §9.1 SCALAR-HOLD
  route is CLOSED-NEGATIVE** (a single global scalar invariant cannot pin a two-integer winding;
  energy-clean, verified). **DO NOT bank "keystone leans negative / sectors don't cohabit" — the keystone
  is UNTESTED.** Option A **NOT triggered** (the "iff clean → A" gate is unmet). **TO-FIX (heldbc branch,
  uncommitted-to-main):** the result-JSON `C_reading` overclaims "keystone leans negative EARNED" past
  the implementer's own "TOO COARSE… Reported NOT forced" caveat — re-scope to "scalar-route
  closed-negative; sector-cohabitation UNTESTED." **NEXT: C″ = hold the (p,q) PAIR as TWO linked
  invariants** (toroidal w_tor + poloidal w_pol, or Γ_tor+Γ_pol; reuse the verified no-work Gram-Schmidt
  apply(), project against TWO gradients, 2-D line-solve; read pair via same `extract_2_3_omega_fast`).
  **BLOCKED on Grant ONTOLOGY ruling (DEC, pre-test-physics-check T8):** is the electron's conserved
  charge the **scalar helicity H_bel** (→ C′ is ~POSITIVE: breather persisted + charge held + neutral →
  Option A) **or the (2,3) integer PAIR** (→ C′ is wrong-object → C″)? Connects to the
  `boundary-observables-m-q-j.md` winding→𝓙 / linking→𝓠 split surfaced in the dimensional-analysis lane.

- **2026-06-16 (Phase 8 — Grant RESOLVED the ontology ONE LEVEL UP: not scalar-vs-pair, but the
  BOUNDARY-OBSERVABLE (𝓜/𝓠/𝓙) test; keystone reframed; Stage 1 GATE dispatched)** — Grant's thread
  (chirality workflow `wbjjtt6o3`, 3 refute lenses conf 0.86–0.93; PR #268 rewritten v2; v1 retained
  below-the-line Rule-12 w/ its 2 errors owned) dissolved the C′ blocker. **The substrate-correct test
  is NOT "hold an interior invariant" (scalar OR pair) — it is READING the three boundary observables
  𝓜/𝓠/𝓙 at ∂Ω of a self-trapped Γ=−1 region** (`boundary-observables-m-q-j.md`). Prior arc negatives
  (passive/held-BC/genesis-23) measured **invisible INTERIOR plumbing = a category error** (clm-sjjvhf);
  NOT echo evidence — the substrate-correct test never ran. **Verified (verify-before-cite, all green):**
  `BoundaryInvariants` `boundary_invariants.py:70` (compute_M real; **compute_Q/J = first-pass PROXIES** —
  Q=local-max count, J=inertia-anisotropy =0 for spherical; rigorous 𝓠=Link/𝓙=Wind DEFERRED, "needs
  full Cosserat-coupled engine, doc 113 §5.4"); `extract_hopf_charge` `cosserat_field_3d.py:2010` (a
  linking number — scaffold for rigorous 𝓠); `HelicityObserver` `helicity_observer.py:39`; `k4`/diamond
  net is the corpus's own **achiral CONTROL** (`chiral_lattice.py:228`, capability-map `:58` "Cubic ↮
  chirality"); **clm-sjjvhf strengthen-by[2] = "Confirm the (M,Q,J) boundary test recovers the electron
  observables"** (canon names this test as its validator); coupled `VacuumEngine3D` (`vacuum_engine.py`
  wraps `CoupledK4Cosserat`) carries K4-photon + **Cosserat (u,ω) winding** + S1-D Axiom-4 saturation +
  the Γ=−1 saturated-bond observer `:440`. (2,3) topology = knot-theory-forced (chirality-independent);
  chirality = sign-only (e⁻/e⁺), PARKED. Magnitudes achiral-OK on a rigid grid → **the §4 "engine that
  doesn't exist" is NOT needed for existence.** **Keystone = 3 staged steps (gate-first; 2–3 moot if 1
  fails):** (1) GATE = self-trap integrator-stability on the coupled engine (no |ω| blow-up, no pump,
  saturated channel persists ≥10 Compton periods); (2) implement rigorous 𝓠=Link (on extract_hopf_charge)
  + 𝓙=Wind (doc-113-§5.4 deferred); (3) read (𝓜,𝓠,𝓙) → (m_e, e, ℏ/2)? **DISPATCHED Stage 1** background
  `ave-implementer` (`ae3c707c0d…`, isolated worktree, branch `analysis/2026-06-16-boundary-mqj-selftrap-integrator`
  off main) — Checkpoint-10 (Γ=−1 as Op17-bounded BC not bulk force = the blow-up discipline) +
  Checkpoint-8 (seed precursor, don't plant end-state) + full-Hamiltonian witness. **Stages 2–3 HELD for
  Grant GO** (Stage 2 = real new implementation, scope against Stage-1 result). C/C′/C″ now SUPERSEDED by
  the boundary test (C′ scalar-route-closure still banked narrow). **NEXT: Stage 1 returns → verify →
  Grant GO on Stage 2.**

- **2026-06-16 (Phase 8.1 — auditor flag absorbed: Stage 1 re-dispatched as a THREE-WAY gate, not
  binary)** — auditor endorsed the staging + clm-sjjvhf find, but flagged a binary blind spot: a Stage-1
  **BLOW-UP** would collapse three distinct conclusions. **Verified the load-bearing tension
  (verify-before-cite, all green):** `engine-capability-map.md:45`+`:79` say `VacuumEngine3D` is
  **softening-only** — its scalar is a **projection** `v_scalar_from_v_inc(V_inc)`
  (`cross_sector_coupling.py:226`, used `k4_cosserat_coupling.py:499`), **no independent A1 field**, so it
  "structurally cannot host the stiffening cage." But the electron self-trap IS the stiffening route
  (C_eff→∞ ⇒ Z→0 ⇒ |Γ|=1, INVARIANT-S2 Q1=B A1 matter-wall). So the `:440` Γ=−1 wall is **likely the
  softening proxy, not the A1 stiffening confinement** — must be determined empirically. **STOPPED** the
  binary agent (`ae3c707c0d…`, killed; orphaned worktree cleaned), **RE-DISPATCHED** (`a24e2aecd…`, same
  branch) with a THREE-WAY gate: (1) **integrator-inadequate** — validate the stiff solver on a
  known-stable STANDALONE verdict-II self-trap FIRST (apparatus-floor known-positive); (2) **🔧 c_eff(V)
  structural gap** — wall forms but Z does NOT →0 (softening proxy) → NOT echo, a BOUNDED build (couple
  the master-equation cage's c_eff(V) into the Cosserat-coupled engine; chiral-srs half stays unneeded);
  (3) **🔴 physical no-trap** — solver-fine + Z→0 present + still no stable trap → the ONLY echo bucket.
  **Key instrument: MEASURE Z AT THE SATURATED WALL** (Z→0 = stiffening confinement vs not = proxy) — the
  bucket-2-vs-3 discriminator; without it BLOW-UP is unroutable. (Note: the killed binary agent's last
  internal note already hit a "V-sector-zero flag" — i.e. it was bumping into the no-A1-field reality;
  the re-dispatch derives it properly.) **NEXT: Stage 1 (3-way) returns → verify → Grant GO on Stage 2.**

- **2026-06-16 (Phase 9 — Stage-1 verdict VERIFIED + BANKED: bucket-2 c_eff(V)-STRUCTURAL-GAP, NOT echo;
  scoped build = §4 two-sector convergence; R10 = separate retention wall)** — verify panel `wvvx6y6zb`
  (code-lens + physics-lens + adjudicator; **physics lens INDEPENDENTLY RE-RAN the gate**) → **GATE
  UPHELD**. Echo would require a LONGITUDINAL Z→0 read coming back ~Z₀ (failed trap); the coupled engine
  instead measures the **TRANSVERSE Meissner Z_eff=√(S_μ/S_ε)** (`cosserat_field_3d.py:491,498`;
  `resonant-lc-solitons.md:41`, Grant-ratified 2026-06-15) — with V_inc=0 (V_sector_energized=false every
  step) + chirality split κ_chiral·h<1.8% → S_μ≈S_ε → achromatic-symmetric → **Z≈Z₀ is the PREDICTED
  reading for a no-independent-A1-field engine, NOT a no-trap signal.** Bucket-1 cleared (standalone
  c_eff(V) cage HELD, instrument_adequate=true). LOCK passive (H_total_ramp=0.906<2.0 on the genuine
  full-H witness `total_hamiltonian()`=k4+T_cos+E_cos(gradient)+coupling, NOT sum(ω²); PUMP control A=6
  trips ramp=163 → witness discriminates). **VERDICT BANKED.** **4 corrections for the `-zwall` result doc
  (none invert the verdict):** (1) committed JSON is **N=18 "fast artifact"** not N=24 default — label or
  re-run (bin N-robust, panel re-ran); (2) committed persistence=3.94P<10P min — panel full-window re-run
  = **11.9P**; cite the long-window run for any ≥10P claim (persistence doesn't gate bucket-2); (3)
  mechanism micro-numbers (S_μ=0.915/S_ε=0.830→Z=1.05) auditor-illustrative, NOT in JSON — emit S_μ/S_ε
  split if load-bearing; (4) known-positive Z_long=0.376 is the **A_cap=0.99 CLAMP floor** (not asymptotic
  Z→0; direction genuine, magnitude clip-set) — annotate.
  **THE SCOPED BUILD (GO pending Grant):** physics SETTLED — one node carries **A1-mass ⊥ T2-winding from
  the same S** (ratified: `photon-identification.md:16-17` PR#151 + `master-equation.md:20` + INVARIANT-S2
  Q1=B); the engines split what the substrate unifies. Engineering = the **§4 TWO-SECTOR convergence
  build**, NOT a one-line c_eff(V) graft: couple the Master-Equation **c_eff(V)/A1 stiffening cage** + the
  **Cosserat-ω winding** through a shared front, AND **reconcile the continuum-scalar-FDTD grid with the
  K4-tetrahedral Cosserat grid** (capability-map §3.1 irrotational↮winding, ∇×∇V≡0, forces two coupled
  sectors not one field). Design-class ("engine does not exist") **MINUS chiral-srs** (chirality parked =
  sign-only e⁻/e⁺; magnitudes achiral-OK). **No DEEPER obstruction** — Z→0 + winding firewalled into
  different sectors the §4 spec bridges. Stage per the §5 build-order DAG (grow one layer, validate each).
  **R10 (anhysteretic↔loop / remanence) = the SEPARATE retention wall** — governs whether the formed
  electron *stays*, not whether it *forms*; parked from the existence test. **NEXT: Grant GO on the
  two-sector-convergence build → Stage 1.5 (add c_eff(V)/A1 cage, reconcile grids, re-run gate for Z→0) →
  Stage 2 (rigorous 𝓠=Link/𝓙=Wind) → Stage 3 (read 𝓜/𝓠/𝓙 → m_e,e,ℏ/2).**
  **GRANT GO'd 2026-06-16 → Stage 1.5 DISPATCHED** (`a2317c9a3df…`, isolated worktree, branch
  `analysis/2026-06-16-boundary-mqj-stage15-ceff-converge` off `origin/…-zwall`): port the
  Master-Equation `c_eff(V)/A1` stiffening cage into the coupled engine + reconcile the
  continuum-scalar-FDTD ⊗ K4-tetrahedral grids (shared front, §4 spec, minus chiral-srs) + re-run the
  gate measuring the **longitudinal** Z_tank=√(L/C_comp) (does it →0?); 4 result-doc corrections folded
  into the brief. Checkpoints 8+10 + full-H witness + known-positive floor. **NEXT: Stage 1.5 returns →
  verify → (Z→0 ⇒ Stage 2 / still-Z≈Z₀ ⇒ characterize / blows-up ⇒ two-grid stiff-instability finding).**

- **2026-06-16 (Phase 10 — DISCRIMINATION REDIRECT: magnitudes are ECHO; the chord is α-FREE
  winding-EMERGENCE; Stage 1.5 re-scoped + re-dispatched)** — audit-lane discrimination workflow
  `wenqg7x94` (6 agents; 2/3 refute lenses confirm conf 0.86/0.90) banked the worth-gate pre-reg
  `reconciliation-handoffs/2026-06-16_electron-existence-discrimination-prereg.md`. **VERDICT: the
  𝓜/𝓠/𝓙 MAGNITUDE test is ECHO** — 𝓜=m_e is a calibration INPUT (ℓ_node≡ℏ/m_e c; "M out" = consistency
  check, `electron-identification.md:50,64`); 𝓠=e is PARTIAL chord (|Q|=1 generic-for-any-soliton; only
  the lattice-PINNED quantization + chiral sign is AVE-distinct); 𝓙=ℏ/2 is the STRONGEST chord but MIXED
  (SU(2)/Finkelstein-Misner scaffolding IMPORTED). **The α=𝓜+𝓙+𝓠 decomposition it rests on is ECHO** —
  verified `ch8-alpha-golden-torus.md:135` ("identification"), `:148` (Λ_vol=16π³(R·r), Λ_surf=4π²(R·r) →
  (R,r,d)→Λ map only 2-D image = COLLINEAR), `:150` (T_d gives A₁⊕T₂=1+3, the 1+2+3 codim ordering has NO
  substrate Hilbert-space realization), `:152` (Class-B, NOT Class-2; magnitude match = Class-4
  observable consistency). **⚠ ORCHESTRATOR OVER-READ OWNED:** I earlier headlined α⁻¹=𝓜+𝓙+𝓠 as a
  striking "not coincidental" result (dimensional-analysis delivery) leaning on the boundary-observables
  leaf without surfacing its Class-B/collinear/no-Hilbert-realization status — a verify-before-cite slip;
  the audit corrected it. **THE ONLY CHORD AXIS = α-free winding-EMERGENCE** (does the (2,3)/Γ=−1 FORM
  self-generate from a precursor, α-free, with Q~137 emerging?) — and this discriminating lane was
  **NEVER EXECUTED** (no engine carries bound-state dynamics + the bond-phasor observer simultaneously;
  the current genesis suite measures a PLANTED ansatz, `2026-06-08_…-finish-adjudication.md:11`). Meta:
  FORM self-generating = the CHORD (deepest); VALUE (m_e, α) = echo. **ACTION:** STOPPED the prior
  Stage-1.5 (`a2317c9a3df`, was building to the Z→0/α-imported target — its last note already confirmed
  the `v_scalar_from_v_inc` projection-not-field gap, no ∂²V/∂t²=c_eff²∇²V integration); **RE-DISPATCHED**
  (`aebbc99dbd…`, branch `analysis/2026-06-16-boundary-mqj-stage15-alphafree-emergence`) with the
  **4-part pre-registered (Rule-11) success criterion**: (1) (2,3)+Γ=−1 self-FORM from generic IC (no
  planted (2,3), CP8); (2) WITHOUT α inserted (α-free; else calibration model); (3) α-free Q EMERGES
  (~137 untold); (4) Z→0 longitudinal confinement NECESSARY-not-SUFFICIENT. Magnitudes (m_e/e/ℏ/2) are
  NOT success. Engine must be α-FREE-CAPABLE (real A1 c_eff(V) field replacing the projection +
  two-grid reconcile, minus chiral-srs). First commit = the Stage-1.5 prereg-freeze. R10 (remanence) =
  separate retention wall, parked. **NEXT: Stage 1.5 (α-free emergence engine) returns → verify →
  EMERGENCE (Q self-generates α-free) = the keystone CHORD / no-emergence = echo-or-build-incomplete.**

- **2026-06-16 (Phase 11 — Stage 1.5 RETURNED: EMERGENCE-NEGATIVE, but layer-a PASS closes bucket-2 +
  two-grid coupling STABLE; the negative is a precursor-class fork, NOT echo)** — Stage 1.5 (`aebbc99dbd`,
  branch `analysis/2026-06-16-boundary-mqj-stage15-alphafree-emergence`, **pushed to origin** as backup,
  tip `be459b7e`, NOT merged) built the α-free two-sector engine through all 3 layers. **Layer (a) PASS:**
  the independent α-free A1 c_eff(V) field self-traps a generic sub-yield blob → longitudinal **Z_tank=√S
  →0.376** (the stiffening wall FORMS, breather persists 12 Compton periods) — **the longitudinal
  confinement the Stage-1 coupled engine COULDN'T show → bucket-2 closed at the Sector-A level.** **Layer
  (b) STABLE:** the two-grid (continuum-FDTD ⊗ K4-tetrahedral) coupling is bounded (|ω|max/seed=1.00); an
  earlier velocity-rotation coupling PUMPED (|ω|→276), diagnosed as a leapfrog/Verlet time-centering
  mismatch, replaced with a conservative position-coupled Hamiltonian force → **the multi-week two-grid
  reconciliation WORKS.** **Layer (c) EMERGENCE-NEGATIVE:** the (2,3)+Γ=−1 do NOT self-form (bulk reactance
  w_tor=w_pol=0 on reliable contours = pure breathing, no winding; the ω-winding w_tor=−1 only on
  unreliable contours = the untrapped photon radiated out); no α-free Q emerged. α-FREE held end-to-end
  (grep-confirmed). CP8 PASS (generic precursor, no planted (2,3)); CP10 front-localized BC. **THE
  OBSTRUCTION (precisely localized, extends the arc one level):** the energize-LOCK loop is INERT because
  `f_V=−κ̃·g·Ξ=0` all run — the saturation FRONT shell and the winding curl have **DISJOINT SUPPORT**: a
  generic *propagating* photon's curl is extended-axial, the cage core compact-centered, they never
  co-locate (photon radiates out). Notably the **CP10 anti-pump front-localization is EXACTLY what spatially
  decouples the winding from the cage core.** **DESIGN FORK → GRANT (Rule 16, NOT an implementer pivot):**
  CP10 front-localization (anti-pump) vs the winding co-locating with the trap (transfer) — does the winding
  need to be a **CONFINED (not propagating) ω-precursor co-located with the cage core FIRST**? **READ: this
  is the C(director)/C′(scalar) WRONG-OBJECT pattern at one level deeper — a clean, well-disciplined negative
  that is likely a WRONG-PRECURSOR-CLASS artifact (propagating-vs-confined), NOT an earned echo. Do NOT bank
  echo.** Rule-11 prereg-freeze first commit `6e5529a1`; 4 corrections folded; result doc + engine + 3 layer
  drivers on branch. (Provenance: `aebbc99dbd` is the AGENT-ID, **NOT a commit** — `git cat-file` invalid;
  the build is **`be459b7e`**. Result-doc build-cite needs the same fix when landed.)

- **🔴 OVERTURNED by Phase 14 (2026-06-16):** the "structural f_V=0 / precursor-class-artifact" verdict
  below was itself the Cartesian-curl-on-dead-sublattice grid-registration artifact — `wpqwmrms0`'s ×4-lens
  validation was fooled (no lens checked the curl STENCIL). The loop was never tested. See Phase 14.
- **2026-06-16 (Phase 11.1 — Stage-1.5 (c) verdict CONFIRMED by verify panel `wpqwmrms0`:
  PRECURSOR-CLASS-ARTIFACT, validated + scoped; my TWO forks were both wrong-next-moves)** — 4 adversarial
  lenses (earned-advocate / re-discovery / CP8-plant / CP10-vs-co-location) all landed **LEANS-EARNED
  (0.68/0.85/0.82/0.82)**, facts grep-confirmed vs committed JSON; both pre-banking gates PASS (frozen-bin
  referential integrity — result bins to the frozen `EMERGENCE-NEGATIVE`, no post-hoc drop; provenance fixed
  above). **The `f_V=0` is STRUCTURAL, not a disabled-flag artifact** (the auditor's sharpest worry, ruled
  out — genesis-omega-wave's `disable_cosserat_lc_force` precedent does NOT apply): the coupling force is
  LIVE every step but evaluates to zero because the deep-saturated cage core is pure A1 dilatation =
  **irrotational** (∇×∇V≡0, `engine-capability-map.md:57`), so the winding curl Ξ is structurally zero there;
  the curl lives only in the rotational photon sector, which radiates out. **The A1 cage is a PROVABLE
  SPECTATOR:** `ω_C_max=0.29916` bit-identical across coupling-OFF / front / interior variants,
  `coupling_work=0` everywhere — even the "obvious fix" (interior-coupling variant) gave `f_V=0`; you can't
  tune to a coupling event. **REFRAME (corrects my over-read):** Layer (c) is NOT a fresh falsification — it
  **RE-RUNS the closed `genesis-omega-wave` (`cc19416d`) / crystal_engine→graft-v4 arc** for the charge-"3"
  ω-photon with the new cage as a spectator. **Foreground Layer (a) as THE earned advance (α-free A1 cage
  self-traps, mass-"3" longitudinal wall forms); scope (c) as a deeper re-confirmation of an already-banked
  negative — do NOT double-count as a new falsification.** **BOTH MY FORKS WERE WRONG (owned):** Fork 1
  (re-seed confined precursor) = **CP8 PLANT HAZARD** — `seed_audit` gates topology but NOT spatial config,
  and (c) proved spatial co-location is load-bearing → hand-placing a confined co-located precursor installs
  the answer (the held-BC C′ sin one level up); needs a 4-prong CP8-confinement gate before any yes-branch.
  Fork 2 (genesis-requires-coherence-leg) = **MOOT for Stage-1.5** — `coupling_work=0` → the loop never
  closes → nothing to phase-lock (unreachable, not answered-NO; still live for the older t2 NO-GENESIS).
  **THE RIGHT NEXT EXPERIMENT (CP8-safe, auditor-surfaced): a moving Γ=−1 / Op17-bounded reflecting wall on
  SECTOR B (the photon sector, NOT Sector A), co-moving with the cage front, SAME generic photon seed
  unchanged** (no seed change → cannot bank the spatial plant; α-free by inheritance). Wall confines photon +
  loop closes → (c) was a fixable mechanism-gap; wall ALSO fails → obstruction promotes toward a real
  substrate statement ("a free propagating massless precursor can't become a bound resonator even with an
  external wall"), and ONLY THEN is Fork 1's gated confined precursor the remaining probe. **NEXT: Grant go
  on the moving-wall-on-Sector-B dispatch (replaces both forks).**

- **2026-06-16 (Phase 12 — Stage 1.6 DISPATCHED: moving Γ=−1 wall on Sector B, the CP8-safe OPEN route;
  Grant GO)** — dispatched `ave-implementer` `a474535a6f` (isolated worktree, branch
  `analysis/2026-06-16-boundary-mqj-stage16-moving-wall-sectorB` off `be459b7e` = the Stage-1.5 α-free
  engine). **Tests:** can an EXTERNAL moving Γ=−1 / Op17-bounded wall on **Sector B** (the photon's own
  sector, NOT the spectator Sector-A cage) confine the **propagating photon** so the energize-LOCK loop
  closes (`coupling_work ≠ 0`, vs (c)'s structural `f_V=0`) — with the **SAME generic seed UNCHANGED**
  (CP8-safety; re-seeding a confined precursor = the held-BC C′ plant hazard). Reuses the
  `saturation-tir-moving-boundary` precedent + Op17 infra. **NEW gate: CP8-SPATIAL-PROVENANCE** (seed_audit
  gates topology not spatial config; generic-offset sweep → loop-closure across a generic range = earned,
  one-tuned-offset = plant). **NEW: figure-emit** — the lane's first real matplotlib figures (moving-wall
  TDR, coupling_work-vs-(c)-baseline, dual-sector Sector-B Smith locus with the 1−α bake-(ii) leak marked
  echo-not-emergence, winding-vs-time, apparatus-floor known-positive). Bins: LOOP-CLOSES (→ emergence read
  → EMERGENCE-CANDIDATE) / WALL-CONFINES-BUT-LOOP-INERT / WALL-ALSO-FAILS (→ promotes to the substrate
  statement, then Fork 1's gated confined precursor) / PUMPS. Ckpt 8+10 + full-H witness + apparatus-floor
  known-positive + α-free inherited. **NEXT: Stage 1.6 returns → verify panel → adjudicate.**

- **2026-06-16 (Phase 13 — Stage 1.6 RESULT [recovered after a 500 killed the agent's final commit]:
  PUMPS [numerical] + physics = WALL-CONFINES-BUT-LOOP-INERT; load-bearing sublattice-registration open;
  verify dispatched)** — the agent ran 42 min / 79 tool-calls then died on a 500 Internal Server Error
  before committing its driver/JSON/figures + writing the result doc. **Recovered from the uncommitted
  artifacts; committed + pushed** to `origin/analysis/2026-06-16-boundary-mqj-stage16-moving-wall-sectorB`
  (recovery commit). **Result (from `stage16_moving_wall_sectorB_results.json`):** `verdict="PUMPS"` — but
  that is a **numerical BC issue**: K_wall=400 stiff wall NOT Op17-bounded at the operating amp=2.0, so
  |ω| diverges (omega_max→20032, diverged step 2530; the no-wall run also diverges →20006 — the photon at
  amp=2.0 is over-driven). **The PHYSICS = WALL-CONFINES-BUT-LOOP-INERT:** the moving wall **does confine**
  (Γ→−0.993 forms; `known_positive_PASS=true` — bounds a known photon, ω 3.6 with-wall vs 3954 without),
  but **`coupling_work=0.0` the ENTIRE trace** (from t=0, before divergence; `loop_fires=false`) — SAME as
  Stage-1.5 (c). The external wall confined the photon but its curl still did not couple to the cage.
  **CP8-spatial-provenance CLEAN:** generic seed (no plant), wall = Γ-field argmin recomputed every substep
  (generic rule), and the **generic-offset sweep is INERT-EVERYWHERE (0/6 fire)** → the inertness is
  generic, not a missed plant. α-free held (κ_chiral=0 override). The **figure-emit WORKED** (5 real
  figures: moving-wall TDR, coupling_work/f_V, Sector-B Γ Smith, winding, apparatus-floor — the lane's
  first plots). **🔴 THE LOAD-BEARING OPEN QUESTION (the agent's own `coupling_curl_sublattice` diagnostic):**
  the gate g and the curl Ξ register on **DIFFERENT sublattices** — `overlap_cells_cartesian=0` vs
  `overlap_cells_tetrahedral=1024` (gXi_cartesian=0, gXi_tetrahedral=2.92). So `coupling_work=0` may be
  **PHYSICAL** (curl genuinely does not co-locate, even confined) **OR a CARTESIAN-vs-TETRAHEDRAL
  grid-registration ARTIFACT** (the deflationary third option — if the coupling integral is computed on the
  sublattice where it is structurally zeroed, the experiment did NOT test the loop, structurally like
  Stage-1.5's ruled-out disabled-flag worry but now a grid bug). **DO NOT bank** — verify panel `w9q6nv9gm`
  dispatched (grid-registration: artifact-vs-structural · physics/PUMPS: separable-BC + does-the-wall-confine
  + does-WALL-CONFINES-BUT-LOOP-INERT-promote-to-the-substrate-statement). **Toolkit-audit note (§12):** the
  real-vs-reactive `coupling_work` classification is MOOT here (coupling_work=0, no work to classify); the
  applicable cross-check is **Op17 T²=1−Γ²** on the PUMPS (does the wall BC violate |Γ|≤1) — folded into the
  panel. **NEXT: panel returns → (artifact ⇒ re-run with matched registration / structural+PUMPS-separable
  ⇒ BC-fix re-run then the substrate statement) → Grant.**

- **2026-06-16 (Phase 14 — verify panel `w9q6nv9gm`: coupling_work=0 is a GRID-REGISTRATION ARTIFACT;
  Stage 1.6 VACUOUS *and* Stage-1.5 (c) RETROACTIVELY OVERTURNED; the loop was NEVER tested)** — the
  grid-registration lens + adjudicator (physics-lens 500'd but moot) returned **VACUOUS on the gated
  question**, grep+arithmetic-confirmed. **THE BUG:** the cross-sector coupling `f_V=−κ̃·g·Ξ` and the
  `coupling_work` accumulator use the **CARTESIAN curl** `_cosserat_axial_curl` (single-axis np.roll±1,
  `a1_cosserat_convergence_engine.py:337-347,366,379`); the moving-wall engine inherits it unchanged. But
  `mask_alive=(all-even)|(all-odd)` (`cosserat_field_3d.py:798-802`) → from any ALIVE cell every single-axis
  ±1 neighbor is **DEAD**, so the Cartesian curl Ξ is nonzero ONLY on dead cells, while g is alive-masked →
  **`g·Ξ_cart ≡ 0` for ANY ω field, confined or not = a disabled flag.** The engine's OWN coupling_overlap
  diagnostic proves it: cartesian overlap=0 vs tetrahedral overlap=1024 = `g_alive_cells` (the FULL
  alive-interior). On the substrate-native lattice g and the physical curl co-locate on EVERY alive cell —
  the supports are **NOT disjoint.** **Substrate-native-check Ckpt-2 violation:** the coupling Ξ is the ONLY
  operator still Cartesian — the wall Γ-field, `_beltrami_helicity`, and the saturation curvature all run on
  `_tetrahedral_curl`/`_tetrahedral_gradient`. **🔴 RETROACTIVE OVERTURN — Stage-1.5 (c) [Phase 11.1] was the
  SAME artifact:** its "STRUCTURAL irrotational / disjoint-support spectator" verdict — which `wpqwmrms0`
  VALIDATED ×4 lenses LEANS-EARNED, and which I BANKED — was the Cartesian-curl-on-dead-cells artifact, NOT
  physics. The "cage is a provable spectator (coupling_work bit-identical across variants)" evidence was
  ALSO fooled — g·Ξ_cart≡0 regardless of the variant. **None of the 4 prior lenses checked the curl STENCIL
  against the substrate-native operator (the missed substrate-native-check Ckpt-2).** Per Rule-12 /
  substitution-not-retraction the Stage-1.5 (c) disjoint-support mechanism paragraph + matrix row
  (`…stage15…_result.md:18,85-90`) need a 🔴 retraction header citing this diagnostic, NOT a silent
  re-narration. **WHAT SURVIVES:** the wall GENUINELY confines (Γ→−0.993, known-positive PASS — uncontaminated,
  from the Γ-field + photon dynamics, not g·Ξ). **PUMPS is separable** (K_wall=400 not Op17-bounded at amp=2.0;
  no-wall diverges too = over-drive) — fix independently. **DOES NOT promote to the substrate statement** (the
  wall DID confine → the WALL-ALSO-FAILS bin isn't hit; the loop-inert bin is unreadable, the test was
  disabled). **NET: the energize-LOCK loop-closure question is GENUINELY UNTESTED across BOTH Stage-1.5 (c)
  AND Stage-1.6 — the keystone is NOT leaning-negative; it was never tested.** **3 DECISIONS → GRANT:** (1)
  AUTHORIZE the dynamics amendment — re-run with Ξ on `_tetrahedral_curl` in `_coupling_forces`+`_coupling_energy`
  (one-line stencil swap, but a dynamics change → flagged amendment); (2) BOUND the wall (Op17 T²=1−Γ² cap, or
  sub-yield amp) before re-reading; (3) RETRACT-don't-re-narrate the Stage-1.5 (c) mechanism paragraph + row,
  hold Stage-1.6 OPEN (bank nothing). **NEXT: Grant authorizes the tetrahedral-curl re-run (the FIRST real
  loop-test) + the Stage-1.5 (c) 🔴 retraction.**

- **2026-06-16 (Phase 14.1 — breadth `aed621454`: CONFINED-TO-STAGE15-16; the re-run is NARROW + DUAL-GATED;
  lesson banked both lanes)** — audit-lane breadth-check resolved the systematic-vs-confined question:
  **CONFINED.** The Cartesian-single-axis-curl-on-parity-mask exists at **exactly ONE site**
  (`a1_cosserat_convergence_engine.py:345-347` `_cosserat_axial_curl`); `grep` returns nothing outside a1.
  Every other coupling engine is stencil-clean (`cross_sector_coupling`/`k4_cosserat_coupling` use full-axis
  `curl_central`, not alive-masked; `cosserat_field_3d`/`vacuum_engine` use the parity-respecting tetrahedral
  stencil). **#269 genesis-23 NOT contaminated** (GAP-1 = the missing-converter mechanism on `CoupledK4Cosserat`
  full-axis, closed by κ̃=6/5 — distinct; genesis-omega-wave = deliberate `disable_cosserat_lc_force`
  flag-zero — distinct). Bug confirmed 3 ways (incl. the auditor's 8³ reproduction: `g·Ξ_cart≡0` over 200
  random alive-masked ω). Audit-lane PRs `#269/#270/#271` = 0 files carry the verdict. → **NARROW one-spot
  fix, no coupling-layer-wide sweep, no re-opened negatives in the audit queue.**
  **🔴 THE DUAL-GATE CAVEAT (load-bearing — the re-run must NOT conflate stencil-fixed with loop-fires):**
  a1's `f_V≡0` has TWO STACKED causes — (i) the stencil bug (`g·Ξ≡0` for ANY ω) AND (ii) the SEPARATE
  committed layer-b PHYSICAL disjoint-support claim (the saturation front-shell g and the winding curl Ξ
  don't co-locate; the untrapped photon radiates out before the cage breathes deep). Fixing the stencil makes
  the disjoint-support question **TESTABLE FOR THE FIRST TIME** — and it can come back EITHER way. **The
  re-run gates on BOTH:** (a) `g·Ξ` now has alive support (parity fixed — overlap by construction) AND (b)
  the supports PHYSICALLY/DYNAMICALLY co-locate so `coupling_work` is ACTUALLY nonzero over the run. Outcomes:
  **overlap + loop FIRES → the bug WAS masking a real coupling → keystone ADVANCES** (then chord/echo); **supports
  still don't co-locate → disjoint-support is the REAL, now-properly-tested obstruction (a genuine negative,
  NOT a bug).** A stencil-only "it's fixed" read would be the same over-claim one level up. **Lesson banked
  (both lanes, shared memory `feedback_structural_null_needs_stencil_lens`):** an adversarial panel
  adjudicating a "structural null" MUST include a substrate-native-operator-stencil lens, or it validates
  discretization bugs as physics (substrate-native-check Ckpt-2 extended into the audit layer). **NEXT: Grant
  GO → dispatch the NARROW re-run (tetra-curl swap at the one site + Op17-bounded wall + the dual-gate
  parity-AND-dynamical-overlap verdict + the Stage-1.5(c) 🔴 retraction); both the no-wall Stage-1.5(c) config
  and the moving-wall config.**

- **2026-06-16 (Phase 15 — audit-lane PRE-FLIGHT `ww8x96sci` (#273) caught 3 MORE gaps in my re-run framing;
  amendments DISPATCHED; my framing CORRECTED)** — the audit lane handed a tracked corpus brief
  ([#273](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/273),
  `_orchestration/2026-06-16_engine-rerun-preflight-handoff.md`, branch …-engine-rerun-preflight-handoff) —
  **FIX-BEFORE-DISPATCH.** It pre-flighted the re-run I was about to dispatch and caught 3 verified gaps (2
  blockers), **two of which correct claims I made:** **(1) the tetra swap is TWO-SIDED, not one-site** — my
  "confined to one site" was the *curl* fn, but the reciprocal `f_omega` (`a1_cosserat_convergence_engine.py:369-372`)
  uses the same Cartesian `np.roll±1` on alive-masked `gV` and ALSO self-zeros on alive → a curl-only fix is a
  **source-only half-loop**; `f_omega` must swap to `adjoint_tetrahedral_divergence` (`cosserat_field_3d.py:161`).
  **(2) PUMPS is NOT separable** (I had it wrong; the physics-lens 500'd and never confirmed) — the wall
  **forms AND pumps together** (Γ→−0.993 WHILE H climbs 4.3e6), wall-coupled; `_rotate_clamp:1760-1783` has
  **NO |ω| ceiling** so "Op17-bound" was a false premise. **(3) BLOCKER — `coupling_work` is a signed
  energy-functional sum, not a measured transfer** — a bounded wall-pump reads LOOP-CLOSES unless gated on
  the conserved `coupling_hamiltonian_full()` ledger (computed, never gated). **+ my 3-bin framing DROPPED the
  frozen 4th bin** (`WALL-ALSO-FAILS`/wall-forms-and-pumps — driver:396-419 already uses the frozen 4; only my
  brief drifted) and cited the **phantom commit `230579b6`** (the engine lives on `a233f9ed`). **5 amendments**
  (all grep-anchored implementer fixes, not new physics): two-sided tetra swap · two-sided fire assertion
  (`fV_live_max>0 AND f_omega_alive_max>0`) · H-ledger bin gate · K_wall sweep (no ceiling exists →
  AMBIGUOUS-pending-stable-BC if none separates) · known-null meter + FROZEN-4-bins. **DISPATCHED** engine-lane
  implementer `acea7c7f20` (branch `analysis/2026-06-16-stage16-rerun-amendments` off `a233f9ed`) to fold in
  the 5 amendments + the Stage-1.5(c) 🔴 retraction + the provenance fix, VALIDATE the corrected engine
  (known-null=0, `f_omega_alive_max>0`, K_wall sweep) — but **NOT run the Q3 physics** (a false LOOP-CLOSES is
  worse than the delay). **GATE SEQUENCE:** amendments in → audit lane re-runs `ww8x96sci` pre-flight (GO-AS-IS)
  → **Grant authorizes Q3** → dispatch (both configs). **NEXT: implementer reports "amendments in" → signal the
  audit-lane pre-flight → Grant Q3.**

- **2026-06-16 (Phase 16 — DOCUMENTATION-COMPLETENESS audit `w0optx9ae`: NOT auditor-reconstructable today;
  backup gaps CLOSED, stale-leaf + index gaps queued)** — audit of every arc derivation vs its durable
  artifacts. **Verdict: an external auditor CANNOT reconstruct the arc from the committed record today**, two
  compounding reasons: **(1) BACKUP** — the entire adjudication NARRATIVE was off-origin (this tracker branch
  + the in-flight amendments branch local-only; the FROZEN discrimination prereg untracked). **CLOSED THIS
  PHASE (orchestrator-now):** pushed `analysis/2026-06-15-passive-eigenmode-solve` (this branch — the whole
  arc narrative, was unbacked) + `analysis/2026-06-16-stage16-rerun-amendments` to origin; copied the frozen
  discrimination prereg into tracked `research/2026-06-16_electron-existence-discrimination-prereg.md`; wrote
  the consolidated **arc INDEX** `research/2026-06-16_electron-existence-arc_INDEX.md` (the auditor-facing
  map — every derivation → prereg/result/JSON/branch/verdict/status). **(2) STALE LEAVES** — three committed
  result docs carry verdicts the arc SUPERSEDED, NOT flagged in the docs (corpus-grep visibility asymmetry —
  reader hits the leaf, not the tracker): 🔴 **Stage-1.5(c)** still reads clean wpqwmrms0-validated
  EMERGENCE-NEGATIVE (Phase-14 overturned it = grid-registration artifact) — THE load-bearing one, Rule-12
  retraction pending (amendments branch); **C′** banks "NEGATIVE-earned" (Phase-7 re-binned
  DISQUALIFY-WRONG-OBJECT) — re-bin pending (heldbc); **driver NEGATIVE-A** mis-binned (Phase-3f) + superseded
  (Phase-8) — annotation pending (driver branch). **Plus: Stage-1.6 result MD never written** (500-killed; the
  grid-registration diagnostic that DRIVES the Stage-1.5(c) overturn lives only in Phase-13). **Owners:**
  amendments-implementer (`acea7c7f20`) lands the Stage-1.5(c) retraction (tasked) + should write the
  Stage-1.6 result MD; the C′ re-bin + driver annotation are separate-branch edits; §11/§12/dimensional-analysis
  → land via the toolkit-index PR (Q3-dispatch). **GRANT-GATE (merge):** do NOT merge any arc branch until the
  3 stale-leaf corrections + the Stage-1.6 result MD land. **2 open Qs → Grant: (Q1)** land all 3 header
  corrections before merge vs tracker-authoritative + branch-docs-scratch? **(Q2)** is JSON+tracker the
  intended durable record for gate-class steps, or do Stage-1 / Stage-1.6 each get a result MD? **NEXT: fold
  the Stage-1.6 result MD + the C′/driver corrections into the amendments / a doc-backfill pass; Grant rules
  Q1/Q2.**

- **2026-06-16 (Phase 17 — amendments `acea7c7f20` IN + VALIDATED: Ckpt-2 fix works (GAP 1 closed); but
  K_wall sweep = AMBIGUOUS-pending-stable-BC + the wall-OFF baseline DETONATES → Q3 NOT clean-fire-ready)** —
  the 5 amendments applied on `analysis/2026-06-16-stage16-rerun-amendments` (engine `a5a34f7c` + driver
  `64d64e47` + retraction `2a83808c`; 129 pytest pass, 0 regressions; pushed). **VALIDATION (scope-guarded,
  NOT Q3):** **GAP 1 CLOSED** — the two-sided tetra swap (new `_cosserat_axial_curl_tet` + `f_omega` →
  `adjoint_tetrahedral_divergence`) makes `f_omega_alive_max` = 0.6–1.9 (was identically 0 on alive); overlap
  128 tet vs 0 Cartesian; adjoint verified (⟨grad V,T⟩=⟨V,adj_div T⟩ ratio 1.0000). Known-null meter = 0
  (−5.97e-9). **Reciprocity FD-clean** (f_V=−dH/dV ratio 1.0000; f_ω ratio 0.95) → the WALL-ON ledger climb is
  genuinely the wall BC, NOT a coupling sign bug. **🔴 K_wall sweep = AMBIGUOUS-pending-stable-BC:** NO K bounds
  the wall — low-K doesn't form (Γ≈0, H+50–90%); K=400 forms (Γ→−0.993) but H+110–1800%; K=800 runs away.
  `_rotate_clamp` has **NO |ω| ceiling** → confinement + pumping rise TOGETHER (GAP-3 "Op17-bound" premise
  confirmed FALSE). So Q3 at amp=2.0 PUMPS regardless of the (correct) stencil fix. **🔴 6th finding
  (implementer-flagged): the wall-OFF baseline DETONATES at amp=2.0** with the corrected stencil
  (`couple_on=False` → |ω|≈1926) — Stage-1.5(c)'s "inert-spectator coupling_work=0" was **DOUBLY an artifact**
  (the Cartesian stencil zeroed the coupling AND masked that the bare super-yield photon detonates). The prereg
  §1 / FIG-2 "inert-spectator" wall-OFF REFERENCE is broken → the meaningful comparison is now **WALL-ON
  conserved-ledger flatness** (the H-ledger gate), NOT ON-minus-OFF `coupling_work` magnitude. **Stage-1.5(c)
  retraction LANDED** (`2a83808c`, stale-leaf #1 CLOSED; arc INDEX updated). Provenance: no-op (`230579b6` in 0
  tracked docs). FROZEN 4 bins confirmed in driver (`:551/567/571/577`). **Q3 IS NOT CLEAN-FIRE-READY — needs
  a 6th amendment: (a) a genuinely bounded wall BC (an Op17 |ω| ceiling, NEW — `_rotate_clamp` has none),
  (b) sub-yield amplitude (so wall-OFF doesn't detonate), (c) the WALL-ON-ledger-flatness verdict (not
  ON-vs-OFF).** **NEXT: signal the audit-lane `ww8x96sci` pre-flight on the corrected engine — but the
  implementer's own validation already shows AMBIGUOUS-BC + the broken baseline → expect a 2nd
  FIX-BEFORE-DISPATCH (bound the wall + sub-yield + re-frame) before Q3. Surface to Grant + the audit lane.**

- **2026-06-16 (Phase 18 — DOC-BACKFILL COMPLETE [Grant ruled Q1=land-before-merge, Q2=result-MD-per-gate-step];
  arc now auditor-reconstructable FROM THE LEAVES)** — workflow `wnzalqm02` (3 worktree-isolated agents, `make
  verify` PASS each): **(1) heldbc** — C′ re-bin `6f4da77c` (Rule-12 demotion header top+§5 + JSON sibling
  `C_reading_rule12_correction`: "NEGATIVE-earned" → DISQUALIFY-WRONG-OBJECT / scalar-route CLOSED-NEGATIVE,
  cohabitation UNTESTED) + driver NEGATIVE-A annotation `7d1341ac` (mis-binned per `w92ft1gkc` + superseded
  Phase-8); all additive, original text preserved. **(2) stage16** — the missing Stage-1.6 result MD
  `d61e6530` (`research/2026-06-16_stage16-moving-wall-sectorB_result.md`): the PUMPS + WALL-CONFINES-BUT-LOOP-INERT
  + the grid-registration-artifact diagnostic, grounded vs the JSON. **(3) zwall** — Stage-1 gate result MD
  `55d27c04` (`research/2026-06-16_stage1-gate-boundary-mqj_result.md`): bucket-2 + the 4 corrections (incl.
  the 11.9P long-window number, was tracker-only). With the Stage-1.5(c) retraction (`2a83808c`) already in,
  **all 3 stale leaves are corrected + both gate-steps have result MDs — a corpus-grep reader now hits the
  CORRECTED verdict on every leaf.** Arc INDEX flipped to COMPLETE-from-leaves. **REMAINING (non-blocking,
  separate PR — Q3-dispatch owner):** §11 EE-sweep + §12 toolkit-audit + the dimensional-analysis lane still
  live only in the tracker → land in `ave-analytical-toolkit-index.md` via the queued toolkit-index PR. **The
  Grant-merge gate is now SATISFIED for the stale-leaf precondition** — when Grant runs #271→#270→#269 +
  the arc branches, no falsified verdict rides into main. **Q3 unchanged: held for the bounded-wall build
  (auditor v2 `w8qwhtslt` pending fold-in-vs-build + the catch-22).**

- **2026-06-16 (Phase 19 — 🔴🔴 SCALE/ARENA finding `wperakoc6`: the cavity IS one Nyquist voxel in the
  corpus but the engine runs MULTI-CELL — a FIRST-ORDER scale+representation mismatch BENEATH the stencil bug;
  GATES Q3)** — ⚠️ **SUPERSEDED-IN-PART by Phase 20 (Rule-12, 2026-06-16). The three DECISIVE claims below
  are OVERTURNED by direct code read: (a) the "real-space torus readout category error" is FALSE —
  `extract_2_3_omega_fast` and `poloidal_quadrature_content` build the SAME phasor `Z=(ω·d̂)+i(π_ω·d̂)` via
  the SAME `interp_vec_batch` sampler + Park-projection, differing ONLY in reducer (integer winding vs ±q
  Fourier); the (R,r) torus is the SAMPLING LOCUS, not the wound quantity — the readout is A46-clean; (b) the
  multi-cell arena is CORRECT-for-emergence (the frozen discrimination prereg DEFINES the chord axis as α-free
  emergence from generic IC, which needs a multi-cell box); (c) Q3 is therefore NOT frozen beneath an arena
  question — it is held on the bounded-wall build (pre-flight v2). What SURVIVES, scoped: dx=0.5 = 2×
  OVERsampling (finer resolution, NOT a sub-Nyquist fiction — minor cleanliness, normalize to dx=ℓ_node), the
  stale `dx=ℓ_node` comment, and the π flux-tube corpus-defect flag (→ reconciliation lane). Original text
  preserved below for the audit trail.** Grant's two questions, answered verbatim-grounded both sides. **(1) Cavity one voxel? CORPUS
  YES, ENGINE NO.** Corpus: the electron is a **single-Nyquist-cell, sub-cell** object — `ℓ_node`=reduced
  Compton=lattice pitch=spatial natural unit (`constants.py:255-257,302`); "the entire electron geometry fits
  inside ONE K4 cell," "a **sub-cell phase-space soliton: NOT a multi-cell extended structure**"
  (`electron-unknot-cosserat-seeder.md:22,63,67`; loop radius ≈0.159 ℓ_node, circumference=ℓ_node=one pitch);
  **"forcing a multi-cell propagating-eigenmode test on the bounded interior is a CATEGORY ERROR"**
  (`boundary-observables-m-q-j.md:87`); one mode per Nyquist cell, sub-cell structure unphysical
  (`op21:120`, `ch8:94`). Engine: **dx=0.5** (one cell = ½ ℓ_node) in BOTH engine defaults
  (`a1_cosserat_convergence_engine.py:82`, `…moving_wall…:109`) + all 4 drivers (`stage15_layer_a:47`,
  `…layer_c:53`, `stage16:54`, `boundary_mqj gate KP_DX:133`); N=24-28 (box=12-14 ℓ_node); soliton spread
  ~10-20 cells; saturated front `g_alive_cells=1024`. So the engine's "cavity" is a multi-cell breather, NOT
  one voxel. **(2) Scale correct? NO — mismatch on BOTH axes:** REAL-SPACE — dx=0.5 oversamples Compton 2×
  and renders a many-cell breather what the corpus says is single-cell/sub-Nyquist; the inline comment
  `boundary_mqj_selftrap_zwall_gate.py:94` "natural units: dx = ℓ_node" is **FALSE** (KP_DX=0.5 one line
  below → dx=ℓ_node/2) — smoking gun for unexamined drift. WINDING — the (2,3) is a phase-space intra-cell
  `(V_inc,V_ref)` bond-phasor winding with **NO real-space torus** (`electron-identification.md:23,77`;
  `master-equation.md:20`), but `extract_2_3_omega_fast` reads it on a **multi-cell real-space torus contour**
  (R,r in CELLS, `fast_winding_extractor.py:135-161`, R≈4.3-11.4 r≈1-4.4). **CREDIT:** the engine got the
  wound QUANTITY right (a phasor pair — it DODGED the A46 real-space-field trap); the defect is the SPATIAL
  carrier (multi-cell real-space at dx=0.5), not phasor-vs-field. **🔴 ORDERING — FIRST-ORDER, gates the
  stencil work:** the Cartesian-stencil bug (Phase 14) is SECOND-ORDER — it presupposes the multi-cell
  real-space lattice is the right arena. This says the arena itself is wrong. **Fixing the stencil to make
  the multi-cell real-space (2,3) coupling order-unity would VALIDATE A REPRESENTATION ARTIFACT** — the
  structural-null-stencil-lesson ONE LEVEL UP (wrong ARENA, not just wrong operator). **So the stencil fork +
  the bounded-wall build (Q3) must NOT be adjudicated as physics until the arena is resolved — this finding
  GATES Q3, not the reverse.** **THE INTENTIONALITY FORK → GRANT (flag-don't-fix, the one genuinely open
  question):** is the multi-cell lattice a DELIBERATE emergence arena (you need room for a generic precursor
  to self-LOCALIZE to one cell — CP8; the single-cell claim is then what the emergence test SHOULD PRODUCE,
  and multi-cell is correct FOR EMERGENCE while a category error for a boundary-observable EXISTENCE read) —
  OR unexamined DRIFT (dx=0.5 off the natural unit; the multi-cell breather + real-space torus is the wrong
  object)? Note: **the winding-READ category error (real-space torus vs intra-cell phasor) holds REGARDLESS
  of the arena answer.** **NEXT: Grant rules the intentionality fork (emergence-arena-by-design vs drift; is
  dx=0.5 intended?); if drift/category-error, the next engine tests the electron as a SINGLE Nyquist cell with
  an INTRA-cell (V_inc,V_ref) phase-space winding — NOT a multi-cell real-space breather + real-space torus.**

- **2026-06-16 (Phase 20 — ✅ REVERSAL of the Phase-19 SCALE/ARENA reframe; grep-grounded, both lanes
  self-corrected)** — The auditor lane ran an adversarial grounding (`w6lhjhsxn` + SCALE/readout/tie-break
  lenses) precisely to challenge its own enthusiasm for the Phase-19 "three-way convergence" (corpus + reframe
  + bounded-wall all naming the K4-TLM/LC-phasor engine). It **reversed**, and this lane **independently
  verified the decisive point by direct code read** before amending — NOT on the auditor's say-so (the original
  sin was banking `wperakoc6`'s reframe without reading the operative reader code; same lesson as `wpqwmrms0`).
  **DECISIVE — the readout is A46-clean (verified `808b8320` working tree):** `extract_2_3_omega_fast`
  (`fast_winding_extractor.py:198-234`) and `poloidal_quadrature_content` (`unified_genesis_engine.py:639-664`)
  both sample `omega` AND `pi_omega` via the SAME `interp_vec_batch`, Park-project onto the SAME ω-covariance
  principal axis `d̂`, and build the SAME phasor `Z=(ω·d̂)+i(π_ω·d̂)`; they differ ONLY in the final reducer
  (integer winding number vs the ±q Fourier coefficient `|A₊q|−|A₋q|`). The (R,r) torus is the spatial
  **sampling locus**, not the wound quantity. So `extract_2_3` IS the same A46-clean phasor read the engine lane
  itself cited as clean for the C′ panel — **the "real-space torus category error" is FALSE.** **Consequence:**
  the arena "gate" dissolves. The multi-cell box is the CORRECT stage for the α-free emergence test (the frozen
  discrimination prereg, `research/2026-06-16_electron-existence-discrimination-prereg.md:19,22-26`, defines the
  chord axis as the (2,3)/Γ=−1 FORM self-generating from generic IC — which needs room; N=24 is the BOX, not
  the object). **Q3 is NOT frozen beneath an arena question — the arena is fine; the only live structural item
  remains pre-flight v2's bounded wall** (the genuine finding, untouched by this reversal). **The Phase-19
  intentionality fork (deliberate-arena vs drift) is MOOT for the path forward** — multi-cell-for-emergence is
  fine either way. **What legitimately SURVIVES Phase 19 (scoped, credit):** (1) `dx=0.5` on the A1/stage15
  engines = 2× **OVERsampling** (resolves the cell finer; does NOT fabricate a multi-cell object — minor
  cleanliness, normalize to `dx=ℓ_node`, NOT load-bearing); (2) the stale inline comment
  `boundary_mqj_selftrap_zwall_gate.py:94` "dx=ℓ_node" vs `KP_DX=0.5` — a real comment/code mismatch; (3) a
  **real pre-existing corpus defect** (verified this lane): the flux-tube real-space geometry is internally
  inconsistent by exactly π — `electron-identification.md:22` sets tube CIRCUMFERENCE=ℓ_node (→ diameter
  ℓ_node/π≈0.318) while `electron-unknot.md:59` sets tube DIAMETER=ℓ_node ("d≡1 l_node"); one leaf confused
  circumference with diameter. Predates the arc → **FLAG to the reconciliation lane** (not this arc's to fix);
  (4) the narrow rider: gate de-novo `w_pol=0` reads behind the r≳3 contour-resolution floor before counting
  them physical. **META-LESSON (banked):** the Phase-19 three-way convergence was a coincidence-magnet — it
  re-explained the already-closed genesis-23→24→crystal negatives with a NEW unverified cause, the
  `challenge-canonical-negative` tell. BOTH lanes were swept; the adversarial grounding workflow + a direct
  read of the operative code caught it. The discipline worked — `feedback_challenge_canonical_negative` +
  `feedback_structural_null_needs_stencil_lens` validated. **CORRECTED NEXT: Q3 = pre-flight v2's bounded-wall
  build on the (correct) multi-cell Cosserat arena — a real build, NOT a representation/engine swap. No
  intentionality ruling needed from Grant. dx-normalize + the π-defect are non-blocking side-items.**

- **2026-06-16 (Phase 21 — 🟢 Q3 AUTHORIZED + DISPATCHED: the K4-TLM bounded-wall build)** — Grant gave the
  go. Dispatched a background worktree-isolated `ave-implementer` (`a056475de24c6853f`) on branch
  `analysis/2026-06-16-stage16-k4tlm-bounded-wall` off the amendments tip `2a83808c`. **Spec = the #273
  pre-flight 5-amendment brief with amendment-4 UPGRADED to a real build**, under the Phase-20 corrected
  framing (multi-cell arena CORRECT; readout A46-clean; this is a bounded-wall BUILD, NOT an engine/representation
  swap). The build: **port the K4-TLM unitary-scatter reflector** (`k4_tlm.py:402-423` `op3_bond_reflection`:
  per-bond Γ/T, `Γ²+T²=1`, power-conserving, |ω|-bounded by construction) as the Stage-1.6 moving-wall BC,
  replacing the unbounded `_rotate_clamp` (`cosserat_field_3d.py:1760-1783`, no |ω| ceiling → forms Γ→−0.993
  WHILE H climbs 4.3×10⁶). This resolves the posable-vs-meaningful catch-22: unitary reflection bounds |ω|
  WITHOUT clamping the reactive exchange the loop test measures. Amendments 1/2/3/5 already folded in on the
  base branch (`a5a34f7c` two-sided tetra swap; `64d64e47` two-sided fire + H-ledger gate + K_wall sweep +
  known-null meter). The K_wall sweep is KEPT as the motivating diagnostic (unbounded clamp → AMBIGUOUS, which
  is why the unitary wall is needed). **Bin gate = the FROZEN 4** (LOOP-CLOSES / WALL-CONFINES-BUT-LOOP-INERT /
  WALL-ALSO-FAILS / PUMPS); LOOP-CLOSES requires two-sided fire (fV AND f_omega both >0 on alive) AND
  H-ledger flat/decaying AND conserved-redistribution AND the known-null meter calibrated. Side-riders:
  dx=0.5→ℓ_node normalize (cleanliness); COMMIT the validation JSON (the arc's validation currently lives
  only in commit-message prose). **GATE ON RETURN: the auditor lane re-verifies the bin verdict + pre-flight
  clearance BEFORE this banks (auditor-not-exempt) — a false LOOP-CLOSES is the one outcome worse than the
  delay.** Implementer instructed to flag (not decide) any framing-level fork in how the unitary scatter
  couples the (ω,π_ω) pair. **STILL OPEN (Grant, separate from Q3): the #248/DEC-01 fork** — (a) close DEC-01
  (weak-C = the regime reading, register:388 stale) vs (b) scope-down #248 (canonize Branch-C-supersedes-A/B
  but keep primitive-vs-regime OPEN per the 2026-06-14 ruling; ACT-02 discriminates). #248 stays UNMERGED until
  ruled.

- **2026-06-16 (Phase 22 — 🟡 Q3 RESULT = PUMPS, but the loop is WIRED + the wall is HONEST + the pump is
  PRE-EXISTING; auditor-verified `a8232246`, NOT merged)** — Build `c5595558` returned, auditor re-verified
  adversarially (reproduced the load-bearing numbers by running the engine code, not on say-so). **5/6 claims
  CONFIRMED; bin = PUMPS (frozen 4, Rule-12 — corrected attribution is a qualifier, NOT a 5th bin).**
  **VERIFIED FACTS (bankable):** (1) **THE LOOP IS WIRED two-sided on alive — the stencil saga is RESOLVED.**
  Auditor RAN the operator: `adjoint_tetrahedral_divergence` puts `|f_ω|=1.31` on 117/128 alive cells, old
  Cartesian `np.roll` gives `0.0` on alive (GAP-1 self-zero reproduced), discrete adjoint closes
  `⟨grad s,T⟩=⟨s,adj_div T⟩=23.317` to float precision. `f_V=133.1` + `f_ω_alive=1.502`; tetra `|Ξ|=2.932`
  on alive w/ 1024 overlap (Cartesian 0). (2) **The K4-TLM unitary wall is energy-honest:** `MᵀM=I` to
  2.2e-16, `|ω|`=279.9 (vs `_rotate_clamp` 20918), `V_clamp≡0`, norm 1.0, α-free, (2,3) readout zero-diff.
  (3) **The PUMPS is NOT the wall — REATTRIBUTION EARNED:** H-pump is K-independent (798/887/798/807% at
  K=100/200/400/800, persists at K=400 where wall barely forms Γ_min=−0.053) AND present wall-OFF (control
  4.86×, |ω|max=20004; `_rotate_clamp` baseline cross-check 20008; coupling byte-inherited from `f4c91bd8`,
  the Stage-1.5 parent). The unbounded wall was MASKING a pre-existing pump in the energize-LOCK coupling +
  the two-grid bulk integration; amendment-4 removed the mask. (4) Driver `verdict_reason` "|ω| blow-up /
  divergence" is CONFIRMED mis-attributed (|ω| bounded 279.9, `diverged=null`; `50·amp` threshold mis-fires).
  **🔴 THE GATE — Finding 3, UNPROVEN:** the "continuum `H_c` cancellation is EXACT" claim — the ENTIRE
  license for "fixable discretization bug" over "substrate negative" — lives ONLY in engine docstring
  `a1_cosserat_convergence_engine.py:374` (quoted by the result doc); NO derivation, NO KB leaf, NO proof.
  **🔴 CHALLENGE-CANONICAL-NEGATIVE (prospective, on our own result):** `loop-gap-electron-resonator-closure-
  doctrine.md:30` records energize-LOCK as a CANDIDATE path with **"genesis-24: pump FALSIFIED"** on the same
  row — **this PUMP may be genesis-24's falsified pump RESURFACING.** "Two-grid time-centering bug" is the
  live hypothesis AND the explain-away shape; given this pump already killed one incarnation, the bar to call
  it "just a bug" is HIGH (the cavity-reframe lesson applied prospectively). **NOT banking "it's a bug."**
  **THE OPEN FORK (NOT yet rule-able — gated on earning the premise):** fixable two-grid coupling-integrator
  time-centering bug (`step_coupled:444-470` — `f_ω` frozen across `n_sub_cos` Sector-B substeps, a known
  discrete-coupling pump source) vs GENUINE SUBSTRATE STATEMENT (a free massless precursor cannot losslessly
  close the loop even with a perfect wall → keystone leans NEGATIVE). **THE DISCRIMINATOR (auditor-identified,
  cheap + decisive, gated on Grant authorization):** (a) the continuum `dH_c/dt=0` integration-by-parts proof
  (highest leverage — converts the fork's premise from asserted→forced); (b) a time-centering known-positive:
  re-run with `n_sub_cos=1` (single-grid, `f_ω` recomputed every step/half-step-centered) + a recompute-
  cadence sweep + a `dt` sweep of the H-climb rate — if H flattens as centering matches → bug (keystone stays
  open, fix + re-test); if H climbs even at matched single-grid centering → substrate (keystone negative).
  **No conservation known-positive currently exists** (the `known_null_meter` −1.76e-7 is a METER calibration,
  not a conservation control). **TWO HYGIENE CALLS → Grant:** (i) continuum-exact language — have the
  implementer write the `dH_c/dt=0` proof as a `sup-` node before banking, OR downgrade to "conservative-by-
  structure, cancellation-proof-pending"; (ii) the `verdict_reason` string — bank with the §5 FLAG as
  authoritative override, or fix the `diverged_note` threshold first. Side-rider: dx-normalize applied to
  stage15 a/c (flagged for owner re-validation), `boundary_mqj` KP_DX left 0.5 (dx-coupled to seed radius)
  with corrected comment; primary verdict stays dx=0.5 (apparatus floor passes there, F-1 SOUND). F-2:
  property-3 (`electron-identification.md:24,25`) forces the TIR-reflector FORM but NOT the `Ω₀` reactance-
  plane normalization (one honest free sub-choice). Branch `analysis/2026-06-16-stage16-k4tlm-bounded-wall`
  tip `c5595558`, 4 commits ahead of `2a83808c`, NOT merged.

## §9 — OPTION C pre-registration (held-BC breather-persistence PROBE; Rule-11 spirit, pre-committed)

**🟢 HELD OBJECT (explicit, per Grant — so a verifier cannot misread):** the held object is the
**PHASE-SPACE (2,3) Clifford-torus winding** (charge) on the **(ω, ω̇) phasor** — **NOT a real-space
knot**, and **NOT** the A1 `(V_inc,V_ref)` breather phasor. The (2,3) is the toroidal-2 + poloidal-3
*phase-space* winding number (`ch8-alpha-golden-torus.md:31` / `electron-identification.md`); cite the
(p,q) phase-space home, NOT `def-3638f2` (the `ambiguous` homonym node on exactly this real-vs-phase
axis). "Re-project the conserved (2,3) topology" = the phase-space reading.

**Physical question:** with the (2,3) charge-winding **HELD** (enforced as a conserved topological
constraint each step — charge conservation, the law the seed-and-evolve driver violated), on the
co-resolving lattice where the A1 mass-breather is real (N=26-class, dx=0.5, ≥5–10 cells), does the
**charge-carrying mass-breather PERSIST** as a bounded, recurrent, non-decaying (except the Q=1/α
radiative leak) mode over many breaths? *(Plumber: pin the conserved circulation on the ω-tank,
energize the LC mass-tank, watch whether it keeps ringing or the pinned charge fights it into
collapse.)*

**What I expect (honest):** uncertain. The mass-breather alone persists (wall-half VINDICATED). The
open question is whether the held charge is **compatible** with it — does the breather carry the
conserved winding stably, or does the constraint destabilize the mode (or vice-versa)?

**Discriminator:**
- **POSITIVE (C-clear → proceed to A):** the held-winding mass-breather **persists** (bounded,
  recurrent, F2-stable over many breaths), the winding stays (2,3) **by construction** (the hold
  works), AND the hold is **CONSERVATIVE** (energy-neutral). → the mass-cavity carries the conserved
  charge stably; strong evidence the electron is a coherent winding-protected mode → build the full
  A self-consistent eigensolve (find-the-pole).
- **NEGATIVE (C-fails):** even with charge held, the breather **decays / destabilizes**, OR the only
  way to keep it standing is to PUMP it → the two sectors do not cohabit → keystone leans negative
  (cheaply, before paying for A).
- **🔴 DISQUALIFY (`ave-conserved-vs-pumped`):** if the (2,3)-hold **injects energy** (a pump, not a
  conservative constraint), a "persistent" result is a **pumped artifact**, NOT bankable as positive.
  The hold MUST be energy-neutral; verify via the energy ledger BEFORE reading persistence.

**Mechanism (`substrate-native-check` + `phase-space-coordinate-check`):** "hold the winding" =
re-project / enforce the (2,3) on the **independent Cosserat-ω carrier** in **PHASE-SPACE** coords
(the (ω, ω̇) phasor / Clifford torus, NOT real-space; A46) each step — a **conservative** projection
(a constraint, not a drive). Never wire it into the A1 (V_inc,V_ref) phasor (the double-count;
G0-clean — preserve it). **C builds this held-BC machinery — which A then reuses + adds the
residual→0 eigensolve.**

**Guards:** `ave-conserved-vs-pumped` (the hold is a conserved constraint, energy-neutral) ·
`substrate-native-check` (hold a topological integer, don't seed-and-evolve it) ·
`phase-space-coordinate-check` (phasor, not real-space) · `ave-driver-script-honesty` (report the
energy ledger + persistence as measured; do not tune) · `ave-apparatus-floor-attribution`
(persistence = physics or a pump/box artifact). **C result → adversarial-verify panel → A iff clean.**

---

## §9.1 — OPTION C′ pre-registration amendment (hold the conserved H_bel, NOT the director template; Grant-greenlit 2026-06-16)

**Why the amendment:** C (the per-cell director-template hold) **DISQUALIFIED** — it pumped 56× by
**overwriting local ω-directions** against the free gradient flow (the verify panel `wvd0c2oib` found
it held the WRONG object). The corpus's conserved charge is **Beltrami helicity** `H_bel = ∫ω·(∇×ω)`
(`master-equation.md:20`, verified verbatim), which the engine has as a **local density**
(`_beltrami_helicity`, `cosserat_field_3d.py:450`, used :521/:581) but does **NOT** track/constrain as
an integral. C′ holds the **conserved H_bel integral**, the corpus's actual charge.

**HELD OBJECT (corrected):** the conserved **H_bel = ∫ω·(∇×ω)** (a single global topological invariant),
NOT the per-cell director template. On the **independent Cosserat-ω carrier** (phase-space; NEVER the
A1 `(V_inc,V_ref)` phasor — G0-clean preserved).

**MECHANISM:** a **NO-WORK constraint** that holds H_bel at its (2,3) target — **energy-neutral BY
CONSTRUCTION** (a Lagrange-multiplier / symplectic-orthogonal correction projected ⊥ the energy
gradient; the gentle global constraint, NOT the brute per-cell overwrite). Build the integral on
`_beltrami_helicity`; the correction must do **zero work by design** (verify via the ledger, but
design it neutral — unlike C where neutrality was only *measured*, and failed).

**PHYSICS:** conserving H_bel **protects the (2,3) topology** — the winding cannot disperse without
changing the helicity, which the constraint forbids. **KEY DESIGN CHECK:** verify that conserving the
*scalar* H_bel actually **maintains the (2,3) winding PAIR** (toroidal-2 + poloidal-3 via
`extract_2_3_omega_fast`). If H_bel-conservation does NOT maintain (2,3), that is a **finding** (the
scalar helicity is too coarse to pin the pair) — report it, do not force.

**DISCRIMINATOR (same §9 bins; NEGATIVE is now EARNED because the hold is conservative):**
- **POSITIVE (C′-clear → A):** the H_bel-held mass-breather **persists** (bounded, recurrent,
  F2-stable over many breaths), the **(2,3) is maintained**, AND the hold is **energy-neutral** (ledger
  flat by construction). → the mass-cavity carries the conserved charge stably → build A (the
  residual→0 eigensolve; target eigenvalue **Q = α⁻¹ ≈ 137**, chord/echo per §6).
- **NEGATIVE (now meaningful):** even with H_bel held **conservatively**, the breather decays /
  destabilizes → the sectors do not cohabit → keystone leans negative (EARNED, not the pump-masked C).
- **🔴 DISQUALIFY:** even the H_bel constraint **pumps** (it shouldn't, if built no-work) → the
  mechanism is still wrong; report + do not bank.

**Guards:** `ave-conserved-vs-pumped` (energy-neutral BY CONSTRUCTION, the full-Hamiltonian witness —
not `sum(ω²)`, the C false-positive) · `substrate-native-check` · `phase-space-coordinate-check` ·
`ave-driver-script-honesty` · `ave-apparatus-floor-attribution`. **C′ result → adversarial-verify →
A iff clean.** Persist the (still-missing) C soft-sweep artifact or scope its "no-window" claim to
hard-hold (A47, deferred-not-blocking).

---

## §11 — EE DIAGNOSTIC + SWEEP PROGRAM (2026-06-16, workflow `wknrs0aal`)

**Are we using the full EE toolkit? NO.** Recon (grep-confirmed): the drivers emit the impedance/reflection
NUMBERS — `Z_eff=√(S_μ/S_ε)` + `Γ=(Z_eff−1)/(Z_eff+1)` (`k4_cosserat_coupling.py:577,673-674`;
`cosserat_field_3d.py:1638-1639`), an explicit "TRUE Smith reflection coefficient" `Γ_true=(n−1)/(n+1)`
(`passive_eigenmode_driver.py:357-366`, off-main), field-level `S11=Σ|Γ|²` (`cosserat_field_3d.py:1285`),
a GENUINE ring-down Q (`measure_Q_from_decay:602-615`, off-main), geometric Q (`extract_quality_factor:2208`),
Hopf charge, winding — **but ZERO matplotlib anywhere; every read is reduced to medians/scalars/JSON,
never kept as a swept LOCUS.** Genuine ABSENT diagnostics: **dispersion ω(k)** (the 3 existing FFTs are
period-only / phase-scramble / Poisson-inverse-curl — none a band read), **TDR**, **S21/S12/S22** (only
S11 exists), and a **continuous amplitude-bifurcation** trace (only `_pick_stable_amplitude` stability-pick).

**🔴 THE ECHO-TRAP (load-bearing; bake structure CORRECTED by audit-lane 2026-06-16, grep-verified):**
there are **TWO distinct α-bakes** in `cvr_model.py` (`src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`):
**(i) Q=1/α — instance-level**, `Q_TANK=1.0/ALPHA` at **`:72`** (NOT `:58` — that's a section comment;
orchestrator slip, fixed) injected via `M.ELECTRON` (`:380`); the form functions `poles/H_scalar/H_chiral`
are keyword-only `*, Q: float` with **no default** → REMOVABLE by feeding a *measured* Q into the clean
forms (don't route through `M.ELECTRON` / `M.Q_TANK`). **(ii) |Γ_EM|²=1−α — universal, Q-INVARIANT**, in
`gamma_em_sq()` (asserted "must not vary with Q") — a SEPARATE bake that staying Q-α-free does **NOT**
remove. Consequence: every instrument agrees on α/137 because they read bake (i) (Smith gap, Bode peak,
S21 notch, Nyquist offset = the SAME number on different displays → **plotting more instruments does NOT
escape echo**); AND even after deleting bake (i), the dual-sector Smith STILL shows the wall **1−α short of
the rim** (bake (ii)) — reading THAT gap as emergence is the echo. The chord is earned ONLY by (a) DELETING
bake (i) (measured-Q into the clean forms) + recovering Q from a cold generic precursor, (b) the genesis
bifurcation LATCHING from a non-planted T2 precursor, (c) a wide IC basin converging to the (2,3) form,
(d) a bound branch self-splitting below the band-edge — FORM-emergence, never the 1−α gap (bake (ii)).

**🔴 INSTRUMENT-FLOOR CATCH (apparatus-floor; SOFTENED by audit-lane 2026-06-16 — prior "uninterpretable /
bench may be broken" was an ORCHESTRATOR OVERSTATEMENT, owned):** the PLV/autoresonance LOCK **leg** IS
floored — `t2_genesis_selflock.py:585-590` in-code DETECTOR FLAG: the known-positive self-focusing sech
bins UNRESOLVED at PLV<0.80 despite ringing-up + persisting. **BUT NO-GENESIS is WEAKENED-not-INVALIDATED:**
the t2 doc already self-scopes — verbatim "the (C) DISPERSE verdict rests on the VALIDATED ring-up/persistence
legs, NOT the PLV/F3 leg" (legs the photon arms fail independently). The floored leg was already set aside;
NO-GENESIS stands on the independent legs. **The real (narrower) adjudication → GRANT (in-code flagged
"auditor+Grant adjudicate"):** does a legitimate *genesis* call REQUIRE the phase-coherence/autoresonance
leg (→ floored PLV leaves NO-GENESIS ambiguous, PLV-repair load-bearing) OR do ring-up + persistence alone
suffice (→ NO-GENESIS holds, PLV-repair is hygiene)? The repair is worth doing but does NOT by itself reopen
NO-GENESIS. **TWO independent apparatus-floor benches** (neither inherits the other): this PLV detector
(`t2_genesis_selflock._phase_coherence`, free-running) is DISTINCT from the audit-lane jw-adjudicator's
lock-IN amplifier (`s11_probe_unified.lockin`, driven I/Q) — different code, no shared path (the "lock"
homonym was a false alarm).

**Prioritized sweep matrix (targeted at α-free emergence, NOT echo magnitudes):**
- **P0 — Genesis bifurcation diagram** (Stage 1.5): GENERIC T2 precursor A₀→past-yield (up+down), plot
  A1-standing-V order-parameter; LATCHED hysteretic switch-on = chord, flat A1-V=0 = the 2026-06-14
  FAIL/echo signature. THE headline — only tool testing FORM-emergence dynamically AND α-free. *Asterisk:
  trustworthy only after the LOCK-detector repair.*
- **P0 — α-free Q-extraction** (Stage 3): feed a MEASURED Q into the clean form functions (delete bake (i):
  no `M.ELECTRON`/`Q_TANK=1/α` at `cvr_model.py:72`), ring-down the self-formed cavity — does Q≈137 EMERGE
  untold? (Running it on the as-built tank = pure echoTrap; the separate 1−α leak (bake (ii)) survives regardless.)
- **P1 — Smith / Γ-plane self-trap LOCUS** (cheap, re-plot existing Z/Γ as a trajectory, not a median;
  **DUAL-SECTOR** per the H3 wall-branch fork / PR#260 — the dual-sector Smith is the instrument that forces
  the magnetic-vs-longitudinal wall label, an audit-lane unique-add): does a generic precursor's Γ migrate
  center→rim? CAVEAT: the terminal |Γ|²=1−α is bake (ii), NOT an emergence read — the locus shows the trap
  FORMS, not that α emerged.
- **GATE (elevated P1→gate, audit-lane add) — Dispersion ω(k)** also settles the `k_max` corpus contradiction
  (`0.577/ℓ_node` vs `π/ℓ_node`, ~5.4×) by reading k_max off the Brillouin edge — load-bearing, not just corroborating.
- **P1 — Dispersion ω(k) bound-mode** (new observer): does a flat/localized branch split below the band-edge
  (existence leg, α-free by construction)?
- **P1 — Precursor-IC basin sweep**: fraction of GENERIC ICs converging to the same (2,3)+Γ=−1 (wide basin
  = attractor/chord; knife-edge = planted/echo) — most direct test of criterion (1).
- **P1 — LOCK-detector repair + known-positive validation** (instrument-floor gate for P0).
- **P2 — TDR moving-wall**, **3-Γ disambiguation tag** (Γ_spinor/Γ_impedance/|Γ_EM|²=1−α — guards the
  genesis-24 double-count), **S21 stopband-notch** (confinement corroboration; floor is the 1−α echo).

**Fold-in:** Stage 1.5 RETURNED (Phase 11) **α-free end-to-end** (grep-confirmed: no `M.ELECTRON`/`Q_TANK`/
`V_yield=√α` leak). The P0/P1 sweeps + **figure-emit** + the **TWO-bench apparatus floor** (this lane's
PLV-detector-repair + the audit-lane stability-classifier `|ω|→1144` jw-axis gate) + the dual-sector Smith
are the **Stage-1.6+ analysis emit-list**, gated on Grant's TWO adjudications (the Stage-1.5 precursor fork
[confined-vs-propagating] + the genesis-requires-coherence-leg question). Full matrix: workflow `wknrs0aal`.

---

## §12 — Analytical-toolkit application audit (workflow `wy0sfe4jm`, 2026-06-16)

**Verdict: applying the toolkit's REFLEXES, not its DISCIPLINE.** The obvious per-class tools are APPLIED +
grep-confirmed (Op2 saturation kernel; Γ_true Smith reflection `passive_eigenmode_driver.py:357-366`;
dual-sector Z=√(S_μ/S_ε) vs Z_long=√(L/C_comp); the full-Hamiltonian pump-witness = Op14 cross-sector;
(2,3)/Hopf/Beltrami topology reads) — they did real work (bucket-2 + LOCK-vs-PUMP at Phase 9). But the full
canonical SET an index-consult would surface was NOT pulled. **Six MISSED-but-applicable tools:**
1. **🔴 §6 Mode — dispersion ω(k) band-read (HIGHEST-value miss).** The keystone is EXISTENCE; ω(k) is the
   α-free-by-construction existence instrument, more direct than the breather-persistence proxy. Its absence
   FORCED existence-by-stability-proxy (the NEGATIVE-A/REFUTED/DISQUALIFY churn Phases 3b-7) AND left the
   `k_max`=0.577 vs π/ℓ_node ~5.4× corpus contradiction open. No extractor exists in any driver.
2. **🔴 §1/§5 — orbital-friction real-vs-reactive classification of `coupling_work` (LOAD-BEARING FOR STAGE 1.6).**
   `coupling_work` is a bare scalar (`a1_cosserat_convergence_engine.py:162,422`), never tagged P_real(cosθ)
   vs Q_reactive(sinθ). The electron bond is REACTIVE (lossless LC, P_real=0); a nonzero-REAL coupling_work =
   a dissipative category error masquerading as the conservative winding↔cage exchange. **If Stage 1.6
   returns LOOP-CLOSES, the coupling_work MUST be real-vs-reactive classified BEFORE banking success** — else
   a real-power leak is mis-read as the chord. (`ave-power-category-check` Axis A.)
3. §1/§5 — Op17 `T²=1−Γ²` as a transmitted-fraction LEAK instrument (EXISTS `universal_operators.py:833`,
   battery-wrapped; ZERO arc driver calls it — "Op17" appears only as a CP10 rendering LABEL). A 2nd
   independent read of the α-leak the lane only measured via decay-envelope. (THE exact failure the index
   was built to prevent — the matched-LC Op17 miss.)
4. §1/§2 — Theorem 3.1' radiation impedance Z₀/(4π) per spinor cycle (cited only to set Q_TARGET=1/α, never
   instantiated). A 3rd independent α read; the Op17/Z₀-4π/decay triad cross-checks a wrong-prefactor error.
5. §2/§8 — the dual-sector Smith swept LOCUS (per-cell Γ exists, median-collapsed; zero matplotlib) — queued
   for Stage-1.6 figure-emit; lower-value (the locus terminal is itself the bake-(ii) 1−α echo).
6. §9/keystone — the M/Q/J read (𝓜/𝓠/𝓙→m_e/e/ℏ/2) was DECLARED the substrate-correct test (Phase 8) but
   never RAN (`computes_MQJ:False`); the arc redirected to emergence (Phase 10). **OPEN ROUTING → Grant: is
   M/Q/J RETIRED or merely PARKED behind the emergence question?** Stage-1.6 needs one sentence.

**Toolkit UPDATES the arc surfaces (to land in `ave-analytical-toolkit-index.md` via branch+PR on Grant's
go — corpus, main-protected):** (a) §6 add a dispersion-ω(k) tool ROW + the k_max-contradiction GATE
(currently §6 has only the Nyquist pitfall, no extractor); (b) §2/§5 add the TWO-BAKES ECHO-TRAP pitfall
(α-tank carries α twice: Q=1/α planted + the 1−α Smith-short by construction; deleting bake-(i) ≠ escaping
echo); (c) §1 add the SPECTATOR-CAGE / f_V=0-structural diagnostic (bit-identical across variants ⇒
spectator, not a physical null; classify reactive/real before binning); (d) §9/§8 bank the EE diagnostic
sweep matrix as a reusable network-diagnostic template; (e) §9/§7 add the CP8-spatial-provenance gate as a
methodology note. **3 INDEX GAPS exposed:** (i) a MOVING Γ=−1 wall has NO §7 entry (only static TIR); (ii)
Topology (Hopf/Vakulenko-Kapitanski/Beltrami/(2,3)) has NO consolidated tool table — the arc pulled from KB
leaves directly, even found an engine-vs-corpus normalized-helicity conflict; (iii) Cosserat/micropolar has
no dedicated class. **NOTE: skill-vs-index DRIFT** — the `ave-analytical-tool-selection` skill body lists
classes 10-12 (Topology/Cosserat/Statistical, added by adversarial-probe #17) but the actual INDEX stops at
§9; the probe amended the skill, never the index. **NEXT (this lane): fold misses #2/#3/#4 into the Stage-1.6
ADJUDICATION (real-vs-reactive coupling_work + the Op17/Z₀-4π/decay α-triad cross-check); the index-update
PR + the M/Q/J routing are Grant calls.**
