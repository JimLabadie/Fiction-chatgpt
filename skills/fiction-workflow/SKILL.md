# Fiction Workflow

Status: PROTOTYPE — NON-GOVERNING
Purpose: Orchestrate fiction work by selecting and sequencing the appropriate skills, repository sources, gates, persistence steps, and stopping conditions without re-implementing the specialist procedures it calls.

## Use when

Use for substantive fiction work, including:
- continuing an existing story;
- developing a scene/chapter/arc;
- writing or revising prose;
- continuity/state repair;
- character/world/presentation/transformation questions tied to story work;
- source recovery affecting fiction;
- story initialization;
- framework-aware fiction tasks that require more than one skill.

This skill owns workflow selection and sequencing. It does not own canon facts, creative decisions, character simulation, prose, recovery, reconciliation, persistence, or audit logic.

## Operating principle

The orchestrator answers:

**What job is Jim asking for, what authoritative context must be loaded, which skills own each part, in what order should they run, where must the workflow stop, and what must be persisted/verified before the task is truly complete?**

It must stay thin. Specialist behavior belongs in specialist skills.

## Entry contract

For substantive fiction work:

1. Retrieve the current live project bootstrap/operating contract.
2. Retrieve the current module router.
3. Resolve the active story or determine that the task is story-agnostic/framework-level. Once an existing story is identified, prefer its maintained README/index/navigation to discover standard lifecycle records; use semantic/repository search for genuinely unknown resources rather than treating search misses as absence.
4. Resolve the current temporal frontier at the precision supported by story authority: current story-relative day/date if known, daypart/time if known, and sequence relative to the last anchored event. Do not infer a new day from a new chapter/scene.
5. Respect the active-story namespace firewall.
6. Retrieve authoritative story-local records and all router-triggered System Bible modules relevant to the requested job.
7. Do not substitute memory, summaries, previously loaded fragments, or another story's material when live authority is available.

Jim should not need to know filenames, skill names, module numbers, lifecycle commands, or persistence mechanics.

## Workflow classification

Classify the request by the work actually needed. More than one class may apply.

### A. Current-state / continuity question
Use when asking what is currently true, what happened, where characters are, what they know, what they have, or what state a story is in.

Typical sequence:
- retrieve active story authority;
- Track State only if an actual state update is requested;
- Reconcile if authoritative records disagree;
- Recover if evidence/provenance is inadequate;
- Audit if Jim asks whether records are complete/correct.

Do not use Develop Story merely to answer current-state facts.

### B. Character behavior / response
Typical sequence:
- retrieve character/current state;
- Contextualize / Inhabit / Present / Transform as triggered;
- Simulate Character;
- Develop Story only if selection among plausible responses would create story direction.

### C. Story development / brainstorming
Typical sequence:
- retrieve current state, outline, development/ideas, characters, routed modules;
- Recover/Reconcile only when prior material or status is uncertain;
- Simulate Character and domain skills to constrain options;
- Develop Story;
- Persist approved/deferred/rejected/pinned development when governance requires.

### D. Prose drafting / continuation
Typical sequence:
- retrieve router, story records, previous approved prose, current handoff, character records, routed modules;
- Develop Story if the scene is not already sufficiently planned;
- Simulate Character and domain skills as needed;
- Write Fiction;
- persist candidate prose immediately when governance requires;
- after Jim approval, Track State + Persist occurred consequences;
- Audit/source-fidelity gate before delivery and/or after persistence as required.

### E. Prose revision
Typical sequence:
- retrieve exact candidate/approved text being revised plus governing sources;
- identify revision scope;
- Develop Story only if revision changes scene/story decisions;
- Simulate Character/domain skills as needed;
- Write Fiction as a constrained revision rather than a fresh scene;
- preserve candidate/approved status correctly;
- Persist exact approved replacement only after approval.

### F. Transformation / presentation / competence work
Typical sequence:
- Transform for actual change mechanics/consequences;
- Present for current composition;
- Inhabit for competence/lived-skill gaps;
- Contextualize for social/cultural meaning;
- Simulate Character for response/choice;
- Track State for established durable deltas;
- Persist when authorized.

### G. Recovery / archaeology / lost-material question
Typical sequence:
- route to recovery protocol and existing Audit infrastructure;
- Recover;
- Reconcile when competing claims/status require disposition;
- Persist only accepted/authorized recovered state;
- Audit coverage/completeness if requested.

### H. Conflict / canon disagreement
Typical sequence:
- retrieve authority/status rules and precise conflicting claims;
- Recover first if provenance/coverage is incomplete;
- Reconcile;
- hand genuine unresolved decision to Jim;
- Persist resolved authoritative changes when authorized.

### I. New sustained story
Typical sequence:
- search for existing matching story first;
- establish approved or explicit working title;
- initialize required story records using current schemas;
- resolve consequential shared-world/life-infrastructure bindings without invention;
- resolve persistent named-character identity requirements;
- Persist and verify initialization;
- then Develop Story and/or Write Fiction.

Casual brainstorming does not automatically require full story initialization. Notice when it becomes sustained development.

## Skill ownership map

- **Recover** — discover/reconstruct prior evidence and provenance.
- **Reconcile** — resolve claims as far as authority/scope/chronology permit.
- **Persist** — make authorized state durable and prove it by read-back.
- **Audit** — test a bounded target against explicit requirements.
- **Transform** — resolve what changed and entailed consequences.
- **Track State** — record established mutable state deltas.
- **Inhabit** — resolve competence and lived-performance gaps.
- **Contextualize** — determine materially applicable social/cultural context.
- **Present** — resolve coherent current presentation.
- **Simulate Character** — resolve character-determined perception/response/behavior.
- **Develop Story** — develop open story possibilities, beats, arcs, pacing, and planning status.
- **Write Fiction** — realize authorized material as prose.

The orchestrator may invoke several; it must not duplicate their internal procedures.

## Sequencing rules

1. **Authority before creativity.**
   Retrieve live governance/story authority before story development or prose.

2. **Recovery before reconciliation when evidence is incomplete.**
   Do not reconcile from fragments if the required evidence universe has not been established.

3. **Reconciliation before persistence when status/scope conflicts.**
   Persist does not decide which claim wins.

4. **Mechanics/context before character response when they materially constrain the character.**
   Transform, Present, Inhabit, and Contextualize provide constraints; Simulate Character owns character response.

5. **Character simulation before story selection when character agency matters.**
   Develop Story may create situations but may not dictate character behavior.

6. **Story development before prose when consequential scene direction remains open.**
   Write Fiction cannot use prose momentum to decide unresolved authorial choices.

7. **Writing before occurred-state propagation.**
   A planned event is not an occurred event. Candidate prose is not approved manuscript.

8. **Approval before approved-manuscript promotion and occurred-state updates.**
   Candidate preservation and approval are separate.

9. **Track State before Persist when an accepted event changes mutable records.**
   Track State defines the supported delta; Persist makes it durable.

10. **Persist before claiming durability.**
    A chat acknowledgement, intended file, commit response without read-back, or audit mention is insufficient.

11. **Narrative progression does not manufacture elapsed time.**
    A next chapter, scene break, location change, or "later" instruction does not by itself mean next day. Temporal advancement must come from authoritative continuity, explicit development, occurred prose after approval, or Jim's decision. When exact clock time is unknown, preserve the known relative anchor instead of inventing precision.

12. **Audit at the appropriate boundary.**
    Use source-fidelity/scene audit for prose; conformance audit for broader repository/workflow claims. Audit does not silently repair.

## Stop conditions

Stop and surface the actual blocker when:
- a consequential creative choice remains genuinely open;
- required authoritative sources cannot be retrieved;
- story namespace/identity is materially ambiguous;
- a routed world/mechanics rule conflicts with the proposed work;
- required staff/person/location/object/affiliation input cannot be resolved for prose;
- same-authority claims conflict and Reconcile cannot settle them;
- Jim approval is required for candidate-to-approved promotion;
- persistence/write verification fails;
- scope expansion would cross into another story/component without authorization.

Do not work around blockers with generic substitutes, silent assumptions, fake completion, or invented canon.

## Continue-without-asking conditions

Do not interrupt Jim for routine implementation when:
- current authority already settles the answer;
- a prior explicit Jim decision already authorizes the action;
- the remaining choice is harmless connective implementation within an approved scene;
- a skill's procedure deterministically resolves the issue;
- persistence/verification is an already-required consequence of an accepted decision;
- the task can be completed safely within current scope without creating new consequential canon.

Jim should not have to approve the same thing twice.

## Persistence/lifecycle rules

When work creates durable project state:
- route story-specific facts to story records;
- route reusable framework/world material to the governing System Bible destination;
- preserve brainstorming alternatives in development/ideas with status/provenance;
- preserve generated manuscript as candidate at delivery time when governance requires;
- promote exact prose only after approval;
- use Track State for occurred mutable changes;
- use Persist for actual durable writes and post-write verification;
- keep discoverability from normal project entry points.

Do not equate conversation memory with project state.

## Output behavior

The orchestrator should normally remain invisible to Jim.

Instead of narrating internal workflow, deliver:
- the requested substantive result;
- only necessary blockers/choices;
- precise persistence/verification status when writes occurred;
- source receipts when required for substantial prose;
- concise notice of incomplete or unverified steps when something failed.

Do not burden ordinary conversation with skill names or administrative checklists unless Jim is explicitly working on the framework itself.

## Cold-start invariant

A fresh session with repository access should be able to:
1. retrieve bootstrap/router;
2. resolve the active story from Jim's natural request;
3. load current story authority;
4. select the necessary skill chain;
5. continue the work correctly;
6. persist/verify resulting durable state;
without relying on prior chat memory or requiring Jim to recite internal procedure.

## Guardrails

- No giant monolithic reimplementation of specialist skills.
- No memory-first fiction when live repository authority is available.
- No cross-story contamination.
- No silent scope expansion.
- No invented resolution to missing inputs.
- No repeated approval requests for already settled decisions.
- No skipping persistence because the conversational answer looks complete.
- No treating persistence as successful before read-back verification.
- No treating plans/candidates as occurred/approved state.
- No workflow step may manufacture authority merely because the process expects a field.
