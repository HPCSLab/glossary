---
aliases: [ClaudeCode, claude code, CLAUDE.md, Auto Memory, MCP, Model Context Protocol, Skills, Hooks, Coding Agent, コーディングエージェント]
tags: [term]
maps: ["[[AI Tools]]"]
status: draft
updated: 2026-10-10
---
# Claude Code

> Anthropicが提供する、コードベースを読み、ファイルを編集し、コマンドを実行し、開発ツールと連携して作業を進める、エージェント型のプログラミング支援ツールである。

## 概要
Claude Codeは、[[Claude]]を用いて、利用者が自然言語で依頼した作業を、計画、ファイルの編集、コマンドの実行、結果の確認を繰り返しながら進める。端末で動作するコマンドラインのツールのほか、VS CodeやJetBrainsのIDEの拡張、デスクトップアプリ、Webブラウザからも利用でき、いずれも同じ仕組みの上で動作する。[[Git|git]]を直接扱い、変更のステージング、コミットメッセージの作成、ブランチの作成、プルリクエストの作成まで行える。

作業の方針を伝える主な手段は、プロジェクトの直下に置く `CLAUDE.md` である。Claude Codeは、各セッションの開始時にこのファイルを読み込み、そこに書かれた規約や手順に従おうとする。各セッションは新しい文脈から始まるため、セッションをまたいで伝えたい指示は `CLAUDE.md` に書く。これとは別に、Claude Codeが作業の中で利用者の修正や好みを自ら記録する自動メモリの仕組みもある。ただし、これらはあくまで文脈として扱われ、強制される設定ではない。特定の操作を確実に禁止したい場合は、操作の前後にシェルのコマンドを実行するhooksを用いる。このほか、外部のデータやツールに接続する開かれた標準であるMCP（Model Context Protocol）、繰り返し使う手順をまとめたskills、複数のエージェントの並列実行などの機能がある。

## どこで出てくるか
このノート群（用語集）は、Claude Codeを用いて作成している。リポジトリの `CLAUDE.md` に、ノートのテンプレート、命名規則、文体、公開情報のみを書くことなどの規則を記述し、利用者が用語を指示すると、Claude Codeが公開の文書を調べてノートを書き、入口ノート（map）を更新し、利用者の確認を経てコミットする、という手順で運用している。

公式の文書は、機能の作成と不具合の修正、テストの作成と実行、ログの解析、gitの操作の自動化などを用途として挙げている。Claude Codeはファイルの編集やコマンドの実行を実際に行うため、どの操作を許可するかを確認しながら使い、生成された変更は必ず差分を読んで確かめる。また、生成された説明や引用は誤りを含みうるため、事実は出典で確認する必要がある。

## 関係
- 上位概念: [[Claude]]（Claude Codeが用いるモデル）
- 対比: [[Codex]]（OpenAIのコーディングエージェント）
- 関連: [[ChatGPT]], [[LLM]]

## 出典
- [Overview - Claude Code Docs](https://code.claude.com/docs/en/overview)
- [How Claude remembers your project - Claude Code Docs](https://code.claude.com/docs/en/memory)
