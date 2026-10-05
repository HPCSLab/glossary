---
aliases: [docker, Docker Engine, dockerd, Dockerfile, Docker Hub, Docker Image, Dockerイメージ, Container Image, コンテナイメージ, OCI Image]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# Docker

> アプリケーションとその実行に必要なものをイメージとしてまとめ、ホストの[[Linux Kernel|カーネル]]を共有する分離された環境（コンテナ）で実行するための、プラットフォームである。

## 概要
Dockerは、クライアントとサーバの構成をとる。常駐するデーモン（`dockerd`）が、イメージやコンテナを管理し、利用者はクライアントの `docker` コマンドでデーモンに指示を出す。両者はREST APIで通信する。

イメージは、コンテナを作るための読み取り専用のひな型であり、Dockerfileに書いた手順に従って作られる。Dockerfileの各命令はイメージの層（レイヤ）となり、変更のあった層だけを作り直せる。コンテナは、イメージから作られた実行中の実体である。イメージは、レジストリに置いて共有され、既定の公開のレジストリはDocker Hubである。

Dockerは、Linuxカーネルの機能を用いてコンテナを実現する。名前空間（namespaces）は、プロセス、ネットワーク、ファイルシステムなどの見え方をコンテナごとに分け、コントロールグループ（cgroups）は、メモリ、CPU、ディスクのI/Oなどの資源の使用量を制限する。コンテナはホストのカーネルを共有するため、それぞれが独自のカーネルを持つ[[Virtual Machine|仮想マシン]]よりも軽い。

## どこで出てくるか
ソフトウェアの実行環境をイメージとしてまとめて配布すれば、異なる計算機でも同じ環境で実行できる。

ただし、Dockerのデーモンは既定ではroot権限で動作し（root権限を要しないrootlessモードもある）、ホストのディレクトリをアクセス権を制限せずにコンテナと共有できるため、コンテナからホストのファイルシステムを書き換えうる。多数の利用者が共有するHPCの環境に向けては、ローレンス・バークレー国立研究所で開発されたApptainer（旧Singularity）がある。Apptainerでは、コンテナの中でも外と同じ利用者のままであり、既定では特権を得られない。DockerやOCIのイメージを用いることができ、[[GPU]]や高速なネットワーク、[[Parallel File System|並列ファイルシステム]]もそのまま使える。

コンテナはホストのカーネルを共有するため、カーネルを改変する研究には向かない。その場合は[[QEMU]]などの仮想マシンを用いる。

## 関係
- 上位概念: [[Linux Kernel]]（名前空間とcgroupsを用いる）
- 対比: [[Virtual Machine]]（独自のカーネルを持つ）, [[Incus]]（システムコンテナを扱う）
- 関連: [[Ubuntu]], [[Copy-on-Write]]（イメージの層の共有）, [[Spack]]

## 出典
- [What is Docker? - Docker Docs](https://docs.docker.com/get-started/docker-overview/)
- [Docker Engine security - Docker Docs](https://docs.docker.com/engine/security/)
- [Introduction to Apptainer - Apptainer User Guide](https://apptainer.org/docs/user/latest/introduction.html)
- [Singularity Compatibility - Apptainer User Guide](https://apptainer.org/docs/user/latest/singularity_compatibility.html)（Singularityからの名称の変更）
- [Copy-on-write - Wikipedia](https://en.wikipedia.org/wiki/Copy-on-write)（Dockerのイメージの層）
