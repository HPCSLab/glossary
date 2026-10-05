---
aliases: [Userspace Block Device, ublk_drv, ublksrv, ユーザ空間ブロックデバイス]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# ublk

> ブロックデバイスの処理をユーザ空間のプロセスで実装するための、[[io_uring]]を基盤としたLinuxの枠組みである。

## 概要
ublkは Linux 6.0 で導入された。カーネル側のドライバは、通常の[[Block Storage|ブロックデバイス]] `/dev/ublkbN` を提供し、そこに届いたI/O要求を、ublkサーバと呼ばれるユーザ空間のプロセスに転送する。サーバは要求を任意の方法で処理し、結果をカーネルに返す。これにより、従来カーネル内で実装されてきた loop デバイスや[[NBD]]のような仮想ブロックデバイスを、ユーザ空間で実装できる。カーネル外での実装は、デバッグの容易さ、障害の隔離、開発の速さの点で有利である。

ublkは三種類のデバイスを用いる。`/dev/ublk-control` はデバイスの追加・設定・開始・停止などの管理コマンドを受け付ける。`/dev/ublkcN` はデバイスごとのキャラクタデバイスで、サーバがI/O要求の受け渡しに用いる。`/dev/ublkbN` は、利用者から見えるブロックデバイスである。I/O要求の受け渡しはio_uringのパススルーコマンドで行う。サーバは `FETCH_REQ` で要求の到着を待ち、処理を終えると `COMMIT_AND_FETCH_REQ` で結果の返却と次の要求の待機を一度に行う。これにより、要求ごとのシステムコールの往復が抑えられる。データの複製を避けるゼロコピーの仕組みも用意されている。参照実装として ublksrv とそのライブラリ libublksrv が提供されており、権限を持たないユーザが自分のデバイスを作成できるモードもある。

## どこで出てくるか
ublkは、独自の圧縮・暗号化・複製・ネットワーク越しの転送などを行うブロックデバイスを試作する際に用いられる。作成したデバイスの上には[[ext4]]などの通常のファイルシステムを構築できるため、ファイルシステムを改変せずに下層の記憶装置の振る舞いだけを変えて評価できる。[[FUSE]]がファイルシステムのインタフェース（ファイル名、[[Metadata|メタデータ]]、[[POSIX]]の意味論）をユーザ空間に委ねるのに対し、ublkはその下のブロックの読み書きのみを委ねる。どちらの層に介入するかは、実現したい機能と、性能上のオーバーヘッドとの兼ね合いで選ぶ。

## 関係
- 上位概念: [[Block Storage]]
- 前提: [[io_uring]]
- 対比: [[FUSE]]（ファイルシステムの層をユーザ空間で実装する）
- 関連: [[NBD]], [[File System]]

## 出典
- [Userspace block device driver (ublk driver) - The Linux Kernel documentation](https://docs.kernel.org/block/ublk.html)
- [Linux 6.0 - Kernel Newbies](https://kernelnewbies.org/Linux_6.0)
