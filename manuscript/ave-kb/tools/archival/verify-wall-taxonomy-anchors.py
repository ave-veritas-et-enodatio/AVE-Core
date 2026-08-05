#!/usr/bin/env python3
"""Leaf-scoped anchor + QUOTE-AT-LINE verifier for `common/wall-taxonomy.md`.

WHY THIS EXISTS (PR #860 audit, findings W1/W2)
-----------------------------------------------
The leaf originally published a "two-method, 48 anchors, 48 PASS" receipt whose
actual content was: *for every cited file, the worktree line equals the
`origin/main` line at the same index*. That sweep is **non-discriminating by
construction** on this branch -- the branch adds files and touches no cite
target, so no cited file COULD have drifted from base. It could not have
failed, and it certified nothing about whether the leaf's quoted excerpts
actually occur at the lines they cite.

This tool runs the check that was missing:

  PASS A -- ANCHOR ENUMERATION + EXISTENCE
      Every `path:NN` anchor in the leaf is extracted by machine (link-form
      `[t](path):NN`, its comma/range continuations `:NN,:MM` / `:NN-MM`, and
      an explicitly-declared supplement for anchors written with an implicit
      file, e.g. a bare `:40` following a named leaf). Each is resolved and
      the line is checked to exist. THE FULL ENUMERATED LIST IS PRINTED --
      a bare count is not auditable (the PR #860 audit got 46, 49 and 64 by
      three different extraction rules, which is exactly the failure mode a
      published count without a published list produces).

  PASS B -- QUOTE-AT-LINE
      For every excerpt the leaf reproduces from canon, the manifest below
      records (i) the SOURCE-side text, (ii) the file and line it is claimed
      to sit at, and (iii) the declared DELTA between the source text and the
      leaf's rendering of it. The tool asserts the source text occurs AT THAT
      LINE (whitespace-normalized substring), and that a probe of the leaf's
      own rendering still occurs in the leaf -- so the manifest cannot drift
      away from the text it documents.

      `delta` is the honesty channel. `EXACT` means the leaf reproduces the
      source byte-for-byte inside its verbatim tag. Anything else names the
      alteration, and every such site in the leaf is tagged "quoted (...)"
      rather than "verbatim" (PR #860 audit finding W6).

NON-GATING and NOT wired into `make verify`: this verifies one leaf, and the
shared gating surface is not this lane's to extend. Re-run by hand:

    python3 manuscript/ave-kb/tools/archival/verify-wall-taxonomy-anchors.py

Exit 0 = all checks pass; exit 1 = at least one FAIL.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from dataclasses import dataclass, field

REPO = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"],
    capture_output=True, text=True, check=True,
).stdout.strip()

LEAF = "manuscript/ave-kb/common/wall-taxonomy.md"
LEAF_DIR = os.path.dirname(LEAF)

# --------------------------------------------------------------------------
# file access (worktree for on-main paths, `git show` for branch-scoped refs)
# --------------------------------------------------------------------------

_CACHE: dict[tuple[str, str | None], list[str] | None] = {}


def lines_of(path: str, ref: str | None = None) -> list[str] | None:
    key = (path, ref)
    if key in _CACHE:
        return _CACHE[key]
    if ref is None:
        full = os.path.join(REPO, path)
        if not os.path.isfile(full):
            _CACHE[key] = None
            return None
        with open(full, encoding="utf-8") as fh:
            out = fh.read().split("\n")
    else:
        proc = subprocess.run(
            ["git", "show", f"{ref}:{path}"],
            cwd=REPO, capture_output=True, text=True,
        )
        out = proc.stdout.split("\n") if proc.returncode == 0 else None
    _CACHE[key] = out
    return out


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


# ==========================================================================
# PASS A -- anchor enumeration + existence
# ==========================================================================
#
# EXTRACTION RULE (stated so the count is reproducible; a count without a
# stated rule and a published list is not auditable):
#
#   (1) MACHINE-EXTRACTED: a markdown link whose target is a repo path with a
#       recognised extension, immediately followed by a line group --
#           [text](path.ext):NN
#           [text](path.ext):NN,:MM,:PP        (comma-chained, no gap)
#           [text](path.ext):NN-MM  /  :NN--MM (range; en-dash or hyphen)
#       A range `:NN-MM` contributes BOTH endpoints as anchors.
#   (2) DECLARED SUPPLEMENT: anchors the leaf writes with an IMPLICIT file --
#       a bare `:NN` continuing a link earlier in the same sentence, or a
#       `:NN` inside a quoted excerpt. These cannot be machine-attributed to a
#       file, so they are declared here by hand and then machine-CHECKED like
#       every other anchor.
#
# An "anchor" for counting purposes = one distinct (path, line) pair.

TARGET_EXTS = "md|py|tex|json|yaml|yml|txt"

LINK_RE = re.compile(
    r"\]\((?P<path>[^)\s]+?\.(?:" + TARGET_EXTS + r"))\)"
    r"(?P<lines>(?::\d+(?:[-–]\d+)?)(?:,\s*:\d+(?:[-–]\d+)?)*)"
)

LINE_RE = re.compile(r":(\d+)(?:[-–](\d+))?")

# (path-as-written-in-leaf, line, why) -- anchors with an implicit file.
SUPPLEMENT: list[tuple[str, int, str]] = [
    ("../vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md", 37,
     "row 1: ', :37 (the falsifiability line)' continues the :33 link across a ')'"),
    ("../vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md", 48,
     "row 1: ', :48-54 (the three-channel table)' continues the :51 link"),
    ("../vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md", 54,
     "row 1: range endpoint of ':48-54'"),
    ("../vol3/claim-quality.md", 1118,
     "row 1: ', :1097 (the caveat)' continues the :1088 link"),
    ("../vol3/claim-quality.md", 1130,
     "row 1: ', :1109 (solidity ...)' continues the :1088 link"),
    ("../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md", 58,
     "row 3: ', :58 ($r_3$; ...)' continues the :60 link"),
    ("../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md", 41,
     "row 6: ', **:41**' continues the :39 link (anchor ADDED by audit W3)"),
    ("../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md", 43,
     "row 6: ', :43-:47 (the Yukawa Resultbox)' continues the :39 link"),
    ("../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md", 46,
     "row 6: 'the $e^{-r/l_c}/r$ form is on **:46**'"),
    ("../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md", 47,
     "row 6: range endpoint of ':43-:47'"),
    ("../../../src/ave/core/constants.py", 337,
     "row 6 / flag 2: range endpoint of ':331-337'"),
    ("../../../research/2026-07-31_qlaw-framing-challenge_walk.md", 898,
     "row 8: ', :898' continues the :893 link"),
    ("../../../research/2026-07-31_qlaw-framing-challenge_walk.md", 973,
     "row 8: ', :973' continues the :893 link"),
    ("../../../research/2026-07-31_qlaw-framing-challenge_walk.md", 1334,
     "row 8: ', :1334' continues the :893 link"),
    ("../../../research/2026-07-31_qlaw-framing-challenge_walk.md", 5,
     "row 8 + Sec 8.2: '(`:5`)' -- implicit-file bare anchor"),
    ("../../../research/2026-07-31_qlaw-framing-challenge_walk.md", 16,
     "row 8 + Sec 8.2: '(**`:16`**)' -- implicit-file bare anchor (B3 fix of :15)"),
    ("../../../research/2026-07-31_qlaw-framing-challenge_walk.md", 15,
     "row 8 + Sec 8.2: ':15 is the NOT-a-pre-registration bullet' -- cited to show what :15 IS"),
    ("envelope-anatomy.md", 40,
     "Sec 3.1: 'that leaf already states ... -- `:40`, verbatim' -- implicit-file bare anchor"),
    ("../vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md", 39,
     "Sec 2: 'Written out for the bulk channel at [...]:39' (machine-caught; listed for completeness)"),
    ("boundary-observables-m-q-j.md", 57,
     "Sec 2.2 + See-also: ':57'-:63' range start"),
    ("boundary-observables-m-q-j.md", 63,
     "Sec 2.2 + See-also: ':57'-:63' range end"),
    ("../vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md", 59,
     "row 5: ':11,:59' comma-chain (machine-caught; listed for completeness)"),
    ("../../../src/ave/core/constants.py", 496,
     "row-3 precision note: 'constants.py:496' for V_snap"),
    ("../vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md", 0,
     "Sec 4: cited WITHOUT a line (verdict leaf, whole-file pointer) -- line 0 = file-existence check only"),
    ("dual-reactance-storage-taxonomy.md", 0,
     "Sec 2 + Sec 8.2: cited WITHOUT a line (section pointer) -- line 0 = file-existence check only"),
]


@dataclass
class AnchorResult:
    path: str
    line: int
    resolved: str | None
    ok: bool
    note: str
    source: str  # "machine" | "declared"


def resolve(path_as_written: str) -> str | None:
    for base in (LEAF_DIR, ""):
        cand = os.path.normpath(os.path.join(base, path_as_written))
        if os.path.isfile(os.path.join(REPO, cand)):
            return cand
    return None


def pass_a(leaf_text: str) -> tuple[list[AnchorResult], int]:
    seen: dict[tuple[str, int], AnchorResult] = {}

    def add(path_as_written: str, line: int, source: str, note: str = "") -> None:
        resolved = resolve(path_as_written)
        key = (resolved or path_as_written, line)
        if key in seen:
            return
        if resolved is None:
            seen[key] = AnchorResult(path_as_written, line, None, False,
                                     "UNRESOLVED path", source)
            return
        if line == 0:
            seen[key] = AnchorResult(path_as_written, line, resolved, True,
                                     "file-existence only (no line cited)", source)
            return
        body = lines_of(resolved) or []
        ok = 1 <= line <= len(body)
        seen[key] = AnchorResult(
            path_as_written, line, resolved, ok,
            note or ("line exists" if ok else f"line {line} > EOF ({len(body)})"),
            source,
        )

    for m in LINK_RE.finditer(leaf_text):
        for lm in LINE_RE.finditer(m.group("lines")):
            add(m.group("path"), int(lm.group(1)), "machine")
            if lm.group(2):
                add(m.group("path"), int(lm.group(2)), "machine")

    for path_as_written, line, why in SUPPLEMENT:
        add(path_as_written, line, "declared", why)

    results = sorted(seen.values(), key=lambda r: (r.resolved or r.path, r.line))
    return results, sum(1 for r in results if not r.ok)


# ==========================================================================
# PASS B -- QUOTE-AT-LINE manifest
# ==========================================================================
#
# One entry per excerpt the leaf reproduces from another file.
#   source     -- the SOURCE-side text, asserted to occur AT `line` of `target`
#   leaf_probe -- a distinctive fragment of the LEAF's rendering, asserted to
#                 occur in the leaf (ties the manifest to the text)
#   delta      -- "EXACT" when the leaf reproduces `source` byte-for-byte
#                 inside its verbatim tag; otherwise the named alteration.
#                 Every non-EXACT site carries a "quoted (...)" tag in the
#                 leaf rather than a bare "verbatim" (PR #860 audit, W6).

@dataclass
class Quote:
    qid: str
    target: str
    line: int
    source: str
    leaf_probe: str
    delta: str
    ref: str | None = None
    span: int = 0  # extra lines to join beyond `line` (range cites)
    result: str = field(default="", init=False)


KB = "manuscript/ave-kb/"

QUOTES: list[Quote] = [
    Quote("Q01", KB + "common/boundary-observables-m-q-j.md", 63,
          r'''do not read "same $\Gamma=-1$ saturation surface" as "same boundary-setting mechanism."''',
          r"""as 'same boundary-setting mechanism.'""",
          "ALTERED -- quote-mark swap (double->single) + spacing inside $\\Gamma=-1$"),

    Quote("Q02", KB + "common/boundary-observables-m-q-j.md", 63,
          r"""are the **same observability object** ($\mathcal{M},\mathcal{Q},\mathcal{J}$) sitting on **different boundary registers**""",
          r"""sitting on **different boundary registers**""",
          "EXACT"),

    Quote("Q03", KB + "common/envelope-anatomy.md", 32,
          r"""total internal reflection ($\lvert\Gamma\rvert = 1$) and hiding the interior""",
          r"""total internal reflection … hiding the interior""",
          "ALTERED -- ellipsis elides '($\\lvert\\Gamma\\rvert = 1$) and'"),

    Quote("Q04", KB + "common/envelope-anatomy.md", 32,
          r"""(magnetic-branch $\mu_{eff}\to 0$ short vs the electric-branch $\varepsilon_{eff}\to 0$ open)""",
          r"""vs the electric-branch $\varepsilon_{eff}\to 0$ open)""",
          "EXACT"),

    Quote("Q05", KB + "common/envelope-anatomy.md", 40,
          r"""The reflection off the knee is **small** ($\lvert\Gamma\rvert \ll 1$, the near-matched sub-yield regime — distinct from the wall's $\lvert\Gamma\rvert = 1$).""",
          r"""the near-matched sub-yield regime — distinct from the wall's""",
          "EXACT"),

    Quote("Q06", KB + "common/envelope-anatomy.md", 101,
          r"""**ideal saturation dissipates nothing** — it is a *lossless refusal*, Axiom-3-compatible""",
          r"""it is a **lossless refusal**, Axiom-3-compatible""",
          "ALTERED -- emphasis re-scoped: source italicises 'lossless refusal', leaf bolds it"),

    Quote("Q07", KB + "common/envelope-anatomy.md", 101,
          r"""a **standing open fork, not a contradiction introduced by this walk-record** — Grant leans reversible; the fork stays open""",
          r"""a **standing open fork**, not a contradiction introduced by this walk-record""",
          "ALTERED -- emphasis re-scoped: source bolds the whole span, leaf bolds only 'standing open fork'"),

    Quote("Q08", KB + "common/envelope-anatomy.md", 109,
          r"""**one cell's rest energy = the quantum of rupture** — which is *why* the products are particles""",
          r"""one cell's rest energy … which is **why** the products are particles""",
          "ALTERED -- bold dropped from first fragment; `*why*` italic -> `**why**` bold; ellipsis elides '= the quantum of rupture --'"),

    Quote("Q09", KB + "common/axiom-register.md", 176,
          r"""Axiom 3's lossless-reactive extremal content is the primitive that MAKES the bond-LC L2 energy invariant exact""",
          r"""is the primitive that MAKES the bond-LC L2 energy invariant exact""",
          "EXACT (truncated at a sentence-internal dash; no interior elision)"),

    Quote("Q10", KB + "common/operators.md", 43,
          r"""$\Gamma = (Z_2 - Z_1)/(Z_2 + Z_1)$""",
          r"""$\Gamma = (Z_2 - Z_1)/(Z_2 + Z_1)$""",
          "EXACT (formula only; the surrounding prose is the leaf's, untagged)"),

    Quote("Q11", KB + "vol1/operators-and-regimes/ch7-regime-map/four-regimes.md", 60,
          r"""from sub-threshold trapping a wave reflects inward at $\Gamma = -1$ and forms a stable standing wave (matter); a super-threshold mode driven through the same boundary ruptures the existing topology. Same Axiom 4 saturation, two operational faces.""",
          r"""Same Axiom 4 saturation, two operational faces.""",
          "EXACT"),

    Quote("Q12", KB + "vol1/operators-and-regimes/ch7-regime-map/four-regimes.md", 58,
          r"""$V_R = V_{BR}$, $M \to \infty$""",
          r"""$V_R = V_{BR}$, $M\to\infty$""",
          "ALTERED -- spacing inside the math span ('M \\to \\infty' -> 'M\\to\\infty')"),

    Quote("Q13", KB + "vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md", 54,
          r"""**BH-echo yes/no is therefore a channel question.**""",
          r"""**BH-echo yes/no is therefore a channel question.**""",
          "EXACT"),

    Quote("Q14", KB + "vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md", 54,
          r'''Statements that "the horizon is a perfect absorber" (EM) and "the horizon reflects shear/GW modes" are **not contradictory** once channel subscripts are explicit.''',
          r"""are **not contradictory** once channel subscripts are explicit.""",
          "ALTERED -- quote-mark swap (double->single) + ellipsis elides two intervening sentences"),

    Quote("Q15", KB + "vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md", 124,
          r"""$\Delta n = 0$ under static B (μ = ideal relativistic inductor, circulation-keyed; static B has no $dB/dt$ → $S_\mu=1$""",
          r"""circulation-keyed; static B has no $dB/dt \to S_\mu = 1$)""",
          "ALTERED -- TeX re-render (bare 'μ' -> '$\\mu$'; two math spans merged; spacing) AND the parenthetical is CLOSED EARLY, dropping the source's trailing '-- [not \"lattice symmetry\"]' cross-link"),

    Quote("Q16", KB + "common/vocabulary-register.md", 404,
          r"""a bound soliton's boundary region is **THREE physically-distinct radial surfaces** on $S(A(r))$: **(i) the wall** (fully-yielded $S\to0$, $\lvert\Gamma\rvert=1$ mirror;""",
          r"""$\lvert\Gamma\rvert=1$ mirror …); **(ii) the balance shell** …;""",
          "ALTERED -- PARENTHETICAL CLOSED EARLY: the leaf writes 'mirror …);' where the source's '(i)' parenthetical continues with three further clauses before its ')'"),

    Quote("Q17", KB + "common/vocabulary-register.md", 404,
          r"""**(iii) the knee / dress edge** (the $\Delta S=\alpha$ proportional limit, $A^2=2\alpha$).""",
          r"""**(iii) the knee / dress edge** (the $\Delta S=\alpha$ proportional limit, $A^2=2\alpha$).""",
          "EXACT"),

    Quote("Q18", KB + "common/translation-tables/translation-circuit.md", 134,
          r"""**Distributed transmission-line input impedance at Hubble-horizon termination**""",
          r"""Machian $G$ $\leftrightarrow$ **Distributed transmission-line input impedance at Hubble-horizon termination**""",
          "ALTERED -- TABLE ROW RENDERED AS PROSE: '$\\leftrightarrow$' INSERTED for the column break, bold dropped from 'Machian $G$', terminal '.' added"),

    Quote("Q19", KB + "vol2/nuclear-field/ch12-millennium-prizes/yang-mills-steps1-2.md", 30,
          r"""a hard ultraviolet cutoff at $\omega_\mathrm{max} = 2c/\ell_\mathrm{node}$. No mode can oscillate faster, eliminating UV divergence.""",
          r"""a hard ultraviolet cutoff … **No mode can oscillate faster, eliminating UV divergence**.""",
          "ALTERED -- emphasis ADDED (source sentence is plain; leaf bolds it) + ellipsis elides 'at $\\omega_\\mathrm{max} = 2c/\\ell_\\mathrm{node}$.'"),

    Quote("Q20", KB + "vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md", 57,
          r"""Any physical excitation operating *below* a medium's natural cutoff frequency becomes an **Evanescent Wave**.""",
          r"""Any physical excitation operating **below** a medium's natural cutoff frequency becomes an **Evanescent Wave**""",
          "ALTERED -- emphasis re-scoped: source italicises 'below', leaf bolds it (declared in-row)"),

    Quote("Q21", KB + "vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md", 55,
          r"""**Characteristic Length Scale** ($l_c = \sqrt{\gamma_c/G_{vac}}$)""",
          r"""$\ell_c = \sqrt{\gamma_c/G_{vac}}$""",
          "ALTERED -- symbol re-render 'l_c' -> '\\ell_c' (leaf's table symbol; not inside a verbatim tag)"),

    Quote("Q22", KB + "vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md", 62,
          r"""V_{weak}(r) \propto \frac{e^{-r/l_c}}{r}""",
          r"""$V_{weak}(r) \propto e^{-r/l_c}/r$""",
          "ALTERED -- TeX re-render: '\\frac{a}{b}' -> 'a/b' (inline form; not inside a verbatim tag)"),

    Quote("Q23", "src/ave/core/constants.py", 331,
          r"""DISAMBIGUATION (two-objects-one-symbol — flag-don't-fix): this ELL_C""",
          r"""⚠ DISAMBIGUATION (two-objects-one-symbol — flag-don't-fix): this `ELL_C`""",
          "ALTERED -- MARKUP NORMALIZED: python comment rendered as markdown (backticks + bold added around ELL_C / l_c / STRUCTURE); wording unchanged"),

    Quote("Q24", "src/ave/core/constants.py", 334,
          r"""vol9 ch9/ch10 + gauge-boson-masses.md:39. Same symbol and same formula STRUCTURE""",
          r"""Same symbol and same formula **STRUCTURE**""",
          "ALTERED -- MARKUP NORMALIZED (see Q23)"),

    Quote("Q25", "src/ave/core/constants.py", 336,
          r"""Surfaced for auditor adjudication""",
          r"""**Surfaced for auditor adjudication**""",
          "ALTERED -- MARKUP NORMALIZED (bold added) + ellipsis elides the vol9 footnote parenthetical"),

    Quote("Q26", "src/ave/core/constants.py", 337,
          r"""not silently merged.""",
          r"""not silently merged.""",
          "EXACT"),

    Quote("Q27", "src/ave/core/constants.py", 338,
          r"""ELL_C: float = np.sqrt(6.0) * L_NODE""",
          r"""$\sqrt6\,\ell_{node} \approx 9.46\times10^{-13}$ m""",
          "RESTATED (not tagged verbatim) -- the leaf gives the VALUE; the anchor holds the definition"),

    Quote("Q28", KB + "vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md", 47,
          r"""**the substrate primitive $\gamma_c$ underlies both the weak force range AND the B-mode mass-gap that freezes substrate magnetic-modulus response to thermal-photon-bath loading**""",
          r"""underlies **both** the weak force range **AND** the B-mode mass-gap""",
          "ALTERED -- emphasis re-scoped: source bolds the whole span, leaf bolds only 'both' and 'AND'"),

    Quote("Q29", KB + "vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md", 47,
          r"""simultaneously falsifies the δ_strain mechanism.""",
          r"""**simultaneously falsifies** the $\delta_{strain}$ mechanism.""",
          "ALTERED -- emphasis ADDED + TeX re-render ('δ_strain' -> '$\\delta_{strain}$') + ellipsis elides the kill-switch parenthetical"),

    Quote("Q30", KB + "common/program-arc-map.md", 126,
          r"""PR #260; `audit/2026-06-15_wall-branch-fork`""",
          r"""PR #260; `audit/2026-06-15_wall-branch-fork`""",
          "EXACT"),

    Quote("Q31", "research/2026-08-02_coldq-pole-derivation_result.md", 208,
          r"""The `A = 1` point is handled as a regular singular point of the ODE whose indicial structure selects the traction-free branch — not by a floor on `S`.""",
          r"""handled as a **regular singular point** of the ODE""",
          "ALTERED -- emphasis re-scoped: source bolds the whole sentence, leaf bolds only 'regular singular point'"),

    Quote("Q32", "research/2026-08-03_coldq-pole-v2.1_result.md", 17,
          r"""**Certification: `SOLVER-NOT-CERTIFIED`. Frozen precedence therefore fires `BIN-F-SOLVER`, and NO physics bin is adjudicated.**""",
          r"""and NO physics bin is adjudicated.**""",
          "EXACT"),

    Quote("Q33", "research/2026-07-31_qlaw-framing-challenge_walk.md", 5,
          r"""🟡 WALK MATERIAL — this document exists to be walked with Grant, not to be believed""",
          r"""🟡 WALK MATERIAL — this document exists to be walked with Grant, not to be believed""",
          "EXACT"),

    Quote("Q34", "research/2026-07-31_qlaw-framing-challenge_walk.md", 16,
          r"""**NOT a claim.** No claim-id is minted""",
          r"""**NOT a claim.** No claim-id is minted""",
          "EXACT (anchor corrected :15 -> :16 by audit finding B3)"),

    Quote("Q35", KB + "vol2/particle-physics/ch01-topological-matter/index.md", 44,
          r"""**Grant's 2026-08-03 walk ratified a BIAS (multiplicative) composition law**, under which **the carve INVERTS**""",
          r"""under which **the carve INVERTS**""",
          "EXACT"),

    Quote("Q36", KB + "vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md", 37,
          r"""a **falsifiable prediction** for any high-gravity observational test""",
          r"""a **falsifiable prediction** for any high-gravity observational test""",
          "EXACT (emphasis is the SOURCE's own bold)"),

    Quote("Q37", KB + "vol3/claim-quality.md", 1118,
          r"""EHT shadow / photon-ring radius do NOT discriminate $r_{\text{sat}}$ from $r_s$ (prior EHT-falsifier overclaim retracted 2026-05-16 per Grant audit).""",
          r"""(prior EHT-falsifier overclaim retracted 2026-05-16 per Grant audit).""",
          "EXACT"),

    Quote("Q38", KB + "vol3/claim-quality.md", 1130,
          r"""solidity: 0.55 (use as input only, don't build deeper)""",
          r"""use as input only, don't build deeper""",
          "EXACT"),

    Quote("Q39", KB + "common/port-register.md", 47,
          r"""arccos top $\pi\sqrt3\,\omega_C \approx 5.44\,\omega_C$""",
          r"""arccos top $\pi\sqrt3\,\omega_C \approx 5.44\,\omega_C$""",
          "EXACT"),

    Quote("Q40", KB + "common/port-register.md", 48,
          r"""gapless acoustic; edge $2c/\ell_{node}$""",
          r"""shear *"edge $2c/\ell_{node}$"*""",
          "EXACT (fragment)"),

    Quote("Q41", KB + "common/port-register.md", 49,
          r"""gapless acoustic; edge $2\sqrt2\,c/\ell_{node}$""",
          r"""bulk *"edge $2\sqrt2\,c/\ell_{node}$"*""",
          "EXACT (fragment)"),

    Quote("Q42", KB + "common/port-register.md", 50,
          r"""**GAPPED**: $\omega^2 = c_\kappa^2 k^2 + m_\omega^2$; edge $2\sqrt2\,c/\ell_{node}$""",
          r"""**GAPPED** … edge $2\sqrt2\,c/\ell_{node}$""",
          "ALTERED -- ellipsis elides ': $\\omega^2 = c_\\kappa^2 k^2 + m_\\omega^2$;'"),

    Quote("Q43", KB + "common/port-register.md", 73,
          r"""**Casimir below-cutoff** (closed by band position)""",
          r"""*"Casimir below-cutoff"* (bold dropped)""",
          "ALTERED -- bold dropped from 'Casimir below-cutoff' (declared in-row)"),

    Quote("Q44", KB + "vol1/dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md", 19,
          r"""the saturating LC reaches $Z \to 0$, $\Gamma \to -1$""",
          r"""the saturating LC reaches $Z \to 0$, $\Gamma \to -1$""",
          "EXACT"),

    Quote("Q45", KB + "vol3/gravity/ch01-gravity-yield/gravitational-coupling-constant.md", 10,
          r"""$\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$""",
          r"""$\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$""",
          "EXACT"),

    Quote("Q46", "src/ave/core/constants.py", 505,
          r"""V_YIELD: float = np.sqrt(ALPHA) * V_SNAP""",
          r"""$V_{yield} = \sqrt{\alpha}\,V_{snap} \approx 43.65$ kV""",
          "RESTATED (not tagged verbatim) -- the leaf gives the value; the anchor holds the definition"),

    Quote("Q47", "src/ave/core/constants.py", 496,
          r"""V_SNAP: float = (M_E * C_0**2) / e_charge""",
          r"""$V_{snap} = m_ec^2/e \approx 511$ kV""",
          "RESTATED (not tagged verbatim) -- the leaf gives the value; the anchor holds the definition"),

    Quote("Q48", KB + "vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md", 59,
          r"""$$\omega^2 = c^2 k^2 + \frac{4 G_c}{I_\omega}$$""",
          r"""$\omega^2 = c^2k^2 + 4G_c/I_\omega$""",
          "ALTERED -- TeX re-render ('\\frac{4 G_c}{I_\\omega}' -> '4G_c/I_\\omega'; display -> inline); not inside a verbatim tag"),

    # --- coldQ v2.4 receipts. RE-POINTED TO main 2026-08-05 (ringdown wave): these were
    # pinned @origin/research/coldq-pole-v2p3 while that lane was unmerged. PR #861 merged it,
    # so the branch ref made the checker report "target unreadable" on content that is now on
    # main. Line indices re-derived on main by content match, not carried over. ---
    Quote("Q49", "research/2026-08-03_coldq-pole-v2.4-root_result.md", 15,
          r"""**Certification: `ROOT-CERTIFIED`.** All twelve gates PASS; all twelve fireability self-tests FIRE. **The frozen precedence therefore reaches the physics bins for the first time in this arc, and they are adjudicated.**""",
          r"""The frozen precedence therefore reaches the physics bins for the first time in this arc, and they are adjudicated.**""",
          "EXACT"),

    Quote("Q50", "research/2026-08-03_coldq-pole-v2.4-root_result.md", 262,
          r"""A `ROOT-CERTIFIED` verdict is a statement about an INSTRUMENT, not about the world.""",
          r"""a statement about an INSTRUMENT, not about the world""",
          "ALTERED -- source bolds the sentence; leaf quotes it inside its own emphasis run"),

    Quote("Q51", "research/2026-08-03_coldq-pole-v2.4-root_result.md", 262,
          r"""**Classification: INSTRUMENT-CONSISTENCY. It is not an emergence claim of any class and it cannot become one.**""",
          r"""**Classification: INSTRUMENT-CONSISTENCY. It is not an emergence claim of any class and it cannot become one.**""",
          "EXACT"),
]


def pass_b() -> tuple[list[Quote], int]:
    fails = 0
    leaf_body = "\n".join(lines_of(LEAF) or [])
    leaf_n = norm(leaf_body)
    for q in QUOTES:
        body = lines_of(q.target, q.ref)
        if body is None:
            q.result = "FAIL (target unreadable)"
            fails += 1
            continue
        if not (1 <= q.line <= len(body)):
            q.result = f"FAIL (line {q.line} > EOF {len(body)})"
            fails += 1
            continue
        window = " ".join(body[q.line - 1: q.line + q.span])
        at_line = norm(q.source) in norm(window)
        in_leaf = norm(q.leaf_probe) in leaf_n
        if at_line and in_leaf:
            q.result = "PASS"
        else:
            bits = []
            if not at_line:
                elsewhere = any(norm(q.source) in norm(ln) for ln in body)
                bits.append("source NOT at cited line"
                            + (" -- FOUND ELSEWHERE IN FILE (stale anchor)" if elsewhere
                               else " -- ABSENT FROM FILE"))
            if not in_leaf:
                bits.append("leaf_probe not found in leaf (manifest drift)")
            q.result = "FAIL (" + "; ".join(bits) + ")"
            fails += 1
    return QUOTES, fails


# ==========================================================================
# main
# ==========================================================================

def emit_markdown(anchors: list[AnchorResult], quotes: list[Quote]) -> None:
    """Emit the exact §8.3 / §8.4 tables the leaf publishes, so the published
    list is generated from the checked data rather than transcribed by hand."""
    by_target: dict[str, list[AnchorResult]] = {}
    for r in anchors:
        by_target.setdefault(r.resolved or r.path, []).append(r)

    print("<!-- BEGIN generated: verify-wall-taxonomy-anchors.py --markdown -->")
    print()
    print("| # | Target file | Lines cited | Result |")
    print("|---|---|---|---|")
    for i, (tgt, rs) in enumerate(sorted(by_target.items()), 1):
        lines = ", ".join(
            ("(file only)" if r.line == 0 else f"`:{r.line}`")
            + ("" if r.source == "machine" else "†")
            for r in sorted(rs, key=lambda x: x.line)
        )
        ok = all(r.ok for r in rs)
        print(f"| {i} | `{tgt}` | {lines} | **{len(rs)}/{len(rs)} "
              f"{'PASS' if ok else 'FAIL'}** |")
    machine = sum(1 for r in anchors if r.source == "machine")
    print(f"\n**TOTAL: {len(anchors)} distinct `(file, line)` anchors across "
          f"{len(by_target)} files — {len(anchors)} PASS, "
          f"{sum(1 for r in anchors if not r.ok)} FAIL.** "
          f"({machine} machine-extracted, {len(anchors) - machine} declared-supplement, "
          "marked †.)")
    print()
    print("| ID | Anchor | Δ vs source | Result |")
    print("|---|---|---|---|")
    for q in quotes:
        loc = f"`{q.target}:{q.line}`" + (f" @`{q.ref}`" if q.ref else "")
        d = q.delta.replace("|", "\\|")
        print(f"| {q.qid} | {loc} | {d} | **{q.result}** |")
    exact = sum(1 for q in quotes if q.delta.startswith("EXACT"))
    altered = sum(1 for q in quotes if q.delta.startswith("ALTERED"))
    restated = sum(1 for q in quotes if q.delta.startswith("RESTATED"))
    print(f"\n**TOTAL: {len(quotes)} quoted excerpts — {len(quotes)} PASS, "
          f"{sum(1 for q in quotes if q.result != 'PASS')} FAIL. "
          f"Δ classes: EXACT {exact} · ALTERED {altered} · RESTATED {restated}.**")
    print()
    print("<!-- END generated -->")


def main() -> int:
    leaf_lines = lines_of(LEAF)
    if leaf_lines is None:
        print(f"FATAL: cannot read {LEAF}")
        return 1
    leaf_text = "\n".join(leaf_lines)

    anchors, a_fail = pass_a(leaf_text)
    quotes, b_fail = pass_b()

    if "--markdown" in sys.argv:
        emit_markdown(anchors, quotes)
        return 0 if (a_fail == 0 and b_fail == 0) else 1

    print("=" * 78)
    print("PASS A -- ANCHOR ENUMERATION + EXISTENCE")
    print("=" * 78)
    print(f"{'#':>3}  {'src':<9} {'result':<6}  target:line")
    for i, r in enumerate(anchors, 1):
        tgt = f"{r.resolved or r.path}"
        loc = tgt if r.line == 0 else f"{tgt}:{r.line}"
        print(f"{i:>3}  {r.source:<9} {'PASS' if r.ok else 'FAIL':<6}  {loc}"
              + ("" if r.ok else f"   <-- {r.note}"))
    machine = sum(1 for r in anchors if r.source == "machine")
    declared = len(anchors) - machine
    print(f"\nPASS A TOTAL: {len(anchors)} distinct (path, line) anchors "
          f"[{machine} machine-extracted + {declared} declared-supplement]; "
          f"{len(anchors) - a_fail} PASS, {a_fail} FAIL")

    print()
    print("=" * 78)
    print("PASS B -- QUOTE-AT-LINE (does the quoted excerpt occur AT the cited line?)")
    print("=" * 78)
    for q in quotes:
        loc = f"{q.target}:{q.line}" + (f"  @{q.ref}" if q.ref else "")
        print(f"{q.qid}  {q.result:<6}  {loc}")
        print(f"       delta: {q.delta}")
    exact = sum(1 for q in QUOTES if q.delta.startswith("EXACT"))
    altered = sum(1 for q in QUOTES if q.delta.startswith("ALTERED"))
    restated = sum(1 for q in QUOTES if q.delta.startswith("RESTATED"))
    print(f"\nPASS B TOTAL: {len(quotes)} quoted excerpts; "
          f"{len(quotes) - b_fail} PASS, {b_fail} FAIL")
    print(f"  delta classes: EXACT {exact} | ALTERED {altered} | RESTATED {restated}")

    print()
    print("=" * 78)
    verdict = "ALL CHECKS PASS" if (a_fail == 0 and b_fail == 0) else "FAILURES PRESENT"
    print(f"VERDICT: {verdict}  (anchors {a_fail} FAIL, quotes {b_fail} FAIL)")
    print("=" * 78)
    return 0 if (a_fail == 0 and b_fail == 0) else 1


if __name__ == "__main__":
    sys.exit(main())
