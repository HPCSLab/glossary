---
aliases: [AMD APU, Accelerated Processing Unit, MI300A, AMD Instinct MI300A, Unified Memory, ユニファイドメモリ, HSA, Heterogeneous System Architecture, Zero-copy]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-06
---
# APU（AMD APU）

> AMDが開発する、汎用のCPUとGPUを一つのチップに統合したプロセッサであり、CPUとGPUが同じメモリを共有できる。正式には Accelerated Processing Unit と呼ばれる。

## 概要
APUは、AMDが2006年にグラフィックスのメーカーATIを買収した後に始めたFusionと呼ばれる計画から生まれた。最初の世代は2011年1月に発表され、高性能向けのLlanoと低消費電力向けのBrazosの二系統が登場した。いずれも、AMD64の汎用のCPUと、統合された[[GPU]]を一つのチップに載せたものである。

APUの重要な特徴は、CPUとGPUによるメモリの共有である。2014年のKaveri以降のAPUでは、ヘテロジニアス・システム・アーキテクチャ（HSA）によって、CPUとGPUが同じメモリのアドレス空間にアクセスでき、ポインタをそのままCPUとGPUの間で受け渡せる。そのため、CPUとGPUのメモリの間でデータを複製する必要がない（zero-copy）。CPUとGPUが別々のメモリを持ち、両者の間でデータを転送する必要がある構成（[[CUDA]]を参照）とは対照的である。

APUは、モバイル、デスクトップから、データセンターまでの各分野で開発が続けられている。データセンター向けのAMD Instinct MI300Aは、CPU（24コアのEPYC Zen 4）、GPU（CDNA3）、128GBの[[HBM]]（HBM3）を一つのパッケージに統合しており、CPUとGPUがこの高バンド幅のメモリを共有する。

## どこで出てくるか
MI300Aは、大規模なスーパーコンピュータに採用されている。米国ローレンス・リバモア国立研究所のEl Capitanは、MI300Aを搭載し、[[LINPACK]]の性能1,809PFlop/sで、2024年11月から2025年6月まで[[TOP500]]の首位であった。国内では、筑波大学計算科学研究センターの[[Sirius]]が、各ノードに4基のMI300Aを搭載し、国立大学のスーパーコンピュータとして初めてAMDのAPUを採用した。Siriusの発表は、MI300AによってCPUとGPUの間のメモリの転送が不要になることを、その特徴として挙げている。

## 関係
- 使う / 使われる: [[GPU]], [[HBM]]
- 対比: [[CUDA]]（CPUとGPUのメモリが分かれた構成でのプログラミング）, [[DGX Spark]]（同じくCPUとGPUがメモリを共有する）
- 関連: [[Sirius]], [[TOP500]], [[Virtual Memory]]

## 出典
- [AMD APU - Wikipedia](https://en.wikipedia.org/wiki/AMD_APU)
- [El Capitan - TOP500](https://top500.org/system/180307/)
- [新型スーパーコンピュータ Sirius (PACS12.0) の運用を開始 - 筑波大学計算科学研究センター](https://www.ccs.tsukuba.ac.jp/release260327/)
