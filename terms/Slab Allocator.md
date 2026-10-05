---
aliases: [Slab, slab, Linux slab, スラブ, スラブアロケータ, Slab Allocation, SLUB, SLAB, SLOB, kmalloc, kzalloc, kfree, kmem_cache, kmem_cache_create, kmem_cache_alloc, /proc/slabinfo, slabinfo, slabtop, GFP_KERNEL, GFP_ATOMIC, vmalloc]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# Slab Allocator（スラブアロケータ）

> カーネルが頻繁に確保と解放を繰り返す同じ種類の小さなオブジェクトを、種類ごとのキャッシュにまとめて効率よく割り当てる、メモリ割り当ての仕組みである。

## 概要
スラブ割り当ては、Jeff Bonwickが1994年にSolaris 2.4のカーネルに導入した手法である。カーネルは、[[Inode|inode]]や[[Dentry|dentry]]のような決まった大きさのオブジェクトを大量に確保しては解放する。これをページ単位の割り当てで行うと、断片化が起き、オブジェクトの初期化と破棄の負担も大きい。スラブ割り当てでは、オブジェクトの種類ごとにキャッシュを作り、一つ以上の連続したページからなるスラブを、同じ大きさのオブジェクトの領域に区切っておく。解放されたオブジェクトはキャッシュに戻され、次の割り当てに再利用される。スラブは、全て空き、一部使用、全て使用の三つの状態で管理される。

[[Linux Kernel|Linuxカーネル]]には、SLAB、SLOB、SLUBの三つの実装があったが、SLOBは6.4で、SLABは6.8で削除され、現在はSLUBのみが用いられている。カーネルのコードでは、ページより小さな任意の大きさの領域は `kmalloc()`（零で初期化する場合は `kzalloc()`）で確保し、`kfree()` で解放する。同じ種類のオブジェクトを多数確保する場合は、`kmem_cache_create()` で専用のキャッシュを作り、`kmem_cache_alloc()` で確保する。大きな領域には、物理的に連続しない `vmalloc()` を用いる。割り当てには、眠ってよいか（`GFP_KERNEL`）、割り込みの処理の中などで眠れないか（`GFP_ATOMIC`）を示すGFPフラグを指定する。

## どこで出てくるか
カーネルのコードを読み書きする際には、構造体の確保に `kmalloc()` や `kmem_cache_alloc()` が使われているのを頻繁に目にする。[[File System|ファイルシステム]]も、inodeやdentry、[[Buffer Head|バッファヘッド]]などを専用のキャッシュから確保している。

各キャッシュの使用状況は `/proc/slabinfo`（rootのみ読める）で、キャッシュごとの使用中のオブジェクトの数、オブジェクトの大きさなどとして確認でき、`slabtop` で実時間に表示できる。カーネルのメモリの使用量を調べる際には、[[Page Cache|ページキャッシュ]]だけでなく、スラブの使用量も確かめる。

## 関係
- 上位概念: [[Linux Kernel]]
- 使う / 使われる: [[Inode]], [[Dentry]], [[Buffer Head]]
- 関連: [[Virtual Memory]], [[Folio]], [[Page Cache]]

## 出典
- [Slab allocation - Wikipedia](https://en.wikipedia.org/wiki/Slab_allocation)
- [Memory Allocation Guide - The Linux Kernel documentation](https://docs.kernel.org/core-api/memory-allocation.html)
- [slabinfo(5) - Linux manual page](https://man7.org/linux/man-pages/man5/slabinfo.5.html)
