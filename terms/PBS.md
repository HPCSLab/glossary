---
aliases: [Portable Batch System, PBS Professional, PBS Pro, OpenPBS, TORQUE, qsub, qstat, qdel, "#PBS", PBS_DPREFIX]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# PBS（Portable Batch System）

> クラスタやスーパーコンピュータで、利用者のジョブを待ち行列に入れ、計算資源を割り当てて実行させるジョブスケジューラの系統であり、`qsub` などのコマンドで使う。

## 概要
PBSは、1991年にNASAの契約による事業として、MRJ Technology Solutionsが開発を始めた。その後、開発の担い手は、2003年にAltair Engineeringに移った。現在は主に三つの系統がある。Altairの商用版であるPBS Professional（PBS Pro）、そのオープンソース版であるOpenPBS（2016年にPBS Proがオープンソースとして公開され、2020年5月にOpenPBSと改称された）、およびAdaptive Computingが保守する派生のTORQUEである。

PBSの基本のコマンドは、POSIX（IEEE Std 1003.1）のバッチ環境のユーティリティとして規格化されている。`qsub` でジョブのスクリプトを投入し、`qstat` でジョブの状態を確かめ、`qdel` でジョブを取り消す。ジョブのスクリプトの中では、`#PBS` で始まる行に、`qsub` のオプション（資源の量、実行時間、待ち行列の名前など）を書いておける。

## どこで出てくるか
計算機センターのスーパーコンピュータのジョブスケジューラには、[[Slurm]]やPBSなどがある。例えば、JCAHPCの[[Miyabi]]はPBS Professionalを用いている。両者は考え方が似ており、Slurmの `sbatch`、`squeue`、`scancel` に、PBSの `qsub`、`qstat`、`qdel` がおおむね対応する。ただし、資源の指定の書き方（何ノード、何コア、何GPUを使うか）や待ち行列の名前は、スケジューラの種類だけでなく計算機センターごとにも異なるため、利用する計算機の利用手引きを確認する必要がある。

## 関係
- 対比: [[Slurm]]（もう一つの代表的なジョブスケジューラ）
- 使う / 使われる: [[Miyabi]], [[Compute Node]]
- 関連: [[MPI]], [[POSIX]]

## 出典
- [Portable Batch System - Wikipedia](https://en.wikipedia.org/wiki/Portable_Batch_System)
- [OpenPBS](https://www.openpbs.org/)
- [openpbs/openpbs - GitHub](https://github.com/openpbs/openpbs)（OpenPBSへの改称）
- [qsub - The Open Group Base Specifications Issue 7 (IEEE Std 1003.1)](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/qsub.html)
- [qstat - The Open Group Base Specifications Issue 7 (IEEE Std 1003.1)](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/qstat.html)
- [qdel - The Open Group Base Specifications Issue 7 (IEEE Std 1003.1)](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/qdel.html)
- [Miyabi システム概要（塙敏博, PCクラスタコンソーシアム HPC研究会, 2025）](https://www.pccluster.org/ja/event/data/250627_PCC-WS-Kashiwa_16_hanawa-miyabi.pdf)
