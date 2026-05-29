import re
import sys


def check_log(log_path: str) -> None:
    overfull_pattern = re.compile(r"Overfull \\hbox \(([\d\.]+)pt too wide\)")
    # max_allowed governs cosmetic overrun tolerance. Threshold history:
    #   15pt original: too tight for foreword's dense narrative paragraphs
    #                  with long inline \texttt{paths} (research/files,
    #                  src/scripts/, KB cross-refs) pdfTeX cannot break.
    #   100pt 2026-05-28: insufficient (max observed = 147pt before fixes,
    #                  108pt after \sloppy + \emergencystretch=5em).
    #   200pt 2026-05-28: pragmatic in-flight threshold accommodating
    #                  foreword + early Vol 9 content while catching
    #                  catastrophic layout overruns.
    #   350pt 2026-05-28 (Vol 9 chapter-buildout PR): bumped again after
    #                  Wave 1-3 chapter content landed with long \texttt{path}
    #                  citations to canonical-leaf paths (max observed 293pt
    #                  at Ch 8 + Ch 11 + Ch 13 + Ch 14 + Ch 15 + Ch 16 path
    #                  citations). Per-overrun cleanup was queued.
    #   45pt 2026-05-28 (vol9-corpus LaTeX-formatting pass): the deferred
    #                  cleanup landed. Long inline \texttt{} path citations
    #                  corpus-wide are now wrapped in \kbleaf{} (= robust
    #                  \texttt{\seqsplit{}}), which breaks the path at any
    #                  character; the widest 5-/7-column Vol 9 tables were
    #                  converted to tabularx wrapping columns; and global
    #                  \sloppy was removed (replaced by a bounded
    #                  \emergencystretch). Measured global max overrun across
    #                  all 8 volumes dropped from 345pt -> 34pt (vol 9 34.05pt,
    #                  vol 0 32.17pt; all others <14pt). Threshold set to 45pt:
    #                  just above the measured max with a small headroom for
    #                  pass-to-pass page-break variation in the cross-volume
    #                  two-pass build.
    max_allowed = 45.0
    failed = False

    try:
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                match = overfull_pattern.search(line)
                if match:
                    pt_over = float(match.group(1))
                    if pt_over > max_allowed:
                        print(f"\n[Error] Hard margin overrun detected: {pt_over}pt")
                        print(f"Log Output: {line.strip()}")
                        failed = True
    except FileNotFoundError:
        print(f"[Error] Log file not found: {log_path}")
        sys.exit(1)

    if failed:
        print(f"\n[Fatal] Build blocked. Fix tables or elements exceeding the text margin by >{max_allowed}pt.\n")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_latex_margins.py <logfile>")
        sys.exit(1)
    check_log(sys.argv[1])
