---
aliases: [Multiversion Concurrency Control, Multi-Version Concurrency Control, 多版同時実行制御, マルチバージョン同時実行制御, VACUUM, Undo Log, undoログ]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-10
---
# MVCC（Multiversion Concurrency Control）

> データの古い版を残しておき、各トランザクションにある時点のスナップショットを見せることで、読み込みと書き込みが互いを待たずに並行して進めるようにする同時実行制御の方式である。

## 概要
複数のトランザクションが同じデータを並行に読み書きするとき、[[Mutex|ロック]]だけで整合性を保つと、書き込み中のデータを読もうとする読み込みは書き込みの終了を待たされ、その逆も起きる。MVCCでは、データを上書きする代わりに新しい版を作り、古い版をしばらく残す。各トランザクションは開始時などの時点のスナップショットに属する版だけを読むため、他のトランザクションが途中まで書いた不整合なデータを見ることがない。その結果、読み込みは書き込みを妨げず、書き込みは読み込みを妨げない。

古い版の持ち方は実装によって異なる。[[InnoDB]]は、行には最新の版を置き、変更前の内容をundoログに記録しておき、古いスナップショットを読むトランザクションには、undoログから以前の版を組み立てて返す。PostgreSQLは、`UPDATE` や `DELETE` の後も古い版の行を表の中に残す。どちらの場合も、もはやどのトランザクションからも見えなくなった古い版は回収しなければならない。InnoDBではこれをpurge、PostgreSQLでは `VACUUM` と呼ぶ。長く終わらないトランザクションが古いスナップショットを保持していると回収が進まず、InnoDBではundoログの領域が膨らみ続ける。

## どこで出てくるか
MVCCは、MySQL（InnoDB）やPostgreSQLなどのデータベースが用いる同時実行制御である。スナップショットを読むことで得られる隔離の水準はスナップショット分離と呼ばれ、[[Consistency Model|一貫性モデル]]やトランザクションの隔離水準の議論で、直列化可能性と対比して現れる。古い版を消さずに残すという考え方は、[[Copy-on-Write|コピーオンライト]]の[[File System|ファイルシステム]]がデータを上書きせずに[[Snapshot|スナップショット]]を安価に作れることと共通している。

## 関係
- 対比: [[Mutex]]（ロックで排他して整合性を保つ）
- 使う / 使われる: [[InnoDB]]
- 関連: [[Consistency Model]], [[Snapshot]], [[Copy-on-Write]]

## 出典
- [Introduction - PostgreSQL Documentation（Concurrency Control）](https://www.postgresql.org/docs/current/mvcc-intro.html)
- [Routine Vacuuming - PostgreSQL Documentation](https://www.postgresql.org/docs/current/routine-vacuuming.html)
- [InnoDB Multi-Versioning - MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/innodb-multi-versioning.html)
