# Present

Status: PROTOTYPE — NON-GOVERNING
Purpose: Resolve a character's coherent current presentation from established individual canon, available resources, applicable context, and current state without turning demographic defaults or generated choices into character canon.

## Use when

Use this skill when a task requires deciding or checking how a character presents in a specific situation: clothing, silhouette, grooming, hair, makeup, footwear, jewelry/accessories, visible body presentation, or the composition of those elements.

This skill resolves presentation. It does not own the underlying character, culture, wardrobe, body, transformation mechanics, or prose style.

## Input model

Inputs are extensible prompts, not mandatory fields. Retrieve only what is relevant and established:
- explicit current presentation state;
- individual character canon/history;
- body, age, proportions, mobility, and physical constraints where relevant;
- character Presentation Profile: taste, presentation intent, invariants, exceptions, body relationship, skills/competence, development;
- Presentation Vocabularies and signifiers applicable to the character;
- culture/community/generation/occupation/context where materially relevant;
- occasion, setting, weather, activity, dress code, safety, and practical constraints;
- wardrobe, possessions, products, resources, budget/status, and availability;
- hair/grooming/makeup state and competence;
- continuity/history: what was worn, changed, acquired, established, or ruled out;
- authorial aesthetic/world defaults when current governance establishes them.

## Precedence and separation

1. Explicit current state and current authoritative character canon outrank generic presentation knowledge.
2. Stable individual preference is distinct from temporary constraint. A constraint may alter today's expression without rewriting what the character likes.
3. Identity, presentation, personality, and observer interpretation are distinct dimensions. Do not infer one mechanically from another.
4. Presentation vocabularies are visual/compositional languages, not uniforms or demographic requirements.
5. Examples illustrate possibilities; they are not requirements.
6. Available wardrobe/resources constrain what can be selected without silently creating possessions.
7. Competence constrains what the character can personally execute; use assistance, services, or the Inhabit skill only when established circumstances support them.
8. A generated free choice is scene resolution, not durable canon, unless accepted/persisted through the governing process.

## Procedure

1. **Resolve the individual first.**
   Retrieve the character's current presentation state, Presentation Profile, relevant history, known wardrobe/resources, and hard invariants. If the individual canon already resolves the question, do not overwrite it with context.

2. **Resolve the situation.**
   Identify the actual presentation problem: occasion, activity, setting, formality, weather, occupational requirement, safety/practical constraint, narrative timing, and any explicit author instruction.

3. **Load only applicable context.**
   Use Contextualize for cultural, generational, occupational, community, regional, class, or other social meaning when it materially affects the presentation. Context may shape interpretation and available vocabulary; it does not replace individual preference.

4. **Resolve body/current-state constraints.**
   Use the character's established current body/presentation state. If transformation mechanics are active, Transform controls what changed; Present does not infer additional bodily or identity changes.

5. **Resolve resources and continuity.**
   Prefer established wardrobe, possessions, products, services, and resources. Check prior presentation continuity. Do not silently invent a closet, purchase, appointment, or possession merely because it would complete a look.

6. **Resolve competence.**
   Determine whether the character can execute the required grooming, styling, garment use, footwear, cosmetics, accessories, or upkeep. If not, use established help/services or Inhabit to resolve the learning/performance gap. Do not grant competence from gender, identity, culture, or transformation alone.

7. **Compose the whole presentation.**
   Build a coherent composition from silhouette, proportion, material, color, grooming/hair/makeup, footwear, jewelry/accessories, and other relevant channels. Whole-composition coherence outranks optimizing one garment or signifier in isolation.

8. **Check meaning and character fit.**
   Test the composition against personal grammar, invariants, occasion, cultural/context meaning, body/current state, resources, competence, and continuity. Avoid stereotype completion and costume-like over-signaling unless canon or scene intent explicitly calls for it.

9. **Separate resolved presentation from prose.**
   Produce a coherent internal/current presentation state first. When prose is requested, pass that state to the writing/prose layer, which selects only details meaningful to POV, action, character, or scene. Do not dump the full resolver output into narration.

10. **Handle persistence deliberately.**
    Wearing/selecting something in one generated scene does not automatically create a permanent preference, wardrobe acquisition, signature look, or character trait. Hand explicitly accepted durable changes to Track State/Persist.

## Output contract

A presentation resolution should be able to state:
- resolved current composition;
- which elements came from established canon/resources;
- which constraints modified expression;
- any unresolved resource/competence gap;
- any contextual meaning that materially matters;
- which choices are scene-local rather than durable canon.

## Guardrails

- No stereotype completion.
- No automatic demographic wardrobe, grooming, hobby, personality, or competence.
- No silent possessions or purchases.
- No silent body/identity changes.
- No canonization of free generated choices.
- No treating temporary constraint as preference change.
- No treating presentation vocabulary as a uniform.
- No confusing observer reading with character identity.
