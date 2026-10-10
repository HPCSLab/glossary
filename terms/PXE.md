---
aliases: [PXE Boot, PXEブート, Preboot Execution Environment, Preboot eXecution Environment, ネットワークブート, Network Boot, iPXE, NBP, Network Bootstrap Program, proxyDHCP]
tags: [term]
maps: ["[[System Administration]]"]
status: draft
updated: 2026-10-10
---
# PXE（PXEブート、ネットワークブート）

> 計算機が、ローカルの記憶装置ではなくネットワーク上のサーバから起動用のプログラムを取得して起動するための仕様である。PXEは Preboot Execution Environment の略で、「ピクシー」と読む。

## 概要
PXEは、Intelが管理のしやすい計算機のための枠組みの一部として定めた仕様であり、1999年に版2.1が公開された。現在はUEFIの標準にもネットワークからの起動の仕組みとして含まれている。PXEに対応した[[NIC]]とファームウェアがあれば、記憶装置にOSが入っていない計算機でも起動できる。

起動の手順は、既存の標準のプロトコルの組み合わせである。まず、ファームウェアが[[DHCP]]の要求をブロードキャストし、IPアドレスなどのネットワークの設定と、起動用のプログラムを置いたサーバのアドレスとファイル名を受け取る。次に、TFTP（Trivial File Transfer Protocol）でそのプログラム（Network Bootstrap Program、NBP）をメモリに読み込んで実行する。TFTPは、[[UDP]]の上で512バイトずつ受け渡す、認証もディレクトリの一覧の機能もない、極めて単純なプロトコルである。NBPは通常、小さなOSやブートローダを読み込み、それがHTTPや[[NFS]]などのより速い手段でOSのインストーラや本体を取得する。既存のDHCPサーバの設定を変えずに、起動用の情報だけを別のサーバ（proxyDHCP）から返す構成もある。

## どこで出てくるか
計算機を何台もまとめてセットアップするときに用いる。データセンターでは、OSの起動、インストール、配備の手段として最も一般的であり、主要な[[Linux Kernel|Linux]]のディストリビューションのインストーラが対応している。クラスタの[[Compute Node|計算ノード]]に一台ずつUSBメモリでOSを入れる代わりに、管理サーバにDHCP、TFTP、HTTPなどのサービスを用意し、ネットワーク越しにインストールする。オープンソースのiPXEは、PXEを拡張したネットワークブートのファームウェアであり、HTTPや[[iSCSI]]からの起動やスクリプトによる制御ができる。NICのPXEのROMを置き換えるほか、通常のPXEからiPXEを読み込む（チェーンロード）ことでも使える。起動しないときは、DHCPの応答が届いているか、TFTPでファイルを取得できているかを順に確かめる。

## 関係
- 前提: [[DHCP]], [[NIC]]
- 使う / 使われる: [[NFS]], [[iSCSI]]

## 出典
- [Preboot Execution Environment - Wikipedia](https://en.wikipedia.org/wiki/Preboot_Execution_Environment)
- [RFC 1350 - The TFTP Protocol (Revision 2)](https://datatracker.ietf.org/doc/html/rfc1350)
- [iPXE - open source boot firmware](https://ipxe.org/)
