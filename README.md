# Brand Writing Skills

Make your AI assistant write like a person, not like a press release.

Three skills in one folder, in the open Agent Skills format. They run in Claude Code, Codex, Cursor, and any agent that reads `SKILL.md` files.

- **edit**: fixes a draft with the smallest change that removes AI patterns and keeps the writer's voice.
- **detect**: names every AI pattern in a draft, quotes the line, gives the fix. No rewrite.
- **proof-points**: turns project notes into evidence-backed claims for a resume, portfolio, post, or sales page.

An `intake` router sends a request to the right one.

## Install

Claude Code, personal:

```bash
git clone https://github.com/skeltonmedia/brand-writing-skills
cp -r brand-writing-skills/skills/brand-writing ~/.claude/skills/
```

For one Claude Code project, copy the same folder to `.claude/skills/` in the repo.

For Codex and Cursor, copy the folder anywhere in the project and point `AGENTS.md` at `skills/brand-writing/SKILL.md`.

Then ask: "edit this for AI slop", "is this AI slop", or "turn these notes into proof points".

## Lint without an agent

The detect skill ships a plain script for the parts a regex can catch (banned words, empty phrases, em dash clusters, binary contrasts):

```bash
python3 skills/brand-writing/detect/scripts/lint.py draft.md
```

Exit code 1 when it finds something. Use it as a pre-commit or CI check on copy.

## Test

```bash
python3 skills/brand-writing/testing/check.py
```

Runs the lint against fixtures and checks every `SKILL.md` has frontmatter and stays under 500 lines.

## What it will not do

It does not guess whether a human or a model wrote the draft. Detectors guess. Named patterns are evidence you can check yourself.

## Want this on your own brand?

The free pack is generic. The paid version encodes your brand guidelines, voice, and examples so every agent in your company writes on brand. Details at skeltonmedia.com.

MIT license. Built by David Skelton, Skelton Media.
