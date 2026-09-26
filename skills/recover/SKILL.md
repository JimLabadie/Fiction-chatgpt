# Recover

Status: PROTOTYPE — NON-GOVERNING
Purpose: Reconstruct prior project material from surviving evidence without silently inventing, promoting, deleting, or canonizing it.

## Use when

Use this skill when the task is to recover prior intent or detail; determine whether information exists or existed; compare historical versions; investigate consolidation loss; establish provenance; audit source coverage; or distinguish recovered material from reconstruction.

Do not use recovery as a substitute for ordinary current-canon retrieval.

## Governing contract

This skill executes recovery procedure. It does not own canon authority.

Always obey current project governance, especially:
- authority/status rules;
- namespace isolation;
- archive-recovery/source-audit rules;
- Jim's current explicit instructions.

Historical evidence remains evidence until governing authority and Jim's decisions establish otherwise.

## Inputs

- recovery target or question;
- requested corpus classes, if specified;
- current authoritative destinations relevant to the target;
- existing recovery/audit catalogs and progress records;
- accessible evidence sources.

## Procedure

1. **Resolve scope.**
   State internally what is being recovered and which corpus classes the request includes. Do not silently substitute one corpus class for another.

2. **Load recovery infrastructure first.**
   Retrieve the maintained recovery protocol and existing Audit catalog/coverage register before ad hoc searching. Reuse existing inventories instead of creating competing catalogs.

3. **Establish accessible evidence universe.**
   Determine which requested sources are searchable now. Treat inaccessible, incomplete, unindexed, or unsearched material as NOT SEARCHED / NOT SEARCHABLE, never as negative evidence.

4. **Inspect current destination state.**
   Retrieve the current controlling destination(s) and relevant recovery metadata. Current canon and historical recovery value are separate questions.

5. **Search systematically.**
   Use the existing inventory as the checklist. Search semantic variants, historical names, aliases, distinctive examples, and source families. Search results identify candidate evidence; inspect relevant sources in context.

6. **Process incrementally.**
   For large corpora, work in bounded source/page/section units. Persist coverage/progress rather than pretending the corpus was consumed atomically.

7. **Extract holdings at claim level.**
   Preserve source identifier/location, the actual claim/rule/fact/correction/decision/question, implicated entities/modules, evidenced status, relationships/conflicts, and processing state. Do not turn summaries into source claims.

8. **Compare versions without filename authority.**
   Do not infer authority from newest-looking names, timestamps, polish, folder placement, "final", "(2)", "(3)", or apparent consolidation. Compare contents and provenance.

9. **Classify findings using hard provenance categories.**
   - SOURCE
   - INFERENCE
   - CONFLICT
   - GAP
   - NOT FOUND IN SEARCHED CORPUS
   - NOT SEARCHED / NOT SEARCHABLE
   - RECONSTRUCTION / NEW MATERIAL

10. **Detect metadata disagreement.**
    Recovery ledgers, coverage registers, audits, and later reconciliation records are themselves evidence about processing state. If they disagree about whether material was incorporated, reviewed, superseded, or complete, report the disagreement and inspect the claimed destination before choosing a conclusion. Confidence or apparent recency alone does not resolve it.

11. **Apply authority only after recovery.**
    Finding historical material does not make it current canon. Use governing authority/status rules to identify what is already resolved and what remains genuinely conflicting or unclear.

12. **Do not dispose of evidence.**
    Duplicate, variant, obsolete, superseded-looking, low-authority, or apparently redundant material remains preserved unless Jim has expressly decided its disposition.

13. **Recovery before reconstruction.**
    Leave gaps visible. Only after the requested accessible corpus has been systematically exhausted may reconstruction/new material be proposed, and it must remain explicitly separate until accepted.

14. **Produce a coverage receipt.**
    Report what was actually searched/processed, what was not, the strength of the conclusion, conflicts/gaps, and any next recovery unit.

15. **Hand off; do not overreach.**
    Send unresolved claim conflicts to reconciliation. Send accepted state changes to persistence. Do not silently edit canon merely because recovery found something.

## Output contract

A recovery result must distinguish:
- recovered SOURCE findings;
- INFERENCES;
- CONFLICTS;
- GAPS / NOT FOUND;
- unsearched or inaccessible corpus;
- current-authority implications;
- coverage receipt;
- recommended next recovery unit when work remains.

Never say "the archive proves", "not found", "complete", "incorporated", "saved", or equivalent more strongly than actual coverage and verification support.

## Cold-test invariant

When two maintained recovery records disagree about a component's completion or incorporation state, this skill must surface the conflict and inspect the substantive destination. It must not select one ledger merely because it is later, more detailed, or more confident.
