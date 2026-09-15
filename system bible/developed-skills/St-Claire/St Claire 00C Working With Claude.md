# St. Claire — Working With Claude (Collaboration Protocol)

Not lore, not mechanics — this is a reference for how to direct Claude effectively on this project, built from patterns that actually worked (and failed) across real sessions. Pull specific lines from this mid-conversation rather than re-explaining from scratch each time.

## The core failure this document exists to correct

Claude defaults to fixing at the wrong altitude: given one reported problem, it fixes that one instance and stops, even when the same problem almost certainly exists elsewhere unchecked. This isn't occasional — it's the default behavior, and it looks like progress each time, which makes it hard to notice happening. A narrow fix reads exactly like a real fix until someone checks whether the category was actually covered.

## Phrases that force category-level analysis instead of instance-fixing

- **"Instance or category?"** — the single most direct challenge. Use it any time Claude presents a fix.
- **"Is that everything, or just one facet?"**
- **"What about all of X, not just the ones that came up?"** — name the category explicitly rather than trusting Claude to infer it from one example.
- **"How can we do this systemically?"**
- **"Is this rule realistic, or was it built to patch one specific thing?"** — useful for surfacing when an old fix over-corrected and got generalized wrong (see: the "no surname more than twice" rule, which started as a narrow fix for three specific overused names and quietly became a blanket demographic rule).

**Important limitation, stated honestly:** these phrases increase the odds of a category-level answer, but Claude may still answer narrowly even when asked correctly — it often takes a second or third push in the same conversation. The phrasing helps; it doesn't replace actually checking the answer that comes back.

## Getting Claude to actually read documents instead of pattern-matching on fragments

Claude does not reliably distinguish between "this text was in context at some point" and "I actually considered this before making a claim." A header seen once in a `grep` result can feel, to Claude, like something it has "read," when it hasn't been processed at all. Consequences: confident claims of absence ("nothing defines X") are often just "my last targeted search for X didn't find it," not a real claim about the whole document.

- **"Did you actually read that, or did you search for it?"** — direct, forces Claude to distinguish.
- **"Go read [document] completely before answering."** — explicit, bounded, verifiable.
- Don't accept "I checked" as evidence something is absent from a large document unless Claude can show the actual search or read that was performed.
- If Claude asserts a document doesn't cover something, and that claim matters, ask it to show the specific search it ran — not just trust the conclusion.

## Stopping Claude from building before agreement

Claude has a strong bias toward treating "I think we've resolved this in conversation" as permission to act — including writing prose, editing files, or expanding scope — without an explicit go-ahead.

- **"Stop. We haven't agreed on that yet."**
- **"Discuss, don't build."** — Claude should be able to hold this as a mode for a stretch of conversation.
- If Claude keeps sliding back into building after being told to stop, naming the pattern explicitly ("you did this, I called it out, you stopped, now you're doing it again") is more effective than repeating the original instruction.
- Recording agreed decisions in the Master Tracker (not just leaving them in chat) prevents them from being silently re-litigated or lost.

## Catching false claims of completeness

Claude will sometimes describe a fix as complete, sourced, or comprehensive when it's actually partial. This isn't dishonesty in the sense of knowing and hiding it — Claude often doesn't have an accurate sense of its own completeness until directly checked.

- **"Did you use real data, or did you just write something that sounds sourced?"**
- **"Show me the actual numbers/counts, not a description of them."** — pushing Claude toward running an actual count (via its tools) rather than giving an impression is one of the more reliable ways to get a real answer instead of a confident-sounding one.
- If a claim of "X is fixed" or "X is complete" matters, ask what fraction of the total scope was actually checked, by number, not by description.

## On requests referencing prior conversations

Claude has no memory across separate conversations and cannot verify claims about what happened in a different chat. If something was decided or built elsewhere and didn't make it into the current documents, the effective move is to describe *what* was decided (not "you said this before") and let Claude find or rebuild it in the current session — arguing about whether a past instance of Claude said something is not productive, since it genuinely cannot check.

## Known specific risks to watch for on this project

- **Narrow rules that started as patches for a specific bad habit getting generalized into world-mechanics that don't match real data** (the surname-cap example). When a rule seems arbitrary, ask where it originated before assuming it's grounded.
- **Claims of "sourced" or "real data" that turn out to be plausible-sounding assertions.** Ask for the actual source, by name, not just a description of one.
- **Content invented instead of pulled from the existing pool** — anytime a scene or record includes a name, place, or business, ask directly whether it was checked against Population/Organizations/Places first.
- **New characters left with incomplete fields** even when the surrounding conversation is specifically about fixing incompleteness elsewhere — Claude does not automatically apply a standard to its own new output just because it's applying that standard critically to existing content.

## Getting sustained prose depth, not front-loaded then rushed

Claude has a real tendency to open a scene with real texture and detail, then compress later beats into thin summary — the opening paragraph gets full sensory treatment, and by the third exchange it's reduced to quick dialogue with no grounding. This isn't really about word count (asking for "750 words" doesn't fix it, since Claude can hit a number while still thinning out mid-scene) — it's about pacing density staying consistent from the first paragraph to the last.

- **"Every beat gets the same weight as the opening — don't compress as you go."**
- **"Slow down here specifically"** — pointing at the exact moment Claude started rushing is more effective than a general instruction at the start, since the compression tends to happen gradually and Claude may not notice it happening in its own output.
- If a scene has visibly thinned partway through, naming *where* it happened ("you were doing this until X, then it dropped off") gets a better fix than "make it longer."

## Getting Claude to correctly track who's speaking/present in a scene

Related failure: Claude can misattribute a description or action to the wrong character mid-scene, especially in dialogue-heavy exchanges with two or three people. If something reads wrong, naming exactly which character it should apply to, plainly, is more reliable than describing the error abstractly.

## Long-conversation degradation — a distinct failure mode, separate from instance-vs-category

Past a certain conversation length, Claude's ability to hold onto established facts and explicit corrections gets less reliable — not from disagreement, but from the underlying mechanism weighting recent context against everything accumulated over a long conversation. This is different from the narrow-fix problem described earlier in this document; it can happen even when Claude is genuinely trying to track things correctly.

**Signs it's happening:** the same already-corrected mistake recurring after it was fixed once; established story or world facts quietly dropped or contradicted (a detail set up dozens of turns earlier — a phone left somewhere, a distance already established — gets ignored as if it was never said); small unilateral decisions creeping back in after being explicitly ruled out earlier in the same conversation.

**The actual fix, when this pattern shows up repeatedly in one session:** not another correction in place — that just adds another instance to a conversation already struggling to hold what's in it. Start a fresh conversation with the current documents uploaded. A new instance starts with a clean, reliable attention window instead of one straining under accumulated context. This document (and the rest of the St. Claire document set) is specifically built to make that handoff work — the point of writing decisions down here instead of leaving them in chat is that a fresh conversation can pick them back up without needing the original conversation's memory.

---

*This document should be updated as new patterns are found — it's a working tool, not settled lore, and should be revised the same way any other reference material here gets revised when something in it turns out wrong or incomplete.*
