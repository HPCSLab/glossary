---
aliases: [SHMEM, Cray SHMEM, NVSHMEM, Sandia OpenSHMEM, SOS, OSHMEM, PE, Processing Element, Symmetric Heap, 対称ヒープ]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# OpenSHMEM

> 他の[[Process|プロセス]]のメモリを、相手の関与なしに直接読み書きする片側通信を中心とした、[[PGAS]]のモデルに基づく並列プログラミングのライブラリの標準規格である。

## 概要
SHMEMは、1993年にCray ResearchがスーパーコンピュータCray T3Dの通信のハードウェアを薄く包むライブラリとして作ったのが始まりである。その後、複数の企業が互換性のない独自のSHMEMを実装したため、共通の規格として、SGIとOpen Source Software Solutions, Inc.を中心にOpenSHMEMが策定された。

OpenSHMEMのプログラムは、同じプログラムの複数のコピー（PE、processing element）として並列に実行される。各PEは、`shmem_put` で相手のPEのメモリにデータを書き込み、`shmem_get` で相手のメモリから読み出す。相手のPEはこの通信に関与しない。遠くからアクセスできるのは、全PEで同じように確保された対称（symmetric）なデータに限られ、動的なデータは `shmem_malloc` などで対称ヒープに確保する。このほか、短いデータに対する不可分操作、バリアや[[Mutex|ロック]]などの同期、総和や放送などの[[Collective Communication|集団通信]]を備える。

## どこで出てくるか
SHMEMは、低[[Latency|遅延]]の分散メモリの計算機で、[[RDMA]]に基づく片側通信を行うことを前提としている。実装には、[[Open MPI]]に含まれるもの、Sandia OpenSHMEM、[[MPI]]の上に実装したOSHMPIなどがある。[[libfabric]]も、SHMEMを設計の対象の一つとしている。NVIDIAのNVSHMEMは、OpenSHMEMをNVIDIAの[[GPU]]向けに実装したものであり、複数のGPUのメモリにまたがる大域的なアドレス空間を提供し、[[CUDA]]のカーネルの中から直接通信を始められる。

## 関係
- 上位概念: [[PGAS]]
- 使う / 使われる: [[RDMA]], [[libfabric]], [[Open MPI]]（実装を含む）
- 対比: [[MPI]]（送受信の対を基本とする。MPIにも片側通信がある）
- 関連: [[GPU]], [[CUDA]]

## 出典
- [SHMEM - Wikipedia](https://en.wikipedia.org/wiki/SHMEM)
- [OpenSHMEM - Wikipedia](https://en.wikipedia.org/wiki/OpenSHMEM)
- [NVSHMEM - NVIDIA Documentation](https://docs.nvidia.com/nvshmem/api/introduction.html)
