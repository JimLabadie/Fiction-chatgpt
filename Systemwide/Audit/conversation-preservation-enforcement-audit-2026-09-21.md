# Conversation preservation enforcement audit

Date: 2026-09-21 (America/Chicago)
Status: COMPLETE FOR THE INSPECTED SCOPE; ENFORCEMENT NOT IMPLEMENTED
Authority: AUDIT EVIDENCE AND RECOMMENDATION; NOT NEW OPERATING RULES OR STORY CANON

Follow-up: the [2026-09-24 story-lifecycle audit](story-lifecycle-audit-2026-09-24.md) adds executable structural validation scoped to generic fixtures and **The Neon Sign**. It does not install the automatic capture mechanism recommended below, and it leaves the semantic fresh-chat test open.

## Answer

The inspected setup has durable records, detailed instructions, repository write capabilities, and native local conversation recording. It does not have an identified automatic connection from fiction conversation turns to repository preservation or a machine-enforced story checkpoint.

Codex lifecycle hooks are a real available implementation route. They were not configured for fiction preservation in the inspected project/user layers. The existing repository protections remain dependent on model execution. This is not evidence that another prose rule is needed.

## Coverage and baseline

The live bootstrap and router were retrieved first:
- `system bible/00-project-bootstrap-template.md`, blob `76a8a2e63c009621f69181b8f330cc58d56e217c`.
- `system bible/00-module-router.md`, blob `6a9d14eb2dfc40e71bba48f197b5b170dedc67b1`.

The router led to the archive recovery protocol, Audit README and component coverage register, modules 01 and 18, and relevant module 01 persistence, ingestion, schema, regression-test, purpose, and ledger records. The active story entry, development record, outline, and current state were inspected for lifecycle evidence.

Live `main` was `a3af93bb57c99ed60644676083d7c85e038ac96b`. Its recursive tree returned `truncated:false`: 698 entries, including 632 files. All paths were enumerated for executable/configuration/automation artifacts. Relevant maintained governance was read or searched; unchanged local copies were checked against live Git blob identities. The existing package-member inventory was consulted for script/hook entries. This is an infrastructure audit, not a semantic review of all historical fiction sources or every packaged document.

The local checkout was clean at `9bd1a0d90b64d97ccfe92c1dd2a1701349474448`, behind the inspected live revision. It is not a continuously synchronized authoritative copy.

The Audit catalog's older baseline remains `230742369a0ef0d441cfa9edf7bc31b44e966adc`. Its 440-path and 402-source counts describe that historical baseline, not the current tree. This audit does not rebuild or replace that catalog.

## Concrete findings

| Layer | Existing mechanism | What actually triggers it | What it proves / fails to prove |
|---|---|---|---|
| Project deployment | Compact project instructions and full bootstrap/router | Project instructions are supplied as context; repository retrieval and application depend on the model | Rules are present. No external pre-turn repository retrieval or successful-application gate was identified. |
| Repository lifecycle | Nine starter documents, candidate/approved chapter areas, approval/state updates, detailed idea preservation | Model follows Markdown instructions and calls tools | No executable initializer, semantic router, checkpoint transaction, or automatic story-state updater was found in the current tree. |
| Audit tooling | `Systemwide/Audit/build_repository_catalog.py` | Someone runs the script | Real executable inventory/hash/container comparison. No scheduler, chat reader, watcher, commit/push operation, or live capture integration. |
| Regression checks | Module 01 `regression-tests.md` | A model/human runs the written scenarios | Markdown test prompts and pass/fail expectations; no executable runner or CI invocation found. |
| GitHub | Repository storage and connector read/write tools | Explicit API/Git operations | Bytes and revisions can be verified after a write; nothing forces the model to make that write. |
| GitHub enforcement | No `.github/workflows` in current tree; runs API returned zero runs; only `main`, `protected:false`; rulesets API returned an empty array | No repository CI trigger found | No active required-check checkpoint found. The workflows-list endpoint itself was rejected by connector URL policy, so the tree and runs evidence support this conclusion. |
| Local Git | Sample hook files only; no configured `core.hooksPath` was returned | Sample hooks are inactive | No installed local Git persistence check found. Connector writes would not execute a workstation Git hook anyway. |
| Codex native storage | A growing local JSONL transcript for this actual audit task, with response and event records | Runtime recording, independently of a model-issued save | Real local raw-history preservation. No repository upload, story attribution, completeness receipt, or canon propagation follows automatically. |
| Codex lifecycle configuration | No user `hooks.json`, inline fiction hooks, or project `.codex` hook layer found | No fiction capture handler configured | Hook capability exists, but a preservation implementation was not found. |
| Existing notification callback | User config contains a computer-use `turn-ended` callback | Configured notification callback | Its target is computer-use integration. No fiction archive destination or preservation routine is configured there; this audit did not claim an observed successful callback execution. |
| Cached plugin hook | Clara package contains a `SessionStart` onboarding-status script | Would depend on plugin activation and hook trust | Inspected handler supplies tutorial context. It is not a fiction recorder. Cache presence does not prove activation or execution. |
| Scheduled work | No local Codex automations directory found | No local saved preservation schedule found | Cloud/account scheduled-task inventory was not available through the inspected configuration; do not infer its absence. |
| Prior-chat access | App `read_thread` successfully returned recent turns from the referenced conversation | Tool invocation | Recovery is possible here. Default responses were truncated; a bounded retrieval is not a full verified export. |

### Existing protections that were not an automatic system

The [Persistence Failure and Repair Record](../../system%20bible/01-system-and-canon-framework/persistence-failure-and-repair-record.md), opened September 13, already records this failure: chat context, archive copies, routing notes, and thin summaries were mistaken for completed propagation. It requires substantive destinations and commit/fetch verification.

The Open Questions and Development Ledger now exists. Its presence corrects a previously missing destination; it does not schedule writes. The ingestion/versioning record explicitly treats historical chat-only validators and documentation-pack architecture as design evidence where working artifacts were absent.

The router explicitly classifies `system bible/developed-skills/**` as recovery evidence, not operating skills. These files are not automatically installed merely by being in GitHub. No fiction-preservation skill appears in this task's available skill catalog. Installing instructional text alone would still not create a lifecycle trigger.

The current compact bootstrap contains an explicit modality-independent automatic-initialization paragraph absent from the project instructions supplied to this task. The installed copy therefore appears stale relative to the maintained compact copy. The full contract already covers input-modality parity. Updating that paragraph would synchronize instructions, not add mechanical execution.

### Current lifecycle evidence

The Even Pretty Girls story has all nine starter records and three approved chapter files. Its README approval register lists chapter 1, then a separate chapter-3 approval section, while current state lists all three chapters. Candidate and approved copies for chapters 1–3 have identical blob hashes and both remain present. The schema calls for removing the promoted candidate in the same revision. The README instead describes copying approval.

These are concrete inconsistencies an executable structural check could flag. They do not prove that the complete Chapter 4–6 planning conversation is preserved, and this audit does not claim to have recovered that planning or authorize changes to story material.

## Available platform mechanisms

[Official hooks documentation](https://learn.chatgpt.com/docs/hooks) describes automatic lifecycle handlers, including `UserPromptSubmit`, `Stop`, `PreCompact`, and `Interrupt`. Hooks can receive a transcript path and turn identity. Non-managed hooks require trust. Synchronous prompt hooks can reject input; Stop blocking requests continuation rather than retracting an answer. Transcript format is unstable and its path may be null. Tool hooks are not a complete enforcement boundary. The installed CLI identifies itself as `0.155.0-alpha.9.2` and exposes hook-trust support; no preservation hook was installed or runtime-tested during this audit.

[Scheduled tasks](https://learn.chatgpt.com/docs/automations) provide actual timed execution and supported app-event triggers. They can run a script or prompt using available tools. A recurring prompt still depends on model compliance; a schedule is not a per-turn transaction or guaranteed full transcript capture. Local runs require the machine and app to remain running. No documented general “every ordinary ChatGPT conversation turn” event was established in this audit.

[ChatGPT Work](https://learn.chatgpt.com/docs/get-started-with-work) supplies file/tool/workflow execution and local/cloud work. Switching to Work alone does not connect all ordinary Chat conversations to a repository capture process. Cloud operation also does not imply access to a local transcript.

[Record & Replay](https://learn.chatgpt.com/docs/extend/record-and-replay) records a demonstrated workflow into a reusable skill and is documented for macOS. It is not a continuous Windows fiction-conversation archive.

## Smallest real enforcement recommendation

Build one project-scoped deterministic recorder, invoked by native Codex lifecycle hooks. Keep the existing fiction governance and destination files.

1. Capture every user/assistant development turn in the selected fiction task without asking the model whether it is substantive. Preserve source text, speaker, order, task/turn identifiers, and provenance. Separately capture manuscript candidates exactly. Avoid copying hidden reasoning, credentials, or unrelated tool payloads as story evidence.
2. Use prompt submission and turn completion as the core capture boundaries; also handle interruption and pre-compaction. Write atomically to a local durable archive and record a content hash plus covered turn range.
3. Check that the previous completed turn has a verified archive receipt before accepting another turn. Capture failures must produce an explicit failure and keep the receipt open. Do not depend solely on asking the model to try again.
4. Upload queued evidence to the authorized repository destination and verify the exact stored bytes/revision. Distinguish local capture from remote backup. This repository is public; a future implementation must keep raw private conversation capture local/private unless publication is explicitly authorized. Existing repository access is not blanket permission to publish all account conversations.
5. Track propagation separately: which captured turns have been reconciled into development, canon, and current-state files. Structural checks can require existing records, valid links, consistent chapter status, and accounted turn ranges. They cannot prove that a paraphrase preserves every meaning or that the model correctly applied canon. Retaining the original text makes those failures recoverable.

This recommendation is engineering analysis, not an installed mechanism or Jim-approved new workflow. Start with capture and receipt verification. A fresh-session test must demonstrate actual automatic invocation without an assistant save call, exact text recovery, duplicate-safe resume, failed-write handling, interruption behavior, and correct project scope. Until that passes, report “not active.”

For ordinary ChatGPT web/voice conversations outside the hooked local runtime, this recorder does not provide coverage. Use accessible conversation retrieval for recovery and verify its pagination/truncation limits. If continued authoring there is essential, separately establish a supported complete export/event integration; none was verified here. A periodic retrieval job can reduce exposure but should not be described as guaranteed lossless capture.

## Remaining limits

- No destructive actions, story edits, new governance rules, hook installation, scheduled-task creation, or native runtime capture test were performed.
- Full cloud project settings, cloud automation inventory, managed policy, and external GitHub webhook consumers were not inspected. Their absence is not asserted.
- No full account export, complete prior-conversation comparison, or semantic completeness test of story planning was performed.
- The public repository findings and this audit can be persisted without publishing local configuration contents or raw private conversations.
