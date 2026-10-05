---
aliases: [リングバッファ, Circular Buffer, 循環バッファ, リングキュー, Ring Queue, SPSC Queue, kfifo]
tags: [term]
maps: ["[[Data Structures]]"]
status: draft
updated: 2026-10-06
---
# Ring Buffer（リングバッファ）

> 固定長の配列の末尾と先頭をつなげて環状に扱い、書き込む位置と読み出す位置の二つの添字を進めていくことで、データを先入れ先出しで受け渡すデータ構造である。

## 概要
リングバッファは、固定の大きさの配列と、二つの添字からなる。生産者（データを書き込む側）は、書き込み位置（head）にデータを置いてheadを進める。消費者（データを読み出す側）は、読み出し位置（tail）からデータを取り出してtailを進める。添字が配列の末尾に達すると先頭に戻るため、配列を環状に使い回せ、データの移動やメモリの確保を伴わずに、継続的にデータを受け渡せる。

headとtailが等しいとき、バッファは空である。一方、バッファを完全に満たすとheadとtailが再び等しくなり、空と区別できなくなる。そのため、一つの要素を常に空けておき、headがtailの一つ手前に来た時点を満杯とみなすか、要素数を別に数えるのが一般的である。配列の大きさを2の冪にしておくと、添字を末尾で先頭に戻す計算を、除算の代わりにビットごとの論理積で行えるため、高速である。

生産者と消費者がそれぞれ一つだけの場合（SPSC）、headは生産者だけが、tailは消費者だけが書き換えるため、ロックを用いずに両者が同時に動作できる。ただし、データを書き込んでからheadを更新する順序が、消費者から見て入れ替わらないようにするため、メモリバリアが必要となる。Linuxカーネルでは、これらの操作を補助するマクロ（`CIRC_CNT`、`CIRC_SPACE` など）が提供されている。

## どこで出てくるか
リングバッファは、二者の間で、片方を待たせずに大量の要求やデータを受け渡す場面で至るところに現れる。[[io_uring]]の投入キューと完了キュー、[[NVMe]]のコマンドの投入キューと完了キューは、いずれもリングバッファの構造を持つ。[[perf]]のリングバッファでは、カーネルが書き込み位置（`data_head`）を進め、利用者が読み終えた位置（`data_tail`）を書き戻す。BPFのリングバッファは、複数のCPU上のBPFプログラムが書き込み、一つの利用者が読み出す形（MPSC）をとる。これらに共通するのは、生産者と消費者が別のCPU、あるいはCPUと装置であり、互いの進み具合を添字の比較だけで知ることができるという点である。性能の面では、バッファが満杯になったときに生産者を待たせるか、データを捨てるかの方針と、バッファの大きさが、スループットと[[Latency|レイテンシ]]に影響する。

## 関係
- 使う / 使われる: [[io_uring]], [[NVMe]], [[perf]], [[BPF]]（リングバッファを使う）
- 関連: [[Little's Law]], [[Latency]]

## 出典
- [Circular Buffers - The Linux Kernel documentation](https://docs.kernel.org/core-api/circular-buffers.html)
- [io_uring(7) - Linux manual page](https://man7.org/linux/man-pages/man7/io_uring.7.html)
- [NVM Express Revision 1.0e](https://nvmexpress.org/wp-content/uploads/2013/04/NVM_10e_specification.pdf)
- [perf_event_open(2) - Linux manual page](https://man7.org/linux/man-pages/man2/perf_event_open.2.html)
- [BPF ring buffer - The Linux Kernel documentation](https://docs.kernel.org/bpf/ringbuf.html)
