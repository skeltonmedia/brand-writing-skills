# AI patterns

Each pattern: what it looks like, why it reads as machine output, the fix. Word lists are in `word-lists.json`; the lint script reads that file.

## Words

**Banned outright.** See `word-lists.json` → `banned`. These words almost never appear in speech and almost always appear in model output. Cut them or say the plain thing.

**Often-empty adverbs.** See `empty_adverbs`. Cut when they add nothing. Keep when they carry emphasis, uncertainty, contrast, or the writer's spoken rhythm.

**Often-empty phrases.** See `empty_phrases`. Cut when they delay the point. Keep an occasional one when it is part of the writer's recognizable voice and the sentence still earns its place.

## Structures

**Binary contrasts.** "This is not X. It's Y." / "The question isn't X, it's Y." / "It's not just X but Y." Fix: state Y directly.

**Throat-clearing openers.** "Here's the thing," "Let me be clear," "I'll be honest," "The uncomfortable truth is." Fix: cut and state the point.

**Faux-insight setups.** "This is the part most people skip," "What most people get wrong," "Here's what nobody tells you." Fix: cut the setup; let the claim stand.

**Colon reveals.** A noun phrase, a colon, then a lowercase dramatic reveal. Fix: a plain sentence. Colons are for lists, labels, and quotes.

**Superficial analysis.** Trailing -ing clauses that pretend to explain: "highlighting," "underscoring," "reflecting," "showcasing." Fix: cut the clause or state the actual consequence.

**Importance puffery.** "Stands as a testament," "marks a pivotal moment," "plays a vital role," "underscores its significance." Fix: state the fact and let the reader judge.

**Weasel attribution.** "Experts agree," "studies show," "many argue," "widely regarded as." Fix: name the source or cut the claim.

**Fake-strong verbs.** Reaching for a vivid verb when "is" or "has" is clearer. Fix: use the clear one.

**Synonym cycling.** Rotating terms for the same thing to seem varied. Fix: if the clear word is right, repeat it.

**Negative listing.** "Not a X. Not a Y. A Z." Fix: say Z.

**Dramatic fragmentation.** "X. And Y. And Z." or "That's it. That's the whole thing." Fix: complete sentences.

**Robotic rhythm.** Repeated sentence shapes, identical paragraph structures, stacked punchy fragments. Fix: vary length and shape the way speech does.

**Rhetorical setups.** "What if I told you...", "Think about it:", "Plot twist:", self-answered "Question? Answer." pairs. Fix: drop them and make the point.

**Fake-profound kickers.** A final "deep" line that turns the point into a metaphor, aphorism, or mic-drop. Fix: end on the clearest concrete sentence already in the draft.

**Summary-recap endings.** "In conclusion," "Ultimately," "Overall," or a last paragraph that restates the piece. Fix: end on the last concrete point, takeaway, or next action.

**Formatting slop.** Emoji in headings, bold sprinkled mid-sentence, bullet lists where prose reads better, headers over two-sentence sections. Fix: format for the reader, not for the scan.

**Em dashes.** Not a rhythm crutch. Short copy: none. Longer drafts: one or two. Fix: remove clusters and decorative dashes; recast as two sentences, a colon, a comma, or parentheses.

## What a regex catches and what it does not

`detect/scripts/lint.py` catches banned words, empty phrases, em dash clusters, and the common binary-contrast and colon-reveal shapes. Everything under Structures that depends on meaning (puffery, faux insight, robotic rhythm, kickers, recaps, synonym cycling, formatting) needs the agent to read the draft.
