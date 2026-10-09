---
aliases: [Redundant Array of Independent Disks, Redundant Array of Inexpensive Disks, RAID0, RAID1, RAID5, RAID6, RAID10, md, mdadm, Software RAID, ソフトウェアRAID, Write Hole, パリティ, Parity, Striping, ストライピング, Mirroring, ミラーリング]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# RAID

> 複数の記憶装置を組み合わせて一つの記憶領域として扱い、データの分散配置と冗長化によって、性能と耐故障性を高める手法である。

## 概要
RAIDは、1987年にカリフォルニア大学バークレー校のPatterson、Gibson、Katzが提唱し、1988年のSIGMODで発表された。当初は、高価な大容量ディスクの代わりに安価な小型ディスクを多数並べることを意図して「安価なディスクの冗長な配列」と名付けられたが、後に「独立したディスクの冗長な配列」と読み替えられた。

構成の方式はレベルと呼ばれる番号で区別される。RAID0は、データを一定の大きさの断片に区切って複数のディスクに順に配置する（ストライピング）。帯域は台数に応じて向上するが冗長性はなく、一台の故障で全データを失う。RAID1は、同じデータを複数のディスクに書く（ミラーリング）。一台が故障しても動作を続けられるが、使える容量は半分以下となる。RAID5は、ストライピングに加えて、各ストライプのデータの排他的論理和であるパリティを各ディスクに分散して書く。一台が故障しても、残りのデータとパリティから失われたデータを再計算できる。RAID6は、二種類のパリティを持ち、二台の同時故障に耐える。RAID10は、ミラーリングした組をさらにストライピングする入れ子の構成である。

パリティ方式には固有の弱点がある。第一に、ストライプの一部だけを書き換える場合でも、パリティを更新するために古いデータとパリティの読み込みが必要となり、小さなランダム書き込みの性能が低下する。第二に、データとパリティの書き込みの途中で電源が断たれると、両者が食い違ったまま残り、後の再構築で誤ったデータを生成しうる。これをwrite holeと呼ぶ。第三に、大容量のディスクでは故障後の再構築に長時間を要し、その間に別のディスクの故障や読み込みエラーが起きるとデータを失う危険がある。大容量の構成でRAID6が好まれるのはこのためである。また、RAIDは装置の故障に対する備えであり、誤った削除や上書きからデータを守るバックアップの代わりにはならない。

## どこで出てくるか
Linuxでは、カーネルのmdドライバによるソフトウェアRAIDを `mdadm` で構成するのが一般的であり、状態は `/proc/mdstat` で確認できる。mdは、write holeへの対策として、ジャーナル用のデバイスや、RAID5向けの部分パリティログ（PPL）も提供する。このほか、[[LVM]]のRAID種別のLV、専用のコントローラによるハードウェアRAID、RAIDの機能を統合したファイルシステムである[[ZFS]]（RAID-Z）や[[btrfs]]がある。ZFSのRAID-Zは、コピーオンライトと可変幅のストライプによってwrite holeを回避している。

大規模なストレージでは、RAIDの考え方は、任意の数の故障に耐えるよう一般化した[[Erasure Coding|消失訂正符号]]（erasure coding）として、多数のサーバにまたがって用いられる。[[Ceph]]や[[Parallel File System|並列ファイルシステム]]のストレージサーバの内部構成、オブジェクトストレージの冗長化などで、複製と消失訂正符号のどちらを選ぶかは、容量効率、再構築の負荷、[[Latency|レイテンシ]]のトレードオフとして設計上の論点となる。

## 関係
- 上位概念: [[Block Storage]]
- 使う / 使われる: [[Device Mapper]], [[LVM]]
- 対比: [[ZFS]]（RAID-Zでwrite holeを回避する）
- 関連: [[btrfs]], [[Ceph]], [[Bandwidth]], [[Crash Consistency]]

## 出典
- [A Case for Redundant Arrays of Inexpensive Disks (RAID) (Patterson, Gibson, and Katz, 1987)](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1987/CSD-87-391.pdf)
- [RAID - Wikipedia](https://en.wikipedia.org/wiki/RAID)
- [RAID arrays - The Linux Kernel documentation](https://docs.kernel.org/admin-guide/md.html)
