---
aliases: [libzpoline, System Call Hook, システムコールフック, Syscall Hooking, システムコールの横取り, CHFS-zpoline, mmap_min_addr]
tags: [term]
maps: ["[[Operating System]]", "[[Storage]]"]
status: draft
updated: 2026-10-10
---
# zpoline

> x86-64のプログラムの `syscall` 命令をバイナリの書き換えによって置き換え、[[Linux Kernel|カーネル]]を改変せずに、全ての[[System Call|システムコール]]を小さな負担で横取りする仕組みである。

## 概要
zpolineは、IIJ技術研究所のKenichi Yasukata、Hajime Tazaki、Pierre-Louis Aublinと、法政大学のKenta Ishiguroが、2023年のUSENIX ATCで発表した。Linux、FreeBSD、NetBSD、DragonFly BSDで動作が確認されている。アプリケーションのシステムコールを横取り（フック）して別の処理に差し替える仕組みは、トレースのツール、サンドボックス、ユーザ空間で実装したファイルシステムやネットワークスタックをアプリケーションから透過的に使わせる場合などに用いられる。しかし、既存の方法には欠点があった。`ptrace` などのカーネルの機能を用いる方法は負担が大きい。`LD_PRELOAD` で標準ライブラリの関数を差し替える方法は、ライブラリを経ずに直接発行されるシステムコールを捕まえられない。

x86-64のシステムコールは、`rax` レジスタにシステムコールの番号（`read` は0、`write` は1など）を入れて、2バイトの `syscall` 命令を実行することで発行される。2バイトでは、任意のフック関数への跳躍命令に書き換えることが難しい。zpolineは、`syscall` を同じ2バイトの `callq *%rax` に置き換える。`rax` には必ずシステムコールの番号が入っているため、この命令は0から最大のシステムコールの番号（約500）までのいずれかのアドレスに飛ぶ。そこで、[[Virtual Memory|仮想アドレス]]0から始まる領域を1バイトの `nop` 命令で埋め、その末尾にフック関数へ飛ぶコードを置く（トランポリン）。どの番号から入っても、`nop` を滑り降りてフック関数に至る。名前は、アドレス0（zero）のトランポリンに由来する。書き換えは、プログラムの `main` が始まる前にメモリ上で行われ、元の実行ファイルは変更されない。

この方法では、本来はプログラムの誤りとして停止させるべき、アドレス0（NULLポインタ）へのアクセスが許されてしまう。zpolineは、トランポリンの領域を実行のみ可能なメモリにするなどして、NULLポインタの読み書きと実行を検出できるようにしている。論文では、全てのシステムコールを横取りできる既存の方法と比べて、横取りの負担が28.1〜761.0分の1であったと報告している。

## どこで出てくるか
zpolineは、Linuxでは `LD_PRELOAD` で `libzpoline.so` を読み込み、フックの処理を実装した共有ライブラリを環境変数 `LIBZPHOOK` で指定して用いる。仮想アドレス0に領域を確保するため、`/proc/sys/vm/mmap_min_addr` を0に設定する必要がある。この設定は、カーネルのNULLポインタの参照の不具合に対する多層防御として、ユーザのプロセスがアドレス0付近に領域を確保することを禁じる制限を外すものである。SELinuxが有効な環境では、それを無効にする必要がある場合もある。いずれも安全性を下げるため、利用する計算機の管理者の判断を要する。

ストレージの研究では、ユーザ空間で実装したファイルシステムを、アプリケーションを改変せずに使わせる手段として用いられる。例えば、[[CHFS]]は、zpolineを用いてファイル操作のシステムコールを横取りするCHFS-zpolineを提供している。同じ目的で、[[GekkoFS]]や[[UnifyFS]]はクライアントのライブラリでファイル操作の呼び出しを横取りし、[[FUSE]]はカーネルを経由してユーザ空間のデーモンに要求を渡す。

## 関係
- 前提: [[System Call]]
- 使う / 使われる: [[CHFS]]
- 対比: [[FUSE]]（カーネルを経由してユーザ空間のファイルシステムに要求を渡す）, [[strace]]（ptraceによりシステムコールを追跡する）
- 関連: [[Ad Hoc File System]], [[Linux Kernel]]

## 出典
- [zpoline: a system call hook mechanism based on binary rewriting - USENIX ATC 2023](https://www.usenix.org/conference/atc23/presentation/yasukata)
- [論文PDF](https://www.usenix.org/system/files/atc23-yasukata.pdf)
- [yasukata/zpoline - GitHub](https://github.com/yasukata/zpoline)
- [Documentation for /proc/sys/vm/ - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/sysctl/vm.html)（mmap_min_addr）
