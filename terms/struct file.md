---
aliases: [File Object, ファイルオブジェクト, file構造体, struct file]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# struct file

> [[VFS]]において、プロセスがオープンしたファイルを表すオブジェクトであり、[[POSIX]]のオープンファイル記述（open file description）のカーネル内での実装である。

## 概要
[[open]]が成功すると、VFSは `struct file` を割り当て、対象の[[Dentry|dentry]]への参照、[[Inode|inode]]から取得した `file_operations`、ファイルオフセット（`f_pos`）、アクセスモードと `O_APPEND` などのフラグを設定する。そのうえで、プロセスのファイルディスクリプタ表の空き番号にこのオブジェクトへのポインタを登録し、その番号を[[File Descriptor|ファイルディスクリプタ]]として返す。すなわち、ファイルディスクリプタはプロセスごとの表の添字であり、その先にある `struct file` がオフセットとフラグの実体を持つ。

`struct file` は参照カウントを持つ。`dup()` による複製や `fork()` による継承では、新しいディスクリプタが同じ `struct file` を指すため、オフセットが共有される。同じファイルを再び `open()` すると別の `struct file` が作られ、オフセットは独立する。すべての参照が[[close]]されると `struct file` は解放される。[[read]]・[[write]]は、ディスクリプタから `struct file` を引き、その `file_operations` を経由してファイルシステムの実装を呼び出す。

## どこで出てくるか
ファイルディスクリプタの共有とオフセットの関係は、ディスクリプタ、`struct file`、inodeの三段構造を理解すると整理できる。ディスクリプタはプロセスごと、`struct file` はオープンごと、inodeはファイルごとに一つ存在する。`/proc/<pid>/fd/` や `/proc/<pid>/fdinfo/` を見ると、プロセスが保持するディスクリプタと、それぞれのオフセットやフラグを確認できる。

## 関係
- 上位概念: [[VFS]]
- 前提: [[File Descriptor]]
- 使う / 使われる: [[Dentry]], [[Inode]]
- 関連: [[open]], [[close]], [[read]], [[write]], [[lseek]]

## 出典
- [Overview of the Linux Virtual File System - The Linux Kernel documentation](https://docs.kernel.org/filesystems/vfs.html)
- [3. Definitions - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html)
