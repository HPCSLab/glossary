---
aliases: [O_DIRECT, Direct I/O, ダイレクトI/O, DIO, STATX_DIOALIGN, Buffered I/O, バッファードI/O]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# Direct I/O（O_DIRECT）

> [[Page Cache|ページキャッシュ]]を経由せず、利用者のバッファと記憶装置の間で直接データを転送するファイルI/Oであり、Linuxでは[[open]]に `O_DIRECT` を指定して用いる。

## 概要
通常のファイルI/O（バッファードI/O）では、[[read]]や[[write]]のデータはカーネルのページキャッシュを経由する。読み込みは一度読んだデータをキャッシュから返せ、書き込みはキャッシュに書いた時点で戻るため、多くのアプリケーションでは速い。一方、データベースのように自前でキャッシュを持つソフトウェアでは、同じデータがページキャッシュと自前のキャッシュに二重に置かれ、主記憶と複製の手間が無駄になる。Direct I/Oは、このキャッシュを避けて、利用者空間のバッファと記憶装置の間で直接転送する。

Direct I/Oには制約がある。バッファのアドレス、転送の長さ、ファイル内のオフセットを、ファイルシステムや装置が定める単位（多くは論理ブロックの大きさ）にそろえる必要があり、そろっていないと `EINVAL` で失敗するか、バッファードI/Oに切り替わる。Linux 6.1以降では、[[stat|statx]] の `STATX_DIOALIGN` でその単位を調べられる。また、`O_DIRECT` は転送をなるべく同期的に行うが、記憶装置への永続化は保証しないため、永続性が必要なら `O_SYNC` を併用するか[[fsync]]を呼ぶ。同じファイルに対してDirect I/Oと通常のI/Oや[[mmap]]を混ぜて用いることは避けるべきとされている。[[POSIX]]には含まれない拡張である。

## どこで出てくるか
[[InnoDB]]は、Linuxでは既定でデータファイルを `O_DIRECT` で開き、自前のバッファプールでキャッシュを管理する。[[GPUDirect Storage]]は、記憶装置と[[GPU]]のメモリの間で直接転送するために、ファイルを `O_DIRECT` で開くことを求める。[[ext4]]の原子的な書き込み（`RWF_ATOMIC`）もDirect I/Oでのみ利用できる。

ストレージの性能評価では、ページキャッシュの効果を除いて記憶装置そのものの性能を測るためにDirect I/Oを用いる。fioでは `direct=1`、[[IOR]]ではPOSIXのバックエンドの `useO_DIRECT`（`--posix.odirect`）でDirect I/Oを用いる。ただし、アプリケーションの実際の性能はページキャッシュの効果を含むため、どちらで測ったかを明記する必要がある。なお、[[NFS]]ではクライアントのページキャッシュは迂回できても、サーバ側でキャッシュされうる。

## 関係
- 前提: [[Page Cache]], [[open]]
- 使う / 使われる: [[InnoDB]], [[GPUDirect Storage]], [[io_uring]]
- 関連: [[fsync]], [[mmap]], [[DMA]]

## 出典
- [open(2) - Linux manual page](https://man7.org/linux/man-pages/man2/open.2.html)
- [Atomic Block Writes - The Linux Kernel documentation（ext4）](https://docs.kernel.org/filesystems/ext4/atomic_writes.html)
- [fio Documentation](https://fio.readthedocs.io/en/latest/fio_doc.html)
- [IOR Options](https://ior.readthedocs.io/en/latest/userDoc/options.html)
- [InnoDB Startup Options and System Variables - MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/innodb-parameters.html)
