---
aliases: [ベクトルDB, ベクトルデータベース, Vector DB, VectorDB, Vector Search, ベクトル検索, Similarity Search, 類似検索, Approximate Nearest Neighbor, ANN, 近似最近傍探索, HNSW, Hierarchical Navigable Small World, IVF, IVFFlat, DiskANN, Vamana, Faiss, Milvus, pgvector, Recall, 再現率]
tags: [term]
maps: ["[[Machine Learning Systems]]", "[[Storage]]"]
status: draft
updated: 2026-10-06
---
# Vector Database（ベクトルDB）

> 文章や画像などを[[Embedding|埋め込み]]のベクトルとして格納し、与えたベクトルに近いベクトルを高速に探す（ベクトル検索）ことを主な機能とするデータベースである。

## 概要
ベクトル検索では、問い合わせのベクトルとの距離（ユークリッド距離、内積、コサイン距離など）が小さい、上位k個のベクトルを探す。全てのベクトルとの距離を計算すれば正確な答えが得られるが、ベクトルの数が多いと遅い。そこで、ベクトルDBは索引を作り、正確さを少し犠牲にして高速に探す近似最近傍探索（ANN）を用いる。正確さは、本当の近傍のうち見つけられた割合（再現率、recall）で表し、速度と再現率のトレードオフを索引の種類と設定で調整する。

代表的な索引には次のものがある。HNSW（Hierarchical Navigable Small World）は、ベクトルを点とし、近い点どうしを辺で結んだグラフを多層に重ねた索引であり、上の粗い層から下の細かい層へとたどって近傍を探す。探索の手間はデータの数の対数に比例し、構造は[[Skip List|スキップリスト]]に似ている。IVF（inverted file）は、ベクトルを複数のリストに分け、問い合わせのベクトルに近い一部のリストだけを調べる。例えば、PostgreSQLの拡張であるpgvectorでは、HNSWはIVFFlatより速度と再現率のトレードオフに優れるが、索引の作成が遅く、IVFFlatは作成が速く、メモリの使用量も少ない。

## どこで出てくるか
ベクトルDBは、文書の埋め込みから関係する文書を探して言語モデルに与える[[RAG|検索拡張生成（RAG）]]、推薦、画像の類似検索などに用いられる。専用のベクトルDBには、例えばMilvusがある。既存のデータベースの拡張として、PostgreSQLのpgvectorがあり、他のデータと同じデータベースでベクトルを扱える。類似検索のライブラリとしては、MetaのFaissがあり、一部のアルゴリズムは[[GPU]]で動く。

ストレージの観点では、索引をメモリに置く方式では、扱えるデータの規模がメモリの容量に制約される。DiskANN（NeurIPS 2019）は、グラフの索引Vamanaを[[SSD]]に置くことで、64GBのメモリと安価なSSDを備えた一台の計算機で、10億個のベクトルを扱い、平均3ミリ秒未満の[[Latency|レイテンシ]]で毎秒5,000件以上の問い合わせに応えたと報告している。Milvusも、索引の種類としてDiskANNを選べる。

## 関係
- 前提: [[Embedding]]
- 使う / 使われる: [[GPU]], [[SSD]], [[LLM]]
- 関連: [[Key-Value Store]], [[Latency]], [[B-Tree]]

## 出典
- [Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs (Malkov and Yashunin) - arXiv](https://arxiv.org/abs/1603.09320)
- [pgvector/pgvector - GitHub](https://github.com/pgvector/pgvector)
- [What is Milvus - Milvus documentation](https://milvus.io/docs/overview.md)
- [facebookresearch/faiss - GitHub](https://github.com/facebookresearch/faiss)
- [DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node (Subramanya et al., NeurIPS 2019)](https://papers.nips.cc/paper/9527-rand-nsg-fast-accurate-billion-point-nearest-neighbor-search-on-a-single-node)
