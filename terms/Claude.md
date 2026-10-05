---
aliases: [Claude Opus, Claude Sonnet, Claude Haiku, Claude Fable, Anthropic, claude.ai]
tags: [term]
maps: ["[[AI Tools]]"]
status: draft
updated: 2026-10-06
---
# Claude

> Anthropicが開発する大規模言語モデルの系列であり、対話のアプリケーション（claude.ai）やAPIを通じて利用できる。

## 概要
Claudeは、AnthropicがAPIや自社のアプリケーションを通じて提供する[[LLM|大規模言語モデル]]の系列である。Anthropicは、自らを「AIの安全性と研究の企業」と位置付け、信頼でき、解釈でき、制御できるAIシステムの構築を掲げる公益法人（Public Benefit Corporation）である。

Claudeは、性能、速度、価格の異なる複数のモデルからなる。2026年10月時点の公式の文書では、長期にわたる困難な推論と自律的な作業向けのFable、長時間の自律的なプログラミングと知的作業向けのOpus、速度と性能の均衡がとれたSonnet、最も高速なHaikuが並び、現行のFable 5.1、Opus 5.5、Sonnet 5.5は、100万トークンの文脈（コンテキストウィンドウ）を扱える。いずれのモデルも、テキストと画像の入力、テキストの出力、多言語、外部のツールの呼び出し（tool use）に対応している。モデルは版ごとに固定された識別子で指定され、古い版は予告されたうえで順に提供を終了する。

## どこで出てくるか
Claudeは、Webやアプリでの対話のほか、プログラムからAPIで呼び出したり、[[Claude Code]]のようなツールの中で用いたりする。研究では、文書の読解や要約、プログラムの作成と修正などに用いることができる。LLMは事実と異なる内容をもっともらしく生成することがある（ハルシネーション）ため、論文の内容、仕様、数値などは、必ず元の文献や公式の文書で確かめる必要がある。このノート群も、Claude Codeを通じてClaudeで下書きし、出典で確認したうえで公開している。モデルの一覧や性能は頻繁に更新されるため、利用時には公式の文書で最新の情報を確認する。

## 関係
- 上位概念: [[LLM]]
- 使う / 使われる: [[Claude Code]]（Claudeを用いるプログラミング支援ツール）
- 対比: [[ChatGPT]]（OpenAIの対話型AI）
- 関連: [[Codex]]

## 出典
- [Models overview - Claude Platform documentation](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Company - Anthropic](https://www.anthropic.com/company)
- [ChatGPT - Wikipedia](https://en.wikipedia.org/wiki/ChatGPT)（ハルシネーションについて）
