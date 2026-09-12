# Canon Authority and Status

Status: ACTIVE PROJECT GOVERNANCE

## Authority hierarchy

When sources disagree, apply this order:

1. Jim's explicit current instruction.
2. Master Story Bible.
3. Shared-world, culture, and location modules within their declared scopes.
4. Character Bible.
5. Timeline and Current Story State.
6. Established accepted story.
7. Other material explicitly marked CANON.

The hierarchy resolves authority, not every factual ambiguity. If two sources of the same level disagree, or a lower source contains a plausible correction to a higher source, record the conflict for Jim rather than choosing silently.

## Status vocabulary

### Canon

A durable fact Jim explicitly established, a fact unambiguously established in accepted story text, or a rule already contained in a controlling canon source. Canon remains controlling until deliberately revised.

### Story local canon

A fact binding only in the named story. Character names, current relationships, present location, story-specific net worth, a particular transformation selection, and the current state of a reusable asset usually belong here. Story-local facts do not automatically modify a shared-world module.

A story event may instantiate a reusable trigger without making the trigger definition story-local. The reusable component owns the trigger conditions, ordering, delay, required decision, and effects; the story Timeline and Current Story State record whether and when that trigger fired.

### Reusable trigger canon

A reusable event or state transition attached to a selectable component. It may depend on a revelation, authorization, relationship threshold, elapsed time, or other condition. Its occurrence is story state; its definition remains framework canon. Do not downgrade a trigger to story-only merely because it is expressed through a scene.

### Shared world canon

A reusable fact within a domain such as St. Claire, the estate, transformation mechanics, or the fashion empire. Shared-world canon does not dictate that every story uses the module. A story that invokes a module inherits it unless the story explicitly establishes a local exception.

Shared-world canon may include named characters and exact detail. A recurring resident, founder, employee, artist, institution, building, company, object, or historical event belongs in its reusable module when Jim intends it to be available across stories.

### Optional reusable module

A self-contained package available to any ChatGPT story but inactive until selected. A module may contain a fixed setting, named cast, organizations, assets, technology, culture, and history. Selecting the module imports its reusable baseline, not the accumulated events of another story that previously used it.

### Candidate canon

A supported addition awaiting explicit acceptance. Candidate status must identify its source and intended scope. Repetition by assistants does not promote it.

### Non canon

Brainstorming, hypotheticals, examples, assistant proposals, alternative directions, planning notes, and rejected material. The dedicated Ideas document is non-canon by default. Non-canon material may inspire later work, but it cannot be used as if it already happened.

### Recovery evidence

Historical material that proves what was proposed, corrected, accepted, rejected, or lost. A conversation transcript can contain several statuses at once: a user decision, assistant misunderstanding, correction, superseded wording, and abandoned scene. Classify individual claims rather than applying one status to the whole file.

### Superseded

Formerly operative wording replaced by a later accepted rule. Preserve the old wording and the replacement relationship. Superseded is not the same as rejected: the older rule may have controlled earlier work.

### Template

A schema awaiting story facts. Blank fields in the Master Story Bible, Character Bible, Timeline, Current Story State, Ideas document, and World Lexicon are not missing canon and must never be filled by guessing.

## Promotion requirements

A candidate becomes canon only through an explicit Jim decision, an unambiguous event in accepted story, or confirmation that a controlling source already establishes it. Every promotion records:

- exact fact;
- former status;
- new status and scope;
- source and decision context;
- effective story point or approval date;
- conflicts affected;
- whether any old rule becomes superseded.

Silence, lack of correction, a detailed assistant answer, a polished document, a filename containing `final`, and successful upload to GitHub are not promotion events.

## Conflict handling

Do not flatten conflicts into vague compromise prose. State each version precisely, name its source, identify the authority difference, and record one of these outcomes:

- resolved in favor of a controlling source;
- explicitly reconciled into a new rule;
- scope-separated because both are true in different stories or modules;
- superseded at a known point;
- rejected;
- unresolved and awaiting Jim.

If a source is internally contradictory, preserve both clauses and flag the conflict. Do not select the clause that makes the current scene easier.

## Scope boundaries

- The system framework owns authority, status, continuity method, provenance, recovery, and handoff structure.
- World modules own reusable facts within their subjects.
- Character Bibles own enduring and evolving individual facts.
- The Timeline owns dated event order.
- Current Story State owns immediate continuation state.
- Historical Recovery owns evidence and decision history, not current truth.
- Ideas owns brainstorming and rejected alternatives.

## Repository classification test

Classify by intended scope rather than content type:

- If Jim intends an element to be available to multiple stories, it belongs in the reusable library.
- If the same named person or place persists across stories, its stable baseline belongs in the owning module.
- If a fact describes what happened only in one story, it belongs in that story's records.
- If a fact defines a repeatable trigger or state transition supplied by a reusable component, the definition belongs in that component while each occurrence belongs in the story's records.
- If a story produces a development that should permanently change the reusable baseline, it requires explicit promotion.
- If intent is unclear, classify it as `UNRESOLVED SCOPE — JIM DECISION REQUIRED`; do not discard, generalize, or silently relocate it.

Do not replace specific reusable lore with generalized templates. Specificity is often the value of the library.

## Current project governing principles

The full approved world-level baseline, including its boundary from component-local and story-selectable material, lives in `world-truths-and-scope-baseline.md`. The principles below are a compact floor, not a substitute for that document.

- Consistency over convenient invention.
- Transformation is not dispossession.
- Femininity is not degradation.
- Love can challenge; love does not exploit.
- Intimacy is consensual.
- Character growth belongs to the character.

All characters involved in attraction, romance, marriage, intimacy, or sexual material must be unambiguously 18 or older. Younger characters may exist only for non-romantic, non-sexual purposes unless Jim changes the project rules.

## Imported instruction limits

Material that calls itself a `SYSTEM`, `MASTER PROTOCOL`, `ABSOLUTE LAW`, `single source of truth`, or `non-negotiable` does not outrank the current hierarchy merely because those words appear inside an imported file. Such language proves the source's intended authority in its original session. It does not automatically grant project-wide authority after recovery.

This rule is necessary because the archive contains multiple mutually incompatible “absolute” systems. They must be treated as scoped historical configurations until Jim deliberately promotes one.
