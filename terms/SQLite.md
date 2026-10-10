---
aliases: [sqlite, sqlite3, SQLite3]
tags: [term]
maps: ["[[Databases]]"]
status: draft
updated: 2026-10-10
---
# SQLite

> 別のサーバのプロセスを持たず、アプリケーションの中にライブラリとして組み込んで使うSQLデータベースであり、データベース全体を一つのファイルに格納する。

## 概要
多くのSQLデータベースは、データベースのサーバのプロセスにクライアントが接続して使う。SQLiteは、ライブラリとしてアプリケーションの[[Process|プロセス]]の中で動き、通常のファイルを直接読み書きする。設定や管理を要さず、表や索引を含むデータベース全体が一つのファイルに収まり、そのファイルの形式は計算機のアーキテクチャによらない。電源断の後もACIDの性質を保つトランザクションを提供する。コードはパブリックドメインであり、世界で最も広く使われているデータベースとされる。

トランザクションの原子性は、既定ではロールバックジャーナルで実現する。これは、データベースのファイルを書き換える前に元の内容を別のファイルに写し、コミットの時点でそれを消す方式である。もう一つの方式であるWALモード（`PRAGMA journal_mode=WAL`）では、変更を別のファイルに追記し、後でデータベースのファイルに反映する。WALモードでは読み手と書き手が互いを妨げずに並行して動けるが、書き手は一度に一つに限られる。

## どこで出てくるか
実験の結果やメタデータを手元に整理して保存する用途や、多くのアプリケーションの設定やデータの保存先として出会う。[[Python]]には標準のモジュール `sqlite3` がある。HPCの環境で注意すべき点は、[[NFS]]などのネットワーク越しのファイルシステム上のデータベースを複数の計算機から使わないことである。SQLiteは書き込みに排他的なロックを用いるが、ネットワークファイルシステムによってはロックが正しく働かず、データベースが壊れた例がある。また、WALモードは共有メモリを用いるため、ネットワークファイルシステムの上では動かない。データと計算を別の計算機に置く必要がある場合は、クライアント・サーバ型のデータベースを用いるのが公式の推奨である。

## 関係
- 対比: [[DuckDB]]（同じく組み込み型だが、分析の処理を対象とする）
- 使う / 使われる: [[Python]]（標準モジュール `sqlite3`）
- 関連: [[Crash Consistency]], [[NFS]], [[LMDB]]

## 出典
- [About SQLite](https://www.sqlite.org/about.html)
- [Write-Ahead Logging - SQLite](https://www.sqlite.org/wal.html)
- [SQLite Over a Network, Caveats and Considerations](https://www.sqlite.org/useovernet.html)
- [sqlite3 — DB-API 2.0 interface for SQLite databases - Python documentation](https://docs.python.org/3/library/sqlite3.html)
