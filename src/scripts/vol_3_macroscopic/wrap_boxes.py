import os
import re

from ave_path_util import manuscript_path

chapters_dir = manuscript_path("vol_3_macroscopic", "chapters")
files = [str(p) for p in chapters_dir.glob("*.tex")]

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace \section*{Chapter Summary} with \begin{summarybox}
    # and find the end of the itemize to insert \end{summarybox}
    if "\\section*{Chapter Summary}" in content:
        # We need to wrap the whole section. It usually looks like:
        # \section*{Chapter Summary}
        # \begin{itemize}
        # ...
        # \end{itemize}

        # We'll use regex to carefully replace it.
        pattern1 = r"\\section\*\{Chapter Summary\}\s*\\begin\{itemize\}(.*?)\\end\{itemize\}"
        replacement1 = r"\\begin{summarybox}\n\\begin{itemize}\g<1>\\end{itemize}\n\\end{summarybox}"
        content = re.sub(pattern1, replacement1, content, flags=re.DOTALL)

        pattern2 = r"\\section\*\{Exercises\}\s*\\begin\{enumerate\}(.*?)\\end\{enumerate\}"
        replacement2 = r"\\begin{exercisebox}\n\\begin{enumerate}\g<1>\\end{enumerate}\n\\end{exercisebox}"
        content = re.sub(pattern2, replacement2, content, flags=re.DOTALL)

        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Wrapped boxes in {os.path.basename(file)}")
