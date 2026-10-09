---
aliases: [PCI Express, PCI-E, PCIe Gen]
tags: [term]
maps: ["[[Parallel Computing]]", "[[Storage]]", "[[Operating System]]"]
status: draft
updated: 2026-10-10
---
# PCIe（PCI Express）

> CPUと[[GPU]]、[[SSD]]、[[NIC]]などの周辺装置とを接続する、計算機内部の高速なシリアル接続の規格である。

## 概要
PCIeは、複数の装置が一本の並列のバスを共有していた旧来のPCIに代わる規格であり、CPU側のルートコンプレックスと各装置とを一対一のリンクで結ぶ。リンクは、送信と受信の信号線の対からなるレーンを束ねたものであり、束ねる数をx1、x4、x8、x16のように表す。装置が多い場合はPCIeスイッチを介して接続する。データはパケットに分けて送られ、ネットワークに近い構成になっている。

規格は世代ごとにレーンあたりの転送速度がおおむね倍になってきた。x16のリンクの片方向の[[Bandwidth|帯域]]は、Gen3で約16 GB/s、Gen4で約32 GB/s、Gen5で約63 GB/sである。Gen6（64 GT/s）からは、信号をPAM4で多値化し、誤り訂正（FEC）を加えた固定長のFLITという単位で転送する。2025年に策定されたGen7は、x16で双方向合計512 GB/sを掲げる。新しい世代の装置を古い世代のスロットに挿すと、両者が対応する世代のうち低い方の速度で動作する。

## どこで出てくるか
[[Compute Node|計算ノード]]の性能を見積もるとき、PCIeの帯域は[[GPU]]と主記憶の間の転送、[[NVMe]]の[[SSD]]からの読み出し、[[InfiniBand]]などのNICによる通信の上限を決める要因となる。例えば、CPUとGPUの間の転送はGPU内部のメモリの帯域よりはるかに遅いため、GPUを使うプログラムでは転送の量と回数を減らすことが重要になる。[[GPUDirect RDMA]]や[[GPUDirect Storage]]は、NICやSSDとGPUがPCIeを介して直接データをやり取りすることで、CPUと主記憶を経由する転送を省く技術である。

実験の際は、Linuxの `lspci` で接続されている装置を、`lspci -t` でその接続の木構造を確認できる。`lspci -vv` の出力では、装置が対応する速度と幅（LnkCap）と、実際に確立したリンクの速度と幅（LnkSta）を比べられる。後者が低い場合は downgraded と表示され、期待した帯域が出ない原因になる。

## 関係
- 使う / 使われる: [[NVMe]], [[CXL]], [[GPUDirect RDMA]], [[GPUDirect Storage]]
- 関連: [[GPU]], [[SSD]], [[Bandwidth]]

## 出典
- [PCI Express - Wikipedia](https://en.wikipedia.org/wiki/PCI_Express)
- [PCI-SIG Releases PCIe 7.0 Specification to Support Bandwidth Demands of AI at 128.0 GT/s - AIwire](https://dev.aiwire.net/2025/06/11/pci-sig-releases-pcie-7-0-specification-to-support-bandwidth-demands-of-ai-at-128-0-gt-s/)
- [lspci(8) - Linux manual page](https://man7.org/linux/man-pages/man8/lspci.8.html)
- [PowerEdge: XE9685L - Linux command "lspci -vvv" shows "downgraded" - Dell](https://www.dell.com/support/kbdoc/000308325/poweredge-xe9685l-linux-command-lspci-vvv-shows-downgraded-on-nvidia-connectx-7-device)
