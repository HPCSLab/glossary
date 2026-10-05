---
aliases: [ルーフラインモデル, Roofline, ルーフライン, Arithmetic Intensity, 演算強度, Operational Intensity, Ridge Point, Memory-bound, メモリバウンド, Compute-bound, 演算律速, メモリ律速]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# Roofline Model（ルーフラインモデル）

> 計算機のピークの演算性能とメモリの[[Bandwidth|バンド幅]]から、ある計算が到達できる性能の上限を、演算強度の関数として見積もる性能モデルである。

## 概要
ルーフラインモデルは、Williams、Waterman、Pattersonが2009年に Communications of the ACM で提案した。中心となる指標は演算強度であり、計算が行う浮動小数点演算の回数を、メモリとの間で移動するデータの量（バイト）で割ったもの（FLOP/byte）である。

ピークの演算性能を π、ピークのメモリのバンド幅を β、演算強度を I とすると、到達できる性能 P の上限は P = min(π, β × I) で与えられる。演算強度を横軸、性能を縦軸に（通常は両対数で）描くと、上限は、傾きβの斜めの線と、高さπの水平な線からなる屋根の形になる。二つの線が交わる点（リッジポイント、I = π/β）より演算強度が小さい計算は、メモリのバンド幅で性能が制限される（メモリ律速）。大きい計算は、演算性能で制限される（演算律速）。

## どこで出てくるか
プログラムの最適化では、まず対象の計算がどちらの領域にあるかを確かめる。メモリ律速の計算の性能を上げるには、演算の速さではなく、データの再利用によって演算強度を高めるか、メモリの転送量を減らす必要がある。[[GPU]]や[[HBM]]を持つ計算機は演算性能もバンド幅も高いが、その比は計算機ごとに異なるため、同じ計算でも律速の要因が変わりうる。演算回数とメモリの転送量は、[[perf]]などでハードウェアの性能カウンタから測定できる。

## 関係
- 前提: [[Bandwidth]]
- 関連: [[GPU]], [[HBM]], [[perf]], [[Latency]]

## 出典
- [Roofline model - Wikipedia](https://en.wikipedia.org/wiki/Roofline_model)
- [Roofline: an insightful visual performance model for multicore architectures (Williams, Waterman, Patterson, CACM 2009)](https://doi.org/10.1145/1498765.1498785)
