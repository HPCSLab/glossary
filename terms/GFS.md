---
aliases: [Google File System, Googleファイルシステム, GFS master, chunkserver, チャンクサーバ, Record Append]
tags: [term]
maps: ["[[HPC Storage]]", "[[Distributed Systems]]"]
status: draft
updated: 2026-10-10
---
# GFS（Google File System）

> Googleが大量のデータの生成と処理のために作った分散ファイルシステムであり、安価な計算機の故障を前提に、巨大なファイルへの追記と順次読み込みに最適化している。

## 概要
GFSはGhemawat、Gobioff、Leungが2003年の[[SOSP]]で発表した。設計は、Googleの作業の観察から導いた次の前提に基づく。部品の故障は例外ではなく常態である。ファイルは数百MB〜数GBと大きい。ファイルは上書きされず、主に末尾への追記で変更され、書いた後は順に読まれる。これらに合わせて、従来の[[Distributed File System|分散ファイルシステム]]の設計を見直している。

GFSのクラスタは、一台のマスタと多数のチャンクサーバからなる。ファイルは64 MBの固定の大きさのチャンクに分けられ、各チャンクはチャンクサーバのLinuxのファイルとして格納され、既定で3台に複製される。名前空間やファイルからチャンクへの対応などの[[Metadata|メタデータ]]はすべてマスタのメモリに置かれ、変更は操作ログに記録されて複数の計算機に複製される。クライアントはチャンクの場所だけをマスタに問い合わせ、データの読み書きはチャンクサーバと直接行う。こうしてマスタを一台にして設計を単純にしつつ、データの経路からは外すことで、マスタがボトルネックになることを避けている。

GFSは[[POSIX]]のAPIを提供せず、[[Consistency Model|一貫性モデル]]も緩い。同じ領域への同時の書き込みの後は、全ての複製が同じ内容になるが、それがどの書き込みの結果とも一致しないことがある。代わりに、複数のクライアントが追加の同期なしに同じファイルに同時に追記できる record append という操作を持ち、各レコードは少なくとも一度、不可分に追記される。重複や詰め物の除去はアプリケーションが行う。

## どこで出てくるか
大規模なデータ処理のためのストレージの古典として、分散ストレージの論文の関連研究や講義でよく参照される。Hadoopの分散ファイルシステムであるHDFSは、GFSの論文に着想を得て作られたオープンソースのソフトウェアである。単一のマスタが[[Metadata|メタデータ]]を持つ設計は、クラスタの規模を制限する要因であり、Googleでは後継の[[Colossus]]がメタデータを分散させてこれを解消している。HPCの[[Parallel File System|並列ファイルシステム]]が多数のプロセスによる同じファイルへの細かい書き込みとPOSIXの意味論を重視するのに対し、GFSは追記を中心とする作業に合わせて意味論を緩めた点が対照的である。

## 関係
- 上位概念: [[Distributed File System]]
- 対比: [[Parallel File System]]（POSIXの意味論を保つのに対し、GFSは追記を中心に意味論を緩める）
- 関連: [[Colossus]], [[HDFS]], [[MapReduce]], [[Bigtable]]

## 出典
- [The Google File System (Ghemawat et al., SOSP 2003)](https://research.google/pubs/the-google-file-system/)
- [Colossus under the hood: a peek into Google's scalable storage system - Google Cloud Blog](https://cloud.google.com/blog/products/storage-data-transfer/a-peek-behind-colossus-googles-file-system)
- [Apache Hadoop - Wikipedia](https://en.wikipedia.org/wiki/Apache_Hadoop)
