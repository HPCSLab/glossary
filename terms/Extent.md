---
aliases: [エクステント, Unwritten Extent, 未書き込みエクステント, Uninitialized Extent, Extent Tree, エクステント木, FIEMAP, filefrag]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# Extent（エクステント）

> ファイルの論理的な範囲と、それを格納する記憶装置上の連続したブロックの範囲との対応を、「開始位置と長さ」の一組で表したものである。

## 概要
[[File System|ファイルシステム]]は、ファイルのデータが[[Block Storage|ブロックデバイス]]上のどこにあるかを[[Metadata|メタデータ]]として記録する。古い方式であるブロックマップ（ext2・ext3の間接ブロック）は、ブロック一つごとに物理位置を記録するため、データが連続して置かれていても、ファイルが大きいほどメタデータが大きくなる。エクステントは連続した範囲をまとめて一つの記録で表すので、連続に配置された大きなファイルを少ないメタデータで表せる。その分、エクステントの数はファイルの断片化の度合いを直接表す。断片化を抑えるために、ファイルシステムは[[Delayed Allocation|遅延割り当て]]などによって、連続した領域をまとめて割り当てようとする。

[[ext4]]のエクステントは12バイトの構造体であり、ファイル内の先頭の論理ブロック番号、ブロック数、物理ブロック番号を持つ。一つで表せるのは最大32768ブロックである。[[Inode|inode]]の中に最初の4個までを直接格納でき、それを超えると最大5段のエクステント木に拡張する。[[XFS]]は、エクステントを[[B-Tree|B+木]]で管理する。

エクステントには、領域は割り当て済みだがデータをまだ書いていないことを示す未書き込み（unwritten）の状態がある。ファイルシステム経由で未書き込みの範囲を読むとゼロが返る。このため、`fallocate()` による範囲のゼロ埋め（`FALLOC_FL_ZERO_RANGE`）は、範囲を未書き込みのエクステントに変換することで、装置に実際にゼロを書かずに実現できる。

## どこで出てくるか
ファイルの断片化を調べるときに出てくる。[[e2fsprogs]]に含まれる `filefrag` は、`FIEMAP` という `ioctl` でファイルのエクステントの一覧を取得し、ファイルがいくつのエクステントに分かれているかを報告する。`FIEMAP` は、論理オフセット、物理オフセット、長さと、未書き込みかどうかなどのフラグを返す。また、[[LVM]]の「物理エクステント」は、ボリュームを切り分ける固定長の単位であり、ファイルシステムのエクステントとは別の概念である。

## 関係
- 上位概念: [[Metadata]]
- 対比: [[LVM]]の物理エクステント（固定長の割り当て単位であり、可変長の範囲ではない）
- 使う / 使われる: [[ext4]], [[XFS]], [[e2fsprogs]]
- 関連: [[Inode]], [[B-Tree]], [[Block Storage]]

## 出典
- [The Contents of inode.i_block - The Linux Kernel documentation](https://docs.kernel.org/filesystems/ext4/ifork.html)
- [Fiemap Ioctl - The Linux Kernel documentation](https://docs.kernel.org/filesystems/fiemap.html)
- [filefrag(8) - Linux manual page](https://man7.org/linux/man-pages/man8/filefrag.8.html)
- [fallocate(2) - Linux manual page](https://man7.org/linux/man-pages/man2/fallocate.2.html)
- [XFS - Wikipedia](https://en.wikipedia.org/wiki/XFS)
