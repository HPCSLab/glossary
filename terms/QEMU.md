---
aliases: [qemu, qemu-system-x86_64, TCG, Emulator, エミュレータ]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# QEMU

> 計算機全体（CPU、メモリ、各種デバイス）をソフトウェアで模擬し、その上でOSを動作させる、オープンソースのエミュレータ兼仮想化ソフトウェアである。

## 概要
QEMUには二つの動作形態がある。システムエミュレーションでは、CPU、メモリ、ディスク、[[NIC|ネットワークカード]]などを備えた仮想的な計算機を構成し、その上でゲストOSを起動する。ユーザモードエミュレーションでは、あるCPU向けにコンパイルされたプログラムを、別のCPUの上で一つのプロセスとして実行する。

CPUの実行方式は二通りある。一つは、ゲストの命令をQEMU自身の変換器（TCG）でホストの命令に翻訳して実行する方式であり、異なるアーキテクチャ（例えばx86のホスト上のARMのゲスト）も実行できるが、低速である。もう一つは、ハイパーバイザによる加速であり、Linuxでは[[Linux Kernel|Linuxカーネル]]の機能である[[KVM]]を用いて、ゲストの命令をホストのCPU上で直接実行する。同じアーキテクチャ同士であれば、KVMを用いることで実機に近い速度が得られる。この場合、CPUとメモリの仮想化はKVMが担い、ディスクやネットワークなどのデバイスの模擬はQEMUが担う。デバイスには、実在のハードウェアを忠実に模擬するもの（例えば[[NVMe]]のコントローラ）と、仮想化のために設計された効率のよい[[virtio]]デバイスがある。

## どこで出てくるか
カーネルやファイルシステム、ドライバを改変する研究では、QEMUの[[Virtual Machine|仮想マシン]]が標準的な開発環境である。変更したカーネルが起動しなくなったりクラッシュしたりしても、実機と異なり容易にやり直せる。`-kernel` オプションでビルドしたカーネルイメージを直接起動できるため、カーネルの変更と動作確認の繰り返しが速い。`-s -S` オプションを付けると、QEMUが[[gdb]]の接続を待ち受け、ゲストのカーネルにブレークポイントを設定してステップ実行できる。仮想マシン内に[[kdump]]を設定しておくことも有効である。

ストレージの研究では、QEMUのNVMeデバイスを用いて、手元にない機能を持つ装置を試すことができる。例えば、複数の名前空間や、ZNS（Zoned Namespaces）の装置を模擬できる。SSD内部の振る舞い（[[FTL]]やガベージコレクション）まで模擬したい場合は、QEMUを拡張した[[FEMU]]が用いられる。一方、仮想マシン上で測定した性能は、仮想化やデバイスの模擬のオーバーヘッドを含むため、実機の性能を論じる根拠としては扱いに注意を要する。

## 関係
- 使う / 使われる: [[FEMU]]（QEMUを拡張したSSDエミュレータ）, [[KVM]], [[NVMe]]（模擬デバイス）
- 関連: [[kdump]], [[Virtual Memory]], [[ublk]]

## 出典
- [About QEMU - QEMU documentation](https://www.qemu.org/docs/master/about/index.html)
- [NVMe Emulation - QEMU documentation](https://www.qemu.org/docs/master/system/devices/nvme.html)
- [GDB usage - QEMU documentation](https://www.qemu.org/docs/master/system/gdb.html)
