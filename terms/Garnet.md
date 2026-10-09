---
aliases: [garnet, Microsoft Garnet, Tsavorite, FASTER, RESP, Redis Serialization Protocol]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-09
---
# Garnet

> Microsoft Researchが開発した、ネットワーク越しに使うキャッシュのための[[Key-Value Store|キーバリューストア]]（キャッシュストア）であり、Redisのプロトコルに対応し、既存のRedisのクライアントからそのまま使える。

## 概要
Garnetは、2024年3月にMicrosoft Researchがオープンソース（MITライセンス）として公開した。Redisの通信のプロトコル（RESP）に対応しているため、多くのプログラミング言語の既存のRedisのクライアントを改変せずに使える。文字列の取得と設定やキーの有効期限、HyperLogLogやビットマップ、ソート済み集合やリストなどの操作のほか、複数のキーにまたがるトランザクションや、C#で書くサーバ側の手続き、Luaのスクリプトを扱える。.NETで書かれ、LinuxとWindowsで動作する。

Garnetの記憶の層はTsavoriteと呼ばれ、Microsoft Researchの以前のキーバリューストアFASTERのフォークである。Tsavoriteは、スレッドの数に応じた拡張性、主記憶・[[SSD]]・クラウドのストレージにまたがる階層的な格納、止まらないチェックポイントと回復、永続化のための操作のログなどを備える。Garnetは、文字列の操作に向けた主ストアと、複雑なデータ型に向けたオブジェクトストアの、二つのTsavoriteのストアを、一つの操作のログで束ねる。Tsavoriteの読み出し、追加・更新（upsert）、削除、不可分な読み出しと更新という少数の操作の上に、多数のRedisのコマンドを実装している。

ネットワークの層では、TLSの処理と記憶の層の操作を、ネットワークのI/Oの完了を受け取ったスレッドの上でそのまま行い、多くの場合スレッドの切り替えを避ける。複数のノードからなるクラスタの形態では、シャーディング、複製、キーの動的な移動に対応し、標準のRedisのクラスタのコマンドで管理できる。ただし、クラスタの形態は受け身であり、リーダの選出は行わず、利用者が用意する制御の仕組みからの指示に従う。

## どこで出てくるか
Microsoftの比較では、Garnetは、Redis、KeyDB、[[DragonflyDB|Dragonfly]]と比べて、クライアントの接続の数が多い場合によく拡張し、高い処理能力と、99パーセンタイルや99.9パーセンタイルでの安定した[[Latency|レイテンシ]]を示したとしている。Microsoftの内部の複数の業務で用いられており、Azure Cosmos DB Garnet Cacheとして管理されたサービスも提供されている。設計の論文は、2026年のVLDB（PVLDB 第19巻）で発表されている。最近では、[[Vector Database|DiskANN]]のアルゴリズムによる近似最近傍探索（Vector Sets）も試験的に提供している。

## 関係
- 上位概念: [[Key-Value Store]]
- 使う / 使われる: [[SSD]], [[Vector Database]]
- 対比: [[RocksDB]]（組み込み型の永続的なKVS）
- 関連: [[Latency]]

## 出典
- [microsoft/garnet - GitHub](https://github.com/microsoft/garnet)
- [Introducing Garnet - Microsoft Research Blog (2024年3月18日)](https://www.microsoft.com/en-us/research/blog/introducing-garnet-an-open-source-next-generation-faster-cache-store-for-accelerating-applications-and-services/)
- [Garnet: A Next-Generation Cache-Store for Accelerating Applications and Services (Chandramouli et al., PVLDB 2026)](https://www.vldb.org/pvldb/vol19/p224-chandramouli.pdf)
