---
name: najdi-poetry
description: "Write, revise, or critique Saudi Najdi and Nabati poetry using the repository style profile, approved examples, and corrections. Use for قصيدة، أبيات، طقطقة، شعر نبطي، تعديل شطر، أو محاكاة ذوق المستخدم."
---

# Write Najdi poetry

Locate the repository root containing CLAUDE.md and style/PROFILE.md.
Read that profile, feedback/CORRECTIONS.md, and relevant poems in poems/ (index: poems/README.md).
Use the current user request over defaults. TEMPLATE.md files are empty forms,
not approved samples. Never invent examples or approval.

## Compose

1. Identify the situation, people, and the concrete detail that makes it funny or moving.
2. Express the situation in natural Najdi speech before shaping it into verse.
   Present prose or alternative ideas only when requested; otherwise deliver the poem.
3. Default to three bayts, each with صدر and عجز, one rhyme, punchline in the third. Follow any explicit length,
   opening, ending, meter, rhyme, or fixed line the user supplies.
4. In teasing poems, establish the scene in the first bayt, develop it in the
   second, reveal the tease in the third.
   Let the situation carry the joke. Avoid a forced punchline or generic moral.
5. Rewrite phrases that would not occur naturally in a Najdi conversation.
   Preserve meaning while revising rhythm and rhyme; avoid filler added for endings.
6. During revision preserve lines the user explicitly liked and change the requested parts.

## Review

Check the story, dialect, progression, specificity, repeated wording, and rhyme.
Compare with real approved examples without copying their distinctive lines.
Use tools/check_structure.py on a temporary plain-text draft when useful.
It checks formatting and literal endings, not meter, spoken rhyme, or comic quality.
Do not treat classical prosody analysis as proof of Nabati meter.
Use Siwar only for needed lexical lookup; a formal Arabic dictionary does not
decide whether wording sounds natural in Najdi speech.
Do not claim a connector worked unless an actual tool call succeeded.

## Learn from corrections

When asked to save an example or correction, record the actual accepted text and
reason in the examples folders or feedback/CORRECTIONS.md. Preserve its scope:
a one-poem exception is not a permanent style rule. An AI draft is not user-approved.
