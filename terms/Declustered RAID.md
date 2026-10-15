---
aliases: [デクラスタ化RAID, Parity Declustering, パリティデクラスタリング, Declustered Parity, デクラスタ化パリティ, Declustering Ratio, Distributed Spare, 分散スペア, dRAID, DCR]
tags: [term]
maps: ["[[HPC Storage]]", "[[Storage]]"]
status: draft
updated: 2026-10-16
---
# Declustered RAID（デクラスタ化RAID）

> 一つのストライプを構成するディスクの数より多くのディスクに、ストライプごとに異なるディスクの組を選んで配置し、故障したディスクの再構築の読み書きを全ディスクに分散させる[[RAID]]の配置方式である。

## 概要
従来のRAID5では、パリティを含むストライプの断片の数Gと、アレイのディスクの数Cが等しい。一台が故障すると、生き残ったすべてのディスクの全体を読み、復元したデータを一台のスペアに書く。再構築の時間は一台のディスクの書き込みの[[Bandwidth|帯域]]で抑えられるため、大容量の[[HDD]]では長時間を要する。その間はアプリケーションへの応答が遅くなり、さらにもう一台が故障すればデータを失う。デクラスタ化は、G個の断片からなるストライプを、それより多いC台のディスクに散らして置く。ストライプごとに使うディスクの組が異なるため、ある一台が故障しても、生き残った各ディスクのうち再構築で読む部分は (G−1)/(C−1) の割合で済む。この比αをデクラスタ化率と呼び、従来のRAID5ではα=1である。この考え方は1990年にMuntzとLuiが提案し、1992年にHollandとGibsonが具体的な配置の方法と、再構築中の性能の評価を示した。

![[Declustered RAID Rebuild.excalidraw]]

読み込みの分散に加えて、スペアの領域も専用のディスクとして置かずに全ディスクに分散させる（分散スペア）と、復元したデータの書き込みも多数のディスクに分かれる。こうして一台のディスクの速度に縛られなくなり、ディスクの台数が多いほど再構築は短くなる。一方で、ストライプがディスクの多くの組み合わせにわたって置かれるため、パリティの数を超える台数が同時に故障すると、どのディスクが故障したかによらず一部のデータを失いうる。HollandとGibsonの配置では、パリティが一つの場合、C台のうちどの二台が故障してもデータを失う。このため、デクラスタ化は、二重以上のパリティを持つ[[Erasure Coding|消失訂正符号]]（8+2など）と組み合わせ、再構築を短くして二台目、三台目の故障が重なる時間を縮める形で用いられる。

## どこで出てくるか
[[Parallel File System|並列ファイルシステム]]を支えるストレージサーバの多数のディスクで用いられる。[[IBM Storage Scale]]のIBM Storage Scale RAID（GPFS Native RAIDとも呼ばれる）は、データ、冗長な情報、スペアの領域をアレイの全ディスクに分散させ、データにはReed-Solomon符号の8+2pや8+3pを用いる。[[EXAScaler|DDN]]のストレージ装置はDCR（DeClustered RAID）として同様の構成を提供する。[[ZFS]]は、OpenZFS 2.1.0から、RAID-Zの変種として分散スペアを組み込んだdRAIDを提供する。dRAIDは、固定幅のストライプにすることで、割り当て済みの領域を順に読む逐次的な再構築を可能にしている。

論文や製品の資料では、ディスク一台の故障からの再構築時間と、再構築中のアプリケーションの[[Latency|レイテンシ]]や帯域の低下が、評価の指標として示される。大容量のディスクを多数並べたストレージで、従来のRAIDの再構築時間が長くなりすぎることが、デクラスタ化が採られる理由である。

## 関係
- 上位概念: [[RAID]]
- 前提: [[Erasure Coding]]
- 対比: [[RAID]]（従来のRAID5ではストライプの幅とディスクの数が等しく、再構築で全ディスクの全体を読み、一台のスペアに書く）
- 使う / 使われる: [[IBM Storage Scale]], [[ZFS]]
- 関連: [[HDD]], [[Parallel File System]]

## 出典
- [Parity Declustering for Continuous Operation in Redundant Disk Arrays (Holland and Gibson, ASPLOS 1992)](https://www.pdl.cmu.edu/PDL-FTP/Declustering/ASPLOS.pdf)
- [Declustered RAID - IBM Spectrum Scale RAID](https://www.ibm.com/support/knowledgecenter/SSYSP8_5.0.0/com.ibm.spectrum.scale.raid.v4r22.adm.doc/bl1adv_introdeclustered.htm)
- [dRAID - OpenZFS documentation](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Pool%20Structure/dRAID%20Howto.html)
- [ESS Disk Management - IBM Community](https://community.ibm.com/community/user/blogs/archive-user/2018/01/02/ess-disk-management)
- [DDN pumps out more affordable burst buffer - The Register](https://www.theregister.co.uk/2017/11/14/ddn_pumps_out_more_affordable_burst_buffer/)
