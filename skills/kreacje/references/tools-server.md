# Server tools (SyncBooster subagent)

Tool mapping version 1. Your tools are bound to one run: the brand, channel and user are fixed by the server, so no tool takes a brand, channel or user id. An id that does not belong to the brand answers "not found".

| Tool | What it does | When to use it |
|---|---|---|
| `getBriefContext` | Returns a section of the brand context in full: profile, knowledge documents, gallery captions, brand kit. | Only when your prompt marks a section as truncated; the context is already in your prompt. |
| `searchPresets` | Ranks scene presets for a query, goal and format; each with `reasons[]`, `needs[]` and `fields`: sample texts shown as examples, not the values the scene is added with (SKILL.md step 4). | Step 2. One call per goal or angle is usually enough. |
| `listSceneTypes` | Lists scene types with fields, `max_length`, `recommended_max_chars`, duration range and `whenToUseForAi`. | When a preset leaves a field's meaning or limit unclear. One call returns the whole catalog. |
| `createDraft` | Creates the project from a ready reel or empty, named `Szkic: <title>`, or binds the existing draft the run revises. | Once, after the plan is complete. |
| `applyOperations` | Applies a batch of operations against the current revision: `set_field`, `add_preset_scene`, `add_scene`, `remove_scene`, `move_scene`, `set_scene_duration`, `set_transition`, `set_text_overlay`, `set_audio`, `set_format`, `set_position`, `reset_position`. | Step 5 as one batch; one more batch for fixes. |
| `getDraft` | Returns the document, `to_complete`, `values_to_confirm` and `over_recommended`: texts and list items over their recommended length. | After the fill batch, and again only if you changed the draft after the last check. |
| `proposeImage` | Records a paid AI image proposal for one empty media field with your prompt. It never generates anything. | At most 4 per run, only for slots where no gallery media fits. |
| `readSkillReference` | Returns one file of this skill, for example `regulated-values.md`. | When SKILL.md is not enough for the case at hand; every call costs a step. |
| `finish` | Ends the run with your summary (at most 600 characters). | Exactly once, as the last call. |

Not available by design: render, price quote, image or video generation, publishing or scheduling, value confirmation, brand kit or brand profile changes. Do not ask for them and never say you did them.

## Operation notes

- `scene_index` is 0-based and refers to the scene order after the earlier operations of the same batch.
- Color fields: `{ "color_token": "accent" }` (or `foreground`, `background`) so the brand kit drives the colors; use a hex color only when the brand kit or the brief names it.
- Logo fields: the brand kit logo media id. No logo in the brand kit: leave the field empty.
- `set_audio`: only with a music upload of the brand listed in the brand context; otherwise leave the audio unset.
- `set_text_overlay`: only on scene types that declare an overlay; otherwise the operation is refused.
- A save conflict (`revision_conflict`) means someone edited the draft: read it again with `getDraft` and apply only what is still needed.

## A typical run

1. `searchPresets` (with `listSceneTypes` in parallel when needed)
2. `createDraft`
3. `applyOperations` (everything)
4. `getDraft`
5. `applyOperations` (fixes) and `proposeImage` calls in parallel
6. `finish`

The run stops at 12 steps. A run that stops without a draft fails; a run that stops with a draft keeps it, so create the draft early and finish deliberately.
