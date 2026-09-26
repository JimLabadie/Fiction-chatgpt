# Audit

Status: PROTOTYPE — NON-GOVERNING
Purpose: Test a defined project target against defined governing requirements and evidence, producing reproducible findings and coverage limits without silently repairing, promoting, deleting, or broadening scope.

## Use when
Use to determine whether a component, story lifecycle, repository structure, source family, workflow, persistence operation, continuity state, routing arrangement, or other bounded target satisfies stated requirements.

Audit asks: "Does the inspected target satisfy these requirements, and what evidence proves or disproves that?"

Recover asks: "What evidence or material existed or was lost?" If an audit requires historical reconstruction beyond the established evidence set, hand that portion to Recover.

## Required inputs
- exact audit question or requirement set;
- bounded target/scope and active namespace;
- baseline/ref/revision when repository state matters;
- governing rules/criteria;
- relevant authoritative records and existing audit infrastructure;
- required evidence classes;
- known access/search limits.

## Procedure
1. State the audit contract: target, requirements, baseline, namespace, evidence classes, and pass/partial/fail/open/not-applicable criteria.
2. Retrieve governing criteria first. Inspect live rules, schemas, validators, lifecycle requirements, authority/status rules, or other controlling criteria rather than remembered requirements.
3. Use existing audit infrastructure. For archive/source coverage begin with `Systemwide/Audit/` and maintained catalogs/registers rather than creating a competing inventory.
4. Establish the inspected universe. Enumerate the files, records, tests, sources, stories, modules, or other units actually in scope. State inaccessible or excluded areas explicitly.
5. Choose proof type per requirement. Distinguish deterministic structural proof, executable test proof, semantic/claim review, provenance proof, persistence proof, and runtime/cold-start proof. Never substitute one proof type for another.
6. Inspect systematically across the full bounded target. Search hits/snippets are leads; inspect substantive evidence where meaning matters.
7. Record findings at requirement level. For each criterion state evidence, result, and limitation.
8. Separate evidence from interpretation. Mark SOURCE/EVIDENCE, INFERENCE, CONFLICT, GAP, NOT FOUND IN SEARCHED SCOPE, NOT SEARCHED/NOT SEARCHABLE, and proposed repair distinctly when applicable.
9. Do not repair during diagnosis unless explicitly authorized. Findings do not authorize deletion, canon promotion, cross-story edits, cleanup, or scope expansion.
10. Respect namespace boundaries. A scoped story/component audit does not authorize inspecting or changing unrelated stories/components merely because a validator can see them.
11. Run reproducible checks when available. Execute maintained validators/tests against the stated baseline/scope and record the test identity/result where supported.
12. Check semantic limits. A structural validator proves only what it checks. File existence, links, counts, hashes, or tests do not prove semantic completeness unless designed to do so.
13. Produce a coverage receipt: baseline, governing criteria inspected, units/evidence inspected, tests executed, exclusions/access limits, and remaining untested requirements.
14. Calibrate the conclusion. Never say complete, clean, fully covered, or equivalent more strongly than the inspected evidence supports.
15. Hand off: missing historical evidence to Recover; conflicting claims to Reconcile; authorized repairs to the owning procedure; durable approved changes to Persist.

## Finding format
For each requirement:
- Requirement
- Evidence inspected
- Result: PASS / PARTIAL / FAIL / OPEN-NOT TESTED / NOT APPLICABLE
- Finding
- Proof type
- Limitation
- Repair/next route, if authorized or useful

## Audit result vocabulary
- PASS — requirement proven for the stated scope and proof type.
- PARTIAL — some required proof exists but the requirement is not fully established.
- FAIL — inspected evidence demonstrates the requirement is violated.
- OPEN / NOT TESTED — required proof was not performed or is unavailable.
- NOT APPLICABLE — requirement does not apply to the stated target.

A collection of PASS results does not imply broader completion outside the audit contract.

## Guardrails
- No silent scope expansion.
- No cross-story inspection or mutation without scope/authority.
- No filename/timestamp/polish-based authority decisions.
- No treating inventory/extraction as semantic review.
- No treating search absence as universal nonexistence.
- No treating a validator as proof of behavior it does not test.
- No treating an audit finding as permission to repair or delete.
- No canon promotion through audit prose.
- No complete claim without a matching completion definition and coverage receipt.
- Preserve evidence and provenance.
