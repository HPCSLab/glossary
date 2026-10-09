---
aliases: [buffer_head, struct buffer_head, バッファヘッド, buffer head, Buffer Heads, bh, get_block, iomap]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# Buffer Head（バッファヘッド）

> Linuxカーネルで、ページ（folio）の中の一つのディスクブロックについて、その位置と状態を記録する構造体 `struct buffer_head` であり、最初のLinuxから続く古い仕組みである。

## 概要
[[Block Storage|ブロックデバイス]]のブロックの大きさ（例えば1KB）は、メモリのページの大きさ（例えば4KB）より小さいことがある。その場合、[[Page Cache|ページキャッシュ]]の一つのページに複数のブロックが入る。バッファヘッドは、そのうちの一つのブロックを表し、そのブロックがディスク上のどこにあるか（ブロックデバイスと番号）、ページの中のどこにあるか、内容が有効か（uptodate）、変更済みか（dirty）、ロック中か、ディスク上の位置が割り当て済みか、などの状態を保持する。同じページのバッファヘッドは、互いに環状のリストでつながっている。

かつては、バッファヘッドは、ページの中のブロックを対応付けるとともに、ファイルシステムとブロック層の間の入出力の単位であった。現在では、入出力の単位は `bio` に移っている。バッファヘッドは、ファイルシステムの `get_block` の呼び出しによるブロックの対応付けの取得、folioの中のブロックごとの状態の管理、および互換性のための入出力の発行に用いられている。

## どこで出てくるか
[[ext4]]や[[JBD2]]は、[[Metadata|メタデータ]]の入出力にバッファヘッドを用いている。カーネルのファイルシステムのコードを読むと、`sb_bread()`（ext4では `ext4_sb_bread()`）でスーパーブロックなどのブロックを読み込み、得られたバッファヘッドの `b_data` を通じて内容を参照する箇所が多くある。

一方、バッファヘッドには、ブロックごとに構造体を持つためのメモリの負担がある。例えば、4KBのブロックからなる2MBのfolioでは、バッファヘッドに約50KBを要する。また、コードが多くの機能を内部に抱え、ファイルシステムごとに異なる部分を用いているため、複雑である。このため、ファイルシステムの範囲（[[Extent|エクステント]]）の対応付けを必要に応じて問い合わせるiomapへの移行が進められている。iomapは、新しいファイルシステムが用いるべきインタフェースとされ、ページより大きなブロックの対応にも必要である。[[XFS]]はすでにバッファヘッドを用いない。

## 関係
- 上位概念: [[Page Cache]]
- 使う / 使われる: [[ext4]], [[JBD2]], [[Folio]], [[Slab Allocator]]
- 対比: [[XFS]]（バッファヘッドを用いない）
- 関連: [[blk-mq]], [[address_space]], [[Superblock]]

## 出典
- [include/linux/buffer_head.h - Linux source (torvalds/linux)](https://github.com/torvalds/linux/blob/master/include/linux/buffer_head.h)
- [Sunsetting buffer heads - LWN.net](https://lwn.net/Articles/931809/)
- [Converting filesystems to iomap - LWN.net](https://lwn.net/Articles/935934/)
- [stop using buffer heads in xfs v6 - LWN.net](https://lwn.net/Articles/758213/)
- [fs/ext4/super.c - Linux source (torvalds/linux)](https://github.com/torvalds/linux/blob/master/fs/ext4/super.c)
