---
aliases: [2PC, 二相コミット, 2相コミット, ツーフェーズコミット, 二段階コミット, Atomic Commit, アトミックコミット, Prepared State, XA, Three-Phase Commit, 3PC, 三相コミット, PREPARE TRANSACTION]
tags: [term]
maps: ["[[Distributed Systems]]", "[[Databases]]"]
status: draft
updated: 2026-10-11
---
# Two-Phase Commit（二相コミット）

> 複数のノードにまたがるトランザクションについて、全参加者がコミットするか全参加者が中断するかのどちらかに揃えるための手順である。

## 概要
一つの[[Transaction|トランザクション]]が複数のデータベースやノードのデータを更新するとき、ある参加者だけがコミットし、別の参加者が中断すると、データが不整合になる。二相コミットは、調整役（コーディネータ、トランザクションマネージャ）がこれを揃える。第一相では、調整役が各参加者に準備を求める。各参加者は、後で確実にコミットできるよう更新内容を安定記憶に書き込んだうえで準備完了（prepared）の状態に入り、その旨を返す。いずれかの参加者が準備できなければ全体を中断する。第二相では、全参加者の準備完了を受け取った調整役がコミットを決定し、その決定を記録してから各参加者に伝える。準備完了の状態に入った参加者は、もはや自分の判断で中断できず、調整役の決定を待つ。

この最後の性質が二相コミットの弱点である。全参加者が準備完了を返した直後に調整役が故障すると、参加者は全体がコミットされたのか中断されたのかを知ることができず、調整役が復旧するまで先に進めない（ブロッキング）。その間、参加者はロックを保持し続ける。単一のプロセスの故障で止まらないようにした手順は三相コミット（three-phase commit）と総称されるが、GrayとLamportは、明確な正しさの条件を満たすことが証明された完全なアルゴリズムは知られていないと指摘し、代わりに調整役の決定を[[Paxos]]による[[Consensus|合意]]で複製するPaxos Commitを提案した。二相コミットは、その故障を一つも許容しない特殊な場合にあたる。

## どこで出てくるか
分散データベースが、複数の断片にまたがるトランザクションを不可分にする手順として現れる。[[Spanner]]は、各断片をPaxosで複製したうえで、断片のリーダーどうしで二相コミットを行う。論文は、Paxosの上で二相コミットを動かすことで、二相コミットの可用性の問題が緩和されるとしている。単体のデータベースでも、外部のトランザクションマネージャが複数のデータベースをまとめてコミットするための機能（X/Open XAなど）として提供されている。PostgreSQLでは `PREPARE TRANSACTION` で準備完了の状態に入り、後から `COMMIT PREPARED` か `ROLLBACK PREPARED` で決着させる。準備完了のまま放置されたトランザクションはロックを持ち続け、`VACUUM` による領域の回収も妨げる。

名前の似た[[Two-Phase Locking|二相ロック]]とは別物である。二相コミットは全参加者の結果を揃える手順（ACIDのA）であり、二相ロックは並行するトランザクションを互いに隔離する方式（ACIDのI）である。

## 関係
- 前提: [[Transaction]]
- 対比: [[Consensus]]（合意は過半数が動けば進むが、二相コミットは一つの参加者でも反対すれば中断し、調整役の故障で止まる）, [[Two-Phase Locking]]（名前は似るが、隔離の方式）
- 使う / 使われる: [[Spanner]], [[Paxos]]（Paxos Commit）
- 関連: [[State Machine Replication]], [[Serializability]]

## 出典
- [Consensus on Transaction Commit (Gray and Lamport, MSR-TR-2003-96)](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2003-96.pdf)
- [Consensus on Transaction Commit (arXiv:cs/0408036)](https://arxiv.org/abs/cs/0408036)
- [PREPARE TRANSACTION - PostgreSQL Documentation](https://www.postgresql.org/docs/current/sql-prepare-transaction.html)
- [Spanner: Google's Globally-Distributed Database (Corbett et al., OSDI 2012)](https://www.usenix.org/system/files/conference/osdi12/osdi12-final-16.pdf)
