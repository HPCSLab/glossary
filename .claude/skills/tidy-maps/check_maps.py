#!/usr/bin/env python3
"""maps/ と terms/ の機械的な不整合を列挙する。

使い方: python3 .claude/skills/tidy-maps/check_maps.py [map名 ...]
引数なしなら全 map を対象にする。リポジトリのルートで実行する。
"""
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path.cwd()
LINK = re.compile(r"\[\[([^\]|#\\]+)(?:#[^\]|\\]*)?(?:\\?\|[^\]]*)?\]\]")


def term_maps(path):
    """用語ノートの frontmatter の maps: に書かれた map 名の集合。"""
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^maps:\s*\[(.*)\]\s*$", text, re.M)
    return set(LINK.findall(m.group(1))) if m else set()


def main():
    terms = {p.stem: p for p in (ROOT / "terms").glob("*.md")}
    maps = {p.stem: p for p in (ROOT / "maps").glob("*.md")}
    targets = sys.argv[1:] or sorted(maps)

    declared = {name: term_maps(p) for name, p in terms.items()}

    for name in targets:
        if name not in maps:
            print(f"!! map が存在しない: {name}")
            continue
        body = maps[name].read_text(encoding="utf-8")
        # 「まず読む」は本編の項目を再掲する場所なので、重複の数え方からは外す
        section, listed, first = None, [], []
        for line in body.splitlines():
            if line.startswith("## "):
                section = line[3:].strip()
            elif line.lstrip().startswith("- [["):
                (first if section == "まず読む" else listed).append(LINK.findall(line)[0])
        counts = Counter(listed)
        for t in first:
            counts.setdefault(t, 0)

        sizes = re.findall(r"^## (.+?)\n((?:(?!^## ).*\n?)*)", body, re.M)
        sizes = {s: sum(1 for l in b.splitlines() if l.lstrip().startswith("- [[")) for s, b in sizes}
        print(f"=== {name}（{len(listed)} 項目） 節ごと: {sizes}")
        for t, c in counts.items():
            if c > 1:
                print(f"  重複掲載: {t} が {c} 回")
        for t in first:
            if t not in listed:
                print(f"  まず読むのみ: {t} が本編のどの節にも無い")
        for t in sorted(counts):
            if t not in terms and t not in maps and t.split("/")[-1] not in maps:
                print(f"  未作成: {t}")
            elif t in terms and name not in declared[t]:
                print(f"  frontmatter不一致: {t} は掲載されているが maps: に {name} が無い")
        for t in sorted(t for t, ms in declared.items() if name in ms):
            if t not in counts:
                print(f"  未掲載: {t} は maps: に {name} を持つが map に無い")

    if not sys.argv[1:]:
        for t, ms in sorted(declared.items()):
            if not ms:
                print(f"!! どの map にも属さない: {t}")
            for m in ms - set(maps):
                print(f"!! 存在しない map を指す: {t} -> {m}")


if __name__ == "__main__":
    main()
