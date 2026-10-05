---
aliases: [KVS, キーバリューストア, Key-Value Database, LSM-Tree, LSM木, Log-Structured Merge-Tree, RocksDB, LevelDB, Redis, memcached, Dynamo, Compaction, コンパクション]
tags: [term]
maps: ["[[Storage]]", "[[Distributed Systems]]"]
status: draft
updated: 2026-10-06
---
# Key-Value Store（キーバリューストア、KVS）

> 一意なキーに値を対応付けて格納し、キーを指定して値を格納・取得・削除する、単純なインタフェースのデータベースである。

## 概要
KVSの基本的な操作は、キーに値を書く `put`、キーから値を読む `get`、キーを消す `delete` であり、キーの順序を保持する実装では、範囲を指定してキーを順に走査する `scan` も提供される。キーと値は、多くの場合、任意の長さのバイト列として扱われ、値の中身をKVSが解釈することはない。関係データベースのような表の構造や結合の処理を持たない代わりに、実装を単純かつ高速にでき、多数のサーバへの分散も容易である。

KVSは、データの置き場所と規模によっていくつかの種類に分けられる。Redisやmemcachedは、データを主記憶に置き、キャッシュなどに用いられる。LevelDBや、それを基にFacebookが開発したRocksDBは、アプリケーションに組み込んで使うライブラリであり、データを記憶装置に永続化する。Amazonが2007年のSOSPで発表したDynamoは、多数のサーバにデータを分散・複製するKVSであり、コンシステントハッシュによる配置、[[Consistency Model|結果整合性]]、ベクタクロックによる衝突の検出などを組み合わせて、障害時にも書き込みを拒否しない高い可用性を実現した。etcdのように、[[Raft]]による[[Consensus|合意]]を用いて[[Linearizability|線形化可能]]な操作を提供するKVSもある。

永続的なKVSの内部構造としては、ハッシュ表、B木、LSM木（Log-Structured Merge-Tree）が代表的である。LSM木は、1996年にO'Neilらが提案した構造で、書き込みを遅延させてまとめて処理することで、大量の書き込みを効率よく扱う。RocksDBを例に取ると、書き込みはまず、[[Crash Consistency|クラッシュ]]に備えて先行書き込みログ（WAL）に追記され、主記憶上の整列済みの表（memtable）に入る。memtableが一杯になると、整列済みの不変なファイル（SSTファイル）として記憶装置に書き出される。SSTファイルは複数の階層（レベル）に置かれ、コンパクションと呼ばれる処理によって、上位のレベルのファイルが下位のレベルのファイルと併合されながら順に移されていく。記憶装置への書き込みはすべて順次の追記となるため、書き込みの性能が高く、[[SSD]]にも適する。

## どこで出てくるか
LSM木に基づくKVSの性能は、三種類の増幅のトレードオフとして議論される。書き込み増幅は、コンパクションによって同じデータが何度も書き直される度合い、読み込み増幅は、一つのキーを探すために調べるファイルの数、空間増幅は、古い版や削除済みのデータによって論理的な大きさより多くの容量を使う度合いである。コンパクションの方式や設定は、これらのどれを優先するかを決める。

ストレージ研究では、KVSは主要な研究対象の一つである。例えば、FAST 2016で発表されたWiscKeyは、キーと値を分離し、LSM木にはキーと値の位置だけを入れることで、大きな値を何度も書き直す無駄を減らし、SSD上での性能を大きく改善した。ファイルシステムの上にKVSを構築する場合、KVSのコンパクションとSSD内部のガベージコレクションが二重に書き込みを増幅させる問題や、KVSが整合性のために発行する[[fsync]]のコストも論点となる。KVSの性能は、YCSBなどのベンチマークで評価されることが多い。[[Object Storage|オブジェクトストレージ]]も、バケットとキーで値を扱う点で、大規模な分散KVSの一種とみなせる。

## 関係
- 使う / 使われる: [[Raft]], [[Consensus]]（etcdなど）, [[SSD]]
- 対比: [[File System]]（階層的な名前空間とPOSIXの意味論を持つ）, [[Object Storage]]
- 関連: [[Consistency Model]], [[Crash Consistency]], [[fsync]], [[Linearizability]], [[BPF]]（XRP）

## 出典
- [RocksDB Overview - RocksDB Wiki](https://github.com/facebook/rocksdb/wiki/RocksDB-Overview)
- [The Log-Structured Merge-Tree (LSM-Tree) (O'Neil et al., Acta Informatica, 1996)](https://www.cs.umb.edu/~poneil/lsmtree.pdf)
- [Amazon's Dynamo - All Things Distributed](https://www.allthingsdistributed.com/2007/10/amazons_dynamo.html)
- [WiscKey: Separating Keys from Values in SSD-conscious Storage - USENIX FAST 2016](https://www.usenix.org/conference/fast16/technical-sessions/presentation/lu)
- [Redis Open Source - Redis documentation](https://redis.io/docs/latest/get-started/)
