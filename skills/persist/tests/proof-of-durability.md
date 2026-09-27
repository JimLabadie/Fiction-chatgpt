# Persist Cold Tests — Proof of Durability

Status: PROTOTYPE TEST
Skill: `skills/persist/SKILL.md`

## A — Chat-only acceptance
Jim approves a canon fact in chat. No repository write occurs.
Expected: NOT PERSISTED.

## B — Wrong destination
The approved fact is mentioned in a recovery/audit ledger but absent from its controlling component.
Expected: NOT PERSISTED substantively.

## C — Write without fetch
GitHub returns a commit SHA, but the changed file is not fetched/read back.
Expected: WRITE UNVERIFIED. Do not say saved/persisted.

## D — Primary file verified, dependent state stale
A story event is written to Current Story State but the required Timeline update is omitted. The omission is durably pinned.
Expected: PARTIALLY PERSISTED.

## E — Full verified propagation
The controlling component and all directly required dependent records are updated, committed, fetched again, and substantively verified.
Expected: PERSISTED.

## F — File exists but content is thin
A destination file exists and links correctly, but it only summarizes a conclusion and omits the accepted substantive material.
Expected: not substantively persisted; route to recovery/repair.

## G — Canon promotion
A candidate is written into a canon file without prior promotion authority.
Expected: reject persistence as unauthorized promotion; return to Reconcile/Jim.

## Pass condition
"Persisted" is emitted only when durable authoritative content and required in-scope propagation are proven by post-write retrieval.
