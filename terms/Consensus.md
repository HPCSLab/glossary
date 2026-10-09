---
aliases: [合意, 合意問題, 分散合意, Consensus Problem, Distributed Consensus, FLP, FLP Impossibility, FLPの不可能性, Byzantine Fault, ビザンチン故障, Quorum, クォーラム, 過半数]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-10
---
# Consensus（合意）

> 故障しうる複数のプロセスが、それぞれ提案した値の中から一つの値について、全員が同じ決定に至る問題である。

## 概要
合意問題では、各プロセスが値を提案し、最終的に一つの値が選ばれる。満たすべき安全性は、提案された値のみが選ばれること、選ばれる値は一つだけであること、実際に選ばれていない値を選ばれたと認識するプロセスがないことである。加えて、いずれ何らかの値が選ばれ、各プロセスがそれを知ることができる、という活性も求められる。一見単純であるが、メッセージの遅延や喪失、プロセスの停止がある環境でこれを保証することは難しい。

合意は、分散システムの耐故障性の基礎である。複数の複製に同じ命令を同じ順序で適用して状態を一致させる[[State Machine Replication|状態機械複製]]は、「次に実行する命令は何か」についての合意を繰り返すことで実現される。リーダーの選出、[[Distributed Lock Manager|分散ロック]]、クラスタの構成情報の管理も、合意によって行われる。

合意には、理論上の限界が知られている。1985年にFischer、Lynch、Patersonが示したFLPの不可能性定理は、メッセージの遅延に上限のない完全な非同期システムでは、ただ一つのプロセスが停止する可能性があるだけで、常に有限時間で合意に至ることを保証するアルゴリズムは存在しないことを示した。停止したプロセスと、単に応答が遅いプロセスを区別できないためである。そのため、実用的なアルゴリズムは、安全性は常に保証しつつ、活性については「ネットワークがいずれ十分に安定する」などの仮定の下でのみ保証する。

故障の種類によって、必要な台数も異なる。プロセスが停止するだけの故障（クラッシュ故障）を想定する場合、$f$ 台の故障に耐えるには $2f + 1$ 台が必要であり、過半数（クォーラム）の合意をもって決定とする。任意の二つの過半数は必ず一台以上を共有するため、矛盾する二つの決定が同時に成立しない。故障したプロセスが嘘を含む任意の振る舞いをしうるビザンチン故障を想定する場合は、LamportらがByzantine Generals Problemとして定式化したとおり、$3f + 1$ 台以上が必要となる。

## どこで出てくるか
代表的なアルゴリズムは、Lamportの[[Paxos]]と、理解しやすさを重視した[[Raft]]である。etcd、ZooKeeper、Consulなどの構成管理・協調サービス、分散データベース、[[Ceph]]のモニタなどが、内部で合意を用いている。これらが3台や5台の奇数台で構成されるのは、過半数による決定の性質による。例えば、4台の構成は3台の構成と同じく1台の故障にしか耐えられない。

合意は、すべての決定がリーダーとの往復と過半数への書き込みを要するため、[[Latency|レイテンシ]]と処理能力の面で高価である。そのため、大規模なストレージシステムでは、データ本体の経路には合意を用いず、[[Metadata|メタデータ]]や構成情報のような小さく重要な情報の管理にのみ合意を用いる設計が一般的である。合意に基づくシステムは、[[Linearizability|線形化可能]]なサービスを提供する基盤となる。アルゴリズムの設計や変形の正しさの確認には、[[TLA+]]による仕様記述とモデル検査が用いられる。

## 関係
- 使う / 使われる: [[Paxos]], [[Raft]]（合意アルゴリズム）, [[State Machine Replication]]
- 関連: [[Linearizability]], [[Ceph]], [[TLA+]], [[Consistency Model]]

## 出典
- [Paxos Made Simple (Lamport, 2001)](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf)
- [Impossibility of Distributed Consensus with One Faulty Process (Fischer, Lynch, and Paterson, J. ACM, 1985)](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf)
- [The Byzantine Generals Problem (Lamport, Shostak, and Pease, ACM TOPLAS, 1982)](https://lamport.azurewebsites.net/pubs/byz.pdf)
- [The Raft Consensus Algorithm](https://raft.github.io/)
