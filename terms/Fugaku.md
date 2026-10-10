---
aliases: [富岳, スーパーコンピュータ富岳, Supercomputer Fugaku, A64FX, Tofu, TofuD, Tofu interconnect D]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# Fugaku（富岳）

> [[RIKEN|理化学研究所]]と富士通が開発し、理化学研究所計算科学研究センター（神戸）に設置されたスーパーコンピュータである。

## 概要
富岳は、スーパーコンピュータ「京」の後継として2014年に開発が始まり、2019年12月から2020年5月にかけて設置され、2021年3月に共用を開始した。158,976台の計算ノードからなり、各ノードは富士通が開発したArmアーキテクチャのプロセッサA64FXを備える。計算ノードは、6次元のメッシュ/トーラス構造を持つ富士通のインターコネクトTofu interconnect D（TofuD）で接続されている。

富岳は、2020年6月から2021年11月まで、[[TOP500]]で世界一の座を保ち、Armアーキテクチャの計算機として初めてTOP500の首位となった。2020年の増強後の[[LINPACK]]（HPL）の性能は442PFLOPSである。2022年5月に、米国の[[ORNL|Frontier]]に首位を譲った。

ストレージは三つの階層からなる。第1階層は計算ノードの近くに置かれたSSDによる高速な記憶で、[[LLIO]]が管理する。第2階層は[[Lustre]]を基にしたファイルシステム[[FEFS]]による約150PBの共有の領域、第3階層はクラウドのストレージサービスである。

## どこで出てくるか
I/Oの観点では、計算ノードの近くのSSDを用いる第1階層と、Lustreを基にした第2階層からなる階層的なストレージの構成が特徴である。富岳でI/Oを行うアプリケーションは、第2階層を直接用いるか、LLIOが提供するキャッシュや一時領域を用いるかを選ぶ。

## 関係
- 使う / 使われる: [[LLIO]], [[Lustre]]（第1階層と第2階層のストレージ）
- 関連: [[TOP500]], [[LINPACK]], [[HPCI]]

## 出典
- [Fugaku (supercomputer) - Wikipedia](https://en.wikipedia.org/wiki/Fugaku_(supercomputer))
- [Status of Lustre-Based Filesystem at the Supercomputer Fugaku (LUG 2020) - Lustre Wiki](https://wiki.lustre.org/images/c/cc/LUG2020-Lustre_File_System_at_Fugaku-Tsujita.pdf)
