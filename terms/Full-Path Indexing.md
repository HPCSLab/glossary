---
aliases: [full path indexing, Full Path Indexing, フルパスインデックス, フルパスによる索引, Range Rename, Relative-Path Indexing, Zoning, Indirection, "The Full Path to Full-Path Indexing"]
tags: [term]
maps: ["[[Storage]]", "[[HPC Storage]]"]
status: draft
updated: 2026-10-10
---
# Full-Path Indexing（フルパスインデックス）

> ファイルとディレクトリのデータや[[Metadata|メタデータ]]を、inodeの番号ではなく、`/home/a/b.txt` のような完全なパス名をキーとして、辞書順に並べて格納する方式である。

## 概要
多くのファイルシステムは、ディレクトリの中の名前と、ディスク上のデータの位置との間に、[[Inode|inode]]という間接参照を置く。名前はディレクトリのエントリからinodeの番号を指し、inodeがデータの位置を指す。この間接参照のおかげで、ディレクトリの[[rename]]は、エントリを一つ書き換えるだけで済む。一方、同じディレクトリの下のファイルが、ディスク上で近くに置かれるとは限らない。

フルパスインデックスでは、完全なパス名をキーとする[[Key-Value Store|キーバリューストア]]にデータとメタデータを格納する。キーは辞書順に並ぶため、あるディレクトリの下の全てのファイルは、キーの連続した範囲になる。このため、`ls -R`、`find`、`grep -r` のようにディレクトリの部分木を走査する操作は、キーの範囲を順に読むだけで済み、記憶装置の大きな逐次読み出しになる。`rm -r` も、キーの範囲の削除として実装できる。

フルパスインデックスの弱点は、大きなファイルやディレクトリの名前の変更である。ディレクトリの名前を変えると、その下の全てのキーが変わり、格納の順序も変わる。単純な実装では、部分木の全体を新しいキーで書き直す必要がある。

## どこで出てくるか
[[B-epsilon Tree|Bε木]]を用いたファイルシステムBetrFSの最初の版（0.1）は、フルパスインデックスを採用した。再帰的なgrepは既存の最良のファイルシステムの3.8倍速かったが、Linuxのソースの木の名前の変更に21.2秒かかった（[[btrfs]]は0.1秒）。そこで、版0.2は、ディレクトリの階層を領域（zone）に分け、領域の間ではinodeによる間接参照を用いる相対パスの索引に後退した。

[[FAST]] 2018の論文 "The Full Path to Full-Path Indexing"（Zhanら）は、この弱点を解消した。Bε木に、ある接頭辞を持つ全てのキーの接頭辞を不可分に置き換えるrange renameの操作を加え、木を元と先の位置で切り分けてポインタを付け替えることで、その費用を部分木の大きさに比例しないようにした。これを実装したBetrFS 0.4は、フルパスインデックスに戻りながら、名前の変更の性能を間接参照に基づくファイルシステムと同等に保ち、再帰的なgrepを前の版の1.5倍、ランダムな書き込みを1.2倍速くした。

HPC向けの[[Ad Hoc File System|アドホックファイルシステム]]の[[GekkoFS]]と[[CHFS]]も、完全なパス名をキーとしてメタデータとデータを格納する。両者は、パス名（データの場合はパス名とチャンクの番号）のハッシュ値によって担当のサーバを決める。このため、ファイルの[[Metadata|メタデータ]]は、親ディレクトリを順にたどることなく、一回の問い合わせで得られる。一方、同じディレクトリのエントリはハッシュによって全てのサーバに散らばるため、ディレクトリの一覧（readdir）は全てのサーバに問い合わせて集める必要がある。また、名前を変えるとキーとハッシュ値が変わり、データとメタデータを別のサーバに移す必要があるため、名前の変更が困難である。CHFSはrenameを提供しておらず、GekkoFSでもrenameは既定では無効の実験的な機能である。

## 関係
- 対比: [[Inode]]（間接参照により名前と位置を分ける）
- 使う / 使われる: [[B-epsilon Tree]], [[Key-Value Store]]
- 使う / 使われる: [[GekkoFS]], [[CHFS]]
- 関連: [[rename]], [[Metadata]], [[FAST]], [[Ad Hoc File System]]

## 出典
- [The Full Path to Full-Path Indexing - USENIX FAST 2018](https://www.usenix.org/conference/fast18/presentation/zhan)
- [論文PDF](https://www.usenix.org/system/files/conference/fast18/fast18-zhan.pdf)
- [BetrFS: A Right-Optimized Write-Optimized File System - USENIX FAST 2015](https://www.usenix.org/conference/fast15/technical-sessions/presentation/jannen)
- [GekkoFS README（Rename） - BSC GitLab](https://storage.bsc.es/gitlab/hpc/gekkofs/-/blob/master/README.md)
- [gekkofs/src/common/rpc/distributor.cpp - BSC GitLab](https://storage.bsc.es/gitlab/hpc/gekkofs/-/blob/master/src/common/rpc/distributor.cpp)（パス名のハッシュによるサーバの決定）
- [otatebe/chfs - GitHub](https://github.com/otatebe/chfs)（APIの一覧、`lib/path.c`、`lib/chfs.c`）
