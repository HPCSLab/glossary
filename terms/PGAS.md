---
aliases: [Partitioned Global Address Space, 区分化大域アドレス空間, 分割大域アドレス空間, UPC, Unified Parallel C, Coarray Fortran, Coarray, Chapel, UPC++]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# PGAS（Partitioned Global Address Space）

> 全[[Process|プロセス]]から参照できる一つの大域的なアドレス空間を考え、それを各プロセスが受け持つ部分に区切ることで、共有メモリのような書きやすさと、データの局所性の明示とを両立させる並列プログラミングのモデルである。

## 概要
分散メモリの並列計算機で広く用いられる[[MPI]]は、プロセスが自分のメモリだけを持ち、他のプロセスのデータは送信と受信の対で明示的にやり取りする。一方、[[OpenMP]]のような共有メモリのモデルは、どのデータにもそのまま読み書きできるが、平坦なアドレス空間ではデータがどこにあるかを区別できない。PGASはその中間にあたる。大域的なアドレス空間を通じて他のプロセスのデータを直接読み書きできる一方、アドレス空間は各プロセスが受け持つ部分に区切られており、どのデータが手元にあり、どれが遠くにあるかをプログラムで区別できる。

遠くのデータへのアクセスは、相手のプロセスが受信の操作をしなくても行える片側通信（put・get）で実現される。これは、相手のCPUを介さずに相手のメモリを読み書きする[[RDMA]]の機能とよく対応する。PGASの言語やライブラリには、Coarray Fortran、Cを拡張したUPC（Unified Parallel C）、ChapelやX10などの言語、Global Arraysなどのライブラリ、そして[[OpenSHMEM]]がある。日本では、[[Omni Compiler]]が実装するXcalableMPが、coarrayの記法による片側通信を備えている。

## どこで出てくるか
並列プログラミングモデルの研究や、MPIの代わりとなる通信の方式を比較する議論で出てくる。[[libfabric]]のような高速ネットワークの通信ライブラリも、MPIと並んでPGASやSHMEMを設計の対象としている。[[GPU]]の間の通信でも、[[OpenSHMEM|NVSHMEM]]のようにPGASのモデルが用いられている。

## 関係
- 対比: [[MPI]]（送受信の対によるメッセージ通信）, [[OpenMP]]（共有メモリのスレッド並列）
- 使う / 使われる: [[OpenSHMEM]], [[Omni Compiler]]（PGASのモデルによる実装）, [[RDMA]]
- 関連: [[libfabric]]

## 出典
- [Partitioned global address space - Wikipedia](https://en.wikipedia.org/wiki/Partitioned_global_address_space)
- [SHMEM - Wikipedia](https://en.wikipedia.org/wiki/SHMEM)
- [NVSHMEM - NVIDIA Documentation](https://docs.nvidia.com/nvshmem/api/introduction.html)
