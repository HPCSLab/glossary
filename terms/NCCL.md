---
aliases: [NVIDIA Collective Communications Library, nccl, RCCL, nccl-tests, NCCL_DEBUG]
tags: [term]
maps: ["[[Machine Learning Systems]]", "[[Network]]"]
status: draft
updated: 2026-10-10
---
# NCCL（NVIDIA Collective Communications Library）

> NVIDIAの[[GPU]]の間で、Allreduceなどの[[Collective Communication|集団通信]]と一対一の送受信を、接続の構成に合わせて高速に行うための通信ライブラリである。

## 概要
NCCLは、並列プログラミングの枠組みそのものではなく、GPU間の通信だけを提供するライブラリである。AllReduce、Broadcast、Reduce、AllGather、ReduceScatter、AlltoAll、Gather、Scatterの集団通信と、一対一の送信と受信を提供する。一つのノードの中の複数のGPUの間でも、複数のノードにまたがっても動作し、接続の手段として[[PCIe]]、[[NVLink]]、[[InfiniBand]]の[[Verbs|verbs]]、IPのソケットを用いる。NCCLは計算機の接続の構成（トポロジ）を調べ、それに合わせた通信の経路とアルゴリズムを選ぶ。

APIは[[MPI]]の集団通信に倣っており、MPIを知っていれば理解しやすい。各集団通信は、通信と計算を一つの[[CUDA]]のカーネルとして実行し、CUDAのストリームを引数に取るため、GPUの計算と同じ流れの中に組み込める。一つのスレッドが全てのGPUを扱う形、GPUごとにスレッドを用いる形、MPIのように複数のプロセスを用いる形のいずれでも使える。

## どこで出てくるか
深層学習の分散学習では、各GPUが計算した勾配の総和を求めるAllReduceが中心となり、その実装としてNCCLが広く用いられている。[[PyTorch]]の `torch.distributed` では、NVIDIAのGPUの間の通信のバックエンドとしてNCCLを選べる。AMDのGPUには、同様の役割のRCCLがある。

通信が遅い、あるいは止まる場合は、環境変数 `NCCL_DEBUG=INFO` を設定するとデバッグの情報が表示され、NCCLが検出した接続や選んだ経路を確かめられる。使うInfiniBandのアダプタは `NCCL_IB_HCA` で、ソケットに用いるネットワークのインタフェースは `NCCL_SOCKET_IFNAME` で指定できる。意図しない経路（例えばInfiniBandの代わりにソケット）が選ばれていると、性能が大きく下がる。集団通信の性能は、NVIDIAのnccl-testsの `all_reduce_perf` などで、メッセージの大きさを変えながら測定できる。

## 関係
- 上位概念: [[Collective Communication]]
- 使う / 使われる: [[GPU]], [[CUDA]], [[NVLink]], [[InfiniBand]], [[PyTorch]]
- 対比: [[MPI]]（CPUのプロセス間の通信の標準規格）
- 関連: [[GPUDirect RDMA]], [[UCX]]

## 出典
- [Overview of NCCL - NVIDIA](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html)
- [Environment Variables - NCCL Documentation](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html)
- [NVIDIA/nccl-tests - GitHub](https://github.com/NVIDIA/nccl-tests)
