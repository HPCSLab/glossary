---
aliases: [make, GNU Make, Makefile, makefile, ビルドツール]
tags: [term]
maps: ["[[Programming]]"]
status: draft
updated: 2026-10-10
---
# Make

> ファイル間の依存関係とその生成手順を記述したMakefileに従い、変更があった部分だけを再構築するビルドツールである。

## 概要
`make` は、プログラムのコンパイルやリンクを自動化するための、古くから広く用いられているツールであり、Linuxで標準的に用いられるのはGNU Makeである。Makefileには、規則（rule）を並べて書く。各規則は、作りたいファイル（ターゲット）、それを作るのに必要なファイル（前提条件）、ターゲットを作るためのコマンド（レシピ）からなる。

```make
prog: main.o util.o
	cc -o prog main.o util.o

main.o: main.c util.h
	cc -c main.c
```

`make` は、ターゲットと前提条件のファイルの更新時刻を比べ、前提条件のほうが新しいターゲットだけを作り直す。例えば、ヘッダファイル `util.h` を変更すると、それをインクルードするソースファイルから作られる `main.o` と、それに依存する `prog` だけが再構築される。大規模なプログラムでも、変更の影響を受ける部分だけをコンパイルし直すため、ビルドの時間を短縮できる。`-j` オプションで、互いに依存しない規則を並列に実行できる。

## どこで出てくるか
Makefileは、C言語やFortranの小・中規模のプログラム、[[Linux Kernel|Linuxカーネル]]のビルド、論文の[[LaTeX]]の文書のビルド、実験の手順の自動化など、様々な場面で用いられる。大規模なプロジェクトでは、Makefileを直接書く代わりに、[[CMake]]などのツールでMakefileを生成することが多い。

新メンバーが最初につまずきやすいのは、レシピの行はスペースではなくタブ文字で始めなければならない点である。また、依存関係の記述が不完全だと、変更したはずのファイルが再構築されず、古いままのプログラムを実行してしまうことがある。挙動が疑わしいときは、`make clean` などで生成物を消してから作り直す。ファイルを生成しないターゲット（`clean`、`all` など）は `.PHONY` として宣言しておく。

## 関係
- 対比: [[CMake]]（Makefileなどのビルドファイルを生成する）
- 使う / 使われる: [[C]]（ビルドの対象）
- 関連: [[Spack]], [[Linux Kernel]]

## 出典
- [Introduction - GNU make](https://www.gnu.org/software/make/manual/html_node/Introduction.html)
