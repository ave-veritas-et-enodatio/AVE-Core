# PRE-REG (FROZEN) — Electron Port-Coupling Network: does a self-braced standing electron BIND?

**Date:** 2026-06-30 · **Lane:** implementer · **Branch:** `analysis/electron-portmap-derivation`
(worktree `/private/tmp/electron-portmap`, off `origin/main` @ `778823e9`).
**Type:** DERIVATION / ANALYSIS. **NO simulation.** Validate only doc + symbolic self-consistency.
**Freeze-before-derive:** this prereg is committed as the FIRST commit of the branch; the
SHA-pin below is filled at commit time and the adjudication criteria (§5) are frozen BEFORE
any derivation line is written. Per Rule 11 no criterion is dropped/weakened post-hoc to
convert a NO-BIND verdict into a BIND verdict.

**SHA-pin (this file, frozen commit):** `<filled at commit>` — the derivation parts (result
doc) are built AFTER this commit and cite it.

---

## SECTOR HEADER (stated before any standard-physics word)

- **MODE:** standing electron — **EXISTENCE**, not genesis. We ask whether a bound state CAN
  exist as an equilibrium of the port network; we do NOT run a formation trajectory (the
  self-formation slot is twice-falsified and stays BARRED, A47 v11b).
- **REGIME:** near-yield, `A → 1`. The Axiom-4 saturation nonlinearity `S(A)=√(1−A²)` is
  **LIVE, not linearized** — `S → 0`, `C_eff=C_0/S → ∞`, `n_grav=S^(−1/2) → ∞` at the core.
- **PHASE-STATE:** self-sustaining locked oscillation (the (2,3) winding runs an AC circulation;
  we ask whether its time-average braces its own envelope).
- **SECTORS in the loop:**
  - **A1** = dilatation = mass envelope. Compressive / **capacitive** (the `C_eff=C_0/S`
    varactor; `resonant-lc-solitons.md`:29–32). Bulk channel `Z_bulk`.
  - **μ** = Cosserat (2,3) micro-rotation winding = charge. Circulating / **inductive**. Carries
    BOTH a DC circulation (the static `Link(∂Ω,F)∈ℤ` boundary integer) AND an AC oscillation.
    Shear channel `Z_shear` (`resonant-lc-solitons.md`:120,124).
  - **Γ=−1 wall** = reflective termination (the self-woven perfect topological mirror,
    `resonant-lc-solitons.md`:44–52).
  - **ε** = transverse permittivity `ε_eff=ε_0·S` (T2). Enters the loop ONLY if the derivation
    shows it does; default is that mass=A1 and charge=shear are the load-bearing pair.

**Guard against SM/QED leak:** no Lagrangian-minimization, no gradient-descent-on-energy-basin,
no continuum-Helmholtz. The equilibrium is a **reactive pressure balance** at a self-set Q-point,
NOT an energy-landscape minimum. Ports are native Cosserat (A1/μ/ε/T2), NOT Cartesian stencils.

---

## THE PICTURE BEING TESTED (the physical hypothesis, stated so it can FAIL)

The (2,3) winding runs an AC circulation. The saturation nonlinearity RECTIFIES it into a
DC time-averaged compression (a ponderomotive envelope) = the rest mass. That inward pull would
IMPLODE unless braced. A stable electron = the balance of the inward pull against an outward
brace that RISES FASTER than the pull as the envelope shrinks. Candidate brace: the winding's
own DC circulation reactive pressure. "Mass IS inductive resistance": the DC store energy = rest
mass; the same reactance's opposition-to-change = inertia.

**This picture is FALSIFIABLE at three points:** (i) the inward-leg sign could be OUTWARD
(no rectified compression → no envelope → picture inverts); (ii) the brace could be ABSENT from
the network (no term rises faster than the pull → implosion); (iii) even if both present, the
stability inequality could fail either way (brace-too-weak → implode; brace-too-early → disperse).
Any of these is an HONEST NEGATIVE, recorded as such, not debugged toward a rescue.

---

## PRIOR STATE (verify-before-cite — what the corpus already fixes, and what it does NOT)

1. **The EIGENMODE frame is FALSIFIED (#415/#417).** The static coupled A1+winding eigensolve
   returned DOES-NOT-EXIST: no bound eigenstate carries BOTH the mass AND the (2,3) winding
   (`research/2026-06-24_engine-coupled-eigensolve_result.md` §0; gate d FAIL, `bw_on_torus≈0.0001`).
   Both the real-space-locus AND the phase-space dynamical-orbit loci read NEGATIVE. **This prereg
   asks a DIFFERENT question** — the NONLINEAR FEEDBACK / STABILITY question (is there a
   reactive-pressure equilibrium?), NOT the linear-eigenfrequency-existence question. Same network
   structure, different operator question. The eigensolve negative is DATA (binding does not fall
   out of the linear frame), held as a real prior odds against easy binding.

2. **The prior "stabilized feedback loop" is RETRACTED AS ARTIFACT (#83).**
   `research/2026-06-26_stabilized-electron-feedback-loop_result.md` header: the "stable lock" was
   **damping-bought-localization** (a viscosity term `e^{−η dt M}`) = an **Axiom-3 violation**, and
   the "ε→α" was α hard-injected on both ends. **HARD GUARD for this derivation:** the brace MUST be
   REACTIVE (lossless). Any equilibrium that requires a dissipative port is DISQUALIFIED as the same
   forbidden crutch. Losslessness is CONFIRMED via Tellegen (all-reactive network), not asserted.

3. **The pressure-equilibrium frame EXISTS but does NOT force `R·r=¼` (Fork-A, #419).**
   `research/2026-06-24_forka-alpha-flip.md`: the self-biased Q-point pressure balance is a
   conservative slosh that fixes a SCALE (`r`, or an `<2H>(R,r)` relation), NOT the product `R·r`;
   and √α re-enters via `V_yield=√α·V_snap`. **Consequence for THIS derivation:** the equilibrium
   SIZE we solve for is a SCALE; the `R·r=¼` product is a Class-B INPUT, not our output. We compare
   our equilibrium scale to the canonical Compton radius; we do NOT claim to derive `R·r=¼`.

4. **The confinement mechanism is SOLID and REACTIVE (`C_eff=C_0/S`, `L=adjoint_div(D∇)`,
   `D=1/S`).** Fork-B (`research/2026-06-20_fork-b-saturation-tank-confinement_result.md`) + the
   mass-sector synthesis: confinement is saturation-structure-decided, scramble-de-confining (NOT a
   projector tautology), shape-generic, lossless. But the bound-mode ω is lattice-band-structure-set,
   diverging with size — NO electron value-anchor (`m_e` definitional). **Consequence:** any binding
   we find is at BEST a FORM-chord / consistency, never a value-chord.

5. **Sign anchors from canon (load-bearing, verify-before-cite):**
   - `boundary_invariants.py`:129–133 — `n_grav = S^(−1/2)`, mass integrand `= n_grav − 1 > 0`
     where strained. **Strain RAISES `n_grav`** ⇒ the ponderomotive index gradient lenses INWARD
     (self-focusing; `research/2026-06-09_...self-focusing...`:15–16). This is the inward-leg sign
     CANDIDATE; §2 DERIVES it rather than assuming it.
   - `resonant-lc-solitons.md`:29–32 — `C_eff=C_0/S → ∞` as `A→α` (varactor SOFTENS the compliance).
   - `resonant-lc-solitons.md`:17–23 — the rest-mass ledger: `E_mag=½L_e I_max²`, `I_max=ξ_topo·c`,
     virial `E_elec=E_mag=½ m_e c²` ⇒ `E_total=m_e c²`. The rest mass = stored inductive+capacitive
     reactance (`clm-jwyy6l`: `E_mass=½L_eff|A|²`, inertia = back-EMF `V=−L di/dt`).
   - `theorem-3-1:32` — `L_e=(ℓ_node/e)² m_e`, `ω_C L_e = ℏ/e² = Z_0/(4πα)` — the reactance is
     α-encoded via the SI definition of `e,ℏ` (this is the §6 downstream relativistic-consistency
     check; OPEN, not resolved here).

---

## THE DERIVATION PLAN (6 parts — locked)

1. **Port network.** Map ports (A1 compressive, μ circulating with DC+AC, Γ=−1 wall, ε?) + every
   coupling. REUSE the coupled 3-channel graded-impedance network structure (`resonant-lc-solitons.md`
   §Z_EM/Z_bulk/Z_shear; the coupled-eigensolve H-structure) — but pose the NONLINEAR
   feedback/stability question. Deliver a port table + coupling diagram. Confirm losslessness via
   Tellegen (every port purely reactive ⇒ Σ V·I* = 0, no dissipative branch).

2. **Inward leg — DERIVE THE SIGN.** Work out the `dω/dt` back-reaction (μ→A1 mutual coupling) and
   whether its time-average is COMPRESSIVE or expansive. Use the varactor `C_eff=C_0/S` and the
   `n_grav=S^(−1/2)` index. Show whether the rectified DC envelope self-focuses (inward) or
   defocuses (outward). **If OUTWARD, the picture inverts — report honestly.**

3. **Brace leg — DERIVE WHICH reactance supplies it.** Candidates: (a) winding DC-circulation
   angular-momentum reactive pressure `∝ L²/r³`; (b) topological ropelength floor (the (2,3) knot
   cannot compress below `~2π ℓ_node` without unwinding — a hard forbidden-wall); (c) saturation
   stiffening `D=1/S → ∞`. Do NOT assume (a). Derive which term is PRESENT in the network and its
   `r`-scaling.

4. **Equilibrium.** Solve inward-pull = outward-brace for the electron SIZE. Compare to the
   canonical Compton radius / `R·r=¼` Golden-Torus scale (`ch8-alpha-golden-torus.md`;
   `L_NODE=ℏ/(m_e c)`). Consistent or not?

5. **Stability criterion (MAKE-OR-BREAK).** At equilibrium, is `d(brace)/dr > d(pull)/dr`
   (magnitudes, restoring sense)? State symbolically + evaluate.

6. **Rest-mass / inertia ledger.** DC envelope stored energy = rest mass (`E_0=m_e c²`); the SAME
   reactance's opposition-to-change (`−L dI/dt`) = inertia. FLAG the downstream check: exact
   rest-mass = inertial-mass equality requires the boosted winding-field momentum to give
   `p = E_0 v/c²` (relativistic consistency) — note OPEN, do NOT resolve here.

---

## ADJUDICATION CRITERIA (FROZEN — the pass/fail, locked before deriving)

Let `P(r)` = inward pull magnitude, `B(r)` = outward brace magnitude, at envelope radius `r`.

**Definitions frozen:**
- **INWARD-LEG SIGN:** the sign of the time-averaged `⟨force⟩` on the A1 envelope from the
  rectified μ back-reaction. `COMPRESSIVE` (inward, `P>0` toward smaller `r`) or `EXPANSIVE`.
- **EQUILIBRIUM EXISTS:** `∃ r* > 0` finite with `P(r*) = B(r*)`.
- **STABLE:** at `r*`, `dB/dr < dP/dr` in the sense that a small `δr` produces a NET RESTORING
  reaction (compress → brace wins → pushes out; expand → pull wins → pulls in). Formally, with the
  net inward force `F_net(r) = P(r) − B(r)`, stability ⇔ `dF_net/dr |_{r*} > 0` (net force is
  restoring: more-inward when expanded, more-outward when compressed).

**FROZEN VERDICTS:**

- **STABLE-EQUILIBRIUM-EXISTS** (self-braced electron VIABLE → sim greenlit) **iff ALL:**
  - (V1) inward-leg sign is **COMPRESSIVE** (the rectified envelope pulls in), AND
  - (V2) a reactive (lossless, Axiom-3-clean) brace term is **PRESENT in the network** and rises
    steeply enough that `∃ r*` finite with `P(r*)=B(r*)`, AND
  - (V3) at `r*`, `dF_net/dr > 0` (stable — net restoring), AND
  - (V4) NO dissipative port is required for the balance (Tellegen losslessness holds), AND
  - (V5) the equilibrium SCALE `r*` is order-consistent with the Compton/`L_NODE` scale (a scale
    match, NOT a claim to derive `R·r=¼` or `m_e`).

- **NO-STABLE-EQUILIBRIUM** (HONEST NEGATIVE — the naive network does not bind) **if ANY:**
  - (N1) inward-leg sign is **EXPANSIVE** (picture inverts — no envelope), OR
  - (N2) **no reactive brace term is present** (only dissipative/hand-set braces would balance →
    disqualified) → **IMPLOSION**, OR
  - (N3) `∄ r*` finite (brace never equals pull: brace-too-weak → runaway compression = IMPLOSION;
    brace dominates at all `r` → runaway expansion = DISPERSION), OR
  - (N4) `∃ r*` but `dF_net/dr < 0` at `r*` (UNSTABLE — the equilibrium exists but any perturbation
    runs away: implosion on one side, dispersion on the other).

- **FORK-FOR-GRANT** if the inward-leg sign or the brace-presence is genuinely AMBIGUOUS at the
  symbolic level (e.g. depends on an un-adjudicated grade-attribution of `V_yield`, or on the
  `γ_surf` line-tension provenance flagged in Fork-A §8). Surface with both readings; do NOT pick.

**Anti-rescue guards (frozen):**
- No dissipative brace may be introduced to force a balance (retract the #83 artifact lesson).
- No new hypothesis refills a NO-BIND slot (A47 v11b substitution-not-retraction).
- If all failure paths point to one mechanism, that is Rule-11 honest closure — name it, close it.
- `m_e` VALUE is calibrated/imported; only the FORM (the mechanism + the scaling) is derived.

---

## CLASSIFICATION (consistency-vs-emergence — pre-committed)

- The **mechanism** (does a reactive brace balance the rectified pull?) is at best a
  **Class-C CONSISTENCY / FORM-chord**: it reproduces "stable localized electron mass exists" via
  an impedance/pressure mechanism the SM lacks, but the SIZE it fixes is a scale tied to the
  imported `L_NODE=ℏ/(m_e c)` (which carries `m_e`), and `R·r=¼` is a Class-B input. It is NOT a
  Class-D emergence (no dimensionless observable computed free of the target).
- Any appearance of α (via `V_yield=√α V_snap` or `Z_0=2αh/e²`) is an ECHO channel, flagged, not
  headlined as emergence (A47 v17 family).
- A NO-STABLE-EQUILIBRIUM verdict is a **Class-C consistency negative** with a named mechanism —
  a legitimate honest result, NOT a failure to debug toward binding.

## DELIVERABLE

`research/2026-06-30_electron-portmap-derivation_result.md`: port network (diagram/table),
inward-leg sign, identified brace, equilibrium size, stability criterion + evaluation,
rest-mass/inertia ledger, and the VERDICT (STABLE-EQUILIBRIUM-EXISTS vs NO-STABLE-EQUILIBRIUM vs
FORK-FOR-GRANT), with honest solidity + open items. NO sim; NO KB/manuscript edits (research/ only).
Push branch, STOP (orchestrator opens the PR after independent verify).
