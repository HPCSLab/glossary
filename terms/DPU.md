---
aliases: [Data Processing Unit, データ処理ユニット, SmartNIC, スマートNIC, IPU, Infrastructure Processing Unit, BlueField, NVIDIA BlueField, DOCA, SNAP, NVMe SNAP]
tags: [term]
maps: ["[[Network]]", "[[Storage]]"]
status: draft
updated: 2026-10-10
---
# DPU（Data Processing Unit）

> 汎用のCPUのコアとネットワークインタフェースのハードウェアを一体化したプログラム可能なプロセッサであり、ネットワーク、ストレージ、セキュリティなどの基盤の処理を、計算機本体のCPUから肩代わりする。

## 概要
DPUは、汎用のCPUのコア、DRAMや記憶装置、そして高速なネットワークインタフェース（[[NIC]]）をデータの経路の上に統合した装置である。SmartNICやIPU（Infrastructure Processing Unit）とも呼ばれる。暗号化と復号、ファイアウォール、TCP/IPのプロトコル処理、[[Virtual Machine|ハイパーバイザ]]やストレージコントローラの機能などを、ホストのCPUの代わりに実行し、ホストのCPUの時間をアプリケーションのために空ける。DPUのCPUのコアは、一般にホストのCPUより非力である一方、100〜400Gbit/s程度のネットワークの処理能力を持つ。

代表的な製品であるNVIDIAのBlueFieldは、ConnectXシリーズのネットワークアダプタと、Armのコアの群を組み合わせたものである。例えばBlueField-2は、ConnectX-6 Dxと8個の64ビットArm（A72）のコアを備え、ネットワーク、暗号、ストレージの処理をハードウェアで行う。NVIDIAは、BlueFieldの役割を、基盤のサービスを「肩代わりし（offload）、加速し（accelerate）、分離する（isolate）」ものと説明している。BlueFieldのArmのコアの上で動作するソフトウェアは、ホストのCPUから分離されているため、ホストが侵害された場合にも、DPU上のセキュリティの機能を保てる。ソフトウェアの開発には、NVIDIAのDOCAというSDKが提供されている。

## どこで出てくるか
ストレージの分野では、DPUは[[RDMA]]や[[NVMe-oF]]の処理を受け持つ。BlueFieldは、SNAPと呼ばれる[[NVMe]]の記憶装置の模擬（storage emulation）とNVMeのストレージの仮想化の機能を持ち、ホストのOSを介さずに、仮想的なブロックデバイスをホストに見せられる。クラウドの仮想マシンの[[Block Storage|ブロックストレージ]]の処理をDPUに移し、ホストのCPUの消費と性能の低下を減らす研究（FlexBSOなど）も行われている。

DPUのCPUのコアはホストのCPUより非力であるため、DPUを用いる設計では、どの処理をホストからDPUへ移すかが論点となる。

## 関係
- 使う / 使われる: [[RDMA]], [[NVMe-oF]], [[NVMe]], [[InfiniBand]]
- 関連: [[Block Storage]], [[NADINO]]

## 出典
- [Data processing unit - Wikipedia](https://en.wikipedia.org/wiki/Data_processing_unit)
- [NVIDIA BlueField - NVIDIA](https://www.nvidia.com/en-us/networking/products/data-processing-unit/)
- [NVIDIA Mellanox BlueField-2 DPU Product Brief - NVIDIA](https://network.nvidia.com/files/doc-2020/pb-bluefield-2-dpu.pdf)
- [FlexBSO: Flexible Block Storage Offload for Datacenters - arXiv](https://arxiv.org/abs/2409.02381)
