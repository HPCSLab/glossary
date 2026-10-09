---
aliases: [Arrow, PyArrow, pyarrow, Arrow IPC, Feather, Arrow Columnar Format, 列指向メモリ形式]
tags: [term]
maps: ["[[Scientific Data]]"]
status: draft
updated: 2026-10-10
---
# Apache Arrow

> 表形式のデータをメモリ上で列ごとに並べて表す、言語に依存しない標準の形式と、それを扱うライブラリ群である。

## 概要
データを扱うシステムがそれぞれ独自のメモリ上の形式を持つと、システムの間でデータを渡すたびに、別の形式への直列化と復元（シリアライズとデシリアライズ）が必要になり、その費用が大きい。Arrowはメモリ上の列指向の形式を標準として定め、同じ形式を使うシステムの間ではほとんど変換なしにデータを渡せるようにする。列の値がメモリ上に連続して並ぶため、CPUのSIMD命令による演算にも向く。

Arrowの形式でファイルに書き出したものがArrow IPCの形式であり、Feather（第2版）はこれと同じものである。IPCの形式はメモリ上の形式そのままであるため、ファイルを[[mmap|メモリにマップ]]すれば、復元やコピーなしに分析できる。

Arrowは2016年にApache Software Foundationのプロジェクトとして発表された。C++、Java、Go、[[Rust]]などの言語ごとの実装があり、[[Python]]のPyArrowはC++の実装の上に作られている。

## どこで出てくるか
[[Parquet]]と組み合わせて現れることが多い。Parquetが保存のために圧縮・符号化したディスク上の形式であり、読むたびに復号が要るのに対し、Arrowは計算に直接使うためのメモリ上の形式である。そのため、Parquetのファイルを読み込んでArrowの表にして処理する、という流れが一般的であり、PyArrowはParquetの読み書きの関数（`read_table()`、`write_table()`）も備える。pandasのDataFrameとの相互変換もできる。

## 関係
- 対比: [[Parquet]]（ディスク上の保存のための形式であるのに対し、Arrowはメモリ上の計算のための形式である）
- 使う / 使われる: [[Python]]
- 関連: [[NumPy]]

## 出典
- [Overview - Apache Arrow](https://arrow.apache.org/overview/)
- [FAQ - Apache Arrow](https://arrow.apache.org/faq/)
- [Reading and Writing the Apache Parquet Format - Apache Arrow Python documentation](https://arrow.apache.org/docs/python/parquet.html)
- [Apache Arrow - Wikipedia](https://en.wikipedia.org/wiki/Apache_Arrow)
