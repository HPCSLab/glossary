---
aliases: [Dynamic Random-Access Memory, ダイナミックRAM, 動的RAM, Main Memory, 主記憶, メインメモリ, DDR, DDR4, DDR5, LPDDR, LPDDR5x, GDDR, SDRAM, Refresh, リフレッシュ, DIMM]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# DRAM（Dynamic Random-Access Memory）

> 一つのビットを1個のトランジスタと1個のコンデンサに蓄えた電荷で表す揮発性の半導体メモリであり、計算機の主記憶に用いられる。

## 概要
DRAMのセルは、1個のトランジスタと1個のコンデンサからなる。コンデンサの電荷は時間とともに漏れて失われるため、DRAMは定期的に内容を読んで書き直す必要がある（リフレッシュ）。JEDECの規格では、各行をおおむね64ミリ秒以内にリフレッシュすることが求められる。これが「動的（dynamic）」の名前の由来である。電源を切ると内容は失われる。

1ビットあたりの部品が少ないため、6個のトランジスタを用いる[[SRAM]]に比べて密度が高く、容量あたりの価格が安い。一方、リフレッシュの回路と複雑な制御を要し、アクセスはSRAMより遅い。この速さと容量の兼ね合いから、DRAMは主記憶に、SRAMはCPUの[[Cache|キャッシュ]]に用いられる。

DRAMには用途に応じた規格の系統がある。サーバやパソコンの主記憶にはDIMMに載せたDDR4やDDR5、モバイル機器や一部の小型の計算機には省電力のLPDDR、グラフィックスのカードにはGDDRが用いられる。DRAMのチップを積み重ねてプロセッサの近くに置き、幅の広いインタフェースで接続したものが[[HBM]]である。

## どこで出てくるか
計算機の性能を考える際、DRAMは記憶階層の中間に位置する。目安として、DRAMへのアクセスの[[Latency|レイテンシ]]は約100ナノ秒であり、CPUのキャッシュより桁違いに遅く、[[SSD]]より桁違いに速い。多くのHPCのアプリケーションは、DRAMの[[Bandwidth|帯域]]で性能が律速される（[[Roofline Model|ルーフラインモデル]]を参照）。

同じDRAMでも、規格によって帯域は大きく異なる。例えば、データセンター向けの[[GPU]]がHBMで数TB/sの帯域を得るのに対し、LPDDR5xを用いる[[DGX Spark]]の帯域は273GB/sである。また、ファイルのデータは[[Page Cache|ページキャッシュ]]としてDRAMに置かれ、[[Intel Optane Persistent Memory|永続メモリ]]や[[CXL]]で接続したメモリは、DRAMとの容量・速度・価格の違いによって記憶階層に位置付けられる。

## 関係
- 対比: [[SRAM]]（速いが密度が低く、リフレッシュを要しない）
- 使う / 使われる: [[HBM]]（DRAMを積層したもの）, [[Virtual Memory]], [[Page Cache]]
- 関連: [[Latency]], [[Bandwidth]], [[CXL]], [[Intel Optane Persistent Memory]], [[DGX Spark]]

## 出典
- [Dynamic random-access memory - Wikipedia](https://en.wikipedia.org/wiki/Dynamic_random-access_memory)
- [Static random-access memory - Wikipedia](https://en.wikipedia.org/wiki/Static_random-access_memory)
