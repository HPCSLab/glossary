---
aliases: [MVAPICH2, MVAPICH2-GDR, MVAPICH2-X, MVAPICH-Plus]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# MVAPICH

> オハイオ州立大学のNetwork-Based Computing Laboratoryが開発する、[[MPICH]]を基にした[[MPI]]の実装であり、[[InfiniBand]]などの高速なインターコネクトでの性能に重点を置く。

## 概要
MVAPICHは、MPICHを基にしてオハイオ州立大学が開発するMPIの実装であり、BSDライセンスで公開されている。基にした版のMPICHとはABI互換であるため、そのMPICHでビルドしたプログラムをMVAPICHのライブラリで動かすことができる。対応するネットワークは、InfiniBand、[[RoCE]]、iWARP、Omni-Path、HPE（Cray）のSlingshotなど、[[RDMA]]を備えた高速なインターコネクトが中心である。

MVAPICHは用途ごとの派生版を持つ。MVAPICH2-GDRは、NVIDIAやAMDの[[GPU]]を持つクラスタと、GPUを用いる深層学習のアプリケーション向けに最適化した版である。MVAPICH2-Xは、MPIに加えて[[OpenSHMEM]]、UPC、UPC++などの[[PGAS]]のモデルを一つの実行環境で扱えるようにしたものである。長くMVAPICH2の名で配布されてきたが、3.0の系列から名称はMVAPICHに改められ、MVAPICH2-GDRとMVAPICH2-Xの機能はMVAPICH-Plusに統合された。

## どこで出てくるか
スーパーコンピュータやInfiniBandのクラスタで、利用できるMPIの一つとして `module` で選ぶ場面で出会う。開発元はMPIなどの通信性能を測る[[OSU Micro-Benchmarks]]も配布しており、そのベンチマークは他のMPIの実装の評価にも広く用いられる。MPIの通信の最適化を扱う論文では、[[Open MPI]]やMPICHと並ぶ比較対象として現れる。開発元の発表では、2026年10月の時点で94か国の3,500以上の組織で利用されている。

## 関係
- 上位概念: [[MPI]]（MVAPICHはMPIの実装である）
- 前提: [[MPICH]]（MVAPICHの基になっている）
- 対比: [[Open MPI]]（もう一つの代表的なMPIの実装）
- 使う / 使われる: [[InfiniBand]], [[RDMA]]
- 関連: [[OSU Micro-Benchmarks]], [[PGAS]]

## 出典
- [MVAPICH :: Home](https://mvapich.cse.ohio-state.edu/)
- [MVAPICH - Wikipedia](https://en.wikipedia.org/wiki/MVAPICH)
