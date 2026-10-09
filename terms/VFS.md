---
aliases: [Virtual File System, Virtual Filesystem Switch, 仮想ファイルシステム]
tags: [term]
maps: ["[[Storage]]", "[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# VFS（仮想ファイルシステム）

> Linuxカーネル内で、ユーザ空間のプログラムにファイルシステムの共通インタフェースを提供し、その下で複数のファイルシステム実装を共存させる抽象化層である。

## 概要
アプリケーションが発行する[[open]]・[[read]]・[[write]]・[[stat]]などの[[System Call|システムコール]]は、まずVFSが受け取る。VFSは、どのファイルシステムにも共通する処理（パス名の解決、権限検査、[[File Descriptor|ファイルディスクリプタ]]の管理、[[Page Cache|ページキャッシュ]]の操作など）を自ら行い、ファイルシステムごとに異なる処理だけを個々の実装（[[ext4]]、[[XFS]]、[[NFS]]、[[Lustre]]のクライアントなど）に委ねる。これにより、アプリケーションは背後の実装を意識せずに同じ[[POSIX]]インタフェースでファイルを扱え、ファイルシステムの開発者は共通部分を再実装せずに済む。

VFSは、ファイルシステムを次の4種類のオブジェクトで表現する。マウントされたファイルシステム全体を表す[[Superblock|スーパーブロック]]、個々のファイルやディレクトリの実体を表す[[Inode|inode]]、パス名の各要素とinodeとの対応を表す[[Dentry|dentry]]、プロセスがオープンしたファイルを表す[[struct file]]である。加えて、ファイルの内容をページキャッシュ上で管理する[[address_space]]がinodeに付随する。

各オブジェクトは、操作を実装する関数ポインタの表を持つ。`super_operations` はスーパーブロックとinodeの生成・破棄を、`inode_operations` はファイルの作成・探索・[[link]]などの名前空間操作を、`file_operations` はオープンしたファイルに対する読み書きや[[mmap]]を、`dentry_operations` はdentryの検証や名前の比較を、`address_space_operations` はページキャッシュと記憶装置の間の読み書きを担う。各ファイルシステムはこれらの表に自らの関数を登録し、VFSは表を介して呼び出す。これはC言語でオブジェクト指向の多態性を実現する典型的な手法である。ファイルシステムは `register_filesystem()` でカーネルに登録され、マウント時にVFSから呼び出されてスーパーブロックを構築する。

[[open]]を例に取ると、VFSはまずパス名をdentryのキャッシュ（dcache）で要素ごとに解決し、キャッシュにない要素はファイルシステムの `lookup` を呼んでdentryとinodeを作る。次に `struct file` を割り当て、dentryへの参照と、inodeから取得した `file_operations` を設定し、プロセスのファイルディスクリプタ表に登録して、その番号を返す。以後の `read()` は、この `struct file` の `file_operations` を経て、ファイルシステムの実装に到達する。

## どこで出てくるか
ファイルシステムの研究や開発では、VFSのどのオブジェクトと操作を実装・変更するかという形で設計を説明することが多い。[[FUSE]]は、VFSからの要求をユーザ空間のプロセスに転送する仕組みであり、カーネルを改変せずに独自のファイルシステムを実装する手段として、研究用の試作によく用いられる。また、[[Metadata|メタデータ]]性能の議論では、dcacheやinodeキャッシュによって記憶装置やサーバへの問い合わせがどれだけ省かれるかが論点となる。

## 関係
- 上位概念: [[File System]]
- 前提: [[System Call]]
- 使う / 使われる: [[POSIX]]（VFSが提供するインタフェース）, [[Superblock]], [[Inode]], [[Dentry]], [[struct file]], [[address_space]]
- 関連: [[Page Cache]], [[FUSE]]

## 出典
- [Overview of the Linux Virtual File System - The Linux Kernel documentation](https://docs.kernel.org/filesystems/vfs.html)
- [Pathname lookup - The Linux Kernel documentation](https://docs.kernel.org/filesystems/path-lookup.html)
