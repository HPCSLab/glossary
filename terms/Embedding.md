---
aliases: [埋め込み, 埋め込み表現, エンベディング, Embedding Layer, 埋め込み層, Embedding Table, 埋め込みテーブル, Embedding Vector, 埋め込みベクトル, DLRM]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-06
---
# Embedding（埋め込み）

> 単語や商品のような離散的な対象を、意味の近いものほど近くに位置するような、低い次元の密な実数のベクトルで表したものである。

## 概要
数万種類の単語を区別するのに、該当する位置だけが1の長いベクトル（one-hot表現）を用いると、入力が巨大で疎になり、ニューラルネットワークの重みも膨大になる。埋め込みは、各対象を、より低い次元の密なベクトルに対応させる。この対応は、モデルの学習の中で埋め込み層として学習され、似た性質の対象ほど、ベクトルの空間の中で近くに位置するようになる。ベクトルの近さは、内積やコサイン類似度、ユークリッド距離で測る。

実装の上では、埋め込み層は、対象の番号を行の番号とする大きな表（埋め込みテーブル）であり、番号を与えるとその行のベクトルを取り出す。[[LLM]]の基になったTransformerも、入力と出力のトークンを、学習された埋め込みによって一定の次元のベクトルに変換している。

## どこで出てくるか
文章を一つのベクトルに変換する埋め込みのモデルを用いると、意味の近い文書を、ベクトルの近さで探せる（ベクトル検索）。ベクトルを格納して検索する専用のデータベースを[[Vector Database|ベクトルDB]]と呼ぶ。[[RAG|検索拡張生成（RAG）]]は、質問に関係する文書を、文書の埋め込みのベクトルの索引から検索し、それを言語モデルの入力に加えて回答を生成する手法である（Lewisら、NeurIPS 2020）。大量のベクトルから近いものを高速に探すために、類似検索のライブラリが用いられる。例えば、MetaのFaissは、メモリに収まらない規模のベクトルの集合も扱え、一部のアルゴリズムは[[GPU]]で動作する。

推薦システムでは、利用者や商品などのカテゴリの値ごとに埋め込みテーブルを持つため、テーブルが巨大になる。Metaの推薦モデルDLRMの論文は、メモリの制約を緩和するために、埋め込みテーブルを複数の装置に分けて持つモデル並列と、全結合層のデータ並列を組み合わせる並列化の方式を示している。

## 関係
- 使う / 使われる: [[LLM]], [[GPU]]
- 関連: [[Vector Database]], [[RAG]], [[KV Cache]], [[Hugging Face]]

## 出典
- [Embeddings - Machine Learning Crash Course - Google for Developers](https://developers.google.com/machine-learning/crash-course/embeddings)
- [Attention Is All You Need (Vaswani et al., 2017) - arXiv](https://arxiv.org/abs/1706.03762)（3.4節 Embeddings and Softmax）
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Lewis et al., NeurIPS 2020) - arXiv](https://arxiv.org/abs/2005.11401)
- [facebookresearch/faiss - GitHub](https://github.com/facebookresearch/faiss)
- [Deep Learning Recommendation Model for Personalization and Recommendation Systems (Naumov et al., 2019) - arXiv](https://arxiv.org/abs/1906.00091)
