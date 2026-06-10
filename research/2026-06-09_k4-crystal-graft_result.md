# RESULT — The K4 Crystal Graft: c_eff(V) trap + conserved ADD-2 converter ON the K4 4-port winding carrier

**Date:** 2026-06-09 · **Lane:** implementer · **Branch:** `analysis/2026-06-09-crystal-k4-graft` (worktree off `analysis/2026-06-09-crystal-engine-design`)
**Engine:** [`src/ave/core/k4_crystal_graft.py`](../src/ave/core/k4_crystal_graft.py) — the K4 4-port carrier (`k4_tlm.py`) + the c_eff(V) bond-Γ wall (Op14, op3_bond_reflection) + the conserved ADD-2 port-rotation converter.
**Driver:** [`src/scripts/vol_1_foundations/k4_crystal_graft_run.py`](../src/scripts/vol_1_foundations/k4_crystal_graft_run.py) · **JSON:** `k4_crystal_graft_results.json` (N=26)
**Predecessor:** [`research/2026-06-09_crystal-engine_result.md`](2026-06-09_crystal-engine_result.md) — the SCALAR-bulk Outcome C, whose §5 surfaced this exact graft as the next step.
**CANONICAL-AVE-ONLY (Grant 2026-06-09):** electron = LONGITUDINAL K4 monopole bulk (the "3"); photon = transverse chiral port mode; absorb/emit = Axiom-4 crystallize/melt via the front converter. Zero QED/Maxwell-vector framing.

---

## §0 — VERDICT: **SMOKE-FAIL** on SMOKE-3 — the real-space trap and the phase-space winding are **DECOUPLED**. (SMOKE-1 + SMOKE-2 PASS. The full α-emergence run is REFUSED by the frozen guard.)

> **The c_eff(V) trap GRAFTS onto the K4 4-port (SMOKE-1 PASS: a Γ→1 bound state forms, retention ratio ~5000× over the
> linear control) and the conserved ADD-2 converter fires CONSERVATIVELY (SMOKE-2 PASS: orthogonal rotation, residual
> 2e-12, centrosymmetric baseline EXACTLY 0, fields O(1) — 4 OOM below genesis-24's detonation). And — the real
> progress over the scalar-bulk Outcome C — the K4 (V_inc,V_ref) phase-space IS a genuine winding carrier: it carries
> w_tor=1.98 at the seed (the scalar bulk carried NOTHING). BUT SMOKE-3 (the load-bearing new check) fails: the
> real-space trap does NOT drive/sustain the phase-space winding. The winding collapses to 0 within ~5 steps,
> identically with the trap ON and OFF — the amplitude-wall binds the +1 isotropic monopole (the trapped MASS) while
> the winding rides the −1 transverse chiral modes (the PHOTON), which radiate away. A real-space-amplitude-trapped,
> phase-space-winding object is INCOHERENT in one scalar-wall engine. Per the frozen guard (a false Class-D is
> strictly worse than an honest negative), the α-emergence run is NOT forced.**

**Why SMOKE-FAIL and not a forced A/B/C (Rule 11 + the frozen α-guard):**
- The task's de-risk gates are explicit: *"(3) PHASE-SPACE … does a real-space-localized trap actually drive phase-space winding, or are they incoherent? If any smoke fails → STOP + report (SMOKE-FAIL) — do not force the full run; the failure mode (esp. real-space-vs-phase-space incoherence) is itself the key finding."* SMOKE-3 reveals exactly that incoherence.
- Forcing the leak-Q / Golden-Torus / joint-ledger run on an engine that **cannot sustain a (2,3)** would measure the Q of a resonator that does not exist → a **param-fluke** number that could masquerade as Class-D. The hard constraint (Grant 2026-06-09: *"a false Class-D chord is strictly worse than an honest C; freeze the α-emergence guards BEFORE running"*) forbids it. The guard fired.

---

## §0.1 — THE HARD PART (surfaced + resolved) and the load-bearing answer

**The fixed-roll-vs-variable-speed problem (`k4_tlm.py:378-383` np.roll connect vs c_eff(V) variable speed) — RESOLVED, and the resolution is itself a finding:**

The K4 `_connect_all` propagates every wave packet exactly one diamond-bond per dt — the lattice **light-cone**, the *maximum* speed. c_eff(V)=c0·(1−A²)^(−1/4) **diverges** in the saturated core; you **cannot roll faster than the light-cone** on a fixed-dt explicit lattice (causality/CFL). So c_eff→∞ is **not** representable as a faster transport. But c_eff→∞ ⟺ refractive index n=c0/c_eff→0 ⟺ a **stopband** ⟺ **total reflection** at the core boundary — and a reflective stopband **is** representable on the fixed-roll lattice as a **bond impedance reflection**. Op14 already supplies the identical law z_local=Z_eff/Z_0=(1−A²)^(−1/4) (`k4_tlm.py:291-294`); a wave entering the high-impedance core sees Γ_bond=(z−1)/(z+1)→+1 and reflects. **The variable wave-speed manifests as REFLECTION, not as a re-timed connect.** This is the physically correct TLM encoding of a refractive medium (impedance loading, not variable transport). I did **not** modify np.roll.

**genesis-24's fix (Flag-5e-A):** genesis-24 had op3_bond_reflection=True yet relaxed to Γ→0/matched because the K4 strain was V_inc/V_SNAP_SI ≈ 10⁻⁶ → saturation **dormant**. The graft passes **V_SNAP = V_yield (engine units)** so the saturation engages — and the wall forms (SMOKE-1).

**The load-bearing answer to the task's central question** — *"make a real-space-trapped, phase-space-winding object coherent, or surface precisely why it can't be done in one engine"*: **It cannot, with a single scalar-amplitude trap, and the reason is a single mechanism (below). A second, mode-selective (chiral) confinement is required — and that is exactly the object that detonates when rendered as a bulk pump (genesis-24).** This answers the pressure-test's double-counting question empirically: one wall cannot do both jobs.

---

## §1 — SMOKE-1: does the Γ-wall bound state form on the 4-port? **PASS**

| quantity | value | criterion | pass |
|---|---|---|---|
| interior-energy retention, sharp strain-snap front (post-transient mean) | **0.277** | > 0.2 (bound state persists) | ✓ |
| same, SMOOTH (sech) seed | **1.3e-5** | (the smooth seed does NOT trap) | — |
| same, LINEAR control (op3 OFF, no wall) | **5.6e-5** | (radiates fully) | — |
| retention ratio (sharp / linear) | **~5000×** | the wall traps | ✓ |
| \|Γ_core\| (bond reflection, mean post-transient) | **1.000** | →1 total reflection (vs genesis-24 Γ→0) | ✓ |
| core strain A (mean post-transient) | **1.086** | > R_II=0.866 (saturated) | ✓ |
| breathing (E-retain std/mean) | **0.010** | < 0.6 (bounded, steady bound state) | ✓ |

**The c_eff(V) trap grafts onto the K4 carrier** — the bound state retains ~28% of its energy behind a |Γ|→1 wall while the
linear control radiates to ~0 (ratio ~5000×). The decisive contrast with **genesis-24** (Γ→0/matched, no bound state).

**The load-bearing sub-finding (the fixed-roll consequence):** the wall forms **only with a TRUE first-order strain-snap
FRONT** — a top-hat, a 1-cell impedance **discontinuity**. A **smooth** seed (sech OR super-Gaussian) does **NOT** trap
(retention 1.3e-5 ≈ the linear control). This is direct: the bond-Γ reflection Γ=(z_B−z_A)/(z_B+z_A) is a **gradient**
effect that needs an actual STEP; the scalar Master Equation's wall is a **path-integrated absolute-c_eff** effect (it
self-focuses a smooth profile) that the **fixed light-cone connect cannot transport**. Consistent with A-034
crystallization being **first-order** (strain-snap), not a smooth refractive well. **(Figure 1.)**

> **Note (`substrate-native-check` CP3, verified):** the K4 4-port equal-admittance junction S = 0.5·𝟙 − I is **independent of z** (verified for z=1,2,10,100). So **node-level** saturation is a no-op on the K4; the **only** c_eff handle is the **bond-gradient** Γ. This is why a sharp step is required and why a smooth core cannot trap.

---

## §2 — SMOKE-2: does ADD-2 fire CONSERVATIVELY (energize-LOCK)? **PASS**

The converter is the K4-native rendering of the validated crystal-engine ADD-2: a **conservative velocity-space rotation**
(`crystal_engine.py:33-37`) lifted to a **port-space orthogonal rotation** of the post-scatter V_ref in the (monopole e0 ⊗
chiral-transverse e2) plane, by θ=κ̃·h·χ_sign·g_front, localized at the saturation front (CP10).

| quantity | value | the genesis-24 contrast | pass |
|---|---|---|---|
| centrosymmetric baseline (h=0): converter residual | **0.0 (EXACTLY)** | the parity-odd selection rule — exact identity | ✓ |
| asymmetric (h=1): per-node norm residual | **2.0e-12** | orthogonal rotation ⇒ energize-LOCK, no pump | ✓ |
| max\|V\| over the window | **1.82** | genesis-24 EMF pump detonated max\|V_inc\| → **1.08e4** (4 OOM) | ✓ |
| \|L\| max (bounded, oscillates) | **15.7** | genesis-24 pump \|L\| 2.7 → **43** (monotone) | ✓ |

The converter is **conservative by construction** — an orthogonal rotation conserves \|V_ref\|² per node EXACTLY, so **no
detonation is possible** (‖R‖=1, bounded). The centrosymmetric baseline is **exactly 0** (the parity-odd I4₁32 rule). **The
two genesis-24 failure modes — dead source AND non-conservative pump→detonation — are both structurally closed.** **(Figure 2.)**

**Honest caveat (flag-don't-fix), which connects to the §3 finding:** the bootstrap ratio (net bulk-monopole sourced from a
pure photon, converter ON / OFF) is **1.00** — the converter does **NOT** net-source the bulk. This is the **flip side of
energize-LOCK**: an exactly-orthogonal rotation **cannot accumulate a one-way transfer**. genesis-24 *did* bootstrap
(it pumped) — and detonated. **A conservative converter locks but does not build; a pumping converter builds but
detonates.** This is the same tension that names the §5 gap.

---

## §3 — SMOKE-3: does the real-space trap DRIVE the phase-space winding? **FAIL — they are DECOUPLED** (the load-bearing finding)

| quantity | value | reading |
|---|---|---|
| carrier winds at seed: w_tor (rel) | **1.98 (0.185)** | the (V_inc,V_ref) phase-space **IS** a real winding carrier (the scalar bulk carried w_tor=w_pol=**0**) |
| late winding, trap **ON** (reliable contour) | **0.00** | the winding has **decayed** |
| late winding, trap **OFF** | **0.00** | …**identically** without the trap |
| trap sustains winding? | **False** | the trap does **not** drive/sustain the phase-space winding |

**The decisive observation:** the toroidal winding **collapses to 0 within ~5 steps**, and the trap-ON and trap-OFF
trajectories **overlap exactly** (Figure 3). The real-space trap and the phase-space winding are **decoupled**.

**The mechanism (single, names all three findings):** the K4 scattering S = 0.5·𝟙 − I has the **monopole** e0=(1,1,1,1)/2 as
its **+1 eigenmode** (an isotropic, **standing**, trappable mode = the bulk **mass**, with **no winding**), and the
**transverse chiral** modes e1,e2,e3 as **−1 eigenmodes** (propagating = the **photon**, which **carries** the winding).
The **amplitude-wall is mode-blind** — it reflects on \|V_inc\| and binds the high-amplitude **monopole**; the winding-carrying
transverse modes are **not bound** by it and **radiate**. The conserved converter rotates monopole↔chiral locally at the
front but, being an **orthogonal rotation (energize-LOCK)**, **cannot lock a standing winding into the trapped core** (§2
caveat). **So the trapped real-space object (monopole breather = mass) and the phase-space winding (transverse modes =
charge/photon) live in DIFFERENT, decoupled modes.** Co-locating the chiral winding **inside** the saturated core at high
amplitude does **not** help — it still decays by ~step 40 (tested; the amplitude-wall does not bind a transverse vortex).

---

## §4 — The (2,3) diagnostic (confirms §3; matched controls) — does NOT close

Run as a **diagnostic confirmation** of the SMOKE-3 finding (NOT the earned full run): evolve 320 steps, measure both windings
on density-filled reliable contours (PML-excluded, CP7), with matched controls.

| config | w_tor (rel) | w_pol (rel) | closes (2,3)? |
|---|---|---|---|
| FULL (trap + converter + photon) | 0.0 (0.0) | 0.0 (0.205) | **no** |
| control: no photon | 0.0 (0.0) | 0.0 (0.263) | no (null) |
| control: no converter | 0.0 (0.0) | 0.0 (0.0) | no (null) |
| control: no trap | 0.0 (0.0) | 0.0 (0.182) | no (null) |

The poloidal contours are **populated and reliable** (rel 0.18–0.26) but carry **zero winding** — and the toroidal "2" that
was present at the seed has **radiated away**. Every control is null. **The (2,3) does not close** — confirming §3 by direct
measurement. (No α-leak-Q / Golden-Torus / joint-ledger was measured: with no sustained (2,3) there is no resonator, and the
frozen guard refuses a fluke Q — §0.)

---

## §5 — THE LOCALIZED GAP (named; one mechanism explains all failures — Rule 11)

The genesis-23 → 24 → crystal-engine → **K4-graft** arc, each gap closed and the residual pinned tighter:

| ingredient | genesis-24 | crystal engine (scalar bulk) | **K4 graft (this work)** |
|---|---|---|---|
| ω→V SOURCE energizes | live but pumps | LIVE + bootstraps (force) | live, conservative (rotation) |
| SOURCE STABILITY | **PUMP → detonates** (E_V→6.8e8) | energize-LOCK (force) | **energize-LOCK** (orthogonal, residual 2e-12) |
| the c_eff Γ-WALL | absent (dormant, Γ→0) | forms (scalar self-focus) | **forms on the K4** (Γ→1, needs a strain-snap STEP) |
| the WINDING CARRIER | toroidal "2" only | **absent** (scalar has no U(1)-fibre) | **PRESENT** (w_tor=1.98 at seed) ✅ |
| trap ⊗ winding COHERENCE | — | (no carrier to test) | **DECOUPLED** (trap binds monopole; winding radiates) |

**The residual gap, named:** a **single scalar-amplitude trap cannot host a real-space-trapped + phase-space-winding object**,
because (i) the fixed-roll connect forces c_eff(V) to enter only as a mode-blind **amplitude** reflection, which (ii) binds the
**+1 monopole** (the standing, non-winding **mass**) while the winding rides the **−1 transverse photon** modes that **radiate**,
and (iii) the only converter that locks them conservatively is an **orthogonal rotation that cannot net-transfer** the winding
into the trap (a pumping converter would, but detonates — genesis-24). **The missing ingredient is a SECOND, mode-selective
(chiral) confinement** that binds the transverse winding modes into a **standing vortex** — distinct from the amplitude wall
that binds the monopole. That chiral wall is precisely what the genesis-24/Cosserat **"Meissner S_μ→0"** coupling tried to be,
and it is the one that **detonates** when rendered as a bulk pump.

**This empirically answers the pressure-test's double-counting question:** you genuinely need **two** confinements (amplitude
for the mass + chiral for the winding); they are **not** the same object, and one engine with **one** scalar wall provably
cannot supply both. **Surfaced for Grant + auditor as a methodology finding (Rule 16), NOT auto-pivoted-to.**

---

## §6 — DERIVED / VERIFIED / BLOCKED ledger

| claim | status |
|---|---|
| c_eff(V) renders on the fixed-roll K4 as the Op14 bond-Γ reflection (not a re-timed connect) | **DERIVED** (HARD-PART resolution; z_local=(1−A²)^(−1/4)) |
| the Γ-wall bound state forms on the 4-port (sharp strain-snap front) | **VERIFIED** (SMOKE-1: retain 0.28 vs lin 5.6e-5, Γ→1, ratio ~5000×) |
| a SMOOTH seed does NOT trap (the fixed-roll-vs-absolute-c_eff finding) | **VERIFIED** (smooth retain 1.3e-5; node-S z-independent) |
| ADD-2 fires conservatively (energize-LOCK, no detonation, centrosym=0) | **VERIFIED** (SMOKE-2: residual 0/2e-12, max\|V\|=1.8, \|L\|=15.7) |
| the K4 (V_inc,V_ref) phase-space IS a winding carrier | **VERIFIED** (w_tor=1.98 at seed — the scalar bulk had 0) |
| the real-space trap DRIVES the phase-space winding | **BLOCKED** (SMOKE-3: decays trap-ON≈trap-OFF; decoupled modes) |
| the (2,3) closes (w_tor≈2 ∧ w_pol≈3, de-novo) | **BLOCKED** (winding radiates; both 0 on reliable contours) |
| α⁻¹, Golden-Torus, joint-ledger | **NOT RUN** (frozen guard: no sustained (2,3) ⇒ no resonator ⇒ refuse a fluke Q) |

**consistency-vs-emergence:** the VERIFIED items are engine-structure / manifestation-class. **No emergence-class quantity
was measured** — and per the guard, none was forced. **No emergence-class positive; no false Class-D.**

---

## §7 — Skills · figures · honest closure

**Skills:** `substrate-native-check` (CP1 wave-not-min; CP2 V-sector phase-space — the K4 IS the carrier the scalar bulk
lacked; CP3 the 4-port S is z-independent ⇒ bond-Γ is the only c_eff handle; CP4 winding in (V_inc,V_ref), not real-space;
CP6 reactance pair V_inc/Φ_link both read; CP7 PML-excluded density-filled contours; CP8 generative precursor = chiral photon
+ saturated bulk, NOT a planted (2,3); **CP8 structural-capability finding = the amplitude-wall binds the monopole but not the
winding modes**; CP10 wall as bond-Γ boundary + converter as bounded rotation). · `ave-conserved-vs-pumped` (the converter is
energize-LOCK by construction — orthogonal, residual 2e-12, centrosym EXACTLY 0; **and the conservative-vs-pump tension IS the
named gap** — a lock cannot build, a pump detonates). · `phase-space-coordinate-check` (A46 — the (2,3) measured in the native
(V_inc,V_ref) chiral phasor; the SMOKE-3 incoherence is precisely a real-space/phase-space coordinate finding). ·
`ave-prereg` / `verify-before-cite` (genesis-24 detonation E_V→6.8e8 / max\|V_inc\|→1.08e4 / \|L\| 2.7→43 from
`2026-06-09_crystal-engine_result.md:82-84,222`; Op14 z_local + np.roll connect from `k4_tlm.py:291-294,378-383`; κ̃=6/5,
V_yield, R_II from `constants.py` — all greped/opened this session). · `consistency-vs-emergence` (no emergence forced; SMOKE-FAIL
guard).

**Figures** (`src/scripts/vol_1_foundations/`, data-derived captions):
- [`k4graft_fig1_wall.png`](../src/scripts/vol_1_foundations/k4graft_fig1_wall.png) — SMOKE-1: sharp-front bound state retains 0.28 (smooth 1.3e-5, linear 5.6e-5); Γ_core→1.0, A=1.09 saturated, vs genesis-24 Γ→0.
- [`k4graft_fig2_converter.png`](../src/scripts/vol_1_foundations/k4graft_fig2_converter.png) — SMOKE-2: max\|V\|=1.8 O(1) (vs 1.08e4), \|L\|=15.7 bounded, residuals 0/2e-12 (orthogonal energize-LOCK).
- [`k4graft_fig3_phasespace_incoherence.png`](../src/scripts/vol_1_foundations/k4graft_fig3_phasespace_incoherence.png) — SMOKE-3 (load-bearing): w_tor=2.0 at seed → 0 by step 5, trap-ON ≡ trap-OFF; the trap binds the monopole, the winding radiates → DECOUPLED.

**Honest closure (Rule 11 / substitution-not-retraction).** The K4 graft is a **disciplined SMOKE-FAIL**, and the **most
informative negative in the arc**: it CLOSES the wall (the c_eff trap grafts onto the K4 with a strain-snap front) AND the
conservative source (energize-LOCK, residual 2e-12) AND it CONFIRMS the K4 is a genuine winding carrier (w_tor=1.98 — the
scalar bulk's exact missing piece). The residual obstruction is pinned to **one mechanism** explaining all failures: a single
scalar-amplitude wall binds the +1 monopole (mass) while the winding rides the −1 photon (radiates), and the only conservative
converter that could lock them is an orthogonal rotation that cannot net-transfer. **A real-space-trapped, phase-space-winding
object needs TWO confinements (amplitude + chiral); one scalar wall cannot supply both — the double-counting question answered
empirically.** No framework failure; no debug-toward-A; the α-emergence run was **refused by the frozen guard** (a false
Class-D is strictly worse than an honest negative). The chiral-confinement synthesis is **surfaced for Grant + auditor, not
auto-pivoted** (Rule 16).
