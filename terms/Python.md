---
aliases: [python, CPython, GIL, Global Interpreter Lock, グローバルインタプリタロック, Free Threading, mpi4py, venv, pip]
tags: [term]
maps: ["[[Programming]]"]
status: draft
updated: 2026-10-06
---
# Python

> 簡潔な文法と豊富なライブラリを特徴とする汎用の高水準プログラミング言語であり、科学技術計算、データ解析、機械学習、実験の自動化に広く用いられる。

## 概要
Pythonは、Guido van Rossumが開発し、1991年に最初の版が公開された。動的型付けのインタプリタ型言語であり、標準の実装はC言語で書かれたCPythonである。CPythonは、ソースコードをバイトコードに変換し、それを仮想機械で一命令ずつ解釈実行する。そのため、数値計算を素朴なループで書くと、[[C]]言語で書いた場合より桁違いに遅い。科学技術計算でPythonが広く使われているのは、重い計算をC、C++、Fortranなどで書かれたライブラリ（[[NumPy]]など）に任せ、Pythonはそれらを組み合わせる役割を担うことで、書きやすさと性能を両立できるためである。

CPythonには、グローバルインタプリタロック（GIL）と呼ばれる仕組みがある。GILは、一度に一つのスレッドしかPythonのバイトコードを実行できないようにするロックであり、インタプリタの実装を単純にする代わりに、スレッドによるCPUの並列利用を妨げる。ただし、I/Oの待ちの間や、多くの拡張モジュールが重い計算を行う間はGILが解放されるため、I/Oの並行処理や、NumPyなどの内部での計算は並列に進みうる。Pythonの処理そのものを複数のコアで並列に実行するには、従来は `multiprocessing` などで複数のプロセスを用いる必要があった。Python 3.13からは、GILを無効にしたフリースレッド版のビルドが提供されている。

## どこで出てくるか
研究室では、実験の制御と自動化、ベンチマーク結果の集計と可視化（pandas、matplotlib）、データの前処理などでPythonを日常的に用いる。HPCでは、mpi4pyによって[[MPI]]をPythonから利用でき、[[HDF5]]や[[netCDF]]、[[Zarr]]のデータもPythonから扱える。一方、性能が重要な部分をPythonの純粋なループで書くと、計算時間の大半がインタプリタの処理に費やされる。性能を評価する際には、時間がPythonの層で費やされているのか、ライブラリ内部の計算で費やされているのかを区別する必要がある。

環境の管理も実務上の要点である。プロジェクトごとに `venv` などで独立した環境を作り、使用したライブラリの版を記録しておくことで、実験の再現性を確保できる。スーパーコンピュータでは、ログインノードと計算ノードで環境が異なることや、多数のプロセスが同時にPythonを起動すると多数の小さなファイルの読み込みが[[Parallel File System|並列ファイルシステム]]の[[Metadata|メタデータ]]サーバに負荷をかけることにも注意を要する。

## 関係
- 使う / 使われる: [[NumPy]], [[C]]（CPythonの実装言語）, [[MPI]]（mpi4py）
- 関連: [[HDF5]], [[netCDF]], [[Zarr]], [[Parallel File System]]

## 出典
- [Glossary - Python documentation](https://docs.python.org/3/glossary.html)
- [Python support for free threading - Python documentation](https://docs.python.org/3/howto/free-threading-python.html)
