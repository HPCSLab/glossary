---
aliases: [GPU Direct RDMA, GPUDirect, GDR, GPUDirect RDMA (GDR), nvidia-peermem, peer-to-peer DMA]
tags: [term]
maps: ["[[Network]]", "[[Parallel Computing]]", "[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# GPUDirect RDMA

> NICなどの[[PCIe]]の装置が、ホストのメモリを経由せずに、[[GPU]]のメモリを直接読み書きできるようにするNVIDIAの技術である。

## 概要
GPUDirect RDMAは、Keplerの世代のGPUとCUDA 5.0で導入された。GPUのメモリは、PCIeのBAR（Base Address Register）と呼ばれるアドレスの窓を通じて、PCIeのアドレス空間に見せることができる。GPUDirect RDMAは、この仕組みを用いて、同じPCIeの階層にあるネットワークのアダプタやストレージのアダプタなどの他の装置が、GPUのメモリに直接DMAで読み書きすることを可能にする。

GPUDirect RDMAがない場合、GPUのデータをネットワークで送るには、まずGPUのメモリからホストのメモリにデータを複製し、それをNICが送信する必要がある。GPUDirect RDMAを用いると、NICがGPUのメモリから直接データを読み出して送り、受信側でも直接GPUのメモリに書き込めるため、ホストのメモリを経由する複製と、それに伴うCPUの処理が不要になる。[[InfiniBand]]や[[RoCE]]のアダプタでは、カーネルモジュール `nvidia-peermem` が、アダプタからGPUのメモリへの直接のアクセスを可能にする。

## どこで出てくるか
GPUDirect RDMAは、複数のノードのGPUを用いる計算で、[[RDMA]]による通信を用いてGPUのメモリの間のデータをホストのメモリを経由せずに転送するために用いられる。NICに限らず、[[NVMe]] SSDからGPUのメモリへの直接の転送にも用いられ、[[GPUDirect Storage]]や[[BaM]]は、SSDとGPUの間の直接の転送にGPUDirect RDMAの技術を用いている。

利用には条件がある。GPUと相手の装置が同じPCIeのルートコンプレックスの下にある必要があり、[[IOMMU]]は無効にするか、アドレスを変換しない設定にする必要がある。計算機のPCIeの構成によっては使えないことがあるため、利用する計算機の構成を確かめる必要がある。

## 関係
- 前提: [[RDMA]], [[GPU]]
- 使う / 使われる: [[InfiniBand]], [[RoCE]], [[CUDA]]
- 関連: [[GPUDirect Storage]], [[BaM]], [[Verbs]]

## 出典
- [GPUDirect RDMA - NVIDIA Documentation](https://docs.nvidia.com/cuda/gpudirect-rdma/index.html)
- [BaM: GPU-Initiated On-Demand High-Throughput Storage Access (Qureshi et al., ASPLOS 2023) - arXiv](https://arxiv.org/abs/2203.04910)
