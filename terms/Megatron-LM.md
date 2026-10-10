---
aliases: [Megatron, Megatron Core, Megatron-Core, megatron-lm, PTD-P, Tensor Parallelism, テンソル並列, Pipeline Parallelism, パイプライン並列, Pipeline Bubble, パイプラインバブル]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# Megatron-LM

> NVIDIAが開発する、[[Transformer]]に基づく大規模な言語モデルを、多数の[[GPU]]に分割して学習するためのソフトウェアであり、テンソル並列とパイプライン並列を広めた。

## 概要
Megatron-LMは、Shoeybiらが2019年の論文で発表した。一つのGPUのメモリに収まらないモデルを学習するため、Transformerの層の中の行列の積を複数のGPUに分割するテンソル並列（層内のモデル並列）を、[[PyTorch]]に少数の通信の操作を加えるだけで実現した。例えば、MLPの層の第一の重み行列を列の方向に、第二の重み行列を行の方向に分けると、各GPUは間に同期を挟まずに自分の部分を計算でき、最後に一回のAllreduceで結果をまとめればよい。論文は、83億パラメータのモデルを512個のGPUで学習し、一つのGPUに対して76%の拡張の効率を得たと報告した。

テンソル並列は、層ごとに[[Collective Communication|集団通信]]を要するため、通信の速いノード内に向く。Narayananらの[[SC]] 2021の論文は、ノード内のテンソル並列、ノード間のパイプライン並列、データ並列を組み合わせる方式（PTD-P）を示した。パイプライン並列は、モデルの層を順に複数のGPUに割り当て、バッチを小さなマイクロバッチに分けて流す。各バッチの始めと終わりにはGPUが待つ時間（パイプラインバブル）が生じるため、各GPUに複数の層の塊を割り当てるインタリーブ方式でこれを減らした。論文は、1兆パラメータのモデルを3,072個のGPUで、毎秒502 PFLOP（GPUあたり理論性能の52%）で学習できたと報告している。

現在は、部品をまとめたライブラリMegatron Coreと、それを用いた学習のスクリプトの集まりであるMegatron-LMに分かれており、テンソル、パイプライン、データ、エキスパート、コンテキストの各並列化と、FP8などの混合精度を提供する。

## どこで出てくるか
[[LLM]]の学習を多数のGPUで行う研究で、並列化の方式の基準や比較の対象として現れる。論文やシステムの説明で「TP=8、PP=4」のように並列化の度数が書かれていれば、テンソル並列とパイプライン並列の分割数を指す。テンソル並列はGPU間の[[NVLink]]の[[Bandwidth|帯域]]を、データ並列やパイプライン並列はノード間の[[InfiniBand]]などの帯域を使うため、計算機の接続の構成が並列化の選び方を左右する。通信には[[NCCL]]が用いられる。

## 関係
- 使う / 使われる: [[PyTorch]], [[NCCL]], [[GPU]], [[Collective Communication]]
- 関連: [[LLM]], [[NVLink]], [[InfiniBand]], [[vLLM]]

## 出典
- [NVIDIA/Megatron-LM - GitHub](https://github.com/NVIDIA/Megatron-LM)
- [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism (Shoeybi et al., arXiv:1909.08053)](https://arxiv.org/abs/1909.08053)
- [Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM (Narayanan et al., SC 2021)](https://arxiv.org/abs/2104.04473)
