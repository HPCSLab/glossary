---
aliases: [nadino, Palladium, DPU-enabled Network Engine, DNE (DPU), CNE, NADINO Ingress, NADINO Network Engine]
tags: [term]
maps: ["[[Network]]"]
status: draft
updated: 2026-10-10
---
# NADINO（DPU-enabled Network Engine, DNE）

> 多数の利用者が共有するサーバレスのクラウドで、関数の間の通信の処理を[[DPU]]と[[RDMA]]に任せ、ホストのCPUの負担を減らすデータプレーンであり、その中核がDPUの上で動くネットワークエンジン（DNE）である。

## 概要
NADINOは、Shixiong Qi、Songyu Zhang、K. K. Ramakrishnanらが、EuroSys 2026で発表した（論文の題名は "Not A DPU in Name Only!"）。同じ著者らが2025年に arXiv で公開した Palladium も、DNEを含む同様の設計を述べている。サーバレスの計算では、関数の間のデータの受け渡しがCPUに頼る重い処理となり、ノード内では共有メモリで負担を減らせても、ノードの間では拡張しにくい。また、多数の利用者が同時にネットワークの資源を奪い合う。

NADINOは、ノードの間のデータの送信を、RDMAを用いて[[NIC]]に任せる。ノード内では共有メモリでデータの複製を避け、ホストのCPUとDPUの間でも共有メモリを用いて無駄なデータの移動を省く。DPUの汎用のコアは非力であるため、処理の大部分はRDMAのNICが担う。中核となるDNE（DPU-enabled network engine）は、DPUの上で動く軽量なリバースプロキシであり、利用者の関数からRDMAの資源を切り離して保護し、ノードの間のRDMAの通信の流れを調整し、競合の下でも公平になるように制御する。さらに、クラウドの入り口（ingress）で、HTTP/TCPの通信をRDMAに変換し、変換の処理を通信の経路の要所から外す。論文は、ゼロコピーのデータプレーンには、片方向（one-sided）よりも両方向（two-sided）のRDMAの操作が適するとしている。

## どこで出てくるか
DPUを用いてホストのCPUの負担を減らす研究の一つである。予備的な結果として、DPUへの処理の移行により、毎秒の要求数が20.9倍になり、最良の場合で遅延が21分の1になり、CPUのコアを最大7個節約しながら、DPUのコアは2個しか用いなかったと報告している。実装は[[GitHub]]で公開されており、DNEを動かすワーカーのノードにはNVIDIAの[[DPU|BlueField]]が必要である（DPUを用いない場合は、ホストのCPUで動くCNEを用いる）。

なお、[[Lustre]]の[[DNE]]（Distributed Namespace）とは別のものである。

## 関係
- 使う / 使われる: [[DPU]], [[RDMA]], [[DPDK]]（入り口のTCPの処理）
- 関連: [[Verbs]], [[Latency]]

## 出典
- [Not A DPU in Name Only! Unleashing RDMA-capable DPUs in Multi-Tenant Serverless Clouds with NADINO (Qi et al., EuroSys 2026)](https://doi.org/10.1145/3767295.3769386)
- [Palladium: A DPU-enabled Multi-Tenant Serverless Cloud over Zero-copy Multi-node RDMA Fabrics - arXiv](https://arxiv.org/abs/2505.11339)
- [ucr-serverless/NADINO - GitHub](https://github.com/ucr-serverless/NADINO)
