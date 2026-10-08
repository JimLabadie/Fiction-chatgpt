# Shared Data Operations

**Purpose**

This module owns reusable acquisition/writer operations. A caller invokes an operation; it does not reproduce that operation's acquisition, normalization, persistence, or verification procedure. Operations do not change behavior based on the caller.

Persisted results are authoritative for consumers. Consumers query the authoritative table and report or use returned values. They do not reacquire, repair, supplement, reinterpret, or validate what the values ought to be. When the governing consumer contract requires the persisted result to be displayed, reported, or rendered, every required returned value must be preserved; presentation may organize or contextualize it but may not summarize, simplify, collapse, omit, hide, improve, curate, substitute, or selectively display it.

Acquisition operations acquire external evidence/results only. Domain reconciliation and consequential judgment remain with the authoritative domain process.

**Fact persistence discipline**

Persist facts that the authoritative record actually owns. Do not persist a second field, table, queue, audit record, snapshot, copied rule set, copied count, readiness/completeness verdict, missing-field list, eligibility verdict, verification flag, or other derived bookkeeping merely to describe what can be determined by querying authoritative facts or live governing rules.

A consumer determines current applicability, completeness, renderability, eligibility, or similar derived conditions from the live authoritative facts and live governing rules at execution time. Missing required facts remain missing; when the governing workflow requires them, acquire/research them from the authorized source, and when authoritative research cannot resolve a material ambiguity, ask the user. Do not manufacture a durable opinion about the absence.

Timestamps, audit recency, ranking heuristics, hard-coded source identifiers, cached summaries, and prior derived judgments must not be used as substitutes for factual authority. Historical execution facts may be persisted when the occurrence/status of that execution is itself the fact being recorded. Provenance may be retained where it is itself required factual source metadata, but it must not be duplicated inside the factual payload or converted into a readiness/quality judgment.

**Governed operation discovery**

The live Workflow authority is the sole authority for whether a governed Shared Data Operation exists and for that operation's definition. Discover and select governed operations from this module and the governing Producer Inventory.

Do not use a generic tool catalog, connector/function discovery, callable-function names, or the presence or absence of a same-named executable function to determine whether a governed operation exists. Those surfaces are implementation mechanisms only and have no authority to add, remove, rename, redefine, or invalidate a governed operation.

After the governing operation has been identified from the live Workflow, use the operation's definition to select the permitted underlying source, connector, tool, and persistence mechanisms required to execute it. An underlying mechanism does not need to share the governed operation's name.

**Acquire Daily Calendar**

Acquire each authorized source calendar independently for the requested identity and acquisition date. Jim scope requires Jim Primary and Labadie Family; Emily scope uses only Emily-authorized calendars. Record successful coverage, verified empty results, and failures separately. An empty result is not evidence a source was queried.

`report_date` identifies the acquisition snapshot date, not an event's date. Acquire the defined near-term horizon including recurring instances, all-day events, and overnight events overlapping the horizon. Preserve calendar\_id, event\_id, start\_time, end\_time, all\_day and source metadata. Interpret local-day boundaries in America/Chicago for Jim, or the explicitly authorized Emily local time zone. Treat event intervals as half-open \[start\_time, end\_time), and preserve distinct event IDs for recurring instances.

Persist Jim Primary and Labadie Family events in `daily_data.jim_calendar_events` and write the same source events into `daily_data.emily_calendar_events` as part of the same acquisition operation. Also acquire Emily's authorized source calendar and include Emily's own events in her snapshot only. Preserve the original `(report_date, calendar_id, event_id)` identity for every row. No mirror tracking table, synchronization status operation, or copying events to Google Calendar is required.

After every required source read succeeds, replace both tables' requested report\_date snapshots in one database transaction. Jim's snapshot contains Jim/Family events; Emily's contains Jim/Family plus Emily's own events. Preserve snapshots from other dates and leave both requested snapshots unchanged if any required source fails. Verify per-source coverage, distinct event identities, and both persisted results. A verified empty source is not an unqueried source. Keep operational proof separate from consumer data.

**Read Daily Calendar**

Consumers use only their identity-authorized persisted table and never reacquire. A daily view filters the latest verified snapshot to events overlapping the requested local calendar day; report\_date alone is not an event-date filter. Include events where start\_time is before the next local midnight and end\_time is after the requested local midnight, including all-day and overnight events. A separate upcoming view requires an explicit horizon. Distinguish a verified empty snapshot from missing or failed acquisition.

Jim daily view:

```sql
SELECT * FROM daily_data.jim_calendar_events
WHERE report_date = CURRENT_DATE
  AND start_time < ((CURRENT_DATE + 1)::timestamp AT TIME ZONE 'America/Chicago')
  AND end_time > (CURRENT_DATE::timestamp AT TIME ZONE 'America/Chicago')
ORDER BY start_time, calendar_id, event_id;
```

Emily uses the same overlap predicate against `daily_data.emily_calendar_events` in her authorized local time zone.

**Acquire Daily Weather**

Get today's current conditions and today's forecast for the required location using a structured weather source without rendering cards. Never fetch yesterday's weather or historical forecasts. Use the authoritative home location as Jim's default. If the required location cannot be resolved, use Glendale, Wisconsin as the default weather location.

Insert or update today's row in `daily_data.weather`, keyed by `(report_date, location_key)`. Do not add tables, reconciliation, historical lookup, or fallback narrative. If today's weather is unavailable, report failure instead of writing stale data. Consumers read the table.

**Read Daily Weather**

```sql
SELECT * FROM daily_data.weather
WHERE report_date = CURRENT_DATE
ORDER BY location_key;
```

**Acquire Wisconsin Sports**

Acquire a fresh, complete current-day Wisconsin sports calendar directly from Internet sources, prioritizing official team, league, athletics, and broadcaster schedules. Cover Wisconsin professional and major collegiate teams, including women's sports and minor-league professional teams. Discover all today's games across the covered teams; do not restrict discovery to the former four teams. Use the current date in America/Chicago; include scheduled, live, and completed events occurring today.

For each event, capture Wisconsin team, opponent, local start time, home/away, venue, television network, streaming service, applicable geographic or blackout restrictions, special viewing and attendance logistics, and authoritative source URL where supported. Unknown details remain unknown. Gmail is not a sports schedule source. Do not render sports cards, widgets, or other user-facing acquisition output. Do not consult existing sports records, historical data, or prior runs to determine what to search.

Publish one row per Wisconsin-team event to existing `daily_data.sports` with today's `report_date`, actual team, and `plays_today = true`, mapping available facts to existing columns. No invented no-game rows. The existing date/team key may prevent multiple same-day games for one team; if encountered, report the schema limitation rather than silently discard events or change schema without approval.

After a successful complete acquisition, atomically replace the entire table: delete all previous sports records and insert today's discovered events in a single transaction. A confirmed no-games day yields an empty table. On acquisition or persistence failure, retain the last valid snapshot and report failure. Do not retain historical dates, compare with yesterday, reconcile sports, or create status/history tables. Read back and verify every inserted event, row count, today's date, and available viewing details. A verified empty result is valid only after a complete successful search.

**Read Daily Sports**

```sql
SELECT * FROM daily_data.sports
WHERE report_date = CURRENT_DATE
ORDER BY team;
```

**Acquire Unemployment External Evidence**

Acquire the current applicable unemployment work-search requirement, reporting-week boundary, and authorized external evidence sources established by the unemployment process, including Primary Sent Gmail and Primary Calendar evidence when required. Write the acquired requirement/week/evidence result to `daily_data.unemployment_external`, keyed by report date. Verify the persisted row.

This operation does not decide whether evidence qualifies, update the Unemployment Log, or decide what Jim must do. Those are unemployment-domain reconciliation/judgment.

**Read Unemployment External Evidence**

```sql
SELECT * FROM daily_data.unemployment_external
WHERE report_date = CURRENT_DATE;
```

**Acquire Job-Search Evidence**

Acquire authorized current job-search correspondence and source evidence, including alerts/search results, governed Spam evidence, individual openings in digests, recruiter/employer correspondence, application/status/assessment/rejection/interview/submission/RTR evidence, requisition IDs, source postings, supported job details, attachments when needed, and supported contact facts contained in those communications.

Write normalized evidence items to `daily_data.job_search_evidence`, keyed by date and stable evidence key. Verify persisted rows.

This operation does not decide opportunity identity, pursuit, representation, Plan work, In Play state, contact-master changes, or other job-search reconciliation. The job-search domain consumes the acquired evidence and owns those decisions/writes.

**Read Job-Search Evidence**

```sql
SELECT * FROM daily_data.job_search_evidence
WHERE report_date = CURRENT_DATE
ORDER BY evidence_type, evidence_key;
```

**Acquire Context Facts**

When an established calendar event, Plan item, or consumer supplies a concrete external-fact need, acquire only that requested context and persist it to `daily_data.context_facts`, keyed by date, context key, and fact key. Verify persisted rows. This is parameterized acquisition; it is not a generic news or interest feed.

**Read Context Facts**

```sql
SELECT * FROM daily_data.context_facts
WHERE report_date = CURRENT_DATE
ORDER BY context_key, fact_key;
```

**Acquire Publishing Evidence**

Within an authorized private context, acquire established publishing evidence from its governed sources, including configured publishing Gmail evidence, JennyMcD Daily Publication Log evidence/freshness, and live publication-status evidence required by the publishing process. Persist normalized evidence to `daily_data.publishing_evidence`, keyed by date and evidence key. Verify persisted rows.

This operation acquires evidence only; publishing-domain reconciliation owns publication-state decisions.

**Read Publishing Evidence**

```sql
SELECT * FROM daily_data.publishing_evidence
WHERE report_date = CURRENT_DATE
ORDER BY evidence_key;
```

**Acquire Targeted Product Research**

When an authorized consumer supplies a concrete unresolved target, acquire current product evidence for that target and persist normalized results to `daily_data.product_research`, keyed by date, target key, and result key. Verify persisted rows. The supplied target controls scope; this operation does not invent shopping needs or convert research into ownership.

**Read Targeted Product Research**

```sql
SELECT * FROM daily_data.product_research
WHERE report_date = CURRENT_DATE
  AND target_key = :target_key
ORDER BY result_key;
```

**Persist Emily Daily Presentation**

This operation is the authoritative persistence boundary for completed Dress Me output.

**Tables**

* `daily_data.emily_presentation_runs` — one Dress Me execution record containing execution facts only: presentation date, run status, and execution timestamps.
* `daily_data.emily_presentation` — one exact persisted resolution per run and atomic category.

**Producer contract**

Dress Me is the producer. Each daily run is freshly generated.

Before composing today's presentation, the producer reads the previous day's completed presentation and excludes every previously selected worn/used item from today's eligible candidate inventory except the explicit continuity exceptions established by the governing presentation contract: the wedding set, everyday Apple Watch, required daily Ray-Ban Meta Gen 3 Zena smart glasses in Milky Pink Blush, and Emily's signature fragrance. This is a hard eligibility exclusion, not a preference for variety.

No other previous-day item may be selected again unless the governing authority is deliberately changed to establish another continuity exception.

Dress Me then composes one coherent complete presentation from the remaining eligible owned/clean/available inventory. The exclusion is applied to candidate eligibility; Dress Me does not independently rotate categories.

Manicure and pedicure are not continuity exceptions. They are freshly selected as coordinated parts of today's complete presentation. Yesterday's polish does not constrain today's color choice. Current physical nail State is used only after today's selection to determine whether Getting Ready must perform a polish change.

Dress Me creates a pending run and writes one resolution row for every category required by the live Style Book. Before completing the run, Dress Me queries the persisted rows for that run and validates them directly against the **current live Style Book requirements for that execution**. It must establish that every live required category has exactly one persisted resolution, no persisted category is outside the live required set, and every field required by the live governing contract is populated.

Do not persist the Style Book category set, a copied expected-category count, missing-category list, completeness/readiness flag, or any equivalent snapshot/derived validation metadata in the run or presentation rows. The live Style Book remains the authority for what is required.

Only after that live validation succeeds may Dress Me invoke:

```sql
SELECT daily_data.complete_emily_presentation_run(:run_id);
```

The completion operation records the execution fact that the already-validated pending run completed. It does not independently cache or recreate the Style Book's rules. If live validation fails, leave the run non-complete and resolve the factual/category problem rather than persisting a derived diagnosis as authoritative state.

**Read previous-day presentation exclusion**

Dress Me queries the immediately previous day's completed presentation before generating today's presentation. Selected worn/used items from that run are excluded from today's candidate inventory except for the explicit continuity exceptions established by the governing presentation contract.

Historical rows older than the immediately previous day may remain useful presentation history, but they do not create the hard exclusion unless another live governing rule explicitly says so.

**Read Emily Daily Presentation**

Consumers, including Morning Briefing, read only completed persisted Dress Me output:

```sql
SELECT *
FROM daily_data.emily_presentation_current
WHERE presentation_date = CURRENT_DATE
  AND run_id = (
    SELECT run_id
    FROM daily_data.emily_presentation_runs
    WHERE presentation_date = CURRENT_DATE
      AND status = 'complete'
    ORDER BY completed_at DESC, run_id DESC
    LIMIT 1
  )
ORDER BY category_ordinal NULLS LAST, category_key;
```

Consumers report or use the returned persisted values. They do not change them, independently decide another value, reacquire a category, reinterpret the resolution, or fill a missing row. If no completed run exists, the presentation is unavailable until Dress Me successfully persists, live-validates, and completes one.

## Persistent schema approval boundary

No table, column, persistent JSON key, data page or store, queue, audit surface, or equivalent durable schema element may be added, renamed, or structurally changed without the user's explicit approval before that change. A request to clean up an approved schema authorizes only the specific approved changes. Do not introduce replacement bookkeeping or parallel persistence as a workaround.

## Emily outfit inventory schema — approved target

`daily_data.emily_visual_items` is for choosing owned items for outfits, rendering them faithfully, and describing them. Its approved target columns are `item_id` (text primary key), `category` (text required), `subcategory` (text), `brand` (text), `product_name` (text), `color` (text), `size` (text), `visual` (jsonb), `geometry` (jsonb), `quantity` (numeric), and `item_notes` (text). `visual` holds factual appearance; `geometry` holds factual shape, construction and dimensions. No self-referential source fields, readiness/verification filler, or acquisition commentary. Existing facts necessary for item selection, availability, rendering, and descriptions must not be silently discarded during migration. This is an approved target, not an assertion that the database migration is complete.
