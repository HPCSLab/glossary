---
aliases: [GPU Direct Storage, GDS, cuFile, cuFileRead, cuFileWrite, nvidia-fs, Bounce Buffer, バウンスバッファ]
tags: [term]
maps: ["[[Storage]]", "[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# GPUDirect Storage（GDS）

> 記憶装置と[[GPU]]のメモリの間で、CPUのメモリの中継（バウンスバッファ）を経ずに直接[[DMA]]でデータを転送する、NVIDIAの技術である。

## 概要
通常、ファイルのデータをGPUで処理するには、まず記憶装置からCPUのメモリにデータを読み込み、それをGPUのメモリに複製する。このCPUのメモリの中間の領域をバウンスバッファと呼ぶ。GPUDirect Storageは、記憶装置とGPUのメモリの間に直接のデータの経路を作り、この中継を省く。これにより、システムの[[Bandwidth|バンド幅]]のボトルネックが緩和され、[[Latency|レイテンシ]]とCPUの負荷が減る。

アプリケーションは、cuFileと呼ばれるAPI（`cuFileHandleRegister` でファイルを登録し、`cuFileRead`、`cuFileWrite` で読み書きする）を用いる。カーネル側では、`nvidia-fs.ko` というドライバが、GPUのメモリのアドレスの変換とDMAの処理を担う。ファイルは、[[Page Cache|ページキャッシュ]]を経由しない `O_DIRECT` で開く必要がある。対応するファイルシステムには、[[ext4]]、[[XFS]]、[[Lustre]]、[[IBM Storage Scale|GPFS]]、[[BeeGFS]]、[[NFS]]などがある。直接の経路が使えない構成では、CPUのメモリを経由する互換モードに自動で切り替わるため、アプリケーションのコードを変えずに動作する。

## どこで出てくるか
機械学習の学習のデータや、大きな科学技術のデータをGPUで処理する場合、記憶装置からGPUへのデータの転送が性能を制限することがある。GDSは、[[NVMe]] SSDや[[NVMe-oF]]、[[Parallel File System|並列ファイルシステム]]からGPUへの読み込みを速くするために用いられる。GDSを評価する際には、互換モードに切り替わっていないかを確かめる必要がある。

GDSは、[[GPUDirect RDMA]]の技術を用いて、SSDとGPUの間のデータの経路からCPUのメモリを取り除く。ただし、データの移動を指示するのはCPUである。GPUのスレッドが自ら記憶装置へのアクセスを発行する方式としては、[[BaM]]が提案されている。

## 関係
- 前提: [[GPU]], [[GPUDirect RDMA]]
- 使う / 使われる: [[NVMe]], [[NVMe-oF]], [[Lustre]], [[CUDA]]
- 対比: [[BaM]]（GPUのスレッドが記憶装置へのアクセスを発行する）
- 関連: [[Page Cache]], [[Bandwidth]]

## 出典
- [NVIDIA GPUDirect Storage Overview Guide - NVIDIA Documentation](https://docs.nvidia.com/gpudirect-storage/overview-guide/index.html)
- [BaM: GPU-Initiated On-Demand High-Throughput Storage Access (Qureshi et al., ASPLOS 2023) - arXiv](https://arxiv.org/abs/2203.04910)（関連研究の節でのGDSの位置付け）
