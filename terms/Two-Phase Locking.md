---
aliases: [2PL, 二相ロック, 二相ロッキング, 2相ロック, ツーフェーズロック, ツーフェーズロッキング, Strict Two-Phase Locking, Strict 2PL, 厳格二相ロック, Strong Strict Two-Phase Locking, SS2PL, Rigorous Two-Phase Locking]
tags: [term]
maps: ["[[Databases]]"]
status: draft
updated: 2026-10-11
---
# Two-Phase Locking（二相ロック）

> トランザクションが、ロックを一つでも解放した後には新たなロックを取得しないという規則であり、これを守れば並行実行が直列化可能になる。

## 概要
複数の[[Transaction|トランザクション]]が同じデータを並行に読み書きするとき、データごとに[[Mutex|ロック]]を取るだけでは正しさは保証されない。あるデータのロックを解放した直後に別のデータのロックを取ると、その間に他のトランザクションが割り込み、どの逐次実行とも一致しない結果が生じうる。二相ロックは、各トランザクションの実行を、ロックを取得するだけの成長相（growing phase）と、解放するだけの縮退相（shrinking phase）の二つに分ける。Eswaranらは1976年に、この規則を守れば実行が[[Serializability|直列化可能]]になることを示した。ロックには、読み込み用の共有ロックと書き込み用の排他ロックを区別するのが普通である。

基本の二相ロックでは、コミット前にロックを解放できるため、他のトランザクションがコミットされていない値を読み、書いた側が中断すると読んだ側も連鎖して中断しなければならない。そこで実際には、排他ロックをコミットか中断まで保持する厳格二相ロック（strict 2PL）や、共有ロックも含めた全てのロックを終了まで保持する方式が用いられる。後者は、直列化の順序が実時間の順序とも一致する厳密直列化可能性を満たす。また、ロックを持ったまま他のロックを待つため、二相ロックでは[[Deadlock|デッドロック]]が避けられない。データベースは、待ちの関係を調べてデッドロックを検出し、トランザクションの一つを中断して解消する。

## どこで出てくるか
ロックに基づく同時実行制御の基本形として、データベースの教科書や論文で現れる。MySQLの[[InnoDB]]は、隔離水準 `SERIALIZABLE` で通常の `SELECT` を共有ロックを取る `SELECT ... FOR SHARE` に変換し、ロックによって直列化を保つ。既定ではデッドロックを検出すると、変更した行数の少ないトランザクションを中断する。[[Spanner]]も、読み書きを行うトランザクションの同時実行制御に二相ロックを用いている。これに対し、[[MVCC]]に基づく方式は、読み込みにロックを取らないことで、読み込みと書き込みが互いを待たないようにする。

名前の似た[[Two-Phase Commit|二相コミット]]とは別物である。二相ロックは一つのデータベースの中でトランザクションを互いに隔離する方式（ACIDのI）であり、二相コミットは複数のノードにまたがるトランザクションを全体としてコミットするか中断するかを揃える手順（ACIDのA）である。分散データベースでは両者を組み合わせて用いることが多い。

## 関係
- 前提: [[Transaction]], [[Mutex]]
- 対比: [[MVCC]]（読み込みにロックを取らず、版を読ませる）, [[Two-Phase Commit]]（名前は似るが、隔離ではなく分散コミットの手順）
- 使う / 使われる: [[Serializability]]（二相ロックが保証する性質）, [[InnoDB]], [[Spanner]]
- 関連: [[Deadlock]]

## 出典
- [The Notions of Consistency and Predicate Locks in a Database System (Eswaran et al., CACM 1976)](https://doi.org/10.1145/360363.360369)
- [Linearizability versus Serializability (Peter Bailis, 2014)](http://www.bailis.org/blog/linearizability-versus-serializability/)
- [Transaction Isolation Levels - MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html)
- [Deadlock Detection - MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/innodb-deadlock-detection.html)
- [Spanner: Google's Globally-Distributed Database (Corbett et al., OSDI 2012)](https://www.usenix.org/system/files/conference/osdi12/osdi12-final-16.pdf)
