---
aliases: [incus, LXD, LXC, liblxc, Linux Containers, System Container, システムコンテナ, Application Container, アプリケーションコンテナ]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# Incus

> システムコンテナ、アプリケーションコンテナ、仮想マシンを、同じコマンドとREST APIで作成・管理するための、オープンソースの管理ツールである。

## 概要
Incusは、CanonicalのLXDのフォークである。CanonicalがLXDをLinux Containersのプロジェクトから自社の管理に移したことを受けて、Aleksa Sarai がフォークを作成し、2023年8月にLinux Containersのプロジェクトとして公開された。開発は、かつてLXDを作った開発者らが中心となって行われている。Goで書かれ、Apache 2.0ライセンスのもとで公開されている。長期サポート版（LTS）のIncus 6.0は、2029年6月まで保守される。

Incusが扱うインスタンスには二種類ある。一つはコンテナであり、ホストの[[Linux Kernel|カーネル]]を共有しながら、分離された環境を作る。コンテナはliblxc（LXC）を用いて実装されており、オーバーヘッドが極めて小さく、多数を密に配置できる。コンテナのうち、システムコンテナは一つのLinuxのディストリビューション全体を動かし、仮想マシンに近い環境を提供する。アプリケーションコンテナは、Docker Hubなどのレジストリにある、一つのアプリケーションを含むOCI形式のイメージを動かす。もう一つは仮想マシンであり、[[QEMU]]を用いて、それぞれが独自のカーネルを持つ完全な仮想化された計算機を作る。異なるカーネルや独自のカーネルモジュールが必要な場合には、仮想マシンを用いる。

インスタンスは、各ディストリビューションのイメージから作成する。例えば、`incus launch images:debian/12 first` でコンテナを、`--vm` を付けると仮想マシンを起動でき、`incus exec first -- bash` で中に入ることができる。`incus snapshot create` で[[Snapshot|スナップショット]]を取っておけば、元の状態に戻すことができる。ストレージには[[ZFS]]、[[btrfs]]、[[LVM]]、[[Ceph]]などを、ネットワークにはブリッジやホスト間のトンネルを用いることができ、複数のホストをクラスタとして管理することもできる。

## どこで出てくるか
一台の計算機を複数の利用者や用途で共有する際に、それぞれに分離された環境を与える手段として用いられる。システムコンテナは、[[Ubuntu]]や[[Rocky Linux]]などの異なるディストリビューションの環境を、仮想マシンより軽く用意できる。ただし、コンテナはホストのカーネルを共有するため、カーネルを改変する研究や、カーネルの版の違いを試す実験には向かず、仮想マシンを用いる必要がある。

## 関係
- 使う / 使われる: [[QEMU]]（仮想マシンの実行に用いる）, [[Linux Kernel]]（コンテナはホストのカーネルを共有する）
- 関連: [[Ansible]], [[ZFS]], [[btrfs]], [[LVM]], [[Ceph]]

## 出典
- [Introduction - Incus](https://linuxcontainers.org/incus/introduction/)
- [Incus announcement - Linux Containers](https://linuxcontainers.org/incus/announcement/)
- [About instances - Incus documentation](https://linuxcontainers.org/incus/docs/main/explanation/instances/)
- [First steps with Incus - Incus documentation](https://linuxcontainers.org/incus/docs/main/tutorial/first_steps/)
