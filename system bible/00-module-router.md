# Mandatory System Module Router

Status: GOVERNING WORKFLOW
Scope: ALL STORY DEVELOPMENT, CONTINUITY, REVISION, DRAFTING, RECOVERY, AND SOURCE AUDIT

## Purpose

The System Bible contains reusable modules that function like skills. They are not useful if a writer must remember from prior conversation which module exists. This router is the mandatory discovery layer.

## ChatGPT Project bootstrap and operating contract

Pasteable Project bootstrap: `system bible/00-chatgpt-project-bootstrap.md`
Full operating contract: `system bible/00-project-bootstrap-template.md`

LOAD WHEN setting up a new ChatGPT Project for this repository, auditing Project bootstrap behavior, diagnosing why a fresh Project/chat did not discover this router, or revising the Project-level operating contract. The compact bootstrap is the text deployed into ChatGPT Project Instructions; it retrieves the full repository operating contract and this router. The repository files are maintained sources; installed Project Instructions do not automatically synchronize.


Before substantive story work, retrieve this router first. Match the requested task, planned scene, characters, setting, relationships, objects, technologies, continuity questions, and recovery/source-audit needs against the triggers below. Retrieve every matched controlling System Bible module before analysis or prose. When a matched parent module points to a detailed reference that is relevant to the task, retrieve that detail too.

Do not rely on memory, story summaries, or a previously loaded subset to decide that an omitted module is irrelevant. Multiple modules may trigger from one scene. Err toward loading an overlapping module when its trigger is plausibly implicated; source conflicts are cheaper than invisible omissions.

## Active-story namespace firewall

Before story-local retrieval or search, resolve the active story. Treat its `stories/<story-name>/` directory as a closed namespace.

For ordinary development, continuity, revision, and drafting:
- search/retrieve the active story directory and deliberately routed System Bible material;
- do not use another `stories/<other-story>/` directory as evidence, inspiration, recovery, characterization, continuity, or gap-filling;
- do not import another story's facts from Memory, conversation summaries, prior chats, or familiar names;
- if a repository-wide discovery search is necessary, discard other-story hits as out of scope unless Jim explicitly requested cross-story comparison, crossover, migration, or recovery;
- absence in the active story means unresolved, not permission to borrow, infer, invent, or genericize an answer. A known group, count, role, or relationship slot does not authorize a generic placeholder member; recover the established individual if one exists or leave the slot unresolved until Jim establishes it when consequential.

Before applying a character fact, verify both the character's canonical full name and active story namespace. Persistent named characters require surnames before established continuity use or manuscript appearance. Same/similar first names, occupations, archetypes, voices, or roles never establish identity across stories. Even matching full names remain separate story-local entities unless shared identity is explicitly established by maintained System Bible canon or Jim.


**System Bible authority is absolute for operating canon.** Only maintained files under `system bible/` that are part of the harmonized System Bible parent/detail structure may control story or framework truth. `system bible/developed-skills/**` is **unaudited original/recovery source material only**. Its `SKILL.md` files and contents may be searched as evidence during recovery, but they are never operating canon, never a story-generation authority, and never a substitute for a harmonized System Bible destination. Material found there must be audited, reconciled, and deliberately promoted into the appropriate maintained System Bible module before it may control story work.

## Mandatory routing sequence

1. Retrieve this router.
2. Describe the task/scene internally in concrete nouns and actions: who is present, where, what relationships are active, what identities/presentations matter, what technology/institutions/property/money are involved, whether transformation/age/life-stage issues are active, and whether the task is asking what historical/source material exists or was lost.
3. Match that description against ALL module triggers below, not merely the most obvious one.
4. If the task is archive recovery, source audit, corpus coverage, provenance, historical comparison, duplicate/version analysis, lost-material recovery, cataloging, or consolidation, retrieve `system bible/00-archive-recovery-and-source-audit-protocol.md` and then its mandatory `Systemwide/Audit/` entry points before ad hoc source discovery.
5. Retrieve every matched parent module and relevant linked detail.
6. Retrieve story-local authority as required by the task.
7. For prose, run the hard pre-draft scene gate in `00-mandatory-source-grounded-drafting.md`: resolve the actual place/establishment, environment, present people and staff, schedule where relevant, story-cast physical state, objects/operations, spatial continuity, and scene plan. Retrieval alone does not satisfy this step.
8. If a matched module creates a conflict, unresolved prerequisite, or unresolved required scene input, stop and report it before silently drafting around it. Do not evade a blocker by leaving the establishment/person/place unnamed, genericizing it, inventing a convenience NPC, or omitting the physical world.
9. Draft/analyze only after routing **and the applicable hard pre-draft gate** are complete.
10. Audit the result against the same loaded modules and the resolved scene inputs. This audit must verify application, not merely retrieval: materially applicable source information must actually constrain or inform the result. For prose, the post-draft source-fidelity gate is mandatory before delivery.
11. For prose, provide the source receipt required by `00-mandatory-source-grounded-drafting.md`, including this router and all matched modules actually retrieved. A receipt is evidence of retrieval only; it is not evidence that the source was applied or that the hard gates passed.

## Recovery / source-audit routing

Path: `system bible/00-archive-recovery-and-source-audit-protocol.md`
Mandatory structural baseline: `Systemwide/Audit/`

LOAD WHEN:
- Jim asks to search/check the archive, chats, source documents, original documents, historical files, developed skills, obsolete material, or recovery evidence;
- determining whether information existed before, was lost during consolidation, survives only in an older version, or is adequately represented in current modules;
- determining where a detail came from or whether it is source-derived, inferred, or invented;
- cataloging, consolidating, deduplicating, comparing versions, deciding what historical material should be retained, or assessing corpus coverage;
- a task depends on claims such as `not found`, `the archive says`, `the original intent was`, `this version supersedes that one`, or `these files are duplicates`.

MANDATORY FOLLOW-THROUGH:
- retrieve `Systemwide/Audit/README.md`;
- retrieve `Systemwide/Audit/component-coverage-register.md`;
- consult relevant Audit inventories/tables before recreating catalogs or relying on ad hoc searches;
- distinguish structural inventory/machine extraction from semantic/claim review;
- persist recovery progress rather than relying on conversational memory.

## Reusable module triggers

### 01 — System and Canon Framework
Path: `system bible/01-system-and-canon-framework.md`
LOAD WHEN determining canon authority, story-vs-shared-world ownership, consent/agency, identity interpretation, intimacy boundaries, recovery evidence, conflict resolution, or what source is allowed to establish a fact.

### 02 — Athena
Path: `system bible/02-athena.md`
LOAD WHEN Athena, S.A.R.A.H., Asteria Intelligence, Project Artemis, hidden AI activity, AI daughter/family relationship, authorization/permission, provenance/version history, pink Mini/Corvette, or Athena-driven commercial activity appears or matters. Load relevant `02-athena/` detail files when needed.

### 03 — Relationships, Family, and Polycule
Path: `system bible/03-relationships-family-and-polycule.md`
LOAD WHEN a polycule/multi-partner relationship, closed/open boundary, polyfidelity, metamour relationship, shared partner network, romantic family, outside dating/flirting/intimacy, integration/invitation, jealousy, household decisions, or joining/leaving matters. Load `invitations-and-integration.md` when implicated.

### 04 — Transformation and Swap Mechanics
Path: `system bible/04-transformation-and-swap-mechanics.md`
LOAD WHEN transformation, body change/swap, sex-characteristic or age change, identity continuity, adaptation, changed anatomy/appearance/abilities, or original-vs-current-state continuity matters.

### 05 — Culture Reference Toolkits
Path: `system bible/05-culture-reference-toolkits.md`
LOAD WHEN race, ethnicity, nationality, religion, regional culture, class formation, family/generational culture, cultural values, code-switching, culturally shaped voice, or culture-specific institutions materially affect characterization or scene texture.

### 06 — Sapphic Culture
Path: `system bible/06-sapphic-culture.md`
LOAD WHEN lesbian/sapphic/WLW/femme/butch/masc/soft-butch/lipstick/chapstick identity or presentation; sapphic spaces/dating/community norms; visual signals; or femme/butch presentation materially matters. Load the relevant maintained child reference(s) linked from `system bible/06-sapphic-culture.md` for the specific subject matter implicated by the task. Pair with gender-presentation material for trans sapphic characters.

### 07 — St. Claire
Path: `system bible/07-st-claire.md`
LOAD WHEN a scene occurs in St. Claire or uses its residents, businesses, institutions, streets, zones, events, history, community norms, geography, architecture, or landmarks. Load relevant maintained references under `system bible/07-st-claire/`. Never route story work to `system bible/developed-skills/St-Claire/`; that directory is unaudited recovery source only.

### 08 — Estate / Dreamhouse / Obsidian Vanguard
Path: `system bible/08-estate-dreamhouse-obsidian-vanguard.md`
LOAD WHEN the Estate/Dreamhouse/Obsidian-Vanguard, its rooms, grounds, circulation, staff, security, architecture, capacities, or physical logistics matter.

### 09 — [Reserved / inspect current System Bible index]
If a numbered parent module exists at `09-*`, add it to this router before relying on it.

### 10 — Footwear, Accessories, Jewelry, and Beauty
Path: `system bible/10-footwear-accessories-jewelry-and-beauty.md`
LOAD WHEN shoes, handbags, jewelry, watches, accessories, cosmetics, skincare, hair/beauty products, routines, styling objects, or their physical specifications matter. Culture modules own cultural meaning; module 10 owns item specification.

### 11 — [Reserved / inspect current System Bible index]
If a numbered parent module exists at `11-*`, add it explicitly.

### 12 — Fashion Empire and Commercial Fashion
Path: `system bible/12-fashion-empire-and-commercial-fashion.md`
LOAD WHEN Fashion Empire businesses, brands, holdings, collections, manufacturing, commercial fashion, fashion technology, beauty systems, Danielle Reyes, or listed companies/entities matter.

### 13–15 — [Reserved / inspect current System Bible index]
Any existing numbered parent modules in this range must be added explicitly.

### 16 — Biotech, Prosthetics, and Advanced Technology
Path: `system bible/16-biotech-prosthetics-and-advanced-technology.md`
LOAD WHEN biotech, prosthetics, advanced medical/assistive technology, body technology, implants, advanced devices, or related speculative engineering materially affects a scene or continuity.

### 17 — [Reserved / inspect current System Bible index]
Any existing numbered parent module must be added explicitly.

### 18 — Historical Recovery and Story Evidence
Path: `system bible/18-historical-recovery-and-story-evidence.md`
LOAD WHEN recovering canon from old drafts, exports, archives, duplicate files, historical versions, obsolete folders, prior AI outputs, or contradictory snapshots; or deciding whether older material is evidence, superseded, lost from later consolidation, or eligible for promotion. For corpus-wide/source-audit work, also load the mandatory recovery protocol above and start from `Systemwide/Audit/`.

## Developed-skill routing families preserved in repository

The repository currently preserves developed skill families including `age-culture`, `change-worldbuilding-toolkit`, `fashion-empire`, `gender-presentation-culture`, `obsidian-vanguard-estate`, `polyamory-family`, `sapphic-culture`, and `wealth-management`.

Their `SKILL.md` descriptions are unaudited recovery evidence only. They may help a recovery audit discover material that needs reconciliation, but they must not be loaded as operational guidance for story work and are never a substitute for the controlling harmonized System Bible.

### Age Culture routing supplement
LOAD WHEN a character's generation/age cohort materially shapes speech, references, technology relationship, institutional expectations, or generational misunderstanding.

### Gender Presentation Culture routing supplement
LOAD WHEN transgender, nonbinary, or gender-nonconforming presentation/transition/community culture; passing/being-read-as; presentation methods; learned presentation competency; or gendered interpretation of appearance materially matters. Pair with Sapphic Culture when appropriate.

### Wealth Management routing supplement
LOAD WHEN an ultra-wealthy anchor character's actual financial/legal structure matters: trusts, holding companies, family office, partner-protection structures, or corporate-empire scaffolding.

## Cross-trigger examples

These are routing examples, not story canon.

- A trans woman enters a lesbian bar in St. Claire and meets a closed polycule: load 06 + gender-presentation detail + 07 + 03, plus story-local records.
- A member of a closed polycule begins flirting with/dating someone outside it: load 03 before deciding whether action is allowed, a violation, or requires discussion.
- A sapphic character wears a violet pendant: load 06 for cultural meaning and 10 for physical specification if needed.
- Characters move into the Estate after becoming extremely wealthy through the Fashion Empire: load 08 + Wealth Management + 12, plus 01 if relationship/property power is implicated.
- A transformed adult reclaims an age-associated experience: load 04 + age-culture/life-stage + 01, plus implicated setting/culture modules.
- Jim asks whether a presentation guideline existed somewhere in hundreds of historical source documents and archived chats: load the recovery protocol first, then `Systemwide/Audit/`, then 18 Historical Recovery, then relevant subject modules. Do not begin with a handful of semantic searches and call that archive coverage.

## Router maintenance rule

Whenever a reusable System Bible parent module, developed skill family, or governing recovery infrastructure is added, renamed, consolidated, or materially changes scope, update this router in the same work session. More generally, persisted material that must govern or inform future work must remain discoverable through an appropriate maintained retrieval path from the project's normal entry points. A module, catalog, detail, rule, event, character record, story-state fact, or other governing material that exists but cannot be discovered through that path is operationally broken. Do not solve this by putting every detail directly in the router; maintain the appropriate parent/index/cross-reference chain.
