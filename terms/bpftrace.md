---
aliases: [Bpftrace, bpftrace -e, .bt, biolatency.bt, opensnoop.bt]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# bpftrace

> [[BPF|eBPF]]を用いてLinuxのカーネルやプログラムの振る舞いを観測するための、awkに似た簡潔な言語とその処理系である。

## 概要
bpftraceの言語は、awk、C、およびDTraceやSystemTapなどの先行するトレーサに影響を受けている。利用者が書いたスクリプトは、LLVMでBPFのプログラムにコンパイルされ、libbpfを介してカーネルに読み込まれる。そのため、稼働中のシステムを止めたり改変したりせずに、小さな負担で観測できる。

スクリプトは、「プローブ /条件/ { 処理 }」の形の組からなる。プローブは処理を取り付ける箇所であり、[[System Call|システムコール]]などのカーネルの静的なトレースポイント（`tracepoint:`）、任意のカーネル関数の入口と出口（`kprobe:`、`kretprobe:`）、ユーザプログラムの関数（`uprobe:`）、アプリケーションに埋め込まれた静的なプローブ（USDT）、一定の周期（`profile:`、`interval:`）などがある。処理の中では、`@` で始まるマップ変数に `count()` や `hist()`（2のべき乗のヒストグラム）で集計し、終了時に結果が表示される。`-l` で利用できるプローブを一覧し、`-e` で一行のスクリプトを実行する。

例えば、次の一行はプロセスごとのシステムコールの回数を数える。

`bpftrace -e 'tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }'`

次の一行は、カーネルの `vfs_read` の所要時間をプロセスごとのヒストグラムにする。

`bpftrace -e 'kprobe:vfs_read { @start[tid] = nsecs; } kretprobe:vfs_read /@start[tid]/ { @ns[comm] = hist(nsecs - @start[tid]); delete(@start, tid); }'`

## どこで出てくるか
ストレージやOSの研究では、カーネルの中のどこで時間がかかっているか、どの関数が何回呼ばれているかを、カーネルを改変せずに確かめる手段として用いられる。リポジトリには、ブロックI/Oの[[Latency|レイテンシ]]のヒストグラムを表示する `biolatency.bt`、ファイルのオープンを一覧する `opensnoop.bt` などの道具が含まれている。カーネル関数の引数の構造体（例えば[[VFS]]の `struct path`）の中身を読む場合、カーネルが[[BTF]]の型情報を持っていれば、全ての構造体を参照できる。持っていなければ、カーネルのヘッダを読み込む必要がある。

一行のスクリプトは `-e` で、長いスクリプトは `.bt` ファイルに書いて実行する。

## 関係
- 前提: [[BPF]]
- 使う / 使われる: [[BTF]], [[System Call]], [[VFS]]
- 対比: [[perf]]（サンプリングとハードウェアの性能カウンタ）, [[Ftrace]], [[strace]]
- 関連: [[Latency]], [[Flame Graph]], [[Systems Performance]]

## 出典
- [bpftrace/bpftrace - GitHub](https://github.com/bpftrace/bpftrace)
- [The bpftrace One-Liner Tutorial - GitHub](https://github.com/bpftrace/bpftrace/blob/master/docs/tutorial_one_liners.md)
- [bpftrace tools - GitHub](https://github.com/bpftrace/bpftrace/blob/master/tools/README.md)
