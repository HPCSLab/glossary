---
aliases: [アドホックファイルシステム, Ad-hoc File System, Ad Hoc Parallel File System, Burst Buffer, バーストバッファ, BeeOND, BeeGFS On Demand, BurstFS]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# Ad Hoc File System（アドホックファイルシステム）

> ジョブなどに割り当てられた計算ノードの上に、そのノードのローカルな高速の記憶装置を束ねて一時的に構築し、一つのアプリケーションや一連の作業のためだけに用いるファイルシステムである。

## 概要
並列計算機のクラスタでは、ジョブ間で共有される常設の記憶装置（[[Parallel File System|並列ファイルシステム]]の背後のディスク）とは別に、[[SSD]]や不揮発性メモリといった、より高速な記憶装置が計算ノードの中に搭載されるようになった。アドホックファイルシステムは、こうしたノードローカルな記憶装置を科学技術計算の作業の流れに体系的に組み込むための手法であり、一群の計算ノードの上に、一つのアプリケーション、あるいはより長く続く一連の計算（キャンペーン）のための一時的な記憶領域として構築される。

アドホックファイルシステムは、ジョブの開始とともに作成され、ジョブの終了とともに消えるのが典型的である。そのため、計算に必要な入力のデータを常設のファイルシステムから事前に読み込み（ステージイン）、残すべき結果を終了前に書き戻す（ステージアウト）作業が必要となる。アプリケーションからの利用の方法は様々であり、マウントポイントとして見せるもの、[[FUSE]]を用いるもの、入出力の呼び出しを横取りするライブラリを用いるものなどがある。

代表的な例として、既存の並列ファイルシステム[[BeeGFS]]を基に、ジョブに割り当てられたノードの記憶装置を束ねて一時的なBeeGFSを作るBeeOND（BeeGFS On Demand）がある。研究の試作としては、[[GekkoFS]]、BurstFS、[[CHFS]]、[[UnifyFS]]などが提案されている。また、[[Fugaku|富岳]]の[[LLIO]]は、計算ノードの近くのSSDを用いて、第2階層のファイルシステムのキャッシュと、ジョブ用の一時領域を提供する。

## どこで出てくるか
アドホックファイルシステムは、HPCストレージの研究の主要な題材の一つである。2017年のDagstuhlセミナーでの議論をもとにまとめられた総説（Brinkmannら、2020年）は、BeeOND、GekkoFS、BurstFSを例として、アドホックファイルシステムが提供するインタフェースと意味論を比較し、バッチジョブのスケジューラとの統合や、常設のファイルシステムとの間のデータのステージングの調整を、今後の研究課題として挙げている。例えば、[[CHFS]]の論文は、BeeONDやGekkoFSとの比較によって性能を評価している。

関連する概念として、バーストバッファがある。バーストバッファは、アプリケーションと外部の記憶装置の間に高速な記憶の層を置いて、チェックポイントなどの短時間に集中する書き込みを一時的に受け止めるという考え方である。2012年の研究（Liuら）は、バーストバッファによって、アプリケーションから見た外部の記憶装置へのスループットを高められ、目標のスループットを満たすために必要な外部の記憶装置の帯域を減らせることを示した。GekkoFSやUnifyFSは、自らをバーストバッファのためのファイルシステムと位置付けている。

## 関係
- 上位概念: [[File System]]
- 対比: [[Parallel File System]]（ジョブ間で共有される常設のファイルシステム）
- 使う / 使われる: [[GekkoFS]], [[CHFS]], [[UnifyFS]], [[LLIO]]（アドホックファイルシステムの例）
- 関連: [[Node-local Storage]], [[Lustre PCC]], [[SSD]], [[Intel Optane Persistent Memory]], [[FUSE]], [[Metadata]]

## 出典
- [Ad Hoc File Systems for High-Performance Computing (Brinkmann et al., Journal of Computer Science and Technology, 2020)](https://jcst.ict.ac.cn/EN/10.1007/s11390-020-9801-1)
- [BeeOND: BeeGFS On Demand - BeeGFS Documentation](https://doc.beegfs.io/latest/advanced_topics/beeond.html)
- [On the Role of Burst Buffers in Leadership-class Storage Systems (Liu et al., MSST 2012)](https://doi.org/10.1109/MSST.2012.6232369)
- [GekkoFS documentation](https://storage.bsc.es/projects/gekkofs/documentation/users/building.html)
- [UnifyFS - GitHub](https://github.com/LLNL/UnifyFS)
- [CHFS: Parallel Consistent Hashing File System for Node-local Persistent Memory - 筑波大学 HPCS研究室](https://www.hpcs.cs.tsukuba.ac.jp/publications/2022/hpcasia2022tatebe/)
