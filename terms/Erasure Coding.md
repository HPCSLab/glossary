---
aliases: [消失訂正符号, イレージャコーディング, Erasure Code, EC, Reed-Solomon, Reed-Solomon Code, リード・ソロモン符号, RS Code]
tags: [term]
maps: ["[[Storage]]", "[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# Erasure Coding（消失訂正符号）

> データをk個の断片に分け、そこからm個の冗長な断片を計算して、合わせてk+m個を別々の記憶装置やサーバに置き、どのm個が失われても残りから元のデータを復元できるようにする冗長化の手法である。

## 概要
記憶装置やサーバの故障に備える最も単純な方法は、同じデータを複数の場所に置く複製である。3重の複製は2台の故障に耐えるが、元のデータの3倍の容量を使う。消失訂正符号では、例えばk=4、m=2とすると、2台の故障に耐えつつ、容量は元の1.5倍で済む。一般に、容量は元の(k+m)/k倍となる。[[RAID]]のRAID5とRAID6は、それぞれm=1とm=2の場合に当たり、消失訂正符号はこれを任意のmに一般化し、多数のサーバにまたがって用いるものと見なせる。代表的な符号はReed-Solomon符号であり、k+m個のうち任意のk個の断片から元のデータを復元できる。

この容量の効率と引き換えに、消失訂正符号には三つの費用がある。第一に、符号化と復号のための計算である。第二に、一つの断片を失ったときの再構築では、他のk個の断片を読み出す必要があり、複製の場合の1個に比べて、ネットワークと記憶装置への負荷が大きい。第三に、小さな部分の書き換えでは、冗長な断片も計算し直すため、既存のデータを読んでから書く必要が生じる。このため、消失訂正符号は、一度書いたら書き換えの少ない大きなデータに向き、小さな書き換えの多いデータや[[Metadata|メタデータ]]には複製が用いられることが多い。

## どこで出てくるか
分散ストレージでは、冗長化の方式として複製と消失訂正符号のどちらを選ぶかが、容量の効率、再構築の負荷、[[Latency|レイテンシ]]のトレードオフとして設計上の論点となる。[[Ceph]]は、プールごとに複製と消失訂正符号を選べ、消失訂正符号のプールではk、mを指定する。HDFSは、既定の方針としてReed-Solomon符号のRS(6,3)を提供する。[[DAOS]]もオブジェクトの冗長化に消失訂正符号を選べる。[[DDN IME]]は、[[Compute Node|計算ノード]]のクライアントが冗長な断片を計算してからサーバに送る。

## 関係
- 対比: [[RAID]]（主に一台の計算機の中の記憶装置の組を対象とし、RAID5とRAID6はm=1とm=2に当たる）
- 使う / 使われる: [[Ceph]], [[DAOS]], [[DDN IME]]
- 関連: [[Distributed File System]], [[Parallel File System]], [[Object Storage]]

## 出典
- [Erasure Code - Ceph Documentation](https://docs.ceph.com/en/latest/rados/operations/erasure-code/)
- [HDFS Erasure Coding - Apache Hadoop](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HDFSErasureCoding.html)
