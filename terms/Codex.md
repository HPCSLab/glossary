---
aliases: [OpenAI Codex, Codex CLI, AGENTS.md]
tags: [term]
maps: ["[[AI Tools]]"]
status: draft
updated: 2026-10-06
---
# Codex

> OpenAIが提供する、プログラミングの作業を自律的に進めるコーディングエージェントである。同名で、かつてGitHub Copilotを支えたコード生成モデルも存在した。

## 概要
Codexという名前は、OpenAIの異なる二つのものを指す。一つは、2021年に公開された、GPT-3から派生したコード生成のための言語モデルであり、GitHub Copilotの基盤として用いられたが、2023年に提供を終了した。もう一つは、2025年4月に公開された現在のCodexであり、目標や課題を与えると、自ら文脈を集め、操作を行い、成果物を作るコーディングエージェントである。まず端末で動作するオープンソースのコマンドラインツールとして公開され、翌月にはクラウド上で動作するエージェントが加わった。現在は、ChatGPTのアプリケーション、Web、コマンドライン、IDEの拡張など、複数の場所から利用できる。

Codexは、コードの調査、機能の作成、変更の確認、不具合の修正などを行う。プロジェクトごとの指示は、`AGENTS.md` というファイルに記述する。

## どこで出てくるか
Codexは、[[Claude Code]]と並ぶ代表的なコーディングエージェントである。両者は、リポジトリを読み、ファイルを編集し、コマンドを実行して作業を進めるという点で共通しており、プロジェクトへの指示を、Codexは `AGENTS.md` に、Claude Codeは `CLAUDE.md` に書く。Claude Codeは `AGENTS.md` も読むことができるため、両方のツールを使うプロジェクトでは、共通の指示を `AGENTS.md` にまとめる方法もある。古い資料で「Codex」とある場合は、2021年のコード生成モデルを指していることがあるため、文脈に注意を要する。

## 関係
- 上位概念: [[LLM]]
- 対比: [[Claude Code]]（Anthropicのコーディングエージェント）
- 関連: [[ChatGPT]], [[Claude]]

## 出典
- [OpenAI Codex - Wikipedia](https://en.wikipedia.org/wiki/OpenAI_Codex)
- [Codex documentation - OpenAI](https://learn.chatgpt.com/docs)
- [How Claude remembers your project - Claude Code Docs](https://code.claude.com/docs/en/memory)（AGENTS.mdの読み込みについて）
