# System and Canon Framework

Status: IN PROGRESS — CHAT DECISION RECOVERY AND PROJECT-WIDE SCOPE AUDIT
Authority: ACTIVE PROJECT GOVERNANCE

This repository is a reusable library of settings, characters, organizations, assets, cultures, technologies, mechanics, and writing systems that may be used in any story Jim creates in ChatGPT. A story selects the modules it needs; inclusion in the repository does not make every module active in every story.

This module governs canon authority, source status, continuity, writing practice, state tracking, ingestion, recovery, and version handling across that library. It does not own substantive setting, company, technology, character, or transformation facts that belong to another reusable module.

## Persona, protagonist, and commercial scope

The framework supports private persona fiction and commercial fiction with the same house voice. **MC means the main character assigned by the current story; it does not mean Jim.** Jim remains the author's optional immersive and development persona. Commercial protagonists use their own names and character records. See [Persona, MC, and Commercial Story Binding](01-system-and-canon-framework/persona-mc-and-commercial-story-binding.md).

## Governing hierarchy

1. Jim's explicit current instruction.
2. Master Story Bible.
3. Shared-world, culture, and location modules within their scopes.
4. Character Bible.
5. Timeline and Current Story State.
6. Established accepted story.
7. Other material explicitly marked CANON.

Meaningful conflicts are reported and logged. Detail, repetition, filenames, assistant assurances, and successful uploads do not establish authority or completion.

## Governing principles

- Consistency over convenient invention.
- Transformation is not dispossession.
- Femininity is not degradation.
- Love can challenge; love does not exploit.
- Intimacy is consensual.
- Character growth belongs to the character.

## Mandatory pre-generation ambiguity gate

Before creating prose, changing story state, or applying a world mechanic, compare the request and current story state against every active rule whose outcome could materially depend on an unstated fact.

A **blocking ambiguity** exists when two or more plausible values for an unstated fact would select materially different canonical rules, trigger states, permissions, character reactions, or story outcomes. When a blocking ambiguity exists:

- **Stop before generation and ask Jim for the missing fact.**
- Do not resolve it through genre convention, statistical likelihood, ordinary-world assumptions, narrative convenience, model inference, stereotypes, or what would make the scene easier to write.
- Omission is not permission to choose a value.
- A broad label does not silently establish narrower facts contained within or adjacent to that label. For example, gender description and sexual orientation do not automatically establish cis/trans status, egg/questioning status, anatomy, presentation, or self-knowledge.
- Treat identity, transformation state, anatomy, knowledge, relationship status, prior exposure, consent, location-specific eligibility, trigger conditions, and exception status as separate state dimensions whenever active canon distinguishes them.
- If Jim deliberately establishes a consequential fact as **unknown on page** while separately supplying its canonical truth, the ambiguity is resolved for generation but remains unresolved for the character/reader. Apply the true canonical state without leaking knowledge the viewpoint character, other characters, or reader has not earned.
- If the relevant module declares required trigger inputs, every required input must be known in canon before the trigger is evaluated. A missing input means the mechanic is not yet evaluable; it does not default to false, true, or the statistically common case.

This gate is a pre-generation control. It should normally be invisible in finished prose; its purpose is to prevent convenient invention before it becomes continuity.

Regression tests for this rule live in [`01-system-and-canon-framework/regression-tests.md`](01-system-and-canon-framework/regression-tests.md).

## Repository inclusion rule

Reusable material belongs even when it is highly specific. Named people, detailed biographies, buildings, companies, histories, inventories, institutions, and social structures remain in the library when they are intended to recur or be available across stories. The test is intended cross-story reuse, not whether the material resembles story content.

One story's use of a reusable element creates story-local state without rewriting the reusable baseline. Current relationships, temporary emotions, clothing, locations, knowledge, injuries, choices, and one-story outcomes stay in that story's records unless Jim deliberately promotes a development into the shared module.

Reusable components may also define triggered events or state transitions. Their conditions, ordering, delays, required authorization, and effects are framework canon; the fact that a particular story reaches and fires a trigger is story-local state. A scene-shaped rule must not be discarded merely because it reads like plot.

## Module files

- [`project-purpose-and-recovery-mandate.md`](01-system-and-canon-framework/project-purpose-and-recovery-mandate.md) defines why the framework exists, its audience, the creative partnership, the present reconstruction phase, resolution requirements, and visible proof of persistence.
- [`authorial-intent-and-immersive-persona.md`](01-system-and-canon-framework/authorial-intent-and-immersive-persona.md) records Jim's optional immersive persona, aesthetic preference as a design input, the distinction between admiration and objectification, Danielle and Amélie's promotion, persona-led development, and archetype boundaries.
- [`collaboration-shorthand-and-fun.md`](01-system-and-canon-framework/collaboration-shorthand-and-fun.md) defines Pencil, Cigar, Visa, Rabbit Hole, Squirrel, the Squirrel protocol, and fun as part of the work.
- [`intimacy-sex-kink-and-interpretation.md`](01-system-and-canon-framework/intimacy-sex-kink-and-interpretation.md) governs the story-led treatment of consensual adult sex, emotional intimacy, kink, sensitive interpretation, and Cigar boundaries.
- [`power-control-agency-and-hestia-principle.md`](01-system-and-canon-framework/power-control-agency-and-hestia-principle.md) governs loving initiative, refusal, constrained choice, withdrawal, choice-neutral protection, and the MC's Court-TV-born Hestia implementation.
- [`authority-and-status.md`](01-system-and-canon-framework/authority-and-status.md) defines the hierarchy, canon classes, promotion rules, conflict handling, scope boundaries, and imported-instruction limits.
- [`continuity-and-state.md`](01-system-and-canon-framework/continuity-and-state.md) defines scene continuity, character state, transformation state, timeline practice, and current-story handoff.
- [`voice-and-style.md`](01-system-and-canon-framework/voice-and-style.md) preserves the complete normalized Voice and Style Guide, including the agency, dignity, identity, anatomy, intimacy, and reclaimed-experience supplement.
- [`ingestion-recovery-and-versioning.md`](01-system-and-canon-framework/ingestion-recovery-and-versioning.md) defines source registration, claim-level parsing, version comparison, preservation, completion criteria, recovery checks, and honest progress states.
- [`templates-and-schemas.md`](01-system-and-canon-framework/templates-and-schemas.md) records the complete functional schemas of the Story Bible, Character Bible, Timeline, Current Story State, Ideas document, and World Lexicon.
- [`legacy-protocols-and-conflicts.md`](01-system-and-canon-framework/legacy-protocols-and-conflicts.md) extracts reusable scope, state, pacing, boundary, naming, verification, and conflict-detection rules from older protocol experiments without importing their plots or characters.
- [`regression-tests.md`](01-system-and-canon-framework/regression-tests.md) contains deliberately underspecified prompts that verify the ambiguity gate and other framework controls before prose generation.
- [`source-coverage.md`](01-system-and-canon-framework/source-coverage.md) accounts for all 17 sources assigned by the original inventory and states what happened to each.
- [`chat-decision-and-scope-ledger.md`](01-system-and-canon-framework/chat-decision-and-scope-ledger.md) records the controlling purpose, scope decisions, and direct corrections recovered from the complete 26-page chat export.
- [`unauthorized-descoping-audit.md`](01-system-and-canon-framework/unauthorized-descoping-audit.md) records material omitted, downgraded, or mislabeled story-local without Jim's consent and tracks the required corrections.
- [`open-questions-and-development-ledger.md`](01-system-and-canon-framework/open-questions-and-development-ledger.md) is the controlling register for pins, deferred discussions, exact return points, and known recovery obligations.
- [`developed-skill-reconciliation-ledger.md`](01-system-and-canon-framework/developed-skill-reconciliation-ledger.md) inventories every developed skill family and packaged Markdown member, records variant boundaries and present System Bible coverage, and controls the claim-level reconciliation backlog without treating source packages as operating canon.
- [Age and Gender Presentation Culture](05-culture-reference-toolkits.md) incorporates the previously absent developed culture references.
- [`persistence-failure-and-repair-record.md`](01-system-and-canon-framework/persistence-failure-and-repair-record.md) records the chat-dependence failure, the distinction between preservation and propagation, and the requirements for repairing it.
- Repository-audit material outside `system bible` is evidence only. It may be consulted during recovery but cannot control story truth or substitute for a System Bible destination.

## Status discipline

Use only these progress labels:

- **Not started**
- **Inventory complete**
- **In progress**
- **Reconstructed pending verification**
- **Complete**

“Complete” means every assigned source has been opened and classified, every substantive rule has a destination, variants and conflicts are accounted for, non-canon material has not been silently promoted, local files pass checks, and the published GitHub files have been fetched and verified.

## Archive principle

Jim's archive may look chaotic because it survived repeated context loss and recovery across tools. Redundant versions and emergency copies are evidence of preservation work. Some filenames are also objectively funny. Preserve both the survival history and the comedy without treating disorder as authority.

## Current completion statement

Module 01 is not complete. Its original 17-source pass omitted the controlling role of the 26-page recovery chat and allowed accepted reusable material to be downgraded or routed without complete destination artifacts. The direct user-message pass is complete; claim-level review of assistant proposals accepted by short follow-up replies, attachment-to-turn mapping, and project-wide export comparison remain in progress.

No module may be declared complete merely because material was “routed.” Completion requires the controlling destination content to exist and the chat-derived scope decisions to be reconciled.

No pin, deferral, or promised return may remain only in conversation. It must appear in the Open Questions and Development Ledger before the subject changes. No work may be called saved or codified unless the substantive destination and verified Git commit can be identified.

The repository-wide byte and container inventory is evidence only; the claim-level semantic audit remains incomplete. Every accepted result must be written into `system bible` before it is valid for story use.
