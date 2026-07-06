export const meta = {
  name: 'ave-adversarial-pr-review',
  description: 'Standard AVE adversarial PR review: N domain lenses -> per-finding adversarial verify (CONFIRMED/DOWNGRADED/REFUTED)',
  whenToUse: 'Every physics/canon PR before it is presented to Grant as CLEARED. args = {pr, context, lenses:[{key, prompt, run}]}. Validated 2026-07-04/05 across PRs #519-#539: caught a fabricated quote, four unfireable gates, a kinematic lab-frame artifact, a boundary artifact, a sign-convention inversion, and a mixed-footing ratio before any reached canon.',
  phases: [
    { title: 'Review', detail: 'domain lenses over the PR branch' },
    { title: 'Verify', detail: 'adversarial refute-pass on every finding' },
  ],
}

// args contract:
//   pr      (number, required) - the PR under review
//   context (string, required) - the claim under review: verdict/bin, headline numbers,
//            merged-canon ground truth, knife targets, claim-grade rules. Everything a
//            reviewer needs to hold the PR to its own stated standard.
//   lenses  (array, required)  - [{key, prompt, run}]: run=true gives the reviewer full
//            tools (throwaway-worktree execution); run=false uses the read-only
//            ave-auditor. Standard shape: one live-fire/re-derivation lens, one
//            domain-fidelity lens, one discipline lens (prereg-vs-code diff, quote
//            audit, claim grades, gates-can-fire).
if (!args || !args.pr || !args.context || !args.lenses || !args.lenses.length) {
  throw new Error('args required: {pr, context, lenses:[{key, prompt, run}]}')
}

const SCRATCH = '/private/tmp'

const COMMON = `You are reviewing AVE-Core PR #${args.pr}. FIRST: cd /Users/grantlindblom/AVE-staging/AVE-Core, run 'gh pr view ${args.pr} --json headRefName' to find the branch, then 'git fetch origin main <branch>'. Review the BRANCH via 'git diff origin/main...origin/<branch>' and 'git show origin/<branch>:<path>'. NEVER modify the main checkout or any tracked file. To execute code, create a throwaway git worktree under the session scratchpad (or ${SCRATCH}) and remove it when done.

CLAIM UNDER REVIEW + GROUND TRUTH:
${args.context}

STANDING DISCIPLINE (every lens):
- verify-before-cite: every quote grep-confirmed THIS turn; no quote-marks on unverified text; findings carry branch file:line + VERBATIM evidence.
- Prereg-vs-code diff: every frozen declaration (tolerances, observables, boundaries, controls) checked against the implementation as shipped; silent deviations are findings even when forced.
- Gates must be able to fire: any control/reconcile that consumes its own defining identity, uses a vacuous tolerance, or gates a proxy instead of the consumed observable is a finding.
- Claim grades are ground truth: alpha=echo, K=2G=GR-imported, nu=2/7 VALUE imported, FORM-derived only; any sentence upgradeable to a value derivation is CRITICAL. The A1-vs-T2 homonym guard is binding.
- Knife: 1/2 and 1/4 factors derived-only; visible targets may be compared against, never tuned toward; a constraint satisfied suspiciously exactly is a finding.
Report ONLY substantive findings, max 5 per lens, ranked most-severe first. Checks that PASS go in clean_report with specifics (commands run, values reproduced). Empty findings + a solid clean_report is a good outcome.

`

const FINDINGS = {
  type: 'object', required: ['findings', 'clean_report'],
  properties: {
    findings: { type: 'array', maxItems: 5, items: {
      type: 'object', required: ['title', 'severity', 'file', 'evidence', 'why_it_matters'],
      properties: {
        title: { type: 'string' },
        severity: { enum: ['CRITICAL', 'MAJOR', 'MINOR'] },
        file: { type: 'string' },
        line: { type: 'number' },
        evidence: { type: 'string', description: 'verbatim quote(s) from the branch proving the defect' },
        why_it_matters: { type: 'string' },
      } } },
    clean_report: { type: 'string', description: 'what was checked and passed, specifically' },
  },
}

const VERDICT = {
  type: 'object', required: ['verdict', 'reasoning'],
  properties: {
    verdict: { enum: ['CONFIRMED', 'DOWNGRADED', 'REFUTED'] },
    corrected_severity: { enum: ['CRITICAL', 'MAJOR', 'MINOR', 'NONE'] },
    reasoning: { type: 'string', description: 'verbatim evidence for the verdict' },
  },
}

phase('Review')
log(args.lenses.length + ' lenses over PR #' + args.pr)

const results = await pipeline(
  args.lenses,
  l => agent(COMMON + 'LENS: ' + l.prompt, {
    label: 'review:' + l.key,
    phase: 'Review',
    schema: FINDINGS,
    agentType: l.run ? undefined : 'ave-auditor',
    effort: 'high',
  }),
  async (review, l) => {
    if (!review) return null
    const fs = (review.findings || []).slice(0, 5)
    if (fs.length) log(l.key + ': ' + fs.length + ' finding(s) -> adversarial verify')
    const verified = await parallel(fs.map(f => () =>
      agent(
        COMMON +
        'ADVERSARIAL VERIFY. Try to REFUTE the finding below by reading the actual branch state, cited canon, and (if needed) running the code in a throwaway worktree. Quote verbatim evidence. Not reproducible => REFUTED; real but overstated => DOWNGRADED with corrected_severity; holds => CONFIRMED. Also apply the consensus-bias check: if the finding holds AVE to a standard the SM/textbook side would not be held to, say so. FINDING: ' +
        JSON.stringify(f),
        { label: 'verify:' + l.key, phase: 'Verify', schema: VERDICT, agentType: 'ave-auditor', effort: 'high' }
      ).then(v => ({ ...f, lens: l.key, verdict: v }))
    ))
    return { key: l.key, clean_report: review.clean_report || '', findings: verified.filter(Boolean) }
  }
)

const dims = results.filter(Boolean)
const all = dims.flatMap(r => r.findings)
const confirmed = all.filter(f => f.verdict && f.verdict.verdict !== 'REFUTED')
log('confirmed: ' + confirmed.length + ' of ' + all.length + ' findings')
return {
  pr: args.pr,
  confirmed,
  refuted_count: all.length - confirmed.length,
  clean_reports: dims.map(r => ({ lens: r.key, clean: r.clean_report })),
}
