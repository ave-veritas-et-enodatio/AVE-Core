# Phase-A feasibility — channel-selective vacuum-impedance probe (RESULT)

**Date:** 2026-06-23 · **Lane:** vacuum-impedance-probe feasibility arc (orchestration) · **Status:** scratch result, NOT canonized.
**Posture:** refute-by-default, feasibility-gated. **Method:** 9-agent workflow (3 ground · 3 derive · 3 refute), all read-only / derive-and-return; no corpus mutation.
**Provenance caveat:** grounded on local `main` (HEAD `05361256`), which was **10 commits behind `origin/main`** at run time. Cited leaves were last touched well below HEAD and are unaffected, but every file:line below should be **re-verified against `origin/main`** before being lifted into canon.

> **Read alongside** `_orchestration/2026-06-23_vacuum-impedance-probe-primitive-handoff.md` (the Cleave-01 red-teamed primitive brief) and the superseded `_orchestration/2026-06-22_vacuum-impedance-probe-handoff.md`. This result is **downstream of and consistent with** the primitive brief's reframe.

---

## 1. Verdict

**INFEASIBLE** — a channel-selective vacuum-impedance probe (an instrument that couples selectively to `Z_shear` or `Z_bulk` while rejecting `Z_EM`) is **not buildable as a distinct near-term bench instrument**, for **both** mechanical channels.

Confirmed by 3 independent derivation agents (all `hard_gate = INFEASIBLE`) and 3 independent adversarial refute lenses (all `over_rescue_flag = False`, i.e. the negative is neither over-rescued **nor** over-pessimistic). The honest prior — channel-selective vacuum coupling at the bench is HARD — is **confirmed by derivation, not asserted**.

This is **gated-not-dead, not closed-negative**: two of the three blocking gaps are engine/ratification TODOs (the coupling magnitude and the transducer pole), and one is a missing target. None is a proven impossibility theorem. But all three are simultaneously unmet today, and the instrument concept itself partly dissolves (§4).

---

## 2. The core physics — one deflationary symmetry

The probe decomposes into the corpus's **two coupling problems** (`device-circuit-models.md:205-210`): an EM(Ω)↔mechanical(ρc) **domain crossing**, then an inter-grade coupling. The load-bearing finding:

> **The same grade/Helmholtz orthogonality that gives clean structural EM-rejection ALSO gates the coupling-in.** You cannot have clean rejection **and** easy coupling from one electrical port — they are two faces of one orthogonality.

EM-rejection is structural in the static/sub-yield regime via three stacked orthogonalities: keyed-argument duality (ε keys on V, μ on circulating I — `graded-network-response.md:255-264`, the **derived** decoupling), grade-orthogonality A1⊥T2 (`master-equation.md:20`), and Helmholtz longitudinal⊥transverse for bulk. (Reason #3, "zero `χ_me` grep hits in src/ave", is **absence-of-evidence, not a derived selection rule** — do not cite it as load-bearing; lead with keyed-argument duality.)

**Per channel:**

- **Shear (`Z_shear`, Cosserat micro-rotation, charge-"3").** The K4(EM)→Cosserat(ω) parametric bridge `W_refl ∝ V²·f(ω)` is **even in ω**, so `∂_ω W|_{ω=0} = 0` — **ω = 0 is an exact fixed point** (`translation-circuit.md:192,239`; code-confirmed `cross_sector_coupling.py:83-90`, the only shear-sourcing terms `f_w ∝ ∂(g·V)` are gated by `g_front`, a Gaussian shell at the yield boundary `R_II`, ≈0 at a cold bench). **A linear electrical drive cannot seed micro-rotation from zero**; it can only parametrically pump an already-seeded Γ→−1 rupture (pair-production regime). No sub-yield linear electrical→shear channel exists in the verified corpus.

- **Bulk (`Z_bulk`, A1 dilatation, mass-"3"/V-sector).** Strictly harder than shear. `Γ_bulk→−1` is a **SHORT** (`Z_bulk→0`, pressure-release `p=0` wall; `node-2domain-nport.md:81`): under Axiom-3 lossless-reactive cycling, a perfect reactive reflector returns all energy — you can present energy at it but deposit none. **And bulk has no derived bench amplitude at all** (the bulk leaf is `no-claim`/structural).

---

## 3. The transduction crux is a PHANTOM

Coupling-efficiency factors as **stage-T × stage-C**:

- **Stage-T** (the EM↔mechanical domain crossing) = the ξ_topo **TKI-transformer** (`def-tk1xfm`). It is the **only** corpus bridge, and it is `status:proposed`, **not canonical**, gain-1, pole-less, lossless, ceiling **"identity-by-translation, NOT a derivation / NOT a pole"** (`vocabulary-register.md:327,333,340`; `translation-circuit.md:660` piezo over-claim guard). It transduces **units** losslessly (efficiency = 1 by construction) but supplies **no coupling pole and no transduction ratio**. The ξ_topo dictionary (`translation-circuit.md:17-26`) covers translational x/v/F + L/C/R only — there is **no invertible row for the rotational/torque (Ω_w) grade**; the couple-stress→mutual-inductance map (`:100-104`) is a structural correspondence, not a units-checked invertible row.
- **Stage-C** (the inter-grade coupling magnitude) = `χ = 0.30` in `cvr_model.py:230,240-246`, an explicit **"STRUCTURAL placeholder ... not a derived magnitude"** (cubic FDTD averages chirality out — AUDITOR_STATE FLAG-4). `κ̃ = 6/5` is FORM-derived/α-free (`cross_sector_coupling.py:22-23`) and the non-reciprocity **sign** is lattice-sourced (I4₁32), but the **magnitude is IMPOSED** (`research/2026-06-20_node-circulator-coupling.md:146-156`, verdict IMPOSED-AT-MAGNITUDE/ECHO; this PR **is merged to `main`** — see §7).

**efficiency = (stage-T = 1, a lossless gauge change) × (stage-C = undefined/imposed) = PHANTOM.** The seductive over-rescue — "the transformer gives gain-1, so coupling is efficient" — conflates a lossless unit-change with a coupling pole, and is explicitly **refused**. The ~12–13-OOM-plus-unit-class `|Z_mech|/Z_EM` mismatch is **transformer-matchable and is NOT the figure of merit** — the verdict does not rest on it.

Blocked on (not substitutable): (i) `def-tk1xfm` ratification AND (ii) a chiral-crystal engine that does not average chirality out. Ratifying the transducer alone does **not** lift the phantom — by its own ceiling it supplies no pole.

---

## 4. Phase-B gate fails independently — the probe dissolves into existing instruments

Even granting coupling, the Phase-B target gate is unmet: **no bankable DERIVED lab-bench amplitude exists in either mechanical channel.**

- **Shear:** the only derived observable is **astrophysical** — BH ringdown eigenvalue (18/49), GW echoes at `r_sat` — read by a **standard LIGO-class detector**, not a channel-selective vacuum transducer (`gw-impedance-perturbation.md:18`: GW is a transverse shear wave perturbing `Z_shear`). The shear channel is **already natively instrumented**.
- **Bulk:** `no-claim`/structural; no lab amplitude, no astrophysical fallback.
- All three **bankable** forward predictions (birefringence coefficient, optical activity ±75.46°/unit, `(q·ℓ_node)⁴` dispersion) are **EM/photon-channel** — standard optical metrology, out of scope.

The corpus already names the problem: **"S₁₁ at Z₀ measures the EM channel only; horizons and electron walls require channel tagging or multi-channel characterization"** (`device-circuit-models.md:99`). Any electrically-recordable readout runs the ξ-dictionary in reverse and lands back on `Z_EM = Z_0`, **re-importing the EM domain at the readout** and collapsing the structural rejection. A truly EM-free mechanical-in/mechanical-out instrument is conceivable but is then **two transducers back-to-back**, not a single-domain "impedance probe" — and the EM channel re-enters wherever it touches lab electronics.

---

## 5. Symmetric-standard refinements — do NOT overclaim the negative

Guarding the SM/QED-prior over-pessimism direction (the refute phase's job):

1. **EM-rejection is NOT an AVE comedown.** EM-contamination rejection is the **universal** transducer-engineering problem — LIGO, piezo, magnetostrictive benches all face it and get a pass. AVE's static grade-orthogonality is, if anything, a *milder* version. Framing rejection as an AVE weakness would be the consensus-bias error.
2. **The Axiom-3 readback is NOT a hard showstopper.** Lossless-reactive forbids **calorimetric** (read-by-absorption) readout, **not** reactive-perturbation readout — the corpus's own minimize-`Re(Z)/Z_0` frequency-pull primitive *is* a coherent reactive readback. (Correction to an earlier over-pessimistic framing.) The readback problem is the EM re-entry of §4, not "lossless ⇒ unreadable."
3. **The coupling magnitude is an engine-TODO, not closed-negative.** The chirality-averaging is a property of the **cubic FDTD discretization**, not the substrate — `STATED-pending-engine`, correctly labeled GATED, not permanently dead.

The genuine AVE-vs-SM asymmetry is **not** any of the above — it is (a) the coupling-IN magnitude is IMPOSED/phantom and (b) there is no derived bench-scale shear/bulk amplitude. That gap SM does not share (SM transducers carry calibrated couplings). **Object-level knife stays sharp: INFEASIBLE is correct.**

---

## 6. What survives — the residual physics gap

The shear channel is covered (LIGO-class). The **bulk / V-sector longitudinal-scalar channel is the genuinely uninstrumented one**: transverse differential-arm detectors are structurally blind to the common-mode breathing mode (`L_x − L_y ≈ 0`), and the corpus has neither a derived bench amplitude nor an existing native instrument for it. That gap is **real but it is a future-physics gap, not a near-term instrument**: building a bulk/V-sector probe is blocked on *both* a derived target amplitude (Phase B) *and* a derived coupling magnitude (the chiral-crystal engine) — neither exists today.

The load-bearing OPEN next move for the broader program is unchanged and untouched by this arc: derive the electron `Q` from channel impedances + the inter-grade `H_couple` via the Fork-A isolation-vs-coupling discriminator (`electron-bound-resonator-coverage.md:100-109`). That is engine work, not instrument design.

---

## 7. Corpus-hygiene defects surfaced (flag-don't-fix)

1. **Stale PR-status in a canonical leaf.** `device-circuit-models.md:203` labels **PR #321, #319, #320 as "PR-pending, not yet on main"** — but git confirms all three merged: `26e61ec0` (#321), `535947db` (#320), `422b81d3` (#319) are ancestors of `main`. Rule-12 correctable (mark merged; preserve history). Spawned as a separate task.
2. **Channel mis-assignment in the primitive brief's fleet table.** `2026-06-23_…-primitive-handoff.md` §4 files **"GW-echo" under the bulk longitudinal `Z_bulk` channel**, but the corpus consistently assigns **GW to the SHEAR channel** (`three-channel-impedances.md:21` "Shear / GW"; `gw-impedance-perturbation.md:18` "transverse shear wave"). Load-bearing for that brief's "bulk is already natively probed" dissolution claim — the bulk/V-sector is in fact the *un*-instrumented channel (§6). Flag to the primitive session before its fleet table is canonized.

---

## 8. Forks for Grant (downstream — do not block on these)

- **Bulk READ siting** (from primitive brief §5): does a non-invasive bulk READ sit at the native SHORT (`Z_bulk→0`, pressure node) or at a rigid high-Z coupler, given `Γ_flow = −Γ_pressure` flips which field nulls? (`field-symbol-registry.md:160`.)
- **Bulk/V-sector instrumentation** (this arc): is the longitudinal-scalar channel's lack of a native detector worth a forward instrument program once a target amplitude is derived — or does it stay parked until the chiral-crystal engine + a bankable bulk prediction both land?

---

## 9. Provenance anchors (re-verify against `origin/main`)

`three-channel-impedances.md:18-24` · `device-circuit-models.md:99,139,205-210` · `graded-network-response.md:255-272,291-294` · `master-equation.md:20` · `translation-circuit.md:17-26,100-104,192,239,660` · `vocabulary-register.md:327,333,340` (def-tk1xfm) · `cross_sector_coupling.py:22-23,76,83-90` · `cvr_model.py:161,230,240-246` · `research/2026-06-20_node-circulator-coupling.md:11-20,143-156` · `gw-impedance-perturbation.md:18` · `bulk-impedance-at-saturation-boundary.md` (no-claim) · `electron-bound-resonator-coverage.md:100-109,159,161` · `constants.py:291(ξ_topo),383-393(EE↔topo dict),664(RHO_BULK),674-676(V_LONG=√2·c₀)`.
