---
aliases: [verbs, ibverbs, libibverbs, IB Verbs, RDMA Verbs, Queue Pair, QP, キューペア, Completion Queue, CQ, Protection Domain, PD, Memory Region, MR, rdma-core]
tags: [term]
maps: ["[[Network]]"]
status: draft
updated: 2026-10-10
---
# Verbs

> [[RDMA]]を利用するための低水準のプログラミングインタフェースであり、Linuxではlibibverbsとして提供される。

## 概要
verbsという名称は、InfiniBandの仕様がハードウェアに対する操作を「動詞（verb）」として抽象的に定義したことに由来する。Linuxでは、rdma-coreパッケージに含まれるlibibverbsがC言語のAPIとして実装しており、関数名は `ibv_` で始まる。[[InfiniBand]]と[[RoCE]]は、いずれもこのインタフェースで利用できる。

verbsのプログラムは、いくつかの資源を順に用意して通信を行う。まず、デバイスを開き、保護ドメイン（PD）を作る。保護ドメインは、以下の資源をまとめて、互いにアクセスしてよい範囲を定める単位である。次に、通信に用いるメモリを `ibv_reg_mr()` で登録し（メモリ領域、MR）、ローカルで使う鍵（lkey）と遠隔のノードに渡す鍵（rkey）を得る。完了通知を受け取る完了キュー（CQ）を作り、通信の端点であるキューペア（QP）を `ibv_create_qp()` で作る。QPは送信キューと受信キューからなり、送信と受信のそれぞれにCQを対応付ける。QPには、一対一の接続を前提に信頼性のある転送を行うRC（Reliable Connection）、信頼性のない接続型のUC、接続を持たないデータグラム型のUDなどの種類がある。

通信は、作業要求（work request）をQPに投入することで行う。受信の準備は `ibv_post_recv()`、送信やRDMAの読み書きは `ibv_post_send()` で投入し、操作の種類として、送受信（SEND）、相手のメモリへの書き込み（RDMA WRITE）と読み出し（RDMA READ）、不可分な遠隔操作（比較交換、加算）を指定する。完了は `ibv_poll_cq()` でCQから取り出して確認する。送信に用いたバッファは、完了を確認するまで再利用してはならない。接続型のQPでは、通信を始める前に、相手のQPの番号やアドレスなどを、TCPなどの別の手段で交換して、QPの状態を順に遷移させる必要がある。

## どこで出てくるか
verbsは柔軟で高性能である一方、資源の準備、接続の確立、メモリの登録、完了の管理をすべて利用者が行う必要があり、記述量が多く誤りやすい。そのため、アプリケーションが直接verbsを用いることは少なく、[[MPI]]の実装、[[UCX]]、libfabric、[[Mercury]]などの通信ライブラリが内部で用いる。一方で、RDMAを用いたシステムの研究では、片側通信の活用やQPの資源の削減など、verbsの水準で設計を工夫することが多く、その仕組みの理解は不可欠である。状態の確認には `ibv_devinfo`、基本的な性能測定にはperftestの `ib_write_bw` などを用いる。

## 関係
- 上位概念: [[RDMA]]
- 使う / 使われる: [[InfiniBand]], [[RoCE]]（verbsで利用できるネットワーク）, [[UCX]], [[Mercury]], [[MPI]]（verbsを内部で使う）
- 関連: [[Latency]], [[io_uring]]（同じく投入キューと完了キューで要求を受け渡す）

## 出典
- [ibv_create_qp(3) - Linux manual page](https://man7.org/linux/man-pages/man3/ibv_create_qp.3.html)
- [ibv_reg_mr(3) - Linux manual page](https://man7.org/linux/man-pages/man3/ibv_reg_mr.3.html)
- [ibv_post_send(3) - Linux manual page](https://man7.org/linux/man-pages/man3/ibv_post_send.3.html)
