---
aliases: [PCC, Persistent Client Cache, LPCC, RW-PCC, RO-PCC, lfs pcc]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# Lustre PCC（Persistent Client Cache）

> [[Lustre]]のクライアント（[[Compute Node|計算ノード]]）のローカルな記憶装置を、Lustreのファイルの[[Cache|キャッシュ]]として用いる機能であり、Lustre 2.13で導入された。

## 概要
PCC（Persistent Client Cache）は、内部に[[SSD]]などを備えたLustreのクライアントが、そのローカルな記憶装置を、Lustreのファイルのキャッシュとして用いる仕組みである。ファイルの名前空間はLustreのサーバ上に保たれたまま、ファイルの内容をクライアントのローカルな記憶装置に置いて読み書きすることで、サーバとの間の通信を減らし、性能を高める。

PCCの設計は、Lustreが本来、テープなどの大容量で低速の記憶装置とのデータの移動に用いる階層ストレージ管理（HSM）の仕組みと、ファイルのレイアウトに対するロックの仕組みに基づいている。2019年の[[SC]]で発表された論文（Qianら、"LPCC: Hierarchical Persistent Client Caching for Lustre"）は、二つの形態を示している。RW-PCCは、一台のクライアントのローカルなSSDの上に、読み書きのキャッシュを作る。RO-PCCは、複数のクライアントのSSDに、読み込み専用のキャッシュを分散して置く。

利用者は、`lfs pcc attach` によってファイルをPCCに取り込み、`lfs pcc detach` によってPCCから外す。

## どこで出てくるか
PCCは、[[Node-local Storage|ローカルストレージ]]を活用する方法の一つである。[[Ad Hoc File System|アドホックファイルシステム]]が、ジョブ用に別の一時的なファイルシステムと名前空間を作るのに対し、PCCは、Lustreの単一の名前空間を保ったまま、その一部のファイルをクライアントのローカルな記憶装置に置く。そのため、アプリケーションは、Lustre上の通常のファイルとしてアクセスしながら、ローカルな記憶装置の性能を利用できる。

## 関係
- 上位概念: [[Lustre]]
- 使う / 使われる: [[Node-local Storage]], [[SSD]]
- 対比: [[Ad Hoc File System]]（別の一時的な名前空間を作る）
- 関連: [[Parallel File System]], [[Page Cache]], [[LLIO]]

## 出典
- [Lustre Software Release 2.x Operations Manual, Chapter 27 Persistent Client Cache (PCC)](https://doc.lustre.org/lustre_manual.xhtml)
- [LPCC: Hierarchical Persistent Client Caching for Lustre - SC19](https://sc19.supercomputing.org/proceedings/tech_paper/tech_paper_pages/pap112.html)
