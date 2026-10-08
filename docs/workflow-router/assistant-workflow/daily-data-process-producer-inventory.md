# Daily Data Process Producer Inventory

## Purpose

Daily Data Process is the scheduled orchestrator for external acquisition and deterministic daily reconciliation. It does not own duplicate acquisition procedures or parallel acquisition files.

Each acquisition responsibility below invokes its corresponding **Shared Data Operations** acquisition/writer operation. The shared operation owns source acquisition, normalization, authoritative persistence, and verification. DDP records operational proof and moves to the next operation.

## Jim / Ashley acquisition inventory

1. **Calendar/day context** — invoke **Acquire Daily Calendar** for Jim Primary Calendar, Labadie Family Calendar, and the useful near-term horizon required by established consumers.
2. **Weather/day context** — invoke **Acquire Daily Weather** for locations established by authoritative day context. If Jim's day context establishes no location, use Jim's authoritative home location as the default.
3. **Wisconsin sports** — invoke **Acquire Wisconsin Sports**.
4. **Unemployment external evidence** — invoke **Acquire Unemployment External Evidence**.
5. **Job-search correspondence/openings/contact-source evidence** — invoke **Acquire Job-Search Evidence**. Contact facts extracted from acquired communications are part of this operation, not a second source fetch.
6. **Additional event/plan-triggered external facts** — invoke **Acquire Context Facts** only when an established context supplies a concrete need.

## Emily-private acquisition inventory

These operations require the governing private authorization and account routing.

1. **Emily calendar/day context** — invoke **Acquire Daily Calendar** for the explicitly Emily-authorized Google Calendar sources and the configured near-term horizon, writing and verifying the date's complete snapshot in `daily_data.emily_calendar_events`. Record source-by-source success, verified empty results, or failure in the private operational proof. This is a required daily acquisition, not a conditional side effect of the Morning Briefing or calendar mirroring. If an authorized source fails, preserve the prior valid snapshot and record the incomplete acquisition; do not treat a stale snapshot as current.
2. **Publishing evidence** — invoke **Acquire Publishing Evidence**.
3. **Targeted product research** — invoke **Acquire Targeted Product Research** only when an established Emily process supplies a concrete unresolved target.

When DDP requires an Emily outfit or presentation, invoke the authoritative Emily Dress-Me Command. DDP does not independently resolve presentation.

## Daily state reconciliation

Acquisition is not reconciliation. After acquisition, execute established deterministic reconciliation against each domain's authoritative records.

### Emily Life reconciliation

Read `daily_data.reconciliation.last_run` before advancing Emily Life state. Reconcile every applicable established Emily Life operation for dates after `last_run` through the current run date, including simulated consumable usage, inventory/replenishment, laundry and worn/clean availability, hair/cycle/beauty/grooming/maintenance state, purse/content state, other established mundane consequences, and verified calendar mirroring during acquisition. Calendar mirroring is part of acquisition: the Jim Primary and Labadie Family event rows are written to both Jim's and Emily's date snapshots, preserving calendar\_id and event\_id. Emily's own calendar events are written only to Emily's snapshot. No separate synchronization pass, Google Calendar copying, mapping table, or mirror status operation. Verify both complete snapshots before reconciliation is marked complete; preserve the checkpoint if acquisition is incomplete. Use each specialized Emily Life authority. Do not invent advancement. After all applicable Emily Life reconciliation operations have completed and their required writes or no-change results have been verified, set `daily_data.reconciliation.last_run` to the current run date and verify the persisted value. Do not advance `last_run` when required Emily Life reconciliation is incomplete.

### Jim operational reconciliation

Consume persisted shared acquisition results and apply them to existing authoritative Jim operational records only where the governing job-search/unemployment workflow establishes the write. Preserve consequential judgments for the governing domain. DDP does not invent unemployment qualification, representation conflict, opportunity value/priority, discretionary funnel judgment, follow-up priority, or Jim-facing action priority.

## Execution

Execute acquisition operations sequentially:

**invoke shared acquisition/writer → verify its authoritative table result → record privacy-safe operational proof → next operation.**

Do not create a second DDP acquisition file, category output, run-suffixed copy, or caller-specific acquisition result.

Conditional applicability changes the persisted result or makes a parameterized operation non-applicable; it does not authorize a substitute acquisition path.

If an acquisition operation cannot obtain its required data, persist the operation's supported result as unavailable, verify that persisted unavailable result, record the failure and its available operational evidence in the cumulative Log File, and continue to the next independent operation. An unavailable acquisition result does not by itself make the Daily Data Process incomplete and does not block independent acquisition or reconciliation operations. Do not invent missing data or substitute an acquisition mechanism not authorized by the Shared Data Operation.

### Blocked writes: continue independent work

If a database write is blocked, rejected, or fails, record that acquisition as **failed / not persisted**. Do not mark it verified or treat it as a successful unavailable result. Preserve existing authoritative records and checkpoints under the writer's failure contract. Record privacy-safe failure evidence in the existing cumulative Log File where possible; if logging is also blocked, disclose that fact in the final summary without claiming the log was updated.

Continue sequentially through every remaining independent acquisition despite the blocked write. Do not abandon the run because an earlier operation failed. Perform only reconciliations whose required source acquisitions and writes have been verified; skip dependent reconciliations and preserve their checkpoints. Do not use stale records as if freshly acquired, invent fallback writers, or create parallel status tables.

At the end of the run, issue **one consolidated summary** covering all applicable operations: verified successes, verified unavailable results, genuine non-applicability, failed or blocked writes, and dependency-skipped reconciliation. State clearly whether the run was fully or partially completed. Do not end the run early with a failure summary while independent operations remain.

## Completion

Completion proves:

1. every applicable shared acquisition operation was invoked or genuinely non-applicable;
2. every invoked operation's authoritative persistence was verified;
3. every applicable deterministic reconciliation ran against its authoritative record;
4. every required reconciliation write or no-change result was verified;
5. the cumulative Log File contains privacy-safe operational proof.

A verified persisted unavailable result satisfies completion for an acquisition operation when that operation was executed but its required data could not be obtained. Completion means the operation was executed and its actual result was persisted and verified; it does not require every external source to return data successfully.

Historical files and prior DDP outputs are history only, not current acquisition authority.
