---
aliases: [トークンバケット, Token Bucket Filter, TBF, トークンバケットフィルタ, NRS TBF, Rate Limiting, レート制限]
tags: [term]
maps: ["[[Network]]"]
status: draft
updated: 2026-10-17
---
# Token Bucket（トークンバケット）

> 一定の速さで補充されるトークンを溜めておき、要求やデータを送るたびにトークンを消費させることで、平均の速さを制限しつつ一時的な集中（バースト）を許す、流量の制御の仕組みである。

## 概要
共有された資源（ネットワークのリンクやストレージのサーバ）を多数の利用者が使うとき、一部の利用者が資源を[[Saturation|飽和]]させると、他の利用者の[[Latency|レイテンシ]]が悪化する。トークンバケットは、利用者ごとに使える量を制限する仕組みである。バケットには一定の速さrでトークンが補充され、容量bを超えた分は捨てられる。要求（あるいはパケットのバイト）一つを通すたびにトークンを一つ消費し、トークンが無ければ補充されるまで要求を待たせる。このため、長い時間で平均した速さはrを超えず、任意の時間tの間に通る量は b + rt 以下に抑えられる。一方、しばらく利用が無かった後は、溜まったトークンの分（最大b）を一度に通せる。単純に一定の間隔でしか通さない方式と比べ、平均を抑えたまま短い集中を吸収できる点が特徴である。

![[Token Bucket.excalidraw]]

制御の性質はrとbの二つの値で決まる。rは[[Bandwidth|帯域]]や[[IOPS]]の上限であり、bは許すバーストの大きさである。bを小さくすると流れは平らになるが、短い集中でも待たされるようになる。

## どこで出てくるか
[[Linux Kernel|Linux]]では、`tc` のキューイングの方式の一つであるTBF（Token Bucket Filter）が、ネットワークインタフェースの送信の速さを `rate`（速さ）、`burst`（バケットの大きさ）、`limit` または `latency`（待たせる量の上限）で制限する。[[Lustre]]のサーバは、到着したRPCの処理の順序を決めるNRS（Network Request Scheduler）の方式の一つとしてTBFを持ち、クライアントのNID、JobID、UIDなどごとに、1秒あたりに処理するRPCの数を制限できる。多数のジョブが一つの[[Parallel File System|並列ファイルシステム]]を共有する環境で、特定のジョブのI/Oが他のジョブの性能を下げることを防ぐ、サービスの品質（QoS）の制御として用いられる。性能の測定で、最初だけ速くその後に一定の速さへ落ちる結果が得られた場合、途中にトークンバケットのような制限がある可能性を疑う必要がある。

## 関係
- 関連: [[Bandwidth]], [[IOPS]], [[Lustre]]

## 出典
- [tc-tbf(8) - Linux manual page](https://man7.org/linux/man-pages/man8/tc-tbf.8.html)
- [Lustre NRS Configuration (Lustre Wiki)](https://wiki.lustre.org/Lustre_NRS_Configuration)
