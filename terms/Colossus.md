---
aliases: [Google Colossus, Curator, Custodian, D file server]
tags: [term]
maps: ["[[HPC Storage]]", "[[Distributed Systems]]"]
status: draft
updated: 2026-10-10
---
# Colossus

> Googleのクラスタ単位のファイルシステムであり、[[GFS]]の後継として、Googleの多くのストレージサービスやサービスのデータを支える。

## 概要
[[GFS]]は一台のマスタのメモリにすべての[[Metadata|メタデータ]]を置いていたため、クラスタの規模がそのマスタで制限されていた。Colossusはこの点を改め、メタデータのサービスを水平に増やせる多数のCuratorで構成し、メタデータそのものはGoogleのNoSQLデータベースである[[Bigtable]]に格納する。Googleによれば、これにより最大のGFSのクラスタの100倍以上の規模に拡張でき、一つのクラスタがエクサバイト級の容量と数万台の計算機を扱える。

構成要素は四つである。アプリケーションが使うクライアントライブラリは、ソフトウェアによる[[RAID]]などの機能を含み、システムの中で最も複雑な部分とされる。Curatorはファイルの作成などの制御の操作を受け持つ。データはクライアントと、ネットワークに接続されたディスクであるDファイルサーバとの間で直接やりとりされる。Custodianは、ディスクの使用量の平準化やRAIDの再構成などを背景で行い、耐久性と可用性を保つ。データの経路からメタデータのサーバを外す点はGFSと同じである。

## どこで出てくるか
ColossusはGoogleの内部のシステムであり、その構成は主にGoogle Cloudのブログなどの公開資料と、他のシステムの論文の記述から知られる。例えば[[Spanner]]の論文は、Spannerのデータを格納する[[Distributed File System|分散ファイルシステム]]としてColossusを挙げている。Google Cloud Storageなどのストレージサービスや、YouTube、Gmailなどのサービスも、Colossusの上に構築されている。

## 関係
- 上位概念: [[Distributed File System]]
- 対比: [[GFS]]（単一のマスタのメモリにメタデータを置くのに対し、Colossusはメタデータを分散したデータベースに置く）
- 使う / 使われる: [[Bigtable]], [[Spanner]]

## 出典
- [Colossus under the hood: a peek into Google's scalable storage system - Google Cloud Blog](https://cloud.google.com/blog/products/storage-data-transfer/a-peek-behind-colossus-googles-file-system)
- [Spanner: Google's Globally-Distributed Database (Corbett et al., OSDI 2012)](https://research.google/pubs/spanner-googles-globally-distributed-database-2/)
