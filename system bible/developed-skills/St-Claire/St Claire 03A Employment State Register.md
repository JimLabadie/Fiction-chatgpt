# St. Claire — Employment State Register

Status: ACTIVE STRUCTURED COMPANION DATA
Authority: operational companion to `St Claire 03 Population.md` implementing `St Claire 00E Population and Staffing Integration.md` without rewriting the large Population file.

## Purpose

`St Claire 03 Population.md` remains the authoritative named-person backbone. This companion exists so employment availability can be tracked and searched safely while the legacy Population records are migrated incrementally.

A missing entry here does **not** mean unemployed. Unknown remains unknown.

## Employment-state vocabulary

Use one of these only when established by evidence:

- full-time
- part-time
- self-employed
- unemployed-seeking
- unemployed-not-seeking
- between jobs
- student
- caregiving
- retired
- disabled or otherwise not working
- other established state
- unresolved legacy state

Each entry records:

- **Name**
- **Occupation/profession**
- **Current employer/organization**
- **Employment state**
- **Work schedule / additional-work availability**
- **Evidence/source**
- **Staffing candidate:** yes / no / unresolved

## Population-first rule

Before creating a new employee, search this register, Population, Households, and existing staffing files. Residents explicitly established as unemployed-seeking, between jobs, apprenticeship-seeking, or part-time and seeking more work are considered before a new resident is created.

Do not infer availability from a blank employer, missing schedule, vague occupation, or an old incomplete record.

## Household-dispersion rule

Partners and family members normally work in different organizations, with separate professional networks and routines. Multiple members of one household working in the same small business requires a specific established reason. A household member without resolved employment is a population-integration gap, not a convenient vacancy filler at her partner's workplace.

## Migration queue

### Existing Population

Current status: MIGRATION REQUIRED.

The legacy Population contains many clearly employed residents because their occupations and organization roles identify current work, but those records predate explicit employment-state tracking. Migrate in small batches from established evidence. Do not rewrite or reinterpret character facts merely to fill this register.

### Pre-00E staffing batches

Current status: STAFF-COMPLETE / POPULATION-INTEGRATION-PENDING.

The employees in 05E, 05F, and 05E2 are clearly employed by their staffing records and therefore are not candidates for other jobs during this repair. Their named partners/household members must be resolved separately.

## Initial verified entries

**Mara Kessler**
- Occupation/profession: Residential service technician / cooperative operations lead
- Current employer/organization: Hearth & Home Service Cooperative
- Employment state: full-time
- Work schedule / additional-work availability: Monday–Friday 7:00 AM–3:30 PM plus established emergency rotation; not an open staffing candidate
- Evidence/source: `St Claire 05E Scene-Ready Staffing.md`
- Staffing candidate: no

**Lena Ortiz**
- Occupation/profession: Service dispatcher/coordinator
- Current employer/organization: Hearth & Home Service Cooperative
- Employment state: full-time
- Work schedule / additional-work availability: Monday–Friday 7:00 AM–3:00 PM plus first Saturday monthly; not an open staffing candidate
- Evidence/source: `St Claire 05E Scene-Ready Staffing.md`
- Staffing candidate: no

**Nia Okafor**
- Occupation/profession: Service dispatcher/coordinator
- Current employer/organization: Hearth & Home Service Cooperative
- Employment state: full-time
- Work schedule / additional-work availability: Monday–Friday 11:00 AM–7:00 PM plus alternating Saturday coverage; not an open staffing candidate
- Evidence/source: `St Claire 05E Scene-Ready Staffing.md`
- Staffing candidate: no

**June Park**
- Occupation/profession: Appliance-repair technician
- Current employer/organization: Hearth & Home Service Cooperative
- Employment state: full-time
- Work schedule / additional-work availability: Tuesday–Saturday 7:00 AM–3:30 PM plus emergency rotation; not an open staffing candidate
- Evidence/source: `St Claire 05E Scene-Ready Staffing.md`
- Staffing candidate: no

**Tessa Vale**
- Occupation/profession: Appliance-repair technician
- Current employer/organization: Hearth & Home Service Cooperative
- Employment state: full-time
- Work schedule / additional-work availability: Tuesday–Saturday 7:00 AM–3:30 PM plus emergency rotation; not an open staffing candidate
- Evidence/source: `St Claire 05E Scene-Ready Staffing.md`
- Staffing candidate: no

**Robin Shah**
- Occupation/profession: General maintenance technician
- Current employer/organization: Hearth & Home Service Cooperative
- Employment state: full-time
- Work schedule / additional-work availability: Monday–Friday 7:00 AM–3:30 PM plus emergency rotation; not an open staffing candidate
- Evidence/source: `St Claire 05E Scene-Ready Staffing.md`
- Staffing candidate: no

**Celia Morgan**
- Occupation/profession: Residential maintenance technician
- Current employer/organization: Hearth & Home Service Cooperative
- Employment state: full-time
- Work schedule / additional-work availability: Monday–Friday 7:00 AM–3:30 PM plus emergency rotation; not an open staffing candidate
- Evidence/source: `St Claire 05E Scene-Ready Staffing.md`
- Staffing candidate: no

**Sofia Rinaldi**
- Occupation/profession: Finish-repair and fixture technician
- Current employer/organization: Hearth & Home Service Cooperative
- Employment state: full-time
- Work schedule / additional-work availability: Monday–Friday 7:00 AM–3:30 PM plus emergency rotation; not an open staffing candidate
- Evidence/source: `St Claire 05E Scene-Ready Staffing.md`
- Staffing candidate: no

**Avery Brooks**
- Occupation/profession: Fixture and residential repair technician
- Current employer/organization: Hearth & Home Service Cooperative
- Employment state: full-time
- Work schedule / additional-work availability: Monday–Friday 7:00 AM–3:30 PM plus emergency rotation; not an open staffing candidate
- Evidence/source: `St Claire 05E Scene-Ready Staffing.md`
- Staffing candidate: no

**Imani Cole**
- Occupation/profession: Residential diagnostic technician
- Current employer/organization: Hearth & Home Service Cooperative
- Employment state: full-time
- Work schedule / additional-work availability: Monday–Friday 10:30 AM–7:00 PM plus emergency rotation; not an open staffing candidate
- Evidence/source: `St Claire 05E Scene-Ready Staffing.md`
- Staffing candidate: no

**Erin Walsh**
- Occupation/profession: Appliance and residential systems technician
- Current employer/organization: Hearth & Home Service Cooperative
- Employment state: full-time
- Work schedule / additional-work availability: Monday–Friday 10:30 AM–7:00 PM plus emergency rotation; not an open staffing candidate
- Evidence/source: `St Claire 05E Scene-Ready Staffing.md`
- Staffing candidate: no

## Unresolved household-member queue — Hearth & Home

The following names were introduced as household/relationship facts in 05E and require resolution against Population and Households before the Hearth & Home batch can clear population integration. They are **not** assumed unemployed and are **not** automatically candidates for Hearth & Home or any other business:

- Elise Navarro — partner of Mara Kessler
- Priya Desai — partner of Lena Ortiz
- Morgan Bell — partner of Lena Ortiz
- Rachel Kim — partner of June Park
- Holly Mercer — partner of Tessa Vale
- Dana Price — partner of Robin Shah
- Mei Alvarez — partner of Robin Shah
- Corinne Blake — partner of Robin Shah
- Naomi Feld — partner of Sofia Rinaldi
- Keisha Ward — partner of Avery Brooks
- Felicia Grant — partner of Imani Cole

Repository search currently finds Elise Navarro only in the 05E staffing record, demonstrating the kind of unresolved Partner-Shaped Object this audit is intended to eliminate. Each queued person must either resolve to an existing authoritative record or receive a complete person/household/employment record in a small checked batch.

## Next migration action

Resolve the Hearth & Home household-member queue first. For each person: search Population and Households; preserve established facts; determine employment state only from evidence; create missing complete records where genuinely absent; distribute employment across St. Claire's existing economic ecology; then perform same-small-business household clustering check before marking Hearth & Home population-integrated.