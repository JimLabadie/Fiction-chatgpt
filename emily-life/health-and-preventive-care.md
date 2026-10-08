# Health & Preventive Care

Page "Health & Preventive Care" — id: jul6wzMx0pT4yq8FVCF5, path: /health-and-preventive-care

## Health & Preventive Care

Page "Health & Preventive Care" — id: jul6wzMx0pT4yq8FVCF5, path: /health-and-preventive-care

### Health & Preventive Care

#### Scope

This record is **simulation continuity for Emily's modeled life**, not management of Jim's real medical care and not a representation of the user's biological medical record. Emily is modeled here as an average-risk 61-year-old postmenopausal woman with an ordinary history of normal preventive screening unless later story/simulation decisions deliberately establish otherwise.

Do not import Jim's real medical records, diagnoses, medications, test results, or health history into this simulated layer unless explicitly instructed. Do not invent disease, abnormal findings, symptoms, or escalating medical drama merely to make the simulation interesting.

The goal is mundane believable life infrastructure: appointments exist, occasionally affect the calendar and Morning Briefing, and usually produce routine normal follow-up.

#### Preventive-care governing model

Supabase personal-runtime is the sole operational record store for Emily Life. Store and reconcile inventory, quantities, locations, container contents, schedules, state, and operational events there. GitBook retains governing documentation only; never write or mirror operational records into GitBook. Current unknown values remain unknown; discarded historical data must not be used to reconstruct current state.

* **Primary/wellness care:** periodic preventive visit.
* **Well-woman/gynecologic care:** periodic well-woman visit remains part of Emily's ordinary care after menopause. Individual screening components do not automatically occur annually.
* **Breast screening:** average risk. Use biennial mammography through age 74 under the current USPSTF baseline.
* **Cervical screening:** cervix present, average risk, adequate normal prior screening, no history of CIN2+, cervical cancer, DES exposure, or immunocompromise. Reassess discontinuation after 65 based on then-current guidance and adequate prior negative screening rather than automatically continuing forever.
* **Colorectal screening:** average risk.
* **Bone health:** no established increased-risk condition in the simulation. Routine DXA is planned at age 65; earlier screening is not automatically scheduled.
* **Dental care:** ordinary preventive dental care is maintained. A six-month simulation cadence is a convenient normal baseline, while recognizing real-world recall intervals are individualized.
* **Eye care:** maintain periodic comprehensive eye care; use a two-year simulation cadence unless a future finding changes it.
* **Vaccination:** review age-appropriate vaccination status during preventive care rather than inventing undocumented prior doses. Annual influenza and then-current COVID recommendations may be handled seasonally. At 61, the simulation should verify completion/status of recombinant zoster, pneumococcal vaccination, and Td/Tdap rather than assume doses were received. RSV remains risk/age-guidance dependent rather than an automatic routine event at 61.

#### Governing current-guidance baseline

Current external guidance is used to keep the simulation plausible and should be rechecked when a future due date arrives rather than frozen forever.

* USPSTF: biennial mammography ages 40–74.
* Current USPSTF cervical guidance in force: ages 30–65 may use primary hrHPV every 5 years, cotesting every 5 years, or cytology every 3 years; the recommendation is under update.
* USPSTF: colorectal screening ages 45–75; colonoscopy is one accepted strategy at a 10-year interval.
* USPSTF: osteoporosis screening for all women 65+, and younger postmenopausal women when increased risk is established.
* ACOG: periodic well-woman care remains appropriate for postmenopausal women; specific services follow their own age/risk intervals.
* CDC vaccination guidance is time-sensitive and must be rechecked at the point of simulated administration.

#### Calendar behavior

Preventive-care appointments belong only on **Emily's calendar**. They may affect outfit, preparation, travel, or the Morning Briefing just like salon maintenance.

Calendar entries are simulation placeholders unless a specific simulated provider/time is deliberately established. Do not write them onto Jim's primary or Labadie Family calendars.

Routine screening results default to ordinary/normal only after the simulated appointment occurs; do not pre-record a future test result.

#### Morning Briefing behavior

Surface preventive care when an appointment is today, when useful preparation is needed, or when a due item is close enough to require scheduling. Do not recite a health checklist every morning.

Keep the tone ordinary and proportionate. A mammogram is an appointment in Emily's life, not an invitation to manufacture anxiety or pathology.
