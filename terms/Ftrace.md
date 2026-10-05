---
aliases: [ftrace, Function Tracer, tracefs, trace-cmd, KernelShark, Tracepoint, トレースポイント, function_graph]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# Ftrace

> Linuxカーネルに組み込まれたトレースの枠組みであり、カーネル内の関数呼び出しやイベントを記録して、カーネルの動作と遅延の原因を調べるために用いる。

## 概要
Ftraceの名称はfunction tracerに由来するが、実際には関数の追跡に限らない複数のトレーサの集合である。操作は、tracefsと呼ばれる特殊なファイルシステム（通常 `/sys/kernel/tracing`、古い環境では `/sys/kernel/debug/tracing`）の中のファイルを読み書きすることで行う。専用のツールがなくても、`echo` と `cat` だけで利用できる点に特徴がある。

使用するトレーサは `current_tracer` に名前を書き込んで選択し、選択可能なものは `available_tracers` で確認する。`function` はカーネル関数の呼び出しを記録し、`function_graph` は関数の入口と出口を記録して、呼び出しの木構造と各関数の所要時間を示す。このほか、割り込みが禁止されていた時間の最大値を測る `irqsoff`、高優先度のタスクが起床してから実行されるまでの遅延を測る `wakeup_rt` など、遅延の調査に特化したトレーサがある。追跡する関数は `set_ftrace_filter` で、対象のプロセスは `set_ftrace_pid` で絞り込める。記録の開始と停止は `tracing_on` で制御し、結果は `trace` で一括して、`trace_pipe` で逐次的に読み出す。

関数の追跡は、カーネルのビルド時にすべての関数の入口へ挿入された呼び出し命令を利用する。この命令は、追跡していない間は実行時に何もしない命令（nop）に書き換えられており、追跡を有効にしたときにのみ書き戻される（dynamic ftrace）。このため、使用していない間のオーバーヘッドはほとんどない。

Ftraceは、カーネルのソースコード中にあらかじめ埋め込まれた計測点であるトレースポイント（trace event）も扱う。トレースポイントは、スケジューラ、[[blk-mq|ブロック層]]、ファイルシステムなどの主要な箇所に設けられており、`events/<サブシステム>/<イベント>/enable` に1を書き込むと有効になる。各イベントには、フィールドの値に基づくフィルタも設定できる。

## どこで出てくるか
Ftraceは、カーネル内部で何が起きているかを、カーネルを再構築せずに確かめる基本的な手段である。例えば、`function_graph` で特定の[[System Call|システムコール]]の処理を追跡すると、[[VFS]]からファイルシステム、[[Page Cache|ページキャッシュ]]、ブロック層へと処理がどのように進み、どこで時間を要しているかを関数単位で把握できる。ブロック層のトレースポイントを有効にすれば、個々のI/O要求の発行と完了を記録できる。

tracefsを直接操作するのは煩雑であるため、記録と表示を行うフロントエンドの `trace-cmd` や、その結果を時系列で可視化するKernelSharkがよく用いられる。[[perf]]や[[BPF]]もトレースポイントを利用しており、Ftraceはこれらと並ぶLinuxのトレース基盤の一つである。三者の使い分けとしては、カーネル関数の呼び出しの流れを詳細に見るにはFtrace、ハードウェア性能カウンタやサンプリングにはperf、カーネル内での柔軟な集計にはBPF、という整理ができる。tracefsの操作には通常root権限が必要である。

## 関係
- 前提: [[Linux Kernel]]
- 対比: [[perf]], [[BPF]]（同じくカーネルの観測に用いる）
- 関連: [[strace]], [[blk-mq]], [[VFS]], [[Systems Performance]]

## 出典
- [ftrace - Function Tracer - The Linux Kernel documentation](https://docs.kernel.org/trace/ftrace.html)
- [Event Tracing - The Linux Kernel documentation](https://docs.kernel.org/trace/events.html)
- [trace-cmd(1) - Linux manual page](https://man7.org/linux/man-pages/man1/trace-cmd.1.html)
