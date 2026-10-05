---
aliases: [ファイルシステム, Filesystem, FS]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# File System（ファイルシステム）

> 記憶装置上のデータを、名前を持つファイルとディレクトリの階層として管理し、アプリケーションに読み書きの手段を提供するソフトウェアの仕組みである。

## 概要
記憶装置そのものは、番号で指定する固定長ブロックの列を読み書きする機能しか持たない。これが[[Block Storage|ブロックストレージ]]である。ファイルシステムはその上に、ファイル名、ディレクトリによる階層構造、サイズ・所有者・権限・タイムスタンプといった[[Metadata|メタデータ]]を構築し、「どのブロックがどのファイルのどの部分か」を管理する。Unix系のファイルシステムでは、ファイルごとのメタデータを[[Inode|inode]]と呼ばれる構造に保持する。

アプリケーションは `open`・`read`・`write`・`close` などのシステムコールを通じてファイルを操作する。オープンしたファイルは整数の[[File Descriptor|ファイルディスクリプタ]]で識別され、読み書きの位置はそれに対応するファイルオフセットとして管理される。これらの関数とその意味論（書き込みの可視性、ファイルの属性、ディレクトリ操作の挙動など）は[[POSIX]]で標準化されており、Linuxではカーネル内の[[VFS]]がこの共通インタフェースを提供し、その下で[[ext4]]や[[XFS]]などの個々の実装が動作する。このためアプリケーションは、背後の実装を意識せずに同じコードでファイルを扱える。

ファイルシステムは、単一ノードのディスクを管理するローカルファイルシステムに限られない。ネットワーク越しにファイルを共有する[[Distributed File System|分散ファイルシステム]]（例：[[NFS]]）や、多数のストレージサーバにデータを分散配置して並列に読み書きする[[Parallel File System|並列ファイルシステム]]（例：[[Lustre]]）も、利用者からは同じくファイルとディレクトリの階層として見える。一方、[[Object Storage|オブジェクトストレージ]]は階層的な名前空間とPOSIXの意味論を持たず、キーで識別されるオブジェクトを丸ごと格納・取得するモデルを採る。

## どこで出てくるか
HPCでは、計算ノード群が共有する並列ファイルシステムに入力データやチェックポイントを置くのが一般的であり、I/O性能がアプリケーション全体の性能を左右する。特に大量の小さなファイルの作成やディレクトリ走査ではメタデータ処理が律速となりやすく、POSIXの厳密な一貫性保証を多数のクライアント間で維持するコストも性能上の論点となる。ストレージ系の論文では、ファイルシステムのインタフェースを維持するか、POSIXの意味論を緩和するか、オブジェクトストレージなど別のモデルに移行するかが、設計上の主要な分岐として議論される。

## 関係
- 前提: [[Block Storage]]
- 対比: [[Object Storage]]（階層とPOSIX意味論を持たず、オブジェクト単位で読み書きする）
- 使う / 使われる: [[POSIX]]（インタフェースの標準）, [[VFS]], [[File Descriptor]]
- 関連: [[Distributed File System]], [[Parallel File System]], [[Metadata]]

## 出典
- [File system - Wikipedia](https://en.wikipedia.org/wiki/File_system)
- [Overview of the Linux Virtual File System - The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/filesystems/vfs.html)
- [The Open Group Base Specifications Issue 8 (POSIX.1-2024)](https://pubs.opengroup.org/onlinepubs/9799919799/)
