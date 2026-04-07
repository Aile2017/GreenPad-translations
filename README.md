# GreenPad Translations

[GreenPad](https://github.com/Aile2017/GreenPad) テキストエディタの言語ファイルを管理するリポジトリです。

本家リポジトリが管理する 6 言語（英語・日本語・中国語簡体字/繁体字・韓国語・ロシア語）に加えて、追加言語の翻訳を管理します。

---

## 収録言語

| ファイル | 言語 |
|---|---|
| `en-US.lng` | English (United States) |
| `ja-JP.lng` | 日本語 |
| `zh-CN.lng` | 中文（简体） |
| `zh-TW.lng` | 中文（繁體） |
| `ko-KR.lng` | 한국어 |
| `ru-RU.lng` | Русский |
| `fr-FR.lng` | Français |

---

## 自動同期について

GitHub Actions ([`.github/workflows/sync-upstream.yml`](.github/workflows/sync-upstream.yml)) により、毎日 2:00 UTC に本家リポジトリの言語ファイルが自動取得されます。

本家で新しいキーが追加された場合、追加言語ファイル（上記 6 言語以外）へ `[TODO]` マーカー付きで自動挿入されます。

```ini
# 例: 未訳の状態
IDS_NOTFOUNDUP = [TODO] String Not Found.\nContinue searching from the bottom?
```

手動実行も可能です: Actions タブ → "Sync from upstream GreenPad" → "Run workflow"

---

## 翻訳への参加方法

1. このリポジトリを fork する
2. `lang/` 以下の対象ファイルを編集する
   - 新規言語を追加する場合は `lang/xx-XX.lng` を作成し、`en-US.lng` を参考に翻訳する
   - 既存ファイルの `[TODO]` 箇所を翻訳して `[TODO]` を削除する
3. Pull Request を送る

### 言語ファイルの形式

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

- エンコーディングは **UTF-8**
- `[Info]` セクションの `Language` と `LangCode` は対象言語に合わせて記述する
- キーは変更しない。値のみ翻訳する

---

## ライセンス

本家 [GreenPad](https://github.com/Aile2017/GreenPad) のライセンスに準じます。
