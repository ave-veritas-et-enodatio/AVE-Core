### ENTRY 2026-08-03-rulings-mr-batch (2026-08-03): implementer — Grant rulings 1 / 3 / 5 / 6 executed (K=2G register, PRODUCT declaration, incompressible repair, neon demote)

- **Class: ruling execution, not adjudication.** Four Grant rulings fired 2026-08-03, **verbatim `[sic]`, as one message**:

  > ***"1. Agree, and I think we should at some point find it's a forced form … 3. follow your rec, there's always a cost when transferring energy between regimes/states/channels right? seems like a theorem or law territory … 5. repair 6. demote"***

  One commit per ruling (four), plus this fragment. **Mints ZERO ids** (INVARIANT-S11) — no `clm-`/`def-`/`exp-`/`sup-`/`ilk-` minted, retired or re-pointed. **No `confidence` / `quality` / `solidity` / `build_status` / `status` field moves anywhere.** `.index/` and `src/` **byte-untouched** (no file from either tree appears in the diff).
- **Two-method verification of every site BEFORE editing** (no line number trusted from the dispatch): each target was located by **content** (`grep -rn` on a quoted string from the sentence itself) and independently by **`git grep`**, and the two methods were required to return the same set. Two dispatch line-cites were off and are corrected in the receipts below.

---

## RULING 1 — `K = 2G` register (agree; plus the routed "forced form" aspiration)

**Ruling `[sic]`: *"1. Agree, and I think we should at some point find it's a forced form"*.** Commit **`7a6f4ba6`**. Two files: [`manuscript/ave-kb/common/interlock-register.md`](../../manuscript/ave-kb/common/interlock-register.md) (the machine home) and [`manuscript/ave-kb/common/form-deriving-value-importing.md`](../../manuscript/ave-kb/common/form-deriving-value-importing.md) (the prose home). Both carry the count; both were checked, and **neither needed a count edit** — see below.

### The tagging half (what the ruling settles)

- **`expected-independent-count:` STAYS 3, byte-untouched.** Verified before editing: `interlock-register.md:12` reads `expected-independent-count: 3` and `:11` reads `calibration-params: clm-0ktpcn clm-5xon03 clm-dsb560`. `form-deriving-value-importing.md:68-70` carries the same set in prose (*"a marked **calibration set of 3 dimensionful constants** `{m_e, α, G}`"*). **`K = 2G` was never in either set** — the ruling's job is to say *why it must not be added*, not to remove it.
- **The ruled sentence, landed at both sites:** `K = 2G` is **NOT an independent calibration input**; it is a **separately-tagged constitutive-FORM import edge** — the GR **trace-reversal lock**, GR-IMPORTED per PR [#261](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/261) (MERGED; both provenance gates pass — *not* crystalline-forced, *not* constitutively-forced) — **distinct from G's value import**.
- **Why the edge classes are genuinely different (the load-bearing distinction).** What `K = 2G` imports is a **relation between two moduli** — a constitutive **FORM**. What G imports is a **VALUE**: the dimensionless Machian termination `ξ ≈ 8.15×10⁴³`, back-solved `ξ = ℏc/(7 G m_e²)` from CODATA G (`ilk-gravmb` grounding; `constants.py:589` `XI_MACHIAN`). Two different objects, two different edges. **Two distinct import edges; one count of 3.**
- **Mechanically why the count is untouched:** `K = 2G` mints no `ilk-` node, adds no `interlocks` edge, and moves no `real_or_fitted` tag. The count is computed **only** from the `ilk-` `real_or_fitted` tags (`compute_independent_parameter_count`, per `interlock-register.md:267`), so a note that mints nothing cannot move it. This is the same *mints-nothing / touches-nothing* shape the register already uses for the Calibration-Constant Criteria view (`:94-100`) and the yield consumer-map (`:102-117`) — the note was placed adjacent to those two, deliberately, so the pattern reads as one.
- **Two explicit prohibitions written into the register:** (i) do **not** book `K = 2G` as a fourth calibration parameter — it is not a dimensionful constant the substrate is fed; (ii) do **not** fold it into G's row — that would collapse a FORM import into a VALUE import and mis-state `ilk-gravmb`'s `mixed` grounding, which the leaf's own *"Accuracy is load-bearing"* banner (`form-deriving-value-importing.md:77-81`) already guards (*"**G is `mixed`, NEVER a pure echo**"*).

### The routed half — OPEN RESEARCH ITEM, recorded not attempted

- **Grant's aspiration, same sentence `[sic]`: *"I think we should at some point find it's a forced form"*.** Recorded as an **OPEN research item** at both sites. **Routed, NOT attempted** — no derivation is asserted, sketched, or graded anywhere in this branch.
- **Why it is the FORM-deriving pattern's completion for this row.** The meta-finding is *AVE forces FORMS, imports VALUES* — and `K = 2G` is **the one row where even the FORM is imported** (`form-deriving-value-importing.md:87`, the row's own "What is the chord (FORM)" cell claims only *"the substrate forces the form of the elastic response `K/G = f(ρ)`"*, i.e. the functional shape, while the **lock** `K = 2G` itself is the import). Forcing it would move the row from *import-of-a-form* to *derivation-of-a-form* — **a strictly different move from flipping a VALUE** (α `fitted→real`; G via Chain B′), and it is why this row is the pattern's completion rather than another instance of it.
- **The named attack point, cited rather than invented.** PR #261's record leaves **exactly one** open physics item. [`program-arc-map.md:118`](../../manuscript/ave-kb/common/program-arc-map.md), verified verbatim at that line: ***"*Closed:* K=2G-as-derived. *Opened:* eigenmode-existence as the only remaining open physics."*** The corresponding un-fired test is `clm-satnec`'s **static-existence test** ([`saturation-rim-inversion.md:55`](../../manuscript/ave-kb/common/saturation-rim-inversion.md): impose the `(2,3)` winding as a boundary condition, relax the lattice, ask whether the relaxed core rails `S → 0`), which the vocabulary register **already** names *"the K=2G eigenmode-existence open item"* ([`vocabulary-register.md:1119`](../../manuscript/ave-kb/common/vocabulary-register.md)). All three cites read and confirmed at this tip.
- **Scope guard, written into both leaves so the item cannot be over-read.** Forcing `K = 2G` **moves no calibration count by itself** — it flips no `real_or_fitted` tag. What it *would* do: (i) remove the GR-import that **Chain B′ currently routes through**, and (ii) lift the **Axiom-4 yield-anchor** row's inherited import (`arc* = 4ρ/(4ρ+1)·ℓ_node` with `ρ = 2 ⟺ K = 2G`, `form-deriving-value-importing.md:88`).
- **★ The one closed route is named so this is not read as re-opening a refutation.** The 2026-07-02 elastic-moduli arc (PRs [#459](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/459)/[#460](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/460)) tested exactly this and **could not** force it: `z=4` fixes only the form `K/G = f(ρ)`, `ρ` inherits from the imported value, and inextensibility (`ρ≫1`) is affirmatively `K=2G`-**forbidden** (`interlock-register.md:224`). That is a **standing negative on one named path**. Both leaves carry the corpus's own **closed ≠ exhausted** (Grant-ratified) qualifier from that same entry, so the aspiration is **live**, not a re-opened refutation.

## RULING 3 — GW-memory + BH-info, bundled PRODUCT declaration

**Ruling `[sic]`: *"3. follow your rec, there's always a cost when transferring energy between regimes/states/channels right? seems like a theorem or law territory"*.** Commit **`77d1c57e`** (KB half only). **KB-FIRST discipline: the `.tex` site rides the held ringdown wave, so the ruling is RECORDED now and the tex edit is STAGED, not fired.**

### (a) LANDED — the BH-information FLAG's declaration half

- **Site content-located, not line-trusted.** [`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md`](../../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md) — the 🔴 FLAG block is at **`:24-26`** at `origin/main` exactly as the dispatch stated (located by the string *"recorded + routed, NOT adjudicated"*; **dispatch cite VERIFIED, not corrected**).
- **THE DECLARATION: PRODUCT.** The retained quantity the FLAG names — the **linking-number invariant** of the knot / the **no-hair $M$–$Q$–$J$** exterior — is declared a **lossless latched residual**, under the discipline at `common/retention-transition-split.md:51` (read verbatim at that line: *"Any load-bearing use of **remanence / irreversible / plastic / latch / dissipates / frozen / erased** must declare WHICH moment it refers to: PRODUCT (product-persistence) or TRANSITION (transition-arrow)."*). **No maintenance resistor** — `:15` (*"Under canon this is **LOSSLESS** and needs **no maintenance resistor**"*) and the PRODUCT row of the regime table at `:57` (`requires_R` = **no**, licensed source *"topology (winding integer) or the `$\Gamma=-1$` reactive wall"*). Consistency-class read, never an emergence chord.
- **The consequence recorded for the body's two undeclared TRANSITION-register clauses** — `:17` *"permanently **erased**"* and `:20` *"enforcing **information loss**"*. Each must **either (a)** be re-scoped to the PRODUCT reading (a lossless latch is not an erasure), **or (b)** carry a **counting-sourced** TRANSITION arrow — mode-spread with reconvergence ≈ 0, or the energy-conserving click (`:33-34`) — and **never a valve**. Tier-1 canon quoted and independently verified at its own line: `research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md:256` reads *"the arrow comes from mode-count or a click, never a valve"*.
- **★ Arm (b) is explicitly recorded as AVAILABLE, not foreclosed — this is the part a careless read would get backwards.** **Regime-IV rupture is one of the corpus's three RULED genuine loss channels** (`common/substrate-native-terminology.md:33`, verified verbatim: *"the corpus's genuine **loss/irreversibility channels reduce from four to THREE**: (1) radiative port, (2) boundary-Joule extraction, (3) Regime-IV rupture"*), and the BH interior **is** Regime IV (`vol3/claim-quality.md:121`). So the leaf is *permitted* to keep an arrow. What the ruling forbids is taking it **for free**: keep *"erased"* and you owe the **counting** source, not a friction.
- **What the ruling does NOT do, stated on the leaf:** the **unitarity question itself stays OPEN**. The declaration **constrains the FORM** any answer may take; it picks no answer. Retention and destruction both stay live; what is foreclosed is a **third** option — sourcing the destruction from a valve / maintenance resistor. The FLAG's **F5 routing** to the generative-cosmology / BH-interior lane (`research/2026-07-17_regime-iv-dissipation-audit.md:127`) **STANDS**.
- **Rule 12:** both FLAG paragraphs are preserved **byte-unedited**; the resolution is a dated additive block beneath them. No body prose above the FLAG is touched. `clm-ir8h78` and `clm-c6k5om` untouched — no re-grade, no retraction.

### (b) STAGED, NOT FIRED — the GW-memory site (fires with the gated ch15 wave)

- **Site + status.** `manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex`, §*"Gravitational Wave Memory as Residual Strain"*. Content-located: the ruled sentence is at **`:322`** at `origin/main` — **dispatch cite VERIFIED**. **HELD.** Nothing in this branch touches that file (`git diff --name-only origin/main...HEAD` does not contain it — confirmed in the battery below).
- **The site's current text, verbatim at `:322` and `:328`:**

  > After a gravitational wave passes, the local metric retains a permanent offset---so-called ``memory'' or residual strain. In the AVE dielectric framework, this is the \textbf{permanent plastic deformation} of the LC lattice after being driven past its linear elastic limit by the passing wave. The residual memory strain scales as:
  >
  > […equation…]
  >
  > This is directly analogous to a metal permanently deforming after exceeding its yield stress $\sigma_Y$. The dimensionless yield strain of the vacuum lattice $h_{yield} = \sqrt{\alpha}$ emerges from the same Axiom 4 saturation physics that defines $V_{yield}$.

- **TWO INDEPENDENT DEFECTS, both ruled, both staged.**
  1. **The which-moment defect (PRODUCT).** *"permanent **plastic** deformation"* — `plastic` is on `retention-transition-split.md:11`'s own declaration-required word list, used here with **no declaration**, and in its dissipative sense (metal plasticity) it is an **Ax3 loss leak**. Ruled wording: **retained residual offset / latched strain; "plastic" struck.**
  2. **The regime-broken premise (independent of #1).** *"after being **driven past its linear elastic limit**"* is **false by ~28 decades**. Verified numerically against the corpus's own numbers: `vol3/gravity/ch08-gravitational-waves/ligo-gw-saturation-ratio.md:15` gives $V_{GW}/V_{\text{snap}} \approx \mathbf{1.4\times10^{-28}}$, and `vol3/claim-quality.md:76` reads *"All observed GW signals are **far in Regime I** (deeply linear)"* with the per-class table at `einstein-field-equation.md:92-95` (GW150914 $\sim10^{-28}$, GW170817 $\sim10^{-29}$, pulsar timing $\sim10^{-22}$; **all Regime I**). Nothing observed is anywhere near yield.

- **★ THE EQUATION SURVIVES THE PREMISE STRIKE — and this is why the strike is a repair, not a deletion.** $\Delta h_{memory} = h_{peak}(h_{peak}/h_{yield})^2$ is exactly the shape of the **leading cubic nonlinear correction of the Axiom-4 kernel expanded about zero** ($\sqrt{1-x^2} \approx 1 - x^2/2$, first correction $O(x^2)$ on a linear response). That is a **Regime-I sub-yield** statement, fully consistent with $V_{GW}/V_{snap} \sim 10^{-28}$. It is **only the post-yield plasticity narrative** that dies, not the scaling law. The staged text keeps the equation byte-unchanged.

- **★ STAGED FLAG (surfaced here, NOT written as a strike) — the word "permanent" is not yet earned by the engine.** A *retained* offset after the drive passes is a **remanence**, and the corpus's own engine map says the canonical kernel cannot produce one: [`common/engine-capability-map.md:67`](../../manuscript/ave-kb/common/engine-capability-map.md), verified verbatim — *"The canonical kernel $S(A)=\sqrt{1-A^2}$ is **anhysteretic** — zero enclosed loop area ⇒ **no remanence**. Every attempt to get retention imposes a latch by hand (the [#215] IMPOSED-LATCH). The loop is the deepest open gap (**R10**)."* So the PRODUCT declaration says *what kind of object this is if it exists* (a lossless latched residual); **whether the substrate has a non-imposed latch to hold it is the OPEN R10 gap.** This is flagged for the ch15 lane, **not** resolved here, and **not** used to strike the section.

- **THE STAGED EDIT TEXT, VERBATIM (to fire with the gated ch15 wave, not now):**

```latex
After a gravitational wave passes, the local metric retains an offset---so-called
``memory'' or residual strain. In the AVE dielectric framework this is read as a
\textbf{retained residual offset}: a \emph{latched} strain state of the LC lattice
that survives with the drive off. Declared per the corpus's PRODUCT/TRANSITION
discipline (\kbleaf{ave-kb/common/retention-transition-split.md}) this is the
\textbf{PRODUCT} moment---persistence of a latched state---which under canon is
\textbf{lossless} and carries \textbf{no maintenance resistor}. The residual memory
strain scales as:
```

```latex
The scaling is a \textbf{sub-yield} statement, not a post-yield one: the cubic form
$h_{peak}(h_{peak}/h_{yield})^2$ is the leading nonlinear correction of the Axiom~4
kernel expanded about zero ($\sqrt{1-x^2} \approx 1 - x^2/2$), which is exactly what
the deeply-linear regime supplies. The dimensionless yield strain $h_{yield} =
\sqrt{\alpha}$ enters as the \emph{normalising} scale of that expansion, from the
same Axiom~4 saturation physics that defines $V_{yield}$.

\noindent\textbf{Regime note (2026-08-03).} Two earlier framings of this section are
struck. (i) The lattice is \textbf{not} ``driven past its linear elastic limit'' by an
observed gravitational wave: LIGO-class signals sit at $V_{GW}/V_{snap} \approx
1.4 \times 10^{-28}$ (\kbleaf{ave-kb/vol3/gravity/ch08-gravitational-waves/ligo-gw-saturation-ratio.md}),
about \textbf{28 decades} below saturation, and every observed source is classified
\textbf{Regime~I, deeply linear} (\kbleaf{ave-kb/vol3/gravity/ch02-general-relativity/einstein-field-equation.md},
regime table). (ii) The metal-plasticity analogy---``permanently deforming after
exceeding its yield stress $\sigma_Y$''---is therefore struck as well, and with it the
word \emph{plastic}: rate-independent plastic loss is a dissipation channel the
lossless substrate (Axiom~3) does not have, and none of the three ruled loss channels
is active here. What remains is a \emph{reactive} latched residual, which is a
statement about a retained state, not about a loss.

\noindent\textbf{Open, flagged not resolved.} Whether the substrate supplies a genuine
(non-imposed) latch to hold such a residual is the standing \textbf{R10 remanence gap}:
the canonical kernel $S(A) = \sqrt{1-A^2}$ is anhysteretic---zero enclosed loop area,
hence no remanence---and every retention obtained so far has been an imposed latch
(\kbleaf{ave-kb/common/engine-capability-map.md}, \S3.3). Until R10 closes, the word
``permanent'' in this section is a description of the \emph{observable} being modelled,
not a property the engine has been shown to produce.
```

  Companion sites in the same staged set, **flagged**: the figure caption at `15_black_hole_orbital_resonance.tex:337` panel (5) reads *"GW memory strain as residual lattice deformation **above** $h_{yield} = \sqrt{\alpha}$"* — same regime-broken premise, wants *"normalised by"* rather than *"above"*. **Disclosed as slightly beyond the dispatch's letter** (which named `:322`): striking the premise at `:322` while leaving the identical premise in the caption and in the `:328` analogy would ship an internally inconsistent section. All three are staged together and **none is fired here**.

### (c) CANONIZATION-CANDIDATE — Grant's theorem instinct (routed for a walk, NOT canonized)

- **Grant, verbatim `[sic]`: *"there's always a cost when transferring energy between regimes/states/channels right? seems like a theorem or law territory"*.**
- **The candidate statement, as this lane would put it for the walk** — *proposed wording only, nothing canonized, no `def-`/`clm-` minted:*
  > **Within-channel reactive exchange is free** (Axiom 3: a lossless substrate moves energy between $L$- and $C$-storage at zero cost, indefinitely). **An ARROW appears iff the transfer crosses a COUNTING boundary** — a mode-spread with reconvergence ≈ 0, or a click. The cost is not paid to a resistor; it is paid in **countability**.
- **Why this shape and not "there is always a cost".** The literal reading would be **false in AVE and would break Axiom 3**: an ideal LC tank transfers 100% of its energy between the electric and magnetic channels every quarter cycle at zero cost, forever — that is the electron's own persistence argument (`retention-transition-split.md:25`, $Q\to\infty$). So the theorem cannot be *"transfer costs"*; it must be *"**crossing a counting boundary** costs"*. This is the **retention-transition-split's own mechanism, generalized** from the yield crossing to any regime/state/channel crossing.
- **The three ruled loss channels would be its instances** (`substrate-native-terminology.md:33`): **(1) radiative port** — energy leaves into a continuum of external modes with no return path (mode-spread); **(2) boundary-Joule extraction** — a real port at the boundary, a genuine $\mathrm{Re}(Z)$, i.e. counting done by the *detector*; **(3) Regime-IV rupture** — the lattice's mode inventory itself changes (the topological canvas is destroyed), which is the sharpest counting boundary in the corpus. **Op3 would be the negative control**: mode-loss without system-loss, RULED lossless transduction (RULING 21) — a channel crossing that does **not** cross a counting boundary and correspondingly has **no** arrow.
- **Status: CANONIZATION-CANDIDATE, routed for a Grant walk. NOT canonized here, NOT minted, NOT load-bearing for the (a) declaration.** Recorded because the ruling sentence carried it, and because a generalization at law/theorem level should get the walk-the-picture-first treatment rather than being landed inside a ruling-execution branch.
- **What the walk would need to settle (the open edges this lane will not decide):** (i) is *"crosses a counting boundary"* a **definition** of the arrow or a **claim** about when arrows occur — i.e. is it a tautology or a theorem; (ii) does the near-yield fork (still **OPEN**, `retention-transition-split.md:61-67`, Grant leans reversible) sit inside or outside its scope; (iii) whether it says anything the split leaf does not already say, or is a re-statement at a higher altitude — the honest null outcome.

## RULING 5 — the incompressible premise (repair)

**Ruling `[sic]`: *"5. repair"*.** Commit **`2d390e99`**. Two files, an exact print/KB mirror pair: `manuscript/vol_2_subatomic/chapters/05_electroweak_gauge_theory.tex` **`:35`** (dispatch cite **VERIFIED**) and its byte-identical KB mirror [`manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md`](../../manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md)**`:34`**.

### BEFORE (verbatim, both sites, modulo `\textbf{}` ↔ `**`)

> Because the vacuum substrate is incompressible ($K = 2G$), an irrotational flow field generates no localised compression ($-\partial_t \mathbf{A}$), no transverse vorticity ($\nabla \times \mathbf{A}$), and no topological defects. It is isomorphic to performing a **Galilean or Lorentz coordinate boost** of the observer's reference frame. Gauge invariance is not violated; it is revealed to be the classical network-dynamic freedom to shift the irrotational background coordinate velocity without altering the physical transverse observables.

### The premise is false — recomputed here, not restated from the corpus

- Isotropic relation $\nu = \dfrac{3K - 2G}{2(3K + G)}$. At $K = 2G$: $\nu = \dfrac{6G - 2G}{2(6G + G)} = \dfrac{4G}{14G} = \mathbf{2/7} = 0.2857\ldots$ — matching the corpus's $\nu_{\text{Hill}} = 2/7$ (the $\nu_{\text{Hill}} \equiv 2/7$ substitution later in the same section, `05_electroweak_gauge_theory.tex:75` at this tip; `common/appendix-derived-numerology.md:22`).
- $\nu \to 1/2$ requires $3K - 2G \to 3K + G$, i.e. $G \to 0$ at finite $K$, or $K \to \infty$ at finite $G$. **No finite $K$ with finite $G$ is incompressible.** So *"the vacuum substrate is incompressible ($K = 2G$)"* is not a rounding or a loose phrase — it is the **opposite** of what $K = 2G$ says. `K = 2G` is a *finite-modulus lock*, and the corpus knows it (`vol3/gravity/ch01-gravity-yield/trace-reversal-mechanism.md:21` puts $\nu = 1/2$ at the **rigidity threshold** $p_G = 0.117$, a **different** operating point from $p^* = 8\pi\alpha = 0.1834$ where $K/G = 2$).

### ★ The premise was LOAD-BEARING, not decorative — which is why this is a repair, not a word-swap

For general $\Lambda$, $\nabla\cdot(\nabla\Lambda) = \nabla^2\Lambda \neq 0$. So the clause *"generates no localised compression"* **does not follow from Helmholtz alone** — incompressibility was exactly the premise being asked to kill it. Removing the premise therefore **removes that leg of the conclusion**. The repair drops the compression leg rather than rescuing it, and keeps only what the gauge argument actually needs.

### AFTER (the ruled replacement, landed at both sites)

> The Helmholtz decomposition is exact at *any* compressibility, and that is all this argument needs: adding $\nabla\Lambda$ changes only the irrotational component, and **the irrotational component sources no transverse observable**. The curl identity $\nabla \times \nabla\Lambda \equiv 0$ leaves the transverse vorticity $\nabla \times \mathbf{A}$ pointwise unchanged, and the loop integral $\oint \nabla\Lambda \cdot d\boldsymbol{\ell} = 0$ around any closed contour (single-valued $\Lambda$) leaves every winding and linking integer unchanged — so no topological defect is created or destroyed. It is isomorphic to performing a **Galilean or Lorentz coordinate boost** … *(tail unchanged)*.

### Chain check — the repaired argument read end to end (the ruling asked for this explicitly)

1. **Critique:** a gauge shift on a *physical* $\mathbf{A}$ would spontaneously move macroscopic mass, violating Noether. *(unchanged, `:31`/`:30`)*
2. **Helmholtz:** $\nabla\Lambda$ is purely irrotational, so it enters only the longitudinal channel. **Exact at any $\nu$ — no premise spent.**
3. **Transverse observables:** built from the solenoidal channel ($\mathbf{B} = \nabla\times\mathbf{A}$); $\nabla\times\nabla\Lambda \equiv 0$ ⇒ **pointwise unchanged.**
3′. **The electric field** (added 2026-08-03, review finding 3): $\delta\mathbf{E} = -\partial_t\nabla\Lambda$ is **not** pointwise zero — but it **is** irrotational, so the whole of it sits in the EM longitudinal channel, which by `def-l0ngdu` has **no restoring force**. A channel with no restoring force **stores no energy and exerts no force** ⇒ **no observable of any kind**, $-\partial_t\nabla\Lambda$ included.
4. **Topological content:** loop/surface integrals of the solenoidal channel; $\oint\nabla\Lambda\cdot d\boldsymbol{\ell} = 0$ for single-valued $\Lambda$ ⇒ **no defect created or destroyed.**
5. **Conclusion:** the shift is a coordinate re-labelling of the irrotational background — the boost reading — so the critique is answered.
**No step uses compressibility**, and with (3′) in place **every** observable named in the critique ($\mathbf{B}$ *and* $\mathbf{E}$) is covered.

> **🔴 CORRECTION 2026-08-03 (review finding 3; the sentence above is the repaired form, the prior one is preserved here per Rule 12).** This chain check originally ended ***"No step uses compressibility. The chain reads soundly."*** with steps (1)–(5) and **no (3′)** — i.e. it **asserted soundness while covering $\mathbf{B}$ only**. That was wrong as written. **Why the gap existed:** the clause this ruling struck was the section's *only* $\mathbf{E}$ coverage, and it was **garbled** — it called $-\partial_t\mathbf{A}$ *"localised compression"* when $-\partial_t\mathbf{A}$ **is** the electric field. Striking it removed the $\mathbf{E}$ leg outright, and $\delta\mathbf{E} = -\partial_t\nabla\Lambda \neq 0$ **pointwise**. The textbook cancellation is **unavailable in this section's variables** — there is no scalar-potential companion here to absorb $\varphi \to \varphi - \partial_t\Lambda$. **The one-step fix, landed at both sites:** promote `def-l0ngdu`'s no-restoring-force clause (`vocabulary-register.md:870`, verified verbatim at that line: *"The **EM longitudinal** $\nabla\cdot\mathbf{A}$ is **GAUGE**: the curl-only EM Lagrangian gives it no restoring force."*) from **grounding-decoration to a step of the chain**. Landed in the print body + source comment (`05_electroweak_gauge_theory.tex`) and in the KB mirror body + chain check + premise note (`gauge-boson-masses.md`). **Disclosed second-order edit:** the body paragraph's closing clause moved from *"without altering the physical **transverse** observables"* to *"without altering the physical observables — transverse or longitudinal"*, because leaving *transverse* as the paragraph's concluding scope would rhetorically re-narrow the very leg (3′) just closed.

### Substrate-native grounding cited (not invented)

The corpus's **adjudicated longitudinal-sector split**, `common/vocabulary-register.md:867` (`def-l0ngdu`), verified verbatim: the mechanical dilatation $\nabla\cdot\mathbf{u}$ is **DYNAMICAL** — *"it carries a genuine bulk restoring force $\tfrac12 K(\nabla\cdot\mathbf{u})^2$ ($K = 2G$) and rides the **gapless lattice-computed P-branch**"* — while the EM longitudinal $\nabla\cdot\mathbf{A}$ is **GAUGE** — *"the curl-only EM Lagrangian gives it no restoring force"* — with the tag line *"**One word each way — $\nabla\cdot\mathbf{u}$ propagates; $\nabla\cdot\mathbf{A}$ is gauge.**"* That split is the substrate-native reason the shift is unobservable **and it needs no compressibility assumption**. Note the corpus's own `def-l0ngdu` text already carries `K = 2G` **alongside** a propagating P-branch — i.e. the corpus elsewhere treats $K = 2G$ as compressible, which is what made the `:35` premise an isolated defect rather than a corpus-wide belief.

### ⚑ FLAGGED, NOT FIXED (surfaced on the KB leaf, outside this ruling's scope)

The paragraph still says $\nabla\Lambda$ is added *"to the **mass flow**"*, reading $\mathbf{A}$ as the mechanical momentum field. The corpus's SOLID adjudication is that $\mathbf{u}$ and $\mathbf{A}$ are **COUNTERPART SECTOR VARIABLES — isomorphic structure, NOT one field** (`common/vocabulary-register.md:882`, `def-uatk1s`, SOLID 2026-07-21), differing precisely in constitutive stencil on the longitudinal channel. Whether that wording needs its own correction is a **separate question, routed** — surfaced rather than absorbed into this repair.

### Two-method mirror sweep — and two sites left deliberately unedited

Method 1 `grep -rn "incompressible\|Incompressible" manuscript/`; method 2 `git grep -in "incompress" -- manuscript/ src/`. **Both returned the same set.**
- **Exactly ONE exact mirror of the ruled sentence exists** — `gauge-boson-masses.md:34` — and it is repaired here.
- **TWO sites carry a DIFFERENT sentence with the same false premise, FLAGGED not edited** (outside the ruling's named scope): `manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/cauchy-implosion-resolution.md:15` and its print mirror `manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex:164` — *"This positive bulk resistance guarantees that the spatial substrate is **incompressible** and thermodynamically stable against gravitational collapse."* Same defect (a finite $K$ is not incompressibility), different sentence, different chapter, and the *"stable against collapse"* conclusion may well survive on a finite-$K$ premise. **Routed as a follow-on; not silently swept in.**
- **NOT defects, checked and cleared so the flag is not over-broad:** the hollow-vortex *"incompressible melted-vacuum EOS floor"* sites (`vol2/claim-quality.md:1554,1557`, `hollow-vortex-binding.md:46,51-52`, `vol_2_subatomic/chapters/01_topological_matter.tex:152`) are **Regime-IV melted-state** statements about the *ruptured* medium's EOS, not cold-lattice $K = 2G$ statements. Different regime, different object, correct as written.

### Scope

**Premise-only.** Conclusion, boost reading, and every downstream result — $(m_W/m_Z)^2 = 1/(1+\nu) = 7/9$, $m_W/m_Z = \sqrt7/3$, $\sin^2\theta_W = 2/9$ — are **unchanged** (recomputed here: $1/(1+2/7) = 7/9$; $1 - 7/9 = 2/9$ ✓). `clm-5zuo7g` and `clm-q8un7j` untouched. **Rule-12 shape per Grant's standing register:** git carries the trail (struck sentence in the diff and in a source comment); the in-doc text is a compact current-status premise note, not a preservation banner — the `.tex` carries the condensed note, the KB leaf the explanation.

## RULING 6 — neon 585–703 nm (demote)

**Ruling `[sic]`: *"6. demote"*.** Commit **`1faee721`**. Two files, an exact print/KB mirror pair.

### ★ Receipt correction — the dispatch's line cite was RIGHT and the upstream fragment's was STALE

- The reconciliation fragment [`2026-08-02-mr-vol6-crosswires`](2026-08-02-mr-vol6-crosswires.md) item **(b)** and the board row it came from (`_orchestration/2026-08-02_manuscript-reconciliation-board.md:509`) both cite the print at **`12_neon.tex:48`**. At `origin/main` the sentence is at **`12_neon.tex:65`**. **The print moved `:48 → :65`; content unchanged.**
- **Two-method located** (`grep -rn "585" manuscript/` intersected with neon context; `git grep`): both methods returned **exactly the same two sites** — `manuscript/vol_6_periodic_table/chapters/12_neon.tex:65` and `manuscript/ave-kb/vol6/period-2/neon/topological-area.md:12`. **No third site anywhere in the corpus.** The correction is recorded on the KB leaf itself, not only here.

### BEFORE (verbatim, both sites)

> When subjected to an external electric field (as in a neon discharge tube), the high-$Q$ internal resonance stores the injected energy with extreme efficiency, then re-radiates it as narrow-band photon solitons at the characteristic $585$--$703$ nm wavelengths. The famous orange-red glow of neon signage is a direct emission signature of the Triangular Bipyramid's resonant frequency response: the photon energies correspond precisely to the standing-wave modes of the $81d$ inter-alpha cavity.

**Two register violations:** *"**characteristic** … wavelengths"* presents **observed** lines as an **output**; *"correspond **precisely**"* asserts a **computed quantitative match**. **Neither is computed** — there is no calculation anywhere in the corpus taking the $81d$ inter-alpha cavity to $585$–$703$ nm (checked: `git grep` for the band endpoints over `src/` and `research/` returns **no** driver, result-doc or JSON that computes a wavelength for this cavity — the only `585`/`703` hits in those trees are unrelated numerals).

### AFTER (demoted to the structural/interpretive register, both sites)

> When subjected to an external electric field (as in a neon discharge tube), the high-$Q$ internal resonance stores the injected energy efficiently and re-radiates it as narrow-band, rather than broadband, emission. Neon's *observed* discharge spectrum — the familiar orange-red signage glow — lies in the $585$--$703$ nm band; those wavelengths are quoted here as **measured values the picture is describing, not as an output of it**. What this leaf offers is a **structural mapping**: a closed, high-$Q$, zero-net-dipole Triangular Bipyramid is the kind of resonator whose response is narrow-band, and the discharge emission is read as that resonant response. **No line position is predicted** — the standing-wave modes of the $81d$ inter-alpha cavity are not computed against the observed lines anywhere in this framework. Read the correspondence as interpretive, not quantitative.

### The governing claim card, as ruled

`manuscript/ave-kb/vol6/claim-quality.md:662` (`clm-y7uvdc`), verified verbatim at that line: *"**Does NOT claim** a quantitative reproduction of multi-electron ionization energies, fine-structure splittings, or **spectroscopic line positions** from the soliton-packing picture alone."* A leaf may not assert what its governing register non-claims; the register wins and the print is demoted to match. **Nothing is retracted at the claim level** — the demote brings the prose *into* the band the card already declared.

### ★ CARD-SCOPE OBSERVATION — surfaced, not resolved (the dispatch's cite corrects the board's, and the gap is real)

- The board row and fragment (b) cite **`clm-f8k2um`** at `vol6/claim-quality.md:566`. That card **is** this leaf's governing claim by frontmatter (`topological-area.md` frontmatter: `claims: [clm-f8k2um]`), and its **solidity is 0.30** (*"do not build on, rework needed"*) — **dispatch cite VERIFIED**.
- **But its non-claim list at `:566` does not name spectra**: *"Does NOT claim quantitative predictions of **bond enthalpies, electronegativity scales** (Pauling / Mulliken), **reaction kinetics, or material constants** from the topology alone."* The **spectroscopic** non-claim lives on the **sibling** card `clm-y7uvdc` (the *Orbital Knot Topology* leaves), which is the card the ruling names — **correctly**, because it is the only one that actually non-claims line positions.
- **Both cards point the same way**, so the demote is not in doubt. **But the "Topological Area" card carrying no spectral non-claim is the actual gap the sweep exposed** — a per-element leaf under `clm-f8k2um` can currently assert spectra without contradicting its own card. **Flagged for the auditor lane. NO card is edited here** — no re-grade, no non-claim added, no solidity move, no `strengthen-by` touched.

### Scope

**Prose register only.** The $81d$ Triangular-Bipyramid geometry, the inertness account in the preceding paragraph, the $R = 81.181d$ figure caption, and every number elsewhere in either file are **unchanged**. Rule-12 shape as in Ruling 5: git carries the trail (struck text in the diff and in a source comment); the KB leaf carries the explanation, the `.tex` a condensed comment.

## Battery (re-run at the branch tip, all four rulings in)

- **`make verify` exit 0** — run after **each** ruling's edits, not once at the end (4 runs + a final tip run). Final: `[Verify] ALL PHYSICS PROTOCOLS PASSED.`
- **`make verify-md-links` gating 0** — `gating errors: 0  warn-only: 207  broken inter: 42` (inter-repo mode: warn; both numbers unchanged from `origin/main`, so this branch introduces no new warn either). **`kbleaf` cites: 1211 → 1213, gating 0** — the two new `\kbleaf{}`/leaf cites this branch adds (Ruling 5's `ave-kb/common/vocabulary-register.md`, Ruling 6's `ave-kb/vol6/claim-quality.md`) both **resolve**.
- **`make refresh-kb-metadata` idempotent** — two consecutive runs, 0 files written, clean tree after. **`.index/` byte-unchanged** (no `clm-`/`def-`/`ilk-` node body, frontmatter `claims:`/`no-claim:`, quality block or `strengthen-by` item was touched anywhere in the diff).
- **`verify-docket-keys`** — **118 entries / 116 unique keys** (117/115 before this fragment, so the one key this branch mints is unique), **no new duplicate keys**; grandfathered numeric dups `22`/`32` unchanged. This branch mints **one** key: `2026-08-03-rulings-mr-batch`. Cross-checked against the **five** sibling branches that also write into `_orchestration/docket-entries/` — all different slugs (`2026-08-03-mr-handoff-mechanical`, `2026-08-03-mr-fragment-cite-repins-correction`, `2026-08-03-petermann-amendments`, `2026-08-03-wall-taxonomy`, `2026-08-03-coldq-v2p2-root`, `2026-08-03-coldq-v2p4-root`). **No collision.**
- **Pure-corpus scan** over the full branch diff **plus** this fragment: **0 hits** (two methods: case-insensitive `grep -E` over `git diff origin/main...HEAD` piped with the fragment, and an independent Python scan of the same text).
- **Zero id churn** — no `clm-`/`def-`/`exp-`/`sup-`/`ilk-` minted, retired or re-pointed; **no `confidence` / `derivation_solidity` / `solidity` / `build_status` / `status` / `real_or_fitted` field moves anywhere**; `expected-independent-count: 3` byte-unchanged; **`src/` byte-untouched** (no `src/` path appears in `git diff --name-only`).

### Branch overlap — ZERO file overlap with every live sibling lane

Verified by intersecting `git diff --name-only origin/main...<branch>` per lane after a fresh `git fetch origin --prune`, **enumerated rather than taken from the dispatch** (the dispatch named one lane; a full enumeration found **eleven** branches ahead of `origin/main`). All tips read at the time of this receipt:

| lane | tip | files | common with this branch |
|---|---|---|---|
| `docs/mr-handoff-mechanical-0803` | `ae96ce22` | 20 | **0** |
| `docs/mr-addenda-0803` | `6d5e0ddc` | 10 | **0** |
| `docs/mr-board-corrections-0803` | `eb914bd1` | 1 | **0** |
| `docs/mr-epic-closeout` | `745b5951` | 1 | **0** |
| `kb/petermann-artifact-record` | `b8f757b9` | 7 | **0** |
| `kb/wall-taxonomy` | `2a00df1a` | 3 | **0** |
| `research/coldq-pole-v2p2` | `53144b5c` | 7 | **0** |
| `research/coldq-pole-v2p3` | `c65c3d7d` | 8 | **0** |
| `analysis/2026-06-06-open-short-relabel` | `cc63c420` | 2 | **0** |
| `analysis/moving-front-freezein` | `f647f58b` | 5 | **0** |
| `analysis/stage4-a1-eos-scope` | `205d6e6b` | 1 | **0** |

- **★ The named collision lane checked explicitly, file by file.** `docs/mr-handoff-mechanical-0803` owns the mechanical batch (k_HB, Li/B, ρ_bulk, Si-28 comment, varactor, boron, magnesium). Its **Vol-6 print** files are `02_chemistry.tex`, `07_boron.tex`, `14_magnesium.tex` — **not** `12_neon.tex`. Its **Vol-6 KB** file is `vol6/framework/chemistry-translation/quantum-vs-topological-shells.md` — **not** `vol6/period-2/neon/topological-area.md`. Its **Vol-2** file is `vol2/appendices/app-c-derivations/index.md` — **not** `vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md`, and it touches no `vol_2_subatomic/chapters/*.tex`. It writes **two** docket fragments, both under different slugs. **Confirmed disjoint at its live tip `ae96ce22`** (it was `0 commits ahead` with only working-tree modifications when this lane started and has since pushed 8 commits — **re-read at the new tip rather than carrying the stale receipt**).
- **★ What zero FILE overlap does not cover.** Ruling 5 flags `manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex:164` + `cauchy-implosion-resolution.md:15` as carrying the same false premise in a different sentence; Ruling 3's GW-memory edit is staged against `manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex`. **None of those three files is edited by this branch**, but any lane that opens the Vol-3 print should read this fragment first.

### This branch's files (8)

`_orchestration/docket-entries/2026-08-03-rulings-mr-batch.md` · `manuscript/ave-kb/common/interlock-register.md` · `manuscript/ave-kb/common/form-deriving-value-importing.md` · `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md` · `manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md` · `manuscript/vol_2_subatomic/chapters/05_electroweak_gauge_theory.tex` · `manuscript/ave-kb/vol6/period-2/neon/topological-area.md` · `manuscript/vol_6_periodic_table/chapters/12_neon.tex`

### Routed follow-ons opened by this branch (none taken here)

1. **Derive `K = 2G` as substrate-forced** — Grant's routed aspiration; attack point = the eigenmode-existence open item (`program-arc-map.md:118` / `clm-satnec`). *(Ruling 1)*
2. **Canonization walk** — Grant's *"cost when transferring energy between regimes/states/channels"* theorem instinct; candidate wording, the three ruled loss channels as instances, and the three open edges are drafted in §Ruling 3(c). **Routed for a Grant walk, NOT canonized.** *(Ruling 3)*
3. **Fire the staged ch15 GW-memory edit** with the gated ringdown wave — text verbatim in §Ruling 3(b), including the `:328` analogy strike and the `:337` panel-(5) caption, and the R10-remanence flag on the word *"permanent"*. *(Ruling 3)*
4. **The `incompressible` premise at two Vol-3 sites** (`cauchy-implosion-resolution.md:15`, `03_macroscopic_relativity.tex:164`) — same false premise, different sentence, outside Ruling 5's named scope. *(Ruling 5)*
5. **The `"mass flow"` wording** at the repaired Vol-2 paragraph vs `def-uatk1s`'s counterpart-sector-variables adjudication. *(Ruling 5)*
6. **`clm-f8k2um` carries no spectral non-claim** while governing leaves that describe spectra — auditor-lane card-scope question. *(Ruling 6)*
7. **Upstream receipt staleness** — the board row and fragment (b) cite `12_neon.tex:48`; the print is at `:65`. Owned by whichever lane next opens the board. *(Ruling 6)*
