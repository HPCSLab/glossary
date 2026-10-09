---
aliases: [perfetto, Perfetto UI, ui.perfetto.dev, Trace Processor, トレースプロセッサ]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# Perfetto

> トレース（時刻付きの出来事の記録）を収集し、ブラウザ上のタイムラインで表示し、SQLで分析するための、Googleが開発するオープンソースのツール群である。

## 概要
Perfettoは、AndroidとChromeの標準のトレースの仕組みとして設計された。三つの部分からなる。一つ目は記録の部分であり、一台の計算機の多数のプロセスから集めた出来事を一つのトレースのファイルにまとめるデーモン、アプリケーションに組み込むC/C++のSDK、AndroidとLinuxでスケジューリング、CPUの周波数、メモリ、コールスタックの標本などを集める仕組みを含む。二つ目はUIであり、インストールなしにWebブラウザで動き、オフラインでも使えるタイムラインの表示器である。三つ目はトレースプロセッサであり、トレースを表として読み込み、SQLで問い合わせて分析する。

UIは、Perfetto自身の形式のほかに、他の道具が出力したトレースも開ける。例えば、ChromeのJSONの形式、Linuxの[[perf]]の出力、[[Ftrace]]のテキストの出力などである。

## どこで出てくるか
Androidやブラウザの性能の調査のほか、自作のプログラムやツールの出力をタイムラインで見る手段として用いられる。例えば、並列I/Oのトレースのツールである[[Recorder]]は、トレースをPerfettoで表示できる形式に変換する道具を備えている。カーネルの観測では、Ftraceの記録をPerfettoで表示して、スケジューリングの遅れや[[Process|プロセス]]の間の待ちを時系列で調べられる。

## 関係
- 使う / 使われる: [[Ftrace]], [[perf]], [[Recorder]]
- 関連: [[Flame Graph]], [[bpftrace]]

## 出典
- [Perfetto - System profiling, app tracing and trace analysis](https://perfetto.dev/docs/)
- [Post-processing and Visualization - Recorder documentation](https://recorder.readthedocs.io/latest/postprocessing.html)
