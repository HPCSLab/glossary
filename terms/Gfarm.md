---
aliases: [gfarm, Gfarm file system, Gfarmファイルシステム, Grid Datafarm, gfmd, gfsd, gfarm2fs, GfarmFS-FUSE, Gfarm/BB, HPCI共用ストレージ, HPCI Shared Storage]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# Gfarm

> 多数の計算機のローカルな記憶装置を束ねて、一つの共有のファイルシステムとして提供する、筑波大学などが開発するオープンソースの[[Distributed File System|分散ファイルシステム]]である。

## 概要
Gfarmは、2000年ごろから研究開発が続けられており、Grid Datafarmの構想（建部らによる2002年のCCGridの論文）に始まる。ローカルエリアネットワークの多数の計算機、一つのクラスタの[[Compute Node|計算ノード]]、さらには広域に分散した複数のクラスタのローカルな記憶装置をまとめ、大規模で高性能な共有のファイルシステムとする。

Gfarmは、三種類のノードからなる。利用者が使うクライアントノード、データを格納し、ファイルの読み書きや複製を担うデーモン（gfsd）が動くファイルシステムノード、ファイルの[[Metadata|メタデータ]]を管理するサーバ（gfmd）が動くメタデータサーバノードである。Gfarmの特徴は、ファイルシステムノード自身がGfarmのクライアントにもなる点であり、各ノードが自分の記憶装置にあるファイルを読み書きすることで、ノード数に応じて拡張する入出力の性能を得る。また、ファイルの複製を複数のノードに置き、どこに置くかを細かく制御できる。これにより、[[NFS]]などで問題となるアクセスの集中による性能の低下を防ぎ、故障や災害への耐性も得る。データの静かな破損を検出する機能も持つ。

Gfarmには、Gfarmのコマンドと独自のAPIで使う方法のほか、[[FUSE]]を用いたgfarm2fsでLinuxのクライアントにマウントし、アプリケーションから透過的に使う方法がある。

## どこで出てくるか
[[HPCI]]共用ストレージは、Gfarmを用いて、全国のHPCIの計算資源から一つのファイルシステムとしてデータを共有できるようにしている。東京大学（柏）と[[RIKEN|理化学研究所]]計算科学研究センター（神戸）の二つの拠点からなり、拠点の間でデータを複製して信頼性を高めている。容量は論理45PB（物理90PB）である。

計算ノードのローカルな記憶装置をジョブの間だけ束ねる[[Ad Hoc File System|アドホックファイルシステム]]として、Gfarmを[[Burst Buffer|バーストバッファ]]に用いるGfarm/BBも提案されている（Journal of Computer Science and Technology、2020年）。同じく建部らが開発する[[CHFS]]は、ノードのローカルな[[Intel Optane Persistent Memory|永続メモリ]]や[[NVMe]] SSDを用いる並列キャッシュファイルシステムである。

## 関係
- 上位概念: [[Distributed File System]]
- 使う / 使われる: [[FUSE]], [[Metadata]], [[Node-local Storage]]
- 関連: [[CHFS]], [[Ad Hoc File System]], [[Lustre]], [[NFS]]

## 出典
- [Gfarm - OSS Tsukuba](https://oss-tsukuba.org/en/software/gfarm)
- [oss-tsukuba/gfarm - GitHub](https://github.com/oss-tsukuba/gfarm)（OVERVIEW.en）
- [Gfarm Grid File System (Tatebe, Hiraga, Soda, New Generation Computing, 2010)](https://doi.org/10.1007/s00354-009-0089-5)
- [Grid Datafarm Architecture for Petascale Data Intensive Computing (Tatebe et al., CCGrid 2002)](https://doi.org/10.1109/CCGRID.2002.1017117)
- [Gfarm/BB - Gfarm file system for node-local burst buffer (Tatebe, Moriwake, Oyama, JCST 2020)](https://doi.org/10.1007/s11390-020-9803-z)
- [HPCI共用ストレージ概要・構成 - HPCI](https://www.hpci-office.jp/info/pages/viewpage.action?pageId=111380786)
