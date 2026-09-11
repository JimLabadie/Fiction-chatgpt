# Change Worldbuilding Toolkit — Master Index

*A reusable module set for keeping Swap/Change fiction internally consistent, story after story.*

> **Instructions for AI Context Integration:** This index is not itself a scene-writing reference — it's the map. When starting a new story, read this first to decide which modules the story actually needs, then copy those module documents into that story's own project/master document and fill in the bracketed fields for that story's specific premise.

## What This Toolkit Is

A set of story-agnostic reference modules for the recurring worldbuilding problem in Swap/Change fiction: keeping the rules of the change, who's currently who, who knows, how minds and personalities shift, and how bodies adapt over time all consistent across dozens of scenes and, often, multiple books. Each module uses the same format as the existing Presentation Matrix (Module 4.5) already in this project — a short AI-integration instruction, fillable fields and tables, and a guardrails box — so they drop into a story's master document the same way.

A core distinction runs through the whole toolkit: a **swap** exchanges an aspect between two or more individuals (one party's gain is another's loss), while a **change** alters one or more individuals without exchanging anything with anyone else — via duplication, mimicry, or an entirely new source. Neither mechanism is reserved for a particular kind of aspect: a body, a body part, a mind, a mental trait, a hobby, a skill, a memory, or anything else this story defines can be either swapped or changed. Module 1, Section 0 spells this out in full, and Section 3A adds a layer-by-layer breakdown (surface, skill, habit, knowledge, memory, objects) of exactly how much of an aspect actually transfers — it's worth reading both first.

Module 1 also supports a distinct **Perceptual** sub-category (Section 3E), for swaps or changes where the aspect that moves isn't anything the subject's own body, mind, or trait possesses — it's every outside observer's *perception* of the subject. Nothing about the subject is actually different; only how they're seen, heard, and treated changes. This sub-category comes with its own set of standing craft guardrails (the Illusion Confidence Rule, the Conformity Pressure Arc, and — for perceived-gender instances specifically — the Gendered Asymmetry in Consequence note) that govern how observers behave under the illusion. Read Section 3E before writing any scene involving a perceptual swap or change.

## The Four Modules + One Reference

| # | Module | Covers | Pairs With |
|---|---|---|---|
| 1 | Swap Mechanics & Rules Ledger | Section 0 defines swap vs. change (any defined aspect can be either) and sets a Default Depth for aspects a scene names without spelling out, plus whether this story's Perceptual sub-category is in play; Section 1A covers mental/personality trait swaps; Section 3 names what transfers and, just as importantly, what's explicitly excluded from scope; Section 3A breaks down which layers of any aspect actually transfer (surface, skill, habit, knowledge, memory, objects); Section 3B covers clothing/presentation changes specifically — single item vs. whole category, whether the associated body part changes too, and what else can ride along; Section 3C is a per-character table of baseline supporting facts (wardrobe, schedule, occupation) with a verified/unconfirmed flag, so scenes draw on settled facts instead of silently-invented ones; Section 3E covers Perceptual Swaps/Changes — when the aspect that moves is observer perception rather than something the subject possesses — along with its standing craft guardrails; the rest covers trigger, duration, cost, consent, and a precedent log. | Foundational — everything else depends on this one. |
| 2 | Identity & Memory Continuity Tracker | Who's currently in whose body; memory, skill, and personality-bleed rules (with a Trait Bleed Tracker). Note: does not apply to Perceptual Swaps/Changes in the usual sense, since no body or mind actually moves — use it only to make explicit, if useful, that a given instance is perceptual rather than a real body/mind swap. | Character State & Progression Logs (your existing Module 4). |
| 3 | Social, Legal & Institutional Response Framework | Who knows, how the world's systems react, concealment and consequences. For Perceptual Swaps/Changes, the Disclosure Status Map tracks who knows the illusion *is* an illusion (typically just the affected parties) rather than who's found out about a real change — see Section 3E's Illusion Confidence Rule for why in-scene corrections don't shift this. | Module 4.5 for concealment tactics specifically. |
| 4 | Physiological & Sensory Adaptation Log | Internal physical/sensory adaptation over story-time. Not applicable to Perceptual Swaps/Changes, since nothing physical changes for the subject. | Module 4.5, the existing Presentation Matrix (grooming/upkeep skill). |
| Ref. A | Mental Trait Taxonomy | A shared vocabulary (Big Five/OCEAN, cognitive, emotional/motivational, social/behavioral, affective — including interest and hobby reference lists — conative, and aptitude traits) for naming what's swapped or changed in Modules 1 and 2. | Module 1 Section 1A and Module 2 Section 3 — read, don't fill in. |

## Tagging Convention

Reference a module in-scene the same way the Presentation Matrix does: **[Refer to \<Module Name\>: \<Character or Event Name\>]**. For example, `[Refer to Identity Tracker: Mara]` or `[Refer to Mechanics Ledger: the Solstice Rite]`.

## Using This Across Different Stories

- **Not every story needs all four** — a single-swap, low-stakes story might only need Module 1 and a light version of Module 2. A story about a change that's a known, regulated part of the world leans harder on Module 3. A story built entirely around a Perceptual Swap/Change may need little of Modules 2 or 4 at all, since neither body nor mind actually moves — Module 1 Section 3E plus Module 3 typically carry most of the weight. Pick what's load-bearing for the premise.
- **Renumber freely** — these are numbered 1–4 for internal cross-referencing inside the toolkit itself. Slot them wherever they fit a given story's own module scheme — e.g., after that story's Module 4 the way the Presentation Matrix already sits at 4.5 in this project.
- **Fill brackets, don't delete structure** — the bracketed examples in each field show the kind of answer expected; replace them with the actual rule for that story, but keep the field itself even if the answer is "not applicable to this story."
- **Update logs live** — Section 7 of Module 1, Section 6 of Module 2, Section 6 of Module 3, and Section 6 of Module 4 are running logs. Update them in the same session a relevant scene is written, not after the fact, or they stop being trustworthy.
- **Reference A is read-only** — the Mental Trait Taxonomy isn't a fillable log like the others; it's a shared vocabulary. Pull trait names from it into Module 1 Section 1A and Module 2 Section 3 rather than inventing new terms for the same thing.
- **Perceptual Swaps/Changes get their own instance files** — same pattern as any other complex instance (see the Joe/Chloe footwear swap): the reusable mechanics live in the ledger itself (Module 1 Section 3E) and, for perceived-gender specifically, in `change-toolkit_perceived-gender-swap-mechanics.md`; a given couple/instance's specific facts (names, workplaces, established relationships) go in their own instance file, like `change-toolkit_tom-nora-perceived-gender-swap.md`.

## Companion Claude Skill

A packaged Claude Skill ships alongside this toolkit (`change-worldbuilding-toolkit.skill`) with the same four modules and the Mental Trait Taxonomy bundled as reference files, plus instructions for when and how to apply them. Installing it means any Claude session — in this project or a brand-new one — knows to check the ledger before writing a swap, keep the identity roster straight, name mental-trait shifts precisely, get "swap" vs. "change" right in narration, apply the Transfer Package breakdown before assuming a swap or change is all-or-nothing, apply the Perceptual Swap guardrails (Illusion Confidence Rule, Conformity Pressure Arc, Gendered Asymmetry in Consequence) whenever a scene involves observer perception rather than an actual change to the subject, and ask before inventing a new rule, without needing these docs re-explained each time. **As of this update, the skill description still needs to be edited by hand to include the Perceptual Swap guardrails — see `change-toolkit_skill-update-notes.md` for the exact text to add.**

## Files in This Toolkit

- `change-toolkit_00-master-index.md` — this file
- `change-toolkit_01-swap-mechanics-rules-ledger.md` — now includes Section 3E (Perceptual Swaps/Changes) and its standing guardrails
- `change-toolkit_02-identity-memory-continuity-tracker.md`
- `change-toolkit_03-social-legal-institutional-response.md`
- `change-toolkit_04-physiological-sensory-adaptation-log.md`
- `change-toolkit_reference-a-mental-trait-taxonomy.md`
- `change-toolkit_perceived-gender-swap-mechanics.md` — the reusable Section 3E addendum and all four Perceptual Swap guardrails, with full revision history
- `change-toolkit_tom-nora-perceived-gender-swap.md` — instance-specific facts and cross-module entries for the Tom/Nora perceived-gender swap
- `change-toolkit_skill-update-notes.md` — text to paste into the companion skill's description to keep it current with Section 3E
- Matching `.docx` versions of the original six were delivered to you directly (formatted like the existing Presentation Matrix) — save those into whichever story project needs them. The three newer files above have not yet been converted to `.docx`; ask if you'd like that done.
