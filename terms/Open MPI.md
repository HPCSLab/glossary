---
aliases: [OpenMPI, Open-MPI, ompi, mpirun]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# Open MPI

> 学術機関、研究機関、企業の共同体によって開発・保守されている、オープンソースの[[MPI]]の実装である。

## 概要
Open MPIは、それまで別々に開発されていた四つのMPIの実装を統合して生まれた。テネシー大学のFT-MPI、ロスアラモス国立研究所のLA-MPI、インディアナ大学のLAM/MPI、そしてシュトゥットガルト大学のPACX-MPIである。ライセンスは修正BSDライセンスである。IBMのRoadrunnerや、日本のスーパーコンピュータ「京」など、多くのHPCシステムで用いられてきた。

Open MPIは、MPIの関数そのものを実装する層（OMPI）、実行環境の層（ORTE）、移植のための層（OPAL）に分かれた、モジュール化された構造を持つ。Slurm、PBS、LSFなどのジョブスケジューラの環境でプログラムを起動できる。2026年10月の時点で、安定版の系列は5.0であり、6.0の公開が予告されている。

## どこで出てくるか
Open MPIは、[[MPICH]]とその派生の実装と並ぶ、代表的なMPIの実装の一つである。通信の層として[[UCX]]を用いることができる。同じMPIのプログラムでも、実装や版によって性能や挙動が異なることがあるため、性能を報告する際には、使用したMPIの実装とその版を明記する必要がある。名前が似ている[[OpenMP]]は、共有メモリ上のスレッド並列のための全く別の規格である。

## 関係
- 上位概念: [[MPI]]（Open MPIはMPIの実装である）
- 対比: [[MPICH]]（もう一つの代表的なMPIの実装）, [[OpenMP]]（名前が似ている別の規格）
- 使う / 使われる: [[UCX]], [[InfiniBand]]
- 関連: [[Slurm]]

## 出典
- [Open MPI](https://www.open-mpi.org/)
- [Open MPI documentation](https://docs.open-mpi.org/en/main/)
- [Open MPI - Wikipedia](https://en.wikipedia.org/wiki/Open_MPI)
- [OpenUCX documentation](https://openucx.readthedocs.io/en/master/)（Open MPIがUCXを用いることについて）
