# Persist

Status: PROTOTYPE — NON-GOVERNING
Purpose: Make an authorized project-state change durable in its correct authoritative destination and prove that the durable artifact contains the intended change.

## Use when
Use when accepted or already-authoritative state must survive chat loss: canon decisions, corrections, pins/return obligations, resolved conflicts, continuity/state changes, source-review dispositions, or approved framework changes.

Persist is not promotion authority. It writes decisions whose status/scope are already established. If status, scope, destination, or conflict disposition is unresolved, return to Reconcile or Jim before writing.

## Persistence invariant
A change is substantively persisted only when:
1. the intended accepted state exists in the correct authoritative destination;
2. required dependent authoritative records are synchronized or explicitly pinned as unfinished;
3. the repository write succeeds; and
4. the published/target artifact is fetched again and its substantive content verified.

Chat memory, summaries, source archives, routing/audit mentions, intended destinations, local drafts, and unverified commits do not satisfy this invariant.

## Procedure
1. **Resolve the payload.** State exactly what accepted/authoritative change must become durable, its status/scope, effective point/date if relevant, provenance/decision context, and affected conflicts.
2. **Resolve the authoritative destination.** Use current governance and namespace ownership. Do not choose a convenient file merely because it mentions the subject.
3. **Read before write.** Fetch the current target and relevant dependent records. Preserve unrelated content, provenance, open fields, and current structure.
4. **Plan propagation.** Identify every authoritative record directly made stale by this change: reusable component, Character Bible, Timeline, Current Story State, conflict/open-question ledger, trigger occurrence, coverage/provenance record, or other governed dependency.
5. **Apply the smallest complete edit.** Write the accepted state with required provenance/status/scope. Do not silently broaden scope, resolve additional questions, or rewrite unrelated material.
6. **Handle unfinished dependencies honestly.** If an affected dependent record cannot be updated in the same authorized operation, create/update the governing pin/open-question destination before moving on. A chat promise is not a pin.
7. **Commit/write.** Perform the actual repository mutation on the intended branch/destination. Record the resulting commit identifier.
8. **Fetch after write.** Retrieve every changed authoritative file from the target branch/revision after the write.
9. **Verify substance, not existence.** Confirm the fetched artifact contains the intended facts/rules/status/scope/provenance and that no required material was lost or contradicted. A successful API response or file count alone is insufficient.
10. **Verify propagation.** Check directly affected records for consistency. If any remain stale, persistence is PARTIAL, not complete.
11. **Report precisely.** Name the authoritative path(s), branch, verified commit(s), what was persisted, and any remaining propagation/pin. Use "persisted/saved/recorded/codified/complete" only when the corresponding verification threshold is met.

## Status results
- NOT PERSISTED — no authoritative write completed.
- WRITE UNVERIFIED — write reported success but post-write fetch/substantive check not completed.
- PARTIALLY PERSISTED — primary authoritative state verified, but required dependent propagation remains and is durably pinned.
- PERSISTED — authoritative destination and all required in-scope dependent records were written and fetched back successfully.
- COMPLETE — use only when the governing domain completion criteria, not merely this write, are satisfied.

## Promotion handling
When persisting a canon promotion, the authorization must already exist. Record the exact fact, former status, new status/scope, source/decision context, effective point/date, affected conflicts, and any superseded rule as required by governance. A GitHub write never creates promotion authority by itself.

## Guardrails
- Never claim persistence based on conversation memory or inherited summary.
- Never equate preserved source evidence with propagated project state.
- Never equate a route, audit row, recovery ledger, or intended destination with the controlling component.
- Never report a successful write as verified before fetching it back.
- Never report a local/unpublished state as remote publication.
- Never silently skip dependent state made stale by the change.
- Never invent missing fields while persisting.
- Never turn a persistence operation into an unapproved cleanup/refactor.
- Repository durability must survive a cold start without relying on ChatGPT recollection.
