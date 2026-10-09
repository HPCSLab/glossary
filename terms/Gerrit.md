---
aliases: [Gerrit Code Review, ゲリット]
tags: [term]
maps: ["[[Programming]]"]
status: draft
updated: 2026-10-10
---
# Gerrit

> [[Git]]で管理されたソフトウェアの変更を、ブランチに取り込む前にWeb上で[[Code Review|コードレビュー]]するためのオープンソースのツールである。

## 概要
Gerritは、Googleが[[Android]]のオープンソース開発（AOSP）のために作ったコードレビューツールであり、Apache 2.0ライセンスで公開されている。現在の実装はJavaであり、3.x系ではレビューのコメントや投票などのメタデータもすべてGitリポジトリの中に保存する。

Gerritでは、レビューの単位は1つのコミットであり、これを change と呼ぶ。開発者は対象ブランチへ直接pushする代わりに、`git push origin HEAD:refs/for/master` のように `refs/for/<ブランチ名>` という特別な参照へpushする。するとGerritは新しい change を作り、レビュアーはWeb画面で差分にコメントを付ける。指摘を受けた開発者は、コミットを `git commit --amend` で修正して再度pushする。コミットメッセージの末尾にある `Change-Id` という行によって、修正版は同じ change の新しい patch set として扱われる。この「1コミットを改訂し続ける」方式は、[[Linux Kernel|Linuxカーネル]]などのメーリングリストでパッチを改訂して送り直す方式に近く、[[GitHub]]の[[Pull Request]]がブランチに修正コミットを積み重ねていく方式とは異なる。

取り込みの可否は、label と呼ばれる投票で決まる。標準の Code-Review label は -2 から +2 の値を持ち、+2 が承認、-2 が拒否（拒否権）を意味する。プロジェクトによっては、[[Continuous Integration|CI]]がビルドとテストの結果を Verified label（-1 から +1）として投票する。既定では、各 label で最高値の投票を得た change だけが submit され、ブランチに取り込まれる。

## どこで出てくるか
Android、Chromium、Qt などの大規模なオープンソースプロジェクトで用いられている。HPCの分野では、[[Lustre]]の開発がGerritを用いており、パッチの投稿やレビュー、テスト結果の確認は https://review.whamcloud.com/ 上で行われる。Lustreのソースコードを読む際に、ある変更が入った経緯や議論を調べるとき、またLustreに修正を投稿するときにGerritを使うことになる。

## 関係
- 前提: [[Git]]
- 対比: [[GitHub]]（Pull Requestがブランチ単位で修正コミットを積むのに対し、Gerritは1コミットを patch set として改訂する）
- 使う / 使われる: [[Lustre]]
- 関連: [[Code Review]], [[Continuous Integration]]

## 出典
- [Gerrit Code Review](https://www.gerritcodereview.com/)
- [Gerrit's History](https://www.gerritcodereview.com/about.html)
- [Gerrit Code Review - Basics (User Guide)](https://gerrit-review.googlesource.com/Documentation/intro-user.html)
- [Gerrit Code Review - Review Labels](https://gerrit-review.googlesource.com/Documentation/config-labels.html)
- [Using Gerrit - Lustre Wiki](https://wiki.lustre.org/Using_Gerrit)
