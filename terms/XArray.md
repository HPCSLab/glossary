---
aliases: [xarray, eXtensible Array, Radix Tree, 基数木, xa_load, xa_store, XA_MARK]
tags: [term]
maps: ["[[Data Structures]]", "[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# XArray

> Linuxカーネルで用いられる、整数の添字からポインタを引く、非常に大きな配列のように振る舞うデータ構造であり、ページキャッシュの管理の中核をなす。

## 概要
XArrayは、利用者からは、0から始まる整数の添字に対してポインタを格納・取得できる巨大な配列のように見える。実際には、添字の上位の桁から順に節点をたどる多段の木（基数木）として実装されており、使われている添字の範囲にだけ節点を作るため、添字が飛び飛びでもメモリを無駄にしない。特に、添字が密に固まっている場合に効率がよい。一方、ハッシュ値のように散らばった添字には向かない。XArrayは、それ以前にカーネルで用いられていた基数木（radix tree）の実装を置き換えるために、より使いやすいAPIとして導入された。

基本的な操作は、`xa_load()` による取得、`xa_store()` による格納、`xa_erase()` による削除、`xa_for_each()` による走査である。読み込みはRCUによってロックなしで行え、書き換えはXArrayが内部に持つロックで保護されるため、多くの場合、利用者が自らロックを管理する必要はない。各要素には、三種類の印（`XA_MARK_0` から `XA_MARK_2`）を付けられ、印の付いた要素だけを効率よく走査できる。また、2の冪の大きさに揃った連続した範囲の添字を、一つの要素としてまとめて格納すること（multi-index entry）もできる。

## どこで出てくるか
XArrayの最大の利用者は、[[Page Cache|ページキャッシュ]]である。ファイルごとの[[address_space]]は、ファイル内の位置（ページ単位の添字）から、その内容を保持するキャッシュ上のメモリ（[[Folio|folio]]）を引くために、XArrayを用いている。[[read]]でキャッシュにページがあるかを調べる処理は、XArrayの探索に対応する。ダーティなページや書き戻し中のページは、XArrayの印（`PAGECACHE_TAG_DIRTY`、`PAGECACHE_TAG_WRITEBACK`）で記録され、書き戻しの際にはこの印の付いた要素だけを走査する。複数ページからなる大きなfolioは、multi-index entryとして、複数の添字にまたがる一つの要素で格納される。ページキャッシュの実装や性能を調べる際には、この構造を理解しておく必要がある。

## 関係
- 使う / 使われる: [[Page Cache]], [[address_space]]（XArrayでfolioを管理する）
- 関連: [[Folio]], [[B-Tree]], [[Linux Kernel]]

## 出典
- [XArray - The Linux Kernel documentation](https://docs.kernel.org/core-api/xarray.html)
- [[PATCH v5 31/78] mm: Convert page-writeback to XArray - linux-kernel mailing list](https://www.mail-archive.com/linux-kernel@vger.kernel.org/msg1564956.html)
- [Folios for 5.17 - LWN.net](https://lwn.net/Articles/878016/)
