---
aliases: [struct address_space, address_space_operations, i_mapping]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# address_space

> Linuxカーネルにおいて、一つのファイルに属する[[Page Cache|ページキャッシュ]]上のページ群を管理するオブジェクトである。

## 概要
各[[Inode|inode]]は一つの `struct address_space` を持ち、ファイル内の位置（ページ単位のインデックス）から、その内容を保持するキャッシュ上のページを引けるようにする。[[read]]はまずここを検索し、ページがあればそれを返し、なければ記憶装置から読み込んで登録する。[[write]]はここにあるページを更新してダーティとし、後の書き戻しの対象とする。また、[[mmap]]でファイルがプロセスのアドレス空間に写像されたとき、どのプロセスのどの領域がこのファイルのページを参照しているかもここで追跡される。最近のカーネルでは、複数ページをまとめたfolioという単位で管理が進められている。

ページキャッシュと記憶装置の間の実際の転送は、ファイルシステムが実装する `address_space_operations` が担う。これには、ページへのデータの読み込み、ダーティページの書き戻し、書き込みの準備と完了などの操作が含まれる。[[VFS]]と汎用のページキャッシュ層が共通の処理を行い、ファイルシステムは自らのデータ配置に応じた転送のみを実装する。

## どこで出てくるか
`address_space` は、ファイルシステムのI/O経路を読む際の起点となる。ページキャッシュのヒット率、書き戻しの粒度、[[fsync]]の挙動は、いずれもこの構造と `address_space_operations` の実装に依存する。名前は「アドレス空間」であるが、プロセスの仮想アドレス空間ではなく、ファイルのバイト位置の空間を指す点に注意を要する。

## 関係
- 上位概念: [[Page Cache]], [[VFS]]
- 前提: [[Inode]]
- 使う / 使われる: [[read]], [[write]], [[mmap]], [[fsync]]

## 出典
- [Overview of the Linux Virtual File System - The Linux Kernel documentation](https://docs.kernel.org/filesystems/vfs.html)
- [Page Cache - The Linux Kernel documentation](https://docs.kernel.org/mm/page_cache.html)
