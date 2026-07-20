[↑ Ch.6 Universal Operators](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-j550uh, clm-9kd2t3]
path-stable: "referenced from photon-identification + L3 closure synthesis as canonical K4 4-port irrep decomposition"
-->

# K4 4-Port Irrep Decomposition: $A_1 \oplus T_2$ + S-Matrix Eigenvalues

The K4 4-port amplitude space decomposes under the tetrahedral group $T_d$ as $V_{\text{4-port}} = A_1 \oplus T_2$. The K4-TLM scattering matrix $S = (1/2)\mathbf{1} - I$ has eigenvalues $\{+1, -1, -1, -1\}$: the $+1$ eigenvector is the $A_1$ "common mode" (all ports equal); the $-1$ triplet spans $T_2$ (traceless). **This is the canonical group-theoretic foundation** for: photon identification ($T_2$-only Cosserat $\omega$ microrotation), photon-electron formation mechanism ($A_1$ dissipates via Gauss's law forbidding longitudinal EM; $T_2$ survives), $A_1$ vs $T_2$ propagation-speed split ($c\sqrt{2}$ vs $c$), and Cosserat sector mapping ($A_1 \leftrightarrow$ translational $u$; $T_2 \leftrightarrow$ microrotational $\omega$).

Here "substrate" refers to the Chiral LC Network of Axiom 1, corresponding to a chiral Laves K4 Cosserat crystal at the substrate level.

## Key Results

| Result | Statement |
|---|---|
| K4 scattering matrix | $S_{ij} = (1/2) - \delta_{ij}$ for $z_{\text{local}} = 1$ |
| Matrix form | $S = (1/2) \mathbf{1} - I$ (all-ones matrix minus identity) |
| Irrep decomposition under $T_d$ | $V_{\text{4-port}} = A_1 \text{ (1D)} \oplus T_2 \text{ (3D)}$ |
| $A_1$ eigenvalue | $+1$ (basis $(1, 1, 1, 1)/2$ — scalar/longitudinal) |
| $T_2$ eigenvalue | $-1$, triply degenerate (basis spans traceless 3D subspace — vector-like/transverse) |
| Eigenvalue sum | $4 \cdot 1 = 4$ (trace of 4×4 correlation matrix) |
| $A_1$ Cosserat mapping | Translational $u$ (isotropic, longitudinal) — propagates at $c \sqrt{2}$ |
| $T_2$ Cosserat mapping | Microrotational $\omega$ (anisotropic, transverse) — propagates at $c$; **THIS IS THE PHOTON** (weak-C 2026-06-15: the **free / sub-saturation / continuum-limit** $T_2$ — its $L \gg \ell_{node}$ limit is the Maxwell field; the *same* $T_2$ sector hosts the bound electron's massive mode at saturation, per §6 line 134) |
| Bare scattering unitarity | Without Op3 dissipation, $A_1$ propagates forever, $T_2$ reflects forever, no energy loss |
| Op3 asymmetric **transduction** (2026-07-19 RULED; ⬇ dated note below) | The $A_1$ **mode** empties by lossless power-conserving scatter (common-mode rejection redistributes $A_1$ content into the $T_2$ irreps); $T_2$ settles into quasi-stable pattern. **Mode-projection loss ≠ system loss** — the system conserves power (`src/ave/core/k4_tlm.py:396-398`). *(Superseded prose, preserved 2026-07-19: "$A_1$ loses energy monotonically; $T_2$ settles into quasi-stable pattern.")* |
| Physical origin of asymmetry | Gauss's law forbids longitudinal EM in vacuum: $\nabla \cdot \mathbf{E} = 0$ |

> **↗ Rotation-flavor tag (2026-07-03, KEEP-BOTH — §8 rotation un-conflation, `research/2026-07-03_em-readout-vsector-stage1_prereg.md` §8; additive):** the "$T_2$ … Microrotational $\omega$ … **THIS IS THE PHOTON**" row above is the **MASSLESS EM-inductive rotation** — the Axiom-1 μ₀-family **B** field, matched ($\Gamma=0$), propagating at $c$. It must be distinguished from the **GAPPED mechanical Cosserat couple-stress $\omega$** that the *static* (2,3) Link rides (Yukawa-screened, short-range; `clm-wcoul2`). These are TWO rotation-flavored fields sharing the symbol $\omega$: the row's free/continuum-limit $T_2$ is the massless photon; the saturation-regime bound mode (§6 line 134, "the same $T_2$ sector hosts the … massive mode") is the gapped mechanical one. The gapped-vs-massless split, not the free-vs-bound one, is the load-bearing sector distinction for the V-sector transducer. Clean reference: [`node-up-small-large-signal.md:39`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md).

> **↗ G2 ADJUDICATED (2026-07-03, KEEP-BOTH — the "$T_2$ Cosserat mapping … Microrotational $\omega$ … THIS IS THE PHOTON" row (line 26) AND the rotation-flavor tag above are BOTH PRESERVED unedited; Grant-adjudicated ruling, `research/2026-07-03_g2-photon-relabel_note.md`; the #491-era rotation-flavor tag's underlying DOF question is now RULED).** The row labels the photon's DOF family as **microrotational $\omega$**. Per the ruling this **family label is CORRECTED**: the massless photon family is the **transverse-TRANSLATIONAL $u$** branches, NOT the node micro-rotation. The two-sublattice band structure (line-26's "propagates at $c$" = $\sqrt{G/\rho}$, the translational-shear speed) is exactly the massless $u$-family; the Step-1 eigenvector-composition rider READS it: the 2 massless transverse branches are **$u$-dominated** ($\omega$-fraction max $=2.5\times10^{-7}$, $u$-fraction $=1.000000$), the 6 gapped branches are **$\omega$-dominated** ($1.000000$) — `g2_photon_eigvec_composition.json`.
> - **What the rotation-flavor tag got RIGHT and the row got WRONG on labels:** the tag correctly split "massless EM-inductive rotation (photon)" from "gapped mechanical Cosserat $\omega$ (winding)". The ruling *sharpens* the first half: the photon's "EM-inductive rotation" is the **bond-level curl $\nabla\times u$ of the massless translational wave**, NOT a micro-rotational $\omega$ DOF. So the row's "Microrotational $\omega$ … THIS IS THE PHOTON" is the **stale label** — the photon is transverse-$u$, and its $\mathbf{B}$ is the $u$-wave's circulation. The **gapped mechanical $\omega$** half of the tag stands unchanged (the winding's home).
> - **Consequence for the $A_1$/$T_2$ speed-split row (line 25):** the "$c\sqrt2$ vs $c$" speeds are unchanged; what is relabeled is *which sector is the photon* — the massless transverse-$u$ pair at $c=\sqrt{G/\rho}$, not the $\omega$ sector. The $A_1$ longitudinal-$u$ mode still dissipates (Gauss); it is not the photon either. The photon is the *transverse* subset of the translational branches.

## §1 — Group-theoretic foundation

<!-- claim-quality: clm-j550uh -->

Under the tetrahedral point group $T_d$ (the symmetry of the four tetrahedral neighbors on K4), the 4-port amplitude space decomposes into irreducible representations as:

$$V_{\text{4-port}} = A_1 \text{ (1D)} \oplus T_2 \text{ (3D)}$$

### $A_1$ — totally symmetric rep (1D)

Basis vector: $(1, 1, 1, 1)/2$ — **all four ports carry equal amplitude.**

Physically: **isotropic, scalar, longitudinal.**

At a node, this is a scalar "breathing" excitation — the node as a whole compresses/expands without directional bias. **Maps to Cosserat translational sector $u$.**

### $T_2$ — 3D triplet rep

Basis spans the traceless 3D subspace $\{v : \sum_i v_i = 0\}$ — **for every excitation at one port, an equal and opposite excitation exists at some combination of other ports.**

Physically: **anisotropic, vector-like, transverse.**

The node as a whole has no net scalar displacement; instead it has a directional (vector-like) excitation. **Maps to Cosserat microrotational sector $\omega$.**

## §2 — Scattering matrix and eigenvalues

The K4 scattering matrix in AVE's TLM implementation (`src/ave/core/k4_tlm.py:36-65`):

$$S_{ij} = (1/2) - \delta_{ij} \text{ for } z_{\text{local}} = 1$$

i.e., $S = (1/2) \mathbf{1} - I$ where $\mathbf{1}$ is the all-ones matrix and $I$ is the 4×4 identity, acting on the 4-vector of port amplitudes.

### Computing $S$ on each irrep

**On $A_1$ basis $(1, 1, 1, 1)/2$:**

$$S \cdot v = ((1/2) \cdot 4 - 1) \cdot v = (2 - 1) \cdot v = +1 \cdot v$$

**$A_1$ eigenvalue: $+1$.**

**On any traceless vector ($A_1$-orthogonal):** $\mathbf{1} \cdot v = 0$, so:

$$S \cdot v = (-I) \cdot v = -v$$

**$T_2$ eigenvalue: $-1$** (triply degenerate).

### Physical interpretation

The $+1$ eigenvalue on $A_1$ means the bare scattering **preserves the $A_1$ mode exactly** (like a DC bias passing through a reflector unchanged). The $-1$ eigenvalue on $T_2$ means $T_2$ modes **flip sign on scatter** — the standard traveling-wave reflection behavior.

## §3 — Empirical eigenvalue measurement

`src/scripts/vol_1_foundations/phasor_discovery.py` at $N = 64$, $n_{\text{steps}} = 300$, seeded $(2, 3)$ Golden-Torus voltage ansatz at $(R, r) = (16.0, 6.108)$, amplitude $0.5$. Snapshot port-correlation eigenvalues at steps 100/200/300:

| Step | $\lambda_1$ | $\lambda_2$ | $\lambda_3$ | $\lambda_4$ |
|---|---|---|---|---|
| 100 | 1.654 | 1.215 | 1.130 | **0.001** |
| 200 | 1.642 | 1.210 | 1.147 | **0.000** |
| 300 | 1.653 | 1.203 | 1.144 | **0.000** |

Sum of eigenvalues $= 4.0$ at each step (trace of 4×4 correlation matrix = 4; sanity check passes). **The smallest eigenvalue is exactly zero, stable across time.** The port-space of the soliton lives in a 3D subspace of the nominal 4D port space — **exactly the $T_2$ subspace**, with $A_1$ fully dissipated.

The $(2, 3)$ winding label here is the electron configuration's phase-space (Clifford-torus) winding; the electron's real-space body is the $0_1$ unknot soliton.

## §4 — How Op3 dissipation breaks the symmetry

<!-- claim-quality: clm-9kd2t3 -->

The bare K4-TLM with $S = (1/2)\mathbf{1} - I$ is unitary. $A_1$ would propagate forever, $T_2$ would reflect forever, no energy loss.

The bond-level **Op3 reflection** (`op3_bond_reflection=True`) adds an impedance mismatch at each bond: $Z_{\text{eff}} = Z_0 / \sqrt{S_{\text{sat}}}$ where $S_{\text{sat}}$ is the Axiom-4 saturation factor.

> **🟢 RULED (2026-07-19, Grant in-chat — Op3 = LOSSLESS TRANSDUCTION, not system dissipation; Rule-12 supersession, the original two sentences are preserved verbatim below).** Grant's verbatim ruling (normalized from "*mode loss should jot equal system loss, its trasnduction right?*" [sic]): the Op3 $A_1$ behaviour is **lossless transduction OUT of the $A_1$ mode** (a power-conserving unitary scatter; common-mode rejection converts $A_1$ content into the other irreps), **NOT system dissipation** — **mode-projection loss ≠ system loss.** The implementing code is unitary and power-conserving (`src/ave/core/k4_tlm.py:396-398`, verified at HEAD: `V_inc_A[k] = Γ·V_ref_A[k] + T·V_ref_B[k]`, `T = √(1−Γ²)`, "**Conserves total power**"); a lossless reactive scatter ($|\Gamma|^2+|T|^2=1$) cannot dissipate. Corrected wording below; the pre-2026-07-19 sentences are preserved verbatim.

This impedance mismatch **transduces energy asymmetrically between the two mode-sectors** (the *system* conserves power — `k4_tlm.py:396-398`):

- **$A_1$** — common-mode "DC" across all ports — has **no spatial gradient in port space**. Its reflection at bonds produces **destructive interference** (common-mode rejection) with neighboring nodes' $A_1$ components. **The $A_1$ mode empties monotonically — its content is transduced into the $T_2$ irreps, not lost from the system.** *(Superseded prose, preserved 2026-07-19: "$A_1$ loses energy monotonically until it reaches zero.")*
- **$T_2$** — carries spatial structure. Reflection at bonds **redirects flux into standing-wave patterns**. $T_2$ re-distributes more slowly, settling into a **quasi-stable configuration**. *(Superseded prose, preserved 2026-07-19: "$T_2$ dissipates more slowly, settling into a quasi-stable configuration.")*

## §5 — Physical correctness: Gauss's law forbids longitudinal EM

This asymmetric **mode-transduction** (2026-07-19 RULED — the $A_1$ mode empties into $T_2$; the system conserves power, not a system loss) is **physically correct** for electromagnetic waves on a Maxwell-substrate: **longitudinal components ($\nabla \cdot \mathbf{E} \neq 0$) are forbidden in vacuum by Gauss's law**, so any $A_1$-type longitudinal excitation must **empty (transduce out of the $A_1$ mode)** to leave only the transverse ($\nabla \cdot \mathbf{E} = 0$) sector. *(Superseded prose, preserved 2026-07-19: "This asymmetric dissipation is physically correct … so any $A_1$-type longitudinal excitation must dissipate to leave only the transverse sector.")*

**The K4 scattering realizes this constraint automatically through $T_d$ symmetry.** No additional physics needs to be imposed; the substrate's tetrahedral symmetry forces the right EM behavior.

## §6 — Propagation-speed split

The two irreps propagate at different speeds on the K4 substrate:

| Mode | Propagation speed | Substrate origin |
|---|---|---|
| $A_1$ (longitudinal) | $c \cdot \sqrt{2} = \sqrt{K_{\text{bulk}} / \rho}$ | Bulk modulus $K_{\text{bulk}}$ governs scalar compression |
| $T_2$ (transverse photon) | $c = \sqrt{G / \rho}$ | Shear modulus $G$ governs transverse shear |

The K4 magic-angle condition $K = 2G$ (Vol 1 Ch 2 macroscopic moduli) makes the substrate's $A_1$ and $T_2$ speeds related by $v_{A_1} / v_{T_2} = \sqrt{2}$ — the same $\sqrt{2}$ that shows up in cardinal-axis kinematics (see [Photon Propagation Baseline](../../dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md)).

> **🔴 WEAK-C SCOPE-NOTE (2026-06-15, Rule 12 — tables above PRESERVED unedited; weak-C canonization, gate `wejkhvnfb`, Grant-confirmed 2026-06-14; prereg at repo-root `research/2026-06-15_weak-c-photon-continuum_prereg.md`).** The "$T_2$ = transverse photon at $c = \sqrt{G/\rho}$" rows (§5 line 26, §6 line 121) name the **free / sub-saturation / continuum-limit** $T_2$ mode. Its long-wavelength regime ($L \gg \ell_{node}$) IS the **Maxwell continuum EM field** — $Z_0 = \sqrt{\mu/\varepsilon}$ and $c = 1/\sqrt{LC}$ are $\ell_{node}$-independent (`z0-derivation.md:40`; `master-equation.md:16, :61`), so the free photon's propagation description does not depend on the lattice pitch. This is the **free** half of the free-vs-locked split already canon in §7 below (the reconciliation sentence): the *same* $T_2$ sector is **massless when propagating freely** AND hosts the bound electron's **massive** Cosserat shell **at saturation** (the locked / matter half). One substrate, two regimes — the continuum is a *regime*, not a coexisting field; input-count stays 3 {$m_e$, $\alpha$, $G$}.

## §7 — Cosserat sector mapping

The $A_1 \oplus T_2$ decomposition aligns directly with the Cosserat split:

| K4 port-space rep | Physical character | Cosserat sector | Mass content |
|---|---|---|---|
| $A_1$ (1D) | Isotropic, longitudinal | Translational $u$ | Massless (propagates at $c\sqrt{2}$) |
| $T_2$ (3D) | Anisotropic, transverse | Microrotational $\omega$ | **Massive** (mass-gap $m^2 = 4 G_c / I_\omega$, see [Cosserat Mass-Gap](../../axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md)) |

This mass split is **exactly what's needed**: the photon ($T_2$) needs to be massless when propagating freely (and it does — at sub-saturation amplitudes the $T_2$ mode is massless); the bound electron's Cosserat shell IS the massive mode that the same $T_2$ sector hosts at saturation.

> **🔴 SECTOR RE-SCOPE — the $T_2$ "Massive (mass-gap $4G_c/I_\omega$)" entry is the FLYWHEEL clock gap, the REST MASS is A1 (2026-06-20, Rule 12 — §7 table + body and the weak-C scope-note above PRESERVED unedited; Grant-ratified mass-sector ruling; ADDS to the existing free-vs-locked note).** The §7 "Mass content" column marks $T_2$ (microrotational $\omega$) **Massive** ("mass-gap $m^2 = 4G_c/I_\omega$") and $A_1$ (translational $u$) **Massless**. **Re-scope (consistency-class):** the $T_2$/$\omega$ mass-gap is the **FLYWHEEL frequency / clock gap** (Compton/Larmor clock of the spin / frequency-regulation sector — the Park-dq FOC rotating frame), re-scoped from "**the** rest mass." The rest-mass *store* is the orthogonal **A1 longitudinal DILATATION** depression ($Z_{bulk}\to0$; [`master-equation.md`](../../dynamics/ch4-continuum-electrodynamics/master-equation.md):20 "A1 dilatation-MASS") — held at $90°$ to $T_2$ by the **GRADE orthogonality** (**A1 ⊥ T2**), which is **why** the table's $A_1$ entry reads "Massless (propagates at $c\sqrt{2}$)" in the *free* phase yet hosts the bound electron's rest-mass depression in the *locked* phase (the free-vs-locked split in the weak-C note above). The flywheel regulates the frequency that SETS the mass (Compton $f = mc^2/\hbar$); mass stays A1. Body preserved per Rule-12. *(⚠ 2026-06-20 CORRECTION: FOC does NOT FORCE A1 ⊥ T2 — the temporal-within-tank "FOC d-q" reading is RETRACTED, `clm-533gvm` solidity 0.30; the canonical FOC homes are SPATIAL inter-object 90°. A1 ⊥ T2 stands FOC-INDEPENDENT on the grade decomposition; REFUTED flag at [`master-equation.md`](../../dynamics/ch4-continuum-electrodynamics/master-equation.md):20.)*

## §8 — Implications

1. **Photon identification:** $T_2$-only is the canonical AVE-native photon ([Photon Identification](../../dynamics/ch4-continuum-electrodynamics/photon-identification.md)). $A_1$ dissipating is the Gauss's-law constraint enforced automatically by $T_d$ symmetry — NOT an additional postulate.
2. **Electron formation:** the canonical electron emerges when a $T_2$ photon at $\omega = \omega_C$ self-saturates at the bond LC tank. The $T_2$ → bound-state transition is the saturation engagement at $V \to V_{\text{yield}}$.
3. **Universal kernel structure:** the same $T_d$ irrep machinery generalizes to other tetrahedrally-coordinated substrates (e.g., diamond lattices in solid-state physics). The K4-specific instance here is the AVE substrate's signature.
4. **No imported QM:** all of this comes from $T_d$ symmetry on the K4 lattice + Maxwell-substrate consistency. **No need to import "transverse vs longitudinal" as a separate postulate** — it emerges from substrate-native group theory.

## Cross-references

- **Canonical scripts:**
  - `src/ave/core/k4_tlm.py:36-65` — scattering matrix implementation
  - `src/scripts/vol_1_foundations/phasor_discovery.py` — empirical eigenvalue measurement
- **KB cross-cutting:**
  - [Photon Identification (T₂-only)](../../dynamics/ch4-continuum-electrodynamics/photon-identification.md) — canonical photon as $T_2$ Cosserat $\omega$ microrotation
  - [Photon Propagation Baseline](../../dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md) — empirical $v = c\sqrt{2}$ cardinal-axis and $A_1$/$T_2$ speed split
  - [K4 Rotation Group $T = A_4$](../../axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) — full rotation symmetry $T = A_4$ on the same port basis (orientation-preserving subgroup of $T_d$)
  - [Cosserat Mass-Gap](../../axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md) — $T_2$ massive mode at $m^2 = 4 G_c / I_\omega$
  - [Lattice Impedance Decomposition](lattice-impedance-decomposition.md) — Op3 bond reflection via $Z_{\text{eff}}(r) = Z_0 / \sqrt{S}$
  - [Universal Saturation-Kernel Catalog (A-034)](../../../common/universal-saturation-kernel-catalog.md) — Op3/Op14 saturation framework
- **Canonical manuscript:**
  - Vol 1 Ch 1 (Axiom 1) — K4 lattice + tetrahedral connectivity
  - Vol 1 Ch 2 (Macroscopic Moduli) — magic-angle $K = 2G$
  - Vol 1 Ch 4 (Continuum Electrodynamics) — Master Equation context

---

> **🔴 FLAG (2026-07-17, flag-don't-fix — body above untouched): Op3 label-vs-code contradiction — ROUTED, not fixed here.**
>
> This leaf's Op3 prose reads the $A_1$ sector as a genuine **system-loss**:
>
> - `:28` — "Op3 asymmetric dissipation | $A_1$ **loses energy monotonically**; $T_2$ settles into quasi-stable pattern"
> - `:109` — "This impedance mismatch **dissipates energy asymmetrically** for the two sectors:" · `:111` — "$A_1$ ... **loses energy monotonically until it reaches zero**."
>
> The **code that implements Op3** is unitary and power-conserving (re-verified at HEAD):
>
> - `src/ave/core/k4_tlm.py:396-398` — "Unitary: `V_inc_A[k] = Γ * V_ref_A[k] + T * V_ref_B[k]`, where `Γ = (Z_B - Z_A)/(Z_B + Z_A)`, `T = sqrt(1 - Γ²)`. Seen from B, the reflection is `-Γ` (opposite sign). **Conserves total power.**"
>
> A lossless reactive scatter ($|\Gamma|^2+|T|^2=1$) cannot dissipate. **Candidate re-read — common-mode rejection / redistribution-by-counting:** $A_1$ is the common mode; its bond-reflection destructively interferes with neighbours (`:111`), so the $A_1$ **mode** empties into the $T_2$ pattern while the **system** conserves power. That is **loss-from-a-mode**, not **loss-from-the-system** (the MODE-vs-SYSTEM carve).
>
> **Adjudication ROUTED; owner = the operator-physics lane.** Consequence: the terminology leaf's "four licensed loss channels" enumeration (`substrate-native-terminology.md:27`) lists this Op3 channel as a genuine system-loss and needs correction on that channel (the other three are unaffected). See the Regime-IV dissipation audit §F4 (`research/2026-07-17_regime-iv-dissipation-audit.md`) and the discipline leaf [`retention-transition-split.md`](../../../common/retention-transition-split.md).
>
> ---
>
> ### 🟢 RESOLUTION — RULED 2026-07-19 (Grant in-chat; supersedes the ROUTED status above)
>
> The routed adjudication is **RULED**. Grant's verbatim ruling (2026-07-19, in-chat): "*mode loss should jot equal system loss, its trasnduction right?*" [sic]. **Ruling (Grant-verbatim intent, normalized):** the Op3 $A_1$ behaviour is **LOSSLESS TRANSDUCTION** out of the $A_1$ mode — a power-conserving unitary scatter in which common-mode rejection converts $A_1$ content into the other ($T_2$) irreps — **NOT system dissipation.** The **candidate re-read named in the flag above (common-mode rejection / MODE-vs-SYSTEM carve) is the ruled reading.**
>
> **Receipts (re-verified at HEAD):** the code that implements Op3 is unitary and power-conserving — `src/ave/core/k4_tlm.py:396-398`: "`V_inc_A[k] = Γ * V_ref_A[k] + T * V_ref_B[k]` … `T = sqrt(1 - Γ²)` … **Conserves total power.**" A lossless reactive scatter ($|\Gamma|^2+|T|^2=1$) cannot dissipate; mode-projection loss ≠ system loss.
>
> **Executed (this ruling):** the §"Key Results" `:28` row and the §4 `:111`/`:113` sentences are corrected to transduction wording (Rule-12; originals preserved verbatim inline). *(Line-anchor repoint 2026-07-19: this ruling's own D1 RULED-block insertion at §4 shifted the pre-insertion `:109`/`:111` sentences down to `:111`/`:113`; the FLAG body above at `:179`/`:185` still quotes them by their pre-insertion `:109`/`:111` anchors and is preserved unedited per Rule-12.)* The terminology leaf's "four licensed loss channels" enumeration is corrected from LOSS to TRANSDUCTION on the Op3 channel (`substrate-native-terminology.md:27`, dated note); the `retention-transition-split.md` Op3 worked example is promoted from "candidate resolution (routed)" to RULED. Docket: RULING 21 (`_orchestration/2026-07-10_rulings-docket.md`). This FLAG's body above is **preserved unedited** per Rule-12; this addendum is the current-status record.
>
> **Blanket reading-note (the remaining "dissipate" mentions in this leaf).** This note dispositions the leaf's other "dissipate"/"dissipation" mentions per RULING 21 — read them all as **mode-emptying / transduction into $T_2$** (the system conserves power), **not a system loss.** It **covers** two classes of site: **(a) the $A_1$-mode "dissipating" mentions** — the intro (line 11, "$A_1$ dissipates via Gauss's law"), §3 (the empirical "$A_1$ fully dissipated"), and §8 ("$A_1$ dissipating is the Gauss's-law constraint"); **and (b) the two "Op3 dissipation" operator-label sites** that name the *operator* rather than the mode-emptying — the §4 header (`:101`, "How Op3 dissipation breaks the symmetry") and the Key-Results bare-row back-ref (`:27`, "Without Op3 dissipation, $A_1$ propagates forever, $T_2$ reflects forever, no energy loss"). Both class-(b) sites are historical-wording covered by the same ruling; I **add them to this note rather than editing them inline** — editing the §4 header would break the "§4" section anchor that external docs cite (the very anchor-drift this batch is repairing), and `:27` is a preserved Key-Results context row. The surrounding physics is unchanged: Gauss's law forbids longitudinal EM, the $A_1$ mode empties, and only the transverse ($T_2$) sector survives. Those bodies are left as written (they were not the load-bearing contradiction sites the flag named) and are dispositioned by this note; the G2-ADJUDICATED KEEP-BOTH block above (line 35, "the $A_1$ longitudinal-$u$ mode still dissipates") is a **separate 2026-07-03 ruling's preserved block** and stays untouched.

---

> **📍 LINE-ANCHOR DRIFT note (2026-07-19; routed to the auditor lane, do NOT chase here).** This leaf has accreted dated Rule-12 scope-notes over several months; each insertion shifts the line anchors below it. The 2026-07-19 RULING-21 D1 block (inserted at §4) shifted §4-and-below anchors by **+2**; earlier dated notes (2026-06-15 weak-C, 2026-06-20 sector re-scope, 2026-07-03 tags) had already shifted the §6/§7 anchors further. **External docs that cite this leaf by line anchor may therefore point stale.** Inventory the batch review surfaced (corrected targets **content-verified at this HEAD** where marked ✓; the rest routed to the auditor for repointing at leisure — no edits made to those docs beyond the weak-C prereg §7 log this batch):
>
> | Citing site | Cited anchor | Corrected target | Status |
> |---|---|---|---|
> | `research/2026-06-15_weak-c-photon-continuum_prereg.md:193` (drift log) | `:26, :121, :134` | `:26` (no drift) ✓, `:121`→`:129` ✓, `:134`→`:144` ✓ | **corrected this batch** (dated note at the prereg §7 log; supersedes its "NO drift (all exact)") |
> | `research/2026-06-15_weak-c-photon-continuum_prereg.md:63` (body cite) | `:134` | `:144` ✓ | routed (prereg body cite; left unedited per surgical scope) |
> | `research/2026-05-17_C13b_bullet_cluster_prereg.md:29` | `:109` | `:111` ✓ | routed (pre-existing loose anchor) |
> | `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md:50` | `:109` | `:111` ✓ | routed (pre-existing loose anchor) |
> | `research/2026-07-03_em-readout-stage0_result.md:88` | `:133` ("Massless (propagates at $c\sqrt2$)") | `:141` ✓ | routed (pre-existing imprecise anchor) |
> | `research/2026-07-17_regime-iv-dissipation-audit_items.json:1571` | `:28,97,101,111` | `:28`/`:97`/`:101` stable, `:111`→`:113` ✓ | routed |
>
> **⚠ Correction to the batch review's F-1(b) estimate:** the review computed the weak-C prereg's `:121`/`:134` cites as "off by 2 (→`:123`,`:136`)" — that captured **only** this batch's +2 D1 shift. The content-verified targets are **`:129` and `:144`** (cumulative drift of +8 / +10 from the 2026-06-15 freeze; the prereg's "NO drift (all exact)" claim was already inaccurate at `origin/main`, not only after this PR). The prereg §7 note repoints to the verified `:129`/`:144`.
>
> **Internal self-references** in this leaf's own preserved Rule-12 blocks are ALSO stale and left **unedited** (preserved-block discipline; routed to the auditor): line 26 and line 31 cite "§6 line 134" (the reconciliation/mass-split sentence, now §7 `:144`); the weak-C scope-note (line 133) cites "(§5 line 26, §6 line 121)" (now §6 `:129`); the 2026-07-17 FLAG body (`:179`/`:185`) quotes the §4 sentences by their pre-insertion `:109`/`:111` anchors (now `:111`/`:113`).

---

> **✅ REPOINTED — completion record (2026-07-19, Tier-2.5 hygiene batch; the routed inventory above is PRESERVED verbatim, this block records execution).** The external cites routed above have been repointed at their citing docs. Each target was **content-verified at this HEAD by grepping the quoted string** (the #728 "cumulative drift ≠ single-insertion offset — grep content, never arithmetic" lesson), not by arithmetic from the inventory's estimates:
>
> | Citing site | Inventory target | **Executed (content-verified) target** | Edit type |
> |---|---|---|---|
> | `research/2026-06-15_weak-c-photon-continuum_prereg.md:63` (body cite) | `:144` | **`:144`** ✓ (matches inventory) | frozen prereg → dated bottom correction-note |
> | `research/2026-05-17_C13b_bullet_cluster_prereg.md:29` | `:111` | **`:129`** ⚠ (inventory was WRONG) | frozen prereg → dated bottom correction-note |
> | `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md:50` | `:111` | **`:129`** ⚠ (inventory was WRONG) | non-frozen KB leaf → in-place Rule-12 |
> | `research/2026-07-03_em-readout-stage0_result.md:88` | `:141` | **`:141`** ✓ (matches inventory) | frozen result → dated bottom correction-note |
> | `research/2026-07-17_regime-iv-dissipation-audit_items.json:1571` | `:28`/`:97`/`:101` stable, `:111`→`:113` | **`:28`/`:97`/`:101` stable, `:111`→`:113`** ✓ | JSON body UNEDITED (see note below) |
>
> **⚠ Self-correction to this inventory (the #728 trap, caught here).** The rows for `C13b:29` and `lc-electrodynamics.md:50` were listed above as `:109`→`:111` with a ✓. That ✓ was **mis-verified**: both cites quote the **§6 transverse-photon speed row** (*"$T_2$ (transverse photon): $c=\sqrt{G/\rho}$"*), which is at **`:129`**, NOT `:111` (line `:111` is the Op3-transduction sentence). The `:111` was an **arithmetic +2** (the RULING-21 D1 §4 shift), applied to cites that actually point at §6 (cumulative drift +20). The inventory's OWN weak-C row correctly maps the identical-content `:121`→`:129`, so `:109`→`:111` for the same content was internally inconsistent. **Corrected content-verified target for both: `:129`** (grep-confirmed at HEAD; executed at both citing docs).
>
> **JSON note (the "else" branch).** `research/2026-07-17_regime-iv-dissipation-audit_items.json` has a **strict uniform 12-key schema** across all 126 items; adding a one-off correction key would break schema uniformity and risk downstream consumers. Per the additive-key-else-drift-inventory-note convention, the `:1571` repoint is recorded **here** and the JSON body is left **unedited**: the `reread_proposal` string at `:1571` recommends "fix at the canonical leaf `k4-port-irrep-decomposition.md:28,97,101,111`"; at HEAD `:28`/`:97`/`:101` are stable and the cited `:111` content (*"$A_1$ loses energy monotonically until it reaches zero"*, now the superseded-preserved prose) is at **`:113`**. That recommended fix was already executed by RULING 21; the repoint is documentary.
