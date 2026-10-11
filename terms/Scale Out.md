---
aliases: [スケールアウト, Scale-Out, Scale-out, Horizontal Scaling, 水平スケーリング, 水平スケール, Scale In, スケールイン, Scale-Out Network, スケールアウトネットワーク, Scale-Out Storage, スケールアウトストレージ]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-11
---
# Scale Out（スケールアウト）

> 計算機（ノード）の台数を増やし、仕事を分担させることで、システムの処理能力を高めることである。

## 概要
一台の計算機を大きくする[[Scale Up|スケールアップ]]には物理的な上限があり、大きな計算機ほど性能あたりの価格が高い。スケールアウトは、比較的小さな計算機を多数並べ、ネットワークで結んで仕事を分担させることで、この上限を超える。台数を増やすほど処理能力を伸ばせ、一部の計算機が故障しても、データを複製しておけば残りの計算機で動き続けられる。その代わり、プログラムは計算機をまたいで仕事とデータを分割し、[[MPI]]などで通信しなければならない。台数が増えるほど、通信や同期の費用、[[Amdahl's Law|逐次部分]]、一貫性を保つための協調が[[Bottleneck|ボトルネック]]になりやすく、管理する計算機も増える。

## どこで出てくるか
スーパーコンピュータは、多数の[[Compute Node|計算ノード]]を高速なネットワークで結んだスケールアウトの構成である。並列プログラムが台数を増やしたときに性能が伸びるかは、[[Strong Scaling|強スケーリング]]と[[Weak Scaling|弱スケーリング]]で評価する。ストレージでは、サーバを足すほど容量と性能が増える構成をスケールアウトストレージと呼び、[[Parallel File System|並列ファイルシステム]]や[[Ceph]]がこれにあたる。データベースでは、データを複数のサーバに分割して置くことで書き込みの負荷を分散する。

近年の[[GPU]]クラスタでは、[[NVLink]]で密に結んだGPUの単位（スケールアップのネットワーク）どうしを、[[InfiniBand]]やEthernetで結ぶ接続をスケールアウトのネットワークと呼ぶ。

## 関係
- 対比: [[Scale Up]]（一台を増強して処理能力を高める）
- 使う / 使われる: [[Compute Node]], [[Parallel File System]], [[Ceph]]
- 関連: [[Strong Scaling]], [[Weak Scaling]], [[Amdahl's Law]], [[Bottleneck]], [[InfiniBand]]

## 出典
- [Scale-up x Scale-out: A Case Study using Nutch/Lucene (Michael et al., SMTPS 2007) - IBM Research](https://research.ibm.com/publications/scale-up-x-scale-out-a-case-study-using-nutchlucene)
- [Scalability - Wikipedia](https://en.wikipedia.org/wiki/Scalability)
- [NVLink & NVLink Switch - NVIDIA](https://www.nvidia.com/en-us/data-center/nvlink/)
