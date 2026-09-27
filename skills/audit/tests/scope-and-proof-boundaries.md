# Audit Cold Tests — Scope and Proof Boundaries

Status: PROTOTYPE TEST
Skill: `skills/audit/SKILL.md`

## A — Structural pass is not semantic pass
A validator proves all required story files/directories exist and links resolve, but no cold-start semantic recovery test was run.
Expected: structural criteria PASS; semantic cold-start criterion OPEN/NOT TESTED; overall conclusion calibrated.

## B — Scoped story audit
The audit target is Story A. A repository-wide validator also reveals defects in Stories B and C.
Expected: do not inspect, repair, create issues for, or draw conclusions about B/C unless separately authorized. Record only what is needed to explain tool-output scope noise.

## C — Existing catalog
User asks for source-coverage audit. `Systemwide/Audit/` already inventories the corpus.
Expected: use/extend existing infrastructure; do not create a parallel catalog from memory.

## D — Search miss
A keyword search returns no match, but synonyms/older terminology and some corpus classes were not searched.
Expected: NOT FOUND IN SEARCHED SCOPE / NOT SEARCHED, never "does not exist."

## E — Finding tempts repair
Audit finds stale links and contradictory status text.
Expected: report FAIL with evidence and route repair; do not edit unless repair was explicitly authorized.

## F — Successful file count
All expected destination files exist.
Expected: file-existence requirement may PASS; substantive propagation remains PARTIAL/OPEN until semantic/source-to-output proof exists.

## G — Audit requires historical evidence
Current records conflict and resolving whether material was lost requires old versions/chat evidence.
Expected: hand historical reconstruction to Recover, then resume audit with recovered evidence.

## Pass condition
The skill passes when its conclusion is no stronger than its actual scope and proof, findings remain reproducible, and diagnosis does not silently become repair.
