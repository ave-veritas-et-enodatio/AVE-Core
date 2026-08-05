# The regulated-return instrument, v2 — **CERTIFICATION RERUN** with two repaired freeze-time constants, **plus Y8: the REACH-THROUGH computation** in the semiconductor register (**SVA pilot case 3**)

**Date:** 2026-08-05
**Class:** DERIVATION pre-registration (research-doc; **mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger — regardless of outcome**). Committed **ALONE** and pushed **before any driver code and before any number produced by this instrument exists**.
**Supersedes (versioned, Rule-11-clean):** `research/2026-08-04_echo-delay-regulated-sum_prereg-FROZEN.md` (v1, commit `1da06a90`, merged). **v1's `DELAY-NOT-CERTIFIED` verdict on `CFG-B` STANDS as a historical fact and is NOT converted to a pass by this document.** v2 is a NEW instrument with a NEW version number, exactly as v1's own §7.0 `BIN-CERT-FAIL` disposition routes it (*"routes to a successor with a new version number"*).
**Result-doc pointer requirement.** The result doc MUST carry `Prereg-file: research/2026-08-05_echo-delay-v2-reach-through_prereg-FROZEN.md` near its top, and every criterion it labels `Frozen:` MUST byte-match a quoted string in THIS file.
**Provenance:** Grant's GO of 2026-08-05. Two deliverables in one lane: **(PART 1)** the certification rerun of the regulated-sum instrument with `G-DISC`'s LAW repaired and `G-DECADE`'s TOLERANCE resized — and no other threshold touched; **(PART 2)** **Y8**, the reach-through computation, which v1 fenced out by name (v1 §1.3 Y8: *"does NOT compute a reflectivity, a tunnelling amplitude, or an evanescent-decay length through the cutoff region"*).
**Written against** `origin/main` = `773fe007`.
**Register ruling, binding on this document.** Y8 is written in the **SEMICONDUCTOR** register: *depletion edge*, *depletion width*, *junction two-port*, *reach-through*. The words **"tunnelling"** and bare **"skin"** are **not used** anywhere in this lane. The three mandatory carves are declared in §0.4 and are load-bearing, not decorative.
**SVA pilot:** this is **pilot case 3** of the Standard Vacuum Analysis (`manuscript/ave-kb/common/standard-vacuum-analysis.md`, PILOT v0.1). Its §0 header is filled below, verbatim rows. **This lane voluntarily adopts pilot-2's two pieces of returned feedback** — a **NUMERICAL CONDITIONING** declaration (§0, row 11) and the **`BRACKETED(pending-ruling)`** provenance tag (§0, row 5) — as an experiment in whether the proposed amendments earn their keep. **Adopting them here is NOT a canonization decision and pre-empts nothing: the ruling is Grant's.**

---

## §P — WHAT THIS LANE IS, IN ONE PARAGRAPH, AND WHAT IT IS NOT

v1 built a lattice-regulated optical-return-delay instrument, certified its RHO-A half against the 2026-06-17 predecessor driver at `7.13e-13`, adjudicated `BIN-DA-CLOSED`, and then **failed its own RHO-B half on two gate constants it had derived wrongly at freeze** — `G-DISC` (a dropped factor of two in the pass attribution) and `G-DECADE` (a tolerance sized for the asymptotic law and applied where the derived `O(S²)` correction exceeds it). **PART 1 of this lane re-freezes those two gates from re-derived law — the law for `G-DISC`, the tolerance for `G-DECADE` — changes nothing else, and re-runs.** Its negative controls are the v1 numbers themselves: **CFG-A must reproduce exactly, and CFG-B's diagnostic numbers must be unchanged, because the gates were wrong and the numbers were not.** **PART 2 answers the question v1 fenced out (Y8) and Grant's §0.2 plumber question turned on: given that the wave reaches the last intact cell, does the composite reflection seen from outside belong to the far contact or to the depletion edge?**

**It is NOT** an adjudication of FORK-3(b), **NOT** a re-run or re-score of the axial RHO-B eigenvalue lane, **NOT** an adjudication of FLAG-W or FLAG-CAUSAL, **NOT** a claim that echoes are or are not observed, **NOT** an echo-amplitude or echo-train claim, and **NOT** a repair of any KB or manuscript leaf.

### §P.1 Predecessor state, in order — and the fence that makes "byte-untouched" checkable

| lane | artifact | state | role here |
|---|---|---|---|
| **v1 regulated sum** (MERGED, PR #880) | `research/2026-08-04_echo-delay-regulated-sum_prereg-FROZEN.md`, `..._result.md`, `research/drivers/echo_delay_regulated_sum{.py,_number_check.py,_results.json}` | CFG-A `DELAY-CERTIFIED` + `BIN-DA-CLOSED`; CFG-B `DELAY-NOT-CERTIFIED` | **The instrument being re-certified.** Its shipped JSON is read **PROGRAMMATICALLY, READ-ONLY** as the NEGATIVE-CONTROL target of `G-NC-V1A` / `G-NC-V1B`. Its bin definitions are carried forward **byte-identical**. |
| **2026-06-17 BH shear-echo forward prereg** (MERGED, FROZEN, SHA-pinned `04bcb4ac`) | `research/2026-06-17_bh-shear-echo-forward-prereg.md`, `src/scripts/vol_3_macroscopic/bh_shear_echo_delay.py` | the RHO-A predecessor | `G-NC` target, unchanged from v1, consumed READ-ONLY. |
| **v2.4 axial cold-Q** (MERGED) | `research/drivers/coldq_pole_v2p4_root_results.json` | `ROOT-CERTIFIED` under RHO-A | Supplies the ringdown frequency scale AND — **new in v2** — the **FROZEN BAND** of §2Y.2, read PROGRAMMATICALLY. |
| **axial RHO-B** (MERGED, PR #876) | `research/2026-08-04_coldq-axial-rhob_prereg-FROZEN.md`, `..._result.md` | `ROOT-NOT-CERTIFIED`; **wall analysis CERTIFIED** | Supplies the **pointer** to the Frobenius wall row. **This lane RE-DERIVES that row from its own Schrödinger-form potential and does NOT import it** (§2Y.4). |

**Predecessor fence, frozen.** `every predecessor file named in section P.1 is BYTE-UNTOUCHED by this lane and the claim is discharged by an empty git diff --stat against the freeze base on each of them; research/drivers/echo_delay_regulated_sum_results.json, research/drivers/coldq_pole_v2p4_root_results.json and src/scripts/vol_3_macroscopic/bh_shear_echo_delay.py are consumed READ-ONLY and are neither edited nor re-scored, and in particular v1's DELAY-NOT-CERTIFIED verdict is neither edited nor withdrawn`.

**Scope fence, frozen.** `this lane writes under research/ and _orchestration/docket-entries/ ONLY, plus exactly one appended Makefile target; it edits no manuscript or KB file, proposes no claim-quality repair, touches no FLAG-W or sign-relativity leaf, adjudicates no fork, and leaves src/ave byte-untouched`.

---

## §0 — Standard Vacuum Analysis header (SVA v0.1-pilot, **+ two pilot-2 amendments adopted voluntarily**)

 1. SECTOR / OWNERSHIP:      The propagating observable is a **transverse shear (T2)** disturbance; the DC grading that slows it is the **A1 radial dilatation** `ε₁₁(r) = 7GM/(c²r)`. A1 owns the bias profile, T2 owns the wave. **Cross-wiring check: the delay and the reflection are BOTH T2 quantities on an A1-set profile — no bulk (A1) wave speed, no Cosserat microrotation, and no EM channel enters any number in this lane.** ★ **Y8-specific cross-wiring check, and it is the one the semiconductor register invites:** the depleted quantity is **T2 signal-band support**, NOT charge, NOT an A1 dilatation reservoir, and NOT a Cosserat winding. **Nothing is depleted of anything; a frequency band loses local support.** The far contact's condition is a **T2 traction/velocity** row, not a charge boundary condition.
 2. REGIME / PHASE-STATE:    **MODE** = small-signal AC transit-time **and small-signal AC reflection** on a static DC bias. **REGIME** = sub-yield lossless-reactive for `r > r_sat`; `r < r_sat` is Regime IV and is **not in the domain**. **PHASE-STATE** = cold lattice with Op14 ON as a static constitutive grade, `A(r) = r_sat/r`, `A = 1` exactly at `r_sat`. **DC bias point** = the gravitational grading itself; the ringdown amplitude does not move it, so small-signal is exact. ★ **Y8 adds one regime statement v1 did not need:** the drive is a **REAL** frequency (a scattering problem), not a complex eigenvalue (a mode problem). Every statement below about branch exponents is a statement about the **real-frequency** problem and bears on no eigenvalue lane.
 3. CIRCUIT STATEMENT:       Before any framework word: **a lossless LC/TLM ladder whose per-section delay `√(L_nC_n)` grows without bound toward one end, cut at the last physical section, terminated by an unresolved contact.** v1 measured its **two-way group delay** (a TOTAL observable, the round-trip phase slope). v2 measures, in addition, **the input reflection coefficient `Γ_in` of that same ladder at a declared plane** — also a TOTAL observable (`Γ` at a plane), never a per-section slot. **`|Γ_in|` and `dφ_Γ/dω` are the two terminal quantities; the per-cell `ABCD` is the machinery, not the observable.**
 4. PLANE & PROJECTION:      **PLANE-∞ (PRIMARY for the DELAY):** the excess over cold-lattice flight, `ΔT = 2∫(1/v − 1/c₀)dr`, `r_out → ∞` — convergent (`O(1/r²)`, no `1/r` term) hence plane-INVARIANT. **PLANE-PEAK (SECONDARY for the DELAY):** the derived maximum of `𝒱(r) = v(r)²U(r)`, ω-independent. ★ **PLANE-JX (PRIMARY for `Γ_in`):** the **outer face of the outermost depleted cell** — the plane the reach-through question is asked at. ★ **PLANE-NW (SECONDARY for `Γ_in`):** the outer face of cell `K` of the frozen near-wall window. **Every `Γ` in this lane is referenced to the LOCAL characteristic impedance at its own plane, and the analogy convention is declared in §2Y.5 rather than assumed** (`Z_shear = √(μρ)` = traction/velocity ⇒ force↔voltage, velocity↔current). **`Γ_in` is reported as a complex number with its plane and its reference impedance named at every site.**
 5. CONSTITUTIVE PROVENANCE: `S(A)=(1−A²)^{1/2}` **DERIVED** (Ax 4). `A(r)=r_sat/r` **DERIVED-FORM / VALUE-IMPORTED** (the `7` rides GR-imported `ν_vac = 2/7`). `μ = G_vac S` **DERIVED**. `Z = ρv = ρ_bulk c₀ S^{1−p}` **DERIVED** here from `μ`, `v` and `p` in one line (§2Y.5). `ρ = ρ_bulk` (RHO-A) vs `ρ_eff = ρ_bulk/S³` (RHO-B) **FORKED (FORK-3(b), OPEN)**. `ℓ_node = ħ/(m_e c)` **IMPORTED-VALUE / DEFINITIONAL**. Band top `β` **BRACKETED(pending-ruling)** — ★ *the pilot-2 proposed fifth provenance tag, adopted here on its proposer's own case: `β ∈ {5.4414, 17.0111} ω_C` is neither DERIVED nor IMPORTED nor FORKED-with-an-id nor ENG-CHOICE, it is a two-valued bracket awaiting a single-scale-vs-stiffness-lifted ruling, and it is swept at both ends.* The far-contact condition `Γ_L ∈ {−1, 0, +1}` is **FORKED (FLAG-CAUSAL, OPEN, Grant's)** and is swept at all three values. `ℓ = 2` **INPUT**. The per-cell electrical-length reading (`E1` vs `E2`) is **ENG-CHOICE, swept**.
 6. ENERGY LEDGER:           **No port is crossed anywhere in this lane and no loss word is used.** `Re{Z} = 0` at every cell by Ax 3. The ladder is lossless, so `|Γ_in| = 1` **exactly** for any `|Γ_L| = 1` termination — this is not an assumption, it is the frozen gate `G-UNIT`, and it is what makes `|Γ_in|` under the **matched** termination a clean measurement of the ladder's own reflection rather than of anything absorbed. **No "absorption", no "dissipation", no "damping", no "loss" is attributed to the wall, to the depleted section, or to the contact by this lane.** The only port in the problem is the radiative one at infinity, outside the interval being measured.
 7. CALIBRATABILITY:         The delay's verdict-class output is the dimensionless `c₀ΔT/r_sat`. Y8's outputs are **already dimensionless by construction** — `|Γ_in|` is a ratio of two amplitudes at one plane, `|T|²` is a power ratio, `W` is an integer count of cells, and `dφ_Γ/dω` is reported in units of `r_sat/c₀`. **`α` appears nowhere in the chain.** The one dimensional output (the ripple period in rad/s) is reported alongside its dimensionless form in `Ω`.
 8. DISCRIMINATION CLASS:    **DC→AC coupling** — a DC gravitational bias modulating an AC shear-wave transit time and reflection. Live chord class. **Tautology filter:** `W(ω)` is NOT a restatement of the v1 turning-point inequality — it is an integer cell count derived from it, and its ZERO-vs-NONZERO verdict carries content the inequality's ratio does not (a ratio of `0.99` and a ratio of `0.23` both give `W = 0`). **`|Γ_in|` under the matched contact is NOT a restatement of the impedance profile**, because the exact continuum near-wall equation is an Euler equation whose two solutions are exact and uncoupled — **the continuum reflects nothing**, so any measured `|Γ_in|` is DISCRETENESS content and nothing else (§2Y.6). **SM/GR counterfactual, stated in advance:** GR-Kerr has no last cell, no depletion edge and no contact — the whole Y8 question is unavailable in the continuum theory; ECO models replace the contact by a free-knob reflectivity, so an ECO can reproduce **any** `Γ_L` and the reach-through verdict discriminates **nothing** by itself. **`FLAG-ECO` therefore extends to Y8 in full and is a frozen headline requirement (§9).**
 9. CERTIFICATION PLAN:      Gates §5 and fireability self-tests §6 frozen before any number exists; **UNRUN ≠ PASSED**; **two negative controls against v1's own shipped numbers** (`G-NC-V1A` exact reproduction of the certified CFG-A set; `G-NC-V1B` invariance of the CFG-B diagnostics) plus v1's own predecessor control `G-NC`; **one cross-part control** (`G-XTIE`: Y8's mirror-termination phase slope must reproduce Part 1's node-sum round-trip delay over the same window); determinism by two-run digest.
10. ADJUDICATION ROUTING:    PART 1 settles **whether the repaired instrument certifies CFG-B**, and if so adjudicates `BIN-DB`, `BIN-DISC` and CFG-B's `BIN-CUTOFF` / `BIN-EVAN` per v1's frozen definitions. PART 2 settles **which of three frozen bins the RHO-B composite reflection falls in** and thereby **updates the chirp question of v1 §2.7**. It settles **nothing** about FORK-3(b), nothing about FLAG-CAUSAL (which it SWEEPS at all three values and does not resolve), nothing about echo amplitude beyond the declared plane, and nothing observational. On every outcome the propagation target is **a research-doc result and a docket fragment only**.
11. ★ NUMERICAL CONDITIONING: *(pilot-2's proposed row 11, adopted voluntarily on its proposer's own case — the v1 near-miss was that a float64 `1 − A²` returns **exactly zero** at these scale ratios and the whole calculation would have shipped silent nonsense with no error.)* **NAMED CANCELLATIONS.** (i) `1 − A²` at the innermost node, where `ℓ_node/r_sat ≈ 6.0e-19` — **catastrophic in float64, returns exactly `0`**; computed instead from `S² = x(2r_sat + x)/(r_sat + x)²`, which is cancellation-free for `x > 0`. (ii) `S^{-p} − 1` in the far field, where `A → 0` — computed from `expm1(−(p/2)·log S²)`. (iii) `artanh(A_hi) − artanh(A_lo)` in the decade sweep: two values of order `40` differenced to expose a relative deviation of order `1e-13`, i.e. **≈ 14 decimal digits of cancellation** — run at mpmath `dps = 50`, leaving `> 30` digits of headroom. (iv) NEW IN v2: `1 + ρ_nΓ` in the Schur recursion, catastrophic only as `ρ_n → −1`; bounded here because `|ρ_n| ≤ (√2−1)/(√2+1) = 0.1716` at every cell (the innermost impedance step is the largest, and it is `√2`). (v) NEW IN v2: accumulated phase `Σ2θ_n` over the window — **bounded at `≈ 27` radians round-trip because the delay law is LOGARITHMIC**, so no argument-reduction blow-up occurs; this is a property of the physics, not a numerical choice, and is stated so a successor on a power-law profile knows it does not carry over. **DYNAMIC RANGE.** `ℓ_node/r_sat ~ 6e-19`; `S ∈ [1.1e-9, 1]` over the window and `S² ∈ [1.2e-18, 1]`; normalized impedance `z ∈ [1e-3, 1]`; per-cell electrical length `θ_n ∈ [~1e-6, ~0.93]` rad; `Ω = O(1)`; `W ∈ ℤ≥0`. **WORKING PRECISION.** mpmath `dps = 50` for every closed form, every gate comparison, every decade/`K_disc` sweep, and every quantity built from `ℓ_node/r_sat` — i.e. **extended precision is used wherever a ratio reaches `1e-19`**. float64 is used ONLY for (a) the `10⁶`-term node-sum block, exactly as v1 (its accumulation error is measured, not assumed, by `G-SUM` and by `G-NC-V1A`/`G-NC-V1B`), and (b) the `10⁶`-cell Schur recursion, which is a composition of **Möbius maps of the unit disc** — non-expansive, so error does not amplify — and whose accumulated float64 error is **measured directly** by `G-UNIT` (`|Γ_in| = 1` exactly for `|Γ_L| = 1`) and **certified against an mpmath `dps = 50` re-run** at `K = 10⁴` by `G-PREC`. **No quantity in this lane is computed in float64 without a gate that measures its float64 error.**

---

## §0.1 — Substrate-native walk (`substrate-native-check`, fired BEFORE the first line of numerical code)

1. **K4 / srs connectivity.** Carried forward from v1 unchanged and re-stated because Y8 leans on it harder than v1 did. Frozen: `the radial path is modelled as a ONE-DIMENSIONAL cascade of node-spaced transmission-line sections, the substrate-native band model for which is the coined-quantum-walk / transmission-line ARCCOS map omega = omega_link*arccos(mu/z) adjudicated at srs-band-structure.md section 2, and NOT the graph-Laplacian omega = sqrt(lambda) map which that same section shows FAILS the 1/sqrt3 velocity gate; the 1D reduction is a DISCLOSED modelling choice for the radial direction and its 3D-srs correction is NOT computed`.
2. **★ THE CHECKPOINT THAT CHANGES Y8, AND IT IS NOT THE ONE A SEMICONDUCTOR ENGINEER WOULD REACH FOR.** The ruled vocabulary says "the per-frequency surface where the local band edge falls to the drive". **A depletion edge in a semiconductor is an EVANESCENCE onset: past it the carrier wave is exponentially attenuated.** On the **adjudicated** substrate-native cell model it is **not**: a cascade of ideal lossless transmission-line sections has **no cutoff at any frequency** — its "band top" `π√3 ω_C` is the **first-Bragg / half-wave-line resonance** that `srs-band-structure.md` §2 identifies it as, not an evanescence onset. **True evanescence exists only under the REJECTED lumped/tight-binding model.** Frozen: `the depletion edge of this lane is defined EXACTLY as v1 section 2.7 defined the band-edge turning point, omega = omega_max(r) = beta*omega_C*S(r)^p, and it is a BRAGG/half-wave surface of the adjudicated distributed cell model rather than an evanescence onset; the semiconductor register's evanescence connotation is DECLARED NOT TO CARRY OVER, no exponential attenuation length is computed or claimed anywhere in this lane, and the exact per-cell ABCD product is the arbiter in place of any band-structure heuristic`.
3. **Op14 saturation.** Enters as the static grade `S = √(1−A²)` in the modulus; under RHO-B a second time in the inertia; a third time in the **local band top** `ω_max(r) = β ω_C S^p` (v1's new content); and — ★ **new in v2, a fourth time** — in the **local characteristic impedance** `Z(r) = ρ_bulk c₀ S^{1−p}`, which under RHO-B **DIVERGES** at the wall where under RHO-A it **VANISHES**. Frozen: `Op14 enters the Y8 two-port through the LOCAL CHARACTERISTIC IMPEDANCE Z = rho*v = rho_bulk*c_0*S^(1-p) as well as through the local speed, so the graded region is an impedance TAPER as well as a delay taper, and the per-cell impedance step is the substrate-native origin of any reflection this lane measures`.
4. **The compactification is the medium's own order parameter.** `A = r_sat/r` IS the Ax-4 saturation amplitude; `A = 1` IS the wall.
5. **Phase-space vs real-space (A46).** Every Y8 verdict-class observable is dimensionless: `|Γ_in|`, `|T|²`, the integer `W`, the phase slope in `r_sat/c₀`. **α-CLEAN.**
6. **Boundary-not-bulk.** Y8 is *entirely* a boundary computation: the frozen window is the innermost `10⁶` cells, three decades of `S`, `x/r_sat ≤ 6.0e-13`. **If the physics does not live in the skin, Y8 measures nothing** — and `G-KWIN` (window-independence) is the gate that says which.
7. **Group vs phase velocity.** Carried forward from v1, re-derived and re-gated (`G-DISP`): under the adjudicated arccos map on the `z = 2` radial cascade the dispersion is **exactly linear**, so `v_group ≡ v_phase = c(r)` and **each cell's electrical length is exactly proportional to ω**. ★ **This is what makes the mirror-termination phase slope EXACTLY frequency-independent, i.e. what makes the delay achromatic at the level of the reflection phase rather than only at the level of a turning-point inequality.**
8. **★ NEW CHECKPOINT forced by Y8: is a cascade of per-cell UNIFORM sections the substrate-native discretization, or is the impedance a BOND quantity defined at cell midpoints?** Undetermined at freeze; frozen as an ENG-CHOICE with the midpoint reading swept as variant `Y-MID` (§4Y.4), because **the answer changes the innermost impedance step and therefore the measured reflection**.

---

## §0.2 — Pre-test physics check (`pre-test-physics-check`, Rule 16 — asked BEFORE the design locks, not after)

> **Grant — v1 asked you which way a tapered ladder terminates, and you ruled the register and the carves. This is the question your ruling creates, and I cannot answer it from canon either.**
>
> Your ruling says the depleted cells are a **junction two-port** and the thin-`W` limit is **reach-through: the far contact governs.** I have built exactly that. But building it forces the question of **what the far contact IS**, and canon gives me three readings and no way to choose:
>
> - **a matched port** — the ROW-IN reading the axial lane derived: purely ingoing at the wall, nothing returns from a termination of infinite electrical length, the Ax-3-licensed mirror of the port at infinity. `Γ_L = 0`.
> - **a free end** — the lattice simply stops; the innermost node has no inward neighbour, so its traction is unopposed. `Γ_L = −1` in the traction↔voltage convention.
> - **a clamped end** — the Regime-IV interior is ruptured topology that does not move, so the innermost node's velocity is pinned. `Γ_L = +1`.
>
> **This is `FLAG-CAUSAL` in its sharpest form and I am NOT going to resolve it by preference.** I sweep all three. But here is why the sweep is worth running rather than being a shrug: **if the reach-through verdict comes back CONTACT-GOVERNED, then `Γ_in` at the observable plane IS `Γ_L`, and the depleted section provides NO isolation between the observable and your unresolved fork.** The whole echo question under RHO-B would then be *your* question, undiminished, with no numerical cushion. **If instead it comes back EDGE-GOVERNED, the near-wall staircase screens the contact and the fork stops mattering for the observable.** So the run tells us **how much the unresolved fork costs**, which is a different and more useful thing than pretending to resolve it.
>
> **My one plumber question, and it is about the model and not about the physics:** when you build a real tapered line out of discrete sections, do you put the section's characteristic impedance at the **node** (each cell uniform, stepping at cell boundaries) or on the **bond** (the impedance is a property of the link between two nodes, i.e. evaluated at the midpoint)? On this profile the two differ **only at the innermost cell** and they differ there by the full `√2` step, which is exactly where the reflection is generated. **I have frozen the node reading as primary and the bond reading as a swept variant, and I will report both.** If your bench instinct says one of them is obviously right for a physical ladder, that is a ruling I would rather have before the next lane than after.
>
> **Carried forward and NOT re-asked:** `FLAG-ECO`, `FLAG-PLANE-GAP`, `FLAG-CANON`, `FLAG-PITCH`, `FLAG-BRACKET`, `FLAG-FREEZE-SIZING`.

---

## §0.3 — Consistency-vs-emergence tag (`consistency-vs-emergence`), computed BEFORE any result

| output | rides an imported VALUE? | class |
|---|---|---|
| `2𝒥_A` (the RHO-A delay coefficient) | **NO** | **AXIOM-MANIFESTATION, FORM-class** |
| any delay in seconds | **YES** (`G`, `M`, the GR-imported `7`, definitional `ℓ_node`) | **VALUE-CONSISTENCY.** May NOT be headlined as value-level emergence. |
| `K_disc(θ) = [ln θ − ψ(θ)]/2` | **NO** — a pure consequence of `Σ1/(n−1+θ)` vs `∫dx/x` | **AXIOM-MANIFESTATION, FORM-class** (it is a property of discreteness, not of AVE) |
| the decade law `δ = (S_hi²−S_lo²)/(4 ln 10)` | **NO** | **AXIOM-MANIFESTATION, FORM-class** — a property of the Ax-4 kernel through `artanh` |
| ★ `W(ω) = ⌊Ω/(2β) + 1 − θ⌋` | **NO** — mass-free; `β` is bracketed and `θ` is a regulator | **FORM-class, DERIVED, MASS-INDEPENDENT.** The **bracket** and the **regulator** are its only inputs and both are swept. |
| ★ `\|Γ_in\|` under the matched contact | **NO** — the near-wall two-port is mass-free to `O(ℓ_node/r_sat)` (§2Y.7) | **FORM-class, DERIVED.** It is a pure number produced by lattice discreteness on the Ax-4 profile. |
| ★ the reach-through BIN | **NO** | **FORM-class.** But see the discrimination fence: an ECO model with a free contact reflectivity reproduces any bin, so **the bin is FORM-class and NOT AVE-discriminating.** |
| the ripple period in rad/s | **YES** (`r_sat/c₀`) | **VALUE-CONSISTENCY** on the seconds value, FORM-class on its `Ω` value. |

Frozen tag: `every LAW derived here is a FORM-class axiom manifestation of the Ax-4 kernel plus lattice discreteness; every SI-second and SI-rad/s VALUE is VALUE-CONSISTENCY class because it rides G, M, the GR-imported nu_vac in r_sat = 7GM/c^2 and the definitional l_node = hbar/(m_e*c); no output of this lane may be headlined as value-level emergence, and the reach-through BIN is explicitly NOT an AVE-vs-ECO discriminator because the ECO family carries a free contact reflectivity`.

---

## §0.4 — ★ THE THREE MANDATORY CARVES, DECLARED (register ruling, binding)

The semiconductor register is used because it is the right engineering language for a graded region that loses band support toward one end. **It imports three theorems that do NOT hold here, and each is carved out explicitly rather than left to context.**

1. **WHAT IS DEPLETED IS SIGNAL-BAND SUPPORT, NOT CHARGE.** Frozen: `nothing in this lane is depleted OF anything; the depleted quantity is the local availability of propagating T2 states at the drive frequency, there is no carrier density, no doping, no ionized-donor background and no charge of any kind in the problem, and the word "depletion" carries ONLY the band-support meaning`.
2. **THE DEPLETION EDGE IS DRIVE-FREQUENCY-INDEXED.** Frozen: `there is no single depletion edge; there is one edge PER DRIVE FREQUENCY, r_dep(omega), and W is therefore a function of omega and not a property of the structure; every W, every junction two-port and every Gamma_in in this lane carries its omega, its beta and its theta at every reporting site`.
3. **NO SPACE-CHARGE / BUILT-IN-FIELD ELECTROSTATICS RIDES ALONG.** Frozen: `no Poisson equation is solved, no built-in potential, no depletion approximation, no abrupt-junction or linearly-graded-junction electrostatics, no C-V relation and no bias-dependent width law enters this lane at any point; W is set by the Ax-4 grading and the drive frequency alone, the analysis is SMALL-SIGNAL NETWORK TOPOLOGY ONLY, and the DC bias point is the gravitational grading which no signal in this lane perturbs`.

**And the fourth carve, which is this lane's own and is a scope fence rather than a vocabulary one.** Frozen: `REACH-THROUGH here means ONLY that the composite reflection at the declared plane is dominated by the far contact rather than by the depletion edge; it does NOT mean punch-through, it does NOT imply breakdown, it does NOT imply any irreversible process, and it makes NO statement about Regime IV, which remains outside the domain`.

---

## §1 — THE TARGET AND THE EXPLICIT NON-CLAIMS

### §1.1 The targets

**PART 1.** Re-run the v1 regulated-return instrument with `G-DISC`'s derived law repaired and `G-DECADE`'s tolerance resized from its own derived correction law, **with no other threshold, bin boundary, variant, mass, `θ`, `β` or `N_split` changed**, and report per-configuration certification and — for any configuration that certifies — the v1 bin verdicts under v1's byte-identical criteria.

**PART 2 (Y8).** Under RHO-B, across the frozen ringdown band, at both band-top bracket ends and both `θ` cutoffs, compute and report: **the depletion width `W(ω)` in cells; the junction two-port `ABCD` across those cells; the composite `Γ_in(ω)` with the far contact's branch-derived condition swept over its three frozen readings; `|T|²` through the depleted section; and the phase slope `dφ_Γ/dω`.** Bin the result into `CONTACT-GOVERNED` / `EDGE-GOVERNED` / `INTERFERENCE`, and state the RHO-A side explicitly.

### §1.2 The non-claims, written in advance and binding

- **NO adjudication of FORK-3(b).** Frozen: `this lane computes under both branches; it does not prefer RHO-A over RHO-B or RHO-B over RHO-A, and a cleaner number on one branch is not evidence for that branch`.
- **NO adjudication of FLAG-CAUSAL.** Frozen: `the far-contact condition is SWEPT at Gamma_L in {-1, 0, +1} and is NOT resolved; no reading is preferred; the lane reports how much the unresolved fork costs the observable and nothing more`.
- **NO echo-TRAIN or echo-AMPLITUDE claim.** Frozen: `an echo train requires an OUTER partial reflector at a plane outside the frozen near-wall window, and this lane computes NO reflection coefficient at any such plane, so it states an INNER reflection at a declared near-wall plane and never an echo amplitude, an echo count, an echo visibility or a detectability`.
- **★ NO `Γ_in` AT PLANE-PEAK OR PLANE-∞, AND THE REASON IS THE RULING ITSELF.** Frozen: `the ruling forbids WKB and forbids any continuum approximation, and the exact per-cell product from the wall to the barrier peak is about 1.2e18 cells, which is not enumerable; this lane therefore reports Gamma_in ONLY at PLANE-JX and PLANE-NW, computes NOTHING at PLANE-PEAK or PLANE-inf, and states that the outer cascade's contribution to the composite reflection is NOT computed and is NOT bounded here`.
- **NO observational claim.** Frozen: `no LIGO/Virgo dataset is analysed, no detection or non-detection is asserted, and every observational quantity that appears is an IN-REPO CITED POINTER used as a comparison scale only`.
- **NO re-score, re-open or withdrawal of v1.** Frozen: `v1's DELAY-NOT-CERTIFIED verdict on CFG-B stands as a historical fact; v2 is a successor instrument with its own version number, and a v2 certification is NOT a retroactive v1 pass`.
- **NO repair of any flagged leaf.** Frozen: `FLAG-ECO-COROLLARY, FLAG-PLANE-GAP, FLAG-CITE-SHIFT and FLAG-CANON are carried forward BY POINTER, are repaired NOWHERE, and no edit to any KB, manuscript or frozen research document is proposed`.

### §1.3 What this lane additionally does NOT do

- **Z1** — does NOT derive `ℓ = 2`, `ν_vac`, `K = 2G`, or the `7`.
- **Z2** — computes no eigenvalue, pole, `Q` or mode; v2.4's certified root is consumed as a **frequency scale and a band definition** only.
- **Z3** — does NOT build the Cosserat microrotational channel and does NOT treat the polar/spheroidal branch.
- **Z4** — does NOT resolve the single-scale-vs-stiffness-lifted band-top fork; **sweeps** it.
- **Z5** — does NOT compute the 3D srs correction to the 1D radial cascade.
- **Z6** — does NOT model the Regime-IV interior and computes nothing at `r < r_sat`.
- **Z7** — ★ does NOT compute an evanescent attenuation length, a WKB transmission integral, or anything the word "tunnelling" would name. **The exact per-cell `ABCD` product replaces all of it, by ruling.**
- **Z8** — does NOT settle whether the lattice pitch is itself strained (`R4` sweeps it, `Y-PITCH` sweeps it in Y8, neither settles it).
- **Z9** — does NOT land any claim, solidity change, KB row, manuscript edit or ledger entry, whatever the outcome.
- **Z10** — does NOT edit any other lane's `Makefile` recipe; it appends its own target only.

---

## §2P — PART 1: THE TWO REPAIRS, RE-DERIVED HERE FROM SCRATCH BEFORE ANY RE-RUN

**Discipline note, stated first.** v1 derived both corrected laws *after* seeing its gates fail. **This lane does not import either of them.** Both are re-derived below from the sum-versus-integral structure and from the Ax-4 kernel's own expansion, and the numbers v1 reported are used **only** afterwards, as a consistency remark, never as the source.

### §2P.1 `K_disc(θ)` — re-derived from the harmonic sum, per ONE-WAY pass

Under RHO-B the speed is `v = c₀S²` and near the wall `S² = x(2r_sat + x)/(r_sat + x)² → 2x/r_sat`, so

```
1/v - 1/c_0  ->  r_sat / (2 c_0 x)          (the factor 1/2 is the whole of v1's error)
```

The regulated node sum places node `n` at `x_n = (n − 1 + θ)ℓ`, so the one-way node sum of the excess over the first `N` cells is

```
SUM_{n=1..N} l * [1/v(x_n) - 1/c_0]  =  (r_sat/(2 c_0)) * SUM_{n=1..N} 1/(n - 1 + theta)
                                      =  (r_sat/(2 c_0)) * [ psi(N + theta) - psi(theta) ]
```

using the exact digamma identity `Σ_{n=1}^{N} 1/(n−1+θ) = ψ(N+θ) − ψ(θ)`. The continuum integral **cut at the same inner radius** `x_in = θℓ` and carried to the same outer radius `x = Nℓ` is

```
INT_{theta*l}^{N*l} r_sat dx / (2 c_0 x)  =  (r_sat/(2 c_0)) * [ ln N - ln theta ]
```

Subtracting and using `ψ(N+θ) − ln N → 0` as `N → ∞`:

```
K_disc(theta)  ==  (sum - integral) / (r_sat/c_0)  =  [ ln(theta) - psi(theta) ] / 2      PER ONE-WAY PASS
```

**Two independent evaluations, both closed-form, available at freeze:** `ψ(1) = −γ` gives `K_disc(1) = γ/2`; `ψ(1/2) = −γ − 2ln2` gives `K_disc(1/2) = (γ + ln2)/2`. Frozen: `the v2 G-DISC gate compares the MEASURED one-way discrete-minus-continuum offset against K_disc(theta) = [ln(theta) - psi(theta)]/2, evaluated in mpmath from the digamma function and NOT from a transcribed constant, at BOTH frozen theta values; the tolerance is CARRIED UNCHANGED from v1 at 1 per cent and is NOT resized, because only the LAW was wrong and the law is now derived rather than assumed`.

**The pass-count discipline the failure bought, frozen as a reporting requirement:** `every discrete-correction constant reported by this lane states its PASS COUNT explicitly at every site; K_disc is a ONE-WAY constant, its round-trip value is 2*K_disc, and a bare "gamma" with no pass count may not appear anywhere in the result document`.

### §2P.2 `G-DECADE` — the tolerance re-sized from the Ax-4 kernel's own expansion

Under RHO-B the one-way excess between two radii is `(r_sat/c₀)[artanh(A_in) − artanh(A_out)]`. Expanding `artanh` at the wall in the medium's own order parameter, with `A = √(1−S²)`:

```
1 - A = S^2/2 + S^4/8 + O(S^6) ,   1 + A = 2 - S^2/2 - S^4/8 + O(S^6)
(1+A)/(1-A) = (4/S^2) [ 1 - S^2/2 + S^4/16 + O(S^6) ]
artanh(A)   = ln(2/S) - S^2/4 + O(S^4)
```

A decade of `S` from `S_hi` down to `S_lo = S_hi/10` therefore contributes

```
Delta = ln 10 + (S_hi^2 - S_lo^2)/4 + O(S_hi^4)
rel deviation from ln 10:   delta(S_hi) = (S_hi^2 - S_lo^2) / (4 ln 10) = 0.99 * S_hi^2 / (4 ln 10)
```

**This is the exact leading law and the `S²/(4 ln 10)` coefficient v1 named, with the `(1 − 10⁻²)` factor v1's one-per-cent remark absorbed.** Its worst value over the frozen five-rung ladder (`S_hi ∈ {1e-2 … 1e-6}`) is at the shallowest rung, `S_hi = 1e-2`.

**Two frozen limbs, because a resized tolerance alone would make the gate weaker and the derived law deserves to be tested rather than merely accommodated:**

- **`G-DECADE(a)` — the leading-term limb, RESIZED.** `max_k |Delta_k/ln10 - 1| <= TOL_DECADE_A`. **`TOL_DECADE_A = 1e-4`**, derived: the largest *derived* deviation is `0.99 × (1e-2)² / (4 ln 10) = 1.0748788e-5`, so `1e-4` carries **`9.30×` headroom over the derived worst case** while remaining **four orders below** the `O(1)` deviation a wrong power law would produce (`FT-DECADE` measures `≈ 1` on the RHO-A profile). **v1's `1e-6` is superseded because it was sized against zero correction; it is NOT widened after seeing a result, it is re-derived from the correction law the v1 prereg itself disclosed at §4.5 and then failed to use.**
- **`G-DECADE(b)` — the RESIDUAL limb, NEW and STRICTLY STRENGTHENING.** `max_k | (Delta_k/ln10 - 1) / [0.99 * S_hi,k^2/(4 ln 10)] - 1 | <= TOL_DECADE_B`. **`TOL_DECADE_B = 1e-3`**, derived: the next-order term enters this ratio as `(3/8)S_hi² + O(S_hi⁴)`, worst `3.75e-5` at the shallowest rung, so `1e-3` carries **`26.7×` headroom**. **This limb tests the `S²` SHAPE, not just its size: a law with a different power fails it by orders.**

**`G-DECADE` = `(a)` AND `(b)`.** Frozen: `G-DECADE in v2 has two limbs and passes only if BOTH pass; limb (a) is the v1 gate with its tolerance re-derived from the O(S^2) correction law and stated with its headroom; limb (b) is a NEW and strictly stronger test of the correction's SHAPE; no other gate, tolerance, bin boundary, variant, mass, theta, beta or N_split anywhere in this instrument is changed from v1`.

### §2P.3 The negative controls — v1's own numbers, and the STOP rule

The gates were wrong; the numbers were not. **Every v1 number this instrument recomputes must come back byte-identical at its shipped precision.**

- **`G-NC-V1A` — the certified CFG-A set.** Frozen: `the v2 driver recomputes J_A, 2*J_A, the CFG-A delay at every mass on the frozen grid, the CFG-A regulator spread and the CFG-A PLANE-PEAK total, and each must reproduce the corresponding value in the READ-ONLY v1 shipped JSON research/drivers/echo_delay_regulated_sum_results.json to EXACT STRING EQUALITY at v1's own 17-significant-digit rendering; a single differing digit FAILS the gate`.
- **`G-NC-V1B` — the CFG-B diagnostics, which must be UNCHANGED under the repaired gates.** Frozen: `the v2 driver recomputes the CFG-B delay at every mass, the round-trip K_disc at every mass, every entry of the CFG-B regulator sweep, both barrier peaks, every S_turn/S_last ratio and every BIN-DISC row, and each must reproduce the v1 shipped value to EXACT STRING EQUALITY at 17 significant digits; the gates were wrong and the numbers were not, so a moved number means something OTHER than the two repairs has changed`.
- **`BIN-STOP-V1` — the STOP rule, frozen.** `if G-NC-V1A or G-NC-V1B fails, the lane STOPS: it reports the moved value with both renderings, adjudicates NO bin in either part, publishes the discrepancy as a FLAG, and does NOT proceed to interpret any Y8 number, because a Y8 built on a drifted Part 1 is uninterpretable`.
- **`G-NC` — v1's predecessor control, carried forward byte-identical.** The 2026-06-17 driver at all four of its own `r_out/r_sat` entries, `1e-10` relative.

---

## §2Y — PART 2: Y8, THE REACH-THROUGH COMPUTATION — every statement below is a THEOREM available at freeze

### §2Y.1 The depletion edge — DEFINED by carrying v1's frozen criterion forward

`ω_max(r) = β ω_C S(r)^p` is the local band top (v1 §2.5, Op14 applied to a band edge). The **depletion edge** at drive frequency `ω` is the radius where it falls to the drive:

```
S_dep(omega, beta, p) = eps^(1/p) ,      eps == omega / (beta * omega_C)
                      = sqrt(eps)        under RHO-B (p = 2)
```

**Byte-identical to v1's `S_turn`.** Frozen: `S_dep is v1's S_turn under a ruled name; no criterion is redefined, and the v2 result doc states the identity explicitly so no reader can mistake the rename for a new definition`.

### §2Y.2 ★ THE FROZEN BAND — a POINTER to v2.4's artifacts, not a transcription

The ringdown-relevant band is the **Lorentzian FWHM of the certified axial pole**, which is the substrate's own answer to "which frequencies are in the ringdown". Both endpoints are read **PROGRAMMATICALLY** from `research/drivers/coldq_pole_v2p4_root_results.json`:

```
Omega_R = certified_root/Omega_re_mp            (the certified real part)
Omega_I = | certified_root/Omega_im_mp |        (the certified imaginary part)
BAND    = [ Omega_R - Omega_I , Omega_R + Omega_I ]        FWHM of the Lorentzian
```

Frozen: `the ringdown-relevant band is the FWHM of the v2.4 certified axial pole, [Omega_R - Omega_I, Omega_R + Omega_I], with BOTH endpoints read programmatically from the v2.4 shipped JSON and NEITHER transcribed; it is sampled at 65 points LINEARLY spaced in Omega inclusive of both endpoints; the number 65 is an ENGINEERING CHOICE sized in section 4Y.2 from the derived ripple period so the band is not undersampled, and no band boundary anywhere in this lane is set from any value this instrument measures`.

**Two-method receipt on the band, gated as `G-BAND`:** the same `Ω_I` must be recoverable as `x_sat × (adjudication/omega_I_M_g)` from the same JSON, since `Ω = ω r_sat/c₀` and `r_sat = 7 GM/c²`. Frozen tolerance `1e-15` relative — both are renderings of one shipped quantity, so anything larger means the JSON's own two fields disagree and that is worth knowing.

### §2Y.3 ★ THE DEPLETION WIDTH `W(ω)` — derived in closed form, and it is MASS-FREE

Nodes sit at `x_n = (n − 1 + θ)ℓ_node`, `n = 1 … N`, with node `1` the innermost intact cell and **no lattice inside `r_sat`** (Regime IV). A cell is **depleted** iff its `S` lies below the edge, `S_n < S_dep`. Since `S_n` increases outward,

```
W(omega, beta, theta) = # { n >= 1 : S_n < S_dep }            [an INTEGER count of cells]
```

**Exact form.** With `A_dep = √(1 − S_dep²)` and `x_dep = r_sat(1/A_dep − 1)`:

```
W = max( 0 , floor( x_dep / l_node - theta + 1 ) )
```

**Asymptotic form, and this is where the content is.** Near the wall `S_n² ≈ 2x_n/r_sat`, and under RHO-B `S_dep² = ε = (ω/ω_C)/β = Ω ℓ_node/(β r_sat)`, so `x_dep ≈ (ε/2)r_sat = Ω ℓ_node/(2β)` and

```
W  =  max( 0 , floor( Omega / (2 beta) + 1 - theta ) )         <-- CONTAINS NO MASS
```

**Both cutoffs scale as `ℓ_node`, so the ratio is a pure number built from the frozen `Ω`, the bracketed `β` and the regulator `θ`, at every mass** — the same mass-independence mechanism v1 found for `S_turn/S_last`, and indeed `W ≥ 1 ⟺ Ω ≥ 2θβ ⟺ S_dep ≥ S_1 ⟺ S_turn/S_last ≥ 1`, so **v2's integer count and v1's ratio are the same statement at different resolution.** Frozen: `W is computed BOTH by the exact inversion and by a direct node-by-node count from the exact cancellation-free S_n, and the two must agree as EXACT INTEGERS (gate G-DEP); the mass-free asymptotic form is reported alongside and its agreement with the exact form is reported as a relative offset in x_dep rather than gated, because W is an integer and an integer either matches or does not`.

### §2Y.4 ★ THE FAR CONTACT'S BRANCH-DERIVED CONDITION — RE-DERIVED HERE, NOT IMPORTED

The axial RHO-B lane derived a wall row at a regular singular point. **This lane re-derives the same indicial structure from its own Schrödinger-form potential** — the one v1's `G-U` gate certifies against the raw transformation — and only afterwards checks that it agrees.

v1 §2.6 (gated by `G-U` at `5.3e-50`) reduces the radial system to `Ψ'' + [ω²/v² − U]Ψ = 0` with `Ψ = r√μ W` and

```
U = l(l+1)/r^2 + 2g/r + g^2/4 + g'/2 ,      g = mu'/mu = (d/dr) ln S
```

Near the wall, with `x = r − r_sat` and `S² ≈ 2x/r_sat`:

```
g = (1/2) d(ln S^2)/dr -> 1/(2x)      =>  g^2/4 = 1/(16 x^2) ,   g'/2 = -1/(4 x^2)
U -> 1/(16 x^2) - 1/(4 x^2) = -3/(16 x^2)                       (the l(l+1)/r^2 and 2g/r terms are subleading)
omega^2/v^2 = Omega^2/(r_sat^2 S^4) -> Omega^2/(4 x^2)          under RHO-B (v = c_0 S^2)
```

so the near-wall equation is **an EULER equation**, exactly:

```
Psi'' + [ Omega^2/4 + 3/16 ] Psi / x^2 = 0
Psi ~ x^s ,   s(s-1) + Omega^2/4 + 3/16 = 0   =>   s_pm = [ 1 +- sqrt(1/4 - Omega^2) ] / 2
```

**The cross-check against the axial lane, done as a derivation and not as an import.** That lane works in `η` with `A = 1 − η²`, so `x = r_sat η²/(1−η²) ∝ η²`, and its `ψ` is related to this lane's `Ψ` by `Ψ = r√μ · A e^{iΩ(1/A+λA)} ψ`, whose prefactor contributes `√S ∝ η^{1/2}` and whose exponential is regular at the wall. Hence `Ψ ∝ η^{σ + 1/2} = x^{(σ + 1/2)/2}`, i.e. `s = (σ + 1/2)/2`, i.e.

```
sigma = 2s - 1/2 = [ 1 +- sqrt(1 - 4 Omega^2) ] / 2
```

**— which is exactly the axial lane's frozen indicial equation `σ(σ−1) + Ω² = 0`, obtained here from a different starting point and a different variable.** Frozen: `the RHO-B near-wall indicial structure is RE-DERIVED in this lane from its own G-U-certified Schrodinger-form potential in the radial variable x, is shown to be an EULER equation, and its exponents are mapped onto the axial lane's sigma by the exact prefactor relation s = (sigma + 1/2)/2; the agreement is recorded as a CROSS-LANE DERIVATION CHECK on two independent algebras and NOT as corroboration of any measured value, since neither lane measured anything here`.

**★ WHAT THE EXPONENTS SAY, AND THE ONE SCOPE STATEMENT THAT MUST TRAVEL WITH THEM.** For a **REAL** drive with `Ω > 1/2` — which every point of the frozen band is — `√(1/4 − Ω²)` is purely imaginary, so

```
s_pm = 1/2 +- (i/2) sqrt(4 Omega^2 - 1)
Psi ~ x^{1/2} exp( +- i * (1/2) sqrt(4 Omega^2 - 1) * ln x )
```

**— two counter-propagating waves whose phase is LOGARITHMIC in `x`.** For `Ω ≫ 1/2` the phase rate approaches `Ω/2` per e-fold of `x`, which is exactly `∫ω dr/v = (Ω/2)ln x`: **the log-divergent optical distance of the axial lane's §2.4(b), recovered as the phase of an exact solution.** Frozen, and it is a SCOPE statement rather than a flag: `at REAL drive frequency with Omega > 1/2 the two RHO-B near-wall exponents are complex conjugates with EQUAL real part 1/2, so Re(sigma_+ - sigma_-) = 0 and neither branch is excluded by boundedness, and the finite-energy criterion Re sigma > 1/2 is marginally violated by BOTH; this is a property of the REAL-FREQUENCY SCATTERING problem this lane poses and it bears on NO eigenvalue lane, because the axial lane's function-space argument is made at COMPLEX Omega where the same difference is generically non-zero; nothing here is offered as a correction to, or a criticism of, that lane`.

**Therefore the far contact is NOT determined by the continuum analysis.** Both exponents are admissible; the selection is the physical question `FLAG-CAUSAL` asks. On the **lattice** the cascade is cut at node 1, and the contact becomes a lumped termination with three frozen readings (§2Y.5).

### §2Y.5 ★ THE PER-CELL TWO-PORT — derived, with its analogy convention declared

**The local characteristic impedance, derived in one line.** With `μ = G_vac S` and `v = c₀S^p`, the inertia is `ρ = μ/v² = ρ_bulk S^{1−2p}`, so

```
Z(r) = rho * v = rho_bulk * c_0 * S^{1-p}
     -> Z_0 sqrt(S)   (RHO-A, p = 1/2)   : VANISHES at the wall
     -> Z_0 / S       (RHO-B, p = 2)     : DIVERGES at the wall
     -> Z_0 / S^2     (SYN,   p = 3)
```

**The RHO-B form reproduces the axial lane's two-method `Z_shear = √(μρ) = ρ c_shear = 1/S` exactly, re-derived here from `p` alone.**

**The analogy convention, DECLARED rather than assumed** (wall-taxonomy §9 discipline). `Z = traction/velocity`, hence **traction ↔ voltage** and **velocity ↔ current**. Under this convention a **traction-free free end is a SHORT (`Γ_L = −1`)** and a **velocity-clamped rigid end is an OPEN (`Γ_L = +1`)`. Frozen: `the force-voltage analogy is DECLARED, the labels free-end and clamped-end map to Gamma_L = -1 and +1 respectively under it, they SWAP under the dual mobility analogy, and every physics statement this lane makes is a statement about the SET {-1, 0, +1} and about spreads across it, so no conclusion of this lane depends on which analogy is chosen`.

**The per-cell `ABCD`, exact.** Cell `n` is a lossless section of characteristic impedance `Z_n` and electrical length `θ_n`:

```
ABCD_n = [ [ cos(theta_n) ,  i Z_n sin(theta_n) ] ,
           [ i sin(theta_n)/Z_n ,  cos(theta_n) ] ]        det = 1 exactly, A,D real, B,C imaginary
```

**The electrical length — two readings, one frozen primary, one swept.**

```
E1 (PRIMARY, radial-delay-consistent):  theta_n = omega * l_node / v(r_n) = (omega/omega_C) / S_n^p
E2 (SWEPT,  band-top-consistent):       theta_n = pi * omega / omega_max(r_n) = pi (omega/omega_C) / (beta S_n^p)
```

**`E1` is frozen PRIMARY for one stated reason and it is not aesthetic:** under `E1` the section's own group delay is `dθ_n/dω = ℓ_node/v(r_n)`, which is **exactly Part 1's certified per-node delay**, so the Y8 phase slope must reproduce the Part 1 node sum — that is the cross-part control `G-XTIE`, and it exists only under `E1`. `E2` sets the section's half-wave resonance exactly at the frozen band top instead; the two differ by the factor `β/π`, which is the `1/√3` network-velocity projection at the lower bracket end. Frozen: `E1 and E2 differ by the ratio beta/pi and the difference is the disclosed 1D-radial-reduction ambiguity of section 0.1 item 1; E1 is PRIMARY because it alone admits the cross-part control G-XTIE, E2 is swept at both bracket ends, and neither is claimed to settle the 3D-srs correction which section 1.3 Z5 fences out`.

**★ A structural consequence, derived at freeze so it is not reported as a discovery.** Under `E1`, `θ_n` does **not** contain `β`. Frozen: `under the PRIMARY E1 reading the near-wall two-port is BETA-INDEPENDENT and beta enters Y8 ONLY through the depletion-edge location and hence through W; "achromatic across the bracket" is therefore AUTOMATIC for the E1 two-port and is a non-result there, and the bracket sensitivity of Gamma_in is measured on the E2 variant where it is real; the result doc must state this rather than present E1's bracket-independence as a finding`.

### §2Y.6 ★ WHY ANY MEASURED REFLECTION IS DISCRETENESS CONTENT — derived at freeze

The near-wall continuum equation of §2Y.4 is an **exact Euler equation**, and `x^{s_+}` and `x^{s_-}` are **exact, uncoupled** solutions of it. **A wave launched inward on one exponent stays on it: the continuum near-wall taper reflects NOTHING.** Frozen: `the RHO-B near-wall region is EXACTLY reflectionless in the continuum, because its reduced equation is an Euler equation whose two solutions are exact; therefore any non-zero |Gamma_in| this lane measures under the MATCHED contact is generated by LATTICE DISCRETENESS alone and by nothing in the profile, and the result doc must report it as such rather than as a taper reflection`.

**Two corollaries frozen with it.** (i) A WKB or first-Born estimate of this reflection is **invalid** here — the WKB parameter `|dλ/dr| = 4π/Ω ≈ 6.8` at the reference band centre, far from adiabatic — which is an independent reason the ruling's "no WKB" is right and not merely conservative. (ii) The per-cell discreteness error scales as `O(θ_n · δZ_n/Z_n) = O(Ω/(4n²))`, which is **summable**, so the measured reflection is expected to CONVERGE in the window size `K`; **that expectation is not assumed, it is the gate `G-KWIN`, and a failure of it is an honest finding rather than an instrument defect.**

### §2Y.7 ★ THE NEAR-WALL TWO-PORT IS MASS-FREE — derived at freeze

Near the wall `S_n² ≈ 2(n−1+θ)ℓ_node/r_sat`, so with `Ω = ω r_sat/c₀`

```
theta_n (E1, p = 2)  =  (omega/omega_C) / S_n^2  =  Omega / ( 2 (n - 1 + theta) )        <- no mass
z_n == Z_n/Z_1       =  (S_n/S_1)^(1-p) = ( theta/(n-1+theta) )^{1/2}   under RHO-B      <- no mass
```

**Every ingredient of the near-wall cascade — per-cell phase, per-cell impedance ratio, per-cell reflection `ρ_n` — is a function of `(Ω, θ, n)` alone.** Frozen: `the RHO-B near-wall two-port is MASS-FREE to relative order l_node/r_sat, derived at freeze from the near-wall expansion, and the claim is TESTED rather than asserted by running the full Y8 chain at three masses on the frozen grid and gating the spread of |Gamma_in| (gate G-MFREE); a failure of that gate would mean the near-wall expansion is not the regime the instrument is in`.

### §2Y.8 ★ THE COMPOSITE `Γ_in` — the Schur recursion, exact and unit-disc-preserving

`Γ` is propagated outward from the contact, always referenced to the **local** cell impedance. Traversing cell `n` multiplies by `e^{−2iθ_n}`; stepping from cell `n` to cell `n+1` applies the Möbius map of the impedance step:

```
rho_n = ( z_n - z_{n+1} ) / ( z_n + z_{n+1} )
Gamma <- Gamma * exp(-2 i theta_n)                     traverse cell n, reference z_n
Gamma <- ( rho_n + Gamma ) / ( 1 + rho_n * Gamma )     re-reference to z_{n+1}
```

**This is algebraically identical to the `ABCD` product** — each step is the Möbius action of the corresponding `2×2` matrix — and it is used because it is **exact for `Γ_L = ±1`** (where the impedance is `0` or `∞` and the `ABCD` route divides by zero) and because **every step is a Möbius map of the closed unit disc onto itself**, so `|Γ| ≤ 1` is preserved structurally and float64 error cannot amplify. Frozen: `Gamma_in is computed by the Schur/Mobius recursion above, which is exact for the |Gamma_L| = 1 terminations, and the explicit ABCD product is computed SEPARATELY for the DEPLETED cells only, where W is small, and is reported entrywise as the ruling requires; the two routes are cross-checked on the depleted section (gate G-ABCD) so the recursion is not trusted on its own`.

**The three frozen far-contact readings** (§0.2, `FLAG-CAUSAL`, swept and not resolved):

| tag | physical content | `Γ_L` |
|---|---|---|
| **`CONTACT-PORT`** | the ROW-IN reading: purely ingoing at the wall, nothing returns from a termination of infinite electrical length; the Ax-3-licensed mirror of the port at infinity | `0` |
| **`CONTACT-FREE`** | the lattice stops; node 1 has no inward neighbour, so its traction is unopposed (traction-free) | `−1` |
| **`CONTACT-CLAMPED`** | the Regime-IV interior does not move; node 1's velocity is pinned | `+1` |

**And the reason the matched reading is the measurement.** Because the ladder is lossless, `|Γ_in| = 1` **exactly** for both mirror readings, at every plane and every frequency (gate `G-UNIT`) — they carry information in their **phase** only. **`|Γ_in|` under `CONTACT-PORT` is therefore the clean, isolated measurement of what the ladder itself reflects**, and it is the quantity the reach-through bins are decided on. Frozen: `the reach-through bins are decided on |Gamma_in| under the MATCHED CONTACT-PORT reading, because the two mirror readings return |Gamma_in| = 1 identically by losslessness and carry their content in phase alone; the mirror readings are nonetheless computed and reported in full, and their PHASE SLOPE is the achromaticity measurement`.

### §2Y.9 ★ `|T|²`, the phase slope, and the ripple period — all three derived at freeze

**Transmission through the depleted section.** The section is lossless and its load is matched, so

```
|T|^2 = 1 - |Gamma_in|^2                    (the reach-through transmission)
W = 0  =>  junction two-port = 2x2 IDENTITY exactly  =>  |T|^2 = 1 exactly
```

**Phase slope — and the one place a careless derivation would have over-claimed, corrected HERE at freeze rather than at result.** The composite map is a product of **ω-INDEPENDENT** impedance-step Möbius maps (`ρ_n` contains no `ω`) and **ω-DEPENDENT** per-cell phase rotations `e^{−2iθ_n}` with `θ_n ∝ ω` exactly (that is `G-DISP`). **The two do not commute**, so `φ_Γ(ω)` is NOT `φ_L − 2Σθ_n(ω)` and its slope is NOT a pure transit delay. Two consequences, both derived at freeze:

```
(i)  steps OFF (rho_n == 0):  phi_Gamma = phi_L - 2 SUM_n theta_n(omega)     EXACTLY
     =>  -d(phi_Gamma)/d(omega) = 2 SUM_n l_node/v(r_n)                      EXACTLY
     =   the Part 1 node-sum ROUND-TRIP delay over the same K cells          <- gate G-XTIE
(ii) steps ON:   D(omega) == -d(phi_Gamma)/d(omega)  is a REFLECTION GROUP DELAY,
     not a transit delay; its excess over the transit delay, and its variation
     across the band, are generated ENTIRELY by the impedance staircase.
```

Frozen: `the cross-part control G-XTIE is stated with the impedance steps SWITCHED OFF, where the mirror phase slope is EXACTLY minus the Part 1 node-sum round-trip delay over the same window; with the steps ON the phase slope is a reflection group delay whose excess over the transit delay is a MEASUREMENT, and this lane does NOT claim that the reflection phase is exactly achromatic — v1's achromaticity statement was about the TRANSIT delay and is not silently promoted here to a statement about the reflection phase`.

**★ AND THIS IS HOW Y8 UPDATES v1's CHIRP QUESTION, QUANTITATIVELY.** v1 §2.7 derived that **if** the band edge governed, the delay would chirp at exactly `dT/d ln ω = −r_sat/c₀`. v1 then found the node governs, so no chirp from that mechanism. **Y8 replaces the inequality with a measured dispersion**: define

```
D(omega) = -d(phi_Gamma)/d(omega)                        the round-trip reflection group delay
CHIRP-MEASURE = max over the frozen band of | dD/d(ln omega) |,  in units of r_sat/c_0
```

and report `CHIRP-MEASURE` against v1's derived band-governed value, which is `1` in those units. Frozen: `CHIRP-MEASURE is a REPORTED quantity and not a bin; it is reported for both mirror contact readings, at both theta, on E1 and E2, and it is presented as an UPDATE to the chirp question of v1 section 2.7 BY CROSS-REFERENCE to that section, with v1's derived band-governed slope quoted as the comparison scale and v1's own numbers NOT restated`.

**Ripple period.** Two reflectors separated by a one-way phase `Φ(ω)` beat with period `Δω = π/(dΦ/dω)`. Over the frozen window, using the digamma sum of §2P.1,

```
Phi(Omega) = SUM_{n=1..K} theta_n = (Omega/2) [ psi(K + theta) - psi(theta) ]
d(Phi)/d(Omega) = (1/2) [ psi(K + theta) - psi(theta) ]
Delta_Omega_ripple = pi / ( d(Phi)/d(Omega) )      and   Delta_omega = Delta_Omega * c_0 / r_sat
```

Frozen: `the ripple period is DERIVED in closed form at freeze from the digamma sum, is reported in Omega and in rad/s whatever the bin outcome, and is used to SIZE the band sampling in section 4Y.2 rather than being read off a computed curve`.

### §2Y.10 The RHO-A side, stated explicitly as the brief requires

Under RHO-A, `S_dep = ε²` while `S_1 = √(2θℓ_node/r_sat)`, so

```
S_dep^2 / S_1^2 = Omega^2 * l_node / ( 2 theta beta^2 r_sat )   ~ 1e-19  at every mass
```

— the edge is inside the last cell by **nineteen orders in `S²`** (v1 measured the corresponding `S` ratio at `~1e-26`). Frozen: `under RHO-A no cell is depleted at any point of the frozen band, at either bracket end, at either theta and at any mass on the frozen grid, so the junction two-port is the identity, |T|^2 = 1 exactly, and the reach-through question is MOOT; this is VERIFIED and RECORDED as bin BIN-RHOA-MOOT rather than assumed, and v1's twenty-five-orders statement is cross-referenced rather than restated with new values`.

---

## §3 — IMPORT LEDGER (every number the instrument consumes, tagged; `substrate-first-for-numbers`)

**v1's ledger `J1`–`J16` is carried forward BYTE-IDENTICAL and is not restated here; it is incorporated by reference from `research/2026-08-04_echo-delay-regulated-sum_prereg-FROZEN.md` §3.** Only the entries that are NEW in v2, or whose ROLE changes in v2, are listed.

| # | Input | Value / form | Class | Source (verified two-method at this freeze) |
|---|---|---|---|---|
| **V1 ★** | **v1's shipped results object** | every certified CFG-A value and every CFG-B diagnostic, read **PROGRAMMATICALLY** from `research/drivers/echo_delay_regulated_sum_results.json` | **`[IN-REPO PRIOR-LANE RESULT — used ONLY as the NEGATIVE-CONTROL TARGET of G-NC-V1A / G-NC-V1B; never as a tolerance, never as a bin boundary, never as a seed]`** | v1 shipped JSON |
| **V2 ★** | **The frozen band** | `[Ω_R − Ω_I, Ω_R + Ω_I]`, both endpoints read **PROGRAMMATICALLY** from `certified_root/Omega_re_mp` and `certified_root/Omega_im_mp` | **`[IN-REPO CERTIFIED PRIOR-LANE RESULT — a BAND DEFINITION, i.e. a frequency SCALE; it is NOT a tolerance and NOT a bin boundary]`** | v2.4 shipped JSON; cross-checked against `adjudication/omega_I_M_g × x_sat` by `G-BAND` |
| **V3 ★** | **The far-contact condition** | `Γ_L ∈ {0, −1, +1}` — matched port / free end / clamped end | **`[FORKED — FLAG-CAUSAL, OPEN, GRANT'S; SWEPT at all three, NOT resolved]`** | §2Y.4 (derived: the continuum does not select), §2Y.8 |
| **V4** | Local characteristic impedance | `Z(r) = ρ_bulk c₀ S^{1−p}` | **`[DERIVED here in one line from μ = G_vac S and v = c₀S^p; reproduces the axial lane's two-method Z_shear = 1/S under RHO-B]`** | §2Y.5 |
| **V5** | Per-cell electrical length | `E1` (radial-delay-consistent) PRIMARY; `E2` (band-top-consistent) SWEPT | **`[ENG-CHOICE — the disclosed 1D-radial-reduction ambiguity; E1 chosen because it alone admits G-XTIE]`** | §2Y.5 |
| **V6** | Cell impedance placement | node-uniform PRIMARY; bond-midpoint swept as `Y-MID` | **`[ENG-CHOICE — the §0.1 item 8 open checkpoint; NEITHER PREFERRED]`** | §0.1, §4Y.4 |
| **V7** | Band-top coefficient | `β ∈ {5.4414, 17.0111} ω_C` | **`BRACKETED(pending-ruling)`** — ★ *the pilot-2 proposed tag, exercised here* | `srs-band-structure.md` §3 |
| **V8** | Y8 instrument numerics | `K ∈ {1e4, 1e5, 1e6}`, `N_band = 65`, the mutation sizes of §6 | **`[ENGINEERING CHOICE — tagged, frozen in §4Y.2, each with its derivation]`** | this lane |

**R8 audit rule (frozen), extended for the register.** `every number the instrument consumes appears on this ledger or on v1's; no SM/GR convention default enters anywhere, and in particular no Regge-Wheeler potential, no Zerilli potential, no tortoise coordinate, no Planck length, no ECO wall-offset parameter, AND — new in v2 because the register invites them — no semiconductor material parameter of any kind: no permittivity, no doping density, no built-in potential, no Debye length, no depletion-approximation width law and no junction capacitance is used as an input, a seed, a comparator or a check`.

**★ Ledger discipline note, restated at freeze.** `V1 and V2 are prior-lane values used ONLY as negative-control targets and as a band definition. Frozen: no gate tolerance and no bin boundary in this lane is set from any prior-lane MEASURED value; every tolerance is derived in section 4.5 or 4Y.5 from the arithmetic of the method, and every bin boundary is derived in section 7 from the structure of the quantity it bins`.

---

## §4 — THE METHOD AND ITS FROZEN NUMERICS

### §4.1 PART 1 method — v1's, unchanged except for the two repairs

Steps 1–8 of v1 §4.1 are carried forward **byte-identical**: closed forms first (`𝒥(p)` in mpmath, `artanh` in mpmath), then the regulated node sum with an exact integral tail, then the turning point, then the barrier peak, then the regulator sweep, then the self-tests, then one JSON run twice. **The only changes are (a) `G-DISC` compares against `[ln θ − ψ(θ)]/2` computed from mpmath's digamma instead of against a transcribed `γ`, (b) `G-DECADE` acquires its two frozen limbs, and (c) two new negative-control gates read v1's shipped JSON.** Frozen: `no method element of v1 section 4.1 is altered, no code path is restructured in a way that could change a float64 summation order, and the negative controls G-NC-V1A and G-NC-V1B exist precisely to detect it if one is`.

### §4.2 PART 1 frozen numerics — **identical to v1 §4.2, restated for auditability**

| symbol | value | role |
|---|---|---|
| `p` | `{0.5, 2.0}` primary; `3.0` synthetic self-test only | branch exponent |
| `theta` | `{1.0, 0.5}` | sub-cell placement of the innermost node |
| `beta` | `{5.4414, 17.0111}` | band-top coefficient in `ω_C`, both bracket ends |
| `N_split` | `{1e5, 1e6, 1e7}`, primary `1e6` | exact-sum / integral-tail split |
| `dps` | `50` | mpmath working precision |
| `quad tol` | `1e-30` | mpmath quadrature target |
| mass grid | `M/M_⊙ ∈ {1, 10, 62, 100}`, `M_ref = 62` | reporting grid |
| `ell` | `2` | multipole (barrier only) |
| `A_peak bracket` | `(0.05, 0.999)` | barrier-peak search bracket |

### §4Y.2 PART 2 frozen numerics — **new, each with its derivation**

| symbol | value | derivation of the value |
|---|---|---|
| `K` (window, cells) | `{1e4, 1e5, 1e6}`, **primary `1e6`** | the window must span enough decades of `S` for the log law's skin content to be represented and few enough cells to be enumerated exactly. `1e6` cells span `S ∈ [S_1, 10³S_1]`, i.e. **three decades of `S`**, carrying `3 ln 10 = 6.9` radians of the one-way `≈ 21` at the reference mass. `1e4` and `1e5` are the convergence ladder for `G-KWIN`. |
| `N_band` | `65` | the derived ripple period is `ΔΩ = π/[(1/2)(ψ(K+θ) − ψ(θ))]`; at `K = 1e6, θ = 1` that is `π/7.196 = 0.4366`, and the band width is `2Ω_I ≈ 2.01`, i.e. **≈ 4.6 ripple periods across the band**. `65` points give `64` intervals, i.e. **≈ 13.9 samples per derived ripple period** — comfortably above the `8` needed to resolve a ripple and its period. **Sized from the derived period, not from a computed curve.** |
| `Gamma_L` | `{0, −1, +1}` | the three frozen far-contact readings (§2Y.8) |
| electrical length | `E1` primary, `E2` swept | §2Y.5 |
| `G-MFREE` masses | `{1, 62, 100} M_⊙` | the extremes and the reference of the frozen grid; a `100×` mass lever on a quantity derived to be mass-free |
| `Y8` reference mass | `62 M_⊙` | `M_ref`, unchanged |
| mutation sizes | `z ratio ∈ {1.01, 3, 1000}` for the three synthetic-ladder self-tests | chosen so the exact single-step reflections `ρ = (1−f)/(1+f)` land at `−0.004975`, `−0.5` and `−0.998`, i.e. **one strictly inside each of the three frozen `BIN-RT` bands**, so each bin is demonstrated reachable **exactly** rather than probabilistically |

### §4Y.4 ★ THE Y8 VARIANT SET — frozen BEFORE any number

| id | variant | what it perturbs |
|---|---|---|
| **`Y-NODE`** | cell impedance uniform per cell, stepping at cell boundaries | **the primary** |
| **`Y-MID`** | cell impedance evaluated at the bond midpoint `x_n + ℓ/2` | the §0.1 item 8 open checkpoint — **changes the innermost step, which is where the reflection is generated** |
| **`Y-E2`** | the band-top-consistent electrical length | the 1D-reduction ambiguity, and the ONLY place the bracket enters the two-port |
| **`Y-PITCH`** | innermost node at `2ℓ_node` (v1's `R4` strained-pitch reading) | `FLAG-PITCH`, swept, settled nowhere |
| **`Y-THETA`** | `θ = 1/2` | sub-cell placement, carried from v1 |

Frozen: `BIN-RT is decided on the FULL variant set {Y-NODE, Y-MID, Y-E2, Y-PITCH, Y-THETA} crossed with both bracket ends and the full frozen band, and no variant may be dropped, re-weighted or excluded after a number is seen`.

### §4Y.5 ★ WHERE EVERY NEW TOLERANCE COMES FROM — derived, with ZERO pre-freeze computation on the Y8 instrument

| gate | tolerance | derivation of the number |
|---|---|---|
| `G-DISC` | **`1 %`, CARRIED UNCHANGED from v1** | only the LAW was wrong; the tolerance was never at issue and is not touched |
| `G-DECADE(a)` | `1e-4` | derived worst-case deviation `0.99·(1e-2)²/(4 ln 10) = 1.0748788e-5`; **`9.30×` headroom**, and still `4` orders below the `O(1)` deviation a wrong power law gives |
| `G-DECADE(b)` | `1e-3` | the next-order term enters the residual ratio as `(3/8)S_hi²`, worst `3.75e-5`; **`26.7×` headroom** |
| `G-NC-V1A` / `G-NC-V1B` | **exact string equality** at v1's 17-significant-digit rendering | there is nothing to size: the same arithmetic on the same machine must give the same digits, and any difference is information |
| `G-BAND` | `1e-15` relative | two renderings of ONE shipped quantity; anything above double-precision round-off means the shipped JSON's own fields disagree |
| `G-DEP` | exact integer equality | `W` is an integer count; two methods either agree or do not |
| `G-ABCD` | `1e-14` on `\|det − 1\|` and on the losslessness/reciprocity structure; `1e-12` on `ABCD`-route vs Schur-route `Γ` over the depleted section | `det = 1` and `A, D` real / `B, C` imaginary are exact identities of the frozen per-cell form, so only float64 round-off remains (`~1e-16` per entry); `1e-14` is `100×` headroom, and the two-route comparison inherits the same floor over a short product |
| `G-UNIT` | `1e-12` on `\|\|Γ_in\| − 1\|` | the Schur recursion composes `10⁶` unit-disc Möbius maps; each contributes `~1e-16` of modulus round-off and the accumulation is at worst a random walk, `√(1e6)·1e-16 = 1e-13`; **`10×` headroom** |
| `G-PREC` | `1e-12` on `\|Γ_float64 − Γ_mpmath\|` at `K = 1e4` | the same walk at `K = 1e4` gives `1e-14`; **`100×` headroom**, and mpmath at `dps = 50` is exact by comparison |
| `G-KWIN` | `1e-3` **absolute** on the spread of `\|Γ_in\|` over `K ∈ {1e4, 1e5, 1e6}` | §2Y.6 derives the residual from cells beyond `K` as `O(Ω/(4K))`, which at the coarsest rung `K = 1e4` is `4.6e-5`; **`21.6×` headroom** |
| `G-XTIE` | `1e-10` relative | with the impedance steps off the mirror phase is EXACTLY linear in `ω`, so the central-difference truncation error is identically zero and only round-off on a `~0.45` rad increment remains (`~2e-15`); **`5` orders of headroom** |
| `G-MFREE` | `1e-6` on the spread of `\|Γ_in\|` across the three masses | the mass dependence enters at relative `O(x/r_sat) = O(Kℓ_node/r_sat) = 6.0e-13` at the primary window; **`6` orders of headroom** |

### §4.6 Determinism

Frozen: `the driver is run twice end-to-end and the shipped JSON must be byte-identical apart from _runtime_sec; the driver emits NO pass field for the determinism gate — it ships the digest only, and the verdict is obtained solely by the external two-run diff recorded in the result doc; _runtime_sec is machine-dependent and is written WITHOUT back-ticks and is NOT registered in the number check`.

### §4.7 ★ PRE-FREEZE COMPUTATION DISCLOSURE

Frozen: `the ONLY arithmetic performed before this document was frozen is (i) the symbolic algebra of sections 2P and 2Y, and (ii) an mpmath evaluation of the two ANALYTIC correction laws of sections 2P.1 and 2P.2 for the sole purpose of SIZING the G-DECADE tolerances with stated headroom, which the brief explicitly directs. NOTHING of the Y8 instrument was run, prototyped, estimated or looked at: no per-cell ABCD was formed, no Schur recursion was stepped, no Gamma_in was computed, no depletion width was counted, and no band point was evaluated. The risk is disclosed and accepted: a tolerance derived rather than scouted can be wrong, and if it is, the gate FAILS and the configuration is reported NOT-CERTIFIED. It will not be retuned.`

---

## §5 — THE GATES (frozen; an UNRUN gate is NOT a passed gate)

### §5.1 PART 1 — carried from v1 unchanged

| gate | scope | frozen tolerance | change from v1 |
|---|---|---|---|
| **G-NC** | CFG-A | `1e-10` rel, every predecessor `r_out` entry | **none** |
| **G-JA** | CFG-A | `1e-20` | **none** |
| **G-CF** | CFG-B | `1e-25` | **none** |
| **G-SUM** | both | `1e-12` rel | **none** |
| **G-U** | both | `1e-30` | **none** |
| **G-DISP** | both | `1e-15` | **none** |
| **G-PEAK** | both | booleans | **none** |
| **G-CANON** | both | machine / exact | **none** |

### §5.2 PART 1 — the two repairs and the two new negative controls

| gate | what it certifies | frozen tolerance |
|---|---|---|
| **G-DISC** ★ | the measured **one-way** discrete-minus-continuum offset equals `K_disc(θ) = [ln θ − ψ(θ)]/2`, evaluated from mpmath's digamma, at both frozen `θ` | `1 %` — **UNCHANGED** |
| **G-DECADE(a)** ★ | each decade of `S` contributes `ln 10 · (r_sat/c₀)` | `1e-4` — **RESIZED from the derived `O(S²)` law, `9.30×` headroom** |
| **G-DECADE(b)** ★ | the decade RESIDUAL matches the derived `0.99·S_hi²/(4 ln 10)` **shape** | `1e-3` — **NEW, strictly strengthening** |
| **G-NC-V1A** ★★ | every certified v1 CFG-A value reproduces to **exact string equality** at 17 significant digits | exact |
| **G-NC-V1B** ★★ | every v1 CFG-B diagnostic reproduces to **exact string equality** at 17 significant digits | exact |

### §5.3 PART 2 — Y8's own gates

| gate | what it certifies | frozen tolerance |
|---|---|---|
| **G-BAND** | the frozen band's `Ω_I` read two ways from the v2.4 JSON agrees | `1e-15` rel |
| **G-DEP** | `W` by exact inversion equals `W` by direct node-by-node count, at every band point, both `β`, both `θ` | exact integers |
| **G-ABCD** | the per-cell `ABCD` has `det = 1`, `A, D` real, `B, C` imaginary; and the `ABCD`-route `Γ` equals the Schur-route `Γ` over the depleted section | `1e-14` / `1e-12` |
| **G-UNIT** ★ | `\|Γ_in\| = 1` **exactly** for both mirror contacts, at every band point and every window — the Ax-3 losslessness receipt | `1e-12` |
| **G-PREC** | the float64 Schur recursion equals an mpmath `dps = 50` recursion at `K = 1e4` | `1e-12` |
| **G-KWIN** | `\|Γ_in\|` under the matched contact is window-independent over `K ∈ {1e4, 1e5, 1e6}` | `1e-3` abs |
| **G-XTIE** ★★ | **CROSS-PART CONTROL** — with the impedance steps switched off, the mirror phase slope equals minus the PART 1 node-sum round-trip delay over the same `K` cells | `1e-10` rel |
| **G-MFREE** | `\|Γ_in\|` is mass-free across `{1, 62, 100} M_⊙` | `1e-6` |

**Frozen:** `a gate that was never run cannot be counted as passed; the result doc must publish a RUN / N-A-BY-CONSTRUCTION / N-A-BY-OUTCOME / UNRUN-BY-OMISSION table per configuration, for BOTH parts`.

---

## §6 — THE FIREABILITY SELF-TESTS (each MUST fire; a gate that cannot fail is not a gate)

### §6.1 PART 1 — v1's twelve, carried BYTE-IDENTICAL

`FT-NC`, `FT-JA`, `FT-CF`, `FT-SUM`, `FT-U`, `FT-DISP`, `FT-PEAK`, `FT-DECADE`, `FT-CUT`, `FT-EVAN`, `FT-TURN`, `FT-CANON` — mutations and thresholds exactly as v1 §6. **`FT-DECADE` now fires if EITHER `G-DECADE` limb fails, and its frozen threshold on limb (a) is unchanged at `≥ 0.1`.**

### §6.2 NEW self-tests

| self-test | mutation | must fire when |
|---|---|---|
| **FT-DISC** ★ | scale the derived `K_disc(θ)` by `1 + 0.02` | `G-DISC` fails, separation `≥ 0.02` against the frozen `1 %` |
| **FT-V1** ★★ | scale one v1-JSON comparison target by `1 + 1e-12` | `G-NC-V1A` fails — **the negative controls are demonstrated fireable every run** |
| **FT-W** ★ | multiply `ω` by `1e3` at the reference mass | `W ≥ 1` at both bracket ends, i.e. **`BIN-W-THIN`/`BIN-W-THICK` demonstrated reachable, and the non-trivial junction `ABCD` product is exercised** |
| **FT-RT-C** ★ | run the frozen `Γ_in` chain and the `BIN-RT` classifier on a **2-cell synthetic ladder** with impedance ratio `1.01`, matched contact | `\|Γ_in\| = 0.004975…` and the classifier returns `CONTACT-GOVERNED` |
| **FT-RT-I** ★ | the same on a ratio-`3` ladder | `\|Γ_in\| = 0.5` and the classifier returns `INTERFERENCE` |
| **FT-RT-E** ★ | the same on a ratio-`1000` ladder | `\|Γ_in\| = 0.998…` and the classifier returns `EDGE-GOVERNED` |
| **FT-UNIT** | give one cell a complex impedance `Z_n(1 + 0.01i)` | `G-UNIT` fails, `\|\|Γ_in\|−1\| ≥ 1e-3` |
| **FT-XTIE** | scale the node-sum comparison target by `1 + 1e-6` | `G-XTIE` fails, separation `≥ 1e-7` |
| **FT-DEP** | add `1` to the closed-form `W` | `G-DEP` fails |

**★ Why the three `FT-RT-*` tests are built as synthetic two-cell ladders rather than as perturbations of the real cascade.** A single impedance step of ratio `f` into a matched load gives `Γ_in = (1−f)/(1+f)` **exactly**, so the three frozen ratios land at `−0.004975`, `−0.5` and `−0.998` — **one strictly inside each frozen `BIN-RT` band, deterministically, on every machine and every run.** They exercise the real recursion and the real classifier. Frozen: `each of the three BIN-RT outcomes is demonstrated reachable EVERY RUN by an exact synthetic ladder whose reflection is known in closed form; no BIN-RT outcome is reachable only in principle`.

**Frozen:** `every self-test above MUST fire; if any self-test fails to fire, the affected configuration is NOT-CERTIFIED, NO threshold is retuned, and the physics bins for that configuration are reported N/A - NOT ADJUDICATED`.

---

## §7 — THE OUTCOME CLASSES (frozen; exhaustive; each reachable)

### §7.0 Certification, and the two precedence chains

**PART 1 precedence, carried byte-identical from v1:** `BIN-EVAN` > `BIN-CUTOFF` > `BIN-DA` / `BIN-DB` > `BIN-DISC` / `BIN-DEGEN`. Certification (`DELAY-CERTIFIED` / `DELAY-NOT-CERTIFIED`) is stated **per configuration** and gates every Part 1 bin.

**PART 2 precedence, new:** `BIN-STOP-V1` > `BIN-W` > `BIN-RT`. Y8 carries its own certification token `Y8-CERTIFIED` / `Y8-NOT-CERTIFIED` on the §5.3 gates and the §6.2 self-tests.

**★ AND THE CROSS-PART GATING, FROZEN.** `Y8's bins are additionally gated on CFG-B being DELAY-CERTIFIED in PART 1: Y8 computes on the same RHO-B profile and its own cross-part control G-XTIE ties its phase bookkeeping to PART 1's node sum, so a DELAY-NOT-CERTIFIED CFG-B makes every Y8 bin a NOT-ADJUDICATED DIAGNOSTIC regardless of Y8's own gates`.

| bin | condition | disposition |
|---|---|---|
| **`BIN-STOP-V1`** ★★ | `G-NC-V1A or G-NC-V1B fails` | **THE LANE STOPS.** The moved value is reported with both renderings and flagged; **no bin in either part is adjudicated.** |
| **`BIN-STOP`** | `CFG-A fails G-NC against the 2026-06-17 predecessor driver` | **THE LANE STOPS**, as v1. |
| **`BIN-CERT-FAIL`** | `any RUN gate FAILS, or any self-test fails to fire, or any gate is UNRUN by omission, for that configuration` | **`DELAY-NOT-CERTIFIED`** / **`Y8-NOT-CERTIFIED`** for that configuration; numbers reported as diagnostics; no bin adjudicated; **no threshold retuned**; routes to a successor with a new version number. |

### §7.1 PART 1 bins — carried from v1 BYTE-IDENTICAL

`BIN-EVAN` (§7.1), `BIN-CUTOFF` (§7.2), `BIN-DA` (§7.3), `BIN-DB` (§7.4), `BIN-DISC` / `BIN-DEGEN` (§7.5) and the §7.5b observational-pointer DIAGNOSTIC are carried forward **with their frozen criteria and thresholds byte-identical to v1** and are incorporated by reference. Frozen: `not one PART 1 bin boundary, sub-bin criterion or threshold is changed from v1; the referential integrity of the v2 result to v1's bins is discharged by the result doc quoting v1's frozen criterion strings verbatim at every adjudication site`.

### §7Y.1 `BIN-W` — is any cell depleted?

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-W-ZERO`** | `W = 0 at EVERY point of the frozen band, at BOTH beta ends, at BOTH theta values, and under every variant of section 4Y.4` |
| **`BIN-W-THIN`** | `1 <= max W <= 10 somewhere on that set` |
| **`BIN-W-THICK`** | `max W > 10 somewhere on that set` |

**Frozen disposition:** `if BIN-W-ZERO fires, the junction two-port is the 2x2 IDENTITY EXACTLY, |T|^2 through the depleted section is 1 EXACTLY, the depletion edge lies inside the innermost intact cell, and the reach-through limit is reached not approximately but exactly; the result doc must report the MARGIN as the ratio of the band top to the derived crossing frequency Omega = 2*theta*beta, because a verdict that holds by a factor of two is reported as holding by a factor of two`.

### §7Y.2 `BIN-RT` — the reach-through verdict

`R ≡ |Γ_in|` at the primary window `K = 1e6` under the **matched** far contact (`CONTACT-PORT`), evaluated over the frozen band × both `β` × both `θ` × the full §4Y.4 variant set.

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-RT-CONTACT`** | `max R < 0.10` — **CONTACT-GOVERNED**: the composite reflection is dominated by the far contact |
| **`BIN-RT-EDGE`** | `min R > 0.90` — **EDGE-GOVERNED**: the depletion-edge / near-wall section dominates |
| **`BIN-RT-INTERFERENCE`** | `neither, i.e. R lands in [0.10, 0.90] somewhere on that set` — **comparable contributions** |

**The thresholds, derived before any number.** `|Γ| = 0.10` is `1 %` reflected power, i.e. a **`−20 dB` return loss** — the standard engineering statement that a section is transparent and its termination governs. `|Γ| = 0.90` is `81 %` reflected power, i.e. the section is the dominant reflector and screens its termination. **Both are engineering conventions with a stated power meaning, frozen here before any number exists, and each is demonstrated reachable every run by an exact synthetic ladder (§6.2).**

**Frozen reporting requirements, all three mandatory whatever the bin:**
1. `the ripple period is reported in Omega and in rad/s at the primary window, computed from the derived digamma closed form, whatever the bin`;
2. `CHIRP-MEASURE is reported for both mirror contact readings and compared BY CROSS-REFERENCE to v1 section 2.7's derived band-governed slope, without restating v1's values`;
3. `the three-way spread of Gamma_in across the frozen far-contact readings is reported, because it IS the quantitative statement of how much the unresolved FLAG-CAUSAL fork costs the observable, and that is the honest deliverable of a lane that sweeps a fork rather than resolving it`.

### §7Y.3 `BIN-RHOA-MOOT` — the RHO-A side, stated explicitly

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-RHOA-MOOT`** | `under RHO-A, W = 0 at every band point, both beta ends, both theta values and every mass on the frozen grid` ⇒ **no cell is depleted before the end; the reach-through question is MOOT** |
| **`BIN-RHOA-LIVE`** | `W >= 1 anywhere on that set` ⇒ the RHO-A branch would have a live reach-through question and the lane must compute it |

### §7Y.4 Reachability audit (frozen)

- `BIN-STOP-V1` is reachable and is **demonstrated reachable every run** by `FT-V1`.
- `BIN-CERT-FAIL` is reachable and is **demonstrated reachable every run**: every self-test drives an actual gate into its failing state.
- `BIN-W-THIN` / `BIN-W-THICK` are reachable and are **demonstrated reachable every run** by `FT-W`.
- `BIN-RT-CONTACT`, `BIN-RT-INTERFERENCE` and `BIN-RT-EDGE` are **each demonstrated reachable every run** by `FT-RT-C`, `FT-RT-I`, `FT-RT-E`, with the exact closed-form reflection of a single impedance step.
- `BIN-RHOA-LIVE` is reachable: it is an inequality on a computed ratio.
- **No outcome requires a criterion to be relaxed after the fact.**

### §7Y.5 ★ PREDICTABILITY DISCLOSURE — what this lane knows in advance, stated without flattery

- **Known at freeze, as THEOREMS of §2P and §2Y:** `K_disc(θ) = [ln θ − ψ(θ)]/2`; the decade law `0.99 S_hi²/(4 ln 10)`; the exact near-wall Euler equation and its exponents `s± = [1 ± √(1/4 − Ω²)]/2`, hence the **continuum near-wall region reflects nothing**; the mass-freeness of the near-wall two-port; `W = ⌊Ω/(2β) + 1 − θ⌋`; the derived ripple period; the exact `G-XTIE` identity with the steps off; and the statement that under `E1` the two-port carries no `β`.
- **★ Evaluated BY HAND at freeze and DISCLOSED so the run is read as a check and not as a discovery:** `W ≥ 1` requires `Ω ≥ 2θβ`, and the frozen band's top is `Ω_R + Ω_I`, while the smallest `2θβ` on the frozen sweep is `2 × 0.5 × 5.4414 = 5.4414`. **Substituting the band endpoints by hand indicates `BIN-W-ZERO` at every sweep point, with a margin of roughly a factor of two in `Ω` at the closest corner.** The result doc must present the `W` verdict as a **CONFIRMED DERIVATION**, not as a measurement, and must report the margin.
- **NOT known at freeze, and these are the only Y8 outputs this lane may present as measurements:** the value of `|Γ_in|` under the matched contact and therefore the `BIN-RT` verdict; whether it converges in the window (`G-KWIN`); the three-way spread across the frozen contact readings; the excess reflection group delay and `CHIRP-MEASURE`; whether `Y-MID` moves the answer; and — for PART 1 — whether the two repaired gates now pass and whether v1's numbers reproduce exactly.

Frozen: `the derived statements of sections 2P and 2Y and the hand-evaluated W verdict are available before the run and may NOT be presented in the result doc as discoveries of the instrument; only the quantities enumerated in the third bullet of section 7Y.5 may be presented as measurements`.

---

## §8 — WHAT TRANSFERS, AND WHAT MUST BE RE-EARNED

**Transfers in:** the Ax-4 kernel; `A = r_sat/r`; `μ = G_vac S`; both inertia readings as a declared fork; the arccos band model and its `1/√3` calibration; `ℓ_node`, `ω_C`; v1's entire instrument, bins and variant set; v2.4's certified root as a frequency scale **and now as a band definition**; the axial lane's indicial structure **as a cross-check on a re-derivation, not as an import**.

**Must be re-earned by a successor and is NOT established here:** `Γ_in` at any plane outside the frozen near-wall window, hence any echo amplitude, visibility, count or train; the resolution of `FLAG-CAUSAL` (swept, not settled); the 3D-srs correction to the 1D radial cascade; whether the lattice pitch is strained; the single-scale-vs-stiffness-lifted band-top ruling; the node-vs-bond impedance placement (swept as `Y-MID`, settled nowhere); and any observational comparison beyond citing an in-repo pointer.

---

## §9 — FLAG-DON'T-FIX: what is raised at freeze and routed, not resolved

1. **★ `FLAG-ECO`, EXTENDED TO Y8 AND MANDATORY IN THE HEADLINE.** v1 froze that the RHO-B log-delay law is structurally degenerate with the ECO / near-horizon-firewall family. **Y8 extends the degeneracy rather than breaking it:** the ECO family carries a **free contact reflectivity**, so an ECO reproduces **any** `Γ_L` and therefore **any** `BIN-RT` outcome. Frozen: `the reach-through verdict is NOT an AVE-vs-ECO discriminator and the result headline must say so; the only structural difference remains that AVE's cutoff length is fixed where the ECO offset is a free knob, and Y8 adds a SECOND free knob on the ECO side rather than removing one`.
2. **★ `FLAG-CAUSAL`, SHARPENED AND STILL GRANT'S.** v1 made the electrical length finite; **v2 makes the cost of not answering it quantitative** (the three-way `Γ_in` spread). **Swept at `Γ_L ∈ {0, −1, +1}`; NOT resolved; no reading preferred.** → **Grant.**
3. **★ `FLAG-PLACEMENT` — NEW.** Is the graded impedance a **node** property (cell-uniform) or a **bond** property (midpoint)? The two differ only at the innermost cell and differ there by the full `√2` step — **exactly where the reflection is generated.** Swept as `Y-MID`; **neither preferred; the constitutive question is left open.** → **Grant / a successor.**
4. **★ `FLAG-REGISTER` — NEW, and it is a vocabulary flag rather than a physics one.** The semiconductor register's **depletion edge carries an evanescence connotation that does NOT hold on the adjudicated distributed cell model**, where the band top is a Bragg/half-wave resonance and the cascade never cuts off (§0.1 item 2). **This lane uses the ruled vocabulary and carves the connotation out explicitly at §0.4; it does not propose a vocabulary change.** → **the auditor lane, if the register is to be reused.**
5. **`FLAG-PITCH`** — swept as `R4` / `Y-PITCH`; settled nowhere.
6. **`FLAG-BRACKET`** — the vector band top is a bracket pending Grant; swept at both ends; the `BRACKETED(pending-ruling)` provenance tag is exercised (§0 row 5) as pilot feedback, **not** as a canonization.
7. **`FLAG-FREEZE-SIZING`** — carried forward from v1 as a lane-pattern for the orchestrator. **v2 is the test of whether the pattern is fixable by deriving gate constants twice: this lane derived both repaired laws independently and sized every new tolerance with a stated headroom factor.** Whether that is enough is a process question this lane raises and does not answer.
8. **`FLAG-ECO-COROLLARY`, `FLAG-PLANE-GAP`, `FLAG-CITE-SHIFT`, `FLAG-CANON`** — all carried forward from v1 and the axial lane **BY POINTER ONLY**, repaired nowhere, no edit proposed.

---

## §10 — VALIDATION REQUIREMENTS (frozen)

- **`make verify` passes** in the worktree before every commit.
- **Gating number check.** `research/drivers/echo_delay_v2_reach_through_number_check.py`, implementing from the first commit all seven accumulated checker lessons — **(i)** a minimum significant-digits floor of 3 enforced at BOTH ends; **(ii)** PER-SITE dedup; **(iii)** list-valued registration; **(iv)** a newline-excluding token pattern; **(v)** a completeness guard; **(vi)** a digest classifier; **(vii)** a **MUTATION RECEIPT** — **plus the span-splitting fix v1 added, so numerals written inside expressions are checked rather than skipped.** Frozen: `the gating number check scans the RESULT DOC only; no claim is made anywhere in this lane that this prereg is machine-checked; the checker ships a mutation receipt demonstrating that it can FAIL`.
- **Makefile target** `verify-echo-delay-v2-number-check`, appended as its OWN target and wired into `verify`; no other lane's recipe is edited. **DISCLOSED: the `.PHONY` line and the `verify:` prerequisite line ARE shared with every other lane's number-check target and are a REAL two-line union-conflict class with any concurrent lane, not an append-only merge.**
- **Determinism** per §4.6.
- **Engine fence.** `src/ave` byte-untouched, discharged by an empty `git diff --stat`.
- **Predecessor fence** per §P.1, discharged by an empty `git diff --stat` on each named file.
- **Docket fragment** `_orchestration/docket-entries/2026-08-05-echo-delay-v2-reach-through.md`, exactly one.
- **PR** titled `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`.
- **Pure-corpus fence.** No external-context reference of any kind in any tracked file, commit message or branch name.

---

> **Freeze statement.** `no gate, tolerance, band, frozen numeric parameter, bin boundary, regulator variant, self-test threshold or method element in sections 2P, 2Y, 4, 4Y, 5, 6, 7 and 7Y may be changed after any gate result is seen; if a configuration fails certification this lane reports NOT-CERTIFIED for that configuration, adjudicates NO physics bin for it, and routes to a successor with a new version number; v1's DELAY-NOT-CERTIFIED verdict on CFG-B is a historical fact that this document does not edit, withdraw or convert`.
