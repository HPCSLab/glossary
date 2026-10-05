---
aliases: [フレームグラフ, Flame Graphs, FlameGraph, flamegraph.pl, stackcollapse-perf.pl, Off-CPU Flame Graph, Differential Flame Graph]
tags: [term]
maps: ["[[Operating System]]"]
status: draft
updated: 2026-10-06
---
# Flame Graph（フレームグラフ）

> プロファイラで標本として集めた多数のコールスタックを、関数の呼び出しの階層と出現の頻度が一目で分かるように描く可視化の手法である。

## 概要
フレームグラフは、Brendan Greggが2011年に、MySQLの性能の問題を調べる際に考案した。プロファイラの出力は、数千の異なるコールスタックの羅列となり、そのままでは読み切れないことが多い。フレームグラフは、同じ経路のスタックをまとめ、どの関数の経路で時間が使われているかを一枚の図に示す。

図の各箱は、スタック上の一つの関数（フレーム）を表す。縦軸はスタックの深さであり、下から上へ、呼び出し元から呼び出し先に積み上がる。横軸は時間の経過ではなく、標本の集合を関数名のアルファベット順に並べたものである。箱の幅は、その関数がスタックに現れた標本の数に比例する。CPUの標本の場合、一番上の箱はその時点でCPU上で実行されていた関数であり、上端の幅が広い箱ほど、その関数自身が多くの時間を使っている。色は、隣り合う箱を区別するためのものであり、通常は意味を持たない。

## どこで出てくるか
フレームグラフは、[[perf]]で取得したスタックから作ることが多い。`perf record -F 99 -a -g` でスタックを標本として記録し、`perf script` で書き出した結果を `stackcollapse-perf.pl` で一行一スタックの形に畳み込み、`flamegraph.pl` でSVGの図を生成する。生成した図はブラウザで開き、箱をクリックしてその部分を拡大したり、関数名を検索してその割合を確かめたりできる。

CPUの時間のほか、メモリの割り当て、CPUを使わずに待っている時間（off-CPU）、二つのプロファイルの差（差分フレームグラフ）などを描く派生もある。off-CPUのフレームグラフは、[[System Call|システムコール]]でのI/Oの待ちなど、プロセスやスレッドがCPU上で実行されずに止まっている時間を調べるのに用いられる。

## 関係
- 使う / 使われる: [[perf]]（スタックの取得）
- 関連: [[BPF]], [[gperftools]], [[Systems Performance]]

## 出典
- [Flame Graphs - Brendan Gregg](https://www.brendangregg.com/flamegraphs.html)
- [brendangregg/FlameGraph - GitHub](https://github.com/brendangregg/FlameGraph)
- [Off-CPU Flame Graphs - Brendan Gregg](https://www.brendangregg.com/FlameGraphs/offcpuflamegraphs.html)
