---
aliases: [並列ファイルシステム, PFS, Parallel Filesystem]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-11
---
# Parallel File System（並列ファイルシステム）

> 多数のストレージサーバにファイルのデータを分散配置し、多数のクライアントから並列に読み書きさせることで、単一サーバを大きく超えるI/O性能と容量を提供する[[File System|ファイルシステム]]である。

## 概要
並列ファイルシステムは、利用者からは通常のファイルとディレクトリの階層として見え、多くは[[POSIX]]のインタフェースを提供する。内部では、名前空間と[[Metadata|メタデータ]]を管理するメタデータサーバと、ファイルの内容を格納するデータサーバとを分離するのが一般的である。代表例である[[Lustre]]では、前者をMDS（その記憶領域をMDT）、後者をOSS（同じくOST）と呼ぶ。クライアントは、[[open]]などの名前空間の操作をメタデータサーバに問い合わせてファイルのデータ配置を知り、以後の[[read]]・[[write]]はメタデータサーバを介さずにデータサーバと直接行う。これにより、データ転送の[[Bandwidth|帯域]]はデータサーバの台数に応じて拡大する。

一つのファイルの内容は、[[RAID|ストライピング]]によって複数のデータサーバに分割して配置される。ファイルを一定の大きさ（ストライプサイズ）の断片に区切り、指定した数（ストライプ数）のデータサーバに順に割り当てる方式であり、大きなファイルへのアクセスを多数のサーバに並列に分散できる。Lustreでは、`lfs setstripe` によりファイルやディレクトリごとにこれらを設定できる。

![[Parallel File System Striping.excalidraw]]

多数のクライアントがそれぞれキャッシュを持ちながら同じファイルを共有するため、POSIXの一貫性を保つには、クライアント間の協調が必要となる。Lustreは[[Distributed Lock Manager|分散ロックマネージャ]]（LDLM）を用い、ファイルの範囲ごとのロックによってキャッシュの整合性を保つ。クライアントとサーバの間は、[[InfiniBand]]などの高速ネットワークで接続され、[[RDMA]]による転送が用いられることが多い。代表的な実装には、Lustre、[[IBM Storage Scale]]（旧GPFS）、[[BeeGFS]]、OrangeFS（旧PVFS）などがある。

## どこで出てくるか
スーパーコンピュータやHPCクラスタでは、全[[Compute Node|計算ノード]]が共有する作業領域として並列ファイルシステムが提供され、入力データ、チェックポイント、計算結果の置き場となる。その性能は[[Access Pattern|アクセスパターン]]に強く依存する。各プロセスが別々のファイルに書く方式（N-N、file-per-process）は、ロックの競合が少ない一方で、プロセス数に比例してファイルが増え、メタデータサーバの負荷が高まる。全プロセスが一つの共有ファイルに書く方式（N-1）は、ファイル数を抑えられる一方で、書き込み範囲がストライプやロックの境界とずれていると、ロックの競合により性能が大きく低下する。これを緩和する手段として、[[MPI-IO]]の[[Collective IO|集団的I/O]]などが用いられる。

小さなファイルを大量に作成する処理や、`ls -l`・`find` による大規模なディレクトリ走査は、すべてのクライアントが共有するメタデータサーバに負荷を集中させ、他の利用者の性能まで低下させることがある。このため、ファイルをまとめて扱う、Lustreでは `find` の代わりに `lfs find` を用いる、といった運用上の配慮が求められる。また、メタデータ性能の拡張のために、Lustreでは[[DNE]]により名前空間を複数のMDTに分散できる。並列ファイルシステムの性能は、データ帯域を測る[[IOR]]やメタデータ性能を測る[[mdtest]]などのベンチマークで評価され、これらを組み合わせた[[IO500]]というランキングも公開されている。

## 関係
- 上位概念: [[File System]], [[Distributed File System]]
- 前提: [[POSIX]], [[Metadata]]
- 使う / 使われる: [[Lustre]], [[IBM Storage Scale]], [[BeeGFS]]（実装例）
- 対比: [[Object Storage]]（POSIXの意味論を持たず、より容易に規模を拡大できる）
- 関連: [[MPI-IO]], [[Page Cache]], [[Consistency Model]]

## 出典
- [Introduction to Lustre - Lustre Wiki](https://wiki.lustre.org/Introduction_to_Lustre)
- [Lustre Software Release 2.x Operations Manual](https://doc.lustre.org/lustre_manual.xhtml)
- [Clustered file system - Wikipedia](https://en.wikipedia.org/wiki/Clustered_file_system)
