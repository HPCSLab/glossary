---
aliases: [Raft Consensus Algorithm, ラフト, Leader Election, リーダー選出, Log Replication, ログ複製, RequestVote, AppendEntries]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-06
---
# Raft

> 複製されたログを複数のサーバ間で一致させるための[[Consensus|合意]]アルゴリズムであり、理解しやすさを主な設計目標とする。

## 概要
RaftはDiego OngaroとJohn Ousterhoutが提案し、2014年のUSENIX ATCで発表された（最優秀論文賞）。それまで標準的であったPaxosは、正しいものの理解と実装が難しいことで知られていた。Raftは、Paxos（multi-Paxos）と同等の耐故障性と効率を持ちながら、問題をリーダー選出、ログ複製、安全性の三つの部分問題に分解することで、理解しやすくした。

Raftは、[[State Machine Replication|状態機械複製]]を実現するために用いられる。クライアントからの命令を順にログに追記し、全サーバが同じ順序で同じ命令を適用すれば、各サーバの状態は一致する。Raftは、このログの内容と順序を全サーバで一致させる。過半数のサーバが稼働して互いに通信できる限り動作を続けられ、例えば5台の構成では2台が故障しても動作する。

各サーバは、フォロワー、候補者、リーダーのいずれかの状態にある。時間は任期（term）と呼ばれる連番の期間に区切られ、各任期には高々一人のリーダーが存在する。フォロワーは、一定時間リーダーからの通信がないと候補者となり、任期を一つ進めて他のサーバに `RequestVote` で投票を求める。過半数の票を得た候補者がリーダーとなる。複数の候補者が票を分け合って選出が長引くことを避けるため、待ち時間（選挙タイムアウト）は一定の範囲（例えば150〜300ミリ秒）から無作為に選ぶ。

リーダーは、クライアントからの命令を自身のログに追記し、`AppendEntries` で他のサーバに複製する。その項目が過半数のサーバに記録された時点で、項目はコミットされたとみなされ、状態機械に適用してよい。ただし、リーダーがこの数え方でコミットを判断できるのは自身の任期に作成した項目に限られ、それ以前の任期の項目は、自身の任期の項目がコミットされることで間接的にコミットされる。また、投票の際には、自分より古いログを持つ候補者には投票しない。これらの規則により、コミットされた項目は以後のすべてのリーダーのログに含まれることが保証される。論文は、これを含む五つの安全性の性質（一任期に高々一人のリーダー、ログの一致、リーダーの完全性、状態機械の安全性など）を示している。

## どこで出てくるか
Raftは、etcd、Consul、CockroachDB、TiKVなど、多くの分散データベースや構成管理システムの中核として実装されている。分散ストレージの研究では、メタデータの複製や構成情報の管理にRaftを用いる設計がよく見られる。大学の分散システムの講義でも、Raftの実装が定番の課題となっている。

Raftは、論文の図に示された規則を一つでも省くと、特定の故障の組み合わせでのみ現れる誤りを生じやすい。上記の、以前の任期の項目を直接コミットしてはならないという規則は、その代表例である。そのため、実装や変形を検討する際には、論文の規則を正確に守るとともに、[[TLA+]]による仕様（原論文に付属する）を参照し、モデル検査で確かめることが有効である。実用上は、クラスタの構成変更やログの肥大化を防ぐスナップショットの扱いも重要な論点となる。

## 関係
- 上位概念: [[Consensus]]
- 前提: [[State Machine Replication]]
- 対比: [[Paxos]]（同等の性質を持つが、理解が難しい）
- 使う / 使われる: [[TLA+]]（仕様の記述と検査）
- 関連: [[Linearizability]]

## 出典
- [The Raft Consensus Algorithm](https://raft.github.io/)
- [In Search of an Understandable Consensus Algorithm - USENIX ATC 2014](https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro)
- [In Search of an Understandable Consensus Algorithm (Extended Version)](https://raft.github.io/raft.pdf)
- [raft.tla - GitHub](https://github.com/ongardie/raft.tla)
