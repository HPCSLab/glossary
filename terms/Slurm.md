---
aliases: [slurm, SLURM, Slurm Workload Manager, sbatch, srun, salloc, squeue, scancel, sinfo, "#SBATCH", ジョブスケジューラ, Job Scheduler, Partition, パーティション]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# Slurm

> Linuxのクラスタで、計算資源を利用者のジョブに割り当て、ジョブの実行と待ち行列を管理する、オープンソースのジョブスケジューラである。

## 概要
Slurmは、耐故障性と高いスケーラビリティを持つ、クラスタの管理とジョブのスケジューリングのためのシステムである。その役割は三つある。第一に、利用者に計算資源（[[Compute Node|計算ノード]]）を一定の時間、排他的あるいは非排他的に割り当てる。第二に、割り当てたノードの上で並列のジョブを起動し、実行し、監視する枠組みを提供する。第三に、待ち行列によって、資源をめぐる競合を調停する。

Slurmは、全体の資源と負荷を監視する中央の管理デーモン（slurmctld）と、各計算ノードで動き、ジョブの実行を担うデーモン（slurmd）からなる。ノードはパーティションと呼ばれる組に分けられ、パーティションはジョブの待ち行列として働く。ジョブは利用者に割り当てられた資源であり、その中で実行される一連の（多くは並列の）タスクをジョブステップと呼ぶ。

## どこで出てくるか
計算機センターやクラスタで計算を行う際には、ログインノードで直接計算するのではなく、スケジューラにジョブを投入する。Slurmでは、ジョブスクリプトに `#SBATCH` で始まる行で資源の量（ノード数や時間など）を指定し、`sbatch` で投入する。対話的に使う場合は `salloc` で資源を確保する。`srun` はジョブステップを起動し、[[MPI]]のプログラムの起動にも用いられる。ジョブの状態は `squeue` で、パーティションとノードの状態は `sinfo` で確認し、ジョブの取り消しには `scancel` を用いる。

ジョブスケジューラは計算機センターごとに異なり、Slurm以外のものが用いられていることもある。用いるシステムの利用手引きで、スケジューラの種類と指定の方法を確認する必要がある。

## 関係
- 使う / 使われる: [[Compute Node]], [[MPI]], [[Open MPI]]
- 関連: [[Fugaku]], [[Miyabi]]

## 出典
- [Slurm Workload Manager - Overview](https://slurm.schedmd.com/overview.html)
- [Slurm Workload Manager - Quick Start User Guide](https://slurm.schedmd.com/quickstart.html)
