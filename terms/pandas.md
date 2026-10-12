---
aliases: [Pandas, パンダス, DataFrame, データフレーム, Series, pd]
tags: [term]
maps: ["[[Programming]]", "[[Scientific Data]]"]
status: draft
updated: 2026-10-13
---
# pandas

> [[Python]]で表形式のデータを読み込み、整形し、集計するためのライブラリであり、列ごとに型を持つ二次元の表DataFrameを中心とする。

## 概要
pandasの中心となるデータ構造は、一次元のSeriesと二次元のDataFrameである。Seriesはラベル（index）付きの、同一の型の配列であり、DataFrameは列ごとに異なる型を持てる表である。DataFrameの各列はSeriesであり、SQLの表や表計算ソフトのシートに相当する。[[NumPy]]のndarrayが配列全体で一つの型を持ち、要素を位置で指すのに対し、pandasは行と列にラベルを持たせ、列ごとに型を変えられる。そのため、数値の列と文字列の列が混在する実験の結果を、列の名前で扱える。

pandasは[[NumPy]]の上に構築され、性能が重要な部分はCythonで実装されている。欠損値の扱い、ラベルによるデータの自動的な位置合わせ、`groupby` による分割・適用・結合（split-apply-combine）の集計、表の結合（merge、join）、ピボットなどの形状変換、時系列の処理を備える。CSVやExcel、[[HDF5]]、[[Parquet]]などのファイル、およびデータベースとの間で読み書きできる。

pandas 3.0（2026年1月）では、[[Copy-on-Write]]が常に有効となった。インデックス参照の結果や、新しいDataFrameを返すメソッドの結果は、常に複製であるかのように振る舞う。そのため、`df[df.a > 0]["b"] = 1` のような連鎖代入（chained assignment）は元の表を変更しない。また、文字列の列は既定で専用の `str` 型となり、PyArrowがインストールされていれば[[Apache Arrow]]の形式で保持される。古い版を前提としたコードは、これらの点で挙動が変わりうる。

## どこで出てくるか
研究室では、ベンチマークの結果やログを集計する場面で最もよく用いる。複数回の測定を記録したCSVを `read_csv()` で読み込み、`groupby()` で条件ごとに平均や標準偏差を求め、[[Matplotlib]]でグラフにする、という流れが典型である。pandasはデータ全体をメモリに載せて処理するため、扱うデータがメモリに収まらない場合や、集計に時間がかかる場合には、[[Parquet]]と[[DuckDB]]や、Arrowを基盤とするPolarsなどの道具が選択肢となる。

## 関係
- 上位概念: [[Python]]（pandasはPythonのライブラリである）
- 前提: [[NumPy]]
- 対比: [[DuckDB]]（pandasはPythonのメソッドで表を操作し、DuckDBはSQLで問い合わせる）
- 使う / 使われる: [[Matplotlib]], [[Apache Arrow]], [[Parquet]], [[HDF5]]
- 関連: [[Copy-on-Write]]

## 出典
- [Package overview - pandas documentation](https://pandas.pydata.org/docs/getting_started/overview.html)
- [What's new in 3.0.0 - pandas documentation](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html)
