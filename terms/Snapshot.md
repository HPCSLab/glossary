---
aliases: [スナップショット, Snapshots, dm-snapshot, snapshot-origin, snapshot-merge, Point-in-time Copy, COW device]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# Snapshot（スナップショット）

> ある時点のボリュームやファイルシステムの状態を、データを丸ごと複製せずに保存したものである。

## 概要
大きなデータの全体を複製するには長い時間がかかり、その間にデータが書き換えられると、複製の内容が一貫しなくなる。スナップショットは、ある時点の状態を、データの量によらずほぼ一定の時間で固定し、その後もアプリケーションの書き込みを続けられるようにする。多くの実装は[[Copy-on-Write|コピーオンライト]]に基づき、スナップショットを取った後に変更された部分だけを別に保持する。

スナップショットは、ボリュームの層とファイルシステムの層の両方で実装される。ボリュームの層では、Linuxの[[Device Mapper|device mapper]]のsnapshotのターゲットが、任意のブロックデバイスのスナップショットを作る。元のデバイスに書き込みがあると、変更される前のデータがスナップショット用の別のデバイス（COWデバイス）に退避され、スナップショットを読むと、変更されていない部分は元のデバイスから、変更された部分はCOWデバイスから読まれる。COWデバイスが満杯になるとスナップショットは使えなくなるため、空きを監視する必要がある。[[LVM]]のスナップショットはこの仕組みを用い、シンプロビジョニングのスナップショットは、元のボリュームとブロックを共有するため効率がよい。ファイルシステムの層では、[[ZFS]]や[[btrfs]]が、コピーオンライトの性質を用いて、ほぼ瞬時にスナップショットを作れる。

## どこで出てくるか
スナップショットは、システムの更新の前の状態を保存して失敗時に巻き戻す用途や、動作中のシステムのバックアップを一貫した状態で取る用途に用いられる。[[Virtual Machine|仮想マシン]]やコンテナの管理でも用いられ、例えば[[Incus]]では、インスタンスのスナップショットを取って元の状態に戻すことができる。実験環境を構築した直後にスナップショットを取っておけば、壊れた際に容易にやり直せる。

ただし、スナップショットはバックアップの代わりにはならない。スナップショットは元のデータと同じ記憶装置にあり、変更されていない部分は元のデータを共有しているため、記憶装置そのものが故障すれば失われる。

## 関係
- 前提: [[Copy-on-Write]]
- 使う / 使われる: [[ZFS]], [[btrfs]], [[LVM]], [[Device Mapper]], [[Incus]]
- 関連: [[Crash Consistency]], [[Block Storage]]

## 出典
- [Snapshot (computer storage) - Wikipedia](https://en.wikipedia.org/wiki/Snapshot_(computer_storage))
- [Device-mapper snapshot support - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/device-mapper/snapshot.html)
- [Copy-on-write - Wikipedia](https://en.wikipedia.org/wiki/Copy-on-write)
