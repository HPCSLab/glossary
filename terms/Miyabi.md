---
aliases: [みやび, Miyabi-G, Miyabi-C, OFP-II, JCAHPC, 最先端共同HPC基盤施設, GH200, Grace Hopper, Xeon Max]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# Miyabi

> 筑波大学と東京大学が共同で運営する最先端共同HPC基盤施設（JCAHPC）のスーパーコンピュータであり、NVIDIA GH200を搭載した国内初の汎用の大規模システムである。

## 概要
JCAHPC（Joint Center for Advanced High Performance Computing）は、筑波大学計算科学研究センターと東京大学情報基盤センターが共同で運営する施設である。Miyabiは、その新しいスーパーコンピュータとして、OFP-IIの名で導入が決定され、東京大学柏キャンパスに設置されて、2025年1月14日に正式な運用を開始した。2025年4月から、文部科学省のHPCIの制度や、両大学の共同利用・共同研究の制度を通じて利用されている。名前には、理論性能が優れているだけでなく、その能力を難なく発揮できるように、という思いが込められている。

Miyabiは、二種類の[[Compute Node|計算ノード]]からなる。Miyabi-Gは、NVIDIAのGH200 Grace Hopper Superchipを搭載した1,120ノードであり、GH200は、CPU（Grace）と[[GPU]]（Hopper）を、高速なCPU-GPU間の専用リンク[[NVLink|NVLink-C2C]]で接続したものである。Miyabi-Cは、IntelのXeon Max 9480を2基搭載した190ノードである。両者は[[InfiniBand]] NDR200で接続され、システム全体の倍精度の演算性能は80.1PFLOPSである。また、すべてのドライブに[[NVMe]] SSDを用いた、10.3PBの[[Parallel File System|並列ファイルシステム]]を備える。2024年11月の[[TOP500]]では、国内の学術目的のスーパーコンピュータとして[[Fugaku|富岳]]に次ぐ第2位の性能を記録した。

共有のファイルシステムは、全ての記憶装置を[[NVMe]] SSDとした11.3PB（1.0TB/s）の[[Lustre]]（[[EXAScaler|DDN EXAScaler]]）である。OSはRocky Linux 9（ログインノードはRed Hat Enterprise Linux 9）、ジョブスケジューラは[[PBS|PBS Professional]]である。

## どこで出てくるか
Miyabiは、筑波大学と東京大学の利用者が共同利用の制度を通じて使える大規模な計算資源である。運営者は、利用者のプログラムのGPUへの移行や、AIを用いた科学（AI for Science）の取り組みを支援する方針を示している。筑波大学計算科学研究センター自身のスーパーコンピュータである[[Pegasus]]や[[Sirius]]とは、運営の主体（JCAHPC）と規模が異なる。

## 関係
- 使う / 使われる: [[GPU]], [[InfiniBand]], [[NVMe]], [[Parallel File System]]
- 対比: [[Pegasus]], [[Sirius]]（筑波大学計算科学研究センターのシステム）, [[Fugaku]]
- 関連: [[TOP500]], [[Compute Node]]

## 出典
- [最先端共同HPC基盤施設における次期システムの名称を決定 - JCAHPC](https://www.jcahpc.jp/pr/news-20240401.html)
- [最先端共同HPC基盤施設（JCAHPC）の新スーパーコンピュータシステム Miyabi（みやび）の運用開始披露式典を開催 - JCAHPC](https://www.jcahpc.jp/pr/news-20250117.html)
- [Miyabi システム概要（塙敏博, PCクラスタコンソーシアム HPC研究会, 2025）](https://www.pccluster.org/ja/event/data/250627_PCC-WS-Kashiwa_16_hanawa-miyabi.pdf)
- [Introduction to the Miyabi Supercomputer System - Information Technology Center, The University of Tokyo](https://www.cc.u-tokyo.ac.jp/en/supercomputer/miyabi/system.php)
- [スーパーコンピュータ「富岳」（公式）の投稿 - X](https://x.com/Fugaku_hpci/status/1882699864925982874)（2024年11月のTOP500について）
