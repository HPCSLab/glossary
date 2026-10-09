---
aliases: [fsync(), fsync(2), fdatasync, fdatasync()]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# fsync

> [[File Descriptor|ファイルディスクリプタ]]が指すファイルの未反映のデータを記憶装置へ書き出し、完了するまで待つ[[POSIX]]の関数である。

## 概要
[[write]]が成功しても、データは[[Page Cache|ページキャッシュ]]などのメモリ上に留まっていることがあり、電源断やOSのクラッシュで失われうる。`fsync()` は、そのファイルのデータを記憶装置へ転送するよう要求し、転送が完了するかエラーが検出されるまで戻らない。これが、アプリケーションが永続化を確認するための基本的な手段である。

`fdatasync()` は、データと、そのデータを後で正しく読み出すために必要な[[Metadata|メタデータ]]（ファイルサイズなど）のみを書き出し、更新時刻のような不要なメタデータの書き出しを省く。そのため、`fsync()` より軽量である。また、Linuxでは、ファイルに対する `fsync()` は、そのファイルを含むディレクトリのエントリまで永続化することを保証しない。新規作成や[[rename]]した名前を確実に残すには、ディレクトリ自体をオープンして `fsync()` する必要がある。

## どこで出てくるか
`fsync()` は記憶装置への書き出しを待つため、頻繁に呼ぶとI/O性能が大きく低下する。データベースやチェックポイントの実装では、永続性と性能の兼ね合いから、`fsync()` を呼ぶ時機と回数が設計上の要点となる。I/Oベンチマークの結果を読む際には、`fsync()` を含む計測か否かによって数値の意味が大きく異なることに注意を要する。

## 関係
- 上位概念: [[POSIX]]
- 前提: [[write]], [[Page Cache]]
- 関連: [[rename]], [[close]], [[open]]（`O_SYNC`・`O_DSYNC`）

## 出典
- [fsync - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/functions/fsync.html)
- [fdatasync - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/functions/fdatasync.html)
- [fsync(2) - Linux manual page](https://man7.org/linux/man-pages/man2/fsync.2.html)
