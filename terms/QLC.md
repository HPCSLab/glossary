---
aliases: [Quad-Level Cell, クアッドレベルセル, QLC NAND, QLC SSD, Indirection Unit, IU]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# QLC（Quad-Level Cell）

> NANDフラッシュメモリの一つのセルに4ビットを記録する方式であり、容量あたりの価格を下げる代わりに、性能と耐久性が低い。

## 概要
[[SSD]]の記憶媒体であるNANDフラッシュは、セルに蓄えた電荷の量（しきい値電圧）の違いで情報を表す。セルあたりのビット数が多いほど、同じ数のセルで多くのデータを記録できる。1ビットを記録するSLCは2つの状態、2ビットのMLCは4つ、3ビットのTLCは8つ、4ビットのQLCは16の状態を区別する。区別すべき状態が多いほど、性能と信頼性は下がる傾向がある。例えば、読み出しでは同じデータを複数のしきい値で読み直す必要が生じることがあり、書き込みと消去を繰り返せる回数も減る。QLCの書き換え回数の上限は、およそ1,000回以下とされ、SLCの数万回やTLCの数千回より少ない。QLCを用いたSSDは2018年に一般向けの製品が登場した。

## どこで出てくるか
QLCのSSDは、大容量で安価な代わりに、書き込みの性能と寿命に制約がある。データセンター向けのQLCのSSDでは、容量を大きくするために、[[SSD|FTL]]が論理アドレスと物理位置を対応付ける単位（indirection unit、IU）を、通常の4KiBより大きい16KiBや64KiBにしたものがある。対応表が小さくなり、SSDに載せる[[DRAM]]を減らせるためである。この場合、IUより小さい、あるいはIUの境界にそろっていない書き込みは、SSDの内部で読み出し・変更・書き戻しを要し、書き込み増幅を増やして性能と寿命を損なう。性能評価やシステムの設計では、書き込みの大きさと位置をIUにそろえることが重要となり、小さなランダムな書き込みを高速な別のデバイスで受け止め、大きな順次の書き込みにまとめてからQLCに書く構成も提案されている。

## 関係
- 上位概念: [[SSD]]

## 出典
- [Multi-level cell - Wikipedia](https://en.wikipedia.org/wiki/Multi-level_cell)
- [Platform Optimization for Performance and Endurance (QLC, CSAL) - Solidigm](https://www.solidigm.com/products/technology/platform-optimization-for-performance-and-endurance-qlc-csal.html)
