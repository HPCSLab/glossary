---
aliases: [xfs, Allocation Group, アロケーショングループ, mkfs.xfs, xfs_repair]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# XFS

> SGIが開発し、Linuxに移植された、大きなファイルと並列なI/Oに強い、ジャーナリングを行うローカルファイルシステムである。

## 概要
XFSは、1993年にSilicon Graphics（SGI）が自社のOSであるIRIXのために開発した。1999年にGPLのもとで公開され、2001年にLinuxに移植された。Red Hat Enterprise Linuxでは、2014年の7.0以降、標準のファイルシステムとなっている。

XFSは、ファイルシステムをアロケーショングループと呼ばれる独立した領域に分割する。各グループが空き領域やinodeを独自に管理するため、複数のCPUからのI/Oを並列に処理できる。空き領域とファイルの配置は、ビットマップではなく、連続したブロックの範囲（[[Extent|エクステント]]）を[[B-Tree|B+木]]で管理する。ブロックの割り当てをデータが実際に書き出されるまで遅らせる遅延割り当てによって、断片化を抑える。クラッシュに備えて、[[Metadata|メタデータ]]の変更をジャーナルに記録し、復旧にかかる時間はファイルシステムの大きさに依存しない。一方、ファイルシステムを縮小することはできない。

## どこで出てくるか
XFSは、[[ext4]]と並ぶLinuxの代表的なローカルファイルシステムであり、[[Rocky Linux]]などのRHEL系のディストリビューションでは標準である。大容量のディスクや、並列に読み書きされるサーバの用途で用いられる。永続メモリのfsdaxの領域の上に作ることもある（[[devdax]]を参照）。

## 関係
- 上位概念: [[File System]], [[Journaling File System]]
- 対比: [[ext4]], [[btrfs]]（コピーオンライト方式）
- 関連: [[B-Tree]], [[VFS]], [[Crash Consistency]]

## 出典
- [XFS - Wikipedia](https://en.wikipedia.org/wiki/XFS)
- [XFS Filesystem Documentation - The Linux Kernel documentation](https://docs.kernel.org/filesystems/xfs/index.html)
