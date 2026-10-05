---
aliases: [Network Block Device, ネットワークブロックデバイス, nbd-server, nbd-client, /dev/nbd0]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# NBD（Network Block Device）

> リモートのサーバが提供する記憶領域を、ネットワーク越しにローカルの[[Block Storage|ブロックデバイス]]として使えるようにする、Linuxの仕組みである。

## 概要
NBDのクライアントは、Linuxカーネルのドライバであり、`/dev/nbd0` のようなブロックデバイスを提供する。このデバイスに読み書きの要求が来ると、ドライバはTCPで要求をサーバに送り、サーバが読み書きの結果を返す。サーバ（nbd-server）は完全にユーザ空間のプログラムであり、Windowsを含む様々なOSに移植されている。カーネルのモジュールが必要なのはクライアントだけである。

NBDはブロックデバイスを提供するため、その上に任意の[[File System|ファイルシステム]]を作ることができる。この点で、ファイルの単位で共有する[[NFS]]とは異なる。ただし、ブロックデバイスを複数のクライアントが同時にマウントすると、通常のファイルシステムは互いの変更を知らないため、データが壊れる。

## どこで出てくるか
NBDは、ブロックデバイスをユーザ空間のプログラムとして実装する手段として用いられてきた。例えば、[[QEMU]]のディスクイメージをホストのブロックデバイスとして見せる用途がある。ユーザ空間でブロックデバイスを実装する比較的新しい仕組みとして、[[io_uring]]を用いてカーネルとの間で要求を受け渡す[[ublk]]がある。ネットワーク越しのブロックデバイスには、ほかに[[iSCSI]]や[[NVMe-oF]]がある。

## 関係
- 上位概念: [[Block Storage]]
- 対比: [[NFS]]（ファイルの単位で共有する）, [[ublk]]（io_uringを用いてユーザ空間で実装する）
- 関連: [[iSCSI]], [[NVMe-oF]], [[QEMU]]

## 出典
- [Network Block Device (TCP version) - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/blockdev/nbd.html)
- [NetworkBlockDevice/nbd - GitHub](https://github.com/NetworkBlockDevice/nbd)
- [QEMU disk image NBD server - QEMU documentation](https://www.qemu.org/docs/master/tools/qemu-nbd.html)
