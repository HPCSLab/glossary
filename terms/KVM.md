---
aliases: [Kernel-based Virtual Machine, kvm.ko, kvm-intel, kvm-amd, /dev/kvm]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# KVM（Kernel-based Virtual Machine）

> [[Linux Kernel|Linuxカーネル]]に組み込まれた仮想化の機能であり、CPUの仮想化支援機能を用いて、ホストのLinuxをハイパーバイザとして働かせる。

## 概要
KVMは、Intel VT-xやAMD-VというCPUの仮想化支援機能を用いて、ゲストOSの命令をホストのCPU上で直接実行させる。共通部分のモジュール `kvm.ko` と、CPUごとのモジュール `kvm-intel.ko` または `kvm-amd.ko` からなり、Linux 2.6.20でカーネルの本流に取り込まれた。

KVMが担うのは、CPUとメモリの仮想化だけである。利用者のプログラムは `/dev/kvm` を開き、ioctlで[[Virtual Machine|仮想マシン]]と仮想CPUを作り、`KVM_RUN` で仮想CPUを実行させる。ディスクやネットワークなどの装置の模擬は、KVMを呼び出すユーザ空間のプログラムが担う。その代表が[[QEMU]]であり、QEMUがKVMを用いると、命令を翻訳して実行する場合に比べて実機に近い速度でゲストを動かせる。ゲストの装置には、模擬した実在の装置のほか、効率のよい[[virtio]]の装置や、[[SR-IOV]]と[[IOMMU]]で物理的な装置を直接割り当てる方法を用いる。

## どこで出てくるか
LinuxでQEMUの仮想マシンを動かすとき、同じアーキテクチャのゲストであれば通常はKVMで加速する。[[Incus]]の仮想マシンもQEMUで実行される。カーネルを改変する研究で仮想マシンを開発環境にする場合も、KVMが使えるかどうかで速度が大きく変わる。`/dev/kvm` が存在しない場合は、BIOSで仮想化支援機能が無効になっているか、KVMのモジュールが読み込まれていない可能性がある。

## 関係
- 上位概念: [[Virtual Machine]]
- 前提: [[Linux Kernel]]
- 使う / 使われる: [[QEMU]], [[Incus]]
- 関連: [[virtio]], [[SR-IOV]], [[IOMMU]]

## 出典
- [KVM - Main Page](https://linux-kvm.org/page/Main_Page)
- [The Definitive KVM API Documentation - The Linux Kernel documentation](https://docs.kernel.org/virt/kvm/api.html)
