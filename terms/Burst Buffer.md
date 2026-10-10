---
aliases: [バーストバッファ, Burst Buffers, Cray DataWarp, DataWarp]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# Burst Buffer（バーストバッファ）

> アプリケーションと[[Parallel File System|並列ファイルシステム]]の間に[[SSD]]などの高速な記憶の層を置き、短時間に集中するI/Oをそこで受け止めて、並列ファイルシステムとのデータの移動を計算と重ねる仕組みである。

## 概要
HPCのアプリケーションのI/Oは、計算の合間のチェックポイントのように、短時間に集中して大量の書き込みが起こる形をとる。並列ファイルシステムの多くは[[HDD]]で構成され、容量は安価に増やせるが、帯域を増やすには多数のディスクとサーバが必要になる。ピークの書き込みに合わせて並列ファイルシステムを設計すると、平常時には帯域が余る。バーストバッファは、帯域あたりの価格が安いSSDの層でピークを受け止め、並列ファイルシステムへの書き戻しを計算と並行して行う。これにより、並列ファイルシステムは容量と信頼性を主として設計できる。Liuらは2012年に、バーストバッファによって、アプリケーションから見た外部の記憶装置への[[Bandwidth|スループット]]を高めつつ、外部の記憶装置に必要な帯域を減らせることを示した。

バーストバッファの構成は二つに大別される。一つは、SSDを搭載した専用のサーバを計算機の[[Interconnect|相互結合網]]に接続し、全ての計算ノードから共有する構成である。CrayのDataWarpはこの例であり、ジョブスクリプトの指示に応じてジョブスケジューラがSSDの領域をジョブに割り当てる。DDNの[[DDN IME]]もこの構成をとる。もう一つは、各[[Compute Node|計算ノード]]に[[NVMe]] SSDを搭載する[[Node-local Storage|ノードローカル]]な構成である。米国の[[ORNL|Summit]]は、各計算ノードに1.6TBのNVMe SSDを搭載し、これをバーストバッファと呼んでいた。ノードローカルな構成では、ノードの記憶装置を束ねて共有の名前空間を作る[[Ad Hoc File System|アドホックファイルシステム]]が用いられ、[[GekkoFS]]や[[UnifyFS]]は自らをバーストバッファのためのファイルシステムと位置付けている。

いずれの構成でも、必要な入力をジョブの開始前に読み込み（ステージイン）、残す結果を終了前に並列ファイルシステムへ書き戻す（ステージアウト）作業が必要となる。この移動をユーザが明示的に行うか、キャッシュとしてシステムが自動的に行うかは、実装によって異なる。

## どこで出てくるか
バーストバッファは、HPCストレージの研究で、並列ファイルシステムとアプリケーションの間の階層として広く用いられる言葉である。ただし、その指す範囲は文献によって異なり、専用のサーバによる共有の層を指す場合も、ノードローカルなSSDを指す場合もある。論文を読む際には、どちらの構成か、データの移動を誰が行うかを確かめる必要がある。[[IOR]]によるチェックポイント型の書き込みの評価や、[[Slurm]]などのジョブスケジューラとの統合が、典型的な論点である。

## 関係
- 前提: [[Parallel File System]], [[SSD]]
- 使う / 使われる: [[DDN IME]], [[Ad Hoc File System]], [[GekkoFS]], [[UnifyFS]]
- 関連: [[Node-local Storage]], [[NVMe]], [[Lustre PCC]], [[LLIO]]

## 出典
- [On the Role of Burst Buffers in Leadership-class Storage Systems (Liu et al., MSST 2012)](https://doi.org/10.1109/MSST.2012.6232369)
- [Architecture and Design of Cray DataWarp (Henseler et al., CUG 2016)](https://cug.org/proceedings/cug2016_proceedings.orig/includes/files/pap105.pdf)
- [Summit User Guide: Burst Buffer - OLCF](https://docs.olcf.ornl.gov/systems/summit_user_guide.html)
