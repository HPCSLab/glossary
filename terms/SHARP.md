---
aliases: [NVIDIA SHARP, SHArP, Scalable Hierarchical Aggregation and Reduction Protocol, Scalable Hierarchical Aggregation Protocol, In-Network Computing, インネットワークコンピューティング, In-Network Aggregation, ネットワーク内集約, スイッチでのリダクション]
tags: [term]
maps: ["[[Network]]", "[[Parallel Computing]]"]
status: draft
updated: 2026-10-17
---
# SHARP（スイッチによる集団通信の集約）

> InfiniBandのスイッチの中で集団通信のリダクション（総和など）を行い、データがネットワークを通る量とノードの計算を減らす、NVIDIAの技術である。

## 概要
[[Collective Communication|集団通信]]のAllreduceは、全[[Process|プロセス]]の値を足し合わせて全プロセスに配る操作である。通常は[[Compute Node|ノード]]どうしがデータを送り合い、受け取ったデータの足し算をノードのCPUや[[GPU]]が行う。リングのアルゴリズムでは各ノードがデータの約2倍の量を送受信し、木のアルゴリズムでは段数に比例して[[Latency|レイテンシ]]が増える。SHARP（Scalable Hierarchical Aggregation and Reduction Protocol）は、スイッチのASICに演算器を持たせ、この足し算をネットワークの中で行う。参加するノードとスイッチを結ぶ木（集約の木）を定め、各スイッチは下から届いたデータを足し合わせて上へ送り、根のスイッチの結果を全ノードへ配る。データは各リンクを上りと下りに一度ずつ通るだけで済み、ノードは集約の計算に関わらないため、ノード側の処理の揺らぎ（ジッタ）の影響も受けにくい。

![[SHARP Aggregation Tree.excalidraw]]

SHARPは、Mellanox（現NVIDIA）が[[InfiniBand]]のEDR世代のスイッチで導入した。第1世代は科学技術計算の小さなメッセージを対象とし、HDR世代のQuantumスイッチの第2世代で大きなメッセージの集約（streaming aggregation）に対応し、第3世代では複数のジョブが同時に集約を利用できるようになった。一つのサブネットで同時に使える集約の木の数や、大きなメッセージの集約を同時に行える木の数には、スイッチの世代ごとに上限がある。集約の木の割り当ては、ファブリックの管理ソフトウェア（UFMなど）とともに動くAggregation Managerが行う。

## どこで出てくるか
NVIDIAのInfiniBandのスイッチを用いるクラスタで、[[MPI]]や[[NCCL]]のAllreduceを高速化する手段として用いられる。MPIでは、NVIDIAのHPC-Xに含まれる[[Open MPI]]の集団通信ライブラリ（HCOLL）がSHARPを利用できる。NCCLでは、HPC-Xに含まれるnccl-rdma-sharpプラグインを用い、環境変数 `NCCL_COLLNET_ENABLE=1` を指定するとSHARPによる集約（CollNet）が有効になる。深層学習の分散学習では、各ステップの勾配のAllreduceの時間を短くする目的で用いられる。スイッチの機能であるため、利用できるかどうかは使う計算機のスイッチの世代と設定に依存し、論文の評価では有効にしたかどうかを明記する必要がある。

## 関係
- 上位概念: [[Collective Communication]]
- 前提: [[InfiniBand]]
- 使う / 使われる: [[MPI]], [[NCCL]]

## 出典
- [Advancing Performance with NVIDIA SHARP In-Network Computing (NVIDIA Technical Blog)](https://developer.nvidia.com/blog/advancing-performance-with-nvidia-sharp-in-network-computing)
- [NVIDIA SHARP Rev 3.13.0 General Information (NVIDIA Documentation)](https://networking-docs.nvidia.com/sharpum/3130/general-information)
- [NCCL-RDMA-SHARP Plugins (NVIDIA HPC-X Software Toolkit documentation)](https://networking-docs.nvidia.com/hpcxum/2.50/nccl-rdma-sharp-plugins)
- [NVIDIA HPC-X Software Toolkit Rev 2.18.1 (PDF)](https://docs.nvidia.com/nvidia-hpc-x-software-toolkit-rev-2-18-1.pdf)
- [Towards A Data Centric System Architecture: SHARP (Graham et al., Supercomputing Frontiers and Innovations, 2017)](https://superfri.org/index.php/superfri/article/view/140)
