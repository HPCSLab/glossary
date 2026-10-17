---
aliases: [dask, Dask Array, Dask DataFrame, Dask Distributed, dask.distributed, Dask Delayed, dask.delayed]
tags: [term]
maps: ["[[Scientific Data]]"]
status: draft
updated: 2026-10-17
---
# Dask

> NumPyの配列やpandasのDataFrameを多数のチャンクに分け、チャンクごとの処理をタスクグラフとして組み立てて並列に実行する、Pythonの並列計算ライブラリである。

## 概要
[[NumPy]]や[[pandas]]は、データ全体をメモリに載せ、一つのコアで処理することを前提とする。Daskは、大きな配列を格子状に並んだ多数の小さなNumPy配列（チャンク）の集まりとして表し（Dask Array）、表を多数のpandasのDataFrameの集まりとして表す（Dask DataFrame）。利用者はNumPyやpandasとほぼ同じAPIで処理を書くが、その時点では計算は行われず、チャンクごとの処理とその依存関係をタスクグラフとして記録するだけである。結果を求めて `compute()` を呼ぶと、スケジューラがグラフを実行し、依存のないタスクを並列に動かす。チャンクを順に読み込んで処理するため、メモリより大きなデータも扱える。

![[Dask Task Graph.excalidraw]]

スケジューラは、一台の計算機の[[Thread|スレッド]]を用いるもの、[[Process|プロセス]]を用いるもの、複数のノードのワーカを用いる分散スケジューラ（dask.distributed）から選ぶ。ArrayとDataFrameの既定はスレッドである。NumPyやpandasの演算は[[C|C言語]]で書かれた部分で[[GIL]]を解放するためスレッドで並列化できるが、[[Python]]で書かれた処理が中心の場合はGILのためにスレッドでは並列にならず、プロセスか分散スケジューラを用いる。チャンクの大きさは並列度とメモリ量とタスクの数を同時に決めるため、小さすぎるとタスクの管理の負荷が、大きすぎるとメモリが問題になる。

## どこで出てくるか
地球科学などで、[[netCDF]]や[[HDF5]]、[[Zarr]]に格納された大規模な多次元配列を解析するときに用いられる。ラベル付きの多次元配列を扱うxarrayは、`open_dataset` に `chunks` を指定するか `open_zarr` で開くと、変数をDaskの配列として遅延して読み込む。Zarrはチャンクを別々のオブジェクトとして格納するため、Daskのチャンクと格納のチャンクを揃えると、各タスクが独立に読み書きできる。HDF5のデータセットも `da.from_array` でDaskの配列として扱える。[[Compute Node|計算ノード]]をまたいで分散スケジューラのワーカを起動し、[[Slurm]]や[[PBS]]のジョブとして解析を並列化することもあり、dask-jobqueueはそのためのワーカの起動を受け持つ。

## 関係
- 前提: [[NumPy]], [[pandas]]
- 使う / 使われる: [[Zarr]], [[HDF5]], [[netCDF]]
- 関連: [[GIL]]

## 出典
- [Dask documentation](https://docs.dask.org/en/stable/)
- [Dask Array (Dask documentation)](https://docs.dask.org/en/stable/array.html)
- [Scheduling (Dask documentation)](https://docs.dask.org/en/stable/scheduling.html)
- [Create Dask Arrays (Dask documentation)](https://docs.dask.org/en/stable/array-creation.html)
- [Dask-Jobqueue documentation](https://jobqueue.dask.org/en/latest/)
- [Parallel Computing with Dask (xarray documentation)](https://docs.xarray.dev/en/stable/user-guide/dask.html)
