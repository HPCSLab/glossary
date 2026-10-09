---
aliases: [ペガサス, Pegasus スーパーコンピュータ, 筑波大学 Pegasus, Cygnus-BD]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-10
---
# Pegasus

> 筑波大学計算科学研究センターのスーパーコンピュータであり、GPUに加えて、各計算ノードにIntel Optane永続メモリを搭載した「ビッグメモリ」のシステムである。

## 概要
PegasusはNECが構築し、筑波大学計算科学研究センターで2023年1月に稼働を開始した。発表の段階では仮称Cygnus-BDとされていた。第4世代Intel Xeonスケーラブル・プロセッサ（Sapphire Rapids）、[[PCIe]] Gen5で接続したNVIDIA H100 GPU、そして次世代のIntel Optane永続メモリの三つを組み合わせた、世界で最初期のシステムである。

各[[Compute Node|計算ノード]]は、[[GPU]]（H100、倍精度の理論ピーク性能51TFlops）、128GBのDDR5メモリ、2TBの[[Intel Optane Persistent Memory|Intel Optane永続メモリ]]（300シリーズ）、3.2TBの[[NVMe]] SSD 2台を備える。永続メモリによって、DRAMだけでは収まらない大規模なデータを扱えるようにしており、ビッグデータ解析、人工知能、大規模な計算科学を対象としている。当初は120ノード、理論ピーク性能約6PFlopsで構成され、現在は150ノード、理論ピーク性能8.1PFlops以上である。ノード間は[[InfiniBand]]で接続される。

並列ファイルシステムとして、7.1PB（40GB/s）の[[EXAScaler|DDN EXAScaler]]（[[Lustre]]）を備える。

## どこで出てくるか
Optane永続メモリは2022年にIntelが事業の終了を発表しており、新たに入手することは難しい。Pegasusは各ノードに永続メモリを搭載しているため、永続メモリを用いたシステムソフトウェアやストレージの研究（[[devdax]]による利用、永続メモリを用いる[[CHFS]]など）の評価に用いることができる。2026年には、同じセンターに[[Sirius]]が導入され、PegasusとInfiniBandで接続されている。

## 関係
- 使う / 使われる: [[Intel Optane Persistent Memory]], [[GPU]], [[NVMe]], [[InfiniBand]]
- 対比: [[Sirius]]（同じセンターのAPUを用いるシステム）, [[Fugaku]]
- 関連: [[devdax]], [[CHFS]], [[Compute Node]]

## 出典
- [Supercomputers - Center for Computational Sciences, University of Tsukuba](https://www.ccs.tsukuba.ac.jp/eng/supercomputers/)
- [スーパーコンピュータ - 筑波大学計算科学研究センター](https://www.ccs.tsukuba.ac.jp/supercomputer/)
- [Introduction of a New Supercomputer with the World's First NVIDIA H100 PCIe and Non-Volatile Memory - CCS, University of Tsukuba](https://www.ccs.tsukuba.ac.jp/release220512e/)
- [筑波大学、「ビッグメモリ」スーパーコンピュータPegasusを配備 - HPCwire Japan](https://www.hpcwire.jp/archives/73217)
- [新型スーパーコンピュータ Sirius (PACS12.0) の運用を開始 - 筑波大学計算科学研究センター](https://www.ccs.tsukuba.ac.jp/release260327/)
- [Intel is Winding Down Its Optane Business - WWT](https://www.wwt.com/blog/intel-is-winding-down-its-optane-business-what-does-this-mean-for-customers)
