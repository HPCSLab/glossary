---
aliases: [Bε-tree, Bε木, B^ε-tree, B-epsilon tree, Be-tree, Write-Optimized Data Structure, 書き込み最適化データ構造, Upsert, Fractal Tree, BetrFS, TokuDB]
tags: [term]
maps: ["[[Data Structures]]", "[[Storage]]"]
status: draft
updated: 2026-10-06
---
# Bε-tree（Bε木）

> [[B-Tree|B木]]の内部の節点にバッファを持たせ、更新をそこに溜めてから葉に向かってまとめて流し込むことで、B木と同程度の探索性能を保ちつつ、挿入を大幅に高速化した、書き込み最適化された索引構造である。

## 概要
Bε木は、BrodalとFagerbergが、探索に有利なB木と、挿入に有利なbuffered repository treeとの間に、性能のトレードオフの曲線が存在することを示すために提案した。その後、この曲線の中間に位置する設定が実用上有用であることが認識され、商用のデータベースTokuDBや、研究用のファイルシステムBetrFSに用いられた。

B木と同じく、内部の節点は区切りのキー（ピボット）と子へのポインタを持つが、Bε木では、節点の空間の一部をバッファに充てる。節点の大きさを $B$ とすると、ピボットと子へのポインタにおよそ $B^\varepsilon$、バッファにおよそ $B - B^\varepsilon$ を用いる。挿入、削除、更新は、メッセージとして根の節点のバッファに追加される。バッファが一杯になると、メッセージの一部が子の節点のバッファへ流し込まれる（flush）。この流し込みは、子に流すべきメッセージが十分に溜まっている場合にのみ行われ、一回あたり少なくともおよそ $B^{1-\varepsilon}$ 個のメッセージがまとめて移される。そのため、節点は、その内容の十分な部分が変わるときにしか書き直されない。探索では、根から葉への経路上のバッファも調べ、そのキーに対する未反映のメッセージを適用した結果を返す。

$\varepsilon$ は0から1の間の調整用の値である。$\varepsilon = 1$ ではバッファがなくなり、通常のB木と同じになる。$\varepsilon = 0$ では各節点が大きなバッファを持つ二分木（buffered repository tree）となる。$\varepsilon$ を大きくすると分岐数が増えて木が浅くなり探索が速くなり、小さくするとバッファが大きくなって流し込み一回あたりのメッセージが増え、挿入が速くなる。例えば $\varepsilon = 1/2$ では、探索のI/O回数は同じ節点の大きさのB木の高々2倍にとどまる一方、挿入はメッセージをまとめて書く分だけ高速になる。$B = 1024$、$\varepsilon = 1/2$ の場合、挿入はB木より16倍速くなる。範囲の問い合わせのI/O回数は、B木と同じく、最初のキーを探す対数の費用に、読み出すキーの数をブロックの大きさで割った費用を加えたものとなる。

Bε木は、更新の内容をメッセージとして表すことを活かし、upsertと呼ばれる操作を提供する。upsertは、キーの値を読み出さずに、値に適用する関数（例えば加算）をメッセージとして書き込む操作であり、メッセージが葉に流し込まれた時点で値に適用される。これにより、読み出してから書き戻す更新の多くを、読み出しのI/Oなしに行える。

## どこで出てくるか
Bε木は、[[LSM-Tree|LSM木]]と並ぶ、代表的な書き込み最適化データ構造である。いずれも小さなランダムな更新をまとめて書くことで、更新一回あたりのI/Oを1回よりはるかに小さくする。ランダムな挿入のたびに対象の葉を書き換えるB木では、挿入一回あたり少なくとも一回のI/Oが必要となる点と対照的である。研究の文脈では、2015年の[[FAST]]で発表されたBetrFSが、Bε木を索引として用いた最初のカーネル内のファイルシステムであり、小さな書き込みが多い処理で、[[ext4]]やXFSを大きく上回る性能を示した。ファイルシステムや[[Key-Value Store|キーバリューストア]]の索引を設計する際には、B木、LSM木、Bε木のいずれを採るかが、読み書きの性能のトレードオフとして論点となる。

## 関係
- 上位概念: [[B-Tree]]（Bε木はB木の拡張である）
- 対比: [[LSM-Tree]]（同じく書き込み最適化された索引）
- 使う / 使われる: [[Key-Value Store]], [[File System]]（BetrFS）
- 関連: [[SSD]], [[Latency]], [[FAST]]

## 出典
- [An Introduction to Bε-trees and Write-Optimization (Bender et al., ;login:, October 2015)](https://www.usenix.org/system/files/login/articles/login_oct15_05_bender.pdf)
- [BetrFS: A Right-Optimized Write-Optimized File System - USENIX FAST 2015](https://www.usenix.org/conference/fast15/technical-sessions/presentation/jannen)
