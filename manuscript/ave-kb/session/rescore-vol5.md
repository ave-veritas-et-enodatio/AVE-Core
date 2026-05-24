# Vol 5 local-rigor rescore worksheet

Scored 22 `confidence: *pending*` entries against their canonical leaves. Grade = local derivation rigor only (solidity left `*pending*` for tooling).

| clm-id | confidence | one-line local-rigor justification |
|---|---|---|
| clm-lm9b3j | 1.0 | ξ_topo ≡ e/ℓ_node = e·m_e·c/ℏ is a pure composition of axiom constants; L=m/ξ² and C=ξ²/k are definitional dimensional bridges (category-i identities). |
| clm-j9l3ww | 0.7 | Op4 well argmin closes to d_HB=1.754 Å, E_HB=0.2158 eV end-to-end; rests on disclosed (1−φ) void-projection structural argument and r_O/r_H imported from the Vol 2 MCL solver. |
| clm-yyhczl | 0.6 | Fabry–Perot eigenvalue formula derived from first principles, but the leaf itself flags real open gaps: S–S +30% outlier "not validated" and systematic −2 to −7% on C–C/C–N/C–H ("open refinement"). |
| clm-4jy0t8 | 0.7 | MNA simulation closes with zero parameters given first-principles k; partial circularity (NIST k path) is disclosed, and 1192 cm⁻¹ is a structural cluster claim, not an exact named-band match. |
| clm-oilm45 | 0.6 | 10/11 passband-membership result on a fixed scale; criterion is disclosed-loose (membership, not peak match) and the C–H self-consistency check is flagged definitional. |
| clm-uowffm | 0.7 | Closed formula T_c=E_HB/(n_coop·k_B)→278.3 K; n_coop=9 imported from Vol 3 Ch.13 and the 4°C water target is an interpretive (not conventional) identification, both disclosed. |
| clm-u4vmgk | 0.3 | RMSD 2.59 Å asserted as an engine output; the folding engine itself is in a private repo with no in-leaf derivation — number stands without a traceable derivation chain. |
| clm-a3rby3 | 1.0 | Notation-binding manifestation of INVARIANT-N4 ($S_{11}$ dual-use); true by the invariant declaration, a definitional meta-claim. |
| clm-enjq28 | 0.3 | η_eq=P_C·5/7 appears only as a translation-table row in common/; the derivation leaf and Villin 0.8% live in the private engine repo — asserted at the leaf level available here. |
| clm-8zwyl3 | 0.1 | Ch.6 content is explicitly hypothesis/prediction with no derived numbers; the underlying biological identifications are asserted structural reinterpretations. |
| clm-239tr4 | 0.5 | The relaxation magnitude (~10⁻²⁰ m via Δr/r=α·ε_11) is a closed sub-calc, but it rests on an asserted h_⊥ chiral-metric bias and the leaf concedes the test is currently unfalsifiable. |
| clm-r6uef4 | 0.1 | +90° intrinsic phase difference is asserted from the L-handedness identification; no derivation of the value from axioms in the leaf. |
| clm-huhz7r | 0.3 | Three-port source/payload/sink model is a structural template; the L≈115.9 fH component is a bridge identity but the architecture identification itself is asserted, validated only downstream. |
| clm-f4osd7 | 0.3 | THz drive identification with Wien-law + ATP frequencies taken as external inputs; no AVE re-derivation and no quantitative spectral density bound. |
| clm-j20lz8 | 0.6 | f∝1/√α to 0.03% closes cleanly, but the leaf discloses this is simulator self-consistency (model behaves as an LC resonator), not independent experimental falsification. |
| clm-pav5m3 | 0.3 | Three-class sidechain partition is a qualitative grouping with no numerical Z thresholds; Z_backbone≈7 imported from the engine repo. |
| clm-br3bcv | 0.7 | Four-step chain closes ℓ_node→a_0→r_cov→d_0=3.80 Å; steps 1–2 are exact identities, step 3 imports covalent lengths (inherits clm-yyhczl residuals), step 4 is fixed-angle rigid-body geometry — all disclosed. |
| clm-x5z09x | 0.5 | Vol 5 manifestation of the cross-cutting saturation entry; the Regime I/II assignments rest on Δφ/α order-of-magnitude indicators (disclosed as non-precision), a real soft step. |
| clm-zt0pd1 | 0.7 | Z_topo=R+jX definition + L_R/C_R summation rules close as a definition inheriting the bridge identities; per-residue quantitative table is disclosed as held in the private engine repo. |
| clm-s11nf0 | 0.3 | Native-fold = unique min-|S_{11}|² is a framework-level mechanism statement; uniqueness is asserted (not proven) and the production solver + PDB validation are in the private repo. |
| clm-a034pf | 0.5 | Identification of folding with the Axiom-4 kernel C_eff=C0/√(1−(d0/d)²); kernel form is axiom-given (manifestation), the cross-scale list is cited not re-derived, application to folding asserted. |
| clm-rg7cls | 0.5 | Five-scale regime table with Δφ/α as disclosed order-of-magnitude indicators; the "unique solution / no search" justification rests on the asserted regime assignments. |

## Flags

- **Stale prose in several claim-quality entries.** clm-u4vmgk, clm-8zwyl3, clm-a3rby3, and clm-enjq28 caveats assert that `vol5/protein-folding-engine/` "does not exist" / "is unauthored" and that S11/Z_topo definition leaves live only in the private repo. As of this pass the directory DOES exist with four authored leaves (`z-topo-definition.md`, `levinthal-mechanical-resolution.md`, `regime-classification.md`, `index.md`). I left the prose untouched (out of scope: edit only the Quality block) but flag it as stale/inconsistent for a later prose pass. The framework *definitions* are now in-repo; only the per-residue quantitative tables and production solver remain external.
- **clm-a034pf depends-on the common A-034 catalog.** The catalog leaf (`common/universal-saturation-kernel-catalog.md`) carries clm-dxdsvt (26-instance catalog) and clm-gz7ryg (universal-kernel key result). I cited clm-dxdsvt (the catalog instance list, which contains the "Protein folding" row) and clm-gz7ryg (kernel definition) as deps — both verified to exist in common/, acyclic for a vol5 claim.
- **clm-a034pf leaf has a dangling relative link** (`../../common/universal-saturation-kernel-catalog.md` resolves to a nonexistent `vol5/common/` target; the real path is KB-root `common/`). This is already noted in the entry's caveat ("dangling link inherited verbatim from L3"); no action taken, flagged only.
- **clm-enjq28 / clm-pav5m3 / clm-zt0pd1 / clm-s11nf0** lean on a per-residue Z_topo table and η_eq derivation held in the private AVE-Protein repo. depends-on enumerated only against in-repo leaves + framework axioms; the external table is noted in rationale but not citable as a clm-dep (no clm-id exists in this repo for it).
- No cyclic or vol6 dependencies introduced. All cross-claim deps point to common/ or earlier-in-vol5 leaves.
