---
aliases: [ワークスティーリング, Work-Stealing, 仕事の横取り, Work-Stealing Scheduler, ワークスティーリングスケジューラ, Work-Stealing Deque]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-17
---
# Work Stealing（ワークスティーリング）

> 仕事が無くなったワーカが他のワーカのタスクのキューからタスクを奪って実行することで、実行時に負荷を自動的に均す、タスク並列のスケジューリングの方式である。

## 概要
再帰的な分割統治のように、実行しながらタスクを生み出す処理では、タスクの数と大きさを事前に知ることができない。最初に仕事を均等に分けても、ワーカ（[[Thread|スレッド]]など）ごとの仕事量に偏りが生じ、最も遅いワーカが全体の時間を決めて[[Parallel Efficiency|並列効率]]が下がる。全てのタスクを一つの共有キューに入れると、多数のワーカが同じキューを取り合う。ワークスティーリングでは、各ワーカが自分専用の両端キュー（deque）を持ち、自分が生んだタスクを新しい側に積み、同じ新しい側から取り出して実行する。キューが空になったワーカ（thief）は、ランダムに選んだ他のワーカ（victim）のキューの古い側からタスクを一つ奪う。

![[Work Stealing Deques.excalidraw]]

持ち主が新しい側から取るため、直前に生んだタスクが続けて実行され、そのデータが[[Cache|キャッシュ]]に残りやすい。盗む側が古い側から取るのは、分割統治では古いタスクほど木の根に近く、大きな仕事を含むためである。両者がキューの逆の端を使うため、同期の調停が必要になるのは主にキューが空に近いときであり、Cilk-5はこの調停を軽い手順（THEプロトコル）で行って、盗まれない場合の持ち主の負担を小さくした。BlumofeとLeisersonは、全ての仕事を逐次に実行した時間をT1、依存関係の最も長い経路の時間をT∞とすると、P個のプロセッサでの実行時間の期待値が T1/P + O(T∞) となることを示した。T∞が十分小さければ、ほぼ理想的な速度向上が得られる。

## どこで出てくるか
MITのCilkとその後継の実装、IntelのoneTBBのタスクスケジューラなど、タスク並列の言語と実行時ライブラリのスケジューラとして用いられる。[[Argobots]]のようなユーザレベルスレッドの処理系や、[[OpenMP]]のtask構文を用いるプログラムの性能を議論する際にも、タスクをどのワーカがどの順に実行するかという観点で現れる。ランダムに盗む相手を選ぶ方式は、データが遠い[[NUMA]]ノードにあるかを区別しないため、メモリの配置を考慮したワークスティーリングも研究されている。

## 関係
- 関連: [[Thread]], [[Parallel Efficiency]], [[Argobots]]

## 出典
- [Scheduling Multithreaded Computations by Work Stealing (Blumofe and Leiserson, Journal of the ACM, 1999)](https://doi.org/10.1145/324133.324234)
- [The Implementation of the Cilk-5 Multithreaded Language (Frigo, Leiserson, and Randall, PLDI 1998)](https://doi.org/10.1145/277650.277725)
- [A NUMA-Aware Provably-Efficient Task-Parallel Platform Based on the Work-First Principle (Deters et al., IISWC 2018)](https://arxiv.org/abs/1806.11128)
- [Intel oneAPI Threading Building Blocks (oneAPI Programming Guide)](https://www.intel.com/content/www/us/en/docs/oneapi/programming-guide/current/intel-oneapi-threading-building-blocks-onetbb.html)
