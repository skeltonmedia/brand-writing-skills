---
name: brand-writing
description: Make writing sound like a person, not like AI. Edit a draft with the smallest change that removes AI patterns and keeps the writer's voice; detect and name AI patterns without rewriting; or turn project notes into evidence-backed proof points for a resume, portfolio, post, or sales page. Use when a draft reads generic, when someone asks "is this AI slop", or when work needs to become claims with evidence.
version: 0.1.0
---

# Brand Writing

Product index. Read `intake/SKILL.md` first; it routes the request to one of three sub-skills.

| Sub-skill | Use when | Returns |
|---|---|---|
| `edit/` | The user wants a draft fixed | The edited draft plus a What changed section |
| `detect/` | The user asks whether a piece reads as AI, or wants an audit without a rewrite | Named patterns, quoted lines, one-line fixes |
| `proof-points/` | The user wants work turned into claims with evidence | A proof note in the fixed format |

Shared references, loaded only when a sub-skill asks for them:

- `references/ai-patterns.md`: the named patterns with examples and fixes.
- `references/word-lists.json`: banned words, empty adverbs, empty phrases. The lint script reads this file.
- `references/voice-preservation.md`: how to keep the writer's voice while editing.
- `references/proof-block-format.md`: the proof note schema and audience variants.
- `references/examples/`: before and after pairs.

Rules that apply to every sub-skill:

1. Never invent claims, examples, numbers, or opinions. Ask when something is unclear.
2. The writer's voice outranks polish. A rough draft with a real voice should still sound like the same person after.
3. Do not guess whether a human or a model wrote the draft. Name patterns; they are evidence the user can check.
