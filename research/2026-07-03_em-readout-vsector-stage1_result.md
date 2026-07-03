# RESULT — EM-readout Stage-1 (the V-sector / transducer build)

**Status:** RUN-COMPLETE. **STAGE-1 VERDICT: [SECTOR-BUILT + MAXWELL-RECOVERED] on the channel; [NON-EMERGENCE] on the transducer coupling** — the gapless EM-ε channel is built on the srs carrier and passes validate-on-known (Coulomb recovered from a KNOWN source, Gauss-counting emerges), BUT the electric monopole does NOT emerge from the axiom-native rotation→translation coupling applied to the winding (∇·(∇×ω) = 0 to machine precision). Per Grant's mission framing ("if it does not emerge, that is the honest stakes-table result; no insertion ever"), this is booked as the honest measured result, no rescue.
**STAGE-2 HELD** until the equation-audit (§4) is reviewed by orchestrator + Grant (prereg §6).
**Prereg (FROZEN + dated correction):** [`2026-07-03_em-readout-vsector-stage1_prereg.md`](2026-07-03_em-readout-vsector-stage1_prereg.md) @ this branch (correction commit `acd2e51d`).
**Charter:** `_orchestration/2026-07-03_em-readout-derivation-charter.md`. **Grant-CONFIRMED target-(1)** (build the transducer).
**Branch:** `analysis/em-readout-vsector-build` (off `origin/main` @ `9956c0b6`, post PR #474). NO self-merge.
**Driver:** [`src/scripts/vol_2_subatomic/em_readout_vsector_transducer.py`](../src/scripts/vol_2_subatomic/em_readout_vsector_transducer.py). **Results JSON:** `..._results.json`.
**Classification (`consistency-vs-emergence`):** the channel is a MEDIUM-scaffold (infrastructure); VoK is CONSISTENCY (Maxwell-recovery from a KNOWN); the transducer is the EMERGENCE test — result NON-EMERGENCE. NO chord/emergence claim minted.

---

## 0. THE ONE-SCREEN SUMMARY

| Deliverable | Result |
|---|---|
| Carrier finding (Rule-10) | diamond-K4 TETRA_OFFSETS cage is BIPARTITE (ill-posed for a static scalar); the EM-ε channel RE-HOMED to the srs (z=3) carrier |
| VoK (a) zero-source floor | PASS — φ≡0, E≡0 exactly |
| VoK (b) Coulomb Green's function | PASS — near-field φ exponent **−1.47 (R²=0.99)**, Coulomb 1/r recovered on the srs carrier |
| VoK (c) superposition + Gauss counting | PASS — field linearity exact (2e-12); ∇·E diagnostic counts total (ratio 2.000) |
| **Transducer (the emergence test)** | **NON-EMERGENCE** — winding Q_link=3, but emergent net electric monopole = **8.9e-16 (machine zero)**; ∇·(∇×ω)=0 identically |
| Equation-audit gate | PASS — 7 AXIOM-DERIVED / 0 ENGINEERING-CHOICE / 3 FORBIDDEN-INSERTION-rejected; no winding→charge insertion; Gauss diagnostic-only |
| §5 rotation-bookkeeping un-conflation | site list landed (8 sites, KEEP-BOTH; surfaced for auditor) |

**The honest physics:** the winding's substrate flux F = ∇×ω is **divergence-free** — it sources a magnetic DIPOLE (Grant ruling part ii, "closed loops make dipoles"), NOT the electric MONOPOLE (part i). The only Link-counting quantity is the helicity ω·(∇×ω) = H_bel = the charge LABEL itself; coupling it to ∇·E as a source is the winding-as-charge insertion the un-riggability rule FORBIDS (measured for the audit, NOT used). So Gauss-as-link-counting does NOT emerge from the axiom-native static rotation→translation coupling. This surfaces a sharp framing question (§6) for the Stage-2-review.

---

## 1. THE CARRIER FINDING (Rule-10 — run the driver early)

The prereg §4 named the "unified srs facade" as the presumptive host. Building the EM-ε static scalar channel required choosing a native stencil for its Laplacian. The first attempt used the diamond-K4 `TETRA_OFFSETS` stencil (the certified `native_cage_imex` Grad/Div). **Measured this session — it is ill-posed for a static scalar Poisson solve:**

- `TETRA_OFFSETS = [(1,1,1),(1,−1,−1),(−1,1,−1),(−1,−1,1)]` — all four offsets have ODD coordinate-sum, so the stencil couples ONLY across the two parity sublattices ⇒ the Laplacian L=Div·Grad is **BIPARTITE with a massive checkerboard nullspace** (≥12 near-zero eigenvalues at N=16, vs the single constant mode a well-posed Laplacian has).
- A static scalar solve `Lφ=source` on it **diverges** (CG → ~1e16 garbage; exterior exponent +0.2, R²=0). No 1/r.
- The certified cores NEVER do a static scalar solve on this L — they use ONLY the shifted DYNAMICAL form `(I + ¼dt²c₀²L)`, where the identity `I` regularizes the nullspace. The diamond cage is the **A1-BULK-VECTOR** carrier, not a scalar EM channel.

**Re-homed to the chiral srs (z=3, (10,3)-a Sunada) carrier** — the free-mode/photon carrier. Its graph Laplacian L = D − A is **well-posed** (nullspace = the constant mode only). This is the substrate-native home consistent with the prereg §4 pointer, and it is where the free transverse (EM) modes already live in the facade. **Class: a build-carrier correction, empirically forced, NOT a substrate blocker** (the srs carrier recovers Coulomb, §2).

---

## 2. VALIDATE-ON-KNOWN (Maxwell-recovery) — ALL PASS on the srs carrier

Per prereg §5. No transducer readout counts until all three pass. They pass.

### (a) Zero-source floor
Source = 0 → φ ≡ 0, E ≡ 0 exactly (`max|φ|=0`, `max|E|=0`). The channel invents no field.

### (b) The Coulomb Green's-function check (the load-bearing sector-validity test)
A KNOWN unit point source (imposed + labeled — prereg §5(b)-sanctioned: validating the SECTOR's dynamics, NOT the winding coupling) → solve Lφ=source → the **near-field potential exponent is −1.47 (R²=0.99)** over r∈[1.5,6] node-distance. That is Coulomb 1/r (the lattice-discrete exponent sits in −1..−2; the field is correspondingly ~1/r²). The far-field (r > box/2) steepens to −5.3 — correctly identified as the **periodic-image / neutralizing-background finite-box artifact**, NOT the physical tail, and reported as the control window, not the certification. **The srs Laplacian's Green's function recovers Coulomb in the physical near-zone. Sector VALID.**

### (c) Superposition + Gauss counting
Two KNOWN sources → the FIELD (gauge-invariant edge gradients) adds linearly to **2e-12** (exact). The ∇·E DIAGNOSTIC (∇·E = −Lφ, MEASURED never enforced) counts the total: ∇·E at two sources / at one source = **2.000**, with global ∇·E ≈ 0 (the neutral background). Gauss-counting EMERGES from the linear solve as a measured property — for the KNOWN imposed source. (Honest caveat, §4: for a KNOWN source ∇·E = −Lφ = source by construction of the solve — this confirms the discrete divergence theorem holds on the srs Laplacian; the NON-trivial emergence question is whether the WINDING sources such a ∇·E, tested in §3.)

---

## 3. THE TRANSDUCER — THE EMERGENCE TEST → NON-EMERGENCE

**The setup.** Seed the (2,3) winding ω on the srs carrier (its OWN DOF, genesis-24-clean seed `seed_pq_winding_on_srs`); read the Link integer it carries (`compute_Q_link_srs` → **Q_link = 3**, w_tor = 2). Build the EM-ε channel's source ONLY from Axiom-1's rotation→translation coupling applied to ω — the ONLY axiom-native place a rotational winding can push the translational (E) sector (`axiom-definitions.md:16`: translational u↔E/ε₀ ⊥ microrotational ω↔B/μ₀, LC-coupled). Measure whether the emergent ∇·E counts the Link (electric monopole EMERGES) or is ~zero (NON-emergence). **NO 𝒬→source insertion; NO ρ=𝒬δ³.**

**The measurement (both axiom-native couplings — I let the substrate decide across both, not cherry-pick):**

| Ax1-native coupling (drive → source b_EM = ∇·drive) | net electric monopole | net / total | verdict |
|---|---|---|---|
| drive = ∇×ω = F (Ampère-like: E-sector driven by curl of ω) | **8.9e-16** | 3.3e-18 | machine zero |
| drive = ω (LC: ∂ₜu ∝ ω) | **−5.3e-15** | 7.6e-18 | machine zero |

**Both give a NET electric monopole of exactly ZERO** (machine precision), despite the winding carrying Q_link = 3. The exterior E-field exponent is +0.72 (R²=0.06) — no monopole structure, consistent with zero net charge. **The electric monopole does NOT emerge from the axiom-native rotation→translation coupling.**

**Why (the mechanism, named):** the substrate flux F = ∇×ω is a **pure curl**, so ∇·F = ∇·(∇×ω) = 0 **identically** (a vector-calculus identity, robust on the substrate-native discrete curl/div to machine precision). A divergence-free flux sources NO monopole — it sources a **magnetic DIPOLE** (Grant ruling part (ii): "closed loops make dipoles — the ring's circulation via the transverse/inductive sector"). The winding is a closed loop; its far field in the transverse/inductive sector is dipolar, exactly as Grant's (ii) predicts. The electric MONOPOLE (part (i)) does not fall out of this coupling.

**The one Link-counting quantity — and why using it is FORBIDDEN.** The only quantity with a non-zero net that counts the Link is the **helicity** ω·(∇×ω) = H_bel = **−115.8** (net; this IS the Beltrami-helicity charge, `master-equation.md:20`, the charge LABEL). But using H_bel AS the source of ∇·E is precisely the winding-as-charge-source insertion the un-riggability rule FORBIDS — it is writing "the charge sources the charge field" by declaration (the def-tk1xfm "identity-by-translation, NOT a derivation" ceiling, made into a hand-wire). I **measured it for the audit** (to show it is the non-zero Link-carrier) but do **NOT use it as a source**. Coupling H_bel → ∇·E would give a 1/r field by construction — the exact rigged outcome the charter §3 forbids.

**The honest emergence verdict (Grant's mission "if it does not emerge, that is the honest stakes-table result"):** Gauss-as-link-counting does **NOT emerge** from the axiom-native static rotation→translation coupling. The winding's flux is divergence-free (magnetic dipole); the electric monopole requires either (a) a coupling to the helicity (= the charge label = a forbidden insertion), or (b) a mechanism not present in the static rotation→translation LC coupling (a rectification/dynamical/topological term the static coupling lacks). Booked as measured NON-EMERGENCE at this coupling grade. No rescue, no hand-wire.

**What this does and does NOT establish (scope discipline):**
- It DOES establish: the *simplest, most direct* axiom-native reading of "the winding sources the EM channel" — the static rotation→translation LC coupling — produces NO electric monopole. The naive transducer is a clean negative.
- It does NOT (yet) establish: that NO axiom-native mechanism can source the monopole. The static-coupling result leaves open whether a *dynamical/rectified* coupling (the winding's persistent circulation at ω_C, time-averaged through the Ax4 saturation nonlinearity) or a *topological boundary* mechanism (the Link as a boundary condition, not a bulk divergence) could produce a non-zero monopole without inserting the charge. That is the framing question (§6) — surfaced, not guessed.

## 4. THE EQUATION-AUDIT GATE (exit gate — Stage-2 HELD until reviewed)

Per prereg §6 (the #384-unriggable-gate pattern for physics equations). Every load-bearing term, tagged; the demonstration that no term references the winding as a charge source by declaration. **Gate verdict: PASS** (`gate_passed = True`).

| Term | Role | Tag | Cite / status |
|---|---|---|---|
| L = D − A (srs graph Laplacian) | the gapless EM-ε channel operator | AXIOM-DERIVED | Ax1 chiral srs net; native discrete Laplace–Beltrami; well-posed |
| D-coefficient = 1 (gapless) | no mass term | AXIOM-DERIVED | cold far-zone S→1; Γ_EM=0 matched; NO ω_gap smuggled |
| E = −grad_graph φ | the electric field | AXIOM-DERIVED | graph gradient (edge differences) |
| ∇·E = −Lφ | Gauss DIAGNOSTIC | AXIOM-DERIVED | MEASURED only; never enforced (no ∮E·dA=𝒬/ε₀ anywhere) |
| F = ∇×ω (substrate flux) | the winding's flux | AXIOM-DERIVED | compute_F_curl; Link(∂Ω,F)=charge, boundary-observables:20 |
| drive = Ax1 rotation→translation (ω or ∇×ω) | the transducer | AXIOM-DERIVED | axiom-definitions.md:16 (LC ω↔u) |
| b_EM = ∇·drive (the EM-ε source) | the emergent source | AXIOM-DERIVED | divergence of the axiom-native drive; MEASURED; ∇·(∇×ω)=0 ⇒ net monopole = 0 |
| b = 𝒬·δ³(r) | would source 1/r by fiat | FORBIDDEN-INSERTION | NOT USED — grep-confirmed absent |
| ∮E·dA = 𝒬/ε₀ enforced | would force Coulomb by fiat | FORBIDDEN-INSERTION | NOT USED — Gauss diagnostic only |
| b_EM = ω·(∇×ω) (helicity = charge label) | would source ∇·E from the label | FORBIDDEN-INSERTION | measured for audit, NOT used as source |

**Tally: 7 AXIOM-DERIVED / 0 ENGINEERING-CHOICE / 3 FORBIDDEN-INSERTION-rejected.**

**Self-grep demonstration (executable code only — docstrings/comments stripped to avoid the grep-completeness false-positive on the audit's own DESCRIPTION of the forbidden patterns):** all four forbidden patterns ABSENT (`rho_eq_Q_delta`, `gauss_enforced`, `helicity_or_Q_into_solve`, `Q_to_field_dictionary` all False). Every `solve_static` source is a labeled KNOWN (the VoK imposed sources) or the emergent `b_EM` — `Q_link` and `hel` NEVER flow into a solve. `all_solve_sources_allowed = True`.

**The gapless / static-curl-free pair (prereg correction item 2, `historical-precedents.md:21`):** `static_curl_free_supported = True` (L is a pure graph ∇²; E = −grad φ is a curl-free static field — the retained Coulomb-longitudinal E) AND `propagating_longitudinal_absent = True` (L carries NO time derivative ⇒ no propagating mode of any polarization ⇒ trivially no propagating longitudinal EM wave, which the corpus forbids). The pair is asserted structurally and holds.

**STAGE-2 HELD.** Per prereg §6, Stage-2 (seed 0₁+(2,3), measure whether ∮E·dA counts Link EMERGENTLY over the full readout) stays HELD until this equation-audit is reviewed by orchestrator + Grant. Given the transducer already returns NON-EMERGENCE at the static-coupling grade, the Stage-2-review must also weigh the §6 framing question (is the negative final, or does a dynamical/topological coupling deserve a Stage-1b before Stage-2).

---

## 5. THE §8 ROTATION-BOOKKEEPING UN-CONFLATION (site list as landed — surfaced for the auditor)

Per prereg §8 + the correction-note items. The corpus conflates the EM-inductive rotation (μ₀-family = B; massless, matched, T2-photon) with the mechanical Cosserat micro-rotation ω (couple-stress; gapped). Each site gets an honest disambiguation (which rotation, gapped-vs-massless tag), KEEP-BOTH per-site — **disambiguate, don't adjudicate; the auditor lands the manual, and the G2 label-inversion sites (7,8) stay Grant-gated where a physics ruling is needed.** All cites verified at HEAD `9956c0b6` this session.

| # | Site | The disambiguation |
|---|---|---|
| 1 | `master-equation.md:20` | the (2,3) WINDING = the GAPPED mechanical Cosserat ω (couple-stress); distinguish from the massless EM-inductive B-rotation |
| 2 | `k4-port-irrep-decomposition.md:26` | the "T₂ = photon" is the MASSLESS EM-inductive rotation (B); distinguish from the gapped mechanical Cosserat couple-stress ω the winding rides |
| 3 | `biquaternion-…:71` | the charge Link boundary is on the mechanical SHEAR sector (Z_shear, lossless static); reconcile with the T2/ω assignment |
| 4 | `node-up-small-large-signal.md:39` | already tagged MECHANICAL + static-reactive — the CLEAN reference the others reconcile to |
| 5 | `translation-circuit.md:541` (Leaf A) | the A_geom ∝ 1/r Coulomb POTENTIAL in the gapless EM-ε channel (clm-4r4jiy); distinguish from the gapped-ω hedgehog |
| 6 | `substrate-perspective-electron.md:109` (Leaf B) | the GAPPED mechanical Cosserat ω hedgehog (short-range residue); distinguish from the gapless EM-ε Coulomb tail |
| **7** | `cosserat-mass-gap.md:145` + `vol1/claim-quality.md:1131` | **G2 INVERSION (Grant-gated):** these call the massless A1/translational-u sector "the photon" and put the mass-gap on T2/ω — the INVERSE of `master-equation.md:20/27` (A1=mass, T2=charge). Flagged in-corpus at `epic:319` (GAP G2). Tag the collision; do NOT adjudicate. |
| **8** | `master-equation.md:27` + `cosserat-mass-gap.md:151` | **the hedge (Grant-gated):** mass=A1 is RATIFIED-CONSISTENCY (PR#260 grade-assignment), NOT driver-validated — the `cosserat-mass-gap.md:108` Verlet driver attributes the mass-gap to T2 with placeholder S4 moduli. Tag; do not resolve. |

**Load-bearing consequence for THIS build:** the un-conflation confirmed the transducer couples FROM the gapped mechanical Cosserat ω (the winding carrier), and reads out INTO the gapless EM-ε channel — the two are distinct sectors bridged by the (attempted) transducer. The G2 inversion (sites 7,8) does not change the Stage-1 result (the ∇·(∇×ω)=0 identity holds regardless of which irrep label is "the photon"), but it is surfaced because it is exactly the sector-label ambiguity the un-conflation exists to make explicit.

---

## 6. THE FRAMING QUESTION THIS SURFACES (for the Stage-2-review — Grant's door)

The Stage-1 measurement is a clean, un-riggable NEGATIVE at the static-coupling grade: **the axiom-native static rotation→translation LC coupling does NOT source an electric monopole from the winding** (∇·(∇×ω) = 0; the only Link-counter is the helicity, whose use as a source is forbidden). This is consistent with Grant's ruling part (ii) (the winding IS a magnetic dipole) but leaves part (i) (the electric monopole) **not-yet-emergent**. Before Stage-2 runs, one framing question must be weighed (surfaced per `pre-test-physics-check`, not guessed):

> **Is the static-coupling non-emergence the FINAL word on the electric monopole, or does part (i) live in a coupling the static rotation→translation LC term structurally lacks?** Three readings, each with a concrete Stage-1b:
> - **(X) FINAL negative — the lone winding sources NO electric monopole.** The electric monopole is a *pair-interaction / topological-boundary* property, not something a single winding's static flux carries (Stage-0 option C, partially resurfacing). ⇒ book the framework-level negative (charter §2 highest-stakes branch); the "charge sources Coulomb" story is a pair/boundary property, not a single-winding field. No Stage-2 winding-monopole readout (it would measure the confirmed zero).
> - **(Y) the monopole needs the DYNAMICAL / rectified coupling** — the winding's persistent circulation at ω_C, time-averaged through the Axiom-4 saturation nonlinearity, may leave a static DC monopole residue the *static* coupling cannot see (the Stage-0 lane-(a) rectification, but now with Ax4 present). ⇒ a Stage-1b: add the Ax4-nonlinear time-averaged coupling and measure ⟨∇·E⟩ over a cycle. (Risk: this is where a rectifier chosen to give 1/r would be a forbidden insertion — the Stage-1b must derive the rectifier from Ax4, not fit it.)
> - **(Z) the monopole is a TOPOLOGICAL BOUNDARY condition, not a bulk divergence** — the Link as a boundary flux-quantization on the EM-ε channel's solution space (Stage-0 lane-c), sourcing a monopole via a boundary term ∮ that ∇·(bulk) misses. ⇒ a Stage-1b: impose the Link as a boundary flux (NOT a bulk ρ) and measure whether the emergent exterior is 1/r. (Risk: imposing the Link as a boundary flux is close to the def-tk1xfm insertion — the Stage-1b must show the boundary condition is forced by the winding's topology, not hand-set.)
>
> **My read (surfaced, not a unilateral pick):** the static result cleanly confirms part (ii) (magnetic dipole) and cleanly refutes the *naive static* route to part (i). Reading (X) is the honest default IF part (i) is meant to be a single-winding static field — the measured zero is exactly what "no electric monopole from a divergence-free flux" predicts. Readings (Y)/(Z) are the two axiom-native escape hatches, each with a named un-riggability risk. **This is the Stage-2-review decision: book (X) as the negative, or authorize a Stage-1b for (Y) or (Z) before Stage-2.** Per your standing door, I stop at the equation-audit HOLD and surface this rather than pick.

---

## 7. DISCIPLINE LEDGER

- **`verify-before-cite`:** the three coordinator items were VERIFIED INDEPENDENTLY at HEAD `9956c0b6` (I ran each grep myself before relying): item 1 (A1 gapless / rotational gapped — `cosserat-mass-gap.md:145`, `vol1/claim-quality.md:1077`, `cosserat-band-structure:74,77`) CONFIRMED, my frozen prereg §2.1 gap-status corrected via dated note (`acd2e51d`); item 2 (static Coulomb-longitudinal E retained — `historical-precedents.md:21`) CONFIRMED, folded into the equation-audit pair; item 3 (G2 inversion + mass=A1 hedge — `cosserat-mass-gap.md:145/151`, `master-equation.md:27`, `epic:319`) CONFIRMED, folded into §5 sites 7–8.
- **`flag-don't-fix`:** the frozen-prereg gap-status error was corrected by a dated ADDENDUM, NOT a silent rewrite; the G2 inversion is tagged-not-adjudicated (Grant-gated); the framing question (§6) is surfaced, not resolved.
- **Rule 10 (empirical-driver):** the driver was run early and caught the diamond-carrier ill-posedness + the transducer non-emergence at integrator time (not by static analysis). The carrier re-home was empirically forced, not assumed.
- **Un-riggability (charter §3):** NO 𝒬→source insertion; NO ρ=𝒬δ³; NO ∮E·dA=𝒬/ε₀ enforced; the helicity (charge label) measured but NOT used as a source. Gauss diagnostic-only. The equation-audit self-grep confirms this on the executable code. The NON-emergence was NOT rescued toward 1/r.
- **`consistency-vs-emergence`:** channel = infrastructure; VoK = CONSISTENCY (Maxwell-recovery from a KNOWN); transducer = EMERGENCE test, result NON-EMERGENCE. NO chord/emergence/DEFENSE claim minted.
- **Rule-14 (reuse certified cores):** the native Grad/Div (native_cage_imex), the winding seed + Link reader (srs_cage_winding, charge_quantization), the srs net (chiral_lattice) were wired verbatim; only the srs graph-Laplacian + the transducer coupling are new (and minimal).
- **INVARIANT-N1:** no new substrate noun; the EM-ε channel / transducer are circuit-model constructs on the existing sectors.
- **Grant mission ("emergence is the goal; if it does not emerge, that is the honest result; no insertion ever"):** honored exactly — emergence was the falsifiable target, it did NOT emerge at the static-coupling grade, and the negative was booked without a rescue-insertion.

---

> **STAGE-1 COMPLETE. HOLD-POINT.** Stage-2 stays HELD until the equation-audit (§4) + the framing question (§6) are reviewed by orchestrator + Grant. The final message surfaces the un-conflation site list, the validation results (the 1/r Green's-function especially), the ledger summary, the equation-audit verdict, and the §6 framing question. Corpus updates (the §5 un-conflation manual entries, the axiom-register Ax2-leg row) are surfaced for the auditor to LAND — implementer does not land manual entries.
