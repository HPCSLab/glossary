---
aliases: [spdk, Storage Performance Development Kit, SPDK NVMe Driver, SPDK bdev, spdk_tgt, setup.sh, Kernel Bypass, カーネルバイパス, Polling, ポーリング, Polled Mode]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# SPDK（Storage Performance Development Kit）

> [[NVMe]] SSDなどの記憶装置を、カーネルを経由せずにユーザ空間のプログラムから直接操作し、高い性能のストレージのアプリケーションを作るための、ツールとライブラリの集まりである。

## 概要
SPDKは、高い性能を得るために三つの方針をとる。第一に、必要なドライバを全てユーザ空間に移し、[[System Call|システムコール]]を避け、アプリケーションからデータを複製せずに扱えるようにする。第二に、割り込みではなく、装置の完了をプログラムが繰り返し確かめる（ポーリング）ことで、[[Latency|レイテンシ]]とそのばらつきを小さくする。第三に、I/Oの経路でロックを用いず、スレッドの間のメッセージの受け渡しで協調する。

その中心は、ユーザ空間で動く、ポーリング方式の、非同期で、ロックを用いないNVMeのドライバである。その上に、装置を抽象化し、論理ボリュームなどを提供するユーザ空間のブロックデバイスの層（bdev）がある。さらに、これらを用いた[[NVMe-oF]]、[[iSCSI]]、vhost（[[Virtual Machine|仮想マシン]]に記憶装置を提供する）のターゲットが含まれる。SPDKは、[[DPDK]]のライブラリを取り込んで用いている。

## どこで出てくるか
SPDKを使うには、ヒュージページのメモリを確保し、NVMeの装置をLinuxの標準のドライバから切り離す必要がある。これを行う `scripts/setup.sh` をroot権限で実行する。切り離した装置はカーネルからは見えなくなるため、その上で通常のファイルシステムを使うことはできない。

SPDKは、カーネルを経由せずにNVMe SSDを用いるストレージのシステムで用いられる。例えば、[[DAOS]]のサーバは、NVMe SSDにSPDKを用いてユーザ空間から直接アクセスする。一方、ポーリングのためにCPUの時間を使い続けることや、ファイルシステムなどのカーネルの機能を使えないことが、カーネルの[[io_uring]]などと比べる際の論点となる。

## 関係
- 使う / 使われる: [[NVMe]], [[DPDK]], [[NVMe-oF]], [[DAOS]]
- 対比: [[io_uring]], [[blk-mq]]（カーネルのI/Oの経路）
- 関連: [[RDMA]], [[ublk]], [[Virtual Memory]]（ヒュージページ）

## 出典
- [About SPDK - SPDK documentation](https://spdk.io/doc/about.html)
- [spdk/spdk - GitHub](https://github.com/spdk/spdk)（Hugepages and Device Binding、DPDKの利用）
