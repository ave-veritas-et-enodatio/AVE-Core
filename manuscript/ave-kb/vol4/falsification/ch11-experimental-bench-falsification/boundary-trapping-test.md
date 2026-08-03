[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-h55fy1]
path-stable: "referenced from vol3 as sec:boundary_trapping"
-->

## Protocol 10: Orbital Detritus and Boundary Trapping

> **🔴 FLAGGED 2026-07-19 (deep-space reactive-bulk ruling, Rule-12 — the Protocol-10 body below is PRESERVED verbatim; the flag recasts its status).** This protocol is a **consumer** of the demoted deep-space stall mechanism (`clm-h55fy1`). Its trapping mechanism — detritus that experiences "a sudden spike in Inductive Drag (topological friction), **shedding orbital kinetic energy**" (`:19`) — is the sub-yield bulk resistive loss **DEMOTED** by the ruling (Grant, in-chat 2026-07-19: the deep-space bulk coupling to slow matter is **lossless / pure-reactance**; primary banners on `vol_1_foundations/chapters/04_continuum_electrodynamics.tex` + `../../../vol1/dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md`). **(1)** The *impedance-boundary / termination-shock* framing (a reflection at an impedance step) can survive as a **reactive** event; the *energy-shedding drag* that stalls the body is retracted. **(2)** The falsification target is **FLIPPED into a discriminator**: the demoted mechanism predicts a Pioneer-transit drag-spike *scaling with velocity*; the reactive ruling predicts **zero energy-shedding drag below the (Cherenkov/Mach) radiation threshold** — a `v`-scaling drag-spike would falsify the reactive reading, its absence the resistive stall. The Asteroid-Belt / Oort structure re-derives as **band-structured reactive coupling** (structure-at-resonances; cf. Kirkwood cavity modes, `../../../vol3/cosmology/ch06-solar-system/kirkwood-gaps-cavity-modes.md`), **SPEC'd, not run** (Grant-gated). Full arc + attribution: `research/2026-07-19_deep-space-reactive-bulk-walk_RECORD.md`.

A standing anomaly in standard orbital mechanics is the distinct, rigid localization of macroscopic detritus into specific zones, such as the Asteroid Belt and the Oort Cloud. While standard models often rely on complex, ad-hoc planetary shepherding resonance theories (like Jupiter's gravitational influence) to explain this containment, they struggle to explain the sheer uniformity of the deep-space Oort Cloud boundary.

The non-linear AVE topological framework predicts these zones natively as a requirement of macroscopic inductive drag. The Sun's massive gravitational core draws a tremendous topological "slipstream" through the background chiral Laves K4 Cosserat crystal (LC Network in continuum-EM dialect).

As this local dielectric strain ($h_{\perp} \propto \frac{1}{r}$) falls off with distance, it eventually intersects and collides with the static background impedance floor of deep galactic space. This intersection creates a sharp topological sheer boundary — a domain where the localized vacuum impedance gradient diverges rapidly.

### Macroscopic Filtering and Falsification

Any low-mass detritus traversing this impedance boundary will experience a sudden spike in Inductive Drag (topological friction), shedding orbital kinetic energy and ceasing transverse migration.

Therefore, the Asteroid Belt and Oort Cloud are not random accumulations; they are the physical manifestations of the Inner and Outer termination shocks of the Solar metric slipstream.

Falsification of this topological theory relies on logging the transit velocities of deep-space probes (e.g., the Pioneer Anomaly). A probe crossing the $\sim 15{,}000$ AU Oort Cloud transition zone should mathematically register a sudden, otherwise inexplicable spike in transit drag as it pierces the dielectric sheer boundary, confirming the absolute macroscopic mutual inductance limit of the Solar metric.

> **🔴 CLAIM-BODY RELABEL (dated 2026-07-20, ratified-by-merge #741; KEEP-BOTH — the Protocol-10 body above is PRESERVED verbatim; this note relabels the falsifier at the claim-body level, formalizing the `:11` status banner).** The falsification target defined in this section — a Pioneer-transit "**sudden spike in transit drag**" **scaling with velocity** — is **RELABELED to a reactive-reflection / zero-drag `v`-independence test.** The reactive deep-space ruling predicts **zero energy-shedding drag below the Cherenkov/Mach radiation threshold**, at most a **bounded, phase-coherent reactive reflection** at the impedance step (`Γ = (Z_2-Z_1)/(Z_2+Z_1)`, energy-conserving) — NOT a secular `∝v` deceleration. A measured `v`-scaling drag-spike would falsify the *reactive* reading; its absence falsifies the *resistive stall*. **Reachability: FUTURE.** The discriminating coordinate is the `~15,000` AU Oort/yield transition; **existing deep-space nulls do NOT yet discriminate** — Pioneer 10/11, Voyager, and New Horizons sit at ~50–160 AU (~2 OOM *inside* the boundary) and the Pioneer anomaly is thermal-recoil-confounded, so those nulls bound only inner-region smooth drag. Per the band-map derivation D1 / repair R1 (`research/2026-07-19_deep-space-band-map_derivation.md` §5, merged #741). Solidity unchanged (0.30, do not build on).

> **⚑ CROSS-VOLUME NUMBER CONFLICT — FLAGGED 2026-08-03, DELIBERATELY NOT RECONCILED (Rule 12: the Protocol-10 body above stays byte-untouched).**
>
> **Vol 3 books `r_sat ≈ 7,439 AU`; Vol 4 books `~15,000 AU` for the claimed same boundary; one-object-or-two routed to Grant 2026-08-03.**
>
> Receipts. **Vol 4 (this leaf, `:25`; also [`vol4/claim-quality.md`](../../claim-quality.md):1123, `:1128`, `:1154`, `:1156`; print twin `vol_4_engineering/chapters/11_experimental_falsification.tex`:370):** *"$\sim 15{,}000$ AU Oort Cloud transition zone"* — an **empirical/round** figure, with no derivation given anywhere in Vol 4. **Vol 3 ([`oort-cloud-saturation-boundary.md`](../../../vol3/cosmology/ch06-solar-system/oort-cloud-saturation-boundary.md), print twin `06_solar_system.tex`):** `r_sat = √(GM_☉/a₀) = 7,438.9 AU` — a **derived** figure from `a₀ = c·H_∞/2π`. **A third number is in the corpus:** the illustrative driver `src/scripts/vol_3_macroscopic/simulate_oort_cloud_trap.py`:76 hand-centers its Oort Gaussian at `10^4.2 ≈ 15,800 AU` (the script's own docstring already discloses the centers are *inputs, not predictions*).
>
> **The gap is a factor of 2.0**, which is far outside the `-5.5%` a₀-provenance band on `r_sat` (10.7% `a₀` deficit propagated through `r ∝ a₀^(-1/2)`). So the two numbers are not the same quantity computed to different precision.
>
> **NOT reconciled here, and the reason is physics, not caution.** Reconciling requires answering whether the Vol-3 `g_N = a₀` field isocline and the Vol-4 "Oort transition zone" are **one object or two** — i.e. whether the Axiom-4 onset radius and the yield/impedance-step boundary are the same surface. That is a substrate question, **Grant's call, routed 2026-08-03**. Picking either number would silently answer it (flag-don't-fix).
>
> **Companion:** the Vol-3 containment claim ("falls within the observed Hills Cloud range") was **RETRACTED 2026-08-03** as propagation of the merged 2026-07-19 ruling; `r_sat` was relabeled to the solar Axiom-4 onset radius under internal-field keying. Nothing in Vol 4's grades or claims moves on that account. Docket: [`2026-08-03-oort-walkback-propagation.md`](../../../../../_orchestration/docket-entries/2026-08-03-oort-walkback-propagation.md).

---
