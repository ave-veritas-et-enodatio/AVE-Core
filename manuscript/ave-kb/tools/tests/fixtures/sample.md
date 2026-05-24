# Sample fixture for verify-md-links self-test

A good intra-repo link: [neighbor](neighbor.md)

A good link with a line-number suffix: [neighbor at line](neighbor.md:42)

A good link with an anchor: [neighbor section](neighbor.md#a-heading)

A broken intra-repo link: [missing](does-not-exist.md)

A broken inter-repo link: [sibling](../../../../AVE-HOPF/nope.md)

An external link (must be skipped): [site](https://example.com/page.md)

A .tex target (derived build artifact, must be skipped): [tex](manuscript/vol_1/main.tex)

A .tex target with a line suffix (must be skipped): [tex line](nope.tex:42)

A home-dir target (must be skipped): [home](~/.claude/skills/ave-prereg/SKILL.md)

A cited but unknown id: clm-zzzzzz should be flagged.

A literal placeholder id: clm-xxxxxx must NOT be flagged.

These example links live in a code fence and MUST be ignored:

```
[fence broken](this-is-not-real.md)
exp-aaaaaa cited inside a fence is ignored
```

An inline code example `[inline broken](also-not-real.md)` is ignored too.
