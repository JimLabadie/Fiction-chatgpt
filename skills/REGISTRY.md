# Prototype Skill Registry

Status: PROTOTYPE — NON-GOVERNING
Scope: Integrated procedural skill set. This registry routes responsibilities; it does not replace each skill's contract or project governance.

| Skill | Trigger / question | Owns | Does not own | Primary handoffs |
|---|---|---|---|---|
| Recover | What existed, was said, was lost, or is represented in surviving evidence? | systematic evidence recovery, provenance, coverage, historical version discovery | deciding discretionary canon; ordinary current-canon retrieval; repair | Reconcile, Persist |
| Reconcile | Competing claims or records disagree or overlap; what do authority/scope/chronology actually settle? | claim comparison, authority/scope disposition, explicit unresolved-decision boundary | evidence-universe discovery; new canon synthesis; writing changes | Recover, Persist, Jim |
| Persist | An authorized state/decision must become durable; can durability be proven? | authoritative destination write, dependent propagation, post-write fetch/substantive verification | canon promotion authority; conflict resolution; unrelated cleanup | Reconcile, Track State, Audit |
| Audit | Does a bounded target satisfy stated requirements, and what proof supports that? | audit contract, proof-type selection, systematic inspection, findings, coverage receipt | silent repair, historical reconstruction, canon promotion | Recover, Reconcile, Persist, owning skill |
| Transform | What exactly changed, and which consequences are entailed? | transformation/change envelope and consequence propagation | inventing mechanics; automatically granting competence/context/presentation/state persistence | Inhabit, Contextualize, Present, Track State |
| Track State | What established mutable state changed? | smallest supported state delta and cross-tracker consistency | deciding what happened; resolving authoritative conflicts; proving repository durability | Reconcile, Persist |
| Inhabit | How can this specific character perform/live an unfamiliar circumstance given actual competence? | competence gap, learning/performance, elapsed adaptation | demographic destiny; automatic skill transfer; general culture ownership | Contextualize, Track State, Jim |
| Contextualize | Which contextual knowledge materially applies to this individual/situation? | relevance and interpretation of culture/generation/community/etc. | individual canon, stereotype-driven choices, final character decision | Inhabit, Present, character simulation/Jim |
| Present | How does this character coherently present right now? | current composition from canon, resources, context, competence, constraints | underlying identity/body/culture/wardrobe ownership; prose style; silent acquisition | Contextualize, Inhabit, Transform, Track State, Persist |
| Simulate Character | What would this specific established character notice, interpret, feel, choose, say, or do here? | character-level attention, interpretation, internal response, option filtering, character-determined choice, expression | plot direction; prose realization; culture/mechanics/presentation ownership; persistence | Contextualize, Inhabit, Present, Transform, Track State, Develop Story/Jim |
| Develop Story | What should the story explore next, and how should approved direction become scene-capable structure? | possibilities, consequences, sequencing, pacing, beats/arcs, planning status, author-choice boundary | character truth; character-determined behavior; prose realization; occurred continuity; canon promotion | Simulate Character, domain skills, Jim, Write Fiction, Track State, Persist |
| Write Fiction | How does the authorized scene become lived narrative experience? | source-grounded prose realization, POV, dialogue, interiority, physical embodiment, rhythm/pacing, candidate-manuscript boundary | unresolved story direction; character truth; canon promotion; world/mechanics invention; persistence proof | Develop Story, Simulate Character, domain skills, Track State, Persist, Audit |
| Fiction Workflow | What complete skill chain should handle this fiction request, in what order, and where should it stop? | orchestration, routing, sequencing, lifecycle/persistence boundaries, stop/continue conditions | specialist logic; canon facts; creative decisions; prose; recovery/reconciliation/persistence/audit internals | all specialist skills, Jim when genuinely required |

## Core routing invariants

1. Governance remains above every skill.
2. Knowledge/data describe; skills operate on them.
3. Recover establishes evidence before Reconcile when provenance/coverage is inadequate.
4. Reconcile resolves only what authority/scope/chronology already determine; genuine authorial choices remain Jim's.
5. Operational skills never manufacture missing canon to finish a task.
6. Transform owns what changed; Inhabit owns competence; Contextualize owns contextual applicability; Present owns current presentation composition.
7. Track State records established mutable consequences; it does not invent the event.
8. Persist owns durability proof; no other skill may call a chat-only or unverified write persisted.
9. Audit diagnoses against an explicit contract; it does not silently become repair.
10. Simulate Character may resolve behavior only where established character/state materially constrains the choice; genuinely open story-direction choices remain open for Develop Story/Jim.
11. Develop Story keeps occurred facts, approved future plans, developed possibilities, and proposals distinct; planning does not make an event occurred.
12. Write Fiction realizes authorized material but may not use prose momentum or beauty to decide unresolved consequential canon; candidate prose remains distinct from approved manuscript.
13. Fiction Workflow selects the smallest complete specialist chain and must not re-implement specialist procedures inside the orchestrator.
14. Scene-local generated choices do not become durable canon merely because an operational skill produced them.

## Known interface gaps

- Simulate Character owns character-determined behavior; Develop Story owns genuinely open story-direction, beat, arc, pacing, and scene-development work while preserving Jim's consequential-choice authority.
- No standalone research/verification skill has yet been extracted for current real-world factual precision.
- The current prototype branches remain non-governing until explicitly promoted.

## Integration status

The original nine skill files were copied unchanged from their isolated prototype branches into the integration branch and fetch-verified before this registry was created. Additional integrated skills were then added and separately verified. Interface testing may justify later edits, but such edits must be explicit and separately verified.
