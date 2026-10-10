---
aliases: [Intelligent Platform Management Interface, BMC, Baseboard Management Controller, ベースボード管理コントローラ, ipmitool, Serial over LAN, SOL, アウトオブバンド管理, Out-of-band Management]
tags: [term]
maps: ["[[System Administration]]"]
status: draft
updated: 2026-10-10
---
# IPMI（Intelligent Platform Management Interface）

> サーバのCPUやOSとは独立に動く管理用の小さな計算機（BMC）を通じて、電源の操作や温度などの監視をネットワーク越しに行うための仕様である。

## 概要
IPMIは、Intelが主導し、1998年に最初の版が公開された仕様であり、多くのサーバの製造元が対応している。サーバのマザーボードには、BMC（Baseboard Management Controller）と呼ばれる専用のコントローラが載っており、本体のCPU、ファームウェア、OSとは独立に動作する。このため、OSが起動する前、OSが停止したとき、さらに本体の電源が切れているときでも、BMCを通じてサーバを管理できる。このように、本体のOSとネットワークを経由せずに管理する方式をアウトオブバンド管理と呼ぶ。

BMCは、温度、ファンの回転数、電圧などのセンサーを監視し、異常を記録・通知するほか、本体の電源の投入・切断やリセットを行う。1.5版でネットワーク越しの操作（IPMI over LAN）が、2004年の2.0版で、本体のシリアルコンソールをネットワーク越しに使うSerial over LAN（SOL）と、強化された認証が加わった。製品によっては、画面とキーボードをネットワーク越しに操作する機能や、手元のディスクイメージを仮想的な媒体として本体に見せる機能も備えるが、これらは標準の範囲外である。

## どこで出てくるか
サーバ室に行かずにサーバを管理するための基本的な手段である。[[Linux Kernel|Linux]]では `ipmitool` を用い、`ipmitool -I lanplus -H <BMCのアドレス> chassis power status` のようにBMCに接続して、電源の状態の確認と操作（`power on`・`off`・`cycle`）、センサーの値の表示（`sensor list`）、イベントの記録の表示（`sel list`）、SOLによるコンソールへの接続（`sol activate`）を行う。`power off` はOSを正しく終了させずに電源を切るため、OSを終了させる場合は `power soft` を用いる。`chassis bootdev pxe` で次回の起動を[[PXE]]からのネットワークブートに切り替えられるため、多数の計算機へのOSのインストールにも用いる。

BMCは本体を完全に制御できるため、その安全性が重要である。古い版のIPMIには、認証も暗号化も行わない方式（cipher zero）を許すなどの設計上の弱点が知られており、BMCのネットワークは管理用の専用のネットワークに分離することが推奨される。より安全な後継として、DMTFがRESTのインタフェースでサーバなどを管理する規格であるRedfishを定めている。

## 関係
- 使う / 使われる: [[PXE]]（起動デバイスの切り替え）

## 出典
- [Intelligent Platform Management Interface - Wikipedia](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface)
- [ipmitool(1) - Linux man page](https://linux.die.net/man/1/ipmitool)
- [Redfish (specification) - Wikipedia](https://en.wikipedia.org/wiki/Redfish_(specification))
