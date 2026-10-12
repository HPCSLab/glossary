---
aliases: [Sirius DB, sirius-db, Sirius（DuckDB）]
tags: [term]
maps: ["[[Databases]]"]
status: draft
updated: 2026-10-13
---
# Sirius（GPUのSQLエンジン）

> [[GPU]]を主な実行装置とするオープンソースのSQLエンジンであり、[[DuckDB]]の拡張として組み込むと、利用者のSQLを変えずに問い合わせをGPUで実行する。

同名の筑波大学のスーパーコンピュータは[[Sirius]]を参照。

## 概要
Siriusは、ウィスコンシン大学マディソン校が中心となり、NVIDIAの支援を受けて開発しているSQLの実行エンジンである。SQLの構文解析や最適化、利用者とのやり取りは既存のデータベースに任せ、最適化後の実行計画を、データベースの間で実行計画を受け渡すための標準形式Substraitで受け取って実行する。こうすることで、既存のデータベースの使い勝手を保ったまま、実行の部分だけをGPUに置き換えられる。結合や集約などの関係演算は、NVIDIAのGPU向けの[[pandas|データフレーム]]のライブラリであるcuDFを用いて実装されている。

DuckDBに組み込んだ場合、DuckDBの問い合わせは最適化の段階で横取りされ、GPUで実行される。Siriusが対応していない演算を含む問い合わせは、自動的にDuckDBのCPUの実行に戻される。データがGPUのメモリに収まらない場合に備えて、GPUのメモリ、ホストのメモリ、ディスクの三階層でデータを管理し、データを分割して処理し、あふれた分を下の階層に退避する。データの入力には、[[Parquet]]のファイルとDuckDBの形式のファイルが使える。

## どこで出てくるか
GPUによるデータ分析の性能を論じる場面で現れる。Siriusを提案した論文「Rethinking Analytical Processing in the GPU Era」はCIDR 2026で発表された。この論文は、GPUのメモリの大容量化、GPUとの間の相互接続とI/Oの高速化、cuDFなどのライブラリの成熟によって、GPUを分析処理に用いる障壁が取り除かれたと主張する。単一ノードのDuckDBに組み込んだ場合、分析処理のベンチマークであるTPC-HとClickBenchで、費用あたりの性能がそれぞれ8.3倍と7.4倍になったと報告している。2025年12月には、GH200 Grace Hopper Superchipを用いてClickBenchの記録を更新したとNVIDIAが発表している。

利用するにはNVIDIAのGPU（Turing世代以降）と[[CUDA]]が必要であり、ファイルの読み込みには[[io_uring]]と、`O_DIRECT` による[[Direct I/O]]に対応したファイルシステムを要する。

## 関係
- 前提: [[CUDA]]
- 対比: [[DuckDB]]（同じSQLを、DuckDB自身はCPUで列指向・ベクトル化して実行する）
- 使う / 使われる: [[GPU]], [[Parquet]]

## 出典
- [sirius-db/sirius - GitHub](https://github.com/sirius-db/sirius)
- [Rethinking Analytical Processing in the GPU Era - CIDR 2026](https://vldb.org/cidrdb/2026/rethinking-analytical-processing-in-the-gpu-era.html)
- [Rethinking Analytical Processing in the GPU Era - arXiv](https://arxiv.org/abs/2508.04701)
- [NVIDIA GPU-Accelerated Sirius Achieves Record-Setting ClickBench Record - NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-gpu-accelerated-sirius-achieves-record-setting-clickbench-record/)
