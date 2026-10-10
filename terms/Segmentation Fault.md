---
aliases: [SEGV, SIGSEGV, segfault, セグメンテーション違反, セグメンテーションフォルト, セグフォ]
tags: [term]
maps: ["[[Operating System]]", "[[Programming]]"]
status: draft
updated: 2026-10-10
---
# Segmentation Fault（セグメンテーション違反）

> プロセスが許されていないメモリ参照を行ったときに、カーネルがそのプロセスに `SIGSEGV` シグナルを送って知らせる異常である。

## 概要
[[Process|プロセス]]は[[Virtual Memory|仮想メモリ]]上のアドレスを通じてメモリにアクセスする。アクセスしたアドレスに有効な対応がない場合、CPUはページフォルトを起こして[[Linux Kernel|カーネル]]に処理を移す。カーネルはそれが正当なアクセスであれば物理ページを用意して実行を続けさせるが、正当でなければ、アクセスした[[Thread|スレッド]]に `SIGSEGV`（Linuxでは11番）を送る。`sigaction(2)` によれば、原因は `si_code` で区別され、どこにも写像されていないアドレスへのアクセス（`SEGV_MAPERR`）と、写像されてはいるが権限のないアクセス（`SEGV_ACCERR`、読み出し専用の領域への書き込みなど）が代表的である。前者の典型はNULLポインタの参照、解放済みや範囲外の領域へのアクセスであり、ほかにスタックを使い切った場合（深すぎる再帰など）にも `SIGSEGV` が送られる。ただし、範囲外のアクセスでも、たまたま写像されている領域に当たれば `SIGSEGV` は起きず、データを黙って壊す。したがって、segfaultが起きないことはメモリ操作が正しいことを意味しない。

`SIGSEGV` の既定の動作はプロセスの終了とコアダンプ（core）である。シェルはシグナル N で終了したコマンドの終了ステータスを 128+N とするため、bashでは 139 となる。コアファイルが実際に書き出されるかは、`ulimit -c`（`RLIMIT_CORE`）と `/proc/sys/kernel/core_pattern` の設定による。systemdを用いるシステムでは、コアダンプは `systemd-coredump` に渡されて保存され、`coredumpctl` で一覧できる。シグナルハンドラで `SIGSEGV` を捕捉することもできるが、[[POSIX]]では、ハードウェア例外による `SIGSEGV` を無視した後のプロセスの動作は未定義である。スタックを使い切ったことによる `SIGSEGV` は、通常のスタックではハンドラを実行できないため、`sigaltstack(2)` で用意した別のスタックでしか捕捉できない。

## どこで出てくるか
[[C]]やC++で書いたプログラム、またはそれらで書かれたライブラリを呼ぶ[[Python]]などのプログラムが、`Segmentation fault (core dumped)` と表示して異常終了する場面で出会う。調査の最初の手順は、[[gdb]]の中で実行するかコアファイルを読み込み、`bt` で落ちた箇所のコールスタックを確かめることである。落ちた箇所と原因の箇所が離れている場合（先に別の場所でメモリを壊していた場合）には、AddressSanitizer（`-fsanitize=address`）を付けてビルドし直すと、範囲外アクセスや解放後の使用を、それが起きた時点で検出できる。[[Rust]]は、安全なコードの範囲ではこの種のメモリ誤りを型検査で排除することを目的に設計されている。

## 関係
- 前提: [[Virtual Memory]], [[Process]]
- 使う / 使われる: [[gdb]]（原因の箇所を調べる）
- 関連: [[C]], [[Rust]]

## 出典
- [signal(7) - Linux manual page](https://man7.org/linux/man-pages/man7/signal.7.html)
- [sigaction(2) - Linux manual page](https://man7.org/linux/man-pages/man2/sigaction.2.html)
- [sigaltstack(2) - Linux manual page](https://man7.org/linux/man-pages/man2/sigaltstack.2.html)
- [core(5) - Linux manual page](https://man7.org/linux/man-pages/man5/core.5.html)
- [AddressSanitizer - Clang documentation](https://clang.llvm.org/docs/AddressSanitizer.html)
