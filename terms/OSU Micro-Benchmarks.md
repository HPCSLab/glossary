---
aliases: [OMB, OSU Benchmarks, osu_latency, osu_bw, OSUマイクロベンチマーク]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Network]]"]
status: draft
updated: 2026-10-10
---
# OSU Micro-Benchmarks（OMB）

> [[MPI]]などの通信ライブラリについて、二プロセス間の通信や[[Collective Communication|集団通信]]の[[Latency|レイテンシ]]と[[Bandwidth|バンド幅]]を、メッセージサイズごとに測る小さなベンチマークの集まりである。

## 概要
OMBは、オハイオ州立大学のNetwork-Based Computing Laboratoryが、MPIの実装である[[MVAPICH]]とともに開発・配布しているベンチマーク集であり、BSDライセンスで公開されている。MVAPICH専用ではなく、[[Open MPI]]や[[MPICH]]など他のMPIライブラリと組み合わせても用いられる。アプリケーション全体ではなく、通信の操作一つを繰り返し実行してその性能だけを測るため「マイクロベンチマーク」と呼ばれる。結果はメッセージサイズを倍々に増やした表として出力され、小さなメッセージではレイテンシが、大きなメッセージではバンド幅が性能を決めることを読み取れる。

代表的なものは二プロセス間の通信を測る `osu_latency` と `osu_bw` である。`osu_latency` はメッセージを交互に送り返すピンポン方式で往復時間を測り、片方向のレイテンシを報告する。`osu_bw` は送信側が一定数（ウィンドウ）のメッセージを続けて送り、受信側がすべてを受け取ってから応答する方式で、持続的に得られる最大のバンド幅を測る。このほか、双方向のバンド幅（`osu_bibw`）、複数の組による合計のバンド幅とメッセージレート（`osu_mbw_mr`）、`osu_allreduce` などの集団通信、`MPI_Put` などの片側通信、`MPI_Init` にかかる時間を測るものがある。MPIのほか、[[OpenSHMEM]]、[[PGAS]]の言語であるUPCとUPC++、[[NCCL]]向けのベンチマークも含む。[[CUDA]]やROCmを有効にしてビルドすると、通信バッファを[[GPU]]のメモリに置いて測定でき、二プロセス間の測定では各ランクのバッファをホスト（`H`）とデバイス（`D`）のどちらに置くかを引数で指定する。

## どこで出てくるか
新しいクラスタやネットワークの性能を確かめるとき、MPIの実装や設定（[[UCX]]の通信経路の選択など）を比べるとき、論文で通信の基本性能を示すときに用いられる。[[InfiniBand]]の性能確認では、[[Verbs|verbs]]のレベルで測るperftestと並んで、MPIのレベルの性能をOMBで測るのが一般的である。両者の差が、MPIのライブラリによるオーバーヘッドを示す。

結果を読むときは、二つのプロセスが同じノードにあるか別のノードにあるか、どのCPUコアやGPUに割り当てられたか（[[NUMA]]の配置）を必ず確認する。同じノード内の通信は共有メモリを通るためネットワークを測っていないことになり、配置によって値が大きく変わるためである。

## 関係
- 使う / 使われる: [[MPI]], [[NCCL]], [[OpenSHMEM]]
- 対比: [[IOR]]（OMBが通信を測るのに対し、並列I/Oの性能を測る）
- 関連: [[Latency]], [[Bandwidth]], [[InfiniBand]], [[MVAPICH]]

## 出典
- [OSU Micro-Benchmarks - MVAPICH](https://mvapich.cse.ohio-state.edu/benchmarks/)
