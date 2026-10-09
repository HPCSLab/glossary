---
aliases: [Cerebras Systems, セレブラス, WSE, Wafer-Scale Engine, WSE-3, WSE-3 Turbo, CS-3, CS-4, Wafer-Scale Integration, ウェハスケール]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# Cerebras（WSE）

> 一枚のシリコンウェハ全体を一つのプロセッサとして作るWafer-Scale Engine（WSE）と、それを搭載したAI用の計算機を開発する米国の企業、およびその製品である。

## 概要
通常のプロセッサは、一枚のウェハから多数のチップを切り出して作り、大きな計算は多数の[[GPU]]をつないで行う。Cerebrasは、ウェハを切り分けずに一つのチップとして用いる。2024年に発表された第3世代のWSE-3は、TSMCの5nmの製造技術による4兆個のトランジスタ、90万個のAI向けのコア、44GBのオンチップのSRAMを持ち、AIの演算のピーク性能は125PFLOPSである。WSE-3を搭載した計算機がCS-3であり、最大2048台を一つのクラスタとして接続でき、1.5TBから1.2PBの外部メモリを組み合わせて、最大24兆パラメータのモデルを学習できるとしている。2026年8月には、演算性能とメモリの帯域を高めたWSE-3 Turboを3枚搭載したラック規模の計算機CS-4が発表された。WSE-3 Turboの1枚あたりの性能は250PFLOPS（疎なFP16）、SRAMの帯域は43.2PB/sである。

GPUとの最大の違いはメモリの構成にある。GPUは、演算器の外に置いた[[HBM]]にモデルの重みを置き、計算のたびにそこから読み出す。WSEは、演算器と同じウェハの上に分散して置いたSRAMに重みを置くため、メモリの[[Bandwidth|帯域]]が桁違いに大きい。WSE-3のSRAMの帯域は21PB/sとされ、NVIDIA H200のHBM3eの4.8TB/sの数千倍に当たる。一方、SRAMの容量は44GBにとどまり、HBMを持つGPUよりはるかに小さい。

## どこで出てくるか
[[LLM]]の推論の高速化の文脈で現れる。LLMのデコードの段階は、トークンを一つ生成するたびに全ての重みを読み出すため、メモリの帯域で律速される。Cerebrasは、全ての重みをオンチップのSRAMに置くことでこの制約を緩め、Llama 4 Scoutで毎秒2,600トークン以上の出力速度を、第三者の計測（Artificial Analysis）で示したとしている。

ただし、SRAMの容量の小ささが制約となる。例えば、16ビットの重みで約140GBを要するLlama 3.1 70Bは一台のCS-3に収まらず、80層を4台のCS-3に分けて置く（パイプライン並列）。長い文脈の[[KV Cache|KVキャッシュ]]もSRAMの容量を圧迫する。性能の比較を読む際には、トークンの生成速度（[[TTFT]]や1要求あたりの毎秒のトークン数）が、メモリの容量と帯域のどちらの制約の下で得られた値なのか、何台の計算機を用いたのかを確かめる必要がある。示されている数値の多くは、Cerebras自身の発表である。

## 関係
- 対比: [[GPU]]（HBMに重みを置き、多数のチップをつないで大きなモデルを扱う）, [[DGX Spark]]（容量は大きいが帯域の小さい統合メモリを持つ）
- 使う / 使われる: [[LLM]]
- 関連: [[HBM]], [[Bandwidth]], [[KV Cache]], [[Roofline Model]]

## 出典
- [Cerebras Systems Unveils World's Fastest AI Chip with Whopping 4 Trillion Transistors - Cerebras](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine)
- [Cerebras Intros Faster WSE-3 Turbo Processor and First Rack-Scale CS-4 System - ServeTheHome](https://www.servethehome.com/cerebras-intros-faster-wse-3-turbo-processor-and-first-rack-scale-cs-4-system/)
- [Cerebras Launches World's Fastest Inference for Meta Llama 4 - Cerebras](https://www.cerebras.ai/press-release/llama4PR)
- [Cerebras gives waferscale chips inferencing twist - The Register](https://www.theregister.com/2024/08/27/cerebras_ai_inference/)
