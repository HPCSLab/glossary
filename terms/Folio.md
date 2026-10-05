---
aliases: [folio, struct folio, Page Folio, Large Folio, Compound Page, 複合ページ, struct page]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# Folio（フォリオ）

> Linuxカーネルのメモリ管理において、物理的に連続した2の冪個のページの集まりを一つの単位として表す構造体であり、ページキャッシュの管理の単位でもある。

## 概要
Linuxカーネルは、物理メモリのページ（通常4KiB）ごとに `struct page` という管理用の構造体を持つ。複数の連続したページを一つにまとめて扱う場合には、従来、複合ページ（compound page）という仕組みが用いられてきた。複合ページは、先頭のページ（head page）と、それに続くページ（tail page）からなる。この方式では、`struct page` へのポインタを受け取った関数が、それが単独のページなのか、複合ページの先頭なのか、途中のページなのかを区別できなかった。そのため、多くの関数で先頭のページを探す処理を繰り返したり、誤って途中のページを操作したりする問題があった。

folioは、この曖昧さを解消するために、Matthew Wilcoxが提案し、Linux 5.16で導入された。`struct folio` は、決して途中のページ（tail page）ではないことが保証された `struct page` であり、2の冪個の連続したページ全体を表す。folioを受け取る関数は、常にその全体を操作すると明確に分かる。これにより、先頭のページを探す無駄な処理が省かれ、コードの意図も明確になった。導入後、メモリ管理と[[Page Cache|ページキャッシュ]]、さらに各ファイルシステムが、順にページ単位からfolio単位の処理へ書き換えられている。

## どこで出てくるか
folioは、現在のページキャッシュの管理の単位である。ファイルごとの[[address_space]]は、ファイル内の位置からfolioを[[XArray]]で引き、[[read]]や[[write]]、書き戻しはfolio単位で行われる。4KiBのページは、大きなファイルを扱うには管理の単位として小さすぎることが多い。ファイルシステムが大きなfolio（large folio）に対応していれば、例えば64KiBのデータを、4KiBのページ16個ではなく一つのfolioとしてキャッシュでき、管理の手間を減らせる。大きなfolioは、[[XArray]]の中で、複数の添字にまたがる一つの要素として格納される。大きなfolioへの対応の状況は、ファイルシステムごとに異なる。カーネルの比較的新しいソースコードやメーリングリストを読むと、`page` の代わりに `folio` を扱う関数が多数現れるため、カーネルのI/O経路を調べる研究ではこの概念を理解しておく必要がある。

## 関係
- 上位概念: [[Virtual Memory]]（ページを単位とするメモリ管理）
- 使う / 使われる: [[Page Cache]], [[address_space]], [[XArray]]
- 関連: [[Linux Kernel]], [[mmap]]

## 出典
- [Clarifying memory management with page folios - LWN.net](https://lwn.net/Articles/849538/)
- [Linux 5.16 - Kernel Newbies](https://kernelnewbies.org/Linux_5.16)
- [Page Cache - The Linux Kernel documentation](https://docs.kernel.org/mm/page_cache.html)
- [Folios for 5.17 - LWN.net](https://lwn.net/Articles/878016/)
