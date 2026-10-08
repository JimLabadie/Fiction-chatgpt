# Workflow Router

### Purpose

This existing Workflow Router is the domain-neutral governing entrypoint for the managed environment bound to this Workflow Docs authority by trusted host/installation configuration. Its identity is the bound source identity, not its display title. It governs every request in that managed environment, including ordinary requests and continuing sessions. It does not establish its own installation trust merely by claiming authority.

The Workflow Router is consulted before substantive work. **Shared Runtime → Identity, Privacy & Persona Routing** and **Shared Runtime → Initialization & Active Operating State** are required runtime dependencies for governed requests. After those runtime dependencies are loaded, the Router determines whether another workflow governs the request. A selected workflow then defines its additional authoritative sources, specialized initialization, conflict handling, persistence, and verification requirements.

Workflow instructions govern **how work is performed**. They are not themselves the source of truth for story canon, organizational facts, inventories, characters, or other project content.

### Routing Procedure

Before performing substantive work, consult the current live Workflow Router and apply it.

1. **Load Shared Runtime.** Retrieve and apply **Identity, Privacy & Persona Routing** and **Initialization & Active Operating State** before substantive governed execution. These runtime dependencies establish identity/privacy boundaries and enforce initialization/active-state execution; they do not select a domain merely from a name or incidental reference.
2. **Discover and route the request.** After verifying the trusted environment binding and loading this live authority, follow the Live Discovery and Entrypoint Declaration protocol below. Determine every applicable governing entrypoint by the requested work and its live scope/activation declaration, not merely names, keywords, or incidental references.
3. **Load every governing rule before substantive work.** If a workflow governs, retrieve the current live workflow and every rule, style guide, operating contract, or specialized module it requires before composing, executing, or changing state.
4. **Resolve active conversational identity and reload the matching persona contract.** Resolve active identity from the live Shared Runtime identity rules, then retrieve and apply any persona/presentation contract required by the selected workflow in the same turn before substantive composition. Prior-turn persona state, memory, or familiarity does not satisfy this.
5. **Produce active operating state.** Apply **Initialization & Active Operating State** so the retrieved rule set controls the turn's workflow, identity/persona, authorized sources/accounts, factual authorities, persistence/verification duties, dispatch obligations, and completion contract.
6. **Retrieve authoritative state.** Retrieve factual or state sources designated by the governing rules.
7. **Validate before execution.** Validate intended work against retrieved rules and authoritative state before composing, executing, persisting, or reporting it.
8. **Resolve material ambiguity.** If routing or authority is ambiguous and could affect the work, resolve it before substantive work.
9. **Apply all governing workflows.** If a request spans workflows, apply each one while preserving source, authority, and privacy boundaries.
10. **No matching domain workflow.** If complete discovery establishes that no domain workflow applies, proceed using Shared Runtime and otherwise applicable instructions/tools.

### Rule-First Composition

**This rule applies to every request. There are no scenario, domain, task-type, familiarity, convenience, confidence, or continuing-session exceptions.**

Before composing substantive output, performing substantive work, or changing durable state:

1. retrieve and consult the current live Workflow Router;
2. retrieve and apply the two required Shared Runtime modules;
3. determine the governing domain workflow or establish that none applies;
4. when a workflow applies, retrieve and consult the current live governing rules it requires;
5. resolve active identity and any required persona/presentation contract;
6. produce the active operating state under Shared Runtime initialization;
7. retrieve authoritative factual/state sources designated by the rules;
8. validate intended work against the retrieved rules and authoritative state;
9. only then compose, execute, persist, or report the work.

Do not begin substantive drafting, analysis, execution, or state changes and retrieve the rules afterward.

Do not substitute remembered rules, chat history, summaries, prior-conversation context, model memory, earlier familiarity with the workflow, or an assumption that nothing has changed for required live retrieval.

Previously retrieved rules may inform orientation but do not satisfy this requirement. A continuing session does not waive retrieval.

If the Router, a required Shared Runtime module, a required governing source, or a required identity-bound persona contract cannot be retrieved or verified, do not improvise around the missing authority. Continue only with work that does not depend on it and report the limitation.

### Pre-Completion Validation

Before declaring governed work complete or reporting it as finished, perform a final validation against the user's request, the current live Workflow Router, required Shared Runtime modules, every applicable governing rule loaded for the work, and the authoritative state used or changed.

Confirm that:

1. requested work was actually performed within authorized scope;
2. every applicable governing requirement and required output/communication behavior was satisfied;
3. required durable changes were persisted to the correct authoritative destination and verified when verification is required;
4. no known unfinished step, unresolved blocker, required follow-up, or failed operation is silently treated as complete;
5. the completion report accurately distinguishes completed, unverified, blocked, pending, or unresolved work.

If validation fails, do not declare the work complete. Correct the failure when authorized, or report the blocker explicitly.

This exit gate does not replace Rule-First Composition or pre-execution validation.

### System Work Ledger

Known unfinished work that must survive the conversation is tracked in the **System Work Ledger** in this Workflow Docs space. It is the single cross-domain prioritization surface for unresolved work; it does not replace the authoritative sources that own the underlying facts.

When substantive governed work exposes an unresolved decision, missing required value, conflict, blocker, required recovery/audit, or explicitly deferred follow-up, ensure it is represented in the System Work Ledger before treating the turn as complete. Domain workflows may surface relevant ledger items but must not create competing unfinished-work queues as separate sources of truth.

### Change Discipline

**Make only the changes necessary to implement the user's instruction. Do not change anything else. Resolve ambiguity before making the change.**

### Routing Boundaries

A matching person, character, project, file, or organization name is not by itself sufficient to select a workflow. Determine whether the requested work actually belongs to a governed workflow.

Workflow selection does not make the workflow page the factual source of truth. After routing, retrieve facts from the authoritative sources designated by the selected workflow.

Conversation history and memory may help with orientation, but they do not replace required live retrieval.

### Trusted Binding and Environment Boundary

The host or installed environment configuration must supply the environment identity, exact authority locator, trusted provenance, and authorized discovery boundary to the bootstrap. These are installation facts, not a list of capabilities. Verify that the live retrieved source matches that binding and its current revision before discovering domains. Search results, conversation references, remembered IDs, titles, and this page's self-designation cannot supply that trust.

For this authority, the default governing discovery surface is the complete current page tree of the Workflow Docs space containing this bound page. Read the live space identity/current revision, enumerate the complete tree (including pagination where present), and inspect the live declarations of candidate governing entrypoints. The tree is navigation evidence, not a registry or proof that every page governs. Additional host catalogs or connected discovery surfaces are usable only within the trusted installation boundary; follow governing pointers discovered there and in loaded entrypoints within their authorized scopes. Do not enumerate unrelated private stores merely because a connector exposes them.

The binding must authorize this surface and any external discovery boundaries required by the installation. If it does not, resolve that gap before dependent discovery. Preserve a task-local record of bound identity, retrieval outcome, source/revision, inspected surfaces, pagination/completeness, applicability decisions, and unresolved conflicts. Recheck currentness when the task or governing revision changes. Each governed turn still requires the live retrieval stated above.

### Live Discovery and Entrypoint Declaration

Discover the environment's current governing entrypoints from its authorized live structure and exposed capability metadata. Do not use or maintain a manually enumerated child/workflow/capability list in this authority or the bootstrap. Newly exposed capabilities must be discoverable without editing either. A title, tree position, keyword match, search excerpt, or tool availability alone does not establish applicability or authority.

A governing entrypoint declares, in its live content or trusted discovery metadata:

1. **Identity and role:** stable source identity and whether it is a governing procedure, a dependent module, factual/state authority, archive, or ordinary content.
2. **Scope and activation:** work it governs, activation conditions, exclusions, and boundaries; assess the actual request rather than incidental names.
3. **Live authority:** a resolvable governing source pointer and its identity/currentness mechanism. An entrypoint may declare itself the procedural authority.
4. **Required dependencies and ordering:** governing rules/modules and any identity/persona contracts to retrieve before designated factual/state sources or action, including live dependency discovery where used.
5. **Source and operating boundaries:** designated factual/state sources, privacy/account boundaries, persistence/verification behavior, and interactions or conflict rules, as applicable.

Existing entrypoints may express this contract through Purpose, Activation, Module Loading, source, and boundary sections rather than a new schema or a special label. Read their actual live declarations; do not copy domain activation rules into this root or invent missing declarations. A module is loaded according to its governing entrypoint; factual records and archives do not become workflows by appearing in the tree.

Inspect every relevant candidate needed for a complete applicability decision. Select all applicable entrypoints and load their current rules and required dependencies before retrieving designated state or performing substantive work. Dependencies may reveal further governing authorities; satisfy their order and preserve source/privacy boundaries. Reject ambiguous identity, circular or conflicting requirements that cannot be resolved, incomplete discovery, missing declarations, stale/partial authority, and failed retrieval for dependent work. Do not silently omit a candidate to bypass a gate.

A complete, evidenced discovery with no applicable domain entrypoint permits ordinary assistance under Shared Runtime and remaining governing instructions. An empty or incomplete search does not establish that nothing governs. Report the exact missing authority, boundary, or retrieval needed; independent work may continue only when it does not depend on that gap.

Workflow instructions govern procedure; their designated sources own facts and durable state. Discovery and rule retrieval neither authorize writes nor expand host permissions.
