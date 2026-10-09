---
aliases: [LSM Tree, LSM木, Log-Structured Merge-Tree, ログ構造化マージ木, Compaction, コンパクション, Memtable, SSTable, SST, Leveled Compaction, Tiered Compaction, Write Amplification, Read Amplification, Space Amplification]
tags: [term]
maps: ["[[Storage]]", "[[Data Structures]]"]
status: draft
updated: 2026-10-06
---
# LSM-Tree（LSM木）

> 書き込みを主記憶上でまとめてから、整列済みのファイルとして記憶装置に順次書き出し、それらを段階的に併合していくことで、大量の書き込みを効率よく扱う索引構造である。

## 概要
LSM木（Log-Structured Merge-Tree）は、1996年にO'Neilらが提案した。B木のように記憶装置上の索引をその場で更新すると、書き込みのたびに記憶装置の様々な位置へのランダムな読み書きが発生する。LSM木は、索引の変更を遅延させてまとめ、主記憶上の部分から記憶装置上の部分へ、マージソートに似た方法で段階的に流し込むことで、このコストを下げる。

現在の実装（[[RocksDB]]など）では、書き込みは次のように処理される。まず、[[Crash Consistency|クラッシュ]]時に失われないよう、変更を先行書き込みログ（WAL）に追記する。次に、主記憶上の整列済みの表であるmemtableに挿入する。memtableが一定の大きさに達すると、変更不可能な整列済みのファイル（SSTファイル、SSTable）として記憶装置に書き出す。更新や削除も、既存のデータを書き換えるのではなく、新しい版や削除の印（tombstone）として追記される。

SSTファイルは複数の階層（レベル）に置かれる。最上位のL0には書き出されたばかりのファイルが置かれ、ファイル間でキーの範囲が重なりうる。L1以降の各レベルは、キーの範囲が重ならないファイルの集合として一つの整列済みの列をなし、下のレベルほど容量の目標値が大きい（例えば10倍ずつ）。あるレベルが目標値を超えると、コンパクションによって、そのファイルが下のレベルの重なる範囲のファイルと併合され、古い版や削除済みのデータが取り除かれる。この方式をレベル型（leveled）と呼ぶ。各レベルに複数の列を許して併合の回数を減らす階層型（tiered）の方式もある。

読み込みでは、新しいデータから順に、memtable、L0の各ファイル、L1以降の各レベルを調べ、最初に見つかったものを返す。存在しないキーを探す場合に多くのファイルを無駄に読まないよう、各SSTファイルには[[Bloom Filter|ブルームフィルタ]]が付けられる。

## どこで出てくるか
LSM木は、RocksDB、LevelDB、Cassandra、HBaseなど、多くの[[Key-Value Store|キーバリューストア]]やデータベースの記憶エンジンの基盤である。記憶装置への書き込みがすべて順次の追記となるため、書き込みの性能が高く、上書きを苦手とする[[SSD]]とも相性がよい。

その性能は、三種類の増幅のトレードオフとして議論される。書き込み増幅は、コンパクションで同じデータが何度も書き直される度合いであり、SSDの寿命と書き込みの帯域を消費する。読み込み増幅は、一つのキーを探すために調べるファイルの数であり、[[Latency|レイテンシ]]に影響する。空間増幅は、古い版や削除済みのデータが残ることで余分に使う容量である。レベル型は読み込みと空間の増幅が小さい代わりに書き込み増幅が大きく、階層型はその逆の傾向を持つ。コンパクションは背景で大量のI/Oを発生させるため、前面の要求のテールレイテンシを悪化させる原因ともなる。これらの問題の改善は、ストレージ研究の主要な題材であり、キーと値を分離して大きな値の書き直しを避けるWiscKey（FAST 2016）などが提案されている。

## 関係
- 使う / 使われる: [[Key-Value Store]]（LSM木を記憶エンジンとする）, [[Bloom Filter]]（読み込みの高速化）
- 対比: [[B-Tree]]（その場で更新する索引）, [[B-epsilon Tree]]（同じく書き込み最適化された索引）
- 関連: [[SSD]], [[Crash Consistency]], [[Latency]]

## 出典
- [The Log-Structured Merge-Tree (LSM-Tree) (O'Neil et al., Acta Informatica, 1996)](https://www.cs.umb.edu/~poneil/lsmtree.pdf)
- [RocksDB Overview - RocksDB Wiki](https://github.com/facebook/rocksdb/wiki/RocksDB-Overview)
- [Leveled Compaction - RocksDB Wiki](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction)
- [WiscKey: Separating Keys from Values in SSD-conscious Storage - USENIX FAST 2016](https://www.usenix.org/conference/fast16/technical-sessions/presentation/lu)
