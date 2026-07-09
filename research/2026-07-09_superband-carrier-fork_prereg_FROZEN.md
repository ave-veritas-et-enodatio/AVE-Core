# SUPER-BAND CARRIER FORK — Pre-Registration (FROZEN)

**Date:** 2026-07-09
**Task:** #29 — "TEST it and RECORD BOTH branches" (Grant ruling). Fork-record engine
test of the super-band (ω ≫ ω₀) carrier question raised by the FPB-corner framing note.
**Branch:** `analysis/x29-superband-carrier-test` (off `main` @ post-#596)
**Status:** **PREREG ONLY — fork record + observables + adjudication criteria FROZEN before
the production driver.** A throwaway pilot (scratchpad, uncommitted) fixed numerical
parameters and the integrator; it did NOT set the adjudication criteria below, which are
physics-principled (power-law → A, exponential → B, evanescent-only → null).
**Skills applied:** `ave-prereg` (corpus-grep §1), `ave-loop-gap-harness-discipline`
(platform choice §2), `substrate-native-check` (§3), `phase-space-coordinate-check`
(A46, §3.4), `consistency-vs-emergence` (§7), `substrate-first-for-numbers`,
`verify-before-cite`, `pure-AVE-corpus`.
**pre-test-physics-check:** SATISFIED upstream — the ontology walk happened in-chat with
Grant, captured in `research/2026-07-09_highE-carrier-fpb-corner_walked-framing.md`
(origin/analysis/highE-carrier-fpb-framing). That note is FRAMING; **this run outranks it**
(flag-don't-fix: contradictions with the note are surfaced, not reconciled).

---

## 1. The question + corpus inventory (ave-prereg)

**THE QUESTION (from the FPB-corner framing note §3, §8):** what carries an
above-band-edge (ω ≫ ω₀) excitation on the lattice, and what is its coupling law to the
in-band smooth (ε-sector) channel? The framing note registers a two-branch fork whose
single discriminating exponent adjudicates the ATLAS γγ→γγ tension (Letter v5, PR #594):

| Branch | Carrier | ε-channel coupling law | ATLAS fate |
|---|---|---|---|
| **A — aliased-Bloch** | super-band wave, spatially aliased into the zone | **power-law** (ω₀/ω)^p | **BOUNDED** — the Letter's EFT scope stands; the closure hope dies (tension REAL) |
| **B — mobile discrete breather** | nonlinearity-localized rotor packet, freq above the linear band | **exponential** (breather tails ∝ e^−κ|n|) | **EVADES** — hard closure; v5 scope-statement upgrades to derived consistency |
| **null / third** | above-band drive reflects/evanesces, NO propagating carrier | — (nothing propagates) | the **smooth sector carries nothing above the edge** — that too is an answer |

**Prior art grepped (verify-before-cite, on this worktree @ post-#596):**

| Doc | What it fixes / leaves open |
|---|---|
| `research/2026-06-08_highE-winding-aliasing-prereg.md` | The *phase-space* winding-aliasing question (particle carrier ω=mc²/ℏ folds). A46-distinct from THIS test (§3.4). Establishes: aliasing STEP coherent, morphology consequence ungrounded. NOT the same object. |
| `research/2026-06-22_k4-bloch-dispersion-quartic_result.md` | The *k-space* directional anisotropy = (qℓ)⁴ cubic harmonic. ORTHOGONAL to THIS transport test (§3.3). Confirms: continuum photon carries no zone-edge (qℓ)² term (gate `wejkhvnfb`); ω_C=c/ℓ_node distinct from spatial zone-edge k=π/ℓ_node (ratio π). |
| `research/2026-06-16_k4-zone-edge-nyquist-settle_result.json` | The srs/diamond **acoustic band**: gapless, monotonic ω(k), band top with v_g→0 at the zone edge. srs tops at ω≈1.9105 rad/step (low-k phase-vel factor 1/√3); diamond keeps linear ω=ck up to ω=π. This is the linear substrate the drive sits above. |
| `_orchestration/2026-06-12_loop-gap-engine-dag.md` + `ave-loop-gap-harness-discipline` | Platform firewall: srs FROZEN at v17; genesis/loop-gap ranks on VacuumEngine3D. This test is NOT genesis work → §2. |
| `research/2026-05-18_prime-n-soliton-stability-{prereg,result}.md` | Prior soliton-stability work (topological loop-count). Not a driven-transport / breather-mobility test. |
| `src/ave/core/universal_operators.py:75` (`universal_saturation`) + `:771` (`universal_dynamic_impedance`, Op14) | The canonical kernel `S(A)=√(1−A²)` (Axiom 4, Born–Infeld n=2) and its ε-load form `Z_eff=Z_0/√S` ⇒ `C_eff=C·S` (the varactor stiffening). This IS the nonlinearity (§3.2). |

**Inventory verdict:** the transport / coupling-law question (this task) is a NEW, un-run
measurement. The two closest prior drivers (k4-bloch eigensolve; zone-edge settle) are
both **linear** and both measure the band, not what a drive ABOVE the band does. No prior
driver drives a boundary above ω_top and measures the in-band leakage exponent.

---

## 2. Platform choice (ave-loop-gap-harness-discipline)

This is **linear + weakly-nonlinear driven wave transport on the lattice**, NOT electron
genesis / nucleation / remanence. Per the harness discipline platform firewall:

- **NOT** the srs genesis engine (`chiral_lattice_v9..17` FROZEN) — no genesis platform is touched.
- **NOT** `VacuumEngine3D` + `loop_gap_harness.py` (that is the softening/loop-gap CLOSURE
  path for the electron resonator; this is a wave-propagation test, no rank ladder).
- **Platform:** a **new, minimal, self-contained driven-lattice wave driver** in the
  K4-TLM / master-equation lane — a 1D chain along a single K4 bond-line with the canonical
  saturable-varactor bond, integrated in continuous time. This is the same lightweight lane
  as `k4_zone_edge_nyquist_sweep.py` (dispersion driver, `src/scripts/vol_1_foundations/`),
  NOT the genesis harness. **One platform, this branch only** (no version treadmill — this
  is not a `chiral_lattice_v{N}` nor a `genesis_v{N}`).

**Anti-loophole check:** this is not a "fourth engine for the next hypothesis." It is a
standard driven-wave sim in the existing dispersion/transport lane, addressing a
falsification-scope question (ATLAS). No new firewalled object-class is claimed.

---

## 3. Substrate-native-check (walk BEFORE the driver)

### 3.1 K4 checkpoint — the lattice IS the physical lattice
Spatial discreteness is **physical**: node pitch ℓ_node = ℏ/(m_e c) (`constants.py:282`),
FIXED (native ℓ=1). The band structure is a real consequence of the bond coupling. The
**band edge is not a numerical knob** — it is the physical acoustic-band top ω_top set by
the bond stencil. The 1D reduction is transport along one K4 bond-line; the acoustic band
ω = 2|sin(kℓ/2)| (native, band top ω_top=2, gapless, v_g→0 at edge) reproduces the *shape*
of the settle-result srs/diamond acoustic branch (the absolute prefactor — 1/√3 network
factor, coordination — is calibrated out; only the shape and the transport physics carry).

### 3.2 Op2 / Op14 saturation checkpoint — the nonlinearity (boundary-condition, no bulk energy term)
The bond is a **saturable reactance** carrying the canonical kernel `S(A)=√(1−A²)`
(`universal_operators.py:75`, Axiom 4 / Born–Infeld n=2). The bond strain is
`r_n = V_{n+1} − V_n` (the ε-sector charge-length differential); yield at |r|=1.
Substrate-native constitutive law (conservative, from a potential — Ax3 lossless):

    U(r) = 1 − √(1 − r²)        (bond potential; Born–Infeld n=2)
    F(r) = U'(r) = r / √(1 − r²) = r / S(r)     (restoring force; STIFFENS to ∞ at yield)
    V̈_n = F(r_n) − F(r_{n−1})     (equation of motion)

This matches Op14 ε-load `Z_eff = Z_0/√S ⇒ C_eff = C·S` (`universal_operators.py:788-793`):
the varactor capacitance falls as strain rises ⇒ local stiffening ⇒ **HARD** nonlinearity
⇒ self-localized modes sit **ABOVE** the linear band (the above-band-breather class the
framing note §3(ii) names). Small-r limit F(r)≈r ⇒ gapless acoustic band (photon-native,
no k=0 gap). **The nonlinearity is a saturable boundary/reactance kernel, NOT a bulk energy
term** (no φ⁴ potential minted; the √(1−r²) is the Axiom-4 kernel).
**Above yield (|r|→1) = topological reorganization = pair production** (framing note §5) —
that is a DIFFERENT regime (rupture, irreversible), explicitly **out of reversible-carrier
scope**; runs that touch yield are flagged RUPTURED and excluded from the carrier verdict.

### 3.3 Anisotropy is NOT what this test measures (flag)
The (qℓ)⁴ cubic-harmonic anisotropy (`k4-bloch-dispersion-quartic`) is a 3D/directional
k-space invariant. THIS test is 1D transport along a propagation line and does **not** probe
anisotropy. Do not read a coupling-law result as anisotropy content, or vice-versa.

### 3.4 Phase-space vs real-space (A46, phase-space-coordinate-check)
The framing note's *identity* `phase advance/node = kℓ_node = ω/ω₀` equates the temporal
drive ω with a spatial k for a luminal carrier. This test drives a **temporal** ω_drive at a
real-space boundary and measures **real-space energy transport** + the temporal spectrum of
what propagates. Both the drive (temporal ω) and the read (real-space flux + its ω-content)
are in the SAME coordinate frame → A46-clean. This is DISTINCT from the phase-space
winding-aliasing prereg (2026-06-08), which lives on the internal-winding Clifford-torus
`(V_inc, V_ref)` axis. We do NOT compare a real-space measurement to a phase-space φ²
prediction (A46-disqualified pattern avoided).

### 3.5 Numerical-vs-physical aliasing separation (the subtlest point — head-on)
On a discrete engine an above-Nyquist drive can alias in TWO ways; they must be separated:
- **Physical (spatial-lattice) aliasing/evanescence** — the lattice node spacing ℓ_node is
  fixed and physical (it IS the AVE substrate). A drive at ω_drive > ω_top has **no linear
  propagating mode** → the linear response is spatially **evanescent** (V_n ∝ (−1)^n e^−κn,
  cosh κ = ω²/2 − 1 from continuing k→π+iκ). This is **PHYSICAL** AVE lattice behavior.
- **Numerical (temporal-integration) artifact** — from finite dt. **Avoided by construction:**
  the equation of motion is a continuous-time ODE; dt is an accuracy knob NOT tied to the
  spatial lattice (dt chosen to resolve ω_drive with ≥ N_sub sub-steps per drive period).
  **VERIFIED empirically** by a dt-halving convergence check (§5, gate G5): any "carrier"
  that appears at coarse dt but vanishes at dt/2 is a numerical artifact and is discarded.
- Energy conservation (symplectic velocity-Verlet on the Hamiltonian H = Σ½p² + ΣU(r)) is
  monitored every run; |ΔH|/H over the recording window must be < 1% for a run to be VALID
  (a "self-localized" state in a non-conserving run is a suspected numerical instability).

---

## 4. Observables (FROZEN)

Native units throughout (ℓ_node=1, c=1, ω_C=c/ℓ_node=1; band top ω_top measured, ≈2).
Drive: left boundary node V_0(t) = A_drive · w(t) · sin(ω_drive t), w = smooth ramp
(≥10 drive periods) to keep the injected spectrum narrow at ω_drive (a hard turn-on injects
broadband incl. in-band and would fake a coupling). Right boundary: matched absorbing sponge
(the far Z_0 vacuum load); sponge cells EXCLUDED from all physics reads (Rule-10 PML-exclusion).

**O1 — Band validation (validate-on-known).** Measure ω_top and the low-k phase velocity of
the linear chain; confirm gapless acoustic band, v_g→0 at edge. Report ω_drive/ω_top AND
ω_drive/ω_C for every drive.

**O2 — Energy transport.** Energy in the far interior region [n_cut, n_sponge) vs time. Does a
localized propagating packet form? Track the energy centroid (COM) of the interior field →
**propagation speed** v (vs c=1). Report packet **width** (nodes above half-peak).

**O3 — Coupling law to in-band modes (THE discriminator).** Only in-band components
(ω < ω_top) propagate to the far region; above-band components are evanescent/pinned near the
drive. The far-region energy accumulation rate = the **in-band radiated power** P_leak.
Transmitted fraction T(ω_drive) = P_leak / P_inject, measured at fixed kernel-engaged amplitude,
swept over the above-band ω_drive set. **Fit T(ω_drive) to BOTH:**
- power-law: log T = log C − p·log(ω/ω_C)  → slope p (Branch A)
- exponential: log T = log C − γ·(ω/ω_C)   → rate γ (Branch B)
Report both fits, both R². Also sweep amplitude at fixed ω_drive → down-conversion order q
(log T vs log A_drive slope) to characterize the leakage mechanism.

**O4 — PN-barrier / mobility probe.** If a self-localized breather forms, apply a momentum
kick (phase-gradient) and measure whether it hops (COM moves at constant v) or stays PN-pinned
(COM fixed, kick radiated). Also measure the translational-mode barrier via the energy
difference between a site-centered and a bond-centered breather (the Peierls–Nabarro barrier).
**A PN-barrier-free luminal packet (v≈c, constant) is the branch-B hard-closure signature; a
pinned breather transports no energy → contributes to the null.**

**O5 — Amplitude axis (THE A-vs-B/null discriminator).** For each above-band ω_drive, sweep
A_drive from linear (bond-strain r≪1) to kernel-engaged (r up to ~0.8, sub-yield). The
signatures:
- **Evanescent-only at ALL amplitudes** → **null** (smooth sector carries nothing above edge).
- **Mobile localized packet appearing only above a kernel threshold, exponential in-band coupling**
  → **Branch B** (breather).
- **Power-law in-band coupling growing smoothly with amplitude, no mobile localized carrier**
  → **Branch A** (aliased-Bloch residual).

---

## 5. Adjudication criteria (FROZEN — committed before the production run)

Gates evaluated against the frozen observables. No post-hoc criterion drops (Rule 11).

| Gate | Pass condition | Reads |
|---|---|---|
| **G1 — band validated** | gapless acoustic band; ω_top measured; v_g→0 at edge; low-k v=c | O1 |
| **G2 — linear evanescence physical** | at small amplitude, above-band drive gives V_n∝(−1)^n e^−κn with measured κ matching analytic cosh κ = ω²/2−1 (within ~15%, near-field-corrected); far-region flux ≈ 0 | O2, O3 |
| **G3 — coupling-law fit** | T(ω_drive) over the above-band set fits power-law OR exponential with clearly better R² (Δ(1−R²) resolves it) | O3 |
| **G4 — mobility** | breather (if any) either hops at v≈c constant (mobile) or stays PN-pinned (immobile) — reported either way | O4 |
| **G5 — dt-convergence (numerical-vs-physical)** | the coupling-law exponent and packet speed change < 5% under dt→dt/2 for a representative above-band case; energy |ΔH|/H < 1% on all VALID runs | §3.5 |

**Branch verdict decision rule (FROZEN):**
- **Branch A (aliased-Bloch, tension REAL)** iff: G3 = power-law wins AND G4 = no mobile
  luminal carrier (breather pinned or absent). In-band leakage ∝ (ω₀/ω)^p, p finite.
- **Branch B (breather, EVADES)** iff: G4 = a mobile luminal (v≈c) self-localized packet forms
  above a kernel threshold AND G3 = its in-band coupling is exponentially suppressed
  (exponential wins, and coupling ↓ as the packet localizes tighter).
- **NULL (smooth sector carries nothing above edge)** iff: G2 holds AND no propagating carrier
  forms at any sub-yield amplitude (far-region flux stays ≈0 or only a PN-pinned non-transporting
  breather forms). This is a legitimate third answer, recorded as such.
- **INDETERMINATE** iff: G5 fails (numerical artifact suspected) or G3 cannot separate the fits.

---

## 6. Frozen drive set

ω_drive/ω_C ∈ {0.5, 1.5} (in-band controls) ∪ {2.1, 2.5, 3, 4, 5, 6} (above the band top ω_top≈2).
**FLAG (flag-don't-fix, surfaced now, decided by the run):** the framing note calls ω_C
("ω₀") "the band edge," but the lattice's linear acoustic band extends to ω_top ≈ 2·ω_C.
So the task's {1.5·ω_C} point is IN-BAND (propagating), not above-edge; the genuine
above-edge tests are {3, 4, 5, 6}·ω_C (plus near-edge {2.1, 2.5}). The run measures against
the TRUE band top ω_top, and reports both ratios. The framing note is FRAMING; the run outranks.

Amplitude axis: A_drive ∈ {0.02 (linear), 0.1, 0.2, 0.3} (kernel-engaged, sub-yield for the
staggered near-boundary field). Yield-touch → run flagged RUPTURED, excluded from verdict.

---

## 7. consistency-vs-emergence classification (FROZEN)

| Sub-claim | Class | Rationale |
|---|---|---|
| ω_C = c/ℓ_node band scale | **IDENTITY** | ℓ_node := ℏ/(m_e c) forces it (`constants.py:282`). Not evidence. |
| Acoustic band + above-band evanescence | **MANIFESTATION (Class B)** | Generic lattice consequence of Axiom-1 discreteness + the bond stencil; substrate-native re-statement of a standard discrete-lattice fact. |
| Saturable-varactor breather existence/threshold | **MANIFESTATION** | Consequence of the Axiom-4 kernel on the bond; discrete-breather physics is standard nonlinear-lattice, here substrate-grounded. |
| The A-vs-B coupling exponent → ATLAS verdict | **CONSISTENCY-CLASS input** | Feeds whether the QED-peer EFT-scope statement holds; not a QED-beating novel prediction. The whole test is a *scope-closure consistency check*, NOT an emergence claim. |

Headline: this is a **CONSISTENCY-class scope-closure test**. Whatever branch lands, it must
NOT be headlined as an AVE-distinct emergence result.

---

## 8. Out of scope
- Above-yield rupture / pair-production (AC→DC rectification) dynamics — separate regime.
- The μ-slew kernel S_B=√(1−A_I²) as a SECOND independent nonlinearity — the ε-varactor is the
  primary hard nonlinearity here; the μ-slew axis is a KEEP-BOTH follow-on if the ε result is
  indeterminate (noted, not run).
- 3D directional anisotropy / (qℓ)⁴ (owned by k4-bloch-dispersion).
- The full FWM matrix element / phase-matching integral (framing note §8.3) — theory, not this driver.

---

**PREREG STATUS: FROZEN — 2026-07-09.** Driver + result are separate commits. The branch
verdict is whatever the frozen gates return; both branches recorded regardless.
