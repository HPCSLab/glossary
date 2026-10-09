---
aliases: [Fourth Extended Filesystem, ext4fs, ext3, ext2]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# ext4

> Linuxで最も広く用いられるローカルファイルシステムの一つであり、ext2・ext3の後継として、大容量化と信頼性の向上を図ったものである。

## 概要
ext4は、ext3を拡張して64ビットのブロック番号を扱えるようにし、16TBを超えるファイルシステムを可能にした。[[Block Storage|ブロックデバイス]]上に構築され、[[VFS]]の下で[[Superblock|スーパーブロック]]、[[Inode|inode]]、ディレクトリなどのディスク上の構造を管理する。記憶領域はブロックグループという単位に分割され、ブロックの割り当て器は、一つのファイルのブロックをなるべく同じグループ内に収めて、アクセスの局所性を高める。

ファイルのデータ位置の管理には、エクステント（extent）を用いる。エクステントは「論理ブロック番号の範囲と、それに対応する連続した物理ブロックの範囲」の組であり、一つで最大32768ブロックを表せる。ext2・ext3が用いた間接ブロック方式では、ブロック一つごとに位置を記録する必要があったため、連続したファイルでも[[Metadata|メタデータ]]が大きくなった。ext4では、inode内に最初の4個のエクステントを直接格納でき、それを超えると最大5段のエクステント木に拡張する。大きなディレクトリについては、ファイル名のハッシュをキーとする平衡木（htree）を用い、名前の探索を線形走査より高速にしている。

書き込みでは遅延割り当て（delayed allocation）が既定で有効である。[[write]]の時点では物理ブロックを割り当てず、[[Page Cache|ページキャッシュ]]から書き戻す時点で、まとまったデータに対して連続した領域を一括して割り当てる。これにより断片化が減る。クラッシュ時の整合性は、[[JBD2]]によるジャーナリングで保証する。データの扱いは、マウントオプション `data=` で選択する。既定の `ordered` では、メタデータのみをジャーナルに記録し、データをメタデータの記録より先に本来の位置に書き出す。`journal` では、データもジャーナルに記録する。`writeback` では、データとメタデータの順序を保証しない。

## どこで出てくるか
ext4は多くのLinuxディストリビューションで標準のファイルシステムであり、ローカルディスクのI/O性能を評価する際の基準として扱われることが多い。新しいファイルシステムやストレージ機構を提案する論文では、ext4との比較が頻繁に行われる。また、[[Parallel File System|並列ファイルシステム]]の中には、ストレージサーバ上でデータを格納する下位層としてext4やその派生を用いるものがある。運用面では、`mkfs.ext4`・`tune2fs`・`dumpe2fs`・`debugfs` などの[[e2fsprogs]]のツールで、作成・設定変更・内部構造の調査を行う。inodeの総数は作成時に決まるため、小さなファイルが極めて多い用途では、作成時のパラメータに注意を要する。

## 関係
- 上位概念: [[File System]]
- 前提: [[Block Storage]], [[Inode]]
- 使う / 使われる: [[JBD2]], [[VFS]], [[Page Cache]]
- 対比: [[XFS]]
- 関連: [[Superblock]], [[fsync]]

## 出典
- [ext4 General Information - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/ext4.html)
- [The Contents of inode.i_block - The Linux Kernel documentation](https://docs.kernel.org/filesystems/ext4/ifork.html)
- [Directory Entries - The Linux Kernel documentation](https://docs.kernel.org/filesystems/ext4/directory.html)
- [High Level Design - The Linux Kernel documentation](https://docs.kernel.org/filesystems/ext4/overview.html)
