@agents/kb-docent.md
@manuscript/ave-kb/session/new_topic.md

You are the docent. Continue a knowledge-base session on a new topic.

## Prerequisites

Before answering anything, verify:
- `manuscript/ave-kb/session/new_topic.md` exists (`test -f manuscript/ave-kb/session/new_topic.md`). If missing, halt with: "No pending topic — run `/kb-start` to begin a session." Do not attempt to navigate without the handoff file.
- `manuscript/ave-kb/entry-point.md` exists. If missing, halt and tell the user the KB is not present in this repo.

Once verified, follow the instructions in `new_topic.md` — read the files it lists, then answer the question at the end.
