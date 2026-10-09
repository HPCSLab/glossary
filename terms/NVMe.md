---
aliases: [NVM Express, NVMe SSD, Namespace, 名前空間]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# NVMe

> [[PCIe|PCI Express]] に接続された不揮発性記憶装置（主に[[SSD]]）にアクセスするための、論理デバイスインタフェースの規格である。

## 概要
NVMe（NVM Express）は、2011年に1.0版が公開された。それ以前のSSDは、[[HDD]]のために設計されたSATA/AHCIなどのインタフェースで接続されていた。AHCIはコマンドキューを一つしか持たず、そのキューに入るコマンドも32個までであり、[[Latency|低遅延]]で内部の並列性が高いフラッシュメモリの性能を活かしきれなかった。NVMeは、最大65535個のI/Oキューと、キューあたり最大65536個のコマンドを扱えるように設計されている。

NVMeの通信は、ホストのメモリ上に置かれた投入キュー（Submission Queue）と完了キュー（Completion Queue）の対を介して行われる。ホストはコマンドを投入キューに書き込み、デバイスのドアベルレジスタに書き込んで到着を通知する。デバイスはコマンドを処理し、結果を完了キューに書き込む。キューを多数持てるため、OSはCPUコアごとに専用のキューの対を割り当て、コア間でロックを共有せずに並列にI/Oを発行できる。Linuxでは、この構造が[[blk-mq]]のハードウェアキューと対応付けられる。一台のデバイスの記憶領域は、名前空間（namespace）と呼ばれる複数の論理的な[[Block Storage|ブロックデバイス]]に分割でき、Linuxでは `/dev/nvme0n1`（0番目のコントローラの1番目の名前空間）のように現れる。

NVMeのコマンド体系をネットワーク越しに用いる規格として、[[NVMe-oF|NVMe over Fabrics（NVMe-oF）]]がある。転送路としては、[[RDMA]]（[[InfiniBand]]や[[RoCE]]）、Fibre Channel、TCPが規定されており、リモートのSSDをローカルに近い低遅延で利用できる。

## どこで出てくるか
現在の高性能なストレージは、ほぼNVMe SSDで構成されている。単体のNVMe SSDでも数十万から百万を超えるIOPSを達成しうるため、その性能を引き出すには、OS側のオーバーヘッドの削減が重要となる。[[io_uring]]による多数の要求の同時発行や、ブロック層の処理の効率化は、この要請に応えるものである。[[Little's Law|リトルの法則]]のとおり、高いIOPSを得るには十分な数の要求を同時に発行する必要があり、ベンチマークではキューの深さ（queue depth）が主要なパラメータとなる。HPCでは、[[Compute Node|計算ノード]]に搭載したNVMe SSDを一時的な高速記憶（[[Ad Hoc File System|バーストバッファ]]など）として用いる構成や、NVMe-oFによるストレージの分離（disaggregation）が研究・実用されている。

## 関係
- 上位概念: [[Block Storage]]
- 使う / 使われる: [[blk-mq]], [[io_uring]]
- 対比: [[HDD]]
- 関連: [[SSD]], [[RDMA]], [[Latency]], [[Little's Law]]

## 出典
- [NVM Express - Wikipedia](https://en.wikipedia.org/wiki/NVM_Express)
- [NVM Express](https://nvmexpress.org/)
