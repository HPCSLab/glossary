---
aliases: [Big accelerator Memory, bam::array, GPU-initiated Storage Access, GPU主導のストレージアクセス]
tags: [term]
maps: ["[[Storage]]", "[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-10
---
# BaM

> [[GPU]]のスレッドが、CPUを介さずに[[NVMe]] SSDへの読み書きの要求を直接発行できるようにする、GPU主導のストレージアクセスのシステムである。

## 概要
BaMは、NVIDIAとイリノイ大学などの研究者（Qureshiら）が、2023年のASPLOSで発表した。従来、GPUで扱うデータを記憶装置から読む際には、CPUがどのデータを読むかを決めて読み込みを発行する（論文はこれをCPU中心の方式と呼ぶ）。この方式は、アクセスするデータが事前に分かる処理には適するが、グラフの解析のように、計算の途中でどのデータが必要になるかが決まる細かいアクセスには向かない。

BaMは、NVMeの提出キューと完了キューをGPUのメモリに置き、SSDのドアベルのレジスタをGPUから書けるように写像する。これにより、GPUの多数のスレッドが、自らNVMeのコマンドを作ってキューに入れ、ドアベルを鳴らし、SSDがGPUのメモリに直接データを転送する。数千のスレッドが同時にキューを操作しても大きな排他区間が生じないように、キューの操作は細かく並行化されている。GPUのメモリには、要求をまとめて記憶装置への余分なI/Oを減らすソフトウェアのキャッシュが置かれる。プログラマは、`bam::array` という、記憶装置上のデータをファイルの[[mmap]]のように配列として扱う抽象を通じて、データにアクセスする。

論文では、グラフ解析のBFSとCCで1.0倍と1.49倍、データ解析の処理で最大5.3倍の速度の向上を、ホストのメモリにデータを置く方式と比べて、より安価なハードウェアで達成したと報告している。

## どこで出てくるか
BaMは、GPUのメモリに収まらない大きなデータを、GPUから記憶装置に細かくアクセスして扱う研究で参照される。[[GPUDirect Storage]]がCPUの決めた転送を直接の経路で行うのに対し、BaMはアクセスの発行そのものをGPUに移す点が異なる。

実装は[[GitHub]]で公開されている。利用には、PCIeの[[GPUDirect RDMA|ピアツーピアのアクセス]]にメモリ全体を公開できるデータセンタ向けのGPU（Volta以降）が必要であり、IOMMUを無効にし、NVMe SSDをLinuxの標準のNVMeドライバから切り離して、BaMのカーネルモジュールで扱う必要がある。このため、SSDは通常のファイルシステムからは使えなくなる。

## 関係
- 前提: [[GPU]], [[NVMe]]
- 対比: [[GPUDirect Storage]]（CPUが転送を発行する）
- 使う / 使われる: [[GPUDirect RDMA]], [[CUDA]]
- 関連: [[SSD]], [[Cache]], [[blk-mq]]

## 出典
- [BaM: GPU-Initiated On-Demand High-Throughput Storage Access (Qureshi et al., ASPLOS 2023) - arXiv](https://arxiv.org/abs/2203.04910)
- [ZaidQureshi/bam - GitHub](https://github.com/ZaidQureshi/bam)
