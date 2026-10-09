---
aliases: [Graphics Processing Unit, GPGPU, アクセラレータ, Accelerator, Streaming Multiprocessor, SM]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# GPU

> 多数の単純な演算器を並べ、大量のデータに同じ処理を並列に適用することに特化したプロセッサであり、HPCと機械学習の計算の主力となっている。

## 概要
GPUは、もとは画像の描画のために開発されたが、現在は汎用の数値計算にも広く用いられる。CPUが、少数の高性能なコアで複雑な制御を伴う逐次的な処理を高速に実行するよう設計されているのに対し、GPUは、トランジスタの多くを演算器に割き、膨大な数のスレッドを同時に実行することで高いスループットを得る。

NVIDIAのGPUを例に取ると、チップは多数のストリーミングマルチプロセッサ（SM）からなり、各SMが多数のスレッドを実行する。スレッドは32個を一組とするワープの単位で、同じ命令を同時に実行する（SIMT）。ワープ内のスレッドが条件分岐で異なる経路に分かれると、それぞれの経路が順に実行されるため、性能が低下する。メモリは階層をなし、各スレッドのレジスタ、SMごとに置かれスレッドブロック内で共有される高速な共有メモリ、全スレッドからアクセスできる大容量のグローバルメモリがある。グローバルメモリには、[[HBM]]などの非常に高い[[Bandwidth|バンド幅]]を持つメモリが用いられる。

GPUは、CPUとは別のメモリを持つ装置として計算機に接続される。CPU側のメモリとGPU側のメモリの間のデータ転送は、[[PCIe|PCI Express]]や[[NVLink]]などの接続を介して行われ、GPU内部のメモリのバンド幅よりはるかに低速である。GPUのプログラミングには、NVIDIAの[[CUDA]]が広く用いられる。

## どこで出てくるか
現在の上位のスーパーコンピュータの多くは、演算性能の大部分をGPUに依存しており、機械学習、特に[[LLM]]の学習と推論はGPUなしには成り立たない。GPUで性能を得るには、十分な並列性を与えて多数のスレッドでGPUを埋めること、データをGPUのメモリ上に置いたまま計算を続けてCPUとの転送を最小限にすること、メモリアクセスを隣接するスレッドが隣接するアドレスを読む形に揃えることが要点となる。多くの計算は演算性能よりもメモリのバンド幅で律速されるため、[[Roofline Model|ルーフラインモデル]]による分析が有効である。GPUのメモリの容量は限られており、LLMの推論では[[KV Cache]]がその容量を圧迫する。ストレージの研究では、GPUへのデータの供給（記憶装置からGPUへの直接転送など）が新たな課題となっている。

## 関係
- 使う / 使われる: [[CUDA]]（プログラミングの手段）, [[LLM]], [[vLLM]]
- 関連: [[Bandwidth]], [[KV Cache]], [[Collective Communication]]（NCCL）, [[RDMA]]

## 出典
- [CUDA C++ Programming Guide (Legacy) - NVIDIA](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html)
- [Programming Model - CUDA Programming Guide - NVIDIA](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)
