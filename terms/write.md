---
aliases: [write(), write(2), pwrite, pwrite()]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# write

> バッファのデータを[[File Descriptor|ファイルディスクリプタ]]が指すファイルへ書き込む[[POSIX]]の関数であり、`pwrite()` は位置を指定して書き込む変種である。

## 概要
`write()` は、ディスクリプタのファイルオフセットの位置からデータを書き込み、成功して戻る前に、実際に書き込んだバイト数だけオフセットを進める。戻り値は要求したバイト数より小さいことがあり（short write）、例えば記憶領域が不足した場合がこれに当たる。`O_APPEND` 付きで[[open]]した場合は、各書き込みの直前にオフセットがファイル末尾へ移される。ファイル末尾より先の位置に書き込むとファイルが拡張され、間の未書き込み領域は[[read]]で値0として読まれる。

`pwrite()` は、引数で与えた位置に書き込み、ディスクリプタのオフセットを変更しない。POSIXは `O_APPEND` の有無にかかわらずこの動作を求めているが、Linuxでは `O_APPEND` 付きでオープンしたファイルに対する `pwrite()` が指定位置を無視して末尾に追記するという、規格からの逸脱がある。

`write()` の成功は、データが記憶装置に到達したことを意味しない。Linuxを含む多くの実装では、書き込まれたデータはまず[[Page Cache|ページキャッシュ]]に置かれ、後で非同期に書き出される。永続化を保証するには[[fsync]]を呼ぶ必要がある。一方で、`write()` が戻った後の[[read]]は、他のスレッドからであっても書き込んだ内容を返さなければならない。この一貫性の要求については[[POSIX]]を参照。

## どこで出てくるか
[[Access Pattern|共有ファイル]]への並列書き込みでは、各プロセスが `pwrite()` で担当領域に直接書き込むのが基本形である。チェックポイントの書き出しでは、`write()` の完了時点ではデータが失われうることを前提に、[[fsync]]と[[rename]]を組み合わせて整合性を確保する。I/Oベンチマークでは、ページキャッシュに書き込んだ時点の性能と、記憶装置への書き出しを含めた性能とを区別して評価する必要がある。

## 関係
- 上位概念: [[POSIX]]
- 対比: [[read]]
- 前提: [[File Descriptor]], [[open]]
- 関連: [[lseek]], [[fsync]], [[Page Cache]]

## 出典
- [write, pwrite - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/functions/write.html)
- [write(2) - Linux manual page](https://man7.org/linux/man-pages/man2/write.2.html)
- [pwrite(2) - Linux manual page](https://man7.org/linux/man-pages/man2/pwrite.2.html)
