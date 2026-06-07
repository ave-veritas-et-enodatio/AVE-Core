# Is the AVE substrate node-algebra a biquaternion? (PREREG, FROZEN)

**Date:** 2026-06-06
**Branch:** `analysis/2026-06-06-biquaternion-node-algebra` (off `origin/main` `63190d35`; worktree `AVE-Core-quaternion-wt`)
**Status:** PREREG FROZEN — implementor derivation pending. Session: orchestration (Grant in-session).
**Origin:** Grant 2026-06-06 — *"should we map this to quaternions? Hamilton and Maxwell might've been close."* Follows the open/short-seam measurement thread, which dissolved into "the reflection wall is `|Γ|=1` + Z→∞ and the SIGN is a Möbius/spinor convention" — i.e. the reflection structure is already SL(2,C)/spinor.

---

## §0 Open goal + scope-fence

**The open goal (prove-or-disprove):** is the natural number-system of an AVE substrate node a **biquaternion** (complex quaternion ℍ⊗ℂ)? Either the one algebra structurally unifies the substrate's rotation/spin/longitudinal/reflection structure (and earns canonization), **or it is elegant re-expression of already-canonical SU(2)/Cosserat/Hopf structure** (consistency-class, a notation/pedagogy aid, NOT new physics). This prereg is written to be able to land EITHER verdict honestly.

**Scope-fence (`ave-evidence-framing`):** do NOT pre-claim "we found the substrate's number system." The default prior is **consistency-class** (re-expression) — the load-bearing work is the `(e)-genuinely-new` gate (§3). NOT a simulation; an analytical derivation + symbolic/numeric consistency checks. Does NOT touch the open/short primer relabel (separate small item; `|Γ|=1` + Z→∞ + sign-is-convention already adjudicated by measurement).

---

## §1 Canonical-framing pull (`ave-canonical-leaf-pull` item-16 — framework-extension)

The pieces the biquaternion would re-express are **already canonical**. Enumerated:

| Piece | Canonical home | Already-canonical content |
|---|---|---|
| **SU(2)→SO(3) double cover = spin-½** | `finkelstein-misner-spin-half-derivation.md` (EE-map means-test #14) | unit quaternions ARE SU(2); the 720° / 4π closure |
| **(2,3) Clifford-torus winding** | `torus-knot-uniqueness.md` (means-test #13) | the electron knot; "2-primary/3-secondary toroidal transformer" |
| **Cosserat SO(3) microrotation** | Axiom 1; `cosserat-mass-gap.md` | the 3 inductive/B DOF = the gyroscope sector |
| **Hopf fibration** | EE-map "toroidal flux-linkage linking number" | S³→S² (the quaternionic Hopf map) |
| **4π spinor-cycle radiation impedance** | `theorem-3-1-q-factor.md:32-36` | `R = Z₀/(4π)`, `α = e²Z₀/(4πℏ)` — the 4π IS the SU(2) double-cover factor in α |
| **α⁻¹ = 4π³ + π² + π = Q_vol+Q_surf+Q_line** | `theorem-3-1-q-factor.md:15` | THE load-bearing number; a volume/surface/line (3D/2D/1D) hierarchy × 4π-spinor |
| **Volumetric / longitudinal 7th mode** | `trampoline-framework.md:241,249`; `master-equation.md:16` ("Maxwell-Heaviside acoustic wave eqn"); `solver-toolchain.md:395` (electron = trapped longitudinal wave) | the scalar/breathing mode with "no rotational character" |
| **Γ reflection / Op17** | `operators.md` Op17; this session's measurement | `Γ=(z_B−z_A)/(z_B+z_A)` = a Möbius transform = SL(2,C)/spinor action (Smith chart) |

**Prior-work inventory (`ave-prereg`, cross-repo):** explicit quaternion/biquaternion/Clifford-*algebra* derivation = **none** (one tangential L3-archive mention, `research/_archive/L3_electron_soliton/11_op10_continuum_promotion.md`; AVE-HOPF carries Hopf/SU(2)/spinor for the antenna application, NOT the substrate-algebra question). New framing territory.

---

## §2 The hypothesis — the biquaternion node-algebra

A biquaternion has 8 real components: a complex scalar + a complex 3-vector. Proposed map of the node's **7 DOF + charge**:

| biquaternion slot | substrate DOF | sector |
|---|---|---|
| complex 3-vector (6) | **E (translational, u) + B (Cosserat ω)** as `F = E + iB` | capacitive + inductive |
| real scalar (1) | **volumetric breathing** (the longitudinal mode) | the 7th mode |
| imaginary scalar (1) | **charge = topological winding** (Axiom 2 [Q]≡[L]) | the spare slot |

Unit-quaternion closure = SU(2) = the spin-½ / (2,3) / 720° double cover. Maxwell's *Treatise* wrote EM as exactly this biquaternion (`F=E+iB` vector part + scalar part); Heaviside/Gibbs (1880s) deleted the scalar part → transverse-only EM. **The deleted scalar = AVE's longitudinal 7th mode.**

---

## §3 The `(e)-genuinely-new` gate (the load-bearing determination)

Per `ave-canonical-leaf-pull`, each piece in §1 is individually `(b)/(c)`-covered (re-expression of canonical SU(2)/Cosserat/Hopf/4π-spinor). The biquaternion is **consistency-class UNLESS** it passes ≥1 of:

- **(G1) Structural unification** — does ONE algebra *force* the closure (§T1), the longitudinal mode (§T2), and the Γ-Möbius reflection (§T3) to **co-occur** as facets of one object, where they are currently three independent canonical facts? (Unification IS new structural content even if each piece is individually canonical — but only if it's necessity, not juxtaposition.)
- **(G2) α-decomposition illumination** — does the biquaternion structure *derive or structurally explain* `α⁻¹ = 4π³ + π² + π = Q_vol+Q_surf+Q_line` (the vol/surf/line dimensional hierarchy × the 4π double-cover), independently of the Golden-Torus geometric derivation? (`α⁻¹` is THE number; an independent structural account is high-value.)
- **(G3) Longitudinal discriminator** — does the biquaternion *force a physical longitudinal mode* (which transverse EM forbids), and does that yield a **NEW testable prediction** (a number, a dispersion relation, a coupling) not already canonical?

**If none of G1–G3 pass → verdict: consistency-class** (re-expression / notation aid). Document honestly, do NOT canonize, do NOT claim new physics. **If ≥1 passes → genuine content**; scope canonization.

---

## §4 Derivation tasks (the implementor's work)

1. **Construct** the biquaternion node-algebra explicitly (the §2 map); state the multiplication + the conjugation(s) (quaternion conjugate, complex conjugate, biquaternion).
2. **§T1 closure:** show whether the unit-quaternion / SU(2) structure recovers the 720° / (2,3) / spin-½ double cover. (Consistency check — should reproduce canonical `finkelstein-misner` + `torus-knot-uniqueness`. Tag consistency-vs-emergence.)
3. **§T2 longitudinal:** show whether the biquaternion **scalar part** = the Maxwell-deleted scalar = the volumetric/longitudinal mode (the `master-equation.md:16` acoustic mode). Is the longitudinal mode a *structural necessity* of the algebra, or just identifiable with it?
4. **§T3 Möbius/reflection:** show whether `Γ=(z_B−z_A)/(z_B+z_A)` is the SL(2,C)/biquaternion action on the reflection (Riemann/Smith) sphere — i.e. is the Smith chart the spinor geometry of impedance? (Ties to this session's measurement: the sign is the Möbius/convention.)
5. **§T4 α-structure (G2 test):** does the biquaternion vol/surf/line + 4π-spinor structure connect to `α⁻¹ = 4π³+π²+π`? Forward only — NO target-fitting to 137.036 (`ave-driver-script-honesty`).
6. **Classify** each result (`consistency-vs-emergence`): definitional-identity / consistency / emergence / unification. **Run the §3 G1–G3 gate explicitly and state the verdict.**
7. **`ave-discrimination-check`** on §T2: is the longitudinal mode AVE-distinct (transverse-EM-forbidden) + does it predict anything new?

**Honest expected outcome (pre-registered):** most likely **partial** — T1 (closure) and T3 (Möbius) are probably consistency-class re-expression (the structure is already SU(2)/SL(2,C)); T2 (longitudinal = Maxwell's scalar) is the strongest genuine-content candidate; T4 (α-structure) is high-risk/high-reward. Pre-commit to landing "consistency-class notation aid" if G1–G3 all fail — that is a valid, publishable result, not a failure.

---

## §5 Discipline

`ave-canonical-leaf-pull` (framework-extension item-16, §1 done) · `ave-prereg` (cross-repo, §1 done) · `consistency-vs-emergence` (§4.6 mandatory classification + the G-gate) · `ave-discrimination-check` (§4.7) · `substrate-native-check` (the algebra must respect K4-bipartite + Cosserat + the (2,3) phase-space, not impose an abstract algebra top-down) · `phase-space-coordinate-check` (the (2,3) lives in (V_inc,V_ref) phase-space; the quaternion map must be phase-space-honest) · `ave-evidence-framing` (no "found the number system" without a passed G-gate) · `ave-canonical-source` (any numeric check imports constants). `ave-ee-first-mapping` already fired: EE = the measurement language (Z, Γ, windings); quaternions = the rotation-group/longitudinal language under it — **complementary, not a replacement**.

**Deliverable:** `research/2026-06-06_biquaternion-node-algebra-result.md` (the 4 derivations + the G-gate verdict + the classification + the discrimination + cross-links to the §1 canonical leaves). Reviewed PR; no merge.
