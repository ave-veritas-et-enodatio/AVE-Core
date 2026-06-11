# Quarter-Fence Verdict Note (billiard/mirror ¼ candidate — reconstruction-stop + the licensed lane)

**Date:** 2026-06-10
**Branch:** `analysis/2026-06-10-survey-verdicts-consolidation`
**Provenance:** Read-only survey workflow (2026-06-10). No engine runs, no corpus mutation. Every file:line re-verified live in this worktree (verify-before-cite governing). One number (ρ̄_wall≈0.304) is a **branch-local, unmerged** result and is tagged as such; one ":7" cite is disambiguated. No origin/main cite FAILED re-verification.
**Status:** FINDINGS FROZEN. The ¼-*selection* lane is RECONSTRUCTION-STOPPED; a distinct PHASOR-NATIVE mirror-quantization lane is recorded as LICENSED-BUT-GATED. Grant's 6-DOF reframe recorded as a candidate second route to (2,3).

---

## §0 Verdict

Grant's billiard / mirror-quantization ¼ candidate is a **RECONSTRUCTION-STOP** per `challenge-canonical-negative` — it is the **same mechanism class** as the 2026-06-04-falsified "half-wave cavity in both quadratures." It does not get a third pass. **But** a genuinely distinct, corpus-novel lane (phasor-native billiard-unfolding in $(V_{inc}, V_{ref})$) survives as **LICENSED-BUT-GATED**.

---

## §1 The ¼-selection lane is reconstruction-stopped

- The billiard/mirror ¼ candidate reconstructs the **same selection-mechanism class** as the falsified "**half-wave cavity in both quadratures**": [`2026-06-04_ee-rf-quadrature-coupling-and-alpha-quarter-hypothesis.md:77-81`](../research/2026-06-04_ee-rf-quadrature-coupling-and-alpha-quarter-hypothesis.md) — "the $1/4$ is 'a half-wave cavity in both quadratures' … **→ GATE (b) OUTCOME 2026-06-04: it does NOT** … tested against every prior attempt and FALSIFIED; Class B holds."
- The anti-pattern marker that **pre-banned a third pass** is at [`2026-06-04_alpha-quarter-adversarial-rechallenge.md:7`](../research/2026-06-04_alpha-quarter-adversarial-rechallenge.md) — "reconstructed twice … and falsified twice … is not reconstructed a **third** time." (Disambiguation: the anti-pattern marker is in the *rechallenge* doc at :7, NOT in the ee-rf-quadrature doc at :7.)

## §2 The ½ is DOUBLE-BOOKED (CANONICAL)

The "½" the billiard story wants to *derive* is **already derived twice, from two different axioms** — so a third derivation adds nothing:

- **R − r = ½** from Ax-2 tube tangency: [`ch8-alpha-golden-torus.md:45`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md) — "centerline separation $2(R-r)$ must equal the tube diameter $d$ $\Rightarrow R - r = 1/2$."
- **R · r = ¼** from the phasor-area=Nyquist identification: [`ch8-alpha-golden-torus.md:46`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md) and [lines 56-57](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md) — "$\pi R r = \pi(d/2)^2 \Rightarrow R\cdot r = 1/4$ at $d = 1\,\ell_{node}$."

The ¼ enters as the **named phasor-area=Nyquist identification**, not as a new resonance selection. A billiard ¼ would be a **third restatement of "it's a half-thing"** — the over-determination tell, per [`rechallenge:54`](../research/2026-06-04_alpha-quarter-adversarial-rechallenge.md) (§5).

## §3 The harvest

### (a) U6 SETTLED — R, r are phasor semi-axes (CANONICAL)

- $R, r$ are **PHASOR SEMI-AXES in $(V_{inc}, V_{ref})$**: [`ch8-alpha-golden-torus.md:52`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md) — "for an elliptical trajectory with semi-axes $(R, r)$ in $(V_\text{inc}, V_\text{ref})$-coordinates."
- The **real-space envelope ratio ≈ 2.27** is a **DIFFERENT canonical quantity** (not $\varphi^2 = 2.618$): archive [`26_step5_phase_space_RR.md:193`](../research/_archive/L3_electron_soliton/26_step5_phase_space_RR.md) ("R/r ≈ 2.27 in REAL space, not 2.618 = $\varphi^2$") + [`78_canonical_phase_space_phasor.md:88`](../research/_archive/L3_electron_soliton/78_canonical_phase_space_phasor.md) ("TLM real-space R/r ≈ 2.27 attractor").
- The **phasor↔real-space area bijection is CLOSED-NEGATIVE (absorbs α)**: [`2026-06-04_alpha-class2-bijection-result.md:10`](../research/2026-06-04_alpha-class2-bijection-result.md) — "closing the bijection … **requires substituting the empirical value of α** … forces $R\cdot r \to 4\pi^2\alpha \approx 0.288$ … **B3 FAILS → Class B**."
- **Consequence for the mfg-flow FBD:** the manufacturing-flow free-body comparison should read against **2.27 (real-space)**, not $\varphi^2$ (phase-space). (Branch-local, PR #164: the coax-secondary Arm-2 closed the real-space $A\to1$ route — "2.27 requires a fitted $\bar{\rho}_{wall} \approx 0.304$"; **this number is on the unmerged PR #164 branch, not in origin/main** — see §Verification.)

### (b) (4,6) is a 2-component LINK, not a knot (CANONICAL)

[`torus-knot-uniqueness.md:67-71`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md) — "If $\gcd(p,q)=d>1$ … is a **$d$-component LINK** (multiple disjoint loops)." $\gcd(4,6)=2 \Rightarrow$ a **2-component link**, not a single-component knot. (The rule is at 67–71; (4,6) follows from it directly.)

### (c) The 6-face cell is the ENGINE VOXEL, not the real cell (open strengthen-by)

[`k4_tlm.py:103`](../src/ave/core/k4_tlm.py) — `K4Lattice3D`: "3D lattice of K4 nodes **embedded in a Cartesian grid**" (a 6-faced cubic voxel). The **real $I4_132$/Laves cell has 4-port $T_d$ junctions** and an **UNDEFINED Brillouin-zone face inventory** — open strengthen-by; the "6-face" count is an engine-representation artifact, not the substrate cell's face count.

## §4 The LICENSED lane (corpus-novel, Grant-gated)

A **PHASOR-NATIVE mirror-quantization** argument is genuinely distinct from the reconstruction-stopped ¼-selection lane:

- The $\Gamma = -1$ TIR wall **is canonically a literal mirror in $(V_{inc}, V_{ref})$** (the impedance-mismatch boundary). A **billiard-unfolding** argument in that phasor plane is **corpus-novel** — never applied to the Clifford torus.
- **Precedent (two-mirror geometric-mean quantization, already canonical):** [`first-principles-bond-force-constants.md:28`](../manuscript/ave-kb/vol5/molecular-foundations/organic-circuitry/first-principles-bond-force-constants.md) — $d_0 = 2\sqrt{r_A\cdot r_B}$ ("one-electron Fabry–Perot eigenvalue"; H$_2^+$: $d_0=2a_0$, exact-QM match at line 33), **coexisting** with the de Broglie ring $2\pi r = n\lambda$ ([`de-broglie-standing-wave.md:52,80,86`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md)). Two quantization conditions already coexist for the electron — but neither has been applied to the Clifford torus.
- **GATE:** licensed *only* through [`rechallenge:54`](../research/2026-06-04_alpha-quarter-adversarial-rechallenge.md) (§5) — it must make a **discriminating secondary prediction** the over-determined ½-stories do not, **and the substrate must confirm THAT**. Absent that, it remains Class-B pedagogy.

## §5 Grant's 6-DOF reframe — candidate second route to (2,3) (hypothesis, Grant-gated)

Recorded as the substrate-native candidate **SECOND ROUTE to (2,3)**: **2 sectors ($u$/$\omega$) × 3 components**, with **$p=2$ = sector alternation** and **$q=3$ = chiral component cycle**. This is a Grant reframe, not yet a corpus claim; recorded for the auditor lane to track. It would be the discriminating-secondary the §4 gate demands **only if** it predicts something the area-identification route does not.

---

## §6 Class-tag table

| Claim | Cite (re-verified) | Class |
|---|---|---|
| ¼-selection = same class as falsified half-wave-cavity | `ee-rf-quadrature…:77-81` | RECONSTRUCTION-STOP |
| Anti-pattern marker pre-bans a third pass | `rechallenge:7` (not ee-rf:7) | CANONICAL (gate) |
| R−r=½ (Ax-2 tangency) double-booked with R·r=¼ (phasor-area=Nyquist) | `ch8:45`; `ch8:46,56-57` | CANONICAL |
| R, r are phasor semi-axes in $(V_{inc},V_{ref})$ (U6) | `ch8:52` | CANONICAL |
| Real-space ratio ≈2.27 ≠ phasor φ²; bijection absorbs α | `26…:193`; `78…:88`; `alpha-class2-bijection:10` | CANONICAL / CLOSED-NEGATIVE |
| 2.27 requires fitted ρ̄_wall≈0.304 | PR #164 branch (unmerged) | **branch-local, NOT origin/main** |
| (4,6) is a 2-component link, not a knot | `torus-knot-uniqueness.md:67-71` | CANONICAL |
| 6-face cell = engine voxel ≠ real $I4_132$/$T_d$ cell | `k4_tlm.py:103` | CANONICAL (open strengthen-by) |
| Phasor-native mirror-quantization (billiard-unfold) | precedent `first-principles-bond-force-constants.md:28` + `de-broglie:52` | LICENSED-BUT-GATED (corpus-novel) |
| 6-DOF reframe (2 sectors × 3 components) → (2,3) | Grant reframe | hypothesis, Grant-gated |
| Coax-ring secondary ran the gate, license-pending-re-run | PR #164 (OPEN, floor-limited) | Grant-gated (in-flight) |

## §7 KB-action / Grant-gated queue

- **GATED (Grant):** the phasor-native mirror-quantization lane (§4) is licensed but must clear `rechallenge:54`'s discriminating-secondary bar before any α-¼-emergence framing. Do NOT reopen the ¼-*selection* lane (reconstruction-stopped, §1).
- **IN-FLIGHT:** PR #164 (branch `analysis/2026-06-10-coax-ring-secondary`, **OPEN**) ran the §5 gate and returned **license-pending-re-run (floor-limited)** — its title reads "§5 license withheld pending re-run; real-space $A\to1$ route closed honest." The ρ̄_wall≈0.304 fit lives there, not in origin/main.
- **CANDIDATE (auditor lane):** Grant's 6-DOF reframe as a tracked second-route-to-(2,3) hypothesis. Implementer surfaces; auditor tracks.

---

## §Verification (verify-before-cite, re-grepped live 2026-06-10)

- **DISAMBIGUATED CITE:** the "anti-pattern marker :7" is `2026-06-04_alpha-quarter-adversarial-rechallenge.md:7` (the genuine anti-pattern marker — "reconstructed twice … falsified twice … not a third time"). The ee-rf-quadrature doc's own line 7 is a *contradiction-note*, NOT an anti-pattern marker; cited the rechallenge doc.
- **BRANCH-LOCAL NUMBER:** `ρ̄_wall ≈ 0.304` did **not** appear in origin/main (`grep` over `research/` + `manuscript/` = no `rho_wall`/`0.304` co-occurrence in a coax result doc). It is a result on the **OPEN, unmerged PR #164** branch `analysis/2026-06-10-coax-ring-secondary` (branch confirmed to exist; PR #164 state = OPEN). Tagged in-flight, not asserted as canon — consistent with the source survey's own "license-pending-re-run" framing.
- **(4,6) note:** `torus-knot-uniqueness.md:67-71` states the general $\gcd=d>1 \Rightarrow d$-component-link rule and lists examples [(2,2),(3,3),(2,4),(4,2),(3,6)]; (4,6) is not listed verbatim but follows directly ($\gcd(4,6)=2$).
- **k4_tlm.py:103** is the `K4Lattice3D` docstring ("embedded in a Cartesian grid"); the "6-face" reading is the cubic-voxel face count of that Cartesian embedding (verified in context), contrasted with the real $T_d$-junction cell.
- All other §1–§5 origin/main cites re-verified verbatim. No origin/main cite FAILED.
