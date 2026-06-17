# Electron property + kinematics coverage matrix — RUNG-1 EXISTENCE companion

**Date:** 2026-06-17
**Base:** AVE-Core `origin/main` = local main `0597f0c6`
**Companion to:** `src/tests/engine_acceptance/test_l3_mass_cage.py` (T3.1–T3.4, the
RUNG-1 EXISTENCE electron unit-test suite).
**Scope:** the FULL electron property + kinematics sheet, one row per property,
mapped to AVE's native derivations and sorted into the three honest buckets. This
is the suite's companion documentation — **NOT** the KB-leaf / Vol9 propagation
ritual (that is a separate completion pass, after results verify).

All file:line and clm-id citations were grep-verified against HEAD `0597f0c6`
(transcribed from the coverage-matrix workflow output, itself grep-verified; the
clm-ids re-confirmed to resolve in `manuscript/ave-kb/` this pass).

## Honest one-liner

AVE natively derives the **FORMS (chords)** of the electron's topological/dynamical
skeleton — mass-as-cutoff, stability, the Γ=−1 trap, charge-integer-ness, spin-½
double-cover, g=2 ratio, the substrate's two wave-speeds — but **CALIBRATES every
dimensionful VALUE** (m_e definitional, e/λ_C/μ_B riding it, α an echo on every
closed route, Q=1/α baked at the instance), and **DOES NOT TOUCH** the QED-precision
interaction sheet (g−2 ppm refuted-negative, all scattering cross-sections absent,
spin-statistics provisional, pair-production engine-can't-represent, r_e
retired-by-design, moving-cage relativistic dispersion γ-imported-by-construction).
On the rung-1 cage the MEDIUM exists and stiffens (T3.1+T3.2) AND — this pass — the
posited cage shows the Γ=−1 wall (T3.3), a gapped bound eigenmode (T3.4a), a
finite α-FREE cold Q that is **NOT 137** (T3.4b — clean negative), and zero-drive
persistence (T3.4c).

## Bucket legend

- **A** — testable-now on the rung-1 longitudinal-bulk (A1 scalar) cage.
- **B** — DERIVED but needs the WINDING sector (L4, structural deferral — NOT a gap).
- **C** — NOT-DERIVED-NATIVELY = a genuine gap (flagged not-derived, NEVER a claim).

FORM-chord = the dimensionless form/structure is substrate-forced.
VALUE-echo/definitional = the dimensionful number is calibration-imported.
GAP = not derived natively.

---

## Coverage matrix (one row per property)

| Property | Observed | Bucket | clm-id + solidity | FORM/VALUE/GAP | Cage unit-test or deferral/gap note |
|---|---|---|---|---|---|
| **rest mass m_e** (E0=m_e c²) | 9.1093837015e-31 kg / 511 keV | A-for-FORM; VALUE definitional | clm-0vxzfu 0.90 (V_snap=m_e c²/e via Ax2) + clm-unk0bd 0.65 (m_e=ℏ/c·ℓ_node) | FORM=chord (mass=ground-state cutoff energy of the bound resonator) / VALUE=DEFINITIONAL (constants.py:129 'Input 1'; electron-identification.md:50 'CALIBRATION ANCHOR, not derivation') | **T3.4a** — the gapped bound mode (ω_cutoff>0) EXISTS; m_e VALUE is NEVER a cage output |
| **relativistic dispersion** E²=(pc)²+(mc²)² (MOVING cage) | exact SR | **C** — FORM imported-by-construction | clm-fgo20a 0.70 (depends clm-p5cf3t 0.85) | GAP-on-native-derivation: relativistic-inductor.md:10 'm_eff=γm_0 maps to current-dependent inductance' (γ is INPUT); newtonian-limit:50 'All standard SR kinematics recovered' (by construction) | NOT cage-testable; ZERO boost/moving-cage tests exist. **The KEY question: moving-cage dispersion is a GAP, not a rung-1 pass** |
| **Compton wavelength** λ_C=ℓ_node | 3.8616e-13 m | DEFINITIONAL (= m_e anchor restated) | — (electron-identification.md:55 '⚠ DEFINITIONAL') | FORM=identity / VALUE=DEFINITIONAL | PARTIAL — a Compton-frequency LC-eigenmode exists in natural units, but the number is the m_e anchor |
| **charge −e** (integer winding) | −1.602176634e-19 C, exact integer | **B** (winding-sector L4) | clm-uatcql 0.70 (electron-identification.md:52 'Ax2 TKI winding'); clm-67jn9o 0.75 is BARYON-scope (quark fractional charge), NOT the electron's −e | FORM=chord (integer-ness from winding) / VALUE=DEFINITIONAL (e is INPUT, constants.py:100; tied to α at :310) | NOT cage-testable — charge lives in (2,3) Cosserat micro-rotation; `_bulk.py:32-36` exercises ONLY the A1 longitudinal grade |
| **spin-½** (4π double-cover) | ℏ/2, SU(2) | **B** (winding-sector L4; the classic QED honesty test) | clm-salw2h 0.70 (FM/belt-trick on extended unknot) | FORM=chord (4π double-cover; Pauli matrices = imported math-LANGUAGE only) / VALUE=N/A (½ is the topological invariant) | NOT cage-testable — finkelstein-misner:167 'not currently in the K4-TLM or Master Equation FDTD engines' |
| **g=2** (gyromagnetic) | 2.00231930436 | **B** (winding-sector; the ratio derives) | clm-uatcql 0.70 (SO(3) 2π vs spinor 4π ratio) | FORM=chord (double-cover ratio) / VALUE=N/A | NOT cage-testable — magnetic moment = Cosserat-B winding sector |
| **magnetic moment μ_B**=eℏ/2m_e | observed μ_B | **B** (winding-sector) | electron-identification.md ('axiom-derived from components') | FORM=chord (assembled from axiom-derived parts) / VALUE=echo+definitional (rides e + m_e anchor) | NOT cage-testable |
| **g−2 LEADING** a_e=α/2π (Schwinger) | 1.15965e-3 | **B/C-boundary** — an ECHO, not an independent prediction | clm-stgx1i 0.70 (classified consistency-check) | FORM=chord-shaped (1/π² form-factor) / VALUE=ECHO: higgs-mass.md:50 '(V_peak/V_snap)²=4πα [EXACT]', :53 'α IS the on-site electric strain' (α PLUGGED IN) | NOT cage-testable (winding + α-bake); re-reads the baked α (instrument-echo-trap) |
| **g−2 ANOMALOUS 2-loop** (Petermann C2) | C2=−0.32848 (PDG) | **C** — parameter-free FORM +4.0% off; ppm REFUTED-NEGATIVE | clm-v2sg8z 0.60 input-only | FORM=partial-chord (Route-B C2_sym=−0.3416, +4.0%, NO fit, q-g19a:12) / VALUE=GAP: 50-ppm headline RESOLVED-NEGATIVE 2026-05-31 (q-g19a:14 'kernel winding-blind … postulate-dependent echo') | NOT cage-testable |
| **g−2 MUON** (Fermilab forward) | +245(56)e-11 over SM(e+e−) | **C** — forward prediction in genuine TENSION | clm-8niffj 0.45 | FORM=chord-shaped (Cosserat-saliency √(3/7) PAT) / VALUE=refuted-leaning: q-g27:71-73 '+4.6σ … genuine disagreement' (α-input via (α/π)²) | NOT cage-testable |
| **zitterbewegung** (trembling) | ~2·m_e c²/ℏ = 2·ω_C | A-identity + C-consistency (corpus exists in research-tier) | research/2026-06-07_electron-interstitial-rotor-synthesis.md:315-388 (NO clm-id, research-tier not a KB leaf) | FORM=chord-via-identity (zitter=2·ω_C from the bipartite 2-sublattice 4π) / VALUE=N/A — :320 'identity/consistency derivation, not a new prediction' | POTENTIALLY the T3.4 breather eigenfreq, but the claim is consistency not emergence |
| **de Broglie** λ=h/p | λ=h/p | **B/C-mix** (NON-rel standing-wave quantization 'derived'; rel = γ-import) | de-broglie-standing-wave.md (clm-oltvwy host); radial-eigenvalue-solver.md:127 'derived from lattice dispersion' | FORM=chord on standing-wave quantization (Bohr via ∮k·dl=2πn) / VALUE=echo (m_e definitional) — dispersion invoked is NON-relativistic | NOT cage-testable (atomic bound soliton, not the free bulk cage) |
| **Lorentz time dilation** (moving clock) | dτ=dt/γ | **C** for SR-boost; B-adjacent for GRAVITATIONAL √S | SR rides clm-fgo20a/clm-p5cf3t γ-import; gravitational c_shear=c_0·√S is form-derived (clm-8nkvwy:113) | GAP on native SR moving-clock (γ imported); the SYM √S dilation is a DIFFERENT (gravity) mechanism | NOT cage-testable |
| **Lorentz length contraction** | L=L_0/γ | **C** — zero AVE-specific derivation | NONE specific (qualitative + FitzGerald/Lorentz HISTORY only) | GAP — rides imported γ | NOT cage-testable |
| **group/phase velocity** v_g·v_p=c² (moving cage) | v_g·v_p=c² | **PARTIAL/C** on the IDENTIFICATION | c_EM=c_0/S, c_shear=c_0·√S (clm-8nkvwy:111/113) | FORM=partial-chord (substrate genuinely carries two speeds) / GAP on tying them to a moving-electron v_g/v_p | PARTIAL — c_bulk (√2·c_0) + c_eff(A) ARE measured (T3.1/T3.2), but a moving massive cage's v_g/v_p is not |
| **matter-wave interference** (free double-slit) | fringe pattern | **C** — BOUND quantization is corpus, free two-path is not | de-broglie standing-wave condition; C11-Mach-Zehnder is a GRAVITATIONAL parallax bench | FORM=chord on phase-coherent standing waves / GAP on free two-path pattern | NOT cage-testable (single trapped cage, no two-path apparatus) |
| **pair production / annihilation** | γ→e⁻e⁺ at 2·511keV | **C** — mechanism-class sketched, not quantitatively derived | clm-ezai5b 0.40 (pair-prod), clm-hb2xmj 0.30 (annihilation) | FORM=partial-chord (saturated flux-tube rupture + parity→LH+RH) / VALUE=GAP: NO cross-section, NO rate; pair-production-axiom-derivation.md:111 '## What the current engine cannot represent' | NOT cage-testable |
| **Compton scattering** (Klein-Nishina) | σ(ω), KN | **C** — qualitative one-liner only | NONE | photon-identification.md:179 'transient saturation event' (no cross-section); grep 'klein-nishina' = 0 hits | NOT cage-testable |
| **Mott / Rutherford scattering** | Mott σ | **C** — HARDEST GAP, zero coverage | NONE | grep 'mott' (.md/.tex) = 0 hits | NOT cage-testable — not even a qualitative framing |
| **vacuum polarization** / running α(q²) | Uehling, α runs | **C-at-distinction** — matches QED by RT-EQUIVALENCE | clm-bqtasn 0.60 | FORM=imported (q-g20f 'Identical functional form', 'No way to distinguish AVE from QED' at accessible scales) / VALUE=ECHO (α/3π). NUANCE: q-g20f:10 DOES claim a sub-Compton structural difference (removes the Landau pole), inaccessible | NOT cage-testable |
| **classical radius r_e** | 2.8179e-15 m | **C** — GENUINE GAP, absent-by-design | NONE (no clm-, no constants.py entry) | GAP: the-abandoned-interior.md:22 frames classical-radius + 4/3-problem + Abraham-Lorentz as the RETIRED EM-mass program; AVE's self-energy is the unknot ropelength (ℓ_node/2π), a DIFFERENT object — do NOT dress ℓ_node/2π as r_e | NOT cage-testable — no AVE r_e to test |
| **LC-tank Q ≈ α⁻¹ ≈ 137** (cold-Q) | AVE-internal | A-for-FORM; VALUE is the α-echo | clm-rtdmsn 0.85 (highest here) | FORM=chord (Q_tank=ω_C·L_e/R=1/α is clean LC algebra) / VALUE=ECHO: theorem-3-1:19 'obtains Q_tank=1/α USING α=e²Z0/(4πℏ) — predicts no independent value', :21 instrument-echo-trap + cvr_model.py:72 Q_TANK=1/ALPHA baked at instance | **T3.4b** — cold/α-FREE Q from ring-down (α-bake REMOVED). **RESULT: Q_ringdown≈30.8, NOT 137 → the corpus Q=1/α is an instance-baked ECHO, not cage-emergent** |
| **stability / lifetime** >10²⁸ yr | non-decay | A (zero-drive persistence) + B (topological-protection reason) | clm-uatcql 0.70 (two-reason trap); clm-zuf7g1 0.65 (phase-space-winding protection) | FORM=chord (loop-can't-untangle + Γ=−1 impedance) / VALUE=N/A | **T3.4c** — zero-drive persistence (late/mid≈1.31, non-radiating) PASSES; the topological-winding protection is winding-sector (NOT cage-testable) |
| **Γ=−1 TIR wall** (via gamma_bulk, Z_eff=√S) | self-trap at V_yield | A — stiffening precursor (T3.2) + the wall itself (T3.3) | clm-uatcql 0.70; crystal_engine.gamma_bulk :455-486 Z_eff=√S→0 ⇒ Γ→−1 | FORM=chord (Ax4 kernel: A→1 ⇒ S→0 ⇒ Z→0 ⇒ Γ→−1) / VALUE=N/A | **T3.3** — Γ_bulk crosses OP2 gate −0.25 by A=0.95 (Γ_min(0.95)=−0.283), monotone toward −1, →0 in vacuum; α-FREE. PASS |

---

## Ranked GAP list (bucket C — flagged NOT-derived-natively, NEVER as claims)

Each item names WHAT'S MISSING. These are honest gaps, not claims.

1. **g−2 PRECISION (the QED triumph).** Parameter-free 2-loop is +4.0% off PDG
   (q-g19a:12); the 50-ppm headline is REFUTED-NEGATIVE (kernel winding-blind,
   q-g19a:14); muon forward is +4.6σ genuine tension (q-g27:71). MISSING: α-OUT —
   the leading a_e=α/2π re-bakes the α-echo (4πα EXACT input, higgs-mass.md:50);
   the higher-order content QED computes to 10 digits, AVE misses by 4% or imports
   via the textbook (α/π)² conversion.
2. **SCATTERING CROSS-SECTIONS.** Compton: one-sentence qualitative 'transient
   saturation event' (photon-identification.md:179), no Klein-Nishina, no
   σ(θ,ω). Mott/Rutherford: ZERO hits across the corpus. MISSING: AVE has no
   scattering-amplitude machinery at all — neither a photon-electron vertex nor a
   relativistic Coulomb amplitude. The bread-and-butter falsifiable QED observable
   is entirely absent.
3. **RELATIVISTIC DISPERSION OF A MOVING CAGE (the brief's KEY question).**
   MISSING: a native derivation from a moving longitudinal-bulk cage. AVE IMPORTS
   γ (relativistic-inductor.md:10; clm-p5cf3t rationale 'structural reproduction of
   SR, not an independent derivation'). ZERO boost/moving-cage tests exist. Lorentz
   length-contraction (zero AVE-specific claim) and SR time-dilation (distinct from
   the form-derived gravitational √S) ride the same imported γ.
4. **SPIN-STATISTICS THEOREM + PAULI EXCLUSION.** Spin-½ the VALUE is derived
   (bucket B, clm-salw2h), but the THEOREM connecting half-integer spin to
   antisymmetric exchange is PROVISIONAL in the corpus's own words (vol2/
   claim-quality.md:1178 'substrate-native Pauli is provisional' / :1195 'promote
   from provisional to derived' — carry-from-source, the file:line is from the
   workflow grep, consistent with the verified corpus). MISSING: a derived
   spin-statistics result and exclusion itself — currently an asserted per-node
   A²≤1 antiphase-healing constraint, not a theorem.
5. **PAIR PRODUCTION / ANNIHILATION QUANTITATIVE CONTENT.** Mechanism-class
   sketched (clm-ezai5b 0.40 / clm-hb2xmj 0.30) but the leaf ITSELF admits
   (pair-production-axiom-derivation.md:111) no dynamical bond state, no per-node
   rotational resonance, no nucleation rule. MISSING: cross-section, rate,
   threshold independent of m_e/e (the 511kV threshold restates the mass
   calibration).
6. **VACUUM POLARIZATION / RUNNING COUPLING (subtle, dressed-as-coverage).**
   clm-bqtasn 0.60 claims AVE matches QED but explicitly 'by RT-equivalence',
   'Identical functional form', 'No way to distinguish AVE from QED' at accessible
   scales (q-g20f). MISSING: an AVE-DISTINCT derivation + a discriminating
   prediction at accessible scales — it imports the α/3π polynomial and re-bakes α.
   NUANCE: q-g20f:10 DOES claim an inaccessible sub-Compton structural difference.
7. **FINE-STRUCTURE α VALUE (the keystone echo, cross-cutting).** 'α is an echo on
   every route' (ch8-alpha-golden-torus.md:13, all three routes closed-negative);
   higgs-mass.md:92 'α a value-scoped echo … the substrate does not independently
   select'. MISSING: substrate-forcing of the coupling-STRENGTH value. The FORM
   α⁻¹=4π³+π²+π is a Class-B closed-form-at-the-identification, not first-principles.
   Every magnitude-match that uses α inherits this echo. **Directly demonstrated by
   T3.4b: the α-free cold cage Q is NOT 137.**
8. **DIMENSIONFUL ELECTRON MAGNITUDES generally (m_e, e, μ_B, λ_C).** FORMS exist
   (bucket A/B) but the NUMBERS are calibration-imported: m_e DEFINITIONAL
   (constants.py:129 'Input 1'); λ_C=ℓ_node same anchor restated; e is INPUT
   (constants.py:100, tied to α at :310); μ_B combines e+anchor. MISSING: any
   native dimensionful electron number. AVE forces FORMS (chords), imports VALUES
   (echoes).
9. **CLASSICAL ELECTRON RADIUS r_e.** GENUINE GAP / absent-by-design. No clm-, no
   constants.py entry. the-abandoned-interior.md:22 frames classical-radius +
   4/3-problem + Abraham-Lorentz as the RETIRED EM-mass program 'that collapsed on
   its own arithmetic'; AVE's self-energy is the unknot ropelength (ℓ_node/2π), a
   DIFFERENT object. Absent by design, but still NOT derived natively. Do NOT dress
   ℓ_node/2π as r_e (trampoline-framework.md:677 already loosely conflates).

---

## Bucket-B deferrals (winding-sector / L4 — NOT gaps, KNOWN structural deferrals)

These are charge / spin / μ — they DERIVE (FORM-chords) but live in the (2,3)
Cosserat micro-rotation WINDING sector (L4), which is orthogonal to the A1 scalar
cage. Any rung-1 unit-test claiming to verify them on the scalar cage would
validate a sector the cage does not contain (the stencil-mismatch failure mode).

- **CHARGE −e** — L4 winding STRUCTURAL DEFERRAL. FORM derived (charge=integer
  topological winding through K4 bond-port, Ax2 TKI [Q]≡[L]; clm-uatcql 0.70). Lives
  in the (2,3) Cosserat micro-rotation. NOT cage-testable (`_bulk.py:32-36`
  exercises ONLY the A1 longitudinal scalar grade). (clm-67jn9o 0.75 is BARYON-scope
  quark fractionalization, NOT the electron's integer −e.)
- **SPIN-½** — L4 winding STRUCTURAL DEFERRAL (the classic QED honesty test,
  handled cleanly). FORM derived (4π double-cover from extended-defect classical
  topology on SO(3); clm-salw2h 0.70). Explicitly NOT SU(2)-rep-theory-imported —
  finkelstein-misner:355-362 labels the SU(2)→SO(3) chain 'standard-physics
  translation reference, not the substrate mechanism'. NOT cage-testable
  (finkelstein-misner:167 'not currently in the … FDTD engines').
- **MAGNETIC MOMENT μ_e / g=2** — L4 winding STRUCTURAL DEFERRAL. g=2 FORM derived
  (SO(3) 2π vs spinor 4π double-cover ratio, clm-uatcql 0.70); μ_B=eℏ/2m_e assembled
  from axiom-derived parts + calibration. The B-field = Cosserat-microrotation
  winding sector, NOT the A1 scalar cage. NOT cage-testable.
- **Canonical deferral cites** (L4 targets needing the chiral srs / winding grid):
  clm-67jn9o 0.75 (charge=winding, Witten/Z3, baryon-scope), clm-8c3yhs 0.70 ((2,3)
  winding uniqueness), clm-unk0bd 0.65 (electron body topology). master-equation.md:20
  two-3s disambiguation: A1 dilatation-MASS '3' (the cage, bucket A) ⊥ Cosserat (2,3)
  WINDING '3' (charge/spin/μ, bucket B).

---

## RUNG-1 EXISTENCE suite results (this pass)

| Test | Frozen bin | Result |
|---|---|---|
| **T3.3** Γ=−1 wall on posited cage | Γ_bulk crosses OP2_GAMMA_BULK_MAX=−0.25, monotone toward −1, →0 in vacuum; literal −1 unreachable | **PASS** — Γ_min(0.95)=−0.283 (crosses), Γ_min(0.99)=−0.454 (deepens), vacuum=0, floor>−1. α-FREE (Z_eff=√S) |
| **T3.4a** mass=cutoff (gapped bound mode) | discrete gapped ω_cutoff>0, ipk>1, peak/mean>50, oscillates | **PASS** — ω_cutoff≈2.87 (natural units), ipk=15, peak/mean≈456, 23 zero-crossings. m_e VALUE never read off the cage |
| **T3.4b** cold/α-FREE Q | Q finite & >0 from cold dynamics; then report vs 137 downstream | **PASS (FORM-bin)** — Q_ringdown≈30.8, Q_linewidth≈3.8, finite & >0, α-bake guards clean. **DOWNSTREAM: NOT 137 → the corpus Q=1/α is an instance-baked ECHO, not cage-emergent (clean chord-vs-echo negative)** |
| **T3.4c** zero-drive persistence | late/mid>0.8 AND late_min>0.05·amp0 | **PASS** — late/mid≈1.31, late_min≈0.34. Non-radiating standing mode; ≠ topological-winding protection |

**Measurement-design finding (Rule 10, surfaced at integrator time):** the posited
Gaussian core does NOT ring under a monopole/DC kick — it slowly RELAXES (an
FFT-bin-1 artifact whose ω scales as 1/n_steps). The discrete bound mode requires
a radial-SHELL breathing kick (∂_t V on the wall, no monopole DC). Recorded in
T3.4a's docstring.

---

> The KB-leaf / Vol9 propagation is the **separate completion-ritual pass** (after
> these results verify). This document is the suite's companion coverage map +
> gap register only — it does not land KB-leaf or manuscript updates.
