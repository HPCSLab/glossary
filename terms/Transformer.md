---
aliases: [トランスフォーマー, トランスフォーマ, Attention Is All You Need, Vision Transformer, ViT, BERT, Positional Encoding, 位置エンコーディング]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# Transformer（トランスフォーマー）

> 系列の各要素が他のすべての要素をどれだけ参照するかをアテンションで計算することで、再帰や畳み込みを用いずに系列を処理するニューラルネットワークの構造である。現在の[[LLM]]の基盤である。

## 概要
Transformerは、2017年にVaswaniらがNIPSの論文 "Attention Is All You Need" で、機械翻訳のモデルとして提案した。それ以前の系列のモデルの主流であった再帰型ニューラルネットワーク（RNN）は、系列の要素を一つずつ順に処理するため、学習を並列化しにくかった。Transformerは再帰をなくし、系列の全要素の関係を[[Attention|アテンション]]で一度に計算するため、並列化しやすく、学習の時間を大きく短縮できた。

入力の各要素（トークン）は、まず[[Embedding|埋め込み]]のベクトルに変換される。アテンションでは、各要素から作ったクエリ（Q）、キー（K）、バリュー（V）のベクトルについて、クエリとキーの内積から重みを求め、バリューの重み付きの和を計算する。これを異なる射影で複数並べたものがマルチヘッドアテンションである。各層は、このアテンションと、要素ごとに同じ処理を適用する全結合のネットワーク（フィードフォワード層）からなり、それぞれに残差接続と層正規化を施す。この層を何段も積み重ねる。アテンション自体は要素の順序を区別しないため、位置の情報を位置エンコーディングとして入力に加える。元の論文のモデルは、入力を読むエンコーダと出力を生成するデコーダからなり、デコーダでは、まだ生成していない後ろの要素を参照しないようにマスクをかけて、自己回帰的な生成を可能にしている。

## どこで出てくるか
Transformerは言語以外にも広がっている。BERTはエンコーダの部分を用いて文章の表現を学習し、Vision Transformer（ViT）は画像を小さなパッチに分けて系列として扱い、[[Diffusion Model|拡散モデル]]のDiTも潜在空間のパッチにTransformerを用いる。[[Hugging Face]]のTransformersライブラリは、こうしたモデルを共通の方法で扱えるようにしている。

システムの観点では、アテンションの計算時間とメモリ量が系列の長さの2乗に比例することが、長い入力を扱う際の障害となる。FlashAttentionは、計算を小さなタイルに分けて[[GPU]]の[[HBM]]とチップ上の[[SRAM]]の間の読み書きを減らし、アテンションを高速化した。推論では、過去のトークンのキーとバリューを[[KV Cache]]に保持して再計算を省く。学習では、[[Megatron-LM]]のように、層の中の行列の積を複数のGPUに分割する並列化が用いられる。

## 関係
- 前提: [[Attention]], [[Embedding]]
- 使う / 使われる: [[LLM]], [[Diffusion Model]]（Transformerを用いるモデル）, [[KV Cache]], [[Megatron-LM]]
- 関連: [[GPU]], [[HBM]], [[Hugging Face]]

## 出典
- [Attention Is All You Need (arXiv:1706.03762)](https://arxiv.org/abs/1706.03762)
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (arXiv:1810.04805)](https://arxiv.org/abs/1810.04805)
- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (arXiv:2010.11929)](https://arxiv.org/abs/2010.11929)
- [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness (arXiv:2205.14135)](https://arxiv.org/abs/2205.14135)
