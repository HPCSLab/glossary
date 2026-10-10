---
aliases: [Apache Parquet, .parquet, 列指向ファイル形式, Columnar Storage Format, Row Group, 行グループ, Column Chunk, カラムチャンク]
tags: [term]
maps: ["[[Scientific Data]]"]
status: draft
updated: 2026-10-10
---
# Parquet（Apache Parquet）

> 表形式のデータを列ごとにまとめて圧縮して格納する、列指向（カラムナ）のファイル形式であり、大量のデータの保存と分析に広く用いられる。

## 概要
CSVのような行指向の形式では、一行のすべての列が並んで格納されるため、少数の列だけを集計する場合にも全体を読む必要がある。Parquetは同じ列の値をまとめて格納するため、必要な列だけを読めばよい。また、同じ列には同じ型の似た値が並ぶため、符号化と圧縮が効きやすい。

ファイルは表を行の範囲で分けた行グループ（row group）からなり、各行グループは列ごとのカラムチャンク（column chunk）を持つ。カラムチャンクはさらにページに分かれる。各カラムチャンクの位置などのメタデータはデータの後ろ（フッタ）に書かれ、読み手はまずフッタを読んで必要なカラムチャンクだけを読み出す。メタデータを後ろに置くのは、書き手がデータを一度だけ順に書いて済ませるためである。ページごとに値の下限と上限を記録するページインデックスを持たせることもでき、条件に合わないページを読み飛ばせる。

Parquetは、TwitterとClouderaの共同開発として始まり、GoogleのDremelの論文の、入れ子構造のデータを列に分解する手法を取り入れている。2013年に最初の版が公開され、現在はApache Software Foundationのプロジェクトである。

## どこで出てくるか
データ分析の基盤で、データを保存する標準的な形式として用いられる。[[Python]]では、[[Apache Arrow]]のPythonの実装であるPyArrowや、pandasから読み書きする。[[HDF5]]や[[netCDF]]が多次元の配列を対象とするのに対し、Parquetは列ごとに型を持つ表を対象とする。HPCでも、I/Oのトレースのツールである[[Recorder]]が、トレースをParquetに変換して他の分析の道具に渡す機能を備えている。

## 関係
- 対比: [[HDF5]]（多次元の配列を格納するのに対し、Parquetは列からなる表を格納する）
- 使う / 使われる: [[Apache Arrow]], [[Recorder]]
- 関連: [[Python]]

## 出典
- [Overview - Apache Parquet](https://parquet.apache.org/docs/overview/)
- [File Format - Apache Parquet](https://parquet.apache.org/docs/file-format/)
- [Page Index - Apache Parquet](https://parquet.apache.org/docs/file-format/pageindex/)
- [Apache Parquet - Wikipedia](https://en.wikipedia.org/wiki/Apache_Parquet)
