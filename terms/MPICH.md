---
aliases: [mpich, MPICH2, MVAPICH, MVAPICH2, Intel MPI]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# MPICH

> [[Argonne|アルゴンヌ国立研究所]]などが開発する、自由に利用できる移植性の高い[[MPI]]の実装であり、多くの企業のMPIの実装の基盤となっている。

## 概要
MPICHの開発は、1992年に、策定中であったMPIの規格に合わせて、アルゴンヌ国立研究所とミシシッピ州立大学で始まった。名前の "CH" は、移植性の高い並列プログラミングのライブラリであった Chameleon に由来する。2001年にMPI-2に対応するために書き直されて以降はMPICH2と呼ばれ、2012年11月に再びMPICHの名に戻った。米国の政府系の研究機関が開発した、オープンソースとパブリックドメインの部品からなる。

MPICHは、多くの企業のMPIの実装の基盤となっている。Intel、Microsoft、Cray、IBMのMPIの実装のほか、オハイオ州立大学のMVAPICHもMPICHを基にしている。MPICHは、2005年にR&D 100 Awardを、2024年には「計算科学と工学の30年にわたる進歩を支えた」としてACM Software System Awardを受けた。

## どこで出てくるか
MPICHは、[[Open MPI]]と並ぶ代表的なMPIの実装であり、IntelやCrayなどの企業のMPIの実装もMPICHを基にしている。通信の層として[[UCX]]を用いることができる。MPIのプログラムの性能や挙動は、実装や版によって異なることがあるため、性能を報告する際には、使用したMPIの実装とその版を明記する必要がある。

## 関係
- 上位概念: [[MPI]]（MPICHはMPIの実装である）
- 対比: [[Open MPI]]（もう一つの代表的なMPIの実装）
- 使う / 使われる: [[UCX]]
- 関連: [[MPI-IO]]

## 出典
- [MPICH - Wikipedia](https://en.wikipedia.org/wiki/MPICH)
- [OpenUCX documentation](https://openucx.readthedocs.io/en/master/)（MPICHがUCXを用いることについて）
