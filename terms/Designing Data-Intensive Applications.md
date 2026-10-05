---
aliases: [データ指向アプリケーションデザイン, DDIA, Designing Data-Intensive Applications 2nd Edition, Martin Kleppmann]
tags: [term, book]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-06
---
# Designing Data-Intensive Applications（データ指向アプリケーションデザイン）

> Martin Kleppmannによる、データベース、分散システム、データ処理の仕組みと設計上のトレードオフを、原理から体系的に解説した書籍である。

## 概要
原著 *Designing Data-Intensive Applications* はO'Reillyから刊行され、通称DDIAと呼ばれる。日本語訳は『データ指向アプリケーションデザイン ―信頼性、拡張性、保守性の高い分散システム設計の原理』（斉藤太郎 監訳、玉川竜司 訳、オライリー・ジャパン、2019年）である。2026年3月には、Chris Riccomini を共著者に加えた第2版が刊行され、主要なクラウドサービスの設計などが新たに扱われている。

本書は、個々の製品の使い方ではなく、多様なデータシステムに共通する基本的な考え方を比較し、それぞれの長所と短所、トレードオフを説明することを目的とする。学術研究の成果と、大規模な実システムでの実践の両方を踏まえている。内容は大きく三部に分かれる。第一部はデータシステムの基礎であり、信頼性・拡張性・保守性という目標、データモデルと問い合わせ言語、記憶と検索のための構造（[[LSM-Tree|LSM木]]とB木など）、データの符号化を扱う。第二部は分散データであり、複製、分割（パーティショニング）、トランザクション、分散システムに固有の問題、そして[[Consistency Model|一貫性]]と[[Consensus|合意]]を扱う。第三部は導出データであり、バッチ処理、ストリーム処理、それらを組み合わせたシステムの設計を扱う。

## どこで出てくるか
本書は、分散システムとデータベースの考え方を学ぶための標準的な入門書として、研究者と実務者の双方に広く読まれている。このノート群で扱った[[Key-Value Store|キーバリューストア]]、[[LSM-Tree|LSM木]]、[[Bloom Filter|ブルームフィルタ]]、[[Linearizability|線形化可能性]]、[[Consistency Model|一貫性モデル]]、[[Consensus|合意]]、[[Raft]]などの概念が、相互の関係とともに一冊にまとめられている。ストレージやHPCの研究をしていても、分散したデータをどう複製し、どこまでの一貫性を保証するかという問題には必ず出会うため、新メンバーが通読する価値の高い本である。各章の末尾には豊富な参考文献が挙げられており、原論文にたどる入口としても有用である。

## 関係
- 関連: [[Key-Value Store]], [[LSM-Tree]], [[Bloom Filter]], [[Consistency Model]], [[Linearizability]], [[Consensus]], [[Raft]], [[Systems Performance]]

## 出典
- [データ指向アプリケーションデザイン - オライリー・ジャパン](https://www.oreilly.co.jp/books/9784873118703/)
- [Designing Data-Intensive Applications](https://dataintensive.net/)
- [Designing Data-Intensive Applications, 2nd Edition - Martin Kleppmann](https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html)
