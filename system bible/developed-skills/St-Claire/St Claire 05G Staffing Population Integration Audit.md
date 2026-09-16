# St. Claire — Staffing Population Integration Audit

Status: ACTIVE REPAIR AUDIT
Authority: implements `St Claire 00E Population and Staffing Integration.md` against the staffing batches created before that mechanic was established.

## Scope

Audit the named staffing already created for:

1. Hearth & Home Service Cooperative
2. Washday Laundry & Cleaners
3. St. Claire Moving & Delivery
4. Quiet Harbor Funeral & Memorial
5. Clearview Optometry & Eyewear
6. St. Claire Physical Therapy & Sports Rehab

No additional business staffing is created until this repair audit clears the existing batches.

## Baseline findings

### Existing-population employment search

The maintained `St Claire 03 Population.md` is rich in already-employed residents, but it does not currently expose a reliable structured employment-state field that can be queried for `unemployed`, `underemployed`, `between jobs`, or similar availability states. Repository searches for those terms do not identify a maintained St. Claire pool of named unemployed citizens.

This is itself a data-quality gap: absence of a searchable unemployed pool cannot be interpreted as proof that no existing resident is available. Future Population records must state actual employment state separately from occupation so the population-first rule can be executed mechanically rather than by inference.

### Partner/household integration finding

The pre-00E staffing batches introduced numerous named partners, triad members, and quad members as relationship facts. Those names create real population obligations. They are not complete merely because the employee's record names them.

The repair therefore treats every newly introduced household member as unresolved until the person is found in the maintained Population/Households data or receives a complete resident record with employment state.

### Household co-employment finding

The staffing records did not intentionally place newly created partners into the same small business as the employee who introduced them. This is good, but it is not sufficient by itself: partner employment must be positively resolved elsewhere rather than left blank. The employment-dispersion rule is satisfied only when household members have their own established employment/life state, not merely when they are absent from the first partner's workplace roster.

## Required data repair before reassignment

Before replacing any created employee with an alleged pre-existing unemployed citizen, the existing population must distinguish:

- occupation/profession;
- current employer, if any;
- current employment state: full-time / part-time / self-employed / unemployed-seeking / unemployed-not-seeking / between jobs / student / caregiving / retired / disabled or otherwise not working / other established state;
- availability for additional work when relevant.

Do not infer unemployment from a missing employer or incomplete old record. Missing data remains missing data.

## Audit ledger

### Hearth & Home Service Cooperative
- Staff coverage: COMPLETE
- Existing-population-first check: PENDING — maintained Population lacks reliable employment-state indexing.
- Named partner/household completion: PENDING.
- Same-small-business household clustering: no intentional partner clustering identified in the staffing design; must recheck as household records are resolved.
- Status: STAFF-COMPLETE / POPULATION-INTEGRATION-PENDING.

### Washday Laundry & Cleaners
- Staff coverage: COMPLETE
- Existing-population-first check: PENDING — maintained Population lacks reliable employment-state indexing.
- Named partner/household completion: PENDING.
- Same-small-business household clustering: must be checked against resolved households.
- Status: STAFF-COMPLETE / POPULATION-INTEGRATION-PENDING.

### St. Claire Moving & Delivery
- Staff coverage: COMPLETE
- Existing-population-first check: PENDING — maintained Population lacks reliable employment-state indexing.
- Named partner/household completion: PENDING.
- Same-small-business household clustering: must be checked against resolved households.
- Status: STAFF-COMPLETE / POPULATION-INTEGRATION-PENDING.

### Quiet Harbor Funeral & Memorial
- Staff coverage: COMPLETE
- Existing-population-first check: PENDING — maintained Population lacks reliable employment-state indexing.
- Named partner/household completion: PENDING.
- Same-small-business household clustering: no household was deliberately used to fill multiple roles; recheck after partner resolution.
- Status: STAFF-COMPLETE / POPULATION-INTEGRATION-PENDING.

### Clearview Optometry & Eyewear
- Staff coverage: COMPLETE
- Existing-population-first check: PENDING — maintained Population lacks reliable employment-state indexing.
- Named partner/household completion: PENDING.
- Same-small-business household clustering: no household was deliberately used to fill multiple roles; recheck after partner resolution.
- Status: STAFF-COMPLETE / POPULATION-INTEGRATION-PENDING.

### St. Claire Physical Therapy & Sports Rehab
- Staff coverage: COMPLETE
- Existing-population-first check: PENDING — maintained Population lacks reliable employment-state indexing.
- Named partner/household completion: PENDING.
- Same-small-business household clustering: no household was deliberately used to fill multiple roles; recheck after partner resolution.
- Status: STAFF-COMPLETE / POPULATION-INTEGRATION-PENDING.

## Repair sequence

1. Add explicit employment-state tracking to the adult Population schema.
2. Audit existing named residents for employment state using established occupation/employer facts; do not invent missing states.
3. Produce a real candidate pool of established residents who are unemployed-seeking, underemployed, part-time and seeking more work, between jobs, or apprenticeship-seeking.
4. Resolve every partner/triad/quad/family name introduced by 05E/05F/05E2 against Population and Households.
5. Complete unresolved household members as real residents in small demographic-checked batches, distributing employment across St. Claire rather than reflexively placing relatives together.
6. Compare the actual available-resident pool against each previously created job. Reassign only where an existing resident is a materially better canonical fit and the change does not damage established facts.
7. Verify household employment dispersion for every small business.
8. Re-run aggregate demographic/relationship checks.
9. Promote each organization from `STAFF-COMPLETE / POPULATION-INTEGRATION-PENDING` to `SCENE-READY` only after all checks pass.

## Stop rule

Do not manufacture an unemployed citizen merely to make the audit appear to have found one. Do not assume a resident with incomplete employment data is unemployed. Do not delete a useful newly created worker merely because population-first should have been checked earlier. Repair from actual established facts.