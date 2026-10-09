---
aliases: [Fujitsu Exabyte File System, 富士通 FEFS, 第2階層ストレージ]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# FEFS（Fujitsu Exabyte File System）

> 富士通が[[Lustre]]を基に拡張した[[Parallel File System|並列ファイルシステム]]であり、スーパーコンピュータ「京」と[[Fugaku|富岳]]で用いられている。

## 概要
FEFSは、富士通がLustreに、大規模な計算機での運用のための拡張と調整を加えたファイルシステムである。主な拡張は、RAS（信頼性・可用性・保守性）、運用のしやすさ、高いI/Oの負荷の下での安定性、多数のクライアントの間での公平な資源の配分（fair-share）の管理などである。富士通はLustreのコミュニティの一員であり、不具合の修正などをコミュニティに報告している。

「京」では、Lustre 1.8を基にしたFEFSが用いられた。京は、二層のファイルシステムを持っていた。[[Compute Node|計算ノード]]から使うローカルファイルシステム（約11PB）と、利用者のデータを置くグローバルファイルシステム（30PB以上）であり、どちらもFEFSであった。ジョブの実行の前に必要なファイルをグローバルファイルシステムからローカルファイルシステムへ移し（ステージイン）、実行の後に結果を戻す（ステージアウト）運用であった。

富岳では、約8年にわたる京での運用の経験を踏まえ、Lustre 2.10を基にしたFEFSが、第2階層のストレージ（約150PB、複数のボリューム）として用いられている。計算ノードの近くの[[SSD]]による第1階層（[[LLIO]]）と連携して、計算中のI/Oを速くし、第2階層の負荷を減らす。第2階層とI/Oノードの間は[[InfiniBand]]で接続されている。

## どこで出てくるか
富岳でジョブを実行する際には、第2階層のFEFSを直接用いるか、[[LLIO]]が提供するキャッシュや一時領域を用いるかを選ぶことになる。FEFSはLustreを基にしているため、ストライプなどの基本的な考え方はLustreに従う。

## 関係
- 上位概念: [[Lustre]]（FEFSはLustreを基にした製品である）
- 使う / 使われる: [[Fugaku]], [[LLIO]]
- 対比: [[EXAScaler]]（同じくLustreを基にした商用の製品）
- 関連: [[Parallel File System]], [[InfiniBand]]

## 出典
- [Status of Lustre-Based Filesystem at the Supercomputer Fugaku (LUG 2020) - Lustre Wiki](https://wiki.lustre.org/images/c/cc/LUG2020-Lustre_File_System_at_Fugaku-Tsujita.pdf)
- [Current Status of FEFS for the K computer (LUG 2012) - Lustre Wiki](https://wiki.lustre.org/images/8/80/LUG-2012-FEFS-Fujitsu.pdf)
