# GreenPad Translations

[GreenPad](https://github.com/Aile2017/GreenPad) text editor language files are managed in this repository.

In addition to the 6 languages maintained in the upstream repository (English, Japanese, Chinese Simplified/Traditional, Korean, and Russian), this repository also maintains additional languages.

---

## Included Languages

| File | Language |
|---|---|
| `en-US.lng` | English (United States) |
| `ja-JP.lng` | Japanese |
| `zh-CN.lng` | Chinese (Simplified) |
| `zh-TW.lng` | Chinese (Traditional) |
| `ko-KR.lng` | Korean |
| `ru-RU.lng` | Russian |
| `fr-FR.lng` | French |
| `de-DE.lng` | German |

---

## Automatic Synchronization

GitHub Actions ([`.github/workflows/sync-upstream.yml`](.github/workflows/sync-upstream.yml)) automatically fetches language files from the upstream repository every day at 2:00 UTC.

When new keys are added upstream, missing entries are automatically inserted into additional language files (languages other than the 6 upstream languages) with a `[TODO]` marker.

```ini
# Example: untranslated state
IDS_NOTFOUNDUP = [TODO] String Not Found.\nContinue searching from the bottom?
```

Manual execution is also available: Actions tab -> "Sync from upstream GreenPad" -> "Run workflow"

---

## How To Contribute Translations

1. Fork this repository.
2. Edit the target file under `lang/`.
   - To add a new language, create `lang/xx-XX.lng` and translate based on `en-US.lng`.
   - Translate `[TODO]` entries in existing files and remove the `[TODO]` marker.
3. Submit a pull request.

### Language File Format

```ini
# GreenPad Language File
# Language: French (France)
# Encoding: UTF-8

[Info]
Language = French
LangCode = fr-FR

[Strings]
IDS_APPNAME = GreenPad
...

[Menu]
...

[Dialog.IDD_FINDREPLACE]
...
```

- Use **UTF-8** encoding.
- Set `Language` and `LangCode` in the `[Info]` section for the target language.
- Do not modify keys. Translate values only.

---

## License

This repository follows the license of upstream [GreenPad](https://github.com/Aile2017/GreenPad).
