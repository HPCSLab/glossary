---
aliases: [Filesystem in Userspace, libfuse, fusermount, /dev/fuse]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# FUSE

> ファイルシステムの実装をカーネルではなくユーザ空間の通常のプロセスとして動作させるための、Linuxの枠組みである。

## 概要
FUSEは、カーネルモジュール（`fuse.ko`）、ユーザ空間のライブラリ（libfuse）、マウント用のユーティリティ（`fusermount`）からなる。FUSEのファイルシステムは、カーネルから見ると[[VFS]]の下にある一つのファイルシステム実装であるが、その操作の中身はユーザ空間のデーモンが実行する。カーネルとデーモンは、キャラクタデバイス `/dev/fuse` を介して要求と応答をやり取りする。

例えばアプリケーションが[[unlink]]を呼ぶと、VFSはFUSEのカーネル側に処理を渡し、カーネル側は要求をキューに入れて呼び出し元を待機させる。デーモンは `/dev/fuse` を[[read]]して要求を受け取り、ファイルの削除に相当する処理を自らのやり方で実行し、結果を `/dev/fuse` に[[write]]して返す。これによって待機していたアプリケーションが再開する。デーモンの処理は任意であるため、ネットワーク上のサーバ、オブジェクトストレージ、データベース、あるいは単なるメモリ上の構造を、[[POSIX]]のファイルとして見せることができる。

libfuseは二種類のAPIを提供する。高水準APIでは、コールバック関数がパス名を受け取り、関数から戻ると処理が完了する。低水準APIでは、コールバックが[[Inode|inode]]番号を扱い、応答を明示的に送る必要がある。前者は実装が容易で、後者は性能と制御の自由度に優れる。`fusermount` は setuid されたヘルパであり、一般ユーザでもマウントを可能にする。このとき、既定ではマウントしたユーザ以外はアクセスできず、他のユーザにも開放するには `allow_other` オプションと管理者による許可が必要となる。

FUSEの性能上の弱点は、要求ごとにカーネルとユーザ空間の間を往復するため、コンテキストスイッチとデータの複製が加わる点にある。これを緩和するため、Linux 6.9では、デーモンが指定した下位のファイルに対して読み書きをカーネル内で直接行うパススルーモードが、Linux 6.14では、[[io_uring]]を用いてCPUコアごとのキューで要求をやり取りするFUSE over io_uringが導入された。

## どこで出てくるか
FUSEは、カーネルを改変せずにファイルシステムを試作できるため、ストレージ研究で新しい設計を実装・評価する際の定番の手段である。一方で、評価結果にはFUSE自体のオーバーヘッドが含まれるため、論文ではカーネル実装との差やFUSEの寄与を区別して議論する必要がある。実用面では、SSH越しにリモートのディレクトリをマウントする `sshfs` や、[[Object Storage|オブジェクトストレージ]]をファイルシステムとして見せるツールなどが広く使われている。ファイル単位ではなくブロックデバイス単位でユーザ空間に処理を委ねる仕組みとしては、[[ublk]]がある。

## 関係
- 上位概念: [[VFS]]
- 前提: [[System Call]]
- 対比: [[ublk]]（ファイルシステムではなくブロックデバイスをユーザ空間で実装する）
- 使う / 使われる: [[io_uring]]
- 関連: [[File System]], [[Object Storage]]

## 出典
- [FUSE Overview - The Linux Kernel documentation](https://docs.kernel.org/filesystems/fuse/fuse.html)
- [FUSE Passthrough - The Linux Kernel documentation](https://docs.kernel.org/filesystems/fuse/fuse-passthrough.html)
- [FUSE-over-io-uring design documentation - The Linux Kernel documentation](https://docs.kernel.org/filesystems/fuse/fuse-io-uring.html)
- [libfuse - GitHub](https://github.com/libfuse/libfuse)
- [Linux 6.9 - Kernel Newbies](https://kernelnewbies.org/Linux_6.9)
- [Linux 6.14 - Kernel Newbies](https://kernelnewbies.org/Linux_6.14)
