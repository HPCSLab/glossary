---
aliases: [ExaScaler, DDN EXAScaler, DDN, DataDirect Networks, ES400NVX2, Whamcloud]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# EXAScaler

> DDN（DataDirect Networks）が提供する、オープンソースの[[Lustre]]を基にした商用の[[Parallel File System|並列ファイルシステム]]であり、専用のストレージ装置と組み合わせて提供される。

## 概要
DDNは、1998年に設立された米国のストレージの企業である。2018年6月に、IntelからLustreの開発チームを買収し、かつてLustreの開発を担った企業の名前であるWhamcloudを復活させた。

EXAScalerは、このLustreに、DDNのストレージ装置、管理のためのツール、独自の機能を加えた製品である。独自の機能には、データを性能と費用に応じた記憶媒体に自動で配置するHot PoolsとHot Nodes、暗号化を伴うマルチテナンシ、[[GPUDirect Storage]]への対応などがある。AIの学習と推論、HPCのクラスタを主な対象としている。中身はLustreであり、ストライプなどの基本的な考え方はLustreに従う。

## どこで出てくるか
計算機センターのスーパーコンピュータの仕様に、並列ファイルシステムとして現れる。例えば、筑波大学の[[Pegasus]]は7.1PB（40GB/s）のDDN EXAScalerを、JCAHPCの[[Miyabi]]は全ての記憶装置を[[NVMe]] SSDとした11.3PB（1.0TB/s）のLustre（DDN EXAScaler）を共有のファイルシステムとして備える。このようなシステムを使う際には、[[Lustre]]の記事と各システムの利用の手引きを参照する。

## 関係
- 上位概念: [[Lustre]]（EXAScalerはLustreを基にした製品である）
- 使う / 使われる: [[Pegasus]], [[Miyabi]], [[GPUDirect Storage]]
- 関連: [[Parallel File System]], [[Lustre PCC]], [[NVMe]]

## 出典
- [EXAScaler Lustre File System - DDN](https://www.ddn.com/products/lustre-file-system-exascaler/)
- [DataDirect Networks - Wikipedia](https://en.wikipedia.org/wiki/DataDirect_Networks)
- [Introduction of a New Supercomputer with the World's First NVIDIA H100 PCIe and Non-Volatile Memory - CCS, University of Tsukuba](https://www.ccs.tsukuba.ac.jp/release220512e/)（Pegasusの並列ファイルシステム）
- [Introduction to the Miyabi Supercomputer System - Information Technology Center, The University of Tokyo](https://www.cc.u-tokyo.ac.jp/en/supercomputer/miyabi/system.php)
