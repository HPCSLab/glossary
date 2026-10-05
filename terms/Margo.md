---
aliases: [mochi-margo, Mochi, Argobots, Thallium, User-Level Thread, ユーザレベルスレッド, ULT]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Storage]]", "[[Network]]"]
status: draft
updated: 2026-10-06
---
# Margo（mochi-margo）

> RPCフレームワーク[[Mercury]]と、ユーザレベルスレッドのライブラリArgobotsを組み合わせ、HPC向けのデータサービスを逐次的な書き方で実装できるようにするライブラリであり、Mochiプロジェクトの中核をなす。

## 概要
Mochiは、アルゴンヌ国立研究所、ロスアラモス国立研究所、カーネギーメロン大学、The HDF Groupの共同プロジェクトであり、HPC向けのストレージサービスを、再利用可能な部品（マイクロサービス）の組み合わせとして構築することを目指している。部品には、キーバリューストアのYokan、大きなデータを扱うWarabi、グループの管理を行うFlockなどがある。Margoは、これらの部品が共通に用いる実行基盤である。

Mercuryは、RPCとRDMAによる高速な通信を提供するが、そのAPIは非同期で、処理をコールバックとして記述するため、複数の通信を組み合わせる複雑な処理を書くのが難しい。Argobotsは、OSのスレッドより軽量で、ライブラリが切り替えを管理するユーザレベルスレッドを提供する。Margoは両者を統合し、Mercuryの操作を発行したスレッドを、その完了までいったん中断し、完了したら自動的に再開させる。そのため、利用者は、RPCの呼び出しを、結果が返るまで待つ通常の関数呼び出しのように逐次的に書ける。サーバ側では、届いたRPCのハンドラがそれぞれユーザレベルスレッドとして実行されるため、多数の要求を、OSのスレッドを増やさずに並行して処理できる。C++からは、Margoを包むThalliumを用いることもできる。

## どこで出てくるか
Margoは、HPC向けのデータサービスや分散ストレージを研究で試作する際の基盤として用いられる。通信の性能をMercuryから得つつ、プログラムを逐次的に書けるため、サービスの論理に集中できる。性能を調べる際には、ユーザレベルスレッドの数や、通信の進行を担うスレッドの配置（専用のスレッドで進行させるか、処理と同じスレッドで行うか）の設定が、[[Latency|レイテンシ]]と処理能力に影響することに注意を要する。

## 関係
- 使う / 使われる: [[Mercury]]（通信）, [[Key-Value Store]]（Yokanなどの部品）
- 関連: [[DAOS]], [[RDMA]], [[Parallel File System]], [[Latency]]

## 出典
- [Mochi documentation](https://mochi.readthedocs.io/en/latest/)
- [mochi-margo - GitHub](https://github.com/mochi-hpc/mochi-margo)
- [Mercury](https://mercury-hpc.github.io/)
