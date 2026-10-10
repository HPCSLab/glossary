---
aliases: [SLCキャッシュ, pSLC, Pseudo-SLC, 疑似SLC, SLC Caching, Static SLC Cache, Dynamic SLC Cache]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# SLC Cache（SLCキャッシュ）

> TLCや[[QLC]]のSSDの一部のセルを、1セルあたり1ビットだけを記録するSLCのように使って書き込みを速くする仕組みである。

## 概要
セルあたり3ビットのTLCや4ビットのQLCは、1ビットのSLCより書き込みが遅い。そこで[[SSD]]は、フラッシュの一部を1ビットだけを記録する方式で使い、そこを書き込みの受け皿とする。ホストからの書き込みはまずこのSLCキャッシュに書かれ、後でTLCやQLCの領域に移される。移すことでキャッシュが空き、再び高速に書き込めるようになる。このように多値のセルをSLCとして使うことは、疑似SLC（pSLC）とも呼ばれる。

キャッシュの大きさを固定する静的なSLCキャッシュと、使用状況に応じて変える動的なSLCキャッシュがある。静的なものは大きさが保証されるが、その領域に書き換えが集中して消耗しやすい。動的なものは消耗を全体に分散できるが、大きさが保証されない。動的なキャッシュの大きさは空き容量によって変わるため、空きの多い大容量のSSDほど、多くのデータを高速に書き込める。

## どこで出てくるか
SSDに大量のデータを書き続けると、ある量を超えたところで書き込みの速度が急に落ちることがある。これは、SLCキャッシュが一杯になり、書き込みが遅い本来の領域に直接行われるようになるためである。[[fio]]などで性能を測るときは、短時間の測定だけで判断せず、十分な量を書き込んで速度の変化を確かめる。空き容量によってキャッシュの大きさが変わるため、測定の前のSSDの使用率も結果に影響する。

## 関係
- 上位概念: [[SSD]]
- 対比: [[QLC]]（多値のセルの本来の記録方式）
- 関連: [[FTL]], [[fio]]

## 出典
- [Maximizing SSD Performance with SLC Cache - Advantech](https://www.advantech.com/en/resources/news/maximizing-ssd-performance-with-slc-cache)
- [Multi-level cell - Wikipedia](https://en.wikipedia.org/wiki/Multi-level_cell)
