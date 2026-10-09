---
aliases: [Kdump, kexec, Crash Dump, クラッシュダンプ, vmcore, /proc/vmcore, crashkernel, makedumpfile, Kernel Panic, カーネルパニック]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# kdump

> Linuxカーネルがクラッシュした際に、その時点のメモリの内容をダンプファイルとして保存するための仕組みである。

## 概要
カーネルがパニックなどで停止すると、通常はその時点の状態が失われ、原因を調べる手掛かりが残らない。kdumpは、kexecと呼ばれる、ファームウェアを経由せずに稼働中のカーネルから別のカーネルを直接起動する機能を用いて、この問題を解決する。

準備として、通常のカーネル（システムカーネル）の起動時に、カーネルの起動オプション `crashkernel=` でメモリの一部を予約しておき、`kexec -p` でその領域にダンプ取得用の別のカーネル（キャプチャカーネル）を読み込んでおく。システムカーネルがクラッシュすると、キャプチャカーネルが予約領域で直ちに起動する。このとき、システムカーネルが使っていたメモリの内容は消去されずに残っており、キャプチャカーネルはそれをELF形式のファイル `/proc/vmcore` として参照できる。これをディスクやネットワーク越しに保存したものがダンプファイル（vmcore）である。予約領域はキャプチャカーネルの起動前から確保されているため、壊れたシステムカーネルの影響を受けにくい。

メモリをそのまま保存すると、ダンプファイルは搭載メモリと同じ大きさになる。`makedumpfile` は、0のみのページ、ページキャッシュ、ユーザプロセスのページ、空きページなど、カーネルの解析に不要なページを除外し、さらに圧縮することで、ダンプファイルを大幅に小さくする。除外するページの種類はダンプレベル（`-d`）で指定する。多くのディストリビューションでは、kdumpのサービスを有効にすれば、これらの設定と保存の処理が自動で行われ、ダンプファイルは `/var/crash/` 以下に保存される。

## どこで出てくるか
kdumpは、本番のサーバや計算機でカーネルのクラッシュが起きた際の原因調査の出発点であり、取得したvmcoreは[[crash]]や[[drgn]]で解析する。カーネルやファイルシステム、ドライバを改変する研究では、自分の変更がカーネルをクラッシュさせることが避けられないため、開発用の環境（[[Virtual Machine|仮想マシン]]など）で事前にkdumpを設定しておくと、再現の難しい不具合の原因を後から調べられる。設定が正しく動作するかは、`echo c > /proc/sysrq-trigger` で意図的にクラッシュを起こして確認できる。ただし、これは実際にシステムを停止させるため、共用の計算機で行ってはならない。

## 関係
- 前提: [[Linux Kernel]]
- 使う / 使われる: [[crash]], [[drgn]]（vmcoreを解析する）
- 関連: [[Page Cache]]（makedumpfileが除外する）

## 出典
- [Documentation for Kdump - The kexec-based Crash Dumping Solution - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/kdump/kdump.html)
- [makedumpfile - GitHub](https://github.com/makedumpfile/makedumpfile)
