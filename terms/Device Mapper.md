---
aliases: [device mapper, device-mapper, デバイスマッパー, dm, dmsetup, dm-crypt, dm-verity, dm-thin, dm-flakey, dm-log-writes, /dev/mapper]
tags: [term]
maps: ["[[Storage]]", "[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# Device Mapper（デバイスマッパー）

> Linuxカーネルにおいて、既存の[[Block Storage|ブロックデバイス]]の上に、対応表に従ってI/Oを変換・転送する仮想的なブロックデバイスを構築する枠組みである。

## 概要
device mapperは、仮想的なブロックデバイスのセクタを、どの下位デバイスのどの位置に、どのような処理を施して対応させるかを、表（テーブル）によって定義する。表の各行は「開始セクタ、セクタ数、ターゲットの種類、ターゲットの引数」からなり、デバイスの領域ごとに異なるターゲットを割り当てられる。作成したデバイスは `/dev/mapper/<名前>`（実体は `/dev/dm-N`）として現れ、通常のブロックデバイスと同様に、その上にファイルシステムを作成したり、さらに別のdevice mapperデバイスを重ねたりできる。表の操作には、低水準のツール `dmsetup` を用いる。

処理の内容はターゲットによって決まる。基本的なものとして、下位デバイスの一部をそのまま対応させる `linear`、複数のデバイスに縞状に分散させる `striped`、複製する `mirror`、0を返す `zero`、常にエラーを返す `error` がある。より高度なものとして、透過的な暗号化を行う `crypt`（dm-crypt）、読み込み時にハッシュ木でデータの改竄を検出する `verity`（dm-verity）、ブロックごとの完全性を検査する `integrity`、多数の仮想デバイスと[[Snapshot|スナップショット]]を一つの領域に格納するシンプロビジョニング（`thin`、`thin-pool`）、高速な装置を低速な装置のキャッシュとして用いる `cache`・`writecache` などがある。

利用者が直接 `dmsetup` を使うことはまれであり、通常は上位のツールを介する。論理ボリューム管理のLVM2は、論理ボリュームをdevice mapperの `linear` や `striped` などのデバイスとして構成する。ディスク暗号化のLUKS（`cryptsetup`）はdm-cryptを用いる。

## どこで出てくるか
`lsblk` の出力に現れる `dm-0` などのデバイスや、`/dev/mapper/` 以下の名前は、LVMや暗号化ディスクがdevice mapperで構成されていることを示す。性能を評価する際には、ファイルシステムと物理デバイスの間にdevice mapperの層（特に暗号化やシンプロビジョニング）が挟まっていないかを確認する必要がある。

研究、特にファイルシステムやストレージの検証では、試験用のターゲットが有用である。`dm-flakey` は、一定の周期で書き込みを黙って破棄する、エラーを返す、データの一部を書き換えるなどして、故障する装置を模擬する。`dm-log-writes` は、すべての書き込みを、キャッシュの書き出し（flush）やFUAとの順序を保ったまま別のデバイスに記録する。これを任意の時点まで再生すれば、その時点で電源が断たれた場合に記憶装置に残る状態を再現でき、[[Crash Consistency|クラッシュ整合性]]や[[fsync]]の扱いの誤りを検出できる。`dm-delay` はI/Oに遅延を加える。ブロック層での独自の処理を試作する手段としては、カーネル内で動作するdevice mapperのターゲットのほかに、ユーザ空間で処理を行う[[ublk]]もある。

## 関係
- 上位概念: [[Block Storage]]
- 使う / 使われる: [[blk-mq]], [[ext4]], [[btrfs]]（device mapperデバイスの上に構築できる）
- 対比: [[ublk]]（ブロックデバイスの処理をユーザ空間で行う）
- 関連: [[Crash Consistency]], [[fsync]], [[Linux Kernel]]

## 出典
- [Device Mapper - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/device-mapper/index.html)
- [dmsetup(8) - Linux manual page](https://man7.org/linux/man-pages/man8/dmsetup.8.html)
- [Thin provisioning - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/device-mapper/thin-provisioning.html)
- [dm-flakey - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/device-mapper/dm-flakey.html)
- [dm-log-writes - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/device-mapper/log-writes.html)
