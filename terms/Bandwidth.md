---
aliases: [バンド幅, 帯域幅, 帯域, Throughput, スループット, Memory Bandwidth, メモリバンド幅]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Storage]]", "[[Network]]"]
status: draft
updated: 2026-10-10
---
# Bandwidth（バンド幅）

> 単位時間あたりに転送できるデータの量であり、データ転送の「太さ」を表す性能指標である。

## 概要
バンド幅は、通信路、メモリ、記憶装置などが単位時間あたりに運べるデータ量を表し、ネットワークではビット毎秒（bit/s）、メモリやストレージではバイト毎秒（B/s）で表すことが多い。一つのデータが届くまでの「時間」を表す[[Latency|レイテンシ]]とは独立した指標であり、両者を合わせて転送性能を特徴付ける。大きなデータの転送時間はバンド幅で、小さなデータの転送時間はレイテンシで、それぞれほぼ決まる。

カタログに記載される値は、ハードウェアが理論上達成しうる最大値（ピーク性能）である。実際にアプリケーションが得られる値は実効バンド幅、あるいはスループットと呼ばれ、プロトコルのオーバーヘッド、[[Access Pattern|アクセスパターン]]、競合などにより、ピークより低くなる。実効バンド幅は、メモリについてはSTREAM、MPI通信については `osu_bw`、ストレージについては[[IOR]]や[[fio]]などのベンチマークで測定する。

高いバンド幅を実際に引き出すには、転送中のデータを常に十分な量だけ確保しておく必要がある。[[Little's Law|リトルの法則]]によれば、達成されるバンド幅は「同時に転送中のデータ量 ÷ レイテンシ」で決まる。そのため、レイテンシが大きい経路ほど、多数の要求を同時に発行しなければバンド幅を使い切れない。メモリアクセスにおけるプリフェッチや複数スレッドによる並列アクセス、SSDに対する深いキューの使用、MPIにおける複数のメッセージの連続送信は、いずれもこの原理に基づく。

## どこで出てくるか
HPCでは、多くのアプリケーションの性能が演算性能ではなくメモリバンド幅で律速される。演算量に対してメモリアクセス量が多いプログラムでは、プロセッサのピーク演算性能をいくら高めても実行時間は短縮されない。[[Parallel File System|並列ファイルシステム]]やネットワークの性能を語る際にも、総バンド幅が主要な指標となる。数値を比較する際には、単位がビットかバイトか（Gb/s と GB/s では8倍異なる）、接頭辞が10進か2進か（GB と GiB）、片方向か双方向の合計か、ピーク値か実測値かを確認する必要がある。

## 関係
- 対比: [[Latency]]（一つのデータが届くまでの時間）
- 関連: [[Little's Law]], [[MPI]], [[Parallel File System]], [[Roofline Model]]

## 出典
- [Bandwidth (computing) - Wikipedia](https://en.wikipedia.org/wiki/Bandwidth_(computing))
- [STREAM: Sustainable Memory Bandwidth in High Performance Computers](https://www.cs.virginia.edu/stream/)
- [OSU Micro-Benchmarks - MVAPICH](https://mvapich.cse.ohio-state.edu/benchmarks/)
