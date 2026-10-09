---
aliases: [git, ギット]
tags: [term]
maps: ["[[Programming]]"]
status: draft
updated: 2026-10-10
---
# Git

> ファイルの変更履歴を記録し、複数人での並行した開発を可能にする分散型のバージョン管理システムである。

## 概要
Gitは、2005年に[[Linux Kernel|Linuxカーネル]]の開発コミュニティ（特にLinus Torvalds）が、それまで用いていた商用のバージョン管理システムBitKeeperを無償で使えなくなったことを受けて開発したものである。数千のブランチが並行する開発と、Linuxカーネルのような大きなプロジェクトを高速に扱うことが設計の目標であった。

Gitは、プロジェクト全体のある時点の状態（スナップショット）をコミットとして記録する。各コミットや各ファイルの内容は、その内容のハッシュ値（SHA-1）で識別されるため、`24b9da6...` のような値がコミットの名前になり、内容の破損や改ざんを検出できる。変更は、作業ツリーで編集し、`git add` でステージングエリアに載せ、`git commit` で `.git` ディレクトリに記録する、という三段階で扱う。

Gitは分散型であり、`git clone` で手元にリポジトリ全体の複製を作るため、履歴の閲覧や差分の計算、コミットはネットワークなしに手元で行える。他者との共有は、[[GitHub]]などに置いたリモートのリポジトリとの間で `git push` と `git pull` を行うことで実現する。一つのコミットから分かれて別々に変更を積むのがブランチであり、機能の追加や実験をブランチで進め、完成したものを本流にマージするのが基本的な開発の進め方である。

## どこで出てくるか
研究で書くプログラム、実験のスクリプト、[[LaTeX]]の論文の原稿など、テキストで書かれたものの版の管理にGitを用いる。論文の実装は多くの場合GitHubなどで公開されており、`git clone` で取得し、論文に記載されたコミットやタグを `git checkout` で指定して、論文と同じ版を再現する。また、[[Lustre]]や[[Linux Kernel|Linuxカーネル]]のソースコードを読む際には、`git log` や `git blame` で、ある行がいつ、どのコミットで、どのような理由で変更されたのかを調べる。

## 関係
- 使う / 使われる: [[GitHub]], [[Gerrit]]
- 関連: [[Linux Kernel]]

## 出典
- [Pro Git, 1.2 A Short History of Git](https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git)
- [Pro Git, 1.3 What is Git?](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F)
