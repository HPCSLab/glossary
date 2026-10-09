---
aliases: [NVMe over Fabrics, NVMeoF, NVMe/TCP, NVMe/RDMA, NVMe/FC, nvme connect, nvmet, NQN, Storage Disaggregation, ストレージの分離]
tags: [term]
maps: ["[[Storage]]", "[[Network]]"]
status: draft
updated: 2026-10-10
---
# NVMe-oF（NVMe over Fabrics）

> [[NVMe]]のコマンド体系を、[[PCIe|PCI Express]]の代わりにネットワークを介して用いることで、リモートの記憶装置をローカルのNVMe装置に近い性能で利用するための規格である。

## 概要
NVMeは、もとはPCI Expressで計算機に直接接続された[[SSD]]のためのインタフェースであり、投入キューと完了キューの対を介してコマンドをやり取りする。NVMe-oFは、このキューの対とコマンドの体系をそのまま保ちつつ、転送路をネットワークに置き換える。現在のNVMeの仕様は、共通の基本仕様に、コマンド体系ごとの仕様と転送路ごとの仕様を組み合わせる構成をとっており、転送路としてPCI Expressのほかに、[[RDMA]]（[[InfiniBand]]や[[RoCE]]）、TCP、Fibre Channelが定められている。

NVMe-oFでは、記憶装置を提供する側をターゲット、利用する側をホストと呼ぶ。ターゲットは、一つ以上の名前空間をまとめたサブシステムを、NQN（NVMe Qualified Name）と呼ばれる名前で公開する。ホストは、ターゲットのアドレスとポート、サブシステムのNQNを指定して接続すると、リモートの名前空間がローカルの[[Block Storage|ブロックデバイス]]（`/dev/nvmeXnY`）として現れ、ローカルのNVMe装置と同じように扱える。Linuxでは、ホスト側の機能がカーネルに含まれ、`nvme-cli` の `nvme discover` で公開されているサブシステムを探し、`nvme connect` で接続する。ターゲット側の機能もカーネルに含まれている。

転送路の選択は性能と導入のしやすさのトレードオフである。RDMAを用いると、データの複製やCPUの処理が少なく、[[Latency|レイテンシ]]の上乗せを小さく抑えられるが、RDMAに対応したネットワークとその設定が必要となる。TCPを用いる方式は、通常のEthernetと[[NIC|ネットワークカード]]で動作するため導入が容易であるが、CPUの負荷とレイテンシはRDMAより大きい。

## どこで出てくるか
NVMe-oFは、ストレージの分離（disaggregation）の中核となる技術である。[[Compute Node|計算ノード]]ごとにSSDを搭載する代わりに、SSDを集めたストレージ用のサーバを用意し、各計算ノードがNVMe-oFで必要な容量だけを利用すれば、計算とストレージの資源を独立に増減でき、SSDの使用効率も高まる。HPCや機械学習のクラスタでは、高速な一時記憶の共有や、[[GPU]]へのデータの供給にも用いられる。研究の観点では、ネットワーク越しのアクセスによって増えるレイテンシ、ターゲット側のCPUの負荷、多数のホストが一つのSSDを共有するときの性能の分離が主な論点となる。NVMe-oFは、ブロックデバイスを提供するにとどまり、複数のホストが同じ名前空間を共有してファイルを読み書きするには、その上に共有を前提としたファイルシステムなどが別途必要となる。

## 関係
- 上位概念: [[NVMe]]
- 使う / 使われる: [[RDMA]], [[RoCE]], [[InfiniBand]]（転送路）
- 対比: [[NVMesh]]（ターゲットのCPUを介さない独自方式）, [[NFS]]（ファイル単位の共有）
- 関連: [[Block Storage]], [[SSD]], [[Latency]], [[blk-mq]]

## 出典
- [Specifications - NVM Express](https://nvmexpress.org/specifications/)
- [nvme-connect - nvme-cli documentation](https://github.com/linux-nvme/nvme-cli/blob/master/Documentation/nvme-connect.txt)
