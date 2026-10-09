---
aliases: [innodb, InnoDB Storage Engine, Doublewrite Buffer, ダブルライトバッファ, Buffer Pool, バッファプール, innodb_flush_log_at_trx_commit]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# InnoDB

> 関係データベースMySQLの標準のストレージエンジンであり、トランザクション、行単位のロック、クラッシュからの回復を備える。

## 概要
MySQLは、SQLを処理する上位の層と、表のデータを実際に格納する下位のストレージエンジンを分けた構成をとる。InnoDBはその標準のストレージエンジンであり、`CREATE TABLE` でエンジンを指定しなければInnoDBの表が作られる。トランザクションのコミットとロールバック、行単位のロック、[[MVCC]]による一貫した読み込み、外部キーの制約を提供する。

各表は、主キーをキーとする[[B-Tree|B木]]（クラスタ化インデックス）の葉に行のデータそのものを格納する。副インデックスは主キーの値を持ち、行全体を得るには主キーで改めてクラスタ化インデックスを探索する。B木の節点にあたるページの大きさは既定で16KBである。読み込んだページは、主記憶上のバッファプールに[[Cache|LRU]]の変種で保持され、専用のサーバでは物理メモリの最大80%程度をバッファプールに割り当てることが多い。

永続性は、二つの仕組みで保つ。一つはredoログであり、データの変更をまずログに追記しておき、クラッシュの後はデータファイルに反映されていなかった変更をログから再適用する（先行書き込みログ）。もう一つはダブルライトバッファであり、ページをデータファイルの本来の位置に書く前に、まず別の領域にまとめて書いておく。16KBのページの書き込みの途中で電源が断たれると、ページの一部だけが書き換わった壊れた状態が残りうるが、このときダブルライトバッファの無傷の写しから復元できる。

## どこで出てくるか
InnoDBの永続化の設定は、[[Crash Consistency|クラッシュ整合性]]のための[[fsync]]の頻度と性能の兼ね合いを示す具体例である。`innodb_flush_log_at_trx_commit` の既定値1では、コミットのたびにログを書いてfsyncするため、記憶装置の書き込みの[[Latency|レイテンシ]]がそのままコミットの速さを左右する。0や2にすると、fsyncを約1秒に1回にまとめて速くなるが、クラッシュ時に直近のトランザクションを失いうる。Linuxでは、データファイルは既定で `O_DIRECT`（[[Direct IO|Direct I/O]]）で開かれ、[[Page Cache|ページキャッシュ]]を経由せずにバッファプールが直接キャッシュを担う。

ダブルライトバッファは同じデータを二度書くが、大きな連続した書き込みと一回のfsyncにまとめるため、I/Oの量や回数が倍になるわけではない。記憶装置がページの原子的な書き込みを保証する場合（MySQLのマニュアルではFusion-ioの装置）には、ダブルライトバッファは無効化される。B木の索引をその場で更新するInnoDBに対し、[[RocksDB]]をMySQLのストレージエンジンとしたMyRocksは、[[LSM-Tree|LSM木]]によって書き込みの増幅をInnoDBの約10分の1に減らせるとしている。

## 関係
- 前提: [[B-Tree]], [[Crash Consistency]]
- 対比: [[RocksDB]]（LSM木に基づく。MyRocksとしてMySQLのエンジンにもなる）
- 使う / 使われる: [[fsync]], [[Page Cache]]
- 関連: [[Key-Value Store]], [[Journaling File System]]

## 出典
- [Introduction to InnoDB - MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/innodb-introduction.html)
- [Clustered and Secondary Indexes - MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/innodb-index-types.html)
- [The Physical Structure of an InnoDB Index - MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/innodb-physical-structure.html)
- [Buffer Pool - MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/innodb-buffer-pool.html)
- [Redo Log - MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/innodb-redo-log.html)
- [Doublewrite Buffer - MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/innodb-doublewrite-buffer.html)
- [InnoDB Startup Options and System Variables - MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/innodb-parameters.html)
- [MyRocks](http://myrocks.io/)
