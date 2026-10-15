---
aliases: [Conflict-free Replicated Data Type, Convergent Replicated Data Type, Commutative Replicated Data Type, 競合のない複製データ型, CvRDT, CmRDT, State-based CRDT, Operation-based CRDT, Strong Eventual Consistency, 強い結果整合性, G-Counter, PN-Counter, LWW-Register, OR-Set]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-16
---
# CRDT（競合のない複製データ型）

> 各複製が他の複製と調整せずに更新を受け付けても、同じ更新を受け取った複製どうしが必ず同じ状態に収束するように設計されたデータ型である。

## 概要
データを複数の計算機に複製し、どの複製でも即座に更新を受け付ける方式では、異なる複製で同時に行われた更新が衝突する。[[Consensus|合意]]によって更新の順序を一つに決めれば衝突は起きないが、そのためには複製の間で通信して待つ必要があり、ネットワークが分断されると更新できなくなる。CRDTはこれとは逆に、衝突しても結果が一意に決まるようにデータ型の側を設計する。Shapiroらは2011年に、この性質を強い結果整合性（strong eventual consistency）として定式化し、それを満たすための十分条件と、条件を満たすデータ型の例を示した。強い結果整合性は、[[Consistency Model|結果整合性]]に「同じ更新の集合を受け取った複製は同じ状態にある」という保証を加えたものである。

CRDTには二つの方式がある。状態ベース（CvRDT）では、複製は自分の状態全体を他の複製に送り、受け取った側は二つの状態を併合（merge）する。状態が半順序をなし、更新が状態を順序の上で増やす方向にのみ変え、併合がその半順序における最小上界（二つの状態の両方以上である最小の状態）を求める操作であれば、複製は収束する。併合は可換かつ冪等であるため、メッセージが失われたり、順序が入れ替わったり、重複して届いたりしてもよい。操作ベース（CmRDT）では、複製は行った操作を他の複製に送り、受け取った側はその操作を適用する。並行に行われた操作どうしが可換であれば、適用する順序によらず結果が一致する。ただし、各操作がすべての複製に一度ずつ、[[Lamport Clock|因果的な順序]]を守って届くことを、通信の側で保証する必要がある。

例えば、増加のみのカウンタ（G-Counter）は、複製ごとに自分の増加分を記録した配列を持ち、併合では要素ごとの最大値をとり、値はその合計とする。増減できるカウンタ（PN-Counter）は、増加用と減少用の二つのG-Counterを組み合わせる。単一の値を持つレジスタでは、並行な代入どうしは可換にならないため、タイムスタンプの最も新しい代入を採用するLWW-Register（Last-Writer-Wins）のように、どちらを残すかの規則を決める。集合では、同じ要素の追加と削除が並行に起きたときにどちらを優先するかによって、2P-SetやOR-Setなどの変種がある。

## どこで出てくるか
複数のデータセンタや端末にデータを複製し、それぞれで書き込みを受け付ける系、すなわち[[Key-Value Store|キーバリューストア]]のマルチリーダ構成や、共同編集のアプリケーションで現れる。Riak KVは、カウンタ、集合、マップなどをCRDTとして提供している。Automergeは、各端末が手元に複製を持ち、オフラインで編集した内容を後から同期する共同編集のためのCRDTのライブラリである。論文では、[[Linearizability|線形化可能性]]のような強い一貫性を合意によって実現する方式と対比され、可用性と[[Latency|遅延]]のために一貫性をどこまで緩めるかという議論の中で出てくる。収束が保証されるのはデータ型の状態についてであり、「残高を負にしない」のような全体にわたる不変条件までは保証しない点に注意が要る。

## 関係
- 上位概念: [[Consistency Model]]（強い結果整合性を実現する手段である）
- 対比: [[State Machine Replication]]（合意で操作の順序を一つに決め、すべての複製で同じ順に適用する）
- 使う / 使われる: [[Key-Value Store]]
- 関連: [[Linearizability]], [[Consensus]]

## 出典
- [A comprehensive study of Convergent and Commutative Replicated Data Types (INRIA RR-7506, 2011)](https://www.csa.iisc.ac.in/~raghavan/CleanedPods2021/crdt-shapiro-2011-techreport.pdf)
- [Conflict-free Replicated Data Types (SSS 2011) - BibTeX](https://asc.di.fct.unl.pt/~nmp/pubs/sss-2011.bib)
- [About CRDTs - crdt.tech](https://crdt.tech/)
- [Data Types - Riak KV documentation](https://docs.riak.com/riak/kv/2.2.3/learn/concepts/crdts)
- [Automerge documentation](https://automerge.org/docs/hello/)
