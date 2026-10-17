---
aliases: [Multi-Instance GPU, マルチインスタンスGPU, MIG Instance, MIGインスタンス, GPU Instance, GPUインスタンス, Compute Instance, MIG Profile]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-17
---
# MIG（マルチインスタンスGPU）

> 一基のGPUを、演算器（SM）とメモリ（容量・バンド幅・L2キャッシュ）をそれぞれ専有する最大7個のインスタンスに分割し、各インスタンスを独立したGPUのように使わせるNVIDIAの機能である。

## 概要
A100やH100のような大きな[[GPU]]は、小さなモデルの推論や開発中の試行のような一つの処理では使い切れないことが多い。一基のGPUを複数の処理で共有する方法として、時間を区切って交互に使う方法や、複数の[[Process|プロセス]]のカーネルを同時に実行させるMPSがあるが、これらはメモリの容量や[[Bandwidth|バンド幅]]、L2[[Cache|キャッシュ]]を処理ごとに分けないため、各処理の性能が他の処理の影響を受け、MPSでは一つのクライアントの障害が他に及ぶ。MIGは、Ampere世代以降の一部のGPUで、ハードウェアの資源そのものを分割する。SMを7つのスライスに、メモリを（対応するメモリコントローラとL2キャッシュとともに）8つのスライスに分け、その組み合わせをGPUインスタンスとして切り出す。各インスタンスは割り当てられた資源を専有するため、他のインスタンスの負荷によって性能が変わらず、障害も分離される。

![[MIG Partitioning.excalidraw]]

インスタンスの大きさはプロファイルで指定する。`3g.40gb` は、SMのスライス3つと40GBのメモリを持つインスタンスを表す。GPUインスタンスの中は、メモリを共有したままSMをさらに分けるコンピュートインスタンスに分割できる。一基のGPUに作れるインスタンスの数は、A100、H100、H200、B200などで最大7個、A30で最大4個であり、組み合わせられる配置もGPUの種類ごとに決まっている。

## どこで出てくるか
複数の利用者で共有するGPUサーバやクラウドで、一基のGPUを小さな単位に分けて割り当てるために用いられる。管理者は `nvidia-smi -i 0 -mig 1` でMIGのモードを有効にし（Ampere世代ではGPUのリセットを伴うことがある）、`nvidia-smi mig -lgip` で使えるプロファイルを確かめ、`nvidia-smi mig -cgi 9,3g.20gb -C`（A100 40GBの例）のようにインスタンスを作る。利用者は `nvidia-smi -L` でMIGのデバイスとそのUUIDを確かめ、`CUDA_VISIBLE_DEVICES=MIG-<UUID>` を指定して[[CUDA]]のプログラムを特定のインスタンスで実行する。MIGのインスタンスで測った性能は、GPU全体の性能とは異なる。共有のサーバで実験する場合は、GPUがMIGで分割されているか、どのプロファイルかを確かめ、論文では使用した構成を明記する。

## 関係
- 上位概念: [[GPU]]
- 使う / 使われる: [[CUDA]]
- 関連: [[HBM]]

## 出典
- [MIG User Guide: Concepts (NVIDIA)](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/concepts.html)
- [MIG User Guide: Supported GPUs (NVIDIA)](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-gpus.html)
- [MIG User Guide: Supported MIG Profiles (NVIDIA)](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-mig-profiles.html)
- [MIG User Guide: Getting Started with MIG (NVIDIA)](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/getting-started-with-mig.html)
