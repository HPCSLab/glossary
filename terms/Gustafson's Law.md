---
aliases: [グスタフソンの法則, Gustafson-Barsis's Law, Scaled Speedup]
tags: [term]
maps: ["[[Parallel Computing]]"]
status: draft
updated: 2026-10-05
---
# Gustafson's Law（グスタフソンの法則）

> 問題の大きさを計算資源に応じて増やす場合、速度向上はプロセス数にほぼ比例して増大しうる、という法則である。

## 概要
1988年にJohn GustafsonとEdwin Barsisが、論文 "Reevaluating Amdahl's Law"（Communications of the ACM）で示した。[[Amdahl's Law|アムダールの法則]]は問題の大きさを固定するが、実際の利用者は、計算資源が増えればそれを使い切るように問題を大きくする、という観察に基づく。並列実行時の実行時間のうち逐次部分の割合を $s$、並列部分の割合を $p = 1 - s$、プロセス数を $N$ とすると、スケールドスピードアップは次の式で与えられる。

$$S(N) = s + p \cdot N = N - (N - 1) \cdot s$$

例えば、$s = 0.05$ で1024プロセスを用いると、速度向上率は約973倍となる。アムダールの法則と異なり、上限を持たない。この法則は[[Weak Scaling|弱スケーリング]]の考え方に対応する。

## どこで出てくるか
グスタフソンの法則は、大規模並列計算機が有用であることの理論的な根拠として引用される。二つの法則は矛盾するものではなく、前提が異なる。アムダールの法則における割合は「逐次実行時」の時間に対するものであり、グスタフソンの法則における割合は「並列実行時」の時間に対するものである。前者は決まった問題をどこまで速く解けるかを、後者は同じ時間でどこまで大きな問題を解けるかを表す。性能の議論では、どちらの前提に立っているかを明確にする必要がある。

## 関係
- 対比: [[Amdahl's Law]]（問題の大きさを固定する場合の法則）
- 使う / 使われる: [[Weak Scaling]]（この法則に対応する評価方法）
- 関連: [[Parallel Efficiency]]

## 出典
- [Gustafson's law - Wikipedia](https://en.wikipedia.org/wiki/Gustafson%27s_law)
- [Scaling - HPC Wiki](https://hpc-wiki.info/hpc/Scaling)
