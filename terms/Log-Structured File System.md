---
aliases: [LFS, ログ構造ファイルシステム, ログ構造化ファイルシステム, Log-structured File System, Sprite LFS, Segment Cleaning, セグメントクリーニング, Inode Map, imap, Checkpoint Region, F2FS, Flash-Friendly File System, NILFS2]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# Log-Structured File System（ログ構造ファイルシステム）

> データと[[Metadata|メタデータ]]の更新を全て記憶装置の上の一つのログの末尾に順に追記し、既存のブロックを上書きしないファイルシステムである。

## 概要
ログ構造ファイルシステム（LFS）は、カリフォルニア大学バークレー校のMendel RosenblumとJohn Ousterhoutが、1991年の[[SOSP]]で発表し、翌年にACM TOCSの論文として出版した。当時、[[DRAM|主記憶]]が大きくなって読み出しの多くが[[Cache|キャッシュ]]で済むようになり、ディスクへのI/Oは書き込みが中心になりつつあった。一方、[[HDD]]は、順次のアクセスの[[Bandwidth|帯域]]は伸びていたが、シークと回転待ちによるランダムなアクセスの遅さは改善が遅かった。従来のファイルシステムは、一つの小さなファイルを作るだけで、[[Inode|inode]]、ビットマップ、ディレクトリなどの離れた位置へ何回も書き込む。LFSは、これらの更新を全て主記憶の上のセグメント（数MB）に集め、満ちたら空いている位置へ一度に順次書き込むことで、ランダムな書き込みを順次の書き込みに変える。

上書きをしないため、ファイルを更新するとinodeの位置が毎回変わる。LFSは、inode番号からinodeの位置を引くinode map（imap）を設け、imapの断片もログに書き、その最新の位置を、記憶装置の固定の位置にあるチェックポイント領域に記録する。古いブロックは不要になっても残るため、クリーナが部分的に使われたセグメントを読み、生きているブロックだけを新しいセグメントに詰め直して、空きのセグメントを作る（ガベージコレクション）。このクリーニングの費用がLFSの主な弱点であり、頻繁に書き換わるデータとほとんど変わらないデータをどう分けるかが設計の論点となる。クラッシュの後は、最後のチェックポイントから読み直し、それ以降にログに書かれた内容をたどって回復する（roll forward）。

## どこで出てくるか
LFSは、[[Copy-on-Write|コピーオンライト]]の考え方を示した、ファイルシステムの教科書的な設計である。NetAppのWAFL、[[ZFS]]、[[btrfs]]は、上書きをしない点でLFSと同じ考え方を用いる。上書きのできないNANDフラッシュを用いる[[SSD]]の内部のFTLも、ログ構造と同じくガベージコレクションを行う。[[Linux Kernel|Linux]]では、フラッシュ向けのログ構造ファイルシステムであるF2FSが、カーネル3.8から利用でき、[[FAST]] '15で発表された。[[Intel Optane Persistent Memory|永続メモリ]]向けの[[NOVA]]は、inodeごとにログを持つことで、ログ構造の手法を変えた例である。[[Key-Value Store|キーバリューストア]]で用いる[[LSM-Tree|LSM木]]も、追記とその後の詰め直し（コンパクション）という同じ構造を持つ。

## 関係
- 前提: [[Inode]], [[HDD]], [[Crash Consistency]]
- 対比: [[Journaling File System]]（ログには更新の記録だけを書き、本体は元の位置に上書きする）
- 使う / 使われる: [[Copy-on-Write]]
- 関連: [[SSD]], [[NOVA]], [[LSM-Tree]], [[ZFS]], [[btrfs]]

## 出典
- [The Design and Implementation of a Log-Structured File System (Rosenblum and Ousterhout, ACM TOCS, 1992)](https://doi.org/10.1145/146941.146943)
- [Log-structured File Systems - Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/file-lfs.pdf)
- [F2FS: A New File System for Flash Storage (FAST '15)](https://www.usenix.org/conference/fast15/technical-sessions/presentation/lee)
