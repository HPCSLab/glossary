---
aliases: [CUDA Graph, CUDAグラフ, cudaGraph, Stream Capture, ストリームキャプチャ, cudaGraphLaunch, torch.cuda.graph, CUDAGraph]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-17
---
# CUDA Graphs（CUDAグラフ）

> GPUで行う一連のカーネルの実行とデータ転送を、依存関係を持つグラフとして事前に定義しておき、一回の操作でまとめて起動することで、CPUによる起動の負担を減らす[[CUDA]]の機能である。

## 概要
CUDAでは、CPUがカーネルを一つずつ[[GPU]]のストリームに投入して実行させる。投入の処理（起動）にはCPU側で一定の時間がかかるため、一つ一つのカーネルの実行時間が短いと、GPUは次の起動を待って空き、全体の時間がCPUの起動の速さで決まる。CUDA Graphsは、カーネルの実行やメモリの転送を節点、それらの依存関係を辺とするグラフで処理を表す。グラフの利用は、定義、インスタンス化、実行の三段階に分かれる。インスタンス化で起動に必要な準備の多くを済ませた実行可能なグラフを作り、以後は `cudaGraphLaunch` の一回の呼び出しでグラフ全体を何度でも実行できる。

![[CUDA Graphs Launch Timeline.excalidraw]]

グラフは、節点を追加するAPIで明示的に組み立てるか、ストリームに投入した処理を記録するストリームキャプチャ（`cudaStreamBeginCapture` と `cudaStreamEndCapture` の間に通常どおり処理を投入する）で作る。インスタンス化したグラフの構造は固定であり、`cudaGraphExecUpdate` で更新できるのは構造が同じ場合の引数などに限られる。構造が変わる場合はインスタンス化をやり直す必要がある。

## どこで出てくるか
[[PyTorch]]では、`torch.cuda.graph` の範囲で実行した処理を記録し、`replay()` で再実行する。再実行は記録時と同じメモリのアドレスを読み書きし、形状が変わる処理は記録できないため、新しい入力は記録に用いた入力のテンソルに書き込んでから再実行する。[[LLM]]の推論のデコードでは、一トークンごとに多数の小さなカーネルを実行するため起動の負担が目立ちやすく、[[vLLM]]などの推論エンジンは、いくつかのバッチの大きさについてグラフを記録しておき、デコードの実行に用いる。プロファイラ（Nsight Systems）の時間軸でカーネルの間に隙間が並んでいる場合は、起動の負担が[[Bottleneck|律速]]している可能性があり、CUDA Graphsの適用を検討する目安となる。

## 関係
- 上位概念: [[CUDA]]
- 使う / 使われる: [[PyTorch]], [[vLLM]]
- 関連: [[GPU]]

## 出典
- [CUDA Graphs (CUDA Programming Guide)](https://docs.nvidia.com/cuda/cuda-programming-guide/04-special-topics/cuda-graphs.html)
- [CUDA semantics: CUDA Graphs (PyTorch documentation)](https://docs.pytorch.org/docs/stable/notes/cuda.html)
- [CUDA Graphs (vLLM design documentation)](https://docs.vllm.ai/en/latest/design/cuda_graphs.html)
