# Multi-Skill Integration Cold Test

Status: PROTOTYPE TEST
Scope: recover, reconcile, contextualize, inhabit, present, transform, track-state, persist, audit

## Scenario

A current story needs a character's presentation after a previously developed transformation. Historical evidence and current records disagree about whether a presentation-related capability transferred. The character has established preferences and wardrobe resources. Applicable cultural context exists. The resulting scene choice may create a persistent state change.

## Expected routing

1. **Recover** inspects the maintained evidence and current destination when the capability-transfer provenance is uncertain.
2. **Reconcile** determines whether authority/scope already resolves the capability question. If same-level evidence remains genuinely ambiguous, stop that decision for Jim.
3. **Transform** supplies only the body/ability/state consequences actually established by the selected mechanism.
4. **Contextualize** supplies relevant cultural/social meaning without replacing the character's canon.
5. **Inhabit** determines what the character can actually execute from established/transferred competence, help, practice, and elapsed time.
6. **Present** resolves the coherent current composition from preferences, resources, situation, context, body/state, and competence. It may not invent possessions or permanent preferences.
7. **Track State** records only persistent deltas actually established by the accepted event/choice.
8. **Persist** writes authorized durable changes to the correct destinations and fetch-verifies them. If a required dependent record remains stale, status is PARTIALLY PERSISTED at most.
9. **Audit** checks the bounded result against the stated requirements and distinguishes structural/persistence proof from semantic correctness.

## Failure conditions

The integrated system fails if any skill:
- invents the missing capability rule;
- treats culture as character destiny;
- grants competence from identity/presentation alone;
- silently creates wardrobe/resources;
- turns a scene-local generated choice into permanent canon;
- records state before the underlying event/choice is established;
- calls a write persisted without read-back verification;
- uses audit findings as authority to repair unrelated material;
- crosses into another story/component namespace without authorization;
- hides an unresolved Jim decision inside synthesized prose.

## Interface pass condition

Each question has one clear owner, supporting skills provide inputs rather than competing answers, unresolved authority returns to Recover/Reconcile/Jim, durable changes end at Persist, and Audit evaluates rather than mutates.
