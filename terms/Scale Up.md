---
aliases: [スケールアップ, Scale-Up, Scale-up, Vertical Scaling, 垂直スケーリング, 垂直スケール, Scale Down, スケールダウン, Scale-Up Network, スケールアップネットワーク]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-11
---
# Scale Up（スケールアップ）

> 一台の計算機のCPU、メモリ、記憶装置などを増強したり、より大きな計算機に置き換えたりして、システムの処理能力を高めることである。

## 概要
処理能力を高める方法は、一台を大きくするスケールアップと、台数を増やす[[Scale Out|スケールアウト]]に大別される。スケールアップでは、プログラムは一台の計算機の中で動き続けるため、共有メモリの上の[[Thread|スレッド]]並列のままで済み、ネットワーク越しの通信や、[[Consensus|合意]]・[[Two-Phase Commit|分散コミット]]のような分散システムに特有の協調が要らない。管理する計算機の台数も増えない。一方で、一台に載せられるCPUやメモリの量には物理的な上限があり、大きな計算機ほど性能あたりの価格が高くなる。また、一台が故障すればシステム全体が止まる。

## どこで出てくるか
データベースやサーバの設計で、負荷の増加にどう対応するかを議論するときに、スケールアウトと対で現れる。IBMのMichaelらは2007年に、大きな共有メモリの計算機（SMP）によるスケールアップと、小さな計算機のクラスタによるスケールアウトを検索エンジンで比較し、スケールアウトが性能あたりの価格で優れる一方、管理の複雑さが増すことを報告している。

近年の[[GPU]]クラスタでは、この語はネットワークの階層の名前としても使われる。[[NVLink]]のように、ラック程度の範囲の多数のGPUを高い[[Bandwidth|帯域]]で密に結んで一つの大きな計算資源として扱うための接続をスケールアップのネットワークと呼び、それらの単位どうしを[[InfiniBand]]やEthernetで結ぶ接続をスケールアウトのネットワークと呼ぶ。NVIDIAは、NVLinkとNVLink Switchをスケールアップのネットワークと位置付け、NVL72では72基のGPUを一つのNVLinkのドメインに収めている。

## 関係
- 対比: [[Scale Out]]（台数を増やして処理能力を高める）
- 関連: [[NVLink]], [[NUMA]], [[Bottleneck]], [[Strong Scaling]]

## 出典
- [Scale-up x Scale-out: A Case Study using Nutch/Lucene (Michael et al., SMTPS 2007) - IBM Research](https://research.ibm.com/publications/scale-up-x-scale-out-a-case-study-using-nutchlucene)
- [Scalability - Wikipedia](https://en.wikipedia.org/wiki/Scalability)
- [NVLink & NVLink Switch - NVIDIA](https://www.nvidia.com/en-us/data-center/nvlink/)
