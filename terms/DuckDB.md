---
aliases: [duckdb]
tags: [term]
maps: ["[[Scientific Data]]"]
status: draft
updated: 2026-10-10
---
# DuckDB

> アプリケーションの[[Process|プロセス]]の中に組み込んで使う、分析（OLAP）向けのSQLデータベースである。サーバを立てずに、手元のファイルに対して集計や結合を高速に行える。

## 概要
DuckDBは、オランダの研究機関CWIのMark RaasveldtとHannes Mühleisenが開発し、SIGMOD 2019で発表した。組み込み型のデータベースとして広く使われる[[SQLite]]は、少数の行を読み書きする処理（OLTP）を想定している。DuckDBは、同じく別のサーバのプロセスを必要としない組み込み型でありながら、表の大部分にわたる集計や結合といった分析の処理を対象とする。そのため、問い合わせの実行には、値を一行ずつではなく列ごとにまとめた塊（ベクトル）として処理する、列指向・ベクトル化の実行エンジンを用いる。外部への依存がなく、ライセンスはMITである。

## どこで出てくるか
実験のログやベンチマークの結果、トレースなどの大きな表形式のデータを、手元で手早く集計するときに用いる。[[Parquet]]のファイルは、`SELECT * FROM 'results.parquet'` のようにファイル名をそのまま表として問い合わせることができ、`results/*.parquet` のようなパターンで複数のファイルをまとめて読める。このとき、問い合わせに必要な列だけを読み、条件に合わない部分は統計情報を用いて読み飛ばす。[[Python]]のパッケージからは、pandasのデータフレームに対しても直接SQLを実行できる。

## 関係
- 対比: [[SQLite]]（同じ組み込み型だが、行単位の更新処理を想定する）
- 使う / 使われる: [[Parquet]], [[Python]]

## 出典
- [Why DuckDB - DuckDB](https://duckdb.org/why_duckdb)
- [Reading and Writing Parquet Files - DuckDB](https://duckdb.org/docs/current/data/parquet/overview.html)
- [DuckDB: an Embeddable Analytical Database (SIGMOD 2019)](https://ir.cwi.nl/pub/28800/28800.pdf)
