---
aliases: [OFI, Open Fabrics Interfaces, OpenFabrics Interfaces, OFIWG, fi_info, FI_PROVIDER, CXI Provider]
tags: [term]
maps: ["[[Network]]"]
status: draft
updated: 2026-10-10
---
# libfabric

> 多様な高速ネットワークを共通のAPIで扱えるようにする、並列・分散アプリケーションのための低水準の通信ライブラリである。Open Fabrics Interfaces（OFI）とも呼ばれる。

## 概要
libfabricは、OpenFabrics Allianceの作業部会であるOFIWGが開発している。[[RDMA]]を中心とする高[[Bandwidth|帯域]]・低[[Latency|遅延]]のネットワークを対象とし、[[MPI]]、SHMEM、PGAS、ストレージなどの上位のソフトウェアが必要とする通信の意味と、ネットワークが提供する機能との食い違いを減らすことを設計の目標とする。APIは特定のネットワークに依存せず、その実装はネットワークごとのプロバイダに任せる。これにより、上位のソフトウェアは同じコードで異なるネットワークを使える。

プロバイダには、特定の種類の装置に対応するコアプロバイダと、他のプロバイダの機能を補うユーティリティプロバイダがある。コアプロバイダには、RDMAの[[NIC]]を[[Verbs|verbs]]で使う `verbs`、HPEの[[Dragonfly Topology|Slingshot]]のための `cxi`、Amazon EC2のEFAのための `efa`、Cornelis NetworksのOmni-Pathのための `opx`、ノード内の共有メモリのための `shm`、どの環境でも動く `tcp` や `udp`、[[UCX]]の上で動き、NVIDIAの[[InfiniBand]]に対応する `ucx` などがある。通信の端点（エンドポイント）には、接続型で信頼性のある `FI_EP_MSG`、接続なしで信頼性のある `FI_EP_RDM`、接続なしで信頼性のない `FI_EP_DGRAM` の種類があり、ユーティリティプロバイダの `rxm` は、MSGのエンドポイントの上にRDMの意味を提供する。

## どこで出てくるか
利用者がlibfabricを直接呼ぶことは少なく、通信ライブラリの下の層として出会う。[[MPICH]]は `--with-device=ch4:ofi` でlibfabricを用いる通信層を選び、[[Open MPI]]は `ofi` MTLなどのコンポーネントでlibfabricを用いる。[[Mercury]]も、ネットワークの抽象化層の一つとしてlibfabricを使える。Slingshotを用いるHPEのスーパーコンピュータやAWSのEFAでは、MPIはlibfabricの `cxi` や `efa` のプロバイダを通じてネットワークを使う。`fi_info` コマンドで利用可能なプロバイダとその性質を確認でき、環境変数 `FI_PROVIDER` で使うプロバイダを限定できる。通信の性能が想定より低いときは、意図しないプロバイダ（例えば `tcp`）が選ばれていないかを確かめる。

## 関係
- 上位概念: [[RDMA]]
- 使う / 使われる: [[Verbs]], [[InfiniBand]], [[NIC]]（プロバイダの対象）, [[MPI]], [[Mercury]]（libfabricを使う）
- 対比: [[UCX]]（同じくMPIの実装の下で多様なネットワークを抽象化する通信フレームワークであり、libfabricからプロバイダとして使うこともできる）
- 関連: [[Dragonfly Topology]]（Slingshot）

## 出典
- [Libfabric OpenFabrics](https://ofiwg.github.io/libfabric/)
- [fi_provider(7) - Libfabric Programmer's Manual](https://ofiwg.github.io/libfabric/main/man/fi_provider.7.html)
- [fi_endpoint(3) - Libfabric Programmer's Manual](https://ofiwg.github.io/libfabric/main/man/fi_endpoint.3.html)
- [fi_info(1) - Libfabric Programmer's Manual](https://ofiwg.github.io/libfabric/main/man/fi_info.1.html)
- [OpenFabrics Interfaces (OFI) / Libfabric support - Open MPI documentation](https://docs.open-mpi.org/en/main/tuning-apps/networking/ofi.html)
- [MPICH README](https://github.com/pmodels/mpich/blob/main/README.md)
