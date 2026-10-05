---
aliases: [線形化可能性, 線形化可能, Linearizable, Atomic Consistency, Strong Consistency, 強い一貫性]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-06
---
# Linearizability（線形化可能性）

> 並行に実行される各操作が、その呼び出しから応答までの間のある一瞬で不可分に実行されたかのように見えることを要求する、一貫性の基準である。

## 概要
線形化可能性は、1990年にHerlihyとWingが並行オブジェクトの正しさの条件として定義した。複数のプロセスが共有オブジェクト（レジスタ、キュー、キーバリューストアのキーなど）を並行に操作するとき、各操作は呼び出しから応答までの時間幅を持ち、他の操作と時間的に重なりうる。線形化可能であるとは、すべての操作を一列に並べた逐次的な実行が存在し、その順序が実際の時間の順序と矛盾せず、かつその逐次実行がオブジェクトの仕様どおりの結果を与えることをいう。すなわち、操作Aの応答が操作Bの呼び出しより前に返っていれば、Bは必ずAの後に実行されたものとして扱われる。利用者から見れば、システムは複製や並行性を持たない単一のオブジェクトのように振る舞う。

似た基準に、Lamportが1979年に定義した逐次一貫性（sequential consistency）がある。逐次一貫性も全操作を一列に並べられることを要求するが、各プロセス内のプログラム順序を守ればよく、異なるプロセス間の実時間の順序は問わない。そのため、あるプロセスが書き込みを完了した後に、別のプロセスが古い値を読むことが許される。線形化可能性は、この実時間の制約を加えた、より強い基準である。また、線形化可能性は局所的（local）な性質を持つ。すなわち、システム全体が線形化可能であることは、個々のオブジェクトがそれぞれ線形化可能であることと同値である。逐次一貫性はこの性質を持たない。複数のオブジェクトにまたがるトランザクションに対して同様の実時間の制約を課す基準は、厳密直列化可能性（strict serializability）と呼ばれる。

## どこで出てくるか
線形化可能性は、分散データベースや合意に基づくシステムが「強い一貫性」と称するときの、最も一般的な意味である。[[Raft]]などの[[Consensus|合意]]アルゴリズムを用いた複製は、読み込みもログを経由させるなどの配慮をすることで、線形化可能なサービスを提供できる。一方、ネットワークの分断が起きた場合、線形化可能性を保ちながらすべてのノードが応答し続けることはできない（CAP定理）。そのため、可用性や[[Latency|レイテンシ]]を優先するシステムは、より弱い[[Consistency Model|一貫性モデル]]を採用する。

ストレージの文脈では、[[POSIX]]が `write()` の後の `read()` に要求する意味論は、線形化可能性に近い強い保証である。[[Parallel File System|並列ファイルシステム]]がロックによってこれを維持するコストや、[[MPI-IO]]がそれを緩和している理由は、この観点から理解できる。システムが線形化可能性を満たすかどうかは、操作の履歴を記録して検査するツール（Jepsenなど）で検証されることがある。

## 関係
- 上位概念: [[Consistency Model]]
- 対比: 逐次一貫性（実時間の順序を要求しない。[[Consistency Model]]を参照）
- 関連: [[Consensus]], [[Raft]], [[POSIX]], [[TLA+]]

## 出典
- [Linearizability: A Correctness Condition for Concurrent Objects (Herlihy and Wing, ACM TOPLAS, 1990)](https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf)
- [Linearizability - Jepsen](https://jepsen.io/consistency/models/linearizable)
- [Sequential Consistency - Jepsen](https://jepsen.io/consistency/models/sequential)
