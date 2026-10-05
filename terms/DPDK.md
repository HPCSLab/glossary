---
aliases: [dpdk, Data Plane Development Kit, PMD, Poll Mode Driver, EAL, Environment Abstraction Layer, mbuf, rte_ring]
tags: [term]
maps: ["[[Network]]"]
status: draft
updated: 2026-10-06
---
# DPDK（Data Plane Development Kit）

> ネットワークのパケットを、カーネルのネットワークスタックを経由せずにユーザ空間で高速に処理するための、ライブラリとドライバの集まりである。

## 概要
DPDKは、Intelの技術者Venky Venkatesanが作り、2013年にオープンソースとなった。現在はLinux Foundationのプロジェクトとして運営され、BSDライセンスで公開されている。

通常、受信したパケットは、NICの割り込みを契機にカーネルのネットワークスタックで処理され、アプリケーションのバッファに複製される。DPDKは、パケットの処理をユーザ空間のプロセスに移し、カーネルとの間の複製をなくす。NICは、ポーリングモードドライバ（PMD）によって操作され、PMDは割り込みを用いずに、パケットの到着を繰り返し確かめる。処理の形には、一つのCPUのコアがパケットを最初から最後まで処理するrun-to-completionと、処理を段階に分け、コアの間でリングを介してパケットを受け渡すpipelineがある。

DPDKは、環境の違いを隠す抽象化の層（EAL）で、CPUのコアへの割り当てやメモリの確保を管理する。コアの間の受け渡しには、ロックを用いない[[Ring Buffer|リングバッファ]]（rte_ring）を用い、パケットのバッファ（mbuf）はあらかじめ確保した領域から取り出す。メモリには[[Virtual Memory|ヒュージページ]]を用いる。ページの数が減ることで、仮想アドレスを物理アドレスに変換するTLBの不足が起きにくくなり、性能が上がるためである。

## どこで出てくるか
DPDKは、データプレーン（パケットの転送の処理）のアプリケーションを高速に動かすために用いられる。ストレージでは、[[SPDK]]がDPDKのライブラリを基盤として用いている。DPDKとSPDKはいずれも、カーネルを経由せず、割り込みの代わりにポーリングを用いて高い性能を得る、カーネルバイパスの例である。同じくカーネルを経由しない通信の手段として、[[RDMA]]がある。

## 関係
- 使う / 使われる: [[SPDK]], [[Ring Buffer]]
- 対比: [[RDMA]]（NICのハードウェアがデータ転送を担う）, [[BPF]]（XDPによるカーネル内のパケット処理）
- 関連: [[Virtual Memory]]（ヒュージページとTLB）, [[DPU]]

## 出典
- [Overview - DPDK Programmer's Guide](https://doc.dpdk.org/guides/prog_guide/overview.html)
- [System Requirements - DPDK Getting Started Guide for Linux](https://doc.dpdk.org/guides/linux_gsg/sys_reqs.html)
- [Data Plane Development Kit - Wikipedia](https://en.wikipedia.org/wiki/Data_Plane_Development_Kit)
