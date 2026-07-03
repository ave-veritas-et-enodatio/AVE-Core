[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-pvlas1, clm-bdualb]
-->

## PVLAS / BMV Static-B Birefringence: the Null is CONSISTENT with AVE (Not a Falsification)

PVLAS, BMV, and the OVAL/ALPS-II lineage search for vacuum birefringence by applying a strong
**static** (or slowly-modulated, $\partial\mathbf B/\partial t \approx 0$ on the optical timescale)
magnetic field $\mathbf B$ transverse to a probe beam and reading the accumulated ellipticity. They
measure a **null** at the QED-expected level. This leaf records the AVE verdict: **the static-B null
is the expected AVE result, not a falsification of AVE.**

## §1 — Why a static B is transparent in AVE

The magnetic ($\mu$) grade of the vacuum LC tank is an **ideal relativistic inductor keyed on the
circulating current** $I$, not on the field magnitude $|\mathbf B|$:

$$
L_{eff}(I) = \frac{L_0}{S(A_I)}, \qquad A_I = \frac{I}{I_{max}}, \qquad I_{max}=\xi_{topo}c\approx124.4\,\text{A}
$$

([`relativistic-inductor.md`](../../circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md):15,:18;
node-up derivation [`node-up-small-large-signal.md`](../../circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md):§4;
full derivation + rescue-guard + the arithmetic-error catch in
[`research/2026-06-22_node-up-small-large-signal_result.md`](../../../../../research/2026-06-22_node-up-small-large-signal_result.md)).
The kernel argument is the **internal vacuum circulation** $I$, a rate/flux variable. By Lenz's law
internal circulation is induced only by a *changing* flux, $\partial\mathbf B/\partial t \ne 0$.

A PVLAS-class **static external** $\mathbf B$ has $\partial\mathbf B/\partial t = 0$ on the optical
probe timescale (the field is sustained by the magnet's transport current, not by any vacuum
circulation). Therefore:

$$
\partial\mathbf B/\partial t = 0 \;\Rightarrow\; I_{vac}=0 \;\Rightarrow\; A_I = 0
\;\Rightarrow\; S_\mu = 1 \;\Rightarrow\; \mu_{eff}=\mu_0 \;\Rightarrow\; \boxed{\delta n_\mu = 0\ \text{EXACTLY}}.
$$

The vacuum stays at $Z_{eff}=Z_0$ and is **transparent** — independent of how large the static field
is. This is **analytically exact**, not a numerical fit: the kernel argument $A_I=I_{vac}/I_{max}$ is
*identically zero* under a static $\mathbf B$, so $S_\mu=\sqrt{1-0^2}=1$ at **every** field strength
(hence trivially "flat" across $2.5\,\text{T}\to1\,\text{kT}$). The direct-kernel positive control
`src/tests/test_vca_node_regime_sweep.py` (which evaluates the Axiom-4 kernel directly, **not** the
fdtd engine) confirms $S_\mu=1$, $\delta n_\mu=0$ at $B=2.5,10,50,100,500,1000$ T. (The fdtd engine
would **not** reproduce this — it carries the live $|\mathbf B|$-keying VCA-R01 defect; see the
node-up code note,
[`node-up-small-large-signal.md`](../../circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md):§5.)

<!-- claim-quality: clm-pvlas1 -->
> **Not $B_{SNAP}$.** $B_{SNAP}=1.89\times10^9$ T is an energy-density scale
> ($B_{SNAP}^2/2\mu_0 = m_ec^2/\ell_{node}^3 = 1$; the **energy-density-matched** magnetic scale,
> `constants.py` `B_SNAP`), **not** the $\mu$-grade kernel argument. There is
> no $B/B_{SNAP}$ saturation of $\mu$ under a static field; the argument is $I/I_{max}$, and a static
> $\mathbf B$ produces $I_{vac}=0$.

<!-- claim-quality: clm-bdualb -->
> **✅ RESOLVED (Grant 2026-07-03, KEEP-BOTH — DISSOLVED-BY-DERIVATION).** The two magnetic
> yield-scales are BOTH correct and answer DIFFERENT questions; their ratio is the **exact, α-free
> geometric constant $\sqrt{8\pi}=5.013257$** (not an approximate ~5× coincidence), so the earlier
> "disagree by ~5×" flag was a **naming collision dissolved by derivation**:
> $$
> \frac{B_{SNAP}}{E_{yield}/c} = \frac{c\,B_{SNAP}}{E_{yield}} = \sqrt{8\pi} = 5.013257 \quad (\text{α CANCELS}).
> $$
> - **$B_{SNAP}$** (the **energy-density-matched** scale, `constants.py` `B_SNAP`) answers *"what
>   $\mathbf B$ stores the cell's rest energy in field-energy-density form?"* — energy-budget arguments
>   ($B_{SNAP}^2/2\mu_0 = m_ec^2/\ell_{node}^3$).
> - **$B_{dual}\equiv E_{yield}/c \approx 3.77\times10^8$ T** (a proposed coinage, `def-bdual1`; the
>   **field-amplitude-matched** scale) answers *"what is the duality image of the $T_2$ electric yield
>   wall?"* — field-scale/duality arguments (the $cB\leftrightarrow E_{yield}$ duality on $E_{yield}\approx
>   1.13\times10^{17}$ V/m). ($B_{dual}$ is coined here rather than $B_{yield}$ because $B_{yield}$ is
>   already overloaded in the corpus — see the research note; surfaced, not forced, per INVARIANT-S12.)
> - **Neither is the R3 / Route-C static-B $\mu$-kernel argument** (circulation-keyed, $I_{vac}=0$). The
>   verdict $A_I=0\Rightarrow\delta n_\mu=0$ is **untouched** — a static $\mathbf B$ never enters the
>   $\mu$-kernel as an amplitude, whichever B-scale a downstream argument nominally references.
>
> The bridge is a **definitional-identity / consistency-class** book-keeping fact (both scales are
> algebraic faces of the single $m_e$ import; the $\sqrt{8\pi}$ is a pure geometric constant with α
> cancelled — **not a chord, not emergence**). Full chain + numeric re-verification against
> `src/ave/core/constants.py` (rel $3.3\times10^{-11}$, α-free): claim `clm-bdualb`,
> [`research/2026-07-03_bsnap-byield-sqrt8pi-dissolution.md`](../../../../../research/2026-07-03_bsnap-byield-sqrt8pi-dissolution.md).
>
> *Original flag text (preserved for the record; git carries the full history):* the two magnetic
> yield-scales were flagged as disagreeing by ~5× — $B_{SNAP}=1.89\times10^9$ T (energy-density-matched)
> vs $E_{yield}/c\approx3.77\times10^8$ T (the duality image, now `def-bdual1`) — with two corpus
> magnetic-birefringence treatments keying on these scales; a scale was deliberately not picked pending
> Grant adjudication (flag-don't-fix). That adjudication is the KEEP-BOTH ruling above.

## §2 — The verdict: consistent, not falsifying

| Framework | Static-B birefringence prediction |
|---|---|
| **QED** (Euler-Heisenberg) | $\delta n \sim 10^{-23}$ at 5 T (real, below current sensitivity) |
| **AVE** | $\delta n_\mu = 0$ **exactly** (categorical; the $\mu$-grade is unloaded) |
| **PVLAS / BMV** | **null** at the QED level |

The PVLAS/BMV null is **consistent with AVE** and does **not** falsify it: AVE predicts exactly zero
static-B birefringence, so a null is the expected outcome. (The null is also consistent with QED,
whose $\sim10^{-23}$ is simply below sensitivity.) **PVLAS does not test AVE** — it applies the wrong
drive (static B, which leaves the $\mu$ grade unloaded). This corrects the earlier KB framing that
attributed $\delta n=0$ under static B to "lattice symmetry"; the correct reason is the **ideal
relativistic-inductor / circulation-keyed** $\mu$-grade (see the reason-fixed leaves
[`q-g20f-vacuum-polarization.md`](../../../vol2/particle-physics/ch06-electroweak-higgs/q-g20f-vacuum-polarization.md)
and [`cosmological-constant-closure.md`](../../../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md)).

> **Honest scope (consistency-vs-emergence).** A *consistency* result, not a confirmation: the null
> rules nothing in. The discriminating measurement is the E-route, where AVE and QED differ by
> $\sim10^7$ (below).

## §3 — The bold side-prediction and the real test (E-route)

> **[Resultbox]** *Bold side-prediction — NO static-B vacuum birefringence*
>
> AVE predicts **zero** static-B vacuum birefringence at **any** field strength (categorical, not a
> bound). A *static-B* birefringence detection at or above the QED level ($\sim10^{-23}$ at 5 T)
> would **FALSIFY** this AVE prediction. This is a clean discriminator once static-B sensitivity
> reaches the QED level: QED says small-but-nonzero, AVE says exactly zero.

**The real test is the E-route.** A static (or DC-biased) electric field $\mathbf E$ *does* load the
$V$-keyed varactor ($\varepsilon$-grade, regime R2), giving a measurable birefringence. The matched
differential observable (par−perp) sits a field-independent factor

$$
\frac{\delta n_{AVE}}{\delta n_{QED}} = \frac{7.5}{\alpha^3} \approx 1.93\times10^7
$$

above differenced Euler-Heisenberg — the OQ-1 discriminator
([`vacuum-birefringence-e4.md`](../../falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md),
clm-pp3qwf). A HIBEF-class facility field (approaching $E_{yield}\approx1.13\times10^{17}$ V/m via
focal enhancement) is the AVE-distinguishing experiment, **not** a high static-B magnet. The facility
landscape for the E-route test — HIBEF @ European XFEL (the only purpose-built bench), the PW-laser field
sources, and the magnetic-route facilities (PVLAS / BMV / OVAL / VMB@CERN) noted as **not** testing AVE — is
surveyed with cited tolerances in
[`research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md`](../../../../../research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md).

---
