---
aliases: [truncate(), truncate(2), ftruncate, ftruncate()]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# truncate

> ファイルのサイズを指定した長さに変更する[[POSIX]]の関数であり、`truncate()` はパス名で、`ftruncate()` は[[File Descriptor|ファイルディスクリプタ]]でファイルを指定する。

## 概要
指定した長さが現在のサイズより小さい場合、それを超える部分のデータは読めなくなる。大きい場合はファイルが拡張され、拡張部分は値0で埋められたものとして読まれる。この拡張部分は、[[lseek]]で末尾より先に書き込んだ場合と同様にホールとして扱われ、記憶領域が割り当てられないことが多い。`ftruncate()` は書き込み可能でオープンしたディスクリプタを要求し、ファイルオフセットは変更しない。成功すると、データ更新時刻（mtime）と状態変更時刻（ctime）が更新される。

[[open]]の `O_TRUNC` フラグは、オープン時に長さを0にする操作であり、既存ファイルを上書き保存する際によく用いられる。

## どこで出てくるか
`ftruncate()` は、書き込みに先立ってファイルの最終サイズを確定させる用途や、共有メモリ領域の大きさを設定する用途で用いられる。サイズ変更はファイル全体に影響する[[Metadata|メタデータ操作]]であるため、[[Parallel File System|並列ファイルシステム]]上の[[Access Pattern|共有ファイル]]に対して多数のプロセスが同時に発行すると、高コストとなる。

## 関係
- 上位概念: [[POSIX]]
- 関連: [[open]], [[lseek]], [[write]], [[Metadata]]

## 出典
- [ftruncate - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/functions/ftruncate.html)
- [truncate - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/functions/truncate.html)
