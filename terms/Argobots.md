---
aliases: [argobots, User-Level Thread, ユーザレベルスレッド, ULT, Tasklet, タスクレット, Execution Stream, 実行ストリーム, Work Unit, Stackable Scheduler]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-06
---
# Argobots

> アルゴンヌ国立研究所が中心となって開発する、OSのスレッドより軽量なユーザレベルスレッドとタスクを提供する、HPC向けの低水準のスレッドの枠組みである。

## 概要
Argobotsは、OpenMPやMPIなどの高水準のプログラミングモデルや実行時システムの土台となることを目的として設計された。論文は2018年に IEEE Transactions on Parallel and Distributed Systems（TPDS）で発表されている。

Argobotsには、二つの階層の並列性がある。一つは実行ストリーム（ES）であり、OSのスレッドに相当し、他のESと独立に実行される。もう一つは作業単位（work unit）であり、ESの上で実行される軽量な処理の単位である。作業単位には二種類ある。ユーザレベルスレッド（ULT）は、自身のスタックを持ち、途中で制御を譲って後で再開できる。タスクレットは、スタックを持たず、ESのスケジューラのスタックを借りて実行され、途中で中断せずに最後まで実行される。タスクレットは文脈の保存とスタックの管理が不要な分、ULTより軽い。

作業単位は、プールと呼ばれる待ち行列に置かれ、各ESのスケジューラがプールから取り出して実行する。プールを複数のESで共有すれば、ES間で作業を分け合える。作業単位の切り替えはプリエンプション（強制的な割り込み）によらず、作業単位が自ら制御を譲る協調的な方式で行われる。例えば、ULTは遠隔のデータを待つ間に制御を譲り、その間に同じESの他の作業単位が実行される。スケジューラは利用者が独自に書くことができ、入れ子にすることもできる。

## どこで出てくるか
Argobotsは、HPC向けのデータサービスの基盤である[[Margo]]で用いられている。Margoでは、届いたRPCの処理がそれぞれULTとして実行され、[[Mercury]]の通信の完了を待つ間、ULTが制御を譲る。このため、多数の要求を、OSの[[Thread|スレッド]]を増やさずに並行して処理できる。論文では、OpenMPの実行時システム、[[MPI]]との連携、計算と同じノードで動くI/Oサービスへの応用が示されている。

ULTは協調的に切り替わるため、一つのULTが制御を譲らずに長い計算を続けると、同じESの他の作業単位は実行されない。Margoを用いたサービスの性能を調べる際には、ESの数や、プールとESの対応付けの設定が、[[Latency|レイテンシ]]と処理能力に影響する。

## 関係
- 上位概念: [[Thread]]（ユーザレベルスレッドは、OSのスレッドの上で実行される）
- 使う / 使われる: [[Margo]]
- 関連: [[Mercury]], [[OpenMP]], [[MPI]]

## 出典
- [pmodels/argobots - GitHub](https://github.com/pmodels/argobots)
- [Argobots: A Lightweight Low-Level Threading and Tasking Framework (Seo et al., IEEE TPDS 2018)](https://doi.org/10.1109/TPDS.2017.2766062)
- [Argobots: A Lightweight Low-Level Threading and Tasking Framework (著者版PDF)](https://www.mcs.anl.gov/~aamer/papers/tpds17_argobots.pdf)
