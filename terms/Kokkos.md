---
aliases: [Kokkos Core, Kokkos Kernels, Kokkos::View, parallel_for, parallel_reduce, Execution Space, Memory Space, 実行空間, メモリ空間]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-11
---
# Kokkos

> 一つのC++のソースコードを、NVIDIAやAMDの[[GPU]]、マルチコアのCPUなど異なる計算機の上で、書き換えずに高い性能で動かすための、性能可搬性を目的とするプログラミングモデルとライブラリである。

## 概要
[[CUDA]]はNVIDIAのGPU専用であり、AMDのGPUにはHIP、IntelのGPUにはSYCL、CPUには[[OpenMP]]と、計算機ごとに書き方が異なる。スーパーコンピュータの世代が変わるたびにアプリケーションを書き直すことを避けるため、一つのソースコードのまま多くの計算機で十分な性能を出す性質を性能可搬性（performance portability）と呼ぶ。Kokkosは米国のSandia国立研究所で開発が始まったC++のライブラリであり、言語自体を拡張せず、上に挙げたCUDA、HIP、SYCL、OpenMP、C++の[[Thread|スレッド]]などをバックエンドとして用いる。どのバックエンドで動かすかはビルド時に[[CMake]]のオプション（`Kokkos_ENABLE_CUDA` など）で選び、一度のビルドで有効にできるGPUのバックエンドは一つである。

プログラムは、並列に実行する処理を `parallel_for`、`parallel_reduce`（総和などの集約を伴う）、`parallel_scan`（累積和）などの実行パターンにラムダ式で渡して書く。処理を実行する場所を実行空間（execution space）、データを置く場所をメモリ空間（memory space）と呼び、GPUで動かすときはデータをGPUのメモリに置く。データは多次元配列 `Kokkos::View` として確保する。KokkosはCPUとGPUの間でデータを暗黙には転送しないため、転送は `deep_copy` で明示的に書く。

Kokkosの特徴は、計算の割り当てだけでなく、データの並べ方（レイアウト）も実行空間に合わせて切り替える点にある。原論文は、移植の主な障害は並列の起動の仕方よりもメモリのアクセスパターンにあると論じた。二次元のViewは、CPUでは一つのスレッドが連続した要素をたどれるように行優先（`LayoutRight`）で、GPUでは同じワープの隣り合うスレッドが隣り合う要素を読み、アクセスがまとめられるように列優先（`LayoutLeft`）で配置される。これは、CPUの[[Cache|キャッシュ]]とGPUのメモリ[[Bandwidth|帯域]]を、同じソースコードのままそれぞれ有効に使うための工夫である。

## どこで出てくるか
米国のエクサスケール計算の計画（Exascale Computing Project）の一部として開発が進められ、異なる種類のGPUを搭載するエクサスケール機でのアプリケーションの性能可搬性を支えた。分子動力学のLAMMPSなどがKokkosによるGPU対応を持つ。線形代数の演算を提供するKokkos Kernelsや、性能を計測するKokkos Toolsも同じプロジェクトで開発されている。現在はLinux Foundation傘下のHigh Performance Software Foundation（HPSF）のプロジェクトである。

## 関係
- 上位概念: [[Performance Portability]]
- 前提: [[GPU]], [[C]]（C++のライブラリとして使う）
- 対比: [[OpenACC]]（指示文をコードに加えるのに対し、KokkosはC++のライブラリの呼び出しとして書く）
- 使う / 使われる: [[CUDA]], [[OpenMP]]

## 出典
- [About Kokkos - kokkos.org](https://kokkos.org/about/)
- [kokkos/kokkos - GitHub](https://github.com/kokkos/kokkos)
- [Configuration Guide - Kokkos documentation](https://kokkos.org/kokkos-core-wiki/get-started/configuration-guide.html)
- [Programming Model - Kokkos documentation](https://kokkos.org/kokkos-core-wiki/ProgrammingGuide/ProgrammingModel.html)
- [View: Multidimensional array - Kokkos documentation](https://kokkos.org/kokkos-core-wiki/ProgrammingGuide/View.html)
- [Kokkos: Enabling manycore performance portability through polymorphic memory access patterns (Edwards, Trott, Sunderland, JPDC 2014) - Sandia](https://www.sandia.gov/research/publications/details/kokkos-enabling-manycore-performance-portability-through-polymorphic-memory-2014-07-22/)
- [New Kokkos release improves performance portability among exascale-era heterogeneous architectures - Exascale Computing Project](https://www.exascaleproject.org/publication/new-kokkos-release-improves-performance-portability-among-exascale-era-heterogeneous-architectures/)
- [Kokkos 3: Programming Model Extensions for the Exascale Era (Trott et al., IEEE TPDS 2022) - Sandia](https://www.sandia.gov/research/publications/details/kokkos-3-programming-model-extensions-for-the-exascale-era-2022-04-01/)
- [Stan Moore: Kokkos in LAMMPS - LAMMPS Workshop 2019](https://www.lammps.org/workshops/Aug19/abstract_moore.html)
