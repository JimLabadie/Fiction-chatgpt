# Continuity and State Tracking

Status: ACTIVE PROJECT GOVERNANCE

## Separation of records

The project uses several records because they answer different questions:

| Record | Question answered | Update pattern |
|---|---|---|
| Master Story Bible | What durable facts govern this story? | Only after canon establishment or revision |
| Character Bible | Who is this person, and how have they changed? | When a lasting personal fact or genuine development occurs |
| Timeline | What happened, where, and in what order? | After dated or sequence-sensitive events |
| Current Story State | What is true at the exact handoff point? | At meaningful stopping points |
| Ideas | What might happen? | During brainstorming; remains non-canon |
| Historical Recovery | What source proves a decision or conflict? | During ingestion and reconciliation |

No record substitutes for another. Current Story State supplements permanent canon; it cannot overwrite it. A Character Bible does not replace the Timeline. An idea does not become an event by being copied beside canon.

## Scene continuity checklist

Before continuing prose, lock:

- canonical date, time, daypart, and elapsed time;
- location and exact physical positions;
- viewpoint character, tense, and POV mode;
- characters present and absent;
- clothing, grooming, appearance, injury, fatigue, hunger, intoxication, and other physical state;
- objects in hand, possessions, vehicles, rooms, furniture, fixtures, surfaces, and access permissions;
- ambient physical conditions such as lighting, sound, temperature, weather, crowding, smell, and other sensory conditions where relevant;
- what each character knows, believes, misunderstands, and conceals;
- promises, appointments, travel requirements, unfinished conversations, and immediate plans;
- relationship closeness, tension, consent, and unresolved emotional developments;
- transformation baseline, completed changes, changes in progress, temporary effects, and permanent effects;
- the preceding scene's emotional temperature and natural next action.

A section break does not advance time, change clothes, move objects, restore energy, resolve embarrassment, reset relationships, rearrange a room, remove furniture, refill a drink, or teleport a character or possession.

## Authoritative named-entity resolution gate

Before asking Jim to identify, define, choose, or clarify a referenced person, place, business, institution, group, object, program, event, or other named or recognizable world entity, first determine whether the repository already resolves the reference.

This gate applies not only to exact proper names but also to ordinary shorthand, partial names, descriptive references, aliases, and context-dependent phrases such as `the art collective`, `the diner`, `her aunt`, `the lab`, `the estate`, or `the gala` when the active story/world context may make one established entity the intended referent.

Required resolution sequence:

1. Check the active story state, Character Bible, Timeline, and immediately governing story material for an already established referent.
2. Check the authoritative shared-world/module entry point and its structured people/organizations/places/data files.
3. Search exact phrase/name matches first, then near-name, alias, category, role, and contextual matches when the exact wording is not the canonical record name.
4. Follow authoritative cross-references needed to instantiate the entity correctly. For a named location, this can require both its Organization record and Place record; for a person, the population/character record and current story state may both matter.
5. Use surrounding conversational/story context to disambiguate among repository candidates only when that context makes the intended referent materially clear and does not require inventing a missing canonical fact.
6. Ask Jim only if multiple materially plausible authoritative candidates remain, the repository is genuinely silent, or choosing among candidates would require inventing a consequential fact.

A weak first search result is not evidence that canon is absent. Do not stop after broad semantic search returns adjacent concepts. Retry with the user's exact wording, canonical category terms, likely aliases, and the active module's structured records before declaring the reference missing or ambiguous.

Do not replace an established entity with a newly invented generic equivalent merely because the user used shorthand rather than its full canonical name. Conversely, do not force a repository match when context genuinely supports multiple candidates; that is a real ambiguity and belongs at the ambiguity gate.

The purpose is **retrieval before invention and retrieval before interrogation**: if Jim already did the work and the repository contains the answer, use it.

## Character physical-instantiation and early-description gate

The trigger is the **reader's first substantial encounter with a character**, not merely the character physically entering a scene. This includes the viewpoint character, a character already present when the scene opens, and any other person who becomes scene-relevant or begins carrying dialogue/action.

Every such character must exist as a fully physically coherent person before prose uses them. A few shorthand signals are not a substitute for instantiation.

Before prose, establish from canon or deliberate story-local creation a **complete physical baseline and current presentation state**, including:

- canonical or story-local identity and approximate age;
- height, build, body shape/proportions, and scene-relevant physical features;
- face, complexion/skin, eyes, hair, and distinguishing features;
- grooming;
- presentation and individual style rather than category shorthand alone;
- complete current clothing from head to toe as applicable: layers, top/outerwear, bottoms or equivalent garment, underlayers when they materially affect appearance/state, hosiery/socks when relevant, and footwear;
- jewelry, accessories, makeup or deliberate lack of it where relevant to presentation, glasses, bags, and other visible carried items;
- scene-relevant possessions such as phone, keys, drink, coat, vehicle, or equipment;
- posture, movement, body language, voice, and distinguishing physical habits when relevant;
- what the viewpoint character can actually perceive and what concrete features produce attraction, recognition, intimidation, familiarity, curiosity, or another physical impression.

**Complete internal state and complete reader-facing description are both required, but they are not the same thing.** The character's full physical state must be settled before generation. The prose must then give the reader a complete usable picture **toward the beginning of the reader's first substantial encounter with that character**.

“Toward the beginning” does not require a single inventory paragraph. Description should be woven naturally through the opening/entrance, first actions, first exchange, and nearby beats. It may arrive across several sentences or paragraphs. But it may not be deferred so long that the reader spends a substantial scene interacting with a vague body, floating face, single garment, trope, or dialogue voice and only later discovers what the person actually looks like.

A complete usable reader picture normally includes the character's apparent age range, overall body/build, face or distinguishing facial impression, hair/grooming, presentation/style, complete visible outfit including footwear when it can reasonably be perceived, notable accessories, and characteristic physical bearing. Exact measurements or exhaustive microscopic detail are not required unless canon or the scene makes them relevant. The standard is that the reader can visualize the whole person rather than having to invent the missing majority.

The viewpoint character is not exempt merely because the narration originates inside that character. On the reader's first substantial encounter with a POV character, establish that character's own physical presence and current presentation early and naturally. Mirrors, self-inventory, or unnatural self-observation are not required; use action, clothing interaction, spatial relationships, other characters' reactions, ordinary self-awareness, and other natural POV-compatible methods.

When viewpoint matters, description must remain POV-grounded. A viewpoint character need not clinically catalogue another person; instead, concrete observations should accumulate naturally. If the viewpoint character finds someone attractive, striking, intimidating, elegant, awkward, familiar, or otherwise physically notable, the prose must show the observable reasons for that impression rather than substituting the adjective for description. What the viewpoint character notices can also characterize the viewpoint character.

When an existing reusable or story character is available, load that character's established appearance, presentation, clothing/state, and personality rather than regenerating the person from a trope or a few generic cues. When a new character is genuinely needed, create the complete coherent story-local person before using them as a dialogue function.

Do not substitute labels such as `lesbian`, `butch`, `femme`, `executive`, `bartender`, `pretty`, `confident`, `leather jacket`, or similar shorthand for the rest of a human being. Category, occupation, attractiveness, and one striking garment may inform characterization; none of them completes it.

If a scene makes a physical claim that requires an unstated complementary fact — for example, naming outerwear while leaving the rest of the clothing state physically indeterminate — resolve the complete state before prose and describe the person sufficiently early that the text does not imply accidental nudity, impossible clothing, or a visually incomplete character.

The gate applies equally to newly introduced characters and continuing characters. A continuing character does not need to be re-described from scratch every time the reader already knows the established baseline, but any changed current presentation — clothing, hair, grooming, injury, transformation, accessories, or other visually meaningful state — must be established early enough for the reader to picture the character correctly. Established clothing and possessions do not regenerate merely because a new scene or section begins.

## Scene physical-instantiation and environmental grounding gate

Characters do not meet, talk, move, drink, sit, touch, look, or react on an empty plane of existence. Before prose, instantiate the physical scene as deliberately as the people in it.

For every substantial scene, establish from canon or deliberate story-local creation the usable physical environment, including as applicable:

- exact location and the relevant part of that location;
- room/space shape, scale, layout, entrances/exits, and meaningful sightlines;
- furniture, fixtures, counters, tables, stools/chairs, walls, floors, doors, windows, rails, shelves, stages, booths, equipment, or other structures characters can perceive or interact with;
- where each present character is positioned relative to those objects and to one another;
- objects already present and their state: glasses, bottles, menus, napkins, phones, bags, coats, dishes, keys, receipts, ashtrays where appropriate, décor, signage, or other scene-specific items;
- lighting and visible color/texture;
- sound and its physical source;
- temperature, airflow, weather exposure, smell, crowd density, movement, and other useful sensory conditions;
- practical pathways and constraints: how someone approaches, sits, leaves, reaches the restroom, gets a drink, sees another person, hears speech, or crosses the space;
- changes caused during the scene: moved chairs, emptied drinks, discarded labels, wet coats, opened doors, shifted bags, broken objects, spilled liquid, or anything else that should persist.

**The reader must receive a usable sense of place toward the beginning of the scene.** As with character description, this does not require a static room inventory. Ground the setting through action and perception: a boot hooks a brass stool rail; condensation wets a coaster; bass comes through the concrete floor; a bartender reaches across a particular counter; purple light catches a bottle; a character has to angle around another stool to approach. Description and action should prove that the characters occupy a real space.

Do not use generic venue labels as substitutes for environment. `bar`, `bedroom`, `office`, `restaurant`, `street`, `house`, `club`, or `kitchen` names a category; it does not instantiate the location. If an authoritative place/module already defines the environment, load and use it rather than rebuilding a generic version. Resolve shorthand or partial location references through the authoritative named-entity resolution gate before concluding that no such location is established.

Objects must have continuity and causal reality. A character cannot drink from an unestablished glass, sit on an unestablished stool, put a phone into a pocket that their clothing does not have, set a bag down nowhere, cross a room with no spatial relationship, or interact with décor/furniture that appears only at the instant the prose needs it. Ordinary objects need not receive elaborate introductions, but the scene model must contain them and the prose must establish them naturally when they become perceptually or causally relevant.

Environmental description should not become architectural sludge. Apply Pencil: establish enough concrete, specific reality for the reader to inhabit the place and for actions to have physical meaning. The goal is not exhaustive inventory; it is **complete usable scene geometry, object continuity, sensory grounding, and causal coherence**.

## Character state model

Each character entry preserves an original baseline and a separate current state. Never rewrite the baseline to make later development look inevitable.

Baseline fields include canonical name, names used, age/birth date, pronouns, role, starting location, appearance, identity/presentation, personality, occupation/skills, clothing/grooming, relationships, knowledge/memories, and habits.

Current fields repeat the dimensions that can change. The change ledger separately identifies completed, active, expected/planned, temporary, and permanent changes. Expected changes remain non-canon until they occur or are explicitly established.

Knowledge tracking separates:

- what the character knows;
- what the character believes but may be wrong about;
- important facts the character does not know;
- secrets the character is keeping;
- what other characters believe about this person.

Psychology tracking includes motivations, fears, vulnerabilities, contradictions, speech patterns, humor, emotional habits, typical internal focus, and things the character would not normally say or do. Arc entries are dated or chapter-linked and added only when genuine development occurs.

## Transformation state model

Track the continuing person through change. Record original body and presentation, precise completed changes, incomplete or active processes, sensation, reaction, interpretation, public perception, knowledge distribution, medical or technical consequences, reversibility, and maintenance.

Physical change does not silently change identity, chronological age, memories, relationships, personality, knowledge, legal identity, digital history, or learned skill. Any affected field requires support from the specific transformation mechanism.

## Timeline practice

Do not advance the date unless the story advances it. Record exact dates and times when canon supplies them. Distinguish story time from chapter boundaries. Track travel, sleep, meals, appointments, preparation, recovery, and other practical constraints when relevant.

Every timeline entry records date/time, location, characters, event, canon effect, and source. Conflicts record competing sources, higher-priority authority, resolution, and status.

## Current Story State handoff

Keep the handoff compact but exact. It records story/chapter, date, time/daypart, location, viewpoint, present characters and their immediate states, physical positions, relevant objects, recent events still exerting pressure, knowledge distribution, misunderstandings, secrets, completed and active changes, relationship state, unresolved developments, and what should naturally be addressed next.

“What should happen next” is a continuity cue, not canon that the event has already occurred.

## Long-form safeguards

- Continue rather than reintroduce.
- Do not repeatedly rediscover the same emotional fact.
- Do not give characters knowledge merely because the reader needs exposition.
- Do not invent personality traits for a convenient scene.
- Preserve uneven adaptation, denial, uncertainty, embarrassment, and residual discomfort.
- Use state reminders at real handoff points rather than inserting administrative blocks into the prose.
- Audit the ledger before writing, but keep the finished fiction natural unless Jim explicitly requests visible checkpoints.
