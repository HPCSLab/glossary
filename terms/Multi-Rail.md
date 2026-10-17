---
aliases: [マルチレール, Multirail, Multi-Rail Network, マルチレールネットワーク, Rail, レール, Network Rail, Rail-Optimized, Rail-Optimized Topology, レール最適化]
tags: [term]
maps: ["[[Network]]"]
status: draft
updated: 2026-10-17
---
# Multi-Rail（マルチレール）

> 一つの計算ノードに複数のネットワークアダプタを載せ、それぞれを別の経路（レール）としてネットワークに接続し、ノード間の通信の帯域を束ねて用いる構成である。

## 概要
[[Compute Node|ノード]]間の通信の[[Bandwidth|バンド幅]]は、[[NIC|ネットワークアダプタ]]一枚のリンクの速度で頭打ちになる。一方、ノードの中では複数の[[GPU]]やメモリが、一枚のNICを大きく上回る速度でデータを生み出す。そこで一つのノードに複数のNIC（[[InfiniBand]]ではHCA）を載せ、各NICをネットワークへの独立した経路として使う構成をマルチレールと呼ぶ。通信ライブラリは、異なるメッセージを異なるレールに振り分けるか、一つの大きなメッセージを分割して複数のレールで同時に送る（ストライピング）ことで、帯域を束ねる。2004年の[[MVAPICH]]の研究では、2本のレールを用いて大きなメッセージのバンド幅をほぼ2倍にした。

![[Multi-Rail Network.excalidraw]]

GPUを多数載せるノードでは、GPU一基ごとに一枚のNICを、そのGPUに近い位置（同じ[[PCIe]]のスイッチの下など）に置く構成がとられる。各GPUは近いNICを使うことで、ソケットをまたぐ転送（[[NUMA]]を参照）を避けられる。さらに、全ノードのi番目のNICを同じスイッチにつなぐ配線をレール最適化（rail-optimized）と呼ぶ。異なるノードの同じ番号のGPUどうしの通信は一段のスイッチだけを通るため、[[Collective Communication|集団通信]]のトラフィックの多くが上位のスイッチを通らずに済む。NVIDIAのDGX SuperPODの設計では、32ノードの単位の中で同じレールの通信は一段で届き、レールをまたぐ通信は上位（spine）のスイッチを通る。

## どこで出てくるか
GPUクラスタや、ノードあたり複数のHCAを持つスーパーコンピュータの構成の説明で使われる。例えば[[Sirius]]の各ノードは400 GbpsのInfiniBand NDRを4本持つ。[[NCCL]]は、複数のNICを持つノードでは異なるノードの同じNIC（同じレール）を使うように通信路を選び、`NCCL_IB_HCA` で使うHCAを限定でき、`NCCL_CROSS_NIC` でレールをまたぐ使い方を許すかを指定する。[[UCX]]では、`UCX_MAX_EAGER_RAILS` と `UCX_MAX_RNDV_RAILS` で一つの通信に使うレールの数を、`UCX_NET_DEVICES` で使うデバイスを指定する。[[OSU Micro-Benchmarks]]などでノード間の帯域を測ると、使われたレールの数と、各[[Process|プロセス]]が近いNICを使ったかで結果が大きく変わるため、評価では通信ライブラリの設定を確認する必要がある。

## 関係
- 前提: [[NIC]]
- 使う / 使われる: [[NCCL]], [[UCX]]
- 関連: [[InfiniBand]], [[NUMA]]

## 出典
- [Building Multirail InfiniBand Clusters: MPI-Level Design and Performance Evaluation (Liu, Vishnu, and Panda, SC 2004)](https://mvapich.cse.ohio-state.edu/static/media/publications/abstract/liuj_sc04.pdf)
- [Environment Variables (NCCL documentation)](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html)
- [FAQ (OpenUCX wiki)](https://github.com/openucx/ucx/wiki/FAQ)
- [Network Fabrics (NVIDIA DGX SuperPOD Reference Architecture, H100)](https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-h100/latest/network-fabrics.html)
