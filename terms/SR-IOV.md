---
aliases: [Single Root I/O Virtualization, VF, PF, Virtual Function, Physical Function]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# SR-IOV（Single Root I/O Virtualization）

> 一つの[[PCIe]]の装置を、それぞれが独立したPCIeの装置として見える複数の仮想的な装置に分ける規格である。

## 概要
SR-IOVは、PCIeの拡張機能として定められている。実際の装置は Physical Function（PF）と呼ばれ、PFのドライバが、仮想的な装置である Virtual Function（VF）をいくつ作るかを制御する。各VFは、通常のPCIeの装置と同じく、自分の構成空間、バス・デバイス・ファンクションの番号、レジスタのためのメモリ領域を持つ。このため、OSからはVFが一台の独立した装置として見え、通常の装置と同じようにドライバを割り当てられる。[[Linux Kernel|Linux]]では、PFの `sriov_numvfs` というsysfsのファイルに数を書き込むことでVFを作成し、0を書き込むと削除する。

SR-IOVの目的は、[[Virtual Machine|仮想マシン]]に装置を直接使わせることである。[[virtio]]のような方式では、仮想マシンが操作する装置はハイパーバイザが提供する仮想的なものであり、装置の処理はホスト側のソフトウェアが担う。これに対し、VFを[[IOMMU]]と VFIO によって仮想マシンにパススルーすれば、仮想マシンは物理的な装置に近い性能でVFを直接操作できる。パススルーだけでは一台の装置を一台の仮想マシンにしか渡せないが、SR-IOVによって一台の装置を複数の仮想マシンで分け合える。

## どこで出てくるか
代表的な例は[[NIC]]である。NVIDIAのConnectXのNICは、ポートあたり最大127個のVFを作れ、[[InfiniBand]]を仮想マシンから用いる場合にもSR-IOVを使う。利用には、BIOSでSR-IOVと仮想化支援機能を有効にし、カーネルでIOMMUを有効にする（Intelの計算機では起動オプション `intel_iommu=on`）必要がある。仮想マシンの上で[[MPI]]や[[RDMA]]を用いる環境を構築する場面で出会う。

## 関係
- 前提: [[PCIe]], [[IOMMU]]
- 対比: [[virtio]]（ハイパーバイザが提供する仮想的な装置を用いる）
- 使う / 使われる: [[Virtual Machine]], [[InfiniBand]]
- 関連: [[RDMA]]

## 出典
- [PCI Express I/O Virtualization Howto - The Linux Kernel documentation](https://docs.kernel.org/PCI/pci-iov-howto.html)
- [Single Root IO Virtualization (SR-IOV) - NVIDIA MLNX_OFED Documentation](https://networking-docs.nvidia.com/mlnxofedswum/24100700/single+root+io+virtualization+(sr-iov))
- [VFIO - "Virtual Function I/O" - The Linux Kernel documentation](https://docs.kernel.org/driver-api/vfio.html)
