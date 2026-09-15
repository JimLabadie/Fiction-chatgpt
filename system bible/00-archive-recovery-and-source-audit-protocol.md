# Mandatory Archive Recovery and Source Audit Protocol

Status: GOVERNING WORKFLOW RULE

## Purpose

This protocol governs archive recovery, source audits, provenance checks, corpus consolidation, and any request whose purpose is to determine whether information exists, existed previously, was lost during consolidation, conflicts across versions, or is adequately represented in current canon/reference material.

It exists to prevent dangerous failure modes: a partial search being reported as an archive-wide conclusion; missing source material being silently replaced by model inference, general knowledge, or newly invented material; apparently obsolete or duplicate material being discarded before its unique holdings are known; and existing recovery infrastructure being forgotten and recreated instead of used.

A source gap must remain visible until it is either recovered from evidence or explicitly reconstructed/created by Jim.

## Mandatory recovery entry point

Before beginning any archive-recovery, source-audit, historical-source, corpus-coverage, duplicate/version, lost-material, catalog, or consolidation investigation, retrieve and inspect the existing recovery infrastructure:

- `Systemwide/Audit/README.md`
- `Systemwide/Audit/component-coverage-register.md`
- relevant generated tables under `Systemwide/Audit/`, including `repository-file-inventory.tsv`, `exact-duplicate-groups.tsv`, `normalized-text-match-groups.tsv`, `filename-family-candidates.tsv`, and `package-member-inventory.tsv` when applicable.

`Systemwide/Audit/` is the structural catalog and baseline for recovery work. Do not create a competing catalog merely because the existing one was not remembered or surfaced automatically.

The Audit directory's own completion boundary controls how its data may be described: structural inventory or machine-readable extraction coverage is not semantic review, claim review, authority resolution, or operational consolidation.

**Information that exists but is not routed into the task is functionally unavailable. Recovery work must therefore begin from the existing Audit catalog, not from model memory or ad hoc source discovery.**

## Core corpus principles

### The entire corpus is the scope, not the execution unit

The recovery/consolidation project must treat the entire surviving corpus as the ultimate unit of coverage. No single topic, example, module, character, spreadsheet, or source family should silently replace that corpus-wide objective.

However, the entire corpus must not be treated as one simultaneous comprehension task. Hundreds of documents, very large documents, and long chat archives exceed practical working context and create exactly the compression/loss problem recovery is intended to solve.

Therefore:

**Corpus-wide coverage must be achieved through incremental, persistent processing.**

The execution unit should be a source document, chat, bounded document section, page range, spreadsheet region, or other manageable chunk. Large sources must be processed in durable checkpoints rather than summarized as though they were consumed atomically.

### Preserve evidence before judging it

Jim's archive was accumulated partly under persistence/survival pressure. It contains iterative drafts, incomplete documents, emergency exports, duplicates, parallel versions, partial consolidations, scraps, and repeated "final" versions because preservation often mattered more than clean version control.

Therefore ordinary cleanup assumptions are unsafe.

Do not infer from filename, timestamp, polish, completeness, apparent version order, or consolidation status that a source is disposable, superseded in all respects, or less valuable as recovery evidence.

A later document may be less complete. An incomplete draft may contain unique detail. A cleaner consolidation may have compressed away operational information. Two apparent duplicates may preserve different holdings. A superseded document may have no current authority while retaining high recovery value.

**During recovery, preservation precedes cleanup.**

## Trigger conditions

Enter Archive Recovery / Source Audit Mode when Jim asks to check/search/look through the archive or chats/source documents; recover prior intent or detail; determine provenance, completeness, conflicts, or losses; or inventory, catalog, consolidate, deduplicate, or decide what historical material should be retained.

When the request names multiple corpus classes, all named corpus classes are part of the requested search. Do not silently treat one class as representative of another.

## 1. Define the corpus before drawing conclusions

Start from `Systemwide/Audit/` to identify the available evidence universe relevant to the request. Depending on the project, this may include archived chats/conversation exports, original/source documents, current System Bible modules, detailed-reference files, developed skills and `SKILL.md` files, historical/recovery folders, story-specific bibles and continuity files, accepted prose, spreadsheets/inventories/exports/bundles, and repository history.

Determine which requested corpus classes are actually accessible/searchable in the current environment. If a requested corpus is inaccessible, incomplete, unindexed, or otherwise cannot be searched, state that explicitly. Never convert inaccessible evidence into negative evidence.

## 2. Exhaustive scope means systematic coverage, not sampling

When Jim asks to check the archive or source corpus, the task is exhaustive within the accessible requested corpus. Do not stop because a few plausible hits were found, current files appear sufficient, a query returned no immediate results, a cleaner file appears authoritative, or enough evidence exists to construct a plausible replacement.

Where the corpus can be enumerated, establish the count from the Audit baseline and track actual coverage. If technical limits require batches, continue in batches. Do not downgrade the request to sampling without saying so.

## 3. Use the existing catalog; do not recreate it

The structural catalog already lives under `Systemwide/Audit/`. It is the inventory/progress-control layer, not a summary of what the project "really means."

Before adding new catalog artifacts, verify whether the Audit directory already provides the needed structure. Extend the existing recovery system rather than creating parallel inventories that can drift apart.

The first-pass structural catalog remains preservation-oriented: it establishes what exists and makes it trackable without prematurely deciding authority, redundancy, or destination.

## 4. Process sources incrementally into a holdings ledger

After inventory, process sources in manageable units. The purpose of extraction is to record what each source actually contains, not merely what topic its filename suggests.

A source may contain holdings relevant to many modules or stories. Preserve those cross-topic holdings rather than forcing the entire source into one category.

For each substantive holding, preserve source identifier, location within source where available, concise rule/fact/example/claim/correction/decision/unresolved idea, implicated subjects/modules/entities, provenance category, authority status only when evidenced, known relationships/conflicts, and processing state.

For very large documents, checkpoint by section/page range or another stable subdivision. Never mark the entire source processed when only part has been inspected.

The holdings ledger is the durable recovery layer beneath later consolidated modules. Consolidation may synthesize or compress; the ledger preserves where the underlying material came from.

## 5. Do not begin with topic whack-a-mole

Examples and discovered deficiencies are diagnostics, not automatic replacements for the corpus-wide objective.

If a question reveals that femme presentation, St. Claire, Athena, polycule rules, Fashion Empire holdings, transformation mechanics, or another area is underrepresented, record that deficiency. Do not silently abandon the corpus process to rebuild only the latest example unless Jim explicitly chooses to do so.

## 6. Search semantically, not only by current terminology

Historical material may use different names, labels, spellings, filenames, or conceptual language. Use multiple searches where necessary: current terminology, older terminology, synonyms, implicated entities, distinctive examples, and likely source-family names.

A failed keyword search is not sufficient evidence that the concept is absent.

## 7. Search results are discovery evidence; inspect relevant sources

Snippets, filenames, inventories, indexes, and search-result excerpts identify candidate evidence but do not automatically establish full meaning.

Open and inspect promising hits in context. When versions exist, compare actual contents rather than assuming the newest-looking filename, timestamp, folder, or consolidation is authoritative.

Historical duplication and chaotic naming are expected recovery evidence, not noise to discard automatically.

## 8. Authority and recovery value are independent

Do not collapse "is this current canon?" and "is this valuable evidence?" into one judgment.

A source can have low or zero current authority while preserving unique high-value recovery evidence. A current authoritative module can be incomplete as an archival representation of earlier detailed material.

Where useful, track source status, authority, recovery value, and evidenced relationships separately. Unknown is preferable to an unsupported assumption.

## 9. No premature KEEP / DELETE judgment

Do not decide that a historical source can be deleted merely because it appears old, incomplete, duplicated, superseded, or incorporated elsewhere.

A source becomes a candidate for true redundancy only after its substantive holdings have been extracted and compared sufficiently to determine that it contributes no unique recovery value that needs preservation.

Cleanup is later than inventory and extraction.

## 10. Hard provenance categories

During recovery/audit work, keep these categories separate:

### SOURCE
Directly stated or clearly established by retrieved evidence.

### INFERENCE
Reasonably derived from retrieved evidence but not itself stated there. Identify it explicitly.

### CONFLICT
Relevant sources materially disagree or authority/provenance cannot yet resolve which governs.

### GAP
The searched evidence does not supply enough information. A gap is not permission to invent.

### NOT FOUND IN SEARCHED CORPUS
Not found after the stated accessible corpus was systematically searched. This does not mean it never existed elsewhere.

### NOT SEARCHED / NOT SEARCHABLE
A corpus or portion was not searched or could not be searched. It cannot be evidence of absence.

### RECONSTRUCTION / NEW MATERIAL
Material deliberately created after recovery fails or proves incomplete. It is not recovered source material and does not become canon merely because proposed.

## 11. No silent gap filling during audits

Do not silently bridge missing information using general model knowledge, real-world or genre conventions, assumptions about Jim's intent, extrapolation from adjacent canon, newly invented examples, or cleaner formulations.

If a source says only `femme — nails, makeup, "girly" clothes`, do not expand that into a detailed aesthetic and describe the expansion as what the source establishes.

First mark the gap. Any interpretation/reconstruction must be clearly separated from recovered evidence.

## 12. Never make synthesis sound like source text

Language describing source contents must be traceable to retrieved evidence. The reader must be able to tell where recovered material ends and model reasoning begins.

## 13. Coverage receipts and persistent progress are mandatory

Every archive-wide recovery or source-audit conclusion must include a coverage receipt showing what was actually searched or processed.

Where counts are available, use the Audit baseline rather than guessing. Structural inventory or machine-extracted text does not mean semantic or claim review.

For incremental corpus processing, persist progress in the Audit/ledger rather than relying on conversational memory. A future session must be able to determine what has and has not been processed without rediscovering the recovery infrastructure.

## 14. Calibrate conclusions to coverage

Use conclusions no stronger than the evidence allows. Partial search means `not found in the subset searched`; complete accessible search can support `not found in the searched accessible corpus`; conflicts remain conflicts; inaccessible material remains explicit.

Never convert `not found` into `does not exist` without evidence that warrants it.

## 15. Authority and recovery are separate questions

Finding historical material does not automatically make it current canon. First establish what the evidence says, then apply the project's authority hierarchy.

Do not erase historical evidence merely because a later consolidation omitted it. Omission may itself be evidence of consolidation loss.

## 16. Recovery before reconstruction

When recovering lost intent/detail:

1. Retrieve the existing Audit baseline and coverage register.
2. Search/process the accessible requested corpus systematically using that inventory as the checklist.
3. Identify direct evidence, partial evidence, conflicts, and gaps.
4. Report coverage and provenance.
5. Only after recovery is exhausted consider reconstruction.
6. Keep reconstruction explicitly separate until Jim accepts it.

Plausibility is not evidence that an answer was ever part of the project.

## 17. Corpus workflow and definition of done

Default pipeline:

**Existing corpus inventory (`Systemwide/Audit/`) → incremental source extraction → holdings/claim ledger → consolidation → operational modules → coverage audit → later redundancy/cleanup review.**

Track independently:

### Archive coverage
Has every accessible source been inventoried and processed to the required semantic degree?

### Operational coverage
Has every extracted substantive holding been incorporated appropriately, deliberately retained as historical evidence, identified as duplicate/superseded with evidence, or flagged unresolved/conflicting?

Do not declare consolidation complete merely because current modules look coherent.

## 18. Relationship to other governing protocols

For story drafting, `00-module-router.md` and `00-mandatory-source-grounded-drafting.md` remain mandatory.

This protocol governs what the archive contains, historical intent, source sufficiency, incremental recovery, and loss detection.

The module router should route recovery/audit tasks here; this protocol then routes those tasks to `Systemwide/Audit/` before raw-source investigation.

## Governing principles

**The entire corpus is the scope, not the execution unit.**

**Corpus-wide coverage must be incremental and persistent, not simultaneous.**

**Preserve evidence before judging authority or redundancy.**

**Searching is not sampling. Inference is not source. Plausibility is not provenance.**

**A gap must remain visible until evidence or Jim fills it.**

**A catalog that cannot be discovered when needed is operationally broken.**
