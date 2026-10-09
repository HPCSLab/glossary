---
aliases: [Unified Communication X, OpenUCX, UCP, UCT, UCS, UCX_TLS]
tags: [term]
maps: ["[[Network]]"]
status: draft
updated: 2026-10-10
---
# UCX

> 多様な高速ネットワークと共有メモリ、GPUメモリを共通のAPIで扱えるようにする、HPCとデータ処理のための通信フレームワークである。正式名称は Unified Communication X である。

## 概要
UCXは、[[InfiniBand]]や[[RoCE]]の[[RDMA]]、ノード内の共有メモリ、TCP、[[GPU]]のメモリ（CUDAやROCm）など、性質の異なる複数の転送手段を抽象化し、上位のソフトウェアから統一的に利用できるようにする。それぞれのハードウェアの能力（RDMAの読み書き、ネットワークによる不可分操作など）を活かしつつ、利用可能な手段の中から適したものを自動的に選ぶ。

UCXは三つの層からなる。UCT（transport）は、各転送手段（[[Verbs|verbs]]、共有メモリなど）を薄く包む低水準の層である。UCP（protocol）は、その上に、タグ付きの送受信、遠隔メモリへのアクセス、ストリーム、不可分操作などの高水準の通信を実装し、メッセージの大きさや宛先に応じて、どの転送手段とプロトコルを使うかを選択する。UCS（services）は、両者が共通に用いるデータ構造や補助機能を提供する。

## どこで出てくるか
UCXは、[[Open MPI]]や[[MPICH]]といった[[MPI]]の実装の通信層として広く用いられている。そのため、利用者がUCXを直接呼ぶことは少ないが、MPIの性能や挙動を調べる際には、その下でUCXが動いていることを意識する必要がある。例えば、環境変数 `UCX_TLS` で使用する転送手段を明示的に指定したり、`ucx_info` で利用可能な転送手段を確認したりできる。通信の性能が想定より低い場合、意図しない転送手段（例えばRDMAの代わりにTCP）が選ばれていることが原因であることがある。GPU間の通信では、GPUのメモリを直接扱えるかどうかが性能を大きく左右する。

## 関係
- 上位概念: [[RDMA]]
- 使う / 使われる: [[Verbs]], [[InfiniBand]], [[RoCE]], [[GPU]]（転送手段）, [[MPI]]（UCXを使う）
- 対比: [[Mercury]]（RPCのためのフレームワーク）
- 関連: [[Latency]], [[Bandwidth]]

## 出典
- [OpenUCX documentation](https://openucx.readthedocs.io/en/master/)
