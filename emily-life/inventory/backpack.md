# Backpack

Page "Backpack" — id: DE3I8s7QhGBnrJXojZEa, path: /inventory/backpack

## Backpack

Page "Backpack" — id: DE3I8s7QhGBnrJXojZEa, path: /inventory/backpack

### Backpack

The **Backpack ledger** is the generic Tier 5 full-day/work/travel carrier ledger. A physical backpack fills this role; the ledger is not renamed for the product.

Supabase personal-runtime is the sole operational record store for Emily Life. Store and reconcile inventory, quantities, locations, container contents, schedules, state, and operational events there. GitBook retains governing documentation only; never write or mirror operational records into GitBook. Current unknown values remain unknown; discarded historical data must not be used to reconstruct current state.

#### Container relationship

The Backpack ledger follows the same container/subcontainer rule as the rest of Emily Life:

* a subcontainer carried in the backpack appears **once** as an item in the Backpack ledger;
* the subcontainer's internal contents remain in the subcontainer's own ledger;
* moving a subcontainer into or out of the backpack changes the Backpack ledger entry, not the subcontainer's internal ledger;
* do not flatten a module's contents into the Backpack ledger.

#### Established Backpack subcontainer roles

The Tier 5 system has established modular roles. Where an exact physical module or exact current packing has not yet been established, preserve that as unresolved rather than inventing it.

| Subcontainer / module role    | Relationship to Backpack ledger |
| ----------------------------- | ------------------------------- |
| Work module                   | One item when packed            |
| Travel module                 | One item when packed            |
| Seasonal module               | One item when packed            |
| Health / first-aid pouch      | One item when packed            |
| Personal-care / hygiene pouch | One item when packed            |
| Makeup / touch-up bag         | One item when packed            |

The approved Tier 5 organization also includes a padfolio and compact mouse. Those are ordinary Backpack-ledger items when packed unless later established inside a specific subcontainer.

The Purse Contents page remains a **capability/coverage specification** for Tier 5. It does not override the operational ledger model and must not be read as requiring every listed Tier 5 object to appear loose in the Backpack ledger.
