---
aliases: [Google Spanner, Cloud Spanner, TrueTime, External Consistency, 外部一貫性, Commit Wait]
tags: [term]
maps: ["[[Distributed Systems]]", "[[Databases]]"]
status: draft
updated: 2026-10-10
---
# Spanner

> Googleの、世界中のデータセンタにデータを複製しながら、全体として一つの順序に従う分散トランザクションを提供するデータベースである。

## 概要
SpannerはCorbettらが2012年の[[OSDI]]で発表した。データを多数の断片に分け、各断片を[[Paxos]]による[[State Machine Replication|状態機械複製]]で複数のデータセンタに複製する。一つのPaxosのグループ内のトランザクションはそのリーダーが処理し、複数のグループにまたがるトランザクションは、グループのリーダーどうしが[[Two-Phase Commit|二相コミット]]で調整する。各グループがPaxosで複製されているため、二相コミットの参加者が一台の故障で止まることを避けられる。データは版を持ち、コミットの時刻で版が区別される（[[MVCC]]）。

Spannerの中心は外部一貫性である。これは、トランザクションT1のコミットがT2の開始より前に起きたなら、T1のコミットの時刻がT2より小さいことを保証する性質であり、[[Linearizability|線形化可能性]]と同等である。これを世界規模で実現するために、SpannerはTrueTimeという時刻のAPIを用いる。TrueTimeは現在時刻を一点ではなく、真の時刻を必ず含む区間 `[earliest, latest]` として返す。区間の幅（時刻の不確かさ）は、GPSと原子時計を基準とする時刻サーバとの同期によって、通常は数ミリ秒に抑えられている。トランザクションには `TT.now().latest` 以上の時刻を割り当て、その時刻が確実に過ぎたと TrueTime が示すまで結果を公開しない（コミット待ち）。不確かさの分だけ待つことで、時計のずれがあっても時刻の順序が実際の順序と一致する。

この仕組みにより、読み込みだけのトランザクションはロックを取らずに、ある時刻のスナップショットを任意の十分に新しい複製から読める。

## どこで出てくるか
分散データベースと[[Consistency Model|一貫性モデル]]の議論で、世界規模に複製したデータで外部一貫性を持つ分散トランザクションを提供した例として現れる。論文は、これを提供した最初のシステムであるとしている。Spannerは、Googleの広告のバックエンドであるF1が最初の利用者であり、現在はGoogle Cloudのサービスとしても提供されている。Spannerのデータは、Googleの分散ファイルシステムである[[Colossus]]に格納される。

## 関係
- 上位概念: [[Distributed Database]]
- 前提: [[Paxos]], [[Two-Phase Commit]], [[Linearizability]]
- 使う / 使われる: [[Colossus]], [[MVCC]]
- 関連: [[Bigtable]], [[Consistency Model]]

## 出典
- [Spanner: Google's Globally-Distributed Database (Corbett et al., OSDI 2012)](https://research.google/pubs/spanner-googles-globally-distributed-database-2/)
- [Spanner: TrueTime and external consistency - Google Cloud Documentation](https://docs.cloud.google.com/spanner/docs/true-time-external-consistency)
