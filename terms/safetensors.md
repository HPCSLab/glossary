---
aliases: [Safetensors, SafeTensors, .safetensors, model.safetensors, safe_open, pickle, Pickle]
tags: [term]
maps: ["[[Machine Learning Systems]]"]
status: draft
updated: 2026-10-09
---
# safetensors

> 機械学習のモデルの重みなどのテンソルを、安全に、かつ高速に読み込めるように保存するための、[[Hugging Face]]が開発したファイル形式とそのライブラリである。

## 概要
[[PyTorch]]は、既定ではPythonのpickleの仕組みでモデルを保存する。pickleのファイルは、読み込むと任意のコードが実行されうるため、インターネットから入手したファイルを読み込むことは安全ではない。safetensorsは、この問題をなくすために作られた。ファイルにはテンソルのデータとその説明だけが入り、コードは入らない。

ファイルの構造は単純である。先頭の8バイトに、続くヘッダの大きさNを、リトルエンディアンの符号なし64ビット整数で書く。続くNバイトがJSONのヘッダであり、テンソルの名前ごとに、データの型（例えば `F16`）、形（shape）、データの領域の中での開始と終了の位置（`data_offsets`）を記す。その後に、全てのテンソルのデータが隙間なく並ぶ。データは行優先（C順）で、ストライドを持たない形に詰めて保存される。悪意のあるファイルによるサービスの妨害を防ぐために、ヘッダの大きさは100MBまでに制限され、各テンソルの領域が重ならないことが保証される。

ヘッダを読めば、どのテンソルがファイルのどこにあるかが分かるため、ファイル全体を読まずに必要なテンソルだけを読み込める（遅延読み込み）。複数の[[GPU]]にモデルを分けて置く場合に、各GPUが担当する部分だけを読むのに役立つ。CPUでは、ファイルがすでに[[Page Cache|ページキャッシュ]]にあれば、データの複製なしに使える。GPUではホストからの転送が必ず必要になるが、全てのテンソルを一度にCPUのメモリに確保することは避けられる。

## どこで出てくるか
[[Hugging Face]]のHubで公開されているモデルの重みは、`model.safetensors` のようなsafetensorsの形式で置かれていることがあり、Transformersなどのライブラリで読み込まれる。Pythonからは、`safe_open` でファイルを開いて必要なテンソルを取り出し、`save_file` で保存する。

## 関係
- 使う / 使われる: [[PyTorch]], [[Hugging Face]], [[GPU]]
- 対比: [[ONNX]]（計算のグラフを含むモデルの形式）, [[HDF5]]（多次元配列の汎用の形式）
- 関連: [[Page Cache]], [[LLM]]

## 出典
- [huggingface/safetensors - GitHub](https://github.com/huggingface/safetensors)（Format、Yet another format?、Notes、Benefits）
- [Safetensors - Hugging Face documentation](https://huggingface.co/docs/safetensors/index)
