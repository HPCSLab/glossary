---
aliases: [Distributed Asynchronous Object Storage, DAOS Foundation, libdaos, dfuse, DFS]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# DAOS

> HPCとAIのために設計された、ユーザ空間で動作する分散オブジェクトストレージであり、高いバンド幅とIOPS、低いレイテンシを特徴とする。正式名称は Distributed Asynchronous Object Storage である。

## 概要
DAOSは、もとはIntelが開発したオープンソースのストレージシステムであり、現在はLinux Foundation傘下のDAOS Foundationが開発を統括している。米国アルゴンヌ国立研究所のスーパーコンピュータAurora、ドイツのライプニッツ・スーパーコンピューティング・センターのSuperMUC-NG、Google CloudのParallelstoreなどで用いられている。

DAOSの設計上の最大の特徴は、OSのカーネルを経由しないことである。サーバは[[NVMe]] SSDに[[SPDK]]を用いてユーザ空間から直接アクセスし、クライアントとサーバの間の通信は[[RDMA]]を含む高速ネットワークのインタフェース（OFI）を用いて行う。これにより、[[System Call|システムコール]]、[[Page Cache|ページキャッシュ]]、[[blk-mq|ブロック層]]といったカーネルのI/O経路のオーバーヘッドを避ける。記憶媒体は二層に分かれ、[[Metadata|メタデータ]]や小さなデータのような[[Latency|レイテンシ]]に敏感なI/Oは高速なメモリ層に、大きなデータはNVMe SSDに置かれる。

データモデルは、ファイルとディレクトリの階層ではなく、オブジェクトを基本とする。記憶領域はプールとして確保され、その中にコンテナを作り、コンテナの中にオブジェクトを格納する。オブジェクトは、キーで値や配列を引く多段のキーバリュー構造を持つ。既存のデータを書き換えずに新しい版を書く方式を採り、版の管理によるスナップショット、分散トランザクション、複製や消失訂正符号による冗長化を提供する。

## どこで出てくるか
DAOSは、[[POSIX]]の強い意味論と単一のメタデータサーバへの集中が[[Parallel File System|並列ファイルシステム]]の拡張を妨げている、という問題意識に対する代表的な解答の一つである。HPCストレージの研究では、[[Lustre]]と並ぶ比較対象として扱われる。アプリケーションはDAOSの独自のAPI（libdaos）を直接用いることもできるが、既存のプログラムのために、POSIXのファイルシステムとして見せるDFSとその[[FUSE]]によるマウント（dfuse）、[[MPI-IO]]や[[HDF5]]の接続部品も提供されている。ただし、POSIXのインタフェースを経由すると、DAOSの性能上の利点の一部が失われる場合がある。どの層のインタフェースを用いるかは、性能と既存のプログラムとの互換性の兼ね合いで選ぶ。

## 関係
- 上位概念: [[Object Storage]]
- 使う / 使われる: [[NVMe]], [[RDMA]], [[MPI-IO]], [[HDF5]], [[FUSE]]（dfuse）
- 対比: [[Lustre]], [[IBM Storage Scale]]（POSIXの並列ファイルシステム）
- 関連: [[Parallel File System]], [[Metadata]], [[Key-Value Store]]

## 出典
- [Architecture - DAOS documentation](https://docs.daos.io/latest/overview/architecture/)
- [DAOS](https://daos.io/)
