---
name: brand-writing-detect
description: Audit a draft for AI patterns without rewriting it. Names each pattern, quotes the line, gives a one-line fix. Never scores the draft or guesses whether a model wrote it.
---

# Detect

Name the evidence. Do not rewrite, score, or guess authorship. AI detectors guess; named patterns are something the user can check.

Load `references/ai-patterns.md` before auditing.

## Workflow

1. Read the full draft.
2. Optionally run `scripts/lint.py` on the text for the regex-catchable patterns (banned words, empty phrases, em dash clusters, binary contrasts). It reads `references/word-lists.json`. Treat its output as a starting list, not the audit.
3. Walk the draft against every pattern in `references/ai-patterns.md`, including the ones a regex cannot catch: robotic rhythm, faux-insight setups, fake-profound kickers, summary-recap endings, synonym cycling, formatting slop.
4. Report findings in the format below. If nothing is found, say so in one line.
5. Offer to edit the draft after.

## Report format

One finding per line, grouped by pattern, most frequent pattern first:

```
**Binary contrast** (2)
- "This isn't about speed. It's about trust." → State the trust point directly.
- "The question isn't whether, it's when." → Say when.

**Importance puffery** (1)
- "marks a pivotal moment for the team" → State what changed.
```

End with the count of patterns and lines, nothing else. No overall score. No "this was likely written by AI."

## What is not a finding

- A banned word used deliberately in a quote or as the subject of discussion.
- An em dash or two in a long piece.
- A fragment or spoken rhythm that is clearly the writer's own voice.
- Strong opinions, profanity, or humor.

When in doubt, leave it out. False positives cost the user trust; a missed pattern costs one edit.
