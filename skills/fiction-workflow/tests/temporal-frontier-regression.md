# Regression Test — Narrative Boundary Must Not Advance Story Day

Status: PROTOTYPE TEST
Origin: live Even Pretty Girls Get the Blues failure discovered during integration testing.

## Failure being prevented
Authoritative development established:
- a Friday daytime thrift-store + Halloway Park picnic sequence;
- the next chapter begins at Blush;
- the Blush return may occur later the same day;
- no authoritative source establishes Saturday.

A workflow incorrectly converted "next chapter begins at Blush" into "Saturday at Blush."

## Required result
On a cold start, Fiction Workflow + Develop Story + Track State must:
1. retrieve the last supported temporal anchor;
2. distinguish narrative/chapter progression from elapsed calendar time;
3. preserve Friday as the controlling day when authority says the Blush return is later that same day;
4. never invent Saturday merely because a new chapter begins;
5. preserve clock time as unknown unless separately established;
6. if sources only say "next chapter" with no supported temporal gap, report the day/time as unresolved rather than selecting one.

## Pass criteria
PASS only if the workflow can state:
- **day:** Friday;
- **sequence:** after the Friday daytime picnic;
- **next narrative unit:** Blush;
- **clock time:** not yet established;
without relying on conversation memory.

Any invented Saturday/date/clock time is a FAIL.
