---
aliases: [NVSwitch, NVLink Switch, NVLink-C2C, NVL72]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# NVLink

> NVIDIAの[[GPU]]同士を、[[PCIe]]を介さずに高い[[Bandwidth|帯域]]で直接接続するための、NVIDIA独自の接続技術である。

## 概要
一つの計算機に複数のGPUを載せる場合、GPU間の通信をPCIeとホストのメモリを経由して行うと、帯域が演算性能に比べて大きく不足する。NVLinkは、GPU同士を直接結ぶ専用のリンクであり、GPUあたりの帯域は、第4世代（Hopper）で900 GB/s、第5世代（Blackwell）で1.8 TB/s、第6世代（Vera Rubin）で3 TB/s に達する。NVIDIAによれば、第6世代のNVLinkの帯域はPCIe Gen6の12倍である。

NVLink Switch は、多数のNVLinkを束ねて、すべてのGPUが互いに最大の帯域で通信できるようにするスイッチである。第4世代では8個、第5世代以降では最大72個のGPUを一つのNVLinkのドメインとして結べる（NVL72）。また、NVLink-C2Cは、NVLinkの技術をチップ間の接続に広げたものであり、NVIDIAのGraceのCPUとGPUを、キャッシュの一貫性を保って高い帯域で接続する。

## どこで出てくるか
[[LLM]]の学習や推論のように、モデルを複数のGPUに分割して載せる場合、GPU間で頻繁に大量のデータを交換するため、NVLinkの有無と構成が性能を大きく左右する。GPU間の[[Collective Communication|集団通信]]を行う[[NCCL]]は、PCIe、NVLink、[[InfiniBand]]などの接続に対応している。[[CUDA]]のピアツーピアの転送も、NVLinkがあればホストのメモリを経由せずにGPU間で直接行われる。[[Miyabi]]のGPUノードのように、CPUとGPUをNVLink-C2Cで結ぶ計算機もある。計算機のGPU間の接続は `nvidia-smi topo -m` で確認でき、NVLinkで結ばれたGPUの組は `NV#`（#はリンクの数）、PCIeを経由する組は `PIX` や `SYS` などと表示される。

## 関係
- 対比: [[PCIe]]（汎用の装置の接続であり、帯域はNVLinkより大幅に低い）
- 使う / 使われる: [[GPU]], [[Collective Communication]], [[Miyabi]]
- 関連: [[InfiniBand]], [[GPUDirect RDMA]]

## 出典
- [NVLink and NVLink Switch - NVIDIA](https://www.nvidia.com/en-us/data-center/nvlink/)
- [NVLink-C2C - NVIDIA](https://www.nvidia.com/en-us/data-center/nvlink-c2c/)
- [Overview of NCCL - NVIDIA](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html)
- [nvidia-smi - Bede Documentation](https://bede-documentation.readthedocs.io/en/latest/software/tools/nvidia-smi.html)
- [CUDA C++ Best Practices Guide - NVIDIA](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html)
