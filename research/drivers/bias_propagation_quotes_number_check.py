#!/usr/bin/env python3
"""Quote gate for the bias propagation theorem lane (R49b/R50).

FROZEN CRITERION being scored, verbatim from
research/2026-08-10_bias-propagation_prereg-FROZEN.md:143 (G-QUOTE):

    "Every ruled/frozen quote byte-checks, two engines, with a committed quote
     gate + `--mutation-receipt`."

This IS that committed gate. It exists because this lane's two withdrawn
findings were BOTH citation failures — one quote fabricated by attribution, one
citing a stale blob — so the gate is scored against the frozen criterion only
once the machinery the criterion names is in the tree.

Two engines per quote:
  (1) subprocess BSD `grep -F` fixed-string search over the bytes;
  (2) Python `str.find` over the same bytes.
Both must find it; disagreement is itself a failure.

Two source classes, because this lane's load-bearing axiom text lives on a
different branch than the lane:
  IN-TREE   — paths resolved against the repo root this script lives in, so the
              gate checks THIS tree's state.
  AT-REV    — blobs retrieved with `git show <rev>:<path>`. The rev is pinned in
              the quote row, which is exactly the defence against the stale-blob
              failure mode: a moving branch name cannot silently re-point.

Supports --mutation-receipt (corrupts one expected string in memory; the gate
must catch it). Auto-discovered by the make-verify umbrella.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
MUTATE = "--mutation-receipt" in sys.argv

# The doc-lane commit the lane's Axiom-5 text is quoted from. PINNED, not a
# branch name — the "Axiom-5 text ambiguity" phantom was a stale-blob read, and
# a pinned rev is what makes that failure mode impossible rather than unlikely.
AX5_REV = "7adbc187"
AX5_PATH = "manuscript/common_equations/eq_axiom_5.tex"

# (rev-or-None, path, expected fixed substring, what it is load-bearing FOR)
QUOTES = [
    # ---- Axiom 5, the target text (AT-REV, pinned) ----
    (AX5_REV, AX5_PATH,
     "Clause G's elliptic law is the \\emph{static abstraction of underived "
     "finite-speed bias dynamics}",
     "result HEADLINE + §1: the named-open (c1) debt this lane confirms"),
    (AX5_REV, AX5_PATH,
     "the finite propagation speed of the bias is \\emph{owed, not held}",
     "result §3(a): why the D3 null is conditional, not receipted"),
    (AX5_REV, AX5_PATH,
     "\\textbf{The $(u,\\pi)$ no-signalling theorem does NOT cover the bias read}",
     "result §1.4: the object split that forbids importing the (u,pi) receipt"),
    (AX5_REV, AX5_PATH,
     "A sourceless bound response (no net A1 flux without matter)",
     "result §1.4 item 3: the horn the axiom forbids"),
    (AX5_REV, AX5_PATH,
     "any new longitudinal stiffness or wave (it adds no kinetic or potential "
     "term on the flat direction, so the pole-absence results survive it untouched)",
     "prereg §6 F1: the arc-level kill's own text"),
    (AX5_REV, AX5_PATH,
     "= 4\\pi\\,T_{00}",
     "result §2.0 surface-note (F5c): the ratified clause-G source convention"),
    # ---- the sqrt(S) symbol collision (F1) ----
    (None, "manuscript/ave-kb/vol3/gravity/ch02-general-relativity/"
           "saturating-modulus-and-backreaction.md",
     "the local clock $\\omega_{\\text{local}}=\\omega\\sqrt{S}$",
     "result §2.2 (F1): an S^(1/2) KERNEL clock in the identical E=hbar*omega "
     "construction the widened lemma weak-field-falsifies"),
    (None, "manuscript/ave-kb/vol3/gravity/ch02-general-relativity/"
           "saturating-modulus-and-backreaction.md",
     "AVE's $\\sqrt{S}$",
     "result §2.2 (F1): the Stage-4 peel target's own symbol"),
    (None, "manuscript/ave-kb/vol3/gravity/ch02-general-relativity/"
           "saturating-modulus-and-backreaction.md",
     "can peel from GR's $\\sqrt{1-r_s/r}$",
     "result §2.2 (F1): the Stage-4 peel target rests on the killed reading"),
    (None, "manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/"
           "temporal-spatial-lattice-decomposition.md",
     "$\\sqrt{g_{00}} = \\sqrt{S} \\approx 1 - GM/rc^2$",
     "result §2.1/§2.2 (F1): the ESCAPING linear clock wearing the same symbol"),
    # ---- the eps_11 / A dialect collision (F6) ----
    (None, "manuscript/common_equations/eq_axiom_4.tex",
     "$r_s/r$ (gravitational metric strain)",
     "result §2.4 (F6): :10 names the gravitational strain as r_s/r"),
    (None, "manuscript/common_equations/eq_axiom_4.tex",
     "BH event horizon $\\varepsilon_{11}(r) = 1$ matches Schwarzschild "
     "$r_s = 2GM/c^2$ \\textbf{exactly}",
     "result §2.4 (F6): :24 writes eps_11 for that same quantity"),
    (None, "manuscript/common_equations/eq_axiom_4.tex",
     "Near a massive defect, $\\varepsilon_{11} \\to 1$",
     "result §2.4 (F6): :56 writes eps_11 for it again"),
    # ---- the canon bias profile + source convention ----
    (None, "manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/"
           "gordon-optical-metric.md",
     "\\epsilon_{11}(r) = \\frac{7GM}{c^{2}r}",
     "result §2.1: the frozen input profile"),
    (None, "manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/"
           "gordon-optical-metric.md",
     "4\\pi Mc^{2}\\delta^{3}(r)",
     "result §2.0 surface-note (F5c): the declared 4-pi source convention"),
    # ---- the banked pulsar comparator (F3 scope) ----
    (None, "manuscript/ave-kb/common/port-register.md",
     "excluded at 9–110σ Hulse-Taylor / 100–1400× the double-pulsar bound",
     "result §1.3 (F3): the BANKED exclusion range, 1e2-1e3 x, quadrupole at O(c)"),
    (None, "manuscript/ave-kb/common/port-register.md",
     "monopole + dipole killed by conservation, but the **quadrupole radiates**",
     "result §1.3 (F3): the multipole order the banked bound was computed for"),
    # ---- canon's observability rule (the F2 rescue that was tested) ----
    (None, "manuscript/ave-kb/CLAUDE.md",
     "only spatial gradients of $A$ across the substrate are physically observable",
     "result §1.2: the one available carrier rescue, tested and refused"),
    # ---- the walk seeds this lane adjudicates (UN-AUDITED INPUT) ----
    (None, "research/2026-08-06_rotation-substance-ontology_framing-note.md",
     "from ONE mechanism — the node clock riding the bias.",
     "result §2.3: the unification claim under adjudication"),
    (None, "research/2026-08-06_rotation-substance-ontology_framing-note.md",
     "resonance's total energy tracks the local clock linearly — underived",
     "result §2.4: counter-arm C7, LIVE"),
    (None, "research/2026-08-06_rotation-substance-ontology_framing-note.md",
     "unification is an ECHO until the force MAGNITUDE reproduces the canon chain",
     "result §2.3 (C9 refinement): the frozen check's own wording"),
    (None, "research/2026-08-06_rotation-substance-ontology_framing-note.md",
     "a trapped resonance saturates its nodes → the local\n  resonant frequency "
     "down-regulates",
     "result §2.2 (C9 refinement): the SATURATION KEYING the lemma kills"),
    # ---- the causality leg this lane's §1.4 item 3 bears on ----
    (None, "research/2026-08-10_bound-constitutive_result.md",
     "clause G makes the grade's GRADIENT local in the dress",
     "result §1.4 consequence: the corpus's only standing causality leg for the bias"),
    (None, "research/2026-08-10_bound-constitutive_result.md",
     "every observable grade reading is a local functional of the causal",
     "result §1.4 consequence: the second half of that leg"),
    (None, "research/2026-08-10_bound-constitutive_result.md",
     "the observable-grade branch lands CAUSAL-CONDITIONAL-ON-BC-SRC",
     "result §1.4 consequence: that lane's FORK-2 verdict, quoted in this lane's "
     "body -- registered 2026-08-11 after the delta re-verify found the span had "
     "been quoted without its verb"),
    # ---- the lane's own frozen prereg (criteria travel verbatim) ----
    (None, "research/2026-08-10_bias-propagation_prereg-FROZEN.md",
     "or any bin admitting a finite-ω longitudinal pole",
     "result §3 (F8d): the frozen F1 disjunct, which carries NO pole qualifier "
     "on the c_g != c arm"),
    (None, "research/2026-08-10_bias-propagation_prereg-FROZEN.md",
     "`SIGNATURE(observable + magnitude)` / `NULL-PEER-WITH-GR` / "
     "`UNCONSTRAINED-BY-RETRIEVAL`",
     "result §3 (F8d): D3's frozen grammar — the three labels BLOCKED-ON-D1 is not"),
    (None, "research/2026-08-10_bias-propagation_prereg-FROZEN.md",
     "Every ruled/frozen quote byte-checks, two engines, with a committed quote "
     "gate + `--mutation-receipt`.",
     "result §4 (F8a): the G-QUOTE criterion THIS gate is scored against"),
    (None, "research/2026-08-10_bias-propagation_prereg-FROZEN.md",
     "`A = 4.2461×10⁻⁶`",
     "result §2.1 (F9): the prereg's frozen pre-M_SUN-repair numeral"),
]


def fail(msg):
    print(f"BIAS-PROPAGATION QUOTE CHECK: FAIL — {msg}")
    sys.exit(1)


def _bytes_for(rev, relpath):
    """Return the file text, from the working tree or from a PINNED rev."""
    if rev is None:
        path = os.path.join(ROOT, relpath)
        if not os.path.exists(path):
            return None
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    out = subprocess.run(
        ["git", "-C", ROOT, "show", f"{rev}:{relpath}"],
        capture_output=True,
    )
    if out.returncode != 0:
        return None
    return out.stdout.decode("utf-8")


def main():
    quotes = list(QUOTES)
    if MUTATE:
        rev, path, q, why = quotes[0]
        quotes[0] = (rev, path, q.replace("static abstraction", "static idealisation"), why)

    bad = []
    for rev, relpath, expected, _why in quotes:
        label = relpath if rev is None else f"{rev}:{relpath}"
        text = _bytes_for(rev, relpath)
        if text is None:
            bad.append(f"{label}: SOURCE UNAVAILABLE")
            continue
        eng2 = expected in text                              # engine 2: python
        try:                                                 # engine 1: grep -F
            rc = subprocess.run(
                ["/usr/bin/grep", "-qF", expected],
                input=text.encode("utf-8"),
            ).returncode
            eng1 = rc == 0
        except OSError:
            eng1 = eng2  # grep unavailable: disclosed single-engine fallback
        if not (eng1 and eng2):
            bad.append(f"{label}: NOT FOUND (grep={eng1}, python={eng2}): {expected[:60]!r}")
        elif eng1 != eng2:
            bad.append(f"{label}: ENGINE DISAGREEMENT on {expected[:60]!r}")

    if MUTATE:
        if bad:
            print(f"BIAS-PROPAGATION QUOTE CHECK: mutation receipt FIRED — "
                  f"corruption caught: {bad[0][:110]}")
            sys.exit(0)
        fail("mutation receipt DID NOT FIRE — the gate is dead")
    if bad:
        fail("; ".join(bad))
    n_rev = sum(1 for rev, *_ in quotes if rev is not None)
    print(f"BIAS-PROPAGATION QUOTE CHECK: PASS — {len(quotes)} quotes two-engine "
          f"byte-verified ({n_rev} at pinned rev {AX5_REV}, "
          f"{len(quotes) - n_rev} in-tree)")
    sys.exit(0)


if __name__ == "__main__":
    main()
