---
aliases: [IME, Infinite Memory Engine, DDN Infinite Memory Engine, IME14K, IME240]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# DDN IME（Infinite Memory Engine）

> [[Compute Node|計算ノード]]と[[Parallel File System|並列ファイルシステム]]の間に[[SSD]]を束ねた層を置き、書き込みを受け止めて整列してから下位のファイルシステムへ書き戻す、[[EXAScaler|DDN]]の[[Ad Hoc File System|バーストバッファ]]製品である。

## 概要
HPCのアプリケーションのI/Oには、チェックポイントのように短時間に集中する書き込みや、多数の[[Process|プロセス]]による一つの共有ファイルへの小さく整列していない書き込みが多い。[[Lustre]]や[[IBM Storage Scale|GPFS]]のような並列ファイルシステムは、このような[[Access Pattern|アクセスパターン]]では、[[Distributed Lock Manager|ロック]]の競合などによって性能が大きく下がる。IMEは、このI/Oを並列ファイルシステムに直接届けず、SSDを搭載した専用のIMEサーバの層で受け止める。

DDNの資料によると、計算ノードのIMEクライアントは、データを断片に分けてパリティを計算し（クライアント側の[[RAID|イレージャコーディング]]）、ハッシュでIMEサーバに分散して送る。IMEサーバは受け取った断片をログ構造の形式で書き込む（[[Log-Structured File System|ログ構造ファイルシステム]]を参照）。下位のファイルシステムへ書き戻す前に、同じストライプに属する断片をまとめ、整列した順次の書き込みとして送る。ファイルの[[open]]、[[close]]、[[stat]]などの[[Metadata|メタデータ]]の操作は、IMEを経由せず下位のファイルシステムに渡される。アプリケーションは、[[POSIX]]または[[MPI-IO]]のインタフェースでI/Oを発行する。

日本では、東京大学と筑波大学が共同で運用した[[Oakforest-PACS]]が、IME14Kを用いた容量940TB（イレージャコーディングのパリティを含む）のバーストバッファを、Lustreの前段のファイルキャッシュとして備えていた。

## どこで出てくるか
IMEは、バーストバッファの研究や、並列ファイルシステムの前段にSSDの層を置く構成の論文で、商用の代表例として参照される。IMEが対象とするのは共有ファイルへの整列しない書き込みのようなデータのI/Oであり、メタデータの操作は下位のファイルシステムに渡されるため、メタデータの性能を高める仕組みではない。この区別は、[[IOR]]と[[mdtest]]で性能を評価する際にも現れる。

## 関係
- 上位概念: [[Ad Hoc File System]]（バーストバッファ）
- 前提: [[Parallel File System]], [[SSD]]
- 対比: [[Lustre PCC]]（クライアントのローカルな記憶装置をキャッシュとし、専用のサーバを持たない）
- 使う / 使われる: [[Lustre]], [[IBM Storage Scale]], [[MPI-IO]]
- 関連: [[EXAScaler]], [[Log-Structured File System]], [[Oakforest-PACS]]

## 出典
- [Infinite Memory Engine: Freedom from Filesystem Foibles (James Coomer, DDN, 2017)](https://hps.vi4io.org/_media/events/2017/eiug17-coomer.pdf)
- [Basic Specification of Oakforest-PACS - JCAHPC](https://www.jcahpc.jp/files/OFP-basic.pdf)
- [Early Evaluation of the "Infinite Memory Engine" Burst Buffer Solution (Schenck et al., ISC High Performance 2016 Workshops, LNCS)](https://doi.org/10.1007/978-3-319-46079-6_41)
