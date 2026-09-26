# Fiction Workflow Orchestration Tests

Status: PROTOTYPE TEST
Skill: fiction-workflow

## A — "Continue the story"
Jim names an existing story and asks to continue it.
Expected: resolve that story, load current records/router/modules, determine whether development is already sufficient, then route through Develop Story if needed, Simulate Character/domain skills, Write Fiction, candidate preservation, and required audits. Do not use chat memory as the primary handoff.

## B — "What does she have in her purse?"
The answer is a current-state inventory question.
Expected: retrieve authoritative current state/inventory. Do not invoke Develop Story or invent contents.

## C — "Would Kate actually say that?"
Expected: retrieve the correct story-local Kate record/current state and use Simulate Character plus relevant context. Do not rewrite plot merely to justify the line.

## D — Historical contradiction
Two current records disagree and provenance is unclear.
Expected: Recover before Reconcile; do not Persist a guess.

## E — Approved scene, prose requested
Scene direction is approved and all consequential inputs are resolved.
Expected: do not re-open settled creative decisions. Route to required domain skills and Write Fiction.

## F — Candidate prose approved
Jim explicitly approves the exact candidate chapter.
Expected: promote exact approved text, Track State occurred consequences, Persist and read-back verify. Do not embellish the approved prose during promotion.

## G — Router reveals missing required location fact
Expected: stop at blocker and resolve via authoritative search / Develop Story / Jim as appropriate. Do not create a generic unnamed venue.

## H — Casual new idea
Jim tosses out a fun one-paragraph story premise and is clearly brainstorming.
Expected: collaborate without immediately forcing full repository initialization. Notice later transition into sustained development.

## I — Sustained new story
The concept acquires recurring characters, scenes, continuity, or manuscript intent.
Expected: search for existing story, establish title/working title, initialize required records, resolve consequential bindings, Persist/verify, then continue development.

## J — Audit discovers unrelated story defect
Expected: respect active namespace and audit scope. Do not repair or open work on the unrelated story without authorization.

## Pass condition
The orchestrator chooses the smallest complete skill chain that satisfies the request, respects authority and scope, stops only for real blockers, and never hides specialist work inside an untestable monolith.
