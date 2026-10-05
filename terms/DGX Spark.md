---
aliases: [NVIDIA DGX Spark, GB10, Grace Blackwell, GB10 Grace Blackwell Superchip]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-06
---
# DGX Spark

> NVIDIAの、GB10 Grace Blackwell Superchipを搭載した机上に置ける小型のAI用計算機であり、128GBの統合メモリを持つ一方、メモリバンド幅は273GB/sにとどまる。

## 概要
DGX Sparkは、CPUとGPUを一つにまとめたGB10 Grace Blackwell Superchipを中心とする小型の計算機である。CPUは20コアのArm（Cortex-X925が10コア、Cortex-A725が10コア）、[[GPU]]は第5世代のTensor Coreを備えたBlackwellであり、FP4の精度で最大1PFLOPの性能を持つ。メモリは、CPUとGPUが共有する128GBのLPDDR5xの統合メモリであり、そのメモリバンド幅は273GB/sである。このほか、最大4TBの[[NVMe]] SSD、200GbpsのConnectX-7のネットワークを備え、大きさは150mm×150mm×50.5mm、電源は240Wである。NVIDIAは、最大700億パラメータのモデルの微調整（fine-tuning）や、最大2,000億パラメータのモデルの推論、AIエージェントやエッジのアプリケーションの試作を用途として挙げている。

## どこで出てくるか
DGX Sparkは、[[LLM]]のような大きなモデルを、一台の手元の計算機のメモリに載せて扱える点に特徴がある。一方、そのメモリはデータセンター向けのGPUが用いる[[HBM]]ではなくLPDDR5xであり、メモリバンド幅の273GB/sは、例えばデータセンター向けのGPUであるNVIDIA H100（SXM版、3.35TB/s）の10分の1にも満たない。そのため、メモリからデータを読み出す速さが性能を決める処理では、演算性能の数値から期待されるほどの性能は得られない。DGX Sparkの性能を評価する際や、他の計算機と比較する際には、演算性能だけでなく、メモリの容量とバンド幅の両方を確認する必要がある。

## 関係
- 使う / 使われる: [[GPU]]（Blackwell）, [[NVMe]]
- 対比: [[HBM]]（データセンター向けのGPUが用いる高バンド幅のメモリ）, [[Sirius]]（CPUとGPUがHBM3を共有する）
- 関連: [[LLM]], [[Bandwidth]], [[Little's Law]]

## 出典
- [NVIDIA DGX Spark - NVIDIA](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)
- [NVIDIA H100 Tensor Core GPU - NVIDIA](https://www.nvidia.com/en-us/data-center/h100/)
