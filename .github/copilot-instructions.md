# GreenPad Translations Workspace Instructions

## Repository Purpose
- This repository manages language files for GreenPad.
- Upstream core language files are synced from the main GreenPad repository.
- Additional language files are maintained here.

## Language and Documentation Rules
- Write all documentation, comments, and instruction text in English.
- Keep language files encoded as UTF-8.
- Preserve original key names; only change values.

## Language File Editing Rules
- Keep the same layout and key order as `lang/en-US.lng`.
- Preserve sections and key structure.
- Keep accelerator markers (`&`) and shortcuts (`\tCtrl+...`) meaningful and intact.
- Keep escape sequences like `\n` exactly as needed.

## Sync and Propagation Rules
- Upstream core files are: `en-US`, `ja-JP`, `zh-CN`, `zh-TW`, `ko-KR`, `ru-RU`.
- Additional languages are updated by propagating missing keys with `[TODO]` markers.
- When translating, remove `[TODO]` and provide final localized text.

## Byte Guideline Rules
- `lang/xx-XX.lng` is the byte-length guideline file.
- It must preserve `en-US` layout and store per-entry max UTF-8 byte lengths.
- Byte limits are evaluated by **section + key** (for duplicate keys like `Caption`).
- Recalculation baseline is the upstream core 6 languages only unless explicitly requested otherwise.

## Validation Rules
- For any new or updated language, verify each entry is within the `xx-XX` limit.
- Report violations as: file, section, key, current bytes, limit, and overage.
- If requested, propose concise wording alternatives that keep meaning and fit limits.

## Safety and Consistency
- Do not rename existing keys.
- Do not reorder unrelated entries.
- Minimize diffs and avoid unnecessary formatting changes.
