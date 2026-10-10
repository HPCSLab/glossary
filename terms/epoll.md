---
aliases: [epoll_create1, epoll_ctl, epoll_wait, EPOLLET, Edge-triggered, エッジトリガ, Level-triggered, レベルトリガ, I/O多重化, I/O Multiplexing]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# epoll

> 多数の[[File Descriptor|ファイルディスクリプタ]]を登録しておき、そのうち読み書きできる状態になったものだけを効率よく知らせる、[[Linux Kernel|Linux]]のI/Oのイベント通知の仕組みである。

## 概要
ネットワークの接続のように多数のファイルディスクリプタを扱うプログラムは、そのうちどれが読み書きできるかを知る必要がある。epollは、従来の `poll()` と同じくこの目的の仕組みであり、監視対象の一覧（interest list）をカーネルの中に保持し、準備ができたものだけを集めた一覧（ready list）を返すことで、多数のファイルディスクリプタに対してもよく拡張する。Linux 2.5.44で導入された。

使い方は三つの[[System Call|システムコール]]からなる。`epoll_create1()` でepollのインスタンスを作り、`epoll_ctl()` で監視するファイルディスクリプタを登録し、`epoll_wait()` で準備ができたものが現れるまで待つ。通知の方式には、準備ができている間は毎回知らせるレベルトリガ（既定）と、状態が変化したときにだけ知らせるエッジトリガ（`EPOLLET`）がある。エッジトリガでは、届いたデータを読み残すと次の通知が来ないことがあるため、ファイルディスクリプタを非ブロッキングにし、[[read]] や [[write]] が `EAGAIN` を返すまで処理を続けるのが推奨される使い方である。

## どこで出てくるか
多数の接続を扱うネットワークのプログラムの、I/Oの待ち方を議論する際に出てくる。一方、通常のファイルやディレクトリはepollに登録できない（`epoll_ctl()` が `EPERM` を返す）。したがって、ファイルのI/Oを待たずに進めたい場合には、epollではなく[[io_uring]]などの非同期I/Oの仕組みを用いる。

## 関係
- 前提: [[File Descriptor]], [[System Call]]
- 対比: [[io_uring]]（準備ができたことを知らせるのではなく、I/Oの要求と完了を受け渡す非同期I/Oである）
- 関連: [[Linux Kernel]]

## 出典
- [epoll(7) - Linux manual page](https://man7.org/linux/man-pages/man7/epoll.7.html)
- [epoll_ctl(2) - Linux manual page](https://man7.org/linux/man-pages/man2/epoll_ctl.2.html)
