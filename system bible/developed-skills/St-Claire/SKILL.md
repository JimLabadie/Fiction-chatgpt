---
name: st-claire
description: "Operational entry point for the reusable St. Claire shared-world module. Load this skill whenever a story, scene, character, organization, place, culture question, membership question, identity/egg/trans question, or St. Claire-specific mechanic touches the district."
---

# St. Claire

This directory is the operational St. Claire shared-world module. `system bible/07-st-claire.md` is a router/legacy partial snapshot and must not be treated as the complete authority when this developed skill is available.

## Authority and loading order

1. `St Claire 00 Concept.md` — source of truth for St. Claire lore, values, institutional design, and settled world reasoning.
2. `St Claire 00B Rules and Mechanics.md` — source of truth for generative mechanics, thresholds, behavioral rules, checks, and exceptions. If a downstream file conflicts with Concept or Rules & Mechanics, the downstream file is corrected rather than overriding them.
3. Structured data files — Population, Households, Organizations, Places, Founding Pioneers, History, and other numbered modules — provide the established facts used to instantiate the world.
4. `St Claire Master Lore Compendium v3.md` is recovery/source material (a quarry), not the maintained operational authority once material has been promoted into the structured documents.
5. Story-local bibles and state may select, instantiate, or deliberately vary reusable St. Claire material within their story scope, but they do not silently rewrite the shared-world baseline.

## Mandatory pre-prose loading

Before generating prose set in St. Claire, load the files needed to answer every consequential world question raised by the prompt. Do not infer a missing consequential fact merely to begin writing.

Always load `St Claire 00B Rules and Mechanics.md` before prose when the prompt touches any of the following:

- gender identity, trans status, egg/questioning status, or identity recognition;
- membership eligibility or adulthood thresholds;
- St. Claire pull, inverse-pull, belonging, staying/leaving, or voluntary transformation mechanics;
- exceptions to a St. Claire rule;
- marriage/household eligibility where membership rules matter;
- any trigger whose outcome changes depending on an unstated character-state fact.

Also load `St Claire 00 Concept.md` whenever the scene depends on the meaning, purpose, culture, or narrative expression of one of those mechanics rather than only its checkable trigger.

## Structured references

Use the narrowest established data file that owns the requested fact:

- `St Claire 03 Population.md` — residents and demographic data.
- `St Claire 04 Households.md` — household structures and established household facts.
- `St Claire 05 Organizations.md` — primary businesses and organizations, including staffing/ownership where established.
- `St Claire 05A Recovered Organizations.md` — source-established organizations and civic functions recovered after consolidation dropped them from the maintained Organizations dataset; load alongside 05 for organization/entity resolution.
- `St Claire 05B Organization Needs.md` — current structural business/organization needs audit. Use it when creating, assessing, or proposing St. Claire businesses so development fills real functional/density gaps rather than duplicating existing institutions.
- `St Claire 05C Ordinary Commerce Expansion.md` — established ordinary businesses added by the closed-structure audit: household repair/service, laundry, moving, end-of-life, optometry/PT, ordinary retail, fabrication/production, insurance, and additional food/drink density. Load alongside 05 and 05A for organization/entity resolution.
- `St Claire 06 Places.md` — locations and physical place records.
- `St Claire 01 Founding Pioneers.md` and `St Claire 00D History.md` — founding figures and historical timeline.
- `St Claire 99 MASTER TRACKER.md` — unresolved development items; it does not override settled Concept or Mechanics.

When a scene uses a named establishment such as Blush, load its Organizations/Places material in addition to any mechanics implicated by the character or event. When resolving any St. Claire organization, search `St Claire 05 Organizations.md`, `St Claire 05A Recovered Organizations.md`, and `St Claire 05C Ordinary Commerce Expansion.md` before concluding that the entity is absent or asking Jim to define it. When the task is to create or assess a new organization, also load `St Claire 05B Organization Needs.md` and prefer an established unmet function over redundant proliferation.

## Ambiguity gate

Apply the project-wide ambiguity gate before prose. A fact is blocking when different possible values would select materially different St. Claire rules or outcomes. Omission is not permission to choose a value.

For example, `straight male` establishes a stated gender description and sexual orientation. It does **not** by itself establish cis status, trans status, egg status, or non-egg status. If those distinctions select different St. Claire mechanics, clarify the missing state unless Jim has deliberately established it as unknown while separately supplying the controlling truth.

If Jim establishes that a fact is unknown on page but known in canon, preserve both layers: the prose must respect the canonical truth without giving the character or reader knowledge they have not earned.

## Scene workflow

1. Identify the St. Claire locations, institutions, people, and mechanics implicated by the request.
2. Load Concept/Rules & Mechanics and the relevant structured data files.
3. Run the ambiguity gate against all trigger inputs and consequential character-state facts.
4. If a blocking fact is missing, ask Jim rather than generating prose.
5. If the canonical fact is known but intentionally unknown on page, generate from the canonical state while preserving character/reader knowledge boundaries.
6. Keep story-specific outcomes in story state; do not promote them back into this shared module unless Jim explicitly does so.
