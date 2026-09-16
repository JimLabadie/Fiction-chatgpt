# St. Claire — Population & Characters

The single searchable record of every named person in St. Claire, regardless of role, status, or how minor. This is the duplicate-checking backbone for the whole project — before naming anyone new, check here first.

**Source of truth order:** St_Claire_00_Concept.md governs the lore. St_Claire_00B_Rules_and_Mechanics.md governs the checkable rules and generation process. St_Claire_01_Founding_Pioneers.md holds founding-era history for the twelve. This document holds everyone's current status — including the twelve founding mothers, per the two-record rule, even when their entry here is minimal (e.g. "retired — journalist" or "deceased").

**Related documents (the full schema):** St_Claire_04_Households.md, St_Claire_05_Organizations.md, St_Claire_06_Places.md, St_Claire_07_Occupations.md. Character records here cross-reference all four rather than duplicating their data.

**Population process:** full rule in St_Claire_00B_Rules_and_Mechanics.md. Names are added here in small batches, checked against everyone already listed before adding more.

## Character Record Template

Every new or substantively repaired adult entry in this document uses this format. Legacy entries that predate a field are not silently assigned a value; they are upgraded from established evidence during the population-integration audit.

- **Name**
- **Status:** active / retired / deceased
- **Birthdate**
- **Tags** — any category memberships this person holds, as a list (e.g. "Founding Mother — leadership & governance," "Informal Mayor," "Council member"). A person can carry multiple tags; this is how categorization works instead of splitting the document into separate sections.
- **Physical description & presentation** — how she looks, how she presents (per Who St. Claire Is For and Feminism & Gender Expression) — enough to actually picture her, not just a label
- **Voice** — how she talks, a real personality signature
- **Occupation** — profession/trade/working identity from the Occupation lookup list (St_Claire_07). Occupation is not the same thing as current employment.
- **Employment state** — full-time / part-time / self-employed / unemployed-seeking / unemployed-not-seeking / between jobs / student / caregiving / retired / disabled or otherwise not working / other established state. Do not infer a state from a blank employer field.
- **Role/Title at Organization** — if applicable; references a specific Organization (St_Claire_05) and whatever title it uses, unless that org's own record flags an exception. Informal, non-Organization-based social roles (like the Mayor) belong in Tags, not here.
- **Work schedule / availability** — when employed, enough recurring schedule to resolve whether the person is plausibly at work for a given day/time; when not fully employed, established availability for additional work if known. Unknown remains unknown rather than being invented.
- **Routine/regular haunts** — where this character habitually is outside of work/home: a standing diner order, a bar she's a regular at, a weekly walk — specific enough to answer "would she plausibly be here" for a given day/time, not just a vague hobby list
- **Household** — references a Household record (St_Claire_04) rather than duplicating residence/relationship data
- **Arrival story** — how/when she joined the community (per the Rites of Passage intake process), or "born here"
- **Notable milestones** — Bloom Day, wedding, etc., if relevant
- **One real, specific trait** — something that makes her a person, not a list of facts
- **Connections** — mentor/mentee, family, named relationships to others already in this document

### Employment-state migration rule

Legacy Population entries are not assumed to be unemployed merely because `Employment state` or `Work schedule / availability` is absent. During staffing/population integration, established occupation, organization, retirement, school, caregiving, and other evidence is used to populate the new fields. Where the evidence does not settle the state, mark it unresolved in the audit rather than manufacturing an answer.

Before a new business employee is invented, search Population and active staffing records for residents explicitly established as unemployed-seeking, underemployed/part-time and seeking more work, between jobs, or apprenticeship-seeking. A missing employment-state field is not an available-worker flag.

## Child Record Template

Children get a deliberately different, minimal template — not the adult presentation/voice fields above, which are specifically about adult lesbian identity culture and don't apply to children (per Concept.md, Family Formation & Co-Parenting):

- **Name**
- **Age**
- **Household** — references a Household record (St_Claire_04)
- **School grade** — if applicable
- **Personality/interests** — brief, real specifics, not a full adult-style profile

---

## Population

> **Legacy dataset preserved below.** Existing records remain authoritative for facts they actually establish. The new Employment state and Work schedule / availability fields are being added through the active population-integration audit; absence of those fields in a legacy record means unresolved migration, not unemployment.

[Existing Population records continue unchanged from the prior version; this schema migration does not alter established character facts.]