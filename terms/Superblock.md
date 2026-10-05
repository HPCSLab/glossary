---
aliases: [スーパーブロック, super_block, struct super_block]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# Superblock（スーパーブロック）

> ファイルシステム全体に関する情報を保持するデータ構造であり、[[VFS]]においてはマウントされたファイルシステム1個を表すオブジェクトである。

## 概要
この語は二つの層で用いられる。ディスク上のスーパーブロックは、[[ext4]]などのブロックデバイス上のファイルシステムが所定の位置に記録する管理情報である。ブロックサイズ、総ブロック数と空きブロック数、[[Inode|inode]]の総数と空き数、各種の機能フラグなど、ファイルシステムを解釈するために最初に読む情報を含む。破損するとファイルシステム全体が読めなくなるため、通常は複数の位置に複製が置かれる。

カーネル内の `struct super_block` は、マウントされたファイルシステムのインスタンスを表すVFSのオブジェクトである。マウント時に、ファイルシステムの実装がディスク上のスーパーブロックを読み込むなどしてこれを構築する。`struct super_block` は、ファイルシステムの種類、ルートディレクトリの[[Dentry|dentry]]、所属するinodeの一覧、`super_operations` への参照を保持する。`super_operations` は、inodeの割り当てと解放、inodeの書き戻し、`statfs`（`df` が用いる容量情報の取得）、同期などを担う。ディスクを持たない擬似ファイルシステム（`proc` や `tmpfs` など）も、マウントされればこのオブジェクトを持つ。

## どこで出てくるか
`df` が表示する容量や `df -i` が表示するinodeの使用状況は、スーパーブロックが管理する情報に由来する。ファイルシステムの作成（`mkfs`）時のパラメータはスーパーブロックに記録され、後から変更できないものも多い。

## 関係
- 上位概念: [[VFS]]
- 使う / 使われる: [[Inode]], [[Dentry]]（ルートディレクトリ）
- 関連: [[File System]]

## 出典
- [Overview of the Linux Virtual File System - The Linux Kernel documentation](https://docs.kernel.org/filesystems/vfs.html)
