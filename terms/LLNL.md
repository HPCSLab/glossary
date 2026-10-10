---
aliases: [Lawrence Livermore National Laboratory, ローレンス・リバモア国立研究所, リバモア国立研究所, Livermore, LC, Livermore Computing, El Capitan]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# LLNL（ローレンス・リバモア国立研究所）

> 米国エネルギー省（DOE）の国家核安全保障局（NNSA）を主な支援元とする、カリフォルニア州リバモアにある国立研究所である。HPCでは、スーパーコンピュータEl Capitanの運用と、[[Slurm]]や[[Spack]]などの多くのソフトウェアの開発で知られる。

## 概要
LLNLは、1952年にカリフォルニア大学放射線研究所のリバモア支所として、アーネスト・ローレンスとエドワード・テラーによって設立された。カリフォルニア大学、Bechtelなどの共同体であるLawrence Livermore National Security, LLCが運営し、職員は約1万人である。主な使命は、核兵器の安全性、確実性、信頼性を科学と工学によって保証することである。

計算機は、Livermore Computingが運用している。El Capitanは、AMDのInstinct MI300Aの[[APU]]を用いるHPE Crayのシステムであり、2024年11月の[[TOP500]]で1位となり、2026年6月の一覧で中国のLineShineに抜かれるまでその座を保った。その主な目的は、核兵器の備蓄の管理を支えることであり、機密の計算に用いられる。

## どこで出てくるか
LLNLは、HPCの現場で使われるソフトウェアの開発元として頻繁に名前を見る。ジョブスケジューラの[[Slurm]]、パッケージマネージャの[[Spack]]、資源管理の枠組みであるFlux、Linuxへの[[ZFS]]の移植（ZFS on Linux）などがLLNLで開発された。ストレージの分野では、[[ORNL]]とともに[[UnifyFS]]を開発している。

## 関係
- 上位概念: [[DOE National Laboratories]]
- 使う / 使われる: [[Slurm]], [[Spack]], [[UnifyFS]], [[ZFS]]（開発元）
- 対比: [[Argonne]], [[ORNL]]（DOEの科学局（Office of Science）の研究所であり、LLNLはNNSAの研究所である）
- 関連: [[TOP500]], [[APU]]

## 出典
- [Lawrence Livermore National Laboratory - Wikipedia](https://en.wikipedia.org/wiki/Lawrence_Livermore_National_Laboratory)
- [El Capitan (supercomputer) - Wikipedia](https://en.wikipedia.org/wiki/El_Capitan_(supercomputer))
- [November 2024 - TOP500](https://www.top500.org/lists/top500/2024/11/)
- [June 2026 - TOP500](https://www.top500.org/lists/top500/2026/06/)
