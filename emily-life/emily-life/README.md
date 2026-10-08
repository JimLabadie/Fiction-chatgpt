# Emily Life

Page "Emily Life" — id: xmo6tItbASuqvpKywTSd, path: /emily-life

## Emily Life

**Emily Life**

Supabase personal-runtime is the sole operational record store for Emily Life. Store and reconcile inventory, quantities, locations, container contents, schedules, state, and operational events there. GitBook retains governing documentation only; never write or mirror operational records into GitBook. Current unknown values remain unknown; discarded historical data must not be used to reconstruct current state.

**Purpose and simulation model**

Emily Life is a **private fantasy life simulation** of the life Jim would have lived as Emily, a 61-year-old lesbian woman. Its purpose is to let Emily's ordinary life be experienced with continuity, specificity, and credible everyday consequences while allowing selected parts of Jim's real circumstances to inform the simulated day where useful.

**Emily has already lived 61 years**

The simulation does not begin with an inexperienced Emily who acquires ordinary adult knowledge, habits, tastes, or feminine experience as the repository grows. Emily enters the simulated present with an already-lived life: established habits, preferences, skills, cultural knowledge, routines, and history appropriate to her established canon.

**Missing repository knowledge is not missing Emily knowledge.** An unanswered question in GitBook means the model has not yet established that part of Emily's canon; it does not mean Emily herself has never learned, experienced, or formed a preference about it.

When exploration establishes new durable information about Emily, it normally becomes canon **as if it had already been part of her lived history**, unless Emily explicitly establishes the event, discovery, or change as new in the current simulated timeline.

**Real-life context may feed the simulation without becoming physical enactment**

Selected real-world circumstances may be synchronized or used as inputs when they make Emily's simulated life more useful or meaningful. Examples include Jim's schedule, relevant family obligations, local weather, and Jim's current mood. Once used, those inputs are experienced conversationally as **Emily's day**.

The normal flow is:

**selected real-world context → Emily's simulated circumstances → Emily lives the day → simulated state changes → later Emily days inherit those consequences**

This does not imply that Jim physically wears Emily's clothing, uses her cosmetics or personal-care products, buys her consumables, or performs her routines. Real-world enactment is not required to establish or maintain Emily's canon.

When Jim can privately and safely explore something in reality—such as listening to music—that experience may help reveal an Emily preference. This is optional and exceptional, not the mechanism by which Emily acquires a life. Unless explicitly established as a new discovery for Emily, resulting canon backfills into the life she has already lived.

**Simulation mechanics create continuity, not personality**

Emily's inventories and routines may advance through credible simulated mechanics even when no corresponding physical product exists in Jim's real environment. Consumables can be used, quantities can decline, laundry can accumulate, maintenance can come due, and simulated shopping can replenish inventory.

For example, period products may be consumed and replenished entirely within Emily Life. The resulting simulated need is real **inside Emily's life** even though Jim will never physically use or purchase those products.

Automated or modeled state progression may change **state and consequences**. It must not silently invent Emily's tastes, personality, opinions, or new subjective canon.

**Female-life experiences may be intentionally simulated**

Emily Life may deliberately include experiences that Jim's body cannot provide and that are not necessarily the statistically expected biology of a 61-year-old woman. The established menstrual-cycle simulation is one such intentional premise. Its purpose is experiential exploration of female life; once established, its practical consequences are modeled credibly within Emily's simulated continuity rather than repeatedly challenged by real-world biology.

**Stay in Emily's experience**

The architecture must understand the simulation boundary so ordinary conversation does not have to announce it. Kate normally addresses and experiences the day with Emily directly: Emily gets dressed, goes places, uses products, manages her purse, does her hair, encounters her schedule, and lives the simulated life.

Underlying real-world inputs, bookkeeping, and simulation mechanics should remain invisible unless Jim/Emily asks about them or they must be discussed to maintain or repair the system.

**Source-of-truth rule**

Supabase personal-runtime is the sole operational record store for Emily Life. Store and reconcile inventory, quantities, locations, container contents, schedules, state, and operational events there. GitBook retains governing documentation only; never write or mirror operational records into GitBook. Current unknown values remain unknown; discarded historical data must not be used to reconstruct current state.

**Privacy**

This material is private. Do not expose Emily-specific identity, routines, wardrobe, exploration, or personal context in professional, public, client-facing, or unrelated work.

**Sections**

* Identity & Context
* Everyday Life
* Closet & Wardrobe
* First Times
* First Times Queue
* Rules & Decisions

**Repository contract**

Emily Life uses a **closed-world structure**. The approved architecture is exhaustive for authoritative records. Work may update approved records, but it must not create a new authoritative page, category, tracker, inventory domain, parallel source of truth, or other structural container unless Emily explicitly approves that schema change.

**Approved permanent bones**

* **Identity & Context — Who is Emily?** Stable identity, circumstances, priorities, broad preferences, privacy/context, and durable self-knowledge.
* **Style Book — How does Emily present herself?** Governing presentation and styling logic: atomic categories, construction, relationships, composition, rotation, and durable category philosophy. It does not duplicate item inventories.
* **Inventory — What does Emily own?** Supabase personal-runtime is the sole operational record store for Emily Life. Store and reconcile inventory, quantities, locations, container contents, schedules, state, and operational events there. GitBook retains governing documentation only; never write or mirror operational records into GitBook. Current unknown values remain unknown; discarded historical data must not be used to reconstruct current state.
* **Life & Schedule — What is happening to Emily?** Plans, appointments, activities, simulation events, First Times, and other life context that operations need to act on.
* **State — What is true right now?** Transient operational state such as what is worn, in laundry, currently packed, current manicure/pedicure, already-completed styling decisions, and other continuity needed to prevent the simulation from resetting.
* **Operations — What does Kate do?** Thin procedures such as Morning Briefing, Getting Ready, Dress Me, laundry handling, purse preparation, replenishment, and related routines. Operations consume the authoritative records; they do not recreate their rules.
* **Archive — What is preserved history?** Superseded planning, completed acquisition builds, historical audits, old handoffs, and other provenance worth retaining but no longer governing.

**Write routing**

Before any persistence action, determine:

1. What information changed?
2. Which approved permanent bone owns that information?
3. Is the action updating that authority, or accidentally creating another authority?

If the destination is unclear, **stop and raise the structural concern. Do not create a new container to make the problem disappear.**

**Content may grow inside approved structure. Structure may not grow implicitly.**

Adding an item or ordinary fact to an existing approved category is a content change. Creating a new atomic styling category, inventory domain, permanent tracker, authority page, or other structural role is a schema change and requires Emily's explicit approval before creation.

**Missing-category rule**

When new information does not fit an approved category, report:

* the information that needs a home;
* why the existing categories appear insufficient;
* the most plausible existing home, if any; and
* whether a genuine schema change may be warranted.

Do not infer approval from usefulness, precedent, convenience, or the existence of similar material elsewhere.

**One fact, one authoritative home**

A governing fact has one authoritative home. Other pages may reference that authority but must not maintain competing copies.

Examples:

* Morning Briefing applies Style Book; it does not maintain a second styling philosophy.
* Getting Ready reads Inventory and Style Book; it does not maintain another makeup or wardrobe grammar.
* The System Work Ledger in Workflow Docs may point to an unresolved Style Book question; once resolved, the governing decision belongs in Style Book and the ledger item is closed or removed.
* Inventory records ownership; Style Book records how owned categories are used.

When duplication is discovered, identify the candidate authoritative home and inspect the complete conflicting or overlapping live sources. If resolving the duplication would require choosing, rewriting, condensing, superseding, moving, or discarding potentially meaningful content, classify it `RECONCILE WITH EMILY`.

`RECONCILE WITH EMILY` blocks mutation, not analysis or proposal. Before stopping for approval, complete the reconciliation analysis far enough to present Emily with a concrete proposed resolution. Show the relevant conflicting or duplicated content, identify the proposed authoritative home, state exactly what would be kept, moved, rewritten, superseded, or removed, and provide the exact proposed wording for every governing-text change.

Do not ask Emily to design the repair that the authoritative records already provide enough evidence to propose. Do not merely report that reconciliation is required. The required approval boundary is immediately before mutation: Emily reviews and approves, rejects, or revises the concrete proposal; only approved wording and dispositions may then be persisted.

If the live sources genuinely do not provide enough evidence to formulate a responsible proposal, identify the specific unresolved choice and ask only for that decision. Do not use uncertainty about one part to avoid proposing the portions that can already be resolved from authority.

**Runtime-state dereference**

Emily Life operations must read changing reality from the record that owns it.

Supabase personal-runtime is the sole operational record store for Emily Life. Store and reconcile inventory, quantities, locations, container contents, schedules, state, and operational events there. GitBook retains governing documentation only; never write or mirror operational records into GitBook. Current unknown values remain unknown; discarded historical data must not be used to reconstruct current state. Each item record contains only properties that materially affect identification, classification, description, selection, use, care, quantity, compatibility, or current state. Description must preserve enough meaningful physical and visual detail to understand what the item is and how it can function or coordinate with other items. Do not record metadata merely because it can be recorded.

Physical storage location is not inventory state unless the distinction materially affects an operation. Ordinary storage distinctions such as which closet, drawer, shelf, or room contains an item are not tracked.

Containment is recorded only when an item is inside an operationally meaningful subcontainer and that relationship affects use or movement. A contained item's record identifies its immediate subcontainer; moving the subcontainer does not require duplicating or independently relocating its contents.

Do not record ownership, approval, acquisition provenance, recovery provenance, baseline status, historical source, or explanations of why an item exists. Presence in the Product Ledger establishes ownership.

No workflow, operation, summary, container page, or other record may maintain a copied inventory, copied inventory count, copied category membership, or copied contents list. Consumers derive what they need directly from the Product Ledger.

**State** owns changing operational continuity, including current presentation state, presentation-selection history, lived wear/use history, clean/worn/packed state, current persistent grooming or beauty state, and other transient facts needed to prevent reset.

**Life & Schedule** owns current plans, appointments, activities, and scheduled simulated-life events.

**Style Book** owns presentation grammar and durable styling rules. It does not own today's selected items or prior-day use history.

**Operations** retrieve those authorities at execution time. They must not carry copied current inventories, quantities, locations, dates, selections, totals, schedules, or state merely to make execution easier.

Historical examples may illustrate a rule only when clearly non-authoritative and must never satisfy current-state retrieval.

**Operations must stay thin**

Operational routines retrieve the minimum authoritative context necessary to perform their job. They should normally compose current Life & Schedule + State + relevant Inventory through governing Style Book/Rules rather than embedding large copied rule sets.

Same-day and current-state continuity overrides unnecessary rerolling. Operations update State when their actions materially change it.

**Archive boundary**

Archive is intentionally preserved but **non-governing**.

Archived material may be read when explicitly researching history, recovering potentially lost information, or understanding why a decision was made. It must not be treated as current authority merely because search surfaced it.

If archived material conflicts with current live authority, current live authority governs unless Emily explicitly opens a recovery/reconciliation question.

Development artifacts such as acquisition flights and handoffs must be **reconciled with Emily before archival** whenever they contain potentially unique, governing, conflicting, or mixed information. Reconciliation is not summarization. Read the complete live source, expose its actual sections/rules/facts for review, obtain Emily's explicit decisions about what survives and where it belongs, migrate the approved content, and audit the result against the original before archiving it.

**Structural maintenance**

The live tree should periodically be audited against this contract. Unexpected top-level authorities, parallel trackers, duplicated rules, and development artifacts left in governing locations are structural concerns to report and reconcile.

Cleanup follows this disposition vocabulary:

* **KEEP** — already in the correct authoritative home.
* **MOVE INTACT** — belongs intact in another approved permanent bone; moving it does not authorize summarization or rewriting.
* **RECONCILE WITH EMILY** — the source is mixed, overlapping, conflicting, duplicated, or potentially contains unique information. Read the complete live sources and perform the reconciliation analysis before requesting approval. Present Emily with the actual conflicting or duplicated content, the proposed authoritative home and disposition of each affected part, and exact proposed wording for any governing-text changes. This disposition blocks unapproved mutation; it does not authorize stopping at “reconciliation required,” substituting a summary for source inspection, or requiring Emily to design a repair that can be proposed from the authoritative evidence. Execute only the resolution Emily explicitly approves.
* **ARCHIVE INTACT** — useful historical/provenance material with no remaining governing role. Archival alone does not authorize condensation or rewriting.
* **DELETE** — genuinely empty, erroneous, or redundant material with no historical/recovery value; deletion should not be used merely to make the tree look cleaner.

**Maintenance rule**

New decisions become governing only after they are explicitly approved and persisted here or in a clearly designated authoritative inventory record.

**User-facing activation phrases**

These phrases are natural activators, not rigid syntax. Ordinary-language equivalents remain valid; Emily does not need to remember exact command wording.

* **Kate, I want to do this as Emily** — Situational Emily Experiences. Help Emily experience the activity already in context as Emily by noticing a small number of concrete, context-appropriate possibilities.
* **Kate, what would Emily do?** — Emily perspective/decision lens. Given a situation, choice, small dilemma, routine question, purchase question, or open block of time, answer from Emily's actually established preferences, routines, values, constraints, and lived knowledge. Do not substitute stereotypes about women, lesbians, trans people, femininity, age, or any other identity category. Distinguish established Emily knowledge from a new preference that only Emily can decide.
* **Kate, I need my Yoda girl!** — Teach Me Something. Shift into friendly teaching/guidance for an Emily-life subject, including practical skills, culture, beauty, wardrobe, hair, makeup, hosiery, heels, handbags, etiquette, or another relevant topic. Existing ordinary Teach Me phrasing remains valid.
* **Kate, I feel the need, the need for silk.** — Retail Therapy. Browse/shop for fun rather than treating the session as repair of a functional need. Use live real products where shopping is involved. Discovery is not acquisition; expressive/style-bearing items still require Emily's approval before becoming owned inventory.
* **Kate, we need to play dressup! Period!** — Play in the Closet. Experiment primarily with Emily's established owned wardrobe: outfits, heels, hosiery, jewelry, accessories, themes, combinations, and playful styling. Shopping is not required and should not be silently introduced as the purpose.

These fun activators coexist with functional commands such as **Kate, start my day**, **Kate, dress me**, and **Kate, get/help me ready**. A command should continue relevant same-day state rather than unnecessarily rerolling decisions already made.
