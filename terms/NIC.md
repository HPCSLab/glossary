---
aliases: [Network Interface Controller, Network Interface Card, ネットワークインタフェースカード, ネットワークカード, ネットワークアダプタ, HCA, Host Channel Adapter, RSS, Receive Side Scaling, マルチキュー]
tags: [term]
maps: ["[[Network]]"]
status: draft
updated: 2026-10-10
---
# NIC（Network Interface Controller）

> 計算機をネットワークに接続するためのハードウェアであり、EthernetやInfiniBandなどの物理層とデータリンク層の処理を担う。

## 概要
NICは、計算機の内部では[[PCIe]]で接続され、外部ではネットワークのケーブルを通じてスイッチにつながる。Ethernetでは各NICにMACアドレスが割り当てられる。送受信するパケットは、NICが[[DMA]]で主記憶のバッファとの間で直接転送し、CPUは送受信の記述子をキューに置くだけでよい。パケットの到着は、割り込みかCPUによるポーリングで検出する。

高速なNICは、複数の送信キューと受信キューを持つ（マルチキュー）。受信したパケットはヘッダのハッシュ値に応じて受信キューに振り分けられ（RSS: Receive Side Scaling）、キューごとに別の割り込みを持つため、複数のCPUコアで受信の処理を分担できる。[[InfiniBand]]のNICは、HCA（Host Channel Adapter）と呼ばれる。

## どこで出てくるか
HPCのクラスタでは、[[Compute Node|計算ノード]]のNICの性能と数が、[[MPI]]の通信や[[Parallel File System|並列ファイルシステム]]へのI/Oの[[Bandwidth|帯域]]を左右する。[[RDMA]]に対応したNIC（NVIDIAのConnectXなど）は、通信の処理をハードウェアで行い、カーネルを経由せずにアプリケーションから直接操作できる。これに対し、[[DPDK]]は通常のNICをユーザ空間のドライバでポーリングして高速化する。NICに汎用のCPUコアを加えて、ホストの処理を肩代わりできるようにしたものが[[DPU]]（SmartNIC）である。また、[[SR-IOV]]を用いると一つのNICを複数の仮想的なNICに分けて[[Virtual Machine|仮想マシン]]に割り当てられる。

## 関係
- 前提: [[PCIe]], [[DMA]]
- 使う / 使われる: [[RDMA]], [[DPDK]], [[SR-IOV]], [[GPUDirect RDMA]]
- 関連: [[InfiniBand]], [[RoCE]], [[DPU]]

## 出典
- [Network interface controller - Wikipedia](https://en.wikipedia.org/wiki/Network_interface_controller)
- [Scaling in the Linux Networking Stack - The Linux Kernel documentation](https://docs.kernel.org/networking/scaling.html)
