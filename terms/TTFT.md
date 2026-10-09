---
aliases: [Time to First Token, 最初のトークンまでの時間, TPOT, Time per Output Token, ITL, Inter-token Latency, トークン間レイテンシ, E2E Latency, End-to-end Latency, TPS, Tokens per Second]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-09
---
# TTFT（Time to First Token）

> [[LLM]]の推論で、要求を送ってから、応答の最初のトークンを受け取るまでの時間であり、利用者が応答の開始を待つ時間を表す指標である。

## 概要
TTFTには、要求が待ち行列で待つ時間、入力のプロンプト全体を処理するプリフィル（prefill）の時間、ネットワークの[[Latency|遅延]]が含まれる。プリフィルでは、生成を始める前に入力の全体を用いて[[KV Cache|KVキャッシュ]]を作るため、プロンプトが長いほどTTFTは長くなる。

LLMの推論の性能は、TTFTのほかに、次の指標と組み合わせて評価する。最初のトークンの後、続くトークンが届く間隔の平均を、トークン間のレイテンシ（ITL、またはTPOT）と呼ぶ。これはデコード（decode）段階の速さを表す。要求を送ってから応答の全体を受け取るまでの時間（end-to-endのレイテンシ）は、TTFTと生成の時間の和である。また、同時に処理している全ての要求の、単位時間あたりの出力のトークン数（TPS）がシステムのスループットであり、同時の要求の数を増やすと、GPUが飽和するまで大きくなる。

## どこで出てくるか
LLMの推論システム（[[vLLM]]など）の評価では、TTFT、ITL、スループットを区別して測る。TTFTは待ち行列で待つ時間を含むため、同時の要求の数を増やしてスループットを上げると、その影響を受けうる。プリフィルは演算性能で、デコードはメモリの[[Bandwidth|バンド幅]]で律速されやすいため、TTFTとITLは異なるハードウェアの性質に影響される（[[LLM]]を参照）。[[RAG]]のように入力が長くなる使い方では、TTFTが特に長くなる。

## 関係
- 上位概念: [[Latency]]
- 前提: [[LLM]], [[KV Cache]]
- 関連: [[vLLM]], [[Bandwidth]], [[RAG]]

## 出典
- [LLM Inference Benchmarking: Metrics - NVIDIA NIM Documentation](https://docs.nvidia.com/nim/benchmarking/llm/latest/metrics.html)
