---
aliases: [NOVA File System, NOn-Volatile memory Accelerated log-structured file system]
tags: [term]
maps: ["[[Storage]]"]
status: draft
updated: 2026-10-10
---
# NOVA

> [[DRAM]]と同じメモリバスに接続された不揮発性メモリ（[[Intel Optane Persistent Memory|永続メモリ]]）のために設計された、inodeごとにログを持つログ構造の[[Linux Kernel|Linux]]のファイルシステムである。

## 概要
NOVAは、カリフォルニア大学サンディエゴ校のJian XuとSteven Swansonが、2016年の[[FAST]]で発表した。永続メモリはバイト単位で高速に読み書きできるため、ディスク向けに設計された従来のファイルシステムでは、ソフトウェアの処理の時間が性能の大半を占める。また、CPUはメモリへの書き込みの順序を入れ替えるため、[[Crash Consistency|クラッシュ一貫性]]を保つには、CPUの[[Cache|キャッシュ]]から明示的に書き戻して順序を強制する必要があり、その費用が大きい。

NOVAは、ログ構造ファイルシステムの手法を永続メモリに合わせて変えた。従来のログ構造ファイルシステムは、ファイルシステム全体で一つのログを持ち、連続した空き領域を確保するためのガベージコレクションの費用が大きい。NOVAは、[[Inode|inode]]ごとに別のログを持つことで、異なるファイルの更新を同期なしに並行して行う。ログは連結リストとして置くため連続した領域を必要とせず、ログの末尾を指すポインタをアトミックに更新することで、追記をアトミックに行う。ファイルのデータはログに書かず、[[Copy-on-Write|コピーオンライト]]で新しいページに書くため、ログが短くなり、回復とガベージコレクションが速い。複数のinodeにまたがるディレクトリの操作（作成、削除、[[rename]]）には、軽量な[[Journaling File System|ジャーナリング]]を用いる。検索用の索引（基数木）は永続メモリには置かず、DRAMの上に構築する。

論文では、書き込みの多い処理で、既存のファイルシステムに比べて22%から216倍、同等に強い一貫性を保証するファイルシステムに比べて3.1倍から13.5倍のスループットを得たと報告している。実装はLinuxカーネル4.0の上で行われ、ソースコードは公開されている。

## どこで出てくるか
NOVAは、永続メモリ向けファイルシステムの研究で、[[ext4|ext4-DAX]]と並んでよく比較の対象となる。[[SingularFS]]の論文でも、ローカルの永続メモリ向けファイルシステムの代表として比較されている。[[devdax]]で扱うDAX（[[Page Cache|ページキャッシュ]]を介さない直接のアクセス）や、[[mmap]]による写像の一貫性を議論する際にも参照される。

## 関係
- 前提: [[Intel Optane Persistent Memory]], [[Crash Consistency]], [[Inode]]
- 対比: [[ext4]]（ext4-DAXはジャーナリングでメタデータを保護し、データのアトミックな更新を保証しない）
- 使う / 使われる: [[Copy-on-Write]]
- 関連: [[devdax]], [[FAST]]

## 出典
- [NOVA: A Log-structured File System for Hybrid Volatile/Non-volatile Main Memories (FAST '16)](https://www.usenix.org/conference/fast16/technical-sessions/presentation/xu)
- [論文PDF - USENIX](https://www.usenix.org/system/files/conference/fast16/fast16-papers-xu.pdf)
- [NVSL/NOVA - GitHub](https://github.com/NVSL/NOVA)
