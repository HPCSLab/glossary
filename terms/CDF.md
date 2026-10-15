---
aliases: [CDF Plot, 累積分布関数, Cumulative Distribution Function, ECDF, Empirical CDF, 経験分布関数, CCDF, Complementary CDF, 相補累積分布関数]
tags: [term]
maps: ["[[Research]]"]
status: draft
updated: 2026-10-16
---
# CDF（累積分布関数）

> ある値xに対して、測定値がx以下となる確率（測定した標本ではその割合）を与える関数であり、論文ではレイテンシなどの測定値の分布全体を一本の曲線で示すグラフとして用いられる。

## 概要
CDF（cumulative distribution function）は F(x) = P(X ≤ x) で定義され、xが大きくなるにつれて0から1へ単調に増える。実験で得たn個の測定値から作るものは経験分布関数（ECDF）と呼ばれ、測定値を小さい順に並べ、i番目の値で高さが i/n となる階段状の曲線になる。平均値や棒グラフは分布を一つの数に縮めるため、ばらつきや外れ値が見えなくなる。ヒストグラムは分布の形を示すが、区間の幅の選び方で見え方が変わる。CDFは区間を選ぶ必要がなく、すべての測定値をそのまま一本の曲線に表せる。

![[CDF Reading.excalidraw]]

CDFは縦と横の二通りに読める。横に読むと、高さ0.5の位置が中央値、高さ0.99の位置が99パーセンタイル（p99）であり、任意のパーセンタイルを図から読み取れる。縦に読むと、ある時間の位置での高さが、その時間内に終わった要求の割合を表す。曲線が左にあるほど速く、立ち上がりが急なほど値がそろっている。右に長く伸びる部分は少数の遅い要求、すなわち[[Latency|テールレイテンシ]]である。二つのシステムの曲線が交差する場合は、中央値で速い方がp99では遅いというように、どちらが速いかが見る位置によって変わる。テールの違いを見たい場合は、1−F(x) を対数の縦軸で描く相補累積分布関数（CCDF）を用いると、p99やp99.9の差が見やすくなる。

## どこで出てくるか
システムの論文では、要求の[[Latency|レイテンシ]]、I/Oの完了時間、ジョブの実行時間、ファイルの大きさなどの分布を示すグラフとして多用される。多数のサーバに要求を分けて送る処理では、最も遅い一つの応答が全体の完了を決めるため、平均ではなく分布の裾を示すことが求められる。[[fio]]は完了までのレイテンシをパーセンタイルで報告し、[[Matplotlib]]は3.8から、測定値の配列からECDFを描く `Axes.ecdf` を提供する。`complementary=True` を指定するとCCDFを描く。

CDFを読むときには、横軸が線形か対数か、何個の測定値から作られたかに注意する。測定値が少ないと、p99やp99.9は数個の値だけで決まり、偶然の影響が大きい。

## 関係
- 使う / 使われる: [[Matplotlib]], [[fio]]
- 関連: [[Latency]]

## 出典
- [matplotlib.axes.Axes.ecdf - Matplotlib documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ecdf.html)
- [The Tail at Scale (Dean and Barroso, Communications of the ACM, 2013)](https://research.google/pubs/pub40801/)
