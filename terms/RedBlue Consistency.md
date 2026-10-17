---
aliases: [RedBlue一貫性, RedBlue整合性, Red-Blue Consistency, レッドブルー一貫性, Shadow Operation, シャドウ操作, Generator Operation, 生成操作, Invariant Safe]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-18
---
# RedBlue Consistency（RedBlue一貫性）

> 地理的に離れたサイトに複製したシステムで、操作を、受け付けたサイトで即座に実行して後から複製する青の操作と、全サイトで一つの順序に揃えるために他のサイトとの調整を要する赤の操作に分け、一つのシステムの中で弱い一貫性と[[Linearizability|強い一貫性]]を使い分ける[[Consistency Model|一貫性モデル]]である。

## 概要
利用者に近いデータセンタ（サイト）で要求を処理すれば応答は速いが、全ての操作の順序をサイトの間で揃える強い一貫性を保つには、操作ごとに遠いサイトとの通信を待つ必要がある。逆に全ての操作を結果整合性で扱うと、サイトごとに状態が食い違ったり、「残高は負にならない」のようなアプリケーションの不変条件が破られたりする。Liらは2012年の[[OSDI]]で、強い一貫性を必要な操作だけに用いるために、RedBlue一貫性を提案した。

RedBlue一貫性では、赤の操作どうしは全順序をなし、青の操作は他の操作との間に半順序しか持たない。各サイトは、この半順序と矛盾せず、自分のサイトで受け付けた操作の[[Lamport Clock|因果関係]]を守る順序で、全ての操作を一つずつ適用する。青の操作の適用順はサイトごとに異なりうるため、全てのサイトが同じ状態に収束するには、青の操作が他の全ての操作と可換である必要がある。例えば銀行口座では、預け入れ（加算）と利息の付与（乗算）は可換ではない。そこで、元の操作を、受け付けたサイトの状態を読んで何をするかを決めるだけで状態を変えない生成操作（generator）と、決まった変化を状態によらずに適用するシャドウ操作（shadow）とに分ける。利息の付与は、生成操作で利息の額を計算し、その額の預け入れというシャドウ操作として全サイトに適用すれば、預け入れと可換になる。

可換であっても、不変条件を守れるとは限らない。二つのサイトで同時に引き出しを青として成功させると、どちらのサイトも元の残高を見て判断するため、残高が負になりうる。論文は、正しい状態に適用すると必ず正しい状態に移るシャドウ操作を、不変条件に対して安全（invariant safe）と定義した。そのうえで、可換でない組をなすシャドウ操作と不変条件を破りうるシャドウ操作を赤に、残りを青にするという分類の手順を示した。銀行の例では、引き出しが成功した場合のシャドウ操作だけが赤になり、預け入れ、利息、引き出しの失敗は青になる。

![[RedBlue Bank Example.excalidraw]]

この考え方は、可換な操作だけで状態を収束させる[[CRDT]]を、全順序を必要とする少数の操作と組み合わせたものとみることができる。著者らが実装したGeminiは、MySQLを記憶の基盤とし、赤の操作の全順序を、サイトの間で受け渡すトークンを持つサイトだけが赤の操作を確定させる方式で決める。論文はサイトの故障に耐えるにはトークンの管理を[[Paxos]]のような[[Consensus|合意]]の手順で行えばよいと述べている。5サイトの構成で、TPC-Wのショッピングの作業は元の実装の3.7倍、RUBiSは2.3倍のピークのスループットを示した。

## どこで出てくるか
複数の地域のデータセンタにデータを複製するサービスの一貫性と[[Latency|遅延]]の兼ね合いを扱う論文で、操作ごとに異なる強さの一貫性を割り当てる方式の一つとして現れる。全ての操作を合意で順序付ける[[Spanner]]のような方式と、全ての操作を調整なしに複製する方式の中間に位置づけられる。後続の研究には、どの操作を赤にすべきかをプログラムの解析で自動的に判断するSIEVE（USENIX ATC 2014）や、不変条件を破らないための権利を予約（reservation）として各サイトに前もって配り、操作の実行時のサイト間の調整を減らすIndigo（EuroSys 2015）がある。

## 関係
- 上位概念: [[Consistency Model]]
- 対比: [[CRDT]]（全ての操作を可換にして調整を一切行わない）、[[Spanner]]（全てのトランザクションを合意で順序付ける）
- 使う / 使われる: [[Consensus]]
- 関連: [[Lamport Clock]], [[Linearizability]]

## 出典
- [Making Geo-Replicated Systems Fast as Possible, Consistent when Necessary (Li et al., OSDI 2012)](https://www.usenix.org/conference/osdi12/technical-sessions/presentation/li)
- [Automating the Choice of Consistency Levels in Replicated Systems (Li et al., USENIX ATC 2014)](https://www.usenix.org/conference/atc14/technical-sessions/presentation/li_cheng_2)
- [Putting Consistency Back into Eventual Consistency (Balegas et al., EuroSys 2015)](https://www.dpss.inesc-id.pt/~rodrigo/indigo_eurosys15.pdf)
