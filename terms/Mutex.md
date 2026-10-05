---
aliases: [ミューテックス, Lock, ロック, Mutual Exclusion, 相互排除, 排他制御, Critical Section, クリティカルセクション, Spinlock, スピンロック, pthread_mutex_lock, pthread_mutex_unlock, Lock Contention, ロック競合, Lock Granularity, ロックの粒度]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# Mutex（ミューテックス）

> 共有データに同時にアクセスできる[[Thread|スレッド]]を一つに限るための、ロックの仕組みである。

## 概要
ミューテックスは、相互排除（mutual exclusion）を略した名前であり、ロックとも呼ばれる。共有データを読み書きする区間（クリティカルセクション）の前でロックを取得し、後で解放する。すでに他のスレッドがロックを持っている場合、取得しようとしたスレッドは、ロックが解放されるまで待たされる。これにより、共有データを同時に操作する競合状態を防ぐ。ロックの実装には、test-and-setやcompare-and-swapなどの不可分な命令が用いられる。

待ち方には二通りある。ミューテックスは、待つスレッドを眠らせて、他の処理にCPUを譲る。スピンロックは、ロックが空くまでCPU上で繰り返し確かめ続ける。スピンロックは待ち時間が短い場合には効率がよいが、長く待つとCPUを浪費する。[[Linux Kernel|Linuxカーネル]]の `mutex` は、持ち主が実行中の間は少しスピンし、それでも空かなければ眠る。また、ロックを持つスレッドのみが解放でき、割り込みの処理の中では使えない。ユーザ空間では、POSIXの `pthread_mutex_lock()` と `pthread_mutex_unlock()` を用いる。

ロックの粒度の選択には、トレードオフがある。少数の大きなロックで広い範囲を守ると、管理の負担は小さいが、多くのスレッドが同じロックを待つロック競合が増える。多数の小さなロックで細かく守ると、競合は減るが、管理の負担が増え、[[Deadlock|デッドロック]]を起こしやすくなる。

## どこで出てくるか
多数のスレッドで共有データを扱うプログラムでは、ロック競合が性能を制限することがある。スレッドの数を増やしても性能が伸びない場合には、原因の候補の一つとしてロックの待ち時間を調べる。カーネル内のロックの競合は `perf lock` で観測できる。

## 関係
- 前提: [[Thread]]
- 関連: [[Deadlock]], [[Linux Kernel]], [[perf]]

## 出典
- [Lock (computer science) - Wikipedia](https://en.wikipedia.org/wiki/Lock_(computer_science))
- [pthread_mutex_lock(3p) - Linux manual page](https://man7.org/linux/man-pages/man3/pthread_mutex_lock.3p.html)
- [Generic Mutex Subsystem - The Linux Kernel documentation](https://docs.kernel.org/locking/mutex-design.html)
- [perf-lock(1) - Linux manual page](https://man7.org/linux/man-pages/man1/perf-lock.1.html)
