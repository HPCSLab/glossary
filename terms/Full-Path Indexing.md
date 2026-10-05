---
aliases: [full path indexing, Full Path Indexing, フルパスインデックス, フルパスによる索引, Range Rename, Relative-Path Indexing, Zoning, Indirection, "The Full Path to Full-Path Indexing"]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-06
---
# Full-Path Indexing（フルパスインデックス）

> ファイルとディレクトリのデータや[[Metadata|メタデータ]]を、inodeの番号ではなく、`/home/a/b.txt` のような完全なパス名をキーとして、辞書順に並べて格納する方式である。

## 概要
多くのファイルシステムは、ディレクトリの中の名前と、ディスク上のデータの位置との間に、[[Inode|inode]]という間接参照を置く。名前はディレクトリのエントリからinodeの番号を指し、inodeがデータの位置を指す。この間接参照のおかげで、ディレクトリの[[rename]]は、エントリを一つ書き換えるだけで済む。一方、同じディレクトリの下のファイルが、ディスク上で近くに置かれるとは限らない。

フルパスインデックスでは、完全なパス名をキーとする[[Key-Value Store|キーバリューストア]]にデータとメタデータを格納する。キーは辞書順に並ぶため、あるディレクトリの下の全てのファイルは、キーの連続した範囲になる。このため、`ls -R`、`find`、`grep -r` のようにディレクトリの部分木を走査する操作は、キーの範囲を順に読むだけで済み、記憶装置の大きな逐次読み出しになる。`rm -r` も、キーの範囲の削除として実装できる。

フルパスインデックスの弱点は、大きなファイルやディレクトリの名前の変更である。ディレクトリの名前を変えると、その下の全てのキーが変わり、格納の順序も変わる。単純な実装では、部分木の全体を新しいキーで書き直す必要がある。

## どこで出てくるか
[[B-epsilon Tree|Bε木]]を用いたファイルシステムBetrFSの最初の版（0.1）は、フルパスインデックスを採用した。再帰的なgrepは既存の最良のファイルシステムの3.8倍速かったが、Linuxのソースの木の名前の変更に21.2秒かかった（btrfsは0.1秒）。そこで、版0.2は、ディレクトリの階層を領域（zone）に分け、領域の間ではinodeによる間接参照を用いる相対パスの索引に後退した。

[[FAST]] 2018の論文 "The Full Path to Full-Path Indexing"（Zhanら）は、この弱点を解消した。Bε木に、ある接頭辞を持つ全てのキーの接頭辞を不可分に置き換えるrange renameの操作を加え、木を元と先の位置で切り分けてポインタを付け替えることで、その費用を部分木の大きさに比例しないようにした。これを実装したBetrFS 0.4は、フルパスインデックスに戻りながら、名前の変更の性能を間接参照に基づくファイルシステムと同等に保ち、再帰的なgrepを前の版の1.5倍、ランダムな書き込みを1.2倍速くした。

## 関係
- 対比: [[Inode]]（間接参照により名前と位置を分ける）
- 使う / 使われる: [[B-epsilon Tree]], [[Key-Value Store]]
- 関連: [[rename]], [[Metadata]], [[FAST]]

## 出典
- [The Full Path to Full-Path Indexing - USENIX FAST 2018](https://www.usenix.org/conference/fast18/presentation/zhan)
- [論文PDF](https://www.usenix.org/system/files/conference/fast18/fast18-zhan.pdf)
- [BetrFS: A Right-Optimized Write-Optimized File System - USENIX FAST 2015](https://www.usenix.org/conference/fast15/technical-sessions/presentation/jannen)
