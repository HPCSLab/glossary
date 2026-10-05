---
aliases: [unlink(), unlink(2), unlinkat]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# unlink

> ディレクトリエントリ（ファイルの名前）を削除し、ファイルのリンク数を1減らす[[POSIX]]の関数である。

## 概要
`unlink()` が削除するのはファイルの名前であり、実体ではない。実体（[[Inode|inode]]）の領域が解放されるのは、リンク数が0になり、かつどのプロセスも[[File Descriptor|ファイルディスクリプタ]]やメモリマッピングで参照していないときである。最後の名前を削除した時点でまだ参照が残っている場合、名前は `unlink()` が戻る前に削除されるが、内容の解放は参照がすべて[[close]]されるまで延期される。`rm` コマンドはこの関数を呼び出しており、「ファイルを削除する」という操作の実態は「名前を外す」ことである。

## どこで出てくるか
この延期の仕組みを利用して、ファイルを[[open]]した直後に `unlink()` すれば、他のプロセスから名前で見えず、プロセス終了時に自動的に消える一時ファイルが作れる。逆に、実行中のプロセスが開いているログファイルを `rm` で削除しても、プロセスが閉じるまで容量は解放されないため、ディスク使用量が減らない原因となる。

## 関係
- 上位概念: [[POSIX]]
- 前提: [[Inode]]
- 対比: [[link]]
- 関連: [[close]], [[rename]]

## 出典
- [unlink, unlinkat - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/functions/unlink.html)
