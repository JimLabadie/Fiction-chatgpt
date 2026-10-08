# Laundry & Worn

Page "Laundry & Worn" — id: mXyVrWQ9EKmXYZc7yiWS, path: /state/laundry-and-worn

## Laundry & Worn

This is the maintained garment wear-and-cleaning state beneath Emily Life **State**.

The item table contains actual owned wearable items whose current wear or cleaning state has been established.

Do not create placeholder rows for empty hampers, furniture, possible locations, or inventory containers. A container's existence belongs to Inventory; this ledger records an item only when there is actual item-level state to maintain.

`Last Worn` is updated only from established lived use. A validated outfit selection or recommendation does not by itself establish wear.

When no item-level wear history is established, leave the ledger without invented item rows. Do not reconstruct wear history from prior briefing prose, remembered outfits, or migrated summaries.

**Garment-care operating baseline**

Emily normally does laundry **once per week**. Laundry catch-up advances the ordinary weekly cleaning workflow; it does not invent clothing wears that were never established.

**Wear-before-cleaning starting framework**

Condition always overrides the counter. Visible soil, odor, meaningful perspiration, spills, or other contamination can make an item cleaning-due immediately.

* **1 wear:** panties; hosiery/tights when appropriate; activewear; anything sweaty, soiled, or otherwise not suitable for another wear.
* **1–2 wears:** dresses worn directly against substantial skin; many blouses/tops; sleepwear depending on use.
* **2–4 wears:** bras; skirts; ordinary dresses with limited soil/perspiration; many trousers.
* **3–5+ wears:** sweaters worn over another layer; cardigans; structured pieces where garment condition permits.
* **Several wears / as needed:** jackets, blazers, coats, trenches, and similar outer layers.
* **Special-care / dry-clean garments:** do not clean automatically after every wear. Accumulate wears according to the garment-specific threshold unless condition requires earlier cleaning.

Manufacturer instructions govern when known. Where exact manufacturer instructions cannot be recovered, a conservative care method may be proposed from verified fabric/construction but must be marked **inferred** rather than represented as manufacturer guidance.

**Garment state**

A wearable garment may move through:

**clean → worn but wearable → cleaning due → cleaning route → clean**

Cleaning routes may include ordinary machine wash, delicate/lingerie wash, hand wash, air-dry handling, or dry cleaning. A dry-clean-only garment does not enter an ordinary laundry hamper.

**Verified care examples**

* **Chantelle bras:** manufacturer guidance is no more than two wears between washings and no consecutive-day wear; hand wash with delicate detergent is preferred. If machine washed, use a lingerie bag and delicate/gentle cycle. Always air dry.

**Laundry-system development rule**

The two existing hampers do not receive permanent purposes until the owned wardrobe care audit establishes the useful routing. The audit should assign each owned garment a cleaning method and wear threshold and recover manufacturer/fabric care where possible.

Laundry consumables become part of Emily's depletion model once the resulting cleaning routes and load pattern are established.

**Verified wardrobe care audit — expanded**

Supabase personal-runtime is the sole operational record store for Emily Life. Store and reconcile inventory, quantities, locations, container contents, schedules, state, and operational events there. GitBook retains governing documentation only; never write or mirror operational records into GitBook. Current unknown values remain unknown; discarded historical data must not be used to reconstruct current state.

**Machine-wash route**

**Dry-clean route**

**Hand-wash / lingerie route**

Items without sufficiently matched manufacturer care remain unaudited rather than inferred silently.

**Verified wardrobe care audit — continued**

Additional manufacturer-verified care:

**Machine-wash route**

**Dry-clean route**

**Hand-wash / lingerie route**

Items still lacking an exact or sufficiently matched manufacturer source remain unaudited rather than silently generalized.
