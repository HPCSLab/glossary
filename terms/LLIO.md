---
aliases: [Lightweight Layered IO Accelerator, Lightweight Layered I/O Accelerator, FEFS, Fujitsu Exabyte File System, 第1階層ストレージ, 第2階層ストレージ]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# LLIO

> スーパーコンピュータ[[Fugaku|富岳]]の第1階層ストレージとして、計算ノードの近くに置いたSSDを用いて、第2階層のファイルシステムのキャッシュと、ジョブ用の一時的なファイルシステムを提供する仕組みである。正式名称は Lightweight Layered IO Accelerator である。

## 概要
富岳のストレージは三つの階層からなる。第1階層は、計算ノードの近くに置かれたSSDによる高速な記憶であり、LLIOがこれを管理する。第2階層は、[[Lustre]]を基に富士通が拡張したファイルシステムFEFS（Fujitsu Exabyte File System）による、容量約150PBの共有の領域である。第3階層は、クラウドのストレージサービスである。

第1階層では、16台の計算ノードのうち1台が、約1.6TBのSSDを持つ計算兼ストレージI/Oノードとなっている。LLIOは、このSSDを用いて、ジョブに三種類の領域を提供する。一つ目は、第2階層のファイルシステムに対する透過的なキャッシュであり、書き込まれたデータは背後で第2階層へ書き戻される。二つ目は、各計算ノードから使う一時的なローカルの領域である。三つ目は、一つのジョブの全計算ノードで共有する一時的な領域である。

## どこで出てくるか
富岳でジョブを実行する際には、第2階層の[[Parallel File System|並列ファイルシステム]]であるFEFSを直接用いるか、LLIOが提供するキャッシュや一時領域を用いるかを選ぶことになる。計算ノードの近くの記憶装置を、ジョブ単位の一時的なファイルシステムとして用いるという点で、[[GekkoFS]]、[[CHFS]]、[[UnifyFS]]などの[[Ad Hoc File System|アドホックファイルシステム]]と共通する。

## 関係
- 上位概念: [[Fugaku]]（LLIOを備えるスーパーコンピュータ）
- 使う / 使われる: [[Lustre]]（FEFSの基盤）, [[SSD]]
- 関連: [[GekkoFS]], [[CHFS]], [[UnifyFS]], [[Parallel File System]]

## 出典
- [Status of Lustre-Based Filesystem at the Supercomputer Fugaku (LUG 2020) - Lustre Wiki](https://wiki.lustre.org/images/c/cc/LUG2020-Lustre_File_System_at_Fugaku-Tsujita.pdf)
- [Fugaku (supercomputer) - Wikipedia](https://en.wikipedia.org/wiki/Fugaku_(supercomputer))
