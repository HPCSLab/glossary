---
aliases: [numpy, ndarray, np, Broadcasting, ブロードキャスト, Vectorization, ベクトル化, Strides, ストライド]
tags: [term]
maps: ["[[Programming]]", "[[Scientific Data]]"]
status: draft
updated: 2026-10-10
---
# NumPy

> [[Python]]で科学技術計算を行うための基盤となるライブラリであり、多次元配列オブジェクトndarrayと、それに対する高速な演算を提供する。

## 概要
NumPyの中心は、多次元配列 `ndarray` である。Pythonのリストが任意の型の要素を個別のオブジェクトとして保持するのに対し、ndarrayは、同一の型（dtype）の要素を一続きのメモリ領域に格納し、大きさは作成時に固定される。配列に対する演算は、事前にコンパイルされたC言語のコードで実行されるため、Pythonでループを書く場合と比べて桁違いに高速である。

NumPyを効果的に使う鍵は、ベクトル化とブロードキャストである。ベクトル化とは、要素ごとのループを書かず、`c = a * b` のように配列全体に対する演算として記述することである。ブロードキャストは、形状の異なる配列の間の演算において、小さい方の配列を暗黙のうちに大きい方の形状に合わせて拡張する規則である。例えば、行列の各行から同じベクトルを引く操作を、ループなしで書ける。

ndarrayのメモリ配置は、ストライドによって表される。ストライドは、各次元の添字を一つ進めたときに、メモリ上で何バイト進むかを表す。NumPyの既定は、最後の次元が連続して並ぶ行優先（C順序）であり、[[C]]言語の配列と同じである。最初の次元が連続する列優先（Fortran順序）も選べる。スライスによる部分配列の取り出しは、データを複製せず、同じメモリ領域を異なるストライドで参照するビューを返す。そのため、ビューを変更すると元の配列も変わる。独立した配列が必要な場合は `.copy()` を用いる。

## どこで出てくるか
NumPyは、SciPy、pandas、[[Matplotlib|matplotlib]]、scikit-learn、[[HDF5]]を扱うh5py、[[Zarr]]など、Pythonの科学技術計算のほぼすべてのライブラリの基盤である。性能の面では、Pythonの要素ごとのループを避けてベクトル化すること、メモリ上で連続した方向にアクセスすること、意図しない配列の複製を避けることが要点となる。行優先の配列を列方向に走査すると、キャッシュの効率が悪く、[[Bandwidth|メモリバンド幅]]を有効に使えない。また、C言語やFortranで書かれたコードや、[[MPI]]などのライブラリにデータを渡す際には、メモリ配置の違い（C順序かFortran順序か、連続か否か）が正しさと性能の両方に影響する。

## 関係
- 上位概念: [[Python]]（NumPyはPythonのライブラリである）
- 使う / 使われる: [[C]]（演算の実装）, [[HDF5]], [[Zarr]]
- 関連: [[Bandwidth]], [[MPI]]

## 出典
- [What is NumPy? - NumPy Manual](https://numpy.org/doc/stable/user/whatisnumpy.html)
- [The N-dimensional array (ndarray) - NumPy Manual](https://numpy.org/doc/stable/reference/arrays.ndarray.html)
