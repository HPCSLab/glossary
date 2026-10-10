---
aliases: [S3, Amazon Simple Storage Service, S3 API, S3互換, ShardStore, S3 Glacier]
tags: [term]
maps: ["[[HPC Storage]]", "[[Distributed Systems]]"]
status: draft
updated: 2026-10-10
---
# Amazon S3（Amazon Simple Storage Service）

> Amazon Web Servicesが提供する[[Object Storage|オブジェクトストレージ]]のサービスであり、そのAPIはオブジェクトストレージの事実上の標準となっている。

## 概要
S3は2006年3月に公開された。データはバケットの中に、キーで識別されるオブジェクトとして格納され、HTTPのAPIでPUT、GET、DELETE、LISTなどの操作を行う。オブジェクトストレージとしての基本的な性質（平坦な名前空間、オブジェクト単位の更新など）は[[Object Storage]]を参照。格納されたオブジェクトの数は、2007年の100億から、2025年には500兆に達している。AWSはS3を、99.999999999%（イレブンナイン）の耐久性を上回るよう設計していると述べている。

アクセスの頻度と取り出しの速さに応じて、複数のストレージクラスを選べる。標準のS3 Standardのほか、アクセスの少ないデータ向けのInfrequent Access、保管（アーカイブ）向けで取り出しに数分から数時間を要しうるGlacierの各クラスなどがあり、長期の保管向けのGlacier Deep Archiveが最も保管の料金が低い。

一貫性については、2020年12月以降、全てのGET、PUT、LISTに強い read-after-write 一貫性を提供している。それ以前は、書き込みが受け付けられた後、全ての読み込みに反映されるまでに短い時間差がありうる、結果整合性のモデルであった（[[Consistency Model|一貫性モデル]]を参照）。

## どこで出てくるか
クラウド上の大規模なデータの置き場として広く使われ、S3のAPIに互換のインタフェースを持つ製品やオープンソースのソフトウェアが多数ある。HPCでも、[[IOR]]がS3のAPIでの読み書きを測定でき、[[Ceph]]はS3互換のインタフェースを提供する。

S3は、大規模なサービスの正しさを形式手法で確かめた事例としても知られる。AWSは[[TLA+]]をS3などの設計に用いたと報告しているほか、S3のデータを格納する記憶ノードのサービスShardStore（[[Rust]]で書かれている）を、実装と同じ言語で書いた参照モデルとの比較などの軽量な形式手法で検証し、[[SOSP]] 2021で発表した。

## 関係
- 上位概念: [[Object Storage]]
- 使う / 使われる: [[IOR]], [[Ceph]]
- 関連: [[Consistency Model]], [[TLA+]]

## 出典
- [What is Amazon S3? - Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [Amazon S3 - Wikipedia](https://en.wikipedia.org/wiki/Amazon_S3)
- [Amazon S3 Storage Classes - AWS](https://aws.amazon.com/s3/storage-classes/)
- [Amazon S3 Strong Consistency - AWS](https://aws.amazon.com/s3/consistency/)
- [Amazon S3 Update – Strong Read-After-Write Consistency - AWS News Blog](https://aws.amazon.com/blogs/aws/amazon-s3-update-strong-read-after-write-consistency/)
- [Allen School affiliated researchers sweep the Best Paper category at SOSP 2021 - Allen School News](https://news.cs.washington.edu/2021/12/09/allen-school-affiliated-researchers-sweep-the-best-paper-category-at-sosp-2021/)
- [How automated reasoning helps us innovate at S3 scale - AWS Storage Blog](https://aws.amazon.com/blogs/storage/how-automated-reasoning-helps-us-innovate-at-s3-scale)
