---
aliases: [スレッド, Multithreading, マルチスレッド, pthreads, POSIX Threads, Pthreads, NPTL, Race Condition, 競合状態, Data Race, データ競合, Thread-local Storage, スレッドローカルストレージ]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# Thread（スレッド）

> スケジューラが独立に管理できる最小の命令の流れであり、一つの[[Process|プロセス]]の中で、複数のスレッドがメモリを共有しながら並行して実行される。

## 概要
プロセスは一つ以上のスレッドで実行される。同じプロセスのスレッドは、実行コード、グローバル変数とヒープのメモリ、開いている[[File Descriptor|ファイルディスクリプタ]]などを共有する。一方、各スレッドは、自身のスタック（局所変数）、レジスタとプログラムカウンタ、スレッドローカルな記憶域、`errno` を個別に持つ。スレッドの切り替えは、[[Virtual Memory|仮想アドレス空間]]を切り替える必要がないため、プロセスの切り替えより軽い。

Linuxでは、スレッドの標準的なAPIはPOSIXの規格であるpthreadsであり、その実装であるNPTLは、各スレッドをカーネルがスケジュールする一つの単位に対応させる（1:1方式）。pthreadsを用いるプログラムは `cc -pthread` でコンパイルする。カーネルを介さずにユーザ空間でスレッドを切り替える、ユーザレベルスレッドの実装もある（[[Argobots]]など）。

スレッドはメモリを共有するため、複数のスレッドが同じデータを同時に読み書きすると、実行のタイミングによって結果が変わる競合状態が生じる。これを防ぐには、[[Mutex|ミューテックス]]などの同期の仕組みで、共有データへのアクセスを調停する必要がある。ただし、同期を誤ると[[Deadlock|デッドロック]]が起きる。こうした誤りは実行のたびに現れたり現れなかったりするため、再現と修正が難しい。

## どこで出てくるか
[[OpenMP]]は、一つのプロセスの中で複数のスレッドを用いて、[[Compute Node|計算ノード]]の多数のコアを使う。これに対し、[[MPI]]は、メモリを共有しない複数のプロセスで並列化する。[[Python]]の標準の実装であるCPythonには、一度に一つのスレッドしかPythonのコードを実行できないようにする[[GIL]]がある（GILを無効にしたビルドも提供されている）。[[perf]]などの出力を読む際には、プロセスだけでなく、どのスレッドの振る舞いかを区別する必要がある。

## 関係
- 対比: [[Process]]（メモリを共有しない）
- 使う / 使われる: [[Mutex]], [[OpenMP]]
- 関連: [[Deadlock]], [[Linux Kernel]], [[Python]]

## 出典
- [Thread (computing) - Wikipedia](https://en.wikipedia.org/wiki/Thread_(computing))
- [pthreads(7) - Linux manual page](https://man7.org/linux/man-pages/man7/pthreads.7.html)
