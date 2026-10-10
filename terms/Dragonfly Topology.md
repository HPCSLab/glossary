---
aliases: [Dragonfly, ドラゴンフライ, Dragonfly Network, Dragonflyトポロジ, Network Topology, ネットワークトポロジ, Slingshot, HPE Slingshot, Global Link, グローバルリンク]
tags: [term]
maps: ["[[Network]]", "[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# Dragonfly Topology（Dragonflyトポロジ）

> ポートの数の多いスイッチをいくつか束ねたグループを一つの大きな仮想的なスイッチとみなし、グループの間を少数の長いケーブルで直接結ぶ、スーパーコンピュータのネットワークの形（トポロジ）である。

## 概要
Dragonflyは、Kim、Dally、Scott、Abtsが、2008年のISCAで提案した。大規模なネットワークの費用の多くはケーブル、特に筐体の間をつなぐ長いケーブルが占める。Dragonflyは、ポート数（radix）の多いスイッチをグループにまとめ、グループの内部は短いケーブルで密に結び、各グループから他の全てのグループへは少数のグローバルなリンクで直接結ぶ。これにより、グループ全体が非常にポート数の多い一つの仮想的なスイッチのように働き、少ない長いケーブルで多くのノードを結べる。最短の経路をとるパケットは、グローバルなリンクを高々一度しか通らない。

論文では、1万6千ノード以上の構成で、Flattened Butterflyに比べて約20%、折り返し型のClos網（folded Clos）に比べて約52%、費用を減らせるとしている。一方、グローバルなリンクに通信が集中すると混雑しやすいため、負荷に応じて他のグループを経由する経路を選ぶ適応的な経路制御が必要となる。論文は、そのための経路制御の方式も提案している。

## どこで出てくるか
Dragonflyは、CrayのXCと、Cray/HPEのEXのスーパーコンピュータで用いられている。EXのシステムは、ポート数64のスイッチを持つHPE SlingshotのEthernetのインターコネクトを用い、米国の最初のエクサスケールの計算機である[[ORNL|Frontier]]などに選ばれた。スーパーコンピュータの仕様には、ネットワークのトポロジとして、Dragonflyやファットツリー（例えば[[Miyabi]]の[[InfiniBand]]のネットワーク）などが記される。同じ名前の[[DragonflyDB|インメモリのデータストア]]とは別のものである。

## 関係
- 関連: [[InfiniBand]], [[Collective Communication]], [[MPI]], [[Miyabi]]

## 出典
- [Technology-Driven, Highly-Scalable Dragonfly Topology (Kim, Dally, Scott, Abts, ISCA 2008)](https://doi.org/10.1109/ISCA.2008.19)
- [Introduction to the Miyabi Supercomputer System - Information Technology Center, The University of Tokyo](https://www.cc.u-tokyo.ac.jp/en/supercomputer/miyabi/system.php)（ファットツリーの例）
- [RETROSPECTIVE: Technology-Driven, Highly-Scalable Dragonfly Topology (Kim et al., ISCA@50 Retrospective, 2023)](https://sites.coecis.cornell.edu/isca50retrospective/files/2023/06/Kim_2008_Technology.pdf)
