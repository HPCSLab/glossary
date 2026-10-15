---
aliases: [Vamana, Fresh-DiskANN, Filtered-DiskANN]
tags: [term]
maps: ["[[Databases]]", "[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-16
---
# DiskANN

> グラフ型の索引を[[SSD]]に置き、一台の計算機で10億個規模のベクトルの近似最近傍探索を行うための、Microsoft Researchが提案した索引と探索の手法である。

## 概要
[[Vector Database|ベクトル検索]]の代表的な索引であるHNSWなどのグラフ型の索引は、索引とベクトルを[[DRAM|メモリ]]に置くことを前提としており、扱えるデータの規模がメモリの容量に制約される。索引を単純にSSDへ移すと、1回の問い合わせで数百回のランダムな読み込みが生じ、一回に数百マイクロ秒かかるSSDの読み込みが積み重なって、数ミリ秒という要求を満たせない。DiskANN（NeurIPS 2019）は、SSDへのランダムな読み込みを1回の問い合わせあたり数十回、SSDとの往復を10回未満に抑えることを目標に設計された。

中核は、Vamanaと呼ぶグラフの構築法である。Vamanaは、各点の辺を選ぶ際にパラメータ α（α ≥ 1）を用いて、近い点だけでなく遠い点への辺も残すことで、グラフの直径を小さくし、探索で目的の点に至るまでの段数を減らす。HNSWなどでは、この α に相当する値が暗黙に1に固定されている。

DiskANNは、データの配置と探索の手順をSSDに合わせている。メモリには、直積量子化（product quantization）で圧縮した全ベクトルだけを置き、SSDには、グラフの辺と圧縮前のベクトルを点ごとに並べて置く。探索では、圧縮したベクトルで距離を見積もりながら、有望な数個（W 個）の点の近傍をまとめて一度に読み込む（beam search）。SSDから少数のセクタを読む時間は一つのセクタを読む時間とほぼ同じであるため、これで往復の回数が減る。近傍を読む際には同じセクタにある圧縮前のベクトルも得られるので、追加の読み込みなしに正確な距離で最終的な順位を付け直せる。論文は、64GBのメモリと安価なSSDを備えた一台の計算機で、10億個のベクトルに対し、95%以上の1-recall@1、平均3ミリ秒未満の[[Latency|レイテンシ]]で、毎秒5,000件以上の問い合わせに応えたと報告している。

## どこで出てくるか
ベクトル検索の論文やベンチマークで、メモリに収まらない規模のデータを扱う手法の基準として、HNSWと並んで比較対象に挙がる。実装は、Microsoftが[[GitHub]]でMITライセンスの下に公開しており、現在の主な開発は[[Rust]]で行われ、以前のC++の実装は別のブランチに残されている。その後、更新を受け付けるFresh-DiskANNや、属性による絞り込みを伴う検索を扱うFiltered-DiskANNなどの派生が提案されている。データベースへの組み込みも進んでおり、Milvusは索引の種類としてDiskANNを選べ、Azure Cosmos DBのベクトル検索（VLDB 2025）や[[Garnet]]のベクトル検索もDiskANNを用いている。

## 関係
- 上位概念: [[Vector Database]]（近似最近傍探索の索引の一つ）
- 前提: [[Embedding]], [[SSD]]
- 関連: [[Latency]], [[Garnet]]

## 出典
- [DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node (Subramanya et al., NeurIPS 2019)](https://papers.nips.cc/paper/9527-rand-nsg-fast-accurate-billion-point-nearest-neighbor-search-on-a-single-node)
- [microsoft/DiskANN - GitHub](https://github.com/microsoft/DiskANN)
- [What is Milvus - Milvus documentation](https://milvus.io/docs/overview.md)
