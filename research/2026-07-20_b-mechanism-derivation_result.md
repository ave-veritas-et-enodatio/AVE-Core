# Reading-B Mechanism Derivation — what closes the bulk channel's far-field port for gravitating sources (result)

**Date:** 2026-07-20
**Class:** DERIVATION (research-doc; **forms derived, values calibration/observation-imported and tagged; mints no `clm-`, propagates to no KB/tex leaf**). Resolves the frozen bins of the companion pre-registration (`research/2026-07-20_b-mechanism-derivation_prereg-FROZEN.md`) for the #753 §6 sharpened obligation.
**Provenance:** Grant-fired 2026-07-20 (verbatim `[sic]`: `"fire"` on the Reading-B mechanism derivation). Executes the three independent traces (B1 constraint / B4 band-structure / B2 source-projection) named in #753 §3 and the port register FLAG-A.
**Lane fences:** DERIVATION lane only. **READ-ONLY on KB.** No engine edits; no `manuscript/` / `manuscript/ave-kb/` leaf edits; no edits to #748/#750/#751 branch files. Every `[canon]` input content-verified two-method at HEAD `e2e870c0` (verify-before-cite). Arithmetic + eigenstructure reproduced by `research/drivers/b_mechanism_k4_commonmode_residual.py` (+ `_results.json`), which imports `ave.core.constants` (`L_NODE`, `C_0`, `OMEGA_C`) read-only and touches no engine primitive.

**HEADLINE (stated plainly, both ways, no thumb on the scale).** The frozen-bin verdict is **UNDETERMINED, leaning B1-FORCED**. A genuine, DERIVED, AVE-native closing mechanism exists — the **K4 tetrahedral (T_d) 4-port common-mode rejection** (the scatter `S = ½·𝟙 − I` has the A1/longitudinal as its `+1` "DC" eigenvector, which is common-mode-rejected and losslessly transduced into the T2/shear triplet — the substrate-native realization of Gauss's law, `∇·E = 0` forbids longitudinal vacuum EM). This is exactly the *"structure the vacuum has and a rock lacks"* the §6 obligation demands (a rock is a continuum with no T_d 4-port scatter; its P-wave is an independent persisting DOF). It WOULD close the port **exactly** (residual `≡ 0`). **But** it rests on ONE unforced choice the corpus carries unresolved: whether the *gravitational* A1-dilatation is governed by the **K4-TLM bond-scatter** (A1 common-mode-rejected — port closed) or by the **srs Cauchy site-elasticity** (which the adjudicated band survey shows DOES carry a gapless propagating P-branch — port open, Reading A, EXCLUDED). Per the discipline, an unforced choice ⇒ UNDETERMINED with the fork stated. **Two of the three traces are decisively closed:** B4 is FALSIFIED (the lattice HAS a gapless propagating compression branch — the sleeper does not win), and B2-via-tracelessness is FALSIFIED (scalar-field quadrupole radiation IS driven by the traceless second moment — the tempting source-vanishing rescue is dead). The whole question collapses onto the single B1 model-ownership fork.

---

## §0 — REGIME / SECTOR / PHASE-STATE header (fired before any structural algebra)

**MODE.** A non-relativistic compact binary (Hulse-Taylor B1913+16, `v/c ~ 10⁻³`; double pulsar J0737-3039A/B, `v/c ~ 2×10⁻³`) as a **source** driving the deep vacuum's A1/bulk sector. Contrast column: the observed orbital decay `Ṗ_b`, matched to the GR shear-quadrupole (#753 §2.2).

**REGIME.** **Regime I** — deeply linear far field (`V_GW/V_snap ~ 10⁻²⁸`, `einstein-field-equation.md:90-97` `[canon]`); the lattice "responds linearly, lossless propagation at `c`." Saturation (Op14) does not enter the propagation.

**PHASE-STATE.** **Cold-reactive** (Ax3-lossless-reactive; `eq_axiom_3.tex` `[canon]`, verbatim: `L_node = ½ε₀|∂_t A_n|² − (1/2μ₀)|∇×A_n|²`, "the vacuum stores and returns energy but does not dissipate it… any apparent loss must be a boundary-radiation or mode-conversion channel, never a bulk resistive one"). Far-field radiation is a legal Ax3 loss channel (port-not-valve), so a radiating bulk channel would NOT violate Ax3 — that is why this is a live question, not an Ax3-forbidden one.

**SECTOR.** The observed GW = **T2 transverse shear** at `c` (`einstein-field-equation.md:84` `[canon]`, "GW are… transverse shear waves"). The channel under test = **A1 bulk dilatation** (the mass sector). **Sector-ownership discipline (do NOT cross-wire):** A1 owns compression/mass/dilatation; T2 owns shear/GW/charge-winding. The binary's masses ARE the A1-dilatation content (`master-equation.md:20` "A1 dilatation-MASS" `[canon]`), so the source is genuinely an A1 source — the derivation must take the A1 far-field seriously, not dismiss it by sector fiat.

**SUBSTRATE-NATIVE + PHASE-SPACE-COORDINATE CHECK (A46).** The corpus claim is a *channel-radiation* claim (does the A1 branch carry a far-field port?). The matching test coordinate is the **K4 port-irrep basis** (A1 dilatation vs T2 shear) — the same basis the corpus's own `A₁ ⊕ T₂` decomposition uses (`k4-port-irrep-decomposition.md` `[canon]`). The check script measures the closing mechanism in THAT basis (the A1/T2 eigenvectors of the K4 scatter), not in a real-space lattice-Cartesian strain the corpus never claimed. Consistency-vs-emergence: the K4 scatter eigenstructure is a **MANIFESTATION** (theorem of `T_d` group theory), not an emergence claim; every VALUE is dimensionless or `[import]`-tagged.

**CONSENSUS-KNIFE, BOTH WAYS (fired up front).** Two priors are in play and both are held: (i) the QED/GR reflex — "the longitudinal is always gauge/constrained" — which would hand B1 the win by default and is a known SM/QED leakage risk; (ii) the AVE-native vacuum-engineer reflex — "the vacuum is a real compressible elastic medium, so it radiates P-waves like a rock" — which would hand Reading A the win by default. **Neither default decides this.** The decider must be an AVE-native *structural* fact. The one I find (K4 T_d common-mode rejection) is AVE-native group theory, not a QED import — but its ownership of the gravitational A1 sector is exactly the unforced choice, so I do not let the QED reflex convert "a real mechanism exists" into "the port is forced closed."

---

## §1 — Trace B4 (band structure, ★the sleeper): FALSIFIED — the lattice HAS a gapless propagating compression branch

**Question (frozen):** does the ADJUDICATED discrete band model carry an independent propagating longitudinal branch, or was the continuum P-wave an idealization the lattice does not realize? If no independent gapless P-branch, B4 wins and FLAG-A dissolves.

**B4.1 — The adjudicated band survey shows a gapless propagating compression branch `[canon-read]`.** `srs-band-structure.md` (`clm-bnd5rq`, gates PASS #604/#607) is explicit:
- **Vector / Cosserat-translational channel: 12 bands, 3 acoustic branches, two distinct speeds `c_P ≠ c_S`** (`:78-89` `[canon]`). Direction-resolved P/S ratio, **lattice-computed**: `[100] 1.71, [110] 1.85, [111] 1.90` (`:120-122` `[canon]`). So the discrete srs net DOES realize an independent longitudinal (P) acoustic branch.
- **NO full stop-band (either channel):** "all 11 adjacent band-pair envelopes overlap; the 12-band manifold is fully connected `0→top`. The `k_a ≫ k_s` split did NOT open a full internal gap" (`:98-99` `[canon]`). The compression branch reaches DC (`k→0` acoustic).
- Cross-check `cosserat-mass-gap.md:132` `[canon]`: "the isotropic-solid longitudinal **P-wave** is `c_L = √(10/3)·c ≈ 1.826·c`… PR #392 reads it as the acoustic-manifold top `= 1.826` **inside the BZ**." The P-wave is a real acoustic Bloch branch, not a continuum-only construct.

**B4.2 — VERDICT: B4-FORCED is FALSIFIED.** The lattice has a gapless propagating longitudinal/compression branch that reaches DC. The binary's `2Ω` is deep in its passband. So the sleeper's hoped-for structural rescue — "the lattice realizes no independent P-branch, FLAG-A dissolves" — **does not win.** B4 does NOT close the port. `[derived]`

**B4.3 — Deviation surfaced (flag-don't-fix), NOT a fix.** The *isotropic* radiative speed `√(10/3)·c` the pulsar-exclusion arithmetic used (#753 §1.2, the `(c_shear/c_long)^5` factor) is tagged in `srs-band-structure.md:116` `[canon]` as a **"K=2G RE-EXPRESSION (GR-imported, PR #261), NOT lattice-emergent — no single lattice direction gives `10/3`; only the VRH (Voigt-Reuss-Hill) average does."** The lattice-real longitudinal speed is either the anisotropic `c_P` (`1.71–1.90 c_S`, vector survey) or `c_0` (scalar-channel acoustic branch, velocity factor `1/√3`, `:46`). This does NOT rescue B4 (the branch propagates and would radiate regardless of the exact speed), but it flags that the exclusion's `(c_s/c_L)^5` suppression rides a VRH/moduli construct, not a Bloch speed. Surfaced for the auditor-lane FLAG-A reconciliation; not fixed here (KB fence).

---

## §2 — Trace B2 (source-side projection): the tempting "tracelessness" rescue is FALSIFIED; the surviving B2 route reduces to B1

**Question (frozen):** does gravitating matter couple to the lattice ONLY through a shear / divergence-free projection (the bulk source term vanishing identically), even though the bulk branch exists? PASSES to B2-FORCED iff the radiative dilatation projection is DERIVED to vanish (a theorem, not an assumed symmetric coupling).

**B2.1 — The seductive rescue, stated so it can be killed.** The A1 channel is the SCALAR/trace/breathing sector. The mass second moment `M_ij = Σ_a m_a x_{a,i} x_{a,j}` has a **trace** `Σ_a m_a r_a²` that, for a circular binary, is **constant** (fixed separation). Tempting inference: "the A1/breathing sector sees only the (constant) trace ⇒ it does not radiate ⇒ B2-FORCED, the source-side vanishes." **The framework WANTS this to be true.** It is not.

**B2.2 — Why it FAILS `[derived]`.** A scalar field `θ` obeying `□θ = s` radiates at **quadrupole order** governed by the **traceless second moment of the scalar SOURCE** `s`, not by its trace (standard acoustic/scalar multipole radiation — the identical structure that gives every earthquake its P-arrival, Aki-Richards `E_S/E_P ≈ 23.4`, #753 §6 `[import]`). With the sector identity **mass = A1-dilatation** (`master-equation.md:20` `[canon]`), the scalar source is `s_a ∝ m_a δ(x − x_a)`, so its second moment IS the mass second moment `M_ij`, and its **traceless part rotates at `2Ω`** — nonzero. Reproduced by the driver (`check_2`): for a circular binary the trace `Σ m r²` is constant, **but** the traceless tensor's `xx` component varies (`std > 10⁻⁶`) — the traceless quadrupole genuinely rotates. So `⃛Q^{TL} ≠ 0` and the scalar quadrupole radiation IS driven. **The tracelessness rescue is dead** (consensus knife applied against the framework's own wish). This is exactly the scalar-GW derivation's §3.3 result (`#750` `[branch:#750]`), re-derived independently here and confirmed: monopole (mass conservation) and dipole (momentum conservation) are killed, but the quadrupole is NOT killed by any conservation law or by tracelessness.

**B2.3 — The ONLY surviving B2 route is not a source-vanishing; it is a change of coupling *channel* — which is B1.** The one way the gravitational source's radiative dilatation projection vanishes is if gravity does **not** couple to the vacuum as a dilatation body force `s ∝ ∇·f` (which drives the propagating compression branch), but instead as a **symmetric constitutive co-modulation** — the mass strains `ε_eff` and `μ_eff` *together*, `n(r) = 1 + 2GM/rc²`, preserving `Z = √(μ_eff/ε_eff) = Z₀` so `Γ = 0` everywhere (`master-equation.md:113` item 3 `[canon]`, "permanently strains the surrounding `ε_eff` and `μ_eff` fields symmetrically… preserving `Z₀`"; `einstein-field-equation.md:44-47` SYM `[canon]`; `translation-circuit.md:117` "SYM scaling… impedance-matched, `Γ=0`" `[canon]`). A symmetric (Z-preserving) index modulation **refracts** but launches no *reflected/impedance-mismatched* longitudinal wave — the radiated content of a `Z`-preserving source is carried by the impedance-*changing* (traceless/T2/shear) part, which is the observed GW. But this is **not** an independent source-vanishing theorem: it rests on the claim that gravity's coupling is the symmetric `(ε,μ)` co-modulation rather than a `∇·f` dilatation drive — which is the **mass = A1-dilatation grade-assignment**, tagged `[canon]` as **"RATIFIED-CONSISTENCY… NOT driver-validated"** (`cosserat-mass-gap.md:151`, `master-equation.md:29` `[canon]`: "No driver discriminates A1-mass from T2-mass"). So the surviving B2 route is not source-vanishing-by-theorem; it **reduces to the B1 question** (is the A1 gravitational coupling the Z-preserving/common-mode sector or an independent compression DOF?), and inherits B1's unforced choice.

**B2.4 — VERDICT: B2-FORCED is FALSIFIED as an independent trace.** No DERIVED source-vanishing theorem exists; the tracelessness route is dead, and the symmetric-coupling route reduces to B1 riding a consistency-class grade-assignment. `[derived]`

---

## §3 — Trace B1 (constraint structure, the GR-parallel): a genuine DERIVED closing mechanism — the K4 T_d common-mode rejection

**Question (frozen):** does the K4/TKI structure make the longitudinal gravitational sector non-dynamical — determined by the instantaneous matter distribution (elliptic `∇²φ = source`) rather than an independently radiating d'Alembertian DOF? Does the TKI (Ax2) mechanical↔EM isomorphism carry EM's longitudinal-photon kill (Gauss) to the mechanical A1 sector? What plays the Gauss-constraint role?

### §3.1 — The Gauss-constraint role IS played, and it is DERIVED group theory `[canon-read + derived]`

The corpus carries a **derived, empirically-confirmed, AVE-native** structure that makes the A1/longitudinal non-propagating — and it is not imported from QED, it is the K4 tetrahedral group theory:

- **The K4-TLM 4-port scatter is `S = ½·𝟙 − I`** (all-ones matrix minus identity; `k4-port-irrep-decomposition.md:65-67`, `clm-j550uh` `[canon]`). Under `T_d`, `V_{4-port} = A₁ ⊕ T₂`.
- **Its A1 eigenvector is the common-mode `(1,1,1,1)/2` with eigenvalue `+1`; the T2 traceless triplet has eigenvalue `−1`** (`:71-81` `[canon]`; reproduced by the driver `check_1`: spectrum `{+1,−1,−1,−1}`, A1 `+1`, T2 `−1`, `trace_S = −2`, exact).
- **The A1 common-mode is REJECTED and losslessly TRANSDUCED into T2** (`:113` `[canon]`, Ruling-21 2026-07-19): *"A₁ — common-mode 'DC' across all ports — has no spatial gradient in port space. Its reflection at bonds produces **destructive interference (common-mode rejection)** with neighboring nodes' A₁ components. The A₁ mode empties monotonically — its content is **transduced into the T₂ irreps**, not lost from the system."* Empirically the A1 port-correlation eigenvalue `→ 0` exactly, stable across time (`:97` `[canon]`).
- **This IS the substrate-native Gauss law** (`:118,:150` `[canon]`): *"longitudinal components (`∇·E ≠ 0`) are forbidden in vacuum by Gauss's law, so any A₁-type longitudinal excitation must empty… A₁ dissipating is the Gauss's-law constraint enforced automatically by `T_d` symmetry — NOT an additional postulate."* And it descends directly from the **Ax3 Lagrangian** `L_node = ½ε₀|∂_t A_n|² − (1/2μ₀)|∇×A_n|²` (`eq_axiom_3.tex` `[canon]`) — a **curl-only** potential energy with **no divergence/compression term**, whose "**U(1) gauge symmetry follow[s] as [a] Noether consequence." A curl-only Lagrangian is *exactly* the Maxwell structure that makes the longitudinal (`∇·A`) part non-dynamical / pure-gauge.

**So the Gauss-constraint role is played by the K4 `T_d` 4-port common-mode rejection** — the A1/longitudinal is the `+1` "DC" eigenmode that destructively self-interferes and transduces into the T2 shear. This is elliptic-constraint behavior (an instantaneous, non-radiating common mode), the direct analog of GR's longitudinal metric parts being constrained and EM's longitudinal photon being gauge-killed. `[derived from canon-read]`

### §3.2 — This is precisely the "structure the vacuum HAS and a rock LACKS" (the §6 obligation, discharged) `[derived]`

A **generic isotropic elastic solid (a rock)** is a spatial continuum with **no discrete 4-coordinated tetrahedral bond node** imposing a `T_d` common-mode scatter. In a rock the longitudinal (P) displacement is an **independent persisting normal mode** — which is why a rock radiates P-waves from any moment source (Aki-Richards `E_S/E_P ≈ 23.4`). In the **K4 vacuum**, the four bonds meeting at each node scatter via `S = ½·𝟙 − I`, whose A1 common-mode is the `+1` mode that **common-mode-rejects (destructive interference with neighbors) and transduces into T2** — the longitudinal common-mode is **non-persisting** (Gauss-constrained), not an independent radiating DOF. **The `T_d` 4-port common-mode-rejection scatter is the non-generic structure the vacuum has and the rock lacks.** A rock has no tetrahedral 4-port scatter to reject its compression common-mode; the K4 vacuum does. This directly answers §6: the vacuum's bulk sector is non-generic *because of its K4 `T_d` port topology*, and the closure comes from the same group-theoretic fact that identifies the photon as `T_2`-only. `[derived]`

### §3.3 — Consistency of B1 with the entire gravity canon (stress-tested against the framework) `[canon-read]`

The B1 mechanism does not merely fail to contradict the gravity canon — it is what the gravity canon already says, read in the port basis:
- **Gravity's field is the STATIC `n(r) = 1 + 2GM/rc²` gradient** (`master-equation.md:113` `[canon]`) — an elliptic/near-zone Newtonian potential (`∇²Φ = 4πGρ`), NOT a radiative `□`-wave. ✓ A1 constrained.
- **The radiative gravitational mode is `T₂` shear ONLY** (`einstein-field-equation.md:84` `[canon]`). ✓ The transduced-into-T2 output IS the observed GW; the mass's A1 coupling emerges as T2 shear, which is exactly what pulsar timing sees (a single quadrupole channel matched to GR, #753 §2.1).
- **The DM halo = the bulk channel's REACTIVE near-field** (`port register P9`, `deep-space-reactive-bulk-walk_RECORD.md` `[canon]`) — added-mass, stores-and-returns, NOT a port. ✓ B1's constrained-A1 = reactive near-field is exactly the halo reading. A constrained (elliptic) A1 is a fine static/reactive near-field (like the Coulomb field) — it just does not radiate.

Stress test (does B1 over-close and break mass = A1?): No. `mass = A1` is the *static* dilatation store (the trampoline depression, the standing reactive bulk-reactance; `master-equation.md:28-32` `[canon]`). B1 says the A1 is reactive-near-field/constrained, NOT that it is absent — the mass store is intact; only the *independent far-field radiative port* is closed. Fully consistent. `[canon-read]`

### §3.4 — Why B1 is NOT forced: the one unforced choice (flag-don't-fix) `[FLAG]`

The B1 mechanism (K4-TLM common-mode rejection) is derived and consistent — but it directly **contradicts** the srs-band survey's finding (§1) that the same K4/srs net, analyzed as **Cauchy site-elasticity**, DOES carry a gapless propagating P-branch (`c_P/c_S ≈ 1.71–1.90`, lattice-computed). The corpus carries **two dynamical models of the same K4 net**, with **opposite verdicts** on whether compression radiates, and does NOT adjudicate which governs the gravitational A1 coupling:

- **Model α — K4-TLM bond-scatter** (`k4-port-irrep-decomposition.md`, `photon-identification.md` `[canon]`): 4 *bond* scalar amplitudes per node; A1 = common-mode; `S = ½·𝟙 − I` **rejects/transduces A1 into T2** ⇒ longitudinal non-radiating ⇒ **B1, port closed exactly**.
- **Model β — srs Cauchy site-elasticity** (`srs-band-structure.md` `clm-bnd5rq` `[canon]`): 3 *site* displacement vectors; **P-branch propagates** (`c_P ≈ 1.8 c_S`), gapless, reaches DC ⇒ **Reading A, port open, EXCLUDED 9–110σ**.

**Verbatim contradiction, both sides (flag-don't-fix, not reframed):**
- Model α: `k4-port-irrep-decomposition.md:113` — *"The A₁ mode empties monotonically — its content is transduced into the T₂ irreps."*
- Model β: `srs-band-structure.md:78-89,120-122` — *"12 bands, 3 acoustic branches, two distinct speeds `c_P ≠ c_S`… [100] 1.71, [110] 1.85, [111] 1.90."*

Both are `[canon]`. The same leaf even carries the internal tension: `k4-port-irrep-decomposition.md:128` labels A1 as *"propagates at `c√2 = √(K_bulk/ρ)`"* while `:113` has it *"empty… transduced into T₂"* — a nominal bulk speed AND a common-mode rejection, on one line-range. **Which model owns the gravitational A1 far-field is the load-bearing unforced choice.** Physically it is genuinely two-sided: the mass IS a mechanical dilatation `∇·u ≠ 0` (favors Model β / radiate), yet its far-field signature IS the symmetric `Z`-preserving index gradient `n(r)` (favors Model α / constrained). The corpus flags this exact fork unresolved (`#750 §7.4`, port register FLAG-A, the `08_gravitational_waves.tex` warningbox). **Per the discipline, an unforced load-bearing choice ⇒ the B1 trace STOPS at UNDETERMINED with the fork stated — it is not promoted to B1-FORCED by fiat.** `[FLAG — Grant/auditor sector-ownership adjudication]`

**What would force it (named, not executed — Rule 12: the slot is not refilled with an assertion):** (a) a ruling/derivation that the K4-TLM common-mode scatter (Model α) is the vacuum's load-bearing *gravitational* A1 dynamics and the srs Cauchy P-branch (Model β) is a characterization of the net's elastic analog that does NOT own the radiative gravitational sector; OR (b) a derivation that the K4 `T_d` common-mode rejection applies to the *mechanical* dilatation (∇·u), not only the *EM-scalar* longitudinal (∇·E) — i.e. that the two A1's (`master-equation.md:20` two-"3"s: A1-dilatation-mass vs the Heaviside-excised EM longitudinal scalar) are the same Gauss-rejected mode. Note the two-"3"s leaf *already* identifies the A1-dilatation-mass AS "the Heaviside-excised longitudinal compression scalar" (`master-equation.md:18,20` `[canon]`), which leans toward (b) being derivable — but it is not yet derived, so it stays a named follow-on, not a claimed closure.

---

## §4 — FROZEN-BIN VERDICT + the decisive step per trace

| Trace | Frozen bin outcome | Decisive step |
|---|---|---|
| **B4** (band-structure sleeper) | **B4-FORCED FALSIFIED** — does NOT close the port | The adjudicated survey `clm-bnd5rq` shows a **gapless propagating compression branch reaching DC** (`c_P/c_S ≈ 1.71–1.90`, no stop-band); the sleeper's "no P-branch" rescue is dead (§1.2). |
| **B2** (source projection) | **B2-FORCED FALSIFIED** as an independent trace | The **tracelessness rescue is dead** — a scalar field's quadrupole radiation is driven by the *traceless* second moment, which rotates (`⃛Q^{TL} ≠ 0`, driver `check_2`); the surviving symmetric-coupling route **reduces to B1** riding a consistency-class grade-assignment (§2.2–2.3). |
| **B1** (constraint / GR-parallel) | **UNDETERMINED, leaning B1-FORCED** | A **derived AVE-native closing mechanism exists** — K4 `T_d` 4-port common-mode rejection `S = ½·𝟙 − I` transduces the A1/longitudinal into T2 (substrate-native Gauss law) — the "structure the vacuum has, rock lacks" (§3.1–3.2); it WOULD close the port exactly and is consistent with all gravity canon (§3.3). **But it rests on ONE unforced choice** (K4-TLM Model α vs srs-Cauchy Model β ownership of the gravitational A1) that the corpus carries unresolved ⇒ STOP at UNDETERMINED, fork stated (§3.4). |

**Overall frozen-bin verdict: UNDETERMINED (leaning B1-FORCED).** The exclusion does NOT go live (NONE-DERIVES is *not* reached — a genuine closing mechanism is available), but neither is the port forced closed (B1-FORCED is *not* reached — its ownership of the gravitational A1 is an unforced choice). The entire question has been **collapsed from a three-trace menu onto a single, sharply-stated model-ownership fork**: does the gravitational A1-dilatation obey the K4-TLM common-mode scatter (port closed exactly) or the srs Cauchy elasticity (port open, excluded)? **The ruling is Grant's/the auditor's** (sector-ownership adjudication).

**Anti-seduction self-audit (the fence held).** NONE-DERIVES was genuinely reachable and I actively tested for it: if B4 had shown a gapless P-branch AND B2's source drove it AND no constraint killed it, the exclusion would go live. B4 and B2 *do* clear the first two conditions — the branch exists and the source drives it. The ONLY thing standing between "exclusion goes live" and "port closes" is the B1 K4-common-mode-rejection constraint, whose applicability is the unforced choice. I did not manufacture that constraint to rescue the framework — it is pre-existing DERIVED group theory (`clm-j550uh`, the same fact that identifies the photon) — but I also did not let its existence upgrade the verdict past what is forced. Both the tracelessness rescue (§2.2) and the "sleeper" rescue (§1.2) were killed against the framework's wish.

---

## §5 — The residual (chord-potential), stated both ways

**IF B1 governs (Model α — K4 common-mode rejection):** the port closes **EXACTLY**, residual `F_bulk/F_shear ≡ 0`. The K4 scatter `S = ½·𝟙 − I` is exact and unitary; the A1 transduction into T2 is complete (empirically the A1 eigenvalue `→ 0` exactly, `k4-port-irrep-decomposition.md:97` `[canon]`). The only conceivable nonzero residual is finite-`k` lattice mode-mixing that leaks a sliver of A1 back out, bounded by `(ω·ℓ_node/c)²`. Evaluated (driver `check_3`, `L_NODE`/`C_0` read-only):

| System | `ω_GW` [rad/s] | `ω_GW·ℓ_node/c` | residual bound `(ω ℓ_node/c)²` |
|---|---|---|---|
| Hulse-Taylor B1913+16 | `4.5×10⁻⁴` | `5.8×10⁻²⁵` | **`3.4×10⁻⁴⁹`** |
| double pulsar J0737-3039 | `1.4×10⁻³` | `1.8×10⁻²⁴` | **`3.4×10⁻⁴⁸`** |

So even the lattice-leakage residual is `~10⁻⁴⁸` — **unobservable at ANY conceivable pulsar-timing precision** (the double-pulsar bound `1.3×10⁻⁴` tightening toward SKA `~10⁻⁶` never approaches `10⁻⁴⁸`). B1's prediction is **exact-null, for all practical purposes.** `[derived]`

**Is the exact-null an AVE-DISTINCT chord? NO (ave-discrimination-check).** GR *also* predicts exactly zero scalar-GW (the longitudinal metric parts are pure-gauge). An exact-null that reproduces GR is a **consistency requirement, PEER-with-GR, not an AVE-distinct chord.** The only chord-eligible content would be a *derived nonzero-but-suppressed* residual — a number a next-gen pulsar array could chase. **The K4 scatter is exact/unitary, so no such nonzero residual is derived.** Hence: **if B1 governs, there is NO positive AVE-distinct forward prediction here — AVE is peer-with-GR (both: pure-tensor forever).** The honest chord-ledger entry is a null.

**IF Reading A governs (Model β — Cauchy P-branch radiates):** `F_bulk/F_shear ≈ 0.03–0.12` (#753 §1.2), **already EXCLUDED at 9–110σ (Hulse-Taylor) / 100–1400× the double-pulsar bound** — the framework is **falsified** in that reading (a clean, bankable negative, Rule 11).

**Net residual statement:** the chord-potential is empty either way — `(exact-null, peer-with-GR)` if B1 governs, or `(excluded/falsified)` if Reading A governs. There is **no derived nonzero residual** and therefore **no chord-eligible number** for next-generation pulsar timing. This matches the framework-wide finding that no AVE-distinct chord lives *inside* the corpus (uniformly peer-with-SM/GR); any chord would live only in a forward prediction, and this sector does not supply one.

---

## §6 — Calibration-vs-derived ledger + owed-follow-ons

### §6.1 — Ledger (`consistency-vs-emergence` tags)

| Quantity | FORM | VALUE | Class |
|---|---|---|---|
| K4 scatter spectrum `{+1,−1,−1,−1}`; A1=`+1` common-mode, T2=`−1` triplet | `[derived]` (`T_d` group theory, driver `check_1`) | dimensionless | **MANIFESTATION** (theorem) |
| A1 common-mode rejection / transduction into T2 (substrate-native Gauss) | `[canon-read]` (`clm-j550uh`, Ruling-21) | — | manifestation (`T_d`-forced, empirically A1→0) |
| "structure vacuum has, rock lacks" = K4 `T_d` 4-port scatter | `[derived]` | — | manifestation (discharges §6 obligation) |
| B4 lattice P-branch exists (gapless, `c_P/c_S≈1.71–1.90`) | `[canon-read]` (`clm-bnd5rq`) | dimensionless | consistency/characterization |
| B2 traceless quadrupole `⃛Q^{TL}≠0` (tracelessness rescue dead) | `[derived]` (driver `check_2`) | — | manifestation (multipole theorem) |
| mass = A1-dilatation (the coupling grade-assignment) | `[canon-read]` | — | **consistency (NOT driver-validated)** — the load-bearing unforced input |
| residual `F_bulk/F_shear ≡ 0` (if B1) + lattice bound `~10⁻⁴⁸` | `[derived]` | dimensionless | manifestation (exact scatter + finite-`k` bound) |
| `ω_GW`, `ℓ_node`, `c` (residual evaluation) | — | `[import]`/`[canon]` (pulsar `P_b`; `L_NODE`,`C_0`) | import/consistency |

No emergence-class claim is headlined. The deliverable is the frozen-bin verdict + the exact-null-peer-with-GR residual; both ride on the B1 fork, not on a hidden calibration.

### §6.2 — Owed-follow-ons (fenced; not executed here — Rule 12)

1. **The B1 model-ownership ruling** — Grant/auditor sector-ownership adjudication: does the gravitational A1-dilatation obey the K4-TLM common-mode scatter (Model α) or the srs Cauchy elasticity (Model β)? *Grant-gated physics ruling first; then auditor lands any leaf.* This is the same ruling the Q1 row (#753 §4) and FLAG-1/D5 (#750 §8) already owed — this lane supplies the *mechanism* (K4 `T_d` common-mode rejection) that Model α would use, and names exactly what would force it (§3.4 a/b).
2. **If Model α (B1) is ruled:** a derivation that the K4 `T_d` common-mode rejection applies to the *mechanical* dilatation `∇·u` (not only the EM-scalar `∇·E`) — the §3.4(b) follow-on, leaning on the `master-equation.md:20` identification of the A1-dilatation-mass as the Heaviside-excised longitudinal scalar. *New lane, own version + verification chain (Rule 12).*
3. **The `08_gravitational_waves.tex` warningbox + FLAG-A speed-label reconciliation** — resolves *with* the ruling (auditor lane; not edited here).
4. **NOT owed:** a nonzero-residual chord driver — because §5 shows the residual is exact-null (peer-with-GR) or excluded; there is no chord-eligible number to pin.

**None of items 1–4 are executed here.** The B1 slot stays **UNDETERMINED** (not refilled with an asserted resolution); this lane *frames and hardens* the fork by supplying the derived closing mechanism and collapsing the three-trace menu onto one model-ownership choice, and leaves the ruling to Grant.

---

> **Derivation-doc provenance.** Fired by Grant 2026-07-20 (`"fire"` on the Reading-B mechanism derivation). Frozen bins pre-registered ALONE before deriving (`_prereg-FROZEN.md`, committed `9ad1831d`). All `[canon]` citations content-verified two-method at HEAD `e2e870c0` (verify-before-cite). FORMs `[derived]` by `T_d` group theory + standard multipole algebra; the K4 scatter eigenstructure, the traceless-quadrupole cross-check, and the lattice-leakage residual are reproduced by `research/drivers/b_mechanism_k4_commonmode_residual.py` (+ `_results.json`), which imports `ave.core.constants` read-only and touches no engine primitive. Mints no `clm-`; propagates to no leaf; READ-ONLY on KB; owed follow-ons fenced to §6.2. **Verdict: UNDETERMINED leaning B1-FORCED — B4 falsified (lattice HAS a gapless compression branch), B2-via-tracelessness falsified, and a derived AVE-native closing mechanism (K4 `T_d` common-mode rejection = the "structure the vacuum has and a rock lacks") exists and would close the port exactly, but rests on one unforced model-ownership choice the corpus carries unresolved. Residual: exact-null (peer-with-GR, no distinct chord) if B1 governs, else excluded/falsified.** Companion: the pre-reg (`_prereg-FROZEN.md`), the Q1 hardening (#753), the scalar-GW derivation (#750), the port register, and the docket continuation (ENTRY 30).

