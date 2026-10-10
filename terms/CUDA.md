---
aliases: [Compute Unified Device Architecture, CUDA C++, nvcc, Kernel, カーネル関数, Warp, ワープ, Thread Block, スレッドブロック, Shared Memory, 共有メモリ, cudaMemcpy, Nsight]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# CUDA

> NVIDIAが提供する、[[GPU]]で汎用の計算を行うための並列計算プラットフォームとプログラミングモデルである。

## 概要
CUDAでは、GPUで実行する関数をカーネルと呼び、CPU側のプログラム（ホスト）からGPU（デバイス）に対して起動する。カーネルは、一度の起動で膨大な数のスレッドとして並列に実行される。スレッドは階層的に組織される。複数のスレッドがスレッドブロックを構成し、複数のスレッドブロックがグリッドを構成する。各スレッドは、自分のブロック番号とブロック内の番号から担当するデータを決め、同じコードを異なるデータに適用する。

ハードウェア上では、一つのスレッドブロックは一つのストリーミングマルチプロセッサ（SM）に割り当てられ、その中で32スレッドからなるワープの単位で実行される。ブロック内のスレッドは、SM上の高速な共有メモリを通じてデータを共有し、同期を取れる。異なるブロック間で直接協調することは基本的にできない。すべてのスレッドからは、大容量だが遅いグローバルメモリにアクセスできる。

ホストとデバイスは別のメモリを持つため、通常、CPU側でデータを用意し、`cudaMemcpy` などでGPUのメモリに転送し、カーネルを実行し、結果をCPU側に転送し戻す、という流れでプログラムを書く。カーネルの起動やデータの転送は非同期に行え、ストリームを用いることで、転送と計算を重ね合わせられる。プログラムはC++を拡張した言語で書き、コンパイラ `nvcc` でコンパイルする。行列演算の[[cuBLAS]]、深層学習の[[cuDNN]]、GPU間の[[Collective Communication|集団通信]]の[[NCCL]]など、多くのライブラリが提供されている。

## どこで出てくるか
深層学習のフレームワークや[[vLLM]]などの推論システムは、内部でCUDAのカーネルとライブラリを用いている。研究で独自のGPU処理を実装する場合、CUDAで直接カーネルを書くほか、PythonからGPUの処理を記述する手段も用いられる。性能の分析には、NVIDIAのNsight Systems（実行の時系列）とNsight Compute（カーネル単位の詳細）を用いる。初心者がつまずきやすいのは、カーネルの起動が非同期であるため、時間を正しく測るには同期を取る必要がある点、CPUとGPUの間の転送が想定外に時間を占めている点、ワープ内の分岐やメモリアクセスの不揃いが性能を大きく下げる点である。CUDAはNVIDIAのGPU専用であり、AMDのGPUにはHIP（ROCm）という類似の環境がある。

## 関係
- 上位概念: [[GPU]]
- 使う / 使われる: [[C]]（C++の拡張として書く）, [[Collective Communication]]（NCCL）
- 関連: [[vLLM]], [[LLM]], [[MPI]], [[perf]]

## 出典
- [CUDA C++ Programming Guide (Legacy) - NVIDIA](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html)
- [Programming Model - CUDA Programming Guide - NVIDIA](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)
- [Collective Operations - NCCL documentation](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)
