---
aliases: [MultiRaft, マルチRaft, Raftグループ]
tags: [term]
maps: ["[[Distributed Systems]]", "[[Databases]]"]
status: draft
updated: 2026-10-16
---
# Multi-Raft

> データをキーの範囲で多数の断片に分け、断片ごとに独立した[[Raft]]のグループで複製し、一つのノードがそれら多数のグループを同時に管理する構成である。

## 概要
Raftの一つのグループでは、すべての書き込みがリーダーを経由し、すべての複製が全データを持つ。そのため、一つのグループで扱えるデータの量と書き込みの速さは、一台の計算機の能力を超えられない。そこで、大規模な[[Key-Value Store|キーバリューストア]]や分散データベースは、キーの空間を連続した範囲に分割（シャーディング）し、範囲ごとにRaftのグループを作る。各グループのリーダーは異なるノードに分散させられるので、書き込みの負荷とデータの量を多数のノードに広げられる。各ノードは多数のグループの複製を持ち、あるグループではリーダー、別のグループではフォロワーとなる。このように一つのノードで多数のRaftのグループを管理することをMulti-Raftと呼ぶ。名前は似ているが、Paxosで値の列に[[Consensus|合意]]するMulti-Paxosとは別の概念である。

範囲の単位は、TiKVではRegion、CockroachDBではRangeと呼ぶ。TiKVのRegionは左閉右開の区間 `[StartKey, EndKey)` であり、既定では256 MiBを超えると分割され、小さくなった隣接するRegionは併合される。どのRegionの複製をどのノードに置くかは、PD（Placement Driver）と呼ぶ管理役が、ノード間で偏らないように決める。同じ考え方は、データを断片ごとに[[Paxos]]のグループで複製する[[Spanner]]にも見られる。

多数のグループを動かすと、グループごとのハートビートなどの制御の通信がグループの数に比例して増える。CockroachDBは、同じノードの組の間ではグループの数によらずハートビートを一回にまとめることで、これを抑えている。

## どこで出てくるか
TiKV（TiDBの記憶層）やCockroachDBなど、Raftを用いる分散データベースの設計を読むときに、RegionやRangeの分割・併合・移動として現れる。断片の分け方によっては、一つのトランザクションが複数のグループにまたがるため、グループ間の不可分性を[[Two-Phase Commit|二相コミット]]などで別に確保する必要がある。

## 関係
- 前提: [[Raft]], [[State Machine Replication]]
- 対比: [[Spanner]]（断片ごとにPaxosのグループで複製する）
- 使う / 使われる: [[Key-Value Store]]
- 関連: [[Two-Phase Commit]], [[Consensus]]

## 出典
- [Multi-Raft - TiKV](https://tikv.org/deep-dive/scalability/multi-raft/)
- [TiDB Storage - TiDB Docs](https://docs.pingcap.com/tidb/stable/tidb-storage/)
- [Replication Layer - CockroachDB Docs](https://docs.cockroachlabs.com/docs/stable/architecture/replication-layer)
- [Scaling Raft (Ben Darnell, 2015) - Cockroach Labs](https://www.cockroachlabs.com/blog/scaling-raft/)
