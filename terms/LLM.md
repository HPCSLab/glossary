---
aliases: [Large Language Model, 大規模言語モデル, Transformer, トランスフォーマー, Attention, アテンション, Token, トークン, Prefill, Decode, 推論, Inference]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-06
---
# LLM（大規模言語モデル）

> 膨大な量のテキストで学習した、数十億から数千億以上のパラメータを持つ言語モデルであり、与えられた文脈に続くトークンを一つずつ予測することで文章を生成する。

## 概要
現在のLLMの多くは、2017年にVaswaniらが "Attention Is All You Need" で提案したTransformerを基盤とする。Transformerは、再帰や畳み込みを用いず、アテンション機構のみによって、系列中の各要素が他の要素をどれだけ参照するかを計算する。テキストはトークンと呼ばれる単位（単語や単語の断片）に分割され、モデルは、それまでのトークン列から次のトークンの確率分布を計算する。

文章の生成（推論）は、自己回帰的に行われる。すなわち、予測したトークンを入力の末尾に加えて、さらに次のトークンを予測することを繰り返す。この推論は、性質の異なる二つの段階からなる。プリフィル（prefill）段階では、入力として与えられたプロンプト全体を一度に処理する。多数のトークンをまとめて計算できるため、演算性能で律速される。デコード（decode）段階では、トークンを一つずつ生成する。各段階で、モデルの全パラメータと過去のトークンの情報をメモリから読み出す必要がある一方、計算量は少ないため、メモリの[[Bandwidth|バンド幅]]で律速される。過去のトークンについてのアテンションの計算結果の一部を保持して再計算を省くのが[[KV Cache]]である。

## どこで出てくるか
システムの研究の観点では、LLMは、計算資源、メモリ、通信、ストレージのすべてに極端な要求を課す対象である。学習では、多数の[[GPU]]にモデルとデータを分割して並列に計算し、勾配の集約に[[Collective Communication|集団通信]]を用いる。チェックポイントの保存は、[[Parallel File System|並列ファイルシステム]]への大規模なI/Oとなる。推論では、GPUのメモリの容量とバンド幅、多数の要求を同時に処理するためのバッチ処理とメモリ管理が、性能とコストを左右する。[[vLLM]]などの推論システムは、この問題に取り組んでいる。性能の議論では、最初のトークンが出るまでの時間（Time to First Token）と、トークンあたりの生成時間、全体のスループットを区別して評価する。

## 関係
- 使う / 使われる: [[GPU]], [[KV Cache]], [[vLLM]]
- 関連: [[Collective Communication]], [[Bandwidth]], [[Latency]], [[CUDA]]

## 出典
- [Attention Is All You Need (Vaswani et al., 2017) - arXiv](https://arxiv.org/abs/1706.03762)
- [Caching - Hugging Face Transformers documentation](https://huggingface.co/docs/transformers/main/en/cache_explanation)
