# Templates and Schemas

Status: ACTIVE STRUCTURAL REFERENCE

## Series folders

Author-established rule (2026-09-14): store each series under `stories/<Series Title>/`, using the readable series title as its folder name. Preserve spaces and capitalization where supported; replace only characters that cannot be used in a folder name. Do not use the protagonist's name or an opaque series ID as the folder name.

During planning, use the current working title and mark it provisional in the series record. If the title changes, rename the folder and update repository links, indexes, and references in the same revision. Keep all series-specific plans, bibles, chapter drafts, timelines, and state records together under that folder. Shared framework material remains under `system bible/`.

## Standard series starter documents

Author-approved on 2026-09-14. Create all nine documents when starting a new series, populated with known facts and explicit **Not yet established** fields:

| Document | Controlling purpose |
|---|---|
| `README.md` | Overview and document index |
| `series-bible.md` | Durable premise and scope |
| `character-bible.md` | Characters, perceptions, relationships, and development |
| `world-and-setting.md` | Shared references and series-specific setting |
| `voice-and-style.md` | House voice and series narration choices |
| `series-outline.md` | Approved plans and proposed scene choices |
| `timeline-and-continuity.md` | Accepted events and continuity |
| `current-story-state.md` | Exact handoff |
| `series-development.md` | Decisions, reasoning, proposals, and open questions |

README includes navigation, chapter workflow, and an approval register. The development record retains decisions, reasoning, open questions, and rejected alternatives. Link to shared world and house-voice records; do not duplicate entire shared bibles. Each fact has one controlling home. An approved plan is not a completed event.

## Chapter artifacts and lifecycle

Create `stories/<Series Title>/chapters/candidate/` and `stories/<Series Title>/chapters/approved/` at series startup. Empty folders may contain `.gitkeep` placeholders.

Name each chapter artifact `<Series Title> - <Chapter Number> - <Chapter Title>.<extension>`. Use readable titles and zero-padded, series-wide sequential numbers (001, 002, ...). Preserve full display titles in the document; replace only filename-unsafe characters in the filename. Book membership belongs in the outline; numbering remains unique across the series. Apply the same base name to document exports.

Example: `A Life in Plain Sight - 001 - The Door.md`.

1. Write and revise chapter prose in candidate.
2. Approval of the exact chapter text must come from the author. Outline approval, approval of another chapter, silence, or a successful upload does not approve prose.
3. After approval, move that chapter into approved with the same filename. Remove the candidate copy as part of the same commit; do not keep two active versions.
4. Record number, title, book, approved revision, approval date/source, and artifact link in the README approval register.
5. Update the timeline, current story state, changed character/relationship facts, relevant durable world/premise facts, and outline progress in the same revision.
6. To revise approved prose, leave the existing approved chapter intact while preparing the proposed revision in candidate. Only after the author approves the revision should it replace the approved artifact; then remove the candidate and reconcile downstream continuity. Git preserves earlier versions.
7. If the series or chapter title changes, rename affected artifacts and update links and registers together.

Unknown titles/numbers must be resolved sufficiently to give a new chapter its own unambiguous filename. Do not create empty prose files for planned chapters; planning belongs in the outline.

## Master Story Bible schema

The master bible stores permanent canon: title and premise; world possibilities and impossibilities; transformation, technology, magic, memory, identity, and social rules; immutable facts; setting, era, and culture; foundational relationships; major canon events; important objects, terms, institutions, and rules; permanent changes; and intentional canon revisions.

Permanent-change entries preserve the original state, the change, and the canonical result. Canon revisions preserve the old fact, new fact, reason, and effective story point.

## Story identity and audience binding

Each Story Bible also records:

- mode: private persona fiction or commercial fiction;
- intended readership and product;
- MC's story name, surname if needed, and aliases;
- persona selection: Jim explicitly selected, or a distinct protagonist;
- baseline identity, pronouns, biography, and current identity state;
- POV and tense;
- selected world and history modules;
- which character occupies creator, owner, anchor, and related roles;
- patron alias, retaining J. unless deliberately changed;
- inherited module facts and any expressly approved departures.

If a commercial MC has not yet been named, use `[MC_NAME]` in planning and resolve it before producing finished prose. Do not silently fill the name with Jim.

## Character Bible schema

Each entry contains identity and role; original/baseline state; current state; completed, active, expected, temporary, and permanent changes; knowledge, beliefs, ignorance, and secrets; motivations, fears, contradictions, voice, humor, emotional habits, and behavioral limits; relationship-specific perceptions and tensions; and a dated/chapter-linked development log.

The baseline is historical and must not be rewritten to conceal development.

## Framework event schema

A **framework event** is a reusable world event whose definition belongs to the shared System Bible while its activation and occurrence are tracked by each story that selects the relevant framework components.

A framework-event definition records, as applicable:

- event name and controlling framework component;
- prerequisites or applicability conditions;
- activation condition or trigger;
- delay/offset or other ordering constraint;
- reusable event content and required participants;
- reusable consequences or state transitions;
- story-local freedoms and intentionally open fields.

Stories do not copy or redefine the framework event. They track the event's story-local state, using states such as **dormant**, **scheduled/due**, **active**, and **completed** where applicable, together with the story-specific activation point, occurrence, consequences, and source.

When a story satisfies a framework event's activation condition, continuity work must surface and track the event. Activation does **not** authorize ChatGPT to hijack narrative pacing or force the event into the next scene. Jim retains control of when and how the activated event is dramatized, subject to established chronology and continuity.

Framework events may be triggered by time, location or institution state, a reveal, knowledge state, relationship state, another event, selected framework components, or other canonically defined conditions. If established reusable material does not fit an existing schema, preserve what the material is and extend the framework deliberately rather than reclassifying, genericizing, or discarding it merely to fit an existing bucket.

**Project Artemis is the reference example:** its reusable definition belongs to the Athena/framework canon; Athena's reveal activates it with a **+1 day** offset; each story records whether that trigger has fired and the event's current story-local state.

## Timeline schema

Each event contains date/time, location, characters, event, canon effect, and source. The continuity fact register tracks possessions, appearance/grooming, clothing, injury/fatigue, learned information, promises/plans/appointments, and relationship changes. The conflict log contains issue, sources, controlling authority, resolution, and status.

## Current Story State schema

The handoff contains story/chapter, canonical date, time/daypart, location, viewpoint, present characters with immediate physical/emotional/clothing state, physical positions, relevant objects, recent events still mattering, knowledge distribution, misunderstandings, secrets, completed and active changes, current relationship state, unresolved developments, and immediate next-story context.

## Ideas schema

Separate areas hold story ideas, possible scenes, possible developments, alternatives, unresolved questions, and rejected/superseded ideas. Everything remains non-canon unless explicitly promoted or unambiguously established in accepted story.

During substantive brainstorming and development, preserve useful creative possibilities before evaluation can erase them. This includes Jim's ideas, ChatGPT proposals, jointly developed possibilities, implications discovered through discussion, competing alternatives, promising rabbit holes, and useful rejected or deferred paths. Preserve the developed detail and reasoning rather than only a title or summary.

Each preserved item records enough provenance and status to distinguish, as applicable:
- Jim-originated material;
- ChatGPT-originated proposal or inference;
- jointly developed material;
- unresolved/deferred possibility;
- rejected or superseded alternative;
- established/approved decision, which must also be persisted to its controlling canon destination when applicable.

Recording an idea does not approve it, canonize it, attribute it to Jim, or require immediate evaluation. The purpose of the ideas/development record is to let brainstorming remain expansive without forcing Jim to choose prematurely merely to prevent useful material from disappearing.

## World lexicon schema

The recovered World Lexicon is a blank template, not an established world. Its useful fields are world rules and physics; chronology/calendar; economy/currency; travel/communication limits; factions with goals, leadership, reputation, reality, aesthetics, and symbols; regions with climate, demographics, culture, significance, and landmarks; and a glossary containing origin, definition, and usage context.

Example entries such as `Ether-burn` and `Iron-pact` are placeholders and are not Jim the Saga canon.

## Prompt input schema

When requesting narrative generation, provide only the context needed for the next section:

- controlling story and module names;
- the story's MC name, persona selection, and audience binding;
- current handoff point;
- requested action or scene scope;
- POV and tense if not already fixed;
- relevant continuity anchors;
- relevant mechanic instance if one is active;
- explicit stopping point if the story must not advance beyond it.

Do not require the visible story output to reproduce administrative tables unless the story's own format calls for them. Internal state checking and natural prose are compatible.

## State correction protocol

When an audit is wrong, Jim's corrected state replaces the incorrect claim at the appropriate authority level. The correction must also update any dependent Character Bible, Timeline, Current Story State, or conflict record. A chat acknowledgement alone is not persistence; the file change must be performed and verified.
