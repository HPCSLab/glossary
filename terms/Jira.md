---
aliases: [JIRA, ジラ, Jira Software]
tags: [term]
maps: ["[[Programming]]"]
status: draft
updated: 2026-10-10
---
# Jira

> Atlassian社が提供する課題管理ツールであり、バグ報告や機能追加などの作業を一件ずつ記録し、その状態を追跡するために用いる。

## 概要
Jiraは、2002年にソフトウェア開発チーム向けの作業追跡ツールとして始まった製品である。作業の単位は issue（日本語ではチケットと呼ぶことが多く、現在のJira Cloudでは work item と呼ぶ）であり、バグ、タスク、機能要望などの種類を持つ。各 issue には、プロジェクトを表す大文字の英字の key と通し番号を組み合わせた `LU-477` のような識別子が付く。この識別子は短く一意であるため、コミットメッセージやメール、議論の中で issue を参照するのに使われる。

ソースコードの変更そのものは[[Git]]や[[Gerrit]]などで管理し、「なぜその変更が必要か」「どのような不具合が報告され、どこまで調査が進んだか」はJiraの issue に記録する、という役割分担になる。[[GitHub]]の Issues も同じ目的の機能である。

## どこで出てくるか
HPCの分野では、[[Lustre]]の開発がJiraを用いており、https://jira.whamcloud.com/ で公開されている。Lustreでは、すべてのパッチに対応する issue が必要であり、コミットメッセージの1行目は `LU-477 ldiskfs: allocate s_group_desc/s_group_info by vmalloc()` のように `LU-番号 コンポーネント名:` で始める決まりである。issue にはGerritの変更へのリンクや試験結果が添付される。そのため、Lustreのコミットやソースコードを調べるときは、`LU-` の番号からJiraの issue をたどることで、変更の背景となった不具合や議論を知ることができる。

## 関係
- 対比: [[GitHub]]（GitHub Issues はリポジトリに付属する課題管理機能である）
- 使う / 使われる: [[Lustre]]
- 関連: [[Gerrit]]

## 出典
- [Jira introduction - Atlassian](https://www.atlassian.com/software/jira/guides/getting-started/introduction)
- [What is a work item? - Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/what-is-an-issue/)
- [Submitting Changes - Lustre Wiki](https://wiki.lustre.org/Submitting_Changes)
- [Commit Comments - Lustre Wiki](https://wiki.lustre.org/Commit_Comments)
