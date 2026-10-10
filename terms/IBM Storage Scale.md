---
aliases: [GPFS, General Parallel File System, IBM Spectrum Scale, Spectrum Scale, Storage Scale, NSD, Network Shared Disk]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# IBM Storage Scale（GPFS）

> IBMが開発した、多数のノードが共有ディスクを介して同じファイルシステムを並列に読み書きする、クラスタ向けの[[Parallel File System|並列ファイルシステム]]である。旧称はGPFS（General Parallel File System）である。

## 概要
GPFSは、IBMのアルマデン研究所で開発され、その設計は2002年の最初の[[FAST]]で論文 "GPFS: A Shared-Disk File System for Large Computing Clusters"（SchmuckとHaskin）として発表された。製品名は、GPFSからIBM Spectrum Scale、さらにIBM Storage Scaleへと変更されたが、現在も構成要素や文書の中にはGPFSの名称が残っており、研究者の間でもGPFSと呼ばれることが多い。

GPFSは、共有ディスク型のファイルシステムである。すべてのノードが、記憶装置を共有のディスクとして参照し、データとメタデータの両方を直接読み書きする。記憶装置がすべてのノードに物理的に接続されていない場合は、NSD（Network Shared Disk）と呼ばれる仕組みで、一部のサーバがネットワーク越しにディスクを他のノードに提供する。[[Lustre]]がメタデータを専用のサーバ（MDS）に集約するのに対し、GPFSはメタデータの処理も多数のノードに分散させる点に特徴がある。

多数のノードが同じファイルやディレクトリを並列に更新しても[[POSIX]]の意味論を保つため、GPFSは[[Distributed Lock Manager|分散ロック]]（トークン）の仕組みを中心に設計されている。ノードは、ファイルのある範囲やメタデータを操作する権利をトークンとして取得し、他のノードと競合するまでは通信なしにキャッシュを用いて処理を進める。論文は、分散ロックと障害からの回復という既存の考え方を、大規模なクラスタに拡張するための工夫を主題としている。現在の製品は、[[NFS]]、SMB、[[Amazon S3|S3]]などのプロトコルでの提供、[[Snapshot|スナップショット]]、遠隔地への複製、クラウドの[[Object Storage|オブジェクトストレージ]]との階層化など、企業向けの機能も多く備えている。

## どこで出てくるか
GPFSは、Lustreと並ぶHPCの代表的な並列ファイルシステムであり、米国のスーパーコンピュータ[[ORNL|Summit]]やSierraをはじめ、多くの計算機センターや企業の大規模なストレージで用いられてきた。研究の文脈では、Lustreとともに、POSIX準拠の並列ファイルシステムの設計の代表例として比較される。特に、メタデータを集約するか分散するか、ロックをどの粒度で管理するかという設計の違いは、[[Metadata|メタデータ]]性能や[[Access Pattern|共有ファイル]]への書き込み性能の違いとして現れる。

## 関係
- 上位概念: [[Parallel File System]]
- 対比: [[Lustre]]（メタデータを専用サーバに集約する）, [[DAOS]]（オブジェクトを基本とする）
- 関連: [[POSIX]], [[Metadata]], [[Consistency Model]], [[FAST]]

## 出典
- [GPFS: A Shared-Disk File System for Large Computing Clusters - USENIX FAST 2002](https://www.usenix.org/conference/fast-02/gpfs-shared-disk-file-system-large-computing-clusters)
- [IBM Storage Scale overview - IBM Documentation](https://www.ibm.com/docs/en/storage-scale/5.2.3?topic=overview-storage-scale)
