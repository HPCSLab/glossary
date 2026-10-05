---
aliases: [beamer, LaTeX Beamer, Beamer class, スライド]
tags: [term]
maps: ["[[Research]]"]
status: draft
updated: 2026-10-06
---
# Beamer

> [[LaTeX]]で発表用のスライドを作成するための文書クラスであり、PDFのスライドを出力する。

## 概要
beamerは、Till Tantauが作成し、2003年3月に最初の版が公開された。現在はJoseph WrightとVedran Miletićが保守している。画面に映して行う発表のスライドを主な対象とし、配布資料や発表者用のノートの作成にも対応している。pdfLaTeX、LuaLaTeX、XeLaTeXなどで処理でき、出力はPDFであるため、環境を問わず同じ見た目で表示できる。

各スライドは `frame` 環境として記述する。`\section` による構成、目次、箇条書きなど、通常のLaTeXの命令をそのまま用いられる。スライドの内容を段階的に表示する重ね合わせ（オーバーレイ）の機能を持ち、一枚のスライドの要素を順に表示させられる。全体の配色、フォント、レイアウトはテーマとして切り替えられる。同じ原稿から、発表用のスライドと、論文の形式の配布資料の両方を作ることもできる。図の描画などには、同じ作者による[[TikZ|PGF]]を利用している。

## どこで出てくるか
論文を[[LaTeX]]で書いている場合、beamerを用いれば、通常のLaTeXの命令がそのまま使えるため、論文の数式などの記述をスライドに流用できる。原稿はテキストファイルであるため、gitで版を管理できる。

## 関係
- 上位概念: [[LaTeX]]
- 使う / 使われる: [[TikZ]]（PGFを用いる）
- 関連: [[Matplotlib]], [[IPSJ SIGHPC]]

## 出典
- [Beamer (LaTeX) - Wikipedia](https://en.wikipedia.org/wiki/Beamer_(LaTeX))
- [beamer - GitHub](https://github.com/josephwright/beamer)
