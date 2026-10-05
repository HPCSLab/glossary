---
aliases: [区間木, Augmented Tree, 拡張木, Augmented Red-Black Tree, 拡張赤黒木, Segment, 区間]
tags: [term]
maps: ["[[Data Structures]]"]
status: draft
updated: 2026-10-06
---
# Interval Tree（区間木）

> 区間（始点と終点の組）の集合を格納し、与えられた区間や点と重なるすべての区間を効率よく求めるための木構造である。

## 概要
区間の集合から、ある点を含む区間や、ある区間と重なる区間を探す問題は、すべての区間を順に調べれば $O(n)$ の時間で解ける。区間木は、これを $O(\log n + m)$ の時間で行う。ここで $n$ は格納された区間の数、$m$ は条件に合う区間の数である。区間の挿入と削除も $O(\log n)$ で行える。

代表的な実装は、平衡二分探索木（赤黒木など）を拡張する方法である。各区間を始点の値をキーとして木に格納し、さらに各節点に、その節点を根とする部分木に含まれるすべての区間の終点の最大値を記録しておく。探索の際、ある部分木の終点の最大値が、問い合わせの区間の始点より小さければ、その部分木には重なる区間が一つもないことが分かるため、部分木全体を調べずに飛ばせる。この最大値は、節点とその子の値だけから計算できるため、挿入や削除、木の回転のたびに少ない手間で更新できる。このように、部分木全体についての情報を各節点に持たせた木を拡張木（augmented tree）と呼ぶ。このほかに、区間を中央の点で分割して再帰的に構成する方式もある。

## どこで出てくるか
区間木は、ファイルやメモリの「範囲」を扱うシステムソフトウェアで頻繁に用いられる。[[Linux Kernel|Linuxカーネル]]は、拡張赤黒木による区間木の汎用的な実装を備えており、カーネルの文書でも拡張赤黒木の代表例として区間木が説明されている。例えば、ファイルを[[mmap|写像]]しているプロセスの仮想メモリ領域は、ファイルの[[address_space]]ごとに区間木（`i_mmap`）で管理されており、ファイルのある範囲を写像しているすべての領域を素早く見つけられる。[[Lustre]]は、オブジェクトの範囲ごとに与えるロック（エクステントロック）の管理に区間木を用いている。このほか、地図の表示範囲に含まれる道路を探すような、範囲の問い合わせ（windowing query）にも用いられる。

## 関係
- 対比: [[B-Tree]]（点のキーを扱う探索木）
- 使う / 使われる: [[Linux Kernel]], [[mmap]], [[Lustre]]（範囲ごとのロック）
- 関連: [[Virtual Memory]], [[address_space]], [[Parallel File System]]

## 出典
- [Interval tree - Wikipedia](https://en.wikipedia.org/wiki/Interval_tree)
- [Red-black Trees (rbtree) in Linux - The Linux Kernel documentation](https://docs.kernel.org/core-api/rbtree.html)
- [[PATCH 2/5] mm: replace vma prio_tree with an interval tree - LKML](https://lkml.iu.edu/hypermail/linux/kernel/1208.0/02653.html)
- [Subsystem Map - Lustre Wiki](https://wiki.lustre.org/Subsystem_Map)
