---
aliases: [Non-Uniform Memory Access, 不均一メモリアクセス, ccNUMA, NUMAノード, NUMA Node, numactl, First Touch, ファーストタッチ]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# NUMA（不均一メモリアクセス）

> 一台の計算機の主記憶が複数の部分に分かれてそれぞれのCPUに接続され、CPUから見てどの部分のメモリにアクセスするかによって[[Latency|レイテンシ]]と[[Bandwidth|帯域]]が異なるメモリの構成である。

## 概要
複数のCPUソケットを持つサーバでは、各ソケットが自分のメモリコントローラと[[DRAM]]を持ち、ソケットの間は専用の接続で結ばれる。全てのCPUが全てのメモリを同じアドレス空間で読み書きできるが、自分のソケットのメモリ（ローカル）へのアクセスは、他のソケットのメモリ（リモート）へのアクセスより速い。一つのバスに全てのメモリを接続する構成では、CPUの数が増えるとバスが性能の上限となるため、メモリをCPUごとに分散させたのがNUMAである。一つのソケットの中でも、コアの多いCPUでは、メモリコントローラごとに複数のNUMAノードに分割する設定がある。

[[Linux Kernel|Linux]]は、CPUとメモリの組をNUMAノードとして扱い、既定ではメモリを、それを要求したCPUのノードから割り当てる（local allocation）。物理ページは最初に触れたときのページフォルトで割り当てられるため（[[Virtual Memory|仮想記憶]]を参照）、配列を一つの[[Thread|スレッド]]で初期化すると、全てのページがそのスレッドのノードに置かれ、他のノードのスレッドは全てリモートのアクセスになる。この配置の規則をファーストタッチと呼ぶ。`numactl` を用いると、ノードの構成を表示し（`--hardware`）、[[Process|プロセス]]を実行するCPUのノード（`--cpunodebind`）と、メモリを割り当てるノード（`--membind`、`--interleave`）を指定できる。

## どこで出てくるか
[[OpenMP]]や[[MPI]]のプログラムの性能の測定では、スレッドやプロセスをどのコアに固定するか（アフィニティ）と、メモリをどのノードに置くかによって、結果が大きく変わる。このため、論文の実験環境には、ソケットの数とNUMAノードの構成を記載し、`numactl` で配置を固定して測定する。ストレージの研究では、[[NIC]]や[[SSD]]が接続されたソケットと、I/Oを処理するスレッドのソケットが異なると性能が下がるため、NUMAノードを意識した配置が論点となる。[[SingularFS]]は、[[Metadata|メタデータ]]を分割してNUMAノードをまたぐアクセスを減らした例である。[[CXL]]で接続したメモリや、[[devdax]]の領域を主記憶として追加したものは、CPUを持たないNUMAノードとしてOSに見える。

## 関係
- 前提: [[DRAM]], [[Virtual Memory]]
- 関連: [[Latency]], [[Bandwidth]], [[Thread]], [[OpenMP]], [[CXL]]

## 出典
- [What is NUMA? - The Linux Kernel documentation](https://docs.kernel.org/mm/numa.html)
- [numactl(8) - Linux manual page](https://man7.org/linux/man-pages/man8/numactl.8.html)
