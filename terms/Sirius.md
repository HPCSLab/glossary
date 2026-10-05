---
aliases: [PACS12.0, PACS 12.0, シリウス, 筑波大学 Sirius]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# Sirius（PACS12.0）

> 筑波大学計算科学研究センターが2026年3月に運用を開始した、AMD Instinct MI300A APUを用いるユニファイドメモリ型のスーパーコンピュータである。

## 概要
Siriusは、筑波大学計算科学研究センターが開発してきたPACSシリーズの第12世代（PACS12.0）にあたり、2026年3月27日に運用を開始した。国立大学に導入されたスーパーコンピュータとして初めて、AMDのAPUを採用している。

各[[Compute Node|計算ノード]]は、4基のAMD Instinct MI300A（[[APU]]）を備える。MI300Aは、CPU（24コアのEPYC Zen 4）、[[GPU]]（CDNA3）、128GBのHBM3（[[HBM|高バンド幅メモリ]]）を一つのパッケージに統合したAPUであり、CPUとGPUが同じメモリを共有するため、両者の間のデータの転送が不要となる。ノードあたりのHBM3の容量は512GB、倍精度の理論ピーク性能は496TFlopsであり、各ノードには約4TBの[[NVMe]] SSDが搭載されている。システムは24ノードからなり、全体の倍精度の理論ピーク性能は11.9PFlopsである。各ノードは400Gbpsの[[InfiniBand]] NDRを4本（計1.6Tbps）で接続され、5.2PBの[[Parallel File System|並列ファイルシステム]]を持つ。既存の[[Pegasus]]ともInfiniBandで接続されている。

## どこで出てくるか
Siriusの特徴は、CPUとGPUが高バンド幅のメモリを共有するユニファイドメモリの構成である。CPUとGPUのメモリが分かれた構成では、両者の間でデータを転送する必要がある（[[CUDA]]を参照）のに対し、Siriusではこの転送が不要となる。学際共同利用、産業利用、HPCIの制度を通じて利用できる。

## 関係
- 使う / 使われる: [[GPU]], [[InfiniBand]], [[NVMe]], [[Parallel File System]]
- 対比: [[Pegasus]]（同じセンターの、永続メモリを用いるシステム）, [[Fugaku]]
- 関連: [[APU]], [[CUDA]], [[Compute Node]]

## 出典
- [新型スーパーコンピュータ Sirius (PACS12.0) の運用を開始 - 筑波大学計算科学研究センター](https://www.ccs.tsukuba.ac.jp/release260327/)
- [スーパーコンピュータ - 筑波大学計算科学研究センター](https://www.ccs.tsukuba.ac.jp/supercomputer/)
- [Supercomputers - Center for Computational Sciences, University of Tsukuba](https://www.ccs.tsukuba.ac.jp/eng/supercomputers/)
