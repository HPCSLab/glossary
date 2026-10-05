---
aliases: [stat(), stat(2), fstat, lstat, fstatat, struct stat]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# stat

> ファイルの[[Metadata|メタデータ]]を取得する[[POSIX]]の関数群であり、結果を `struct stat` 構造体に格納する。

## 概要
`stat()` はパス名で、`fstat()` は[[File Descriptor|ファイルディスクリプタ]]で対象を指定する。`lstat()` はシンボリックリンク自体の情報を返し、リンク先をたどらない。得られる主な情報は、ファイルの種類と権限（`st_mode`）、所有者（`st_uid`・`st_gid`）、サイズ（`st_size`）、ハードリンク数（`st_nlink`）、実際に割り当てられたブロック数（`st_blocks`）、3種類のタイムスタンプである。タイムスタンプは、最終アクセス時刻（atime）、最終データ更新時刻（mtime）、最終状態変更時刻（ctime）からなる。ctimeは作成時刻ではなく、権限変更や[[link]]などのメタデータ変更時刻である点に注意を要する。ファイルの同一性は、デバイス番号（`st_dev`）と[[Inode|inode]]番号（`st_ino`）の組で識別される。

## どこで出てくるか
`ls -l`、`find`、`du` などのコマンドは、ファイルごとに `stat()` を発行する。[[Parallel File System|並列ファイルシステム]]上の大量のファイルに対してこれらを実行すると、メタデータサーバへの問い合わせが集中し、システム全体の応答を悪化させることがある。また、`st_size` が見かけのサイズであるのに対し、`st_blocks` は実際の使用量であり、両者の差からスパースファイルを判別できる。

## 関係
- 上位概念: [[POSIX]]
- 前提: [[Inode]], [[Metadata]]
- 関連: [[link]], [[truncate]]

## 出典
- [fstatat, lstat, stat - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/functions/stat.html)
- [sys/stat.h - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/sys_stat.h.html)
