# Track State

Status: PROTOTYPE — NON-GOVERNING
Purpose: Keep mutable project/story state synchronized with established events and elapsed time.

## Use when
An event changes a roster, body/identity occupancy, awareness, adaptation, inventory, relationship, schedule, precedent, continuity field, or other explicitly tracked state.

## Temporal state invariant
Story time is first-class mutable state, not connective inference. Track the smallest supported temporal position at the precision actually established: calendar date if known, story-relative day, daypart/time if known, sequence relative to anchored events, elapsed duration when established, and explicit unknowns.

A chapter/scene boundary does **not** imply a new day. "Next chapter," "later," "afterward," and similar narrative sequencing may advance narrative position without advancing calendar/story day. Never increase temporal precision by invention.

## Procedure
1. Retrieve the authoritative current state and applicable event/mechanic.
2. Resolve the temporal delta before other propagation: previous temporal anchor; event temporal anchor; whether time advanced; supported elapsed duration/day/date/daypart precision; and any temporal field that remains unknown. If only narrative order is known, preserve narrative order without inventing a clock/day/date.
3. Identify exactly which tracked fields the established event changes.
4. Apply the smallest state delta supported by the event.
5. Preserve unchanged fields; do not infer collateral changes.
6. Update all directly dependent trackers in the same work session when persistence is authorized.
7. Record effective story time/chapter/event at the greatest supported precision; explicitly preserve unknown clock/date/daypart fields rather than filling them from narrative sequence.
8. Verify cross-tracker consistency: identity/occupancy, knowledge/awareness, adaptation/competence, objects/inventory, and precedent must not contradict one another.
9. If two authoritative trackers disagree, stop and hand the conflict to reconciliation rather than choosing silently.
10. Persistence is not complete until the authorized destination is written and verified.

## Guardrails
Tracking records what happened; it does not invent what happened.
