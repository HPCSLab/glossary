---
aliases: [Oak Ridge National Laboratory, オークリッジ国立研究所, Oak Ridge, OLCF, Oak Ridge Leadership Computing Facility, Frontier, Summit, Titan]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# ORNL（オークリッジ国立研究所）

> 米国エネルギー省（DOE）の国立研究所の一つであり、テネシー州オークリッジにある。HPCでは、世界初のエクサスケールのスーパーコンピュータFrontierを運用したことで知られる。

## 概要
ORNLは、1943年にマンハッタン計画の一部として設立され、初期にはプルトニウムを生産するX-10黒鉛炉を擁した。テネシー大学とBattelle Memorial Instituteの共同体であるUT-Battelle, LLCが運営し、職員は約5,700人である。計算機は、Oak Ridge Leadership Computing Facility（OLCF）が運用している。

ORNLは、何代にもわたって世界最速のスーパーコンピュータを設置してきた。Jaguarは2009年から2010年にかけて世界最速であり、それを[[GPU]]で強化したTitanは2012年11月の[[TOP500]]で1位となった。Summitは2018年11月から2020年6月まで世界最速であった。Frontierは、2022年5月に1.102 EFLOPSを記録し、世界で初めてエクサスケールに達したシステムである。AMDのEPYCのCPUとInstinct MI250XのGPUを用い、ネットワークにはHPEのSlingshotによる[[Dragonfly Topology|Dragonfly]]のトポロジを、ストレージには容量700PBの[[Lustre]]のファイルシステムであるOrionを用いる。

## どこで出てくるか
Frontierは、2024年11月にEl Capitan（[[LLNL]]）に抜かれるまでTOP500の1位であり、エクサスケールのシステムの代表例として論文や講演で言及される。ストレージの分野では、LLNLとともに[[UnifyFS]]を開発している。

## 関係
- 上位概念: [[DOE National Laboratories]]
- 使う / 使われる: [[Lustre]], [[Dragonfly Topology]]（Frontierの構成要素）, [[UnifyFS]]（開発元）
- 対比: [[Argonne]], [[LLNL]]（同じDOEの国立研究所）
- 関連: [[TOP500]], [[GPU]]

## 出典
- [Oak Ridge National Laboratory - Wikipedia](https://en.wikipedia.org/wiki/Oak_Ridge_National_Laboratory)
- [Frontier (supercomputer) - Wikipedia](https://en.wikipedia.org/wiki/Frontier_(supercomputer))
- [Frontier - Oak Ridge Leadership Computing Facility](https://www.olcf.ornl.gov/frontier/)
- [November 2024 - TOP500](https://www.top500.org/lists/top500/2024/11/)
