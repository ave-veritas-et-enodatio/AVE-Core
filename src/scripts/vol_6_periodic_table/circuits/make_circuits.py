import subprocess

tex_h1 = r"""\documentclass[tikz,border=15pt]{standalone}
\usepackage{circuitikz}
\begin{document}
\begin{tikzpicture}
    \begin{scope}[shift={(0,0)}]
        \draw (0,0.5) to[L=$L_{proton}$, *-*] (0,-1.5);
        \draw (2,0.5) to[C=$C_{vac}$, *-*] (2,-1.5);
        \draw (0,0.5) -- (2,0.5);
        \draw (0,-1.5) -- (2,-1.5);
        \node at (1, -2.5) {Nucleon Tank ($6^3_2$)};
    \end{scope}

    \begin{scope}[shift={(6,0)}]
        \draw (0,0.5) to[L=$L_{elec}$, *-*] (0,-1.5);
        \draw (2,0.5) to[C=$C_{vac}$, *-*] (2,-1.5);
        \draw (0,0.5) -- (2,0.5);
        \draw (0,-1.5) -- (2,-1.5);
        \node at (1, -2.5) {Orbital Phase Tank ($3_1$)};
    \end{scope}

    \draw[<->, dashed, blue, thick] (2.2,-0.5) -- (5.8,-0.5) node[midway, above] {$M_{orbit} \propto \frac{1}{r_{Bohr}}$};

    \node at (4, 2.5) {\Large \textbf{Hydrogen-1 (Protium) AVE Circuit}};
\end{tikzpicture}
\end{document}
"""

tex_he4 = r"""\documentclass[tikz,border=15pt]{standalone}
\usepackage{circuitikz}
\begin{document}
\begin{tikzpicture}
    \def\tank#1#2#3{
        \begin{scope}[shift={(#1)}]
            \draw (0,0.5) to[L=$#3$, *-*] (0,-1.5);
            \draw (1.5,0.5) to[C=$C_v$, *-*] (1.5,-1.5);
            \draw (0,0.5) -- (1.5,0.5);
            \draw (0,-1.5) -- (1.5,-1.5);
        \end{scope}
    }
    
    \tank{0,4}{1}{L_{p1}}
    \tank{5,4}{2}{L_{p2}}
    \tank{0,0}{3}{L_{n1}}
    \tank{5,0}{4}{L_{n2}}
    
    \draw[<->, dashed, blue, thick] (1.7,3.5) -- (4.8,3.5) node[midway, above] {$M$};
    \draw[<->, dashed, blue, thick] (1.7,-0.5) -- (4.8,-0.5) node[midway, below] {$M$};
    \draw[<->, dashed, blue, thick] (0.75,2.3) -- (0.75,1.2) node[midway, left] {$M$};
    \draw[<->, dashed, blue, thick] (5.75,2.3) -- (5.75,1.2) node[midway, right] {$M$};
    \draw[<->, dashed, blue, thick] (1.5,2.3) -- (4.8,1.2) node[midway, above right, pos=0.2] {$M$};
    \draw[<->, dashed, blue, thick] (5,2.3) -- (1.7,1.2) node[midway, above left, pos=0.2] {$M$};
    
    \node at (3.25, 6) {\Large \textbf{Helium-4 (Alpha Particle) Core Network}};
    \node at (3.25, -2.5) {Symmetric Tetrahedron: All nodes mutually coupled ($M_{ij} \propto 1/d_{core}$)};
\end{tikzpicture}
\end{document}
"""

tex_li7 = r"""\documentclass[tikz,border=15pt]{standalone}
\usepackage{circuitikz}
\begin{document}
\begin{tikzpicture}
    \def\tank#1#2#3{
        \begin{scope}[shift={(#1)}]
            \draw (0,0.3) to[L=$#3$, *-*] (0,-1.0);
            \draw (1,0.3) to[C, *-*] (1,-1.0);
            \draw (0,0.3) -- (1,0.3);
            \draw (0,-1.0) -- (1,-1.0);
        \end{scope}
    }
    
    % Alpha Core
    \draw[rounded corners=10pt, fill=blue!5, thick] (-1,-1.5) rectangle (3.5,2.5);
    \node at (1.25, 3) {\textbf{Alpha Core (He-4)}};
    
    \tank{0,1}{1}{p}
    \tank{1.5,1}{2}{p}
    \tank{0,-0.5}{3}{n}
    \tank{1.5,-0.5}{4}{n}
    
    % Outer Shell
    \draw[rounded corners=10pt, fill=red!5, thick] (6,-2.5) rectangle (10.5,3.5);
    \node at (8.25, 4) {\textbf{Outer Shell}};
    
    \tank{7.5,1.5}{5}{n}
    \tank{6.5,-1}{6}{p}
    \tank{8.5,-1}{7}{n}
    
    % Loose Mutual Coupling
    \draw[<->, dashed, blue, thick, out=0, in=180] (3.5, 0.5) to (6, 0.5) node[midway, above] {$M_{\text{core-halo}}$};
    
    \node at (4.75, 5) {\Large \textbf{Lithium-7 Equivalent Circuit}};
\end{tikzpicture}
\end{document}
"""

tex_be9 = r"""\documentclass[tikz,border=15pt]{standalone}
\usepackage{circuitikz}
\begin{document}
\begin{tikzpicture}
    \def\tank#1#2#3{
        \begin{scope}[shift={(#1)}]
            \draw (0,0.3) to[L=$#3$, *-*] (0,-1.0);
            \draw (1,0.3) to[C, *-*] (1,-1.0);
            \draw (0,0.3) -- (1,0.3);
            \draw (0,-1.0) -- (1,-1.0);
        \end{scope}
    }
    
    % Alpha Core 1 (Left)
    \draw[rounded corners=10pt, fill=blue!5, thick, dashed] (-5,-1.5) rectangle (-0.5,2.5);
    \node at (-2.75, 3) {\textbf{Alpha Core}};
    
    \tank{-4,1}{1}{p}
    \tank{-2.5,1}{2}{p}
    \tank{-4,-0.5}{3}{n}
    \tank{-2.5,-0.5}{4}{n}
    
    % Alpha Core 2 (Right)
    \draw[rounded corners=10pt, fill=blue!5, thick, dashed] (5,-1.5) rectangle (9.5,2.5);
    \node at (7.25, 3) {\textbf{Alpha Core}};
    
    \tank{6,1}{5}{p}
    \tank{7.5,1}{6}{p}
    \tank{6,-0.5}{7}{n}
    \tank{7.5,-0.5}{8}{n}
    
    % Bridge Neutron (Center)
    \draw[rounded corners=5pt, fill=green!10, thick] (1.7,-1.5) rectangle (3.3,1.5);
    \node at (2.5, 2) {\textbf{Bridge}};
    \tank{2.0,0.5}{9}{n}
    
    % Endothermic Coupling (Tension)
    \draw[<->, violet, thick, out=0, in=180] (-0.5, 0.5) to (1.7, 0.5) node[midway, above] {$M_{bridge}$};
    \draw[<->, violet, thick, out=180, in=0] (5, 0.5) to (3.3, 0.5) node[midway, above] {$M_{bridge}$};
    
    \node at (2.25, 4.5) {\Large \textbf{Beryllium-9 Dual-Core Endothermic Circuit}};
\end{tikzpicture}
\end{document}
"""

with open("circuit_h1.tex", "w") as f:
    f.write(tex_h1)
with open("circuit_he4.tex", "w") as f:
    f.write(tex_he4)
with open("circuit_li7.tex", "w") as f:
    f.write(tex_li7)
with open("circuit_be9.tex", "w") as f:
    f.write(tex_be9)

files = ["circuit_h1", "circuit_he4", "circuit_li7", "circuit_be9"]
for file in files:
    subprocess.run(["pdflatex", "-interaction=nonstopmode", f"{file}.tex"])
    subprocess.run(["sips", "-s", "format", "png", f"{file}.pdf", "--out", f"{file}.png"])
