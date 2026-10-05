---
aliases: [ジャーナリングファイルシステム, Journaling, ジャーナリング, Journal, Physical Journaling, Logical Journaling, Metadata Journaling, メタデータジャーナリング]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# Journaling File System（ジャーナリングファイルシステム）

> ファイルシステムを更新する前に、行う変更をジャーナルと呼ばれるログに記録しておき、クラッシュの後にそれを再実行することで一貫した状態に素早く戻せるファイルシステムである。

## 概要
ファイルの作成や追記のような一つの操作でも、[[Inode|inode]]、ディレクトリ、空き領域の管理情報など、ディスク上の複数の場所への書き込みが必要である。その途中で電源断やクラッシュが起きると、データ構造が一貫しない状態で残る。従来は、起動時に `fsck` でファイルシステム全体の構造を調べて修復していたが、容量が大きいほど時間がかかった。

ジャーナリングでは、変更を本来の場所に書く前に、まずジャーナルに記録する（先行書き込みログ）。クラッシュの後は、ジャーナルを読んで記録された変更を再実行するだけで、一貫した状態に戻せる。ジャーナルへの記録が完了した変更は全て再実行され、完了していない変更は捨てられるため、一連の変更は不可分になる。全てのブロックをジャーナルに記録する物理ジャーナリングは、データも保護できるが、同じブロックを二度書くため性能の負担が大きい。[[Metadata|メタデータ]]の変更のみを記録する論理ジャーナリングは、性能はよいが、データとメタデータが食い違うおそれがある。

## どこで出てくるか
Linuxの[[ext4]]（[[JBD2]]を用いる）と[[XFS]]は、いずれもジャーナリングファイルシステムである。ext4は既定ではメタデータのみをジャーナルに記録し（`data=ordered`）、マウントのオプション `data=journal` でデータもジャーナルに記録できる。クラッシュの後の一貫性を保つ方式には、ほかに、更新を常に新しい場所に書く[[ZFS]]や[[btrfs]]のコピーオンライト方式がある。ジャーナリングが保証するのはファイルシステムの構造の一貫性であり、アプリケーションのデータの永続化には[[fsync]]が必要である（[[Crash Consistency]]を参照）。

## 関係
- 上位概念: [[File System]]
- 対比: [[Copy-on-Write]]（[[ZFS]]、[[btrfs]]が採る方式）
- 使う / 使われる: [[ext4]], [[XFS]], [[JBD2]]
- 関連: [[Crash Consistency]], [[fsync]], [[Metadata]]

## 出典
- [Journaling file system - Wikipedia](https://en.wikipedia.org/wiki/Journaling_file_system)
- [ext4 Data Structures and Algorithms: Journal (jbd2) - The Linux Kernel documentation](https://docs.kernel.org/filesystems/ext4/journal.html)
