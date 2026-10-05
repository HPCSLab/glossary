---
aliases: [Retrieval-Augmented Generation, 検索拡張生成, 検索拡張型生成, RAG-Sequence, RAG-Token, Retriever, リトリーバ, DPR, Dense Passage Retriever, Chunk, チャンク分割]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-06
---
# RAG（Retrieval-Augmented Generation、検索拡張生成）

> 言語モデルが回答を生成する際に、外部の文書の集まりから質問に関係する文書を検索し、それを手がかりとして与えることで、モデルの重みに含まれない知識を利用できるようにする手法である。

## 概要
RAGは、Lewisら（Facebook AI Researchなど）が、2020年のNeurIPSで提案した。事前学習した[[LLM|言語モデル]]は、多くの知識を重み（パラメータ）の中に蓄えるが、その知識を後から更新することや、回答の根拠を示すことは難しく、事実と異なる内容（ハルシネーション）を生成することもある。RAGは、重みに蓄えた知識（パラメトリックな記憶）と、検索で引ける外部の文書（ノンパラメトリックな記憶）を組み合わせる。

原論文のRAGは二つの部品からなる。一つは検索器（retriever）であり、質問を[[Embedding|埋め込み]]のベクトルに変換し、あらかじめ文書の埋め込みから作っておいた索引から、内積の大きい上位k件の文書を探す。もう一つは生成器であり、質問と検索した文書を入力として回答を生成する。論文では、Wikipediaの記事を100語ずつの断片に分けた約2,100万件の文書の埋め込みを、FaissのHNSWの索引に格納した。生成の全体で同じ文書を用いるRAG-Sequenceと、トークンごとに異なる文書を用いうるRAG-Tokenの二つの形を比べている。外部の文書の索引を新しいものに差し替えるだけで、モデルの知識を更新できることも示した。

## どこで出てくるか
現在では、手元の文書（論文、マニュアル、社内の資料など）を断片に分けて埋め込みを計算し、[[Vector Database|ベクトルDB]]に格納しておき、質問に近い断片を検索して言語モデルの入力に加える、という形で用いられている。ベクトルDBの主な用途の一つでもある。

システムの観点では、検索の索引の大きさと検索の速さが問題となる。原論文では、Wikipedia全体の文書のベクトルをCPUのメモリに置き、約100GBを要した。Faissの圧縮の機能を用いると36GBに減った。文書の数が増えると、索引をメモリに収めるか、[[SSD]]に置くかの選択が必要となる。また、検索した文書の分だけ言語モデルの入力が長くなるため、推論の[[KV Cache|KVキャッシュ]]の大きさや処理の時間も増える。

## 関係
- 前提: [[LLM]], [[Embedding]]
- 使う / 使われる: [[Vector Database]]
- 関連: [[KV Cache]], [[vLLM]], [[Hugging Face]]

## 出典
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Lewis et al., NeurIPS 2020) - arXiv](https://arxiv.org/abs/2005.11401)
- [What is Milvus - Milvus documentation](https://milvus.io/docs/overview.md)（ベクトルDBの用途としてのRAG）
