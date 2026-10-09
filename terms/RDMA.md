---
aliases: [Remote Direct Memory Access, リモートダイレクトメモリアクセス, iWARP]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Network]]"]
status: draft
updated: 2026-10-10
---
# RDMA

> あるノードのメモリから別のノードのメモリへ、双方のOSを介さずに[[NIC|ネットワークアダプタ]]が直接データを転送する仕組みである。

## 概要
通常のTCP/IP通信では、送信データはアプリケーションのバッファからカーネルのバッファに複製され、プロトコル処理を経てネットワークアダプタに渡される。受信側でも同様の処理が逆向きに行われる。これらの処理は、[[System Call|システムコール]]の発行、データの複製、割り込みの処理を伴い、CPU時間と[[Latency|レイテンシ]]を消費する。RDMAでは、アプリケーションがネットワークアダプタに直接要求を渡し（カーネルバイパス）、アダプタがアプリケーションのメモリとネットワークの間でデータを直接転送する（ゼロコピー）。プロトコル処理もアダプタが担うため、CPUは転送の間、他の計算を進められる。

RDMAのプログラミングインタフェースは[[Verbs|verbs]]と呼ばれ、Linuxではlibibverbsとして提供される。通信の端点はキューペア（QP）であり、送信キューと受信キューからなる。アプリケーションは、作業要求（work request）をこれらのキューに投入し、その完了を完了キュー（CQ）から受け取る。転送に用いるメモリは、事前に `ibv_reg_mr()` で登録（memory registration）しておく必要がある。登録により、そのメモリは物理メモリ上に固定され、ローカルでの使用に用いる鍵（lkey）と、遠隔のノードがその領域にアクセスするための鍵（rkey）が発行される。登録の処理は高コストであるため、通常は通信の前にまとめて行い、使い回す。

操作には二種類がある。SEND/RECEIVEは、送信側のSENDに受信側があらかじめ投入したRECEIVEが対応する、両側の参加を要する通信である。RDMA WRITE/READは、rkeyを知っている側が、相手のCPUの関与なしに相手のメモリへ直接書き込み、あるいは読み出す片側通信である。比較交換（compare-and-swap）や加算（fetch-and-add）などの不可分な遠隔操作も提供される。

RDMAを提供するネットワーク技術としては、[[InfiniBand]]、Ethernet上でRDMAを実現する[[RoCE]]（RDMA over Converged Ethernet）、TCP上でRDMAを実現するiWARPがある。

## どこで出てくるか
HPCでは、[[MPI]]の実装がノード間の通信にRDMAを用いており、マイクロ秒程度の低いレイテンシと高い[[Bandwidth|バンド幅]]はこれによって実現されている。MPIの片側通信は、RDMA WRITE/READの考え方に直接対応する。ストレージでは、[[Lustre]]のネットワーク層LNet、[[NVMe-oF]]、並列ファイルシステムのクライアントとサーバ間の転送などに用いられる。研究の文脈では、片側通信によってサーバのCPUを介さずにデータへアクセスする分散データ構造やキーバリューストアが、盛んに設計されている。一方、メモリ登録のコスト、登録されたメモリの固定、接続ごとに必要なQPの資源などは、大規模化に伴う課題となる。

## 関係
- 前提: [[System Call]], [[Latency]]
- 使う / 使われる: [[InfiniBand]], [[RoCE]]（RDMAを提供するネットワーク）, [[Verbs]]（プログラミングインタフェース）, [[MPI]], [[Lustre]], [[NVMe-oF]]
- 関連: [[UCX]], [[Mercury]], [[Bandwidth]], [[io_uring]]

## 出典
- [Remote direct memory access - Wikipedia](https://en.wikipedia.org/wiki/Remote_direct_memory_access)
- [ibv_reg_mr(3) - Linux manual page](https://man7.org/linux/man-pages/man3/ibv_reg_mr.3.html)
- [ibv_post_send(3) - Linux manual page](https://man7.org/linux/man-pages/man3/ibv_post_send.3.html)
