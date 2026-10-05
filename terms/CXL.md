---
aliases: [Compute Express Link, CXL.mem, CXL.cache, CXL.io, CXL Memory, CXLメモリ, Memory Expander, Memory Pooling, メモリプーリング, Tiered Memory, 階層メモリ]
tags: [term]
maps: ["[[Operating System]]", "[[Storage]]"]
status: draft
updated: 2026-10-06
---
# CXL（Compute Express Link）

> PCI Expressの物理層の上に、キャッシュの一貫性を保ったメモリアクセスの仕組みを加えた、CPUとメモリ、アクセラレータを接続するための開かれた業界標準のインターコネクトである。

## 概要
CXLは主にIntelが開発し、2019年に業界団体のCXL Consortiumが発足した。その後、競合していたGen-ZとOpenCAPIの規格も、CXL Consortiumに移管された。規格の主な版は、PCIe 5.0を基盤とする1.0/1.1（2019年）、スイッチを介した接続と装置の共有（プーリング）を加えた2.0（2020年）、PCIe 6.0を基盤とし、多段のスイッチとメモリの共有を拡充した3.0（2022年）、階層メモリのための機能を加えた3.2（2024年）、転送速度をさらに倍にした4.0（2025年）である。

CXLは三つのプロトコルを組み合わせる。CXL.ioは、PCIeと同等の、装置の検出や設定のためのプロトコルである。CXL.cacheは、装置がCPUのメモリを一貫性を保ってキャッシュするためのプロトコルである。CXL.memは、CPUが装置側のメモリを、通常の主記憶と同じようにロード・ストア命令で読み書きするためのプロトコルである。これらの組み合わせによって、装置は三つの型に分けられる。Type 1は、CXL.ioとCXL.cacheを用い、自身のメモリを持たないアクセラレータ（スマートNICなど）である。Type 2は、三つすべてを用い、自身のメモリをCPUと一貫性を保って共有するアクセラレータ（[[GPU]]など）である。Type 3は、CXL.ioとCXL.memを用い、CPUにメモリの容量を提供する装置であり、その代表が主記憶を増設するメモリ拡張装置である。

Linuxでは、Type 3の装置のメモリは、CPUを持たない独立したNUMAノードとして主記憶に追加されるか、[[devdax]]のデバイスとしてアプリケーションに直接写像される。CXLで接続したメモリは、CPUに直接接続されたDRAMより[[Latency|レイテンシ]]が大きく、一般に百数十から二百ナノ秒程度の上乗せがあるとされる。

## どこで出てくるか
CXLは、データセンターやHPCにおけるメモリの容量と柔軟性の問題に対する主要な技術として注目されている。[[LLM]]の推論のようにメモリの容量を大量に必要とする処理では、CPUのメモリスロットの数に縛られずに主記憶を増やせることが利点となる。CXL 2.0以降のプーリングや共有では、複数のサーバが一つのメモリ装置を分け合い、必要に応じて容量を割り当てることで、メモリの使用効率を高められる。

研究の観点では、速いDRAMと遅いCXLメモリが混在する階層メモリにおいて、どのデータをどちらに置くかの管理が中心的な課題となる。OSがページのアクセス頻度を監視して、頻繁に使われるページを速いメモリへ移す手法などが研究されている。これは、[[Virtual Memory|仮想記憶]]のページ管理や、[[Page Cache|ページキャッシュ]]、記憶階層の間のデータ配置の問題の延長にある。また、[[Intel Optane Persistent Memory|永続メモリ]]の研究で扱われた、CPUからバイト単位で直接アクセスする記憶の考え方は、CXLで接続したメモリの議論に引き継がれている。

## 関係
- 使う / 使われる: [[devdax]]（CXLメモリの利用形態の一つ）
- 対比: [[Intel Optane Persistent Memory]]（DIMMスロットに装着する不揮発性メモリ）
- 関連: [[Virtual Memory]], [[Latency]], [[Bandwidth]], [[GPU]], [[LLM]], [[KV Cache]], [[NVMe]]

## 出典
- [About CXL - Compute Express Link Consortium](https://computeexpresslink.org/about-cxl/)
- [Compute Express Link - Wikipedia](https://en.wikipedia.org/wiki/Compute_Express_Link)
- [Devices and Protocols - The Linux Kernel documentation](https://docs.kernel.org/driver-api/cxl/devices/device-types.html)
- [Compute Express Link - The Linux Kernel documentation](https://docs.kernel.org/driver-api/cxl/index.html)
