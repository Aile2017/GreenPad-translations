---
name: greenpad-language-maintenance
description: "Use when adding a new GreenPad language file, propagating missing keys, recalculating xx-XX byte limits from core 6 languages, checking byte-limit violations, or shortening strings to fit limits."
---

# GreenPad Language Maintenance Skill

## Goal
Maintain GreenPad translation files with consistent layout, complete key coverage, and byte-safe UI strings.

## Use This Skill When
- Adding a new language file such as `lang/de-DE.lng`.
- Applying upstream key changes to additional languages.
- Recalculating `lang/xx-XX.lng` byte limits.
- Checking whether translations exceed byte limits.
- Shortening strings while preserving meaning.

## Core Rules
- Keep UTF-8 encoding.
- Keep key names and section structure unchanged.
- Preserve `&`, `\t`, and `\n` behavior.
- Keep all docs/comments in English.

## Standard Workflow
1. Baseline and layout
- Use `lang/en-US.lng` as the structural template.
- Keep section order and key order aligned.

2. Add or update language content
- For new files, translate values only.
- For propagated keys, replace `[TODO]` markers with final translations.

3. Recalculate byte guideline (`xx-XX`)
- Source set must be core 6 only:
  - `en-US.lng`, `ja-JP.lng`, `zh-CN.lng`, `zh-TW.lng`, `ko-KR.lng`, `ru-RU.lng`
- Compute max UTF-8 bytes per **section + key**.
- Write results into `lang/xx-XX.lng` while preserving `en-US` layout.

4. Validate target languages against `xx-XX`
- Compare UTF-8 bytes per section+key.
- Produce violation list with:
  - file
  - line
  - section
  - key
  - current bytes
  - limit
  - overage

5. Fix violations
- Propose concise alternatives first.
- Apply edits that keep meaning and fit limit.
- Re-run validation until zero violations.

## Expected Outputs
- Updated language files with minimal diffs.
- Updated `lang/xx-XX.lng` when requested.
- Clear summary of violations and fixes.
