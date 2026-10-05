---
aliases: [GDB, GNU Debugger, GNUデバッガ, デバッガ, Debugger, Breakpoint, ブレークポイント, Backtrace, バックトレース, Core File, コアファイル, Core Dump, コアダンプ]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# gdb（GNU Debugger）

> 実行中のプログラムの内部で何が起きているか、またはクラッシュした時点で何をしていたかを調べるための、GNUプロジェクトのデバッガである。

## 概要
gdbでは、主に四つのことができる。プログラムを指定した引数や環境で起動すること、指定した条件でプログラムを停止させること、停止した時点の状態を調べること、変数の値などを書き換えて修正の効果を試すことである。[[C]]、C++、Fortran、[[Rust]]、アセンブリなどの言語に対応している。

ソースコードの行や変数の名前で調べるには、プログラムをデバッグ情報付き（`-g`）でコンパイルしておく必要がある。GCCでは、`-g` と最適化の `-O` を同時に指定でき、最適化したプログラムもデバッグできる。基本的な操作は次のとおりである。`break` で関数や行にブレークポイントを設定し、`run` でプログラムを起動する。停止したら、`backtrace`（`bt`）で呼び出しの履歴（コールスタック）を、`print` で変数や式の値を表示する。`next` は関数の中に入らずに次の行へ、`step` は関数の中に入って次の行へ進み、`continue` で次の停止まで実行を続ける。

gdbは、gdbの中で起動したプログラムだけでなく、`gdb -p <PID>` で実行中の[[Process|プロセス]]に後から接続（attach）することもできる。接続するとプロセスは停止し、`detach` で切り離すと実行を再開する。また、`gdb program core` のように、クラッシュしたプロセスのメモリの内容を書き出したコアファイルを読み込み、クラッシュした時点のスタックや変数を調べることもできる。プログラムの引数を指定するには `gdb --args program arg1 arg2` とする。

## どこで出てくるか
プログラムがセグメンテーション違反などで異常終了した場合、gdbで実行するかコアファイルを読み込み、`bt` でどこで落ちたかを確かめるのが最初の手順である。プログラムが止まったまま進まない場合も、`gdb -p` で接続して各[[Thread|スレッド]]のスタックを調べると、[[Deadlock|デッドロック]]などの原因を特定できる。

gdbはカーネルのデバッグにも用いられる。[[QEMU]]の仮想マシンでは、QEMUが待ち受けるgdbに接続して、ゲストのカーネルをステップ実行できる。カーネルのダンプファイルを解析する[[crash]]も、内部でgdbの機能を用いている。

## 関係
- 使う / 使われる: [[C]], [[Rust]], [[QEMU]], [[crash]]
- 関連: [[strace]], [[drgn]], [[kdump]], [[Deadlock]]

## 出典
- [GDB: The GNU Project Debugger](https://sourceware.org/gdb/)
- [A Sample GDB Session - Debugging with GDB](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Sample-Session.html)
- [Invoking GDB - Debugging with GDB](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Invoking-GDB.html)
- [Attach - Debugging with GDB](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Attach.html)
- [Compilation - Debugging with GDB](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Compilation.html)
