---
aliases: [tikz, PGF, PGF/TikZ, pgfplots, TikZ ist kein Zeichenprogramm]
tags: [term]
maps: ["[[Research]]"]
status: draft
updated: 2026-10-06
---
# TikZ

> [[LaTeX]]などのTeXの文書の中で、図形を座標と命令によって記述し、ベクタ形式の図を描くためのパッケージである。

## 概要
TikZとPGFは、Till Tantauが設計した、図を記述するための二層の言語である。PGFは低水準の層であり、TeXの様々な出力系（pdfTeXやdvipsなど）に対応した描画の命令を提供する。TikZは、その上に構築された、利用者が書きやすい高水準の命令の集まりである。TikZという名前は、ドイツ語の "TikZ ist kein Zeichenprogramm"（TikZは描画ソフトではない）の頭文字をとった再帰的な略語である。LaTeXのほか、ConTeXtやplain TeXでも利用できる。2018年以降は、Henri Menkeが主な開発者となっている。

TikZでは、点の座標、線、図形、文字の位置を命令として書き、図をソースコードとして記述する。有限オートマトン、回路、木、グラフの自動配置など、多くの種類の図のためのライブラリが用意されている。

## どこで出てくるか
TikZの図は、TeXの文書の中で、本文と同じ仕組みで組版される。図はテキストとして記述されるため、gitで変更を管理できる。グラフについては、[[Matplotlib|matplotlib]]などのソフトウェアがTikZの形式で図を出力する機能を備えており、[[Beamer|beamer]]もPGFを利用している。

## 関係
- 上位概念: [[LaTeX]]
- 使う / 使われる: [[Beamer]]（PGFを用いる）
- 関連: [[Matplotlib]]

## 出典
- [PGF/TikZ - Wikipedia](https://en.wikipedia.org/wiki/PGF/TikZ)
- [pgf-tikz/pgf - GitHub](https://github.com/pgf-tikz/pgf)
