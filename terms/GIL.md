---
aliases: [Global Interpreter Lock, グローバルインタプリタロック, Free Threading, Free-threaded Python, フリースレッド, PEP 703, PYTHON_GIL]
tags: [term]
maps: ["[[Programming]]"]
status: draft
updated: 2026-10-10
---
# GIL（グローバルインタプリタロック）

> [[Python]]の標準の実装であるCPythonが持つ、一度に一つの[[Thread|スレッド]]しかPythonのバイトコードを実行できないようにするインタプリタ全体のロックである。

## 概要
CPythonのオブジェクトは[[Reference Counting|参照カウント]]を持ち、`dict` などの組み込み型も内部の状態を持つ。これらを複数のスレッドが同時に更新すると、カウントが壊れてオブジェクトが誤って解放されるなどの不具合が起きる。GILは、インタプリタ全体を一つの[[Mutex|ロック]]で守ることで、オブジェクトごとの排他制御を不要にし、実装を単純にしている。その代わり、同じ[[Process|プロセス]]の中のスレッドは、複数のコアがあってもPythonのコードを並列に実行できない。スレッドは一定の時間ごとにGILを受け渡して交互に実行される。

ただし、GILは常に保持されているわけではない。I/Oを行う間は必ず解放され、圧縮やハッシュの計算のような重い処理を行う拡張モジュールの多くも、その間はGILを解放する。このため、I/Oの多い処理や、[[NumPy]]などのライブラリの内部で計算が進む処理では、スレッドでも並行・並列の効果が得られる。並列化が効かないのは、純粋なPythonのコードでCPUを使う処理である。

Python 3.13からは、PEP 703に基づき、GILを無効にしたフリースレッド版のビルドが提供されている。これは参照カウントの方式の変更や、リストや辞書へのオブジェクトごとのロックの導入によって、GILなしでの安全性を確保する。3.14ではPEP 779によって公式にサポートされたが、既定のビルドではない。単一スレッドの性能はやや低下し、フリースレッドに対応していない拡張モジュールを読み込むと、GILが自動的に再び有効になる。

## どこで出てくるか
Pythonの処理をスレッドで並列化しても速くならないとき、まず疑うのがGILである。CPUを使う処理を複数のコアで並列に実行するには、`multiprocessing` などで複数のプロセスを用いるのが従来の定石であるが、プロセスの起動とデータの受け渡しのシリアライズに負担がかかる。[[MPI]]をmpi4pyで用いる場合も、並列化の単位はプロセスである。[[PyTorch]]などの機械学習の処理でも、[[GPU]]への計算の投入や前処理はPythonで行われるため、GILが性能の議論に現れる。フリースレッド版で動いているかどうかは、`sys._is_gil_enabled()` で確かめられる。

## 関係
- 上位概念: [[Mutex]]
- 前提: [[Thread]], [[Reference Counting]]
- 対比: [[Process]]（`multiprocessing` はプロセスごとに別のインタプリタを持つため、GILを共有しない）
- 関連: [[Python]], [[NumPy]], [[PyTorch]]

## 出典
- [Glossary: global interpreter lock - Python documentation](https://docs.python.org/3/glossary.html)
- [Python support for free threading - Python documentation](https://docs.python.org/3/howto/free-threading-python.html)
- [sys - System-specific parameters and functions - Python documentation](https://docs.python.org/3/library/sys.html)
- [PEP 703 – Making the Global Interpreter Lock Optional in CPython](https://peps.python.org/pep-0703/)
- [PEP 779 – Criteria for supported status for free-threaded Python](https://peps.python.org/pep-0779/)
