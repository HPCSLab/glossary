---
aliases: [vllm, PagedAttention, Continuous Batching, 連続バッチ処理, LLM Serving, LLMサービング]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# vLLM

> [[LLM]]の推論とサービングのためのオープンソースのライブラリであり、PagedAttentionによる[[KV Cache|KVキャッシュ]]の効率的な管理を特徴とする。

## 概要
vLLMは、カリフォルニア大学バークレー校のSky Computing Labで開発され、2023年の[[SOSP]]で論文 "Efficient Memory Management for Large Language Model Serving with PagedAttention"（Kwonら）として発表された。現在は多数の貢献者からなるコミュニティによって開発されている。

論文が指摘した問題は、KVキャッシュのメモリの無駄である。KVキャッシュは要求ごとに生成の進行とともに伸び、最終的な長さは事前に分からない。従来のシステムは、要求ごとに最大の長さ分の連続したメモリを確保していたため、使われない領域や断片化によって、[[GPU]]メモリの多くが無駄になり、同時に処理できる要求の数が制限されていた。PagedAttentionは、OSの[[Virtual Memory|仮想記憶]]におけるページングに倣って、KVキャッシュを固定長のブロックに分割し、論理的に連続したキャッシュを物理的には不連続なブロックに格納する。ブロックは必要になった時点で割り当てられ、対応表（ブロックテーブル）で管理される。これにより、メモリの無駄はほぼなくなり、同じプロンプトを共有する要求の間や、一つの要求から複数の候補を生成する場合に、ブロックを共有することもできる。論文は、同程度の[[Latency|レイテンシ]]で、既存のシステムに比べてスループットが2〜4倍に向上したと報告している。

このほかに、vLLMは、処理の終わった要求をすぐに抜き、新しい要求をすぐに加えて、バッチを常に満たし続ける連続バッチ処理、プレフィックスキャッシュ、各種の量子化、複数のGPUにモデルを分割するテンソル並列やパイプライン並列を提供する。OpenAI互換のAPIサーバとして起動でき、NVIDIAとAMDのGPUのほか、様々なハードウェアに対応している。

## どこで出てくるか
vLLMは、LLMを自前で動かす際の標準的な推論エンジンの一つであり、研究でLLMの推論の性能を評価する際の基準（ベースライン）としてもよく用いられる。KVキャッシュの退避、スケジューリング、メモリ管理などの推論システムの研究は、vLLMを改変して実装されることが多い。PagedAttentionは、OSの古典的な手法である仮想記憶とページングが、全く新しい問題領域で有効に働いた例であり、システム研究において既存の知識を応用することの価値をよく示している。

## 関係
- 上位概念: [[LLM]]
- 使う / 使われる: [[KV Cache]], [[GPU]], [[CUDA]]
- 関連: [[Virtual Memory]], [[Python]], [[Latency]]

## 出典
- [vLLM documentation](https://docs.vllm.ai/en/latest/)
- [Efficient Memory Management for Large Language Model Serving with PagedAttention (Kwon et al., SOSP 2023) - arXiv](https://arxiv.org/abs/2309.06180)
