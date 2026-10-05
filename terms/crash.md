---
aliases: [crash utility, crash(8), Crash Utility]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# crash

> Linuxカーネルのクラッシュダンプ、あるいは稼働中のシステムのメモリを対話的に解析するためのツールである。

## 概要
`crash` は、カーネル固有の解析機能と、GNUデバッガ（gdb）のソースコード水準の解析機能を組み合わせたツールである。[[kdump]]などで取得したダンプファイルを解析するには、ダンプファイルと、それを生成したカーネルと完全に同じ版の、デバッグ情報付きのカーネルイメージ（`vmlinux`）が必要である。稼働中のシステムを解析する場合は、`/proc/kcore` などを通じてメモリを参照する。

主なコマンドは次のとおりである。`log` はカーネルのログバッファ（`dmesg` に相当）を表示し、クラッシュ直前のメッセージを確認する最初の手段となる。`bt` はタスクのカーネルスタックのバックトレースを表示し、クラッシュした箇所に至る関数呼び出しの経路を示す。`ps` はプロセスの一覧を、`files` はプロセスが開いているファイルを表示する。`struct` はカーネルの構造体の定義や、特定のアドレスにある構造体の中身を表示する。`kmem` はメモリの使用状況を、`dis` は関数の逆アセンブルを、`rd` は任意のアドレスのメモリの内容を表示する。`foreach` は、全タスクに対して同じコマンドを繰り返す。

## どこで出てくるか
カーネルのクラッシュの調査は、通常、`log` でパニックの原因となったメッセージ（不正なメモリアクセスやアサーションの失敗など）を確認し、`bt` でその時点の呼び出し経路を調べ、`struct` で関係するデータ構造の状態を確かめる、という手順で進む。デッドロックの調査では、`foreach bt` で全タスクのスタックを一覧し、どのタスクがどのロックを待っているかを調べる。

`crash` は長年にわたりカーネルのダンプ解析の標準的なツールとして用いられてきた。一方、決まったコマンドを組み合わせる操作が中心であるため、複雑なデータ構造をたどる定型的でない解析には向かない場面がある。そのような解析には、Pythonで解析を記述できる[[drgn]]が用いられる。

## 関係
- 使う / 使われる: [[kdump]]（解析対象のダンプを生成する）
- 対比: [[drgn]]（Pythonで解析を記述できる）
- 関連: [[Linux Kernel]], [[Ftrace]]

## 出典
- [crash(8) - Linux manual page](https://man7.org/linux/man-pages/man8/crash.8.html)
- [Crash Utility](https://crash-utility.github.io/)
- [Documentation for Kdump - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/kdump/kdump.html)
