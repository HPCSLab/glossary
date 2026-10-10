---
aliases: [paxos, パクソス, Multi-Paxos, Basic Paxos, Proposer, Acceptor, Learner, The Part-Time Parliament, Paxos Made Simple]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-10
---
# Paxos

> Lamportが提案した、故障しうる複数のサーバの間で一つの値に合意するための、古典的な合意アルゴリズムである。

## 概要
Paxosは、Leslie Lamportが1989年に投稿し、1998年に論文 "The Part-Time Parliament" として発表した。架空の古代ギリシャの議会の物語として書かれたこの論文は難解であったため、2001年に平易に説明し直した "Paxos Made Simple" が公開されている。

Paxosの参加者は、値を提案する提案者（proposer）、提案を受け入れるかを決める受理者（acceptor）、決まった値を知る学習者（learner）の役割を持つ。合意は二つの段階で進む。第一段階（prepare/promise）では、提案者が番号付きの提案の準備を受理者に求め、受理者はそれより小さい番号の提案を受け入れないことを約束し、すでに受け入れた値があれば返す。第二段階（accept/accepted）では、提案者が値を送り、受理者の過半数が受け入れれば値が決まる。任意の二つの過半数は必ず重なるため、異なる値が決まることはない。

Paxosは、どのような故障やメッセージの遅れの下でも誤った値が決まらないこと（安全性）を保証するが、非同期のネットワークでは必ず合意に至ること（活性）は保証できない。これは[[Consensus|合意]]の一般的な限界（FLPの不可能性）による。一つの値ではなく、値の列に繰り返し合意するように拡張したものをMulti-Paxosと呼ぶ。

## どこで出てくるか
Paxosは、[[State Machine Replication|状態機械複製]]を実現する合意アルゴリズムとして、GoogleのChubby（[[Distributed Lock Manager|分散ロック]]サービス）や[[Spanner]]（データベース）などで用いられている。理解と実装が難しいことでも知られ、これを改善するために[[Raft]]が提案された。Lamport自身による、[[TLA+]]で記述したPaxosの仕様も公開されている。

## 関係
- 上位概念: [[Consensus]]
- 対比: [[Raft]]（同等の性質を持ち、理解しやすさを重視して設計された）
- 使う / 使われる: [[State Machine Replication]]
- 関連: [[TLA+]], [[Linearizability]]

## 出典
- [Paxos (computer science) - Wikipedia](https://en.wikipedia.org/wiki/Paxos_(computer_science))
- [Paxos Made Simple (Lamport, 2001)](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf)
- [tlaplus/Examples - GitHub](https://github.com/tlaplus/Examples)（TLA+によるPaxosの仕様）
