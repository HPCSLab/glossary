---
aliases: [状態機械複製, ステートマシンレプリケーション, SMR (replication), Replicated State Machine, 複製状態機械, Replicated Log, 複製ログ]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-06
---
# State Machine Replication（状態機械複製）

> 決定的なサービスの複製を複数のサーバで動かし、全ての複製に同じ入力を同じ順序で与えることで、故障に耐えるサービスを作る手法である。

## 概要
状態機械複製は、サービスを状態機械として捉える。状態機械は、状態と入力から次の状態と出力を決める。その遷移が決定的であれば、同じ初期状態から始め、同じ入力を同じ順序で与えた複製は、同じ出力を返し、同じ状態に至る。そこで、サービスの複製を複数のサーバで動かし、全ての複製に同じ順序で入力を与えれば、一部のサーバが故障しても、残りの複製がサービスを続けられる。この手法は、Lamportらの研究を基に、Schneiderが1990年のチュートリアルで体系化した。

この手法の中心的な課題は、全ての複製の間で入力の順序を一致させることであり、その順序を決めるために[[Consensus|合意]]のアルゴリズムが用いられる。多くの実装は、入力を順に追記したログを複製し、合意によって確定したログの内容を各複製が順に適用する。停止する故障（クラッシュ）を F 台まで許すには 2F+1 台の複製が、任意の誤った振る舞いをする故障（ビザンチン故障）を F 台まで許すには 3F+1 台の複製が必要である。

## どこで出てくるか
[[Paxos]]や[[Raft]]は、状態機械複製のログを一致させるための合意アルゴリズムである。分散データベースや、構成情報を保持する協調サービス、分散ストレージの[[Metadata|メタデータ]]の管理など、高い可用性が必要なサービスの多くがこの手法に基づく。Raftの論文や実装を読む際には、合意そのものと、それを用いて状態機械を複製する部分を区別すると理解しやすい。

## 関係
- 上位概念: [[Distributed Systems]]
- 前提: [[Consensus]]
- 使う / 使われる: [[Paxos]], [[Raft]]
- 関連: [[Linearizability]], [[Key-Value Store]]

## 出典
- [State machine replication - Wikipedia](https://en.wikipedia.org/wiki/State_machine_replication)
- [Implementing fault-tolerant services using the state machine approach: a tutorial (Schneider, ACM Computing Surveys 1990)](https://doi.org/10.1145/98163.98167)
