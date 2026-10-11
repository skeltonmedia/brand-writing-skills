# Proof block format

A proof point is a claim with its evidence attached. The chain every proof point must show:

```
source evidence -> before -> intervention -> after -> value -> reusable claim
```

Missing a link means the claim is a hypothesis or a draft, and the note must say so.

## Proof note

```markdown
---
type: proof-point
status: draft | captured | packaged | published
confidence: strong | medium | draft
audience:
tools_used: []
trigger:
proof_target: resume | portfolio | post | sales-page | case-study | internal
created: YYYY-MM-DD
---

# [Outcome-first title]

## Source evidence
- [file, link, dashboard, or message] - what it proves

## Context
Why the work mattered, in two or three sentences.

## Before
What was slow, manual, unclear, risky, fragmented, or missing.

## Intervention
What was built, designed, automated, or changed. Named tools and mechanisms.

## After
What is now possible, faster, clearer, safer, or reusable. Numbers with sources.

## Value
Speed, quality, clarity, risk, revenue, reuse. Name one or two, not all.

## Reusable claims
- Resume bullet:
- Portfolio angle:
- Post angle:
- Sales-page angle:
- Internal angle:

## Confidence notes
What is proven, what is inferred, what would strengthen it.

## Next action
Where this proof goes next.
```

## Confidence levels

- **Strong:** multiple sources, visible output, concrete before and after, clear value.
- **Medium:** good evidence, value or outcome partly inferred.
- **Draft:** promising, but evidence or outcome incomplete.

## Audience variants

**Resume bullet.** One sentence. Strong verb. System, action, value.
`Designed and ran [system] to [change], enabling [value].`

**Portfolio angle.** Situation, approach, outcome. Show reasoning, constraints, and artifact quality.

**Post angle.** Lead with the lesson.
`The useful part was not [surface artifact]. The useful part was [what changed in how work happens].`

**Sales-page angle.** Translate the proof into an offer.
`I help teams [do the thing] by turning [scattered input] into [system or loop].`

**Internal angle.** Safety, repeatability, stakeholder clarity, fit with how the organization already works.

## Evidence checklist

- Sources inspected
- Before state named
- After state named
- Output artifact linked
- Value stated without exaggeration
- Privacy and sensitivity considered
- Next use identified
