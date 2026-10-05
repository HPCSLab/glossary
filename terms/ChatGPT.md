---
aliases: [chatgpt, OpenAI, GPT, Generative Pre-trained Transformer, RLHF, Hallucination, ハルシネーション]
tags: [term]
maps: ["[[AI Tools]]"]
status: draft
updated: 2026-10-06
---
# ChatGPT

> OpenAIが開発した対話型の生成AIであり、利用者の指示に応じて、文章、音声、画像などを生成する。

## 概要
ChatGPTは、2022年11月30日に一般に公開され、公開から5日で100万人、2か月で月間1億人の利用者に達し、当時最も速く普及したインターネットのアプリケーションとなった。基盤には、OpenAIのGPT（Generative Pre-trained Transformer）と呼ばれる[[LLM|大規模言語モデル]]の系列が用いられている。学習では、人が模範となる応答を示す教師あり学習に加えて、人が応答の良し悪しを順位付けした結果を用いて出力を改善する、人間のフィードバックによる強化学習（RLHF）が用いられた。

## どこで出てくるか
ChatGPTは、LLMを用いた対話型AIを広く社会に普及させた製品であり、[[Claude]]などとともに、文書の作成、要約、翻訳、プログラミングの補助などに用いられる。OpenAIのコーディングエージェントである[[Codex]]も、ChatGPTのアプリケーションから利用できる。

一方で、既知の弱点もある。事実と異なる内容をもっともらしく提示するハルシネーション、利用者が誤っていても同調してしまう傾向、学習データに由来する偏りなどである。研究で用いる際には、生成された内容、特に文献の引用、数値、仕様についての記述を、そのまま信じずに元の資料で確かめる必要がある。

## 関係
- 上位概念: [[LLM]]
- 対比: [[Claude]]（Anthropicの対話型AI）
- 関連: [[Codex]], [[Claude Code]]

## 出典
- [ChatGPT - Wikipedia](https://en.wikipedia.org/wiki/ChatGPT)
