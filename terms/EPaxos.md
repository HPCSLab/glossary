---
aliases: [Egalitarian Paxos, There Is More Consensus in Egalitarian Parliaments]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-16
---
# EPaxos

> 固定のリーダーを置かず、どの複製も命令を提案でき、互いに干渉しない命令は1往復で確定できるようにした、[[Paxos]]系の[[Consensus|合意]]アルゴリズムである。

## 概要
Multi-Paxosや[[Raft]]は、安定したリーダーが命令の順序を一つに決める。この方式は単純であるが、すべての命令がリーダーを経由するため、リーダーの負荷が処理能力の上限となり、データセンタをまたぐ広域の構成では、リーダーから遠いクライアントの[[Latency|レイテンシ]]が大きくなる。また、リーダーが故障すると、新しいリーダーが選ばれるまで命令を確定できない。EPaxos（Egalitarian Paxos）は、Moraruらが2013年の[[SOSP]]で発表したもので、この「すべての命令に一つの順序を付ける」という前提を緩めることで、リーダーへの集中を除いた。

EPaxosの出発点は、異なるオブジェクトを更新する命令のように、実行の順序を入れ替えても結果が変わらない（干渉しない）命令どうしには、順序を決める必要がないという観察である。クライアントは任意の複製に命令を送り、受け取った複製がその命令の「命令リーダー」となる。命令リーダーは、その命令が干渉する既知の命令の一覧（依存関係）を添えて他の複製に送る。故障を F 個まで許す 2F+1 個の複製のうち、F + ⌊(F+1)/2⌋ 個（命令リーダーを含む）が同じ依存関係を返せば、命令は1往復で確定する（fast path）。依存関係が食い違った場合は、F+1 個の複製との Paxos の accept に相当する2往復目で確定する（slow path）。

確定と実行は分かれている。各複製は、確定した命令と依存関係からなるグラフを作り、その強連結成分を逆トポロジカル順に、成分の中は列番号（seq）の順に実行する。これにより、すべての複製で干渉する命令が同じ順序で実行され、[[State Machine Replication|状態機械複製]]としての[[Linearizability|線形化可能性]]が保たれる。

## どこで出てくるか
広域に複製するシステムや、リーダーを持たない合意の研究では、Multi-Paxosと並ぶ比較対象としてEPaxosが用いられる。ただし、性能は命令の干渉の頻度に強く依存する。2021年の[[NSDI]]の論文 "EPaxos Revisited" は、中央値のレイテンシについての元の主張を確かめた一方、干渉が起きる負荷ではテールレイテンシがMulti-Paxosの4倍以上に悪化することを報告した。また、プロトコルが複雑で仕様の記述に曖昧さがあることも指摘されており、修正と簡略化を提案する後続の研究がある。EPaxosの結果を引用・比較する際には、評価に用いた負荷の干渉の割合を確かめる必要がある。

## 関係
- 上位概念: [[Consensus]]
- 前提: [[Paxos]], [[State Machine Replication]]
- 対比: [[Raft]]（安定したリーダーがすべての命令の順序を決める）
- 関連: [[Linearizability]], [[Latency]]

## 出典
- [There Is More Consensus in Egalitarian Parliaments (Moraru, Andersen, Kaminsky, SOSP 2013)](https://www.pdl.cmu.edu/ftp/associated/epaxos-sosp2013.pdf)
- [EPaxos Revisited (Tollman, Park, Ousterhout, NSDI 2021) - USENIX](https://www.usenix.org/conference/nsdi21/presentation/tollman)
- [Making Democracy Work: Fixing and Simplifying Egalitarian Paxos - arXiv](https://arxiv.org/abs/2511.02743)
