---
aliases: [VirtIO, VIRTIO, virtio-blk, virtio-net, virtio-scsi, virtio-fs, virtio-pci, Virtqueue, virtqueue, Paravirtualization, 準仮想化, Paravirtualized Device, 準仮想化デバイス]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# virtio

> [[Virtual Machine|仮想マシン]]の中のドライバと、ハイパーバイザが提供する仮想的な装置との間のやり取りを定めた、開かれた標準の規格である。

## 概要
実在の装置（例えば特定の[[NIC|ネットワークカード]]やディスクのコントローラ）を忠実に模擬すると、ゲストのドライバは実機と同じ手順で装置を操作するため、そのたびにハイパーバイザが細かい操作を模擬する必要があり、遅い。virtioは、仮想化のために最初から設計された装置の規格であり、ゲストが仮想の装置であることを前提に効率よく通信する（準仮想化）。規格はOASISが策定しており、単純で、効率がよく、標準的で、拡張可能な仕組みを目標とする。

ドライバと装置は、共有メモリ上のvirtqueueと呼ばれるデータ構造でデータをやり取りする。virtqueueは、バッファの記述子の[[Ring Buffer|リングバッファ]]であり、ドライバが要求を置き、装置が処理を終えたものを返す。装置が処理を終えると、ハイパーバイザが割り込みでドライバに通知する。virtqueueには、記述子の表と二つのリングに分けたsplit形式と、一つの環状のバッファにまとめたpacked形式がある。装置は、PCI、MMIO、IBMのメインフレームのチャネルI/Oのいずれかの方式でゲストに見せられ、どの機能を使うかは機能ビットの交渉で決まる。

規格には、ネットワーク（virtio-net）、ブロックデバイス（virtio-blk）、SCSI、コンソール、メモリのバルーン、GPU、ファイルシステム（virtio-fs）、永続メモリなど、19種類の装置が定められている。

## どこで出てくるか
[[QEMU]]と[[KVM]]で仮想マシンを動かす場合、ディスクやネットワークにvirtioの装置を選ぶことができ、Linuxのカーネルはvirtioのドライバを備える。仮想マシンの中でI/Oの性能を測る場合、装置がvirtioか、実在の装置の模擬かによって結果が変わりうるため、構成を明記する必要がある。ストレージの研究で[[NVMe]]の振る舞いそのものを調べたい場合には、virtio-blkではなく、QEMUのNVMeの装置の模擬や[[FEMU]]を用いる。

## 関係
- 上位概念: [[Virtual Machine]]
- 使う / 使われる: [[QEMU]], [[Ring Buffer]]
- 対比: [[NVMe]]（QEMUで実在の装置として模擬できる）
- 関連: [[Block Storage]], [[Linux Kernel]], [[FEMU]]

## 出典
- [Virtual I/O Device (VIRTIO) Version 1.3 - OASIS](https://docs.oasis-open.org/virtio/virtio/v1.3/virtio-v1.3.html)
- [Virtio on Linux - The Linux Kernel documentation](https://docs.kernel.org/driver-api/virtio/virtio.html)
