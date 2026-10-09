---
aliases: [Direct Memory Access, ダイレクトメモリアクセス, DMA API, dma_map_single, Pinned Memory, ピン留めメモリ, Page-locked Memory]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# DMA（Direct Memory Access）

> CPUが一語ずつデータを運ぶ代わりに、周辺装置が主記憶を直接読み書きしてデータを転送する仕組みである。

## 概要
[[NIC]]、[[SSD]]、[[GPU]]などの装置と主記憶との間で大量のデータを移すとき、CPUが装置のレジスタとメモリの間でデータを一語ずつ複製していては、CPUの時間が転送に費やされる。DMAでは、CPU（ドライバ）は転送元・転送先のアドレスと大きさを装置に伝えるだけであり、実際のデータの移動は装置が[[PCIe]]などを介して行う。転送の完了は割り込みか、CPUによる完了の確認（ポーリング）で知らされる。

装置は、CPUの[[Virtual Memory|仮想記憶]]を通らずにメモリにアクセスするため、ドライバはカーネルの仮想アドレスではなく、装置から見えるアドレス（DMAアドレス）を装置に渡す必要がある。[[Linux Kernel|Linux]]では、`dma_map_single()` などのDMA APIがこの変換を行い、[[IOMMU]]がある場合はその対応付けもこのときに作られる。また、DMAの途中で転送先のページが退避されたり移動されたりしてはならないため、ユーザ空間のメモリをDMAに用いる場合は、そのページを物理的な位置に固定（ピン留め）する。

## どこで出てくるか
高速なI/Oの技術の多くは、DMAをどう使うかの工夫である。[[NVMe]]のSSDやNICは、要求の記述子を置いたキューとデータのバッファをDMAで読み書きする。[[CUDA]]では、ホストとGPUの間の非同期な転送にピン留めした（page-locked）ホストのメモリが必要であり、ピン留めしたメモリは最も高い転送[[Bandwidth|帯域]]を得られる。[[RDMA]]は、NICが相手の計算機のメモリをDMAで直接読み書きする通信であり、[[GPUDirect RDMA]]と[[GPUDirect Storage]]は、NICやSSDがGPUのメモリへ直接DMAで転送することで、ホストのメモリを経由する複製を省く。

## 関係
- 前提: [[PCIe]], [[Virtual Memory]]
- 使う / 使われる: [[NVMe]], [[NIC]], [[RDMA]], [[GPUDirect RDMA]], [[GPUDirect Storage]], [[IOMMU]]

## 出典
- [Dynamic DMA mapping Guide - The Linux Kernel documentation](https://docs.kernel.org/core-api/dma-api-howto.html)
- [Network interface controller - Wikipedia](https://en.wikipedia.org/wiki/Network_interface_controller)
- [CUDA C++ Best Practices Guide - NVIDIA](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html)
