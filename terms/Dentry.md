---
aliases: [dentry, Directory Entry, ディレクトリエントリ, dcache, Dentry Cache, struct dentry]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# Dentry（dentry）

> [[VFS]]において、パス名の一要素（ファイル名やディレクトリ名）と、それが指す[[Inode|inode]]との対応を表すオブジェクトである。

## 概要
パス名 `/home/user/data.txt` は、`/`、`home`、`user`、`data.txt` という要素に分解され、VFSは各要素に対応するdentryをたどってinodeに到達する。dentryは、要素の名前、親ディレクトリのdentry、対応するinodeへの参照を保持し、全体として木構造を形成する。dentryはパス名の解決を高速化するためにメモリ上にのみ存在し、ディスクには保存されない。ディスク上でディレクトリの中身として記録される「名前とinode番号の組」もディレクトリエントリと呼ばれるが、dentryはそれをカーネル内でキャッシュとして表現したものである。

dentryの集合はdentryキャッシュ（dcache）と呼ばれる。パス名の解決では、まずdcacheを検索し、見つからない要素についてのみファイルシステムの `lookup` 操作を呼んでdentryとinodeを作成する。存在しない名前に対しても、inodeへの参照が空の「ネガティブdentry」を作り、「この名前は存在しない」という結果をキャッシュする。パス名の解決には、ロックを取らずに高速に走査するRCU-walkと、参照カウントとロックを用いる確実なREF-walkの二つの方式があり、前者が失敗した場合に後者へ切り替える。

## どこで出てくるか
dcacheが有効に働く限り、繰り返しの[[open]]や[[stat]]はディスクやサーバに問い合わせずに完了する。ネットワーク越しのファイルシステムや[[Parallel File System|並列ファイルシステム]]では、他のノードによる変更を反映するためにキャッシュの有効性を検証する必要があり、この検証のコストと鮮度の兼ね合いが[[Metadata|メタデータ]]性能の論点となる。存在しないファイルを繰り返し探索するプログラム（ライブラリの探索パスの走査など）では、ネガティブdentryが性能に寄与する。

## 関係
- 上位概念: [[VFS]]
- 対比: [[Inode]]（名前を持たない実体）
- 使う / 使われる: [[struct file]]（オープン時にdentryを参照する）, [[Superblock]]（ルートのdentryを持つ）
- 関連: [[open]], [[stat]], [[link]], [[rename]]

## 出典
- [Overview of the Linux Virtual File System - The Linux Kernel documentation](https://docs.kernel.org/filesystems/vfs.html)
- [Pathname lookup - The Linux Kernel documentation](https://docs.kernel.org/filesystems/path-lookup.html)
