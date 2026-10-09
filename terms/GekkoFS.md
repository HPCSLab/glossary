---
aliases: [gekkofs, GekkoFS burst buffer file system]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# GekkoFS

> 複数の[[Compute Node|計算ノード]]のローカルな記憶装置を束ね、ジョブの実行中だけ存在する一時的な[[Distributed File System|分散ファイルシステム]]を、ユーザ空間で構築するアドホックファイルシステムである。

## 概要
GekkoFSは、ドイツのマインツ大学（JGU）とスペインのバルセロナ・スーパーコンピューティング・センター（BSC）が開発し、2018年の[[IEEE Cluster]]で発表された（Vefら、"GekkoFS - A Temporary Distributed File System for HPC Applications"）。データ集約型のHPCアプリケーションの新しいアクセスのパターンに合わせて最適化された、一時的でスケーラブルなバーストバッファのファイルシステムである。

GekkoFSは、ジョブに割り当てられた各計算ノードの高速なローカルの記憶装置（主に[[SSD]]）をまとめ、すべての参加ノードからアクセスできる一つの名前空間を提供する。[[POSIX]]の意味論は緩和されており、多くのアプリケーションが実際に必要とする機能だけを提供する。各ノードではデーモンが動作し、[[Metadata|メタデータ]]はノードごとの[[RocksDB]]（[[Key-Value Store|キーバリューストア]]）に格納される。ノード間の通信には[[Mercury]]と[[Margo]]を用いる。メタデータとデータは、完全なパス名のハッシュ値によって担当のノードが決まる（[[Full-Path Indexing|フルパスインデックス]]）。このため、名前の変更（[[rename]]）は困難であり、既定では無効の実験的な機能にとどまる。アプリケーションは、`LD_PRELOAD` で読み込むクライアントのライブラリを介して利用し、このライブラリがファイル操作の[[System Call|システムコール]]を横取りしてGekkoFSに転送する。カーネルを改変せずに一般の利用者が起動でき、論文では、512ノードのクラスタで毎秒数千万のメタデータ操作を達成したと報告している。

## どこで出てくるか
GekkoFSは、計算ノードのローカルな記憶装置を、ジョブごとに一時的な共有ファイルシステムとして使う[[Ad Hoc File System|アドホックファイルシステム]]の一つであり、常設の[[Parallel File System|並列ファイルシステム]]とは別に、ジョブの中で用いる。日本で開発された[[CHFS]]の論文は、GekkoFSを比較の対象としている。米国で開発された[[UnifyFS]]も、ノードローカルな記憶装置を用いる同種のファイルシステムである。

## 関係
- 対比: [[Parallel File System]], [[Lustre]]（ジョブ間で共有される常設のファイルシステム）
- 使う / 使われる: [[Mercury]], [[Margo]], [[RocksDB]], [[SSD]]
- 関連: [[CHFS]], [[UnifyFS]], [[LLIO]], [[POSIX]], [[Metadata]]

## 出典
- [GekkoFS - A Temporary Distributed File System for HPC Applications (Vef et al., IEEE Cluster 2018) - Semantic Scholar](https://www.semanticscholar.org/paper/GekkoFS-A-Temporary-Distributed-File-System-for-HPC-Vef-Moti/4f57678b3999190f0602fb1f4779aac840eaeafd)
- [Installing GekkoFS - GekkoFS documentation](https://storage.bsc.es/projects/gekkofs/documentation/users/building.html)
- [GekkoFS - Glenn K. Lockwood](https://www.glennklockwood.com/garden/gekkofs)
- [GekkoFS README - BSC GitLab](https://storage.bsc.es/gitlab/hpc/gekkofs/-/blob/master/README.md)（renameの扱い）
- [gekkofs/src/common/rpc/distributor.cpp - BSC GitLab](https://storage.bsc.es/gitlab/hpc/gekkofs/-/blob/master/src/common/rpc/distributor.cpp)（パス名のハッシュによるノードの決定）
