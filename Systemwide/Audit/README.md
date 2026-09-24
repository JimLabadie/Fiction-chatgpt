# Repository Audit

Status: INVENTORY COMPLETE FOR BASELINE; SEMANTIC AND CLAIM AUDIT IN PROGRESS
Authority: RECOVERY METADATA; NOT CANON
Baseline: `main` at `230742369a0ef0d441cfa9edf7bc31b44e966adc`

The machine-readable baseline is also recorded in [`repository-baseline.txt`](repository-baseline.txt).

## Purpose

This directory records what is actually present in the repository before anyone decides what it means, which version controls, or where it belongs. It exists to prevent four recurring errors:

1. treating the most visible Estate or St. Claire material as the whole project;
2. treating a filename such as `final`, `copy`, `old`, or `(3)` as authority;
3. treating routing to a future destination as completed reconstruction; and
4. treating an unread source as absent, unimportant, optional, story-only, or non-canon.

The inventory is deliberately evidence-first. Mechanical matches are review leads, not canon decisions.

## Baseline facts

| Measure | Count |
|---|---:|
| Tracked project paths, excluding this audit directory | 440 |
| Distinct Git blobs represented by those paths | 401 |
| Preserved-source paths under `Systemwide/Source` | 402 |
| Distinct preserved-source blobs | 363 |
| Original-document paths | 330 |
| Obsolete-document paths | 34 |
| Readable conversions | 11 |
| Conversation pages | 26 |
| Existing curated System Bible files | 38 |
| Byte-identical groups across the preserved sources | 33 |
| Redundant paths in those byte-identical groups | 39 |
| Normalized extracted-text match groups | 47 |
| Mechanical filename/version-family candidates | 52 |
| `.skill` packages | 16 |
| Other ZIP wrappers | 1 |
| Members indexed inside those packages/wrappers | 101 |

### Preserved source formats

| Format | Paths |
|---|---:|
| DOCX | 222 |
| Markdown | 114 |
| JSON | 26 |
| SKILL | 16 |
| XLSX | 11 |
| CSV | 6 |
| OLD | 3 |
| PDF | 1 |
| TXT | 1 |
| ZIP | 1 |
| Extensionless HTML capture | 1 |

The extensionless file `jAc7Xsfo7zr8wVqE1EWVc` is a saved Microsoft Copilot share-page shell. It is provenance/link evidence, not the missing conversation content itself.

## Conversation archive

The 26 JSON pages are one thread:

- title: `Persist Story Bibles`;
- thread ID: `6aa207ac-f5a8-83ea-92f5-3d0213b36a43`;
- order: newest first;
- turns: 254 unique turns;
- messages: 254 user messages and 254 assistant messages;
- extracted word counts: 9,220 user words and 129,018 assistant words.

The imbalance is one reason claim-level authority parsing matters. Assistant volume is not acceptance. Jim's requests, corrections, acceptances, rejections, and unresolved replies must be distinguished from assistant proposals.

## Generated evidence tables

- [`repository-file-inventory.tsv`](repository-file-inventory.tsv) contains one row for every baseline path with zone, format, size, Git blob SHA, SHA-256, exact-duplicate group, container metadata, and a filename-family lead.
- [`exact-duplicate-groups.tsv`](exact-duplicate-groups.tsv) records byte-identical Git objects. Exact duplication proves identical bytes, not authority.
- [`normalized-text-match-groups.tsv`](normalized-text-match-groups.tsv) detects files whose machine-readable text matches after Unicode and whitespace normalization even when container bytes differ. A match still does not decide authority.
- [`filename-family-candidates.tsv`](filename-family-candidates.tsv) groups mechanically similar names for comparison. It explicitly does not assert equivalence or chronology.
- [`package-member-inventory.tsv`](package-member-inventory.tsv) opens every `.skill` and ZIP wrapper and records each internal path, size, compressed size, and content hash.
- [`component-coverage-register.md`](component-coverage-register.md) maps the substantive source families now visible to their current destinations and recovery state.
- [`build_repository_catalog.py`](build_repository_catalog.py) reproduces the machine inventory. It excludes this audit directory to avoid a self-hashing catalog loop.

## Extraction result and limit

Machine-readable text was extracted from every one of the 402 preserved-source paths. This is an inventory success, not a semantic-completion claim. It does not establish that every paragraph, spreadsheet row, image, assistant proposal, user correction, version delta, or attachment relationship has been reviewed and routed.

Extracted source excerpts and per-file content-derived labels or counts are intentionally not reproduced in the inventory. The catalog records structural metadata and hashes without concentrating personal or sensitive source text into a second artifact.

No source is treated as claim-reviewed merely because it appears in the catalog. That status changes only after a real content and authority review.

## Immediate version findings

- The three Fashion Empire skill packages are not interchangeable. The `(2)` package has 20 members; `(3)` and the unnumbered package have 23. Several shared members differ, and the unnumbered package contains a different `metis-werks.md` from `(3)` despite otherwise extensive overlap.
- The three Estate skill packages share the same skill instructions and staffing plan, but `(2)` contains a different, shorter estate master plan. The unnumbered and `(3)` master plans match internally even though the ZIP blobs differ.
- The three Wealth Management packages have matching extracted contents. `(2)` and `(3)` are byte-identical; the unnumbered ZIP differs at the container level while its two internal files match.
- The Change Worldbuilding Toolkit package contains eleven substantive files, including identity/memory continuity, social/legal response, physiological/sensory adaptation, digital-life mechanics, perceived-gender mechanics, a mental-trait taxonomy, and a lived-competency bank. Loose surrounding files preserve additional revisions.
- The St. Claire family contains original, obsolete, copied, converted, PDF, DOCX, and Markdown branches with both exact duplicates and materially different versions. Folder placement alone cannot select the controlling state.
- `z-calendar - girl1.zip` is a wrapper around `girl1.xlsx`; the workbook is now indexed and text-extracted rather than left invisible inside the ZIP.

## Completion boundary

The byte/container inventory is complete for the stated baseline. The semantic audit is not complete. A component becomes complete only after its assigned sources are claim-reviewed, version relationships are resolved or left explicitly open, substantive material reaches a real destination, and the published result is fetched back and verified.

## Conversation preservation enforcement audit

[2026-09-21 audit](conversation-preservation-enforcement-audit-2026-09-21.md) distinguishes repository conventions, executable tooling, native recording, lifecycle hooks, and verified trigger configuration. It records the inspected scope, remaining access limits, and a proposed minimal capture mechanism. The recommendation is not installed automation or new operating governance.

## Story lifecycle validation

[2026-09-24 lifecycle audit](story-lifecycle-audit-2026-09-24.md) traces GitHub issue #2 against the maintained lifecycle and records the exact structural pass/fail boundary. [`validate_story_lifecycle.py`](validate_story_lifecycle.py) now checks starter records, chapter directories, promoted-candidate cleanup, approval-register discoverability, and current-state presence. [`test_validate_story_lifecycle.py`](test_validate_story_lifecycle.py) contains isolated regression fixtures. These checks do not claim semantic completeness or automatic conversation capture.
