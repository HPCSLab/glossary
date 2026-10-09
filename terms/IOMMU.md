---
aliases: [Input-Output Memory Management Unit, I/O MMU, VT-d, AMD-Vi, VFIO, vfio-pci, IOMMU group]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# IOMMU

> 周辺装置が[[DMA]]で主記憶を読み書きする際のアドレスを変換し、装置がアクセスできるメモリの範囲を制限するハードウェアである。

## 概要
[[GPU]]、[[SSD]]、[[NIC]]などの[[PCIe]]の装置は、CPUを介さずに主記憶を直接読み書きするDMAによってデータを転送する。何の制限もなければ、装置は任意の物理アドレスを読み書きできるため、誤動作した装置やドライバがカーネルのメモリを破壊しうる。IOMMUは、CPUのMMUが[[Virtual Memory|仮想記憶]]で[[Process|プロセス]]のアドレスを変換するのと同じように、装置から見えるアドレス（IOVA）を物理アドレスに変換し、許可された範囲以外へのアクセスを拒否する。[[Linux Kernel|Linux]]では、ドライバがDMAの前に `dma_map_*()` で対応付けを作り、使い終わると `dma_unmap_*()` で解除する。

IntelはVirtualization Technology for Directed I/O（VT-d）、AMDはI/O Virtualization Technology（AMD-Vi）という名前の仕様でIOMMUを提供している。IOMMUが互いに分離できる装置の最小の集まりをIOMMU groupと呼ぶ。PCIeの接続の構成によっては、複数の装置が一つのgroupにまとめられ、個別には分離できない。

## どこで出てくるか
IOMMUの代表的な用途は、装置を安全にカーネルの外に渡すことである。Linuxの VFIO（`vfio-pci` ドライバ）は、IOMMUによる保護の下で、装置をユーザ空間のプログラムや[[Virtual Machine|仮想マシン]]に直接使わせる仕組みである。仮想マシンにGPUやNICを直接割り当てる（パススルー）場合や、[[SPDK]]や[[DPDK]]がユーザ空間のドライバで[[NVMe]] SSDやNICを扱う場合に用いる。

一方、装置同士が直接データをやり取りする技術では、IOMMUが障害になることがある。[[GPUDirect RDMA]]は、GPUと相手の装置から見える物理アドレスが同一であることを前提とするため、IOMMUを無効にするか、1対1の対応付けをするパススルーの設定（Linuxの起動オプション `iommu=pt` など）にする必要がある。[[BaM]]も同様にIOMMUの無効化を求める。IOMMUが許可していないアクセスを装置が行うと、`DMAR: [fault reason ...]` や `AMD-Vi: Event logged [IO_PAGE_FAULT ...]` のようなメッセージがカーネルのログに出る。

## 関係
- 前提: [[PCIe]], [[Virtual Memory]]
- 使う / 使われる: [[Virtual Machine]], [[SPDK]], [[DPDK]], [[GPUDirect RDMA]]
- 関連: [[BaM]]

## 出典
- [VFIO - "Virtual Function I/O" - The Linux Kernel documentation](https://docs.kernel.org/driver-api/vfio.html)
- [x86 IOMMU Support - The Linux Kernel documentation](https://docs.kernel.org/arch/x86/iommu.html)
- [GPUDirect RDMA - NVIDIA Documentation](https://docs.nvidia.com/cuda/gpudirect-rdma/)
- [System Configuration User Guide - SPDK](https://spdk.io/doc/system_configuration.html)
- [Linux Drivers - DPDK documentation](https://doc.dpdk.org/guides/linux_gsg/linux_drivers.html)
