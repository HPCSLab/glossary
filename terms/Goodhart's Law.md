---
aliases: [グッドハートの法則, Goodhartの法則, グッドハート則]
tags: [term]
maps: ["[[Research]]"]
status: draft
updated: 2026-10-10
---
# Goodhart's Law（グッドハートの法則）

> 指標を目標として最適化すると、その指標は本来測ろうとしていたものを正しく表さなくなる、という経験則である。

## 概要
経済学者Charles Goodhartが1975年に英国の金融政策について述べた「観測された統計的な規則性は、それを制御の目的で圧力にさらすと崩れる傾向がある」という指摘に由来する。広く知られた「測定値が目標になると、それは良い測定値ではなくなる」という表現は、人類学者Marilyn Strathernが1997年に英国の大学評価を論じた論文で示した言い換えである。指標はもともと、直接測りにくい目的（性能、品質、成果）と相関するから使われる。その指標の値を上げること自体が目的になると、目的に寄与しない方法でも値を上げられる余地が利用され、指標と目的の相関が失われる。同じ現象は社会指標についてのCampbellの法則としても論じられている。

## どこで出てくるか
計算機システムの研究では、性能を[[Benchmark|ベンチマーク]]の数値で示すことが多い。[[TOP500]]の順位を決める[[LINPACK]]や、ストレージの[[IO500]]のように、単一の数値で順位を付ける指標は比較を容易にするが、その数値だけに合わせて設定や実装を調整すると、目的のアプリケーションでの性能を反映しなくなる。機械学習では、公開されたベンチマークのスコアを競うことでそのデータセットへの過剰な適合が起こる問題や、強化学習のエージェントが不完全に定義された報酬を想定外の方法で最大化する報酬ハッキング（reward hacking）が、この法則の例として挙げられる。研究室の議論では、評価指標を選ぶ際や、ある数値の改善が本当に目的の改善を意味するかを検討する際にこの名前が出てくる。

## 関係
- 関連: [[Benchmark]], [[TOP500]], [[LINPACK]], [[IO500]]

## 出典
- [Goodhart's law - Wikipedia](https://en.wikipedia.org/wiki/Goodhart%27s_law)
- [Strathern, M. "'Improving ratings': audit in the British University system." European Review 5(3), 1997](https://cambridge.org/core/journals/european-review/article/improving-ratings-audit-in-the-british-university-system/FC2EE640C0C44E3DB87C29FB666E9AAB)
- [Manheim, D. and Garrabrant, S. "Categorizing Variants of Goodhart's Law." arXiv:1803.04585, 2018](https://arxiv.org/abs/1803.04585)
