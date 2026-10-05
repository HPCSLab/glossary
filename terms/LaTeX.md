---
aliases: [Latex, latex, LaTeX2e, TeX, pdfLaTeX, LuaLaTeX, XeLaTeX, LuaTeX-ja, BibTeX, TeX Live, Overleaf, 組版]
tags: [term]
maps: ["[[Research]]"]
status: draft
updated: 2026-10-06
---
# LaTeX

> 文書の内容と見た目を分けて記述し、高品質な組版を行う文書作成システムであり、技術文書や学術論文の作成に広く用いられる。

## 概要
LaTeXは、1980年代初めにLeslie Lamportが、Donald Knuthの組版システムTeXの上に作成した。現在標準となっている版は、1994年に公開されたLaTeX2eであり、LaTeX Projectが保守している。ライセンスはLaTeX Project Public License（LPPL）である。

ワードプロセッサが画面上で見た目を直接整えるのに対し、LaTeXでは、`\section{...}` や `\title{...}` のように、文書の構造を表す命令を書き込んだテキストファイルを作成し、それを処理して見た目を自動的に決める。著者は内容と構造に集中し、体裁の設計はクラスファイルやスタイルに任せる、という考え方である。数式の組版、相互参照、参考文献の管理、多言語の文書に強い。

LaTeXの文書を処理するエンジンには複数の種類がある。pdfTeXはPDFを直接出力し、XeTeXとLuaTeXはUnicodeとOS上のフォントを扱える。日本語の文書には、LuaTeX上で日本語の組版を行うパッケージであるLuaTeX-jaなどを用いる。参考文献はBibTeXなどで管理する。LaTeXとその関連ソフトウェアは、TeX LiveやMiKTeXといった配布形態でまとめて導入でき、Overleafのように、ブラウザ上で共同編集できるサービスもある。

## どこで出てくるか
LaTeXは、複雑な数式や多言語を含む科学技術の文書の作成において、学術界の標準となっている。発表のスライドは[[Beamer|beamer]]で、図は[[TikZ]]や[[Matplotlib|matplotlib]]で作成でき、いずれもLaTeXの文書と同じフォントや数式の表記で揃えられる。原稿はテキストファイルであるため、gitで版を管理できる。

## 関係
- 使う / 使われる: [[Beamer]]（スライドを作るクラス）, [[TikZ]]（図を描くパッケージ）
- 関連: [[Matplotlib]], [[Bachelor's Thesis]], [[Master's Thesis]], [[Doctoral Dissertation]], [[Peer Review]]

## 出典
- [About LaTeX - The LaTeX Project](https://www.latex-project.org/about/)
- [LaTeX - Wikipedia](https://en.wikipedia.org/wiki/LaTeX)
- [LuaTeX-ja - TeX Wiki](https://texwiki.texjp.org/?LuaTeX-ja)
