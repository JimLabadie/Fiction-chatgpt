# Ingestion Recovery and Versioning

Status: ACTIVE PROJECT GOVERNANCE

## Why recovery is necessary

The archive survived across changing AI contexts, workspaces, exports, conversations, and tools. Duplicates, partial consolidations, emergency copies, contradictory snapshots, and eccentric filenames may reflect preservation attempts rather than careless planning. They may also be funny. Both facts belong in the historical record.

Never discard a source because another file appears cleaner. Never assume `final`, a later modification date, a higher version number, or more polished prose makes a document controlling.

## Source registration

Every ingested source receives:

- exact repository path and filename;
- format;
- known creation/export date and modification date when reliable;
- original platform or author when known;
- primary domain and secondary domains;
- declared status inside the file;
- actual project status after review;
- relationship to duplicates or versions;
- decisions, facts, templates, and assistant-generated matter contained within it;
- destination module;
- ingestion status and unresolved questions.

## Mixed-document parsing

Conversation exports and AI-produced documents cannot be assigned one blanket authority. Parse them at claim level:

1. Identify Jim's request or correction.
2. Identify the assistant's proposed interpretation.
3. Determine whether Jim accepted, modified, rejected, or never answered it.
4. Preserve the chronology.
5. Route story facts to the story; route reusable mechanics to the appropriate module; route assistant error patterns and decision history to recovery evidence.

An assistant saying “I have updated,” “locked,” “ingested,” or “made this canon” is not proof that any persistent record changed. Verify the actual artifact.

## Version comparison

For near-duplicates, compare content rather than filenames. Record additions, deletions, renamed characters, generalized placeholders, changed mechanics, and contradictory clauses. Determine whether the later file is:

- an exact duplicate;
- a formatting conversion;
- a generalized reusable form;
- an additive revision;
- a partial rewrite;
- a story-specific branch;
- a correction session;
- an obsolete predecessor;
- unresolved.

If a revised document introduces conflicts without resolving the older rule, retain both and flag the contradiction.

## Preservation architecture

The original source remains unchanged under `Systemwide/Source`. The System Bible contains interpreted canon, detailed ledgers, conflicts, and coverage records. It should not destroy provenance by replacing the archive with a prose synthesis.

Large domains use a top-level index plus child files. Each top-level index states authority, scope, current completion state, controlling sources, child-file map, and unresolved conflicts. Child files hold the detail. A `source-coverage.md` file lists every assigned source and disposition.

## Completion criteria

A domain is complete only when:

- every assigned source appears in its coverage ledger;
- every source has been opened and classified;
- substantive facts and rules have a destination;
- duplicates and variants have a stated relationship;
- conflicts are resolved or explicitly logged;
- non-canon and assistant-generated material are not silently promoted;
- source-to-output checks find no unaccounted substantive sections;
- the published GitHub files are fetched again and verified after upload.

File creation, replacement of a placeholder, a successful commit, or a `10/10` upload count does not prove substantive completeness.

## Import and export lessons from the archive

The legacy Continuity Documentation Pack proposed useful durability concepts: version tags, timestamps, rule snapshots, lineage references, export/import checks, gap tracking, patch logs, interface maps, and recovery verification. Much of that document is assistant-generated scaffolding and contains claims of completion unsupported by actual artifacts. Its architecture is therefore retained as design evidence, not accepted wholesale as an implemented system.

Current exports should be plain, durable, and inspectable. A usable package includes authoritative Markdown, machine-readable tables only where they materially help, source paths, explicit statuses, and version history in Git. Avoid pretending that chat-only menus, validators, dashboards, or “active memory” exist unless the corresponding files and working implementation actually exist.

## Recovery checks

After restoration or migration:

1. Verify the repository tree and branch.
2. Verify source files are intact.
3. Verify every domain index points to existing child files.
4. Verify authority and status language survived.
5. Verify source coverage totals.
6. Verify conflict ledgers remain present.
7. Verify current story handoff against the last accepted scene.
8. Compare the restored revision to the prior Git commit.

## Honest reporting

Progress reports use only these states:

- **Not started:** no source review performed.
- **Inventory complete:** sources identified, content not yet reconstructed.
- **In progress:** some sources or sections processed.
- **Reconstructed pending verification:** content written, coverage check incomplete.
- **Complete:** all completion criteria above passed and remote publication verified.

Never call a summary a complete reconstruction. Never report a local commit as published when the remote push failed.
