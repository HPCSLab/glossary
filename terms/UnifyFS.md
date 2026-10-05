---
aliases: [unifyfs, UnifyFS burst buffer file system]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# UnifyFS

> スーパーコンピュータの計算ノードのローカルな記憶装置に対して、ジョブの実行中だけ存在する共有の名前空間を提供する、ユーザレベルの一時的なファイルシステムである。

## 概要
UnifyFSは、米国のローレンス・リバモア国立研究所（LLNL）とオークリッジ国立研究所（ORNL）が開発しており、2023年のIPDPSで論文 "UnifyFS: A User-level Shared File System for Unified Access to Distributed Local Storage" として発表された。この論文は、IPDPSで初めて設けられた、オープンソースへの貢献に対する最優秀賞を受けた。

UnifyFSの目的は、計算ノードのローカルな高速の記憶装置（バーストバッファ）を、センター全体の[[Parallel File System|並列ファイルシステム]]と同じくらい容易に使えるようにすることである。アプリケーションはUnifyFSのクライアントのライブラリとリンクして用いる。このライブラリが入出力の呼び出しを横取りし、UnifyFSのファイルに対する要求をUnifyFSのサーバに送り、それ以外のファイルの要求は通常のシステムに渡す。UnifyFSはジョブの実行中にのみ存在し、サーバが終了するとファイルシステムも消える。そのため、ジョブの後も残す必要のあるデータは、UnifyFSが提供するAPIやツールで、常設のファイルシステムへ明示的に移す必要がある。チェックポイントとリスタートのような、HPCのアプリケーションに典型的な一括同期型の入出力を主な対象としている。

## どこで出てくるか
UnifyFSは、[[GekkoFS]]や[[CHFS]]と並ぶ、ノードローカルな記憶装置を用いる[[Ad Hoc File System|アドホックファイルシステム]]の一つである。論文では、書き込みの性能がよく拡張し、調整済みの構成に比べてアプリケーションのチェックポイントの性能を最大で3倍改善したと報告している。

## 関係
- 対比: [[GekkoFS]], [[CHFS]]（同じくアドホックファイルシステム）, [[Parallel File System]]
- 関連: [[LLIO]], [[SSD]], [[POSIX]]

## 出典
- [UnifyFS - Lawrence Livermore National Laboratory](https://computing.llnl.gov/projects/unifyfs)
- [UnifyFS Overview - UnifyFS documentation](https://unifyfs.readthedocs.io/en/latest/overview.html)
- [UnifyFS: A User-level Shared File System for Unified Access to Distributed Local Storage - Oak Ridge National Laboratory](https://www.ornl.gov/publication/unifyfs-user-level-shared-file-system-unified-access-distributed-local-storage)
- [UnifyFS Team Wins IPDPS Award for Open Source Software - LLNL](https://software.llnl.gov/news/2023/06/27/unifyfs/)
