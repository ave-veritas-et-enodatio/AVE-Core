#!/usr/bin/env python3
"""
Generate TikZ circuit schematics for heavy elements (S-32 through Fe-56).

Each circuit uses the AVE house figure style (WHITE print profile, Okabe-Ito
colourblind-safe palette; single source of truth src/ave/viz/README.md +
src/ave/viz/style.py):
- White background (no canvas fill)
- COLORS["ave"] alpha blocks
- COLORS["accent"] bus coupling lines
- COLORS["data"] (black) blocks for polar/halo/special nodes
- Black text, COLORS["muted"] legend frames

[2026-08-05 STATUS: SUPERSEDED-BUT-MAINTAINED. Every tracked circuit_*.tex in
 src/scripts/vol_6_periodic_table/figures/ -- including all six this script names
 (s32, ar40, ca40, ti48, cr52, fe56) -- carries the 21-line preamble emitted by
 generate_all_semiconductor_circuits.py, NOT the preamble below (verified by
 md5 of the first 21 lines against a sandbox run of both generators, 2026-08-05:
 19/19 match generate_all, 0/6 match this file). So this script is not the
 producer of any shipped figure. It is whitened here anyway so that it cannot
 re-introduce a dark canvas if anyone runs it.]

Geometries are taken directly from the semiconductor_binding_engine.py:
  S-32:  8α  Cube
  Ar-40: 10α Bicapped Square Antiprism
  Ca-40: 10α Bicapped Square Antiprism (isobar of Ar-40)
  Ti-48: 12α Cuboctahedron
  Cr-52: 13α Centered Icosahedron
  Fe-56: 14α FCC-14
"""

import os
import subprocess

# [2026-08-05 PATH DEFECT FIXED] Was ("..", "..", "periodic_table", "figures"), which
# resolves to src/scripts/periodic_table/figures -- a directory that does not exist. Paired
# with the os.makedirs(exist_ok=True) further down, a run silently created that stray
# directory and wrote there, so "regenerate" never touched the tracked sources.
OUTDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "figures"))

# ============================================================================
# Common preamble and styles
# ============================================================================

PREAMBLE = r"""\documentclass[tikz,border=10pt]{standalone}
\usepackage{circuitikz}
\usepackage{xcolor}
\usepackage{amsmath}
\usetikzlibrary{arrows}

\begin{document}
\begin{tikzpicture}[>=latex']

% --- AVE house figure style: WHITE print profile, Okabe-Ito colourblind-safe palette.
%     Hex values copied by hand from src/ave/viz/style.py COLORS + _PROP_CYCLE
%     (`ave.viz` is matplotlib-only and has no TikZ mechanism). All clear 3:1 on white.
\definecolor{aveblue}{HTML}{0072B2}       % COLORS["ave"]        -- alpha blocks
\definecolor{aveaccent}{HTML}{009E73}     % COLORS["accent"]     -- bus coupling
\definecolor{avevermillion}{HTML}{D55E00} % COLORS["comparison"] -- halo / avalanche
\definecolor{aveink}{HTML}{000000}        % COLORS["data"]       -- polar / special nodes, text
\definecolor{avemuted}{HTML}{7F7F7F}      % COLORS["muted"]      -- annotations, frames

% Background: WHITE. The prior `\fill[darkbg] (-7,-8) rectangle (7,7)` canvas is REMOVED,
% replaced by an unpainted `\path` over the SAME rectangle so the standalone bounding box
% (page size / aspect ratio) is preserved exactly.
\path (-7,-8) rectangle (7,7);

\tikzset{
    alpha block/.style={
        draw=#1, thick, fill=white!85!#1,
        rectangle, rounded corners=3pt,
        minimum width=2.0cm, minimum height=1.2cm,
        text=aveink, font=\bfseries, align=center
    },
    bus/.style={
        draw=aveaccent, ultra thick, dashed
    }
}
"""

POSTAMBLE = r"""
\end{tikzpicture}
\end{document}
"""

# ============================================================================
# Sulfur-32: 8α Cube
# ============================================================================

tex_s32 = (
    PREAMBLE
    + r"""
% Title
\node[text=aveink, font=\bfseries\Large] at (0, 6) {Sulfur-32 ($8\alpha$ Cube Architecture)};

% 8 Alphas at cube vertices (projected as two squares)
% Front face (inner square)
\node[alpha block=aveblue] (F1) at (-2.0, 2.5) {$\alpha_1$};
\node[alpha block=aveblue] (F2) at (2.0, 2.5) {$\alpha_2$};
\node[alpha block=aveblue] (F3) at (2.0, -0.5) {$\alpha_3$};
\node[alpha block=aveblue] (F4) at (-2.0, -0.5) {$\alpha_4$};

% Back face (outer square)
\node[alpha block=aveink] (B1) at (-4.0, 4.0) {$\alpha_5$};
\node[alpha block=aveink] (B2) at (4.0, 4.0) {$\alpha_6$};
\node[alpha block=aveink] (B3) at (4.0, -2.0) {$\alpha_7$};
\node[alpha block=aveink] (B4) at (-4.0, -2.0) {$\alpha_8$};

% Front face edges
\draw[bus] (F1) -- (F2);
\draw[bus] (F2) -- (F3);
\draw[bus] (F3) -- (F4);
\draw[bus] (F4) -- (F1);

% Back face edges
\draw[bus] (B1) -- (B2);
\draw[bus] (B2) -- (B3);
\draw[bus] (B3) -- (B4);
\draw[bus] (B4) -- (B1);

% Depth connections
\draw[bus] (F1) -- (B1);
\draw[bus] (F2) -- (B2);
\draw[bus] (F3) -- (B3);
\draw[bus] (F4) -- (B4);

% Legend
\node[text=aveink, text width=9cm, align=center, draw=avemuted, dashed, inner sep=8pt] at (0, -5.5) {
    \textbf{Large Signal Regime ($M = 32.8$, $V_R/V_{BR} = 0.994$)}\\
    First element requiring avalanche multiplication correction.\\
    Each $\alpha$ encapsulates a 4-nucleon LC mesh.\\
    \textit{Total Network: 496 discrete connections.}
};
"""
    + POSTAMBLE
)

# ============================================================================
# Argon-40: 10α Bicapped Square Antiprism
# ============================================================================

tex_ar40 = (
    PREAMBLE
    + r"""
% Title
\node[text=aveink, font=\bfseries\Large] at (0, 6) {Argon-40 ($10\alpha$ Bicapped Antiprism)};

% 8 in antiprism ring (two staggered squares)
\node[alpha block=aveblue] (T1) at (90:3.0) {$\alpha_1$};
\node[alpha block=aveblue] (T2) at (0:3.0) {$\alpha_2$};
\node[alpha block=aveblue] (T3) at (-90:3.0) {$\alpha_3$};
\node[alpha block=aveblue] (T4) at (180:3.0) {$\alpha_4$};

\node[alpha block=aveblue] (B1) at (45:2.0) {$\alpha_5$};
\node[alpha block=aveblue] (B2) at (-45:2.0) {$\alpha_6$};
\node[alpha block=aveblue] (B3) at (-135:2.0) {$\alpha_7$};
\node[alpha block=aveblue] (B4) at (135:2.0) {$\alpha_8$};

% 2 Polar Caps
\node[alpha block=aveink] (P1) at (0, 4.5) {$\alpha_{cap}$};
\node[alpha block=aveink] (P2) at (0, -4.5) {$\alpha_{cap}$};

% Outer square ring
\draw[bus] (T1) -- (T2);
\draw[bus] (T2) -- (T3);
\draw[bus] (T3) -- (T4);
\draw[bus] (T4) -- (T1);

% Inner square ring
\draw[bus] (B1) -- (B2);
\draw[bus] (B2) -- (B3);
\draw[bus] (B3) -- (B4);
\draw[bus] (B4) -- (B1);

% Cap to outer
\draw[bus] (P1) -- (T1);
\draw[bus] (P1) -- (T2);
\draw[bus] (P1) -- (T4);
\draw[bus] (P2) -- (T3);
\draw[bus] (P2) -- (T2);
\draw[bus] (P2) -- (T4);

% Legend
\node[text=aveink, text width=9cm, align=center, draw=avemuted, dashed, inner sep=8pt] at (0, -7) {
    \textbf{Noble Gas Configuration}\\
    Bicapped square antiprism: complete $n=3$ closure.\\
    45 inter-alpha coupling pairs.\\
    \textit{Total Network: 780 discrete connections.}
};
"""
    + POSTAMBLE
)

# ============================================================================
# Calcium-40: 10α Bicapped Square Antiprism (Large Signal)
# ============================================================================

tex_ca40 = (
    PREAMBLE
    + r"""
% Title
\node[text=aveink, font=\bfseries\Large] at (0, 6) {Calcium-40 ($10\alpha$ Large Signal)};

% Same geometry as Ar-40 but in Large Signal regime
\node[alpha block=avevermillion] (T1) at (90:3.0) {$\alpha_1$};
\node[alpha block=avevermillion] (T2) at (0:3.0) {$\alpha_2$};
\node[alpha block=avevermillion] (T3) at (-90:3.0) {$\alpha_3$};
\node[alpha block=avevermillion] (T4) at (180:3.0) {$\alpha_4$};

\node[alpha block=avevermillion] (B1) at (45:2.0) {$\alpha_5$};
\node[alpha block=avevermillion] (B2) at (-45:2.0) {$\alpha_6$};
\node[alpha block=avevermillion] (B3) at (-135:2.0) {$\alpha_7$};
\node[alpha block=avevermillion] (B4) at (135:2.0) {$\alpha_8$};

\node[alpha block=avevermillion] (P1) at (0, 4.5) {$\alpha_{cap}$};
\node[alpha block=avevermillion] (P2) at (0, -4.5) {$\alpha_{cap}$};

% Outer ring
\draw[bus, draw=red] (T1) -- (T2);
\draw[bus, draw=red] (T2) -- (T3);
\draw[bus, draw=red] (T3) -- (T4);
\draw[bus, draw=red] (T4) -- (T1);

% Inner ring
\draw[bus, draw=red] (B1) -- (B2);
\draw[bus, draw=red] (B2) -- (B3);
\draw[bus, draw=red] (B3) -- (B4);
\draw[bus, draw=red] (B4) -- (B1);

% Cap connections
\draw[bus, draw=red] (P1) -- (T1);
\draw[bus, draw=red] (P1) -- (T2);
\draw[bus, draw=red] (P1) -- (T4);
\draw[bus, draw=red] (P2) -- (T3);
\draw[bus, draw=red] (P2) -- (T2);
\draw[bus, draw=red] (P2) -- (T4);

% Legend
\node[text=aveink, text width=9cm, align=center, draw=avemuted, dashed, inner sep=8pt] at (0, -7) {
    \textbf{Large Signal Regime ($M = 32.9$, $V_R/V_{BR} = 0.994$)}\\
    Same topology as Ar-40 but with 2 extra protons.\\
    Avalanche multiplication required for mass closure.\\
    \textit{Total Network: 780 discrete connections.}
};
"""
    + POSTAMBLE
)

# ============================================================================
# Titanium-48: 12α Cuboctahedron
# ============================================================================

tex_ti48 = (
    PREAMBLE
    + r"""
% Title
\node[text=aveink, font=\bfseries\Large] at (0, 6) {Titanium-48 ($12\alpha$ Cuboctahedron)};

% 12 alphas at cuboctahedron vertices (projected)
% Equatorial ring (4)
\node[alpha block=aveblue] (E1) at (3.5, 0) {$\alpha_{eq}$};
\node[alpha block=aveblue] (E2) at (0, 2.5) {$\alpha_{eq}$};
\node[alpha block=aveblue] (E3) at (-3.5, 0) {$\alpha_{eq}$};
\node[alpha block=aveblue] (E4) at (0, -2.5) {$\alpha_{eq}$};

% Upper ring (4)
\node[alpha block=aveink] (U1) at (2.5, 3.5) {$\alpha_{up}$};
\node[alpha block=aveink] (U2) at (-2.5, 3.5) {$\alpha_{up}$};
\node[alpha block=aveink] (U3) at (-2.5, 1.0) {$\alpha_{up}$};
\node[alpha block=aveink] (U4) at (2.5, 1.0) {$\alpha_{up}$};

% Lower ring (4)
\node[alpha block=avevermillion] (L1) at (2.5, -1.0) {$\alpha_{lo}$};
\node[alpha block=avevermillion] (L2) at (-2.5, -1.0) {$\alpha_{lo}$};
\node[alpha block=avevermillion] (L3) at (-2.5, -3.5) {$\alpha_{lo}$};
\node[alpha block=avevermillion] (L4) at (2.5, -3.5) {$\alpha_{lo}$};

% Equatorial ring
\draw[bus] (E1) -- (E2);
\draw[bus] (E2) -- (E3);
\draw[bus] (E3) -- (E4);
\draw[bus] (E4) -- (E1);

% Upper ring
\draw[bus, draw=aveink] (U1) -- (U2);
\draw[bus, draw=aveink] (U2) -- (U3);
\draw[bus, draw=aveink] (U3) -- (U4);
\draw[bus, draw=aveink] (U4) -- (U1);

% Lower ring
\draw[bus, draw=avevermillion] (L1) -- (L2);
\draw[bus, draw=avevermillion] (L2) -- (L3);
\draw[bus, draw=avevermillion] (L3) -- (L4);
\draw[bus, draw=avevermillion] (L4) -- (L1);

% Cross connections
\draw[bus] (E1) -- (U4);
\draw[bus] (E1) -- (L1);
\draw[bus] (E2) -- (U1);
\draw[bus] (E2) -- (U2);
\draw[bus] (E3) -- (U3);
\draw[bus] (E3) -- (L2);
\draw[bus] (E4) -- (L3);
\draw[bus] (E4) -- (L4);

% Legend
\node[text=aveink, text width=9cm, align=center, draw=avemuted, dashed, inner sep=8pt] at (0, -6.5) {
    \textbf{First Transition Metal ($3d^2\,4s^2$)}\\
    Cuboctahedral alpha packing: 66 inter-alpha pairs.\\
    Each $\alpha$ encapsulates a 4-nucleon LC mesh.\\
    \textit{Total Network: 1128 discrete connections.}
};
"""
    + POSTAMBLE
)

# ============================================================================
# Chromium-52: 13α Centered Icosahedron
# ============================================================================

tex_cr52 = (
    PREAMBLE
    + r"""
% Title
\node[text=aveink, font=\bfseries\Large] at (0, 6) {Chromium-52 ($13\alpha$ Centered Icosahedron)};

% Central alpha
\node[alpha block=avevermillion, minimum width=2.5cm] (CENTER) at (0, 0) {$\alpha_0$\\center};

% 12 icosahedral vertices (projected as two pentagons + 2 poles)
% Outer pentagon (upper)
\node[alpha block=aveblue] (I1) at (90:4.0) {$\alpha$};
\node[alpha block=aveblue] (I2) at (162:4.0) {$\alpha$};
\node[alpha block=aveblue] (I3) at (234:4.0) {$\alpha$};
\node[alpha block=aveblue] (I4) at (306:4.0) {$\alpha$};
\node[alpha block=aveblue] (I5) at (18:4.0) {$\alpha$};

% Inner pentagon (rotated 36°)
\node[alpha block=aveink] (I6) at (126:2.5) {$\alpha$};
\node[alpha block=aveink] (I7) at (198:2.5) {$\alpha$};
\node[alpha block=aveink] (I8) at (270:2.5) {$\alpha$};
\node[alpha block=aveink] (I9) at (342:2.5) {$\alpha$};
\node[alpha block=aveink] (I10) at (54:2.5) {$\alpha$};

% Poles (projected to sides)
\node[alpha block=avevermillion] (P1) at (-5.5, 0) {$\alpha_N$};
\node[alpha block=avevermillion] (P2) at (5.5, 0) {$\alpha_S$};

% Outer pentagon
\draw[bus] (I1) -- (I2);
\draw[bus] (I2) -- (I3);
\draw[bus] (I3) -- (I4);
\draw[bus] (I4) -- (I5);
\draw[bus] (I5) -- (I1);

% Center to all
\draw[bus, draw=avevermillion] (CENTER) -- (I1);
\draw[bus, draw=avevermillion] (CENTER) -- (I2);
\draw[bus, draw=avevermillion] (CENTER) -- (I3);
\draw[bus, draw=avevermillion] (CENTER) -- (I4);
\draw[bus, draw=avevermillion] (CENTER) -- (I5);

% Legend
\node[text=aveink, text width=9cm, align=center, draw=avemuted, dashed, inner sep=8pt] at (0, -7) {
    \textbf{Anomalous Half-Fill ($3d^5\,4s^1$)}\\
    Central $\alpha$ coupled to 12-vertex icosahedral shell.\\
    78 inter-alpha coupling pairs.\\
    \textit{Total Network: 1326 discrete connections.}
};
"""
    + POSTAMBLE
)

# ============================================================================
# Iron-56: 14α FCC-14
# ============================================================================

tex_fe56 = (
    PREAMBLE
    + r"""
% Title
\node[text=aveink, font=\bfseries\Large] at (0, 6) {Iron-56 ($14\alpha$ FCC Architecture)};

% FCC unit cell: 8 corner alphas + 6 face-center alphas
% Corners (projected cube)
\node[alpha block=aveblue] (C1) at (-3, 3.5) {$\alpha_c$};
\node[alpha block=aveblue] (C2) at (3, 3.5) {$\alpha_c$};
\node[alpha block=aveblue] (C3) at (3, 0.5) {$\alpha_c$};
\node[alpha block=aveblue] (C4) at (-3, 0.5) {$\alpha_c$};
\node[alpha block=aveblue] (C5) at (-4.5, 2.0) {$\alpha_c$};
\node[alpha block=aveblue] (C6) at (4.5, 2.0) {$\alpha_c$};
\node[alpha block=aveblue] (C7) at (4.5, -1.0) {$\alpha_c$};
\node[alpha block=aveblue] (C8) at (-4.5, -1.0) {$\alpha_c$};

% Face centers
\node[alpha block=avevermillion] (F1) at (0, 3.5) {$\alpha_f$};
\node[alpha block=avevermillion] (F2) at (0, 0.5) {$\alpha_f$};
\node[alpha block=avevermillion] (F3) at (-3.75, 0.5) {$\alpha_f$};
\node[alpha block=avevermillion] (F4) at (3.75, 0.5) {$\alpha_f$};
\node[alpha block=avevermillion] (F5) at (0, 2.0) {$\alpha_f$};
\node[alpha block=avevermillion] (F6) at (0, -1.0) {$\alpha_f$};

% Corner edges (cube projection)
\draw[bus] (C1) -- (C2);
\draw[bus] (C2) -- (C3);
\draw[bus] (C3) -- (C4);
\draw[bus] (C4) -- (C1);

% Face-to-corner links
\draw[bus, draw=avevermillion] (F1) -- (C1);
\draw[bus, draw=avevermillion] (F1) -- (C2);
\draw[bus, draw=avevermillion] (F2) -- (C3);
\draw[bus, draw=avevermillion] (F2) -- (C4);

% Legend
\node[text=aveink, text width=9cm, align=center, draw=avemuted, dashed, inner sep=8pt] at (0, -5) {
    \textbf{Minimum Mass per Nucleon (Fusion Endpoint)}\\
    FCC-14: 8 corner + 6 face-center alpha clusters.\\
    91 inter-alpha coupling pairs.\\
    \textit{Total Network: 1540 discrete connections.}
};
"""
    + POSTAMBLE
)


# ============================================================================
# Write and compile
# ============================================================================

circuits = {
    "circuit_s32": tex_s32,
    "circuit_ar40": tex_ar40,
    "circuit_ca40": tex_ca40,
    "circuit_ti48": tex_ti48,
    "circuit_cr52": tex_cr52,
    "circuit_fe56": tex_fe56,
}

if not os.path.isdir(OUTDIR):
    raise SystemExit(
        f"OUTDIR does not exist: {OUTDIR}\nRefusing to create it -- this generator writes "
        "over TRACKED figure sources, so a missing target means the path is wrong."
    )

for name, tex in circuits.items():
    tex_path = os.path.join(OUTDIR, f"{name}.tex")
    pdf_path = os.path.join(OUTDIR, f"{name}.pdf")

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex)
    print(f"Wrote {tex_path}")

    # Compile to PDF
    result = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-output-directory", OUTDIR, tex_path],
        capture_output=True,
        text=True,
        cwd=OUTDIR,
    )
    if result.returncode == 0:
        print(f"  ✓ Compiled {name}.pdf")
    else:
        print(f"  ✗ FAILED {name}: {result.stderr[-200:]}")

    # Clean aux/log files
    for ext in [".aux", ".log"]:
        auxfile = os.path.join(OUTDIR, f"{name}{ext}")
        if os.path.exists(auxfile):
            os.remove(auxfile)

print("\nDone! Circuit PDFs are in:", OUTDIR)
