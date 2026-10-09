---
aliases: [Github, ギットハブ, GitHub Issues, GitHub Actions, GitHub Pages]
tags: [term]
maps: ["[[Programming]]"]
status: draft
updated: 2026-10-10
---
# GitHub

> [[Git]]のリポジトリをクラウド上で預かり、課題管理やコードレビュー、自動化の機能を加えて共同開発を支えるサービスである。

## 概要
Gitそのものは手元で動くバージョン管理のソフトウェアであり、複数人で開発するには共有のためのリモートのリポジトリが必要である。GitHubは、このリモートのリポジトリを提供し、その上に開発のための機能を加えたサービスである。GitとGitHubは別物であり、Gitの操作（コミット、ブランチ、マージ）はGitHubがなくても行える。

主な機能として、作業やバグを記録する Issues、変更を提案してレビューを受け、承認されたものを取り込む[[Pull Request]]がある。他者のリポジトリに書き込み権限がない場合は、そのリポジトリを自分のアカウントに複製した fork を作り、fork のブランチから元のリポジトリへ Pull Request を出す。また、リポジトリの `.github/workflows` に置いたYAMLファイルに従って、push や Pull Request を契機にビルドやテストを自動で実行する GitHub Actions（[[Continuous Integration|CI]]）と、リポジトリのファイルから静的なWebサイトを公開する GitHub Pages を備える。

## どこで出てくるか
研究で開発したソフトウェアや論文の実装を公開する場として用いられ、[[CHFS]]、[[Omni Compiler]]、[[BaM]]、[[NADINO]]などの実装もGitHubで公開されている。論文を読んで実装を試すときは、GitHubのリポジトリから `git clone` で取得し、Issues で既知の問題や使い方の質問を調べる。一方、[[Lustre]]のように、コードレビューに[[Gerrit]]、課題管理に[[Jira]]を用いるプロジェクトもあり、その場合の議論や経緯はGitHubではなくそれらのサービス上にある。

## 関係
- 前提: [[Git]]
- 対比: [[Gerrit]]（GitHubはブランチ単位の Pull Request でレビューする）, [[Jira]]（課題管理を専門とするツールである）
- 関連: [[Pull Request]], [[Continuous Integration]]

## 出典
- [About GitHub and Git - GitHub Docs](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git)
- [About forks - GitHub Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks)
- [Understanding GitHub Actions - GitHub Docs](https://docs.github.com/en/actions/get-started/understand-github-actions)
- [What is GitHub Pages? - GitHub Docs](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
