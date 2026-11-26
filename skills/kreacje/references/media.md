# Media

## Where media comes from, in this order

1. **Media the caller passed** (`media_ids` of the run): use them first, in the most prominent slots (hook, offer), in the given order, when their kind fits the field.
2. **Brand gallery**: pick by caption fit with the scene's message (the product, the place, the people). The brand context lists only ready, usable media; images go into image fields, ready videos into clip fields.
3. **Brand kit**: the brand kit logo in logo fields; colors through color tokens. A scene with a `palette` field (the neon `featured` and the sale `seasonal` scenes) keeps `brand`, the brand kit colours; pick a fixed style (`sunset`, `gold`, ...) only when the brief asks for that mood.
4. **Nothing fits**: leave the slot empty; for a required slot, propose an image.

## Choosing well

- One media item per slot; reuse an item only when the gallery has too few.
- Never use an item whose caption contradicts the scene (another product, another season, another place).
- People: use a photo of a person in a testimonial only when its caption ties the person to the quoted customer.
- Framing (focus, zoom): only when the caption says where the subject is; the defaults are fine otherwise.
- Kit sample media are neutral placeholders, not brand content; do not use them in a draft.

## Proposing an AI image (`proposeImage`)

- Only for an empty media field where nothing in the gallery fits; one proposal per field, at most 4 per run.
- It is paid: the user sees the price and decides later, and may decline. Never write that the image exists, was generated or will appear; the slot stays empty until the user approves and the image is ready.
- Prompt in English, 1-3 sentences, concrete and visual: the subject from the brief, the setting, the composition for the scene's frame (vertical for 9:16), the light, a style that fits the brand. End with "no text, no logos, no watermarks".
- Do not invent product details the brief does not state (labels, packaging text, colors of a real product). Never depict a real person by name.
- Never for logos, and never as proof: no generated customers, before/after results or "real" photos of the business.

## Video

No AI video in this version: clip fields use ready gallery videos or stay empty.
