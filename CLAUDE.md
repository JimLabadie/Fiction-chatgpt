# Fiction-chatgpt — Claude Bootstrap

This repository (`JimLabadie/Fiction-chatgpt`) is Jim's authoritative repository for both his
fiction and his personal-assistant workflow system. It is also Git-synced with GitBook:
anything pushed to `main` appears in the corresponding GitBook spaces, and edits made in
GitBook arrive here as commits (`GITBOOK-…`).

This file is Claude's equivalent of `system bible/00-chatgpt-project-bootstrap.md`. That
file and the full operating contract (`system bible/00-project-bootstrap-template.md`) remain
the maintained sources of authority. If this file and the repository contract ever differ,
follow the repository contract and tell Jim this file may need updating.

## Reading the governing documents as Claude

The governing documents were written for ChatGPT. Wherever they say "ChatGPT," read it as
the assistant doing the work — Claude. Wherever they refer to "ChatGPT Memory," that maps to
Claude's memory and past-chat search: useful for orientation, never authoritative over this
repository. Do not rewrite the governing documents to say "Claude" unless Jim asks.

## Before every operation

"Fresh retrieval" from the governing documents means, for Claude:

1. Pull the latest `main` (`git pull`) so the working copy matches GitHub and any edits Jim
   made in GitBook.
2. Determine which domain the request belongs to (below), then re-read that domain's
   governing files from the working copy — do not work from a remembered version of them,
   even later in the same conversation.
3. Retrieve every additional module, skill, story record, or state source those governing
   files route you to, and actually apply them to the work.

## Domains and entry points

**Fiction** — stories, worldbuilding, the System Bible, drafting, canon:

- `system bible/00-project-bootstrap-template.md` — the full operating contract
- `system bible/00-module-router.md`
- `skills/fiction-workflow/SKILL.md`
- `system bible/01-system-and-canon-framework/collaboration-shorthand-and-fun.md` —
  governing collaboration voice, applied to all work including technical and repair work

**Workflow / personal assistant** — Assistant Workflow, Jim and Emily personal operations,
job search, Daily Data Process, morning briefings, shared runtime:

- `docs/README.md` — the Workflow Router (GitBook "Workflow" space), then its Shared Runtime
  modules and whichever domain workflow it selects (`docs/SUMMARY.md` lists the tree)
- Operational data lives in Supabase project `personal-runtime` (`ftpmqywsggplvomjbebx`);
  GitBook/this repo holds governing documentation only. Work directly against that project.

**Emily Life** — `emily-life/` (its `README.md` and `SUMMARY.md` are the entry points).

If a request spans domains, apply each domain's governance while keeping their sources and
privacy boundaries separate.

## Core rules (full detail lives in the contract)

- Jim is the author and final authority. He should talk naturally; finding filenames,
  modules, workflows, and routing is Claude's job, never his.
- Search before assuming something does not exist. Never invent a generic substitute for
  established material.
- Each `stories/<story-name>/` directory is a closed namespace — no cross-story material
  unless Jim asks for it.
- Continue requested work until it is complete unless a consequential creative decision
  genuinely needs Jim.
- Never claim a retrieval, edit, commit, push, or verification that did not actually happen.

## Committing and GitBook sync

- Commit directly to `main` and push when the governing rules call for persistence (e.g.,
  candidate prose preserved at delivery, approved decisions persisted). Pushing is what makes
  the change appear in GitBook.
- Before pushing, `git pull --rebase` so GitBook-originated commits are not overwritten.
- Commit messages name what changed (story/chapter, module, or workflow page).
- Do not edit `gitbook-docs.yaml`, any `.gitbook.yaml`, or a space's `SUMMARY.md`
  structure unless the change requires it — these control what GitBook publishes. When a
  page is added or moved in a GitBook space, update that space's `SUMMARY.md` so it stays
  discoverable.
- Some GitBook settings (creating spaces, publishing/visibility, branding) live in GitBook,
  not in Git. Claude cannot change them; tell Jim when one is needed.
