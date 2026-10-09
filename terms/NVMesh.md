---
aliases: [Excelero NVMesh, Excelero, RDDA, Remote Direct Drive Access]
tags: [term]
maps: ["[[Storage]]", "[[Network]]"]
status: draft
updated: 2026-10-10
---
# NVMesh

> Excelero社が開発した、複数のサーバに搭載された[[NVMe]] SSDをネットワーク越しにまとめ、共有のブロックストレージとして提供するソフトウェアである。

## 概要
NVMeshは、各サーバに分散して搭載されたNVMe SSDを一つの資源の集まりとして束ね、そこから論理的なボリュームを切り出して、ネットワーク上の任意のホストに[[Block Storage|ブロックデバイス]]として提供する。専用のストレージ装置を用いずに、汎用のサーバとSSDでSAN（Storage Area Network）のような共有ストレージを構成する、いわゆるソフトウェア定義ストレージの一種である。

構成は三つの部品からなる。ボリュームを利用する各ホストには、Linuxのブロックデバイスのドライバとして動作するクライアントを導入する。NVMe SSDを搭載したサーバには、そのSSDを公開するためのターゲットの部品を導入する。少なくとも一台のサーバで、全体の構成、監視、管理を行う管理用の部品を動かす。

NVMeshの技術的な特徴は、独自のRDDA（Remote Direct Drive Access）という方式にある。ホストがリモートのSSDにアクセスする際、[[RDMA]]を用いて、リモートのサーバの[[NIC|ネットワークカード]]を介してSSDに直接読み書きを行い、リモートのサーバのCPUを関与させない。データの冗長化などの処理も、ストレージ側のCPUではなく、クライアント側に分散して行う。これにより、SSDを搭載したサーバのCPUをアプリケーションの計算のために空けておけ、ストレージの処理が他の計算を妨げる問題を避けられる。この点で、一般にターゲット側のソフトウェアがコマンドを処理する[[NVMe-oF]]とは設計が異なる。

## どこで出てくるか
NVMeshは、[[Compute Node|計算ノード]]のローカルSSDを束ねた高速な共有ストレージとして、HPCや[[GPU]]クラスタで用いられた。Excelero社は2022年3月にNVIDIAに買収され、既存の顧客への保守は継続されたものの、Exceleroの製品としての新たな展開は終了した。現在では、製品そのものよりも、ターゲットのCPUを介さずにリモートのSSDへアクセスするという設計が、ストレージの分離（disaggregation）やRDMAを用いたストレージの研究における先行例として参照される。

## 関係
- 使う / 使われる: [[NVMe]], [[RDMA]], [[InfiniBand]], [[RoCE]]
- 対比: [[NVMe-oF]]（標準規格による、ネットワーク越しのNVMe）
- 関連: [[Block Storage]], [[SSD]], [[GPU]]

## 出典
- [Nvidia Acquires Software-Defined Storage Provider Excelero - HPCwire](https://www.hpcwire.com/2022/03/07/nvidia-acquires-software-defined-storage-provider-excelero/)
- [Nvidia buys Excelero to speed GPU cluster block data access - Blocks and Files](https://blocksandfiles.com/2022/03/07/nvidia-buys-excelero-to-speed-gpu-cluster-block-data-access/)
- [Excelero NVMesh Architecture - Advanced HPC](https://www.advancedhpc.com/pages/excelero-nvmesh-architecture)
