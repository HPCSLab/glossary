---
aliases: [High Bandwidth Memory, 高バンド幅メモリ, 広帯域メモリ, HBM2, HBM2E, HBM3, HBM3E, HBM4, TSV, Through-Silicon Via]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# HBM（High Bandwidth Memory）

> 複数の[[DRAM]]のチップを垂直に積み重ね、非常に幅の広いインタフェースでプロセッサと接続することで、高い[[Bandwidth|バンド幅]]を得るメモリの規格である。

## 概要
HBMは、2008年頃からAMDで開発が始まり、2013年10月にJEDECによって標準規格として採択された。同年にSK hynixが最初のHBMのチップを製造し、2015年にAMDのFijiが、HBMを用いた最初のGPUとなった。

HBMでは、4、8、12、あるいは16枚のDRAMのチップ（ダイ）を、一枚の論理チップの上に積み重ね、チップを貫通する電極（TSV、through-silicon via）で接続する。この積層したメモリを、シリコンインターポーザなどを介してプロセッサのすぐ近くに置き、1024ビット（HBM4では2048ビット）という非常に幅の広いインタフェースで接続する。これにより、DDR4やGDDR5より高いバンド幅を、より少ない電力と小さな面積で実現する。

HBMは世代を重ねており、積層一つあたりのバンド幅は、HBM2/HBM2Eで最大307GB/s、HBM3/HBM3Eで819〜1,229GB/s、HBM4で最大2,048GB/sに達する。

## どこで出てくるか
HBMは、AIの学習と推論に用いるアクセラレータ、データセンター向けの[[GPU]]など、極めて高いメモリバンド幅を必要とするプロセッサに用いられている。例えば、NVIDIAのH100（SXM版）は80GBのメモリで3.35TB/sのバンド幅を持ち、[[Sirius]]が搭載するAMDのMI300Aは、CPUとGPUで128GBのHBM3を共有する。一方、[[DGX Spark]]のようにLPDDR5xを用いる計算機のメモリバンド幅（273GB/s）は、HBMを用いるデータセンター向けのGPUより大幅に低い。計算機の性能を比較する際には、演算性能だけでなく、メモリの種類とバンド幅も確認する必要がある。

## 関係
- 上位概念: [[Bandwidth]]（HBMはメモリのバンド幅を高めるための技術である）
- 使う / 使われる: [[GPU]], [[Sirius]]
- 対比: [[DGX Spark]]（LPDDR5xを用いる）
- 関連: [[LLM]], [[KV Cache]], [[Little's Law]]

## 出典
- [High Bandwidth Memory - Wikipedia](https://en.wikipedia.org/wiki/High_Bandwidth_Memory)
- [NVIDIA H100 Tensor Core GPU - NVIDIA](https://www.nvidia.com/en-us/data-center/h100/)
- [新型スーパーコンピュータ Sirius (PACS12.0) の運用を開始 - 筑波大学計算科学研究センター](https://www.ccs.tsukuba.ac.jp/release260327/)
- [NVIDIA DGX Spark - NVIDIA](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)
