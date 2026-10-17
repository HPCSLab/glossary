---
aliases: [書き込みスキュー, ライトスキュー, Write-Skew, A5B, Predicate-Based Write Skew, 述語に基づく書き込みスキュー]
tags: [term]
maps: ["[[Databases]]"]
status: draft
updated: 2026-10-18
---
# Write Skew（書き込みスキュー）

> 並行する二つのトランザクションが同じデータを読み、それぞれが読んだ値に基づいて異なる項目を書き込むことで、各トランザクションは単独では守っている複数の項目にまたがる制約が、両方のコミット後に破られる異常である。

## 概要
書き込みスキューは、[[MVCC]]によるスナップショット分離（snapshot isolation）で起こる代表的な異常である。スナップショット分離では、各[[Transaction|トランザクション]]は開始時のスナップショットを読み、並行する二つのトランザクションが同じ項目を書いた場合は、先にコミットした方だけを成功させる（first-committer-wins）。この規則によって、二つの更新の一方が失われる異常は防げるが、書き込む項目が異なれば何も検出されない。BerensonらはSQLの隔離水準を論じた1995年の論文でこの異常をA5Bと名付け、スナップショット分離では書き込みスキューが起こりうることを示した。

Feketeらは、二つの口座の残高XとYについて、合計が正であれば一方は負になってもよいという制約（X + Y > 0）の例を示している。X = 70, Y = 80 のとき、T1はXとYを読み、合計が150なのでXから100を引いても制約を守れると判断する。並行するT2も同じスナップショットを読み、Yから100を引く。各トランザクションは単独では正しいが、両方がコミットすると X = −30, Y = −20 となり、制約が破られる。どちらの順に一つずつ実行しても、後のトランザクションは合計が50であることを読んで引き出しをやめるため、この結果はどの直列の実行とも一致せず、[[Serializability|直列化可能性]]を満たさない。

![[Write Skew Under Snapshot Isolation.excalidraw]]

読んだ項目が存在しない場合にも同じ異常が起こる。例えば「一人の従業員に同じ日に8時間を超える仕事を割り当てない」という制約の下で、二つのトランザクションがそれぞれ該当する割り当てが無いことを確かめ、5時間の割り当てを別々の行として挿入すると、合計10時間となる。これは述語に基づく書き込みスキュー（predicate-based write skew）と呼ばれる。

トランザクションの間の依存関係をグラフで表すと、書き込みスキューは、一方が読んだ項目をもう一方が書くという読み書きの逆依存（rw）が、二つのトランザクションの間で互いに向き合う閉路になる。Feketeらは2005年に、スナップショット分離の下で直列化可能でない実行には、並行するトランザクションの間のrwの辺が二本続く部分を含む閉路が必ず存在することを示した。Cahillらは2008年にこれを基に、実行時にこの構造を検出してトランザクションを中断するSerializable Snapshot Isolation（SSI）を提案した。

## どこで出てくるか
データベースの隔離水準の議論で、スナップショット分離と直列化可能性の違いを示す例として現れる。PostgreSQLの `REPEATABLE READ` はスナップショット分離で実装されており、書き込みスキューを防がない。`SERIALIZABLE` はSSIで実装されており、異常を検出するとSQLSTATE `40001` のエラーでトランザクションの一つを中断する。Oracleの `SERIALIZABLE` もスナップショット分離であり、書き込みスキューが起こりうる。直列化可能でない隔離水準のまま書き込みスキューを防ぐには、`SELECT ... FOR UPDATE` などで読んだ項目にも書き込みと同じ衝突を起こさせる方法や、制約を表す別の項目を用意して関係する全てのトランザクションにそれを更新させ、衝突を表に出す方法がある。

## 関係
- 前提: [[Snapshot Isolation]], [[Transaction]]
- 対比: [[Serializability]]（書き込みスキューを含む全ての直列化の異常を許さない）
- 使う / 使われる: [[MVCC]]
- 関連: [[Isolation Level]], [[Two-Phase Locking]], [[Consistency Model]]

## 出典
- [A Critique of ANSI SQL Isolation Levels (Berenson et al., SIGMOD 1995)](https://arxiv.org/abs/cs/0701157)
- [Making Snapshot Isolation Serializable (Fekete et al., ACM TODS, 2005)](https://classpages.cselabs.umn.edu/Spring-2018/csci8980/Papers/ConcurrencyControl/serializable-snapshot.pdf)
- [Serializable Isolation for Snapshot Databases (Cahill, Röhm, and Fekete, SIGMOD 2008)](https://courses.cs.washington.edu/courses/csep544/09sp/resources/fekete-sigmod2008.pdf)
- [Serializable Snapshot Isolation in PostgreSQL (Ports and Grittner, VLDB 2012)](https://arxiv.org/abs/1208.4179)
- [Transaction Isolation (PostgreSQL Documentation)](https://www.postgresql.org/docs/current/transaction-iso.html)
