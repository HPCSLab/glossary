---
aliases: [オブジェクトストレージ, Object Store, オブジェクトストア, S3]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-05
---
# Object Storage（オブジェクトストレージ）

> データを、一意なキーで識別されるオブジェクトとして平坦な名前空間に格納し、オブジェクト単位で格納・取得させるストレージのモデルである。

## 概要
オブジェクトは、データ本体と、それを説明する[[Metadata|メタデータ]]（キーと値の組）からなる。オブジェクトはバケットと呼ばれる入れ物に格納され、バケット内ではキーによって一意に識別される。代表的な実装であるAmazon S3では、オブジェクトの格納（PUT）、取得（GET）、削除（DELETE）、キーの一覧（LIST）をHTTPのREST APIとして提供する。このS3 APIは事実上の標準となっており、多くのオブジェクトストレージ製品やオープンソース実装が互換インタフェースを提供している。

[[File System|ファイルシステム]]との最大の違いは、名前空間と更新の単位にある。名前空間は平坦であり、ディレクトリは存在しない。`photos/2006/sample.jpg` のようなキーは、`/` を含む一つの文字列にすぎない。LISTでプレフィックスと区切り文字を指定すると、ディレクトリのように階層的に閲覧できるが、これは文字列の前方一致による模倣である。したがって、ディレクトリの[[rename]]のような操作は不可分には行えず、配下のオブジェクトをすべて複製して削除する処理となる。更新はキー単位であり、一つのキーへのPUTは不可分で、読み手は旧データか新データのいずれかを得る。一方、複数のキーにまたがる不可分な更新はできず、同じキーへの同時書き込みは最後の書き込みが勝つ。また、一般にオブジェクトの一部だけを書き換える操作は持たず、[[POSIX]]の[[write]]のようにファイルの任意の位置を上書きすることはできない。大きなオブジェクトは、マルチパートアップロードにより、部分ごとに並列に送信してから一つのオブジェクトに結合できる。

これらの制約は、スケーラビリティの代償である。オブジェクト間の依存関係を持たず、POSIXのような強い意味論やディレクトリの整合性を維持しなくてよいため、データとメタデータを多数のサーバに分散しやすく、極めて大規模な容量と高い可用性を実現できる。なお、S3は2020年以降、オブジェクトのPUTとDELETEについて、成功の応答を受けた後の読み込みと一覧が必ずその結果を反映する、強い read-after-write 一貫性を提供している。

## どこで出てくるか
クラウドでは、オブジェクトストレージは大容量データの保管、データレイク、バックアップの標準的な置き場となっている。HPCの文脈では、POSIXの意味論が並列ファイルシステムのスケーラビリティを制約しているという問題意識から、オブジェクトストレージの考え方を取り入れたストレージ（例：[[DAOS]]）や、オブジェクトストレージを並列ファイルシステムの下位層・階層ストレージの一段として用いる構成が研究・実用されている。既存のアプリケーションからオブジェクトストレージを利用するために、[[FUSE]]でファイルシステムとして見せるツールも用いられるが、部分的な上書きやディレクトリのrenameなど、POSIXの操作の一部は非効率になるか、提供されない。オープンソースの実装としては、[[Ceph]]のRADOS Gatewayなどがある。

## 関係
- 対比: [[File System]]（階層的な名前空間とPOSIXの意味論を持つ）, [[Block Storage]]（番号で指定するブロックを単位とする）
- 関連: [[POSIX]], [[FUSE]], [[DAOS]], [[Ceph]], [[Consistency Model]]

## 出典
- [What is Amazon S3? - Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [Organizing objects using prefixes - Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html)
- [Uploading and copying objects using multipart upload in Amazon S3 - Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)
