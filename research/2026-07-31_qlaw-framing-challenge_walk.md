# Q-law — ADVERSARIAL FRAMING CHALLENGE + VACUUM-CIRCUIT MAPPING (pre-derivation walk material)

**Date:** 2026-07-31
**Lane:** implementer, framing-challenge mode (no derivation, no pre-reg, nothing minted)
**Status:** 🟡 WALK MATERIAL — this document exists to be walked with Grant, not to be believed
**Provenance:** Grant's conditional yes on the cold-Q derivation, 2026-07-31, verbatim `[sic]`:
*"Yes but challenge all framing, assumptions, and map to the vacuum circuits and physical lattice walk first"*.
Upstream: [`research/2026-07-30_qlaw-derivation_scoping.md`](2026-07-30_qlaw-derivation_scoping.md)
(routes R1–R6, findings F1–F9, walk questions Q1–Q8) — read that first; this document
**challenges** it rather than extending it.

## What this document is NOT

- **NOT a derivation.** No solver was run. No route was pursued. No `Q` was computed.
- **NOT a pre-registration.** No bin is frozen. The success bins stay in the upstream scoping doc, DRAFT.
- **NOT a claim.** No claim-id is minted. No existing claim's solidity is changed. No corpus file is modified.
- **NOT an adjudication.** Every fork below is *surfaced with both paths*; none is picked. Where this
  document's own analysis points to an answer (CF-5), the answer is routed to Grant for ratification and
  explicitly fenced as **not yet canon**.
- **NOT a retitle of the upstream scoping doc.** F1–F9 stand as written; this document adds CF-1…CF-15
  in a separate numbering space so the two sets never collide.

## Sections

- §0 — Sector / regime / phase-state / coordinate header
- **PART 1** — §1 Adversarial framing challenge (A1–A9, verdict table, CF-1…CF-15)
- **PART 2** — §2 The vacuum-circuit mapping (EE-first)
- **PART 3** — §3 The lattice walk (sit-inside-the-cell, one page)
- §4 — The fork menu for Grant (one plumber question per OPEN fork)
- Appendix A — Step-0 skill-selection plan + retro-pass
- Appendix B — verify-before-cite battery (two-method receipts)

---

## §0 — Sector / regime / phase-state / coordinate header (declared BEFORE any physics word)

- **MODE.** Post-merger remnant ringing down. The object under challenge is the **cold** ($a_*=0$)
  anchor: $\omega_R M_g = 18/49$, $Q = \ell = 2$, against the frozen corrected-Kerr reference
  $Q_{GR}(0) = 2.10021$ (upstream §2.0).
- **SECTOR.** The **observable** is a **transverse shear (T2)** oscillation. The **bias field** that
  builds the cavity is the **A1 radial dilatation** $\varepsilon_{11} = 7GM/(c^2r)$. These are
  orthogonal grades (A1 ⊥ T2) and must not be cross-wired: the A1 strain is the **DC operating point**,
  the T2 shear mode is the **small-signal AC** riding on it. Receipt for the identification of
  $\varepsilon_{11}$ as the Axiom-4 amplitude: [`common/vocabulary-register.md:309`](../manuscript/ave-kb/common/vocabulary-register.md)
  — *"$\varepsilon_{11} = 7GM/(c^2 r)$ … the A1-dilatation radial 'strain' that IS the Axiom-4 saturation amplitude $A$"*.
- **REGIME.** Far field = **Regime I** (linear, lossless, reactive; a legal radiating port).
  Near the wall = **Regime III→IV** soft-mode transition ($G_{shear}\to 0$).
  Inside $r_{sat}$ = **Regime IV** (ruptured topology; shear cannot propagate at all).
- **PHASE-STATE.** Op14 **ON** at and near the boundary; the DC strain is at yield ($A = 1$) exactly at
  $r_{sat} = 7GM/c^2$; $\Gamma_{EM} = 0$ (SYM saturation, $Z_{EM} = Z_0$ invariant),
  $\Gamma_{shear} = \Gamma_{bulk} = -1$ per [`vol3/claim-quality.md:122`](../manuscript/ave-kb/vol3/claim-quality.md).
- **COORDS (A46 / `phase-space-coordinate-check`).** The confrontation lives in the
  **dimensionless-eigenvalue register** ($\omega_R M_g$, $\omega_I M_g$, $Q$) that AVE and GR share —
  no phase-space/real-space mismatch. **But PART 2 introduces a second register, the impedance plane**
  ($Z$, $\Gamma$, Smith), and the two are only *exactly* interchangeable for an isolated single pole.
  That caveat is **CF-14** and it is a live A46-class item for the derivation pre-reg, not a formality.
- **CLASS CEILING (`consistency-vs-emergence`), inherited unchanged from upstream §2.1.** Every object
  here rides $\nu_{vac} = 2/7$, whose **VALUE is GR-IMPORTED** via $K = 2G$. Nothing in this document
  can be headlined as value-level emergence. Where this document produces a number, its class is stated
  inline; most are **IDENTITY** (algebraic re-expression of two canonical lines) or
  **arithmetic-consistency observation on banked corpus inputs** — the same class as upstream §1.3/§2.0.

---

## PART 1 — ADVERSARIAL FRAMING CHALLENGE

### §1.0 — Verdict table

**Legend.** **FORCED** = canon (axioms + ratified leaves) leaves no alternative. **CHOICE** = a
defensible pick that canon states but does not derive; a different pick is admissible. **OPEN-FORK** =
two or more live readings, both canonically supported or neither excluded; the substrate has not been
asked.

| # | Assumption under challenge | Verdict | Load-bearing findings |
|---|---|---|---|
| **A1** | The resonator is the wall rim at $r_{sat}$ (the "bell") | **OPEN-FORK** — four candidate resonators, canon has explored one; and the standing chain contains **two different radii** for the same mode | CF-1, CF-2, CF-3, CF-9, CF-10 |
| **A2** | Sector ownership: observable is shear (T2); no A1 admixture | **FORCED** at linear order (A1 = DC bias, T2 = AC signal; any A1 product lands at $2\omega$ or DC, not $\omega$). **Sub-fork OPEN**: does the anisotropic vessel state split the rim modes? | CF-12 |
| **A3** | Mode geometry: whispering-gallery $\ell = 2$, linear-$\ell$ dispersion | **OPEN-FORK** on $\ell$ vs $\sqrt{\ell(\ell+1)}$ (upstream F4, binned UNDETERMINED). **Separate GAP, not a fork**: the radial-overtone index $n$ has **no AVE object at all** | CF-8, and §2.6 probe E15 |
| **A4** | The loss channel is radiation outward into the graded exterior | **FORCED by canon** that the wall is lossless and contributes **nothing** to $Q$ — which makes the corpus's own label ("$Q$ from the $\Gamma=-1$ TIR boundary") a mis-attribution. **OPEN** off the exact $A=1$ point: $\lvert\Gamma\rvert < 1$ there, and the transmitted shear has nowhere to go as shear | CF-11, CF-15 |
| **A5** | The local shear speed exponent ($\sqrt{S}$ vs $S^{1/4}$) is the biggest open input | **RECLASSIFIED → CHANNEL fork, and CLOSED for the shear integrand at $\sqrt{S}$** by three-way over-determination in the $(L,C)$ constitutive pair. **Routed to Grant for ratification; NOT canon until he rules.** | **CF-5, CF-6** ★ |
| **A6** | The $(1+\nu)$ loading factor | **CHOICE** — the FORM (a Poisson factor on a shell mode) is plausible and unexceptional; the SPECIFIC $r_{sat}/(1+\nu)$ is **asserted, not derived**, and its VALUE is GR-imported (upstream F3). It also implies a tangential phase speed of $1.286\,c_0$ | CF-1, CF-4 |
| **A7** | Which $Q$ the derivation targets ($\omega_R/2\omega_I$) | **FORCED** — the $\tau$ observable is the physical ratio; the integer mode-count reading coincides only at $a_*=0$ (upstream §1.6 fourth reading). **New caveat:** port-$Q$ and pole-$Q$ diverge once the exterior carries a branch cut | CF-14 |
| **A8** | Boundary condition at the wall: $\Gamma = -1$ | **FORCED** at $\lvert\Gamma\rvert = 1$ (#260 B3-DEGENERATE). The **sign is Q-neutral in the loss ledger** (a lossless termination either way) but **Q-relevant through the frequency**: short vs open moves the rim between a node and an antinode, a quarter-wave shift in effective length | CF-13 |
| **A9** | Where the radiated energy goes; re-reflection from the taper | **OPEN-FORK** — the strain grade is $\approx 0.41$ wavelengths thick, i.e. **borderline** between adiabatic and lumped, exactly the regime where partial re-reflection is expected and $Q$ is $O(1)$. Re-reflection **does** feed back into $Q$ by definition (it is the taper's input impedance). The echo cavity is **wall ↔ taper**, not wall ↔ light-ring | CF-9, and §2.3 |

---
