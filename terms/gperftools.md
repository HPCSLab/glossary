---
aliases: [Gperftools, Google Performance Tools, Gperftools Heap Profiler, gperftools Heap Profiler, Heap Profiler, ヒーププロファイラ, TCMalloc, tcmalloc, libtcmalloc, pprof, HEAPPROFILE, CPU Profiler]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# gperftools

> Googleで開発された、高速な `malloc()` の実装であるTCMallocと、それを基盤とするヒーププロファイラやCPUプロファイラなどからなる、性能解析のためのツール群である。

## 概要
gperftools（旧称 Google Performance Tools）は、BSDライセンスで公開されており、主にLinuxで用いられる。中心となるTCMallocは、マルチスレッドのプログラムで高速に動作する `malloc()` と `new` の実装であり、標準のメモリ割り当てを置き換えて用いる。このほか、ヒーププロファイラ、ヒープチェッカ、CPUプロファイラが含まれる。

ヒーププロファイラは、ある時点でヒープに何が確保されているか、メモリリークがどこにあるか、どこで大量のメモリ割り当てが行われているかを調べるためのツールである。TCMallocの上に実装されているため、プログラムを `-ltcmalloc` を付けてリンクするか、実行時に `LD_PRELOAD` でTCMallocのライブラリを読み込ませて用いる。環境変数 `HEAPPROFILE` に出力ファイルの名前を与えて実行するか、プログラム中で `HeapProfilerStart()` と `HeapProfilerStop()` を呼ぶと、プロファイルが `<prefix>.0001.heap` のような名前のファイルに書き出される。書き出しは、一定量（既定では1GB）の割り当てが行われるごと、または使用量が一定量（既定では100MB）増えるごとに行われる。

書き出したプロファイルは、`pprof` で解析する。`--text` で関数ごとの表を、`--gv` などで呼び出しの関係の図を表示できる。`--inuse_space` は現在確保されているメモリの量を、`--alloc_space` はそれまでに割り当てられたメモリの総量を示す。`--base` に以前のプロファイルを指定すると、その間に増えた分だけを表示できるため、メモリリークの特定に役立つ。現在、pprofはGoで書き直された版が google/pprof として保守されている。

## どこで出てくるか
長時間動くサーバや、大きなデータを扱うプログラムで、メモリの使用量が想定より大きい、あるいは時間とともに増え続ける場合に、その原因となる割り当ての箇所を特定するために用いる。[[C]]やC++のプログラムが主な対象である。CPU時間の内訳を調べる場合は、[[perf]]や[[Flame Graph|フレームグラフ]]を用いる。

## 関係
- 使う / 使われる: [[C]]
- 関連: [[perf]], [[Flame Graph]], [[gdb]], [[Virtual Memory]]

## 出典
- [gperftools/gperftools - GitHub](https://github.com/gperftools/gperftools)
- [Gperftools Heap Profiler](https://gperftools.github.io/gperftools/heapprofile.html)
- [google/pprof - GitHub](https://github.com/google/pprof)
