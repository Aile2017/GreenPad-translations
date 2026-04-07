#!/usr/bin/env python3
"""
en-US.lng を参照として、追加言語ファイルに不足しているキーを
[TODO] マーカー付きで挿入するスクリプト。

対象: BASE_LANGS 以外の lang/*.lng ファイル
"""

import os
import sys

LANG_DIR = "lang"
BASE_LANGS = {"en-US", "ja-JP", "zh-CN", "zh-TW", "ko-KR", "ru-RU"}
REFERENCE = "en-US"


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines()


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def parse_entries_ordered(lines):
    """セクションごとにキーを順序つきで返す: {section: [(key, value), ...]}"""
    sections = {}
    current = None
    for line in lines:
        s = line.strip()
        if s.startswith("[") and s.endswith("]"):
            current = s[1:-1]
            sections.setdefault(current, [])
        elif current is not None and "=" in s and not s.startswith("#"):
            idx = s.index("=")
            key = s[:idx].strip()
            val = s[idx + 1:].strip()
            sections[current].append((key, val))
    return sections


def get_section_order(lines):
    order = []
    for line in lines:
        s = line.strip()
        if s.startswith("[") and s.endswith("]"):
            name = s[1:-1]
            if name not in order:
                order.append(name)
    return order


def propagate(reference_lines, target_path):
    target_lines = read_lines(target_path)

    ref_by_section = parse_entries_ordered(reference_lines)
    tgt_by_section = parse_entries_ordered(target_lines)

    ref_section_order = get_section_order(reference_lines)

    # 不足キーをセクションごとに収集 (参照ファイルでの出現順を保持)
    missing_by_section = {}
    for section in ref_section_order:
        ref_pairs = ref_by_section.get(section, [])
        tgt_keys = {k for k, _ in tgt_by_section.get(section, [])}
        missing = [(k, v) for k, v in ref_pairs if k not in tgt_keys]
        if missing:
            missing_by_section[section] = missing

    if not missing_by_section:
        return False

    result = list(target_lines)

    for section, entries in missing_by_section.items():
        section_header = f"[{section}]"

        # セクションが target に存在するか検索
        section_idx = None
        for i, line in enumerate(result):
            if line.strip() == section_header:
                section_idx = i
                break

        if section_idx is None:
            # セクションが無い場合はファイル末尾に追記
            if result and result[-1].strip():
                result.append("")
            result.append(section_header)
            for key, value in entries:
                result.append(f"{key} = [TODO] {value}")
        else:
            # セクション内の最後のエントリ行を探す
            last_entry_idx = section_idx
            for i in range(section_idx + 1, len(result)):
                s = result[i].strip()
                if s.startswith("[") and s.endswith("]"):
                    break
                if s and not s.startswith("#"):
                    last_entry_idx = i

            insert_lines = [f"{key} = [TODO] {value}" for key, value in entries]
            result = result[:last_entry_idx + 1] + insert_lines + result[last_entry_idx + 1:]

    write_lines(target_path, result)
    return True


def main():
    reference_path = os.path.join(LANG_DIR, f"{REFERENCE}.lng")
    if not os.path.exists(reference_path):
        print(f"ERROR: Reference file not found: {reference_path}", file=sys.stderr)
        sys.exit(1)

    reference_lines = read_lines(reference_path)

    changed = []
    for filename in sorted(os.listdir(LANG_DIR)):
        if not filename.endswith(".lng"):
            continue
        lang_code = filename[:-4]
        if lang_code in BASE_LANGS:
            continue
        target_path = os.path.join(LANG_DIR, filename)
        if propagate(reference_lines, target_path):
            changed.append(filename)
            print(f"Updated: {filename} (missing keys added with [TODO] marker)")
        else:
            print(f"Up to date: {filename}")

    if changed:
        print(f"\nPropagated to: {', '.join(changed)}")
    else:
        print("\nAll additional language files are up to date.")


if __name__ == "__main__":
    main()
