[↑ Orchestration Index](index.md)

# Wall-Branch Fork (H3): the electron's Γ=−1 wall — MAGNETIC or CAPACITIVE saturation?

**Lane founded:** 2026-06-15 · **Branch:** `analysis/2026-06-15-wall-branch-fork` (off `main` @ `40a2a2e7`) · **Worktree:** `AVE-Core-wall-wt` · **Status:** ACTIVE — Phase 1 (corpus map + prereg)

**Arc:** corpus-grep prereg → Rule-11 freeze → auditor-gate → driver → result → adjudicate to Grant. `main` PROTECTED; all edits via reviewed PR; **Grant merges**.

---

## 1. Charter (derivation target)

Which saturation branch forms the electron's Γ=−1 confining wall?

- **MAGNETIC** branch: $\mathbf{B}$ saturates $\mu_{eff}\to0$ first → $Z=\sqrt{\mu_{eff}/\varepsilon_0}\to0$ → Γ→−1 (short). [`master-equation.md`:85, `clm-lv3uw1`]
- **CAPACITIVE** branch: the local topological twist drives dielectric saturation $C_{eff}\to\infty$ → $Z_{core}=\sqrt{\mu_0/C_{eff}}\to0$ → Γ=−1. [`resonant-lc-solitons.md`:29–46, `clm-kezk9z`]
- **THIRD config (reserved, NOT the wall):** ε-rupture → $\varepsilon_{eff}\to0$ → $Z\to\infty$ → the anti-confinement / opaque / photon branch. [`master-equation.md`:84] — distinguish, do **not** conflate.

**Discriminator (charter):** the branch (μ vs ε) that reaches Z→0 *first* and *stably confines* = the wall mechanism. **If degenerate / co-saturating → report it** (a real result; informs the A1-vs-T2 fork).

**Knock-on (flag-don't-fix to Grant):** this couples to the **A1-vs-T2 mass-sector fork** — magnetic/μ ↔ T2 inductive/micro-rotation (charge-"3" winding); capacitive/ε ↔ A1 dilatation/E (mass-"3"). The result tells which "3" carries the mass.

---

## 2. ⚠ CRITICAL PRE-FINDING — this is NOT a green-field fork (ave-prereg payoff)

The corpus is **already self-aware of this exact fork** and has worked it substantially. The prompt's grounded-starting-state did not mention this; verified 2026-06-15. The fork is a **named open flag (FLAG-2)** with a layered, *partially self-contradictory* corpus state and a recent (2026-06-13) candidate **gauge-dissolution**. Verbatim, verified:

### 2a. It is already FLAG-2
`vol4/claim-quality.md`:1256 (clm-fd1e7a) + `cvr-dc-operating-point.md`:55 (AUDITOR_STATE FLAG-2):
> "which constitutive parameter moves at the wall (capacitive $C_{eff}\to\infty$ vs magnetic $\mu_{eff}\to0$) … **both routes give the same $Z=Z_0\sqrt{S}$ curve, so the bundle is robust but the attribution is unsettled.** **Magnetic is PRIMARY** per the handoff; the capacitive route is the flagged co-attribution."

→ **The equilibrium impedance observable $Z=Z_0\sqrt{S}$ is DEGENERATE between the two branches by the corpus's own admission.** The naive "which reaches Z→0 first" on the operating-point curve cannot discriminate. The charter anticipated this ("if degenerate → report it").

### 2b. `clm-lv3uw1` (magnetic) is INPUT-ONLY
The magnetic-branch claim is tagged an asserted **input**, not a derived result (`vol4/claim-quality.md`:1268 "rests on the input-only clm-lv3uw1").

### 2c. 2026-06-02 Grant-adjudicated dual-branch table (`dual-reactance-storage-taxonomy.md`:193-206)
| Branch | Saturates | Z, Γ | Sector | Outcome |
|---|---|---|---|---|
| **Electric** | $\varepsilon_{eff}\to0$ (μ intact) | $Z\to\infty$, Γ→+1, open | **X_C** (capacitive/transl-E) | **τ_yield** (dielectric breakdown) |
| **Magnetic** | $\mu_{eff}\to0$ (ε intact) | $Z\to0$, Γ→−1, short | **X_L** (inductive/microrot-B) | **rest mass** (Fermion confinement), clm-lv3uw1 |

Claims branch↔sector is "**canonical, not asserted**" via `translation-circuit.md`:464,526.

### 2d. ⚠ DIRECT CONTRADICTION (the heart of the fork)
- **Taxonomy (2c):** the **capacitive/X_C** sector saturating → $\varepsilon_{eff}\to0$ → **Z→∞** → τ_yield/rupture (NOT the electron wall).
- **`resonant-lc-solitons.md`:29-46:** the **capacitive** sector saturating → $C_{eff}\to\infty$ → **Z→0** → the electron wall (Γ=−1).

Same dielectric sector, **opposite** impedance limit. The pivot is the INVARIANT-S2 specialization $C_{eff}=C_0/S\;(\uparrow\infty)$ **vs** $\varepsilon_{eff}=\varepsilon_0 S\;(\downarrow0)$ — C and ε move *oppositely* in the AVE kernel, so "dielectric sector saturates" gives Z→0 in the C-form and Z→∞ in the ε-form. `cvr-dc-operating-point.md`:57 acknowledges the convention pair but sidesteps it by using the convention-independent $Z=Z_0\sqrt{S}$ form — which is exactly what makes the attribution degenerate.

### 2e. 2026-06-13 candidate gauge-dissolution (MOST RECENT; `cvr-reflection-smith.md`:67)
> "the apparent $\mu_{eff}\to0$-vs-$C_{eff}\to\infty$ split is **partly the two gauge sides of one wall** ($Z\to0$ inside ↔ $Z\to\infty$ outside, Möbius $Z\leftrightarrow1/Z$, $|\Gamma|=1$) — **not a physical branch.** The physical, gauge-invariant axis is the **two-'3's** (mass-dilatation ⊥ charge-winding; `master-equation.md`:20)."

→ The corpus already proposes the fork **largely reduces to the A1-vs-T2 / two-"3"s question**, with the Z→0/Z→∞ μ-vs-C distinction substantially a **gauge** (inside/outside Möbius) artifact. "**Partly**" = NOT a complete dissolution; a genuine sector residue remains. Consistent with memory `project_electron_two_threes_vortex_ring` (SECTOR⊥GAUGE advance).

**Working thesis (to verify, not assume):** the magnetic-vs-capacitive *impedance* fork is **not an independent physical branch** — the equilibrium observable is degenerate, the Z→0/∞ sign is gauge (Möbius inside/outside), and the genuine physical content is the **A1(ε/dilatation/mass-"3") vs T2(μ/microrotation/charge-"3") sector** question: *does the electron's confining excitation load the ε-sector (a STATIC dilatational twist — INVARIANT-S2: a static field has no ∂B/∂t, loads ε-only) or the μ-sector (a circulating winding current)?* INVARIANT-S2's static-field rule leans **ε/capacitive/A1**; `clm-lv3uw1` asserts **magnetic/T2 PRIMARY**. These conflict — the live flag.

---

## 3. MODE / REGIME / PHASE-STATE declaration (ave-regime-phase-state-check)

Declared before any run, per discipline:
- **MODE:** longitudinal-bulk dielectric (ε / A1 / capacitive `X_C`) **and** microrotational inductive (μ / T2 / `X_L`) saturation at the soliton **core/wall**. NOT EM-transverse propagation. The observable is a **boundary impedance** (Γ at the core↔ambient interface), rendered as a boundary condition (Op17-bounded), not a bulk force term (substrate-native-check CP10).
- **REGIME:** **near-yield / saturating** ($S\to0$, $A\to A_{yield}$). The wall exists only at saturation; linear-regime statements are off-target. Two sub-regimes matter and must be kept distinct: (i) the **formation transient** (which reactance's kernel argument reaches 1 *first* as the soliton assembles) — the charter's discriminator; (ii) the **formed operating point** ($A_\star\to1$, residual $\sqrt{S_\star}\approx\alpha/4$) — where Z is degenerate.
- **PHASE-STATE:** forming → formed **bound resonator** (a confined soliton = the electron). Bound-resonator-class, not free-propagating. Q baked in as $Q_e=1/\alpha$ at the operating point.

---

## 4. Discriminator design (substrate-native, NON-degenerate)

The equilibrium Z curve is degenerate (§2a). Candidate discriminators that are NOT degenerate:
1. **Formation-order (engine):** instrument whether $C_{eff}(V)$ [varactor] or $L_{eff}(I)$ [varinductor] (`cosserat_field_3d.py`:411-413) reaches its kernel argument = 1 **first** as a soliton forms on `crystal_engine` / `master_equation_fdtd` (the A1-cage's engine home — harness lacks the cage, per index 2026-06-13 addendum). Requires the engine to evolve BOTH reactances independently (S_μ, S_ε tracks) — VERIFY it does.
2. **Energy-sector / static-loading (analytical):** which sector does the electron's *defining* excitation load? The static topological twist (charge="3", winding) — does it load ε-only (INVARIANT-S2 static-field rule → A1/capacitive) or drive a circulating current → μ (T2/magnetic)? Virial says E_C = E_L = ½m_ec² at equilibrium (degenerate on energy *partition*), so the discriminator is FORMATION-order / which-saturates-first, not equilibrium energy.
3. **Gauge vs physical test:** is the μ↔C, Z↔1/Z, Γ-sign distinction a Möbius gauge pair (one wall, two frames) or two physically distinct walls? If gauge → the fork dissolves into the two-"3"s axis (the 2026-06-13 thesis).

**Adjudication rule:** branch reaching Z→0 first AND stably confining = wall mechanism. Degenerate/co-saturating / gauge-dual → report degeneracy + relocate to the A1-vs-T2 axis.

---

## 5. Arc plan (phases)

- **Phase 1 — corpus map + prereg** (IN PROGRESS): exhaustively verify the fork's full corpus state (close gaps: `translation-circuit.md`:464,526; `trampoline-framework.md`:641 §6.1 Möbius; cvr-ee-sweep handoff; vol3 `bulk-impedance-at-saturation-boundary` + `electron-bh-isomorphism`; L3 archive); ADVERSARIALLY verify the §2d contradiction + the §2e gauge-dissolution; check engine reality (does crystal_engine/cosserat evolve C_eff vs L_eff independently?). Then write + **Rule-11 freeze** the prereg.
- **Phase 2 — auditor-gate:** ave-auditor reviews the frozen prereg + contradiction map against verified corpus state.
- **Phase 3 — driver:** analytical adjudication (constitutive law + static-field loading + gauge test) + optional engine formation-order probe; adversarially verified.
- **Phase 4 — result + adjudicate to Grant:** result doc; flag-don't-fix the precise state + recommendation + A1-vs-T2 knock-on; inline options for Grant.

## 6. Open questions for Grant (stub — populated at Phase 4)
- (pending Phase 3)

## 7. Verified-citation ledger (verify-before-cite)
| Claim | Source | Verified |
|---|---|---|
| Magnetic branch = wall (Z→0, Γ−1) | `master-equation.md`:85, clm-lv3uw1 | ✅ 2026-06-15 read |
| ε-rupture = Z→∞ (third config) | `master-equation.md`:84 | ✅ |
| Capacitive branch = wall (C_eff→∞, Z→0) | `resonant-lc-solitons.md`:29-46 | ✅ |
| FLAG-2 / Z=Z₀√S degenerate / magnetic PRIMARY | `cvr-dc-operating-point.md`:55 | ✅ |
| 2026-06-02 dual-branch table | `dual-reactance-storage-taxonomy.md`:193-206 | ✅ |
| 2026-06-13 gauge recontextualization | `cvr-reflection-smith.md`:67 | ✅ |
| varactor C_eff + varinductor L_eff (two reactances) | `cosserat_field_3d.py`:411-413 | ✅ |
| branch↔sector "canonical" | `translation-circuit.md`:464,526 | ⏳ Phase 1 |
| Möbius gauge pair | `trampoline-framework.md`:641 §6.1 | ⏳ Phase 1 |

> NOTE on line-number drift: claim-quality/taxonomy cite `master-equation.md`:78-79,81 for the branch text; the live `.md` carries it at :84-87. Content verified; cite the live `.md` lines.
