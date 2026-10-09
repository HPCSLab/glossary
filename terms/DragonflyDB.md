---
aliases: [Dragonfly (KVS), Dragonfly KVS, dragonflydb, Dragonfly in-memory data store, Dashtable, VLL]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-09
---
# DragonflyDB（Dragonfly）

> RedisとMemcachedのAPIに対応した、多数のスレッドで動くインメモリのデータストア（[[Key-Value Store|キーバリューストア]]）であり、製品名はDragonflyである。

## 概要
Dragonflyは、DragonflyDB社が開発し、既存のRedisとMemcachedのクライアントからそのまま使える。Dragonflyは、キーの空間を複数のスレッドに分け、各スレッドが自分の担当の部分（シャード）だけを管理する、資源を共有しない（shared-nothing）設計をとる。複数のキーにまたがる操作の不可分性は、主記憶のデータベースのためのロックの管理の手法VLLに基づき、[[Mutex|ミューテックス]]やスピンロックを用いずに実現する。中心のハッシュ表（Dashtable）は、永続メモリのためのハッシュ法Dashの論文に基づく。また、`fork` を用いないスナップショットの方式を持ち、スナップショットの間にメモリの使用量がほとんど増えないとしている。

ライセンスはBusiness Source License 1.1であり、インメモリのデータストアの製品やサービスとして提供することは許されない。2030年11月1日にApache License 2.0に切り替わると定められている。

## どこで出てくるか
Redisと互換のキャッシュストアの性能の比較で、Redisや[[Garnet]]などとともに現れる。READMEでは、AWSのc6gn.16xlargeのインスタンスで、一つのRedisのプロセスの25倍の処理能力（毎秒380万件以上の問い合わせ）を示したとしている。同じ名前のネットワークのトポロジ（[[Dragonfly Topology]]）とは別のものである。

## 関係
- 上位概念: [[Key-Value Store]]
- 対比: [[Garnet]]（同じくRedisと互換のキャッシュストア）
- 関連: [[Thread]], [[Snapshot]], [[Copy-on-Write]]

## 出典
- [dragonflydb/dragonfly - GitHub](https://github.com/dragonflydb/dragonfly)
- [LICENSE.md - dragonflydb/dragonfly](https://github.com/dragonflydb/dragonfly/blob/main/LICENSE.md)
