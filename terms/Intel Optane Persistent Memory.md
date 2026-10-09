---
aliases: [Optane Persistent Memory, Intel Optane DC Persistent Memory, Optane PMem, PMem, DCPMM, Persistent Memory, 永続メモリ, 不揮発性メモリ, NVM, NVDIMM, 3D XPoint, App Direct Mode, Memory Mode, PMDK, libpmem, libpmemobj, CLWB, ADR]
tags: [term]
maps: ["[[Storage]]", "[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# Intel Optane Persistent Memory（永続メモリ）

> DRAMと同じメモリスロットに装着し、CPUからバイト単位で読み書きでき、かつ電源を切ってもデータが失われない、Intelのメモリ製品である。

## 概要
Optane Persistent Memory（PMem）は、IntelとMicronが共同開発した不揮発性メモリの技術3D XPointを用いた製品であり、2019年に第2世代Xeonスケーラブル・プロセッサ（Cascade Lake）とともに登場した。DRAMよりも大容量かつ安価で、NAND型の[[SSD]]よりもはるかに低遅延であり、両者の中間に位置する。一方で、DRAMと比べると、読み書きの[[Latency|レイテンシ]]は大きく、特に書き込みの[[Bandwidth|バンド幅]]は低い。

PMemには二つの動作形態がある。メモリモードでは、PMemを大容量の主記憶として用い、DRAMはその前段のキャッシュとして働く。アプリケーションからは単に主記憶が大きくなったように見え、改変なしに利用できるが、データは永続化されない。App Directモードでは、PMemを永続的な記憶領域としてOSに見せ、アプリケーションが直接扱う。Linuxでは、PMemの領域はnamespaceとして構成され、ファイルシステムを介して[[mmap]]で写像するfsdax、あるいはキャラクタデバイスとして直接写像する[[devdax]]などの形態で利用する。いずれも[[Page Cache|ページキャッシュ]]を経由せず、ロード・ストア命令でPMem上のデータを直接読み書きする（DAX）。

永続メモリへの書き込みは、ストア命令を実行しただけでは永続化されない。データはまずCPUのキャッシュに置かれるため、キャッシュラインを書き出す命令（CLWBなど）と、その完了を待つ順序付けの命令（SFENCE）を発行して初めて、電源断にも耐える領域（メモリコントローラの書き込みキュー以降）に到達する。さらに、複数のデータを不可分に更新するには、ログを用いるなど、[[Crash Consistency|クラッシュ整合性]]を自ら確保する必要がある。これを支援するために、IntelはPMDK（Persistent Memory Development Kit）を提供しており、低水準の永続化を扱うlibpmemや、トランザクションを備えた永続オブジェクトの格納を提供するlibpmemobjなどが含まれる。

## どこで出てくるか
PMemは、2010年代後半から2020年代初頭にかけて、ストレージとシステムソフトウェアの研究で最も盛んに扱われた題材の一つであった。永続メモリ向けのファイルシステム、[[Key-Value Store|キーバリューストア]]、データ構造、トランザクションの手法が数多く提案された。2020年のFASTで発表されたYangらの研究は、実際のOptaneの性能が、それ以前にエミュレーションで想定されていたものと大きく異なることを実測で示し、その後の研究の前提を改めさせた。[[DAOS]]も、当初は[[Metadata|メタデータ]]や小さなデータの格納先としてPMemを用いる設計であった。

しかし、Intelは2022年7月にOptane事業の終了を発表し、PMemの開発は打ち切られた。そのため、PMemを前提とした研究成果を現在のシステムで再現・発展させるのは難しくなっている。PMemの研究で培われた、バイト単位でアクセスできる永続的な記憶と、キャッシュの書き出しによる永続化の順序制御という考え方は、[[CXL]]で接続するメモリなど、後継の技術の議論に引き継がれている。

## 関係
- 使う / 使われる: [[devdax]]（Linuxでの利用形態）, [[mmap]], [[DAOS]]
- 対比: [[SSD]]（ブロック単位でアクセスする記憶装置）
- 関連: [[Crash Consistency]], [[Page Cache]], [[Virtual Memory]], [[Latency]], [[Bandwidth]], [[FAST]]

## 出典
- [3D XPoint - Wikipedia](https://en.wikipedia.org/wiki/3D_XPoint)
- [An Empirical Guide to the Behavior and Use of Scalable Persistent Memory - USENIX FAST 2020](https://www.usenix.org/conference/fast20/presentation/yang)
- [Persistent Memory Development Kit - pmem.io](https://pmem.io/pmdk/)
- [Intel is Winding Down Its Optane Business: What Does This Mean for Customers? - WWT](https://www.wwt.com/blog/intel-is-winding-down-its-optane-business-what-does-this-mean-for-customers)
