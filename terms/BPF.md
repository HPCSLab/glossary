---
aliases: [eBPF, Extended BPF, Berkeley Packet Filter, BSD Packet Filter, cBPF, bcc, libbpf, XDP, sched_ext]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# BPF

> 利用者が作成した小さなプログラムを、安全性を検証したうえでLinuxカーネル内で実行させる仕組みである。現在は主に拡張版のeBPFを指す。

## 概要
BPFの起源は、1992年にMcCanneとJacobsonが発表したBSD Packet Filterである。これは、`tcpdump` などのパケットキャプチャで、受信したパケットのうち必要なものだけをカーネル内で選別するための、簡素な仮想機械であった。Linuxは2014年のLinux 3.18で `bpf()` [[System Call|システムコール]]を導入し、命令セットを拡張したeBPF（extended BPF）を整備した。eBPFは、パケットの選別にとどまらず、カーネルの様々な箇所で任意の処理を行える汎用の実行基盤へと発展したため、BPFという名称はもはや字義どおりの意味を持たない。旧来の方式は、区別のためにcBPF（classic BPF）と呼ばれる。

eBPFのプログラムは、通常、C言語などで記述してBPFのバイトコードにコンパイルし、`bpf()` でカーネルに読み込む。読み込み時には、カーネル内の検証器（verifier）がプログラムを静的に解析し、必ず終了すること、範囲外や未初期化のメモリにアクセスしないことなどを確認する。検証を通らないプログラムは拒否される。検証後のプログラムはJITコンパイルによって機械語に変換され、カーネルのネイティブなコードと同等の速度で動作する。この検証の仕組みにより、カーネルモジュールのようにカーネル全体を危険にさらすことなく、カーネルの振る舞いを拡張できる。

プログラムは、カーネル内の決められた箇所（フック）に取り付けられ、その箇所を処理が通過するたびに実行される。フックには、システムコール、トレースポイント、任意のカーネル関数の入口と出口（kprobe）、ユーザプログラムの関数（uprobe）、ネットワークのパケット受信処理（XDP）などがある。プログラムはカーネルの任意の関数を呼べず、ヘルパ関数と呼ばれる定められたAPIのみを利用できる。プログラムとユーザ空間、あるいはプログラム同士の間のデータの受け渡しには、マップと呼ばれるハッシュ表や配列、リングバッファなどのデータ構造を用いる。[[BTF]]と呼ばれる型情報を用いたCO-REの仕組みにより、一度コンパイルしたプログラムを異なるバージョンのカーネルで動作させることもできる。

## どこで出てくるか
最も身近な用途は、性能解析と観測（トレーシング）である。bccや[[bpftrace]]を用いると、稼働中のシステムを停止・改変することなく、[[Block Storage|ブロックデバイス]]のI/Oの[[Latency|レイテンシ]]分布、どのプロセスがどのファイルを[[open]]したか、[[System Call|システムコール]]ごとの所要時間などを集計できる。例えば、`biolatency` はブロックI/Oのレイテンシのヒストグラムを、`opensnoop` はファイルのオープンを一覧する。ネットワークでは、XDPによる高速なパケット処理やロードバランサ、コンテナのネットワーク制御に用いられ、セキュリティでは、システムコールの監視や制限に用いられる。

研究の文脈では、eBPFはカーネルを改変せずにその方針を差し替える手段として注目されている。Linux 6.12で導入されたsched_extは、プロセスのスケジューリング方針をBPFプログラムで定義できるようにした。ストレージでは、[[NVMe]]ドライバにBPFのフックを設け、B木の探索のように前の読み込み結果に応じて次の読み込みが決まる処理を、ドライバ内で連鎖的に実行してカーネルの上位層の処理を省くXRP（OSDI 2022）などが提案されている。

## 関係
- 前提: [[System Call]]
- 使う / 使われる: [[Latency]]（観測の対象）, [[NVMe]]（XRP）
- 関連: [[VFS]], [[blk-mq]], [[io_uring]], [[FUSE]]

## 出典
- [What is eBPF? - ebpf.io](https://ebpf.io/what-is-ebpf/)
- [bpf(2) - Linux manual page](https://man7.org/linux/man-pages/man2/bpf.2.html)
- [The BSD Packet Filter: A New Architecture for User-level Packet Capture (McCanne and Jacobson, 1992)](https://www.tcpdump.org/papers/bpf-usenix93.pdf)
- [Extensible Scheduler Class - The Linux Kernel documentation](https://docs.kernel.org/scheduler/sched-ext.html)
- [Linux 6.12 - Kernel Newbies](https://kernelnewbies.org/Linux_6.12)
- [XRP: In-Kernel Storage Functions with eBPF - USENIX OSDI 2022](https://www.usenix.org/conference/osdi22/presentation/zhong)
