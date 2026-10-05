---
aliases: [perf_events, perf stat, perf record, perf report, perf top, perf trace, Linux perf, PMU, Hardware Performance Counter, ハードウェア性能カウンタ]
tags: [term]
maps: ["[[Operating System]]", "[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# perf

> Linuxカーネルのperf_events機構を用いて、ハードウェア性能カウンタ、ソフトウェアイベント、トレースポイントを計測・解析するツール群である。

## 概要
`perf` は[[Linux Kernel|Linuxカーネル]]のソースツリーで開発されている性能解析ツールであり、CPUの性能監視ユニット（PMU）が提供するハードウェア性能カウンタと、カーネルが提供するソフトウェアのイベントやトレースポイントの両方を扱う。機能はサブコマンドに分かれている。

`perf stat` は、プログラムの実行中に発生したイベントの回数を数える。サイクル数、命令数、キャッシュミス数、分岐予測ミス数などを計測でき、命令数をサイクル数で割ったIPC（1サイクルあたりの命令数）から、プロセッサがどれだけ効率よく動作しているかの見当を付けられる。`perf list` で利用可能なイベントの一覧を確認できる。

`perf record` は、一定の間隔で実行中の命令の位置やコールスタックを標本として記録する（サンプリング）。`perf report` はその結果を関数ごとに集計して表示し、`perf annotate` はソースコードや機械語の命令単位で時間の多い箇所を示す。`perf top` は同様の集計を実時間で表示する。記録したコールスタックは、[[Flame Graph|フレームグラフ]]として可視化されることが多い。フレームグラフは、横幅がその関数の現れた標本の割合を、縦方向が呼び出しの深さを表す図であり、横軸は時間の経過ではない。`perf trace` は、[[strace]]に似た[[System Call|システムコール]]の追跡を、より小さなオーバーヘッドで行う。

## どこで出てくるか
`perf` は、HPCアプリケーションの最適化において、どの関数が実行時間を占めているか（ホットスポット）を特定する最初の手段である。`perf stat` の結果から、性能がメモリアクセスで律速されているのか、演算で律速されているのかの手掛かりを得られ、[[Roofline Model|ルーフラインモデル]]などの分析につなげられる。カーネル内の時間も含めて計測できるため、I/Oやシステムコールのオーバーヘッドの分析にも用いられる。

一般ユーザが利用できる範囲は、sysctlの `kernel.perf_event_paranoid` の値で制限される。値が大きいほど制限が強く、2以上では自身のプロセスのユーザ空間での実行しか計測できない。共用の計算機では、システム全体の計測やカーネル内の計測が許可されていないことが多い。また、仮想マシンやコンテナ内では、ハードウェア性能カウンタが使えない場合がある。

## 関係
- 前提: [[Linux Kernel]]
- 対比: [[strace]]（ptraceによる追跡で、オーバーヘッドが大きい）
- 関連: [[BPF]], [[Roofline Model]], [[Systems Performance]], [[ltrace]]

## 出典
- [perf(1) - Linux manual page](https://man7.org/linux/man-pages/man1/perf.1.html)
- [Perf events and tool security - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/perf-security.html)
- [Flame Graphs - Brendan Gregg](https://www.brendangregg.com/flamegraphs.html)
