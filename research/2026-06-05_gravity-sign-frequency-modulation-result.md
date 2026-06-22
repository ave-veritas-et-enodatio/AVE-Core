# RESULT — Gravity sign via reactive LC frequency-modulation

**Status:** COMPLETE, 2026-06-05. Implementor session, branch `analysis/gravity-sign-freq-modulation` (off `origin/main` @ `0e3890df`).
**Prereg (frozen):** [`2026-06-05_gravity-sign-frequency-modulation-prereg.md`](2026-06-05_gravity-sign-frequency-modulation-prereg.md)
**Verification script:** `src/scripts/verify/gravity_sign_freq_modulation.py` (+ `_results.json`) — numpy-only, imports G, C_0, L_NODE, Z_0, MU_0, EPSILON_0, M_SUN from `ave.core.constants`; NO hard-coded GR targets.
**Companion:** [`2026-06-05_gravity-ppn-coherence-result.md`](2026-06-05_gravity-ppn-coherence-result.md) (separate branch `origin/analysis/gravity-ppn-coherence`).
**Class:** Internal-COHERENCE + intuition-correction (**Class C**). NOT an emergence test, NOT an AVE-distinctness claim. The corpus already classifies weak-field gravity (lensing/Shapiro/perihelion) as "AVE = GR at O(GM/c²r), no AVE-distinct observable."

## Verdict (one line)

**SIGN is SETTLED by frequency-modulation; the factor-2 is NOT.** Grant's reactive-LC-frequency-modulation framing yields the **correct lensing sign cleanly** (H1 PASS) and the **invariant-Z reflectionless gravity** exactly (Z = Z₀ to 2.2×10⁻¹⁶). But the brief's **two-reactance {1/S, 1/√S} factor-2 mechanism does NOT map cleanly** from the canonical {c_EM = c₀/S, c_shear = c₀√S} and **conflicts with canonical Op16** — so H2 is **FLAGGED, not confirmed**. The canonical factor-2 remains carried by the **2/7 : 1/7 Poisson projection** (unchanged). Per the prereg STOP condition ("if the c_EM/c_shear↔index mapping resists, STOP and report — do not force it"), the H2 mapping is reported as **NOT-FORCED**, surfaced for Grant adjudication, not papered over.

---

## Phase 1 — SIGN (H1): does frequency-modulation give the correct sign? YES.

**Setup (substrate-native, EE-first).** Each K4 node is an LC tank with `L_cell = μ₀ℓ_node`, `C_cell = ε₀ℓ_node`, ringing at `ω_node = 1/√(L_cell C_cell) = c₀/ℓ_node` at the cold lattice (C5, vol9 ch10:41). Symmetric (gravity-class) loading drives the node toward its yield point at operating amplitude `A` (A = A/A_yield ∈ [0,1)), with kernel `S = √(1−A²) ∈ (0,1]` (Ax 4, C3). Two lumped reactances each **rise as 1/S** under their own-sector drive (canonical, vol4 ch1):
- electric sector — metric varactor `C_eff(V) = C₀/S` (eq:varactor),
- magnetic sector — relativistic inductor `L_eff(I) = L₀/S` (eq:relativistic_inductor),
- and these "are projections of the single Axiom 4 kernel onto the electric and magnetic sectors" (vol4 ch1:278).

**The node rings slower under loading (time dilation).**
```
ω_node = 1/√(L_eff C_eff) = (1/√(L₀C₀))·S = ω_node,0 · S   → DROPS as S→0
```
This IS Grant's lever: a frequency/phase re-tuning of the tank. At rupture (A²→1, S→0) the local clock freezes — exactly Op14 `ω_local = ω_global√(1−A²)` (op14-local-clock-modulation.md:11).

**The signal speed drops → n > 1 → light bends toward mass.** The energy-transport (group/signal) speed is the lensing observable, NOT the phase velocity. Three signal-side speeds, all dropping under loading:

| speed | expression | trend | index n = c₀/c | source |
|---|---|---|---|---|
| node LC frequency | ω_node = ω₀·S | DROPS | — | C5, Op14 |
| group / mass-freeze | c_shear = c₀√S | DROPS | n_shear = **1/√S > 1** | claim-quality:113, Op16 |
| both-reactance signal | c_light = ℓ/√(L_eff C_eff) = c₀·S | DROPS | n_light = **1/S > 1** | derived from C_eff,L_eff=·/S |

**The phase velocity rises — and that is fine.** The constitutive (small-signal transverse-probe) parameters move the *other* way: `ε_eff = ε₀S`, `μ_eff = μ₀S` (both < 1, C3/C4). Then
```
Z = √(μ_eff/ε_eff) = √(μ₀S/ε₀S) = √(μ₀/ε₀) = Z₀          INVARIANT (verified to 2.2e-16)
c_EM = 1/√(μ_eff ε_eff) = c₀/S   → RISES (>c₀)            Maxwell PHASE velocity
```
`c_EM = c₀/S` is the **phase** velocity (claim-quality:111: "c_EM,sym = c₀/S → ∞, EM phase velocity rises"). Phase velocity exceeding c₀ carries no energy and is **not the ray observable** — exactly as the brief anticipated. The ray (group) velocity is c_shear (or c_light), which drops.

**H1 verdict: PASS.** Verification (`gravity_sign_freq_modulation.py`, phase1): all signal speeds drop monotonically; both bending indices > 1; phase c_EM rises; Z/Z₀ deviates by 2.22×10⁻¹⁶ (machine zero). Sample at A=0.5 (S=0.866): ω_node/ω₀ = 0.866, c_light/c₀ = 0.866, c_shear/c₀ = 0.931, c_EM/c₀ = 1.155, n_light = 1.155, n_shear = 1.075, n_EM = 0.866 (<1, phase). **The principle yields the correct sign: loading → freq down → signal speed down → n > 1 → light bends toward mass.** Reflectionless because Z is invariant.

**Sign reconciliation (the S-vs-1/S knot, resolved).** The corpus carries two reciprocal "loading" conventions that move ε,μ in opposite directions, and conflating them is where a sign error would hide:
- **Saturation-S convention** (Ax 4): `ε_eff = ε₀S, μ_eff = μ₀S` with S ≤ 1 (load → ε,μ DOWN). Gives c_EM = c₀/S (phase up), c_shear = c₀√S (group down).
- **Gravity-n convention** (C6, `eq_gravity_derived.tex`): `μ_eff = μ₀·n, ε_eff = ε₀·n` with n = 1+2GM/rc² ≥ 1 (load → μ,ε UP). Gives c_local = c₀/n (down), n > 1.

These are **reciprocal: n ↔ 1/√S** for the temporal/clock index (canonical, op14-local-clock-modulation.md:45: "`n(r) = 1 + 2GM/(rc²) ≈ 1/√S`"). Both conventions agree on the physical outcome: **the signal/group speed drops and n > 1.** No sign ambiguity once the phase (c_EM) vs signal (c_shear/c_light) distinction is held — which is precisely Grant's framing.

## Phase 2 — TWO-REACTANCE / factor-2 (H2): exact map + the FLAG

**The exact c_EM/c_shear ↔ index map (n = c₀/c_signal).** Verified in `gravity_sign_freq_modulation.py` (phase2), sample S=0.8:

| canonical speed | value | index n = c₀/c | numeric (S=0.8) |
|---|---|---|---|
| c_shear (group/mass/clock) | c₀√S | **1/√S** | n_shear = 1.118 |
| c_EM (Maxwell phase) | c₀/S | **S (< 1)** | n_EM = 0.800 |
| c_light (both reactances, signal) | c₀·S | **1/S** | n_light = 1.250 |

**Load-bearing correction to the brief's H2 framing:** the brief mapped "`c_EM = c₀/S` → n_light ≈ 1/S." This is **arithmetically wrong** as stated: `c_EM = c₀/S` is a speed *above* c₀, so its index is **n_EM = c₀/c_EM = S < 1**, NOT 1/S. The index `1/S` is the index of the **both-reactance signal speed** `c_light = c₀·S` (the speed of a packet that sees BOTH L_eff and C_eff loaded by 1/S), not the index of c_EM. So "light to BOTH (the L·C product) → n_light ≈ 1/S" is recoverable, but **via c_light = c₀·S, not via c_EM.** c_EM is the phase velocity and plays no bending role.

**Does {1/S, 1/√S} give factor-2 arithmetically?** YES, in the weak-loading limit. With matter at n_matter = 1/√S (one sector / group) and light at n_light = 1/S (both reactances):
```
(n_light − 1)/(n_matter − 1) = (1/S − 1)/(1/√S − 1)  → 2   as S → 1
```
Verified numerically: ratio = 2.0050 (ε=10⁻²), 2.00050 (10⁻³), … 2.0000005 (ε=10⁻⁶). Exact-2 in the limit; ≈2.08 at A=0.5 (finite-loading correction, fine for weak field). So the reactance-counting **number** is 2.

**THE FLAG (flag-don't-fix — surfaced, NOT reconciled).** The {1/S, 1/√S} reactance-counting factor-2 is a **different mechanism** from the canonical one, and it **conflicts with canonical Op16**:

1. **Conflict with Op16 (the decisive one).** Canonical `Op16 Universal Wave Speed = c_shear = c₀√S` (operators.md:56) is *universal* — the D'Alembertian Op13 "uses local saturated c_eff … per Op16" (operators.md:53). A **propagating wave** (including the transverse-EM photon) therefore travels at c₀√S → index **1/√S** — the **SAME index as matter**. If light and matter both sit at 1/√S, the deflection ratio is **1, not 2** (verified: `op16_light_index_equals_matter_index_FLAG: True`). For the brief's H2 to hold, light must travel at c₀·S (index 1/S, steeper than the universal wave speed) — but the corpus's universal propagating-wave speed is c₀√S, not c₀·S. **The corpus does not assign light the index 1/S anywhere; it assigns the universal wave speed c₀√S.**

2. **Different mechanism than canonical.** The canonical factor-2 (C8, `02_general_relativity_and_gravity.tex:179-206`) is the **2/7 : 1/7 Poisson projection** of one strain field ε₁₁: light couples transversely (Poisson ν_vac = 2/7), matter couples to the isotropic bulk (1/7), and `(n_⊥−1)/(n_scalar−1) = (2/7)/(1/7) = 2` (verified: poisson ratio = 2.0). Both indices have the form `1 + k·χ_vol` — the factor-2 is in the **coupling coefficient k**, NOT in the **power of S**. The reactance-counting story puts the factor-2 in the {1/S vs 1/√S} *powers* of a single loading kernel. These are two structurally distinct routes to the same number.

3. **The coincidence-magnet tell.** Per the "challenging a canonical negative" discipline: two different mechanisms landing on the *same* number (2) is a coincidence-magnet. The honest reading is that frequency-modulation cleanly delivers the **sign + invariant-Z** (H1), but the **factor-2 is over-determined** — it is already carried by the Poisson projection, and the reactance-counting route reaches 2 only by assigning light a steeper index (1/S) than the canonical universal wave speed (1/√S → index of *everything* that propagates). I do **not** reframe either mechanism to match the other.

**H2 verdict: FLAGGED (not confirmed).** Exact index map established (c_shear→1/√S, c_EM→S, c_light→1/S). Reactance-counting ratio → 2 in the weak limit. But the mapping **resists** clean attachment to {c_EM, c_shear}, and conflicts with Op16. Per the prereg STOP condition this is reported as NOT-FORCED. **The canonical 2/7:1/7 Poisson factor-2 is unchanged and remains the load-bearing derivation** (it reproduces 4GM/bc² = 1.7517″ = GR; see Phase 4).

## Phase 3 — BENCH per-sector validity (H3): consistent, with one tension flagged

**The claim under test.** Static external E (no ∂B/∂t) loads the **capacitive sector only** → asymmetric scaling → Z-step → reflection (bench signal valid); a mass-soliton (Beltrami standing wave, internal E **and** B) loads **both** sectors → symmetric scaling → Z invariant → reflectionless gravity. Asymmetric-bench and symmetric-gravity must be mutually consistent under per-sector loading.

**The two-mechanism Z taxonomy is canonical and consistent (C2/C9, claim-quality:111-112).**
- **SYMMETRIC** (gravity, BH interior, particle confinement): μ and ε both scale → `Z_sym = Z₀` (invariant) → Γ = 0, reflectionless. RF-transparent stealth, `S₁₁ = −∞ dB` (C9, `01_vacuum_circuit_analysis.tex:438-447`).
- **ASYMMETRIC** (one sector only): `Z_asym = Z₀/√S → ∞` → impedance step → reflection. The bench falsification tests (C12, `11_experimental_falsification.tex:185-189`) read exactly this asymmetric Z-step (TVS/Zener rupture, Γ = −1 at V_yield).

So the *structural* premise — asymmetric→reflective, symmetric→reflectionless — is **canonical and internally consistent**. A static-E bench probe that loads one sector produces a Z-step and a measurable reflection; a mass-soliton loads both and is reflectionless. No contradiction at the taxonomy level.

**The mass-soliton loads BOTH sectors (C10, confirmed).** Vol 2 Ch 1:40: the electron is "a Beltrami standing wave where the continuous **E** and **B** field lines are mutually orthogonal and feed into each other in a closed topological loop (∇×A = kA), permanently trapping the energy"; Vol 2 Ch 1:35: "Mass is the stored **inductive** energy …" while the resonant LC loop also stores capacitive/strain energy (Virial, vol4 ch1:524-525). Internal E+B ⟹ both sectors loaded ⟹ symmetric ⟹ Z invariant ⟹ reflectionless gravity. Consistent with the symmetric branch.

**TENSION (RESOLVED 2026-06-22 → see verdict below; preserved as flagged for trail).** The brief's H3 premise that *static external E loads C only / μ_local = μ₀ under DC* read at the time as in tension with the Ax 4 small-signal modulation (C3/C4, `manuscript/ave-kb/CLAUDE.md:73,75`; was `:58,:60`), which as then-worded read as if a DC operating-point bias scales **BOTH** μ and ε **symmetrically**:
> Small-signal transverse propagation through a region at operating point A₀ sees modulated effective parameters `ε_eff = ε₀ S(A₀)`, `μ_eff = μ₀ S(A₀)`, `C_eff = C₀/S(A₀)` — the same varactor-bias mechanism … (Op14 local clock modulation, Op16 universal wave speed).

i.e. canonical DC-bias modulation is **SYM-class (both sectors, Z invariant)**, not the C-only ASYM the bench premise assumes. Two readings, surfaced for adjudication (NOT resolved here):

- **(R-a) Regime distinction.** The canonical "DC bias scales both" (C4) is the **per-node operating-point shift A₀** that requires facility-class fields (~8×10¹⁶ V/m to reach appreciable per-node A₀; `manuscript/ave-kb/CLAUDE.md:75`). The bench falsification tests (C12) operate at **large-signal apparatus voltages** that drive the *capacitive* sector to rupture (V_yield ≈ 43.65 kV across the apparatus geometry) without a matching B-drive — genuinely **asymmetric** in that regime → Z-step → reflection. Under R-a, the bench (asymmetric, large-signal, C-sector rupture) and gravity (symmetric, both-sector soliton/operating-point) are **consistent** because they live in different drive regimes.
- **(R-b) The "loads C only" wording is CORRECT even small-signal — and is the WINNING axis.** "Static external E loads C only" does **not** contradict C4 once C4 is read with its W6 scope: C4's both-scale form is the **symmetric-internal** operating point (both grades driven). A static *external* E is **asymmetric by construction** — it loads the V-keyed varactor (ε) but has no ∂B/∂t to load the I-keyed relativistic inductor (μ), so S_μ=1 even small-signal. The reconciliation is therefore a **scope rescope of C4 (R-b axis: symmetric-vs-asymmetric LOADING)**, NOT a large-signal-vs-small-signal regime split (R-a). R-a is consistent but is not where the resolution lives; the keyed-argument duality (node-up leaf) is.

**H3 verdict: RESOLVED 2026-06-22 (commit e5307e53 W6 scope + node-up leaf).** The reconciliation is the **R-b rescope axis** (symmetric-internal-loading scopes C4), NOT the R-a regime distinction: a static-external E is asymmetric by construction (loads ε only, S_μ=1) because the μ-grade is an I-keyed relativistic inductor with no ∂B/∂t under DC. INVARIANT-S2 now carries this scope at `manuscript/ave-kb/CLAUDE.md:75`; the node-up small/large-signal derivation is canonical at `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md`. The asymmetric-bench / symmetric-gravity consistency holds; the "μ_local = μ₀ under DC / loads C only" phrasing is now canonical, not flagged.

## Phase 4 — VERDICT, classification, W2/W4 queue

### Is the sign crack SETTLED by frequency-modulation?

**The SIGN: YES, SETTLED.** Grant's reactive-LC-frequency-modulation lever delivers the correct lensing sign cleanly and without convention-juggling: loading drops ω_node (time dilation) → the signal/group speed drops (c_shear = c₀√S, c_light = c₀·S) → n > 1 → light bends toward mass — at **invariant impedance Z = Z₀** (verified to 2.2×10⁻¹⁶), hence reflectionless. The phase velocity c_EM = c₀/S rising above c₀ is the expected reactive-tank behavior and is *not* the ray observable. This is exactly the "frequency/phase re-tuning of a lossless tank at invariant impedance" framing, and it reproduces the canonical symmetric-gravity Z-invariance (C2/C6/C9) from the LC-tank picture. **The "denser medium / which-way-does-light-bend" intuition crack is closed by the reactance-retuning picture: light slows because the local tank rings slower, not because the medium is denser.**

**The FACTOR-2: NOT settled by frequency-modulation.** The two-reactance {1/S, 1/√S} mechanism reaches the *number* 2 in the weak limit but (a) does not map cleanly from {c_EM, c_shear} — c_EM's index is S, not 1/S; (b) conflicts with canonical Op16 (universal propagating-wave speed = c₀√S → index 1/√S, the same as matter → ratio 1); (c) is a structurally different mechanism from the canonical 2/7:1/7 Poisson projection, which is over-determined with it. Per the prereg STOP condition the H2 mapping is reported **NOT-FORCED**. **The canonical factor-2 (2/7:1/7 Poisson) is unchanged and remains load-bearing.**

**Overall (against the frozen adjudication criteria):** H1 **PASS**, H3 **PASS** (under R-a), H2 **FLAG** (cleanly explained: frequency-modulation gives the sign + invariant-Z; the factor-2 is carried by the Poisson projection, and the reactance-counting route to 2 is over-determined/Op16-conflicting). Per the frozen "Overall SETTLED" rule (H1 PASS ∧ H3 PASS ∧ (H2 PASS ∨ H2-FLAG-cleanly-explained)): the **sign sub-claim is SETTLED**; the **factor-2 sub-claim is NOT settled via frequency-modulation** and stays with the Poisson mechanism.

### consistency-vs-emergence classification (load-bearing)

**Skill fired:** `consistency-vs-emergence` (Trigger: compute an AVE observable and compare to GR with overlapping inputs; the work depends on `ave.core.constants`).

- **Inputs traced:** `G` — CODATA-derived (constants.py:156); the lensing number routes through G via the standard weak-field formula → **Class C structural dependence** (remove G, prediction dies). `C_0` defined SI; `M_SUN`, `R_SUN` IAU observational. `S = √(1−A²)`, `Z = √(μ/ε)`, `ν_vac = 2/7` axiom-derived.
- **Class designations:**
  - **Sign + Z-invariance: identity/manifestation-class.** `Z = √(μ₀S/ε₀S) = Z₀` is an algebraic **identity** (S cancels); the sign follows from the kernel monotonicity. No CODATA target enters. This is the *intuition-correction* core of the result.
  - **Lensing number (1.7517″): Class C consistency.** AVE = GR at O(GM/c²r) **by construction** (the 2/7 photon index reduces to √(g_ij/−g₀₀)_GR; companion PPN audit §4). predictions.yaml P10 already tags this `consistency_check`. Agreement is structural, NOT predictive.
- **`ave-discrimination-check`:** consistency-class, **NOT distinct**. There is no SM/GR-counterfactual-distinguishing observable here. The result must **NOT** be headlined as emergence or distinctness. It is an internal-coherence + intuition-correction fact about the corpus's gravity sector.
- **Promotion ceiling (clean):** nothing is reclassified upward. The H2 FLAG and H3 wording-tension are surfaced for adjudication, NOT fixed; no canonical leaf edited (Rule 6 / Rule 12).

### pre-test-physics-check — surfaced question (did NOT halt; sign question well-posed)

The prereg flagged: STOP if frequency-modulation does not cleanly give the sign, or the c_EM/c_shear↔index mapping resists. **The sign question is well-posed and cleanly answered (H1 PASS) — no halt on the sign.** The **mapping did resist** for the factor-2 (H2): per the scope guard I report it NOT-FORCED rather than forcing {1/S,1/√S} onto {c_EM,c_shear}. The one plumber-physical question I surface to Grant:

> **In the LC-tank picture, does a propagating photon ride the "universal wave speed" c₀√S (canonical Op16 — same speed as a mechanical shear wave / a matter packet, index 1/√S), or a steeper both-reactance signal speed c₀·S (index 1/S)?** If Op16 (c₀√S) is universal for *all* propagating waves including light, then light and matter share the index 1/√S and the {1/S,1/√S} reactance-counting factor-2 cannot stand — the factor-2 must come from the Poisson coupling (2/7:1/7), not from a difference in S-power. If instead light couples to the *full* L·C product (c₀·S, index 1/S) while matter (a standing soliton, not a propagating wave) couples to one sector (c₀√S, index 1/√S), the reactance-counting factor-2 is physical. The corpus currently says Op16 is *universal* (operators.md:53,56), which favors the first reading and demotes the reactance-counting factor-2 to a coincidence-of-the-number. **This is the framing-level fork only Grant should call.**

> **R1-INDEX FORK RESOLVED 2026-06-22 (Grant call (a)).** Grant ratified **n = 1/√S** as the canonical R1 small-signal ray/probe index: a propagating photon rides the universal Op16 wave speed c_shear = c₀√S (`operators.md`:56), so δn ≈ +¼ A² (positive; light slows, gravity-well-like). The reciprocal **n = 1/S form (δn ≈ +½ A², the "both-reactance signal" c₀·S) is REJECTED** — it propagates nothing; nothing in the corpus assigns light the index 1/S. This is the **first reading** above (Op16 universal). Consequently the {1/S, 1/√S} reactance-counting factor-2 **cannot stand**, and the canonical factor-2 remains carried by the 2/7:1/7 Poisson projection (H2 verdict below unchanged). Basis: `operators.md`:56 (Op16 c_shear = c₀√S universal) + commit e5307e53 / INVARIANT-S2 W6 scope. The Maxwell **phase** index n_EM = S (c_EM = c₀/S rises, carries no energy) is a phase-velocity aside, distinct from the probe observable n = 1/√S.

### Walk-back queue (NOT applied here — for a separate adjudicated session)

Per scope guards, no canonical leaf or Ch 14 is edited in this session. Queued for adjudication (Rule 12 substitution-not-retraction: flags, not retractions; no slot refilled):

- **W4 (Ch 14 density-language — this brief's primary queue).** `manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex:63`: "the inner edge of an orbit is travelling through a *denser, higher-impedance* topological medium than the outer edge." Under Grant's principle Z is **INVARIANT** (reactance re-tuned at constant Z₀, C2/C9), so "higher-impedance" is the **energy-density framing**, not the reactance-retuning framing. Candidate resolution for Grant/auditor: replace "denser, higher-impedance" with reactance-retuning language ("a more strongly-loaded, slower-ringing LC region at the same characteristic impedance Z₀"), consistent with `01_vacuum_circuit_analysis.tex:438-447` (gravity is Z-invariant). The *math* (inner edge slower) is unchanged; only the interpretive density/impedance language is at issue. **The same "denser optical medium" language also appears at `03_macroscopic_relativity.tex:105` and `16_sagnac_inductive_drag_spice.tex:28` ("inductively denser vacuum path, increased μ_eff") — flag the set, do not edit.**

- **W2 (redshift slope factor-2 — re-queued from companion PPN audit).** `eq_gravity_derived.tex:53,63`: `n_temporal = 1 + (2/7)ε₁₁ = 1 + 2GM/c²r` (so n_temporal − 1 = **2GM/c²r**), but the same file states the redshift is `z ≈ GM/c²r` (the GR value, **half**). The companion PPN audit (W2) surfaced this identical tension and queued it for Grant. Re-queued here because the frequency-modulation picture sharpens the plumber-physical question: **if n_temporal is the "how slow does the clock tick" index, its slope should be 1 (z = GM/c²r); but the corpus writes slope 2.** Under Op14, the clock factor is `ω_local/ω_global = √S ≈ 1 − GM/c²r` (slope 1), which matches z = GM/c²r — so the Op14/√S clock index (slope 1) and the `n_temporal` (slope 2) label are **two different quantities wearing the same hat**. Needs Grant framing adjudication before any edit. (Companion audit also queued W1 (9/7 "controls light deflection" outlier) + W3 (Ch14 V_tidal redundancy) on its own branch — out of scope here.)

- **H2-FLAG (factor-2 mechanism).** **R1-INDEX FORK RESOLVED 2026-06-22 (Grant call (a)):** the canonical R1 ray/probe index is **n = 1/√S** (Op16 universal c_shear = c₀√S, `operators.md`:56); the n = 1/S "both-reactance signal" form is **rejected** (propagates nothing) — see the resolved fork note in the pre-test-physics-check section. This confirms the **first reading**: light and matter both ride 1/√S, so the {1/S, 1/√S} reactance-counting factor-2 **cannot stand**. The canonical 2/7:1/7 Poisson factor-2 stands unchanged and remains the load-bearing derivation. Basis: `operators.md`:56 + commit e5307e53 / W6.

- **H3-RESOLVED (2026-06-22, commit e5307e53 + node-up leaf).** "static external E loads C only / μ_local = μ₀ under DC" is **canonical**, reconciled with C4 via the **R-b rescope axis** (C4's both-scale form is the symmetric-internal operating point; a static-external E is asymmetric by construction because the μ-grade is an I-keyed relativistic inductor with no ∂B/∂t under DC → S_μ=1). NOT the R-a regime distinction. Scope now at `manuscript/ave-kb/CLAUDE.md:75`; node-up derivation at `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md`.

### Verification numbers (AVE-derived; GR recomputed from imported G, no hard-coded target)

Source: `src/scripts/verify/gravity_sign_freq_modulation.py` → `gravity_sign_freq_modulation_results.json`. Imports `G = 6.674300e-11`, `C_0 = 2.997925e+08`, `L_NODE = 3.861593e-13`, `Z_0 = 376.7303`, `MU_0`, `EPSILON_0`, `M_SUN = 1.989e30` from `ave.core.constants`. External: R_SUN = 6.957×10⁸ m (IAU 2015).

```
Phase1 SIGN (PASS):
  signal speeds (omega_node, c_light, c_shear) all DROP monotonically : True
  bending indices n_light=1/S, n_shear=1/sqrt(S) both > 1             : True
  phase velocity c_EM=c_0/S RISES (not the ray observable)            : True
  Z_local/Z_0 invariant, max deviation                               : 2.22e-16
  at A=0.5 (S=0.866): n_light=1.155  n_shear=1.075  n_EM=0.866(<1,phase)

Phase2 MAP+factor2 (FLAGGED):
  c_shear -> index 1/sqrt(S)                                          : 1.118 (S=0.8)
  c_EM    -> index S  (NOT 1/S)                                       : 0.800 (S=0.8)
  c_light -> index 1/S                                                : 1.250 (S=0.8)
  reactance ratio (n_light-1)/(n_shear-1) -> 2 in weak limit          : 2.0000005 (eps=1e-6)
  Op16 light index == matter index (=> ratio 1, FLAG)                 : True
  canonical Poisson (2/7)/(1/7)                                       : 2.0

Phase4 LENSING (Class C consistency):
  AVE (2/7) photon index, Snell-gradient delta=2K*GM/bc^2 (K=2)       : 1.7517 arcsec
  matter (1/7), K=1 (Soldner)                                        : 0.8759 arcsec
  GR Einstein 4GM/bc^2 recomputed from imported G                    : 1.7517 arcsec
  ratio light/matter                                                  : 2.0000  (Einstein/Soldner)
  ratio light/GR                                                      : 1.0000  (Class C, by construction)
  observed solar deflection                                          : 1.75 arcsec
```

**n_light = 1/S, n_matter = 1/√S, sign = correct (n > 1, light bends toward mass). Z invariant to machine precision. Lensing = GR exactly (Class C). Factor-2 via reactance-counting reaches 2 but is FLAGGED (Op16-conflict + over-determined with Poisson).**

---

## Summary table

| Sub-claim | Verdict | Mechanism |
|---|---|---|
| H1 SIGN (loading → n>1 → bends toward mass) | **PASS / SETTLED** | ω_node drops at invariant Z; signal speed drops; phase c_EM rises but isn't the observable |
| Z invariant (reflectionless gravity) | **PASS** (2.2e-16) | √(μ₀S/ε₀S) = Z₀ identity (SYM-class, C2/C9) |
| H2 factor-2 via {1/S, 1/√S} | **FLAGGED, NOT-FORCED** | reaches 2 in weak limit but Op16-conflicting + over-determined with canonical 2/7:1/7 Poisson |
| H3 bench/gravity per-sector consistency | **PASS under R-a** | asymmetric→reflective / symmetric→reflectionless taxonomy canonical; soliton loads both (E+B) |
| Canonical factor-2 (2/7:1/7 Poisson) | **unchanged, load-bearing** | reproduces 4GM/bc² = 1.7517″ = GR |
| W4 (Ch 14 density language) | **QUEUED** (not edited) | Z-invariant ⟹ "denser, higher-impedance" is energy-density framing |
| W2 (redshift slope factor-2) | **QUEUED** (not edited) | n_temporal slope 2 vs z≈GM/c²r slope 1; Op14 √S clock = slope 1 |

**Class C internal-coherence + intuition-correction. NOT distinctness, NOT emergence. No canonical leaf edited; all walk-backs queued for Grant adjudication.**
