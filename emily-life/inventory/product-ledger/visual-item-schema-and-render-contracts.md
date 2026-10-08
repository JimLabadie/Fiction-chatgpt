# Visual Item Schema & Render Contracts

## Purpose

This record defines the canonical visual-description schema and minimum render-readiness contracts for Emily's owned visual inventory. It exists so an owned item can be rendered as a faithful reasonable facsimile without forcing an image model to invent materially different geometry, color, silhouette, scale, or defining features.

This is an inventory-data contract, not an image-generation prompt. The owning item record remains authoritative for the item. Dress Me selects owned items; visualization consumes the selected item records. Image generation does not own, repair, infer, or silently enrich inventory facts.

## Canonical item identity

Every separately owned renderable item must have a stable item identity sufficient to distinguish it from other owned items.

Required identity fields:

* `item_id` — stable unique identifier.
* `category` — governing inventory category.
* `subcategory` — physical item type where category alone is not specific enough.
* `brand` — manufacturer/designer when established; null only when genuinely unknown or unbranded.
* `product_name` — established product/model name when available.
* `variant` — owned colorway/finish/print/model variant when applicable.
* `size` — owned size when the item is sized and the value is established.

Identity fields identify the owned object. They do not substitute for the visual fields below.

## Universal visual fingerprint

Every visually renderable item uses one common visual object. Fields that genuinely do not apply to an item type are null/not-applicable rather than fabricated.

```
visual: {
  primary_color,
  secondary_colors[],
  material,
  finish,
  pattern,
  pattern_colors[],
  silhouette_form,
  scale,
  distinctive_details[],
  image_reference,
  source_reference,
  evidence_status
}
geometry: {
  ...category-specific physical attributes
}
render_readiness
render_readiness_notes
```

Definitions:

* `primary_color` — dominant visible color.
* `secondary_colors[]` — materially visible additional colors.
* `material` — visually significant material or material family.
* `finish` — matte, satin, patent, metallic, crystal, brushed, sheer, glossy, textured, etc., when visually material.
* `pattern` — solid, floral, leopard, stripe, plaid, engineered pleat, graphic, etc.
* `pattern_colors[]` — colors necessary to reproduce a non-solid pattern.
* `silhouette_form` — concise physical form needed to keep the renderer in the correct family.
* `scale` — visually relevant relative or physical scale where size materially affects appearance.
* `distinctive_details[]` — visible identity features that distinguish the item from a generic member of its category.
* `image_reference` — authoritative product/image reference when one is durably available.
* `source_reference` — evidence supporting researched visual facts.
* `evidence_status` — `manufacturer`, `retailer`, `authoritative_record`, `researched_secondary`, `user_established`, or `unknown`.
* `geometry` — category-specific physical attributes defined below.
* `render_readiness` — `complete`, `known_variance`, or `insufficient`.
* `render_readiness_notes` — explicit known unknowns or limitations that affect fidelity.

A field may be null because it is genuinely not applicable. A required applicable field may not be silently omitted, inferred, or guessed.

## Readiness rule

An item is **complete** when every applicable minimum field in its category contract is established with adequate evidence.

An item is **known\_variance** when one or more exact details remain genuinely unknown but the established visual fingerprint is still sufficient to create a reasonable facsimile without changing the item's category, silhouette, major color, scale, or defining features. Known unknowns must be explicit.

An item is **insufficient** when a missing fact would force the renderer to invent a materially important visual property. Insufficient items fail closed for outfit visualization until the missing render-critical fact is established. A product name or brand reputation is never permission to guess.

Optional detail may improve fidelity but does not block rendering.

## Minimum category render contracts

### Dresses

Minimum: primary color; material/finish when visually significant; pattern and pattern colors when non-solid; overall silhouette; dress length/hem position; neckline; sleeve type and sleeve length; waist/fit treatment; skirt shape; and any defining construction such as pleating, draping, ruching, cutouts, slit, tiers, or conspicuous closure.

Geometry keys: `length`, `neckline`, `sleeve_type`, `sleeve_length`, `waist_fit`, `skirt_shape`, `closure`, `pleating`, `slit`.

### Skirts

Minimum: primary color; material/finish; pattern when applicable; silhouette; length/hem position; rise/waist treatment; shape; and defining construction such as pleating, wrap, slit, tiers, ruching, or asymmetric hem.

Geometry keys: `length`, `rise`, `waist_fit`, `skirt_shape`, `closure`, `pleating`, `slit`.

### Tops, blouses, shirts and camisoles

Minimum: primary color; material/finish; pattern when applicable; silhouette/fit; neckline; sleeve type/length or strap type; garment length; and defining details such as collar, buttons, bow, drape, ruching, peplum, lace, or transparency.

Geometry keys: `garment_length`, `neckline`, `collar`, `sleeve_type`, `sleeve_length`, `strap_type`, `fit`, `closure`.

### Cardigans, layered sweaters and knit layers

Minimum: primary color; knit/material impression; pattern/texture; silhouette/fit; garment length; neckline; sleeve length; open-front/pullover/closure form; and defining knit or trim details.

Geometry keys: `garment_length`, `neckline`, `sleeve_length`, `fit`, `front_form`, `closure`.

### Jackets and coats

Minimum: primary color; material/finish; pattern when applicable; silhouette/fit; outerwear length; collar/lapel/neckline; sleeve length; closure type; and defining details such as belt, quilting, hardware, pockets, trim, or hood.

Geometry keys: `outerwear_length`, `collar_lapel`, `sleeve_length`, `fit`, `closure`, `belted`, `hooded`.

### Activewear

Minimum according to physical garment subtype using the applicable top, bottom, dress/one-piece, jacket, or shoe contract. Technical function alone is not a visual description.

### Sleep gowns, nightgowns, robes and private-femininity clothing

Minimum according to physical garment form: primary color; material/finish; opacity where relevant; silhouette; garment length; neckline; sleeve/strap form; closure/tie treatment; and defining lace, trim, embroidery, sheer panels, or other visible construction.

Geometry keys: `garment_length`, `neckline`, `sleeve_or_strap`, `fit`, `closure_or_tie`, `opacity`.

### Bras, panties, bodysuits, bustiers, basques, slips and shapewear

Minimum for a normally concealed foundation item: subtype, primary color, material/finish, coverage/silhouette, strap/sleeve form when applicable, leg/hem form when applicable, and visually defining lace, mesh, boning, cups, panels, closures, or trim. Exact hidden construction that cannot affect a normal clothed rendering is optional. If the item is intentionally visible in the requested look, its visible geometry becomes render-critical.

Geometry keys as applicable: `coverage`, `cup_form`, `strap_form`, `leg_cut`, `garment_length`, `boning`, `closure`, `opacity`.

### Shoes and heeled boots

Minimum: shoe/boot type; primary color; material/finish; toe shape; heel type; **heel height in millimeters or an evidence-backed equivalent convertible to millimeters**; platform height when present; upper/vamp shape; boot shaft height when applicable; strap configuration when applicable; and defining ornament/hardware.

Geometry keys: `shoe_type`, `toe_shape`, `heel_type`, `heel_height_mm`, `platform_height_mm`, `upper_shape`, `shaft_height`, `strap_configuration`.

For a flat shoe, `heel_height_mm` may be zero or the established low heel height. For a heeled item, heel height is mandatory. Visualization may not silently shorten, raise, flatten, or otherwise reinterpret established heel geometry.

### Handbags, purses, clutches and backpacks

Minimum: bag type; primary/secondary colors; material/finish; overall shape; approximate or exact visible scale; width/height/depth when established and materially useful; carry style; handle/strap type; closure; hardware color/finish; and distinctive construction, print, novelty shape, or ornament.

Geometry keys: `bag_shape`, `width`, `height`, `depth`, `handle_drop`, `strap_type`, `carry_style`, `closure`.

A novelty or representational bag requires its recognizable subject/shape as a defining detail; it may not be normalized into a generic bag.

### Belts

Minimum: primary color; material/finish; width or visual width class; buckle shape; buckle material/color; fastening form; and distinctive ornament, texture, or construction.

Geometry keys: `belt_width`, `buckle_shape`, `buckle_finish`, `fastening`.

### Scarves and wearable fabric accessories

Minimum: shape; dimensions or reliable size class; primary/ground color; material/finish; print/pattern; important pattern colors; border treatment; and intended visible wearing form when the selected styling establishes one.

Geometry keys: `scarf_shape`, `length`, `width`, `border`, `wearing_form`.

### Hosiery, tights and stockings

Minimum: hosiery type; primary color; opacity/denier when established; sheer/opaque finish; pattern type; pattern scale/density; pattern placement when non-uniform; and defining seam, back detail, welt, shimmer, or texture.

Geometry keys: `hosiery_type`, `denier`, `opacity`, `pattern_type`, `pattern_scale`, `pattern_placement`, `seam_detail`.

### Sunglasses and eyeglasses

Minimum: frame shape; frame color; frame material/finish; lens shape; lens color/appearance; lens transparency/tint behavior when visually relevant; bridge/temple character when distinctive; and defining hardware.

Geometry keys: `frame_shape`, `frame_material`, `lens_shape`, `lens_color`, `lens_type`, `bridge_form`.

### Watches

Minimum: case shape and approximate size; case material/color; dial/display appearance; band type/material; band color; and defining bezel, crown, face, or smart-display characteristics.

Geometry keys: `case_shape`, `case_size`, `dial_display`, `band_type`, `band_width`.

### Rings and wedding sets

Minimum: metal/color; ring form; band width/scale; principal stone/material when present; stone color; stone shape/cut; setting style; and defining halo, side-stone, stack, signet, engraving, or sculptural details. Wedding sets must preserve the visible relationship of the component rings.

Geometry keys: `ring_form`, `band_width`, `stone_shape`, `setting`, `component_count`.

### Earrings

Minimum: earring type; metal/color; overall scale; drop length when applicable; stone/pearl/material; stone color and shape when applicable; and defining geometry or movement.

Geometry keys: `earring_type`, `overall_size`, `drop_length`, `stone_shape`, `setting`.

### Necklaces and pendants

Minimum: metal/color; chain or structural form; necklace/chain length or reliable length class; pendant/centerpiece dimensions or scale when present; stones/materials and colors; and defining station, pendant, collar, strand, or layered geometry.

Geometry keys: `necklace_type`, `chain_length`, `centerpiece_size`, `strand_count`.

### Bracelets, bangles and cuffs

Minimum: type; metal/color/material; width/scale; rigid/flexible form; stones/materials and colors; closure when visually relevant; and defining geometry.

Geometry keys: `bracelet_type`, `width`, `rigidity`, `closure`.

### Brooches and pins

Minimum: recognizable motif/form; primary and secondary colors; material/finish; approximate dimensions/scale; orientation; and defining enamel, stone, metal, text, figure, or novelty details.

Geometry keys: `motif`, `width`, `height`, `orientation`.

### Tiaras, crowns and head jewelry

Minimum: headpiece type; metal/material and color; overall silhouette; approximate width/circumference/fit where established; maximum visible height; motif; stones/materials and colors; symmetry/asymmetry; and defining decorative construction.

Geometry keys: `headpiece_type`, `circumference_or_fit`, `width`, `max_height`, `motif`, `symmetry`.

A distinctive motif such as the Lalique Dragonfly Tiara's dragonfly identity is render-critical and may not be replaced with generic princess/crystal ornament.

### Hair barrettes, clips, pins, sticks, combs, headbands, bows, ribbons, scrunchies and ponytail ornaments

Minimum: physical ornament type; primary/secondary colors; material/finish; approximate dimensions/scale; silhouette; attachment/placement form; and defining motif, print, crystal, pearl, bow, flower, tail, bead, or sculptural details.

Additional minimum by subtype: combs require comb/ornament width or reliable scale; hair sticks/pins require length; headbands require band width/profile and ornament placement; bows/ribbons require bow size and tail length class; scrunchies require visible volume class; ponytail cuffs require cuff form and finish.

Geometry keys as applicable: `ornament_type`, `width`, `height`, `length`, `band_width`, `tail_length`, `volume_class`, `placement_form`.

### Makeup

For render purposes the owned cosmetic product needs the visible-result fingerprint rather than package geometry.

Minimum: product function; shade/color family; finish; opacity/intensity class where material; and visible effect/placement relevant to its function. Examples include foundation finish/coverage, blush color and finish, eyeliner color/finish, mascara color/effect, eyeshadow color/finish, highlighter reflectivity, and lip color/finish.

Geometry is not normally required. Exact package size, tube shape, compact shape, and applicator are optional unless the product itself is being depicted.

### Manicure and pedicure products

Minimum: color; finish; opacity; effect type such as cream, shimmer, metallic, chrome, scattered holographic, glitter, jelly, or pearl; and any render-critical topper/layering relationship.

When selected for a look, the visible nail result is authoritative; the renderer must not substitute a materially different nail color merely because exact polish photography is unavailable.

### Fragrance

For ordinary worn-outfit rendering, fragrance is non-visible and therefore does not require bottle geometry for presentation readiness. Minimum inventory identity remains brand, product name, concentration/variant when applicable, and ownership status. If the bottle itself is to be depicted, a separate object-render fingerprint is required: bottle shape, glass/color, cap, label/ornament, and approximate scale.

## Category mapping and extensibility

A new inventory category does not require a new physical table. Add a category/subcategory render contract when its physical form is not adequately covered by an existing contract. Reuse the closest physical contract only when the required geometry is genuinely the same.

A subtype may add required fields to its parent category. It may not weaken parent requirements merely to make an incomplete record pass.

## Evidence and research

Visual properties should be established from, in preference order: manufacturer/designer evidence; reliable retailer evidence for the exact product/variant; existing authoritative Emily record; reliable researched secondary evidence; explicit user-established fact.

Do not infer a missing physical specification from a similar product, another colorway with materially different construction, brand convention, generated image, or prior approximation.

When reliable evidence cannot recover an exact detail, preserve the unknown. If the remaining established fingerprint still prevents material substitution, mark `known_variance`; otherwise mark `insufficient`.

## Consumer contract

Dress Me continues to select from authoritative owned inventory. A completed presentation should retain a stable reference to each selected owned item wherever the source architecture supports it.

**Kate, let me see what I'm wearing.** consumes the completed Dress Me selection, resolves each selected item to its authoritative owned-item record, and constructs the image specification from these visual fingerprints. It must not copy guessed visual properties into the presentation record or make generated pixels authoritative inventory evidence.

The visualization may approximate an exact branded product only when the item is `complete` or `known_variance` and the approximation stays within the established visual fingerprint. An `insufficient` selected item blocks rendering of the outfit until the render-critical gap is resolved.

## Audit requirement

The existing owned inventory must be audited against these contracts. The audit must classify every renderable owned item as `complete`, `known_variance`, or `insufficient`, identify each missing applicable minimum field, research recoverable facts from reliable evidence, and persist only established values.

The audit is complete only when every owned renderable item has been evaluated. A subset, sample, or category-level assumption does not establish collection-wide readiness.
