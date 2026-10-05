---
aliases: [プロセス, PID, Process ID, プロセスID, fork, exec, Context Switch, コンテキストスイッチ]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# Process（プロセス）

> 実行中のプログラムの実体であり、OSが資源を割り当て、互いに分離して管理する単位である。

## 概要
プログラムはディスク上の実行ファイルであり、それを読み込んで実行しているものがプロセスである。同じプログラムから複数のプロセスを起動できる。各プロセスは、独自の[[Virtual Memory|仮想アドレス空間]]（実行コード、データ、関数呼び出しのためのスタック、実行中に確保するヒープ）、開いているファイルを表す[[File Descriptor|ファイルディスクリプタ]]、所有者や権限などの属性、レジスタなどのCPUの状態を持つ。一つのプロセスは一つ以上のスレッドで実行され、同じプロセスのスレッドはメモリを共有する。

プロセスは互いに分離されており、他のプロセスのメモリを直接読み書きすることはできない。プロセスの間でデータをやり取りするには、パイプ、共有メモリ、ソケットなど、OSが提供する仕組みを用いる。OSは、実行するプロセスを切り替えること（コンテキストスイッチ）で、CPUの数より多くのプロセスを並行して動かす。Linuxでは、プロセスは `fork` で自身を複製して作られ、`exec` で別のプログラムに置き換えられる。各プロセスはプロセスID（PID）で識別される。

## どこで出てくるか
[[MPI]]のプログラムは、多数のプロセスを起動し、それぞれが独立したメモリを持つため、データはメッセージの通信で交換する。これに対し、[[OpenMP]]は一つのプロセスの中の複数のスレッドでメモリを共有する。[[System Call|システムコール]]や[[strace]]、[[perf]]の出力を読む際にも、どのプロセスの振る舞いかを区別する必要がある。

## 関係
- 前提: [[Virtual Memory]]
- 使う / 使われる: [[File Descriptor]], [[System Call]]
- 関連: [[Linux Kernel]], [[MPI]], [[OpenMP]]

## 出典
- [Process (computing) - Wikipedia](https://en.wikipedia.org/wiki/Process_(computing))
- [fork(2) - Linux manual page](https://man7.org/linux/man-pages/man2/fork.2.html)
- [execve(2) - Linux manual page](https://man7.org/linux/man-pages/man2/execve.2.html)
