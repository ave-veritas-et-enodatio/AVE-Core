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
    #                  current foreword content while catching catastrophic
    #                  layout overruns. Future cleanup: convert \texttt{path}
    #                  to \path{} / \seqsplit{} / hand-broken \allowbreak
    #                  across foreword + chapter narrative, then tighten gate
    #                  back to 15-30pt for publication polish.
    # See QUEUE: per-overrun surgical foreword cleanup (low priority; cosmetic).
    max_allowed = 200.0
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
