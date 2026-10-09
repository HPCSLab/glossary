---
aliases: [beegfs, FhGFS, Fraunhofer File System, ThinkParQ]
tags: [term]
maps: ["[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# BeeGFS

> ドイツのFraunhoferで開発された、HPC向けの[[Parallel File System|並列ファイルシステム]]であり、サーバがユーザ空間のデーモンとして動く点に特徴がある。

## 概要
BeeGFSは、ドイツのFraunhoferのHPCの研究センターで、2005年に開発が始まった。2007年に初めて公開され、当初はFhGFSと呼ばれた。2014年にFraunhoferからスピンオフしたThinkParQが設立され、名前がBeeGFSに改められた。無償で利用できるCommunity Editionと、サポートの契約を伴うEnterprise Editionがある。

BeeGFSは、管理（management）、メタデータ（metadata）、ストレージ（storage）、クライアント（client）の四つのサービスからなる。ファイルの内容は複数のストレージのターゲットにストライプされ、並列に読み書きされる。[[Metadata|メタデータ]]はディレクトリの単位で複数のメタデータサーバに分散される。サーバは、OSに特別な要求のない通常のユーザ空間のデーモンとして動き、クライアントはLinuxのカーネルモジュールとして通常のマウントポイントを提供する。二つのターゲットの間でデータを複製するbuddy groupによる冗長化にも対応する。

## どこで出てくるか
BeeGFSは、[[Lustre]]や[[IBM Storage Scale]]と並ぶHPC向けの並列ファイルシステムであり、[[TOP500]]に載るいくつかのスーパーコンピュータで用いられている。ジョブに割り当てられた[[Compute Node|計算ノード]]のローカルな記憶装置を束ね、ジョブの間だけ一時的なBeeGFSを作るBeeONDは、[[Ad Hoc File System|アドホックファイルシステム]]の代表的な例である。

## 関係
- 上位概念: [[Parallel File System]]
- 対比: [[Lustre]], [[IBM Storage Scale]]
- 関連: [[Ad Hoc File System]], [[Metadata]], [[Node-local Storage]]

## 出典
- [BeeGFS - Wikipedia](https://en.wikipedia.org/wiki/BeeGFS)
- [Overview - BeeGFS Documentation](https://doc.beegfs.io/latest/architecture/overview.html)
