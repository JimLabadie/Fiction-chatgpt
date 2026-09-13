# Source Recovery Inventory

Status: SUPERSEDED BASELINE SUMMARY — CURRENT MACHINE CATALOG AVAILABLE
Authority: RECOVERY METADATA; NOT CANON
Original baseline examined: `main` at `f8058a34291dbdbb8093e08d6be30285623edc26`
Current audited baseline: `main` at `230742369a0ef0d441cfa9edf7bc31b44e966adc`

The complete current inventory, duplicate tables, package-member catalog, mechanical version-family leads, and component coverage map now live in [`Systemwide/Audit`](../Audit/README.md). The figures below are retained as historical evidence of the earlier pass and must not be used as current repository totals.

This file records what is demonstrably present in the repository. It does not decide canon from filenames, repetition, file dates, or apparent polish.

## Earlier repository snapshot

- Tracked repository paths reported by the earlier pass: **418**
- Preserved source paths reported by the earlier pass: **401**
- Entries under `Original-Documents`: **330**
- Readable source conversions: **11**
- Conversation archive pages: **26**
- Current curated Markdown outputs under `system bible`: **17**
- Exact-duplicate groups found among original documents by Git blob SHA: **23**
- Redundant copies represented by those exact-duplicate groups: **27**

### Preserved source types

| Type | Count |
|---|---:|
| DOCX | 222 |
| Markdown | 113 |
| JSON | 26 |
| SKILL | 16 |
| XLSX | 11 |
| CSV | 6 |
| OLD | 3 |
| PDF | 1 |
| TXT | 1 |
| ZIP | 1 |
| No extension | 1 |

## Exact duplicates confirmed by content hash

These are byte-identical repository objects, not merely similar filenames. Every source path remains preserved.

- `change-toolkit perceived-gender-swap-mechanics 1.md`; `change-toolkit perceived-gender-swap-mechanics 2.md`; `change-toolkit perceived-gender-swap-mechanics.md`
- `create fictitious luxury penthouses near the atta.._(2).docx`; `create fictitious luxury penthouses near the atta.._(3).docx`; `create fictitious luxury penthouses near the atta.._.docx`
- `gender-presentation-culture 1.skill`; `gender-presentation-culture 2.skill`; `gender-presentation-culture.skill`
- `metis-collaboration-review (2).md`; `metis-collaboration-review (3).md`; `metis-collaboration-review.md`
- `24_clothes and body (2).xlsx`; `24_clothes and body.xlsx`
- `31_female life events (2).docx`; `31_female life events.docx`
- `34_Footwear_Registry (2).csv`; `34_Footwear_Registry.csv`
- `Create a list of 25 pop culture reference used by .._(1).docx`; `Create a list of 25 pop culture reference used by .._.docx`
- `Create a list of 25 pop culture reference used in .._(1).docx`; `Create a list of 25 pop culture reference used in .._.docx`
- `Lesbian jewelery constellation pettern(1).docx`; `Lesbian jewelery constellation pettern.docx`
- `Obsidian-vanguard-staffing-plan.md`; `claude report-obsidian-vanguard-staffing-plan.md`
- `barbies dreamhouses (2).docx`; `barbies dreamhouses.docx`
- `billionaire_Vacation_homes.csv`; `billionaire_unified_portfolio.csv`
- `cassandra_labs_draft (2).md`; `cassandra_labs_draft.md`
- `claude report-obsidian-vanguard-estate-master-plan (1).md`; `obsidian-vanguard-estate-master-plan.md`
- `claude report-obsidian-vanguard-wealth-management.md`; `obsidian-vanguard-wealth-management.md`
- `jim-story preserved-scenes (1).md`; `jim-story preserved-scenes.md`
- `metis-techne-buildout (2).md`; `metis-techne-buildout.md`
- `oam-selection-draft (2).md`; `oam-selection-draft.md`
- `techne-company-profile (2).md`; `techne-company-profile.md`
- `techne-floor23 (2).md`; `techne-floor23.md`
- `techne-full-building (2).md`; `techne-full-building.md`
- `wealth-management (2).skill`; `wealth-management (3).skill`

## Conversation recovery

`Systemwide/Source/conversations/page-001.json` through `page-026.json` are pages of the same ChatGPT thread:

- Thread title: **Persist Story Bibles**
- Thread ID: `6aa207ac-f5a8-83ea-92f5-3d0213b36a43`
- Page order: newest first
- Recovery status: preserved; decision extraction not complete

Jim confirmed that work in the original chat stopped after this export. The archive is therefore the historical handoff for that chat, while later repository-management chats are separate operational history.

## Classification rules

- Original source storage is a mixed preservation archive, not a canon directory.
- Exact duplicates remain preserved but count once for substantive review.
- Near-duplicates and apparent versions require field-level comparison.
- Story files do not enter the reusable output as stories or story-local state.
- A story file may contain reusable candidates, but those require independent support or Jim's decision before promotion.
- Reusable components may be related without belonging to one monolithic setting.
- Inclusion in one file does not prove that two components are inseparable.
- Assistant-generated proposals, brainstorming, examples, and explicit non-canon material are not promoted silently.
- No module is complete until its assigned sources, duplicates, variants, conflicts, and destinations are accounted for and the published result is fetched and verified.

## Current recovery warning

The existing curated outputs are not uniformly at the same confidence level. Module 01 has a bounded 17-source coverage ledger. Other top-level modules do not yet have equivalent repository-wide source accounting and must not be treated as complete merely because a Markdown file exists.

The Estate module is the first confirmed example: the archived conversation records known propagation gaps and competing space/naming models that are not honestly represented by its current `RECONSTRUCTED PROPERTY CANON` label.

## Next inventory work

1. Build subject clusters from all 330 original-document entries.
2. Identify near-duplicate and version families within each cluster.
3. Separate story-only files from reusable-component evidence.
4. Record required, optional, historical, and uncertain relationships among reusable components.
5. Select a bounded module, enumerate all assigned sources, reconcile claims, and publish a verified increment.
