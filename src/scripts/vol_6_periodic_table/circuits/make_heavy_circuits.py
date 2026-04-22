#!/usr/bin/env python3
"""
Generate TikZ circuit schematics for heavy elements (S-32 through Fe-56).

Each circuit uses the same visual style as the existing periodic table circuits:
- Dark background (RGB 15,15,15)
- Neon blue alpha blocks
- Neon green bus coupling lines
- Purple blocks for polar/halo/special nodes
- White text and legends

Geometries are taken directly from the semiconductor_binding_engine.py:
  S-32:  8α  Cube
  Ar-40: 10α Bicapped Square Antiprism
  Ca-40: 10α Bicapped Square Antiprism (isobar of Ar-40)
  Ti-48: 12α Cuboctahedron
  Cr-52: 13α Centered Icosahedron
  Fe-56: 14α FCC-14
"""

import subprocess
import os
import sys

OUTDIR = os.path.join(os.path.dirname(__file__), "..", "..", "periodic_table", "figures")

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

\definecolor{neonblue}{RGB}{0, 255, 255}
\definecolor{neongreen}{RGB}{0, 255, 128}
\definecolor{darkbg}{RGB}{15, 15, 15}
\definecolor{neonpurple}{RGB}{200, 0, 255}
\definecolor{neonorange}{RGB}{255, 165, 0}

% Fill background
\fill[darkbg] (-7,-8) rectangle (7,7);

\tikzset{
    alpha block/.style={
        draw=#1, thick, fill=darkbg!80!#1,
        rectangle, rounded corners=3pt,
        minimum width=2.0cm, minimum height=1.2cm,
        text=white, font=\bfseries, align=center
    },
    bus/.style={
        draw=neongreen, ultra thick, dashed
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
\node[text=white, font=\bfseries\Large] at (0, 6) {Sulfur-32 ($8\alpha$ Cube Architecture)};

% 8 Alphas at cube vertices (projected as two squares)
% Front face (inner square)
\node[alpha block=neonblue] (F1) at (-2.0, 2.5) {$\alpha_1$};
\node[alpha block=neonblue] (F2) at (2.0, 2.5) {$\alpha_2$};
\node[alpha block=neonblue] (F3) at (2.0, -0.5) {$\alpha_3$};
\node[alpha block=neonblue] (F4) at (-2.0, -0.5) {$\alpha_4$};

% Back face (outer square)
\node[alpha block=neonpurple] (B1) at (-4.0, 4.0) {$\alpha_5$};
\node[alpha block=neonpurple] (B2) at (4.0, 4.0) {$\alpha_6$};
\node[alpha block=neonpurple] (B3) at (4.0, -2.0) {$\alpha_7$};
\node[alpha block=neonpurple] (B4) at (-4.0, -2.0) {$\alpha_8$};

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
\node[text=white, text width=9cm, align=center, draw=white, dashed, inner sep=8pt] at (0, -5.5) {
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
\node[text=white, font=\bfseries\Large] at (0, 6) {Argon-40 ($10\alpha$ Bicapped Antiprism)};

% 8 in antiprism ring (two staggered squares)
\node[alpha block=neonblue] (T1) at (90:3.0) {$\alpha_1$};
\node[alpha block=neonblue] (T2) at (0:3.0) {$\alpha_2$};
\node[alpha block=neonblue] (T3) at (-90:3.0) {$\alpha_3$};
\node[alpha block=neonblue] (T4) at (180:3.0) {$\alpha_4$};

\node[alpha block=neonblue] (B1) at (45:2.0) {$\alpha_5$};
\node[alpha block=neonblue] (B2) at (-45:2.0) {$\alpha_6$};
\node[alpha block=neonblue] (B3) at (-135:2.0) {$\alpha_7$};
\node[alpha block=neonblue] (B4) at (135:2.0) {$\alpha_8$};

% 2 Polar Caps
\node[alpha block=neonpurple] (P1) at (0, 4.5) {$\alpha_{cap}$};
\node[alpha block=neonpurple] (P2) at (0, -4.5) {$\alpha_{cap}$};

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
\node[text=white, text width=9cm, align=center, draw=white, dashed, inner sep=8pt] at (0, -7) {
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
\node[text=white, font=\bfseries\Large] at (0, 6) {Calcium-40 ($10\alpha$ Large Signal)};

% Same geometry as Ar-40 but in Large Signal regime
\node[alpha block=neonorange] (T1) at (90:3.0) {$\alpha_1$};
\node[alpha block=neonorange] (T2) at (0:3.0) {$\alpha_2$};
\node[alpha block=neonorange] (T3) at (-90:3.0) {$\alpha_3$};
\node[alpha block=neonorange] (T4) at (180:3.0) {$\alpha_4$};

\node[alpha block=neonorange] (B1) at (45:2.0) {$\alpha_5$};
\node[alpha block=neonorange] (B2) at (-45:2.0) {$\alpha_6$};
\node[alpha block=neonorange] (B3) at (-135:2.0) {$\alpha_7$};
\node[alpha block=neonorange] (B4) at (135:2.0) {$\alpha_8$};

\node[alpha block=neonorange] (P1) at (0, 4.5) {$\alpha_{cap}$};
\node[alpha block=neonorange] (P2) at (0, -4.5) {$\alpha_{cap}$};

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
\node[text=white, text width=9cm, align=center, draw=white, dashed, inner sep=8pt] at (0, -7) {
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
\node[text=white, font=\bfseries\Large] at (0, 6) {Titanium-48 ($12\alpha$ Cuboctahedron)};

% 12 alphas at cuboctahedron vertices (projected)
% Equatorial ring (4)
\node[alpha block=neonblue] (E1) at (3.5, 0) {$\alpha_{eq}$};
\node[alpha block=neonblue] (E2) at (0, 2.5) {$\alpha_{eq}$};
\node[alpha block=neonblue] (E3) at (-3.5, 0) {$\alpha_{eq}$};
\node[alpha block=neonblue] (E4) at (0, -2.5) {$\alpha_{eq}$};

% Upper ring (4)
\node[alpha block=neonpurple] (U1) at (2.5, 3.5) {$\alpha_{up}$};
\node[alpha block=neonpurple] (U2) at (-2.5, 3.5) {$\alpha_{up}$};
\node[alpha block=neonpurple] (U3) at (-2.5, 1.0) {$\alpha_{up}$};
\node[alpha block=neonpurple] (U4) at (2.5, 1.0) {$\alpha_{up}$};

% Lower ring (4)
\node[alpha block=neonorange] (L1) at (2.5, -1.0) {$\alpha_{lo}$};
\node[alpha block=neonorange] (L2) at (-2.5, -1.0) {$\alpha_{lo}$};
\node[alpha block=neonorange] (L3) at (-2.5, -3.5) {$\alpha_{lo}$};
\node[alpha block=neonorange] (L4) at (2.5, -3.5) {$\alpha_{lo}$};

% Equatorial ring
\draw[bus] (E1) -- (E2);
\draw[bus] (E2) -- (E3);
\draw[bus] (E3) -- (E4);
\draw[bus] (E4) -- (E1);

% Upper ring
\draw[bus, draw=neonpurple] (U1) -- (U2);
\draw[bus, draw=neonpurple] (U2) -- (U3);
\draw[bus, draw=neonpurple] (U3) -- (U4);
\draw[bus, draw=neonpurple] (U4) -- (U1);

% Lower ring
\draw[bus, draw=neonorange] (L1) -- (L2);
\draw[bus, draw=neonorange] (L2) -- (L3);
\draw[bus, draw=neonorange] (L3) -- (L4);
\draw[bus, draw=neonorange] (L4) -- (L1);

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
\node[text=white, text width=9cm, align=center, draw=white, dashed, inner sep=8pt] at (0, -6.5) {
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
\node[text=white, font=\bfseries\Large] at (0, 6) {Chromium-52 ($13\alpha$ Centered Icosahedron)};

% Central alpha
\node[alpha block=neonorange, minimum width=2.5cm] (CENTER) at (0, 0) {$\alpha_0$\\center};

% 12 icosahedral vertices (projected as two pentagons + 2 poles)
% Outer pentagon (upper)
\node[alpha block=neonblue] (I1) at (90:4.0) {$\alpha$};
\node[alpha block=neonblue] (I2) at (162:4.0) {$\alpha$};
\node[alpha block=neonblue] (I3) at (234:4.0) {$\alpha$};
\node[alpha block=neonblue] (I4) at (306:4.0) {$\alpha$};
\node[alpha block=neonblue] (I5) at (18:4.0) {$\alpha$};

% Inner pentagon (rotated 36°)
\node[alpha block=neonpurple] (I6) at (126:2.5) {$\alpha$};
\node[alpha block=neonpurple] (I7) at (198:2.5) {$\alpha$};
\node[alpha block=neonpurple] (I8) at (270:2.5) {$\alpha$};
\node[alpha block=neonpurple] (I9) at (342:2.5) {$\alpha$};
\node[alpha block=neonpurple] (I10) at (54:2.5) {$\alpha$};

% Poles (projected to sides)
\node[alpha block=neonorange] (P1) at (-5.5, 0) {$\alpha_N$};
\node[alpha block=neonorange] (P2) at (5.5, 0) {$\alpha_S$};

% Outer pentagon
\draw[bus] (I1) -- (I2);
\draw[bus] (I2) -- (I3);
\draw[bus] (I3) -- (I4);
\draw[bus] (I4) -- (I5);
\draw[bus] (I5) -- (I1);

% Center to all
\draw[bus, draw=neonorange] (CENTER) -- (I1);
\draw[bus, draw=neonorange] (CENTER) -- (I2);
\draw[bus, draw=neonorange] (CENTER) -- (I3);
\draw[bus, draw=neonorange] (CENTER) -- (I4);
\draw[bus, draw=neonorange] (CENTER) -- (I5);

% Legend
\node[text=white, text width=9cm, align=center, draw=white, dashed, inner sep=8pt] at (0, -7) {
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
\node[text=white, font=\bfseries\Large] at (0, 6) {Iron-56 ($14\alpha$ FCC Architecture)};

% FCC unit cell: 8 corner alphas + 6 face-center alphas
% Corners (projected cube)
\node[alpha block=neonblue] (C1) at (-3, 3.5) {$\alpha_c$};
\node[alpha block=neonblue] (C2) at (3, 3.5) {$\alpha_c$};
\node[alpha block=neonblue] (C3) at (3, 0.5) {$\alpha_c$};
\node[alpha block=neonblue] (C4) at (-3, 0.5) {$\alpha_c$};
\node[alpha block=neonblue] (C5) at (-4.5, 2.0) {$\alpha_c$};
\node[alpha block=neonblue] (C6) at (4.5, 2.0) {$\alpha_c$};
\node[alpha block=neonblue] (C7) at (4.5, -1.0) {$\alpha_c$};
\node[alpha block=neonblue] (C8) at (-4.5, -1.0) {$\alpha_c$};

% Face centers
\node[alpha block=neonorange] (F1) at (0, 3.5) {$\alpha_f$};
\node[alpha block=neonorange] (F2) at (0, 0.5) {$\alpha_f$};
\node[alpha block=neonorange] (F3) at (-3.75, 0.5) {$\alpha_f$};
\node[alpha block=neonorange] (F4) at (3.75, 0.5) {$\alpha_f$};
\node[alpha block=neonorange] (F5) at (0, 2.0) {$\alpha_f$};
\node[alpha block=neonorange] (F6) at (0, -1.0) {$\alpha_f$};

% Corner edges (cube projection)
\draw[bus] (C1) -- (C2);
\draw[bus] (C2) -- (C3);
\draw[bus] (C3) -- (C4);
\draw[bus] (C4) -- (C1);

% Face-to-corner links
\draw[bus, draw=neonorange] (F1) -- (C1);
\draw[bus, draw=neonorange] (F1) -- (C2);
\draw[bus, draw=neonorange] (F2) -- (C3);
\draw[bus, draw=neonorange] (F2) -- (C4);

% Legend
\node[text=white, text width=9cm, align=center, draw=white, dashed, inner sep=8pt] at (0, -5) {
    \textbf{Peak Binding Energy per Nucleon}\\
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

os.makedirs(OUTDIR, exist_ok=True)

for name, tex in circuits.items():
    tex_path = os.path.join(OUTDIR, f"{name}.tex")
    pdf_path = os.path.join(OUTDIR, f"{name}.pdf")

    with open(tex_path, "w") as f:
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
