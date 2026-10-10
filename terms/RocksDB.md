---
aliases: [rocksdb, Memtable, メムテーブル, SST File, SSTファイル, SSTable, Column Family, カラムファミリ, Universal Compaction, FIFO Compaction, Merge Operator]
tags: [term]
maps: ["[[Databases]]"]
status: draft
updated: 2026-10-10
---
# RocksDB

> Facebook（現Meta）が開発した、アプリケーションに組み込んで用いる永続的な[[Key-Value Store|キーバリューストア]]のライブラリであり、[[LSM-Tree|LSM木]]に基づき、[[SSD]]などの高速な記憶装置に向けて設計されている。

## 概要
RocksDBは、FacebookのDatabase Engineeringのチームが、GoogleのLevelDBを基に開発した。GPLv2とApache 2.0の二つのライセンスで公開されている。

データは、LSM木の構造で管理される。書き込みは、まず[[Crash Consistency|クラッシュ]]に備えて先行書き込みログ（WAL）に記録され、主記憶上の表（memtable）に入る。memtableが一定の大きさに達すると、キーの順に並べた不変のファイル（SSTファイル）として記憶装置に書き出される。SSTファイルは複数の段（レベル）に整理され、背後で動くコンパクション（併合）が古いデータを整理する。コンパクションの方式には、記憶領域の効率を重視するLevel、書き込みの負担を抑えるUniversal、キャッシュのような用途に向くFIFOがある。

RocksDBは、書き込みの増幅（write amplification）、読み込みの増幅、領域の増幅の三つの間のトレードオフを、設定によって調整できるように設計されている。読み込みを速くするために、SSTファイルのブロックをキャッシュするブロックキャッシュと、キーがSSTファイルに含まれないことを素早く判定する[[Bloom Filter|ブルームフィルタ]]を用いる。操作には、キーの取得、追加、削除のほか、キーの範囲を順にたどるイテレータ、複数の書き込みを不可分に行うバッチ、読み出しと更新を一度に行うMerge（merge operator）があり、一つのデータベースを複数の論理的な区画（column family）に分けることもできる。

## どこで出てくるか
RocksDBは、他のシステムに組み込まれて、その記憶エンジンとして用いられる。例えば、[[GekkoFS]]は、各ノードの[[Metadata|メタデータ]]をRocksDBに格納する。RocksDBの元になったLevelDBは、[[IndexFS]]がメタデータの格納に用いている。

増幅のトレードオフが設定で変わるため、RocksDBを用いた性能を評価する際には、コンパクションの方式などの設定を明記する。

## 関係
- 上位概念: [[Key-Value Store]]
- 使う / 使われる: [[LSM-Tree]], [[Bloom Filter]], [[SSD]], [[GekkoFS]]
- 関連: [[IndexFS]], [[B-epsilon Tree]], [[Crash Consistency]]

## 出典
- [facebook/rocksdb - GitHub](https://github.com/facebook/rocksdb)
- [RocksDB Overview - RocksDB Wiki](https://github.com/facebook/rocksdb/wiki/RocksDB-Overview)
