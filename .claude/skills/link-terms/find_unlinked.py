#!/usr/bin/env python3
"""用語の名前・aliases が本文に現れているのに、本文でリンクされていない箇所を列挙する。

使い方: python3 .claude/skills/link-terms/find_unlinked.py [名前 ...]
  名前には用語名（terms/ のファイル名）か、ノート名（terms/・maps/ のファイル名）を与える。
  用語名なら「その用語へのリンクが欠けている箇所」（被リンク）を、
  ノート名なら「そのノートの中でリンクが欠けている用語」（発リンク）を出す。
  引数なしなら全組を出す。リポジトリのルートで実行する。
出力は候補であり、リンクするかどうかは文脈を読んで判断する。
"""
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
MIN_LEN = 3  # これより短い英数字の別名（C, PC など）は誤検出が多いので除く

LINK = re.compile(r"\[\[([^\]|#\\]+)[^\]]*\]\]")
# 照合から外す部分: 既存のリンク, インラインコード, Markdownリンク, URL
MASK = re.compile(r"\[\[[^\]]*\]\]|`[^`]*`|\[[^\]]*\]\([^)]*\)|https?://\S+")
SKIP_SECTIONS = ("## 関係", "## 出典")  # 本文のリンクの有無の判定と照合の対象から外す節


def parse(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    front, body = (m.group(1), text[m.end():]) if m else ("", text)
    a = re.search(r"^aliases:\s*\[(.*)\]\s*$", front, re.M)
    aliases = [s.strip().strip('"') for s in a.group(1).split(",")] if a else []
    return body, aliases


def body_lines(body):
    """見出しと関係・出典の節を除いた本文の行を (行番号, 行) で返す。"""
    section = ""
    for i, line in enumerate(body.splitlines(), 1):
        if line.startswith("#"):
            section = line
            continue
        if not section.startswith(SKIP_SECTIONS):
            yield i, line


def pattern(name):
    esc = re.escape(name)
    if name.isascii():
        return re.compile(rf"(?<![A-Za-z0-9_\-/.]){esc}(?![A-Za-z0-9_\-])")
    return re.compile(esc)


def main():
    terms = {p.stem: p for p in (ROOT / "terms").glob("*.md")}
    notes = list(terms.values()) + list((ROOT / "maps").glob("*.md")) + [ROOT / "index.md"]
    names = {}
    for stem, p in terms.items():
        _, aliases = parse(p)
        names[stem] = [n for n in [stem] + aliases
                       if n and not (n.isascii() and len(n) < MIN_LEN)]
    # 名前の長い順。長い名前が先に当たった位置は、短い名前の照合から外す
    # （例: 「Lustre PCC」の中の「Lustre」を Lustre の候補にしない）
    by_len = sorted(((pattern(n), n, s) for s, ns in names.items() for n in ns),
                    key=lambda x: -len(x[1]))

    args = set(sys.argv[1:])
    for note in sorted(notes):
        if args and note.stem not in args and not (args & set(terms)):
            continue
        body, _ = parse(note)
        lines = list(body_lines(body))
        linked = {t for _, l in lines for t in LINK.findall(l)}
        found = {}
        for i, line in lines:
            masked = MASK.sub(lambda m: " " * len(m.group()), line)
            for p, name, stem in by_len:
                if stem in found or stem in linked:
                    continue
                if note.parent.name == "terms" and stem == note.stem:
                    continue
                m = p.search(masked)
                if m:
                    found[stem] = (i, m.group(), line.strip())
                    masked = p.sub(lambda m: " " * len(m.group()), masked)
        for stem, (i, word, line) in sorted(found.items(), key=lambda x: x[1][0]):
            if args and stem not in args and note.stem not in args:
                continue
            rel = note.relative_to(ROOT)
            print(f"{rel}:{i}\t{stem}\t「{word}」\t{line[:100]}")


if __name__ == "__main__":
    main()
