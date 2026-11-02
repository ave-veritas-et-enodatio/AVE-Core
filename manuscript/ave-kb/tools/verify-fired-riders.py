#!/usr/bin/env python3
r"""Verify that FIRED prereg riders have reached the corpus.

WHAT THIS CATCHES THAT NOTHING ELSE DOES
----------------------------------------
A frozen prereg registers a RIDER: a threshold stated in advance whose crossing
falsifies a NAMED chain. When one fires, every site printing that chain's OUTPUT
VALUE is stale -- and the printed value does not change, so:

  * the board's print-vs-KB-truth comparison passes (both sides still agree),
  * the cite ratchet passes (the cite is present and correct),
  * verify-md-links passes (the target resolves),
  * the tex-vs-KB staleness scan passes (the cited leaf gained no demotion marker
    -- the demotion lives in a RESULT DOC the leaf never learned about).

Measured instance: the `(1+nu_vac)` rider fired 2026-08-03 at a 27.91% deviation
against a frozen 3% trip level. Thirty-four days later nine KB sites still booked
the falsified chain as a zero-free-parameter derivation and every checker above
was green. Supersession of this species lives in VALUES, not citations.

WHAT IT CHECKS
--------------
  [1] LEDGER REGRESSION (hard, exit 1). A rider whose registry row declares a
      `ledger_slug` must still find that slug in the falsification ledger. This
      catches a propagated firing being deleted or renamed out from under itself.
  [2] UNDOCUMENTED DEBT (hard, exit 1). A rider marked FIRED with no
      `ledger_slug` MUST carry a `note` saying where it stands. Silent debt is
      the failure mode; disclosed debt is a decision Grant has made.
  [3] VALUE SITES (report only, never gates). Sites printing a fired rider's
      output patterns without a post-firing dated marker nearby. Advisory
      BY DESIGN -- these are candidates for a human read, and gating on known
      debt would just paint the build permanently red.

ANTI-TAUTOLOGY / LIVENESS
-------------------------
Before trusting any zero, the checker proves it can find a slug that IS there:
`RD-KAPPAMAX-PULSAR-KILLLINE` propagated correctly and its slug is in the
ledger. If that control does not resolve, the FINDER is broken, not the corpus,
and the run aborts rather than reporting a false clean. A check that cannot fail
is not a check.
"""
import json, os, re, subprocess, sys

ROOT = subprocess.run(['git','rev-parse','--show-toplevel'],
                      capture_output=True, text=True).stdout.strip()
os.chdir(ROOT)

REGISTRY = '_orchestration/fired-riders.json'
LEDGER   = 'manuscript/ave-kb/common/genesis-chord-falsification-ledger.md'
CONTROL  = 'RD-KAPPAMAX-PULSAR-KILLLINE'
SEARCH_ROOTS = ['manuscript']
# A dated banner near a value is the corpus's own disclosure form.
MARKER = re.compile(
    r'RETRACT|DEMOT|WALK-?BACK|SUPERSED|STRUCK|FALSIFI|WITHDRAWN|'
    r'RE-?BAND|scope-correct|\U0001F534|rider|v2\.4|ROOT-CERTIFIED',
    re.IGNORECASE)

def sh(a):
    return subprocess.run(a, capture_output=True, text=True).stdout

def main():
    reg = json.load(open(REGISTRY))
    riders = reg['riders']
    ledger = open(LEDGER, encoding='utf-8', errors='replace').read()

    # ---- liveness control: prove the finder works before trusting any zero ----
    ctl = next((r for r in riders if r['rider_id'] == CONTROL), None)
    if ctl is None or not ctl.get('ledger_slug'):
        print('[fired-riders] ABORT: liveness control %s missing or has no '
              'ledger_slug. Cannot distinguish "nothing to find" from "finder '
              'broken".' % CONTROL)
        return 2
    if ctl['ledger_slug'] not in ledger:
        print('[fired-riders] ABORT: liveness control %s declares slug %r but it '
              'is not in %s. The FINDER is broken (or the ledger moved) -- a '
              'clean report here would be false.'
              % (CONTROL, ctl['ledger_slug'], LEDGER))
        return 2
    print('[fired-riders] liveness OK — control %s resolves in the ledger.' % CONTROL)

    fired = [r for r in riders if r.get('fired') == 'FIRED']
    hard, owed, sites = [], [], []

    for r in fired:
        slug = r.get('ledger_slug')
        if slug:
            if slug not in ledger:
                hard.append((r['rider_id'],
                             'declares ledger_slug %r, absent from the ledger — '
                             'a propagated firing was deleted or renamed' % slug))
        else:
            if not (r.get('note') or '').strip():
                hard.append((r['rider_id'],
                             'FIRED with no ledger_slug AND no note — silent debt'))
            else:
                owed.append((r['rider_id'], r['fired_date'], r.get('note', '')))

    # ---- [3] advisory value-site scan, unpropagated riders only ----
    for r in fired:
        if r.get('ledger_slug'):
            continue
        for pat in r.get('output_patterns', []):
            out = sh(['git', 'grep', '-n', '-F', pat, '--'] + SEARCH_ROOTS)
            for line in out.splitlines():
                parts = line.split(':', 2)
                if len(parts) < 3:
                    continue
                path, ln, text = parts
                if MARKER.search(text):
                    continue
                sites.append((r['rider_id'], pat, path, ln, text.strip()[:110]))

    print('\n=== [1]+[2] HARD ===')
    for rid, why in hard:
        print('  FAIL  %-28s %s' % (rid, why))
    if not hard:
        print('  none')

    print('\n=== FIRED but UNPROPAGATED (disclosed debt, not a gate) ===')
    for rid, d, note in owed:
        print('  %-28s fired %s' % (rid, d))
        print('        %s' % note[:150])
    if not owed:
        print('  none')

    print('\n=== [3] VALUE SITES without a nearby dated marker (advisory) ===')
    byr = {}
    for rid, pat, path, ln, text in sites:
        byr.setdefault(rid, []).append((path, ln, pat, text))
    for rid, rows in byr.items():
        print('  --- %s: %d site(s) ---' % (rid, len(rows)))
        for path, ln, pat, text in rows[:25]:
            print('    %s:%s  [%s]  %s' % (path, ln, pat, text))
        if len(rows) > 25:
            print('    … %d more not listed' % (len(rows) - 25))
    if not byr:
        print('  none')

    print('\n[fired-riders] riders=%d fired=%d hard=%d owed=%d advisory-sites=%d'
          % (len(riders), len(fired), len(hard), len(owed), len(sites)))
    return 1 if hard else 0

if __name__ == '__main__':
    sys.exit(main())
