# Track State

Status: PROTOTYPE — NON-GOVERNING
Purpose: Keep mutable project/story state synchronized with established events and elapsed time.

## Use when
An event changes a roster, body/identity occupancy, awareness, adaptation, inventory, relationship, schedule, precedent, continuity field, or other explicitly tracked state.

## Procedure
1. Retrieve the authoritative current state and applicable event/mechanic.
2. Identify exactly which tracked fields the established event changes.
3. Apply the smallest state delta supported by the event.
4. Preserve unchanged fields; do not infer collateral changes.
5. Update all directly dependent trackers in the same work session when persistence is authorized.
6. Record effective story time/chapter/event when relevant.
7. Verify cross-tracker consistency: identity/occupancy, knowledge/awareness, adaptation/competence, objects/inventory, and precedent must not contradict one another.
8. If two authoritative trackers disagree, stop and hand the conflict to reconciliation rather than choosing silently.
9. Persistence is not complete until the authorized destination is written and verified.

## Guardrails
Tracking records what happened; it does not invent what happened.
