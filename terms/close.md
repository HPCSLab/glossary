---
aliases: [close(), close(2)]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# close

> [[File Descriptor|ファイルディスクリプタ]]を解放し、以後の[[open]]などで再利用可能にする[[POSIX]]の関数である。

## 概要
`close()` はディスクリプタを解放する。そのディスクリプタが指していたオープンファイル記述は、それを指すすべてのディスクリプタ（`dup()` による複製や `fork()` で継承されたものを含む）が閉じられた時点で解放される。また、[[unlink]]済みのファイルは、最後の参照が閉じられた時点で領域が解放される。

`close()` はデータの永続化を保証しない。POSIXは、未完了のI/Oの処理を `close()` に委ねるのではなく、閉じる前に[[fsync]]を呼ぶことを推奨している。一方で、遅延された書き込みのエラーが `close()` の戻り値として報告される実装もあり、その場合でもディスクリプタ自体は解放される。

## どこで出てくるか
`close()` の戻り値を検査しないコードでは、ネットワーク越しのファイルシステムなどで書き込みエラーを見落とすおそれがある。また、ディスクリプタを閉じ忘れると、プロセスが同時に開けるディスクリプタ数の上限に達し、「Too many open files」エラーとなる。

## 関係
- 上位概念: [[POSIX]]
- 対比: [[open]]
- 関連: [[File Descriptor]], [[fsync]], [[unlink]]

## 出典
- [close - The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/functions/close.html)
