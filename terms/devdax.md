---
aliases: [Device DAX, device-dax, DAX, Direct Access, fsdax, Filesystem DAX, /dev/dax, ndctl, daxctl, namespace, MAP_SYNC]
tags: [term]
maps: ["[[Storage]]", "[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# devdax（Device DAX）

> Linuxにおいて、永続メモリなどのCPUから直接アクセスできる記憶領域を、ファイルシステムを介さずにキャラクタデバイス `/dev/daxX.Y` として提供し、[[mmap]]による直接の写像のみを許す利用形態である。

## 概要
DAX（Direct Access）は、[[Intel Optane Persistent Memory|永続メモリ]]のようにCPUがバイト単位で直接アクセスできる記憶装置に対して、[[Page Cache|ページキャッシュ]]を介さずに読み書きする仕組みである。通常のファイルI/Oでは、データは記憶装置とページキャッシュの間で複製されるが、DAXではその複製を省き、ファイルを写像した場合は記憶装置そのものがプロセスの[[Virtual Memory|仮想アドレス空間]]に直接対応付けられる。

Linuxでは、永続メモリの領域をnamespaceとして構成し、`ndctl` でその利用形態（モード）を選ぶ。主なモードは次のとおりである。

| モード | デバイス | 内容 |
|---|---|---|
| raw | `/dev/pmemN` | 単純なメモリディスクであり、DAXに対応しない |
| sector | `/dev/pmemNs` | セクタ単位の不可分な書き込みを保証するブロックデバイスであり、従来のファイルシステム向けである |
| fsdax | `/dev/pmemN` | DAXに対応したブロックデバイスであり、その上に[[ext4]]や[[XFS]]を作成し、DAXを有効にしてマウントする |
| devdax | `/dev/daxX.Y` | ファイルシステムを持たないキャラクタデバイスであり、mmapによる写像でのみ利用する |

devdaxでは、ファイルシステムが存在しないため、領域全体が一つの大きなメモリとして、アプリケーションの責任で管理される。ファイルシステムのメタデータの処理や、ページフォルト時のブロックの割り当てが介在しないため、写像したメモリへのアクセスが予測しやすい。また、2MiBや1GiBの大きなページ単位で写像する整列を指定でき、TLBの負担を減らせる。

## どこで出てくるか
devdaxは、仮想マシンに永続メモリを割り当てる場合、[[RDMA]]のメモリ登録の対象とする場合、データベースや独自のストレージエンジンが領域全体を自ら管理する場合など、ファイルシステムが不要で、大きく予測可能な写像が必要な用途に用いられる。永続メモリを用いた研究の実装では、ファイルシステムの影響を排除してデバイスの特性を直接評価するために、devdaxを用いることが多い。一方、ファイルとして名前を付けて管理したい場合は、fsdaxの上のファイルシステムを用いる。

devdaxの領域は、`daxctl` によって通常の主記憶（システムRAM）として再構成し、独立したNUMAノードとしてOSに追加することもできる。この仕組みは、永続メモリに限らず、CXLで接続したメモリなど、性質の異なるメモリを主記憶の一部として扱う場合にも用いられる。

## 関係
- 上位概念: [[Intel Optane Persistent Memory]]（主な対象となる記憶装置）
- 使う / 使われる: [[mmap]]（唯一のアクセス手段）
- 対比: fsdax（DAXに対応したファイルシステムを介する形態）, [[Page Cache]]（DAXが迂回する）
- 関連: [[Virtual Memory]], [[RDMA]], [[ext4]], [[Crash Consistency]]

## 出典
- [Direct Access for files - The Linux Kernel documentation](https://docs.kernel.org/filesystems/dax.html)
- [Managing Namespaces - NDCTL User Guide](https://docs.pmem.io/ndctl-user-guide/managing-namespaces)
