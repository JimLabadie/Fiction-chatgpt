# Mandatory Archive Recovery and Source Audit Protocol

Status: GOVERNING WORKFLOW RULE

## Purpose

This protocol governs archive recovery, source audits, provenance checks, corpus consolidation, and any request whose purpose is to determine whether information exists, existed previously, was lost during consolidation, conflicts across versions, or is adequately represented in current canon/reference material.

It exists to prevent dangerous failure modes: a partial search being reported as an archive-wide conclusion; missing source material being silently replaced by model inference, general knowledge, or newly invented material; and apparently obsolete or duplicate material being discarded before its unique holdings are known.

A source gap must remain visible until it is either recovered from evidence or explicitly reconstructed/created by Jim.

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

Enter Archive Recovery / Source Audit Mode when Jim asks to do things such as:

- check/search/look through the archive;
- check/search the chats, conversations, source documents, original documents, historical files, developed skills, or recovery material;
- determine whether something existed before;
- recover the original version, intent, rule, aesthetic, fact, relationship, history, mechanic, or wording;
- determine whether current source material is complete or sufficient;
- compare current material with historical material;
- find where a detail came from;
- determine whether a detail is source-derived or invented;
- investigate an apparent loss caused by consolidation, migration, harmonization, summarization, or rewriting;
- inventory, catalog, consolidate, deduplicate, or decide what historical material should be retained.

When the request names multiple corpus classes, all named corpus classes are part of the requested search. Do not silently treat one class as representative of another.

## 1. Define the corpus before drawing conclusions

Identify the available evidence universe relevant to the request. Depending on the project, this may include:

- archived chats/conversation exports;
- original/source documents;
- current System Bible modules;
- detailed-reference files;
- developed skills and their `SKILL.md` files;
- historical/recovery folders;
- story-specific bibles and continuity files;
- accepted/approved prose;
- spreadsheets, inventories, exports, bundles, and other retained artifacts;
- repository history or older versions where available.

Determine which requested corpus classes are actually accessible/searchable in the current environment.

If a requested corpus is inaccessible, incomplete, unindexed, or otherwise cannot be searched, state that explicitly. Never convert inaccessible evidence into negative evidence.

## 2. Exhaustive scope means systematic coverage, not sampling

When Jim asks to "check the archive," "look through the chats and source documents," or otherwise requests archive-wide recovery, the task is exhaustive within the accessible corpus.

Do not stop because:

- a few plausible hits were found;
- current files appear to answer the question;
- a search query returned no immediate results;
- a later-looking or cleaner file appears authoritative;
- the likely answer seems obvious;
- enough evidence exists to construct a plausible replacement.

Search every accessible requested corpus class. Where the corpus can be enumerated, establish the count and track coverage. If there are 26 accessible archived chats, an archive-wide chat search is not complete until all 26 have been searched or inspected to the degree necessary for the question. If hundreds of source documents are available, do not describe a subset search as a search of "the source documents."

If technical limits prevent exhaustive inspection in one operation, continue in batches. Do not downgrade the request to sampling without saying so.

## 3. Build a persistent corpus catalog before aggressive consolidation

Before trying to decide globally what to keep, delete, merge, or rewrite, create and maintain a catalog of the surviving corpus.

The catalog is an inventory and progress-control layer, not a summary of what the project "really means."

For each source, record as available:

- stable source identifier/path;
- filename/title;
- source type (document, chat, spreadsheet, skill, module, export, etc.);
- size/page/row/message information where available;
- apparent date/version metadata without treating it as authoritative;
- processing status;
- source status if evidenced: draft, iterative, consolidated, current, historical, export, unknown;
- known relationships to other sources: predecessor, successor, apparent duplicate, partial overlap, consolidation, divergent branch, unknown;
- notes about accessibility or extraction limitations.

Do not require full interpretation of a source merely to catalog its existence.

The first catalog pass is preservation-oriented: establish what exists and make it trackable.

## 4. Process sources incrementally into a holdings ledger

After inventory, process sources in manageable units. The purpose of extraction is to record **what each source actually contains**, not merely what topic the filename suggests it contains.

A source may contain holdings relevant to many different modules or stories. Preserve those cross-topic holdings rather than forcing the entire source into one category.

For each substantive holding, record enough information to preserve provenance, including:

- source identifier;
- location within source (section/page/row/message/range where available);
- concise description or extracted rule/fact/example;
- implicated subjects/modules/entities;
- whether the holding is direct source content or an explicit inference;
- relationship to known parallel holdings if established;
- authority status only when supported by evidence;
- unresolved conflicts/questions.

For very large documents, checkpoint by section/page range or another stable subdivision. Never mark the entire source processed when only part has been inspected.

The holdings ledger is the durable recovery layer beneath later consolidated modules. Consolidation may synthesize or compress; the ledger preserves where the underlying material came from.

## 5. Do not begin with topic whack-a-mole

Examples and discovered deficiencies are diagnostics, not automatic replacements for the corpus-wide objective.

If a question reveals that femme presentation, St. Claire, Athena, polycule rules, Fashion Empire holdings, transformation mechanics, or another area is underrepresented, record that deficiency. Do not silently abandon the corpus process to rebuild only the latest example unless Jim explicitly chooses to do so.

The catalog and holdings process must continue to provide systematic corpus-wide coverage.

## 6. Search semantically, not only by current terminology

Historical material may use different names, labels, spellings, filenames, or conceptual language.

Use multiple searches where necessary, including:

- current terminology;
- older known terminology;
- synonyms and closely related concepts;
- names of implicated characters, places, organizations, systems, or aesthetics;
- distinctive examples or phrases remembered from later material;
- likely filenames/source-family names.

A failed keyword search is not sufficient evidence that the concept is absent.

## 7. Search results are discovery evidence; inspect relevant sources

Snippets, filenames, inventories, indexes, and search-result excerpts may identify candidate evidence but do not automatically establish its full meaning.

Open and inspect promising hits in context before relying on them for substantive conclusions. When different versions exist, compare their actual contents rather than assuming the newest-looking filename, timestamp, or consolidation is authoritative.

Historical duplication, inconsistent versioning, repeated `final` filenames, emergency exports, and partial consolidations are expected features of this archive. Treat them as recovery evidence, not noise to be discarded automatically.

## 8. Authority and recovery value are independent

Do not collapse "is this current canon?" and "is this valuable evidence?" into one judgment.

A source can have low or zero current authority while preserving unique high-value recovery evidence. A current authoritative module can be incomplete as an archival representation of earlier detailed material.

Where useful, track separately:

- **Source status:** draft / iterative / consolidated / current / historical / recovered / export / unknown.
- **Authority:** governing / subordinate / superseded / non-canon / uncertain / not yet assessed.
- **Recovery value:** unique detail / duplicated detail / partial overlap / possible lost detail / provenance-only / not yet assessed.
- **Relationship:** predecessor / successor / apparent duplicate / consolidation / divergent branch / unknown.

These classifications must be evidence-based. Unknown is preferable to an unsupported assumption.

## 9. No premature KEEP / DELETE judgment

Do not decide that a historical source can be deleted merely because it appears old, incomplete, duplicated, superseded, or incorporated into another file.

A source becomes a candidate for true redundancy only after its substantive holdings have been extracted and compared sufficiently to determine that it contributes no unique recovery value that needs preservation.

Until then, retain it.

Cleanup is a later phase than inventory and extraction.

## 10. Hard provenance categories

During recovery/audit work, keep the following categories separate:

### SOURCE
Directly stated or clearly established by retrieved evidence.

### INFERENCE
A conclusion reasonably derived from retrieved evidence but not itself stated there. Identify it explicitly as inference.

### CONFLICT
Two or more relevant sources materially disagree, or authority/provenance cannot yet resolve which version governs. Report the conflict rather than silently selecting the convenient answer.

### GAP
The searched evidence does not supply enough information to answer the question. A gap is not permission to invent.

### NOT FOUND IN SEARCHED CORPUS
The information was not found after the stated accessible corpus was systematically searched. This does not mean it never existed outside that corpus.

### NOT SEARCHED / NOT SEARCHABLE
A corpus or portion of a corpus was not searched or could not be searched. It cannot be used as evidence of absence.

### RECONSTRUCTION / NEW MATERIAL
Material deliberately created after recovery fails or proves incomplete. It must be identified as reconstructed/new rather than recovered source material and does not become canon merely because it was proposed.

## 11. No silent gap filling during audits

During Archive Recovery / Source Audit Mode, do not silently bridge missing information using:

- general model knowledge;
- real-world conventions;
- genre conventions;
- assumptions about what Jim probably intended;
- extrapolation from adjacent canon;
- newly invented examples;
- a cleaner or more internally consistent formulation.

If the source says only `femme — nails, makeup, "girly" clothes`, do not expand that into a detailed aesthetic and then describe the expansion as what the source establishes.

If additional reasoning would be useful, first mark the source gap. Any proposed interpretation or reconstruction must then be clearly labeled separately from recovered evidence.

## 12. Never make synthesis sound like source text

Language describing source contents must be traceable to retrieved source evidence.

Do not say:

- "the guide establishes..."
- "the archive says..."
- "the source defines..."
- "the original intent was..."

unless the retrieved evidence supports that statement.

When appropriate, instead say:

- "the source explicitly states..."
- "the examples consistently suggest..." (INFERENCE)
- "I have not found a source that defines..." (GAP or NOT FOUND, depending on coverage)
- "I would propose..." (NEW MATERIAL)

The reader must be able to tell where Jim's recovered material ends and model reasoning begins.

## 13. Coverage receipts and persistent progress are mandatory

Every archive-wide recovery or source-audit conclusion must include a coverage receipt sufficient to show what was actually searched or processed.

Where counts are available, report them, for example:

`Coverage: archived chats 26/26; indexed source documents 347/347; developed skill families 8/8; current System Bible searched. Not searchable: 3 binary legacy artifacts.`

If exact counts cannot be established, name the corpus classes and state the limitation rather than inventing precision.

For incremental corpus processing, persist progress in the catalog/ledger rather than relying on conversational memory. A future session must be able to determine what has and has not been processed without rereading the entire archive.

A coverage receipt describes work actually completed. Never report intended, assumed, or partial coverage as completed coverage.

## 14. Calibrate conclusions to coverage

Use conclusions no stronger than the evidence allows.

- Partial search: `Not found in the subset searched.`
- Complete accessible search: `Not found in the searched accessible corpus.`
- Inaccessible material remains: explicitly identify it.
- Multiple versions disagree: `Conflicting versions found.`
- Evidence supports only part of remembered material: `Partial recovery.`
- Direct historical source recovered: `Recovered`, with provenance.

Never convert `not found` into `does not exist` unless the evidence genuinely warrants that claim.

## 15. Authority and recovery are separate questions

Finding historical material does not automatically make it current canon.

First determine what the historical evidence says. Then apply the project's authority hierarchy to determine whether it governs, conflicts, was superseded, or should be proposed for restoration.

Do not erase useful historical evidence merely because a later consolidation omitted it. Omission may itself be evidence of consolidation loss.

## 16. Recovery before reconstruction

When the purpose is to recover lost intent or detail:

1. Search/process the accessible requested corpus systematically.
2. Identify direct evidence, partial evidence, conflicts, and gaps.
3. Report coverage and provenance.
4. Only after recovery is exhausted should reconstruction be considered.
5. Reconstruction requires explicit separation from recovered material and does not become canon until Jim accepts it.

The model's ability to produce a plausible answer is not evidence that the answer was ever part of the project.

## 17. Corpus workflow and definition of done

The default corpus-recovery pipeline is:

**Corpus inventory → incremental source extraction → holdings ledger → consolidation → operational modules → coverage audit → later redundancy/cleanup review.**

Track two independent kinds of completeness:

### Archive coverage
Has every accessible source been inventoried and processed to the required degree?

### Operational coverage
Has every extracted substantive holding been incorporated into an appropriate operational module, deliberately retained as historical evidence, identified as duplicate/superseded with evidence, or flagged as unresolved/conflicting?

Do not declare the corpus consolidation complete merely because current modules look coherent. Completion requires both forms of coverage to be accounted for.

## 18. Relationship to other governing protocols

For story drafting, `00-module-router.md` and `00-mandatory-source-grounded-drafting.md` remain mandatory.

This protocol adds a different layer: it governs claims about what the archive contains, what was historically intended, whether source material is sufficient, how the corpus is incrementally recovered, and whether information has been lost.

When both modes apply, perform recovery/source audit first where unresolved provenance could materially affect drafting. Do not draft through an unresolved recovery question by substituting model invention.

## Governing principles

**The entire corpus is the scope, not the execution unit.**

**Corpus-wide coverage must be incremental and persistent, not simultaneous.**

**Preserve evidence before judging authority or redundancy.**

**Searching is not sampling. Inference is not source. Plausibility is not provenance.**

**A gap must remain visible until evidence or Jim fills it.**
