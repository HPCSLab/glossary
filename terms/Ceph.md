---
aliases: [RADOS, CRUSH, CephFS, RBD, RADOS Gateway, RGW, OSD, BlueStore, Placement Group]
tags: [term]
maps: ["[[Storage]]", "[[Distributed Systems]]"]
status: draft
updated: 2026-10-06
---
# Ceph

> 汎用サーバ群の上に、オブジェクト、ブロック、ファイルの三種類のインタフェースを提供する、オープンソースの分散ストレージシステムである。

## 概要
CephはSage Weilらがカリフォルニア大学サンタクルーズ校で開発し、2006年のOSDIで発表された。現在はオープンソースのプロジェクトとして、クラウド基盤や大規模なストレージの構築に広く用いられている。

Cephの基盤は、RADOSと呼ばれる分散オブジェクトストアである。その上に、三種類のインタフェースが構築されている。RBDは仮想的な[[Block Storage|ブロックデバイス]]を、RADOS Gateway（RGW）はS3やSwiftと互換の[[Object Storage|オブジェクトストレージ]]を、CephFSは[[POSIX]]互換の[[File System|ファイルシステム]]を提供する。いずれも、最終的にはRADOSのオブジェクトとしてデータを格納する。

RADOSは、役割の異なるデーモンで構成される。OSDは記憶装置ごとに動作し、オブジェクトの格納、複製、障害からの回復を担う。現在の標準の格納方式であるBlueStoreは、ファイルシステムを介さずに記憶装置を直接管理する。モニタ（MON）は、クラスタの構成情報（クラスタマップ）を、[[Consensus|合意]]によって複数台で一致させて保持する。CephFSを用いる場合は、[[Metadata|メタデータ]]を管理するMDSも動作する。

Cephの最大の特徴は、データの配置を決めるCRUSHアルゴリズムである。オブジェクトはまずプール内の配置グループ（placement group）に割り当てられ、CRUSHが配置グループからOSDの組を計算によって決定する。クライアントはクラスタマップを持ってこの計算を自ら行うため、「どのデータがどこにあるか」を問い合わせる中央の表やサーバを必要とせず、OSDと直接通信できる。CRUSHは、障害の単位（ホスト、ラック、電源系統など）を考慮して複製を分散させるよう規則を記述できる。データの冗長化には、複製のほかに、容量効率の高い消失訂正符号（erasure coding）も選べる。

## どこで出てくるか
Cephは、OpenStackなどのクラウド基盤で、仮想マシンのディスク（RBD）やオブジェクトストレージ（RGW）を提供する用途で広く用いられている。HPCの文脈では、[[Lustre]]などの[[Parallel File System|並列ファイルシステム]]と比較される。Cephは、汎用性、自己修復、運用の柔軟性に優れる一方、HPCの大規模な並列I/Oに対する性能では、専用の並列ファイルシステムが優位とされることが多い。研究の文脈では、中央の表を持たずに計算でデータを配置するCRUSHの考え方や、ファイルシステムを介さないBlueStoreの設計が、分散ストレージの設計例としてよく参照される。

## 関係
- 上位概念: [[Object Storage]]（RADOSとRGW）
- 使う / 使われる: [[Block Storage]]（RBD）, [[File System]]（CephFS）, [[Consensus]]（モニタ）
- 対比: [[Lustre]], [[Parallel File System]]
- 関連: [[Metadata]], [[Distributed File System]]

## 出典
- [Architecture - Ceph Documentation](https://docs.ceph.com/en/latest/architecture/)
- [Ceph: A Scalable, High-Performance Distributed File System - USENIX OSDI 2006](https://www.usenix.org/conference/osdi-06/ceph-scalable-high-performance-distributed-file-system)
