---
aliases: [openmp, OMP, OMP_NUM_THREADS, pragma omp, "#pragma omp parallel for", Fork-Join, フォーク・ジョイン, スレッド並列]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# OpenMP

> C、C++、Fortranで、共有メモリ上のスレッドによる並列プログラムを、主にコンパイラへの指示文（ディレクティブ）を書き加えることで記述するためのAPIである。

## 概要
OpenMPの仕様は、非営利の団体であるOpenMP ARB（Architecture Review Board）が策定している。最初の仕様は1997年（Fortran）と1998年（C/C++）に公開され、その後、2008年の3.0でタスクの構文が、2013年の4.0でGPUなどのアクセラレータに処理を移す（target offloading）ための指示文が加わった。同じ目的の指示文の規格に[[OpenACC]]がある。最新の版は2024年11月の6.0である。

OpenMPは、フォーク・ジョインのモデルに基づく。プログラムは一つのスレッドで始まり、並列化する部分に来ると、そのスレッドが複数のスレッドを生成して処理を分担させ、終わると再び一つのスレッドに戻る。並列化する部分は、C/C++では `#pragma omp parallel for` のような指示文で示し、例えばこの指示文を付けたループは、その繰り返しが複数のスレッドに分配される。スレッドの数は、環境変数 `OMP_NUM_THREADS` や実行時の関数で指定する。指示文を書き加えることで、元の逐次のプログラムを大きく書き換えずに並列化できる。

## どこで出てくるか
OpenMPは、一つの計算ノードの中の多数のコアを使うための並列化の手段として広く用いられる。複数のノードを用いる大規模な並列計算では、ノード間の並列化を[[MPI]]で、ノード内の並列化をOpenMPで行うハイブリッド並列が用いられる。名前が似ている[[Open MPI]]は、MPIの実装であり、OpenMPとは全く別のものである。

OpenMPによる並列化は手軽である一方、注意も要する。複数の[[Thread|スレッド]]が同じ変数を同時に書き換えると競合（データ競合）が起き、結果が誤る。また、異なるスレッドが同じキャッシュラインの別々の変数を頻繁に書き換えると、偽共有（false sharing）によって性能が低下することがある。並列化の効果は、[[Strong Scaling|強スケーリング]]の測定で確認する。

## 関係
- 対比: [[MPI]]（プロセスとメッセージ通信による分散メモリの並列化）, [[Open MPI]]（名前が似ている別のもの）
- 関連: [[Parallel Efficiency]], [[Strong Scaling]], [[GPU]], [[Compute Node]]

## 出典
- [About Us - OpenMP](https://www.openmp.org/about/about-us/)
- [OpenMP Specifications - OpenMP](https://www.openmp.org/specifications/)
- [OpenMP - Wikipedia](https://en.wikipedia.org/wiki/OpenMP)
