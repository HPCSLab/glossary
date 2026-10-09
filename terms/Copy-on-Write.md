---
aliases: [CoW, COW, コピーオンライト, Copy on Write, Shadowing, シャドウイング, reflink, FICLONE, "cp --reflink", Clone-on-Write]
tags: [term]
maps: ["[[Operating System]]", "[[Storage]]"]
status: draft
updated: 2026-10-10
---
# Copy-on-Write（コピーオンライト）

> 複数の利用者が同じデータを使う際に、すぐには複製せずに共有しておき、誰かが書き換えようとした時点で初めて、その部分だけを複製する手法である。

## 概要
データの複製には時間と容量がかかるが、複製したデータの多くは書き換えられずに終わる。コピーオンライト（CoW）は、複製を求められた時点では元のデータを共有し、書き換えが起きた部分だけを後から複製することで、この無駄を省く。書き換えられなければ、複製は作られない。この考え方は、メモリ、ファイル、データ構造に広く用いられている。

[[Virtual Memory|仮想記憶]]では、`fork()` がその代表例である。Linuxの `fork()` は、親の[[Process|プロセス]]のメモリを複製せず、親と子のページテーブルから同じ物理ページを読み取り専用として共有する。どちらかがそのページに書き込むと、ページフォルトが起き、カーネルがそのページだけを複製して書き込み可能にする。このため、`fork()` の負担は、ページテーブルの複製とプロセスの管理構造の作成にほぼ限られる。子が直後に `exec` で別のプログラムに置き換わる場合、メモリの複製はほとんど起きない。[[mmap]]の `MAP_PRIVATE` による写像も、コピーオンライトで書き込みをプロセス専用の複製に向ける。

記憶装置では、データを元の場所に上書きせず、変更されたブロックを新しい場所に書き、それを指す[[Metadata|メタデータ]]を更新する方式を指す。[[ZFS]]や[[btrfs]]はこの方式のファイルシステムであり、変更を新しい場所に書いてから参照を不可分に切り替えることで、クラッシュの後も一貫した状態を保つ（[[Crash Consistency]]を参照）。古いブロックを残しておけば、ある時点の状態をほぼ瞬時に保存する[[Snapshot|スナップショット]]になる。ファイルの単位では、記憶領域を共有したままファイルを複製するreflinkがあり、`cp --reflink` や `ioctl(FICLONE)` で用いる。

## どこで出てくるか
コピーオンライトは、ファイルシステムの設計を比べる際の主要な軸であり、上書きした上で[[Journaling File System|ジャーナリング]]によって一貫性を保つ[[ext4]]や[[XFS]]と対比される。コピーオンライトのファイルシステムでは、データベースの格納ファイルや[[Virtual Machine|仮想マシン]]のディスクイメージのように、同じファイルの中を頻繁に上書きする用途で、断片化と性能の低下が起きやすい。

メモリのコピーオンライトは、大きなメモリを確保したプロセスが `fork()` で子を作る場合に意味を持つ。子を作った直後は物理メモリの使用量は増えないが、親や子が書き込むたびにページが複製され、使用量が増えていく。

## 関係
- 使う / 使われる: [[ZFS]], [[btrfs]], [[Snapshot]], [[Virtual Memory]], [[mmap]]
- 対比: [[Journaling File System]]（元の場所に上書きし、ジャーナルで一貫性を保つ）
- 関連: [[Crash Consistency]], [[Process]], [[B-Tree]]

## 出典
- [Copy-on-write - Wikipedia](https://en.wikipedia.org/wiki/Copy-on-write)
- [fork(2) - Linux manual page](https://man7.org/linux/man-pages/man2/fork.2.html)
- [mmap(2) - Linux manual page](https://man7.org/linux/man-pages/man2/mmap.2.html)
- [ioctl_ficlone(2) - Linux manual page](https://man7.org/linux/man-pages/man2/ioctl_ficlone.2.html)
- [cp(1) - Linux manual page](https://man7.org/linux/man-pages/man1/cp.1.html)
