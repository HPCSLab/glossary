---
aliases: [Alloy Analyzer, Alloy 6, Small Scope Hypothesis, 小スコープ仮説, Lightweight Formal Methods, 軽量形式手法]
tags: [term]
maps: ["[[Distributed Systems]]"]
status: draft
updated: 2026-10-10
---
# Alloy

> 構造とその変化を関係（リレーション）の論理で記述し、小さな範囲の全ての場合を自動で探索して、例や反例を見つけるための形式仕様記述言語とその解析器である。

## 概要
AlloyはMITのDaniel Jacksonらが開発し、最初の版は1997年に作られた。仕様は、要素の集合を表すシグネチャ（`sig`）と、要素の間の関係からなる一階論理で書く。解析器Alloy Analyzerは、仕様を命題論理に変換して[[SAT Solver|SATソルバ]]に解かせ、得られた解を元の仕様の具体例（インスタンス）に戻して示す。`run` は述語を満たす例を探し、`check` は表明（assertion）を破る反例を探す。

全ての場合を調べるために、Alloyのモデルには必ず大きさの上限（スコープ）を与える。例えば `check P for 5` は、各シグネチャの要素が5個までの全ての場合で反例を探す。反例が見つからなくても、それはスコープの中に反例がないことを示すだけであり、性質が一般に成り立つことの証明ではない。それでもこの方法が有効なのは、誤りの多くは小さな反例を持つという小スコープ仮説による。このように、完全な証明を目指さず、小さな仕様を自動で手軽に検査する考え方は、軽量形式手法と呼ばれる。

当初のAlloyは静的な構造の記述が中心であったが、Alloy 6では変化する状態を `var` で宣言し、`always`、`eventually` などの時相論理の演算子で振る舞いを書けるようになった。これにより、[[TLA+]]と同じように、状態遷移の列に対する[[Model Checking|モデル検査]]が行える。

## どこで出てくるか
プロトコルやデータ構造の設計を、実装の前に確かめる場面で用いられる。よく知られた例として、Zaveは[[Chord]]のリング維持のプロトコルをAlloyでモデル化して解析し、元の論文と同じ故障の仮定のもとでは、公開されたどの版も正しくないことを示した（ACM SIGCOMM CCR、2012年）。[[TLA+]]が状態とその遷移の記述から出発するのに対し、Alloyは要素の間の関係という構造の記述から出発し、SATソルバによる有限の範囲の探索を基本とする。

## 関係
- 上位概念: [[Formal Methods]]
- 対比: [[TLA+]]（状態遷移の記述とTLCによる状態の探索が中心であるのに対し、Alloyは関係の論理とSATソルバによる有限の範囲の探索が中心である）
- 使う / 使われる: [[SAT Solver]], [[Model Checking]]
- 関連: [[Chord]]

## 出典
- [About Alloy - alloytools.org](https://alloytools.org/about.html)
- [Alloy 6 - alloytools.org](https://alloytools.org/alloy6.html)
- [Commands - Alloy Documentation](https://alloy.readthedocs.io/en/latest/language/commands.html)
- [Alloy (specification language) - Wikipedia](https://en.wikipedia.org/wiki/Alloy_(specification_language))
- [Using Lightweight Modeling To Understand Chord (Zave, ACM SIGCOMM CCR 2012)](https://www.cs.princeton.edu/courses/archive/fall14/cos561/papers/ChordModel12.pdf)
