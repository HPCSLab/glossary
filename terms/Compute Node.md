---
aliases: [計算ノード, ノード, Node, Login Node, ログインノード, Cluster, クラスタ]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# Compute Node（計算ノード）

> HPCのクラスタやスーパーコンピュータを構成する個々の計算機のうち、利用者のジョブの計算を実際に実行するために用いられるものである。

## 概要
HPCの意味でのクラスタは、高帯域かつ低遅延の通信を提供するネットワークで接続された、多数のノードの集まりである。ノードは、一つ以上のCPUのソケットを持つ一台の計算機である。ノードは役割によって区別され、計算ノードは、メモリを多く使う、あるいは長時間にわたる科学技術計算などの実際の計算を実行するために用いられる。これに対し、ログインノードは、利用者が施設の計算機に接続するために用いられ、多くの場合、プログラムの試験や対話的な作業にも使える。

計算ノードの利用は、[[Slurm]]などのジョブスケジューラが管理する。スケジューラは、計算ノードへの排他的あるいは非排他的なアクセスを一定の時間だけ利用者に割り当て、割り当てたノードの上で並列のジョブを起動・実行・監視し、待ち行列によって資源の競合を調停する。並列プログラムは、[[MPI]]などによって、割り当てられた多数の計算ノードの上で協調して動作し、ノード間は[[InfiniBand]]などの高速なネットワークで通信する。[[Fugaku|富岳]]は158,976台の計算ノードからなる。

## どこで出てくるか
計算ノードからは、一般に、ホームディレクトリ（`/home`）や作業用の[[Parallel File System|並列ファイルシステム]]（`/work` など）といった、ノード間で共有されるファイルシステムを利用できる。これに加えて、多くの施設では、各計算ノードが、そのノードだけで使える一時的な記憶領域（[[Node-local Storage|ローカルストレージ]]）を持つ。どのファイルシステムがどのノードから見えるか、どれが共有でどれがノードに閉じているかを把握しておくことは、I/Oの性能と、データを失わないための運用の両面で重要である。

## 関係
- 対比: ログインノード（接続と対話的な作業のためのノード）
- 使う / 使われる: [[Node-local Storage]], [[Parallel File System]], [[InfiniBand]]
- 関連: [[MPI]], [[Slurm]], [[Fugaku]]

## 出典
- [HPC-Dictionary - HPC Wiki](https://hpc-wiki.info/hpc/HPC-Dictionary)
- [File System Separation (Admin Guide) - HPC Wiki](https://hpc-wiki.info/hpc/Admin_Guide_File_System_Separation)
- [Fugaku (supercomputer) - Wikipedia](https://en.wikipedia.org/wiki/Fugaku_(supercomputer))
- [Slurm Workload Manager - Overview](https://slurm.schedmd.com/overview.html)
