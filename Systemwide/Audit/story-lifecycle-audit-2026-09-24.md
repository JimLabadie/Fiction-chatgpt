# Story lifecycle and conversation-dependency audit

Date: 2026-09-24 (UTC)
Status: PARTIAL PASS; MECHANICAL STRUCTURE ENFORCED, SEMANTIC COLD START STILL OPEN
Tracks: GitHub issue #2
Authority: AUDIT EVIDENCE AND TEST RESULTS; NOT STORY CANON

## Answer

The repository can now automatically detect several concrete lifecycle failures that previously depended on a model or human noticing them. The new validator and unit tests pass, and **The Neon Sign** passes the structural lifecycle check.

Issue #2 must remain open. This work does not prove that a model notices the transition from casual brainstorming to sustained development, preserves every developed meaning, writes candidate prose immediately, handles a failed write before continuing, or resumes correctly in a genuinely isolated fresh chat. Those are semantic/runtime behaviors rather than repository-shape facts.

## Governing sources and baseline

The live bootstrap and router were retrieved before work. The recovery/source-audit route was followed through:

- `system bible/00-archive-recovery-and-source-audit-protocol.md`;
- `Systemwide/Audit/README.md`;
- `Systemwide/Audit/component-coverage-register.md`;
- System Bible modules 01 and 18;
- the persistence-failure record, open-questions ledger, lifecycle schemas, continuity guidance, and regression tests;
- the 2026-09-21 conversation-preservation enforcement audit;
- GitHub issue #2.

Inspected live baseline: `203268358e61174e5ecb9833b91b37b5d73aa538`.

## Executable coverage added

`validate_story_lifecycle.py` verifies repository facts that can be established deterministically:

- all nine standard starter records exist;
- canonical `chapters/candidate/` and `chapters/approved/` directories exist;
- the noncanonical plural `chapters/candidates/` directory is absent;
- a byte-identical promoted candidate is not retained beside its approved copy;
- a differing candidate beside an approved chapter is reported as a proposed revision requiring status review, not silently deleted;
- every approved Markdown chapter is discoverable in the controlling series-outline chapter map;
- README names or links the required story records without becoming a competing status authority;
- approved prose has a nonempty, recognizable current-story-state handoff.

`test_validate_story_lifecycle.py` supplies isolated fixtures for:

1. a complete passing story;
2. detection of a retained promoted candidate;
3. detection of approved prose without a current handoff;
4. detection of a series-outline/approved-directory authority conflict;
5. detection of an incomplete README navigation map.

These checks enforce structure and discoverability. They deliberately do not claim semantic completeness or authorial approval.

## Test results

Command:

```text
python3 -m unittest discover -s Systemwide/Audit -p 'test_validate_story_lifecycle.py' -v
```

Result: five tests passed.

Scoped repository validation:

- **The Neon Sign:** zero structural findings.
- generic unit suite: five tests passed.

No other story namespace is part of this audit's result. A prior revision exceeded the active-story boundary by testing and changing unrelated stories. The corrective revision restored those story files to their exact pre-audit state and removed the cross-story conclusions. Structural findings outside the active namespace do not authorize inspection, disposition, cleanup, or issue creation without the required task scope and author authority.

## Lifecycle matrix

| Lifecycle stage | Durable rule/record | Executable proof in this pass | Status |
|---|---|---|---|
| Natural idea begins | bootstrap lifecycle threshold | None; semantic recognition is model/runtime behavior | OPEN |
| Brainstorming becomes substantive | bootstrap + development-record requirements | Validator confirms the development destination exists, not that every idea reached it | OPEN |
| Story gets a working/final title | README and series records | Starter-record existence only | PARTIAL |
| Story namespace initializes | nine starter documents + chapter directories | Deterministic structural validation | PASS FOR THE NEON SIGN |
| Development state remains discoverable | README navigation, development, outline, current state | Required links and outline chapter registration checked | PARTIAL PASS |
| Candidate prose is preserved immediately | candidate chapter directory | Repository end state checked; timing/turn boundary cannot be reconstructed automatically | OPEN |
| Revision updates the live candidate | one candidate per prose unit | Differing approved/candidate pair is surfaced for status review | PARTIAL |
| Approval promotes exact text | approved directory + series-outline chapter map | Stale identical candidate and missing outline entry are detectable | PASS FOR THE NEON SIGN |
| Approval updates continuity/handoff | timeline/current state/related records | Current-state presence is checked; semantic completeness is not | PARTIAL |
| Fresh chat resumes correctly | bootstrap/router/story entry point | No genuinely isolated new-chat execution was available in this work session | OPEN |
| Failed write stops continuation | bootstrap failure rule | No controlled connector-write failure was induced | OPEN |
| Interruption/pre-compaction preserves work | recommended lifecycle recorder | No active automatic recorder/hook exists for ordinary ChatGPT conversations | OPEN |

## Remaining closure work for issue #2

1. Run a genuinely isolated fresh-chat test using only the installed Project Instructions and live repository. Record every retrieval, the resolved active story, current handoff, and the correct next pre-work decision.
2. Exercise candidate delivery, revision, approval, and new-chat recovery on one bounded test chapter without leaving duplicate lifecycle artifacts.
3. Exercise a failed persistence operation and verify that the session reports failure before substantive continuation.
4. Establish and runtime-test an automatic capture/receipt mechanism if the goal is protection independent of model compliance. The 2026-09-21 audit explains why repository rules and this validator cannot by themselves guarantee per-turn capture.
5. Decide how ordinary ChatGPT web/voice conversations outside any hooked local runtime receive equivalent coverage. Do not describe the solution as lossless until that route is actually verified.

## Honest completion boundary

This pass materially reduces silent structural drift and supplies repeatable regression evidence. It does **not** close conversation dependency. Structural validation can prove that required artifacts and links exist; it cannot prove that every developed idea was preserved faithfully or that a future model will retrieve and apply them. Issue #2 remains open until the semantic/runtime steps above pass.
