---
aliases: [open(), open(2), openat, openat()]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# open

> パス名で指定したファイルをオープンし、それを指す[[File Descriptor|ファイルディスクリプタ]]を返す[[POSIX]]の関数である。

## 概要
`open()` は、パス名からファイルを探索し、アクセス権を検査したうえで、新たなオープンファイル記述（open file description）とそれを指すファイルディスクリプタを作成する。ファイルオフセットはファイルの先頭に設定される。以後のI/Oはすべてこのディスクリプタを介して行われ、使用後は[[close]]で解放する。`openat()` は、カレントディレクトリではなく、引数で与えたディレクトリのディスクリプタを基準にパス名を解決する変種である。

第2引数のフラグにより、オープン時の振る舞いと、以後のI/Oの意味論が決まる。アクセスモードは `O_RDONLY`・`O_WRONLY`・`O_RDWR` のいずれかである。`O_CREAT` はファイルが存在しなければ作成し、これに `O_EXCL` を併用すると、存在の確認と作成が他のスレッドの `open()` に対して不可分に行われ、既に存在する場合は失敗する。`O_TRUNC` は、書き込み可能でオープンした既存の通常ファイルの長さを0にする（[[truncate]]と同じ効果）。`O_APPEND` は各[[write]]の直前にオフセットをファイル末尾へ移す。`O_SYNC`・`O_DSYNC` は書き込みを同期I/Oとし、各書き込みの完了時点で[[fsync]]相当の永続化を求める。`O_CLOEXEC` は `exec` 時にディスクリプタを自動的に閉じる。なお、Linuxの `O_DIRECT`（[[Page Cache|ページキャッシュ]]を経由しないI/O）はPOSIXには含まれない独自拡張である。

## どこで出てくるか
`open()` は、パス名の探索、権限検査、ファイル作成を伴う[[Metadata|メタデータ]]操作である。[[Parallel File System|並列ファイルシステム]]ではメタデータが専用サーバで管理されることが多く、多数のプロセスが同時に `open()`・作成を行うとそのサーバに負荷が集中する。ファイル単位のロックファイルや一意な一時ファイルの作成には、`O_CREAT | O_EXCL` の不可分性が利用される。

## 関係
- 上位概念: [[POSIX]]
- 使う / 使われる: [[File Descriptor]]（`open()` が生成する）
- 関連: [[close]], [[read]], [[write]], [[truncate]]

## 出典
- [open - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/functions/open.html)
