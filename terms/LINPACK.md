---
aliases: [Linpack, linpack, HPL, High Performance LINPACK, High-Performance Linpack, Rmax, Rpeak, LINPACKベンチマーク]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# LINPACK（HPL）

> 密行列の連立一次方程式を解く計算によって計算機の浮動小数点演算性能を測るベンチマークであり、その分散メモリ計算機向けの実装HPLは、[[TOP500]]の順位付けに用いられる。

## 概要
LINPACKベンチマークは、Jack Dongarraによって導入された。$Ax = b$ の形の密な連立一次方程式を、部分ピボット選択付きのLU分解によって解き、その所要時間から性能を求める。演算は64ビットの倍精度浮動小数点数で行い、演算回数は $\frac{2}{3}n^3 + O(n^2)$ として数える。Strassenの方法のような高速な行列積のアルゴリズムや、反復改良による精度の補正は認められない。問題の大きさ $n$ は、計算機の性能が最大になるように利用者が選んでよい。

報告される主な値は三つある。Rmaxは、ある問題の大きさで達成した最大の実効性能であり、TOP500の順位はこの値で決まる。Rpeakは、ハードウェアの仕様から求めた理論上の最大性能である。$N_{1/2}$ は、Rmaxの半分の性能が得られる問題の大きさである。

HPL（High Performance LINPACK）は、このベンチマークを分散メモリの計算機で実行するための可搬な実装であり、ランダムに生成した密な連立一次方程式を倍精度で解く。通信に[[MPI]]を、行列演算にBLAS（Basic Linear Algebra Subprograms）を用いる。

## どこで出てくるか
LINPACKは、TOP500を通じて、ほぼすべての主要なスーパーコンピュータについて性能の値が得られる点で、広く用いられている。一方、開発者自身が述べているとおり、この性能は計算機の全体的な性能を表すものではなく、どの単一の数値もそれを表すことはできない。LINPACKが測るのは密な連立一次方程式を解く性能である。TOP500の運営者は、別のベンチマークであるHPCGによる一覧も公表している。

## 関係
- 使う / 使われる: [[TOP500]]（LINPACKで順位付けする）, [[MPI]]（HPLが用いる）
- 対比: [[IOR]]（I/Oの性能を測るベンチマーク）
- 関連: [[GPU]]

## 出典
- [The LINPACK Benchmark - TOP500](https://top500.org/project/linpack/)
- [HPL - A Portable Implementation of the High-Performance Linpack Benchmark for Distributed-Memory Computers - Netlib](https://www.netlib.org/benchmark/hpl/)
- [Introduction - TOP500](https://top500.org/project/introduction/)
