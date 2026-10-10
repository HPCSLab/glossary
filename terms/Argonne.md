---
aliases: [Argonne National Laboratory, ANL, アルゴンヌ国立研究所, アルゴンヌ, ALCF, Argonne Leadership Computing Facility, Aurora]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# Argonne（アルゴンヌ国立研究所）

> 米国エネルギー省（DOE）の国立研究所の一つであり、イリノイ州のシカゴ近郊にある。HPCでは、エクサスケールのスーパーコンピュータAuroraの運用と、[[MPICH]]などの基盤ソフトウェアの開発で知られる。

## 概要
アルゴンヌ国立研究所は、マンハッタン計画の一部としてシカゴ大学に置かれた冶金研究所を前身とし、1946年に設立された。DOEが支援し、シカゴ大学が子会社のUChicago Argonne LLCを通じて運営している。職員は約3,400人である。計算機の分野では、Argonne Leadership Computing Facility（ALCF）がスーパーコンピュータを運用している。ALCFのAuroraは、IntelのXeon MaxのCPUとIntel Max seriesの[[GPU]]を用いる、エクサスケールのシステムである。

数値計算と並列計算のソフトウェアの開発の歴史も長い。1970年代に数値線形代数のプログラムをFortranに移したことが、[[LINPACK]]とEISPACKの開発につながった。[[MPI]]の代表的な実装である[[MPICH]]の開発は、1992年にアルゴンヌとミシシッピ州立大学で始まった。HPCの通信の基盤である[[Mercury]]も、アルゴンヌとThe HDF Groupが共同で開発した。I/Oの特性評価のツールである[[Darshan]]や、軽量なスレッドの枠組みである[[Argobots]]も、アルゴンヌが中心となって開発している。

## どこで出てくるか
MPICHや、Mercuryを基盤とする[[Margo|Mochi]]のプロジェクトなど、HPCのシステムソフトウェアの論文やソフトウェアの開発元として名前を見る。Auroraは[[TOP500]]の上位に入るシステムであり、2024年11月の一覧で3位であった。Auroraのストレージには[[DAOS]]が用いられている。

## 関係
- 上位概念: [[DOE National Laboratories]]
- 使う / 使われる: [[MPICH]], [[Mercury]], [[Darshan]], [[Argobots]]（開発元）, [[DAOS]]（Auroraのストレージ）
- 対比: [[LLNL]], [[ORNL]]（同じDOEの国立研究所）
- 関連: [[TOP500]]

## 出典
- [Argonne National Laboratory - Wikipedia](https://en.wikipedia.org/wiki/Argonne_National_Laboratory)
- [Aurora (supercomputer) - Wikipedia](https://en.wikipedia.org/wiki/Aurora_(supercomputer))
- [November 2024 - TOP500](https://www.top500.org/lists/top500/2024/11/)
