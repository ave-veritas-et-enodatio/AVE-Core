[↑ Ch.3 Pin/Port Configuration](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Vol-9 Class-C CONSISTENCY filing — the canonical home for the valence-distinct node-scatter BEDROCK S_n = (2/n)J - I assembled on the REAL srs/diamond CONNECT map (srs deg-3 = 192 DOF vs diamond deg-4 = 64 DOF; fixes the dense-TETRA_OFFSETS-cube collapse that graded_vacuum_network.py hardwires). Documents the bare spectrum {+1 common, -1x(n-1) differential} and four validate-on-known anchors (n=3 differential mult = 2 = photon transverse polarizations; winding 𝒬=3; α-free; spectrum forced). Originates NO new substrate primitive: the Op5 shunt-junction scatter, the K4 CONNECT map, and the (2,3) winding are PRE-EXISTING canonical content this leaf composes. Records the Fork-A outcome HONESTLY: the pre-committed 'longitudinal confinement needs the diamond's 3rd differential mode' was REFUTED, but it is a projector-algebra SECTOR-ORTHOGONALITY FACT (the A1 scalar IS the +1 common mode by construction, scramble-invariant), NOT a discriminating chord. The 2-vs-3 transverse multiplicity is an ECHO of DOF-counting (peer-to-SM rep-theory). NO emergence, NO value-prediction."
-->

## Node-Scattering Multiplicity (valence-distinct scatter bedrock, canonical leaf)

**Classification:** Class C — CONSISTENCY / structural-identity. This leaf is the **canonical home** for the node-scatter bedrock first banked in `research/2026-06-20_node-scattering-containment-gate_result.md` (PR #304). It documents an **operator** (the valence-distinct $n$-port node scatter) and its **bare spectrum**, both forced linear algebra; it originates no new physical claim. (Forward references previously pointed at [`device-circuit-models.md`](device-circuit-models.md) as the bedrock's home — that leaf never contained it; this leaf is the home, and those refs are repointed here.)

**Skills applied (2026-06-20 filing pass):** `substrate-native-check` (the operator is the Op5 shunt-junction scatter composed with the K4 CONNECT permutation — built FROM the bond graph, never imposed on a Cartesian grid) · `consistency-vs-emergence` v1.3 (Class-C; the spectrum is forced, the Fork-A verdict is a structural negative, neither is emergence) · `phase-space-coordinate-check` ($S_n$ eigenvectors live in $n$-PORT space; the A1 scalar / Cosserat vector live in real-space; the port→grade map is SHOWN, not assumed) · `consensus-bias-symmetric-standard` (the 2-vs-3 transverse count is peer-to-SM rep-theory; the SM also imports it) · `verify-before-cite` (anchors re-grepped on the source module + #304 result doc).

**Discipline:** This leaf is the **source of truth** for the node-scatter multiplicity bedrock. The CODE is `src/ave/solvers/node_scattering_multiplicity.py` (the first `build_srs_net` solver call-site); tests `src/tests/test_node_scattering_multiplicity.py` (13 passing, incl. the scramble-invariance regression marker). Result/prereg context: `research/2026-06-20_node-scattering-containment-gate_result.md` + `research/2026-06-20_node-scattering-containment-gate_prereg.md` (frozen commit `f87914fa`).

> ↗ See also: [`device-circuit-models.md`](device-circuit-models.md) §6 (the graded vacuum impedance network whose dense-`TETRA_OFFSETS` collapse this bedrock fixes); [`per-dof-vacuum-node-circuit.md`](per-dof-vacuum-node-circuit.md) (the per-DOF node-constitutive layer); [`vacuum-varactor-scatter-operator.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/vacuum-varactor-scatter-operator.md) (the $S(A)$-reading admittance-weighted generalization of this bedrock).

---

### 1. The valence-distinct node scatter (the bedrock operator)

A degree-$n$ substrate node is a shunt junction of $n$ directed bond-ports. The Op5
shunt-junction reduction (a common node voltage $V$, KCL on the equal-admittance
ports) gives the single-node scatter

$$
S_n = \frac{2}{n}\,J - I, \qquad (J = \text{all-ones } n\times n),
$$

with $S_n^2 = I$ (a lossless orthogonal reflection). The **load-bearing fix** is that
the *global* operator is assembled from the lattice's **OWN bond-graph CONNECT map**
(`chiral_lattice.scatter_matrix(n)` composed with the directed-edge `connect_index()`
permutation on `build_srs_net` / `build_diamond_net`), **NOT** the dense
`TETRA_OFFSETS` cube that `graded_vacuum_network.py` hardwires. Because the chiral
**srs** net is degree-3 and the **diamond** net is degree-4, the two assembled
operators are **genuinely structurally distinct**:

| Net | node valence $n$ | nodes (default $L$) | total DOF | differential mult $n-1$ |
|---|---|---|---|---|
| chiral **srs** | 3 | 64 | **192** | 2 |
| **diamond** | 4 | 16 | **64** | 3 |

This is the distinctness the dense-cube collapse erased: 192 vs 64 DOF, no collapse to
an identical operator (`operators_are_distinct`, HALT-gate H1). This module is the
**first solver call-site on `build_srs_net`** (it had zero before). The construction is
**PURE LINEAR ALGEBRA**: no dynamics, no posited core, no boundary.

### 2. The bare spectrum (validate-on-known)

$S_n$ is a rank-1 perturbation of $-I$. The all-ones port-sum vector is the single
**$+1$ eigenvector** (the **COMMON MODE** = the symmetric breathing / longitudinal
channel = Grant's bulk-saturation channel, Fork B); its orthogonal complement is the
**$-1$ eigenspace** of dimension $n-1$ (the **DIFFERENTIAL** modes). The differing
$-1$ multiplicity is the structural distinctness:

$$
\text{spectrum}(S_n) = \{\,+1\ (\times 1,\ \text{common}),\quad -1\ (\times (n-1),\ \text{differential})\,\}.
$$

- **$S_3$**: $\{+1\times 1,\ -1\times 2\}$ → differential multiplicity **2**.
- **$S_4$**: $\{+1\times 1,\ -1\times 3\}$ → differential multiplicity **3**.

Both global operators $\mathcal{S}$ are orthogonal with every eigenvalue on the unit
circle (the lossless-reflection sanity gate). The spectrum is **forced** — it is the
linear algebra of $(2/n)J - I$, not a fitted result (`consistency-vs-emergence`:
structural-identity / manifestation class).

### 3. Validate-on-known anchors

The bedrock was wired to four pre-committed validate-on-known anchors (prereg §2),
all PASS live (Stage 1 = PROCEED, no HALT):

| Anchor | Result | Reading |
|---|---|---|
| **(a) bare spectra** | $S_3=\{+1,-1\times 2\}$, $S_4=\{+1,-1\times 3\}$; $S^2=I$; common mode = port-sum | spectrum is canonical / forced |
| **(b) photon anchor** | srs differential mult $=2$ $==$ the photon's **2 transverse polarizations** (`test_l1_photon.py`) | the transverse count is reproduced from node valence |
| **(c) winding anchor** | seeded $(2,3)$ → $\mathcal{Q}_{\text{link}}=3$, $w_{\text{tor}}=2$; null → $0$ | the charge winding integer $\mathcal{Q}=3$ behaves |
| **(d) α-free invariance** | $\alpha\to 2\alpha$: spectra bit-identical, $\mathcal{Q}_{\text{link}}\ 3\to 3$, $d\mathcal{Q}/\mathcal{Q}=0$ | **structural** $\alpha$-independence (the load-bearing anchor) |

The $\alpha$-invariance is **structural, not numerical**: the operator modules import no
`ALPHA` (import-guarded — `assert "ALPHA" not in globals()`), no `Q_TANK`, no `ELECTRON`
instance. The $S_n$ matrix contains no $\alpha$; the winding integer $\mathcal{Q}_{\text{link}}$
contains no $\alpha$. This is the frame-independent anchor that survives the
eigen-vs-driven mismatch flagged in the prior prereg's Rule-12 retraction. None of the
HALT conditions tripped: H1 (collapse) NO; H2 (wrong spectrum) NO; H3 ($\sim$137/$\sim$3
artifact) NO — the only "3"s present are the *legitimate* diamond differential
multiplicity ($n-1=3$) and the winding integer $\mathcal{Q}=3$; H4 (winding broken) NO;
H5 ($\alpha$-leak) NO.

### 4. The Fork-A outcome — honest scope (REFUTED-as-a-test; a sector-orthogonality FACT)

> **🟡 HONEST-SCOPE (load-bearing — mirrors the #304 result doc's Rule-12 self-retraction).**
> Fork A pre-committed the prediction that **longitudinal confinement of the electron's
> A1 dilatation MASS-"3" requires the diamond's 3rd *differential* mode** (so it would
> exist on the degree-4 net and not on the degree-3 net). That prediction was
> **REFUTED** — but the honest reading is sharper than "a clean test came out negative":
> it is a **projector-algebra SECTOR-ORTHOGONALITY FACT, true by construction**, NOT a
> discriminating chord.

**Why it is a fact, not a test.** The longitudinal A1 dilatation **scalar IS the $+1$
common mode** of $S_n = (2/n)J - I$ (the all-ones eigenvector), and it is orthogonal to
the entire $-1$ differential sector **by construction**. The port→real-space embedding
($B_u$, rows = bond directions) is genuinely derived and SHOWN — the $+1$ common-mode
port-vector projects to a real-space **scalar** ($\sqrt{\text{degree}}$ content) with
**zero** real-space vector grade on a force-balanced node; the $-1$ differential modes
project to a real-space **vector/shear** grade with **zero** scalar. But the embedding
**does not feed the verdict**: the verdict-driving quantities
(`differential_scalar_content`, `common_mode_scalar_content`) are
**scramble-invariant projector identities** ($|a\cdot\text{ones}|=0$ for the $-1$ sector
by orthogonality; $\sqrt{\text{degree}}$ for the $+1$ sector by construction). The
regression marker
`test_node_scattering_multiplicity.py::test_fork_a_verdict_is_invariant_under_bond_unit_scramble`
verifies live that scrambling the bond directions (which destroys force-balance) leaves
those quantities **bit-unchanged** — so the verdict could only ever come out R3, for ANY
lattice, with no physics in the decision (`verdict_is_projector_tautology=True`).

**Fork A was MISCAST.** It presupposed that longitudinal confinement lives in the
*differential* sector; it does not. An isotropic/longitudinal scalar IS the $+1$ common
mode and is orthogonal to the differential sector **by definition** (consistent with
`master-equation.md`:20 — A1 ⊥ T2; never wire the winding into the breather's own
phasor). R3 is TRUE, but true **by construction**.

**The genuine deliverables (untouched by this correction):**

1. **A sound, reusable BEDROCK** — the genuinely-distinct $n$-port scattering operators
   assembled from the real srs / diamond CONNECT map (§1; 192 vs 64 DOF; first
   `build_srs_net` solver call-site; the `graded_vacuum_network` `TETRA_OFFSETS`
   collapse genuinely fixed). Plus the four validate-on-known anchors (§3).
2. **A tautological-but-USEFUL sector redirect** — R3 correctly REDIRECTS A1
   mass-containment away from the differential-multiplicity red herring and onto the
   $+1$ common mode (Grant's bulk-saturation / Fork-B framing). Useful as a redirect;
   not a test result. (Fork B = the unbuilt $Z_{\text{core}}\to\infty$ open-boundary
   operator on the common-mode channel — DEFERRED, surfaced for adjudication, not
   silently pivoted to.)
3. **An honest ECHO on the transverse 2-vs-3 count** — srs's 2 differential modes
   $= 2$ photon polarizations $=$ **peer-to-SM rep-theory DOF-counting**.
   Symmetric-standard (`consensus-bias-symmetric-standard`): the SM also imports the
   massless-vector (2 DOF) vs massive-vector (3 DOF) count from representation theory;
   AVE *re-derives* the transverse count from node valence (at parity on the transverse
   sector, arguably ahead). The *longitudinal-containment* claim that would have put AVE
   genuinely *ahead* was **never a real test** — so AVE is not ahead there, and we say
   so. **NO discriminating chord emerged from this gate.**

This is honest closure (Rule 11): the branch closes on a named mechanism (longitudinal =
common-mode scalar, not differential), not debugged toward a rescue, not re-binned
post-hoc. Per Rule 12, the #304 result doc preserves its original headline/§2/§5 body
unedited beneath a 🔴 scope-correction header; this leaf documents the **corrected** net
outcome as the canonical filing.

### 5. Structural-vs-asserted / class table

| Item | Class | Status |
|---|---|---|
| $S_n = (2/n)J - I$ bare spectrum $\{+1, -1\times(n-1)\}$ | structural-identity (forced linear algebra) | **derived** (forced) |
| srs/diamond operator distinctness (192 vs 64 DOF) | structural | **derived** from the CONNECT map |
| $\alpha$-free invariance of spectrum + $\mathcal{Q}$ | structural | **derived** (import-guarded, scramble-tested) |
| srs differential mult $= 2 =$ photon transverse DOF | consistency (validate-on-known) **+ ECHO** of rep-theory DOF-counting | re-derived from valence; peer-to-SM |
| seeded $(2,3) \to \mathcal{Q}=3$ winding | consistency (validate-on-known) | **derived** GIVEN [Q]≡[L] (asserted posit) |
| A1 longitudinal scalar $=$ $+1$ common mode | projector-algebra **sector-orthogonality FACT** (scramble-invariant) | true **by construction**, NOT a test |
| Fork-A "longitudinal needs the 3rd differential mode" | pre-committed prediction | **REFUTED** (miscast; a fact, not a chord) |

No emergence-class claim is made anywhere in this leaf. No CODATA / manuscript-quoted
target was input. Nothing here is labelled "derived" beyond the forced linear algebra
and the explicitly-conditional winding (conditional on the asserted [Q]≡[L] posit).
