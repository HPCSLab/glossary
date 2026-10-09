---
aliases: [libpmemkv, PMemKV, cmap, vsmap, vcmap, csmap]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# pmemkv

> [[Intel Optane Persistent Memory|永続メモリ]]に最適化された、Intelが開発したローカルな組込み型の[[Key-Value Store|キーバリューストア]]である。現在は開発が終了している。

## 概要
pmemkvは、アプリケーションのプロセスの中にライブラリとして組み込んで用いるキーバリューストアであり、`put`、`get`、`remove` などの共通のAPIを持つ。C/C++のAPIのほか、Java、Node.js、Python、Rubyのバインディングがある。

pmemkvは、実装の異なる複数のストレージエンジンを持ち、同じAPIのまま、実行時にエンジンの名前を指定して切り替えられる。エンジンは三つの性質で区別される。第一は永続性であり、永続的なエンジンはクラッシュや電源断の後も内容が一貫した状態で残るが、低速である。揮発的なエンジンは高速だが、データベースを閉じると内容は失われる。第二は並行性であり、並行なエンジンでは複数の[[Thread|スレッド]]から同時に読み書きでき、更新の拡張性が高い。第三は整列であり、整列されたエンジンでは、あるキーより大きい（小さい）キーの範囲を問い合わせられる。最も成熟し、永続的な用途に推奨されるエンジンはcmapであり、PMDKのC++ライブラリ（libpmemobj-cpp）の永続的な並行ハッシュマップを用いる。このほか、揮発的な整列されたマップのvsmap、揮発的な並行マップのvcmap、実験的な永続的エンジン（csmap、radixなど）がある。

永続的なエンジンは、PMDKを介して永続メモリにアクセスし、DAXに対応したファイルシステム（fsdax）上のファイル、またはDAXのデバイス（[[devdax]]）を用いる。データベースを開く際には、設定で、プールのファイルのパス（`path`）、大きさ（`size`）、存在しない場合に作成するか（`create_if_missing`）などを指定する。

## どこで出てくるか
pmemkvは、永続メモリを用いるストレージの研究で、永続メモリ上のキーバリューストアの部品として用いられた。例えば、[[Ad Hoc File System|アドホックファイルシステム]]の[[CHFS]]は、ファイルのデータと[[Metadata|メタデータ]]をpmemkvに格納する。

ただし、IntelはPMDKの長期的な方針の見直しに伴い、pmemkvの開発、保守、不具合の修正を終了しており、2023年3月にリポジトリは読み取り専用となった。Optaneの製品自体も終息しているため、新たに用いる際や、pmemkvに依存するソフトウェアを構築する際には、この状況を前提とする必要がある。

## 関係
- 上位概念: [[Key-Value Store]]
- 前提: [[Intel Optane Persistent Memory]]
- 使う / 使われる: [[devdax]], [[CHFS]]
- 関連: [[Crash Consistency]], [[Thread]]

## 出典
- [pmem/pmemkv - GitHub](https://github.com/pmem/pmemkv)
- [libpmemkv(7) - pmemkv](https://github.com/pmem/pmemkv/blob/master/doc/libpmemkv.7.md)
- [pmemkv - pmem.io](https://pmem.io/pmemkv/)
- [Update on PMDK and our long term support strategy - pmem.io](https://pmem.io/blog/2022/11/update-on-pmdk-and-our-long-term-support-strategy/)
