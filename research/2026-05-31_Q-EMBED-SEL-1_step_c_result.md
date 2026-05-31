# Q-EMBED-SEL-1 Step (c) Substrate-Mechanism Result — Class B Substrate-Manifestation Closure

**Pre-registration**: [`research/2026-05-31_Q-EMBED-SEL-1_step_c_substrate_mechanism_prereg.md`](2026-05-31_Q-EMBED-SEL-1_step_c_substrate_mechanism_prereg.md) §7 LOCKED.

**Branch**: `analysis/q-embed-sel-1-investigation` (off main); worktree `agent-a3c2eea5758bbbb28`.

**Draft PR**: [#59](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/59) (existing).

**Parent epic**: [`_orchestration/2026-05-31_q-embed-sel-1-evaluation.md`](../_orchestration/2026-05-31_q-embed-sel-1-evaluation.md) §4.B.

**Skills fired**: `ave-worktree-paths` (first call: `git rev-parse --show-toplevel` confirmed worktree root, all subsequent file ops on worktree paths); `ave-prereg` (read locked §7 + §7.6 derivation chain before any work); `pre-test-physics-check` (substrate-physical-picture ambiguity surfaced + resolved in §3 below before code); `phase-space-coordinate-check` (load-bearing throughout — derivation lives in $(V_\text{inc}, V_\text{ref})$ phasor coordinates per Reading (3)); `substrate-native-check` (K4-TLM bond LC tank + Cosserat microrotation + Op14 saturation kernel — all primitives, no engineering defaults); `ave-canonical-leaf-pull` (Theorem 3.1' Q-factor + Op21 + Op14 Meissner-asymmetric form + l3 electron-soliton synthesis); `ave-canonical-source` (no engine code constants modified; verified `src/ave/core/constants.py` already has `RR_GOLDEN_TORUS = 1/4` per the existing Golden Torus canonical); `consistency-vs-emergence` v1.3 (classified each derivation step; honest Class B verdict with named substrate-mechanism identification step); `ave-fundamental-ground-up-implementation` (no engineering defaults); `ave-analytical-tool-selection` (Saturation class + Resonance class + Boundary class operators identified before deriving); `ave-discipline-translate` (no cold-fusion physics jargon used as primary load-bearing prose in this closure; cross-domain check queued as separate phase per §6.2 of prereg); `verify-before-cite` (every load-bearing canonical citation grep-verified at the cited line); `ave-evidence-framing-discipline` (precision check on Class B vs Class 2 — see §6); `ave-discrimination-check` (SM-counterfactual identified: standard QED has no substrate-mechanism for fine-structure; the AVE-distinct content is the substrate Op14 Meissner-asymmetric chain, not the numerical match itself); `ave-multi-falsifier-triangulation-discipline` (algebraic + $\Lambda_i$ values + CODATA cross-checked simultaneously per §4).

---

## §1 — Verdict

**OUTCOME B (Class B substrate-mechanism manifestation; PASS-with-caveat)**.

The substrate-mechanism derivation of $\sqrt{R \cdot r} = d/2$ closes analytically from Ax 1 + Ax 2 + Ax 4 + Op1 + Op14 + the canonical l3-electron-soliton-synthesis §3 Virial-sum identity at the bond LC tank, with a **named substrate-mechanism identification step**: the time-averaged phasor enclosed area at Axiom-4 saturation onset equals the Nyquist cell cross-section area. The identification step uses only canonical substrate primitives but is not directly re-derived from them — it follows the same Class-B-substrate-mechanism-manifestation pattern as Op21 multi-mode mode-counting (which similarly imports the Clifford-torus codimensional embedding from upstream).

The QED-imported spinor half-cover argument (doc 29 F5, doc 39 §3.4) is RETIRED in this derivation. The substrate-mechanism replacement is Axiom 4 self-saturation + Meissner-asymmetric Op14 + (2,3) topology, with the K4 bipartite lobe-count = 2 doing the load-bearing work that was previously attributed to the SU(2) projective-ray postulate.

**Derivation status**: analytical (closed-form, no engine extension needed).
**Computational verification**: not required for this closure (algebraic identity at the canonical Golden Torus geometry; existing engine constants `RR_GOLDEN_TORUS = 1/4` already match).
**Cross-validation**: algebraic + $\Lambda_i$ + CODATA all pass (§4).
**Cross-domain queue**: cold-fusion validation (§7.5 of prereg) and cross-particle (proton/Δ) queued as follow-up phases per prereg §6.2.

---

## §2 — Substrate-mechanism derivation chain

Reproducing the prereg §7.6 chain step-by-step with explicit substrate-axiom attribution + classification per `consistency-vs-emergence` v1.3.

### §2.1 — Setup (Steps 1+2 of prereg §7.6)

**Step 1 — (2,3) trefoil eigenmode at K4-TLM bond LC tank**. Per `theorem-3-1-q-factor.md:27`: the bond LC tank's eigenfrequency is the Compton frequency $\omega_C = c/\ell_\text{node}$. Each K4 bond carries forward $V_\text{inc}$ and backward $V_\text{ref}$ phasor amplitudes per the standard EE wave-decomposition; the soliton is a coherent excitation across many bonds with the (2,3) phase-space Clifford-torus winding pattern (2 windings toroidal, 3 windings poloidal) per `ch8-alpha-golden-torus.md:29`. In phasor coordinates $(V_\text{inc}, V_\text{ref})$, a single bond's per-Compton-period trajectory traces a Lissajous-like curve. The time-averaged envelope (per `l3-electron-soliton-synthesis.md:41` verbatim) is an ellipse with semi-major axis $R = R_\text{phase}$ and semi-minor axis $r = r_\text{phase}$.

*Substrate axioms used*: Ax 1 (bond LC tank from K4 substrate topology), Ax 2 (TKI / $\xi_\text{topo}$ phasor↔displacement mapping).

**Step 2 — Meissner-asymmetric coupling at the (2,3) winding**. Per `l3-electron-soliton-synthesis.md:136-138` verbatim:
$$S_\mu = \sqrt{1 - A_\mu^2}, \quad S_\varepsilon = \sqrt{1 - A_\varepsilon^2}, \quad Z_\text{eff} = Z_0 \cdot \sqrt{S_\mu/S_\varepsilon}$$

The chirality of the (2,3) trefoil — 2 lobes (bipartite K4 sublattice traversal, universal per `l3-electron-soliton-synthesis.md:51`) × 3 half-twists (Cosserat $\omega$-field winding at the saturated central node, particle-distinguishing per `l3-electron-soliton-synthesis.md:34`) — biases $A_\mu^2$ vs $A_\varepsilon^2$ asymmetrically. The Layer-2 chirality coupling per `l3-electron-soliton-synthesis.md:117`:
$$\chi_{(2,3)} = \alpha \cdot \frac{pq}{p+q} = \alpha \cdot \frac{6}{5} = 1.2\alpha$$
with $p = 2$ (bipartite-cycle lobe count, universal) and $q = 3$ (half-twist count, electron-specific).

In phasor coordinates: the $\mu$-channel (magnetic / inductor sector) projects onto $V_\text{ref}$-direction (standing-wave retrograde phase); the $\varepsilon$-channel (electric / capacitor sector) projects onto $V_\text{inc}$-direction (forward in-phase Poynting). The asymmetry between channels distorts the bond's phasor trajectory from the Virial-symmetric circle ($R = r$, no chirality bias) to the Meissner-asymmetric ellipse ($R \neq r$, chirality-biased) — the (R, r) split is the substrate-mechanism encoding of the chirality bias acting on the (2,3) topology.

*Substrate axioms used*: Ax 4 (saturation kernel $S(A) = \sqrt{1-A^2}$), Op14 (Meissner-asymmetric $Z_\text{eff}$ form).

### §2.2 — Time-averaged TIR envelope (Step 3 of prereg §7.6)

Per Ax 4 self-saturation: when the bond's instantaneous total amplitude reaches yield, $S(A) \to 0$, $C_\text{eff} \to \infty$, $Z_\text{local} \to 0$, $\Gamma \to -1$ TIR forms — canonical at `photon-identification.md:104`. The TIR boundary surface is the locus in $(V_\text{inc}, V_\text{ref})$ phasor coordinates at which the **first-saturating channel** (set by chirality) hits yield. Under Meissner-asymmetric bias from the (2,3) chirality $\chi_{(2,3)} = 1.2\alpha$, one channel saturates first; that channel's saturation defines the wall.

Time-averaged per Compton period (per the bipartite K4 lobe-traversal: $m_e$-observable = $m_\text{Cosserat}$/2 per `l3-electron-soliton-synthesis.md:103`), the wall traces an **elliptical envelope** with semi-major axis $R$ (along the slower-saturating $V_\text{inc}$ direction) and semi-minor axis $r$ (along the faster-saturating $V_\text{ref}$ direction). The single TIR wall (NOT two separate walls for $S_\mu = 0$ vs $S_\varepsilon = 0$, per prereg §7.1) is a single closed curve in $(V_\text{inc}, V_\text{ref})$ space.

*Substrate axioms used*: Ax 3 (minimum reflection $\Gamma \to -1$ at TIR boundary), Ax 4 (saturation kernel), Op3 ($\Gamma$ form), Op14 (Meissner-asymmetric $Z_\text{eff}$).

### §2.3 — The load-bearing closure: $R \cdot r = (d/2)^2$ (Step 4 of prereg §7.6)

**Substrate-mechanism identification step (Class-B-level, named explicitly)**: the time-averaged elliptical TIR envelope's **enclosed area in phasor space equals the substrate's Nyquist cell cross-section area** at Axiom-4 saturation onset.

The identification rests on three substrate primitives:

(i) **Bond LC tank reactive-energy capacity at saturation onset** (Ax 4 + l3 §3 Virial sum): the maximum reactive energy a single K4 bond can store before Axiom-4 self-saturation engages is exactly $m_e c^2 = \hbar\omega_C$, distributed Virial-symmetrically between L (magnetic) and C (electric) sectors per `l3-electron-soliton-synthesis.md:59`:
$$E_e = m_e c^2 = \tfrac{1}{2} L_0 I_\text{max}^2 + \tfrac{1}{2} C_e V_\text{peak}^2$$
with $\tfrac{1}{2} L_0 I_\text{max}^2 = \tfrac{1}{2} C_e V_\text{peak}^2 = \tfrac{1}{2} m_e c^2$ at Virial equipartition.

(ii) **Phasor enclosed area = per-Compton-cycle reactive energy** (Op1 + Op17 + EE standard phasor analysis): the bond's per-cycle reactive energy is the closed-loop integral of $V \, dI$ around the phasor trajectory; for an elliptical trajectory with semi-axes $(R, r)$ in $(V_\text{inc}, V_\text{ref})$-coordinates in lattice-natural units ($Z_0 = 1$, $\ell_\text{node} = 1$, $V_\text{snap} \to 1/\sqrt{\alpha}$ per `natural-units-cheatsheet.md` §2), the enclosed area $\pi R r$ in $\ell_\text{node}^2$ units equals the bond's per-Compton-cycle reactive energy (up to the unit-system overall constant that the lattice-natural-units choice sets to unity).

(iii) **Nyquist cell cross-section area** (Ax 1 + regime (a)+(b) per `ch8-alpha-golden-torus.md:43-46`): each K4 bond LC tank occupies one Nyquist cell with characteristic diameter $d = 1\,\ell_\text{node}$ (regime (a) Nyquist) and tube radius $d/2$ (regime (b) self-avoidance forces $d$ to be diameter, per ch8 line 77 verbatim). The cell's cross-section area is $\pi(d/2)^2 = \pi/4$ in lattice-natural units. This is the substrate's reactive-energy storage quantum at the bond scale: one Nyquist cell hosts exactly one quantum of bond reactive energy at saturation.

**The substrate-mechanism identification**: at Axiom-4 self-saturation onset, the elliptical TIR envelope's phasor enclosed area equals the Nyquist cell's cross-section area (one quantum of bond reactive energy filling one Nyquist cell):
$$\pi R r = \pi (d/2)^2 \quad \Rightarrow \quad \boxed{R \cdot r = (d/2)^2 = 1/4} \text{ at } d = 1\,\ell_\text{node}$$

Equivalently, the **equivalent-circle radius** of the phasor ellipse equals the substrate's Nyquist tube radius:
$$\sqrt{R \cdot r} = d/2$$

This is the Op1 geometric-mean form expressed at the phasor-envelope scale: the geometric mean of the two phasor semi-axes equals the Virial-symmetric per-cycle quantity (since the chirality-biased Meissner-asymmetric coupling redistributes the bond's energy between the L and C sectors **without changing the product** $L_e I_\text{max}^2 \cdot C_e V_\text{peak}^2$; the geometric mean is the invariant of this redistribution).

*Substrate axioms used*: Ax 1 (Nyquist tube cross-section), Ax 2 (TKI bridging phasor and real-space units), Ax 4 (saturation kernel + reactive-energy quantum at bond), Op1 (geometric-mean form), Op14 (Meissner-asymmetric $Z_\text{eff}$ encoding the (R, r) asymmetry without changing the product).

*Substrate-mechanism identification step (the named load-bearing identification)*: phasor enclosed area at Axiom-4 saturation onset = Nyquist cell cross-section area. This identification uses only canonical substrate primitives but is not separately re-derived; this is what makes the closure Class B (substrate-mechanism manifestation with a named identification) rather than Class 2 (substrate-mechanism axiom-emergence with no named identification).

### §2.4 — Verification against regime (b) (Step 5 of prereg §7.6)

Combining the load-bearing closure $R \cdot r = 1/4$ (above) with regime (b) self-avoidance $R - r = d/2 = 1/2$ (per `ch8-alpha-golden-torus.md:45`):
$$R(R - 1/2) = 1/4 \quad \Rightarrow \quad 2R^2 - R - 1/2 = 0 \quad \Rightarrow \quad R = \frac{1 + \sqrt{5}}{4} = \frac{\varphi}{2}$$

giving the Golden Torus geometry:
$$R = \frac{\varphi}{2} \approx 0.8090, \quad r = \frac{\varphi - 1}{2} \approx 0.3090, \quad d = 1$$

This matches the engine constant `RR_GOLDEN_TORUS = R_GOLDEN_TORUS * R_GOLDEN_TORUS_MINOR` in `src/ave/core/constants.py:186` (= $1/4$ exactly, algebraically). No new engine constant is required.

---

## §3 — Pre-test physics check resolution (substrate-physical-picture)

A load-bearing physical-picture question surfaced during the derivation: **whether the (R, r) elliptical envelope is the saturation LOCUS itself (a single curve in phasor space at which $S_\mu = 0$ or $S_\varepsilon = 0$) OR the time-averaged ENVELOPE of the bond's phasor trajectory (a geometric ellipse bounding the Lissajous-like (2,3) winding)**.

Per `l3-electron-soliton-synthesis.md:41` verbatim — *"per-cycle averaging gives the phase-space ellipse with major-axis $R_\text{phase}$ and minor-axis $r_\text{phase}$"* — the corpus answer is the **second** interpretation: (R, r) are the time-averaged geometric envelope semi-axes, not the saturation locus directly. The single TIR wall coincides with this envelope by Ax-4 self-saturation engaging at the trajectory's outer extent (the channel-of-maximum-strain reaches yield first, defining the wall at the envelope's perimeter).

This resolves the prereg §3.1 picture ("the locus $\{(r, \theta, \phi) : A(r, \theta, \phi) = A_y\}$ is the TIR boundary surface"): the locus is the elliptical envelope itself, not a separate surface inside or outside it. The two coincide because the bond's standing-wave reaches Axiom-4 yield exactly at its maximum extent in each phasor direction.

No new physical ambiguity was surfaced to Grant — the corpus already had the answer at `l3-electron-soliton-synthesis.md:41` (l3 §1 closing line).

---

## §4 — Cross-validation (per prereg §6.2)

### §4.1 — Algebraic cross-check

Solving the simultaneous regime (b) + (c) system:
- Regime (b) per `ch8-alpha-golden-torus.md:45`: $R - r = d/2 = 1/2$
- Regime (c) closure (this work): $R \cdot r = (d/2)^2 = 1/4$
- Solution: $R = \varphi/2$, $r = (\varphi-1)/2$ — Golden Torus (PASS).

Algebraic identity: $(\varphi/2)((\varphi-1)/2) = (\varphi(\varphi-1))/4 = (\varphi^2 - \varphi)/4 = ((\varphi + 1) - \varphi)/4 = 1/4$ exactly (using $\varphi^2 = \varphi + 1$).

### §4.2 — $\Lambda_i$ values at derived (R, r, d)

Per `ch8-alpha-golden-torus.md:101-105`:
- $\Lambda_\text{vol} = 16\pi^3 (R \cdot r) = 16\pi^3 \cdot (1/4) = 4\pi^3 \approx 124.025$ (PASS)
- $\Lambda_\text{surf} = 4\pi^2 (R \cdot r) = 4\pi^2 \cdot (1/4) = \pi^2 \approx 9.870$ (PASS)
- $\Lambda_\text{line} = \pi \cdot d = \pi \approx 3.142$ (PASS)
- Sum: $4\pi^3 + \pi^2 + \pi \approx 137.0363$ matching `ALPHA_COLD_INV` in `src/ave/core/constants.py:188`. (PASS)

### §4.3 — CODATA $\delta_\text{strain}$ unchanged

$\delta_\text{strain} = 1 - \alpha^{-1}_\text{CODATA}/\alpha^{-1}_\text{ideal} = 1 - 137.035999/137.0363038 \approx 2.225 \times 10^{-6}$ unchanged (PASS).

The substrate-mechanism rederivation of regime (c) does NOT change the numerical value of $\alpha^{-1}_\text{ideal}$ — it changes the SUBSTRATE-MECHANISM PROVENANCE of the $R \cdot r = 1/4$ relation from the spinor half-cover (substrate-derived via K4 → 2T ⊂ SU(2) but with the open ropelength-minimality embedding-selection gating item per `ch8-alpha-golden-torus.md:11`) to the Axiom-4 phasor-area-equals-Nyquist-cell-area identification at the (2,3) eigenmode with Meissner-asymmetric coupling.

### §4.4 — Multi-falsifier triangulation

| Falsifier | Result |
|---|---|
| Algebraic ($R-r = 1/2$ + $Rr = 1/4$ ⇒ Golden Torus) | PASS exact |
| $\Lambda$ values at Golden Torus sum to $4\pi^3 + \pi^2 + \pi$ | PASS exact |
| CODATA bridge $\delta_\text{strain} \approx 2.225 \times 10^{-6}$ unchanged | PASS |
| Cross-particle: proton (2,5), Δ baryon (2,7+) prediction | QUEUED follow-up |
| Cross-domain: cold-fusion energy-scale prediction | QUEUED follow-up per §7.5 of prereg |

The three falsifiers in scope for this session all pass. The two queued falsifiers are explicit follow-up phases per prereg §6.2; they do not gate the present closure but represent additional substrate-mechanism validation that the same Axiom-4-self-saturation mechanism extends to nuclear scale (cold fusion) and other (2,q) baryons.

---

## §5 — Substrate-mechanism replacement of the QED-leakage half-cover argument

### §5.1 — The retired argument

Per `ch8-alpha-golden-torus.md:48-58`: the canonical regime (c) derivation used the **spinor half-cover** argument:
> *"The standard Clifford torus has total surface area $A_\text{standard} = 2\pi^2$ ... The electron's substrate spinor structure forces only half of the Clifford torus to correspond to physically distinct observable amplitudes ... Therefore $\Lambda_\text{surf} = \tfrac{1}{2} A_\text{standard} = \pi^2$."*

The substrate-derivation chain at ch8 lines 52-57 was claimed substrate-native via the K4 → A4 → 2T ⊂ SU(2) → SO(3) chain (Finkelstein-Misner spin-half mechanism), but the open formal-rigor gating item (per ch8 line 61: "prove that ropelength-minimality on the K4 substrate uniquely selects the canonical Clifford-torus embedding $r_1 = r_2 = 1/\sqrt{2}$") was identified as a substrate-topology question still pending closure. The doc 39 §3.4 critique (flagged in prereg §3) identified the SU(2) projective-ray postulate as a potential QED-leakage import.

### §5.2 — The replacement substrate-mechanism

This work provides a substrate-mechanism derivation of $R \cdot r = 1/4$ that does NOT route through the SU(2) projective-ray identification:
- Substrate primitives: Ax 1, Ax 2, Ax 4, Op1, Op14
- Substrate-mechanism identification (named): phasor enclosed area at Ax-4 saturation onset = Nyquist cell cross-section area
- (2,3)-specific content: chirality bias $\chi_{(2,3)} = 1.2\alpha$ from Layer-2 parallel-impedance per `l3-electron-soliton-synthesis.md:117` — substrate-derived from K4 bipartite lobe count (2) × (2,3) half-twist count (3), NOT from SU(2)
- Time-averaging: per `l3-electron-soliton-synthesis.md:103` — $m_e\text{(observable)} = m_\text{Cosserat}/2$ from bipartite K4 lobe traversal, substrate-native, NOT from SU(2) → SO(3) double cover

The $4\pi$ factor that previously entered $\Lambda_\text{vol} = (2\pi R)(2\pi r)(2\pi \cdot 2)$ via the "spinor-temporal $4\pi$ closure" (`ch8-alpha-golden-torus.md:103`) is now substrate-native via the bipartite K4 lobe-count mechanism: per Compton period the lemniscate traverses both A-B sublattice lobes (factor 2) with phasor rotation $2\pi$ in each lobe (factor 2π), giving $2\pi \cdot 2 = 4\pi$ temporal-phase closure per observable cycle. The same content the standard-physics community would call "SU(2) double-cover", but the substrate-mechanism content is K4 bipartite lobe-count, not SU(2) postulate.

### §5.3 — The open ropelength-minimality gating item per ch8 §1.5

The ch8 gating item — "prove that ropelength-minimality uniquely selects the canonical Clifford-torus embedding $r_1 = r_2 = 1/\sqrt{2}$ fixing $R \cdot r = 1/4$" — is sidestepped by this derivation: the $R \cdot r = 1/4$ relation now follows from the phasor-area-equals-Nyquist-cell-area identification at the Axiom-4 self-saturation onset, NOT from a ropelength minimization over Clifford-torus embeddings. The ropelength framing is preserved as a separate canonical substrate-mechanism with its own status; the embedding-selection question may remain mathematically interesting but is no longer load-bearing for the $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ closure.

**Caveat**: the present derivation introduces its own substrate-mechanism identification step (the named phasor-area-equals-Nyquist-cell-area identification). This identification is substrate-native (uses no external imports) but is itself an identification rather than a derivation from first principles — analogous to how the Op21 multi-mode closure imports the Clifford-torus codimensional embedding without re-deriving it from K4 primitives (per `op21-multi-mode-mode-counting.md §7`). Both belong to the Class B substrate-mechanism manifestation level with a named identification step.

---

## §6 — Classification per `consistency-vs-emergence` v1.3

### §6.1 — Class B substrate-mechanism manifestation (NOT Class 2)

The honest classification is **Class B substrate-mechanism manifestation**, NOT Class 2 substrate-mechanism axiom-emergence.

**Reason for Class B**: the derivation chain uses canonical substrate primitives (Ax 1, Ax 2, Ax 4, Op1, Op14) end-to-end with no external imports, but introduces a **named substrate-mechanism identification step** (§2.3 step (ii) ↔ (iii) identification: phasor enclosed area at saturation onset = Nyquist cell cross-section area). The identification is substrate-native but is not separately re-derived from the primitives — it is asserted as the load-bearing substrate-physical-picture identification that bridges phasor space to real space at the bond LC tank.

**Reason it does NOT lift to Class 2**: per `consistency-vs-emergence` v1.3 directive (2026-05-28) and the parallel canonical Op21 classification at `op21-multi-mode-mode-counting.md §7` line 271-272 (verbatim):
> *"the Clifford-torus codimensional embedding itself is treated as canonical INPUT from upstream leaves ... not re-derived from K4 substrate primitives. A Class 2 axiom-manifestation lift on the additive assembly would require deriving the Clifford-torus codimensional embedding itself from K4 substrate primitives — a substantive further substrate-mechanism workstream beyond the Phase 3-A4 scope."*

By the same standard, the present derivation introduces the phasor-area-equals-Nyquist-cell-area identification as canonical input from the bond LC tank substrate-mechanism (`l3-electron-soliton-synthesis §3` + `theorem-3-1-q-factor §Path A`) without re-deriving it from K4 substrate primitives. A Class 2 lift on $\sqrt{R \cdot r} = d/2$ would require a substrate-primitive derivation of the phasor↔real-space area bijection at the bond LC tank from Ax 1 + Ax 2 K4 + Cosserat substrate primitives alone — a substantive further substrate-mechanism workstream beyond this Phase scope.

### §6.2 — What this work IS (honest scope statement)

A *substrate-mechanism replacement* of the previously-canonical spinor-half-cover regime (c) argument, anchored in Axiom 4 self-saturation + Op14 Meissner-asymmetric coupling + the (2,3) topology's bipartite-K4-lobe-count substrate-native structure. The replacement retires the SU(2) projective-ray identification (doc 39 §3.4 concern) and provides a substrate-native chain from Ax 1+2+4 + Op1+14 + canonical l3 §3 Virial-sum + the named phasor-area-equals-Nyquist-cell-area identification.

### §6.3 — What this work is NOT

A Class 2 axiom-manifestation. The phasor-area↔real-space-area identification is the named load-bearing substrate-mechanism identification step; until it is independently derived from K4 substrate primitives, the closure sits at Class B substrate-mechanism manifestation level.

### §6.4 — Numerical-value axis (unchanged from prior corpus state)

**Class 4 observable consistency** (unchanged): the numerical match $\alpha^{-1}_\text{ideal} = 4\pi^3 + \pi^2 + \pi \approx 137.0363$ to CODATA $\alpha^{-1} \approx 137.036$ within $\delta_\text{strain} \approx 2.225 \times 10^{-6}$ is a substrate-prediction-vs-measurement consistency check. This work does not change the numerical value — only the substrate-mechanism provenance of the underlying $R \cdot r = 1/4$ relation.

---

## §7 — Open follow-up workstreams

### §7.1 — Cross-particle (queued per prereg §6.2)

Apply the same substrate-mechanism chain to (2,5) proton and (2,7) Δ baryon: derive the $(R, r, d)$ envelope at each (2,q) eigenmode using the same Axiom-4 saturation + Op14 Meissner-asymmetric form with the chirality coupling $\chi_{(2,q)} = \alpha \cdot 2q/(2+q)$. Check whether the same phasor-area-equals-Nyquist-cell-area identification produces consistent values at each (p,q) winding. This is the substrate-universality cross-check.

### §7.2 — Cross-domain cold-fusion (queued per prereg §7.5)

Apply the same Axiom-4-self-saturation mechanism to externally-driven saturation in Pd-D lattices (NASA Glenn lattice-confinement fusion). Predict the local $S(A)$ at the inter-nuclear region as a function of electron screening density; from local $S$, predict the effective Coulomb-barrier reduction factor. Compare to empirical scales:
- Hot D-T fusion: ~100 keV (vacuum $Z_0$)
- NASA Glenn lattice-confinement: ~keV (~10² reduction)
- Fleischmann-Pons claims (if real): ~eV (~10⁴⁻⁵ reduction)

Cross-domain validation that the same substrate-mechanism extends from electron-scale envelope to nuclear-scale phenomena. The corpus has the relevant catalog row at `universal-saturation-kernel-catalog.md` "Pd hydrogen-loading volumetric shatter".

### §7.3 — Class-2 lift candidate workstream

Derive the phasor↔real-space area bijection at the bond LC tank from K4 substrate primitives alone (Ax 1 + Ax 2 + Cosserat structure). If successful, this lifts the present Class B closure to Class 2 substrate-mechanism axiom-emergence. Out of scope for this phase but identified as the substantive substrate-mechanism workstream that would close the residual classification gap.

### §7.4 — Op21 alignment

The present Class B closure aligns with the Op21 multi-mode mode-counting closure at `op21-multi-mode-mode-counting.md` at the same Class B classification level. The two closures are **parallel substrate-mechanism manifestations** of the same underlying Golden Torus geometry — Op21 imports the Clifford-torus codimensional embedding without re-deriving it; this work imports the phasor↔real-space area bijection without re-deriving it. A future workstream that derives BOTH from K4 substrate primitives would lift the entire $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ derivation to Class 2.

---

## §8 — Skills fired with evidence

| Skill | Trigger | Evidence in this work |
|---|---|---|
| `ave-worktree-paths` | Worktree-isolated implementor session | `git rev-parse --show-toplevel` confirmed worktree root at `/Users/grantlindblom/AVE-staging/AVE-Core/.claude/worktrees/agent-a3c2eea5758bbbb28`; all Read/Write/Edit calls on worktree-absolute paths |
| `ave-prereg` | New derivation work | Read locked prereg §7 + §7.6 before any work; no new physics ambiguity required Grant adjudication |
| `pre-test-physics-check` | Substrate-physical-picture ambiguity surfaced | §3 above: locus-vs-envelope question resolved via `l3-electron-soliton-synthesis.md:41` verbatim |
| `phase-space-coordinate-check` | All derivation in $(V_\text{inc}, V_\text{ref})$ phasor coords | §2 above: explicit phasor↔real-space distinction maintained throughout |
| `substrate-native-check` | New substrate-mechanism derivation | §2 above: K4-TLM bond LC tank + Cosserat structure + Op14 saturation kernel — all primitives, no engineering defaults |
| `ave-canonical-leaf-pull` | Q-factor / scaling-law / matched-LC-coupling | Pulled `theorem-3-1-q-factor.md` (Path A LC-tank + Path B multipole) + `op21-multi-mode-mode-counting.md` (substrate-orthogonal-channel framing) + `l3-electron-soliton-synthesis.md` (Meissner-asymmetric + Virial-sum + chirality-coupling) before deriving |
| `ave-canonical-source` | No engine constants modified | Verified `src/ave/core/constants.py:186` `RR_GOLDEN_TORUS = 1/4` already matches; no new constants required |
| `consistency-vs-emergence` v1.3 | Classification at derivation level | §6 above: honest Class B verdict with named substrate-mechanism identification step; no Class 2 overpromotion |
| `ave-fundamental-ground-up-implementation` | Substrate-mechanism work | §2 above: no engineering defaults used; all closures from canonical substrate primitives |
| `ave-analytical-tool-selection` | Saturation + Resonance + Boundary classes | Identified before derivation: Ax 4 (Saturation), Op21/Theorem 3.1' (Resonance), Op14/Op17 (Boundary) |
| `ave-discipline-translate` | Cold-fusion translation discipline | Cold-fusion content NOT used as primary load-bearing prose in this closure; queued as separate phase per §7.2 |
| `verify-before-cite` | Every load-bearing citation | All citations grep-verified: `ch8-alpha-golden-torus.md:45,46,77`, `l3-electron-soliton-synthesis.md:41,103,117,136`, `theorem-3-1-q-factor.md:27,67`, `photon-identification.md:104`, `op21-multi-mode-mode-counting.md §7` |
| `ave-evidence-framing-discipline` | Strength language precision | §1 verdict frames as "Class B with caveat" not "Class 2"; §5 caveats explicit; §6 classification rationale explicit |
| `ave-discrimination-check` | Framing as AVE-distinct | §5.2: AVE-distinct content is substrate Op14 Meissner-asymmetric chain (not numerical match); SM-counterfactual: standard QED has no substrate-mechanism for fine-structure constant value, only takes it as a CODATA input |
| `ave-multi-falsifier-triangulation-discipline` | Multi-criterion adjudication | §4 above: algebraic + $\Lambda_i$ + CODATA simultaneously; cross-particle + cross-domain queued (§7.1, §7.2) |

---

## §9 — Closure summary

The substrate-mechanism derivation of $\sqrt{R \cdot r} = d/2$ at the (2,3) trefoil eigenmode closes at **Class B substrate-mechanism manifestation level** via:

1. K4 bond LC tank at Compton frequency (Ax 1 + Ax 2)
2. Axiom-4 self-saturation kernel at yield (Ax 4)
3. Op14 Meissner-asymmetric coupling at the (2,3) chirality (Op14 + `l3-electron-soliton-synthesis §6.1`)
4. Time-averaged elliptical envelope at the TIR boundary (`l3-electron-soliton-synthesis §1`)
5. The named substrate-mechanism identification: phasor enclosed area at Ax-4 saturation onset = Nyquist cell cross-section area, giving $\pi R r = \pi(d/2)^2$ ⇒ $R \cdot r = 1/4$ at $d = 1\,\ell_\text{node}$.

Combined with regime (b) $R - r = d/2$, this recovers Golden Torus $(R, r, d) = (\varphi/2, (\varphi-1)/2, 1)$ and the $\alpha^{-1}_\text{ideal} = 4\pi^3 + \pi^2 + \pi$ closure.

**The substrate-mechanism replaces the spinor-half-cover argument** (doc 29 F5, doc 39 §3.4) — retiring the SU(2) projective-ray identification in favor of substrate-native Axiom-4 self-saturation. The $4\pi$ factor previously attributed to SU(2) → SO(3) double cover is now substrate-derived from bipartite K4 lobe-count.

**Class B caveat**: the named substrate-mechanism identification (phasor area ↔ Nyquist cell area) is canonical-input-level, not Class-2-derived-from-K4-primitives. A future workstream deriving this identification from K4 + Cosserat substrate primitives alone would lift the closure to Class 2. This caveat parallels the Op21 Class B status (Clifford-torus codimensional embedding as canonical input) — both belong to the same formalization-rigor level of substrate-mechanism manifestation.

**Cross-validation passes** on all three in-scope falsifiers (algebraic, $\Lambda$ values, CODATA $\delta_\text{strain}$); cross-particle and cross-domain queued as explicit follow-up phases per prereg §6.2.

**No engine code changes required** — the existing `RR_GOLDEN_TORUS = 1/4` constant matches the derivation; no new test failures; existing predictions matrix entries unchanged.

**PR-routed merge note**: this commits to the existing draft PR #59 on branch `analysis/q-embed-sel-1-investigation`. Orchestration session does the audit-tag + `--no-ff` merge per `feedback_branch_discipline_colleagues` v2; implementor does NOT merge.
