---
aliases: [inode, アイノード, i-node, index node, struct inode]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# Inode（inode）

> Unix系のファイルシステムで、個々のファイルやディレクトリの実体を表し、その[[Metadata|メタデータ]]とデータの所在を保持するデータ構造である。

## 概要
inodeは、ファイルの種類と権限、所有者、サイズ、タイムスタンプ、ハードリンク数、そしてデータが記憶装置上のどのブロックにあるかを保持する。ファイル名は保持しない。名前はディレクトリの側に「名前からinode番号への対応」として記録され、一つのinodeを複数の名前が指すことができる（[[link]]）。inode番号はファイルシステム内で一意であり、[[stat]]の `st_ino` として得られる。名前を持たないことから、[[unlink]]で名前がすべて消えても、オープン中であれば実体は存続する。

[[VFS]]における `struct inode` は、この実体をカーネルのメモリ上で表すオブジェクトである。ブロックデバイス上のファイルシステムでは、ディスク上のinodeが必要に応じてメモリに読み込まれ、変更は後でディスクに書き戻される。ディスクを持たない擬似ファイルシステムでは、メモリ上にのみ存在する。`struct inode` は、名前空間の操作を担う `inode_operations` と、オープン時に[[struct file]]へ引き渡される `file_operations` への参照を持ち、ファイルの内容をキャッシュする[[address_space]]を内包する。読み込まれたinodeはinodeキャッシュに保持され、繰り返しのアクセスでディスクを読まずに済むようにしている。

## どこで出てくるか
`ls -i` でinode番号を、`df -i` でinodeの使用状況を確認できる。[[ext4]]などではinodeの総数がファイルシステム作成時に決まるため、小さなファイルを大量に作るとディスク容量に余裕があってもinodeが枯渇し、ファイルを作成できなくなる。[[Parallel File System|並列ファイルシステム]]では、inodeに相当するメタデータを専用のメタデータサーバが管理する設計が多く、その処理能力がファイル作成や `stat` の性能を決める。

## 関係
- 上位概念: [[VFS]], [[File System]]
- 対比: [[Dentry]]（名前とinodeの対応）
- 使う / 使われる: [[address_space]], [[struct file]], [[Superblock]]
- 関連: [[link]], [[unlink]], [[stat]], [[Metadata]]

## 出典
- [Overview of the Linux Virtual File System - The Linux Kernel documentation](https://docs.kernel.org/filesystems/vfs.html)
- [sys/stat.h - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/sys_stat.h.html)
