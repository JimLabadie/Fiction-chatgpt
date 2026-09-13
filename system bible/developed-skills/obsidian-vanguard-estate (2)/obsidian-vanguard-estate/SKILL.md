---
name: obsidian-vanguard-estate
description: "Reusable location reference for the Obsidian-Vanguard Estate — a converted 650,000 sq ft former mall on 42.5 acres, fully mapped down to wings, room-by-room layout, and staffing. Use whenever a story places characters at this estate, needs a scene set there, or needs to reuse it as a home/setting in a new or different story than the one it originated in. Also use when the user wants to add/modify a room, resolve a square-footage or layout question, or staff the property. Covers architecture and staffing ONLY — does NOT cover the household's private wealth/financial structure, which is intentionally a separate, non-bundled document. Trigger this any time 'Obsidian-Vanguard,' 'the estate,' or a description matching this property comes up, even if the user doesn't name the skill directly."
---

# Obsidian-Vanguard Estate

A reusable physical setting: a former upscale mall (the Galleria at University Park) converted into a 650,000 sq ft private residence on 42.5 acres. The building is fixed canon across every story that uses it. The household living in it is not — each story fills that in separately.

## What This Skill Covers (and What It Doesn't)

Covers the **physical property**: room-by-room architecture, wing layout, space accounting, grounds, and the staffing plan required to run it. This is location infrastructure, not character or plot content.

Does **not** cover:
- The household's private wealth, investment structure, or financial tiers — that lives in a separate document outside this skill and should never be pulled in here.
- Swap/change mechanics, character identity, or continuity tracking — that's the `change-worldbuilding-toolkit` skill's job. This skill and that one are independent; a story can use either, both, or neither.

## Files in This Skill

- `references/estate-master-plan.md` — the architecture: property overview, grounds, wing-by-wing layout, space accounting. Section 1 ("The Family Sanctuary & Master Quarters") has bracketed fields for the current story's household — who the anchor is, how many people live there, suite usage. Everything else is fixed and should not be altered without the user explicitly asking to modify the building itself.
- `references/estate-staffing-plan.md` — staffing plan (roles, headcounts, comp) sized to the physical plant. Already story-agnostic; use as-is unless the story's household size changes staffing needs materially (e.g., a much larger or smaller family changing childcare/housekeeping headcount).

## The Estate's House-Wide Intelligence

Estate technology described here — the Cascade Array's biometric-reading fixtures, the Wardrobe Intelligence System, staff notification systems — is natural territory for a single, sentient, house-wide intelligence to actually be running underneath, rather than a collection of separate smart-home features. If a story also uses `fashion-empire`, that skill's `references/athena-the-algorithm.md` covers exactly this entity: the same sentient system the empire's capital-deployment algorithm already is, extended to cover estate operations. Treat it as one entity across both domains rather than two coincidentally similar systems. A story using this estate skill without `fashion-empire` can simply leave the house's systems as ordinary (non-sentient) smart-home technology — the sentience angle is an optional layer, not a requirement of using this estate.

Separately, and independent of whether a story gives the house a sentient intelligence at all: the Anchor's and Partner Dressing Rooms' concealed retrieval-and-dressing stations, and the Grand Wardrobe Complex's robotic tailoring units, are `fashion-empire`'s Threadbourne Robotics technology (see that skill's `references/threadbourne-robotics.md` and its individual product manifests) — a real, commercially-sold robotics product, not an extension of Athena's own sentience. A story can use one, both, or neither of these `fashion-empire` layers without the others.

## Workflow

1. **New story wants to use this estate:** read `estate-master-plan.md` first. This file describes a *building*, not a relationship structure — the floor plan (one anchor suite flanked by multiple partner suites) happens to read naturally as a multi-partner household, but using this estate does not by itself mean a story is polyamorous. Ask the user directly: who the anchor is, who currently lives with them, and what the relationship structure actually is for this story (polyamorous household, a single couple using only part of the wing, etc.) — don't assume either way, and don't carry over a previous story's household roster or relationship structure. Fill Section 1's bracket accordingly once confirmed. Note that suite/shower/closet capacity is fixed, oversized architecture independent of headcount (built for a much larger family than any story needs to start with) — a small starting household doesn't require shrinking those numbers, and a growing household doesn't require expanding them.
2. **Scene set at the estate:** pull the relevant wing's details from `estate-master-plan.md` for physical accuracy (square footage, room contents, adjacency) rather than inventing layout details on the fly.
3. **Staffing comes up on-page** (a butler, a security officer, a stylist): check `estate-staffing-plan.md` for role, realistic headcount, and how that role would plausibly interact with the household day to day.
4. **A financial/wealth question comes up:** this skill doesn't cover it. Flag that it's out of scope here and ask the user for the relevant document rather than inventing wealth details.
5. **The user wants to add or change something about the building itself** (a new wing, a different total square footage): treat `estate-master-plan.md` as the living original — update it in place as though the change was always true, the same convention used elsewhere in this user's projects. Confirm the change with the user before writing it.
