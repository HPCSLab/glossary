---
aliases: [singularfs, Log-free Metadata Operations, Hierarchical Concurrency Control, Hybrid Inode Partition]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# SingularFS

> 単一のメタデータサーバで十億規模のファイルを扱うことを目指し、[[Intel Optane Persistent Memory|永続メモリ]]と[[RDMA]]を前提にそのサーバの性能を引き出す、清華大学の[[Distributed File System|分散ファイルシステム]]である。

## 概要
SingularFSは、Hao Guo、Youyou Luらが、2023年の[[USENIX ATC]]で発表した。多くの分散ファイルシステムは、[[Metadata|メタデータ]]サーバを増やして十億規模のファイルに対応する。一方、論文は、データセンタの分散ファイルシステムの多くは十億ファイル以内の規模であり、そのメタデータは一台のサーバに収まると主張する。一台であれば、サーバ間の分散トランザクションと負荷分散が不要になる。サーバは永続メモリの上の[[Key-Value Store|キーバリューストア]]に全ての[[Inode|inode]]を格納し、クライアントはユーザ空間のライブラリからRDMAでサーバと通信する。ファイルのデータはメタデータと分離し、[[Object Storage|オブジェクトストア]]で管理する。

一台のサーバの性能を引き出すため、主な工夫は三つある。第一に、ログを用いないメタデータ操作（log-free metadata operations）である。ディレクトリのエントリを子のinodeと同じキー（親のinode番号と名前）に置くことで、エントリとinodeの更新を一回のキーバリューの更新にまとめる。さらに、inodeに作成時刻と削除時刻を加え、子のinodeを更新してから親のディレクトリの時刻を更新するという順序を守る。これにより、[[rename]]以外の操作では、[[Journaling File System|ジャーナリング]]なしに[[Crash Consistency|クラッシュ一貫性]]を保つ。第二に、階層的な並行制御（hierarchical concurrency control）である。多数のクライアントが一つのディレクトリにファイルを作成すると、親のディレクトリのロックが競合する。SingularFSは、inodeの書き換えにはinodeごとの読み書きロックを用い、親のディレクトリの時刻の更新はロックを用いずにアトミックな命令で行う。第三に、ハイブリッドなinodeの分割（hybrid inode partition）である。ディレクトリのinodeから時刻の情報を切り出し、その子のinodeと同じ[[NUMA]]ノードに置くことで、ファイルの操作がNUMAノードをまたがないようにする。

論文では、一台のメタデータサーバで、ファイルの作成で8.36M IOPS、属性の取得で18.80M IOPSを達成し、32台のメタデータサーバを用いたInfiniFSが論文で報告した性能を上回ったと報告している。比較の対象には、[[Ceph|CephFS]]、InfiniFS、ローカルの永続メモリ向けファイルシステムの[[NOVA]]などが含まれる。

## どこで出てくるか
SingularFSは、分散ファイルシステムのメタデータの性能に関する研究で、メタデータサーバを増やす方向とは逆に、一台のサーバの性能を高める方向の代表例として参照される。共有ディレクトリでの一斉のファイルの作成によるロックの競合は、[[mdtest]]などで測定されるHPCのメタデータの負荷でも問題となる。

## 関係
- 上位概念: [[Distributed File System]]
- 前提: [[Metadata]], [[Inode]], [[Crash Consistency]]
- 対比: [[IndexFS]]（メタデータを多数のサーバに分散して拡張する）
- 使う / 使われる: [[Intel Optane Persistent Memory]], [[RDMA]], [[Key-Value Store]]
- 関連: [[NUMA]], [[USENIX ATC]]

## 出典
- [SingularFS: A Billion-Scale Distributed File System Using a Single Metadata Server (USENIX ATC '23)](https://www.usenix.org/conference/atc23/presentation/guo)
- [論文PDF - USENIX](https://www.usenix.org/system/files/atc23-guo.pdf)
