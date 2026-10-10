---
aliases: [Lightning Memory-Mapped Database, lmdb, MDB]
tags: [term]
maps: ["[[Databases]]"]
status: draft
updated: 2026-10-10
---
# LMDB（Lightning Memory-Mapped Database）

> データベースのファイル全体をメモリに写像して読み書きする、[[B-Tree|B+木]]に基づく組み込み型のキーバリューストアである。

## 概要
LMDBは、Symasが[[LDAP|OpenLDAP]]プロジェクトのために開発した、アプリケーションに組み込んで使う[[Key-Value Store|キーバリューストア]]である。データベースのファイル全体を[[mmap]]で[[Virtual Memory|仮想アドレス空間]]に写像するため、読み出しは写像されたメモリから直接値を返し、データを複製しない。キーは常に整列されて格納される。

更新は[[Copy-on-Write|コピーオンライト]]で行い、使用中のデータのページを上書きしない。これにより、読み手はロックを取らずに一貫した版を読め、読み手と書き手が互いを妨げない（[[MVCC]]）。書き込みのトランザクションは一度に一つに限られ、直列に実行される。上書きをしないため、クラッシュの後に特別な回復の処理を必要としない。ログや後から行う圧縮（[[LSM-Tree|コンパクション]]）も不要である。

## どこで出てくるか
LMDBを用いるアプリケーションの容量や性能の問題を調べる際には、次の注意点が関わる。写像の大きさ（`mdb_env_set_mapsize()`）がデータベースの最大の大きさとなるため、将来の増加を見込んで大きく設定する。長く続く読み出しのトランザクションがあると、新しい書き込みで不要になったページを再利用できず、ファイルが急速に大きくなる。また、公式の文書は、リモートのファイルシステムの上でLMDBを使わないよう求めている。[[NFS]]や[[Parallel File System|並列ファイルシステム]]の上に置くことは避ける。

## 関係
- 上位概念: [[Key-Value Store]]
- 使う / 使われる: [[B-Tree]], [[mmap]], [[Copy-on-Write]], [[MVCC]]
- 対比: [[RocksDB]]（LSM木に基づき、書き込みに強い）
- 関連: [[SQLite]]

## 出典
- [LMDB - Symas](https://www.symas.com/mdb)
- [lmdb.h - LMDB source (GitHub mirror)](https://github.com/LMDB/lmdb/blob/mdb.master/libraries/liblmdb/lmdb.h)
