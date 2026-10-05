---
aliases: [iscsi, Internet Small Computer Systems Interface, Initiator, イニシエータ, iSCSI Target, iSCSIターゲット, LUN, Logical Unit Number, IQN, SAN, Storage Area Network]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# iSCSI

> SCSIのコマンドをTCP/IPのネットワークで運び、リモートの記憶装置にブロックの単位でアクセスできるようにする、ストレージのネットワークの規格である。

## 概要
iSCSIは、記憶装置を操作するSCSIのコマンドを、TCP/IPの上で送受信する。要求を出す側をイニシエータ（クライアント）、記憶領域を提供する側をターゲット（サーバ）と呼ぶ。ターゲットは、論理ユニット（LUN）と呼ばれる、個別に指定できる記憶装置を提供する。イニシエータは、LUNをローカルのSCSIのディスクと同じ[[Block Storage|ブロックデバイス]]として扱い、その上に[[File System|ファイルシステム]]を作ることができる。規格は2004年のRFC 3720で定められ、現在はRFC 7143にまとめられている。

ブロックの単位で記憶装置を共有するネットワーク（SAN）には、専用の配線を必要とするFibre Channelが用いられてきた。iSCSIは、既存のEthernetとIPのネットワークをそのまま使えるため、安価に構築できる。

## どこで出てくるか
iSCSIは、仮想化の基盤やサーバで、ストレージの装置のディスクを各サーバに割り当てる際に用いられる。ネットワーク越しのブロックデバイスには、ほかに[[NBD]]や、[[NVMe]]のコマンドをネットワークで運ぶ[[NVMe-oF]]がある。

## 関係
- 上位概念: [[Block Storage]]
- 対比: [[NVMe-oF]]（NVMeのコマンドを運ぶ）, [[NBD]]
- 関連: [[NFS]]

## 出典
- [iSCSI - Wikipedia](https://en.wikipedia.org/wiki/ISCSI)
- [RFC 7143: Internet Small Computer System Interface (iSCSI) Protocol (Consolidated)](https://www.rfc-editor.org/rfc/rfc7143)
