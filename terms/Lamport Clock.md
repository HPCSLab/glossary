---
aliases: [ランポート時計, Lamport Timestamp, ランポートタイムスタンプ, Logical Clock, 論理時計, Happened-before, Happens-before, 事前発生関係]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-16
---
# Lamport Clock（ランポート時計）

> 分散システムの各プロセスが持つ整数のカウンタであり、事象ごとに値を進め、メッセージに値を載せて受信側の値を引き上げることで、一方が他方に影響しうる二つの事象には必ず小さい値から大きい値が付くようにする論理的な時計である。

## 概要
複数の計算機の物理的な時計は完全には一致しないため、異なる計算機で起きた二つの事象のどちらが先かを、時計の値で決めることはできない。Lamportは1978年の論文で、時刻の代わりに事前発生関係（happened-before、a → b と書く）を定義した。同じプロセスでaがbより先に起きた場合、aがメッセージの送信でbがその受信である場合、およびこれらを推移的につないだ場合に a → b とする。a → b でも b → a でもない二つの事象は並行（concurrent）であり、互いに影響を与えることができない。事前発生関係は、全事象を一列に並べる全順序ではなく、並行な事象の組を含む半順序である。

ランポート時計は、この関係と矛盾しない数値を事象に付ける仕組みである。各プロセスは事象のたびにカウンタを1増やし、送信ではその値をメッセージに付ける。受信では、自分の値と受け取った値の大きい方に1を足した値を新しい値とする。こうすると、a → b ならば必ず C(a) < C(b) となる。逆は成り立たず、C(a) < C(b) であっても、aとbが因果でつながっているのか並行なのかは値からは区別できない。並行性まで判定するには、プロセスごとのカウンタの配列を持つ[[Vector Clock|ベクトルクロック]]を用いる。

![[Lamport Clock Space-Time Diagram.excalidraw]]

値が同じ事象は、プロセスの番号で順序を決めれば、事前発生関係と矛盾しない全順序が得られる。全プロセスがこの同じ順序で要求を処理すれば、プロセス間で状態を一致させられる。Lamportは論文で、この全順序を用いた分散の[[Mutex|相互排除]]を例に示した。後にLamportは、この全順序で任意の状態機械を分散して実装できることがこの論文の要点であったと述べており、これは[[State Machine Replication|状態機械複製]]の考え方につながる。

## どこで出てくるか
分散システムの論文や教科書では、プロセスを時間の軸に沿った線、事象を点、メッセージを線の間の矢印で描く時空図（space-time diagram）とともに、事前発生関係と並行性の議論に用いられる。[[Consistency Model|一貫性モデル]]のうち因果一貫性は、事前発生関係で順序づけられる操作を全員が同じ順序で観測することを要求するものであり、その定義の前提となる。[[CRDT]]の操作ベースの方式が通信に求める因果的な順序での配送も、この関係で定義される。

物理的な時計に基づく方式との対比でも用いられる。[[Spanner]]は、論理時計ではなく時刻の不確かさの幅を明示する物理時計のAPI（TrueTime）を用いて、トランザクションの順序を実時間と一致させる。ランポート時計の順序は因果関係とは矛盾しないが、因果でつながらない事象の間では実時間の順序と一致するとは限らない。

## 関係
- 対比: [[Vector Clock]]（並行な事象を判定できる）, [[Spanner]]（物理時計とその誤差の幅で順序を決める）
- 使う / 使われる: [[State Machine Replication]], [[CRDT]]
- 関連: [[Consistency Model]], [[Mutex]]

## 出典
- [Time, Clocks and the Ordering of Events in a Distributed System (Lamport, Communications of the ACM, 1978) - Microsoft Research](https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system)
- [The Writings of Leslie Lamport](https://lamport.azurewebsites.net/pubs/pubs.html)
- [Logical clocks - Rutgers University CS 417 lecture notes](https://people.cs.rutgers.edu/~pxk/classes/417/notes/logical-clocks.html)
