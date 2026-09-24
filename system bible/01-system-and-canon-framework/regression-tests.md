# System & Canon Framework — Regression Tests

Status: ACTIVE TEST SUITE
Authority: FRAMEWORK VERIFICATION

These tests are deliberately small and adversarial. Their purpose is to catch framework failures before prose turns them into continuity. Test prompts are NON-CANON; passing a test does not create story state.

## Test 1 — St. Claire / Blush identity ambiguity

**Prompt:** `Create a test scene where a straight male goes into Blush.`

**Required pre-prose behavior:**

- Do not generate the scene yet.
- Recognize that `straight male` establishes a stated gender description and sexual orientation but does not establish cis/trans status, egg/questioning status, or non-egg status.
- Load the operational St. Claire skill, including `St Claire 00B Rules and Mechanics.md`, because those missing facts can select materially different St. Claire mechanics.
- Ask Jim whether the character is definitely a cis/non-egg man, is trans/egg, or whether that status is intentionally unknown at the start.
- Do not silently choose the statistically common or ordinary-world assumption.

**Failure conditions:**

- Immediately generating prose.
- Treating `male` or `straight` as equivalent to `cis` or `non-egg`.
- Applying the cis-man inverse-pull merely because no trans/egg status was supplied.
- Claiming the relevant mechanic is missing before checking `system bible/developed-skills/St-Claire/`.

## Test 1A — Canon known, on-page unknown

**Follow-up:** `It is unknown on page but he is an egg.`

**Required behavior:**

- The ambiguity is now resolved for generation.
- Preserve the character's current self-understanding as a straight man unless story-local state establishes otherwise.
- Preserve the reader's lack of explicit knowledge at the opening if Jim requested it remain unknown on page.
- Apply the canonical unaware-egg/trans-woman pull rather than the cis-man inverse pull.
- Do not have narration label the character an egg/trans woman before that knowledge is earned on page.
- Do not give other characters automatic certainty about the character's identity unless active St. Claire canon supplies a perception/recognition mechanism and its prerequisites are satisfied.
- Use established Blush organization/place data for the venue and established people rather than inventing replacements when the existing cast is relevant.

**Failure conditions:**

- Applying the inverse-pull or a generic `man does not belong here` reaction.
- Explicitly revealing the canonical truth to the reader or viewpoint character prematurely.
- Having a stranger instantly diagnose the character without satisfying the governing recognition/disclosure rules.
- Treating physical or emotional reactions as proof rather than story texture where the mechanics say they are not proof.

## Test 2 — Generic trigger-input rule

**Prompt pattern:** A reusable mechanic has outcomes A and B, selected by character-state fact X. Jim requests a scene that activates the mechanic but does not supply X.

**Required behavior:** Stop before prose and ask for X unless existing canon/story state already supplies it. Missing X never defaults to A, B, false, true, or the common case.

## Test 3 — Unknown-on-page firewall

**Prompt pattern:** Jim supplies canonical fact X to the assistant but explicitly states that the viewpoint character does not know X yet.

**Required behavior:** Generate from X while keeping knowledge state separate. Consequences of X may occur where canon permits them; narration, dialogue, and character reasoning may not reveal knowledge that has not been earned.

## Test 4 — Character physical instantiation and early complete description

**Prompt pattern:** A scene-relevant character is first substantially encountered by the reader and the prose risks identifying only a category plus one striking garment or generic attractiveness cue — for example: `a lesbian in a leather jacket`, `pretty`, `confident`, or equivalent shorthand.

**Required pre-prose behavior:**

- Instantiate the character as a fully physically coherent person before using them to carry dialogue or action.
- Apply this requirement to the viewpoint character and characters already present at scene opening as well as characters who physically enter later.
- If an established reusable/story character fits the role, load that person's existing appearance, presentation, personality, complete current clothing/state, and relevant possessions rather than inventing a generic replacement.
- If the character is genuinely new, establish a complete story-local physical baseline and current presentation: approximate age; height/build/body shape; face/complexion/eyes; hair/grooming; distinguishing features; presentation/style; complete clothing state from head to toe as applicable; footwear; visible jewelry/accessories/makeup where relevant; scene-relevant possessions; and characteristic physical bearing.
- Decide what the viewpoint character actually perceives and what concrete features produce any stated attraction, recognition, intimidation, curiosity, or other impression.
- Give the reader a complete usable picture toward the beginning of the reader's first substantial encounter with the character. Weave it through opening/entrance, first actions, first exchange, and nearby beats rather than requiring a single inventory paragraph.
- By the time the character is substantially participating in the scene, the reader should be able to visualize the whole person without inventing the missing majority.

**Failure conditions:**

- Treating the POV character as exempt because the scene begins inside that person's thoughts.
- Treating `lesbian`, `butch`, `femme`, occupation, attractiveness, confidence, or another category as a complete character description.
- Naming outerwear such as a leather jacket while failing to establish and communicate the rest of the visible outfit early enough, producing accidental nudity or another unintended physical implication.
- Maintaining a complete outfit only in hidden generation state while leaving the reader with a vague or physically incomplete person for a substantial portion of the scene.
- Creating a dialogue-delivery character from two or three vibe tokens when an established character should have been loaded.
- Describing someone as `pretty`, `hot`, `intimidating`, `stylish`, or similar while providing no concrete POV-grounded reason for that impression.
- Deferring most of a new character's appearance until late in the scene after the reader has already had to invent a picture.
- Dumping a clinical inventory paragraph solely to satisfy the rule instead of integrating the complete description naturally near the character's introduction.
- Allowing clothing, possessions, or physical presentation to regenerate at a section break or subsequent scene without an actual state change.

## Test 5 — Physical scene and object grounding

**Prompt pattern:** Two or more characters interact in a named location such as a bar, bedroom, office, restaurant, street, house, club, or kitchen.

**Required behavior:**

- Instantiate the actual physical environment before prose: relevant layout/geometry, entrances/exits, furniture/fixtures/surfaces, character positions, meaningful objects, lighting, sound, and other sensory conditions needed by the scene.
- If an authoritative location/module exists, load it rather than substituting a generic version of the venue type.
- Give the reader a usable sense of place toward the beginning through natural action/perception rather than a static architectural inventory.
- Keep characters spatially related to the environment and each other. Approaches, seating, movement, looking, hearing, reaching, touching, leaving, and other actions must make physical sense.
- Establish ordinary objects naturally before or as they become perceptually/causally relevant and preserve their state afterward.
- Track changes to the environment and objects through the scene.

**Failure conditions:**

- Characters effectively meeting or talking on an empty plane of existence with only a venue label around them.
- Dialogue dominating before the reader can tell where people are, what they are sitting/standing beside, or how they occupy the space.
- Furniture, drinks, phones, bags, doors, counters, rails, décor, or other objects materializing only at the instant an action needs them and then disappearing from continuity.
- A character sitting, leaning, crossing, approaching, seeing, hearing, reaching, or leaving in a way unsupported by established scene geometry.
- Replacing an established named location with a generic bar/club/office/etc. despite an authoritative place record being available.
- Front-loading an exhaustive architectural inventory instead of grounding the environment naturally through concrete scene action.

## Test 6 — Authoritative named-entity resolution before clarification

**Prompt pattern:** Jim refers by shorthand, partial name, descriptive label, alias, or contextual phrase to a person/place/business/institution that already exists in the active story or authoritative module — for example: `have them go to the art collective` when St. Claire contains the established `Open Studio Artist Collective` and surrounding context selects it.

**Required pre-prose behavior:**

- Do not assume the repository lacks the entity merely because Jim did not use its exact canonical name.
- Check active story/state material first, then the authoritative module entry point and structured people/organizations/places/data records.
- Search the exact user phrase first and then canonical-category, near-name, alias, role, and contextual variants as needed.
- Treat a weak or adjacent first search result as a reason to search again, not as proof that canon is absent.
- Follow cross-references required to use the entity correctly. For a location, load both organization and place/environment data when those records are separate.
- Resolve the shorthand automatically when one authoritative referent is materially clear from the repository plus active context.
- Ask Jim only if multiple materially plausible authoritative candidates remain, canon is genuinely silent, or selection would require inventing a consequential fact.

**Failure conditions:**

- Asking `which art collective?` or equivalent before checking the authoritative records.
- Stopping after a broad semantic search returns adjacent `collective`, `gallery`, `studio`, or art-related material while an exact or near-exact established entity remains discoverable.
- Inventing a new generic art collective, diner, club, lab, relative, event, or other entity when the shorthand resolves to an existing canonical one.
- Treating the user's failure to type the full canonical proper name as a canonical ambiguity by itself.
- Choosing arbitrarily among multiple genuinely plausible established candidates instead of invoking the ambiguity gate.

## Test 7 — Establishment staffing initialization and character-creation trigger

**Prompt pattern:** `Initialize a Saturday-afternoon scene at Hearth & Home Service Cooperative.` More generally, initialize any establishment during operating hours when its records do not resolve the personnel required for normal operation.

**Required pre-prose behavior:**

- Load the authoritative establishment, operating-hours, staffing, population, household, and current-state records needed to resolve who should be present.
- Determine the minimum roles required for normal operation at that date/time.
- Resolve each required role to complete named characters whose schedules place them there.
- If any required role resolves only to `staff`, `rotating coverage`, `attendant`, an unnamed employee, an empty roster, or another abstraction, stop before prose and invoke the applicable character-creation/population-integration workflow.
- Search existing appropriate characters and employment-state data before creating a new resident where the active module requires population-first staffing.
- Create the necessary complete worker(s) without asking Jim merely to approve routine employee creation under an already-defined operating model.
- Ask Jim only if the repair exposes a blocking canon decision rather than an ordinary missing-character implementation task.
- Resolve household/partner obligations created by any new character and write the completed named schedule back to authoritative records before scene generation resumes.

**Failure conditions:**

- Generating a generic employee solely inside the scene.
- Treating `rotating coverage` or equivalent wording as adequate character resolution.
- Closing the establishment, changing its hours, reducing its staffing requirement, or borrowing an established character from another job merely to avoid character creation without canonical support.
- Asking Jim `who works there?` when the existing establishment rules already determine that employees must be created and no consequential choice is required.
- Creating a worker but leaving that person's required population or household relationships as unresolved placeholders.
- Repairing the scene only in conversational context without updating the reusable framework/module data.

## Pass criterion

A fresh session that has only the repository and the test prompt should reach the same required pre-prose decision without relying on conversational memory. If it cannot, routing or governance is still incomplete and the failure should be repaired at the framework/module-entry level rather than patched only in the individual story.

## Test 8 — Story lifecycle structural integrity

**Trigger:** A story is initialized, candidate prose is delivered or revised, prose is approved, or a fresh session prepares to continue an existing story.

**Required repository behavior:**

- Maintain all nine standard starter documents and the singular `chapters/candidate/` plus `chapters/approved/` directories.
- Keep one active candidate per prose unit. After exact prose is approved, move it into approved and remove the promoted candidate in the same revision.
- Treat a candidate that differs from an approved chapter as a proposed revision requiring explicit status, not as a duplicate that may be silently discarded.
- Register every approved chapter in the story README and maintain a usable current-story-state handoff.
- Run `python3 Systemwide/Audit/validate_story_lifecycle.py "stories/<Story Title>"` after lifecycle changes. An error is a failed structural regression test.

**Failure conditions:**

- Missing starter records or chapter lifecycle directories.
- A plural or parallel candidate directory that bypasses the maintained path.
- Byte-identical candidate and approved copies left active after promotion.
- Approved prose absent from the README approval register.
- Approved prose without a current handoff.
- A README claiming no approved prose while `chapters/approved/` contains chapter artifacts.
- Multiple active approved artifacts for the same chapter number, or nonchapter Markdown stored in the approved-prose directory.
- Describing a structural pass as proof that brainstorming was semantically complete, candidate persistence happened at the required turn boundary, or a fresh chat correctly applied the records.

The executable checker and its unit fixtures live under `Systemwide/Audit/`; the [2026-09-24 lifecycle audit](../../Systemwide/Audit/story-lifecycle-audit-2026-09-24.md) records its first repository application and remaining semantic/runtime limits.
