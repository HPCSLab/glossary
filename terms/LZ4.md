---
aliases: [lz4, LZ4 HC, LZ4_HC, LZ4_RAW, liblz4]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# LZ4

> 圧縮率を抑える代わりに、圧縮と伸長（展開）を非常に速く行うことを目的とした、可逆圧縮のアルゴリズムとそのライブラリである。

## 概要
LZ4はYann Colletが2011年に公開した。LZ77系の圧縮であり、すでに現れたバイト列と一致する部分を「どこから何バイトを写すか」という参照に置き換える。DEFLATE（gzipやzlibが用いる方式）は、この後にハフマン符号化などのエントロピー符号化を重ねて圧縮率を上げるが、LZ4はこの段を持たない。そのため圧縮率はDEFLATEより低いが、圧縮も伸長も数倍から十倍以上速い。

公式のベンチマーク（Silesiaコーパス、1スレッド）では、既定の設定で圧縮率は約2.1、圧縮は約780 MB/s、伸長は約5 GB/sである。同じ表では[[Zstandard]]の最も速い設定が圧縮率約2.9、伸長約1.4 GB/sであり、LZ4は圧縮率で劣る代わりに速度で勝る。圧縮に時間をかけて圧縮率を上げる LZ4 HC という変種もあり、こちらも伸長の速さは変わらない。

この性質から、LZ4は「圧縮しても記憶装置やネットワークより遅くならない」ことが重要な場面で選ばれる。読み書きのたびに圧縮と伸長を行う透過的な圧縮では、圧縮が遅いとI/Oの[[Bandwidth|帯域]]を削ってしまうためである。

## どこで出てくるか
[[ZFS]]では、圧縮を `compression=on` にしたときの既定の方式が（`lz4_compress` の機能が有効なプールでは）LZ4である。[[Linux Kernel|Linuxカーネル]]は3.11からLZ4の実装を持ち、SquashFSなどで用いられる。データの形式では、[[Parquet]]が列のページの圧縮方式の一つとしてLZ4（`LZ4_RAW`）に対応しており、旧来の `LZ4` の指定は独自の枠組みを持つため非推奨とされている。

## 関係
- 対比: [[Zstandard]]（エントロピー符号化を持ち圧縮率が高いが、伸長はLZ4より遅い）
- 使う / 使われる: [[ZFS]], [[Parquet]]

## 出典
- [lz4/lz4 - GitHub](https://github.com/lz4/lz4)
- [LZ4 (compression algorithm) - Wikipedia](https://en.wikipedia.org/wiki/LZ4_(compression_algorithm))
- [zfsprops.7 - OpenZFS documentation](https://openzfs.github.io/openzfs-docs/man/master/7/zfsprops.7.html)
- [Compression - Apache Parquet](https://parquet.apache.org/docs/file-format/data-pages/compression/)
