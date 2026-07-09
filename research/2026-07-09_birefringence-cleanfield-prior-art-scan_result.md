# RESULT — Clean-field / prior-art scan for the SVE birefringence Letter (adversarial, deep-research + session adjudication)

**Date:** 2026-07-09 · **Status:** COMPLETE (with 2 owed follow-ups flagged) · **Supersedes/extends:** the 2026-07-03 prior-art exposure scan (which returned CLEAN-FIELD for the specific geometry).
**Method:** deep-research harness (107 agents, 6 search angles, 24 primary sources fetched, 101 claims extracted, 25 adversarially verified 3-vote, 23 confirmed / 2 refuted) + a first-pass manual WebSearch (all-optical / vacuum-Kerr / E144 / PVLAS) + **session adjudication** (I decide, the harness retrieves).
**Question under test:** does ANY completed/published measurement constrain the SVE **electric-route** vacuum birefringence — field-independent `δn_bir = −½(E/E_c)² ≈ 2.2×10⁵ × δn_QED`, `E_c=√α·E_Schwinger≈1.13×10¹⁷ V/m`, ≈3×10⁻⁷ at the demonstrated 10²¹ W/cm² pump — in any propagating/radiative configuration?

---

## ★ VERDICT — CLEAN-FIELD CONFIRMED (primary threat), with ONE referee-objection to preempt + 4 thin vectors to close

The core clean-field claim **survives**: the optical-pump / X-ray-probe (and the all-optical) electric-route birefringence measurement is **genuinely un-run**, and — the strongest evidence — **the field's own leading theory groups say so**, not us:
- Karbstein et al. 2021 (New J. Phys. 23, 095001), verbatim: *"quantum vacuum nonlinearities in macroscopic electromagnetic fields have so far not been observed in a controlled laboratory experiment."*
- BIREF@HIBEF Collaboration Letter of Intent 2024 (arXiv 2405.18063), verbatim: this *"fundamental tenet … is yet to be tested in the laboratory."*

This is corroboration from non-adversarial parties (Jena/HZDR + the collaboration itself). A July-2026 cross-check found no completed BIREF@HIBEF pump-on result. **So the prediction is a genuine forward prediction, not a retrodiction.**

**But two things a "100% clean" claim must NOT paper over:**
1. **★ The heavy-ion light-by-light objection (a referee-press, NOT a bound — must be preempted in the Letter).**
2. **Thin coverage on 4 vectors** (vacuum n₂/Kerr, LSW/dichroism, DeLLight, astrophysical) + one specific completed all-optical vacuum experiment (Bernard 2000) whose bound-vs-SVE mapping was not resolved.

---

## Per-vector table

| # | Vector | Strongest completed measurement | Observable / field-config | Verdict | Type |
|---|---|---|---|---|---|
| 1 | All-optical laser–laser birefringence | **none** — proposals only (Luiten-Petersen 2004; Ataman 2018 PRA 97 063811; Ataman-Nakamiya 2025; PRR 7 023026 2025) | propagating optical, projected sensitivity only | does NOT bound | **no measurement exists** (strong) |
| 2 | XFEL X-ray pump-ON birefringence (the exact geometry) | **none** — LoI/proposal stage (Karbstein-Sundqvist 2016 PRD 94 013004; Karbstein 2021 NJP 23 095001; BIREF@HIBEF LoI 2024 arXiv 2405.18063) | optical pump + X-ray probe forward δn; no pump-on data | does NOT bound | **no measurement exists** (strong) |
| — | (out of scope) PVLAS / BMV / OVAL | Δn~3×10⁻²³ T⁻² (PVLAS, static/pulsed **B**) | static-magnetic route | OUT OF SCOPE — model predicts δn=0 for static B by construction (circulation-keying) | side-prediction confirmed |
| — | (not a measurement) X-ray polarimeter purity floor | 2.4×10⁻¹⁰ (Marx 2013; since improved by diamond channel-cut) | pump-OFF instrument capability | NOT a bound — the floor the prediction sits ~7 OOM above | capability demo |
| 4 | Heavy-ion light-by-light (ATLAS/CMS Pb-Pb) | **ATLAS 2019** γγ→γγ, 8.2σ, σ_fid~78 nb (arXiv 1904.03536); Born-Infeld bound M≳100 GeV (Ellis-Mavromatos-You 2017, PRL 118 261802) | real 2→2 wide-angle scattering **cross-section** from quasi-real nuclear-Coulomb photons; **no coherent pump** | does NOT bound the forward δn coefficient | **wrong observable/regime** (weaker) + ★ see caveat |
| 3 | Vacuum n₂ / Kerr | thin — no surviving standalone claim (first-pass: only *material* Kerr found; **Bernard 2000** LULI four-wave-mixing found in search, unresolved) | — | provisionally does NOT bound | thin — owed |
| 6 | LSW / vacuum dichroism (ALPS, OSQAR) | OSQAR photon-regeneration null (static **B**) | axion-like parity-odd rotation, static B | provisionally does NOT bound (different signature: pure retardance vs rotation; static B) | thin — owed |
| 7 | DeLLight / interferometric vacuum-index | projected sensitivity only, no pump-on result | — | does NOT bound | thin — owed |
| 8 | Astrophysical | magnetar polarization inference | not controlled-lab; static-B / co-propagating (Letter already argues geometric suppression) | does NOT bound | thin — owed |

---

## ★ The one real thing the scan surfaced — the heavy-ion LbL / four-photon-coupling objection

**This is NOT an existing bound. It IS the sharpest surviving referee-press, and the Letter does not yet address it.**

The chain a skeptical referee will build:
1. ATLAS measured γγ→γγ (light-by-light) in ultraperipheral Pb-Pb, **SM-consistent** (8.2σ observation, cross-section matches QED).
2. In QED, the vacuum birefringence δn **and** the LbL scattering cross-section descend from the **same** Euler–Heisenberg four-photon coupling.
3. SVE claims a δn coefficient **2.2×10⁵ × QED**. If that enhancement lived in the four-photon *vertex*, it would inflate the LbL cross-section by a comparable (indeed squared, ∝amplitude²) factor — and ATLAS would have **excluded** it.

**Why it is not actually a bound (the decoupling — sound but model-dependent):** SVE's enhancement is **not** a perturbative four-photon vertex modification. It is a *constitutive saturation* of the vacuum permittivity, `ε=ε₀√(1−A²)`, that responds to a **strong coherent background field** (the pump). ATLAS LbL has **no coherent background** — it is incoherent 2→2 scattering of two individual quasi-real photons at GeV wide angle. The saturable-ε forward response (coherent, strong-background-keyed, small-angle/forward) and the wide-angle incoherent γγ→γγ scattering are **dissociable limits of the four-photon amplitude** (cross-section ∝ amplitude²; forward δn ∝ amplitude). The one published analog — Ellis-Mavromatos-You's ATLAS bound on **Born-Infeld** (the archetypal saturating NED) — is on the polarization-averaged **cross-section** and, tellingly, B-I is the *birefringence-free* NED, so its LbL bound says nothing about a δn.

**Recommendation:** the Letter should carry a short preemptive paragraph (Sec. on prior nulls / forward-prediction) stating: (a) SVE's tree-level enhancement lives in the coherent-forward strong-background channel, decoupled from the wide-angle incoherent γγ→γγ cross-section ATLAS constrains; (b) ATLAS therefore does not bound the electric-route coefficient; (c) acknowledge honestly that this decoupling is a model feature, not an ATLAS-tested fact. Stating it *before* a referee raises it is far stronger than being asked.

---

## Owed follow-ups (before external submission)

1. **Close the 4 thin vectors** with a dedicated targeted pass — in particular **Bernard et al. 2000** (Eur. Phys. J. D 10, 141, "Search for stimulated photon-photon scattering in vacuum"): a *completed* all-optical vacuum four-wave-mixing measurement at LULI that set an upper limit on the vacuum photon-photon cross-section (~17 orders above the QED cross-section). First-order mapping: SVE's amplitude enhancement 2.2×10⁵ → cross-section enhancement ~(2.2×10⁵)²~5×10¹⁰ × QED, still far below Bernard's ~10¹⁷×-QED bound ⇒ **does not bound SVE** — but this mapping (saturable-ε forward response → a four-wave-mixing cross-section) is model-dependent and should be done rigorously, not asserted.
2. **Add the LbL-decoupling paragraph to the Letter** (above).

## Residual caveats (honest)
- **Time-sensitivity:** fast-moving field; ReLaX recently inaugurated, BIREF@HIBEF background runs scheduled. Vector-2 clean-field requires re-verification on any future timescale (re-run this scan before submission if months pass).
- **ReLaX 10²¹ W/cm² "demonstrated":** the surviving-claim set did NOT independently corroborate a ReLaX intensity-demonstration primary source — treat that operating point as the Letter's own input, not corroborated here. (Worth a citation check.)
- **Polarimeter floor:** 2.4×10⁻¹⁰ is the 2013 value, since improved; the ~7-OOM headroom is order-of-magnitude robust regardless.
- **Vectors 3/6/7/8** rest on thinner footing than 1/2/4 — see owed follow-up #1.

## Sources (primary, deep-research surviving set)
- Luiten & Petersen 2004 — https://arxiv.org/abs/physics/0402071
- Ataman 2018 (PRA 97 063811) — https://arxiv.org/abs/1807.11299
- Ataman & Nakamiya 2025 (Phys. Scr. 100 075537) — https://iopscience.iop.org/article/10.1088/1402-4896/ade5d7
- laser-induced VB via enhancement cavities (PRR 7 023026, 2025) — https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.7.023026
- Karbstein & Sundqvist 2016 (PRD 94 013004) — https://arxiv.org/pdf/1605.09294
- Karbstein et al. 2021 (NJP 23 095001) — https://arxiv.org/pdf/2105.13869 · https://iopscience.iop.org/article/10.1088/1367-2630/ac1df4
- BIREF@HIBEF Letter of Intent 2024 (arXiv 2405.18063) — https://arxiv.org/abs/2405.18063
- Marx et al. 2013 (PRL 110 254801, X-ray polarimeter purity) — https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.110.254801/fulltext
- ATLAS LbL 2019 (arXiv 1904.03536) — https://arxiv.org/pdf/1904.03536
- Ellis-Mavromatos-You 2017 (PRL 118 261802, B-I from LbL) — https://arxiv.org/abs/1703.08450
- Bernard et al. 2000 (Eur. Phys. J. D 10 141) — flagged for the owed rigorous mapping
- OSQAR photon-regeneration null — https://www.researchgate.net/publication/1904210

---

## ADDENDUM (2026-07-09, same day): the LbL objection ADJUDICATED — cross-check refuted the first defense; EFT-scope resolution adopted (Grant path a+b)

**The make-or-break derivation ran (implementer cross-check + in-chat orchestrator derivation, reconciled).** Outcome:

1. **Two of three escape mechanisms REFUTED.** (i) Forward-vs-wide-angle: FALSE — the same local χ³ feeds the forward δn and the wide-angle 2→2 amplitude; the wide-angle cross-section carries the SQUARED enhancement (χ³ ratio 2.36×10⁵ → σ ratio 5.6×10¹⁰). The v5 first-draft paragraph built on this mechanism was WRONG and is superseded (PR #594 commit 2). (ii) Frame-dependence: INSUFFICIENT — O(1) angular/polarization effect; lab≈CMB frame to β~10⁻³; cannot bridge 10¹¹.
2. **Orchestrator derivation error owned:** the in-chat "mildest (ω₀/ω)² rolloff makes SVE invisible at GeV" compared a rolled-off SVE against an un-rolled-off QED box. The box itself dies ~(ω₀/ω)⁴ vs its contact extrapolation, so under ANY power-law dispersion anchored at ω₀=m_ec² the 2.2×10⁵ enhancement is a frequency-independent PREFACTOR surviving to GeV → contact/power-law readings are BOUNDED-BY-ATLAS (~11 orders χ³-method; ~22 orders contact-BI method, Λ_SVE≈0.27 MeV vs E-M-Y Λ≳100 GeV, verified).
3. **The adopted resolution (Grant ruling, path a):** the kernel is a LOW-FREQUENCY EFT with response scale ω₀ = m_ec²; collider kinematics (√s≈10⁴ħω₀) are OUTSIDE its domain — the same reason EH is never extrapolated to GeV. Above ω₀ the four-photon physics is the shared electron-pair box (the SM-consistent ATLAS result IS the shared physics). The constitutive channel's closure above ω₀ (hard lattice-band-edge mode cutoff vs power-law tail — the srs Brillouin-zone/Nyquist argument; a kinematic/basis statement outside the power-law families the cross-check bounded) is a NAMED OPEN ITEM, not asserted. Letter v5 (PR #594 commit 2) states all of this plainly.
4. **(path b) UV-completion derivation OPENED as a gated item:** χ³(ω) on the discrete srs network — nonlinear-TLM four-wave phase-matching of Bloch modes at/above the zone edge; front half gated on the open high-energy-carrier thread (what carries ω≫band-edge quanta; does it see the per-node kernel). If it lands, the Letter's scope-statement upgrades to derived consistency.
5. **In-band margins VERIFIED (paper-grade):** Bernard 2000 (EPJ D 10,141; 0.8 eV stimulated FWM at LULI): bound ~10¹⁸×σ_QED → ~7 orders above the enhanced prediction. SACLA X-ray: Inada 2014 (PLB 732,356) limit 1.7×10⁻²⁴ m² at ω_cms=6.5 keV vs σ_QED=2.5×10⁻⁴⁷ m² (Yamaji 2016, PLB 763,454) → ~12 orders above the enhanced prediction. [Supersedes the pre-verification "~8-9 orders" estimate above.] Both are COMPLETED, in-band, right-observable searches → strongest clean-field class; the enhanced in-band γγ cross-section is flagged as a candidate FOURTH testable consequence (a modern petawatt Bernard-type run could reach it).

**Vectors 6/7/8 CLOSED (second agent, adversarially verified):**
- **V6 ALPS/OSQAR:** completed measurements are ALP photon-REGENERATION in static-B (OSQAR PRD 92,092002: g_aγγ≲3.5×10⁻⁸ GeV⁻¹) — wrong observable AND wrong regime; no completed propagating-pump δn at either facility. CLEAN.
- **V7 DeLLight:** the ONLY experiment in the matched regime (propagating pump, crossed geometry, vacuum δn). Status: air proof-of-concept (PRA 109,053510) + pump-absent noise prototype (2026) — NO vacuum pump-on result. CLEAN (un-run). ★ STANDING WATCH: since the SVE coefficient is 2.2×10⁵×QED, an EARLY DeLLight vacuum run adjudicates SVE long before QED sensitivity — a near-term discriminator AND the likeliest future bound. Re-scan on every DeLLight data release.
- **V8 astrophysical (IXPE magnetars, 4U 0142+61 PNAS 2023 etc.):** static magnetar dipole B with radiation as PROBE not pump → zero-by-construction sector; cosmological birefringence = parity-odd ROTATION (different signature). CLEAN.

**Net verdict after adjudication: CLEAN-FIELD stands on every vector, now including the LbL objection — resolved by EFT-domain scoping (honest, stated in-Letter) rather than the refuted decoupling. The registered falsifier remains a genuine forward prediction; the model's real in-band γγ exposure (Bernard-class, DeLLight) is a feature: more near-term ways to kill or confirm it.**
