---
aliases: [io-uring, liburing, SQE, CQE, SQPOLL]
tags: [term]
maps: ["[[Storage]]", "[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# io_uring

> ユーザ空間とカーネルが共有するリングバッファを介してI/O要求とその完了を受け渡す、Linuxの非同期I/Oインタフェースである。

## 概要
io_uringはLinux 5.1（2019年）で導入された。それ以前のLinuxでは、[[read]]・[[write]]などの通常の[[System Call|システムコール]]は呼び出しごとに完了まで待つ同期I/Oであり、既存の非同期I/Oインタフェース（Linux AIO）は実質的に `O_DIRECT` のI/O（[[Direct IO|Direct I/O]]）でしか非同期に動作しないなどの制約を抱えていた。io_uringは、[[Page Cache|ページキャッシュ]]を経由するバッファードI/Oと `O_DIRECT` の双方について、高速でスケーラブルな非同期I/Oを提供することを目的として設計された。

中心となるのは、ユーザ空間とカーネルが共有メモリ上に持つ二つのリングバッファである。アプリケーションは、操作の種類、対象の[[File Descriptor|ファイルディスクリプタ]]、バッファのアドレスと長さ、および任意の識別値（`user_data`）を記した要求（SQE）を投入キュー（SQ）に書き込む。カーネルは要求を処理し、識別値と結果を記した完了通知（CQE）を完了キュー（CQ）に書き込む。要求の完了順序は投入順序と一致するとは限らないため、アプリケーションは `user_data` によって完了と要求を対応付ける。

システムコールは、リングを作成する `io_uring_setup()`、要求の投入と完了の待機を行う `io_uring_enter()`、資源を事前登録する `io_uring_register()` の三つである。多数のSQEを書き込んでから一度の `io_uring_enter()` で投入できるため、要求ごとのシステムコールのオーバーヘッドが大幅に削減される。さらにSQPOLLモードでは、カーネルのスレッドが投入キューを監視するため、投入のためのシステムコールそのものが不要となる。ファイルディスクリプタやバッファを事前に登録しておくと、要求ごとの参照の取得やメモリのピン留めの処理を省ける。実際のプログラムでは、これらの低水準の操作を包むライブラリliburingを用いるのが一般的である。

io_uringはファイルI/Oに限らず、ネットワークの送受信、ファイルのオープンや[[stat]]など、多様な操作を非同期に実行できるよう拡張されてきた。また、デバイスドライバ固有のコマンドをio_uring経由で渡すパススルーの仕組みも備えており、[[ublk]]はこれを用いてカーネルとユーザ空間の間でブロックI/O要求をやり取りし、[[FUSE]]もio_uringを用いた通信路を備えている。

## どこで出てくるか
io_uringは、高速な[[NVMe]] SSDの性能を引き出す手段として、ストレージの研究やI/Oベンチマークで広く用いられる。fioでは `ioengine=io_uring` として選択でき、従来の同期I/OやLinux AIOとの比較が頻繁に行われる。データベースやストレージシステムの実装でも、I/Oのバックエンドとしての採用が進んでいる。一方で、カーネルの広い機能を新たな経路で公開することから、セキュリティ上の攻撃面として問題視されることもあり、Linux 6.6以降では sysctl の `kernel.io_uring_disabled` によって利用を制限できる。コンテナ環境や共用システムでは利用が無効化されている場合があるため、利用前に確認を要する。

## 関係
- 前提: [[System Call]], [[File Descriptor]]
- 使う / 使われる: [[ublk]], [[FUSE]]（io_uringを通信路として使う）
- 関連: [[Page Cache]], [[NVMe]], [[Latency]], [[Bandwidth]]

## 出典
- [io_uring(7) - Linux manual page](https://man7.org/linux/man-pages/man7/io_uring.7.html)
- [Linux 5.1 - Kernel Newbies](https://kernelnewbies.org/Linux_5.1)
- [Linux 6.6 - Kernel Newbies](https://kernelnewbies.org/Linux_6.6)
- [Documentation for /proc/sys/kernel/ - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/sysctl/kernel.html)
- [Userspace block device driver (ublk driver) - The Linux Kernel documentation](https://docs.kernel.org/block/ublk.html)
