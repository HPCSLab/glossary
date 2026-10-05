---
aliases: [デッドロック, Coffman Conditions, コフマンの条件, Circular Wait, 循環待ち, Lock Ordering, ロックの順序, ABBA Deadlock, Livelock, ライブロック, lockdep]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# Deadlock（デッドロック）

> 複数の[[Thread|スレッド]]やプロセスが、互いに相手の持つ資源の解放や相手の動作を待ち合い、いずれも先に進めなくなる状態である。

## 概要
典型的な例は、二つのロックAとBを逆の順序で取得する場合である。スレッド1がAを持ったままBを待ち、スレッド2がBを持ったままAを待つと、どちらも永遠に進めない。このため、ABBAデッドロックとも呼ばれる。同じ[[Mutex|ミューテックス]]を、それを持つスレッド自身が再び取得しようとしても、デッドロックになる。

Coffmanらは1971年に、デッドロックが起きるための四つの条件を示した。資源を同時に一つの主体しか使えないこと（相互排除）、資源を持ったまま別の資源を待つこと（保持と待機）、持っている資源を強制的に取り上げられないこと（横取り不可）、待ちの関係が輪になること（循環待ち）である。いずれか一つを崩せばデッドロックは起きない。代表的な方法は、全てのロックを決められた順序で取得する規則であり、これによって循環待ちを防ぐ。このほか、資源を割り当てる前に安全性を確かめる回避（銀行家のアルゴリズムなど）と、起きたデッドロックを検出して回復する方法がある。デッドロックと似て、状態は変わり続けるが処理が進まない状態をライブロックと呼ぶ。

## どこで出てくるか
デッドロックは、プログラムが止まったまま何も出力しなくなるという形で現れる。[[Linux Kernel|Linuxカーネル]]には、ロックの取得の順序を実行時に記録し、実際にデッドロックが起きる前に、循環する依存関係を検出して報告するlockdepという仕組みがある。

[[MPI]]のプログラムでも、デッドロックは起きる。例えば、二つのプロセスが共に先に受信を呼ぶと、相手の送信を待ち続けて必ずデッドロックになる。共に先に送信を呼ぶ場合は、MPIの実装がメッセージをバッファに格納できれば完了するが、メッセージが大きくバッファが足りなければデッドロックになる。このようにバッファに依存するプログラムは安全でないとされ、送受信の順序を工夫するか、ノンブロッキング通信を用いて避ける。小さな入力では動くが大きな入力では止まる場合は、この種のデッドロックを疑う。

## 関係
- 前提: [[Mutex]], [[Thread]]
- 関連: [[MPI]], [[Linux Kernel]], [[Model Checking]], [[Consensus]]

## 出典
- [Deadlock (computer science) - Wikipedia](https://en.wikipedia.org/wiki/Deadlock_(computer_science))
- [Runtime locking correctness validator - The Linux Kernel documentation](https://docs.kernel.org/locking/lockdep-design.html)
- [Semantics of Point-to-Point Communication - MPI 4.1 Standard](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node68.htm)
- [Nonblocking Communication - MPI 4.1 Standard](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node71.htm)
