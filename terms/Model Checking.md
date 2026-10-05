---
aliases: [モデル検査, Model Checker, モデル検査器, State Space Explosion, 状態爆発, Counterexample, 反例, SPIN]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-06
---
# Model Checking（モデル検査）

> システムを有限の状態を持つモデルとして記述し、その全ての状態を網羅的に調べて、仕様として与えた性質を満たすかを自動で検査する、形式検証の手法である。

## 概要
モデル検査は1980年代に、システムの性質を時相論理で記述し、有限状態のモデルがそれを満たすかを検査する手法として始まった。その創始と発展の功績により、Clarke、Emerson、Sifakisが2007年のチューリング賞を受けている。

検査する性質には、悪いことが決して起きないという安全性（例えば、二つのサーバが異なる値に合意しない）と、良いことがいつか必ず起きるという活性（例えば、要求がいつか処理される）がある。モデル検査器は、到達しうる全ての状態を調べ、性質が破れる場合には、そこに至るまでの具体的な実行の列を反例として示す。テストでは偶然にしか現れない、まれな実行の順序による誤りを見つけられる点が利点である。一方、状態の数は変数やプロセスの数に対して組合せ的に増える（状態爆発）ため、検査できるのはサーバの台数などを小さく限ったモデルに限られることが多い。

## どこで出てくるか
分散システムでは、メッセージの遅れや故障の組合せによって誤りが起きやすいため、[[Consensus|合意]]のアルゴリズムなどの設計をモデル検査で確かめることが多い。[[TLA+]]の仕様は、モデル検査器TLCで検査できる。[[Raft]]や[[Paxos]]の仕様もTLA+で書かれている。代表的なモデル検査器には、ほかにSPINなどがある。

## 関係
- 使う / 使われる: [[TLA+]]
- 関連: [[Consensus]], [[Raft]], [[Paxos]], [[Linearizability]]

## 出典
- [Model checking - Wikipedia](https://en.wikipedia.org/wiki/Model_checking)
- [tlaplus/Examples - GitHub](https://github.com/tlaplus/Examples)（TLA+によるPaxosなどの仕様）
- [ongardie/raft.tla - GitHub](https://github.com/ongardie/raft.tla)（TLA+によるRaftの仕様）
