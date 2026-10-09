---
aliases: [matplotlib, pyplot, plt, Figure, Axes, savefig]
tags: [term]
maps: ["[[Programming]]", "[[Research]]"]
status: draft
updated: 2026-10-10
---
# Matplotlib

> [[Python]]で、論文などに用いる品質のグラフを作成するための、最も広く用いられている描画ライブラリである。

## 概要
Matplotlibは、2003年頃にJohn D. Hunterが作成した。脳波（EEG）のデータを解析するアプリケーションをMATLABで作っていたHunterが、Pythonで作り直す際に、MATLABの描画機能を手本として開発した。論文に使える品質のグラフ、TeXの文書のための出力、GUIへの組み込みなどを当初からの要件としていた。

Matplotlibの図は階層的な構造を持つ。Figureは図全体を表し、その中に、データを描く領域であるAxesを一つ以上置く。Axesは、目盛りやラベルを持つ軸（Axis）を持つ。描画の書き方は二通りある。`fig, ax = plt.subplots()` のようにFigureとAxesを明示的に作り、`ax.plot(...)` のようにそのメソッドを呼ぶオブジェクト指向の書き方は、複雑な図や再利用するスクリプトに向く。`plt.plot(...)` のように、pyplotに現在の図を暗黙に管理させる書き方は、対話的に手早く確かめるのに向く。描画する関数は、[[NumPy]]の配列、あるいはそれに変換できるデータを受け取る。

作成した図は `savefig()` で、PNG、PDF、SVGなどの形式で保存できる。[[TikZ|PGF]]の形式で出力すると、図の中の文字を[[LaTeX]]で組版させられ、論文の本文と同じフォントを図の中でも用いられる。

## どこで出てくるか
Matplotlibは、ベンチマークの結果や実験の測定値を、論文やスライドのグラフにする際に用いられる。pandasのDataFrameなども、NumPyの配列に変換して、あるいは `data` 引数で列の名前を指定して描画できる。図はスクリプトとして作成されるため、そのスクリプトを実験のデータとともに保存しておけば、データを更新したときに同じ図を作り直せる。

## 関係
- 上位概念: [[Python]]
- 使う / 使われる: [[NumPy]]（描画するデータ）, [[LaTeX]]（PGFでの出力）
- 関連: [[TikZ]], [[Beamer]], [[IOR]]

## 出典
- [Quick start guide - Matplotlib documentation](https://matplotlib.org/stable/users/explain/quick_start.html)
- [History - Matplotlib documentation](https://matplotlib.org/stable/project/history.html)
- [Text rendering with XeLaTeX/LuaLaTeX via the pgf backend - Matplotlib documentation](https://matplotlib.org/stable/users/explain/text/pgf.html)
