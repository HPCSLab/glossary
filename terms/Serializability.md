---
aliases: [直列化可能性, 直列化可能, Serializable, シリアライザビリティ, 直列可能性, Strict Serializability, 厳密直列化可能性, Strong Serializability]
tags: [term]
maps: ["[[Databases]]", "[[Distributed Systems]]"]
status: draft
updated: 2026-10-11
---
# Serializability（直列化可能性）

> 並行に実行された複数のトランザクションの結果が、それらを何らかの順序で一つずつ実行した場合の結果と同じになることを要求する、トランザクションの正しさの基準である。

## 概要
データベースでは、複数の読み書きをまとめた[[Transaction|トランザクション]]を並行に実行して性能を得る。しかし操作が無秩序に交錯すると、他のトランザクションが途中まで書いた値を読むなどして、どの逐次実行でも起こりえない結果が生じる。直列化可能性は、並行実行の結果が、全トランザクションをある一列の順序で一つずつ実行した結果と等しいことを要求する。利用者は、各トランザクションが単独で実行されたものとして正しさを考えればよい。ACIDの I（Isolation、隔離性）の最も強い水準であり、SQLの標準の隔離水準 `SERIALIZABLE` もこの性質で定義されている。Papadimitriouは1979年に、与えられた実行の履歴が直列化可能かを判定する問題がNP完全であることを示した。そのため実際のシステムは、履歴を事後に判定するのではなく、[[Two-Phase Locking|二相ロック]]などの同時実行制御によって、直列化可能な履歴しか生じないようにする。

直列化可能性が要求するのは「何らかの」逐次順序の存在だけであり、その順序が実時間と一致することは要求しない。そのため、トランザクションT1のコミットが完了した後に開始したT2が、T1の書き込みを含まない古い状態を読むことも、T2をT1より前に置けば直列化可能である。この点が[[Linearizability|線形化可能性]]との本質的な違いである。両者は次のように比較できる。

| 観点 | 直列化可能性 | 線形化可能性 |
| --- | --- | --- |
| 対象 | 複数のオブジェクトにまたがるトランザクション | 単一のオブジェクトに対する単一の操作 |
| 順序の条件 | 何らかの逐次順序が存在すればよい | 逐次順序が実時間の順序と一致する |
| 局所性 | 持たない（オブジェクトごとに満たしても全体で満たすとは限らない） | 持つ（オブジェクトごとに満たせば全体で満たす） |
| 由来 | データベース | 並行プログラミング・分散システム |

両者を合わせた基準、すなわち直列化可能であり、かつその順序が実時間と一致することを要求するものを厳密直列化可能性（strict serializability）と呼ぶ。線形化可能性は、各トランザクションが一つのオブジェクトに対する一つの操作だけからなる場合の厳密直列化可能性とみなせる。読み書きのロックをトランザクションの終了まで保持する二相ロックは厳密直列化可能性を満たすが、[[MVCC]]に基づく実装には、直列化可能であっても厳密ではないものがある。

## どこで出てくるか
データベースの隔離水準の議論で、最も強い基準として現れる。SQLの標準は、`SERIALIZABLE` より弱い水準を、ダーティリード、反復不能読み込み、ファントムといった、許してよい異常現象によって定めている。多くのデータベースは既定では直列化可能性を提供せず、例えばPostgreSQLの既定は Read Committed である。PostgreSQLの `SERIALIZABLE` は、[[MVCC]]によるスナップショット分離に、直列化の異常を検出する検査を加えたSerializable Snapshot Isolationで実装されている。異常を検出するとトランザクションの一つを中断し、SQLSTATE `40001` のエラーを返すため、アプリケーションはトランザクションを再試行できるように書く必要がある。

分散データベースでは、直列化可能性に実時間の条件を加えた厳密直列化可能性が「強い一貫性」として掲げられる。[[Spanner]]は、トランザクションのコミットの順序を実時間の順序と一致させる外部一貫性を提供しており、これを直列化可能性より強い性質と説明している。直列化可能性も線形化可能性も、ネットワークの分断の下で全ノードが応答し続けることとは両立しないため、可用性や[[Latency|レイテンシ]]を優先するシステムは、より弱い[[Consistency Model|一貫性モデル]]や隔離水準を採用する。

## 関係
- 上位概念: [[Consistency Model]]
- 前提: [[Transaction]]
- 対比: [[Linearizability]]（単一オブジェクトの単一操作が対象で、実時間の順序を要求する）
- 使う / 使われる: [[Two-Phase Locking]], [[MVCC]], [[Spanner]]
- 関連: [[Snapshot Isolation]], [[Isolation Level]]

## 出典
- [Serializability of Concurrent Data Base Updates (Papadimitriou, MIT-LCS-TR-210, 1979)](https://dspace.mit.edu/handle/1721.1/149497)
- [Linearizability versus Serializability (Peter Bailis, 2014)](http://www.bailis.org/blog/linearizability-versus-serializability/)
- [Serializability - Jepsen](https://jepsen.io/consistency/models/serializable)
- [Strict Serializability - Jepsen](https://jepsen.io/consistency/models/strict-serializable)
- [Transaction Isolation - PostgreSQL Documentation](https://www.postgresql.org/docs/current/transaction-iso.html)
- [Linearizability: A Correctness Condition for Concurrent Objects (Herlihy and Wing, ACM TOPLAS, 1990)](https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf)
