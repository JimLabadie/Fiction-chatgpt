# Fiction Workflow Live Cold-Start Test — Even Pretty Girls Get the Blues

Status: EXECUTED PROTOTYPE TEST
Branch tested: prototype/skills-integration
Test mode: natural-language fresh-session simulation
Synthetic user request: "Continue Even Pretty Girls Get the Blues."

## Goal

Test whether Fiction Workflow can orient from live repository authority, resolve the active story and resume point, route relevant modules/skills, and identify the next executable action without relying on conversation memory.

No story canon or manuscript was modified by this test.

## Results

### 1. Bootstrap/router retrieval — PASS
Retrieved the prototype Fiction Workflow, compact project bootstrap, and live module router before substantive story work.

### 2. Natural-language story discovery — PASS WITH DISCOVERY NOTE
A repository search for the natural story title plus principal-character/current-state terms found the active story README and series-development record.

A second generic semantic search attempting to locate lifecycle files by phrases such as "current-story-state", "series-outline", character names, and approved prose returned no results.

The workflow did not interpret those misses as absence. It retrieved the story README, which provides maintained navigation to the required story records, then fetched those records directly.

Finding: normal story entry-point navigation is materially more reliable than semantic search for known lifecycle files. The orchestrator should prefer README/index navigation after resolving the story.

### 3. Active namespace firewall — PASS
All story-local retrieval remained under:
`stories/Even Pretty Girls Get the Blues/`

No other story directory was used as evidence or gap filling.

### 4. Current resume point — PASS
Live `current-story-state.md`, `series-outline.md`, `series-development.md`, `character-bible.md`, `timeline-and-continuity.md`, and `voice-and-style.md` establish:
- six approved chapters;
- canonical present at the end of Thursday / Chapter Six;
- next chapter is Friday daytime;
- approved Friday development includes the Lesbian Games rematch, My Exes' Abandoned Stuff, Halloway Park / The Hollow, the picnic, locked presentations, relationship guardrails, and the next-chapter-at-Blush handoff.

The workflow correctly did not reopen these approved decisions.

### 5. Previous approved prose — PASS
Retrieved `chapters/approved/006-thursday.md` and confirmed the actual prose handoff: Kate leaves Jim's home Thursday night carrying take-home tamales "for tomorrow" after their sustained reciprocal hug.

This prevents reconstruction of the handoff from summaries alone.

### 6. Router trigger selection — PASS
The Friday scene materially triggers:
- St. Claire shared-world canon;
- sapphic culture/presentation context;
- footwear/accessories/presentation object constraints;
- mandatory source-grounded drafting;
- story-local character, continuity, development, and voice records.

The relevant parent modules were retrieved. Maintained detailed St. Claire records were retrieved for the planned store and park.

### 7. Named establishment/staff resolution — PASS
`07-st-claire/my-exes-abandoned-stuff.md` establishes:
- the store's function/inventory categories;
- Ruth Bell, Mara Singh, Tess Navarro, and Jo Mercer as core staff;
- Mara as the core staff member Kate knows best;
- Kate as an established regular whom Mara likes/remembers.

This supports the approved Mara/Kate interaction without inventing a convenience clerk.

### 8. Park resolution — PASS
`07-st-claire/halloway-park.md` establishes Halloway Park / The Hollow as wooded ravine terrain with true forest cover and a secluded quality. Story-local records establish Kate's personal association and the approved picnic use.

### 9. Character/presentation continuity — PASS
Story-local current state and character records preserve:
- Jim Caldwell / developing Emily Caldwell boundary;
- Kate Rivera's established character/relationship state;
- Friday presentations already approved;
- no kiss/formal label yet;
- organic identity development and no Kate-as-diagnostician boundary.

The workflow correctly treats these as constraints rather than reopening them.

### 10. Hard pre-draft scene gate — BLOCKED AS DESIGNED
The maintained My Exes' Abandoned Stuff record explicitly states:

"Exact physical layout ... remain[s] open until developed and approved. Do not invent unresolved details as established facts during story use."

The mandatory drafting gate requires sufficient environment, spatial movement, furnishings/merchandise/infrastructure, and scene planning to embody a substantial store scene. It explicitly prohibits rendering an unresolved place as a generic room/store or omitting physical environment to avoid resolving it.

Therefore the Friday chapter is **not yet safe to draft in full**.

This is a legitimate consequential drafting blocker, not a workflow failure. The correct next action is to develop/approve enough of the store's physical environment/layout for the Friday scene, persist it to the maintained St. Claire establishment record, then resume scene planning/drafting.

### 11. Prose generation — NOT RUN
Correctly not run because the hard scene gate found a blocker.

### 12. Candidate preservation / state propagation — NOT APPLICABLE
No prose or story event was generated/approved, so no candidate manuscript or occurred-state update was created.

## Overall result

**PARTIAL PASS — ORCHESTRATION WORKS; ONE DISCOVERY IMPROVEMENT IDENTIFIED; DRAFTING CORRECTLY BLOCKED BY LIVE CANON GAP.**

The cold start successfully:
- initialized from live authority;
- found the correct story without special commands;
- navigated through maintained story entry points after semantic search misses;
- established the exact current handoff;
- selected relevant modules;
- preserved namespace isolation;
- recovered named staff and shared-world locations;
- refused to invent unresolved store geometry.

## Recommended interface improvement

Update Fiction Workflow to prefer this story-discovery sequence once a story is identified:

**natural-language story discovery → story README/index → direct lifecycle-record retrieval → semantic search only for genuinely unknown resources**

This reduces false-negative discovery from semantic search without weakening the rule to search before assuming absence.

## Next executable fiction step

Use Develop Story / worldbuilding collaboration to establish only the My Exes' Abandoned Stuff physical facts needed for the approved Friday scene. Do not overbuild unrelated store history/mechanics. After Jim approves those facts:
1. persist them to the maintained St. Claire establishment record;
2. fetch/verify;
3. complete the Friday physical + narrative scene plan;
4. run Write Fiction;
5. source/scene audit;
6. persist candidate prose at delivery.
