---
aliases: [TLA, Temporal Logic of Actions, TLC, TLC Model Checker, TLAPS, PlusCal, 形式仕様, Formal Specification]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-06
---
# TLA+

> Leslie Lamportが考案した、並行システムや分散システムの設計を数学的に記述し、その正しさを検査するための形式仕様記述言語である。

## 概要
TLA+は、行動の時相論理（Temporal Logic of Actions、TLA）に集合論を組み合わせた言語であり、1999年に発表された。2002年には解説書 *Specifying Systems* が刊行されている。TLA+はプログラミング言語ではなく、実装の詳細を省いた高い抽象度で、システムが取りうる状態とその遷移を記述する。設計段階の根本的な誤りは、コードになってからでは発見も修正も難しいため、それを実装前に見つけることを目的とする。

TLA+では、システムを変数の値の組である状態の列として捉える。仕様は主に二つの述語からなる。`Init` は許される初期状態を、`Next` は一つの状態から次の状態への許される遷移を定める。仕様全体は、`Init` から始まり、各段階で `Next` を満たす（あるいは変数が変化しない）すべての振る舞いの集合として表される。この仕様に対して、満たすべき性質を記述する。性質は二種類に分けられる。安全性（safety）は「悪いことが決して起きない」ことであり、例えば「同時に二つのリーダーが存在しない」という不変条件がこれに当たる。活性（liveness）は「良いことがいずれ起きる」ことであり、例えば「要求はいずれ処理される」がこれに当たる。

検査には主に二つのツールを用いる。モデル検査器TLCは、プロセス数やメッセージ数などを小さな有限の値に限定したうえで、到達可能なすべての状態を網羅的に探索し、性質に違反する振る舞いがあれば、初期状態からそこに至る具体的な手順（反例）を示す。証明システムTLAPSは、有限の範囲に限らず性質が成り立つことを定理として証明するために用いる。また、擬似コードに近い記法で書いたアルゴリズムをTLA+に変換するPlusCalも提供されている。現在は、Linux Foundation傘下のTLA+ Foundationが普及を推進している。

## どこで出てくるか
分散システムのプロトコルは、メッセージの遅延、喪失、順序の入れ替わり、ノードの故障が組み合わさることで、人間が想定しきれないほど多くの実行順序を取りうる。テストでは稀にしか現れない誤りも、TLCは小さな構成で網羅的に探索することで発見できる。Amazon Web Servicesは2011年頃からTLA+を用い、DynamoDB、S3、EBSなどの設計で微妙な誤りを発見したと報告している。Microsoft Azure Cosmos DBの一貫性モデルの設計にも用いられている。

研究の文脈では、合意アルゴリズムなどの新しいプロトコルを提案する際に、TLA+による仕様と検査結果を併せて示すことがある。[[Raft]]の原論文も、約400行のTLA+による仕様を付している。TLA+の検査は、あくまで仕様（設計）が性質を満たすことを示すものであり、実装がその仕様に従っていることまでは保証しない点に注意を要する。

## 関係
- 使う / 使われる: [[Raft]]（TLA+で仕様が記述されている）
- 関連: [[Consensus]], [[Linearizability]], [[Model Checking]]

## 出典
- [The TLA+ Home Page - Leslie Lamport](https://lamport.azurewebsites.net/tla/tla.html)
- [TLA+ - Wikipedia](https://en.wikipedia.org/wiki/TLA%2B)
- [TLA+ Foundation](https://foundation.tlapl.us/)
- [In Search of an Understandable Consensus Algorithm (Extended Version)](https://raft.github.io/raft.pdf)
