# St. Claire — Migration Provenance & Status Map

Status: MIGRATION WORKING RECORD — NOT CANON Purpose: preserve source authority, provenance, duplicate generations, and unresolved migration questions while moving St. Claire into Fiction Docs.

## Current authority finding

The live GitHub routing entry `system bible/07-st-claire.md` explicitly states that the maintained System Bible is the sole operating source of truth for St. Claire. Maintained canon/references belong under `system bible/07-st-claire/` and its parent module.

`system bible/developed-skills/St-Claire/`, historical compendia, Claude-era records, obsolete documents, and other source artifacts are recovery/evidence only. They must not override the maintained St. Claire tree. Recovery material becomes operating canon only after audit, reconciliation, deliberate promotion, and verification.

**Migration consequence:** GitBook must preserve this authority relationship during migration. No legacy or recovery source is promoted merely because it is newer, larger, more detailed, or duplicated in Drive.

## Source strata

### A. Governing maintained St. Claire — migrate as authority

* `system bible/07-st-claire.md` — active shared-world routing entry and authority declaration.
* `system bible/07-st-claire/amour-noir.md` — maintained establishment record.
* `system bible/07-st-claire/blush.md` — maintained establishment record.
* `system bible/07-st-claire/halloway-park.md` — maintained establishment record.
* `system bible/07-st-claire/hestia-principle.md` — maintained St. Claire principle record.
* `system bible/07-st-claire/my-exes-abandoned-stuff.md` — maintained establishment record.
* `system bible/07-st-claire/developed-reference/` — maintained detailed-reference layer, but individual records still retain provenance/status distinctions and must be migrated without flattening those distinctions.

### B. Maintained developed-reference set — preserve status and provenance

Current files observed:

* `St Claire 00 Concept.md`
* `St Claire 00B Rules and Mechanics.md`
* `St Claire 00C Working With Claude.md`
* `St Claire 00D History.md`
* `St Claire 01 Founding Pioneers.md`
* `St Claire 03 Population.md`
* `St Claire 04 Households.md`
* `St Claire 05 Organizations.md`
* `St Claire 06 Places.md`
* `St Claire 07 Occupations.md`
* `St Claire 08 Name Pools.md`
* `St Claire 99 MASTER TRACKER 1.md`
* `St Claire Master Lore Compendium v3.md`

The presence of a file in this maintained reference directory does not erase its internal status or provenance. In particular, the Master Lore Compendium and tracker must not be treated as blanket permission to promote every contained statement.

### C. Recovery / unaudited GitHub stratum — evidence, not canon

`system bible/developed-skills/St-Claire/` contains an older/parallel normalized and recovery generation, including Concept, Rules and Mechanics, History, Founding Pioneers, Population, Households, Organizations, Places, Occupations, Name Pools, Master Tracker, Master Lore Compendium, and later companion/audit files for population, staffing, household integration, organization recovery/expansion, and density completion.

The current St. Claire authority page explicitly marks this tree unaudited original/recovery source material. It is useful for detecting material that may not yet have been promoted, but it is not story-generation authority.

### D. Jim/Primary Google Drive legacy estate — preserve for provenance

Drive contains multiple generations and duplicates, including:

* current-looking normalized files such as `St Claire 00 Concept.md`, `St Claire 03 Population.md`, `St Claire 04 Households.md`, `St Claire 05 Organizations.md`, `St Claire 06 Places.md`, `St Claire 00D History.md`, and `St Claire 99 MASTER TRACKER 1.md`;
* earlier `(2)` generations and `old.` generations;
* `st. claireV2.docx`, `old.st. claire.docx`, `st. claire Markup.pdf`, `The District of St. Claire.docx`, `The District of St. Claire (2).docx`, and `The District of St. Claire — Master Lore Compendium.docx`;
* `St_Claire_Session_Salvage.docx`;
* `St Claire Master Lore Compendium v3.md` plus multiple same-size v3 copies and older v2 material.

Several Drive files match maintained GitHub filenames and sizes, strongly indicating exported/copied generations rather than independent authorities. They remain legacy evidence until content/hash comparison proves identity.

### E. Explicit obsolete/audit material

Repository audit records identify obsolete St. Claire documents and duplicate groups, including byte-identical Master Lore Compendium v3 copies. These are useful provenance evidence and should remain historical/recovery material, not migration authority.

## Duplicate and generation findings

1. `St Claire Master Lore Compendium v3.md` appears repeatedly across maintained developed-reference, recovery/developed-skills, obsolete source inventory, and Jim Drive. GitHub copies observed with blob SHA `bc7036a3f414af4f663bba0ec68aa38f8a6dfaed` and size 83,310 bytes indicate exact duplicate instances exist.
2. Jim Drive contains at least three v3 files of the same 83,310-byte size, plus v2 and DOCX compendium generations. Size alone is not sufficient to declare every Drive copy byte-identical; preserve until verified.
3. Normalized files such as Concept, Population, Households, Organizations, and Places exist in multiple Drive generations with materially different sizes. These are version families, not safe duplicates.
4. Some maintained developed-reference files have different blob SHAs/sizes from their recovery/developed-skills counterparts. They must not be collapsed merely because names match.

## Migration authority order

Until a specific conflict proves otherwise, use this migration order:

1. Current explicit author decisions and authority rules in the maintained System Bible.
2. Maintained `system bible/07-st-claire/` records.
3. Maintained `system bible/07-st-claire/developed-reference/` according to each record's internal status/provenance.
4. Recovery/developed-skills, Jim Drive generations, obsolete/source documents, audits, and historical exports as evidence for recovery/reconciliation only.
5. Chat memory/summaries only as navigation clues, never as a replacement for live source retrieval.

## Do-not-do list

* Do not bulk-copy the Jim Drive St. Claire folder into GitBook.
* Do not treat newest timestamp as authority.
* Do not treat largest/more detailed file as authority.
* Do not collapse same-named generations without comparison.
* Do not promote unprocessed Compendium material silently.
* Do not delete or move legacy files during archaeology.
* Do not rewrite canon to make conflicting generations agree.

## First bounded migration candidate

Create `Fiction Docs → Worlds → St. Claire` using the maintained authority/routing material first. Preserve its explicit authority language and legacy-snapshot status. Then migrate the maintained establishment records and developed-reference components incrementally, retaining status labels and provenance.

Before promoting the first bounded slice, compare the applicable maintained record against same-named recovery and Drive generations and record any material conflict. Identical/derived legacy copies remain evidence; compatible additions remain candidates; contradictions require author decision.

## Reconciliation findings — Rules & Mechanics and Hestia

### Resolved: presentation taxonomy conflict

The maintained `system bible/07-st-claire/developed-reference/St Claire 00B Rules and Mechanics.md` explicitly supersedes the recovery/developed-skills generation on presentation taxonomy.

The recovery copy retains the inherited ratio of approximately 48% femme / 30% androgynous / 21% butch / 1% other. The maintained record explicitly identifies that ratio and the Androgynous/Andro bucket as an unaudited Claude-era generation artifact, states that it must not be used, and establishes the approved shared-world categories as High Femme, Femme, Trans Femme, Trans High Femme, Trans Masc, and Butch.

Migration disposition: **resolved without author intervention.** The maintained six-category taxonomy is governing. Recovery presentation ratios remain provenance evidence only. Existing inherited Androgynous/Andro data is audit debt, with Femme as the default repair unless deliberate author-established evidence supports another approved category.

The maintained mechanics record also changes the validation method: new population work is checked against the approved taxonomy and genuinely established demographic rules, rather than manufacturing presentation percentages to satisfy the inherited quota.

### Confirmed: Hestia Principle status and protected incompleteness

The maintained `system bible/07-st-claire/hestia-principle.md` is explicitly **CONTROLLING ST. CLAIRE LORE COMPONENT** with status **ACCEPTED CULTURAL AND HISTORICAL BASELINE — ORIGIN DETAILS OPEN**.

Its governing core truth is that loving people protect the people they love, with protection defined as preserving enough safety and independence for genuine choice, refusal, departure, return, disagreement, or change. Housing, money, healthcare, employment, family recognition, and community belonging are not to become leverage.

Migration disposition: the principle itself and its core meaning are safe to migrate as governing St. Claire lore. Its historical origin, naming event/date, formal legal/customary status, named cases/figures/ceremonies, and the gap between ideal and imperfect practice are deliberately unresolved and must remain open rather than being recovered by inference.

### Consequence for the first migration slice

The St. Claire world landing page correctly carries the maintained presentation taxonomy and does not import the obsolete recovery ratio. The landing page was merged and published in Fiction Docs CR #9. Hestia was then migrated as its own maintained child component in Fiction Docs CR #10, preserving the protected unresolved origin details rather than inventing historical detail on the landing page.

## Open reconciliation queue

* Determine which maintained developed-reference files are direct promoted descendants of the recovery/developed-skills versions and which contain later author-approved changes.
* Compare the multiple Concept generations; sizes differ materially.
* Compare Population and Households generations before any bulk migration of people/households.
* Compare Organizations and Places generations before establishment migration beyond the already-maintained individual venue pages.
* Determine what material in the Master Tracker/Compendium remains explicitly unpromoted.
* Review `St_Claire_Session_Salvage.docx` and markup/source documents for unique recovery evidence after the governing maintained baseline is established.

## Current migration state

Archaeology/provenance mapping is active. The first Fiction Docs St. Claire landing-page slice was merged and published in Fiction Docs CR #9. The Hestia Principle child component was subsequently verified, merged, published, and read back in Fiction Docs CR #10. No legacy St. Claire source has been deleted or moved, and no recovery material has been silently promoted.
