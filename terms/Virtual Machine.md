---
aliases: [VM, 仮想マシン, 仮想計算機, Hypervisor, ハイパーバイザ, Type-1 Hypervisor, Type-2 Hypervisor, Guest OS, ゲストOS, Host OS, ホストOS, Hardware-assisted Virtualization, Intel VT-x, AMD-V, 仮想化]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# Virtual Machine（仮想マシン）

> 一台の物理的な計算機の上に、ソフトウェアによって作られた独立した計算機であり、その中でOS（ゲストOS）をそのまま動かすことができる。

## 概要
仮想マシンを作り、管理するソフトウェアをハイパーバイザと呼ぶ。1974年のPopekとGoldbergの定義では、仮想マシンは「実際の計算機の、効率がよく、分離された複製」である。1960年代のIBMのCP-40とCP-67が、この考え方の始まりである。

ハイパーバイザには二つの型がある。Type 1は、ハードウェアの上で直接動き、ハードウェアとゲストOSを管理する（Xen、Hyper-V、VMware ESXiなど）。Type 2は、通常のOSの上で他のプログラムと同じように動く（VirtualBox、VMware Workstationなど）。Linuxの[[QEMU|KVM]]は、カーネルのモジュールとしてホストのLinuxをType 1のハイパーバイザに変えるものとされ、分類は明確ではない。2005〜2006年に導入されたIntel VT-xやAMD-Vなどの、CPUによる仮想化の支援機能により、改変しないゲストOSを効率よく動かせるようになった。ディスクやネットワークなどの装置は、実在の装置を模擬するか、仮想化のために設計された[[virtio]]の装置をゲストに見せる。

仮想マシンは、それぞれが独自のカーネルを持つ点で、ホストのカーネルを共有するコンテナ（[[Docker]]や[[Incus]]のシステムコンテナ）と異なる。コンテナは軽い一方、カーネルを分けることはできない。

## どこで出てくるか
カーネルやファイルシステム、ドライバを改変する研究では、[[QEMU]]の仮想マシンが開発と試験の標準的な環境である。変更したカーネルがクラッシュしても、実機と異なり容易にやり直せ、[[gdb]]でゲストのカーネルを調べたり、[[Snapshot|スナップショット]]で状態を戻したりできる。

一方、仮想マシンの中で測った性能は、仮想化の負担や装置の模擬の影響を含む。実機の性能を論じる根拠とする場合には、その影響に注意し、測定の環境を明記する必要がある。

## 関係
- 使う / 使われる: [[QEMU]], [[virtio]], [[Incus]]
- 対比: [[Docker]]（ホストのカーネルを共有するコンテナ）
- 関連: [[Linux Kernel]], [[Virtual Memory]], [[Snapshot]], [[gdb]]

## 出典
- [Virtual machine - Wikipedia](https://en.wikipedia.org/wiki/Virtual_machine)
- [Hypervisor - Wikipedia](https://en.wikipedia.org/wiki/Hypervisor)
