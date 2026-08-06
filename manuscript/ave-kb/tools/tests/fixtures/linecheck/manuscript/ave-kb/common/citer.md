[↑ Parent](index.md)

# Line-cite fixture — ERROR SOURCE (manuscript/ave-kb/, gates)

Every line below is a deliberate case for `check_line_cites`. Line numbers in
this file are asserted by the test, so do not reflow it.

OK backticked, content line: `target.md:5`
DEAD backticked, past EOF: `target.md:999`
BOGUS path, backticked: `no-such-file-anywhere.md:12`
BLANK cited line: `target.md:12`
DECORATION-only cited line: `target.md:18`
OK link-ext (KB house style): [target](target.md):5
DEAD link-ext: [target](target.md):999
DEAD link-in: [target](target.md:998)
OK range: `target.md:5-9`
DEAD range end (start is in range, end is not): `target.md:28-44`
OK parent-dir hop: `../../../src/tool.py:5`
DEAD parent-dir hop: `../../../src/tool.py:999`
HISTORICAL PIN — correct as written against `abc1234`: `target.md:999`
ELISION pattern, unresolvable by shape: `vol9/.../gone.md:4`
SIBLING repo, absent on a fresh checkout: `AVE-HOPF/docs/glossary.md:9`
HOME dir: `~/.claude/notes.md:3`
AMBIGUOUS basename — the vol9 twin is 400 lines, so this is NOT dead: `twin.md:300`
AMBIGUOUS basename past BOTH candidates: `twin.md:900`
PATH ONLY, no line: `target.md`
NOT A CITE, just prose in backticks: `the quick brown fox`

A fenced block's cites are illustrative and must never be extracted:

```markdown
see `target.md:999` and [t](target.md):999
```
