---
aliases: [RDMA over Converged Ethernet, RoCEv2, RoCE v2, RoCEv1, PFC, Priority Flow Control, Lossless Ethernet, ロスレスEthernet]
tags: [term]
maps: ["[[Network]]"]
status: draft
updated: 2026-10-10
---
# RoCE

> [[RDMA]]をEthernetのネットワーク上で実現するためのプロトコルであり、正式名称は RDMA over Converged Ethernet である。

## 概要
RoCEは、[[InfiniBand]]のRDMAの仕組みを、データセンターで広く用いられるEthernetの上で動作させるものであり、仕様はInfiniBandと同じくIBTAが定めている。アプリケーションからはInfiniBandと同じ[[Verbs|verbs]]のインタフェースで利用でき、[[MPI]]の実装や[[UCX]]などのソフトウェアの多くをそのまま用いることができる。

版は二つある。RoCE v1は、Ethernetのリンク層のプロトコルとして動作するため、同じブロードキャストドメイン内でしか通信できない。RoCE v2は、UDP/IPの上で動作し（UDPの宛先ポート4791を使用）、ルータを越えて通信できる。現在一般に使われているのはRoCE v2である。

InfiniBandは、受信側の空きを確認してから送るフロー制御によって、混雑時にもパケットを失わない。一方、通常のEthernetは混雑時にパケットを破棄し、その回復を上位のTCPに任せる。RDMAのプロトコルはパケットの喪失に弱いため、RoCEで十分な性能を得るには、混雑時に送信を一時停止させるPFC（Priority Flow Control）などによって、パケットを失わない（ロスレスな）Ethernetを構成するのが一般的である。RoCE v2は、ECNによる輻輳の通知に基づく輻輳制御の仕組みも備える。

## どこで出てくるか
RoCEは、InfiniBandの専用のネットワークを持たないデータセンターやクラウド、また機械学習用の大規模な[[GPU]]クラスタで、RDMAを用いるために広く採用されている。HPCクラスタでも、Ethernetの設備を活かしつつ低[[Latency|遅延]]の通信を得る手段として用いられる。運用上は、PFCの設定の不備によって性能が大きく低下したり、PFCによる一時停止が連鎖してネットワーク全体が停滞したりする問題が知られており、ネットワークの設定と監視が性能を左右する。性能を評価する際には、InfiniBandとRoCEのどちらで、どの速度のリンクを用いているかを明記する必要がある。

## 関係
- 上位概念: [[RDMA]]
- 対比: [[InfiniBand]]（RDMAのための専用のネットワーク）
- 使う / 使われる: [[Verbs]]（共通のプログラミングインタフェース）
- 関連: [[UCX]], [[MPI]], [[Latency]], [[Bandwidth]]

## 出典
- [RDMA over Converged Ethernet - Wikipedia](https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet)
