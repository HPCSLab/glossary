---
aliases: [lseek(), lseek(2), seek]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# lseek

> [[File Descriptor|ファイルディスクリプタ]]のファイルオフセットを変更する[[POSIX]]の関数である。

## 概要
`lseek()` は、第3引数 `whence` に応じて新しいオフセットを計算する。`SEEK_SET` は指定値そのもの、`SEEK_CUR` は現在位置に指定値を加えた位置、`SEEK_END` はファイルサイズに指定値を加えた位置をオフセットとする。戻り値は新しいオフセットであるため、`lseek(fd, 0, SEEK_CUR)` で現在位置を、`lseek(fd, 0, SEEK_END)` でファイルサイズを得る用法が一般的である。`lseek()` 自体はI/Oを行わず、オフセットを変更するだけである。

オフセットはファイル末尾より先に設定できる。その位置に[[write]]すると、間の未書き込み領域はホール（hole）となり、[[read]]では値0として読まれる。ホールに記憶領域を割り当てない実装では、見かけのサイズより実際の使用量が小さいスパースファイルとなる。POSIX.1-2024では、ホールでないデータ領域とホールの位置を探す `SEEK_DATA`・`SEEK_HOLE` も規定されている。

## どこで出てくるか
`lseek()` と[[read]]・[[write]]の組み合わせは位置の変更とI/Oが別の呼び出しになるため、ディスクリプタを共有する複数スレッドの間で競合する。並列I/Oではこれを避けるために `pread()`・`pwrite()` を用いる。また、`ls -l` が示すサイズと `du` が示す使用量が大きく異なる場合、スパースファイルであることが多い。

## 関係
- 上位概念: [[POSIX]]
- 前提: [[File Descriptor]]
- 関連: [[read]], [[write]], [[truncate]]

## 出典
- [lseek - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/functions/lseek.html)
