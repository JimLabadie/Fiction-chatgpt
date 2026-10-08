# Jim Job Search & Employment

Page "Jim Job Search & Employment" — id: gqdeerJSttq6IONpbbQa, path: /workflow-router/assistant-workflow/jim-job-search-and-employment

## Jim Job Search & Employment

Page "Jim Job Search & Employment" — id: gqdeerJSttq6IONpbbQa, path: /workflow-router/assistant-workflow/jim-job-search-and-employment

### Jim Job Search & Employment

Page "Jim Job Search & Employment" — id: gqdeerJSttq6IONpbbQa, path: /workflow-router/assistant-workflow/jim-job-search-and-employment

#### Jim Job Search & Employment

**Scope**

This module governs Assistant Workflow-managed job search, recruiter, application, résumé, interview, unemployment work-search, representation/RTR, submission, and related employment operations for Jim.

**Operational Architecture**

The **Supabase project personal-runtime, schema job\_search** is the governing operational database for Jim's job search.

Operational tables exist to own their facts. Their existence does not make them Ashley Daily report sections. Query In Play, Discovery, representation/RTR, interactions, contacts, Opportunity Desk, or the full Plan when the operation or an ad-hoc request actually requires them.

Do not substitute chat memory, prior reports, summaries, Google Sheets, copied counts, or narrative assumptions for authoritative live sources.

**Ashley Daily**

Ashley Daily answers one consumer question: **what does Jim need for today?**

Ashley Daily is a consumer/reconciliation workflow, not an external acquisition implementation. It reads authoritative persisted acquisition results from `daily_data` and applies only the job-search/unemployment reconciliation and consumer reporting defined here.

For the current implementation:

1. Read today's persisted **Job-Search Evidence** and **Unemployment External Evidence**.
2. Reconcile supported evidence into the appropriate `job_search` relations when the governing domain rules establish that write.
3. Read today's persisted **Calendar**, **Weather**, and **Sports** results.
4. Produce only the consumer sections defined below.
5. Write Ashley Daily execution history to `job_search.ashley_daily`. Successful run-log persistence is operational plumbing and is not a consumer report section. Surface it only when the write or required verification fails.

Representation/RTR is reconciliation and authorization state. It is not a prerequisite for an opportunity to be In Play and is not a standalone Ashley Daily report.

Interactions preserve contact/recruiter history. If an interaction requires Jim to do something, that work belongs in Plan; interactions are not a standalone Ashley Daily report.

In Play and Discovery are operational state available for reconciliation and ad-hoc inspection. Their actionable work belongs in Plan; they are not standalone Ashley Daily report sections.

Opportunity Desk is a derived/ad-hoc state view and is not an Ashley Daily report section.

Publishing and Fiction are not part of Jim's Ashley Daily.

**Ashley Daily Consumer Report**

Use descriptive section titles. Never expose implementation labels such as Q1, Q2, or database plumbing as report headings.

**Today's Plan**

Report the active Plan work:

```sql
SELECT
  p.action,
  p.due_date,
  COALESCE(d.position, i.position) AS position,
  COALESCE(d.customer, i.customer) AS customer,
  COALESCE(d.employment_type, i.employment_type) AS employment_type,
  COALESCE(d.work_arrangement, i.work_arrangement) AS work_arrangement,
  COALESCE(d.compensation, i.compensation) AS compensation,
  COALESCE(d.source_url, i.job_url) AS job_url
FROM job_search.opportunity_plan p
LEFT JOIN job_search.discovery_queue d ON d.discovery_id = p.discovery_id
LEFT JOIN job_search.in_play i ON i.opportunity_key = p.opportunity_key
WHERE p.active = true
ORDER BY p.due_date NULLS LAST, p.plan_id;
```

Render Plan as **Company | Position | Employment Type | Work Arrangement | Compensation | Action | Job**. Render `job_url` as a clickable **Job** link. Do not expose internal identifiers or lifecycle plumbing in the consumer grid.

**Unemployment**

Read today's persisted unemployment external result through **Shared Data Operations → Read Unemployment External Evidence**. Do not reproduce or maintain the shared read query here.

Reconcile supported qualifying evidence into the authoritative Unemployment Log before reporting.

**Application Logging:** When Jim applies to a job, record the application in the authoritative opportunity state and interaction history, and also write the qualifying work-search activity to `job_search.unemployment_log` using the application date, employer, position, application method, and authoritative job URL when available. Do not wait for a later Ashley Daily reconciliation to create the unemployment record when the application is already established during the current operation.

Query the Unemployment Log for the current UI week. Derive the current Sunday-through-Saturday UI-week label in the query rather than assuming a column that does not exist:

```sql
SELECT * FROM job_search.unemployment_log
WHERE week =
  to_char(CURRENT_DATE - EXTRACT(DOW FROM CURRENT_DATE)::int, 'MM/DD/YY')
  || ' through '
  || to_char(CURRENT_DATE + (6 - EXTRACT(DOW FROM CURRENT_DATE)::int), 'MM/DD/YY')
  || ', UI Week #'
  || to_char(CURRENT_DATE, 'IW')
  || '/'
  || to_char(CURRENT_DATE, 'YY')
ORDER BY to_date(date, 'MM/DD/YY'), activity;
```

Report the current requirement, the number of qualifying logged activities, what remains required, and the returned current-week activities in a grid with headers. Do not replace current-week results with historical rows.

**Calendar**

Invoke **Shared Data Operations → Read Daily Calendar** for Jim and render every returned row as the combined Calendar grid. Do not maintain a second calendar read query here, reacquire calendar data, or silently include unrelated scopes.

**Weather**

Invoke **Shared Data Operations → Read Daily Weather** and render every returned row. Do not maintain a second weather read query here or reacquire weather.

**Sports**

Invoke **Shared Data Operations → Read Daily Sports** and render every returned row as a grid. Do not maintain a second sports read query here.

**Consumer Presentation Boundary**

Ashley Daily reports today's consumer information, not successful execution mechanics.

Do not report prior runs, successful Gmail acquisition, successful reconciliation, successful integrity checks, successful run-log writes, query names/numbers, database table names, or other operational proof merely because it occurred. If an operational failure materially prevents or undermines the consumer result, surface that failure.

Use grids with headers for structured daily data. Do not turn the report into an executive summary, recap, concluding roll-up, or database dump.

**Database Authority**

Use the database relation that owns the fact.

Operational areas include:

* `opportunity_plan` — the job-search work queue.
* `in_play` — tangible opportunities where Jim has taken or explicitly authorized pursuit.
* `discovery_queue` — durable intake for plausible newly discovered jobs before they become In Play.
* `opportunity_interactions` — recruiter/contact activity and response history.
* `opportunity_representation` — representation/RTR decisions and authorization paths.
* `employment_contact` — recruiter/contact master data.
* `unemployment_log` and `unemployment_log_archive` — unemployment-reporting work-search activity.
* `ashley_daily` — durable Ashley Daily run history.
* `opportunity_desk` — joined/derived state view available for ad-hoc inspection.

**Plan**

**Plan is the job-search work queue.** Discovery is intake. In Play is tangible opportunity state. Plan is work.

A newly discovered job creates Plan work for review only when it passes the Discovery Acceptance Gate below. The Plan row for Discovery review must retain its `discovery_id` relationship so the day's Plan can retrieve the authoritative source URL without duplicating Discovery as a report section. Discovery alone does not make an opportunity In Play.

**Discovery Acceptance Gate:** Evaluate the actual current job posting and available authoritative evidence before creating Plan work. The question is whether the opportunity is one Jim could plausibly pursue and accept, not whether its title or keywords merely resemble his background. Do not invent favorable values for missing criteria.

* **Compensation:** Compensation is a primary acceptance criterion. For salaried employment, the stated base-salary range must reach at least **$125,000 per year**; **$140,000 or more** is the normal target. A salaried role whose maximum stated base salary is below $125,000 does not pass. For contract work, the stated rate must reach at least **$65/hour for W-2** or **$80/hour for C2C/1099**. When compensation is not stated, preserve it as unknown rather than assuming it passes or rejecting the role solely for the missing value.
* **Core work and qualifications:** Jim must have a credible path to performing the core work from his established experience. Do not require every preferred qualification and do not use title or nominal seniority as an independent rejection criterion. Reject roles whose central required expertise is materially outside Jim's background.
* **Location and work arrangement:** Remote work is acceptable when the employer permits Jim to work from Wisconsin; a remote posting whose geographic restrictions exclude Wisconsin does not pass. For hybrid or onsite work, a normal one-way driving time of **120 minutes or less from Jim's home** is within the ordinary commute range. Evaluate commute feasibility by normal driving time rather than straight-line distance or mileage. A longer commute does not automatically reject an otherwise qualifying opportunity; clearly surface the location, onsite requirement, and likely relocation or exceptional-commute issue for Jim's decision.
* **Relocation:** Required relocation is not an automatic rejection. When an opportunity otherwise qualifies, retain it for review and clearly identify the required relocation and destination. Do not assume Jim will relocate; Jim decides whether the specific opportunity justifies relocation.
* **Contract duration:** Contract duration is not an automatic rejection criterion. Short contracts, including engagements of less than six months, may pass when they otherwise satisfy the criteria. Clearly identify the known contract duration for Jim's decision.
* **Cloud-platform experience:** Reject roles whose required core qualifications depend on hands-on **AWS or Google Cloud Platform (GCP)** experience, because Jim does not have established experience with those platforms. Incidental exposure to AWS or GCP, or a preferred rather than required qualification, is not by itself disqualifying; evaluate whether the role can credibly be performed from Jim’s established experience. **Azure is within Jim’s established cloud background. Amazon/AWS and Google/Google Cloud are not excluded employers; employment by either company is acceptable when the specific role otherwise passes the acceptance gate.**
* **Employment practicality:** Reject an opportunity when an established legal, employment-eligibility, clearance, or other mandatory condition makes Jim unable to take the job. Do not treat ordinary shift or on-call requirements as an initial Discovery rejection criterion.
* **Opportunity validity:** The opportunity must be identifiable and current. Reject a dead posting, obvious spam or candidate-harvesting advertisement, or other item that cannot be established as a real current job opportunity.

Conditions that can materially affect Jim's decision but are not automatic rejection criteria—including relocation, short contract duration, substantial travel, longer commute, hybrid/onsite requirements, unusual employment arrangements, and unknown compensation—must be surfaced accurately rather than silently converted into rejection or acceptance.

A role that passes this gate creates Discovery Plan work with the action below. **A role that fails the Discovery Acceptance Gate is discarded. Remove any records created for that candidate from the entire `job_search` operational database, including Discovery, Plan, In Play, interaction, representation, or other opportunity-specific state. A failed candidate that was never pursued, applied to, submitted, represented, or otherwise required as evidence leaves no durable job-search record.**

**Discovery Plan Action:** When a newly discovered role creates Plan work, set the Plan action to exactly `Review the role`. Do not generate explanatory, procedural, disposition, verification, or qualification language in the action.

**Job URL Persistence:** Persist the canonical job posting or application URL when one can be established. Do not persist email-tracking, aggregator-tracking, or redirect URLs as the authoritative job URL when their destination can be resolved. Before a newly discovered role is presented in Plan, verify that its persisted job URL resolves to the intended current job posting. If no working authoritative URL can be established, preserve that fact rather than presenting a known-broken link.

Every active In Play opportunity has active Plan work. When an opportunity closes, mark it no longer In Play and complete/deactivate its current Plan work.

Do not maintain a separate funnel field, remembered funnel state, or narrative funnel summary as operational state.

**Plan Action Completion**

When the action represented by an active Plan row is performed, complete that Plan row immediately by setting it inactive and recording its completion date. Do not replace completed work with passive waiting such as “await response,” “await recruiter reply,” “await client response,” or equivalent language. Waiting is opportunity state, not Plan work.

Record the performed activity in the authoritative interaction/contact history and update applicable contact state such as `last_contact`. If a later response or event creates new work for Jim, create a new Plan item for that new action. Do not keep the completed action open merely because the underlying opportunity remains In Play.

**Opportunity Identity and Representation**

Treat the underlying client opportunity as the unit of identity, not each recruiter's copy of it.

Use client + requisition/job ID as the primary duplicate key when available. If no requisition/job ID exists, use supported client/employer + position + role-description similarity and preserve ambiguity rather than inventing identity.

Recruiter/firm identifies a representation path, not the opportunity itself. Preserve duplicate recruiter approaches as interaction/history without creating duplicate In Play opportunities.

**Historical and Migration Sources**

The native Google Sheet named **leads** and its tabs are migration/historical/supporting material after this cutover. They are not the governing operational job-search record.

Older native leads workbooks, leads.xlsx, and the older Recruiters sheet are historical/supporting sources unless historical recovery is specifically required.

**Jim Contextual Authority**

Use **Jim Personal Operations** for Jim's Identity Profile and general personal context. Job-search operational facts come from the database and current Primary Gmail input.

**Scheduled Operations**

The active **Ashley Daily** ChatGPT Task is an invocation and cadence mechanism only. The live Workflow is the substantive authority for Ashley Daily behavior. The Task does not define a second Ashley Daily procedure.

**Recruiter Keep-Warm Communication**

Generic recruiter keep-warm email is **event-driven contact maintenance**, not a blanket weekly mailing list.

Evaluate eligibility per individual contact. A recruiter/contact receives a generic “I’m still looking” or equivalent keep-warm email only when that contact has an enabled keep-warm communication trigger and the trigger is due.

Suppress the generic keep-warm email for the current communication cycle when either of these conditions is true:

* the contact has an active opportunity with Jim; or
* meaningful recruiter contact has already occurred during the current cycle, including an opportunity-specific follow-up, recruiter reply, submission/status exchange, interview coordination, or other substantive job-search contact.

An opportunity closing does not make the contact immediately eligible for a generic keep-warm email if meaningful contact already occurred during the current cycle. The contact becomes eligible again only on the next allowed cycle when the configured trigger is due and no active-opportunity or same-cycle-contact suppression applies.

`employment_contact.active_opportunity` records the currently active opportunity for the individual contact when one exists. It is blank when no opportunity is active. Recent-contact suppression is tracked separately from active-opportunity state.

`contact_email_trigger` owns per-contact trigger state. Its compound identity is `contact_email + trigger_type + opportunity_key`. Use its enabled/trigger dates and communication history together with current active-opportunity and recent-contact state to determine whether a generic keep-warm email is eligible.

Do not infer firm-level eligibility from another contact at the same company. Communication eligibility belongs to the individual contact.
