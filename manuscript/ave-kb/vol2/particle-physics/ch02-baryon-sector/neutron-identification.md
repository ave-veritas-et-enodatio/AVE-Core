[↑ Ch.2 — Baryon Sector](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-6kwzot, clm-w8jn3q]
path-stable: "referenced from common/full-derivation-chain + vol6/period-1/hydrogen + vol4/falsification/ch11 as canonical neutron identification"
-->

# Neutron — Canonical Identification + First-Principles Axiom Audit

The AVE-native canonical identification of the neutron, structured to parallel `proton-identification.md` (on sibling branch `analysis/proton-definition-canonical`, not yet merged to L3), `../ch01-topological-matter/electron-identification.md` (on sibling branch `analysis/electron-definition-canonical`), and [`../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md).

**Load-bearing finding:** the neutron in AVE is a **composite structure** — a proton ($6_2^3$ Borromean linkage) with an electron ($0_1$ unknot) topologically threaded through its central structural void: $\boxed{n = 6_2^3 \cup 0_1}$. This is mechanically SIMPLER than the Standard Model (which says the electron is *created* during β-decay): in AVE the electron *already exists*, threaded into the proton's void, and β-decay is the topological slip-event where the threading lock fails and the pre-existing electron is ejected. Charge neutrality is literal additive cancellation ($+1$ proton + $-1$ threaded electron = $0$), NOT Witten-effect quark cancellation.

**Two load-bearing derivation gaps:** (a) the mass split $m_n - m_p \approx 1.293$ MeV is mechanism-named (elastic-expansion tension from threading) but **not quantitatively derived** from a Faddeev-Skyrme calculation; (b) the mean lifetime $\tau_n \approx 880$s is mechanism-named (dielectric tunneling + CMB-noise-driven threading slip) but **the rate is not derived** from a corpus calculation. Both gaps are flagged in the corresponding matrix rows (parallel to the C13b bullet-cluster offset and C14 DAMA amplitude TBD-pin derivation-gap class).

## §1 — Canonical 4-property definition

<!-- claim-quality: clm-6kwzot -->

The neutron in AVE is defined by **four tightly-coupled topological/dynamical properties**:

1. **Composite topology: $n = 6_2^3 \cup 0_1$** — the canonical Vol 2 Ch 2 framing (per `vol_2_subatomic/chapters/02_baryon_sector.tex:294`): a proton Borromean linkage ($6_2^3$, three mutually entangled flux loops, $(2,5)$ cinquefoil per the torus-knot ladder) with an electron $0_1$ unknot topologically threaded through its central structural void. NOT a different $(2,q)$ family entry; NOT a $6_2^3$ with axial twist; NOT a $6_2^3 \cup 3_1$ (trefoil). Three stale corpus framings inconsistent with this canonical are flagged in §3 below.
2. **Charge neutrality via literal additive cancellation** — the proton contributes $+e$ (Ax2 TKI charge twist at Borromean cage center); the threaded electron contributes $-e$ (the $0_1$ unknot's charge per electron canonical leaf); net charge = $0$. This is mechanically simpler than the Standard Model's udd quark-content explanation (the corpus uses ZERO udd/uud framing — `grep` confirmed zero matches across all repos for "udd").
3. **Mass split mechanism: elastic-expansion tension** — per Vol 2 Ch 2 figure caption (`02_baryon_sector.tex:299`): "The elastic expansion required to accommodate the threaded electron accounts for the $1.293$ MeV mass surplus of the neutron over the proton." Ax1 forbids any flux tube from shrinking below transverse thickness $1\,\ell_{node}$, so threading an electron tube into the proton's core forces the Borromean rings to stretch outward — the elastic tension of this stretch is the $\Delta m c^2 = 1.293$ MeV mass surplus. **Mechanism canonical; quantitative value not derived (TBD).**
4. **β-decay via dielectric tunneling + topological slip** — outside a nucleus, the threaded electron is metastable. Stochastic CMB-noise-driven lattice perturbations occasionally drive the electron to tunnel through the Borromean dielectric lock barrier; once the topological lock slips, the electron is ejected and the proton core elastically relaxes. The angular-momentum-conservation shockwave shed by the lattice during this structural relaxation IS the antineutrino $\bar{\nu}_e$ (per `proton-neutron-mass-split.md:6`). **Decay channel canonical; rate constant $\tau_n \approx 880$ s not derived (TBD).**

## §2 — First-principles axiom audit per property

### Topological/dynamical properties (the 4 from §1)

| Property | Axiom support | Derivation status | Open items |
|---|---|---|---|
| 1. Composite $n = 6_2^3 \cup 0_1$ topology | Ax1 (K4 chiral lattice supports topological-link composites; the central Borromean void can accommodate a threaded $0_1$ unknot per geometric topology) + Ax2 (the threaded electron's $-e$ TKI charge is preserved through the threading operation) | ✅ axiom-derived structurally | None on topology; some corpus framings (3 stale leaves per §3) need reconciliation |
| 2. Charge neutrality via additive $+1 + (-1) = 0$ | Ax2 TKI (charge is the integer topological twist count; the proton's $+1$ twist + the threaded electron's $-1$ twist sum directly) | ✅ axiom-derived | None — mechanically simpler than SM udd cancellation |
| 3. Mass split $m_n - m_p \approx 1.293$ MeV from elastic-expansion tension | Ax1 (flux tubes cannot shrink below $\ell_{node}$ → threading forces Borromean expansion) + Faddeev-Skyrme energy increase from the stretched configuration | ⚠️ **MECHANISM derived, MAGNITUDE not** — no FS calculation of threaded-knot energy producing 1.293 MeV; corpus uses empirical value as input downstream (e.g., He-4 binding) | **TBD-pin: derive 1.293 MeV from FS solver applied to threaded $0_1$-in-$6_2^3$ topology.** Same shape as proton mass eigenvalue derivation but with threaded-electron constraint. |
| 4. β-decay mechanism (dielectric tunneling + CMB-noise threading slip + antineutrino as angular-momentum shockwave) | Ax4 (saturation kernel governs the dielectric tunneling barrier) + Ax1 (lattice perturbations from CMB background) + classical angular-momentum conservation | ⚠️ **MECHANISM derived, RATE not** — no derivation of $\tau_n \approx 880$ s tunneling rate; empirical value used as input | **TBD-pin: derive $\tau_n$ from WKB tunneling through the threaded-knot dielectric barrier with CMB-noise driving.** Could explain bottle-vs-beam anomaly (`vol4/falsification/ch11-experimental-bench-falsification/existing-experimental-signatures.md:18-24` predicts wall phonon coupling lowers the bottle barrier ~9s, but magnitude not derived). |

### Observable properties — load-bearing audit

| Observable | Axiom support | Derivation status | Notes |
|---|---|---|---|
| **Rest mass $m_n \approx 1.001378\,m_p \approx 939.565$ MeV** | Composite of proton mass eigenvalue ($m_p$, ✅ axiom-derived to 0.002% per `proton-identification.md`) + threaded-electron elastic-expansion contribution (mechanism-only, not derived) | **PARTIAL** — $m_p$ component is the framework's flagship mass prediction (axiom-derived; the per-channel loop-role is a matched structural assignment, same class as the lepton couplings — see the parameter ledger); the $\Delta m \approx 1.293$ MeV addition is empirical input | Per §1 property 3 TBD-pin |
| Charge $0$ | Ax2 TKI literal addition | ✅ axiom-derived | Per §1 property 2 |
| Spin-½ | Same Cosserat microrotation + Finkelstein-Misner mechanism as electron and proton (Ax1); composite spin = $\frac{1}{2}_p + \frac{1}{2}_e$ angular-momentum-coupled to net ½ | ✅ axiom-derived | Inherits from `proton-identification.md` and electron-identification structural inheritance pattern |
| Mean lifetime $\tau_n \approx 880$ s (free) | Per §1 property 4: dielectric tunneling + CMB-noise threading slip | **MECHANISM, NO RATE** | TBD-pin per property 4 |
| Bottle-vs-beam lifetime anomaly (~9 s shorter in trapped material vs free beam) | Wall phonon coupling lowers the dielectric tunneling barrier in trapped configurations (per `existing-experimental-signatures.md:24`) | **POSTDICTED qualitatively, magnitude not derived** | Open testbed for the dielectric-tunneling mechanism if magnitude could be calculated |
| Magnetic moment $\mu_n \approx -1.913\,\mu_N$ (negative, anomalous in SM) | Composite of proton's $+2.793\,\mu_N$ + threaded-electron's $-2\,\mu_B$ rescaled to nuclear units, geometrically combined per Borromean configuration | **STRUCTURAL — full derivation TBD** | The SM treats this as a free parameter requiring careful quark-current modeling; AVE has a structural pathway via the composite topology but no derived value in the corpus |
| Charge radius (mean-square) | Composite of proton charge distribution + threaded electron's smearing | **STRUCTURAL — derivation TBD** | The neutron's small but nonzero $\langle r^2 \rangle$ is naturally explained by the threaded-electron composite |
| Decay product spectrum (electron + antineutrino + proton recoil) | Per §1 property 4 directly | ✅ structural | Mechanism canonical; spectrum shape derivation TBD |

### §2.1 — Why the mass split is structurally bounded (without being derived)

Even without a full FS calculation, the corpus provides a structural bound on the expected mass split. The proton has 🔴 *[dimensional-provenance relabel 2026-06-08]* ~~confinement radius $r_{opt} = \kappa_{FS}/c_5 = 8\pi/5 \approx 4.97\,\ell_{node}$~~ **dimensionless coupling-budget ratio $r_{opt} = \kappa_{FS}/c_5 = 8\pi/5 \approx 5.03$ (a pure number, NOT a length — $\kappa_{FS}=8\pi$ is a pure geometric constant per `constants.py:683-687`; the $\ell_{node}$ units were spurious)** per `proton-identification.md`. 🔴 **FLAG (separately suspect — inherits the same error):** the bound below treats "threading an electron unknot through the central void requires the Borromean rings to **expand by at least $\ell_{node}$ radially**" as a real-space radial expansion in $\ell_{node}$ units. Because the only measured proton size is the sub-node $D_p = 0.841$ fm ($\approx 460\times$ smaller than $\ell_{node} = 386$ fm), an "$\ell_{node}$ radial expansion" length premise is **not established** and is flagged for adjudication (it does not follow from the now-dimensionless $r_{opt}$). The corresponding strain energy is bounded above by the linear-elastic stiffness of the Borromean cage times the strain squared. This bound is consistent with — but does not derive — the empirical $\Delta m c^2 = 1.293$ MeV. **Derivation TBD: compute the FS energy of the $6_2^3 \cup 0_1$ composite minus the FS energy of the bare $6_2^3$, in units of $m_e c^2$.**

## §3 — Framing translation guide (reconciliation of 8 framings)

The corpus carries multiple historically-evolved framings of the neutron, three of which contradict the canonical Vol 2 framing. The translation guide pins each framing's substrate role and reconciles against the canonical.

<!-- claim-quality: clm-w8jn3q (the SM-translation row + the Strong-CP θ row below carry the two-ontology reconciliation: Witten fractions = effective dressing of the fundamental integer charge; Grant-ratified 2026-06-23) -->

| Framing | Source | Substrate role | Reconciliation against canonical |
|---|---|---|---|
| **Canonical: $n = 6_2^3 \cup 0_1$** | `vol_2_subatomic/chapters/02_baryon_sector.tex:294,299` + `vol_2_subatomic/chapters/06_electroweak_and_higgs.tex:660` + `proton-neutron-mass-split.md:6` | Composite topology: proton Borromean + threaded electron unknot | **Authoritative.** This is the canonical AVE neutron identification per Vol 2 source. |
| Vol 4 falsification: $n = 6_2^3 \cup 3_1$ (trefoil threaded, not unknot) | `vol4/falsification/ch11-experimental-bench-falsification/existing-experimental-signatures.md:22` + `vol4/falsification/ch11-experimental-bench/existing-signatures.md:18` | **STALE — contradicts canonical.** Wrong threaded knot (trefoil instead of unknot). | **FLAGGED FOR REVISION 2026-05-17.** Vol 4 leaves should be updated to match Vol 2 canonical ($0_1$ unknot, not $3_1$ trefoil). Per AGENTS §6 authority rules: Vol 2 source wins. |
| Vol 6 hydrogen: $n = 6_2^3 + \text{axial twist}$ | `vol6/period-1/hydrogen/structure-isotope-stability.md:8` | **STALE — contradicts canonical.** Wrong mechanism (axial twist instead of threaded unknot link). | **FLAGGED FOR REVISION 2026-05-17.** Vol 6 hydrogen leaf should be updated to canonical $6_2^3 \cup 0_1$ threading framing. |
| Standard Model: $n = u + d + d$ quarks (udd composition) | External (PDG, QCD textbooks); not in corpus | SM framing — describes the same particle in different ontology | **AVE has NO internal udd/uud framing** (zero corpus matches). The udd substructure observed in deep inelastic scattering is the SM projection of the Borromean linkage's three flux loops (per `topological-fractionalization.md`); the threaded electron contributes no quark-like flux loop — it sits in the central void. **Translation:** SM "u-d-d" maps to AVE "$(2,5)$ Borromean cage + threaded $0_1$ via Witten-effect fractional charges + literal threaded electron." The two ontologies make the same predictions about observables; AVE's mechanical picture is the substrate explanation of why the SM ontology works. **🔵 TWO-ONTOLOGY CONTRADICTION FLAG RESOLVED — RECONCILED 2026-06-23 (`clm-w8jn3q`, Grant-ratified):** the apparent A-vs-B tension (Witten fractional charges vs integer charge-linking) is NOT a contradiction. Ontology B (the integer linking $\mathcal{Q}$) is FUNDAMENTAL; Ontology A (the Witten fraction) is the EFFECTIVE appearance — a body-angular-momentum $\mathcal{J}$ dressing that leaves $\mathcal{Q}$ invariant. This row's "same predictions … why the SM ontology works" is the half-statement that the reconciliation completes with a substrate mechanism. **Scope note:** the "$+1 + (-1) = 0$ literal additive cancellation, NOT Witten-effect quark cancellation" at the load-bearing finding (line 13) + §1 property 2 (line 24) is scoped to the NEUTRON's charge-NEUTRALITY balance ONLY — it does NOT assert a flat A-vs-B incompatibility, and is consistent with the reconciliation (the neutron's net-zero comes from the literal $\mathcal{Q}$ integers of proton + threaded electron; the Witten fractions are the effective dressing of the proton's internal three-loop structure). |
| β-decay flux-loop break (attosecond) | `vol_2_subatomic/chapters/06_electroweak_and_higgs.tex:131` | Substrate detail: during β-decay slip event, the primary topological knot "undergoes extreme mechanical shear and must structurally split to shed phase-frequency. This splitting process breaks the continuous magnetic flux loop open for a fraction of an attosecond." | Same event as the dielectric tunneling described in §1 property 4 — different aspect (attosecond-timescale microdynamics vs ~880 s tunneling rate). **Reconciliation:** the tunneling event itself is the slow stochastic part (~880 s typical); once it triggers, the actual topological flux-loop break is attosecond-fast. Both descriptions are aspects of the same event. |
| He-4 tetrahedral Borromean braid stability | `proton-neutron-mass-split.md:8-44` + `vol6/framework/computational-mass-defect/mutual-coupling-constant.md` | The threaded-electron metastability is locked in nuclear binding via $K_4$ full-mesh high-Q (≈ 19.22) breathing mode | **Reconciliation:** inside He-4, the high-Q $K_4$ mesh provides a coherent resonant lock that prevents the CMB-noise-driven tunneling that destabilizes free neutrons. The neutron is stable in He-4 because the breathing-mode oscillation periodically reinforces the dielectric tunneling barrier faster than CMB noise can drive the slip. **Mechanism canonical; quantitative threshold not derived.** |
| Isotopic stability curve $N \approx Z + 1.2\alpha Z^2$ | `common/translation-tables/translation-particle-physics.md:25` | Optimal neutron count for stable isotopes scales with $Z$ via geometric Coulomb penalty + topological packing | **Reconciliation:** the threaded-electron neutron provides the charge-cancellation needed to maintain Borromean stability at high $Z$ where Coulomb repulsion between proton flux loops would otherwise destabilize the nucleus. **Mechanism structural; $1.2\alpha Z^2$ scaling not derived in corpus.** Flag for future derivation work. |
| Strong-CP / neutron EDM ($\theta \neq 0$ implications) | `vol_2_subatomic/chapters/10_open_problems.tex:33` | Topological θ-vacuum of the proton's Borromean cage; CP-violation would manifest as neutron electric dipole moment | **Reconciliation:** AVE's Witten-effect $\theta \in \{0, \pm 2\pi/3, \pm 4\pi/3\}$ for fractional quark charges (per `topological-fractionalization.md`) provides natural CP-preserving discrete θ-values. The neutron EDM null observation supports the discrete-θ picture over continuous-θ Strong-CP problem. **Open question:** is this AVE explanation rigorous, or just suggestive? *(Partly addressed by `clm-w8jn3q` 2026-06-23: the discrete θ-values are the effective body-angular-momentum dressing of the fundamental integer $\mathcal{Q}$; the discreteness traces to the $N$-fold body-rotation share $1/N$, which is FORM-forced — but the specific value $N=3$ remains the FED-IN observed loop count, so "rigorous vs suggestive" stays OPEN on the value, RECONCILED on the form.)* |

## §4 — Honest scoping of derivation gaps

Two TBD-pin derivation gaps need to be flagged as parallel to the C13b/C14 derivation-gap class in the divergence-test substrate map:

1. **Mass split $\Delta m = m_n - m_p = 1.293$ MeV** — mechanism (elastic-expansion tension from threading) is canonical and structurally bounded; the quantitative derivation via Faddeev-Skyrme solver applied to the $6_2^3 \cup 0_1$ composite topology is NOT in the corpus. Derivation pattern would parallel `self-consistent-mass-oscillator.md` for the proton but with the additional threaded-electron constraint adding to the FS energy integral.

2. **Mean lifetime $\tau_n \approx 880$ s (free neutron)** — mechanism (dielectric tunneling through Borromean lock barrier driven by CMB noise) is canonical but the rate is NOT derived. Derivation would require WKB tunneling calculation through the threaded-knot dielectric barrier potential, with CMB-noise spectrum providing the driving stochastic force. The bottle-vs-beam ~9 s anomaly is qualitatively explained by wall phonon coupling lowering the barrier but the magnitude is not derived.

Both derivations are FAR more tractable than they sound, because the corpus already provides:
- The proton mass eigenvalue derivation chain (per `proton-identification.md`)
- The Faddeev-Skyrme solver pattern (per `self-consistent-mass-oscillator.md`)
- The dielectric tunneling formalism (per Ax4 saturation kernel + standard WKB)
- CMB noise spectrum (well-characterized empirically)

**Next-up implementer work:** stand up a focused derivation pass for one or both of these gaps. Estimated effort 1-3 sessions per gap, given the corpus structural ingredients already present.

## §5 — Implications for the divergence-test matrix

This leaf surfaces three new matrix-relevant items for future tracking:

1. **A new META row candidate:** "Neutron mass split + lifetime derivations TBD" — parallel to C13c three-mechanism-unification META, tracks the open derivation gaps as theoretical-gap items.

2. **Translation guide cleanup:** three stale corpus framings ($6_2^3 \cup 3_1$ in Vol 4, $6_2^3 + \text{axial twist}$ in Vol 6 hydrogen, and the bottle-vs-beam quantitative anomaly) need scope-correction commits to align with the canonical Vol 2 framing.

3. **Cross-row physics consistency:** the threaded-electron mechanism implies that some of the "weak-force" matrix rows (e.g., neutron decay-related anomalies) should be reclassified as Ax1+Ax4-derived topological transitions rather than as separate force-mediated processes. This may affect existing weak-force-class framing in Vol 2 Ch 6 and Vol 4 falsification chapters.

## Cross-references

- **Canonical manuscript source:**
  - `manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex:292-301` (canonical Vol 2 source for $6_2^3 \cup 0_1$)
  - `manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex:131,660` (β-decay flux-loop break + corroborating caption)
- **KB distillations:**
  - [`proton-neutron-mass-split.md`](proton-neutron-mass-split.md) — KB distillation of canonical neutron framing + He-4 binding
  - [`self-consistent-mass-oscillator.md`](self-consistent-mass-oscillator.md) — proton mass eigenvalue pattern that the neutron mass-split TBD would parallel
  - [`topological-fractionalization.md`](topological-fractionalization.md) — Witten-effect fractional quark charges for proton (informs SM-to-AVE translation in §3); carries the canonical two-ontology reconciliation `clm-w8jn3q` (Witten fractions = effective dressing of the fundamental integer charge)
  - [`../../../common/boundary-observables-m-q-j.md`](../../../common/boundary-observables-m-q-j.md) — the $\mathcal{Q}$ (1D linking) vs $\mathcal{J}$ (2D winding) boundary-integral separability that mechanizes the reconciliation (`clm-w8jn3q`)
  - [`../../../vol6/framework/computational-mass-defect/mutual-coupling-constant.md`](../../../vol6/framework/computational-mass-defect/mutual-coupling-constant.md) — He-4 binding K = 11.337 MeV·fm
  - [`../../../vol6/framework/computational-mass-defect/pn-junction-coupling.md`](../../../vol6/framework/computational-mass-defect/pn-junction-coupling.md) — p-n diode coupling forward-bias framing
- **Pattern templates for identification leaves:**
  - `proton-identification.md` (on sibling branch `analysis/proton-definition-canonical`, pulled for this leaf's pattern)
  - `../ch01-topological-matter/electron-identification.md` (on sibling branch `analysis/electron-definition-canonical`)
  - [`../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md)
- **Stale framings to flag for revision:**
  - `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/existing-experimental-signatures.md:22` (uses $6_2^3 \cup 3_1$ trefoil instead of canonical $0_1$ unknot)
  - `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench/existing-signatures.md:18` (same stale framing)
  - `manuscript/ave-kb/vol6/period-1/hydrogen/structure-isotope-stability.md:8` (uses "$6_2^3 + \text{axial twist}$" instead of canonical $\cup 0_1$ threading)
- **Experimental signatures:**
  - `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/existing-experimental-signatures.md:18-24` (β-decay bottle-vs-beam anomaly qualitatively postdicted)
- **Translation tables:**
  - `manuscript/ave-kb/common/translation-tables/translation-particle-physics.md:25` (isotopic stability $N \approx Z + 1.2\alpha Z^2$, not yet derived)
