# Templates and Schemas

Status: ACTIVE STRUCTURAL REFERENCE

## Master Story Bible schema

The master bible stores permanent canon: title and premise; world possibilities and impossibilities; transformation, technology, magic, memory, identity, and social rules; immutable facts; setting, era, and culture; foundational relationships; major canon events; important objects, terms, institutions, and rules; permanent changes; and intentional canon revisions.

Permanent-change entries preserve the original state, the change, and the canonical result. Canon revisions preserve the old fact, new fact, reason, and effective story point.

## Character Bible schema

Each entry contains identity and role; original/baseline state; current state; completed, active, expected, temporary, and permanent changes; knowledge, beliefs, ignorance, and secrets; motivations, fears, contradictions, voice, humor, emotional habits, and behavioral limits; relationship-specific perceptions and tensions; and a dated/chapter-linked development log.

The baseline is historical and must not be rewritten to conceal development.

## Timeline schema

Each event contains date/time, location, characters, event, canon effect, and source. The continuity fact register tracks possessions, appearance/grooming, clothing, injury/fatigue, learned information, promises/plans/appointments, and relationship changes. The conflict log contains issue, sources, controlling authority, resolution, and status.

## Current Story State schema

The handoff contains story/chapter, canonical date, time/daypart, location, viewpoint, present characters with immediate physical/emotional/clothing state, physical positions, relevant objects, recent events still mattering, knowledge distribution, misunderstandings, secrets, completed and active changes, current relationship state, unresolved developments, and immediate next-story context.

## Ideas schema

Separate areas hold story ideas, possible scenes, possible developments, alternatives, unresolved questions, and rejected/superseded ideas. Everything remains non-canon unless explicitly promoted or unambiguously established in accepted story.

## World lexicon schema

The recovered World Lexicon is a blank template, not an established world. Its useful fields are world rules and physics; chronology/calendar; economy/currency; travel/communication limits; factions with goals, leadership, reputation, reality, aesthetics, and symbols; regions with climate, demographics, culture, significance, and landmarks; and a glossary containing origin, definition, and usage context.

Example entries such as `Ether-burn` and `Iron-pact` are placeholders and are not Jim the Saga canon.

## Prompt input schema

When requesting narrative generation, provide only the context needed for the next section:

- controlling story and module names;
- current handoff point;
- requested action or scene scope;
- POV and tense if not already fixed;
- relevant continuity anchors;
- relevant mechanic instance if one is active;
- explicit stopping point if the story must not advance beyond it.

Do not require the visible story output to reproduce administrative tables unless the story's own format calls for them. Internal state checking and natural prose are compatible.

## State correction protocol

When an audit is wrong, Jim's corrected state replaces the incorrect claim at the appropriate authority level. The correction must also update any dependent Character Bible, Timeline, Current Story State, or conflict record. A chat acknowledgement alone is not persistence; the file change must be performed and verified.
