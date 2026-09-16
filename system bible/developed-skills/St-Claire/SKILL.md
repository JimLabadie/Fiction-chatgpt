---
name: st-claire
description: "Operational entry point for the reusable St. Claire shared-world module. Load this skill whenever a story, scene, character, organization, place, culture question, membership question, identity/egg/trans question, or St. Claire-specific mechanic touches the district."
---

# St. Claire

This directory is the operational St. Claire shared-world module. `system bible/07-st-claire.md` is a router/legacy partial snapshot and must not be treated as the complete authority when this developed skill is available.

## Authority and loading order

1. `St Claire 00 Concept.md` — source of truth for St. Claire lore, values, institutional design, and settled world reasoning.
2. `St Claire 00B Rules and Mechanics.md` — source of truth for generative mechanics, thresholds, behavioral rules, checks, and exceptions.
3. `St Claire 00E Population and Staffing Integration.md` — active mechanics extension for population-first staffing, partner/household completion, existing-resident reuse, and household employment dispersion. Load it for all population or staffing creation/audits. If 00E appears to conflict with 00B, stop and reconcile rather than silently choosing one.
4. Structured data files — Population, Households, Organizations, Places, Founding Pioneers, History, and other numbered modules — provide the established facts used to instantiate the world.
5. `St Claire Master Lore Compendium v3.md` is recovery/source material (a quarry), not maintained operational authority once material has been promoted.
6. Story-local bibles and state may select, instantiate, or deliberately vary reusable St. Claire material within their story scope, but they do not silently rewrite the shared-world baseline.

## Mandatory pre-prose loading

Before generating prose set in St. Claire, load the files needed to answer every consequential world question raised by the prompt. Do not infer a missing consequential fact merely to begin writing.

Always load `St Claire 00B Rules and Mechanics.md` before prose when the prompt touches gender identity, trans/egg/questioning status, membership, St. Claire pull/inverse-pull, belonging, transformation, exceptions, marriage/household eligibility, or any trigger whose outcome changes with an unstated character-state fact. Load `St Claire 00 Concept.md` when meaning, culture, or narrative expression of those mechanics matters.

For any task that creates, assigns, audits, or resolves residents, employees, partners, household members, occupations, or organization staffing, also load `St Claire 00E Population and Staffing Integration.md`.

## Structured references

- `St Claire 03 Population.md` — primary residents and demographic data.
- `St Claire 04 Households.md` — household structures and established household facts.
- `St Claire 05 Organizations.md` — primary businesses and organizations, including staffing/ownership where established.
- `St Claire 05A Recovered Organizations.md` — recovered source-established organizations/civic functions.
- `St Claire 05B Organization Needs.md` — current structural business/organization needs audit and stop rule.
- `St Claire 05C Ordinary Commerce Expansion.md` — established ordinary businesses added by the closed-structure audit.
- `St Claire 05D Density Completion.md` — final specialty-retail additions used to reach minimum density targets.
- `St Claire 05E Scene-Ready Staffing.md` — incremental named staffing beginning with Hearth & Home Service Cooperative.
- `St Claire 05F Scene-Ready Staffing Batch 2.md` — incremental named staffing for Washday Laundry & Cleaners and St. Claire Moving & Delivery.
- `St Claire 05E2 Scene-Ready Staffing - Professional Services.md` — incremental named staffing for Quiet Harbor, Clearview, and Physical Therapy.
- `St Claire 06 Places.md` — locations and physical place records.
- `St Claire 01 Founding Pioneers.md` and `St Claire 00D History.md` — founding figures and historical timeline.
- `St Claire 99 MASTER TRACKER.md` — unresolved development items; does not override settled Concept or Mechanics.

### Population and staffing resolution

`St Claire 03 Population.md` remains the primary population dataset. Until incremental staffing records are physically consolidated into Population, all active 05-series staffing files are also authoritative named-person records and must be searched for duplicate names, demographics, relationships, schedules, and scene presence.

Before creating a worker, search the existing population and household ecology as required by 00E. Existing unemployed, underemployed, part-time, between-job, apprenticeship-seeking, retired-but-working, or otherwise available residents must be considered before a new resident is invented. Existing character agency and established career facts are not overwritten merely to fill a vacancy.

A named partner or household member is a population obligation, not a relationship placeholder. Resolve that person to an existing complete record or create the complete record, including occupation/employment state. Partners do not inherit one another's workplace.

For small businesses, default to household employment dispersion: members of the same household normally work in different workplaces and maintain independent professional/social networks. Shared employment requires a concrete established reason such as a genuinely family-run business, co-founded practice, succession/apprenticeship, temporary coverage, or other specific history.

A business is fully scene-ready only when ordinary operating coverage resolves to named complete people **and** every named adult household member introduced through those workers has been population-integrated. An unnamed staffing slot or unresolved named partner is a development gap, not permission to invent a convenience NPC during prose.

The Hearth & Home, Washday, Moving & Delivery, Quiet Harbor, Clearview, and Physical Therapy staffing batches predate the population-first integration mechanic. Treat them as `STAFF-COMPLETE / POPULATION-INTEGRATION-PENDING` until the 00E repair audit resolves their workers, partners, households, existing-resident reuse, co-employment, and aggregate demographic checks. Do not create the next staffing batch before that repair is complete.

When a scene uses a named establishment, load its Organizations/Places material plus applicable staffing file. At a specified date/time, use established schedules plus story state to determine who is plausibly present; employees are not permanently installed at workplaces.

When resolving any St. Claire organization, search 05, 05A, 05C, and 05D before concluding it is absent or asking Jim to define it. When creating/assessing a new organization, load 05B first; do not add organizations merely for generic structural completeness when current density and closed-structure tests already pass.

## Ambiguity gate

Apply the project-wide ambiguity gate before prose. A fact is blocking when different possible values select materially different St. Claire rules or outcomes. Omission is not permission to choose a value.

For example, `straight male` establishes a stated gender description and sexual orientation. It does not establish cis, trans, egg, or non-egg status. If those distinctions select different mechanics, clarify unless Jim has deliberately established the controlling truth while keeping it unknown on page.

If a fact is known in canon but intentionally unknown on page, preserve both layers: prose respects canonical truth without leaking knowledge to character or reader.

## Scene workflow

1. Identify implicated St. Claire locations, institutions, people, households, and mechanics.
2. Load Concept/Rules & Mechanics and relevant structured data; load 00E for population/staffing work.
3. Run the ambiguity gate against trigger inputs and consequential character-state facts.
4. Resolve named staff and actual schedule coverage for the scene's day/time rather than inventing workers.
5. Resolve any named relationship/household references to actual complete residents; do not create relationship-only placeholders.
6. If a blocking fact is missing, ask Jim rather than generating prose.
7. If canonical fact is known but intentionally unknown on page, generate from canonical state while preserving knowledge boundaries.
8. Keep story-specific outcomes in story state; do not promote them back into the shared module unless Jim explicitly does so.
