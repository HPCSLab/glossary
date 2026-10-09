---
aliases: [Static Random-Access Memory, スタティックRAM, 静的RAM, 6T Cell, On-chip Memory, オンチップメモリ]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# SRAM（Static Random-Access Memory）

> 一つのビットを、互いに出力を入力につないだ二つのインバータで保持する、高速だが容量あたりの面積の大きい揮発性の半導体メモリである。

## 概要
典型的なSRAMのセルは、6個のトランジスタ（6T）からなる。4個が互いにつながった二つのインバータを作ってビットを保持し、残りの2個が読み書きの際にセルを信号線につなぐ。電源がある限り値を保持し続けるため、[[DRAM]]のような定期的な書き直し（リフレッシュ）を必要としない。電源を切ると内容は失われる（揮発性）。

SRAMはDRAMより速いが、1ビットあたりのトランジスタの数が多く、シリコンの面積を多く使うため、容量あたりの価格が高く、密度が低い。そのため、大容量の主記憶には用いられず、プロセッサのチップの中に置く小さく速い記憶に用いられる。

## どこで出てくるか
CPUのレジスタと[[Cache|キャッシュ]]、[[GPU]]のSMごとの[[CUDA|共有メモリ]]やキャッシュは、いずれもチップ上のSRAMである。計算機の記憶階層は、上から、小さく速いSRAM、大きく遅いDRAM（主記憶や[[HBM]]）、さらに大きく遅い[[SSD]]などの記憶装置と並ぶ。プログラムの最適化で「データをキャッシュに収める」「共有メモリを使う」というのは、SRAMの速さを活かすことを意味する。

AI用のプロセッサの設計では、SRAMの容量が論点となる。[[Cerebras]]のWSE-3は、ウェハ全体に44GBのSRAMを分散して置き、モデルの重みをDRAMではなくSRAMに置くことで、[[LLM]]の推論のメモリの[[Bandwidth|帯域]]の制約を緩めている。一方、SRAMの容量が小さいため、大きなモデルは複数の装置に分けて置く必要がある。

## 関係
- 対比: [[DRAM]]（1ビットを1個のトランジスタとコンデンサで保持し、密度が高いがリフレッシュを要する）
- 使う / 使われる: [[Cache]], [[GPU]], [[Cerebras]]
- 関連: [[HBM]], [[Bandwidth]], [[Latency]]

## 出典
- [Static random-access memory - Wikipedia](https://en.wikipedia.org/wiki/Static_random-access_memory)
- [Dynamic random-access memory - Wikipedia](https://en.wikipedia.org/wiki/Dynamic_random-access_memory)
